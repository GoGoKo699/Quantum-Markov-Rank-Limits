# A locally faithful fermionic input and weak unital noise

This note defines the model used in the [instability theorem](instability-theorem.md). The input is a pure, gapped free-fermion ground state, but its density operator on every finite set of modes is strictly positive. The noise consists of two layers of nearest-neighbor fermionic channels, with fresh maximally mixed ancillas. An exact tensor identity relates the noisy state to the scalar construction of [Newsom and Levin, arXiv:2610.12929v3](https://arxiv.org/html/2610.12929v3).

The model is local in the fermionic algebra. No Jordan–Wigner identification with a strictly local spin channel is assumed.

## 1. Sites, covariance, and the finite-range Hamiltonian

The fine lattice is $\mathbb Z$. Each fine site $x$ carries two fermionic modes $c_{x,1},c_{x,2}$, satisfying the canonical anticommutation relations. A fine site therefore has a four-dimensional Fock space.

For the two-layer circuit, group two adjacent fine sites into a coarse cell:

$$
x=2j+p,\qquad p\in\{0,1\},\qquad
c_{j,p,a}:=c_{2j+p,a}.
\tag{M1}
$$

There are four modes per coarse cell. The internal ordering of the one-particle space is $p\otimes a$: fine-site parity first, orbital second.

We use the one-particle density matrix

$$
C_{i j}=\omega(c_j^\dagger c_i).
\tag{M2}
$$

For a gauge-invariant Gaussian state, $0\le C\le I$. Its reduced state on a finite mode set $R$ is Gaussian with covariance $C_R$, and

$$
S(\omega_R)=\operatorname{Tr}h(C_R),\qquad
h(t)=-t\log t-(1-t)\log(1-t).
\tag{M3}
$$

Logarithms are natural throughout. In particular, entropy and conditional mutual information are in nats.

On a periodic chain of $N$ coarse cells, our Fourier convention is

$$
c_{p,a}(k)=\frac1{\sqrt N}\sum_{j=0}^{N-1}e^{-ikj}c_{j,p,a},
\qquad k=\frac{2\pi n}{N}.
\tag{M4}
$$

Consequently a translation-invariant covariance has the inverse transform

$$
C_{(j,p,a),(\ell,q,b)}
=\int_{-\pi}^{\pi}\frac{dk}{2\pi}\,
e^{ik(j-\ell)}C(k)_{(p,a),(q,b)}
\tag{M5}
$$

in infinite volume. This convention makes the occupied-band projector the covariance and gives the Gaussian channel rule $C\mapsto XCX^\dagger+Y$.

Fix a finite $m>1$. Consider the real-space Hamiltonian

$$
H_m=\sum_{x\in\mathbb Z}
\left[
m\,c_{x,1}^{\dagger}c_{x,2}
+c_{x,1}^{\dagger}c_{x+2,2}
+\mathrm{h.c.}
\right].
\tag{M6}
$$

Its hopping range is two fine sites. It is invariant under translation by **one** fine site. The even and odd fine sites form two identical, independent SSH chains. In coarse-cell momentum space,

$$
h_{\mathrm{in},m}(k)=I_p\otimes h_m(k),\qquad
h_m(k)=
\begin{pmatrix}
0&m+e^{ik}\\
m+e^{-ik}&0
\end{pmatrix}.
\tag{M7}
$$

Define

$$
E_m(k)=\sqrt{(m+e^{ik})(m+e^{-ik})},
\qquad
P_m(k)=\frac12\left(I_a-\frac{h_m(k)}{E_m(k)}\right).
\tag{M8}
$$

The positive root is used for real $k$. Since $E_m(k)\ge m-1>0$, the finite periodic Hamiltonian has a unique Fock-space ground state obtained by filling all negative-energy modes. Its many-body excitation gap is at least $m-1$, uniformly in the circumference. Restricting the allowed particle number can increase this gap; no such restriction is needed here.

Let $\omega_m$ be its local thermodynamic limit. It is a pure, gauge-invariant Gaussian state with covariance

$$
C_{\mathrm{in},m}(k)=I_p\otimes P_m(k).
\tag{M9}
$$

The input is invariant under a one-fine-site translation. The brickwork noise below generally leaves only a two-fine-site translation symmetry. Thus one coarse cell is the common translation unit used for all entropy asymptotics.

## 2. Every finite input reduction is faithful

Here, a finite reduced state is **faithful** if its density operator is strictly positive on the entire finite Fock space. There is no lower-eigenvalue bound uniform in the size of the region.

### Proposition 1: local faithfulness of the input

For every finite set $R$ of modes, including disconnected sets and subsets of the orbitals at a site,

$$
0<(C_{\mathrm{in},m})_R<I,
\qquad
(\omega_m)_R>0.
\tag{M10}
$$

### Proof

Diagonalizing a finite Gaussian covariance with eigenvalues $\nu_1,\ldots,\nu_r$ puts its density operator into the form

$$
\bigotimes_{\ell=1}^{r}
\left[(1-\nu_\ell)|0\rangle\langle0|
+\nu_\ell|1\rangle\langle1|\right].
\tag{M11}
$$

It is therefore enough to exclude covariance eigenvalues $0$ and $1$ on a finite set.

First consider one of the two parity chains, with infinite-volume covariance $P_m$. Suppose a finite compression has eigenvalue $0$ or $1$, and extend its eigenvector by zero to a nonzero compactly supported vector $v$. Since $P_m$ is an orthogonal projection,

$$
\langle v,P_mv\rangle=0\ \Longrightarrow\ P_mv=0,
\qquad
\langle v,(I-P_m)v\rangle=0\ \Longrightarrow\ P_mv=v.
\tag{M12}
$$

The Fourier transform $v(z)$, with $z=e^{ik}$, is a two-component vector of Laurent polynomials. Equation (M12) implies

$$
h_m(z)v(z)=\pm E_m(z)v(z).
\tag{M13}
$$

Choose a component $v_a(z)$ which is not identically zero. Away from its finitely many zeros, (M13) writes $E_m(z)$ as the ratio of two Laurent polynomials. Squaring gives a rational-function identity

$$
\left(\frac{(h_m(z)v(z))_a}{v_a(z)}\right)^2
=(m+z)(m+z^{-1}).
\tag{M14}
$$

The identity initially holds on the unit circle and hence holds as an identity of rational functions. Its right side has simple zeros at $z=-m$ and $z=-1/m$. A square of a rational function has even order at every zero and pole. This is impossible.

Thus neither $P_m$ nor $I-P_m$ annihilates a nonzero compactly supported vector. The same conclusion holds for $I_p\otimes P_m$: at least one parity component of a nonzero compactly supported vector is nonzero. Compressing to any finite mode set proves the first part of (M10), and (M11) proves the second. $\square$

This proof concerns the infinite-chain state and its finite restrictions. The entire ground state on a finite closed ring is pure and therefore not faithful. The thermodynamic distinction is essential: first fix a finite region and take the ring circumference to infinity.

## 3. The weak unital bond channel

For a fine bond $(x,x+1)$, set

$$
s_{x,a}=\frac{c_{x,a}+c_{x+1,a}}{\sqrt2},
\qquad a=1,2.
\tag{M15}
$$

Introduce two fresh ancillary fermions $d_{x,1},d_{x,2}$, each in the maximally mixed state $I/2$, and apply the even, number-conserving Gaussian unitary

$$
V_{x,\epsilon}
=\exp\!\left[
\epsilon\sum_{a=1}^{2}
\left(s_{x,a}^{\dagger}d_{x,a}
-d_{x,a}^{\dagger}s_{x,a}\right)
\right].
\tag{M16}
$$

The two terms in the exponent commute, since they are even bilinears on disjoint mode sets. The bond channel is

$$
\Phi_{x,\epsilon}(\rho)
=\operatorname{Tr}_{d_{x,1},d_{x,2}}
\left[
V_{x,\epsilon}
\left(\rho\otimes\frac{I_d}{4}\right)
V_{x,\epsilon}^{\dagger}
\right].
\tag{M17}
$$

The fermionic product with the environment is well defined because the environment state is even. This dilation specifies the action on correlated system states, rather than only on a standalone bond density matrix. It is physically local in the CAR algebra and preserves the parity superselection rule. Ancillas are discarded after the gate and are never shared between gates.

The finite bond map is CPTP and unital:

$$
\Phi_{x,\epsilon}(I_{\mathrm{bond}})=I_{\mathrm{bond}}.
\tag{M18}
$$

Indeed, the input identity tensored with the normalized environmental identity commutes with every unitary in (M16).

For clarity about weakness, write

$$
G_x=\sum_a(s_{x,a}^{\dagger}d_{x,a}
-d_{x,a}^{\dagger}s_{x,a}),
\qquad \|G_x\|\le2.
$$

The first derivative of (M17) at $\epsilon=0$ vanishes: every first-order term contains one ancillary creation or annihilation operator, whose trace in the maximally mixed state is zero. The double-commutator bound for the second derivative therefore gives

$$
\|\Phi_{x,\epsilon}-\mathrm{id}\|_\diamond
\le 2\|G_x\|^2\epsilon^2
\le8\epsilon^2.
\tag{M19}
$$

This is a conservative bound, sufficient to make each physical gate arbitrarily weak. It uses the finite local gate and its fermionic dilation; it does not assert that the full extensive circuit is close to the identity in global diamond norm. The scalar gate is also the channel in NL, Eqs. (4)–(6), whose random-unitary form appears in Appendix G, Proposition 7.

We work with

$$
0<\epsilon<\epsilon_*:=\frac{\pi}{2}.
\tag{M20}
$$

This is the range treated in NL and includes arbitrarily weak nonzero noise. No statement about every nonzero angle is intended.

Apply all even bonds first and all odd bonds second:

$$
\mathcal E_\epsilon
=
\left(\prod_{x\ \mathrm{odd}}\Phi_{x,\epsilon}\right)
\circ
\left(\prod_{x\ \mathrm{even}}\Phi_{x,\epsilon}\right).
\tag{M21}
$$

Each product is a layer of disjoint fine-site bonds. In infinite volume, the channel on any finite observable is defined by its finite backward cone. Let

$$
\rho_{m,\epsilon}=\mathcal E_\epsilon(\omega_m).
\tag{M22}
$$

## 4. Exact covariance matrices of the circuit

For one orbital and one bond, let

$$
|s_x\rangle=(|x\rangle+|x+1\rangle)/\sqrt2.
$$

The system block of the one-particle dilation is

$$
X_x=I+(\cos\epsilon-1)|s_x\rangle\langle s_x|,
$$

and the environmental covariance is $I/2$. Therefore

$$
C\longmapsto X_x C X_x^\dagger
+\frac{I-X_xX_x^\dagger}{2}.
\tag{M23}
$$

The same form telescopes under composition. In the coarse-cell $p$-space, define

$$
\Pi_0=\frac12
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
\Pi_1(k)=\frac12
\begin{pmatrix}1&e^{-ik}\\e^{ik}&1\end{pmatrix},
\tag{M24}
$$

$$
X_0=I_p+(\cos\epsilon-1)\Pi_0,\qquad
X_1(k)=I_p+(\cos\epsilon-1)\Pi_1(k),
$$

$$
X_\epsilon(k)=X_1(k)X_0,\qquad
T_\epsilon(k)=X_\epsilon(k)X_\epsilon(k)^\dagger,
\qquad
Q_\epsilon(k)=\frac{I_p-T_\epsilon(k)}2.
\tag{M25}
$$

The matrix $X_0$ represents the even layer and $X_1$ the odd layer. Each layer has eigenvalues $1,\cos\epsilon$, so $X_\epsilon$ is invertible in the chosen range and is a contraction. In particular $0\le Q_\epsilon\le I_p/2$.

Because both orbitals receive identical noise, the full Gaussian channel has matrices

$$
\mathsf X_\epsilon(k)=X_\epsilon(k)\otimes I_a,\qquad
\mathsf Y_\epsilon(k)=Q_\epsilon(k)\otimes I_a.
\tag{M26}
$$

It follows that

$$
\begin{aligned}
C_{m,\epsilon}(k)
&=T_\epsilon(k)\otimes P_m(k)+Q_\epsilon(k)\otimes I_a\\
&=Q_\epsilon(k)\otimes(I_a-P_m(k))
+(I_p-Q_\epsilon(k))\otimes P_m(k).
\end{aligned}
\tag{M27}
$$

The matrix $Q_\epsilon$ is exactly the scalar noisy-vacuum covariance used in NL, expressed in our covariance convention. More explicitly,

$$
Q_\epsilon(k)=
\begin{pmatrix}
a_\epsilon(k)&\overline{b_\epsilon(k)}\\
b_\epsilon(k)&a_\epsilon(k)
\end{pmatrix},
\tag{M28}
$$

$$
a_\epsilon(k)
=\frac12\sin^2\epsilon
-\frac14\sin^4\epsilon\,\cos^2(k/2),
$$

$$
b_\epsilon(k)
=\frac14\sin^2\epsilon\,(1+e^{ik})
\left[
\cos^4(\epsilon/2)+\sin^4(\epsilon/2)e^{ik}
\right].
\tag{M29}
$$

NL, Eqs. (7), (9)–(11), uses the opposite ordering of the covariance indices. Thus (M28) is the transpose of their displayed symbol. This convention change leaves the physical restricted-covariance spectra and all interval entropies unchanged. In particular, the two-site unit cell in NL is exactly one coarse cell here.

## 5. An exponentially local dressing that commutes with the noise

Let

$$
P_{\mathrm{prod}}=\frac{I_a-\sigma_x}{2},
\qquad
\theta_m(k)
=\frac{\log(m+e^{ik})-\log(m+e^{-ik})}{2i},
\tag{M30}
$$

$$
u_m(k)=
\begin{pmatrix}
e^{i\theta_m(k)/2}&0\\
0&e^{-i\theta_m(k)/2}
\end{pmatrix}.
\tag{M31}
$$

Since $m>1$, use the logarithms obtained from
$\log(m+z)=\log m+\log(1+z/m)$ on the annulus containing the unit circle. The function $\theta_m$ is real on real $k$, periodic, and analytic in the strip $|\operatorname{Im}k|<\log m$. There is no winding ambiguity. Directly,

$$
u_m(k)P_{\mathrm{prod}}u_m(k)^\dagger=P_m(k).
\tag{M32}
$$

The Fourier series is

$$
\theta_m(k)
=\sum_{r\ge1}\frac{(-1)^{r+1}}{r m^r}\sin(rk).
\tag{M33}
$$

Hence $u_m=e^{-ik_m}$, where
$k_m(k)=-\theta_m(k)\sigma_z/2$, is generated in unit time by exponentially decaying hopping. For example, with
$A_r=(-1)^{r+1}/(r m^r)$, a real-space generator is

$$
K_m=\sum_{j,p}\sum_{r\ge1}
\frac{iA_r}{4}
\left[
c_{j,p,1}^{\dagger}c_{j+r,p,1}
-c_{j+r,p,1}^{\dagger}c_{j,p,1}
-c_{j,p,2}^{\dagger}c_{j+r,p,2}
+c_{j+r,p,2}^{\dagger}c_{j,p,2}
\right].
\tag{M34}
$$

Its hopping distance is $2r$ in fine-site units. Denote its time-one automorphism by $\mathcal U_m$; on finite rings it is conjugation by the number-conserving second quantization of $I_p\otimes u_m(k)$. Writing $\mathcal U_m$ as an automorphism avoids assuming the existence of a single global Hilbert-space unitary in infinite volume.

Let $\omega_{\mathrm{prod}}$ be the onsite product state with covariance $I_p\otimes P_{\mathrm{prod}}$. At each fine site, its antisymmetric orbital is occupied and its symmetric orbital is empty. Then

$$
\omega_m=\mathcal U_m(\omega_{\mathrm{prod}}).
\tag{M35}
$$

Define the reference noisy state

$$
\tau_\epsilon=\mathcal E_\epsilon(\omega_{\mathrm{prod}}).
$$

Its covariance is

$$
C_{\tau_\epsilon}(k)
=Q_\epsilon(k)\otimes(I_a-P_{\mathrm{prod}})
+(I_p-Q_\epsilon(k))\otimes P_{\mathrm{prod}}.
\tag{M36}
$$

Since $X_\epsilon\otimes I_a$ and $Q_\epsilon\otimes I_a$ commute with $I_p\otimes u_m$, equations (M27) and (M32) give the exact state identity

$$
\boxed{\rho_{m,\epsilon}=\mathcal U_m(\tau_\epsilon).}
\tag{M37}
$$

Gaussianity makes equality of these covariances equality of states. This argument only needs the stated Gaussian inputs; it does not rely on a stronger arbitrary-state covariance of the channel.

After a fixed onsite orbital rotation diagonalizing $P_{\mathrm{prod}}$, the reference state has two independent Gaussian sectors with covariances $Q_\epsilon$ and $I_p-Q_\epsilon$. Thus every complete-cell interval has twice the entropy of the scalar NL noisy-vacuum state:

$$
S_{\tau_\epsilon}(n)=2S_{\mathrm{NL},\epsilon}(n).
\tag{M38}
$$

This is the essential locality mechanism. The **actual noise** remains the strictly nearest-neighbor circuit (M21). It has not been defined by conjugating a local noise channel into a channel with exponentially long tails.

## 6. Every finite output reduction is also faithful

### Proposition 2: local faithfulness after the channel

For every finite mode set $R$,

$$
0<(C_{m,\epsilon})_R<I,
\qquad
(\rho_{m,\epsilon})_R>0.
\tag{M39}
$$

### Proof

In real-space one-particle notation, write
$\mathsf X=X_\epsilon\otimes I_a$ and
$\mathsf Y=(I-\mathsf X\mathsf X^\dagger)/2$. The circuit rule gives

$$
C_{m,\epsilon}=\mathsf X C_{\mathrm{in},m}\mathsf X^\dagger+\mathsf Y,
$$

$$
I-C_{m,\epsilon}
=\mathsf X(I-C_{\mathrm{in},m})\mathsf X^\dagger+\mathsf Y.
\tag{M40}
$$

The matrix $\mathsf Y$ is positive. Moreover $\mathsf X$ has finite propagation range and is invertible: each layer is bounded below in singular value by $\cos\epsilon>0$.

For a nonzero compactly supported vector $v$, the vector
$w=\mathsf X^\dagger v$ is therefore compactly supported and nonzero. Proposition 1 yields

$$
\langle w,C_{\mathrm{in},m}w\rangle>0,
\qquad
\langle w,(I-C_{\mathrm{in},m})w\rangle>0.
$$

Equation (M40) then gives strict positivity of both quadratic forms on $v$. Compress to any finite $R$, and use (M11). $\square$

The global Bloch symbol nevertheless reaches occupations $0$ and $1$ at a dark momentum. A finite-region spectral floor is not uniform as its size increases. Local full rank therefore does not remove the asymptotic entropy singularity used in the [instability theorem](instability-theorem.md).

## 7. Finite-volume and locality conventions

The finite-volume construction uses a ring of $N$ coarse cells, equivalently $2N$ fine sites. Both bond matchings and all fresh ancillas are then finite. Its covariance symbols are the matrices above evaluated at the discrete momenta $2\pi n/N$.

The infinite states $\omega_m$ and $\rho_{m,\epsilon}$ are defined by taking $N\to\infty$ with the observed finite region fixed. The entropy and CMI asymptotics subsequently take region sizes to infinity at fixed $m>1$ and fixed $0<\epsilon<\epsilon_*$.

Both $P_m(k)$ and $C_{m,\epsilon}(k)$ are analytic in every closed substrip of $|\operatorname{Im}k|<\log m$. Their real-space covariance entries therefore decay exponentially. Periodic sampling differs from the infinite covariance by exponentially small image terms on regions far from the periodic closure. The [locality and CMI bounds](locality-and-cmi.md) work directly with the infinite-chain automorphism and local finite-window approximations; a global trace-norm thermodynamic limit is not required.

The input's finite Markov length and the preservation of the leading macroscopic CMI coefficient under $\mathcal U_m$ are proved there. The [central theorem](instability-theorem.md) combines these facts with the imported scalar entropy asymptotic.
