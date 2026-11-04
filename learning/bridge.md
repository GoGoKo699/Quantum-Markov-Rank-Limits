# From finite-dimensional quantum information to local-rank instability

Consider a region of a quantum chain, a surrounding buffer, and a more distant region. The local density matrices describe which measurements can occur. Conditional mutual information asks how much correlation remains across the buffer after the buffer is included in the description. This project asks whether strict positivity of **every finite local density matrix** protects exponential decay of that conditional information against weak local noise.

The answer in the construction is negative. The input is a pure, gapped fermionic ground state with faithful finite reductions and finite Markov length. Two layers of arbitrarily weak unital nearest-neighbor noise preserve faithfulness of all finite reductions while producing an inverse-square conditional-information tail. Understanding this statement requires keeping local rank, entropy, spatial locality and limiting procedures separate, then connecting them through the proof.

The educational anchor is [Mark M. Wilde, *Quantum Information Theory*, second edition (2017)](README.md#selected-educational-anchor). The section references below use that edition. The [30-part understanding map](milestones.md) gives the complete progression; this bridge develops the connections behind it. Research sources support the additional Gaussian, locality and asymptotic arguments through the [scientific account](../science/README.md) and [reference catalogue](../references/README.md).

## 1. The finite-region question

**Connection to the map:** [M01–M03](milestones.md#m01-local-modes-density-operators-and-strict-positivity) and [M07–M09](milestones.md#m07-from-entropy-to-conditional-quantum-correlations). **Wilde:** §§4.1, 4.3, 11.4, 11.6–11.7.

Start with three finite systems $`A,B,C`$ and their joint density operator $`\rho_{ABC}`$. The reduced operator $`\rho_{AB}=\operatorname{Tr}_C\rho_{ABC}`$ reproduces all measurements supported on $`AB`$. The von Neumann entropy of a reduction is

```math
S_\rho(A)=-\operatorname{Tr}(\rho_A\log\rho_A).
```

The project's conditional mutual information, or CMI, is

```math
\begin{aligned}
I_\rho(A:C\mid B)
={}&S_\rho(AB)+S_\rho(BC)\\
&-S_\rho(B)-S_\rho(ABC).
\end{aligned}
```

Equivalently, it is $`S_\rho(A\mid B)-S_\rho(A\mid BC)`$, where conditional entropy is defined by a difference of joint entropies. In a quantum state, this definition does not require measuring $`B`$ or replacing it by a classical outcome. Strong subadditivity says the difference is nonnegative.

For spatial systems, $`A,B,C`$ are regions. A one-sided arrangement consists of three consecutive intervals. The Markov-length definition used here instead shields the central region on both sides:

```math
C_-\quad B_-\quad A\quad B_+\quad C_+,
\qquad
B=B_-\cup B_+,\quad C=C_-\cup C_+.
```

The buffer widths separate $`A`$ from the exterior pieces. Finite Markov length requires a finite $`\xi`$ and a fixed polynomial $`P`$ such that

```math
I_\rho(A:C\mid B)
\le P(|A|,|B|,|C|)\,e^{-\operatorname{dist}(A,C)/\xi}
```

throughout the specified family of finite shielded regions. This is a spatially uniform requirement. A small CMI for one finite triple, or exponential decay of a particular two-point correlation function, does not by itself establish it. The exact convention is in [the theorem's definitions](../science/instability-theorem.md#1-definitions-normalization-and-order-of-limits).

## 2. A notation translation

Wilde's state, channel and entropy language applies directly to the finite restrictions used in the project. Three conventions deserve explicit translation.

| Object | Wilde's convention or finite-system language | Project convention |
|---|---|---|
| Entropy | $`H(A)_\rho`$, with base-two logarithms | $`S_\rho(A)`$, with natural logarithms |
| Conditional mutual information | $`I(A;C\mid B)_\rho`$ | $`I_\rho(A:C\mid B)`$; the punctuation has no mathematical significance |
| Quantum channel | Usually $`\mathcal N`$ | $`\Phi_{x,\epsilon}`$ for a bond gate and $`\mathcal E_\epsilon`$ for the two-layer circuit |
| State distance | Trace norm and its normalized half-distance appear separately | The locality estimates use $`t=\tfrac12\lVert\rho-\sigma\rVert_1`$ |
| Infinite state | Finite density operators provide the starting language | $`\omega_m`$ and $`\rho_{m,\epsilon}`$ denote consistent infinite-chain states; their finite restrictions are density operators |
| Gaussian covariance | An additional representation beyond the prerequisites used from Wilde | $`C_{ij}=\omega(c_j^\dagger c_i)`$ is a one-particle occupation matrix, not a trace-one many-body density matrix |

Thus

```math
S_{\rm nats}=(\log 2)H_{\rm bits},
\qquad
I_{\rm nats}=(\log 2)I_{\rm bits}.
```

Every coefficient in the scientific account is in nats. Dividing it by $`\log 2`$ gives the coefficient in bits.

The symbol $`C`$ also labels an exterior region; the presence of matrix indices or a subscript such as $`C_R`$ identifies the covariance. A fine site contains two fermionic modes and has Fock-space dimension four. A coarse cell contains two fine sites, hence four modes and dimension sixteen. The finite-depth theorem measures interval lengths in **coarse cells**. The continuous-time companion uses a different, explicitly stated two-mode site convention.

Fermionic subsystems require one further specification. The account uses restrictions of parity-even states to finite CAR algebras. The [fermionic entropy conventions](../science/locality-and-cmi.md#fermionic-entropy-conventions) justify the regional entropy inequalities used in the proof. They do not identify arbitrary disconnected fermionic reductions with disconnected spin reductions under a fixed Jordan–Wigner ordering. That distinction is handled separately in the spin realization.

## 3. A worked spectrum: full rank without a uniform margin

**Connection to the map:** [M01–M02](milestones.md#m01-local-modes-density-operators-and-strict-positivity), [M06](milestones.md#m06-gaussian-occupations-and-many-body-entropy), and [M28](milestones.md#m28-qualitative-rank-versus-a-uniform-occupation-margin). **Wilde:** §§3.8, 4.1, 4.3, 11.1, 11.10.

For $`0<\eta<1`$, consider the single-mode density operator

```math
\rho_\eta=
\begin{pmatrix}1-\eta&0\\0&\eta\end{pmatrix}.
```

It is strictly positive because both eigenvalues are positive. Consequently every nonzero positive measurement effect $`E`$ has positive probability:

```math
\operatorname{Tr}(\rho_\eta E)
\ge \min(\eta,1-\eta)\operatorname{Tr}E>0.
```

This local mixedness is compatible with a pure global state. The vector

```math
|\psi_\eta\rangle
=\sqrt{1-\eta}\,|00\rangle+\sqrt\eta\,|11\rangle
```

is pure, while tracing out either mode gives $`\rho_\eta`$. The Schmidt coefficients make the relation between global purity and the local spectrum explicit.

Now let $`\eta_\ell=e^{-\ell}`$ for positive integers $`\ell`$. Every $`\rho_{\eta_\ell}`$ is full rank, but its smallest eigenvalue tends to zero. There is no fixed $`\delta>0`$ that bounds all those eigenvalues below. The quantifiers differ:

```math
\text{for every }\ell:\quad \lambda_{\min}(\rho_{\eta_\ell})>0,
```

```math
\text{there exists }\delta>0\text{ for every }\ell:\quad
\lambda_{\min}(\rho_{\eta_\ell})\ge\delta.
```

Only the first statement holds.

The Gaussian version makes the occupation/many-body distinction visible. Take two independent normal modes with occupations $`\eta`$ and $`1-\eta`$. Their covariance is $`\operatorname{diag}(\eta,1-\eta)`$, and the many-body eigenvalues, in some order, are

```math
\eta^2,\quad \eta(1-\eta),\quad
\eta(1-\eta),\quad (1-\eta)^2.
```

At $`\eta=1/4`$, these are $`1/16,3/16,3/16,9/16`$. They sum to one, all are positive, and the entropy is

```math
\begin{aligned}
S&=2h(1/4)\\
&=2\log4-\frac32\log3
\simeq1.12467\ \text{nats},
\end{aligned}
```

where $`h(x)=-x\log x-(1-x)\log(1-x)`$. This same entropy follows either from the four many-body eigenvalues or from the two occupation eigenvalues.

For $`r`$ normal modes, an occupation margin $`\delta\le\nu_j\le1-\delta`$ bounds every individual occupation away from a pure value. It does **not** give a size-independent lower bound on the many-body density matrix. A product with every occupation equal to a fixed $`\delta<1/2`$ has smallest many-body eigenvalue $`\delta^r`$. Thus a shrinking many-body eigenvalue alone cannot diagnose the missing protection in this project. The relevant stronger condition is a uniform margin for the one-particle occupations.

The entropy function remains continuous at the occupation endpoints, but its derivative does not remain bounded:

```math
h'(x)=\log\frac{1-x}{x},
\qquad
h(x)=x(1-\log x)+O(x^2)
\quad(x\downarrow0).
```

Strict positivity at each finite size supplies no uniform distance from this edge. These finite spectra isolate that distinction; they are not asserted to be the reductions of one common infinite chain, and they do not establish a spatial CMI tail. The actual construction supplies both the compatible infinite state and the noise dynamics.

## 4. Why noise on the buffer can increase CMI

**Connection to the map:** [M07–M09](milestones.md#m07-from-entropy-to-conditional-quantum-correlations). **Wilde:** §§11.6–11.7, 11.9, 12.1, 12.3.

A three-register classical example, embedded as a diagonal quantum state, separates endpoint data processing from noise on the conditioning register. Let $`X`$ be a uniform bit and initially set $`A=B=C=X`$. The joint state is

```math
\rho_{ABC}
=\tfrac12|000\rangle\langle000|
+\tfrac12|111\rangle\langle111|.
```

Knowing $`B`$ already specifies the common bit, so $`I(A:C\mid B)=0`$. Now flip only $`B`$ with probability $`p`$. If $`N`$ is an independent Bernoulli-$`p`$ bit, the output variables are $`A=C=X`$ and $`B=X\mathbin\oplus N`$.

The entropies can be computed directly. The register $`B`$ is still uniform, while the pair $`AB`$ determines both $`X`$ and $`N`$:

| Reduction | Output entropy in nats |
|---|---|
| $`B`$ | $`\log2`$ |
| $`AB`$ or $`BC`$ | $`\log2+h(p)`$ |
| $`ABC`$ | $`\log2+h(p)`$ |

Substitution gives

```math
I(A:C\mid B)=h(p)>0
\qquad(0\lt p\lt1).
```

The quantum channel is the unital bit-flip map

```math
\Lambda_p(\rho)=(1-p)\rho+pX_B\rho X_B,
```

with $`\lVert\Lambda_p-\mathrm{id}\rVert_\diamond=2p`$. The upper bound follows by the triangle inequality, and the input $`|0\rangle`$ attains it. Hence the conditioning operation can be arbitrarily weak. It damages the buffer's record of the common bit while leaving the endpoint correlation present.

This finite example does not have the local-faithfulness or spatial assumptions of the theorem. Its role is to show why the usual data-processing inequality on an **endpoint** does not imply that arbitrary noise on $`B`$ decreases $`I(A:C\mid B)`$. The spatial proof must control how buffers change, rather than invoking such a monotonicity.

Recovery gives another perspective. In a finite tripartite system, zero CMI characterizes an exact quantum Markov condition, and small CMI gives a quantitative approximate-recovery guarantee. The project's algebraic tail still tends to zero with distance. Its conclusion concerns the failure of a uniform **exponential CMI law**; it does not establish the impossibility of every approximate recovery operation. Markov length adds a spatial decay requirement to the finite-system recovery framework.

## 5. What weak local noise means here

**Connection to the map:** [M04–M05](milestones.md#m04-local-noise-environments-and-unital-channels), [M13](milestones.md#m13-local-approximations-and-the-order-of-limits), and [M17](milestones.md#m17-a-strictly-local-weak-unital-noise-circuit). **Wilde:** §§4.4–4.5, 5.2, 9.1.

The physical gate acts on two neighboring fine sites. For each orbital it couples the symmetric bond mode to a fresh maximally mixed ancillary fermion. A unitary acts jointly on bond and ancillas, and the ancillas are discarded. In the familiar finite-dimensional form,

```math
\Phi(\rho)
=\operatorname{Tr}_E\!\left[
V\left(\rho\otimes\frac{I_E}{d_E}\right)V^\dagger
\right].
```

This expression is completely positive and trace preserving. It is unital because the joint input proportional to the identity remains unchanged under unitary conjugation. The project's even fermionic dilation also specifies its action on a bond correlated with the rest of the chain. The [model note](../science/model-and-rank.md#3-the-weak-unital-bond-channel) gives the precise modes and unitary.

The diamond norm compares channels while allowing the input to be entangled with a reference system. Here each bond gate obeys

```math
\lVert\Phi_{x,\epsilon}-\mathrm{id}\rVert_\diamond
\le8\epsilon^2,
\qquad 0<\epsilon<\pi/2.
```

The quadratic bound follows from the dilation: its first-order contribution vanishes when traced against the maximally mixed ancillas, and the second derivative is bounded by a double commutator. The circuit applies all even bonds and then all odd bonds. Its depth is two, its support per gate is fixed, and the ancillas are fresh for every gate.

This weakness statement is local. It bounds a finite-support channel uniformly over its allowed inputs; it does not bound the global diamond distance of a circuit acting across an arbitrarily long chain. The relevant limiting sequence is:

1. Fix a finite observation region and take the ring circumference to infinity, obtaining its infinite-chain reduction.
2. Increase the region and buffer sizes at fixed $`m>1`$ and fixed nonzero $`\epsilon`$.
3. Recognize that the same conclusion is available for arbitrarily small such fixed $`\epsilon`$.

The positive tail coefficient decreases to zero with the noise strength. The theorem does not exchange the large-region and zero-noise limits or provide a uniform crossover size in that joint limit.

## 6. From density matrices to a locally faithful gapped input

**Connection to the map:** [M06](milestones.md#m06-gaussian-occupations-and-many-body-entropy), [M11–M12](milestones.md#m11-gapped-hamiltonians-and-occupied-band-projectors), and [M15–M16](milestones.md#m15-the-concrete-gapped-input-and-its-two-spatial-scales). **Wilde:** §§3.3, 4.1, 11.1 supply the finite-dimensional spectral language; the Gaussian and band arguments are supplied in the project.

A gauge-invariant Gaussian state is determined by its one-particle covariance. On a finite region with occupation eigenvalues $`\nu_1,\ldots,\nu_r`$, a change to normal modes gives

```math
\rho_R\simeq
\bigotimes_{j=1}^r
\left[(1-\nu_j)|0\rangle\langle0|
+\nu_j|1\rangle\langle1|\right].
```

The symbol $`\simeq`$ means unitary equivalence within that finite region. Therefore

```math
S(\rho_R)=\sum_{j=1}^r h(\nu_j),
\qquad
\rho_R>0\ \Longleftrightarrow\ 0\lt C_R\lt I.
```

The input fills the negative-energy band of two identical interleaved SSH chains. For one chain the Bloch Hamiltonian and its positive energy are

```math
h_m(k)=
\begin{pmatrix}0&m+e^{ik}\\m+e^{-ik}&0\end{pmatrix},
\qquad
E_m(k)=|m+e^{ik}|.
```

For $`m>1`$, $`E_m(k)\ge m-1`$. Filling the negative band gives the projector

```math
P_m(k)=\frac12\left(I-\frac{h_m(k)}{E_m(k)}\right).
```

The global covariance is a projector, as expected for a pure Gaussian state. A finite compression of a projector need not be a projector: the region excludes the tails of its occupied and empty modes. The Hamiltonian's energy gap is thus a different condition from an occupation margin of a covariance compression.

The rank proof asks whether a finite compression could nevertheless have an eigenvalue exactly zero or one. Such an eigenvalue would produce a nonzero **compactly supported** vector in the global empty or occupied band. Its Fourier components would be Laurent polynomials. The band equation would then express $`E_m(z)`$ as a rational function, with $`z=e^{ik}`$. But

```math
E_m(z)^2=(m+z)(m+z^{-1})
```

has simple zeros at $`-m`$ and $`-1/m`$, whereas the square of a rational function has even order at every zero and pole. This contradiction excludes both occupation endpoints on every finite mode set. [Proposition 1 of the model note](../science/model-and-rank.md#proposition-1-local-faithfulness-of-the-input) supplies the full argument, including disconnected sets.

The distinction from exponentially localized modes is essential. Exponential tails can be very small without vanishing. Truncating a localized occupied or empty mode produces finite-region occupations extremely close to one or zero, while the argument above prevents equality at any finite size.

## 7. The dressing identity and its locality content

**Connection to the map:** [M18–M20](milestones.md#m18-the-tensor-identity-that-preserves-the-solvable-reference). **Wilde:** §§3.3, 3.5, 4.4, 11.7, 11.10; the exact dressing and locality bounds are project-specific.

The construction begins from a simple onsite product state with one orbital combination occupied and its orthogonal combination empty. A momentum-dependent orbital rotation $`u_m(k)`$ turns its constant projector $`P_{\mathrm{prod}}`$ into $`P_m(k)`$:

```math
P_m(k)=u_m(k)P_{\mathrm{prod}}u_m(k)^\dagger.
```

The chosen rotation is analytic in a strip around real momentum. Its Fourier coefficients, and the hoppings of an explicit generator, decay exponentially. Denote the resulting fixed-time evolution by $`\mathcal U_m`$.

There are two separate internal indices. The noise mixes the parity/subcell index $`p`$ and treats both orbitals $`a`$ identically. Its matrices have the form $`X_\epsilon(k)\otimes I_a`$ and $`Q_\epsilon(k)\otimes I_a`$. The dressing has the form $`I_p\otimes u_m(k)`$. These matrices commute because they act on different tensor factors. Gaussianity turns the resulting covariance identities into the exact state identities

```math
\omega_m=\mathcal U_m(\omega_{\mathrm{prod}}),
\qquad
\rho_{m,\epsilon}=\mathcal U_m(\tau_\epsilon),
```

where $`\tau_\epsilon=\mathcal E_\epsilon(\omega_{\mathrm{prod}})`$ is the solvable noisy reference. The physical noise is still the original nearest-neighbor circuit. It has not acquired the dressing's exponentially decaying range.

Output faithfulness follows from a second useful identity. Writing the one-particle channel as $`C\mapsto\mathsf X C\mathsf X^\dagger+\mathsf Y`$, one has $`\mathsf Y\ge0`$ and the same noise term for $`I-C`$. The matrix $`\mathsf X`$ is invertible and has finite propagation range in the specified angle interval. Thus $`\mathsf X^\dagger`$ maps a nonzero compactly supported test vector to another such vector. Input strict positivity then proves strict positivity of both output quadratic forms. This is [Proposition 2](../science/model-and-rank.md#proposition-2-local-faithfulness-after-the-channel).

The dressing identities do not make regional CMI invariant by themselves. A unitary crossing a region boundary can change its entropy. Locality is the ingredient that controls this change. For the input, the dressing of a product state can be approximated near the shielding boundaries; the reference has zero CMI on the appropriate enlarged partition, and entropy continuity bounds the remaining error exponentially. The proof is in [initial exponential CMI](../science/locality-and-cmi.md#initial-exponential-cmi).

## 8. The entropy correction that survives in CMI

**Connection to the map:** [M21–M23](milestones.md#m21-the-inherited-dark-mode-and-algebraic-interval-entropy). **Wilde:** §§11.1, 11.7, 11.9–11.10; the scalar asymptotic is a research theorem of [Newsom and Levin](../references/README.md#nl).

The scalar noisy reference has a dark momentum where an occupation vanishes quadratically. Its covariance is analytic, but composing an occupation approaching zero with $`h`$ introduces the nonanalytic behavior $`-x\log x`$. In the two-sector reference used here, the complementary occupation reaches one and has the same entropy. The existence and exact coefficient of the finite-interval correction require an interval-entropy theorem; they do not follow merely by inspecting this singularity.

NL's Appendix E.1, Eq. (132), supplies that theorem. After including the two complementary orbital sectors, it reads

```math
S_{\tau_\epsilon}(n)
=s_\epsilon n+b_\epsilon
-\frac{\kappa_\epsilon}{n^2}+O(n^{-3}),
```

```math
\kappa_\epsilon
=\frac{\sin^2\epsilon}{8(1+\cos^2\epsilon)}\,\zeta(3)>0.
```

Here $`n`$ counts coarse cells, exactly NL's two-site cells. The formula is for the **undressed reference** $`\tau_\epsilon`$.

For three consecutive equal intervals, the definition of CMI gives a useful explicit cancellation:

```math
\begin{aligned}
\mathcal I_{\tau_\epsilon}(L,L,L)
&=2S_{\tau_\epsilon}(2L)
-S_{\tau_\epsilon}(L)-S_{\tau_\epsilon}(3L)\\
&=\frac{\kappa_\epsilon}{L^2}
\left(1+\frac19-\frac12\right)+O(L^{-3})\\
&=\frac{11\kappa_\epsilon}{18L^2}+O(L^{-3}).
\end{aligned}
```

Both the extensive entropy and its constant boundary term disappear. CMI detects the smaller size-dependent correction.

To transfer this coefficient to the actual output, the locality proof approximates $`\mathcal U_m`$ and its inverse by local circuits on the relevant observation windows. Their boundary displacements are $`O(\log L)`$, and their local half trace-distance errors can be made $`O(L^{-8})`$. Conditional-entropy continuity then contributes only $`O(L^{-7})`$: the logarithm of an endpoint Hilbert-space dimension grows linearly in $`L`$.

Strong subadditivity and the chain rule sandwich the dressed CMI between reference CMIs with these slightly shifted endpoints and buffers. Shifting a macroscopic inverse-square term by $`O(\log L)`$ changes it by $`O(\log L/L^3)`$. The forward and inverse comparisons therefore have the same leading coefficient. This proves the **CMI transfer** in [Proposition 4 of the locality note](../science/locality-and-cmi.md#macroscopic-cmi-squeeze), without requiring an individual dressed interval-entropy expansion.

For the fully shielded geometry, take all five blocks to have length $`L`$. An exact entropy identity expresses its CMI as

```math
I_{\rm sh}
=\mathcal I_\rho(L,L,L)
+\mathcal I_\rho(2L,L,2L)-M_2(L)+M_1(L),
```

where $`\mathcal I_\rho`$ denotes one-sided interval CMI and

```math
M_2=I(C_-B_-:B_+C_+),
\qquad M_1=I(B_-:B_+).
```

The separated-block mutual informations are exponentially small. This follows from analytic covariance together with a Gaussian entropy-continuity bound that does not assume an occupation margin. The two one-sided coefficients are $`11\kappa_\epsilon/18`$ and $`184\kappa_\epsilon/225`$, respectively. Consequently,

```math
I_{\rm sh}
=\frac{643\kappa_\epsilon}{450L^2}+o(L^{-2}).
```

All region sizes grow proportionally to $`L`$. A positive inverse-square tail cannot satisfy a bound consisting of any fixed polynomial in these sizes times $`e^{-L/\xi}`$ with finite $`\xi`$. This is the fully shielded infinite-Markov-length conclusion, established in [the central theorem](../science/instability-theorem.md#5-the-exact-fully-shielded-asymptotic).

## 9. Which ingredients the scientific account supplies

The [background synthesis M14](milestones.md#m14-background-synthesis-the-stability-question-as-a-complete-statement) joins the textbook concepts into the assumptions of a precise problem. The subsequent milestones depend on additional results with their own hypotheses. Their roles can be located directly:

| Ingredient | Textbook foundation | Additional result and authoritative location |
|---|---|---|
| Finite states, channels, entropy and operational distance | Wilde Chapters 4–5, §9.1, Chapter 11 | Model-specific sites, ancillas, normalization and local channel bound in [Model and local rank](../science/model-and-rank.md) |
| Fermionic Gaussian reductions | Finite spectra and reduced states | CAR conventions and covariance entropy formula in the model/locality notes; [Gaussian primary references](../references/README.md#gaussian-reductions) |
| Faithfulness on every finite set | Strict positivity and support | The compact-band-vector obstruction and the finite-propagation output argument in the two model propositions |
| Exponential initial CMI and controlled dressing | Strong subadditivity and entropy continuity | [Locality and CMI](../science/locality-and-cmi.md), including exponential interaction bounds, finite-window circuits and the forward/inverse comparison; primary locality sources are identified there |
| The reference inverse-square entropy correction | Entropy as a function of eigenvalues | NL's scalar interval theorem, with exact normalization in [the inherited entropy section](../science/instability-theorem.md#3-the-inherited-single-orbital-entropy-theorem) |
| Fully shielded asymptotics | CMI identities and ordinary MI | The five-block identity and the separated-block Gaussian estimate in [the theorem](../science/instability-theorem.md#5-the-exact-fully-shielded-asymptotic) |
| Other realizations | Composite systems and channels | The [ordinary-spin lift](../science/spin-realization.md) and [continuous-time companion](../science/continuous-time.md), with their distinct input and locality assumptions |

These links are proof dependencies, not additional educational anchors. In particular, Wilde is not being used as a source for fermionic Toeplitz asymptotics, a general theorem about gapped-state Markov length, or a Jordan–Wigner equivalence for disconnected regions.

## 10. Connecting the realizations and the scope

**Connection to the map:** [M24–M27](milestones.md#m24-lifting-the-local-gates-to-ordinary-spins) and [M28–M30](milestones.md#m28-qualitative-rank-versus-a-uniform-occupation-margin).

The ordinary-spin realization attaches tracial auxiliary degrees of freedom and implements the required gates by strictly local Pauli operators. Its finite reductions are faithful and its shielded coefficient is the same as in the finite-depth fermionic theorem. Its input is globally mixed. Disconnected spin regions are treated by ordinary tensor-factor locality, rather than by importing a disconnected fermionic entropy identity.

The continuous-time realization uses one SSH chain with two modes per site and balanced gain/loss jumps proportional to $`c_j-c_{j+1}`$. Its covariance is

```math
C_t(k)=\frac I2+e^{-t(2-2\cos k)}
\left(P_m(k)-\frac I2\right).
```

The evolution is defined by local thermodynamic limits of even finite-volume states. For every fixed finite $`t>0`$, its output is locally faithful and has shielded CMI

```math
I_{\rm sh}^{\rm ct}
=\frac{643t\zeta(3)}{900L^2}+o(L^{-2}),
```

where $`L`$ now counts the two-mode sites of that model. The time normalization and site conversion are checked explicitly in [the continuous-time proof](../science/continuous-time.md#imported-scalar-entropy-and-its-normalization).

Across these realizations, the result concerns a qualitative hypothesis: every finite reduction has full support. It does not establish instability under a generic open set of noise parameters or for positive-temperature Gibbs inputs. The retained dark mode is a tuned feature of the noise. In the same Gaussian model, a fixed finite nonnegative inverse temperature gives an occupation margin away from zero and one, removing the edge singularity used by this construction; that observation alone is not a general finite-temperature stability theorem.

The final synthesis is the conjunction of the proved properties. An energy gap and full support of every finite local density matrix coexist with an occupation spectrum that approaches pure-mode edges on growing regions. The compatible weak local channel retains a known entropy singularity, and the locality argument carries its conditional-information coefficient to the faithful correlated output. The exact shielding identity turns that coefficient into the stated limitation of local rank as a stability criterion.
