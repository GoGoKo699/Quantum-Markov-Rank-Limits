# Numerical evidence and reproduction

`results.json` contains completed finite-size calculations for the four-mode
finite-depth construction and a two-mode balanced Lindblad illustration.
The calculations use the infinite-chain covariance symbol, discretize its
Fourier integral, and restrict the resulting correlation matrix to a finite
interval. They do **not** replace the analytic full-rank argument or prove
an infinite-distance decay law by finite-size fitting.

## Reproduce

Python 3 with NumPy and SciPy is sufficient. The archived calculations used
Python 3.12.14, NumPy 2.3.5, and SciPy 1.17.0. From the repository root:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
  python code/reproduce.py --checks-only
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
  python code/reproduce.py \
  --output data/results.json
```

The first command checks covariance identities, unitality, the zero-noise
limit, covariance positivity up to roundoff, the dark occupations, and the
balanced occupation spectrum. It does not run the entropy sweeps or write
files. The second reproduces all archived entropy rows. Small differences
in the last digits are expected across numerical libraries and platforms.

All entropies use natural logarithms. For a covariance restriction with
occupation eigenvalues $`\nu_j`$, the code evaluates

```math

S(L)=\sum_j[-\nu_j\log\nu_j-(1-\nu_j)\log(1-\nu_j)],
\qquad I_n=2S(2n)-S(n)-S(3n).
```

Thus $`I_n`$ is the CMI of **three equal contiguous intervals**. The code
does not numerically identify a disconnected spin marginal with a fermionic
one. The two-sided shielding argument is analytic.

## Finite-depth data

One coarse cell has four physical modes: two NL subcells and two SSH orbital
flavors. The input covariance is $`I_2\otimes P_{\rm SSH}(k)`$, with $`m=2`$.
Noise strengths are $`\epsilon=0.2,0.4,0.8`$, and
$`n=8,16,32,64,96`$ counts coarse cells.

The implementation directly applies both affine covariance layers and
independently checks

```math

C_{\rm out}(k)=C_{\rm NL}(k)\otimes[I-P_{\rm SSH}(k)]
  +[I-C_{\rm NL}(k)]\otimes P_{\rm SSH}(k).
```

It also compares $`C_{\rm NL}`$ against the explicit formula in
Newsom--Levin equations (9)--(11), rather than only comparing two algebraic
rearrangements of the same implementation. The NL formula is transposed to
the convention specified below. In the full-grid
checks, maximum differences were below $`3.4\times10^{-16}`$.

The field `undressed_n2_limit` is the analytic equal-interval coefficient
for the two independent undressed NL copies,

```math

\frac{11\gamma\zeta(3)}{18},\qquad
\gamma=\frac{\sin^2\epsilon}{8(1+\cos^2\epsilon)}.
```

The dressed finite-size values approach this reference:

| $`\epsilon`$ | $`n^2 I_n`$, $`n=96`$ | Reference coefficient |
|---:|---:|---:|
| 0.2 | 0.001869266824 | 0.001848601390 |
| 0.4 | 0.007529487717 | 0.007533608151 |
| 0.8 | 0.031451949617 | 0.031811292196 |

A statement about the dressed asymptotic coefficient requires the analytic
CMI comparison argument; it does not follow from this table alone.

## Balanced Lindblad illustration

This separate illustration has **two physical modes per cell** and uses

```math

C_t(k)=\tfrac12I+e^{-t(2-2\cos k)}
  [P_{\rm SSH}(k)-\tfrac12I].
```

It is balanced gain and loss, hence unital. Its damping convention is fixed
by this equation; the time parameter should not be imported into a
differently normalized Lindblad generator without conversion. The data use
$`t=0,0.02,0.1,0.4`$ and $`n=8,16,32,64,96,128`$. The field
`predicted_scaled_limit` is the reference coefficient
$`11t\zeta(3)/36`$.

| $`t`$ | $`n^2 I_n`$, $`n=128`$ | Reference coefficient |
|---:|---:|---:|
| 0.02 | 0.007299177814 | 0.007345903297 |
| 0.10 | 0.036123479716 | 0.036729516485 |
| 0.40 | 0.143227044493 | 0.146918065942 |

At $`t=0`$, the CMI is approximately $`1.49\times10^{-6}`$ for $`n=8`$
and $`1.59\times10^{-11}`$ for $`n=16`$. Larger buffers reach cancellation
noise in double precision. Tiny negative values are retained in the data
and are numerical roundoff, not physical negative CMI.

## Numerical limits and provenance

The Fourier grid has 32,768 points; arrays use double precision. Covariance
eigenvalues outside $`[0,1]`$ by more than $`10^{-11}`$ raise an error.
Excursions within that tolerance are clipped before evaluating the entropy.
This clipping is solely a numerical convention and cannot certify that a
finite reduced density matrix is strictly positive.

The largest diagonalizations are 1152 by 1152 for the finite-depth data and
768 by 768 for the balanced data. The published entropy values were
assembled from the completed 2026-11-04 calculations; no additional large
parameter sweep was used to select the reported strengths. The quick
identity and limiting-case checks were run again with the public script.
An earlier pure-gain exploratory calculation is not part of these balanced
data or of this reproduction script.

The public script follows the model convention
$`C_{ij}=\langle c_j^\dagger c_i\rangle`$,
$`c(k)=\sum_j e^{-ikj}c_j`$, and
$`[X_1(k)]_{01}=-\sin^2(\epsilon/2)e^{-ik}`$.
Real-space covariance blocks are therefore computed by IFFT. The initial
exploration used the opposite phase in $`X_1`$ and FFT. Those historical
entropy values remain valid. At the symbol level, changing only the noise
phase gives, with $`S_p=\sigma_x\otimes I_{\rm orbital}`$,
$`C_{\rm new}(k)=S_p C_{\rm old}(k)S_p^\dagger`$, because
$`X_1(-k)=\sigma_xX_1(k)\sigma_x`$, $`X_0`$ commutes with $`\sigma_x`$,
and the input is proportional to identity on the parity factor.
For the actual combined change of phase **and** transform, an even simpler
real-space equivalence holds. Since
$`P_m(-k)=\sigma_xP_m(k)\sigma_x`$, changing variables $`k\mapsto-k`$
in the old FFT shows
$`C_{{\rm new},d}=S_a C_{{\rm old},d}S_a^\dagger`$, with
$`S_a=I_{\rm parity}\otimes\sigma_x`$. It is an onsite orbital swap,
so every complete-cell restriction, including a disconnected union, has
exactly the same eigenvalues and entropy. For the balanced two-mode data,
the same statement uses $`S_a=\sigma_x`$.
The public quick checks verify both the symbol parity swap and the actual
real-space orbital swap. Retained finite-size rows were checked under the
aligned convention without rerunning the full entropy sweep.

## Primary source

D. C. Newsom and M. Levin, *An Instability of the Quantum Markov Length*,
[arXiv:2610.12929v3](https://arxiv.org/html/2610.12929v3), equations (9)--(16),
Appendix A (affine layers), Appendix E (interval-entropy asymptotics),
Appendix G (random-unitary and unital gates), and Appendix H (continuous-time
analogue). The four-mode input, its exact covariance decomposition, and the
local-faithfulness analysis are developed in the companion science notes.
