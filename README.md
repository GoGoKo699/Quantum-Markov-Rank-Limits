# Quantum Markov Rank Limits

**Does full rank of every finite reduced density matrix protect the quantum Markov length against weak local noise?** This project gives an explicit negative answer. A one-dimensional gapped fermionic ground state has faithful reductions on every finite region and exponentially decaying conditional mutual information (CMI), yet an arbitrarily weak, depth-two circuit of unital nearest-neighbor channels produces algebraic CMI and infinite Markov length. Every finite output reduction remains faithful.

The construction also has an ordinary-spin realization with four qubits per fine site. Its input is globally mixed because of maximally mixed auxiliary modes. The same local-faithfulness and Markov-length conclusions hold for this spin state.

## Principal result

Fix the SSH parameter $`m>1`$ and a noise angle $`0<\epsilon<\pi/2`$. Each physical fine site has two fermionic orbitals; a coarse cell contains two fine sites. Let five consecutive coarse blocks be ordered $`C_-B_-AB_+C_+`$, each of length $`L`$. Write

```math

\kappa_\epsilon=
\frac{\zeta(3)\sin^2\epsilon}{8(1+\cos^2\epsilon)}.
```

For both the fermionic output and its spin realization,

```math

I(A:C_-\cup C_+\mid B_-\cup B_+)
=\frac{643\,\kappa_\epsilon}{450L^2}+o(L^{-2}).
```

The shielding width grows with $`L`$, so this positive algebraic tail is incompatible with an exponential bound having any fixed polynomial region-size prefactor. The initial state satisfies an exponential shielding bound. Each noise gate is at most $`8\epsilon^2`$ from the identity in the local diamond norm.

| Question | Established answer | Authoritative account |
|---|---|---|
| Are all finite input and output reductions full rank? | Yes, for every fixed allowed parameter choice. No region-independent spectral margin is assumed. | [Model and rank proof](science/model-and-rank.md) |
| Is the physical noise strictly local and weak? | Two nearest-neighbor layers, unital gates, and an explicit local norm bound. | [Model and rank proof](science/model-and-rank.md) |
| Does the output violate the fully shielded Markov-length condition? | Yes; the exact five-block coefficient is shown above. | [Instability theorem](science/instability-theorem.md) |
| Does the result extend to ordinary spins? | Yes, with four qubits per fine site and a globally mixed input. | [Spin realization](science/spin-realization.md) |
| Is there a continuous-time counterpart? | Yes, for a specified balanced local gain-and-loss generator. | [Continuous-time companion](science/continuous-time.md) |

All entropies are in nats. The thermodynamic limit is taken before the large-region limit, with $`m`$ and the nonzero noise strength fixed.

## Why the construction works

The input is an exponentially local unitary dressing of a product band state. Its occupied and empty bands contain no nonzero compactly supported vector, which rules out occupation eigenvalues exactly zero or one in every finite region. Truncated exponentially localized band vectors nevertheless approach these endpoints as the region grows.

The noise acts identically on the two orbital flavors, so its covariance evolution commutes with the dressing. This exact compatibility keeps the physical noise at finite depth while connecting its output to the solvable noisy reference of Newsom and Levin. A local-circuit CMI comparison transfers the reference's macroscopic algebraic coefficient through the dressing. A separate entropy identity and exponentially small ordinary mutual information establish the fully shielded result.

The scalar noise model and entropy asymptotic are inherited from [Newsom–Levin](references/README.md#nl). The auxiliary spin embedding follows [Negari–Zou–Hsieh](references/README.md#nzh). The added consequence is the instability with **every finite marginal faithful**, together with the compatible finite-range gapped input, strict physical noise locality, and the quantitative CMI transfer. The [related-work account](references/README.md) identifies these dependencies and the limits of the comparison.

## Reading routes

Start with the [scientific overview](science/README.md) for definitions and proof dependencies. For the physical interpretation, read [what local faithfulness does and does not control](science/interpretation.md). For the precise result, follow [model](science/model-and-rank.md) → [locality and CMI](science/locality-and-cmi.md) → [instability theorem](science/instability-theorem.md).

The [numerical data guide](data/README.md) explains the finite-size evidence and its normalization. The [verification guide](verification/README.md) gives commands and separates numerical corroboration from analytical proof. [llms.txt](llms.txt) maps scientific questions to their authoritative files.

## Learning route

The single educational anchor is **Mark M. Wilde, *Quantum Information Theory*, second edition (2017)**. The [learning guide](learning/README.md) connects its treatment of channels, entropy, conditional mutual information, and recoverability to this construction.

Begin with the [source-to-project bridge](learning/bridge.md), which develops the distinction between full rank and a uniform spectral margin through small examples, then explains the compatible dressing and the CMI argument. The [30-milestone map](learning/milestones.md) provides the complete understanding route: 14 background milestones connect finite quantum systems to spatial conditional independence, and 16 project milestones assemble the construction, theorem, realizations, and scope.

## Reproduce the calculations

The archived calculations used Python 3.12.14, NumPy 2.3.5, and SciPy 1.17.0. From the repository root:

```bash
python -m pip install -r verification/requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/reproduce.py --checks-only
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python code/reproduce.py --output /tmp/quantum-markov-rank-results.json
```

The quick command checks independent covariance formulas, unitality, limiting cases, and Fourier conventions. The full command regenerates the entropy rows in [data/results.json](data/results.json). Finite-size calculations support the theorem; they cannot establish strict local faithfulness or the infinite-distance asymptotic by themselves.

## Scope

The noise retains a tuned dark momentum mode. No generic-noise or finite-temperature Gibbs-state instability is claimed. The pure gapped input belongs to the fermionic construction; the spin input has tracial auxiliaries and an extensively degenerate ground-space interpretation. Faithfulness is a statement about each finite region of an infinite-chain state, not a uniform lower bound on its spectrum. The coefficient is independent of fixed $`m`$, while approximation constants and crossover lengths may depend on it.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
