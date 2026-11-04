#!/usr/bin/env python3
"""Reproduce the covariance checks and finite-size Gaussian entropy data.

Dependencies: numpy and scipy. Run with OPENBLAS_NUM_THREADS=1 for predictable
dense eigensolver performance. All entropies are in natural-log units.
The numerical data corroborate, but do not replace, the analytic proofs.
"""

import argparse
import json
import platform
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import eigvalsh
from scipy.special import zeta


ROOT = Path(__file__).resolve().parents[1]
GRID = 32768
MASS = 2.0
FINITE_DEPTH_SIZES = [8, 16, 32, 64, 96]
BALANCED_SIZES = [8, 16, 32, 64, 96, 128]


def adjoint(a):
    return a.conj().swapaxes(-1, -2)


def ssh_projector(k, m=MASS):
    """Occupied-band projector, with off-diagonal phase m+exp(ik)."""
    z = m + np.exp(1j * k)
    p = np.zeros((len(k), 2, 2), dtype=complex)
    p[:, 0, 0] = p[:, 1, 1] = 0.5
    p[:, 0, 1] = -0.5 * z / np.abs(z)
    p[:, 1, 0] = p[:, 0, 1].conj()
    return p


def batch_kron(a, b):
    n = len(a)
    return np.einsum("kab,kcd->kacbd", a, b).reshape(n, 4, 4)


def finite_depth_symbol(k, epsilon, m=MASS):
    """Apply both affine layers directly and check the exact decomposition.

    Tensor order: NL even/odd subcell, then SSH orbital. Each coarse cell
    contains four physical fermion modes. NL refers to arXiv:2610.12929v3.
    """
    p = ssh_projector(k, m)
    identity = np.broadcast_to(np.eye(2), p.shape)
    c = np.cos(epsilon / 2) ** 2
    s = np.sin(epsilon / 2) ** 2
    x0 = np.array([[c, -s], [-s, c]], dtype=complex)
    x1 = np.zeros_like(p)
    x1[:, 0, 0] = x1[:, 1, 1] = c
    x1[:, 0, 1] = -s * np.exp(-1j * k)
    x1[:, 1, 0] = x1[:, 0, 1].conj()
    matrix = x1 @ x0
    cnl = (identity - matrix @ adjoint(matrix)) / 2

    # NL equations (9)--(11), transposed to the model's Fourier convention.
    a = 0.5 * np.sin(epsilon) ** 2 - 0.25 * np.sin(epsilon) ** 4 * np.cos(k / 2) ** 2
    b = 0.25 * np.sin(epsilon) ** 2 * (1 + np.exp(-1j * k)) * (c * c + s * s * np.exp(-1j * k))
    nl_formula = np.zeros_like(cnl)
    nl_formula[:, 0, 0] = nl_formula[:, 1, 1] = a
    nl_formula[:, 0, 1] = b
    nl_formula[:, 1, 0] = b.conj()

    initial = batch_kron(identity, p)
    a0 = batch_kron(np.broadcast_to(x0, p.shape), identity)
    a1 = batch_kron(x1, identity)
    y0 = (np.eye(4)[None] - a0 @ adjoint(a0)) / 2
    y1 = (np.eye(4)[None] - a1 @ adjoint(a1)) / 2
    first = a0 @ initial @ adjoint(a0) + y0
    direct = a1 @ first @ adjoint(a1) + y1
    decomposed = batch_kron(cnl, identity - p) + batch_kron(identity - cnl, p)
    checks = {
        "NL_vacuum_formula_max_error": float(np.max(np.abs(cnl - nl_formula))),
        "two_layer_dressing_max_error": float(np.max(np.abs(direct - decomposed))),
        "layer_0_unital_max_error": float(np.max(np.abs(0.5 * a0 @ adjoint(a0) + y0 - 0.5 * np.eye(4)))),
        "layer_1_unital_max_error": float(np.max(np.abs(0.5 * a1 @ adjoint(a1) + y1 - 0.5 * np.eye(4)))),
    }
    return direct, checks


def balanced_symbol(k, t, m=MASS):
    """Two-mode-cell, continuous-time balanced (unital) noise convention."""
    damping = np.exp(-t * (2 - 2 * np.cos(k)))
    return 0.5 * np.eye(2)[None] + damping[:, None, None] * (ssh_projector(k, m) - 0.5 * np.eye(2)[None])


def entropy(blocks, n):
    """Entropy of the infinite-chain covariance restricted to n cells."""
    q = blocks.shape[1]
    indices = np.arange(n)
    matrix = blocks[(indices[:, None] - indices[None, :]) % len(blocks)]
    matrix = matrix.transpose(0, 2, 1, 3).reshape(q * n, q * n)
    eigenvalues = eigvalsh(matrix, check_finite=False)
    if eigenvalues.min() < -1e-11 or eigenvalues.max() > 1 + 1e-11:
        raise ValueError("Covariance spectrum outside [0,1] beyond roundoff tolerance")
    eigenvalues = np.clip(eigenvalues, 0.0, 1.0)
    x = eigenvalues[(eigenvalues > 0) & (eigenvalues < 1)]
    return float(np.sum(-x * np.log(x) - (1 - x) * np.log1p(-x)))


def equal_interval_cmis(symbol, sizes):
    # C_ij=<c_j^dagger c_i>, c(k)=sum_j exp(-ikj)c_j:
    # C_(i-j) is the inverse Fourier transform of the symbol.
    blocks = np.fft.ifft(symbol, axis=0)
    entropies = {n: entropy(blocks, n) for n in sorted({j * n for n in sizes for j in (1, 2, 3)})}
    return [(n, 2 * entropies[2 * n] - entropies[n] - entropies[3 * n]) for n in sizes]


def fast_checks():
    """Only identities and limiting cases; no large entropy sweep."""
    k = 2 * np.pi * np.arange(257) / 257
    projector = ssh_projector(k)
    out = {"ssh_projector_error": float(np.max(np.abs(projector @ projector - projector)))}
    zero, _ = finite_depth_symbol(k, 0.0)
    initial = batch_kron(np.broadcast_to(np.eye(2), projector.shape), projector)
    out["zero_gate_input_error"] = float(np.max(np.abs(zero - initial)))
    out["zero_time_input_error"] = float(np.max(np.abs(balanced_symbol(k, 0.0) - projector)))
    # Historical +ik layer convention differs by an onsite parity swap.
    epsilon = 0.4
    c, s = np.cos(epsilon / 2) ** 2, np.sin(epsilon / 2) ** 2
    x0 = np.array([[c, -s], [-s, c]], dtype=complex)
    x1_old = np.broadcast_to(x0, projector.shape).copy()
    x1_old[:, 0, 1] = -s * np.exp(1j * k)
    x1_old[:, 1, 0] = x1_old[:, 0, 1].conj()
    old_m = x1_old @ x0
    identity = np.broadcast_to(np.eye(2), projector.shape)
    old_nl = (identity - old_m @ adjoint(old_m)) / 2
    old_covariance = batch_kron(old_nl, identity - projector) + batch_kron(identity - old_nl, projector)
    swap = np.kron(np.array([[0, 1], [1, 0]]), np.eye(2))
    new_covariance, _ = finite_depth_symbol(k, epsilon)
    out["historical_parity_swap_error"] = float(np.max(np.abs(new_covariance - swap @ old_covariance @ swap)))
    orbital_swap = np.kron(np.eye(2), np.array([[0, 1], [1, 0]]))
    old_blocks = np.fft.fft(old_covariance, axis=0) / len(k)
    new_blocks = np.fft.ifft(new_covariance, axis=0)
    out["historical_real_space_orbital_swap_error"] = float(np.max(np.abs(new_blocks - orbital_swap @ old_blocks @ orbital_swap)))
    for epsilon in (0.2, 0.4, 0.8):
        covariance, checks = finite_depth_symbol(k, epsilon)
        out[f"finite_depth_{epsilon}_max_identity_error"] = max(checks.values())
        values = np.linalg.eigvalsh(covariance)
        out[f"finite_depth_{epsilon}_spectral_violation"] = float(max(0.0, -values.min(), values.max() - 1.0))
        dark = np.linalg.eigvalsh(covariance[0])
        out[f"finite_depth_{epsilon}_dark_band_error"] = float(max(abs(dark[0]), abs(dark[-1] - 1.0)))
    for t in (0.02, 0.1, 0.4):
        covariance = balanced_symbol(k, t)
        values = np.linalg.eigvalsh(covariance)
        q = -0.5 * np.expm1(-t * (2 - 2 * np.cos(k)))
        target = np.stack((q, 1 - q), axis=1)
        out[f"balanced_{t}_occupation_error"] = float(np.max(np.abs(values - target)))
    if max(out.values()) > 1e-12:
        raise AssertionError(out)
    return out


def reproduce():
    k = 2 * np.pi * np.arange(GRID) / GRID
    result = {
        "format_version": 1,
        "description": "Finite-size corroboration and exact covariance-identity checks; entropies in nats.",
        "parameters": {"m": MASS, "fourier_grid": GRID, "finite_depth_sizes": FINITE_DEPTH_SIZES, "balanced_sizes": BALANCED_SIZES},
        "conventions": {"covariance": "C_ij=<c_j^dagger c_i>", "fourier_modes": "c(k)=sum_j exp(-ikj)c_j", "inverse_transform": "IFFT", "odd_layer_01_phase": "exp(-ik)"},
        "software": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "fast_checks": fast_checks(),
        "finite_depth": [],
        "balanced_lindblad": [],
    }
    for epsilon in (0.2, 0.4, 0.8):
        covariance, checks = finite_depth_symbol(k, epsilon)
        gamma = 0.125 * np.sin(epsilon) ** 2 / (1 + np.cos(epsilon) ** 2)
        rows = [{"n": n, "cmi": cmi, "n2_cmi": n * n * cmi} for n, cmi in equal_interval_cmis(covariance, FINITE_DEPTH_SIZES)]
        result["finite_depth"].append({"m": MASS, "epsilon": epsilon, "checks": checks, "undressed_n2_limit": float(11 * gamma * zeta(3, 1) / 18), "rows": rows})
    for t in (0.0, 0.02, 0.1, 0.4):
        covariance = balanced_symbol(k, t)
        for n, cmi in equal_interval_cmis(covariance, BALANCED_SIZES):
            result["balanced_lindblad"].append({"m": MASS, "t": t, "n": n, "cmi": cmi, "scaled_n2": n * n * cmi, "predicted_scaled_limit": float(11 * t * zeta(3, 1) / 36)})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checks-only", action="store_true", help="run fast identities and limiting cases without writing data")
    parser.add_argument("--output", type=Path, default=ROOT / "data" / "results.json")
    args = parser.parse_args()
    if args.checks_only:
        print(json.dumps(fast_checks(), indent=2))
        return
    result = reproduce()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Saved {len(result['finite_depth'])} finite-depth cases and {len(result['balanced_lindblad'])} balanced rows to {args.output}")


if __name__ == "__main__":
    main()
