# Learning route from Wilde to the local-rank question

The organizing question is whether full rank of every finite local density matrix is enough to preserve finite quantum Markov length under weak local noise. The project constructs a counterexample with a pure, gapped fermionic input, faithful finite reductions before and after the noise, and an inverse-square conditional-mutual-information tail after two layers of weak unital gates.

The learning material connects this statement to finite-dimensional quantum information, then identifies the additional Gaussian, spatial and thermodynamic arguments that establish it.

## The connected account

- **[Bridge](bridge.md):** a substantive explanation from regions, spectra and channels to the construction. It includes a worked full-rank spectrum, a calculation showing how conditioning noise can increase CMI, a notation translation, and the entropy-to-CMI mechanism.
- **[Understanding map](milestones.md):** exactly 30 project-defined milestones with central questions, understanding targets, earlier dependencies, conceptual connections and source pointers. M01–M14 are background/preliminaries; M15–M30 are narrative/innovation. M14 and M30 synthesize their phases.
- **[Scientific account](../science/README.md):** the complete model, proofs, coefficient normalization, related realizations and scope.
- **[Research references](../references/README.md):** primary theorem sources and comparison of assumptions. These are proof dependencies and attribution sources, distinct from the single educational anchor below.

<a id="selected-educational-anchor"></a>

## Selected educational anchor

**Mark M. Wilde, *Quantum Information Theory*, second edition, Cambridge University Press (2017).** DOI: [10.1017/9781316809976](https://doi.org/10.1017/9781316809976). Hardback ISBN: 9781107176164.

Cambridge's [official second-edition frontmatter](https://assets.cambridge.org/97811071/76164/frontmatter/9781107176164_frontmatter.pdf) identifies the edition and year. Its [official table of contents](https://assets.cambridge.org/97811071/76164/toc/9781107176164_toc.pdf) verifies the section numbers and printed starting pages used here and in the map.

The author's [public draft, *From Classical to Quantum Shannon Theory*](https://markwilde.com/qit-notes.pdf), is an alternative access point to the same work. The inspected copy is dated 5 December 2021 and contains later corrections with different pagination. Its page numbers should therefore not be substituted for the 2017 printed locators below. The draft is not a second educational anchor.

## Precise source connections

| Foundation used in the project | Second-edition sections | Printed starting pages |
|---|---|---|
| Finite dimensions, composite systems and Schmidt spectra | §§3.5, 3.7–3.8 | 73, 93, 98 |
| Density operators and reduced states | §§4.1, 4.3 | 102, 117 |
| Channels, their interpretation and environmental realizations | §§4.4–4.5, 5.1–5.2 | 129, 141, 165, 168 |
| State and channel distinguishability | §9.1 | 230 |
| Entropy and conditional entropy | §§11.1–11.2, 11.4 | 301, 306, 311 |
| Mutual information, CMI and entropy inequalities | §§11.6–11.7, 11.9 | 315, 318, 327 |
| Entropy continuity | §11.10 | 339 |
| Recovery and its relation to conditional information | §§12.1, 12.3 | 347, 353 |

These pointers describe the parts of Wilde used as foundations. The project does not require the book's channel-coding development to state its central question. The Gaussian representation, occupied-band construction, compact-support obstruction, exponentially local dressing and scalar interval-entropy asymptotic are supplied by the scientific notes and their research citations.

## How the map connects to the bridge

| Milestones | Role in the connected argument | Bridge location |
|---|---|---|
| [M01–M06](milestones.md#m01-local-modes-density-operators-and-strict-positivity) | States, finite reductions, parity conventions, noise and Gaussian spectra | [Notation](bridge.md#2-a-notation-translation), [worked spectrum](bridge.md#3-a-worked-spectrum-full-rank-without-a-uniform-margin), and [weak gates](bridge.md#5-what-weak-local-noise-means-here) |
| [M07–M10](milestones.md#m07-from-entropy-to-conditional-quantum-correlations) | Conditional information, permitted inequalities, recovery and continuity | [Region question](bridge.md#1-the-finite-region-question) and [conditioning-noise calculation](bridge.md#4-why-noise-on-the-buffer-can-increase-cmi) |
| [M11–M14](milestones.md#m11-gapped-hamiltonians-and-occupied-band-projectors) | Band projectors, exponential locality, limits and background synthesis | [Gapped input](bridge.md#6-from-density-matrices-to-a-locally-faithful-gapped-input) and [research ingredients](bridge.md#9-which-ingredients-the-scientific-account-supplies) |
| [M15–M20](milestones.md#m15-the-concrete-gapped-input-and-its-two-spatial-scales) | Concrete Hamiltonian, input/output rank, noise and compatible dressing | [Input proof mechanism](bridge.md#6-from-density-matrices-to-a-locally-faithful-gapped-input) and [dressing identity](bridge.md#7-the-dressing-identity-and-its-locality-content) |
| [M21–M23](milestones.md#m21-the-inherited-dark-mode-and-algebraic-interval-entropy) | Imported scalar asymptotic, CMI transfer and the shielded theorem | [Entropy correction and CMI](bridge.md#8-the-entropy-correction-that-survives-in-cmi) |
| [M24–M27](milestones.md#m24-lifting-the-local-gates-to-ordinary-spins) | Ordinary-spin and continuous-time realizations | [Realizations and scope](bridge.md#10-connecting-the-realizations-and-the-scope) |
| [M28–M30](milestones.md#m28-qualitative-rank-versus-a-uniform-occupation-margin) | Spectral margins, assumptions and final synthesis | [Spectrum distinction](bridge.md#3-a-worked-spectrum-full-rank-without-a-uniform-margin) and [final connection](bridge.md#10-connecting-the-realizations-and-the-scope) |

## Conventions that carry through the account

Wilde uses base-two entropy; the scientific notes use natural logarithms. Thus an entropy or CMI coefficient in nats is divided by $`\log2`$ to obtain bits. A covariance matrix records one-particle occupations and is distinct from the many-body density matrix. A strictly positive finite reduction has no exactly forbidden nonzero positive measurement effect, but its smallest occupation can still approach zero as the region grows.

The finite-depth result uses four-mode coarse cells, each consisting of two fine sites. Its initial state is an infinite-chain state obtained by a local thermodynamic limit. Spatial asymptotics then hold at fixed nonzero noise strength. The ordinary-spin and continuous-time branches preserve the central local-rank distinction with their own explicitly stated input, locality and length conventions.
