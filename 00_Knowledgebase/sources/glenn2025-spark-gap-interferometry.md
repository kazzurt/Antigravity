# Glenn spark-gap interferometry

**Paper assessed:** Chance Michael Glenn, Experimental Spacetime Distortion: Generating Gravitational Waves in the Laboratory, European Journal of Engineering and Technology Research 10(2), 39-48 (2025). [G1]

> **Assessment: gravitational attribution unsupported.** Spark-correlated fringe changes are reported, but the two-wavelength argument does not exclude refraction, the optical observable is incompletely calibrated, and a gravitational source-to-detector prediction is absent. Thermal, mechanical, optical and electrical artifacts remain plausible. Their individual contributions have not been demonstrated.

### 1. Apparatus and reported observations

- **Spark source:** a transformer described as capable of about 400 kV, pointed tungsten electrodes and nominal gaps of 2.5 or 5 mm. The energy model uses a cylinder of radius 0.25 mm and length 2.5 mm; Figure 1 instead says 3.5 mm. Repetition rates reach roughly 5 Hz.
- **Interferometer:** 532 and 650 nm lasers, mirrors about 150 mm from the splitter, a screen about 500 mm away, and quoted L = 725 mm. The spark sits near one arm. The phrase common-path Michelson requires clarification against the depicted separated-arm layout; it is not intrinsically contradictory because modified common-path Michelson designs exist. [G5]
- **Readout:** 30 fps video of fringes, with image rotation, thresholding, vertical summation and smoothing. Peak shifts between spark-on and baseline images are converted into nanometres using fringe spacing.
- **Results:** peak shifts about 140-160 nm; response over roughly 0.17-0.23 s with ringing; similar reported magnitudes at two wavelengths and two spark orientations; decreasing response with distance, described as absent beyond about 20 mm.
- **Additional claims:** response increases with input power and repetition rate, appears additive for sparks in series and is stronger in helium. The paper interprets this as spacetime distortion and proposes phased arrays, propulsion, fusion and biological applications.

### 2. What is and is not established

The plots document a reported spark-correlated optical response. They do not provide an uncertainty budget, a numerical measurement table, reusable raw records, randomized blind tests or a calibrated exclusion of competing pathways. The gravitational interpretation is unsupported; the supplied data also do not uniquely establish a thermal or mechanical cause.

Published 25 April 2025; author affiliations: Morningbird Space Corporation and Alabama A&amp;M University. Funding is identified as NSF SBIR Phase I. The local PDF metadata names an unrelated article, apparently a production error; this is not itself a physics objection.

<!-- page -->

## 3. Optical-path and thermal checks

### 3.1 The two-colour control does not discriminate

The paper expects a refractive displacement ratio of 1.22. That is 650/532, a wavelength ratio, not the refractivity ratio relevant to an air-density change. Standard-air (n-1) is approximately 2.782×10<super>-4</super> at 532 nm and 2.763×10<super>-4</super> at 650 nm. Their ratio is 1.00682. [G2]

<!-- figure: glenn -->

**Figure 1.** Approximate equality of nanometre OPL changes permits both air-density changes and geometric path changes. The reported peak ratio has no supplied uncertainty; this is a conceptual comparison, not a statistical fit.

For a fixed optical-path change, fringe count scales approximately as 1/λ. After conversion back into OPL nanometres, nearly equal values do not identify refraction, mirror motion or gravity. Air's **refractivity (n-1)** differs by about 0.7%; its full index n does not differ by 0.7%.

### 3.2 A conditional thermal budget

| Assumed gas path for a 150 nm OPL change | Required magnitude of Δn | Linearized temperature change at 295 K |
| --- | --- | --- |
| 5 mm total traversed optical length | 3.0×10<super>-5</super> | About 32 K |
| 20 mm total traversed optical length | 7.5×10<super>-6</super> | About 8 K |
| 5 mm physical region, crossed twice | 1.5×10<super>-5</super> | About 16 K |
| 20 mm physical region, crossed twice | 3.75×10<super>-6</super> | About 4 K |

These estimates assume a uniform, approximately isobaric ideal-gas density change, with magnitudes related by Δn ≈ (n-1)ΔT/T. Modest heating can matter, but this does not solve the actual plume, shock, beam trajectory or detector response. The double-pass convention must be stated before comparing numbers.

The paper's lower energy-density range and cylinder dimensions imply about 0.7-1.2 J. Assigning half of 1.2 J to air in a 5 mm-radius sphere gives an order-900 K heat-capacity budget. This simplified budget neglects expansion and loss and is not a measured or predicted local temperature. Heating lowers density and OPL at fixed pressure; the observed sign needs an independent phase calibration.

<!-- page -->

## 4. Measurement, source energy and alternative pathways

### 4.1 Calibrate differential phase, not screen position alone

**Δφ = (2π/λ) Δ(OPL); a Michelson mirror displacement Δx contributes 2Δx.**

The analysis must separate phase translation from beam steering, changing fringe shape, spark-light contamination, threshold bias and automatic camera exposure. Retain unthresholded frames, lock exposure and analysis settings, and verify the complete pipeline with known phase steps. These are candidates for testing, not identified causes of the published result.

L = 725 mm cannot simply be accepted as a gravitational-wave sensing length. The common route from recombination to the screen does not add an independent differential arm. Derive the response from the two-pass geometry, arm orientations, local perturbation and mechanical mounting. Dividing 160 nm by 725 mm gives 2.2×10<super>-7</super>, but that arithmetic does not establish a measured gravitational-wave strain.

### 4.2 Electrical energy is not specified by nominal voltage

**E<sub>deposited</sub> = ∫ V(t) I(t) dt; stored plasma energy need not equal delivered energy.**

The product V(t)I(t)τ requires a pulse-shape or average-power definition. A transformer's nominal maximum voltage does not establish voltage/current during breakdown. Electrical waveforms, timing, electrode losses and the changing plasma volume are needed to validate energy density. Differentiating a scalar energy-density estimate does not supply a gravitational-wave source model.

| Paper input, using radius 0.25 mm and length 2.5 mm | Implied energy per spark |
| --- | --- |
| Section 4: 1.4-2.4 GJ/m<super>3</super> | 0.69-1.18 J |
| Section 2: 10<super>11</super>-10<super>12</super> J/m<super>3</super> | 49-491 J |
| Upper range repeated at 5 Hz | Approximately 0.25-2.5 kW average input if fully delivered each pulse |

These ranges are inconsistent without further definitions. The alternative 3.5 mm caption length increases each volume-derived energy by 40%. These are arithmetic consequences of stated assumptions, not independent energy measurements.

### 4.3 Other exclusions remain incomplete

**Orientation and white light:** a distributed gas-density change can alter OPL without a visibly coloured interface or a strong change between two electrode orientations. The 0°/90° comparison is not an exhaustive refraction test.

**Helium:** its refractivity is lower than air's, but the paper does not sufficiently specify purity, enclosure, flow, pressure and deposited energy. Helium-air mixing could itself change OPL; it is not established that mixing occurred. A controlled pure-helium comparison would be informative. Higher response, additivity and power scaling alone do not select gravity over ordinary pathways.

<!-- page -->

## 5. Gravitational theory and interpretation limits

### 5.1 A changing energy density is not a radiation calculation

A prediction requires the conserved stress-energy distribution of the full system, including the supply, electrodes, electromagnetic field, plasma and surroundings. In the weak-field radiation limit, the changing quadrupole and detector projection matter. A spherically symmetric redistribution does not produce quadrupolar gravitational waves. A large du/dt alone establishes neither radiation amplitude nor optical phase. [G3]

For stipulated localized energy E ≈1.2 J at r =1 cm, 2GE/(c<super>4</super>r) ≈1.9×10<super>-42</super>. This is a characteristic metric scale, **not a computed strain response** of this mounted interferometer. It is about 35 orders below the paper's nominal ΔL/L number, showing the severe scale problem; an exact 35-order detector discrepancy has not been derived.

For illustrative source times of 1 µs and 1 ms, wavelengths cτ are approximately 300 m and 300 km. At centimetre range the beam is deep in the near zone, so a simple far-zone wave treatment is inappropriate. This does not mean gravity is absent. These electrical times are illustrative assumptions, not waveforms resolved by the 30 fps recording.

### 5.2 The Alcubierre substitution is not a spark model

- **Velocity:** the paper substitutes the rate of inferred fringe displacement, about 650-850 nm/s, for bubble velocity. These are different observables; no mapping from optical rate to metric motion is derived.
- **Units:** with a c<super>4</super>/G prefactor, speed must enter as v/c. If v in nm/s is inserted literally, the expression is dimensionally inconsistent; use (v/c)<super>2</super>, or the corresponding c<super>2</super>/G prefactor for SI velocity.
- **Algebra and geometry:** substituting the printed derivative into (9) yields c<super>4</super>/(8πG), not c<super>4</super>/(2πG) in (12). The transverse angular factor of the Alcubierre energy density is also omitted.
- **Energy and field equations:** the original metric requires negative energy density in its wall for the relevant observers, not the positive plasma energy invoked here. Matching a shaping function is not a solution of the field equations for the measured discharge. [G4]

### 5.3 Ringing, duration and range are not decisive

A 0.17-0.23 s response and ringing make thermal, acoustic and mechanical transfer functions important. They do not themselves identify the cause: a gravitational drive can excite a mechanical detector, as resonant-bar detectors illustrate. [G6] A source impulse can also produce a detector response longer than the impulse.

An effect described as absent beyond 20 mm may be below the detection threshold. Without uncertainties and upper limits, this is neither a demonstrated physical cutoff nor a rejection of an inverse-square dependence. The plotted curves do not establish a precise inverse-square law.

<!-- page -->

## 6. Controls, evidence rating and reproducibility

| Priority control | Purpose and conditions for interpretation |
| --- | --- |
| Known phase steps; raw fixed-exposure video; fast phase readout | Calibrate magnitude, sign and time response. Test extraction against beam steering, contrast changes and saturation. |
| Evacuated beam section; measured window/case temperatures | Reduce gas-path changes while monitoring window stress, heat transfer and mechanical motion. A surviving signal is not automatically gravitational. |
| Separate support; accelerometers; fixed optical reference | Measure acoustic/mechanical transfer into mirrors, windows, camera and beam. Ringing alone does not identify the forcing mechanism. |
| Electrical dummy discharge; optical flash without a nearby spark | Test EMI/electrostatic pickup and image contamination separately; characterize how well each control reproduces the relevant disturbance. |
| Pure-gas/pressure tests; heating mimic; enclosure changes | Record deposited energy, gas properties, source geometry and temperature. Enclosures alter the discharge and still transmit heat/vibration. |
| Randomized repeated distance, energy and orientation scans | Supply uncertainties, null upper limits and a prespecified analysis. Record synchronized voltage/current, phase and environmental channels. |

### Assessment and relevance

**Evidence rating: E for gravitational attribution** (internal project scale). The fringe response is worth recording, but the controls do not establish gravity and the theory does not predict the observable. This supplies neither a demonstrated propulsion mechanism nor a quantitative gravitational constraint. Its citation by Unspace is claim provenance, not independent confirmation. No project gate decision changes.

A tube, helium substitution or one null control cannot promise to settle the question immediately. A useful control program produces a calibrated residual with explicit limits on competing pathways. The exact cause of the currently reported fringe movement remains unresolved.

### Sources and reproducible checks

[G1] C. M. Glenn (2025), [doi:10.24018/ejeng.2025.10.2.3246](https://doi.org/10.24018/ejeng.2025.10.2.3246). Locators: §§2-5; equations (4)-(9), (12)-(17); Figures 5, 7-15. Canonical PDF remains in 03_Propulsion-and-Anomalies/.

[G2] NIST, [Refractive Index of Air documentation](https://emtoolbox.nist.gov/wavelength/documentation.asp). [G3] S. Carroll, [GR lecture notes](https://arxiv.org/abs/gr-qc/9712019), weak fields and gravitational radiation.

[G4] M. Alcubierre, [The warp drive: hyper-fast travel within general relativity](https://arxiv.org/abs/gr-qc/0009013) (1994).

[G5] Vakhtin et al., [Common-path interferometer for frequency-domain optical coherence tomography](https://doi.org/10.1364/AO.42.006953) (2003). [G6] J. T. Whelan, [Gravitational-wave measurements with bar detectors](https://arxiv.org/abs/gr-qc/0509109) (2005).

Calculation package: 02_Gravitation-Theory/Unspace-Glenn-Claim-Audit/. Run unspace_glenn_claim_checks.py, then build_assessment_pdfs.py; independent_review_checks_2026-11-13.py supplies additional checks. This digest is the editable PDF source. Thermal and GR numbers are conditional scales, not fitted artifact or detector-response models.
