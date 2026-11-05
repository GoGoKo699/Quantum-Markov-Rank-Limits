# Ordinary-spin realization with locally faithful input

## Statement and scope

The four-mode fermionic construction has an ordinary-spin realization with
the same instability and with every finite input and output density matrix
strictly positive. The spin input is **globally mixed**. It has finite
Markov length because it is obtained from a product mixed state by a
fixed-time evolution with exponentially decaying interactions.

There are four qubits per fine site, or eight qubits per two-site coarse
cell. For every fixed $`m>1`$ and $`0<\epsilon<\pi/2`$, the noise is a
depth-two circuit of unital channels supported within neighboring fine
sites. Each such gate obeys

```math

\|\widetilde{\mathcal G}_{j,\epsilon}-\mathrm{id}\|_\diamond
\le 8\sin^2(\epsilon/2)\le 8\epsilon^2.
\qquad\text{(S1)}
```

The output has infinite Markov length in the two-sided shielding geometry.
In fact, for five consecutive equal coarse blocks
$`C_L,B_L,A,B_R,C_R`$, each of length $`n`$, its shielded CMI obeys

```math

\begin{gathered}
I_{\sigma_\epsilon}(A:C_LC_R\mid B_LB_R)
=\frac{643}{450}\,\kappa_\epsilon n^{-2}+o(n^{-2}),
\\

\kappa_\epsilon=\gamma_\epsilon\zeta(3),\\

\gamma_\epsilon=\frac{\sin^2\epsilon}{8(1+\cos^2\epsilon)}.
\end{gathered}
\qquad\text{(S2)}
```

The derivation below separates the strictly local spin construction, the
basic algebraic obstruction, and the stronger coefficient statement. No
identity for disconnected spin and fermion marginals is used.

The auxiliary-Majorana embedding is inherited from
Negari--Zou--Hsieh [2, Sec. II B and Supplemental Sec. SIII]. We adapt it to
the random-unitary factors of the finite-depth Newsom--Levin circuit
[1, Appendix G]. The local-faithfulness construction and its application
to this spin circuit are the additional ingredients.

The physical state and channel conventions are specified in
[the model and rank proof](model-and-rank.md). The shared unitary locality
and CMI estimates are proved in
[the locality note](locality-and-cmi.md).

## 1. Physical modes, auxiliaries, and the embedding

Let $`j\in\mathbb Z`$ label fine sites, each containing physical fermions
$`c_{j,0},c_{j,1}`$. Add an auxiliary fermion $`g_{j,a}`$ for every physical
mode. The orbital labels $`0,1`$ here are a relabeling of $`1,2`$ in the
model note. All these are CAR modes, including anticommutation between physical
and auxiliary operators. Write

```math

\eta_{j,a}=g_{j,a}+g_{j,a}^\dagger,\qquad \eta_{j,a}^2=I.
```

On a finite set with $`N_{\rm p}`$ physical modes, an even physical density
operator is an even polynomial $`r(c,c^\dagger)`$, normalized in the
physical Hilbert space. Its normalized embedding in the enlarged CAR
algebra is

```math

\mathfrak E(r)=2^{-N_{\rm p}}r(c,c^\dagger).
\qquad\text{(S3)}
```

This is the physical state with tracial auxiliary modes. Reordering all
physical modes before the auxiliary modes by a finite fermionic mode
permutation identifies its spectrum with that of
$`r\otimes I_{\rm aux}/2^{N_{\rm p}}`$. This is a spectral identification;
after an interleaved Jordan--Wigner transformation it need not be a tensor
product between the subsets of physical and auxiliary *spins*.

The infinite-chain embedding is defined by consistent finite CAR
restrictions. Equivalently, use finite open chains and their local
thermodynamic limits. All states and dynamics below are even, so odd
total-parity observables have zero expectation. This specifies their
ordinary-spin states as well.

## 2. Exact lift of each random-unitary gate

For one orbital flavor on a fine bond, define

```math

\begin{gathered}
s_{j,a}=\frac{c_{j,a}+c_{j+1,a}}{\sqrt2},\\

\Gamma^x_{j,a}=s_{j,a}+s_{j,a}^\dagger,\\

\Gamma^y_{j,a}=i(s_{j,a}^\dagger-s_{j,a}).
\end{gathered}
```

Both $`\Gamma^x,\Gamma^y`$ are odd Hermitian unitaries. With
$`p=\sin^2(\epsilon/2)`$, the NL gate agrees on even physical density
operators with the following map [1, Proposition 7]:

```math

\mathcal E_{j,a}
=\bigl[(1-p)\mathrm{id}+p\,\mathrm{Ad}_{\Gamma^y_{j,a}}\bigr]
 \bigl[(1-p)\mathrm{id}+p\,\mathrm{Ad}_{\Gamma^x_{j,a}}\bigr].
\qquad\text{(S4)}
```

Replace each odd unitary by

```math

\widetilde\Gamma^\alpha_{j,a}
=i\eta_{j,a}\Gamma^\alpha_{j,a},
\qquad \alpha=x,y.
\qquad\text{(S5)}
```

These operators are even, Hermitian, and square to $`I`$. If $`r`$ is an
even physical polynomial, $`\eta_{j,a}`$ commutes with $`r`$ and
anticommutes with $`\Gamma^\alpha_{j,a}`$. Therefore

```math

\widetilde\Gamma^\alpha_{j,a}\,
\mathfrak E(r)\,\widetilde\Gamma^\alpha_{j,a}
=\mathfrak E(\Gamma^\alpha_{j,a}r\Gamma^\alpha_{j,a}).
\qquad\text{(S6)}
```

Replacing the conjugations in (S4) by these even conjugations consequently
gives an exact channel lift:

```math

\widetilde{\mathcal E}_{j,a}\circ\mathfrak E
=\mathfrak E\circ\mathcal E_{j,a}.
\qquad\text{(S7)}
```

The output remains an even physical polynomial with tracial auxiliaries,
so the identity can be iterated through every gate and both circuit
layers. It applies to correlated even physical input states. It is not
restricted to the vacuum or to a Lindblad infinitesimal.

The odd-Majorana formula is used only on the even physical density
operators in (S6)--(S7). A dilation extended to arbitrary parity-odd
physical operators can carry parity factors; no arbitrary-state
fermionic-channel equality or diamond-norm bound is inferred from dropping
those factors. In contrast, the spin channel is defined directly by the
Pauli unitaries (S9).

This lift is random unitary and hence unital on the entire spin Hilbert
space, not merely on the embedded states. The identity branch has weight
$`(1-p)^2`$, yielding

```math

\|\widetilde{\mathcal E}_{j,a}-\mathrm{id}\|_\diamond
\le2[1-(1-p)^2]\le4p.
\qquad\text{(S8)}
```

Compose the two orbital gates into
$`\widetilde{\mathcal G}_{j} =\widetilde{\mathcal E}_{j,1}\widetilde{\mathcal E}_{j,0}`$.
Contractivity and a telescoping bound give (S1).

## 3. Jordan--Wigner locality and depth

Order the modes at each fine site as

```math

(c_{j,0},g_{j,0},c_{j,1},g_{j,1}),
```

and order fine sites along the chain. Every term in (S5) is an even
bilinear supported on the physical bond and the auxiliary at its left
endpoint. Its Jordan--Wigner image has no string outside that bond's two
fine sites.

The locality can also be read from explicit Pauli operators. Let
$`r=4j+2a`$ be the qubit position of $`c_{j,a}`$, so its auxiliary is at
$`r+1`$ and $`c_{j+1,a}`$ is at $`r+4`$. In the convention
$`c=(\mu^x+i\mu^y)/2`$, the lifted operators are

```math

\begin{aligned}
\widetilde\Gamma^x_{j,a}
&=\frac{-Y_rX_{r+1}
 +Y_{r+1}Z_{r+2}Z_{r+3}X_{r+4}}{\sqrt2},\\
\widetilde\Gamma^y_{j,a}
&=\frac{X_rX_{r+1}
 +Y_{r+1}Z_{r+2}Z_{r+3}Y_{r+4}}{\sqrt2}.
\end{aligned}
\qquad\text{(S9)}
```

Within each line the two Pauli terms anticommute, so the normalized sum
is a Hermitian unitary, as also follows from (S5). Both flavors together
act within the eight qubits of fine sites $`j,j+1`$. The even-bond gates
have disjoint spin supports, as do the odd-bond gates. Applying all even
bonds and then all odd bonds is thus a literal depth-two local spin
circuit. Blocking four qubits into a fine site only makes this support
statement more compact; no nonlocal operation is hidden in the blocking.

Only the infinite line and finite open chains are used here. No local-spin
identification of a fermionic closing bond on a ring is assumed.

## 4. The dressed input and exact output identity

Group fine sites $`2x,2x+1`$ into a coarse cell. Its physical covariance
has parity/subcell and orbital tensor factors. Let

```math

\begin{gathered}
P_m(k)=\frac12
\begin{pmatrix}1&-f_m(k)\\-\overline{f_m(k)}&1\end{pmatrix},
\\
 f_m(k)=\frac{m+e^{ik}}{|m+e^{ik}|},\\
 m>1.
\end{gathered}
```

The physical input is the pure Gaussian state with covariance
$`I_{\rm parity}\otimes P_m(k)`$. Its local faithfulness is established
by the no-compact-band-vector argument: a finite covariance eigenvalue
zero or one would force $`f_m(z)`$ to be rational, whereas

```math

f_m(z)^2=\frac{z(m+z)}{mz+1}
```

has odd-order zeros and poles. This argument applies to either parity
chain and hence to their product.

Choose the fixed projector $`P_0=\mathrm{diag}(1,0)`$, and set

```math

\begin{gathered}
W=\frac1{\sqrt2}\begin{pmatrix}-1&1\\1&1\end{pmatrix},
\\
 D_m(k)=\mathrm{diag}(f_m(k),1),
\\
 U_m(k)=D_m(k)W.
\end{gathered}
```

Then $`P_m=U_mP_0U_m^\dagger`$. The undressed physical state has orbital
0 filled and orbital 1 empty at every fine site. After adding tracial
auxiliaries it is a tensor product spin state, denoted $`\tau_0`$.

The physical dressing is even and number conserving. Its
Jordan--Wigner image gives a spin automorphism $`\mathcal U_m`$.
The spin input and the undressed noisy spin state are

```math

\sigma_0=\mathcal U_m(\tau_0),\qquad
\tau_\epsilon=\widetilde\Phi_\epsilon(\tau_0),
```

where $`\widetilde\Phi_\epsilon`$ is the depth-two circuit above.

For completeness, the Gaussian covariance identity underlying the
construction is exact. If $`M(k)=X_1(k)X_0(k)`$ is the NL two-layer
single-particle matrix and $`C_{\rm NL}=(I-MM^\dagger)/2`$, then the
orbital-isotropic layers give

```math

C_{\rm out}
=C_{\rm NL}\otimes(I-P_m)+(I-C_{\rm NL})\otimes P_m.
\qquad\text{(S10)}
```

Thus the dressed and undressed physical Gaussian outputs are related by
$`I\otimes U_m(k)`$. Gaussianity, (S7), and compatibility of the
embedding with even physical unitaries imply the spin-state identity

```math

\sigma_\epsilon
\equiv\widetilde\Phi_\epsilon(\sigma_0)
=\mathcal U_m(\tau_\epsilon).
\qquad\text{(S11)}
```

This does not assert that the lifted channel commutes with
$`\mathcal U_m`$ on arbitrary spin inputs. The exact identity on the
specified Gaussian embedded states is all that is needed.

### Exponential locality of the spin dressing

The phase $`f_m(k)=e^{i\theta_m(k)}`$ has zero winding and a periodic
analytic logarithm. Explicitly,

```math

\theta_m(k)
=\sum_{r\ge1}\frac{(-1)^{r+1}}{r\,m^r}\sin(rk).
\qquad\text{(S12)}
```

The diagonal unitary $`D_m`$ is generated in fixed time by physical
quadratic hopping whose distance-$`r`$ coefficients are bounded by
$`C m^{-r}/r`$. The onsite rotation $`W`$ requires only an onsite
quadratic generator. Jordan--Wigner transforms a distance-$`r`$ hopping
into a bounded Pauli string on its intervening interval, preserving the
coefficient norm. Consequently the spin interaction has a finite
exponentially weighted interaction norm after decreasing the decay
exponent to absorb interval-length factors. The evolution and its
inverse therefore admit the finite-window circuit approximations used
below. A global unitary on a particular infinite Fock representation is
not needed.

## 5. Faithfulness of spin reductions

For any complete contiguous interval $`R`$ containing $`N_{\rm p}(R)`$
physical modes and their auxiliaries, even parity cancels the
Jordan--Wigner string to the left of $`R`$. The reduced spin spectrum is

```math

\mathrm{spec}(\sigma_R)
=\left\{2^{-N_{\rm p}(R)}\lambda:
\lambda\in\mathrm{spec}(\rho^{\rm phys}_R)\right\},
\qquad\text{(S13)}
```

with each eigenvalue repeated $`2^{N_{\rm p}(R)}`$ times. One way to see
this is to reorder the physical and auxiliary modes *inside the
interval* and use (S3). This also gives

```math

S_{\rm spin}(R)
=S_{\rm phys}(R)+N_{\rm p}(R)\log2.
\qquad\text{(S14)}
```

Since every finite physical input density operator is positive definite,
(S13) proves faithfulness on every complete spin interval. Any finite
set of qubits lies in such an interval, and a partial trace of a
positive-definite density matrix is positive definite. Therefore
**every finite spin input marginal is full rank**, including disconnected
sets and sets that do not contain complete cells.

Faithfulness persists after the spin circuit. For a finite output set
$`R`$, let $`R^+`$ be its finite backward light cone. The input obeys
$`\sigma_{0,R^+}\ge\lambda I_{R^+}`$ for some $`\lambda>0`$.
Run the relevant local unital circuit on this light cone and trace the
extra modes. Positivity gives a strictly positive multiple of $`I_R`$
as a lower bound on the output. The bound may depend on $`R`$; no
uniform spectral margin is asserted.

Equation (S13) is **not** asserted for an arbitrary disconnected spin
region. Faithfulness for disconnected sets follows by reduction of an
enclosing faithful interval, not by identifying their fermion and spin
spectra.

## 6. Initial finite Markov length and shielded CMI transfer

The shielding geometry is $`C_LB_LAB_RC_R`$, with
$`B=B_L\cup B_R`$ and $`C=C_L\cup C_R`$.
For the input we establish the stronger shielding estimate in
[Proposition 1 of the locality note](locality-and-cmi.md#initial-exponential-cmi):
the exponential bound has a polynomial prefactor in $`|A|,|B|`$ that is
independent of the size of the exterior $`C`$.

The circuit comparison, also proved as
[Lemma 2 of the locality note](locality-and-cmi.md#circuit-cmi-comparison),
has the following elementary extension
to this geometry. For a depth-$`D`$ unitary circuit whose interval gates
have width at most $`r`$, assume both buffers are wider than $`2Dr`$.
Absorb, layer by layer backwards, complete gate blocks touching $`A`$
or $`C`$ into those endpoint registers. Each buffer loses at most
$`2Dr`$ sites, and each boundary moves by at most $`Dr`$. Denote the
resulting sets by $`A',B',C'`$. Then for every global state $`\rho`$,

```math

I_{V\rho V^\dagger}(A:C\mid B)
\le I_\rho(A':C'\mid B').
\qquad\text{(S15)}
```

The proof does not require connected registers. Adding exterior
registers to $`A,C`$ uses data processing; moving strips $`a,c`$ from
the buffer into the endpoints uses

```math

I(A:C\mid aB'c)\le I(Aa:Cc\mid B').
\qquad\text{(S16)}
```

The difference is a sum of nonnegative CMIs by the chain rule. The
enlarged cuts lie at the actual layer's block boundaries, so that layer
then factors into unitaries on $`A',B',C'`$ and the exterior. CMI is
invariant under these separate unitaries. This proves (S15) one layer
at a time; no uncorrelated-exterior assumption is made.

For the fixed-time exponentially local dressing, finite-window
Lieb--Robinson locality and the boundary-patching construction give a
constant-depth interval circuit $`V_\ell`$, with gate width
$`O(\ell)`$, such that on a window $`R`$

```math

\tfrac12\|[\mathcal U_m(\rho)]_R
 -(V_\ell\rho V_\ell^\dagger)_R\|_1
\le C(|R|+\ell)e^{-c\ell}.
\qquad\text{(S17)}
```

The same bound holds for the inverse dressing and uniformly over
global input states; see
[Lemma 3 of the locality note](locality-and-cmi.md#local-circuit-approximation)
for the full construction. This is the exponentially decaying-interaction
version of the finite-window argument, using [3,4]; the extension is
obtained by summing the exponentially small cross-cut tails before
performing the disjoint boundary patches. It does not follow by
treating a large global error as a local trace estimate.

For trace distance $`\delta=\tfrac12\|\rho-\omega\|_1`$, the conditional
entropy continuity bound [5] applied twice gives

```math

\begin{gathered}
|I_\rho(A:C\mid B)-I_\omega(A:C\mid B)|
\le4\delta\log d_{\min}+2g(\delta),
\\

g(\delta)=(1+\delta)h_2\!\left(\frac{\delta}{1+\delta}\right).
\end{gathered}
\qquad\text{(S18)}
```

Here $`d_{\min}=\min(\dim A,\dim C)`$, and logarithms are natural.

For $`\sigma_0=\mathcal U_m(\tau_0)`$, absorb the onsite $`W`$ rotation
into the product mixed input and apply the fixed-time exponential
evolution implementing $`D_m`$. All assumptions of Proposition 1 in the
locality note hold by (S12). Its factorization around the two shielding
buffers, followed by (S18), gives constants $`C,a>0`$ and an integer $`q`$
such that

```math

\begin{gathered}
I_{\sigma_0}(A:C\mid B)
\le C(1+|A|)(1+|B|)^q e^{-a b},
\\
 b=\min(|B_L|,|B_R|).
\end{gathered}
\qquad\text{(S18a)}
```

The proof permits mixed product input and is uniform in the finite
exterior $`C`$. Taking its increasing-exterior limit therefore gives the
same bound when $`C`$ is the entire exterior. This establishes initial
finite Markov length without an exterior-volume prefactor.

Conversely, an algebraic shielded CMI witness of polynomial total size
for $`\tau_\epsilon`$ transfers through the inverse dressing using
$`\ell=L_0\log n`$. Its boundaries move by $`O(\log n)`$, its buffers
remain $`n-O(\log n)`$, and the continuity error can be made
$`o(n^{-2})`$. Therefore such a witness rules out finite Markov length
for $`\sigma_\epsilon`$.

## 7. A two-sided lower bound using only interval entropies

The undressed spin state $`\tau_\epsilon`$ is the output of a
depth-two local spin channel on a product state. Output regions with
disjoint backward light cones factor exactly. For the five equal
coarse blocks $`C_LB_LAB_RC_R`$, take $`n`$ larger than the fixed
circuit range. Then

```math

\begin{gathered}
(\tau_\epsilon)_{B_LB_RC_R}
=(\tau_\epsilon)_{B_L}\otimes
  (\tau_\epsilon)_{B_RC_R},
\\
 I_{\tau_\epsilon}(B_L:C_R\mid B_R)=0.
\end{gathered}
\qquad\text{(S19)}
```

The chain rule and nonnegativity now give

```math

\begin{aligned}
I_{\tau_\epsilon}(A:C_LC_R\mid B_LB_R)
&\ge I_{\tau_\epsilon}(A:C_R\mid B_LB_R)\\
&=I_{\tau_\epsilon}(AB_L:C_R\mid B_R).
\end{aligned}
\qquad\text{(S20)}
```

The last CMI uses four *contiguous* intervals, of lengths $`3n,2n,n,4n`$.
If $`S_{\rm NL}(L)`$ is the interval entropy of the original NL
vacuum-output chain, then in complete coarse cells

```math

S_{\tau_\epsilon}(L)=2S_{\rm NL}(L)+4L\log2.
\qquad\text{(S21)}
```

The first term contains the independent empty and filled orbital
copies. The second term counts four auxiliary modes per coarse cell.
It follows from (S14) and cancels in the CMI.

Using the inherited interval asymptotic [1, Eq. (15), Appendix E]

```math

S_{\rm NL}(L)
=sL+s_0-\frac{\gamma_\epsilon\zeta(3)}{2L^2}
 +O(L^{-3}),
\qquad\text{(S22)}
```

equation (S20) yields

```math

I_{\tau_\epsilon}(A:C_LC_R\mid B_LB_R)
\ge \frac{101}{144}\,\kappa_\epsilon n^{-2}
 +O(n^{-3}).
\qquad\text{(S23)}
```

Indeed, the geometric coefficient is
$`1+1/16-1/9-1/4=101/144`$.
For every fixed $`\epsilon>0`$ this gives a positive algebraic lower
bound for sufficiently large $`n`$. Section 6 transfers the obstruction
to the dressed spin output. This already proves the claimed instability.

## 8. The exact five-block coefficient

The sharper result (S2) can be obtained without assuming that dressing
preserves an individual interval entropy correction.

First, the gate-block comparison and its inverse give the macroscopic
one-sided CMI squeeze proved in
[Proposition 4 of the locality note](locality-and-cmi.md#macroscopic-cmi-squeeze):
if the three interval lengths are
$`(an,bn,cn)`$, then endpoint changes of $`O(\log n)`$ sandwich the
dressed CMI between corresponding undressed CMIs, with error
$`o(n^{-2})`$. Equation (S22) is uniform under these boundary changes.
Consequently,

```math

\begin{aligned}
&I_{\sigma_\epsilon}(an:cn\mid bn)\\
&=\kappa_\epsilon
\left[b^{-2}+(a+b+c)^{-2}-(a+b)^{-2}-(b+c)^{-2}\right]n^{-2}
 +o(n^{-2}).
\end{aligned}
\qquad\text{(S24)}
```

Second, ordinary mutual information of separated macroscopic intervals
in $`\sigma_\epsilon`$ is exponentially small. To prove this, use
(S17) with $`\ell`$ a small fixed fraction of their separation. The
approximating unitary circuit, composed with the fixed-depth channel
preparing $`\tau_\epsilon`$, has disjoint past cones for the two
intervals and hence a product marginal there. Its trace-distance error
is exponentially small with a polynomial volume factor. Entropy
continuity then bounds the mutual information by the same type of
exponential estimate. This uses the ordinary spin tensor factors
throughout.

For the five equal blocks, write $`S_\sigma(kn)`$ for the entropy of
a contiguous $`kn`$-cell interval. Exact spin entropy identities give

```math

\begin{aligned}
&I_{\sigma_\epsilon}(A:C_LC_R\mid B_LB_R)\\
&={}S_\sigma(3n)+2S_\sigma(2n)-2S_\sigma(n)-S_\sigma(5n)\\
&\quad+I_{\sigma_\epsilon}(B_L:B_R)
 -I_{\sigma_\epsilon}(C_LB_L:B_RC_R).
\end{aligned}
\qquad\text{(S25)}
```

Both ordinary MI terms have separation $`n`$, so they are exponentially
small. The contiguous entropy combination is exactly the sum of
one-sided CMIs with length ratios $`(2,1,2)`$ and $`(1,1,1)`$.
Applying (S24) gives

```math

\begin{aligned}
I_{\sigma_\epsilon}(A:C_LC_R\mid B_LB_R)
&=\kappa_\epsilon
\left[
 1+\frac1{25}-\frac2{9}
 +1+\frac1{9}-\frac12
\right]n^{-2}+o(n^{-2})\\
&=\frac{643}{450}\kappa_\epsilon n^{-2}+o(n^{-2}),
\end{aligned}
```

which proves (S2). The disconnected entropies in (S25) were rewritten
using *spin* mutual information, not replaced by disconnected fermionic
entropies.

## 9. Ground-state language and limitations

The physical fermionic input is a pure gapped ground state. The spin
input here has tracial auxiliaries and is globally mixed. It should
not be described as a unique pure spin ground state.

A precise finite-volume ground-space statement is available on open
chains. Add zero-energy auxiliary modes to the physical SSH Hamiltonian
and apply the interleaved Jordan--Wigner transformation. Each physical
quadratic term has finite spatial range, so its spin image also has
finite range. The finite-dimensional transformation preserves the
spectrum, while adding $`N_{\rm p}`$ zero-energy auxiliary modes
replicates it $`2^{N_{\rm p}}`$ times. For the trivial SSH termination
with $`m>1`$, the one-particle gap is at least $`m-1`$, since the
off-diagonal block is $`mI+T`$ with $`\|T\|\le1`$. The normalized
ground-space projector is the embedded physical ground state with
tracial auxiliaries. Its local thermodynamic limit is the spin input
used above. The extensive auxiliary degeneracy is part of this
statement.

Local full rank is asserted for each finite region of the
infinite-chain state. No uniform lower bound on the smallest
eigenvalues as regions grow is implied. The result is not a
finite-temperature Gibbs-state instability theorem, and the noise
retains the inherited dark-mode fine tuning.

## Primary references

1. D. C. Newsom and M. Levin, *An Instability of the Quantum Markov Length*,
   [arXiv:2610.12929v3](https://arxiv.org/html/2610.12929v3), especially
   Eqs. (9)--(16), Appendix E, and Appendix G. The scalar noise model,
   its algebraic interval entropy, and the random-unitary representation
   are inherited results.
2. A.-R. Negari, Y. Zou, and T. H. Hsieh, *Instability of Markov chains
   under infinitesimal coherent dissipation*,
   [arXiv:2610.18983v1](https://arxiv.org/pdf/2610.18983v1), Sec. II B and
   Supplemental Sec. SIII. The tracial-auxiliary Majorana embedding,
   its exact evolution identity, and its interval spectral identity
   are inherited; (S4)--(S9) give the finite-depth random-unitary
   specialization used here.
3. T. J. Osborne, *The Dynamics of 1D Quantum Spin Systems Can Be
   Approximated Efficiently*, Phys. Rev. Lett. **97**, 157202 (2006),
   [arXiv:quant-ph/0508031v2](https://arxiv.org/abs/quant-ph/0508031v2).
   The boundary-patching mechanism is the relevant ingredient; the
   exponentially decaying-interaction extension requires the tail
   estimates stated in Section 6.
4. B. Nachtergaele and R. Sims, *Lieb--Robinson Bounds and the
   Exponential Clustering Theorem*, Commun. Math. Phys. **265**,
   119--130 (2006),
   [arXiv:math-ph/0506030v3](https://arxiv.org/abs/math-ph/0506030v3).
5. A. Winter, *Tight uniform continuity bounds for quantum entropies:
   conditional entropy, relative entropy distance and energy
   constraints*, Commun. Math. Phys. **347**, 291--313 (2016),
   [arXiv:1507.07775v6](https://arxiv.org/abs/1507.07775v6).
