# Tate Finite Ring and Measurement Audit

**Date:** 2026-09-04  
**Scope:** map the July 24 stiffness kernel to finite-ring winding and pickup observables; audit accessible primary evidence.  
**Companion calculation:** [tate_ring_analysis.py](../02_Gravitation-Theory/Tate-Ring-Analysis/tate_ring_analysis.py).  
**Source audit:** [primary-source and input manifest](../02_Gravitation-Theory/Tate-Ring-Analysis/sources/SOURCE-AND-INPUT-MANIFEST-2026-09-04.md).

## Target

Derive the rotation-frequency spacing between specified winding branches of a finite superconducting ring, retaining its magnetic self-inductance, kinetic inductance, and pickup geometry. Determine which coefficients this observable can identify. This is an identity/proposition and bounded numerical calculation, not a microscopic niobium theory or a re-fit of Tate data.

The exact measurement target is a sequence of **zeros of a defined, background-corrected pickup observable**. Published abstracts refer to successive zero-flux rotation frequencies; their complete zero estimator, background subtraction, and geometry were not recovered. Consequently, identifying the model pickup-zero with every operational detail of Tate's measured zero remains an explicit missing step.

## Status

**COHERENT AFTER REFRAMING / EXTRA ASSUMPTION.**

The finite-loop calculation is completed under the assumptions below. It produces three substantive results:

1. Winding-sector spacing depends on both the bulk rotation coefficient and the winding-flux coefficient. For the two-component kernel, when the electronic winding changes by one and the other winding is fixed,

   \[
   \boxed{\frac{m_{\rm spacing}}{m_s}=
   \frac{1+x+y(x+r)}{1+xy}.}
   \tag{1}
   \]

   This differs from the bulk-field ratio, whose denominator is \(1+2xy+ry^2\). The July 24 **neutral** specialization \(y=0\), \(m_{\rm spacing}/m_s=1+x\), survives, conditional on fixed neutral winding and calibrated finite-geometry/surface effects. The July 24 general charged inversion must not be substituted directly into a winding-spacing measurement.

2. In a narrow loop, inductance changes signal amplitude but cancels from the ideal zero spacing. In a finite-width film, penetration depth and pickup geometry generally enter a derived effective area. A zero of pickup flux does not require all local film currents to vanish.

3. The accessible experimental record supplies the published summary \(m_{\rm app}/(2m_e)=1.000084(21)\), but does not supply the raw observations and calibration covariance needed to separate geometry, surface response, trapped-flux history, or a hypothetical neutral mode. No empirical decomposition or revised significance is claimed.

## Invariant Object

The organizing object is the gauge-invariant circulation source and its transfer to the measured pickup:

\[
\Psi_{\boldsymbol n}\equiv
\frac{Q^T R\Gamma_{\boldsymbol n}}{Q^T RQ},
\qquad (\Gamma_{\boldsymbol n})_a=\frac{h n_a}{m_a}.
\tag{2}
\]

Here \(n_a\) is the integer winding of a genuinely independent coherent phase. Neither the unqualified bulk magnetic field nor the magnetic flux alone replaces this object.

## Assumptions

- Slow stationary rotation about the ring axis; \(\nu=\Omega/(2\pi)\) is cyclic frequency in Hz, while \(\Omega\) is angular speed in rad/s.
- A connected annular superconducting film with no vortices crossing its material during each stationary branch. A hole permits nonzero winding even though the material is locally vortex-free.
- The ordinary crystal is mechanically clamped to the rotating substrate. It is not an additional compact phase.
- The hypothetical additional components have independently meaningful windings unless an explicitly specified locking law removes that independence. Their existence in niobium is not assumed as evidence.
- Local isotropic, nondissipative, positive-definite stiffness \(R\); linear quasistatic electromagnetism. Its charge-to-mass vector \(Q_a=q_a/m_a\) uses signed charges.
- For the closed annulus formulas, stiffness ratios and masses are homogeneous. Penetration depth can enter the electromagnetic operator but not vary with winding or rotation within a fitted sequence.
- The thin-film numerical example assumes an axisymmetric film, thickness small compared with penetration depth, negligible thickness variation, and small width/radius. It is an illustrative finite-width electromagnetic model, not the recovered Tate geometry.
- External magnetic background and readout coefficients are constant between compared branches unless represented as explicit nuisances.
- Gravity is absent. The thermodynamic and moving-surface corrections are tracked separately from the baseline kernel; neither is counted twice as an area correction.

## Notation

| Symbol | Meaning |
|---|---|
| \(m_s,q_s\) | Electronic pair mass parameter and signed charge, \(q_s=-2e\) |
| \(R, Q,\boldsymbol 1\) | Stiffness matrix, charge-to-mass vector, all-ones vector |
| \(D=Q^TRQ>0\) | Electromagnetic stiffness; \(\lambda^2=1/(\mu_0D)\) in this baseline |
| \(K=Q^TR\boldsymbol1/D\) | Bulk rotation-to-field coefficient, \(B=-2K\Omega\) |
| \(\Gamma_a,\Psi_{\boldsymbol n}\) | Phase circulation and projected winding-flux source |
| \(S,\ell,A_c\) | Loop area, circumference, current-carrying cross section |
| \(\Phi,\Phi_{\rm ext}\) | Total magnetic flux and externally sourced magnetic flux |
| \(L_g,L_k,\mathsf L\) | Geometric, kinetic, and full discretized inductance |
| \(I_i,M_i,\phi_p\) | Azimuthal strip current, pickup mutual inductance, pickup flux |
| \(U,V,S_{\rm eff}=V/U\) | Winding transfer, rotation transfer divided by \(2K\), effective area |
| \(x,r,y\) | \(\rho_{s\chi}/\rho_s,\rho_\chi/\rho_s,Q_\chi/Q_s\); positivity requires \(r>x^2\) |
| \(\zeta,\alpha\) | Conventional bulk chemical-potential and external surface corrections in the cited theory |
| \(S_{\rm ref},m_{\rm app}\) | Area used in data reduction and mass parameter inferred from measured frequency spacing |

## Derivation Strategy

Start from the existing matter-current kernel, integrate gauge kinematics around the hole, and only then solve the electromagnetic boundary/readout problem. Derive winding steps before interpreting a spacing as a mass. Use the narrow-loop reduction as a limiting case of the finite-width operator, and carry the remaining observable-level nuisances into an identifiability calculation.

## Derivation Map

1. Compact phase kinematics supplies circulation integers; rigid-body rotation contributes \(2\Omega S\).
2. Project circulation through the same stiffness matrix that supplies the charge current.
3. Eliminate the self-field with geometric and kinetic inductance.
4. Project the finite current distribution through the actual pickup coupling.
5. Compare specified winding sectors and convert angular to cyclic frequency.
6. Separate neutral fixed-winding, relaxed-winding, and phase-locked interpretations.
7. Add conventional surface/geometry calibration and derive covariance and parameter rank.

## Main Derivation

### Step 1 — Circulation is not a local zero-current condition

**Identity within the phase model.** Define

\[
\mathbf w_a=\frac{\hbar}{m_a}\nabla\theta_a-Q_a\mathbf A
-\boldsymbol\Omega\times\mathbf r.
\]

For an oriented contour \(C\) around the ring hole,

\[
\oint_C\mathbf w_a\cdot d\mathbf l
=\frac{h n_a}{m_a}-Q_a\Phi_C-2\Omega S_C.
\tag{3}
\]

The second term uses Stokes' theorem for the magnetic vector potential; the third is rigid-rotation circulation. Winding is compatible with \(\nabla\times\nabla\theta_a=0\) in the annular material because a surface spanning the hole is not contained in that material.

### Step 2 — Generalized fluxoid from the existing kernel

**Identity for spatially constant \(R,Q\).** The already-derived current law is

\[
\mathbf j_q=Q^TR\mathbf w.
\]

Multiplying Eq. (3) by \(Q^TR\), summing, and dividing by \(D\) gives

\[
\boxed{\Phi_C+\frac1D\oint_C\mathbf j_q\cdot d\mathbf l
=\Psi_{\boldsymbol n}-2K\Omega S_C.}
\tag{4}
\]

For one component, \(\Psi_n=nh/q_s\), \(K=m_s/q_s\). The left side is a fluxoid, not just magnetic flux. For several independently wound phases, the projected source \(\Psi_{\boldsymbol n}\) need not be an integer multiple of one universal flux quantum; accessible composite sectors depend on the coupling and phase-slip physics.

### Step 3 — Narrow-loop reduction

**Approximation.** Let the current be uniform over a narrow cross section with circumference \(\ell\). Then

\[
L_k=\frac{\ell}{D A_c}=\mu_0\lambda^2\frac{\ell}{A_c},
\quad \Phi=\Phi_{\rm ext}+L_g I,
\]

\[
\boxed{(L_g+L_k)I=\Psi_{\boldsymbol n}-\Phi_{\rm ext}-2K\Omega S.}
\tag{5}
\]

**Proposition.** With unchanged background, the ideal circulating-current zero on branch \(\boldsymbol n\) is

\[
\Omega_{\boldsymbol n}=\frac{\Psi_{\boldsymbol n}-\Phi_{\rm ext}}{2KS}.
\tag{6}
\]

Positive inductance changes the flux/rotation slope but not this root. A fixed trapped/background flux shifts the intercept but not adjacent spacing. A rotation-dependent background or a changing winding sector does change the result. Taking stiffness to zero does not create a measurable robust root: signal amplitude then vanishes and superconducting phase/winding assumptions eventually cease to apply.

### Step 4 — Finite-width film and pickup geometry

**Linear electromagnetic discretization.** Partition an axisymmetric thin film into radial azimuthal strips. Each strip has area \(S_i=\pi r_i^2\), current \(I_i\), and self/mutual magnetic flux \(\sum_j (L_g)_{ij}I_j\). With no vortex between strips, each independent phase has the same winding integer at every radius. Let

\[
\mathsf L=L_g+\operatorname{diag}(L_{k,i}),
\qquad L_{k,i}=\mu_0\lambda^2\frac{2\pi r_i}{t\,\Delta r_i}.
\]

Equation (4) becomes

\[
\mathsf L\mathbf I=\Psi_{\boldsymbol n}\boldsymbol1
-2K\Omega\mathbf S-\boldsymbol\Phi_{\rm ext}.
\tag{7}
\]

For pickup mutual-inductance vector \(\mathbf M\), after subtracting a specified direct external pickup contribution,

\[
\phi_p=\mathbf M^T\mathbf I+b_0+b_\Omega\Omega.
\tag{8}
\]

Here \(b_0,b_\Omega\) are residual readout/background terms, not an assumed anomalous current. A full boundary calculation may put a moving-surface response into \(\mathsf L\), the source vectors, or a direct pickup term; Eq. (8) is an explicit linear observable parameterization, not a universal microscopic surface model.

Define

\[
U=\mathbf M^T\mathsf L^{-1}\boldsymbol1,
\quad V=\mathbf M^T\mathsf L^{-1}\mathbf S,
\quad c_0=b_0-\mathbf M^T\mathsf L^{-1}\boldsymbol\Phi_{\rm ext}.
\]

Then

\[
\phi_p=U\Psi_{\boldsymbol n}-(2KV-b_\Omega)\Omega+c_0.
\tag{9}
\]

**Proposition in the linear model.** Provided \(U\neq0\) and \(2KV-b_\Omega\neq0\), roots from winding steps \(\Delta\boldsymbol n\) obey

\[
\Delta\Omega=\frac{U\Delta\Psi}{2KV-b_\Omega},
\qquad
\Delta\nu_{\rm Hz}=\frac{U\Delta\Psi}{2\pi(2KV-b_\Omega)}.
\tag{10}
\]

For a baseline with \(b_\Omega=0\), define

\[
\boxed{S_{\rm eff}=\frac{\mathbf M^T\mathsf L^{-1}\mathbf S}
{\mathbf M^T\mathsf L^{-1}\boldsymbol1},\qquad
\Delta\nu_{\rm Hz}=\frac{\Delta\Psi}{4\pi K S_{\rm eff}}.}
\tag{11}
\]

This is a derived effective area, not automatically the inner-hole, film-center, or optical rotor area. If every \(S_i=S\), Eq. (11) reduces identically to the narrow-loop result, regardless of \(\mathsf L\) or pickup gain. For finite width, the weights depend on penetration and pickup. They are not asserted positive for every possible circuit; there is no general claim that the resulting area must lie between the smallest and largest strip areas.

At a finite-width pickup root, \(\mathbf M^T\mathbf I=0\) can result from currents of both signs. Setting every strip current to zero before solving this problem would remove the very finite-width correction being audited.

### Step 5 — The observable mass depends on the winding step

**Identity.** If one defines a mass parameter from the ideal spacing using the correctly computed area,

\[
m_{\rm spacing}\equiv\frac{h}{4\pi S_{\rm eff}\Delta\nu_{\rm Hz}}
=\frac{hK}{\Delta\Psi},
\]

\[
\boxed{m_{\rm spacing}=
\frac{Q^TR\boldsymbol1}
{Q^TR\operatorname{diag}(1/m_a)\Delta\boldsymbol n}.}
\tag{12}
\]

The signed ordering of branches must be chosen consistently; a reported positive spacing uses the corresponding magnitude. When \(\Delta\Psi=0\), that step supplies no magnetic zero-spacing observable and this mass definition is undefined.

For the two-component normalization

\[
R=\rho_s\begin{pmatrix}1&x\\x&r\end{pmatrix},
\quad Q=Q_s(1,y)^T,
\]

the winding increment \(\Delta\boldsymbol n=(1,0)\) gives

\[
K=\frac1{Q_s}\frac{1+x+y(x+r)}{1+2xy+ry^2},
\quad
\Delta\Psi_s=\frac h{q_s}\frac{1+xy}{1+2xy+ry^2}.
\tag{13}
\]

Dividing proves Eq. (1). The denominator of the bulk ratio cancels from the spacing ratio. A generic bulk \(B/\Omega\) inversion therefore cannot be called a complete Tate-ring inversion.

**One-component normalization check:**

\[
\Delta\Omega=\frac h{2m_s S},\qquad
\Delta\nu_{\rm Hz}=\frac h{4\pi m_s S},\qquad
\boxed{\frac{\hbar}{m_s}=2S\Delta\nu_{\rm Hz}.}
\tag{14}
\]

The APS PRB abstract's \(h/(2\pi m')=2S\Delta\nu\) is consistent with Eq. (14). Dropping the bar on \(\hbar\) in extracted text introduces a factor \(2\pi\) error; Hz and angular speed are kept separate throughout.

### Step 6 — Neutral winding, equilibration, and phase locking

**Conditional result.** For \(y=0\),

\[
\Psi_{n_s,n_\chi}=\frac h{q_s}
\left(n_s+x\frac{m_s}{m_\chi}n_\chi\right),
\quad K=\frac{1+x}{Q_s},
\]

\[
\boxed{\frac{m_{\rm spacing}}{m_s}=
\frac{1+x}{\Delta n_s+x(m_s/m_\chi)\Delta n_\chi}.}
\tag{15}
\]

The familiar \(1+x\) result requires \(\Delta n_s=1,\Delta n_\chi=0\). There is presently no evidence establishing a neutral niobium phase, its phase-slip rate, its winding lifetime, or the winding preparation needed for this interpretation.

**Relaxed neutral circulation, continuous approximation.** In the narrow loop the local kinetic energy is proportional to \(w_s^2+2xw_sw_\chi+rw_\chi^2\). If neutral circulation can relax continuously, minimization over \(w_\chi\) gives

\[
xw_s+rw_\chi=0,
\quad j_q=Q_s\rho_s(1-x^2/r)w_s.
\tag{16}
\]

At an ideal current zero, positivity \(r>x^2\) then implies \(w_s=w_\chi=0\): the ordinary spacing is recovered. Actual neutral winding is integer-valued, so this is a coarse-grained limit of frequent phase slips, not an exact replacement of topology. Discrete relaxation can instead produce additional steps, offsets, and hysteresis. If \(\Delta n_\chi=(m_\chi/m_s)\Delta n_s\) is an accessible commensurate integer step, Eq. (15) recovers the ordinary spacing exactly. The code verifies this distinct limiting case.

More explicitly, in the narrow-loop zero-charge-current sector \(w_s=-xw_\chi\), the remaining kinetic energy density is

\[
f_{j_q=0}=\frac12\rho_s(r-x^2)
\left[\frac{h n_\chi/m_\chi-2\Omega S}{\ell}\right]^2.
\]

Its unconstrained neutral minimum favors the integer nearest \(2m_\chi\Omega S/h\). This exposes the scale of neutral winding changes; an actual branch selection also obeys electronic winding, electromagnetic energy, and barriers. Positive definiteness guarantees positive residual stiffness, not preparation or lifetime of a fixed neutral sector.

**Phase locking.** An ordinary Josephson term only makes sense for a gauge-invariant relative phase combination. Two equal-charge condensates can have their relative phase locked, restricting accessible winding increments and removing the independent neutral-winding assumption. A charged electronic condensate and a genuinely neutral condensate cannot be assigned \(\cos(\theta_s-\theta_\chi)\) as a gauge-invariant locking term without additional charged fields. Any permitted locking/conversion operator must be supplied before specifying \(\Delta\boldsymbol n\). The spectrum, activation barriers, and scan history are physical inputs, not merely algebraic choices.

### Step 7 — Surface, thermodynamic, and area bookkeeping

**Primary-theory distinction.** Liu's bulk chemical-potential correction is approximately \(\zeta\sim10^{-10}\). Jiang–Liu retain an external moving-surface correction and write \(m_{\rm obs}=(1+\zeta)(1-\alpha)m_e\); their work-function scale gives \(\alpha\simeq8\times10^{-6}\). The normalized pair ratio has the same multiplicative correction. These statements are verified in [Liu 1998, PDF p2](https://arxiv.org/abs/cond-mat/9806300) and [Jiang–Liu 2001, PDF p6 Eqs. 56–58; p7 Eq. 75](https://arxiv.org/abs/cond-mat/0010260). The latter paper uses rationalized Heaviside–Lorentz units: its \(1/r\) vector-potential coefficient is not the full SI flux quantum.

**Observable parameterization, not a newly derived microscopic portal.** For the neutral fixed-winding limit, if a boundary calculation justifies the cited multiplicative surface form, and no additional pickup nuisance remains,

\[
\frac{m_{\rm app}}{2m_e}=
\frac{m_s}{2m_e}\,(1+x)(1+\zeta)(1-\alpha)
\frac{S_{\rm eff}}{S_{\rm ref}}.
\tag{17}
\]

Here \(m_s/(2m_e)\) is the baseline mass parameter. The baseline electromagnetic \(S_{\rm eff}\) includes penetration and pickup but excludes the separately modeled moving-surface term. Alternatively, solve the full surface boundary problem inside the transfer coefficients and set the separate \(\alpha\) correction to zero. Applying both would double count the surface effect. The conventional \(\zeta\) correction is also applied once; no hypothetical multicomponent generalization of it is claimed.

The same warning applies to \(S_{\rm ref}\): if an experimental reduction already corrected optical area into a magnetic effective area, an additional independent area correction must not be applied again. The unavailable complete reduction protocol is needed to establish that mapping.

The published comparisons remain

\[
1.000084-1=84\ {\rm ppm},\qquad
1.000084-0.999992=92\ {\rm ppm}.
\tag{18}
\]

These are absolute normalized-ratio differences. The multiplicative residual is \(1.000084/0.999992-1=92.000736\ldots\) ppm, negligible at the published precision but conceptually distinct. No uncertainty on the approximate theory comparator is supplied here, so dividing 92 ppm by the experimental 21 ppm is not a complete model-comparison significance calculation.

### Step 8 — Covariance and identifiability

**Statistical model.** For an identified sequence with fixed winding increments and stable coefficients, fit

\[
\nu_n=a+n\Delta\nu+\epsilon_n,
\quad \operatorname{Cov}(\boldsymbol\epsilon)=C,
\]

\[
\hat\beta=(X^TC^{-1}X)^{-1}X^TC^{-1}\boldsymbol\nu,
\quad C_\beta=(X^TC^{-1}X)^{-1}.
\tag{19}
\]

This covariance applies to the specified linear noise model, not automatically to frequency-dependent systematics. A constant common offset contributes to \(a\); frequency-scale calibration contributes a shared multiplicative error to the slope. Branch-dependent trapped-flux changes, drift, and misidentified slips require additional nuisance terms and can invalidate a single-spacing fit.

For an ideal one-component mass reduction,

\[
\ln m_{\rm app}=\ln h-\ln(4\pi)-\ln S_{\rm ref}-\ln\Delta\nu.
\]

Thus area and spacing covariance enters with a **positive** cross term:

\[
\operatorname{Var}(\ln m_{\rm app})=
\operatorname{Var}(\ln S_{\rm ref})+
\operatorname{Var}(\ln\Delta\nu)+
2\operatorname{Cov}(\ln S_{\rm ref},\ln\Delta\nu),
\tag{20}
\]

before adding other calibration/reference uncertainties. If area is approximated by two perpendicular diameters \(S=\pi d_1d_2/4\), its log error is \(d\ln S=d\ln d_1+d\ln d_2\). That is an ellipse/metrology reduction, not a claim that two diameters completely describe all rotor roundness. Common laser frequency and thermal-calibration errors make the diameter errors correlated.

To infer a small neutral shift using Eq. (17), holding the baseline parameter \(m_s/(2m_e)\) fixed,

\[
d\ln(1+x)=d\ln(m_{\rm app}/2m_e)
-d\ln(S_{\rm eff}/S_{\rm ref})
-\frac{d\zeta}{1+\zeta}+\frac{d\alpha}{1-\alpha}.
\tag{21}
\]

If that baseline is uncertain, also subtract \(d\ln[m_s/(2m_e)]\) on the right. Let \(J_{\log}\) be the Jacobian of \(\ln(1+x)\) with respect to all calibrated/nuisance inputs \(\theta\); then \(J_x=(1+x)J_{\log}\) and \(\sigma_x^2\simeq J_xC_\theta J_x^T\). Use this full covariance propagation rather than adding guessed systematic magnitudes in quadrature. Constants used to normalize an old \(h/m\) measurement also have a measurement-era convention; the unrounded primary observable is needed before reexpressing it under newer constants.

**Identifiability result.** With one unchanged geometry, repeated spacing measurements constrain one combination, approximately

\[
\delta\ln m_{\rm app}\simeq x+\zeta-\alpha+
\delta\ln(S_{\rm eff}/S_{\rm ref}).
\tag{22}
\]

The local design columns for \(x\), an area scale, and a surface offset are collinear: rank one. Repeating the same measurement reduces noise but does not separate these explanations. Absolute pickup slopes and flux-step amplitudes provide useful calibration checks, but their ratio reproduces the same spacing and is not automatically a new independent microscopic constraint. Independently calibrated geometry/penetration and surface response, or independently established mode/winding observables, are required to increase rank.

## Completed Numerical Verification

The [Python calculation](../02_Gravitation-Theory/Tate-Ring-Analysis/tate_ring_analysis.py) uses NumPy/SciPy and writes [verification_results.json](../02_Gravitation-Theory/Tate-Ring-Analysis/verification_results.json) and [synthetic_annulus_sensitivity.csv](../02_Gravitation-Theory/Tate-Ring-Analysis/synthetic_annulus_sensitivity.csv). It verifies eight groups of checks: single-component units and inductance-independent zeros; fixed and co-winding neutral limits; 200 positive-stiffness charged examples; equal-charge/mass common winding; constant-flux offsets; correlated-noise GLS; parameter rank; and finite-film roots/mesh refinement.

The finite-width magnetic operator uses the coaxial Neumann mutual-inductance kernel, expressed with complete elliptic integrals. Strip self terms and neighboring terms include the cell-averaged logarithmic singularity. The diagonal self approximation uses geometric mean distance \(e^{-3/2}\Delta r\). This is a controlled thin-strip quadrature, not a full three-dimensional finite-element model. Its positive spectrum is checked for each reported case.

**All geometry and uncertainty examples below are synthetic, not Tate apparatus inputs or data.** The illustrative annulus has mean radius 10 mm, width 0.2 mm, thickness 5 nm, with a coaxial pickup of radius 8 mm at axial separation 1 mm. Material viability of this film is not claimed; dimensions define the linear model only.

| Assumed penetration depth | \(10^6[S_{\rm eff}/(\pi r_0^2)-1]\) at 512 strips | Change from 256 to 512 strips |
|---|---:|---:|
| 50 nm | -1183.099 ppm | -0.195 ppm |
| 100 nm | -1097.420 ppm | -0.061 ppm |
| 200 nm | -890.333 ppm | -0.018 ppm |

These values demonstrate that an uncalibrated geometric area can differ materially from a pickup-weighted area, and that penetration can influence that difference. They do **not** estimate any actual Tate correction or explain 92 ppm. Mesh differences quantify numerical refinement of this approximate model, not total physical model uncertainty. Thin-film, thin-strip and source/readout mapping approximations have not been bounded at ppm precision and can exceed the displayed mesh differences. At the computed pickup root, the summed pickup signal vanishes while strip currents of both signs remain.

A separate **synthetic** uncertainty example assigns 8 ppm area, 5 ppm spacing, and 3 ppm surface uncertainty. For area/spacing correlations \(-0.8,0,+0.8\), the inferred-shift standard uncertainties are respectively 5.83, 9.90, and 12.73 ppm. These numbers illustrate why covariance matters; none is an experimental uncertainty reconstruction.

## Primary Evidence and Missing Inputs

The [1989 PRL abstract](https://doi.org/10.1103/PhysRevLett.62.845) and [1990 PRB abstract](https://doi.org/10.1103/PhysRevB.42.7885) support the published ratio and the area/zero-spacing measurement. A historical [Stanford thesis-abstract collection](https://einstein.stanford.edu/content/sci_papers/abstracts.pdf), PDF p40/printed p39, describes a thin-film niobium equatorial ring on a quartz hemispherical rotor, a helium gas bearing at 6 K, SQUID flux readout, and two perpendicular diameter measurements. It is a 1987 abstract, not the full thesis; its 30 ppm systematic uncertainty must not replace the later journal's 21 ppm result.

The publisher-deposited abstract for [Tate, McIntyre and Cabrera's diameter metrology paper](https://doi.org/10.1063/1.1140291) states 200 nm/4 ppm measurement accuracy. This is not a measured rotor diameter; no numerical Tate ring radius is inferred from those rounded figures. Source PDFs, checked page evidence, metadata, hashes, and access failures are recorded in the [source manifest](../02_Gravitation-Theory/Tate-Ring-Analysis/sources/SOURCE-AND-INPUT-MANIFEST-2026-09-04.md).

| Missing input | What it prevents | Required form |
|---|---|---|
| Full 1990 paper and complete reduction/systematic table | Identifying already-applied corrections and the operational zero | Original equations, tables, acquisition/reduction description |
| Raw flux/rotation sweeps and branch history | New spacing fit, drift and phase-slip audit | Time-stamped sweeps, winding labels, zero estimator, temperature/spin history |
| Film width/thickness/profile and actual diameter/roundness data | Calculating actual \(\mathsf L\), area and geometry covariance | Cryogenic geometry with calibration provenance/covariance |
| Pickup and shielding geometry | Mapping measured SQUID zero to Eq. (9) | Mutual coupling, direct pickup and background-subtraction calibration |
| Penetration depth versus temperature, field and film state | Distinguishing geometry response from intrinsic coefficient | Same-film measurements with uncertainty |
| Rotor charge, surface state and work-function history | Separating rotation-dependent electric/surface contributions | Controlled charge and surface measurements or justified constraints |
| Unrounded original \(h/m\), reference constants, covariance | Updating normalization or significance | Original numerical estimate and calibration correlations |
| Hypothetical neutral-mode existence and winding dynamics | Interpreting Eq. (15) as material physics | Independent spectroscopy/thermodynamics and phase-slip/locking evidence |

No actual frequency spacing, radius, film dimensions, or calibration covariance is fabricated. No Hoang value is admitted as independent numerical input; the source audit found an affiliation-only corrigendum but no full results/calibration package.

## Remarks and Interpretation

- The completed July 24 calculation remains a valid bulk-kernel result in its own scope. This report repairs the missing mapping between that kernel and a finite multiply connected measurement.
- The neutral 92 ppm cross-stiffness remains a conditional numerical target, not a discovered niobium coefficient. In a finite ring its interpretation additionally requires the winding protocol, geometry, and surface observable to be controlled.
- An extra phase does not automatically produce a stable anomalous spacing: its winding may be pinned, relax, lock, or change discontinuously. Those cases have distinct formulas and signatures.
- The finite-width calculation gives a concrete reason to demand primary apparatus data; it does not establish that an unmodeled conventional correction exists in Tate's original reduction.
- Neither a London coefficient nor an unexplained magnetic residual supplies a gravitational response. Any gravity claim requires a separate non-electromagnetic observable and stress-energy calculation.

## Boundaries and Non-Claims

- No full Tate reanalysis, empirical fit, revised mass estimate, anomaly explanation, or independent replication has been performed.
- No known niobium neutral condensate, ionic phase inheritance, gravitational gain, or shielding is established.
- The thin-film annulus operator excludes arbitrary three-dimensional non-axisymmetric geometry, finite-thickness corrections, anisotropic/nonlocal kernels, vortices, and dissipation.
- Equations (1), (12), and (15) are conditional on the stated winding sectors. They do not prove those sectors are accessible or stable in any candidate material.
- The surface factor in Eq. (17) is a primary-theory-informed observable parameterization; an actual finite-ring interface solution is required to apply it to an apparatus.
- Numerical refinement errors are separate from model approximations and the missing empirical input errors.

## Open Risks and Decisive Next Measurement

The historical-data task is blocked specifically at full apparatus/reduction documentation and raw covariance, not at the finite-ring algebra. Obtain those records before an empirical re-fit.

For a new discriminating measurement, use **one characterized rotating ring with two independently calibrated pickup geometries**, measured over temperature with independently measured penetration depth and controlled surface/charge state. Fit the full flux-versus-rotation branches, including flux steps and offsets, rather than only a final apparent mass. The two geometries test whether a common intrinsic coefficient survives different derived \(S_{\rm eff}\) factors. Repeat scans at different rates and reversal histories to test fixed versus relaxed winding and drift. If an additional coherent field is proposed, require its independent spectroscopic signature and an operator-consistent winding/locking model before interpreting residual spacing as \(x\).

The decision product is a joint model whose calibrated nuisance columns and proposed intrinsic-response column are independently constrained. A residual that survives that test remains a matter-response result until a separate gravitational measurement is supplied.
