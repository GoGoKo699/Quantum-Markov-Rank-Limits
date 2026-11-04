# Sources and related results

This project studies whether full rank of every finite reduced density matrix is sufficient to stabilize finite Markov length under weak local noise. The scalar instability mechanism is established prior work. The construction here preserves that mechanism while removing every exact local rank deficiency and retaining strictly local, fixed-depth noise.

## Comparison at the level of assumptions

| Source | Established ingredient or setting | Relation to this project |
|---|---|---|
| [NL](#nl) | Weak two-layer unital Gaussian noise produces algebraic CMI from a product state; the extension uses at least one rank-deficient finite reduction | Supplies the circuit and scalar entropy asymptotic. The present correlated input has every finite reduction full rank, addressing the possibility left open in its Discussion |
| [NZH](#nzh) | Infinitesimal local Lindbladian instability, rapidly relaxing steady-state examples, and an auxiliary-fermion spin construction | Supplies a related instability and the auxiliary lifting method. Here the central channel has fixed finite depth and the input is locally faithful |
| [Yi et al.](#yi) | Decay properties of MI and CMI under almost-local evolution and local reversibility | Supplies locality and fermionic entropy machinery. Exponential initial decay here uses the explicitly exponential tail of the dressing, not the general superpolynomial headline theorem |
| [Chen–Grover](#cg) | Detailed-balance-breaking perturbations of Langevin steady states and cutoff-suppressed CMI tails | Addresses a related issue for phase diagnostics in a different dynamical setting; it does not supply this finite-depth construction |
| [Zhang–Gopalakrishnan](#zg) | Stability results for specified classical and commuting-Hamiltonian Gibbs states under local decoherence | Uses different input and channel hypotheses. The zero-temperature construction here does not settle general finite-temperature Gibbs stability |
| [Product-input stability](#product-stability) | Faithful bounded-depth channels acting on uniformly full-rank product inputs | Product structure is essential to that argument. Local faithfulness of a correlated ground state does not satisfy its input hypothesis |

The literature comparison concerns these inspected operational models and theorem statements. It is not an exhaustive priority claim. In particular, no claim is made here to the first weak-noise instability, first algebraic CMI example, first auxiliary-fermion lift, or first locality-based CMI bound.

<a id="newsom-levin2026"></a>

## NL

David C. Newsom and Michael Levin, **An Instability of the Quantum Markov Length**, [arXiv:2610.12929v3](https://arxiv.org/html/2610.12929v3), 29 October 2026.

The model uses its Eqs. (4)–(6). The scalar vacuum covariance and quadratic occupation-band edge are in Eqs. (9)–(13). Equation (15), with the rigorous derivation culminating in Appendix E.1, Eq. (132), supplies the interval-entropy correction. Appendix G gives alternative channel representations; Appendix H, especially Eqs. (169) and (174), supplies the scalar Lindblad companion and its entropy coefficient. Its Discussion explicitly identifies initial states with all finite reductions full rank as an unresolved possibility.

Our contributions are the covariance-compatible orbital dressing, the no-compact-band-vector proof of local faithfulness, and the resulting instability theorem with that input. The scalar dark-mode mechanism and $\zeta(3)$ coefficient are attributed to NL.

## NZH

Amir-Reza Negari, Yijian Zou and Timothy H. Hsieh, **Instability of Markov chains under infinitesimal coherent dissipation**, [arXiv:2610.18983v1](https://arxiv.org/html/2610.18983v1), 13 October 2026.

The local Lindblad and steady-state examples provide close comparisons. Supplemental Section SIII gives the auxiliary-Majorana construction and the contiguous-interval entropy identity. The [spin realization](../science/spin-realization.md) adapts that algebraic lift to the finite-depth random-unitary factors. It treats disconnected regions separately instead of assuming a Jordan–Wigner entropy identity for them.

<a id="yi2026"></a>

## Yi

Jinmin Yi, Kangle Li, Chuan Liu, Zixuan Li and Liujun Zou, **Universal decay of mutual information and conditional mutual information in gapped pure- and mixed-state quantum matter**, *Physical Review Letters* **136**, 116604 (2026), [doi:10.1103/mqp8-y1m7](https://doi.org/10.1103/mqp8-y1m7), [arXiv:2510.22867v3](https://arxiv.org/html/2510.22867v3), revised 19 March 2026.

Supplemental Theorem III.1 and Eqs. (III.4)–(III.11) express locality-decomposition errors in terms of interaction tails. The model's exponentially decaying generator permits exponential estimates from those expressions. Supplemental Section VIII addresses the entropy inequalities needed in fermionic systems. The unitary endpoint-enlargement proof used here is presented explicitly in [Locality and CMI](../science/locality-and-cmi.md).

## CG

Yu-Hsueh Chen and Tarun Grover, **Markov length can diverge in systems whose universal physics is spatially Markovian**, [arXiv:2610.11235v1](https://arxiv.org/html/2610.11235v1), 8 October 2026.

Their central operation changes the steady state of a perturbed stochastic dynamics. The critical and conserved examples clarify why a CMI tail and a phase transition are different questions. That steady-state limit is distinct from applying the fixed-depth circuit studied here to a given gapped input.

## ZG

Yifan F. Zhang and Sarang Gopalakrishnan, **Stability of mixed-state phases under weak decoherence**, [arXiv:2511.01976v1](https://arxiv.org/abs/2511.01976v1), 2025.

Yifan Zhang and Sarang Gopalakrishnan, **Conditional Mutual Information and Information-Theoretic Phases of Decohered Gibbs States**, [arXiv:2502.13210v1](https://arxiv.org/abs/2502.13210v1), 2025.

These give positive stability results under their specified classical, commuting or commuting-Pauli hypotheses and channel conditions. They should not be paraphrased as an unrestricted theorem for correlated quantum inputs.

## Product stability

**Quantum-Markov-Stability**, [scientific account at the inspected revision](https://github.com/GoGoKo699/Quantum-Markov-Stability/tree/9f9feca6f987e11de5e339f9fb806dbfc64b381a).

Its contraction argument concerns independent full-rank input factors and uniformly faithful bounded-depth local channels. The present input is correlated and globally pure, although every finite marginal is faithful. The results are therefore compatible and separate product structure from qualitative local rank.

## Continuity

<a id="winter2016"></a>

Andreas Winter, **Tight uniform continuity bounds for quantum entropies: conditional entropy, relative entropy distance and energy constraints**, *Communications in Mathematical Physics* **347**, 291–313 (2016), [doi:10.1007/s00220-016-2609-8](https://doi.org/10.1007/s00220-016-2609-8), [arXiv:1507.07775v6](https://arxiv.org/abs/1507.07775v6).

The conditional-entropy continuity bound controls the CMI error introduced by a local approximation to the dressing. The dimension entering the bound is an endpoint dimension.

<a id="audenaert2007"></a>

Koenraad M. R. Audenaert, **A sharp continuity estimate for the von Neumann entropy**, *Journal of Physics A: Mathematical and Theoretical* **40**(28), 8127–8136 (2007), [doi:10.1088/1751-8113/40/28/S18](https://doi.org/10.1088/1751-8113/40/28/S18), [arXiv:quant-ph/0610146v1](https://arxiv.org/abs/quant-ph/0610146v1). The preprint title is **A Sharp Fannes-type Inequality for the von Neumann Entropy**.

The sharp entropy-continuity inequality is applied to a normalized one-particle matrix embedding in the Gaussian mutual-information estimate. This controls the entropy error from exponentially small off-diagonal covariance blocks without assuming a uniform occupation gap.

## Local dynamics

Bruno Nachtergaele and Robert Sims, **Lieb–Robinson Bounds and the Exponential Clustering Theorem**, *Communications in Mathematical Physics* **265**, 119–130 (2006), [doi:10.1007/s00220-006-1556-1](https://doi.org/10.1007/s00220-006-1556-1), [arXiv:math-ph/0506030v3](https://arxiv.org/abs/math-ph/0506030v3). This gives the locality and clustering framework cited in the spin construction; the explicit interval-interaction norm needed here is specified in the locality note.

<a id="nachtergaele-ogata-sims2006"></a>

Bruno Nachtergaele, Yoshiko Ogata and Robert Sims, **Propagation of Correlations in Quantum Lattice Systems**, *Journal of Statistical Physics* **124**(1), 1–13 (2006), [doi:10.1007/s10955-006-9143-6](https://doi.org/10.1007/s10955-006-9143-6), [arXiv:math-ph/0603064v1](https://arxiv.org/abs/math-ph/0603064v1).

Theorems 2.1 and 2.2 give weighted-interaction Lieb–Robinson estimates and the existence of infinite-volume dynamics. The [locality note](../science/locality-and-cmi.md) specifies the exponentially decaying interaction norm and its use for the even-fermion dressing.

<a id="osborne2006"></a>

Tobias J. Osborne, **Efficient Approximation of the Dynamics of One-Dimensional Quantum Spin Systems**, *Physical Review Letters* **97**, 157202 (2006), [doi:10.1103/PhysRevLett.97.157202](https://doi.org/10.1103/PhysRevLett.97.157202), [arXiv:quant-ph/0508031v2](https://arxiv.org/abs/quant-ph/0508031v2). The preprint title is **The Dynamics of 1D Quantum Spin Systems Can Be Approximated Efficiently**.

Jeongwan Haah, Matthew B. Hastings, Robin Kothari and Guang Hao Low, **Quantum algorithm for simulating real time evolution of lattice Hamiltonians**, [arXiv:1801.03922v4](https://arxiv.org/abs/1801.03922v4), [doi:10.1137/18M1231511](https://doi.org/10.1137/18M1231511).

Osborne and Haah et al. are sources for boundary patching and locality-based decompositions. The exponential-interaction specialization used here is stated and justified in the locality note; it is not attributed to a nearest-neighbor theorem without the necessary extension.

## Gaussian reductions

<a id="peschel2003"></a>

Ingo Peschel, **Calculation of reduced density matrices from correlation functions**, *Journal of Physics A: Mathematical and General* **36**(14), L205–L208 (2003), [doi:10.1088/0305-4470/36/14/101](https://doi.org/10.1088/0305-4470/36/14/101), [arXiv:cond-mat/0212631v1](https://arxiv.org/abs/cond-mat/0212631v1).

Ingo Peschel and Viktor Eisler, **Reduced density matrices and entanglement entropy in free lattice models**, *Journal of Physics A: Mathematical and Theoretical* **42**, 504003 (2009), [doi:10.1088/1751-8113/42/50/504003](https://doi.org/10.1088/1751-8113/42/50/504003), [arXiv:0906.1663](https://arxiv.org/abs/0906.1663).

Ferenc Iglói and Ingo Peschel, **On reduced density matrices for disjoint subsystems**, *EPL* **89**, 40001 (2010), [doi:10.1209/0295-5075/89/40001](https://doi.org/10.1209/0295-5075/89/40001), [arXiv:0910.5671](https://arxiv.org/abs/0910.5671).

Peschel (2003) derives reduced density matrices from correlation functions; Peschel and Eisler review covariance-based reduced states and entropy calculations. Iglói and Peschel explain why disconnected spin and fermion reductions generally differ, a distinction preserved in the spin proof.

Machine-readable references are in [references.bib](references.bib).
