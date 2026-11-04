# Scientific account

The question is whether qualitative local faithfulness closes the weak-noise instability of quantum Markov length. Here **local faithfulness** means that the reduced density operator on every finite region is strictly positive. **Finite Markov length** means exponential decay of conditional mutual information across a shielding region, allowing a fixed polynomial prefactor in the region sizes. These conditions describe different aspects of a state.

The construction separates them in a controlled one-dimensional setting. The input is a pure Gaussian ground state of a finite-range gapped Hamiltonian, with full-rank finite reductions and finite Markov length. Two layers of arbitrarily weak unital nearest-neighbor noise give an output that still has full-rank finite reductions but has infinite Markov length. An auxiliary construction makes the same distinction for ordinary spins with a globally mixed input.

## Main route

1. **[Model and local-rank proof](model-and-rank.md).** Define the fine lattice, coarse cells, covariance convention, range-two SSH Hamiltonian, even ancilla dilation, and exact affine noise map. Prove local faithfulness by excluding compactly supported band vectors. Derive the compatible exponentially local dressing and the local diamond-norm bound.
2. **[Locality and CMI](locality-and-cmi.md).** Justify entropy inequalities for even fermionic restrictions; establish the initial exponential shielding bound; construct local circuit approximations uniformly over correlated inputs; and prove the two-sided CMI comparison that preserves the leading macroscopic coefficient.
3. **[Instability theorem](instability-theorem.md).** Import the precise scalar interval-entropy theorem, track all normalization factors, and prove both the one-sided and fully shielded CMI asymptotics. The fully shielded conclusion uses an exact entropy identity, not monotonicity in the conditioning region.
4. **[Interpretation](interpretation.md).** Explain why local full rank can coexist with near-pure modes, what a uniform occupation margin would add, and which stability questions remain outside the theorem.

These pages form one connected account. The model and locality notes are the authoritative homes of their proofs; the central theorem identifies the dependencies used to obtain the result.

## Two related realizations

- **[Ordinary spins](spin-realization.md):** explicit Pauli gates, four qubits per fine site, a tracial-auxiliary embedding, and the same shielded coefficient. The input is mixed, and disconnected spin marginals are handled directly.
- **[Continuous time](continuous-time.md):** a balanced nearest-neighbor Lindblad generator with a fixed normalization, faithful finite output reductions, and an explicit algebraic coefficient for every positive time.

## Claim-to-evidence map

| Claim | Decisive argument |
|---|---|
| Every finite fermionic reduction is faithful | A finite occupation eigenvalue zero or one would force a compact band vector; the band dispersion has no rational square root. |
| The input has finite Markov length | Its explicit exponential dressing of a product state admits a shielding decomposition with exponentially small error. |
| The physical channel remains strictly local | The bond-mode dilation is applied in two disjoint-bond layers; dressing commutes with the specified covariance evolution. |
| The output CMI has an exact algebraic coefficient | The inherited interval asymptotic is sandwiched between reference CMIs with logarithmically shifted boundaries. |
| The fully shielded geometry is unstable | Its entropy combination is the sum of two macroscopic one-sided CMIs plus exponentially small ordinary-MI corrections. |
| Ordinary-spin local marginals are faithful | Complete-interval spectra inherit physical faithfulness; arbitrary finite sets follow by partial trace. |

## Definitions and normalization

For finite disjoint regions,

$$
I(A:C\mid B)=S(AB)+S(BC)-S(B)-S(ABC).
$$

The finite-depth construction has two physical fermionic modes per fine site and four per coarse cell. Its spin realization adds one tracial auxiliary per physical mode, giving four qubits per fine site. The continuous-time companion instead uses two physical modes per cell. Each page states its length convention explicitly. Natural logarithms are used throughout; dividing by $\log 2$ converts entropy and CMI to bits.

The infinite-chain state is defined before taking region sizes to infinity. Noise strength and $m>1$ are fixed in those asymptotics. No global trace-norm convergence of infinite many-body states is assumed.

## Sources and reproduction

The [reference catalogue](../references/README.md) separates inherited scalar asymptotics, locality estimates, auxiliary embeddings, and the additional local-faithfulness consequence. The [data guide](../data/README.md) explains the archived finite-size calculations. The [verification guide](../verification/README.md) provides executable checks and their limits.
