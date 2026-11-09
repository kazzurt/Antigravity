# Ning Li — Annotated Derivation Audit

**Date:** 2026-07-15  
**Primary sources:** Li and Torr (1991, 1992); Torr and Li (1993)  
**Purpose:** reconstruct the published derivation exactly enough to identify what is algebra, what is conventional physics, what is an approximation, and what requires a new physical postulate.

## Target

The published target is a measurable electromagnetic-to-gravitational cross-response in a superconductor:

\[
\mathbf E_g^{\mathrm{ind}}
= \mathcal X_{g\leftarrow em}\,\mathbf E_0,
\qquad
\mathbf B_g^{\mathrm{ind}}
= \mathcal X_{g\leftarrow em}\,\mathbf B_0,
\]

where, in Li and Torr's local, isotropic, half-space model,

\[
\boxed{
\mathcal X_L
= \frac{\mu_g}{\mu}\frac{m}{q}
}
\tag{T1}
\]

has units of charge per mass in their SI-like GEM convention. Here `m` and `q` are the Cooper-pair mass and charge, `μ` is the magnetic permeability assigned to the superconductor, and `μ_g` is its proposed gravitomagnetic permeability.

The audit asks whether the papers derive `X_L`, or whether they assume the material response needed to make it large.

## Status

**NOT YET COHERENT**

The 1991 coupled-field solution is algebraically coherent within its stated weak-field model **if** `μ_g` and `μ` are granted as valid material coefficients. The complete 1991–1993 amplification derivation is not coherent as published because:

1. the superconducting condensate phase is reassigned to individual lattice-ion coordinates without a many-body locking law;
2. the uncertainty principle is incorrectly used to require nonzero winding;
3. the ionic countercurrent needed for charge cancellation is asserted rather than dynamically derived;
4. Meissner screening is represented as an extremely small local scalar permeability;
5. the final coherent-ion field estimate is inconsistent with the total angular momentum and laboratory geometry by roughly 21–24 orders of magnitude.

The target can be reframed coherently as a conditional theory, but it requires at least two explicit new ingredients: a real condensate–lattice entrainment mode and a derived gravitational response law for that mode.

## Invariant Object

The organizing object is the complete linear cross-response from an electromagnetic drive to a physical gravitational observable:

\[
\boxed{
\mathcal X_{gA}(\omega,\mathbf k)
= \underbrace{\mathcal G_{gT}(\omega,\mathbf k)}_{
\text{stress-energy to gravitational field}}
\underbrace{\chi_{TA}(\omega,\mathbf k)}_{
\text{EM drive to total stress-energy}}
}
\tag{I1}
\]

This factorization keeps two questions separate:

- **Matter response:** does the superconducting state create an unusual charge-neutral mass or angular-momentum current?
- **Gravity response:** does that real source create only the standard weak GR field, or is the source-to-field law itself modified?

Li's single ratio `μ_g/μ` blends these two operations. Equation (T1) is therefore treated as Li's local proxy for (I1), not as the fundamental object.

## Assumptions

### Explicit approximations shared by the papers

- Weak gravitational field and low carrier velocity.
- Linearized gravitoelectromagnetic notation.
- An ideal, pure, homogeneous superconductor.
- Local, isotropic scalar material coefficients `μ`, `ε`, `μ_g`, and `ε_g`.
- Predominantly `s`-wave, spin-singlet Cooper pairing.
- London gauge and a macroscopic condensate description.
- A half-infinite planar sample for the analytic field solutions.
- Small gravitational perturbations and, at several stages, neglected displacement-current changes.

### Additional assumptions needed by the published amplification

- `A1 — gravitational constitutive analogy:` a superconductor possesses a local gravitomagnetic permeability `μ_g` analogous to magnetic permeability.
- `A2 — ion-phase ownership:` the superconducting order-parameter phase may be differentiated with respect to an individual lattice-ion coordinate.
- `A3 — forced nonzero winding:` every relevant ion occupies a state with winding `n >= 1`.
- `A4 — coherent ionic counterflow:` lattice-ion charge current nearly cancels Cooper-pair charge current throughout the screening state.
- `A5 — mass-current addition:` the corresponding mass currents add because the carriers' masses have the same sign.
- `A6 — permeability representation:` current cancellation can be encoded as `μ_r << 1`, with Meissner screening behaving like an ordinary local permeability.
- `A7 — coherent source summation:` approximately `10^28` ionic angular momenta contribute with a common field geometry.

Only `A5` is kinematically automatic **if** the counterflow in `A4` physically exists. The other assumptions require derivation or replacement.

## Notation

- `ψ = |ψ| exp(iφ)`: superconducting order parameter.
- `m, q`: Cooper-pair mass and charge; `q < 0` in the papers' convention.
- `m_i, q_i`: lattice-ion mass and effective charge. The papers use subscript `t` in 1992 and `i` in 1993; this audit uses `i`.
- `A, φ_e`: electromagnetic vector and scalar potentials.
- `A_g, φ_g`: weak-field gravitational vector and scalar potentials in the authors' GEM convention.
- `E, B`: electric and magnetic fields.
- `E_g, B_g`: gravitoelectric and gravitomagnetic fields.
- `j_{e,f}, j_{m,f}`: free Cooper-pair charge and mass currents.
- `j_{e,M}, j_{m,M}`: proposed bound ionic charge and mass currents.
- `μ_r = μ/μ_0`, `μ_{g,r} = μ_g/μ_{g,0}`: relative magnetic and gravitomagnetic permeabilities.
- `γ_c = q/(2m)`, `γ_i = q_i/(2m_i)`: carrier and ion gyromagnetic ratios.
- `λ_L`: London penetration depth.
- `Q = q^2|ψ|^2/m`: Li–Torr kernel for the condensate current.

Equation signs and factors in GEM depend on convention. This audit preserves the papers' convention when tracing their algebra and uses order-of-magnitude expressions when comparing to standard weak-field gravity.

## Derivation Strategy

The reconstruction follows the papers chronologically:

1. **1991:** derive the coupled magnetic/gravitomagnetic field solution and expose the undetermined coefficient `μ_g/μ`.
2. **1992:** trace the attempt to derive `μ_g/μ` from lattice-ion angular momentum, bound/free current cancellation, and the `σ–μ` model.
3. **1993:** trace the time-dependent gravitoelectric prediction and the numerical magnitude estimate.
4. **Conventional reconstruction:** retain every supported coupling while removing the ionic and permeability assumptions.
5. **Minimum-new-physics reconstruction:** state the smallest extra laws that would make Li's physical mechanism calculable without using invalid steps.

Each nontrivial step is labeled:

- **Identity:** algebra once the preceding definitions are accepted.
- **Proposition:** follows only under stated physical conditions.
- **Approximation:** a restricted model or neglected term.
- **Interpretation:** a physical reading, not a deduction.
- **Extra assumption:** not derived in the cited chain.
- **Blocker:** the conclusion does not follow, even if unconventional physics is allowed.

## Derivation Map

| Gate | Published move | Type | Audit result |
|---|---|---|---|
| G1 | Weak-field Lorentz-like force for charge and mass | Approximation | Retain with convention caveat |
| G2 | Canonical momentum contains `qA + mA_g` | Proposition within weak-field minimal coupling | Retain |
| G3 | London current screens `A + (m/q)A_g` | Proposition for condensate | Retain in the idealized limit |
| G4 | Introduce scalar material `μ_g` | Extra assumption | Permissible phenomenology, not a derivation |
| G5 | Solve coupled half-space field equations | Identity/approximation | Algebraically coherent conditional on G1–G4 |
| G6 | Assign condensate phase gradient to each ion | Extra assumption/blocker | Requires a separate ionic collective field and locking law |
| G7 | Use uncertainty to infer `n >= 1` | Blocker | Does not follow; `n = 0` is allowed |
| G8 | Infer universal ionic angular momentum `L_i = 2nℏ` | Blocker | Depends on G6–G7 and lacks preparation/conservation accounting |
| G9 | Define relative permeabilities by current projections | Constitutive assumption | Not a general material definition; valid only in a specified local linear model |
| G10 | Let ionic and pair charge currents cancel while mass currents add | Proposition plus extra assumption | Algebra is sound if a real ionic counterflow exists; the counterflow is not derived |
| G11 | Identify Meissner screening with `μ_r << 1` | Blocker in conventional superconductivity | Requires a new constitutive law, not standard Meissner electrodynamics |
| G12 | Obtain `μ_{g,r} ~ 10^4` and `X_L ~ 10^-9 C/kg` | Conditional algebra | Inherits G6–G11 and numerically depends mainly on `1/μ_r` |
| G13 | Sum `10^28` coherent ion fields to `B_g ~ 10^-9 s^-1` | Numerical blocker | Inconsistent with total angular momentum density and laboratory geometry |

The shortest dependency chain is:

\[
\boxed{
\text{phase locking}
\rightarrow \text{ionic counterflow}
\rightarrow \text{charge cancellation/mass addition}
\rightarrow \text{large matter response}
\rightarrow \text{gravitational field}
}
\tag{M1}
\]

Li's papers derive the field solution on the right and assert most of the material mechanism on the left.

## Main Derivation

### Step 1 — Weak-field carrier coupling (1991)

Li and Torr begin with a Lorentz-like force,

\[
\mathbf F
=q(\mathbf E+\mathbf v\times\mathbf B)
+m(\mathbf E_g+\mathbf v\times\mathbf B_g),
\tag{1.1}
\]

and a corresponding nonrelativistic Lagrangian. The canonical momentum is

\[
\mathbf p
=m\mathbf v+q\mathbf A+m\mathbf A_g.
\tag{1.2}
\]

For a condensate with phase `φ`, the normalized quantum relation is

\[
\hbar\nabla\phi
=m\mathbf v_s+q\mathbf A+m\mathbf A_g.
\tag{1.3}
\]

**Classification:** proposition within weak-field minimal coupling.

**Audit:** this is the strongest part of the program. It says that a charged massive coherent carrier is sensitive to electromagnetic and gravitational potentials. It does not imply that the carrier generates an amplified gravitational field.

### Step 2 — Condensate charge and mass currents

With `j_e = nq v_s` and `j_m = nm v_s`, the same carrier obeys

\[
\mathbf j_m=\frac{m}{q}\mathbf j_e.
\tag{2.1}
\]

For a uniform phase slice, Li and Torr write the London-like current as

\[
\mathbf j_e
=-\frac{1}{\mu\lambda_L^2}
\left(\mathbf A+\frac{m}{q}\mathbf A_g\right),
\tag{2.2}
\]

and hence

\[
\mathbf j_m
=-\frac{1}{\mu\lambda_L^2}\frac{m}{q}
\left(\mathbf A+\frac{m}{q}\mathbf A_g\right).
\tag{2.3}
\]

**Classification:** identity after the London response and common-carrier assumption.

**Audit:** the proportionality of charge and mass current is valid for one carrier species. The use of material `μ` inside the penetration-depth normalization is already model-dependent; standard treatments normally express the screening length through superfluid density and vacuum electromagnetic constants rather than an extremely small bulk `μ_r`.

### Step 3 — Coupled field equations

Under stationary conditions, substitution into the Maxwell-like curl equations produces

\[
\nabla^2\mathbf B
=\frac{1}{\lambda_L^2}
\left(\mathbf B+\frac{m}{q}\mathbf B_g\right),
\tag{3.1}
\]

\[
\nabla^2\mathbf B_g
=-\frac{m^2\mu_g}{q^2\mu\lambda_L^2}
\left(\mathbf B_g+\frac{q}{m}\mathbf B\right).
\tag{3.2}
\]

The combinations

\[
\mathbf B_1=\mathbf B+\frac{m}{q}\mathbf B_g,
\qquad
\mathbf B_2=\mathbf B+\frac{q\mu}{m\mu_g}\mathbf B_g
\tag{3.3}
\]

diagonalize the half-space problem: `B_1` is exponentially screened and `B_2` is harmonic in the idealized geometry.

**Classification:** algebra plus half-space approximation.

**Audit:** the diagonalization is a real result of the assumed equations. It does not determine the material coefficients appearing in them.

### Step 4 — The 1991 interior response

Farther than a penetration depth from the surface, the paper obtains, to leading order in the small gravitational coupling,

\[
\mathbf B
\simeq
-\frac{m^2\mu_g}{q^2\mu}\mathbf B_0
-\frac{m}{q}\mathbf B_{g,0},
\tag{4.1}
\]

\[
\mathbf B_g
\simeq
\mathbf B_{g,0}
+\frac{\mu_g}{\mu}\frac{m}{q}\mathbf B_0.
\tag{4.2}
\]

Equation (4.2) exposes the entire amplification problem:

\[
\mathcal X_L
=\frac{\mathbf B_g-\mathbf B_{g,0}}{\mathbf B_0}
=\frac{\mu_g}{\mu}\frac{m}{q}.
\tag{4.3}
\]

**Classification:** conditional result.

**Audit:** 1991 derives how a granted coefficient would enter. It explicitly leaves the value of `μ_g/μ` to later work. It is therefore a transfer-function paper, not an amplification derivation.

### Step 5 — Free and bound current split (1992)

The 1992 paper rewrites the condensate currents as

\[
\mathbf j_{e,f}
=-Q\left(\mathbf A+\frac{m}{q}\mathbf A_g\right),
\qquad
\mathbf j_{m,f}
=\frac{m}{q}\mathbf j_{e,f},
\tag{5.1}
\]

with

\[
Q=\frac{q^2}{m}|\psi|^2.
\tag{5.2}
\]

It then introduces ionic “bound” currents with a phase-gradient term and the ionic vector-potential coupling. In normalized form,

\[
\mathbf j_{e,M}
\sim q_i n_i\mathbf v_i,
\qquad
\mathbf j_{m,M}
\sim m_i n_i\mathbf v_i
=\frac{m_i}{q_i}\mathbf j_{e,M}.
\tag{5.3}
\]

**Classification:** (5.1) is a conventional current relation; (5.3) is an identity if a physical ionic velocity field `v_i` exists.

**Audit:** separating charge and mass currents is productive. The missing element is not the ratio in (5.3); it is the derivation of a coherent ionic `v_i` in a stationary lattice.

The paper also assumes the lattice-ion density equals `|ψ|^2/2` “to maintain charge neutrality.” Charge neutrality alone does not imply that equality. It depends on ionic valence, the fraction of electrons in the superfluid, core electrons, and normal carriers. This affects every current magnitude downstream.

### Step 6 — Transfer of the condensate phase to lattice ions

Li and Torr assign an ion momentum

\[
\mathbf p_i=2\hbar\nabla_i\phi,
\tag{6.1}
\]

and integrate it around a closed path:

\[
\oint\mathbf p_i\cdot d\mathbf l=2nh.
\tag{6.2}
\]

They then use an uncertainty expression to require

\[
n\ge 1,
\tag{6.3}
\]

and infer for every lattice ion

\[
\mathbf L_i=2n\hbar.
\tag{6.4}
\]

**Classification:** extra assumption at (6.1); blocker at (6.3); unsupported conclusion at (6.4).

**Internal audit independent of paradigm:**

1. `φ` was defined as the superconducting condensate phase. A derivative `∇_iφ` with respect to an ionic coordinate requires a joint many-body state or a second ionic order parameter. The papers provide neither.
2. Single-valuedness gives integer winding, `n in Z`. It does not exclude `n = 0`.
3. The uncertainty relation constrains variances; it does not set a topological winding sector.
4. Even if an ion collective mode had quantized circulation, a nonzero sector would require preparation and angular-momentum transfer. It cannot be universal without a source and conservation account.

These are not objections of “conventional taste.” They are missing logical and dynamical links that any replacement theory must supply.

### Step 7 — Permeability definitions

The 1992 paper defines relative responses through projections of bound and free currents:

\[
\mu_r
=1+\frac{\mathbf j_{e,M}\cdot\mathbf j_{e,f}}
{|\mathbf j_{e,f}|^2},
\tag{7.1}
\]

\[
\mu_{g,r}
=1+\frac{\mathbf j_{m,M}\cdot\mathbf j_{m,f}}
{|\mathbf j_{m,f}|^2}.
\tag{7.2}
\]

Combining the same-carrier ratios yields, in magnitude,

\[
\frac{\mu_{g,r}-1}{\mu_r-1}
=\frac{j_{e,f}}{j_{m,f}}
\frac{j_{m,M}}{j_{e,M}}
=\frac{q/m}{q_i/m_i}
=\frac{\gamma_c}{\gamma_i}.
\tag{7.3}
\]

**Classification:** algebra after accepting (7.1)–(7.2) as constitutive definitions.

**Audit:** equation (7.3) contains Li's strongest physical intuition. If two oppositely charged carrier systems counterflow so their charge currents cancel, their mass currents need not cancel because their mass-to-charge ratios differ. This is kinematically sound.

What is not established is that (7.1) is the correct description of the Meissner state or that the proposed ionic carrier system actually moves. A permeability is normally defined through a specified field-response relation, including spatial dispersion, frequency, geometry, and boundary conditions. The current-projection formulas assume the required local, collinear linear response.

### Step 8 — Charge cancellation and mass-current addition

The cleanest way to expose this part is to write the two-carrier currents directly:

\[
\mathbf j_e
=q n_s\mathbf v_s+q_i n_i\mathbf v_i,
\tag{8.1}
\]

\[
\mathbf j_m
=m n_s\mathbf v_s+m_i n_i\mathbf v_i.
\tag{8.2}
\]

If a physical entrainment law produces charge cancellation,

\[
\mathbf j_e\simeq 0
\quad\Rightarrow\quad
\mathbf v_i
\simeq-\frac{q n_s}{q_i n_i}\mathbf v_s,
\tag{8.3}
\]

then

\[
\boxed{
\mathbf j_m
\simeq n_s
\left(m-\frac{m_iq}{q_i}\right)\mathbf v_s
}
\tag{8.4}
\]

and, because `q` and `q_i` have opposite signs, the two mass-current contributions add.

**Classification:** identity conditional on a real counterflow.

**Audit:** equation (8.4) is the strongest conventional reconstruction of Li's intuition. A charge-neutral but mass-current-rich mode is possible in principle. It does not follow from ordinary Meissner screening, and its kinetic energy,

\[
\mathcal E_{\mathrm{kin}}
=\frac12 mn_s v_s^2
+\frac12 m_i n_i v_i^2,
\tag{8.5}
\]

mechanical momentum, and angular momentum remain in the accounting. Coherence cannot remove these costs.

### Step 9 — The claimed permeability enhancement

Taking `μ_r << 1`, Li and Torr obtain approximately

\[
\mu_{g,r}\sim
\left|\frac{\gamma_c}{\gamma_i}\right|
\sim 10^4,
\tag{9.1}
\]

and

\[
\frac{\mu_g}{\mu}
=\frac{\mu_{g,0}}{\mu_0}
\frac{\mu_{g,r}}{\mu_r}
\sim
\frac{\mu_{g,0}}{\mu_0}
\frac{10^4}{\mu_r}.
\tag{9.2}
\]

**Classification:** conditional algebra.

**Audit:** the often-cited `10^4` is not by itself enough. The claimed observable response is dominated by the much larger factor `1/μ_r`:

\[
\mathcal X_L
\sim
\left(7.4\times10^{-21}\right)
\frac{10^4}{\mu_r}
\left(5.7\times10^{-12}\right)
\ \mathrm{C\,kg^{-1}}.
\tag{9.3}
\]

Representative values give

| Assumed `μ_r` | `X_L` from (9.3) |
|---:|---:|
| `10^-17` | `4.2 × 10^-11 C/kg` |
| `10^-20` | `4.2 × 10^-8 C/kg` |
| `10^-27` | `4.2 × 10^-1 C/kg` |
| `10^-33` | `4.2 × 10^5 C/kg` |

The papers do not use a stable value. The 1992 discussion infers values around `10^-27` from conductivity and still smaller values near `10^-32`–`10^-33` from its screening argument. The 1993 paper instead quotes approximately `10^-17` from mesoscopic normal-metal rings and `10^-20` from its earlier theory. Because `X_L` scales as `1/μ_r`, these differences move the prediction by 10–16 orders of magnitude.

This numerical instability shows that the result is not a parameter-free consequence of the theory.

### Step 10 — The `σ–μ` branch

The 1992 paper develops a conductivity-permeability model and obtains, in its limiting form,

\[
\sigma\propto\frac{1}{\mu_r^2}.
\tag{10.1}
\]

It then uses large superconducting conductivity to infer extremely small `μ_r`, and uses that `μ_r` to amplify the gravitational response.

**Classification:** conditional model plus interpretation.

**Audit:** this is not an independent empirical determination of permeability. The relation (10.1) was derived inside the same free/bound-current and gravitational-permeability framework whose coefficient it is used to support. Standard superconductivity does not identify zero DC resistance or long current lifetime with a local bulk `μ_r` of `10^-20` to `10^-33`. Magnetic-field exclusion is generated by condensate screening currents with finite penetration depth and geometry dependence.

The branch is therefore circular as evidence for the amplification, even where its internal algebra is followed correctly.

### Step 11 — Dynamic gravitoelectric solution (1993)

The 1993 paper derives coupled electric and gravitoelectric half-space equations and obtains, deep inside the idealized sample,

\[
\widetilde{\mathbf E}
+\frac{m}{q}\widetilde{\mathbf E}_g=0.
\tag{11.1}
\]

The induced gravitoelectric field is

\[
\boxed{
\widetilde{\mathbf E}_g^{\mathrm{ind}}
=\frac{\mu_g}{\mu}\frac{m}{q}
\widetilde{\mathbf E}_0
}
\tag{11.2}
\]

and the static magnetic counterpart is

\[
\boxed{
\mathbf B_g^{\mathrm{ind}}
=\frac{\mu_g}{\mu}\frac{m}{q}\mathbf B_0.
}
\tag{11.3}
\]

The paper estimates

\[
\mathcal X_L\sim10^{-9}\ \mathrm{C\,kg^{-1}}.
\tag{11.4}
\]

**Classification:** the field solution is conditional algebra; the magnitude is inherited from Steps 6–10.

**Audit:** equation (11.1) says the net generalized force on a Cooper pair vanishes in the idealized bulk. It is not, by itself, gravitational shielding or inertial decoupling. Equations (11.2)–(11.3) are useful targets, but they do not independently validate the material coefficient.

The paper also neglects gradients of the spatially varying permeability. A scalar coefficient does not make its gradient disappear: applying a curl to a product generally produces a term such as `∇μ × j`. The authors mention an additional gradient term and set it to zero for later treatment. The solution therefore applies only where those gradients can consistently be neglected.

### Step 12 — Persistent-current analogy

To estimate `μ_r`, the 1993 paper uses persistent electron currents measured in mesoscopic normal-metal rings as an analog for the proposed persistent **ionic** vortical current.

**Classification:** interpretation.

**Audit:** the measured normal-metal currents are electronic equilibrium currents. They do not establish lattice-ion circulation or provide its magnetic moment density. Using them to infer the ionic `μ_r` changes the identity of the carrier and does not close the derivation.

### Step 13 — Coherent-ion field sum

The paper estimates

\[
B_{g,\mathrm{ion}}\sim10^{-37}\ \mathrm{s^{-1}}
\tag{13.1}
\]

and multiplies by roughly `N = 10^28` coherent ions to obtain

\[
B_g\sim10^{-9}\ \mathrm{s^{-1}}.
\tag{13.2}
\]

**Classification:** numerical interpretation.

**Audit:** the source-observer distance in the single-ion estimate is not carried consistently into the macroscopic sum. A direct total-angular-momentum check avoids that ambiguity. Even granting every ion `2ℏ`,

\[
J_{\mathrm{tot}}
\sim N(2\hbar)
\sim2.1\times10^{-6}\ \mathrm{kg\,m^2\,s^{-1}}.
\tag{13.3}
\]

For the paper's `0.1 m^3` volume, the angular-momentum density is approximately

\[
\mathcal L\sim2.1\times10^{-5}\
\ \mathrm{kg\,m^{-1}\,s^{-1}}.
\tag{13.4}
\]

Using the ordinary weak-field scale `μ_{g,0} = 4πG/c^2`,

\[
B_g^{\mathrm{GR}}
\sim\mu_{g,0}\mathcal L
\sim2\times10^{-31}\ \mathrm{s^{-1}},
\tag{13.5}
\]

up to geometry and convention factors of order unity. A dipole estimate at `R = 0.1–1 m` gives approximately `10^-30–10^-33 s^-1`.

This is roughly 21–24 orders below (13.2). Coherence can justify adding amplitudes associated with a genuine ordered source, but it cannot change the total source angular momentum in (13.3). A new source-to-gravity law would be required in addition to coherent ionic alignment.

## Strongest Conventional Reconstruction

Remove only the unsupported ingredients while keeping the real coupling.

### C1 — Condensate coupling

\[
\hbar\nabla\phi
=m\mathbf v_s+q\mathbf A+m\mathbf A_g.
\tag{C1}
\]

This predicts gravitational and rotational corrections to superconducting phase and fluxoid observables.

### C2 — No ionic collective phase by default

For a stationary lattice,

\[
\mathbf v_i=0,
\qquad
\mathbf j_{m,M}=0
\tag{C2}
\]

apart from explicitly excited phonon, rigid-rotation, spin, or other material modes. Condensate winding remains

\[
\oint
\left(m\mathbf v_s+q\mathbf A+m\mathbf A_g\right)
\cdot d\mathbf l=nh,
\qquad n\in\mathbb Z,
\tag{C3}
\]

including `n = 0`.

### C3 — Standard field response

Without a new gravitational constitutive law,

\[
\mu_g\simeq\mu_{g,0},
\qquad
\mu\simeq\mu_0
\tag{C4}
\]

for the source-to-field comparison; Meissner screening is treated through the superconducting response kernel and penetration depth rather than `μ_r -> 0`.

The cross coefficient is then of order

\[
\mathcal X_{\mathrm{conv}}
\sim
\frac{\mu_{g,0}}{\mu_0}\frac{m}{q}
\sim4\times10^{-32}\ \mathrm{C\,kg^{-1}}.
\tag{C5}
\]

**Conventional result:** the coupling exists, but it is far below Li's predicted response. This is the control case, not a proof that the control case is complete.

## Minimum-New-Physics Reconstruction

The published target can be made logically coherent only by stating the new laws instead of hiding them inside `μ_g` and `μ`.

### N1 — A distinct ionic collective field

Introduce an ionic collective phase or orientation field `Θ_i`, separate from the superconducting phase `φ`, with a locking interaction such as

\[
\mathcal L_{\mathrm{lock}}
=K\cos(\Theta_i-\alpha\phi)
\tag{N1}
\]

or a symmetry-allowed gradient entrainment term. This does not require every ion to have nonzero winding. It provides dynamics from which a driven ionic mode might emerge.

Required outputs are its excitation gap, coherence length, damping, angular momentum, preparation mechanism, and non-gravitational signature.

### N2 — A derived two-fluid response

The condensate and ionic velocities must follow from coupled equations of motion. The response can be written schematically as

\[
\begin{pmatrix}
\mathbf j_e\\[2pt]
\mathbf j_m
\end{pmatrix}
=
\begin{pmatrix}
\chi_{eA} & \chi_{eA_g}\\
\chi_{mA} & \chi_{mA_g}
\end{pmatrix}
\begin{pmatrix}
\mathbf A\\[2pt]
\mathbf A_g
\end{pmatrix}.
\tag{N2}
\]

Li's desired matter-side effect is a state in which `χ_eA` is screened while `χ_mA` remains large. Equation (8.4) shows the kinematic possibility; a microscopic theory must determine whether the state exists.

### N3 — Keep ordinary gravity and new gravity separate

First calculate the field from the resulting complete stress-energy using standard weak gravity:

\[
\mathbf B_g^{\mathrm{GR}}
=\mathcal G_{gT}^{\mathrm{GR}}
\chi_{TA}\mathbf A.
\tag{N3}
\]

Only if this is insufficient and a replacement principle is proposed should one introduce

\[
\mathcal G_{gT}
=\eta_g(\omega,\mathbf k,|\psi|,\Theta_i)
\mathcal G_{gT}^{\mathrm{GR}}.
\tag{N4}
\]

The full response is then

\[
\boxed{
\mathcal X_{gA}
=\eta_g\,
\mathcal G_{gT}^{\mathrm{GR}}
\chi_{TA}^{\text{two-fluid}}.
}
\tag{N5}
\]

This formulation identifies exactly where a paradigm change may live:

- `χ_TA`: a new coherent matter mode but standard gravity;
- `η_g`: a new source-to-spacetime response;
- both, if required.

### N4 — Conditional statement that replaces the published claim

A Li-like enhancement follows in this minimum reconstruction only if the theory supplies all of the following:

1. a coherent ionic, spin, or neutral collective mode with measured angular momentum;
2. a dynamical coupling that drives it from the superconducting state or applied field;
3. charge-current suppression without corresponding mass-current cancellation;
4. complete energy and angular-momentum accounting;
5. either sufficient ordinary stress-energy or an explicit new gravitational response `η_g`;
6. a field solution with the correct geometry and boundary terms.

This conditional form is coherent. The published papers do not derive items 1–5.

## Remarks and Interpretation

- **What survived unchanged:** weak-field coupling of a superconducting carrier to `A_g`; the usefulness of superconducting phase as a gravity/rotation probe; the algebraic fact that charge cancellation need not imply mass-current cancellation.
- **What was reframed:** `μ_g/μ` is a compound proxy for a matter-response problem and a gravity-response problem. These must be calculated separately.
- **What failed internally:** forced nonzero winding, universal ionic angular momentum, use of electron ring currents as ionic evidence, and the macroscopic coherent field sum.
- **What may still represent a paradigm clue:** a coherent neutral counterflow or spin/lattice mode that couples unusually to spacetime. The audit does not dismiss that possibility; it states the missing law required to investigate it.
- **Most important new insight from the reconstruction:** Li's `10^4` factor can be understood as a mass-to-charge-ratio advantage of a hypothetical ionic counterflow. The truly enormous gain in her prediction comes from treating Meissner screening as `1/μ_r` and then allowing that small denominator to enter the gravitational cross-response.

## Boundaries and Non-Claims

- This document audits Li's published derivation; it does not yet choose among deeper replacement principles.
- Failure of the ionic derivation does not prove that superconducting coherence has no anomalous gravitational coupling.
- The numerical comparison uses weak-field order-of-magnitude formulas; GEM conventions can change factors of order unity, not the 20-plus-order gap.
- The document does not infer an apparatus or experimental frequency.
- The 1997 static null is an empirical boundary on a later configuration, not a step in the 1991–1993 derivation.
- The audit does not assume that GR must remain exact. It requires any departure to be stated as a law with identifiable degrees of freedom and observable consequences.

## Open Risks

- Li, Torr, and Karwacki's referenced 1994 preprint, *Lattice Ion Rotations and the Dipole Gravitomagnetic Field of Superconductors*, was not available and may contain an attempted repair.
- The 1993 phrase “spin angular momentum” is not cleanly separated from orbital lattice motion; the two source models should not be conflated.
- A modern multiband or unconventional superconductor could support collective modes absent from the simple `s`-wave model. That would require a new derivation, not retroactive validation of (6.1)–(6.4).
- The correct gravitational observable should ultimately be expressed covariantly rather than through scalar GEM permeabilities.
- Any future theory must distinguish bulk response from surface screening and include spatial dispersion and boundary gradients.

## Primary Equation Sources

- Ning Li and D. G. Torr, “Effects of a Gravitomagnetic Field on Pure Superconductors,” *Physical Review D* **43**, 457–459 (1991), DOI [`10.1103/PhysRevD.43.457`](https://doi.org/10.1103/PhysRevD.43.457). [Local PDF](../02_Gravitation-Theory/Ning-Li-Superconductivity-Program/Gravitomagnetic%20field%20on%20SCs.pdf).
- Ning Li and D. G. Torr, “Gravitational Effects on the Magnetic Attenuation of Superconductors,” *Physical Review B* **46**, 5489–5495 (1992), DOI [`10.1103/PhysRevB.46.5489`](https://doi.org/10.1103/PhysRevB.46.5489). [Local PDF](../02_Gravitation-Theory/Ning-Li-Superconductivity-Program/Gravitational%20effects%20on%20magnetic%20attenuation%20SCs%20PhysRevB.46.5489.pdf).
- Douglas G. Torr and Ning Li, “Gravitoelectric-Electric Coupling via Superconductivity,” *Foundations of Physics Letters* **6**, 371–383 (1993), DOI [`10.1007/BF00665654`](https://doi.org/10.1007/BF00665654). [Local PDF](../02_Gravitation-Theory/Ning-Li-Superconductivity-Program/cupdf.com_torr-and-li-1993-gravitoelectric-electric-coupling.pdf).
- [Contextual Ning Li deep-dive report](Ning-Li-Superconductors-and-Gravitomagnetism-Deep-Dive-2026.md).
