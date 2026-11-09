# Derivation Package - Rotating-Superconductor Ionic Current, Response Matrix, and Tate Inversion

> **Finite-ring follow-up, 2026-09-04:** the [ring/measurement audit](01_Reports-and-Syntheses/Tate-Finite-Ring-and-Measurement-Audit-2026.md) now derives the winding-spacing observable. The bulk equations below retain their stated scope. For an electronic winding increment with the second winding fixed, the general charged spacing denominator is `1+xy`, rather than the bulk-field denominator `1+2xy+ry^2`. The neutral `1+x` specialization survives only with fixed neutral winding and controlled geometry/surface response. The full empirical Tate fit remains pending primary apparatus/calibration data.

**Date:** 2026-07-24
**Scope:** equilibrium matter response only; no gravitational amplification term is assumed

## Target

This package answers two linked questions.

1. Can the superconducting condensate phase, by itself, derive the coherent ionic/lattice mass current required by the Li-Torr amplification mechanism?
2. What is the most general isotropic two-component rotation-to-magnetic response at quadratic order, and what stiffness or entrainment coefficients would reproduce the Tate niobium residual?

The intended outputs are:

- a derivation or refutation of a superconductivity-induced ionic current;
- a protected one-component London coefficient;
- a two-component response formula;
- an explicit inversion for the `+84 ppm` and `+92 ppm` Tate comparisons;
- a statement of what is and is not thereby established.

## Status

**COHERENT AFTER REFRAMING / EXTRA ASSUMPTION**

The published Li-Torr ionic-current target does not survive unchanged.

- In an ordinary superconducting crystal, the ionic lattice is described by an elastic displacement field, not by the compact phase of the electronic condensate.
- At fixed rigid rotation, the lattice has its ordinary mechanical mass current in both the normal and superconducting states. The superconductivity-induced increment of the equilibrium bulk ionic current is zero.
- A charge-canceled but mass-current-carrying mode is derivable only after introducing a genuinely independent mobile coherent component with its own phase or an explicitly driven lattice mode. That is additional physics, not a consequence of the Meissner state.

The Tate response calculation is coherent after this reframe. In the two-phase model derived below, a neutral second component reproduces a `92 ppm` intrinsic shift when

\[
\frac{\rho_{s\chi}}{\rho_s}=9.2\times10^{-5},
\]

subject to positive definiteness,

\[
\frac{\rho_\chi}{\rho_s}>
\left(\frac{\rho_{s\chi}}{\rho_s}\right)^2
=8.46\times10^{-9}.
\]

This is a data inversion, not evidence that such a component exists in niobium.

## Invariant Object

The organizing observable is the intrinsic stationary rotation-to-magnetic transfer coefficient

\[
\mathcal K_\Omega\equiv-\frac{B}{2\Omega}.
\]

For a one-component superconductor,

\[
\mathcal K_\Omega=\frac{m_s}{q_s}
\]

up to the thermodynamic and surface corrections stated below. Here \(q_s\) is signed.

For a multicomponent coherent medium, the invariant object is the quadratic stiffness matrix \(R\), together with the vector of signed charge-to-mass ratios

\[
Q_a\equiv\frac{q_a}{m_a}.
\]

The current, field, and neutral-mode statements must all follow from the same \(R\). This prevents charge cancellation from being asserted independently of momentum and energy.

## Assumptions

1. The sample rotates slowly, \(\Omega R/c\ll1\).
2. The calculation is stationary, isotropic, and linear in \(\Omega\).
3. The analyzed bulk region is vortex-free and farther than a penetration depth from the surface.
4. The magnetic induction is uniform in that bulk slice.
5. The ordinary lattice is an elastic field \(\mathbf u(\mathbf r,t)\), with velocity

   \[
   \mathbf v_L=\boldsymbol\Omega\times\mathbf r+\dot{\mathbf u}.
   \]

6. The electronic superconducting phase is \(\theta\). The optional field \(\chi\) is an independently phase-rigid counterfactual, not a relabeling of the lattice.
7. The two-component stiffness matrix is symmetric and positive definite.
8. Electromagnetism uses vacuum constants and explicit currents. No scalar magnetic or gravitational permeability is inserted.
9. Electrochemical and surface-double-layer corrections are separated from the intrinsic bulk stiffness response.
10. Gravity is excluded from the derivation. Any gravitational field must later be calculated from the measured total stress-energy.

## Notation

- \(m_s,q_s,\theta\): mass, signed charge, and phase of a Cooper pair.
- \(\mathbf A,\mathbf B=\nabla\times\mathbf A\): electromagnetic vector potential and magnetic induction.
- \(\mathbf u,\mathbf v_L\): lattice displacement and velocity.
- \(\mathbf v_s\): condensate velocity in the laboratory frame.
- \(\mathbf w_s=\mathbf v_s-\mathbf v_L\): condensate velocity relative to the lattice.
- \(\chi,m_\chi,q_\chi,\mathbf v_\chi,\mathbf w_\chi\): corresponding quantities for an optional second coherent component.
- \(R=(\rho_{ab})\): positive stiffness or entrainment matrix in velocity normalization.
- \(Q_a=q_a/m_a\): signed charge-to-mass ratio.
- \(\rho_s=\rho_{ss}\), \(x=\rho_{s\chi}/\rho_s\), \(r=\rho_\chi/\rho_s\), \(y=Q_\chi/Q_s\).
- \(\eta=1+\mu_{\rm chem}/c^2\): frame-independent thermodynamic correction in Liu's formulation.
- \(\alpha\): surface-double-layer contribution to the externally inferred flux coefficient.
- \(\delta=B/B_0-1\): fractional shift from the one-component intrinsic London value.

## Derivation Strategy

The derivation proceeds from the ordinary crystal to the hypothetical extension.

1. Keep the condensate phase and lattice displacement as distinct objects.
2. Derive the standard relative-current relation and its equilibrium consequence.
3. Separate ordinary rigid-body ionic mass flow from a superconductivity-induced current.
4. Introduce an optional second phase only after the one-component result is fixed.
5. Derive the multicomponent magnetic field by imposing gauge kinematics and zero uniform bulk charge current.
6. Derive the surviving relative mass current from the same stiffness matrix.
7. Reduce the general result to a two-component closed form and invert it for Tate.

## Derivation Map

1. Gauge invariance defines \(\mathbf v_s\).
2. The co-rotating equilibrium current depends on \(\mathbf v_s-\mathbf v_L\), not on an ionic phase.
3. Zero uniform bulk current plus vortex-free phase kinematics gives the one-component London field.
4. The same zero-current condition forces zero relative bulk momentum for one component.
5. With two independent charge-to-mass ratios, zero charge current no longer forces zero mass current.
6. The response matrix yields \(B/\Omega\) and the neutral mass-current coefficient simultaneously.
7. The Tate residual fixes a curve in \((x,r,y)\), rather than a free Cooper-pair rest mass.

## Main Derivation

### Step 1 - Condensate and lattice are different symmetry fields

**Identity / definition.** For a Cooper-pair condensate,

\[
\mathbf v_s=
\frac{\hbar}{m_s}\nabla\theta
-\frac{q_s}{m_s}\mathbf A.
\tag{1}
\]

In a vortex-free bulk region,

\[
\nabla\times\nabla\theta=0,
\]

so

\[
\nabla\times\mathbf v_s
=-Q_s\mathbf B.
\tag{2}
\]

The lattice is described by three displacement Goldstone fields,

\[
\mathbf u(\mathbf r,t),
\]

not by \(\theta\). Its velocity is

\[
\mathbf v_L=\boldsymbol\Omega\times\mathbf r+\dot{\mathbf u}.
\tag{3}
\]

The circulation of \(\nabla\theta\) may be quantized. The circulation of an ordinary elastic displacement is not assigned the same winding number.

**Proposition.** A term of the form \(\nabla_i\theta\), interpreted as the momentum of an individual ion, requires a joint many-body locking law or a second compact order parameter. Ordinary superconductivity supplies neither.

This is the exact point at which the published Li-Torr ionic derivation requires an extra assumption.

### Step 2 - One-component equilibrium current

Mario Liu's frame-independent thermodynamic result may be written schematically as

\[
\mathbf j_s
=\rho_s\left(\frac{\mathbf v_s}{\eta}-\mathbf v_L\right),
\qquad
\eta=1+\frac{\mu_{\rm chem}}{c^2}.
\tag{4}
\]

Here \(\mathbf j_s\) is the persistent current relative to the rotating crystal, not the total laboratory mass current of every constituent.

**Proposition under the bulk assumptions.** A uniform bulk magnetic induction has no uniform Ampere source:

\[
\nabla\times\mathbf B=0
\quad\Longrightarrow\quad
\mathbf j_s=0
\]

in the analyzed bulk slice. Equation (4) therefore gives

\[
\mathbf v_s=\eta\mathbf v_L.
\tag{5}
\]

Taking a curl and using

\[
\nabla\times\mathbf v_L=2\boldsymbol\Omega
\]

with Eq. (2),

\[
-Q_s\mathbf B=2\eta\boldsymbol\Omega.
\]

Hence

\[
\boxed{
\mathbf B_0
=-\frac{2\eta}{Q_s}\boldsymbol\Omega
=-\frac{2\eta m_s}{q_s}\boldsymbol\Omega
}.
\tag{6}
\]

This is the protected one-component bulk London coefficient. The pair density and ordinary band effective mass do not appear as free multiplicative gains.

For niobium, the thermodynamic estimate in Liu's treatment is

\[
\left|\eta-1\right|
\sim10^{-10}.
\tag{7}
\]

### Step 3 - The ionic mass current is ordinary rigid rotation

Let \(\rho_i\) be the ionic mass density. In the laboratory frame,

\[
\mathbf j_{m,i}^{\rm lab}
=\rho_i\mathbf v_L.
\tag{8}
\]

This current exists above and below the superconducting transition whenever the solid rotates.

Define the superconductivity-induced ionic current at fixed imposed rotation:

\[
\Delta\mathbf j_{m,i}
\equiv
\mathbf j_{m,i}^{\rm SC}
-\mathbf j_{m,i}^{\rm normal}.
\tag{9}
\]

For static equilibrium in the co-rotating frame,

\[
\dot{\mathbf u}=0,
\]

and the imposed rigid rotation is the same in the two states. Therefore

\[
\boxed{
\Delta\mathbf j_{m,i}^{\rm bulk}=0
}.
\tag{10}
\]

**Interpretation.** Charge neutrality makes the electric current of a uniformly co-rotating neutral solid vanish while its ordinary total mass current remains nonzero. That fact is not a superconducting amplification mechanism. It is the mass current of an ordinary rotating body.

During spin-up or a normal-to-superconducting transition, small angular momentum is exchanged among the condensate, electromagnetic field, lattice, and external drive:

\[
\Delta\mathbf L_L
=-\Delta\mathbf L_s
-\Delta\mathbf L_{\rm EM}
-\Delta\mathbf L_{\rm support}.
\tag{11}
\]

This transient conservation law does not quantize every ion or create an additional stationary ionic circulation.

### Step 4 - Charge cancellation and mass addition as a conditional identity

For two genuinely mobile carrier populations,

\[
\mathbf j_q
=q_1n_1\mathbf v_1
+q_2n_2\mathbf v_2,
\tag{12}
\]

\[
\mathbf j_m
=m_1n_1\mathbf v_1
+m_2n_2\mathbf v_2.
\tag{13}
\]

If dynamics produces

\[
\mathbf j_q=0,
\]

then

\[
\mathbf v_2
=-\frac{q_1n_1}{q_2n_2}\mathbf v_1,
\]

and

\[
\boxed{
\mathbf j_m
=n_1\left(
m_1-\frac{m_2q_1}{q_2}
\right)\mathbf v_1
}.
\tag{14}
\]

For opposite signed charges, the two mass contributions add.

**Classification:** Eq. (14) is an exact kinematic identity conditional on the existence of two physical mobile currents. It does not derive the second current.

For the ordinary lattice, Eq. (14) merely restates neutral rigid-body motion unless a superconductivity-dependent \(\Delta\mathbf v_L\) is independently derived. Equation (10) shows that the equilibrium standard theory gives no such increment.

### Step 5 - General two-phase stiffness model

Now add one explicitly hypothetical independent phase \(\chi\). Define

\[
\mathbf w=
\begin{pmatrix}
\mathbf w_s\\
\mathbf w_\chi
\end{pmatrix},
\qquad
R=
\begin{pmatrix}
\rho_s & \rho_{s\chi}\\
\rho_{s\chi} & \rho_\chi
\end{pmatrix}.
\tag{15}
\]

The quadratic kinetic free-energy density is

\[
f_{\rm kin}
=\frac12\mathbf w^TR\mathbf w.
\tag{16}
\]

Stability requires

\[
\rho_s>0,\qquad
\rho_\chi>0,\qquad
\rho_s\rho_\chi-\rho_{s\chi}^2>0.
\tag{17}
\]

For \(N\) coherent components, define

\[
Q=
\begin{pmatrix}
Q_1\\
\vdots\\
Q_N
\end{pmatrix},
\qquad
\mathbf 1=
\begin{pmatrix}
1\\
\vdots\\
1
\end{pmatrix}.
\]

For a vortex-free phase,

\[
\nabla\times\mathbf w_a
=-Q_a\mathbf B-2\boldsymbol\Omega.
\tag{18}
\]

For uniform rotation and field, write

\[
\mathbf w_a
=\alpha_a\boldsymbol\Omega\times\mathbf r.
\]

Equation (18) gives

\[
\alpha_a
=-1-\frac{Q_aB}{2\Omega}.
\tag{19}
\]

The electric current obtained from variation with respect to \(\mathbf A\) is

\[
\mathbf j_q
=Q^TR\mathbf w.
\tag{20}
\]

Uniform bulk \(B\) requires

\[
\mathbf j_q=0.
\tag{21}
\]

Substituting Eq. (19) into Eq. (20) yields

\[
0
=-Q^TR\mathbf 1
-\frac{B}{2\Omega}Q^TRQ.
\]

Therefore

\[
\boxed{
B
=-2\Omega
\frac{Q^TR\mathbf 1}{Q^TRQ}
}.
\tag{22}
\]

This is the general isotropic response-matrix result.

For one component,

\[
\frac{Q^TR\mathbf 1}{Q^TRQ}
=\frac1{Q_s},
\]

and Eq. (22) reduces to Eq. (6) after restoring \(\eta\).

With a diagonal two-component stiffness and oppositely charged electron and proton condensates, Eq. (22) reduces, up to sign convention, to the density-dependent rotation field derived by Babaev and Ashcroft.

### Step 6 - The neutral mass-current mode

The total momentum or mass current relative to the lattice in this Galilean quadratic model is

\[
\mathbf g_{\rm rel}
=\mathbf 1^TR\mathbf w.
\tag{23}
\]

Using Eq. (19) and the field in Eq. (22),

\[
\mathbf g_{\rm rel}
=
\left[
-\mathbf 1^TR\mathbf 1
+\frac{(\mathbf 1^TRQ)^2}{Q^TRQ}
\right]
\boldsymbol\Omega\times\mathbf r.
\tag{24}
\]

For one component, \(Q\) is proportional to \(\mathbf 1\), and the bracket vanishes:

\[
\boxed{
\mathbf g_{\rm rel}^{(1)}=0
}.
\tag{25}
\]

For multiple components with unequal charge-to-mass ratios, zero electric current does not generally force Eq. (24) to vanish.

This is the consistent derivation of Li's surviving intuition:

> A neutral mass-current mode is possible, but only when there is more than one independent mobile coherent component.

An elastic lattice clamped to the rotating frame is not such a component.

### Step 7 - Closed two-component response

Normalize the stiffness matrix and charge-to-mass vector as

\[
R
=\rho_s
\begin{pmatrix}
1 & x\\
x & r
\end{pmatrix},
\qquad
Q
=Q_s
\begin{pmatrix}
1\\
y
\end{pmatrix},
\tag{26}
\]

where

\[
x=\frac{\rho_{s\chi}}{\rho_s},
\qquad
r=\frac{\rho_\chi}{\rho_s},
\qquad
y=\frac{Q_\chi}{Q_s}.
\tag{27}
\]

The one-component reference is

\[
B_0=-\frac{2\Omega}{Q_s}.
\]

Equation (22) gives

\[
\frac{B}{B_0}
=
\frac{1+x+y(x+r)}
{1+2xy+ry^2}.
\tag{28}
\]

Hence the fractional intrinsic shift is

\[
\boxed{
\delta
\equiv\frac{B}{B_0}-1
=
\frac{(1-y)(x+ry)}
{1+2xy+ry^2}
}.
\tag{29}
\]

Solving Eq. (29) for the cross-stiffness gives

\[
\boxed{
x
=
\frac{
\delta(1+ry^2)-ry(1-y)
}{
(1-y)-2\delta y
}
}.
\tag{30}
\]

Positive definiteness becomes

\[
\boxed{
r>x^2
}.
\tag{31}
\]

Equations (29)-(31) define the complete two-component inversion at this order.

### Step 8 - Tate observable and the baseline distinction

Tate et al. reported

\[
\frac{m_{\rm app}}{2m_e}
=1.000084(21).
\tag{32}
\]

Two comparisons must remain separate:

\[
\delta_{\rm bare}
=1.000084-1
=84\times10^{-6},
\tag{33}
\]

\[
\delta_{\rm published\ baseline}
=1.000084-0.999992
=92\times10^{-6}.
\tag{34}
\]

The primary Jiang-Liu calculation distinguishes the intrinsic bulk London field from the externally inferred flux. Its bulk relativistic correction is approximately

\[
\zeta\simeq\frac{\mu_{\rm chem}}{c^2}
\sim-10^{-10}.
\tag{35}
\]

The external flux also contains a surface-double-layer contribution:

\[
m_{\rm obs}
=(1+\zeta)(1-\alpha)m_e.
\tag{36}
\]

Using a work-function scale near \(-4\ {\rm eV}\), the paper obtains approximately

\[
\alpha\simeq8\times10^{-6},
\]

and therefore

\[
\frac{m_{\rm obs}}{m_e}
\simeq0.999992.
\tag{37}
\]

This corrects a shorthand in the local strategic review: Jiang-Liu drives the *bulk* relativistic correction toward zero, but its treatment of the externally observed Tate-type flux retains the approximately `-8 ppm` surface contribution. For that observable, the anomaly comparison remains approximately `+92 ppm`.

The full Tate 1990 geometry and systematic budget are not reproduced here. Equation (37) is the theory baseline used for the coefficient inversion, not a reanalysis of the experiment.

### Step 9 - Neutral-component inversion

For a neutral second phase,

\[
Q_\chi=0
\quad\Longrightarrow\quad
y=0.
\]

Equation (29) becomes

\[
\boxed{
\delta=x
=\frac{\rho_{s\chi}}{\rho_s}
}.
\tag{38}
\]

The Tate comparisons therefore require:

| Comparison | Required \(x=\rho_{s\chi}/\rho_s\) | Minimum \(r=\rho_\chi/\rho_s\) from stability |
|---|---:|---:|
| Relative to bare \(2m_e\) | \(8.4\times10^{-5}\) | \(>7.06\times10^{-9}\) |
| Relative to \(0.999992\) baseline | \(9.2\times10^{-5}\) | \(>8.46\times10^{-9}\) |
| Hoang `18 ppm` secondary-summary value | \(1.8\times10^{-5}\) | \(>3.24\times10^{-10}\) |

The Hoang row is an arithmetic comparator only. The project has not admitted that measurement as independent evidence.

An equivalent added inertia per pair is

\[
\Delta m_{\rm pair}=2m_e\delta.
\tag{39}
\]

For `92 ppm`,

\[
\Delta m_{\rm pair}
=1.68\times10^{-34}\ {\rm kg}.
\tag{40}
\]

Relative to one niobium atom,

\[
\frac{\Delta m_{\rm pair}}{M_{\rm Nb}}
=1.09\times10^{-9}.
\tag{41}
\]

Equation (41) is a parameterization of the response coefficient. It does not mean that this fraction of an ion has been observed to co-move.

### Step 10 - Why the entire lattice cannot be inserted as \(\chi\)

Suppose the rigid ionic lattice were incorrectly treated as a second compact phase with its full ionic stiffness and opposite charge.

Electrical neutrality relates its density and charge to the electronic sector. Because the ionic mass is roughly \(10^5\) electron masses, the resulting \(r\) is very large while \(y=Q_i/Q_s\) is very small and oppositely signed. Their product is not generically small.

Equation (29) would then predict an order-one material-dependent violation of the London law, not a `92 ppm` effect.

This is both theoretically and experimentally wrong for ordinary superconductors. The error is the identification of an elastic lattice with an independently phase-rigid superfluid component.

The only consistent ways to make the lattice-like sector enter Eq. (29) are:

1. a genuine supersolid or defect condensate;
2. a separately condensed ionic or excitonic component;
3. a driven coherent phonon treated as a nonequilibrium response, not an equilibrium phase;
4. another independently established compact collective coordinate.

No such component is established in ordinary niobium.

### Step 11 - Channel table for the Tate coefficient

| Channel | Status in this derivation | Expected equilibrium scale or requirement | Distinguishing dependence |
|---|---|---:|---|
| One-component bulk London response | Protected | bare \(m_s/q_s\) | universal at fixed carrier charge |
| Thermodynamic bulk correction \(\eta-1\) | Conventional | \(\sim10^{-10}\) | chemical potential |
| Surface double layer / work function | Conventional observable correction | approximately `-8 ppm` in the cited treatment | surface and work function |
| Static entrainment with a clamped elastic lattice | No intrinsic bulk shift | exactly zero in Eq. (10) at fixed rotation | none at equilibrium; dynamics may differ |
| Finite penetration depth, trapped flux, ring geometry, charging | Measurement-specific | not bounded by this package | geometry, temperature, flux history |
| Independently phase-rigid neutral \(\chi\) | Hypothetical but calculable | \(x=84\) to `92 ppm` for Tate | second transition, collective-mode spectrum, temperature, frequency |
| Driven phonon or nonequilibrium lattice mode | Outside the static theorem | unconstrained here | drive frequency, chirality, reversal parity, mechanical torque |
| Gravitational interpretation | Not derived | requires separate source-to-metric law | non-electromagnetic probe and stress-energy closure |

## Remarks and Interpretation

1. **The ionic-current question is now derived, with a negative standard result.** Ordinary superconductivity does not produce the Li-Torr independent ionic current. It produces a relative surface current and a London magnetic field while the bulk body undergoes ordinary rigid rotation.
2. **The mass-current intuition survives conditionally.** Equations (22)-(25) show exactly when charge cancellation can coexist with mass flow: at least two independent coherent components with unequal charge-to-mass ratios are required.
3. **Tate constrains a response coefficient, not a free mass.** The neutral inversion \(x=\delta\) makes the required cross-stiffness explicit.
4. **The required coefficient is small but not thereby plausible.** A `92 ppm` entrainment ratio is mathematically modest. The missing fact is the existence of a second phase-rigid component in niobium.
5. **The local baseline should be corrected.** The Jiang-Liu paper supports a near-zero intrinsic bulk relativistic correction while retaining the roughly `-8 ppm` surface contribution for an external-flux observable.
6. **Nothing here supplies gravitational gain.** If a neutral mode is identified, its ordinary gravitational field must be calculated from its measured energy, momentum, pressure, and angular momentum. A discrepancy in \(B/\Omega\) is not itself a metric response.

## Boundaries and Non-Claims

- This package does not reproduce the full Tate 1990 apparatus model or error covariance.
- It does not establish that the Tate residual is physical.
- It does not use the unaudited Hoang value as corroboration.
- It does not derive a microscopic value of \(\rho_{s\chi}\) for niobium.
- It does not treat anisotropic, nonlocal, finite-frequency, vortex, or strongly nonequilibrium response.
- It does not assign a compact phase to an ordinary lattice.
- It does not infer gravitomagnetism, gravity shielding, propulsion, or a modified gravitational permeability.
- It does not claim that every possible condensate-lattice coupling leaves the measured external flux unchanged; surface and dynamic channels are explicitly outside the bulk theorem.

## Open Risks

1. The [September finite-ring report](01_Reports-and-Syntheses/Tate-Finite-Ring-and-Measurement-Audit-2026.md) supplies the conditional winding/pickup mapping. Applying it to Tate still requires the actual geometry, winding/readout protocol, and calibrated electromagnetic boundary model.
2. The Tate 1990 full text and calibration data are required to separate geometry, penetration depth, trapped flux, and charging at the `20 ppm` level.
3. A microscopic Kubo or effective-action calculation is required to map candidate niobium collective modes onto \(\rho_{s\chi}(\omega,\mathbf k)\).
4. The positive-definite quadratic theory does not cover dissipative drag or driven phonon angular momentum.
5. The generalization to an anisotropic tensor stiffness \(R_{ab}^{ij}\) may produce orientation-dependent corrections absent from Eq. (29).
6. A real second phase should produce independent thermodynamic or spectroscopic evidence; no such niobium phase has been identified.

## Reproducibility

The arithmetic and the inversion identity are implemented in:

`02_Gravitation-Theory/Rotating-Superconductor-Response/rotating_superconductor_response.py`

The script verifies Eq. (30), the positive-definiteness thresholds, and the `84 ppm`, `92 ppm`, and `18 ppm` conversions.

## Primary Sources

1. J. Tate, B. Cabrera, S. B. Felch, and J. T. Anderson, "Precise Determination of the Cooper-Pair Mass," *Physical Review Letters* 62, 845 (1989), [DOI 10.1103/PhysRevLett.62.845](https://doi.org/10.1103/PhysRevLett.62.845). The reported result is \(m_{\rm app}/(2m_e)=1.000084(21)\).
2. J. Tate, S. B. Felch, and B. Cabrera, "Determination of the Cooper-pair mass in niobium," *Physical Review B* 42, 7885 (1990), [DOI 10.1103/PhysRevB.42.7885](https://doi.org/10.1103/PhysRevB.42.7885). Full apparatus reanalysis remains future work.
3. M. Liu, "Rotating Superconductors and the Frame-independent London Equation," *Physical Review Letters* 81, 3223 (1998), [arXiv:cond-mat/9806300](https://arxiv.org/abs/cond-mat/9806300). Provides the frame-independent current relation and the approximately \(10^{-10}\) bulk correction.
4. Y. Jiang and M. Liu, "Rotating Superconductors and the London Moment: Thermodynamics versus Microscopics," *Physical Review B* 63, 184506 (2001), [arXiv:cond-mat/0010260](https://arxiv.org/abs/cond-mat/0010260). Separates the bulk correction from the surface-double-layer contribution and gives the observed-mass form used in Eqs. (35)-(37).
5. E. Babaev and N. W. Ashcroft, "Violation of the London Law and Onsager-Feynman quantization in multicomponent superconductors," *Nature Physics* 3, 530 (2007), [arXiv:0706.2411](https://arxiv.org/abs/0706.2411). Supplies the explicit two-condensate rotational limit reproduced by Eq. (22).
6. A. F. Andreev and E. P. Bashkin, "Three-velocity hydrodynamics of superfluid solutions," *Soviet Physics JETP* 42, 164 (1975), [OSTI record](https://www.osti.gov/biblio/4106539). Establishes the general entrainment-matrix concept.
