# Unspace radial-stress torsion balance

**Paper assessed:** Lentz et al., Methodological Baseline for Probing Macroscopic Gravitational Symmetry Breaking via Radial Stress, Symmetry 18(9), 1457 (2026). [U1]

> **Assessment: gravitational attribution unsupported.** The experiment reports a spin-correlated torsion-balance response in air. Ordinary disturbances remain quantitatively unresolved. Independently of the artifact question, the proposed force law, energy integral and metric contain errors that prevent them from predicting a gravitational signal.

### 1. What the experiment measures

- **Sources:** two counter-rotating W-Ni-Cu (90/6/4) masses, 1.690 and 1.694 kg, with spherical bodies and polar shafts; equatorial radius 27 mm. Top speeds are 5,463-5,494 rad/s, approximately 52,000 rpm, with a 147 m/s rim speed.
- **Detector:** two 38.3 g test masses on 50 mm arms, suspended by a CuBe torsion ribbon. The stated 492 s period gives k = 3.16×10<super>-8</super> N·m/rad under the paper's inertia approximation. Source-to-test centre distance is about 46.6 mm; rotor-to-case clearance is 1.41 mm.
- **Readout and protocol:** a 400 Hz laser scanner with stated 20 µm displacement resolution; 30 cases at 15 speeds and two turntable stops. Rest, spinning and post-spin phases nominally last about three hours each. Measurements were made at atmospheric pressure.
- **Controls reported:** active vibration isolation, sealing and an external airflow check, motor heat sinks and thermocouples, grounding, a locked-rotor powered-motor test, magnetic surveying, counter-rotation and rotor balancing. A roughly 50 dB acoustic reduction reportedly left the signal unchanged.

### 2. Result and scope of the authors' claim

The mean static deflection is about 0.00598 rad; the rotation-associated deflection reaches 0.036-0.037 rad. The paper reports approximately quadratic speed dependence and a &gt;5σ regression result. This demonstrates a systematic response under the regression assumptions, not extraction of a gravitational signal.

The abstract explicitly acknowledges residual fluid effects and the need for vacuum testing. Sections 4.1.2 and 4.3 presume artifact dominance. Stronger claims in section 4.5 and Appendix A are conditional or speculative, and sometimes exceed those qualifications. The abstract should not be characterized as concealing the atmospheric limitation.

Authors: Phillip Lentz, Ben Peters, Evan Laske, Kevin Stephens, Jon Crombe and Bianca Esquivel, Unspace LLC. Published 30 August 2026; NSF SBIR Phase I grant 2236806. The paper cites Glenn's spark experiment, but the two experiments do not corroborate a shared quantitative prediction.

<!-- page -->

## 3. Measured response and physical scales

<!-- figure: unspace -->

**Figure 1.** Table 3 measurements and illustrative scaling estimates. The green and orange curves are approximate calculations, not validated finite-source predictions. Table 3 does not supply pointwise measurement uncertainties.

| Quantity near top speed | Value | Interpretation |
| --- | --- | --- |
| Measured rotation / mean static deflection | About 6.1 | Large spin-correlated response; cause unresolved |
| Equivalent torque / force per test mass | 1.15×10<super>-9</super> N·m / 1.15×10<super>-8</super> N | Assumes stated ribbon calibration |
| Rotational kinetic energy / rest energy | 4.84×10<super>-14</super> | GR rotational-energy deflection scale about 2.9×10<super>-16</super> rad |
| Rough centrifugal-deformation scale | About 2×10<super>-7</super> rad | Thin-disk formula and stated density; not a solved sphere model |
| Numerical substitution into paper eq. (89) | 6.20×10<super>-16</super> rad | Formula reproduction only; force derivation fails (section 6) |

### Correcting the crossover speed

At 1,089.09 rad/s the rotation magnitudes are 0.00062 and 0.00120 rad, below the 0.00489 rad static value. The claimed crossover near 1,100 rad/s is incorrect. The published fit 1.35×10<super>-9</super>ω<super>2</super> crosses the mean static value at **2,104 rad/s**. Against each pair's own static value, the pair mean remains slightly smaller at 2,474 rad/s and is clearly larger at 2,752 rad/s.

The rotational-energy scale is about 14 orders below the top-speed response. This is an order-of-magnitude comparison, not a complete GR prediction at r ≈ 1.7R. Stress, kinetic energy, deformation and supporting structures must be treated consistently. A stationary isolated system cannot acquire an arbitrary extra far-field mass by counting internal stress separately from the full conserved system.

Equation (89) is numerically about 13.8 orders below the measurement, rather than the approximately ten stated. Reproducing its arithmetic does not validate its conversion of metric perturbation into force.

<!-- page -->

## 4. Artifact budgets and measurement reliability

The equivalent force is small enough that ordinary disturbances are plausible. These budgets do not demonstrate the actual coupling from rotor to pendulum or readout. The test masses sit inside a case; rotor surface pressure is not pressure measured at a test mass.

| Illustrative budget | Numerical result | Limit of inference |
| --- | --- | --- |
| Stokes-equivalent airflow at an 8.19 mm test sphere | 4.1 mm/s | Re ≈4.5, outside strict creeping flow; an order scale only |
| Equivalent pressure difference | 5.5×10<super>-5</super> Pa | About 4×10<super>-9</super> of rotor dynamic pressure; case transfer not calculated |
| Inviscid buoyancy speed estimate over 5 cm | About 10 mK | Rayleigh number ≈128; diffusion, viscosity and enclosure geometry matter |
| Rotor environment | Re ≈2.7×10<super>5</super>; 1.41 mm gap | Steady flow, case distortion and heat transfer require measurement |

The airflow seal test, motor-region thermocouples and acoustic reduction do not supply quantified limits for every steady thermal, pressure or optical coupling. The paper acknowledges possible steady aerodynamic housing distortion. Control effectiveness must be expressed as transfer functions and residual torque limits, not inferred from qualitative absence of motion.

### Speed scaling is not a mechanism discriminator

A log-log fit above 500 rad/s gives an exponent 2.27 ± 0.09 (formal regression standard error). A one-parameter quadratic has about 3.5 times smaller residual sum of squares than a cubic. This does not distinguish stress gravity from aerodynamic forcing. Nor does it quantitatively exclude heating: thermal generation, cooling and conversion into torque can all depend on speed.

### Equilibrium, drift and the optical readout

The reported effective drift is 9.52×10<super>-4</super> rad; the example includes an overnight rest-to-spin gap. Table 5's damping coefficient and Table 2's inertia imply an amplitude decay time 2I/b ≈3.16 h. About 39% of an initial free-oscillation amplitude remains after three hours under that linear model. The paper uses fitted/back-traced equilibria, so its algorithm, residuals and drift covariance are essential; nominal waiting time alone does not validate equilibrium.

Use a fixed reference mirror through the same optical environment and a separate displacement measurement to distinguish pendulum rotation from readout motion, external hot-air refraction or window distortion. The stated 20 µm scanner resolution needs an explicit conversion to angular uncertainty and calibration against known motion.

Randomized, repeated rest-spin-rest sequences should bracket drift and estimate repeatability at each speed. Regression significance does not replace this systematic-error analysis.

<!-- page -->

## 5. Numerical audit and the GR force derivation

### 5.1 Calibration statistics and parameters

- **G arithmetic:** Table 3 yields approximately 6.32×10<super>-11</super>. Mixing signed CW values with a positive mean reproduces the reported large scatter. Magnitudes give SD ≈8.99×10<super>-12</super> and Z≈2.1 if all 30 rows were independent, or ≈1.5 treating 15 pairs as independent. These are diagnostic calculations, not a complete calibration uncertainty.
- **Geometry:** a simplified two-sphere calculation gives an opposing far-source torque of about 7.7%. Applying that correction raises inferred G to about 6.85×10<super>-11</super>. Shafts, supports, arm/mirror inertia, gravitational stiffness and positioning errors remain unmodeled; this is not a validated 5% G measurement.
- **Zero reference:** each CW/CCW rest pair has equal-magnitude deflections and a midpoint matching θ<sub>0</sub> to about 10<super>-5</super> rad. This suggests a computed midpoint, but the processing must be documented. The first row's +0.00084 is inconsistent with its subtraction; -0.00084 is implied. Thirty derived rows should not automatically be treated as independent.
- **Density and elasticity:** 7,800 kg/m<super>3</super> gives only 0.64 kg for the 27 mm sphere body. The stated alloy and test-mass geometry imply a denser material (test mass: about 16,644 kg/m<super>3</super>). Correct properties and a sphere-with-shafts model are needed. The earlier 2.9 µm disk-rim estimate is not a precise spherical deformation prediction.
- **Units and timing:** 1.666 rad/s<super>2</super> for 500 s reaches 833 rad/s, not 5,462. The controller's stated range ends at 5,236 rad/s. Equation (3) subtracts 0.00325 m although the preceding value is in radians; with a 50 mm arm, clearance would be about 9.20 mm, not 6.11 mm. Magnetic field magnitudes are not supplied.
- **Refitting:** after dropping linear and constant terms, refit the remaining coefficient. Table 3 gives 1.2701×10<super>-9</super> s<super>2</super>, rather than retaining 1.35×10<super>-9</super> from the full polynomial.

### 6. Equation (88) uses the wrong leading force component

On source p. 33, equation (88) converts c<super>2</super>∂<sub>r</sub>h<sub>rr</sub> directly into acceleration. For a stationary weak field and a slow test body, the leading acceleration follows Γ<super>i</super><sub>00</sub>. With the paper's +--- convention and g<sub>00</sub> = 1 + 2Φ/c<super>2</super>: [U2]

**a<super>i</super> ≈ -(c<super>2</super>/2) ∂<sub>i</sub>h<sub>00</sub> = -∂<sub>i</sub>Φ**

A derivative of h<sub>rr</sub> cannot replace this term. A consistent solution must include trace reversal, the full conserved stress-energy distribution, boundary conditions and source supports. Constraining the mass with a torsion spring does not change the leading gravitational force law. Equation (89) consequently lacks a valid derivation as the predicted balance response.

<!-- page -->

## 7. Energy integral and proposed metric

### 7.1 Changing kernels and an unspecified reference

Equation (68) uses a two-dimensional logarithmic Green function. Equations (92)-(95) use 1/(2π|r-r′|), whereas (97) and (107) return to a logarithm. These are different kernels. With T<sub>rr</sub> in Pa and dV in m<super>3</super>, printed equation (95) has units **J/m, not J**. A finite thin disk in three-dimensional space does not automatically have a two-dimensional logarithmic gravitational field.

A logarithm requires ln(distance/L<sub>0</sub>) and boundary conditions. Evaluating (107) literally yields -4.08×10<super>-13</super> J with metre-valued arguments, +1.16×10<super>-13</super> J with centimetre-valued arguments, and -1.35×10<super>-12</super> J if the slice half-thickness is the source radius. The paper reports +4.90×10<super>-13</super> J. This exposes an unspecified reference/normalization; changing units consistently at fixed physical L<sub>0</sub> would not change the result. Potential sign alone is not a test of gravity.

The extra (ωr′/c)<super>2</super> factor supplies the desired ω<super>4</super> scaling; the chosen Z = R<sub>p</sub> slice sets an amplitude. The claimed angular restriction θ<sub>max</sub> = ωR/c is unproved: slow rotation does not confine contributing source material to a tiny wedge. Table 6's experimental energy at 2,085 rad/s is 4.44×10<super>-13</super> J, while (109) gives 5.44×10<super>-13</super> J.

### 7.2 Stored detector energy is not a source force law

A source integral must predict an interaction energy and its angular derivative, or an equation of motion. Matching a number to kδθ<super>2</super>/2 does not do this. For a fixed torque, θ = τ/k and the spring stores τ<super>2</super>/(2k), which depends on detector stiffness. Equation (9) also equates half kδθ<super>2</super> to final torque times δθ, a factor-of-two inconsistency. A preloaded ribbon's actual energy change includes kθ<sub>rest</sub>δθ; removing it requires an explicitly defined effective potential.

### 7.3 Appendix A fails its own energy and sign checks

Equation (A2) identifies -U<sub>rest</sub>/m with -GM/r. The parameters give stored ribbon energy 5.64×10<super>-13</super> J, versus 9.28×10<super>-11</super> J for GMm/r from one nearby source: a factor of about 165. These are physically different energies, irrespective of numerical agreement.

**Equations (A4)-(A6): √[E<sub>s</sub> / (mΦ<sub>rest</sub>)]**

With positive tabulated E<sub>s</sub> and negative Φ<sub>rest</sub>, the radicand is negative and g<sub>tt</sub> becomes complex. A factor-of-two convention cannot fix the sign. Using the negative logarithmic result instead abandons the published positive-energy match and still fails (A2). The metric also contains detector mass m and the test-radius slice; no derivation removes this dependence in the test-body limit.

<!-- page -->

## 8. Interpretation, tests and provenance

**Astrophysical extrapolation:** a stationary axisymmetric field conserves orbital energy. Anisotropy alone cannot produce different incoming/outgoing asymptotic spacecraft speeds in the source frame. The flyby explanation needs time dependence or an energy-transfer mechanism. A speed-dependent pulsar moment of inertia also needs a specified torque law and I(ω); it does not itself supply a quantitative braking-index prediction. [U1, Appendix A; U2]

| Control or analysis | What it can establish; remaining conditions |
| --- | --- |
| Pressure/gas series; case thermometry | Test gas-mediated coupling while measuring motor load, case temperature and thermal gradients. Density-only scaling or unchanged signal is not decisive. |
| Grounded barrier; fixed reference mirror; independent displacement | Separate flow/electric coupling and readout artifacts. Monitor barrier motion, window effects and mechanical transfer. |
| Alternate rotor material; distance/gap scan | Compare explicit force predictions. Account for density, Poisson ratio, conductivity, magnetism, balance and motor loading; aluminium is not a one-variable substitution. |
| Co-/counter-rotation; different ribbon stiffness | Test directional coupling and detector dependence. Stiffness tests the energy ansatz; ordinary and gravitational external torques both follow mechanical response. |
| Randomized repeated runs; complete records | Estimate repeatability, drift and fitted-equilibrium errors. Publish synchronized displacement, speed, temperature, vibration and analysis code. |

### Data availability and project relevance

The source states that TDMS and drift records are on Zenodo (10.5281/zenodo.21909560). The initial audit recorded a README and a small summary workbook rather than full time series. Retrieval during the independent review failed, so current deposit contents are **not independently reverified**. The source's supplement describes compiled results; continuous records and processing are needed to reproduce the fits.

**Evidence rating: E for anomalous gravitational attribution; C as an apparatus description** (internal project scale). The paper reports measurements and engineering details, but establishes neither a new gravitational mechanism, a validated quantitative constraint on one, nor a universal metric response. No project gate decision changes. The exact conventional origin of the response remains unresolved.

### Sources and reproducible checks

[U1] Lentz et al. (2026), [doi:10.3390/sym18091457](https://doi.org/10.3390/sym18091457). Locators: Table 3; §§2.4, 3.3-3.6, 4.1-4.6; equations (3), (9), (88)-(109), (A1)-(A6). Canonical source PDF remains in 03_Propulsion-and-Anomalies/.

[U2] S. Carroll, [Lecture Notes on General Relativity](https://arxiv.org/abs/gr-qc/9712019), Newtonian limit, Killing symmetries and weak fields. Force and conservation objections are applications of these principles to [U1].

Calculation package: 02_Gravitation-Theory/Unspace-Glenn-Claim-Audit/. Run unspace_glenn_claim_checks.py, then build_assessment_pdfs.py. The builder also runs independent_review_checks_2026-11-13.py. This knowledgebase digest is the editable source for the revised PDF; published inputs, arithmetic reproductions and physical scales are distinguished above.
