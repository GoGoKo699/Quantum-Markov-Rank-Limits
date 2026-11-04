# Local full rank does not stabilize the quantum Markov length

The [model and rank proof](model-and-rank.md) supplies a pure, gapped fermionic ground state $`\omega_m`$, a depth-two unital nearest-neighbor channel $`\mathcal E_\epsilon`$, and its output $`\rho_{m,\epsilon}`$. Both states have strictly positive reduced density operators on every finite mode set. Nevertheless, $`\omega_m`$ has finite Markov length, while $`\rho_{m,\epsilon}`$ has infinite Markov length for arbitrarily weak nonzero $`\epsilon`$.

The algebraic entropy asymptotic used below is inherited from [Newsom and Levin, arXiv:2610.12929v3](https://arxiv.org/html/2610.12929v3). The new step is the exactly compatible, exponentially local dressing of a locally faithful input, with the physical noise kept strictly finite depth.

## 1. Definitions, normalization, and order of limits

All lengths in this note count **coarse cells**. One coarse cell contains two fine sites, each with two fermionic orbitals. The noise gates remain nearest-neighbor gates on the fine chain.

For finite disjoint fermionic regions, entropy is the entropy of the restricted even state on the corresponding finite CAR algebra. We use natural logarithms:

```math

I_\sigma(A:C\mid B)
=S_\sigma(AB)+S_\sigma(BC)-S_\sigma(B)-S_\sigma(ABC).
\tag{T1}
```

For a coarse-translation-invariant state, write $`S_\sigma(n)`$ for the entropy of $`n`$ consecutive complete cells and

```math

\begin{aligned}
\mathcal I_\sigma(n_A,n_B,n_C)
&:=I_\sigma(A:C\mid B)\\
&=S_\sigma(n_A+n_B)+S_\sigma(n_B+n_C)
-S_\sigma(n_B)-S_\sigma(n_A+n_B+n_C),
\end{aligned}
\tag{T2}
```

where $`A,B,C`$ are consecutive intervals of the indicated lengths.

The Markov-length definition uses the fully shielded geometry

```math

C_-\,\,B_-\,\,A\,\,B_+\,\,C_+,
\qquad B=B_-\cup B_+,\qquad C=C_-\cup C_+.
\tag{T3}
```

A finite Markov length means that, uniformly over these finite shielded regions,

```math

I_\sigma(A:C\mid B)
\le P(|A|,|B|,|C|)\,
e^{-\operatorname{dist}(A,C)/\xi}
\tag{T4}
```

for some finite $`\xi`$ and a fixed polynomial $`P`$. This is the size-prefactor convention of NL, Eq. (2). Constant changes between fine-site and coarse-cell distance do not affect whether $`\xi`$ is finite.

The states in the theorem are infinite-chain states. They are obtained from periodic rings by taking the circumference to infinity with the observed finite region fixed. Region sizes are then sent to infinity at fixed

```math

m>1,\qquad 0<\epsilon<\epsilon_*=\pi/2.
\tag{T5}
```

The asymptotics are not claimed uniformly as $`m\downarrow1`$ or $`\epsilon\downarrow0`$. In particular, the large-region limit and the zero-noise limit must not be interchanged without an additional estimate.

## 2. Central theorem

Define

```math

\gamma_\epsilon
=\frac{\sin^2\epsilon}{8(1+\cos^2\epsilon)},
\qquad
\kappa_\epsilon=\gamma_\epsilon\zeta(3),
\tag{T6}
```

and, for $`a,b,c>0`$,

```math

F(a,b,c)
=\frac1{b^2}+\frac1{(a+b+c)^2}
-\frac1{(a+b)^2}-\frac1{(b+c)^2}.
\tag{T7}
```

### Theorem

For the model of (T5):

1. The input $`\omega_m`$ is the pure thermodynamic ground state of the range-two Hamiltonian in the model note, with a size-independent gap at least $`m-1`$. Every finite reduced density operator of both $`\omega_m`$ and $`\rho_{m,\epsilon}`$ is faithful.
2. The input $`\omega_m`$ satisfies an exponential CMI bound of the form (T4).
3. For any fixed $`a,b,c>0`$, choose positive integers $`a_L,b_L,c_L`$ with $`a_L=aL+O(1)`$, $`b_L=bL+O(1)`$, $`c_L=cL+O(1)`$. Then

```math

\boxed{
\mathcal I_{\rho_{m,\epsilon}}(a_L,b_L,c_L)
=\frac{\kappa_\epsilon F(a,b,c)}{L^2}
+o(L^{-2}).
}
\tag{T8}
```

4. For five consecutive blocks $`C_-,B_-,A,B_+,C_+`$, each of $`L`$ cells,

```math

\boxed{
I_{\rho_{m,\epsilon}}
(A:C_-\cup C_+\mid B_-\cup B_+)
=\frac{643}{450}\,
\frac{\kappa_\epsilon}{L^2}
+o(L^{-2}).
}
\tag{T9}
```

Consequently $`\rho_{m,\epsilon}`$ has infinite Markov length. Each gate of $`\mathcal E_\epsilon`$ is unital and has distance at most $`8\epsilon^2`$ from the identity in the local diamond norm, so the conclusion holds under arbitrarily weak gates.

The coefficient in (T8) is strictly positive:

```math

F(a,b,c)
=\int_0^a\!\int_0^c
\frac{6\,ds\,dt}{(b+s+t)^4}>0.
\tag{T10}
```

It is independent of the fixed SSH parameter $`m`$. The approximation constants and the finite-size crossover can depend on $`m`$.

The rank, gap, and weak-channel statements are proved in the [model note](model-and-rank.md). The remainder of this note proves the CMI statements.

## 3. The inherited single-orbital entropy theorem

Let $`\sigma_{\mathrm{NL},\epsilon}`$ be the one-orbital noisy-vacuum state produced by the two-layer channel of NL. For an interval of $`n`$ **two-site unit cells**, the rigorous result in Appendix E.1, Eq. (132), of

[D. C. Newsom and M. Levin, “An Instability of the Quantum Markov Length,” arXiv:2610.12929v3, 29 October 2026](https://arxiv.org/html/2610.12929v3)

is

```math

S_{\mathrm{NL},\epsilon}(n)
=n\bar s_\epsilon+\Delta_\epsilon
-\frac{\gamma_\epsilon\zeta(3)}{2n^2}
+O_\epsilon(n^{-3}).
\tag{T11}
```

The value of $`\gamma_\epsilon`$ is their Eq. (13). Equation (T11) is an interval result, not an inference from a periodic-ring entropy. Its cell size is exactly the coarse-cell size used here.

The reference state $`\tau_\epsilon`$ in the model note has independent orbital sectors with covariances $`Q_\epsilon`$ and $`I-Q_\epsilon`$. The identity $`h(1-t)=h(t)`$ therefore gives

```math

S_{\tau_\epsilon}(n)
=2S_{\mathrm{NL},\epsilon}(n)
=2n\bar s_\epsilon+2\Delta_\epsilon
-\frac{\kappa_\epsilon}{n^2}
+O_\epsilon(n^{-3}).
\tag{T12}
```

Substitution into (T2) cancels the extensive and boundary terms. For fixed positive macroscopic ratios,

```math

\mathcal I_{\tau_\epsilon}(a_L,b_L,c_L)
=\frac{\kappa_\epsilon F(a,b,c)}{L^2}
+O_\epsilon(L^{-3}).
\tag{T13}
```

Bounded integer rounding changes only the $`O(L^{-3})`$ term. No estimate of derivatives of an unspecified entropy remainder is needed, since all four interval lengths are proportional to $`L`$.

## 4. Transferring the coefficient through the dressing

The model gives the exact identities

```math

\omega_m=\mathcal U_m(\omega_{\mathrm{prod}}),
\qquad
\rho_{m,\epsilon}=\mathcal U_m(\tau_\epsilon),
\tag{T14}
```

where $`\mathcal U_m`$ is a unit-time, number-conserving Gaussian evolution with exponentially decaying hopping amplitudes.

The [locality and CMI note](locality-and-cmi.md) proves the required local-unitary approximation and CMI sandwich. The principle is elementary. For one layer of disjoint unitary blocks, enlarge the endpoint regions backwards to unions of blocks,

```math

X=Ax,\qquad Y,\qquad Z=zC.
```

The final buffer is $`xYz`$. The chain rule and strong subadditivity give

```math

I_{\mathrm{after}}(A:C\mid xYz)
\le I_{\mathrm{after}}(Ax:zC\mid Y)
=I_{\mathrm{before}}(X:Z\mid Y).
\tag{T15}
```

The equality is invariance under the three block-local unitaries. Exterior sites absorbed into the endpoint regions can be traced out using endpoint data processing. Repeating the construction through the circuit moves each boundary by at most its total light-cone radius. Applying the same argument to the inverse circuit gives the lower bound.

More explicitly, suppose local circuit approximations of $`\mathcal U_m`$ and its inverse have half trace-distance error $`\delta_L`$ on the required finite observation intervals and radius at most $`r_L`$, where

```math

r_L=o(L),\qquad
L\delta_L+h(\delta_L)=o(L^{-2}).
\tag{T16}
```

Up to an error $`e_L=o(L^{-2})`$, the resulting CMI is bounded below and above by

```math

\begin{aligned}
&\mathcal I_{\tau_\epsilon}
(a_L-2r_L,\ b_L+2r_L,\ c_L-2r_L)-e_L\\
&\hspace{12mm}\le
\mathcal I_{\rho_{m,\epsilon}}(a_L,b_L,c_L)\\
&\hspace{12mm}\le
\mathcal I_{\tau_\epsilon}
(a_L+2r_L,\ b_L-2r_L,\ c_L+2r_L)+e_L .
\end{aligned}
\tag{T17}
```

Integers can be rounded outward, and all lengths are positive for sufficiently large $`L`$. The factors $`2r_L`$ allow both endpoints of each endpoint interval to move; they are conservative.

For this explicit dressing, Lemma 3 of the locality note provides depth-two block circuits with $`r_L=O(\log L)`$ and local half trace-distance error $`\delta_L=O(L^{-8})`$. The circuit follows from a block-and-boundary decomposition of the exponentially local evolution. It applies to inputs correlated with their exterior. The associated CMI continuity error is $`O(L^{-7})`$. A separate local circuit approximation of the inverse evolution supplies the lower comparison.

Applying (T12) to the shifted lengths in (T17) is legitimate uniformly: each remains bounded above and below by a positive constant times $`L`$. The function $`F`$ is continuous on positive macroscopic ratios, and $`r_L/L\to0`$. Both bounds therefore tend, after multiplication by $`L^2`$, to the same value $`\kappa_\epsilon F(a,b,c)`$. This proves (T8). In fact, Proposition 4 of the locality note gives the stronger remainder $`O_{m,\epsilon,a,b,c}(\log L/L^3)`$.

This argument transfers the **CMI coefficient**. It does not assume that every term in the dressed interval-entropy expansion has already been computed.

### Finite-volume passage

The locality proof compares the infinite-chain evolution with a circuit supported on a finite window padded around the observation interval. It bounds the induced local evolution uniformly for all inputs, including those correlated with the outside of that window. It therefore does not replace the input by an uncorrelated finite-volume state.

Equivalently, one may take the finite-volume limit at each fixed $`L`$, since the locality constants are uniform in the exterior volume. The defining order remains “thermodynamic limit first, interval limit second.” Periodic covariance approximations provide another controlled route: the reference covariance is finite range and the dressed covariance has exponentially small periodic image corrections. Gaussian entropy continuity makes these corrections negligible. No global trace-norm limit of the many-body states is assumed.

## 5. The exact fully shielded asymptotic

The passage from consecutive intervals to (T3) must account for both components of the buffer. It is not a general monotonicity in the conditioning system.

We first record why separated blocks of the output have exponentially small ordinary mutual information. The output covariance symbol is analytic, so for constants $`K,\mu>0`$ at fixed $`m,\epsilon`$,

```math

|C_{ij}|\le K e^{-\mu\operatorname{dist}(i,j)}.
\tag{T18}
```

For disjoint finite mode sets $`X,Y`$, let

```math

D=C_{XY}-(C_X\oplus C_Y),\qquad
n=\text{number of modes in }X\cup Y.
```

For $`\|D\|_1/n\le1/2`$, matrix eigenvalue variation and binary-entropy continuity yield

```math

I(X:Y)
\le n\,h\!\left(\frac{\|D\|_1}{n}\right).
\tag{T19}
```

This inequality requires no lower bound on covariance eigenvalues. It follows by bounding the $`\ell^1`$ change of the ordered eigenvalues by $`\|D\|_1`$, using
$`|h(s)-h(t)|\le h(|s-t|)`$, and then using concavity of $`h`$. For blocks with $`O(L)`$ modes separated by $`L`$ cells, (T18) gives
$`\|D\|_1\le\operatorname{poly}(L)e^{-\mu L}`$. Hence

```math

I(X:Y)=O(\operatorname{poly}(L)e^{-\mu' L})
\tag{T20}
```

for a positive $`\mu'`$. This applies also to the disconnected fermionic regions below.

Now take the five consecutive equal blocks in (T3), each of $`L`$ cells. Define

```math

M_2(L)=I(C_-B_-:B_+C_+),\qquad
M_1(L)=I(B_-:B_+).
\tag{T21}
```

Both pairs are separated by the central block $`A`$, so both quantities obey (T20). The defining entropies in (T1) give the exact identity

```math

\begin{aligned}
I(A:C_-\cup C_+\mid B_-\cup B_+)
={}&S(3L)+2S(2L)-2S(L)-S(5L)\\
&-M_2(L)+M_1(L).
\end{aligned}
\tag{T22}
```

Translation invariance by one coarse cell gives a second exact identity:

```math

S(3L)+2S(2L)-2S(L)-S(5L)
=\mathcal I_\rho(L,L,L)+\mathcal I_\rho(2L,L,2L).
\tag{T23}
```

Thus the two required one-sided asymptotics are already covered by (T8). Their coefficients are

```math

F(1,1,1)=\frac{11}{18},
\qquad
F(2,1,2)=\frac{184}{225},
```

```math

\frac{11}{18}+\frac{184}{225}=\frac{643}{450}.
\tag{T24}
```

Equations (T20)–(T24) prove (T9).

In particular, for every fixed allowed $`m,\epsilon`$, sufficiently large $`L`$ obeys the explicit lower bound

```math

I_{\rho_{m,\epsilon}}
(A:C_-\cup C_+\mid B_-\cup B_+)
\ge\frac{643\,\kappa_\epsilon}{900\,L^2}>0.
\tag{T25}
```

The five regions all have sizes proportional to $`L`$, and the shielding width is also proportional to $`L`$. No polynomial size prefactor multiplying an exponential in that width can dominate (T25) for arbitrarily large $`L`$. The output therefore has infinite Markov length in the fully shielded definition.

## 6. Why the input has finite Markov length

The initial covariance is a projector, so ordinary covariance clustering alone should not be used as an unexplained substitute for a CMI bound. The input admits the explicit dressing (T14) of an onsite product state by exponentially decaying hopping.

The [locality and CMI note](locality-and-cmi.md) proves an exponential bound by approximating that evolution near the buffer boundaries with local unitaries. Their light cones leave a nonempty buffer between the enlarged endpoint regions. The product state has exactly zero CMI on the enlarged partition, and entropy continuity controls the exponentially small approximation error. The resulting bound has the form

```math

I_{\omega_m}(A:C\mid B)
\le P_m(|A|,|B|,|C|)
e^{-\operatorname{dist}(A,C)/\xi_m}
\tag{T26}
```

with finite $`\xi_m`$ and a polynomial $`P_m`$.

The locality decomposition is supported by [Yi et al., arXiv:2510.22867v3](https://arxiv.org/html/2510.22867v3), Supplemental Theorem III.1 and Eqs. (III.4)–(III.11). Those expressions are specialized to the explicit exponentially decaying generator of this model. The general theorem for arbitrary almost-local evolutions states superpolynomial decay; an exponential conclusion for all gapped ground states is neither needed nor asserted.

Together with Propositions 1 and 2 of the model note, this finishes the theorem.

## 7. Coefficient audit and scope

The factors of two arise from two distinct choices: NL's unit cell contains two fine sites, and the present reference contains two orbital sectors. They should not be combined into an additional change of length.

| Quantity | Leading algebraic term, with $`n,L`$ in coarse cells |
|---|---|
| Single-orbital NL interval entropy | $`-\gamma_\epsilon\zeta(3)/(2n^2)`$ |
| Two-orbital reference interval entropy | $`-\kappa_\epsilon/n^2`$ |
| Output CMI on $`L,L,L`$ | $`11\kappa_\epsilon/(18L^2)`$ |
| Output shielded CMI on five blocks of $`L`$ | $`643\kappa_\epsilon/(450L^2)`$ |

In particular,

```math

\mathcal I_{\rho_{m,\epsilon}}(L,L,L)
=
\frac{11\zeta(3)\sin^2\epsilon}
{144(1+\cos^2\epsilon)}\,L^{-2}
+o(L^{-2}),
\tag{T27}
```

```math

I_{\mathrm{shielded}}
=
\frac{643\zeta(3)\sin^2\epsilon}
{3600(1+\cos^2\epsilon)}\,L^{-2}
+o(L^{-2}).
\tag{T28}
```

Since $`\gamma_\epsilon=\epsilon^2/16+O(\epsilon^4)`$, their weak-noise coefficients are respectively
$`11\zeta(3)\epsilon^2/288+O(\epsilon^4)`$ and
$`643\zeta(3)\epsilon^2/7200+O(\epsilon^4)`$.
For entropy measured in bits, divide every entropy and CMI coefficient by $`\log2`$. If the buffer is instead measured in fine sites, its width is $`2L`$; expressing the same asymptotic in that length multiplies the displayed $`L^{-2}`$ coefficient by four.

The result disproves sufficiency of full rank of all finite reductions for stability of Markov length in this fermionic setting. It does not concern a full-rank density matrix on the entire finite system: the initial thermodynamic state is pure. It also does not prove instability of finite-temperature Gibbs states or instability under generic local noise.

The dark momentum mode remains a tuned feature of the noise. What changes relative to the rank-deficient-input construction is that neither the input nor the output has an exactly pure degree of freedom inside any finite region. The finite-region eigenvalues approach the endpoints of the occupation interval as the region grows, and local faithfulness does not supply a size-independent spectral floor.
