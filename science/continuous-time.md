# A two-mode balanced Lindblad companion

The finite-depth construction has a simpler continuous-time companion. It uses one SSH chain, with two fermionic orbitals per site, and balanced nearest-neighbor gain and loss. Its initial and evolved states are faithful on every finite region, while any fixed positive evolution time produces infinite Markov length.

Lengths in this note count these **two-mode sites**. They are not the four-mode coarse cells of the [finite-depth theorem](instability-theorem.md). All entropies use natural logarithms.

## Model and exact covariance

Fix $m>1$, and prepare the pure ground state of

$$
H_m^{\mathrm{ct}}
=\sum_{j\in\mathbb Z}
\left[
m\,c_{j,1}^\dagger c_{j,2}
+c_{j,1}^\dagger c_{j+1,2}
+\mathrm{h.c.}
\right].
\tag{C1}
$$

This Hamiltonian has nearest-neighbor range and a gap at least $m-1$. Denote its thermodynamic ground state by $\omega_m^{\mathrm{ct}}$. With the covariance and Fourier conventions of the [model note](model-and-rank.md), its occupied-band covariance is

$$
P_m(k)=\frac12\left[
I-\frac1{E_m(k)}
\begin{pmatrix}0&m+e^{ik}\\m+e^{-ik}&0\end{pmatrix}
\right],
\qquad
E_m(k)=|m+e^{ik}|.
\tag{C2}
$$

The local-faithfulness proof for a single SSH component in Proposition 1 of that note applies without change.

Define

$$
\mathcal D[L](\rho)
=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\},
\qquad
d_{j,a}=c_{j,a}-c_{j+1,a},
$$

$$
\mathcal L
=\frac12\sum_{j,a}
\left(\mathcal D[d_{j,a}]+\mathcal D[d_{j,a}^\dagger]\right).
\tag{C3}
$$

There is no Hamiltonian term in this evolution. The generator is local in the fermionic algebra; no spin-local realization is asserted here. Each balanced pair is unital because
$\mathcal D[d](I)+\mathcal D[d^\dagger](I)=0$.
The difference mode $d_{j,a}$ is **not normalized**. The prefactor in (C3) fixes the time convention.

The infinite-chain notation $\rho_{m,t}^{\mathrm{ct}}=e^{t\mathcal L}(\omega_m^{\mathrm{ct}})$ means the local thermodynamic limit of finite-open-chain evolutions of the restricted input state. Every input and evolved state is parity even. The locality statement concerns this even sector; the raw sum of odd-jump GKSL terms is not asserted to be a norm-local generator on arbitrary odd CAR observables.

This limit can be seen directly at covariance level. On a finite interval $\Lambda$, let

$$
F_\Lambda=
\sum_{j,j+1\in\Lambda}
|e_j-e_{j+1}\rangle\langle e_j-e_{j+1}|\otimes I_{\mathrm{orbital}}.
$$

The linear fermionic jumps preserve Gaussianity, and the exact finite-volume covariance is

$$
C_\Lambda(t)=\frac I2+
e^{-tF_\Lambda/2}
\left(C_\Lambda(0)-\frac I2\right)
e^{-tF_\Lambda/2}.
\tag{C3a}
$$

The uniform bound $\|F_\Lambda\|\leq4$ and convergence of its finite-range matrix elements give local convergence of (C3a). The limiting Gaussian covariances determine all finite even-state restrictions. In momentum space, put

$$
f(k)=|1-e^{ik}|^2=2-2\cos k.
$$

The gain and loss one-particle rate matrices are both $f(k)I/2$. Hence

$$
\partial_t C_t(k)
=-\frac12\{f(k)I,C_t(k)\}+\frac12f(k)I
=-f(k)\left(C_t(k)-\frac I2\right),
$$

$$
\boxed{
C_t(k)=\frac I2+e^{-t f(k)}
\left(P_m(k)-\frac I2\right).
}
\tag{C4}
$$

Its occupations are $q_t(k)$ and $1-q_t(k)$, where

$$
q_t(k)=\frac{1-e^{-t f(k)}}2.
\tag{C5}
$$

This is the damping convention used in the [balanced numerical data](../data/README.md).

## Faithfulness and the dressing identity

For every fixed finite $t>0$, $q_t(k)>0$ except at $k=0$ modulo $2\pi$, a set of measure zero. Moreover,

$$
C_t(k)\ge q_t(k)I,\qquad
I-C_t(k)\ge q_t(k)I.
\tag{C6}
$$

If a nonzero vector $v$ has finite support, its Fourier transform is a nonzero vector of Laurent polynomials, and

$$
\langle v,C_tv\rangle
\ge\int_{-\pi}^{\pi}\frac{dk}{2\pi}\,
q_t(k)\|v(k)\|^2>0.
\tag{C7}
$$

The same estimate holds for $I-C_t$. Thus every finite covariance compression has eigenvalues strictly between zero and one, and every finite reduced density operator is faithful. This proof uses positivity almost everywhere; it does not treat the infinite-range attenuation matrix $e^{-t f/2}$ as a finite-range map on compactly supported vectors.

The same orbital dressing $u_m(k)$ as in (M30)–(M33) sends the onsite projector $P_{\mathrm{prod}}$ to $P_m(k)$. Since $e^{-t f(k)}I$ is scalar in orbital space, (C4) gives

$$
\rho_{m,t}^{\mathrm{ct}}=\mathcal U_m(\tau_t^{\mathrm{ct}}),
\tag{C8}
$$

where, after a fixed onsite orbital rotation, the reference state has two independent sectors with covariances $q_t$ and $1-q_t$. The initial state is the same exponentially local dressing of an onsite product state. The [locality note](locality-and-cmi.md) therefore establishes finite initial Markov length and transfers the reference CMI asymptotic through this dressing.

## Imported scalar entropy and its normalization

The scalar reference is the staggered version of the Lindbladian example in [Newsom–Levin, arXiv:2610.12929v3, Appendix H](https://arxiv.org/html/2610.12929v3). Their Eq. (169) has occupation

$$
\lambda_{\mathrm{NL}}(k)
=\frac12\left[1-e^{-2t_{\mathrm{NL}}\sin^2(k/2)}\right].
$$

Equation (C5) agrees with it at

$$
t_{\mathrm{NL}}=2t.
\tag{C9}
$$

Equivalently, on each orbital sector, (C3) is twice the staggered NL generator: their bond mode is normalized by $1/\sqrt2$, while $d_{j,a}$ in (C3) is not.

Their rigorous interval formula, Eq. (174), is written for $N$ two-site cells, or $n=2N$ scalar sites:

$$
S_{\mathrm{NL}}(N)
=N\bar s+\Delta-\frac{t_{\mathrm{NL}}\zeta(3)}{32N^2}
+O(N^{-3}).
\tag{C10}
$$

Substituting (C9) and $N=n/2$ gives the single-orbital coefficient
$-t\zeta(3)/(4n^2)$. The two complementary orbital sectors have equal entropy, so

$$
S_{\tau_t^{\mathrm{ct}}}(n)
=n s_t+b_t-\frac{\kappa_t^{\mathrm{ct}}}{n^2}
+O_t(n^{-3}),
\qquad
\kappa_t^{\mathrm{ct}}=\frac{t\zeta(3)}2.
\tag{C11}
$$

The source directly supplies (C11) for even $n$. Applying the dressing argument after blocking two sites uses only those interval lengths. Arbitrary integer tripartitions follow by enlarging or contracting endpoint intervals by at most two sites to compare with aligned tripartitions. These bounded boundary shifts preserve the leading macroscopic CMI coefficient.

## Corollary: algebraic CMI after every fixed positive time

For fixed $m>1$, fixed finite $t>0$, and positive $a,b,c$, the CMI of consecutive intervals of lengths $aL+O(1),bL+O(1),cL+O(1)$ satisfies

$$
I_{\rho_{m,t}^{\mathrm{ct}}}(A:C\mid B)
=\frac{t\zeta(3)}{2L^2}
\left[
\frac1{b^2}+\frac1{(a+b+c)^2}
-\frac1{(a+b)^2}-\frac1{(b+c)^2}
\right]+o(L^{-2}).
\tag{C12}
$$

In particular,

$$
\boxed{
I_{\rho_{m,t}^{\mathrm{ct}}}(L:L\mid L)
=\frac{11t\zeta(3)}{36L^2}+o(L^{-2}).
}
\tag{C13}
$$

The notation in (C13) means three consecutive equal intervals, as in (T2).

The symbol (C4) is analytic, so ordinary mutual information between finite blocks separated by $L$ decays exponentially, by the Gaussian estimate in the locality note. For five consecutive equal blocks $C_-,B_-,A,B_+,C_+$, each of $L$ sites, the entropy identity (T22)–(T24) therefore gives

$$
\boxed{
I_{\rho_{m,t}^{\mathrm{ct}}}
(A:C_-\cup C_+\mid B_-\cup B_+)
=\frac{643t\zeta(3)}{900L^2}+o(L^{-2}).
}
\tag{C14}
$$

This positive algebraic tail establishes infinite Markov length in the fully shielded geometry. It holds for arbitrarily short positive times. The thermodynamic limit is taken first, followed by $L\to\infty$ at fixed $m,t$; the bounds are not uniform in a joint zero-time or infinite-time limit. All coefficients are in nats and are divided by $\log2$ when entropy is measured in bits.
