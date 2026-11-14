# Independent review of the Unspace and Glenn assessments

Reviewed 13 November 2026. Scope: disagreements with, and omissions from, the two Opus technical assessments. **Implemented the same day:** both assessment PDFs were replaced at Kurt's request, without retaining the previous PDF editions. Their knowledgebase digests are now the revised PDF authoring source. Original research papers and calculation inputs remain unchanged. Assessment page numbers below are historical references to the replaced editions, not the current PDFs.

## Overall judgment

I agree that neither experiment establishes an anomalous gravitational effect. The assessments identify important problems, particularly Glenn's wavelength argument and Unspace's fitted energy comparison. However, they sometimes turn a plausible conventional explanation into an asserted identification, overstate what a single control would settle, and overlook more fundamental mathematical problems in Unspace's derivation.

The strongest additional findings are the incorrect conversion of a spatial metric perturbation into a static force, the changing Green-function kernel, and the invalid energy/metric construction in Unspace Appendix A. These do not depend on identifying the actual laboratory artifact.

## Sources and reproducibility

- Assessment: `../../01_Reports-and-Syntheses/Unspace-Radial-Stress-Torsion-Balance-Technical-Assessment-2026-11-13.pdf` (reviewed edition: 5 pages; replaced by revised 6-page report).
- Assessment: `../../01_Reports-and-Syntheses/Glenn-Spark-Gap-Interferometry-Technical-Assessment-2026-11-13.pdf` (reviewed edition: 4 pages; replaced by revised 5-page report).
- Unspace source: `../../03_Propulsion-and-Anomalies/Lentz-Methodological-Baseline-Radial-Stress-Gravitational-Symmetry-Breaking-Symmetry-2026.pdf` (46 pages); [publisher](https://www.mdpi.com/2073-8994/18/9/1457).
- Glenn source: `../../03_Propulsion-and-Anomalies/Glenn-Experimental-Spacetime-Distortion-Spark-Gap-Gravitational-Waves-EJENG-2025.pdf` (10 pages; printed journal pp. 39-48).
- Supplementary checks: `independent_review_checks_2026-11-13.py`. Run `python independent_review_checks_2026-11-13.py` with numpy installed. It reads the existing Table 3 literal without executing the original audit or overwriting results. Its inputs were compared with source Table 3.
- Relevant equations and figures were inspected in rendered source pages, including Unspace pp. 33, 36 and 44 and Glenn p. 5. No CAD/FEA or solver calculations were performed.
- The current Zenodo deposit could not be independently retrieved during this review. The original assessment's claim about missing TDMS data is therefore not newly verified here.

## Unspace: corrections to the assessment

### 1. The stated crossover speed is wrong

Assessment p. 3, Figure 1 caption repeats the source paper's erroneous claim that the rotational displacement exceeds the static displacement near 1,100 rad/s.

At 1,089.09 rad/s, source Table 3 gives rotational magnitudes 0.00062 and 0.00120 rad, versus static magnitude 0.00489 rad. The rotation signal is smaller by factors of approximately 8 and 4.

Using the paper's simplified fit and mean static deflection gives

`sqrt(0.00597733 / 1.35e-9) = 2104.2 rad/s`.

Comparing each measured pair with its own static value, the pair mean is still slightly smaller at 2,474 rad/s and clearly larger at 2,751.51 rad/s. Thus the precise crossing depends on which comparison is intended; 1,100 rad/s is unsupported in either case. The assessment's own graph visually contradicts its caption.

### 2. The abstract is more qualified than Opus says

Assessment section 4.8 says an abstract-only reader would receive the opposite of the body's conclusion. The source abstract explicitly describes atmospheric limitations, possible fluid artifacts, the need for vacuum testing, and conditional astrophysical implications. There is still strong tension between cautious language and categorical passages elsewhere, especially Appendix A.1. But it is unfair to imply that the abstract conceals the need to eliminate artifacts.

### 3. The artifact estimates are plausibility checks

The 4.1 mm/s Stokes estimate gives a test-sphere Reynolds number of approximately 4.5, outside the creeping-flow limit required for exact Stokes drag. It establishes a small force scale, not a calibrated airflow threshold.

The 10 mK convection estimate is obtained by inverting an inviscid buoyancy speed scale. With the calculation's assumed 5 cm length, the Rayleigh number is about 128. Viscosity, heat diffusion, cavity geometry and the orientation of heating matter. This is not a demonstrated cavity-flow solution. It does not prove that a 10 mK gradient produces the measured torque.

Similarly, a fitted exponent near two cannot quantitatively favor pressure over heating without a thermal transport model: heat production, convective cooling and thermal-to-torque conversion can each depend on speed. The formal regression uncertainty is not an uncertainty budget for the physical mechanism.

Pressure changes, helium and an aluminium rotor are useful controls, but gas viscosity, heat transfer, motor loading, elastic properties and magnetic properties need monitoring. Neither an aluminium rotor nor a reduced-pressure run alone necessarily settles the origin of a residual signal.

### 4. Some numerical precision should be reduced

The density criticism is valid, but the assessment then uses the questionable 7,800 kg/m3 density and a thin-disk deformation formula to label a sphere's deformation as 2.9 micrometres and its Newtonian deflection as 2.2e-7 rad. These should be explicitly identified as rough scaling estimates. The small GR rotational-energy scale is robust; a complete finite-source prediction at a separation of only about 1.7 source radii has not been performed.

The far-sphere correction is useful but does not establish a validated 5% G measurement. Source shafts/supports, pendulum arm and mirror inertia, gravitational stiffness, positioning errors and correlated drift still require a complete uncertainty model. Midpoint symmetry supports the inference that the reference zero was computed, but does not by itself prove the undocumented processing procedure or statistical independence of all 15 pairs.

## Unspace: substantive omissions

### 5. Equation (88) does not give the GR force on a slow stationary test mass

Source p. 33 sets the gravitational acceleration proportional to `c^2 partial_r h_rr`. For a stationary weak field and a slowly moving test body, the leading acceleration is determined by `Gamma^i_00`, hence the gradient of `h_00`; with this paper's +--- convention and `g_00 = 1 + 2 Phi/c^2`, it is `a^i = -(c^2/2) partial_i h_00` to leading order.

A derivative of `h_rr` cannot simply replace it. The stress contribution must be included through a consistent metric solution, trace reversal, conservation and source/support model. Constraining the test mass with a torsion spring does not change which metric component provides the leading gravitational force.

Thus Opus's arithmetic substitution into equation (89) is a reproduction of the authors' formula, not validation of that formula as a GR prediction. The independent rotational-energy estimate remains useful as an order-of-magnitude comparison. See [Carroll's GR notes, Newtonian limit and weak-field sections](https://arxiv.org/abs/gr-qc/9712019).

### 6. The kernel changes form and dimensions

Source equation (68) uses a two-dimensional logarithmic Green function. Equations (92)-(95), visibly printed on p. 36, instead use an inverse-distance kernel, `1/(2 pi |r-r'|)`. Equations (97) and (107) then return to a logarithm.

These are different kernels, not algebraic rearrangements. With stress in Pa and `dV` in m3, equation (95)'s printed inverse-distance expression has units J/m, despite being labelled J. The logarithmic expression can have energy units after supplying a reference length inside the logarithm. Moreover, a thin finite disk in three-dimensional space does not automatically produce a two-dimensional logarithmic gravitational field.

Opus correctly finds the logarithmic calculation depends on an unspecified length scale. The refined criticism is that a log Green function needs `ln(distance/L0)` and boundary conditions. Changing units while retaining the same physical `L0` does not change the physics. An additive potential constant normally disappears from a force; it becomes consequential here because the paper matches the absolute integral to stored spring energy. The sign of a potential by itself is not evidence against gravity.

The further restriction of the geometrical source angle to `omega R/c` in equations (90)-(92) is also unproved. Slow source motion does not restrict all contributing source material to a narrow angular wedge facing the detector.

### 7. Appendix A confuses detector energy with gravitational potential and produces a complex metric

Equation (A2) equates `-U_rest/m`, with `U_rest = k theta_rest^2/2`, to `-GM/r`. These are different quantities. The first is elastic energy stored by a particular instrument divided by test mass; the second is gravitational potential relative to a chosen reference.

Using the paper's parameters:

- Elastic energy: `5.64e-13 J`.
- `GMm/r` for one nearby source: `9.28e-11 J`.
- Ratio: approximately 165.

This comparison uses exactly the quantities equated in (A2); adding the other source does not repair the identification.

Equations (A4)-(A6) contain `sqrt(E_s / (m Phi_rest))`. With the paper's tabulated positive `E_s` and its explicitly negative `Phi_rest`, the argument is negative. At the 2,085 rad/s example it is approximately `-0.00528` if the listed two-source energy is inserted. An alternative factor-of-two convention changes the magnitude, not the sign. The resulting `g_tt` is complex. Using the negative value of Opus's logarithmic integral would contradict the positive energy used to obtain the published match and still would not fix (A2).

The proposed metric also contains the test mass `m` and the test-radius slice `Z = Rp`; no derivation removes this detector dependence in the test-body limit. It therefore has not established a universal source metric.

### 8. Energy matching is not a force law

Even a normalized, dimensionally consistent source integral must predict a torque through an interaction energy and its angular derivative, or through an equation of motion. Equating a source-energy number with the ribbon's stored energy is insufficient.

For a prescribed external torque, `theta = tau/k` and the spring energy is `tau^2/(2k)`. It depends on the instrument stiffness. A source-only energy integral cannot generally equal that stored energy for arbitrary choices of `k`. Varying stiffness, while accounting for the resulting position change, is a useful test of this energy ansatz; it does not itself discriminate gravitational from other external forces.

Equation (9) also equates `k delta_theta^2/2` to the final torque times `delta_theta`. With the paper's own equilibrium law, the latter is `k delta_theta^2`, twice the former. The actual change in ribbon energy from a preloaded rest position includes `k theta_rest delta_theta` as well as `k delta_theta^2/2`. A shifted effective potential can legitimately remove a constant preload term, but that definition and its energy balance must be explicit.

### 9. The flyby claim lacks the required energy-transfer mechanism

Appendix A.1 claims an explanation of non-conservative asymptotic spacecraft speed changes. A stationary axisymmetric gravitational potential, even if anisotropic, conserves orbital energy. A source-frame trajectory entering and leaving the same asymptotic potential cannot acquire a different asymptotic speed solely from that static field.

Time dependence or another energy-transfer mechanism would be required. This is a structural problem with the proposed explanation, independent of disputed flyby data. The conserved quantity for a stationary metric follows from its timelike Killing symmetry; see [Carroll, section 5](https://arxiv.org/abs/gr-qc/9712019).

### 10. Additional apparatus/data checks worth adding

- **Optical readout control:** use a fixed reference mirror through the same optical environment and an independent displacement measurement. External hot gas, window distortion or readout motion must be distinguished from actual pendulum rotation.
- **Equilibrium extraction:** Table 5's damping coefficient and Table 2's inertia imply an amplitude decay time `2I/b` of 3.16 hours. After three hours the linear model retains about 39% of the initial free-oscillation amplitude. The paper describes fitted/back-traced equilibrium estimates, so this is not proof those estimates fail; it makes their algorithm, residuals and drift treatment essential.
- **Clearance unit error:** source p. 11 calls 0.00325 a displacement in radians, but equation (3) subtracts 0.00325 metres. On a 5 cm arm, 0.00325 rad is 0.0001625 m, giving 0.0091975 m rather than 0.00611 m under those stated definitions.
- **Regression:** a zero-intercept quadratic should be refitted after dropping the other terms. Table 3 gives approximately `1.2701e-9 s2`, not the retained `1.35e-9 s2`. This is a modest correction and cannot explain the enormous physics gap.

## Glenn: corrections to the assessment

### 11. Wavelength independence permits refraction; it does not identify it

Opus correctly rejects the claimed 1.22 refractive-index ratio. The relevant air refractivity ratio for density changes at 532 and 650 nm is about 1.00682, consistent with the small dispersion described by [NIST](https://emtoolbox.nist.gov/wavelength/documentation.asp).

However, the assessment's description of equality as the refractive signature is too strong. The same optical-path change caused by mirror motion also yields approximately equal nanometre values. The correct conclusion is that this two-colour result does not distinguish those causes. Air's **refractivity** `(n-1)`, not its full index `n`, differs by approximately 0.7%.

### 12. Near zone, ringing and range do not provide the exclusions claimed

- Being deep in the near zone means a simple far-zone propagating-wave interpretation is inappropriate. It does not mean there is literally no gravitational field or possible gravitational response there.
- `2GE/(c^4 r)` is a characteristic metric scale for the stipulated localized energy, not a computed strain response of this mounted interferometer. A radiation prediction needs a conserved source, its changing quadrupole, and a detector response. The conclusion that ordinary GR is extraordinarily weak remains sound; an exact 35-order detector discrepancy is not established by that calculation alone.
- A gravitational drive can excite mechanical ringing. Resonant-bar gravitational-wave detectors explicitly exploit mechanical response; see [Whelan's detector-response paper](https://arxiv.org/abs/gr-qc/0509109). Ringing strongly motivates mechanical controls, but does not identify the forcing mechanism by itself.
- A signal reported as absent beyond 20 mm can be below the detection threshold. Without uncertainties and upper limits, this does not establish a physical cutoff or disprove an inverse-square law. The plotted distance data also do not themselves establish a reliable inverse-square fit.

The claimed 0.17-0.23 s behavior is measured with 30 fps video. Opus's microsecond/millisecond source times are illustrative assumptions, not resolved electrical waveforms from this paper.

### 13. The heat and helium stories remain conditional

The thermal energy budget makes refraction plausible but does not reproduce the observed spatial and temporal response. The interpretation of a stronger signal in helium is especially underdetermined: the paper does not provide enough detail about enclosure, purity, flow, deposited energy and pressure to establish whether helium-air mixing occurred. It is a possible confound, not a measured explanation. A well-controlled pure-helium comparison would be informative, although it still would not alone establish gravity.

The warming estimates also need a double-pass convention. If 150 nm is round-trip OPL change and a physical 5 mm gas region is crossed twice, the linearized temperature estimate is about 16 K, not 32 K; for a 20 mm physical region it is about 4 K, not 8 K. Opus's values are valid if its lengths mean total traversed optical length. This ambiguity strengthens the need for explicit calibration, without undermining plausibility.

### 14. The proposed controls are useful, not decisive individually

A sealed tube can retain internal thermal gradients; windows transmit vibration and can change optical path with temperature or stress. Glass does not exclude all heat, acoustic coupling or electromagnetic pickup. A surviving signal does not automatically become gravitational. Altering the spark enclosure can also alter the discharge energy and waveform.

The promise to settle the question in an afternoon should be replaced by a staged control program. Likewise, common-path Michelson variants exist: the terminology is not inherently contradictory, though Glenn's illustrated separated-arm layout is inadequately described. See the original [common-path Michelson-type design](https://opg.optica.org/ao/abstract.cfm?uri=ao-42-34-6953).

## Glenn: substantive omissions

### 15. The gravitational-wave source and optical observable are not defined sufficiently

A rapidly changing scalar energy density does not by itself specify gravitational radiation. The relevant source is the conserved stress-energy distribution of the full system, including the electrical supply, electrodes and plasma; a changing quadrupole and its projection onto the detector must be calculated. A spherically symmetric redistribution does not radiate quadrupolar gravitational waves. Opus mentions a quadrupole scale but does not develop this central failure of the paper's `du/dt` argument.

The measured quantity should be a differential optical phase, with `Delta phi = 2 pi Delta(OPL)/lambda`. For a conventional Michelson, a mirror displacement contributes twice that displacement to OPL. The common path from recombination to the screen does not simply supply extra differential sensing length. Glenn's `L = 725 mm` therefore needs justification from the actual geometry and response, rather than being accepted as the gravitational-wave strain denominator.

The image-analysis pipeline should distinguish phase translation from beam steering, changing fringe shape, spark-light contamination, threshold bias and camera exposure changes. Recommended controls include saved unthresholded frames with fixed exposure, a calibrated phase step, a dummy optical flash, and an electrical dummy discharge that reproduces pickup without a nearby plasma. These are candidate artifacts to test, not established causes.

### 16. Spark energetics and Alcubierre units need correction

The general deposited electrical energy is `E = integral V(t) I(t) dt`; `V(t) I(t) tau` requires a specified pulse shape or averaged power. Energy delivered through a circuit is also not necessarily the instantaneous energy retained within the chosen plasma cylinder. The paper does not provide the electrical waveform measurements needed to independently validate its energy-density inference.

In the Alcubierre expression written with a `c^4/G` prefactor, speed must be normalized as `v/c`. Glenn defines the substituted speed in nm/s without showing that normalization. If used literally, the formula is dimensionally inconsistent: it needs `(v/c)^2`, or a corresponding `c^2/G` prefactor for a speed in m/s. This is separate from the factor-of-four algebra error Opus correctly identifies. The underlying mistake of identifying a fringe-motion rate with a warp-bubble velocity remains. [Alcubierre's original paper](https://arxiv.org/abs/gr-qc/0009013) specifies its unit convention and metric construction.

## Suggested disposition

Retain the conclusion that neither paper supplies convincing evidence of new gravitation. Revise the assessments to distinguish numerical reproduction, physical prediction, plausible artifact budgets and demonstrated explanations. Add the Unspace metric, kernel and force-law failures before expanding laboratory speculation. For any further experimental work, prioritize calibrated readout, recorded source waveforms, randomized repeated controls and quantitative transfer functions.

Implementation complete: corrected both digests, rebuilt both PDFs from that same text, and visually inspected all 11 revised pages. The previous assessment PDFs were overwritten, with no backup editions. Reproduction commands and validation are recorded in README.md.
