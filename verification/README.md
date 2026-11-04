# Verification and reproduction

The result is analytical. Computation checks the concrete covariance conventions and provides finite-size corroboration of the derived asymptotics. The local-rank and locality proofs remain necessary even if all numerical checks pass.

## Environment and commands

The archived calculations used Python 3.12.14, NumPy 2.3.5, and SciPy 1.17.0. Pinned numerical dependencies are in [requirements.txt](requirements.txt). From the repository root:

```bash
python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/reproduce.py --checks-only
```

The command prints the maximum errors and raises an exception if any quick-check residual exceeds $10^{-12}$. It does not modify files or run the dense entropy sweep. The checks include:

- Projector idempotence and the zero-noise and zero-time input limits.
- Agreement of the direct two-layer affine map with the dressed covariance decomposition and with the independent Newsom–Levin formula.
- Unitality of both layers and occupation eigenvalues in the physical interval up to roundoff.
- The dark occupation endpoints and the explicit balanced gain-and-loss spectrum.
- The parity-swap and real-space orbital-swap identities relating the historical and current Fourier conventions.

The refreshed quick residuals are below $4\times10^{-16}$ in the recorded environment. These are floating-point consistency checks, not proofs of exact identities.

To regenerate all finite-size rows without overwriting the archived data:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/reproduce.py --output /tmp/quantum-markov-rank-results.json
```

The Fourier grid contains 32,768 points. The largest dense matrices are $1152\times1152$ for finite-depth noise and $768\times768$ for continuous time. The output records parameters, numerical-library versions, covariance checks, interval CMI, and the analytical scaled limits. The [data guide](../data/README.md) gives representative values and the provenance of the completed sweep. Reproduced values may differ in their last digits across platforms.

## What the data measure

The entropy routine restricts the infinite-chain covariance to a finite contiguous interval. For equal interval length $n$, it computes

$$
I_n=2S(2n)-S(n)-S(3n).
$$

For finite-depth noise, $n$ counts four-mode coarse cells, and

$$
\lim_{n\to\infty}n^2 I_n
=\frac{11\zeta(3)\sin^2\epsilon}{144(1+\cos^2\epsilon)}.
$$

For the continuous-time normalization in the companion note, $n$ counts two-mode cells and the limit is $11t\zeta(3)/36$. The archived points are consistent with these limits. They do not evaluate disconnected spin marginals or numerically establish the fully shielded coefficient; that result follows from the entropy identities and locality arguments in the science notes.

## Analytical checks that computation cannot replace

| Issue | Required argument |
|---|---|
| Strict positivity of every finite density matrix | The compact-band-vector contradiction in [model-and-rank.md](../science/model-and-rank.md). Rounding tiny occupations to zero or one cannot decide rank. |
| Initial exponential CMI | The explicit shielding decomposition in [locality-and-cmi.md](../science/locality-and-cmi.md). Covariance clustering alone is insufficient. |
| The large-region algebraic coefficient | The inherited interval theorem and the forward/inverse CMI squeeze in [instability-theorem.md](../science/instability-theorem.md). |
| Strict physical gate locality and weakness | The even finite-dimensional dilation and norm estimate in the model note. |
| The spin result | The parity-aware auxiliary lift and spin-only disconnected-region argument in [spin-realization.md](../science/spin-realization.md). |
| Lindblad factors of two | The explicit generator and conversion to the source convention in [continuous-time.md](../science/continuous-time.md). |

The numerical entropy clips occupation excursions smaller than $10^{-11}$ to the physical interval and rejects larger violations. At zero noise, large-buffer CMI reaches subtraction roundoff; tiny negative values in the archived data are retained as numerical diagnostics. All analytical asymptotics use fixed nonzero noise strength before the large-region limit.
