# What local full rank does and does not control

The [instability theorem](instability-theorem.md) separates two questions. A finite reduced density matrix can be strictly positive, so that no nonzero local measurement effect is exactly forbidden, while its small eigenvalues approach zero rapidly as the region grows. The distinction matters because the von Neumann entropy is not analytic at zero occupation.

## Qualitative faithfulness and nearly pure modes

For the input state, every finite covariance compression has spectrum in $(0,1)$; this is proved in [Model and local rank](model-and-rank.md). Nevertheless, the full one-particle covariance is a projector. Its occupied and empty subspaces contain exponentially localized Wannier modes, although neither contains a nonzero compactly supported mode.

Here is a quantitative form of this difference. Let $P$ denote the occupied projector of one SSH copy. Choose a normalized occupied Wannier vector $v$ centered at the origin. For every fixed $0<\mu<\log m$, the analytic dressing gives

$$
\|(1-Q_r)v\|^2\leq C_\mu e^{-2\mu r},
$$

where $Q_r$ projects onto the cells from $-r$ to $r$. Put $w_r=Q_rv/\|Q_rv\|$. Since $Pv=v$,

$$
1-\langle w_r,Pw_r\rangle
=\|(1-P)w_r\|^2
\leq
\frac{\|(1-Q_r)v\|^2}{\|Q_rv\|^2}.
$$

For sufficiently large $r$, the denominator is bounded below by a positive constant. The variational principle therefore gives

$$
1-\lambda_{\max}(Q_rPQ_r)
\leq C'_\mu e^{-2\mu r}.
$$

The same argument with an empty Wannier vector gives

$$
\lambda_{\min}(Q_rPQ_r)
\leq C'_\mu e^{-2\mu r}.
$$

These eigenvalues remain strictly between zero and one at every finite $r$. Local faithfulness is thus compatible with arbitrarily accurate finite-region approximations to pure modes. A uniform covariance margin $\delta I\leq C\leq(1-\delta)I$, with $\delta>0$, would be a substantially stronger hypothesis.

This covariance margin should not be confused with a region-independent lower bound on the full many-body density matrix. Even a full-rank product state has many-body eigenvalues that decrease exponentially with the number of sites.

## Why the noise retains an algebraic tail

The scalar circuit of [Newsom and Levin](../references/README.md#nl) has a dark momentum mode, with one occupation band touching zero quadratically. In the two-sector reference used here, the complementary filled sector supplies a particle-hole partner touching one. The entropy function

$$
h(x)=-x\log x-(1-x)\log(1-x)
$$

then produces algebraic corrections to interval entropies. That mechanism, including its scalar coefficient, is inherited from their work.

The orbital dressing changes the real-space occupied and empty subspaces. It removes every exact finite-region rank deficiency. Because the noise acts identically on the two orbital flavors, it commutes with that dressing at covariance level, and the occupation-band singularity survives. The [locality argument](locality-and-cmi.md) transfers the resulting CMI tail without replacing the physical nearest-neighbor noise by a quasi-local channel.

For each fixed $m>1$, the covariance remains analytic in a strip around real momentum after the noise. Ordinary two-point correlations, and mutual information between separated finite macroscopic blocks, therefore decay exponentially. Conditional correlations have a different asymptotic behavior. The fully shielded $L^{-2}$ law concerns the same geometry used to define Markov length.

## Weakness is measured per local gate

The noise strength tends to zero in the diamond norm of each finite-support gate. For the two-orbital gate, a convenient bound is

$$
\|\Phi_{x,\epsilon}-\operatorname{id}\|_\diamond
\leq 8\epsilon^2.
$$

The depth and support size remain fixed as the system size grows. Each collision uses a fresh maximally mixed environment mode. There is no postselection or shared environmental memory. On any fixed finite observation region, the noisy state approaches the initial state as $\epsilon\to0$.

The infinite-Markov-length statement takes large spatial separation at a fixed nonzero $\epsilon$. Its positive tail coefficient tends to zero with $\epsilon$. It does not assert a uniform macroscopic trace distance between an infinite system and its noiseless state, nor that a small finite experiment can resolve the asymptotic tail at arbitrary accuracy.

## A finite-temperature comparison in the same model

For a fixed finite inverse temperature $0\leq\beta<\infty$, replace the occupied projector by

$$
C_\beta(k)=\bigl[I+e^{\beta h_m(k)}\bigr]^{-1}.
$$

Since $m-1\leq E_m(k)\leq m+1$, its occupation eigenvalues obey

$$
\delta_\beta I\leq C_\beta(k)\leq(1-\delta_\beta)I,
\qquad
\delta_\beta=\frac{1}{1+e^{\beta(m+1)}}>0.
$$

Let $M(k)$ be the two-layer contraction on the parity subcell index. The same unital noise gives

$$
C_{\beta,\epsilon}(k)
=\frac{I}{2}
+M(k)M(k)^\dagger\otimes
\left(C_\beta(k)-\frac{I}{2}\right).
$$

Because $0\leq M(k)M(k)^\dagger\leq I$, the output obeys the same occupation margin $\delta_\beta$. In this comparison, the covariance-edge singularity used in the zero-temperature construction disappears. This algebraic observation is distinct from a general Markov-length stability theorem for finite-temperature Gibbs states.

## Consequence for stability statements

The construction rules out qualitative full rank of all finite marginals as a sufficient stability condition, even when the initial fermionic state is a gapped ground state with short-range correlations and finite Markov length. It also provides a locally faithful ordinary-spin realization through [the auxiliary construction](spin-realization.md); that spin input is mixed.

The result leaves several hypotheses distinct:

| Property | Status in this construction |
|---|---|
| Every finite-region density matrix is strictly positive | Holds before and after noise |
| Initial finite Markov length | Holds |
| Finite correlation length for ordinary observables | Holds |
| Uniform occupation margin away from zero and one | Fails in the zero-temperature construction |
| Product input on physical sites | Fails |
| Generic noise with an open parameter neighborhood | Not asserted; a dark mode is retained |
| Positive-temperature Gibbs-state instability | Not established |

In particular, the [product-input stability result](../references/README.md#product-stability) has a different hypothesis. Replacing product structure by faithfulness of each finite marginal would lose the protection it provides.

Markov-length divergence alone does not establish a thermodynamic phase transition or an obstruction to every notion of local reversibility. [Negari, Zou and Hsieh](../references/README.md#nzh) and [Chen and Grover](../references/README.md#cg) explain related distinctions between conditional-information tails, relaxation, and phase definitions. The contribution here is the precise limitation of a proposed local-rank criterion.
