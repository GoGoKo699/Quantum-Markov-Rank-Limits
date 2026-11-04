# Project understanding map

This map contains exactly 30 project-defined milestones. **M01–M14 are background/preliminaries; M15–M30 are narrative/innovation.** The first phase joins finite-dimensional quantum information to the fermionic, spatial and thermodynamic conventions needed here. The second assembles the construction and its proofs, then connects the spin and continuous-time realizations to the result's scope. M14 and M30 integrate their respective phases.

The single educational anchor is **Mark M. Wilde, _Quantum Information Theory_, second edition (2017)**. Section numbers and printed starting pages below are checked against Cambridge's [official second-edition contents](https://assets.cambridge.org/97811071/76164/toc/9781107176164_toc.pdf). Wilde supplies the state, channel, entropy, distance and recovery foundations. The linked scientific notes supply the fermionic, Fourier, locality and asymptotic extensions. Research articles identified in the [reference catalogue](../references/README.md) are primary proof dependencies and attribution sources.

Each record gives a central question, an understanding target, earlier-ID dependencies and its place in the story, a conceptual connection, and source pointers. The enclosing phase heading supplies the phase field. The targets cover the connected scientific argument; specialist calculations remain in their canonical scientific notes.

## Phase I — Background and preliminaries: M01–M14

### M01. Local modes, density operators and strict positivity

**Central question.** What does it mean for a finite local state to assign positive probability to every nonzero measurement effect?

**Understanding target.** Interpret a density operator as a positive, normalized operator; distinguish positivity from strict positivity and purity from mixedness. Relate a single fermionic mode to its empty/occupied states, two modes to a four-dimensional fine-site space, and four modes to a sixteen-dimensional coarse-cell space.

**Dependencies and story role.** None. This starts with the finite local objects whose rank appears in the project's question.

**Conceptual connection.** Full rank is a statement about the support of a density operator. It supplies no size-independent lower bound on its smallest eigenvalue.

**Source pointers.** Wilde §§3.7 (p. 93), 4.1 (p. 102). Project: [sites and conventions](../science/model-and-rank.md#1-sites-covariance-and-the-finite-range-hamiltonian), and the definition preceding [Proposition 1](../science/model-and-rank.md#2-every-finite-input-reduction-is-faithful).

### M02. Global purity and faithful local reductions

**Central question.** How can a pure state have a strictly positive density operator on a smaller region?

**Understanding target.** Explain partial trace, entanglement and the Schmidt-spectrum relation in a finite bipartite example. Distinguish purity of the whole state from rank of a reduced state, and distinguish a family of finite reductions of an infinite state from one full finite-system density matrix.

**Dependencies and story role.** M01. This joins local state descriptions into a composite system and removes an apparent contradiction in the intended input.

**Conceptual connection.** Entanglement can make local reductions mixed even when the total state is pure. The project asks for this local positivity on every finite region after the thermodynamic limit.

**Source pointers.** Wilde §§3.8 (p. 98), 4.3 (p. 117), 11.2 (p. 306). Project: [local faithfulness of the input](../science/model-and-rank.md#2-every-finite-input-reduction-is-faithful) and [finite-volume conventions](../science/model-and-rank.md#7-finite-volume-and-locality-conventions).

### M03. Fermionic regions and ordinary tensor factors

**Central question.** Which subsystem operations and entropy inequalities remain valid for fermions?

**Understanding target.** Identify modes, regions and parity-even states; explain why even regional restrictions permit the tensor-factor arguments used for strong subadditivity. Distinguish intrinsic CAR restrictions from disconnected spin marginals in a fixed spatial Jordan–Wigner ordering.

**Dependencies and story role.** M01, M02. This specifies what a region means before channels and conditional information are assigned to it.

**Conceptual connection.** The usual quantum-information language remains usable, but the mode ordering and parity assumptions must be stated. Contiguous-interval spectral identities do not automatically identify disconnected spin and fermion reductions.

**Source pointers.** Wilde §§3.5 (p. 73), 4.3 (p. 117) provide the ordinary tensor-product foundation. Project: [fermionic entropy conventions](../science/locality-and-cmi.md#fermionic-entropy-conventions). Primary extensions: [Yi et al.](../references/README.md#yi), Supplemental Sec. VIII, and [the disjoint-subsystem reference](../references/README.md#gaussian-reductions).

### M04. Local noise, environments and unital channels

**Central question.** How does a local interaction with an environment define a noisy quantum operation?

**Understanding target.** Explain complete positivity, trace preservation, unitary dilation and discarding an environment. Recognize unitality as preservation of the identity, and understand how a fresh maximally mixed environment produces the specified unital gate on a correlated input.

**Dependencies and story role.** M02, M03. This adds controlled dynamics to the local state description.

**Conceptual connection.** The experiment is specified by a physical local dilation and its environment state. The affine covariance rule used later is a consequence of that construction.

**Source pointers.** Wilde §§4.4 (p. 129), 4.5 (p. 141), 5.2 (p. 168). Project: [the weak unital bond channel](../science/model-and-rank.md#3-the-weak-unital-bond-channel). Primary circuit source: [NL](../references/README.md#nl), Eqs. (4)–(6).

### M05. Operational distance and weakness per gate

**Central question.** In what sense can a noisy circuit be arbitrarily weak on each local gate?

**Understanding target.** Interpret trace distance as a measure of state distinguishability and understand why channel comparison must allow an entangled reference system. Distinguish a local gate's diamond-norm bound from a claim about the global distance of an extensive circuit.

**Dependencies and story role.** M04. This makes the noise-strength quantifier precise before discussing instability.

**Conceptual connection.** A bound tending to zero with the local noise angle controls each finite-support operation. A large-distance property can still change after infinitely many such operations are arranged across the chain.

**Source pointers.** Wilde §9.1 (p. 230), with §4.4 (p. 129) for channels. The diamond-norm specialization and its bound are supplied in [the bond-channel proof](../science/model-and-rank.md#3-the-weak-unital-bond-channel), Eqs. (M19)–(M20), and [weakness per local gate](../science/interpretation.md#weakness-is-measured-per-local-gate).

### M06. Gaussian occupations and many-body entropy

**Central question.** When can a small one-particle matrix determine a many-body state's entropy and rank?

**Understanding target.** Distinguish the covariance $`C_{ij}=\omega(c_j^\dagger c_i)`$ from the normalized many-body density matrix. For a gauge-invariant Gaussian state, explain independent occupation eigenvalues, the formula $`S(\rho_R)=\mathrm{Tr}h(C_R)`$, and why all occupations in $`(0,1)`$ are equivalent to a faithful finite reduction. Keep the project's natural-log entropy convention explicit.

**Dependencies and story role.** M01–M04. This supplies the calculational representation that connects local probabilities to the many-body problem.

**Conceptual connection.** Gaussianity makes occupation spectra sufficient. The binary entropy's behavior near zero and one will matter even when no finite-region occupation equals either endpoint.

**Source pointers.** Wilde §§4.1 (p. 102), 11.1 (p. 301). Project: [covariance conventions and Proposition 1](../science/model-and-rank.md), Eqs. (M2)–(M3), (M11). Primary Gaussian results: [Gaussian reductions](../references/README.md#gaussian-reductions).

### M07. From entropy to conditional quantum correlations

**Central question.** What information does conditional mutual information retain after a buffer is specified?

**Understanding target.** Connect joint entropy, conditional entropy and mutual information, then interpret the four entropies in $`I(A:C\mid B)`$. Distinguish ordinary correlations between endpoints from correlations conditioned on an intervening region.

**Dependencies and story role.** M02, M06. This builds the three-region quantity whose spatial decay defines the problem.

**Conceptual connection.** CMI combines overlapping reductions. Its behavior is not determined by one two-point correlation function or by the purity of any individual region.

**Source pointers.** Wilde §§11.2 (p. 306), 11.4 (p. 311), 11.6 (p. 315), 11.7 (p. 318). Project: [CMI definitions and normalization](../science/instability-theorem.md#1-definitions-normalization-and-order-of-limits).

### M08. Strong subadditivity and permitted boundary moves

**Central question.** Which changes to the endpoint and buffer regions give a valid CMI inequality?

**Understanding target.** Use nonnegativity, the chain rule and endpoint data processing to understand
$`I(A:C\mid aB_0c)\le I(Aa:Cc\mid B_0)`$.
Distinguish this controlled movement of buffer strips from an unsupported monotonicity claim about arbitrary changes to the conditioning region.

**Dependencies and story role.** M03, M07. This turns entropy inequalities into the geometric tool needed by the dressing proof.

**Conceptual connection.** A local circuit can move information across a boundary. Absorbing complete gate blocks into endpoints converts that motion into an inequality on a nearby partition.

**Source pointers.** Wilde §§11.7 (p. 318), 11.9 (p. 327). Project: [circuit CMI comparison](../science/locality-and-cmi.md#circuit-cmi-comparison), especially Eq. (9).

### M09. Shielding, recoverability and Markov length

**Central question.** What does finite Markov length require across an entire family of regions?

**Understanding target.** Read the two-sided geometry $`C_-B_-AB_+C_+`$ and its exponential CMI bound with a fixed polynomial size prefactor. Explain why a positive algebraic tail on regions whose sizes grow proportionally to the buffer violates that bound. Relate small CMI to recovery while keeping the spatial uniformity requirement distinct.

**Dependencies and story role.** M07, M08. This extends a tripartite information quantity into a property of an infinite spatial state.

**Conceptual connection.** Recovery supplies operational motivation for CMI. Markov length additionally asks for uniform decay across shielding geometries, beyond ordinary two-point clustering.

**Source pointers.** Wilde §§11.7 (p. 318), 12.1 (p. 347), 12.3 (p. 353). Project: [the exact definition](../science/instability-theorem.md#1-definitions-normalization-and-order-of-limits), Eq. (T4). Primary definition and setting: [NL](../references/README.md#nl), Eq. (2).

### M10. Entropy continuity without a spectral floor

**Central question.** How can a small state-approximation error control CMI near nearly pure modes?

**Understanding target.** Explain why finite-dimensional entropy continuity does not require a positive eigenvalue lower bound. Track the endpoint dimension in conditional-entropy continuity, and distinguish this dimension factor from an unnecessary dependence on the entire exterior.

**Dependencies and story role.** M05, M07. This supplies the error control needed to replace exact dynamics by local approximants.

**Conceptual connection.** The entropy function is singular at zero, yet its continuity remains quantitative. A polynomially small trace error can therefore be chosen small enough to resolve a polynomial CMI tail.

**Source pointers.** Wilde §§9.1 (p. 230), 11.10 (p. 339). Project: [continuity estimate](../science/locality-and-cmi.md#continuity-estimate), Eq. (1), and [Gaussian MI bound](../science/locality-and-cmi.md#gaussian-mutual-information-bound). Primary sharp bounds: [Winter and Audenaert](../references/README.md#continuity).

### M11. Gapped Hamiltonians and occupied-band projectors

**Central question.** What is the relation between an energy gap, a pure Gaussian state and its local occupation spectrum?

**Understanding target.** Explain a quadratic Hamiltonian's one-particle bands and the projector onto occupied negative-energy states. Distinguish a Hamiltonian energy gap from an occupation margin away from zero and one, and understand why compressing a projector to a finite region need not leave a projector.

**Dependencies and story role.** M02, M06. This connects the information-theoretic state description to the ground-state preparation.

**Conceptual connection.** A globally pure Gaussian state has a projector covariance. Its finite compressions can be faithful, although occupations may approach zero and one as regions grow.

**Source pointers.** Wilde §§3.3 (p. 60), 4.1 (p. 102), 11.1 (p. 301) provide the unitary, spectral and entropy foundations. The band construction is supplied by [the finite-range Hamiltonian](../science/model-and-rank.md#1-sites-covariance-and-the-finite-range-hamiltonian) and [nearly pure modes](../science/interpretation.md#qualitative-faithfulness-and-nearly-pure-modes).

### M12. Fourier structure and exponential spatial locality

**Central question.** How does a smooth momentum-space construction become a spatially local operation?

**Understanding target.** Connect an analytic periodic symbol with exponentially decaying real-space coefficients. Explain the role of an explicit analytic phase in constructing the dressing generator, and distinguish locality of the covariance from locality of the nonlinear entropy function.

**Dependencies and story role.** M03, M11. This translates the single-particle band description into the spatial estimates used later.

**Conceptual connection.** Analytic dressing can preserve exponential ordinary correlations while changing the exact support of occupied modes. Entropic singularities can survive such a change of basis.

**Source pointers.** Wilde §3.3 (p. 60) supplies reversible-evolution language. Fourier and locality details are project-supplied: [the explicit dressing](../science/model-and-rank.md#5-an-exponentially-local-dressing-that-commutes-with-the-noise) and [interaction norm](../science/locality-and-cmi.md#infinite-volume-dynamics-and-interaction-norm). Primary locality sources are collected under [Local dynamics](../references/README.md#local-dynamics).

### M13. Local approximations and the order of limits

**Central question.** How can infinite-chain evolution be compared rigorously on a finite observation region?

**Understanding target.** Explain finite-window approximations that remain valid for inputs correlated with the exterior. Distinguish an infinite-volume automorphism from a global Fock-space unitary, and keep the thermodynamic limit, large-region limit and zero-noise limit in their stated order.

**Dependencies and story role.** M05, M10, M12. This combines local dynamics and finite-dimensional error estimates into a controlled infinite-chain framework.

**Conceptual connection.** Uniform local estimates make the large-system argument possible without a global trace-norm limit. The relevant boundary displacements and continuity errors must remain below the scale of the CMI being studied.

**Source pointers.** Wilde §§4.3 (p. 117), 9.1 (p. 230), 11.10 (p. 339). Project: [local circuit approximation](../science/locality-and-cmi.md#local-circuit-approximation) and [finite-volume order of limits](../science/locality-and-cmi.md#finite-volume-order-of-limits). Primary extension: [Local dynamics](../references/README.md#local-dynamics).

### M14. Background synthesis: the stability question as a complete statement

**Central question.** What must be established to decide whether local faithfulness protects finite Markov length?

**Understanding target.** Assemble the state, region, channel and limiting conventions into one statement: faithful finite input reductions, initial exponential shielded CMI, arbitrarily weak strictly local gates, faithful finite output reductions, and a positive shielded algebraic tail. Keep each assumption tied to the argument that would establish it.

**Dependencies and story role.** M01–M13. This integrates the background phase into the proof architecture needed for the construction.

**Conceptual connection.** Local rank, energy gap, channel strength and conditional-information decay constrain different mathematical objects. The stability question concerns their conjunction.

**Source pointers.** Wilde §§4.3 (p. 117), 4.4 (p. 129), 11.7 (p. 318), 12.1 (p. 347). Project: [scientific account and claim-to-evidence map](../science/README.md) and [the central theorem](../science/instability-theorem.md#2-central-theorem).

## Phase II — Narrative and innovation: M15–M30

### M15. The concrete gapped input and its two spatial scales

**Central question.** Which local Hamiltonian provides the input, and why are four modes grouped into a coarse cell?

**Understanding target.** Explain the two interleaved SSH chains, the parity/subcell and orbital tensor factors, the gap for $`m>1`$, and the relation between fine sites and coarse cells. Keep the input's one-fine-site translation symmetry distinct from the circuit's two-site period.

**Dependencies and story role.** M11, M12, M14. This begins the narrative with the explicit local Hamiltonian and its physical degrees of freedom.

**Conceptual connection.** The tensor factors support different operations: the orbital structure creates a nontrivial faithful input, while the parity/subcell structure retains the solvable noise circuit.

**Source pointers.** Wilde §§3.3 (p. 60), 3.5 (p. 73), 4.1 (p. 102). Project: [model conventions and Hamiltonian](../science/model-and-rank.md#1-sites-covariance-and-the-finite-range-hamiltonian), Eqs. (M1), (M6)–(M9).

### M16. Excluding compact band modes proves local faithfulness

**Central question.** Why does this pure ground state have no exactly forbidden state on any finite region?

**Understanding target.** Follow the implication from a finite covariance eigenvalue zero or one to a compactly supported occupied or empty band vector. Explain how its Laurent-polynomial components would force a rational square root of the dispersion, contradicting the simple zeros and poles.

**Dependencies and story role.** M02, M06, M15. This establishes the first additional ingredient: faithfulness on every finite mode set.

**Conceptual connection.** Exact compact support is much stronger than exponential localization. Eliminating compact band vectors removes local rank deficiencies while retaining a pure, gapped ground state.

**Source pointers.** Wilde §§4.1 (p. 102), 4.3 (p. 117), 11.1 (p. 301). The compact-support and rational-function argument is the project's [Proposition 1](../science/model-and-rank.md#proposition-1-local-faithfulness-of-the-input), Eqs. (M12)–(M14).

### M17. A strictly local, weak, unital noise circuit

**Central question.** How is the physical perturbation implemented without increasing its range or depth?

**Understanding target.** Explain the symmetric bond mode, its fresh maximally mixed ancilla, the two disjoint-bond layers and the identical treatment of both orbitals. Connect the local dilation to unitality and the $`8\epsilon^2`$ diamond-norm bound.

**Dependencies and story role.** M04, M05, M15. This adds the concrete local perturbation to the faithful input.

**Conceptual connection.** The small parameter controls each physical gate while the circuit depth and support stay fixed. The scalar circuit is inherited; the choice of orbital action enables its use with the new input.

**Source pointers.** Wilde §§4.4 (p. 129), 4.5 (p. 141), 5.2 (p. 168), 9.1 (p. 230). Project: [bond channel](../science/model-and-rank.md#3-the-weak-unital-bond-channel) and [covariance matrices](../science/model-and-rank.md#4-exact-covariance-matrices-of-the-circuit). Primary circuit: [NL](../references/README.md#nl), Eqs. (4)–(6), Appendix G.

### M18. The tensor identity that preserves the solvable reference

**Central question.** Why does the orbital dressing remain compatible with the strictly local noise?

**Understanding target.** Explain why the noise matrices act as a parity/subcell matrix tensored with the orbital identity, while the dressing acts on the orbital factor. Use the resulting covariance identities to relate both the input and output to their undressed references.

**Dependencies and story role.** M12, M15, M17. This joins the Hamiltonian and channel into the central construction.

**Conceptual connection.** Exact tensor commutation relates the specified Gaussian states to a solvable product-input reference while preserving the physical nearest-neighbor gates. It does not require a general commutation claim on arbitrary spin inputs.

**Source pointers.** Wilde §§3.3 (p. 60), 3.5 (p. 73), 4.4 (p. 129). Project: [exact covariance matrices](../science/model-and-rank.md#4-exact-covariance-matrices-of-the-circuit) and [compatible exponential dressing](../science/model-and-rank.md#5-an-exponentially-local-dressing-that-commutes-with-the-noise), Eqs. (M30)–(M36).

### M19. Local faithfulness survives the finite-depth channel

**Central question.** Why does the output also avoid every finite-region rank deficiency?

**Understanding target.** Follow how a nonzero finite-support vector remains finite-support and nonzero under the adjoint of the circuit's invertible finite-propagation matrix. Combine input faithfulness with positivity of the affine noise term for both $`C_{\mathrm{out}}`$ and $`I-C_{\mathrm{out}}`$.

**Dependencies and story role.** M16, M18. This closes the local-rank argument on both sides of the perturbation.

**Conceptual connection.** Strict positivity of every finite compression is compatible with a global occupation band touching zero or one at a dark momentum. The output's entropic tail need not arise from an exactly pure local mode.

**Source pointers.** Wilde §§4.1 (p. 102), 4.4 (p. 129), 11.1 (p. 301). Project: [Proposition 2](../science/model-and-rank.md#proposition-2-local-faithfulness-after-the-channel), Eqs. (M37)–(M40).

### M20. Exponential CMI of the initial state

**Central question.** What proves the initial shielded CMI bound beyond ordinary correlation decay?

**Understanding target.** Explain the buffer-local decomposition of the exponential dressing, its exact Markov reference state, and the use of conditional-entropy continuity. Track why the error is controlled by the shielding strips and remains independent of the exterior size.

**Dependencies and story role.** M08, M10, M13, M18. This establishes the global information property of the prepared input.

**Conceptual connection.** Dressing a product state for fixed time with exponentially decaying interactions leaves exponentially little conditional information across a wide shield. The explicit interaction tail is the hypothesis that supports the exponential conclusion here.

**Source pointers.** Wilde §§11.7 (p. 318), 11.9 (p. 327), 11.10 (p. 339). Project: [initial exponential CMI, Proposition 1](../science/locality-and-cmi.md#initial-exponential-cmi). Primary decomposition: [Yi et al.](../references/README.md#yi), Supplemental Theorem III.1 and Eqs. (III.4)–(III.11).

### M21. The inherited dark mode and algebraic interval entropy

**Central question.** How can short-range covariance coexist with an algebraic entropy correction?

**Understanding target.** Connect the scalar circuit's quadratic occupation-band zero to the singularity of binary entropy at zero. Identify the interval-entropy asymptotic as an imported theorem, and account for the two complementary orbital sectors that change its coefficient to $`\kappa_\epsilon=\gamma_\epsilon\zeta(3)`$.

**Dependencies and story role.** M06, M07, M18. This supplies the solvable reference's long-distance mechanism.

**Conceptual connection.** Analytic covariance alone does not make the entropy analytic at a spectral edge. The source's interval result, with its two-site length convention, gives the precise correction required by the project.

**Source pointers.** Wilde §11.1 (p. 301) provides the entropy foundation. Project: [inherited single-orbital entropy theorem](../science/instability-theorem.md#3-the-inherited-single-orbital-entropy-theorem), Eqs. (T11)–(T13). Primary theorem: [NL](../references/README.md#nl), Eq. (13) and Appendix E.1, Eq. (132).

### M22. Transferring the coefficient through a local CMI sandwich

**Central question.** Why does the dressing preserve the leading macroscopic CMI coefficient?

**Understanding target.** Explain the forward and inverse circuit comparisons, including both inner and outer endpoint boundaries. Relate logarithmic boundary shifts and sufficiently small local trace error to a common $`L^{-2}`$ leading term, without assuming an individual dressed-entropy expansion.

**Dependencies and story role.** M08, M10, M13, M18, M21. This transports the reference mechanism to the physical output.

**Conceptual connection.** Strong subadditivity supplies a geometric comparison; locality keeps the comparison regions close; continuity controls the approximation. Together they preserve a coefficient that none of these ingredients determines alone.

**Source pointers.** Wilde §§11.7 (p. 318), 11.9 (p. 327), 11.10 (p. 339). Project: [macroscopic CMI squeeze, Proposition 4](../science/locality-and-cmi.md#macroscopic-cmi-squeeze) and [the coefficient-transfer argument](../science/instability-theorem.md#4-transferring-the-coefficient-through-the-dressing).

### M23. The fully shielded instability theorem

**Central question.** How does the one-sided asymptotic prove the exact two-sided Markov-length claim?

**Understanding target.** Reconstruct the five-block entropy identity as two one-sided CMIs plus ordinary-MI corrections. Explain why analytic covariance makes those corrections exponentially small and why the positive coefficient $`643\kappa_\epsilon/450`$ proves infinite Markov length despite faithful input and output reductions.

**Dependencies and story role.** M09, M19, M20, M22. This integrates the main fermionic construction into its complete theorem.

**Conceptual connection.** The conditioning geometry is handled by an exact entropy identity. All five region sizes grow proportionally, so a positive inverse-square tail defeats every allowed polynomial-prefactor exponential bound.

**Source pointers.** Wilde §§11.6 (p. 315), 11.7 (p. 318), 11.9 (p. 327). Project: [fully shielded asymptotic](../science/instability-theorem.md#5-the-exact-fully-shielded-asymptotic), Eqs. (T18)–(T25), and [Gaussian MI bound](../science/locality-and-cmi.md#gaussian-mutual-information-bound).

### M24. Lifting the local gates to ordinary spins

**Central question.** How can the fermionic gate be realized as a strictly local ordinary-spin channel?

**Understanding target.** Explain the tracial auxiliary mode attached to each physical mode and the even lift $`\widetilde\Gamma=i\eta\Gamma`$. Follow the exact embedding identity on even physical states and the Jordan–Wigner cancellation that produces the displayed two-site Pauli gates.

**Dependencies and story role.** M03, M04, M17. This opens the ordinary-spin branch at the level of a concrete local operation.

**Conceptual connection.** The auxiliary embedding converts the required odd conjugations into even local operators. The resulting spin channel is unital on its whole finite Hilbert space, while the input acquires tracial auxiliary degrees of freedom.

**Source pointers.** Wilde §§4.3 (p. 117), 4.4 (p. 129), 5.2 (p. 168). Project: [the exact gate lift](../science/spin-realization.md#2-exact-lift-of-each-random-unitary-gate) and [Jordan–Wigner locality](../science/spin-realization.md#3-jordan--wigner-locality-and-depth), Eqs. (S3)–(S9). Primary embedding: [NZH](../references/README.md#nzh), Supplemental Sec. SIII.

### M25. Completing the ordinary-spin result

**Central question.** Which statements survive the spin realization, and how are disconnected regions handled?

**Understanding target.** Derive arbitrary-set faithfulness from faithful complete intervals and partial trace. Explain initial finite Markov length for the dressed mixed product input and ordinary-spin MI decay from disjoint past cones. Track the same shielded coefficient while retaining the globally mixed input and extensive auxiliary degeneracy.

**Dependencies and story role.** M23, M24. This joins the spin construction to the global conditional-information conclusion.

**Conceptual connection.** Contiguous interval spectra import the solvable entropy data. Tensor-factor locality supplies the disconnected-region estimates directly, so no disconnected fermion/spin entropy identity is required.

**Source pointers.** Wilde §§4.3 (p. 117), 11.6 (p. 315), 11.7 (p. 318), 11.10 (p. 339). Project: [spin realization](../science/spin-realization.md), Sections 5–9, especially Eqs. (S13)–(S25).

### M26. The balanced continuous-time companion

**Central question.** How does local gain and loss produce the same type of obstruction with two modes per site?

**Understanding target.** Explain the balanced nearest-neighbor generator, its scalar orbital damping and the occupations $`q_t(k)`$ and $`1-q_t(k)`$. Understand its even-sector finite-volume definition and why positivity almost everywhere proves output faithfulness when the attenuation matrix has infinite range.

**Dependencies and story role.** M18, M19. This opens the continuous-time branch with its local generator and exact state evolution.

**Conceptual connection.** Orbital isotropy again preserves the dressing identity. The continuous-time positivity proof uses the symbol's almost-everywhere positivity, replacing the finite-propagation argument available for the circuit.

**Source pointers.** Wilde §§4.1 (p. 102), 4.4 (p. 129) provide state and evolution foundations. Project: [continuous-time model and covariance](../science/continuous-time.md#model-and-exact-covariance) and [faithfulness](../science/continuous-time.md#faithfulness-and-the-dressing-identity), Eqs. (C1)–(C8). Primary scalar dynamics: [NL](../references/README.md#nl), Appendix H.

### M27. The continuous-time coefficient and its limits

**Central question.** What fixes the algebraic coefficient for every fixed positive evolution time?

**Understanding target.** Track the source conversion $`t_{\mathrm{NL}}=2t`$ and $`n=2N`$ separately, then include both complementary orbital sectors. Explain why even-length source intervals suffice for the macroscopic comparison and obtain the shielded coefficient $`643t\zeta(3)/900`$ at fixed finite $`t>0`$.

**Dependencies and story role.** M21, M22, M23, M26. This completes the continuous-time branch and its normalization.

**Conceptual connection.** The same entropy-to-CMI mechanism survives, with a distinct site convention and time normalization. Arbitrarily short positive times are compatible with nonuniform zero-time and large-region limits.

**Source pointers.** Wilde §§11.1 (p. 301), 11.7 (p. 318), 11.10 (p. 339). Project: [imported scalar entropy and normalization](../science/continuous-time.md#imported-scalar-entropy-and-its-normalization) and [continuous-time corollary](../science/continuous-time.md#corollary-algebraic-cmi-after-every-fixed-positive-time), Eqs. (C9)–(C14). Primary theorem: [NL](../references/README.md#nl), Appendix H, Eqs. (169), (174).

### M28. Qualitative rank versus a uniform occupation margin

**Central question.** What quantitative protection is missing from local faithfulness?

**Understanding target.** Explain how truncating an exponentially localized Wannier mode produces nearly pure finite-region occupations without creating an exact zero eigenvalue. Distinguish a uniform one-particle occupation margin from a uniform lower bound on a many-body density matrix, and interpret the finite-temperature covariance comparison within its stated scope.

**Dependencies and story role.** M02, M06, M16, M19, M23, M26. This connects all realizations to the spectral distinction underlying the result.

**Conceptual connection.** Exact positivity is qualitative. A uniform occupation margin keeps the relevant entropy function away from its singular edges; the construction deliberately retains access to those edges in growing regions.

**Source pointers.** Wilde §§4.1 (p. 102), 11.1 (p. 301), 11.10 (p. 339). Project: [nearly pure modes](../science/interpretation.md#qualitative-faithfulness-and-nearly-pure-modes) and [finite-temperature comparison](../science/interpretation.md#a-finite-temperature-comparison-in-the-same-model).

### M29. The precise boundary of the contribution

**Central question.** Which stability hypothesis is ruled out, and which nearby hypotheses remain distinct?

**Understanding target.** Separate qualitative local faithfulness from product structure and uniform spectral conditions. Distinguish the pure fermionic input from the mixed spin input, fine-tuned noise from generic noise, and conditional-information divergence from a general phase-transition or irreversibility claim. Identify the scalar asymptotic and auxiliary embedding as inherited ingredients.

**Dependencies and story role.** M09, M23, M25, M27, M28. This places the combined result among the actual neighboring statements.

**Conceptual connection.** The counterexample has force because its assumptions are explicit. Comparing assumptions, mechanisms and limiting procedures prevents stronger conclusions than the proof supports.

**Source pointers.** Wilde §§4.3 (p. 117), 11.7 (p. 318), 12.1 (p. 347). Project: [consequences for stability](../science/interpretation.md#consequence-for-stability-statements) and [coefficient audit and scope](../science/instability-theorem.md#7-coefficient-audit-and-scope). Primary comparisons: [the reference catalogue](../references/README.md#comparison-at-the-level-of-assumptions).

### M30. Final synthesis: a local-rank condition cannot control the tail

**Central question.** How do the local construction, spectral mechanism and global information estimates form one scientific result?

**Understanding target.** Give a connected account from the gapped faithful input and compatible weak local noise to the retained dark-mode entropy singularity, the rigorous CMI transfer and the fully shielded inverse-square tail. Integrate the spin and continuous-time realizations with their distinct state, locality and normalization conventions, and state the resulting limitation of qualitative local rank.

**Dependencies and story role.** M14, M23, M25, M27, M28, M29. This integrates the narrative phase and the project as a whole.

**Conceptual connection.** The result separates local measurement support from the uniform spectral control needed to constrain long-distance conditional information. The proof combines exact model identities with locality and entropy inequalities.

**Source pointers.** Wilde §§11.1 (p. 301), 11.7 (p. 318), 11.9 (p. 327), 12.1 (p. 347). Canonical synthesis: [scientific account](../science/README.md), [central theorem](../science/instability-theorem.md#2-central-theorem), [spin realization](../science/spin-realization.md), [continuous-time companion](../science/continuous-time.md), and [interpretation](../science/interpretation.md).
