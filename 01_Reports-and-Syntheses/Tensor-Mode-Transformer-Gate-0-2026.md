# Tensor-Mode Transformer Gate 0 — Static Bimetric Source and Boundary Derivation

**Date:** 2026-09-04  
**Scope:** one explicit singly coupled Hassan–Rosen-type theory, its homogeneous linearization, and a constrained static planar boundary diagnostic.  
**Decision:** **NO-GO for converting the common massless field by multiplying the interaction potential by a scalar phase coefficient.** A conditional window remains for filtering an already-present massive Yukawa component. That is a different, narrower observable and is not a demonstrated material response.

## Target

Test Idea 1 of the [July 20 architecture portfolio](../idea-stage/IDEA_REPORT.md): can a phase-programmed two-metric wall convert a stationary external gravitational field into a screened mode? The calculation must determine the physical metric's lapse and acceleration, rather than substitute transmission of a transverse wave or of one massive eigenmode.

The immediate deliverable is a **conditional proposition plus a solved source problem**. We choose the conservative coupling in which source, detector, clocks, and ordinary matter all see the same metric `g`. The gate changes a scalar prefactor of the tuned bimetric potential; the two Einstein–Hilbert coefficients and the proportional background ratio remain fixed.

## Status

**COHERENT AFTER REFRAMING / EXTRA ASSUMPTION.**

The homogeneous theory and its common/massive mode decomposition are well-defined. A scalar prefactor changes the massive eigenvalue, not the eigenvectors. The proposed optical-style mixing-angle gate therefore fails already at the action-to-linear-response step.

A finite static slab can nevertheless be solved without discarding the Fierz–Pauli constraints. The reduction used below is exact within a specified *linear, plane-symmetric, prescribed-positive-profile* problem. It is not a nonlinear solution for a material phase boundary. In particular, the scalar profile, its support apparatus, and their gravitational backreaction are not solved by assigning a function `mu(z)`.

For the synthetic `0.10 m` wall example, the massive-mode transmission is `0.00091965`, but the physical acceleration transmission is `0.55329` when the Planck-mass ratio is one and source/detector gaps are both `0.20 m`. The common massless contribution is unchanged. A source whose incoming field is almost entirely common-mode receives almost no screening.

## Invariant Object

The organizing object is the **source-referenced physical-metric response**, including its reaction ledger. For a stationary physical metric with lapse `N`, the proper acceleration of the stationary detector congruence is

\[
a_i^{\rm hold}=c_{\rm light}^2\partial_i\ln N,
\qquad N^2=-g_{00}.
\tag{1}
\]

Its free-particle acceleration relative to that congruence is opposite at leading order. Writing

\[
g_{00}=-(1+2\Phi_g/c_{\rm light}^2),
\quad a_z^{\rm free}=-\partial_z\Phi_g,
\tag{2}
\]

defines the weak-field potential used below. Lapse differences also determine stationary clock comparisons; `R_{0z0z}=Phi_g''/c_light^2` is the corresponding linear tidal component. Time normalization and the source-supported frame are held fixed between gate states. An arbitrary additive potential is not an observable.

An infinite planar source has an affine massless potential and zero exterior Newtonian tide. We use it as a local source-supported acceleration test, not as a globally asymptotically flat spacetime or a complete terrestrial geometry.

## Assumptions

1. **Exact action choice:** positive constant `M_g^2` and `M_f^2`; the Hassan–Rosen square-root potential; a canonical scalar `chi`; ordinary matter coupled only to `g`; no direct ordinary-matter coupling to `f`.
2. **Homogeneous reference branch:** `g=f=eta`, signature `(-,+,+,+)`, scalar at a constant zero-energy stationary state, and tuned potential coefficients given below. The perturbation expansion requires a real square-root branch connected to the identity.
3. **Linear probe approximation:** metric perturbations and source-induced changes are small; the massive helicity-0 sector must also lie outside any nonlinear/Vainshtein regime. Small `gL/c^2` alone does not guarantee the latter.
4. **Additional interface assumption:** for the slab diagnostic, replace the scalar-dependent mass by a prescribed positive `mu^2(z)`. Subtract the unperturbed gate field and neglect the gate's probe-dependent stress at first order. The scalar/support background is *not* claimed to be an exact flat solution of the full action.
5. **Static symmetry:** time independence, translational symmetry in `x,y`, rotation symmetry in the `x-y` plane, no momentum density, and a nonrelativistic source with only `T_00=rho` at the retained order. Holding-force stresses from the weak source field are higher order; the gate reaction is calculated separately at the first nonzero, quadratic order.
6. **Boundary problem:** `mu_out>0` on both sides, a finite barrier `mu(z)>=mu_out`, ordinary `g`-coupled source outside it, no independent `f`-sector source, and no externally imposed growing massive solution. No mass coefficient crosses zero.
7. **Numerical examples:** all masses, source densities, and distances are synthetic inputs. They are not a fit to experiments, an allowed cosmological model, or specifications of an available material.

## Notation

| Symbol | Meaning |
|---|---|
| `g=eta+h`, `f=eta+l` | Physical and second metric; `h,l` are dimensionless perturbations |
| `alpha=M_f/M_g`, `M_T^2=M_g^2+M_f^2` | Fixed kinetic normalization ratio and total squared Planck scale |
| `H=(h+alpha^2 l)/(1+alpha^2)` | Common massless perturbation |
| `D=h-l`, `w=alpha^2/(1+alpha^2)` | Relative massive perturbation and its weight in `h=H+wD` |
| `E=G^L` | Linearized Einstein tensor operator, including its constraint components |
| `F(chi)>0`, `m_*` | Scalar potential prefactor and reference inverse-length mass |
| `mu^2=m_*^2 F(1+alpha^-2)` | Massive Fierz–Pauli eigenvalue, in inverse square metres after restoring units |
| `A=D_00`, `B=D_xx=D_yy`, `C=D_zz` | Plane-symmetric static components; `D=-A+2B+C` is the trace |
| `d,a,b` | Wall thickness, source-to-wall gap, wall-to-detector gap |
| `Sigma` | Source surface rest-mass density in SI units |
| `G_infinity`, `G_Y=(4/3)alpha^2 G_infinity` | Common-mode and massive static source strengths |
| `R`, `D_out`, `T_m` | Static reflected amplitude, transmitted wall-face amplitude, transmission relative to the homogeneous exterior |
| `T_phys` | Gate-on/gate-off physical acceleration ratio at the same source and detector positions |

The covariant derivation uses `hbar=c_light=1`; `c_light` is restored explicitly in physical observables. `alpha` here is a Planck-mass ratio, not the scalar matter-coupling notation used in some chameleon papers. No background proportionality factor is denoted by `c` in this report.

## Derivation Strategy

Start from a conservative nonlinear action, identify what its scalar control can actually change, retain the complete static constraints, and only then reduce the planar problem to a second-order boundary equation. Solve that boundary equation with a specified source, reconstruct the physical lapse, and obtain the source/gate reaction from the same static response functional.

## Derivation Map

1. The tuned potential and fixed kinetic terms determine the common and relative combinations. **Identity on the chosen homogeneous branch.**
2. A scalar prefactor multiplies the relative-mode mass operator without rotating its basis. **Conditional no-conversion proposition.**
3. Divergence and trace equations constrain lapse and longitudinal components. **Identities of the full linear equations.**
4. Plane symmetry and pressureless static sourcing produce `A=2B` and a fixed `C`; the Helmholtz equation follows from these constraints. **Exact reduction under assumptions 3–6.**
5. Finite-slab matching gives transmission/reflection and the source-referenced physical response. **Solved boundary-value problem.**
6. The reduced source functional gives equal and opposite source/gate forces. **Static reaction identity; not a nonlinear material stress solution.**
7. Numerical limits, smooth-profile convergence, and reconstructed component equations verify the calculation. **Computational checks, not empirical validation.**

## Main Derivation

### 1. Action, flat branch, and scalar control

**Action choice.** Let `S=sqrt(g^-1 f)` and `e_n(S)` be elementary symmetric polynomials. Use

\[
\begin{aligned}
I={}&\frac{M_g^2}{2}\int\sqrt{-g}\,R[g]
 +\frac{M_f^2}{2}\int\sqrt{-f}\,R[f]\\
&-m_*^2 M_g^2\int\sqrt{-g}\,F(\chi)U(S)\\
&+\int\sqrt{-g}\left[-\frac12(\partial\chi)^2-W(\chi)\right]
 +I_m[g,\psi]+I_{\rm hold}[g,\chi,\zeta],\\
U(S)={}&\sum_{n=0}^4\beta_n e_n(S),
\qquad(\beta_0,\ldots,\beta_4)=(-3,1,0,0,-1).
\end{aligned}
\tag{3}
\]

All integrals include `d^4x`; `zeta` represents the still-unspecified physical control/support variables. The signs in (3) include a minus sign before `U`; the resulting quadratic relative mass is positive for `F>0`. This is the minimal Hassan–Rosen interaction with a rescaled mass convention. The original paper establishes the constant-coefficient nonlinear construction and its mode decomposition; its equations (10)–(16) are a direct normalization check. [Hassan and Rosen, original full text](https://arxiv.org/html/1109.3515v2#S4).

**Identity.** At `S=1`,

\[
U(1)=-3+4-1=0,\quad
\beta_0+3\beta_1+3\beta_2+\beta_3=0,\quad
\beta_4+3\beta_3+3\beta_2+\beta_1=0.
\tag{4}
\]

The two metric tadpoles and scalar potential term vanish on the common flat configuration for every value of `F`. A constant `chi_0` with `W=W'=0` and no holding source is therefore a valid flat reference state. The relative potential begins at quadratic order in `D`.

**Interface limitation.** A varying canonical `chi_0(z)` still has stress

\[
T^{\chi}_{\mu\nu}=\partial_\mu\chi\partial_\nu\chi
-g_{\mu\nu}\left[\frac12(\partial\chi)^2+W\right].
\tag{5}
\]

Equation (4) does not cancel this stress. Arbitrarily prescribing `chi_0(z)` while keeping both full metrics flat is generally inconsistent. With
`J_hold=-(1/sqrt(-g)) delta I_hold/delta chi`, its equation is

\[
\Box_g\chi-W'(\chi)-m_*^2M_g^2F'(\chi)U(S)=J_{\rm hold}.
\tag{6}
\]

The actual gate must solve (6), both metric equations, and the holding-sector equations. The scalar stress, potential stress, and apparatus exchange momentum; their divergences cannot be dropped independently. On a constant flat scalar background the `F' U` perturbing force starts at order `D^2`, but a background scalar gradient also couples to metric perturbations and requires its own response analysis.

Scalar-dependent graviton masses are established theory prior art. In particular, chameleon bigravity promotes the potential coefficients to scalar functions and solves scalar/matter equations in addition to the two Einstein equations. That work uses a universal conformal matter metric in its example; we set that extra coupling to unity here. It supplies no identified superconducting portal for (3). [De Felice, Mukohyama, and Uzan, equations (10)–(14), (25)–(30)](https://arxiv.org/html/1702.04490).

### 2. Common mode, massive mode, and fixed mixing

**Homogeneous linearization; then the prescribed-profile diagnostic.** Write `P_mu nu(D)=D_mu nu-eta_mu nu D`. The two metric equations at retained order are

\[
E(h)+\frac{m_*^2F}{2}P(D)=\frac{T}{M_g^2},\qquad
E(l)-\frac{m_*^2F}{2\alpha^2}P(D)=0.
\tag{7}
\]

Here `T` is a tensor, not its trace; its trace is written with indices below. For the slab calculation (7) defines the frozen-profile linear diagnostic. It does not by itself prove the background assumed in deriving it is supported by a material.

**Exact linear combinations.** Adding the equations with kinetic weights and subtracting gives

\[
\boxed{E(H)=\frac{T}{M_T^2}},\qquad
\boxed{E(D)+\frac{\mu^2(z)}{2}P(D)=\frac{T}{M_g^2}},
\quad h=H+wD.
\tag{8}
\]

No derivative of `F` enters the change of variables because its coefficients are constant. In canonically normalized variables `q_g=M_g h`, `q_f=M_f l`, the unit common and relative directions are proportional to `(M_g,M_f)` and `(M_f,-M_g)`. The mixing angle may be described by `tan(theta)=alpha`; `F` changes neither direction.

**Conditional no-conversion proposition.** For fixed positive Einstein–Hilbert coefficients, this common proportional background, single-metric matter coupling, and a scalar prefactor affecting only the potential, an arbitrary prescribed `F(z)` cannot convert an incident homogeneous solution of `H` into `D` at linear order. The common sector has no gate-dependent operator. If the added source and its boundary data are fixed and the gate adds no probe-dependent source, uniqueness gives the same `H` in both states.

The common massless sector therefore cannot be removed by making the massive eigenvalue large. This statement is broader than plane symmetry *within equation (8)*, but is not a theorem about arbitrary curved bimetric backgrounds.

The algebraic separation in (8) also survives replacing the prescribed prefactor by `F(t,z)` while retaining the same flat linear operators and source assumptions. Merely modulating this same coefficient therefore does not repair the missing common-to-relative conversion. A driven relative mode can exchange energy with a pump, and scalar/support response or nonlinear terms can add sources; those are additional calculations, not consequences of an optical Floquet analogy. The static solution below makes no claim about their stability or efficiency.

Changing individual `beta_n` while artificially holding the same proportional background fixed also leaves the quadratic mass direction fixed; only its coefficient changes. If those changes instead move the background ratio, the field equations must be re-solved. A spatially varying background ratio is not a free mixing-angle knob. For the ordinary constant-parameter proportional vacuum ansatz, the Bianchi equation enforces a constant ratio, except for degenerate special branches. [Proportional background and spectrum discussion, sections 5.3.1–5.3.2](https://arxiv.org/html/1512.00021v2#S5.SS3).

### 3. The static constraints, including variable mass

**Identity.** The linear Einstein operator is divergence-free. For a conserved source, the second equation of (8) requires

\[
\partial^\mu\left[\mu^2(D_{\mu\nu}-\eta_{\mu\nu}D)\right]=0.
\tag{9}
\]

When `mu` varies, (9) is *not* the constant-mass condition
`partial^mu D_mu nu=partial_nu D`. The trace equation is

\[
\Box D-\partial_\mu\partial_\nu D^{\mu\nu}
-\frac32\mu^2D=\frac{T^\mu{}_{\mu}}{M_g^2}.
\tag{10}
\]

Thus assigning independent decays to `D_00`, spatial components, and trace generally violates the equations. Neither `D=0` nor a scalar equation for `D_00` may be assumed in advance at a variable-mass interface.

**Exact planar component calculation.** For `D_mu nu=diag(A,B,B,C)` with all fields depending on `z`, direct evaluation gives

\[
G^L_{00}=-B'',\qquad
G^L_{xx}=G^L_{yy}=\frac12(B''-A''),\qquad
G^L_{zz}=0.
\tag{11}
\]

For `T_00=rho`, all other retained components zero, the independent equations are

\[
\begin{aligned}
-B''+\frac{\mu^2}{2}(2B+C)&=\rho/M_g^2,\\
\frac12(B''-A'')+\frac{\mu^2}{2}(A-B-C)&=0,\\
\frac{\mu^2}{2}(A-2B)&=0.
\end{aligned}
\tag{12}
\]

Because `mu^2>0`, the last equation constrains the lapse: `A=2B`. Eliminating `C` using the remaining equations yields

\[
\boxed{B''-\mu^2 B=-\frac{2\rho}{3M_g^2}},\qquad
\boxed{A=2B,\quad C=\frac{2\rho}{3M_g^2\mu^2}}.
\tag{13}
\]

The source trace is `D=C`. This is an algebraic longitudinal/contact response inside the source, not a freely imposed additional boundary datum. In the source-free wall and detector region,

\[
\boxed{A''-\mu^2(z)A=0,\quad B=A/2,\quad C=D=0.}
\tag{14}
\]

A finite-density source must satisfy the independent local linearity condition

\[
|C|=\left|\frac{2\rho}{3M_g^2\mu^2}\right|\ll1,
\quad\text{or in SI}\quad
|C|=\frac{16\pi(1+\alpha^2)G_\infty\rho_{\rm mass}}
{3c_{\rm light}^2\mu^2}\ll1.
\tag{14a}
\]

A tiny exterior lapse perturbation does not ensure (14a). The ideal sheet below is only an exterior Green-function construction; its delta-function `C` is not asserted to be a physical linear metric in the source. The numerical checks also solve a regular finite-density source, as described in section 7.

This is a constrained static lapse equation, not a transverse-wave analogy. The nontrivial variable-mass divergence component is exactly
`partial_z[mu^2(C-D)]=0`, including any `mu'` terms. The trace identity is also satisfied. All time-space and off-diagonal equations vanish under the imposed symmetry, rather than being discarded dynamical modes.

For finite positive step coefficients without independent surface stress, (12) requires continuity of `A` and `A'` (equivalently `B,B'`). Their jumps would otherwise produce delta or derivative-of-delta terms. A real stressed interface can change that matching and lies outside this diagnostic. Crossing `mu=0` invalidates the division in (13) and the constraint rank used here; it is deliberately excluded.

### 4. A specified source and physical lapse

The common planar solution can be put in the usual static isotropic gauge, with `H_00=H_xx=H_yy=H_zz=A_H` and

\[
A_H''=-\rho/M_T^2.
\tag{15}
\]

Define `Phi_H=-c_light^2 A_H/2` and `Phi_Y=-c_light^2 w A/2`. Restoring SI source density, (13) and (15) become

\[
\Phi_H''=4\pi G_\infty\rho_{\rm mass},\qquad
(\partial_z^2-\mu^2)\Phi_Y=4\pi G_Y\rho_{\rm mass},
\quad G_Y=\frac43\alpha^2G_\infty.
\tag{16}
\]

The `4/3` factor follows here from the static lapse constraints, not from a tensor-wave source overlap. `G_infinity` equals `1/(8pi M_T^2)` in natural units. It is not automatically the locally measured Newton constant if a substantial massive mode or nonlinear screening is present.

Place a source sheet at `z=-a`, a wall in `0<z<d`, and a test detector at `z=d+b`. The sheet is the external-field limit of a thin smooth planar source; its contact term in (13) should be resolved for an interior source model. Outside the source, the homogeneous no-wall massive potential is

\[
\Phi_Y^{(0)}(z)=-\frac{2\pi G_Y\Sigma}{\mu_0}
e^{-\mu_0|z+a|}.
\tag{17}
\]

On the detector side the common acceleration magnitude is
`g_H=2pi G_infinity Sigma`. The massive/common acceleration ratio with the wall off is

\[
r=\frac43\alpha^2e^{-\mu_0(a+d+b)}.
\tag{18}
\]

The source launches both sectors because it couples to `g`, not to an artificially prepared pure massive mode. At fixed source density the reflected massive field modifies the force on the source, but not its prescribed density or its derivative jump at this order. The source support supplies the balancing force.

### 5. Exact finite step-slab solution

Normalize the incident massive potential at the left wall face to one. Between source and wall write

\[
y(z)=e^{-\mu_0z}+R e^{\mu_0z};
\qquad y(z)=D_{\rm out}e^{-\mu_0(z-d)}\quad(z>d).
\tag{19}
\]

Across a uniform wall of inverse length `mu_w`, continuity gives

\[
\begin{pmatrix}y(d)\\y'(d)\end{pmatrix}
=\begin{pmatrix}
\cosh x&\sinh x/\mu_w\\
\mu_w\sinh x&\cosh x
\end{pmatrix}
\begin{pmatrix}y(0)\\y'(0)\end{pmatrix},\quad x=\mu_wd.
\tag{20}
\]

Solving the two boundary conditions gives

\[
D_{\rm out}=\frac{2\mu_0}{2\mu_0\cosh x+
(\mu_w+\mu_0^2/\mu_w)\sinh x},
\tag{21}
\]

\[
R=\frac{(\mu_0^2-\mu_w^2)\sinh x}
{2\mu_0\mu_w\cosh x+(\mu_w^2+\mu_0^2)\sinh x},
\quad T_m=e^{\mu_0d}D_{\rm out}.
\tag{22}
\]

`T_m` compares the wall-on massive response with propagation through the same distance filled with the exterior phase. It includes impedance/matching effects as well as the wall's exponential factor. `R` is a static Green-function amplitude; its square is not a propagating energy reflectance.

Both the massive lapse and its exterior gradient are multiplied by `T_m`, since the exterior inverse length is the same in both states. The full physical acceleration is therefore

\[
\boxed{T_{\rm phys}=\frac{1+rT_m}{1+r}},
\qquad
\boxed{T_{\rm phys}\ge\frac{1}{1+r}\quad(\mu_w\ge\mu_0>0).}
\tag{23}
\]

The bound follows from positivity of the static massive Green function and the barrier: `0<T_m<=1`. Its common-mode term is exactly unmodified. The same positivity argument extends to the smooth nonnegative barriers solved numerically below.

**Operational consequences.**

- Making the massive penetration length arbitrarily short approaches the nonzero floor in (23); it does not eliminate the common field.
- For a pure common-mode incident field, the wall response is exactly unchanged in this approximation.
- For a distant localized source whose massive component has already decayed, `r` is small and `T_phys` approaches one. A real extended terrestrial source requires spatial integration and, where applicable, nonlinear matching; inserting Earth's radius into (18) would not be such a calculation.
- Even in the zero-gap limit, `alpha=1` gives a floor `3/7`; `alpha=0.1` gives `0.986842`. A 99% reduction requires at least `r>=99` even for an ideal infinitely suppressing wall. That demands a source field dominated by the massive interaction. It is not a way to attenuate an already-established massless field.
- A plane source's massless exterior tide vanishes. Suppressing the massive tide by `T_m` while leaving a common acceleration is therefore possible; a small tide alone does not demonstrate interior weightlessness.

### 6. Gate stress, source recoil, and support forces

The same reduced static source kernel admits the functional, per unit transverse area,

\[
\mathcal E_Y[\Phi_Y]=\int dz\left[
\frac{(\Phi_Y')^2+\mu^2(z-Z)\Phi_Y^2}{8\pi G_Y}
+\rho_{\rm mass}\Phi_Y\right].
\tag{24}
\]

Varying `Phi_Y` gives (16). On shell its interaction energy is `1/2 int rho Phi_Y`; `Z` is the gate position. This is the constrained static exchange functional, not a proposed positive local energy density for the full gravitational field or an independent scalar-mediator theory.

With incident potential
`I=-2pi G_Y Sigma exp(-mu_0 a)/mu_0`, the source's reflected contribution is

\[
\Phi_Y^{\rm ref}(-a)=-\frac{2\pi G_Y\Sigma}{\mu_0}
R e^{-2\mu_0a}.
\tag{25}
\]

Differentiating the source interaction energy or evaluating the reflected acceleration gives

\[
\frac{F_{\rm source}^{Y}}{\mathcal A}
=2\pi G_Y\Sigma^2 R e^{-2\mu_0a}.
\tag{26}
\]

The wall's force from (24) is

\[
\frac{F_{\rm gate}^{Y}}{\mathcal A}
=\frac{1}{8\pi G_Y}\int dz\,(\mu^2)'\Phi_Y^2.
\tag{27}
\]

For the finite step this is
`(mu_w^2-mu_0^2)[Phi_Y(0)^2-Phi_Y(d)^2]/(8pi G_Y)`.
For any differentiable source-free profile,

\[
\frac{d}{dz}\left[(y')^2-\mu^2y^2\right]=-(\mu^2)'y^2,
\qquad\int_0^d(\mu^2)'y^2dz=-4\mu_0^2 R.
\tag{28}
\]

Equations (26)–(28) therefore give

\[
\boxed{F_{\rm gate}^{Y}=-F_{\rm source}^{Y}.}
\tag{29}
\]

For the stiffer barrier `R<0`: the reflected Yukawa contribution repels the source from the gate, and pushes the gate toward the detector side. The stationary source support supplies `-F_source`, and the gate support supplies `-F_gate`. Releasing the supports changes the problem into a dynamical source/gate system; it does not remove the opposite momentum.

This ledger concerns the *increment associated with the prescribed massive barrier*. A real gate also has its own mass, scalar-gradient stress, elastic stress, and common gravitational interaction. Those must be added, not identified with the small force in (27). The test detector has negligible backreaction here. At finite detector mass, the symmetric Green function adds detector/source/gate reaction terms. The switching work is set by the change in the on-shell field energy plus the scalar and actuator free energies; no static force calculation determines those unknown material costs.

### 7. Reproducible results and nontrivial checks

The [calculation](../02_Gravitation-Theory/Tensor-Mode-Transformer/tensor_mode_transformer.py) independently compares (21) with SciPy's collocation solution of (14), reconstructs the static tensor components, and checks the force integral. [Machine-readable results](../02_Gravitation-Theory/Tensor-Mode-Transformer/results.json) and [physical-response table](../02_Gravitation-Theory/Tensor-Mode-Transformer/physical_transfers.csv) are generated by the same run.

Reference inputs are `mu_0=1 m^-1`, `d=0.10 m`, `mu_w=ln(100)/d=46.0517 m^-1`, and `a=b=0.20 m`. The wall eigenmass energy is `hbar c_light mu_w=9.08724 micro-eV`. This familiar penetration-scale number fixes no full physical-field attenuation by itself.

| Synthetic result | Value |
|---|---:|
| Massive response `T_m` | `0.000919653586` |
| Reflected static amplitude `R` | `-0.957485600` |
| Physical response, `alpha=0.1` | `0.991985178` |
| Physical response, `alpha=1` | `0.553292174` |
| Physical response, `alpha=10` | `0.013122794` |
| Physical response, `alpha=1`, source gap `5 m` | `0.993394624` |
| Physical response, `alpha=1`, source gap `20 m` | `0.999999997966` |

For a purely illustrative `Sigma=100 kg/m^2` and `G_infinity=6.67430e-11 SI`, the `alpha=1` common acceleration is `4.19359e-8 m/s^2`; total acceleration changes from `7.58497e-8` to `4.19671e-8 m/s^2`. Source and gate interaction forces are respectively `-3.58871e-6` and `+3.58871e-6 N/m^2`. Those numbers describe hypothetical response coefficients, not an experimentally available force.

| Verification | Result |
|---|---|
| No barrier (`mu_w=mu_0`) at three masses | `T_m=1`, `R=0` to machine precision |
| Zero wall thickness | `T_m=1`, `R=0` exactly |
| Zero matter overlap (`alpha=0`) | Physical response exactly one |
| Long source separation | Physical response approaches one |
| Static sourced-component check | Manufactured smooth positive density satisfies all three FP component equations, trace, and variable-mass divergence to floating-point precision |
| Regular source plus smooth gate | A finite `cos^2` density source and the entire gate are solved on one domain; its transmitted lapse agrees with an independent source-moment calculation followed by the wall transfer |
| Independent BVP vs exact step | Transmission relative error decreases from `1.89e-6` to `3.28e-9` to `8.05e-12` as tolerance is tightened |
| Off-mesh reconstructed FP residual | Approximately `8.8e-10` relative at the tightest convergence run |
| Static force/recoil identity | Step example closes at relative error below `1e-14` |
| Smooth-profile force integral | Relative discrepancy below `4e-13` in the tested ramps |

The smooth profiles have `C1` sine-squared ramps with width `w_r` at each face and a constant middle. With `w_r/d = 0.25, 0.10, 0.04, 0.01`, the massive transmission is respectively `0.00269907, 0.00143040, 0.00109965, 0.000961950`, tending toward the independently derived sharp value `0.000919654`. This is profile-to-step convergence, distinct from numerical mesh/tolerance convergence. It verifies matching rather than assuming an exponential for the lapse without its other components.

For the regular source check, `rho_mass=(Sigma/s) cos^2[pi(z+a)/(2s)]` on `|z+a|<s`, zero outside, with `s=0.01 m`. Its exterior incident amplitude differs from the ideal-sheet amplitude by the exactly integrated form factor `[sinh(mu_0 s)/(mu_0 s)] pi^2/[pi^2+(mu_0 s)^2]`. The full-domain solution is compared with that independent source moment and the separate smooth-wall solution. At `Sigma=100 kg/m^2` and `alpha=1`, its peak density is `10,000 kg/m^3` and `max|C|=2.49e-22`, so the local contact-metric condition is satisfied for this synthetic input. This does not establish the gate's separate microscopic or nonlinear consistency.

## Remarks and Interpretation

The project now has a solved counterexample to the assumption that a material-dependent bimetric mass automatically creates a controllable mixing angle. Two propagating sectors alone do not give two independently programmable static channels. In the chosen action, the scalar coefficient controls the stiffness of `h-l`; the common metric direction remains fixed and continues to couple to ordinary matter.

The narrower effect is physically different: a phase-sensitive wall could, **if its coefficient were realized and the full background remained consistent**, filter a Yukawa contribution already sourced outside. A substantial state-dependent signal would then be a constraint on that massive interaction and its gate. It would not imply that standard common-mode gravity had been blocked.

The original wave-oscillation literature concerns different production/detection and propagation bases for radiative tensors; it does not establish static lapse conversion at a material boundary. [Max, Platscher, and Smirnov](https://arxiv.org/abs/1703.07785). The present result is a project-specific static reduction and audit of that extrapolation, not a claim of novelty for massive/massless bimetric eigenstates or scalar-dependent graviton mass.

## Go/No-Go Decision and Minimal Repair

| Gate | Result | Operational consequence |
|---|---|---|
| Explicit conservative metric and matter sector | Pass for constant scalar and fixed coefficients | One physical metric and a specified flat branch are available |
| Scalar-prefactor mode rotation | **Fail** in the chosen linearization | Close `F(chi) U` as a common-to-massive converter |
| Static constrained slab solution | **Pass conditionally** | A massive lapse response, matching law, and physical transfer are computed |
| Filtering the common massless component | **Fail** under the frozen-profile assumptions | Do not infer 99% physical shielding from `mu d=ln(100)` |
| Source/support/recoil within reduced model | Pass | The source and gate receive equal and opposite incremental forces |
| Real material `F(chi)` and finite stress-supported background | Unresolved | No experimental build is licensed by the synthetic parameter window |
| General scalar/vector/tensor perturbative stability of a supported interface | Unresolved | Positive planar `mu^2` is insufficient for a general stability claim |
| Whole-craft field-supported worldtube | Unresolved | No shell, interior worldtube, startup, or thrust solution is produced |

**Recommended next minimal repair:** if a tensor converter remains the target, replace the assumed mixing profile with one explicit, dynamically solved background that actually changes the kinetic/background eigenvectors while maintaining a unique physical matter metric. The smallest serious calculation is a smooth one-dimensional solution for `g_0(z), f_0(z), chi_0(z)` and its support source, followed by the complete linear static response about it. A universal scalar–tensor completion of the kinetic sector is a possible model class to investigate, not a validated repair; its extra degree of freedom, matter response, and constraint structure must be included. Simply inserting `theta(z)`, `alpha(z)`, or a varying proportionality factor into (8) does not qualify.

Before a broader nonlinear search, apply one filter to any proposed repair: write the linear equation sourcing a change in the common physical lapse and identify the external stress or boundary datum on its right-hand side. If that term is only the gate's ordinary added energy and pressure, the work has become direct stress-source engineering. It should be assessed against the [worldtube source benchmark](Worldtube-Source-Theorem-and-Phase-Localized-Metric-Higgs-Gate-0-2026.md), rather than described as conversion.

A second, narrower continuation is to take the surviving Yukawa-transmission target seriously: choose a published scalar-controlled bimetric model, compute a supported gate and source profile, and map existing inverse-square, light-deflection, scalar-force, and stability limits before proposing apparatus. The present large-overlap table is deliberately not such a viability map.

## Boundaries and Non-Claims

- The exact nonlinear claim here is the chosen constant-coefficient HR structure and its homogeneous branch. The finite varying-profile slab is a conditional linear diagnostic, not a covariant material solution.
- The no-conversion proposition uses fixed kinetic coefficients, fixed proportional background, fixed matter coupling, and negligible probe-dependent gate stress. It does not exclude nonproportional backgrounds, scalar–tensor kinetic sectors, additional sources, or other theories.
- A nonzero massless overlap alone does not set a parameter-independent numerical floor: `alpha` and the incoming source decomposition matter. The floor in (23) is specific to the stated positive barrier and same-sign ordinary source problem.
- Plane symmetry tests the static scalar/lapse sector. It does not solve transverse spatial Fourier modes, finite spherical junctions, edges, vector modes on a nonuniform background, or the full tensor response of an arbitrarily oriented source.
- The infinite source plane is a local approximation with forces per area. Its affine common potential is only used over a weak-field laboratory interval. The sheet's interior delta/contact metric is not treated as a literal weak nonlinear material solution; a smooth finite source resolves it.
- An exterior coefficient of exactly zero is outside the analysis. Taking small positive `mu` does not establish a healthy zero-mass interface or evade the vDVZ/nonlinear limit.
- The scalar support term in (3) is a named missing physical sector. Its Hamiltonian consistency, coupling to `chi`, energy, and equation of state are not established by this report. Ghost freedom of a constant HR potential is not a certificate for arbitrary actuator couplings.
- Linear massive gravity around an unscreened compact source has an extra scalar contribution. Nonlinear Vainshtein screening can change the source response and restore local GR; parameters and branch matter. The characteristic estimate `r_V ~ (r_s/mu^2)^(1/3)` is at most an order-of-magnitude guide for a finite source, not a check for this infinite planar source. [Babichev and Crisostomi, nonlinear source analysis](https://arxiv.org/abs/1307.3640).
- The Planck-normalized phase coefficient, its radiative stability, and its scalar-gradient stress are not inferred from a superconducting transition. Neither the micro-eV inverse-length scale nor the tiny dimensionless metric makes those costs disappear.
- Static support can require force without steady mechanical work. Gate formation, modulation, and recoil remain in the complete momentum/energy ledger. No reactionless propulsion, terrestrial hovering craft, or protected accelerating interior has been demonstrated.

## Open Risks

1. The full scalar-supported background could change the static response or be unstable. That is why the main decision is scoped to the specified prefactor implementation, rather than all bimetric theories.
2. A large pre-existing massive overlap may already conflict with source and metric tests, unless a specific environmental/nonlinear mechanism modifies it. Those mechanisms could simultaneously suppress the external signal the gate hopes to filter.
3. The holding apparatus may supply the very stress that changes the physical field. Any follow-up must measure or derive it rather than subtract it conceptually.
4. Extending the planar calculation to finite geometry introduces constraints not represented by one scalar `mu(z)` equation. A spherical source/shell calculation is subsequent work, not an omitted routine numerical detail.

## Reproducibility and Source Provenance

Run `C:/Python314/python.exe 02_Gravitation-Theory/Tensor-Mode-Transformer/tensor_mode_transformer.py` from the project root. The script needs NumPy and SciPy; the verified run used NumPy `2.4.3` and SciPy `1.17.1`. It writes results beside itself and checks its own analytic limits, static components, BVP convergence, profile convergence, and reaction identity. No source PDFs, papers, or user data are changed.

Primary web pages were opened on **2026-09-04**. Equations in this report after the action/mode setup were independently derived for the stated model; numerical tables are generated synthetic calculations.

1. S. F. Hassan and R. A. Rosen, *Bimetric Gravity from Ghost-free Massive Gravity*, JHEP **02** (2012) 126. [arXiv:1109.3515](https://arxiv.org/abs/1109.3515), [full text](https://arxiv.org/html/1109.3515v2), [DOI](https://doi.org/10.1007/JHEP02(2012)126). Direct source for the conservative potential, kinetic normalization, and original mass-eigenstate structure.
2. A. Schmidt-May and M. von Strauss, *Recent developments in bimetric theory*, J. Phys. A **49** (2016) 183001. [arXiv:1512.00021](https://arxiv.org/abs/1512.00021), [full text](https://arxiv.org/html/1512.00021v2), [DOI](https://doi.org/10.1088/1751-8113/49/18/183001). Technical cross-check of proportional-background constraints and mass normalization; an author review, not experimental evidence.
3. A. De Felice, S. Mukohyama, and J.-P. Uzan, *Extending applicability of bimetric theory: chameleon bigravity*. [arXiv:1702.04490](https://arxiv.org/abs/1702.04490), [full text](https://arxiv.org/html/1702.04490). Direct prior art for scalar-dependent bimetric coefficients and simultaneous scalar/metric conservation equations; its specific matter/scalar model differs from the prefactor diagnostic here.
4. Q.-G. Huang, Y.-S. Piao, and S.-Y. Zhou, *Mass-Varying Massive Gravity*, Phys. Rev. D **86** (2012) 124014. [arXiv:1206.5678](https://arxiv.org/abs/1206.5678), [DOI](https://doi.org/10.1103/PhysRevD.86.124014). Precedent for a constrained scalar-dependent mass in a specific massive-gravity model, not a proof for this unsolved support sector.
5. K. Max, M. Platscher, and J. Smirnov, *Gravitational Wave Oscillations in Bigravity*, Phys. Rev. Lett. **119** (2017) 111101. [arXiv:1703.07785](https://arxiv.org/abs/1703.07785), [DOI](https://doi.org/10.1103/PhysRevLett.119.111101). Radiative-mode motivation only.
6. E. Babichev and M. Crisostomi, *Restoring General Relativity in massive bi-gravity theory*, Phys. Rev. D **88** (2013) 084002. [arXiv:1307.3640](https://arxiv.org/abs/1307.3640), [DOI](https://doi.org/10.1103/PhysRevD.88.084002). Nonlinear source/Vainshtein limitation on a linear-source extrapolation.
