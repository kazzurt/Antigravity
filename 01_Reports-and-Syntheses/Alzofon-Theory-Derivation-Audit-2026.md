# Alzofon's Theory of Gravity — Derivation Audit

**Date:** 2026-11-09
**Purpose:** reconstruct what Frederick Alzofon's theory actually states, separate algebra from postulate, and determine what, if anything, it predicts for a dynamic-nuclear-polarization weighing experiment such as Falcon Space's.
**Companion:** this audit covers the theory. The standard-physics spin analysis, evidence review, and experimental hypothesis ladder are in the [intrinsic-spin report](Intrinsic-Spin-Alzofon-and-Gravitational-Current-Research-Report-2026.md), which this document extends and in two places corrects (§6.1).
**Calculations:** [`alzofon_theory_audit_checks.py`](../02_Gravitation-Theory/Alzofon-Theory-Audit/alzofon_theory_audit_checks.py); every number below is produced and asserted there.

## Scope limit — read this first

The 1981 AIAA paper (AIAA-81-1608), the two *Physics Essays* papers (1993, 2001), and the 2016/2018 books were **not read**. The AIAA record is behind a publisher bot check and no open copy from a legitimate host was found. The audit therefore rests on:

| Source | Read | What it supplies |
|---|---|---|
| Alzofon, *A "New and Simple Idea", Dark Matter-Energy and the Crisis in Physical Theory*, viXra:1007.0008 (2010), 20 pp. | Full text | Alzofon's own last statement of the formalism (eqs. 1–11) and gravity model (§7). He states it uses the same formalism as the 1981 and *Physics Essays* papers |
| Stark, Grafe, Tajmar, *Measurement* 237, 115075 (2024); arXiv:2402.15529 | Full text | Summary of the 1981 paper and book: the Compton-wavelength mechanism and the order-to-disorder bridge; the 1994 parameters |
| Prutchi, diyPhysics Technical Note 2019-1 | Full text | 1994 run-by-run reconstruction from the 2018 book; the magnet-off control |
| Ionescu, *JHEPGC* 7, 1182 (2021) and viXra:2106.0056 (with Hathaway) | Full text | The "Alzofon–Ionescu" reinterpretation; Hathaway's description of the AGNUE mechanism and apparatus |
| Sokol, Chester, Perrone, Falcon Space poster (2024) | Full text and figures | Falcon's stated theoretical basis, block diagram, and the weight-versus-field trace |

Findings about the 2010 formalism are direct. Findings about the 1981 derivation are second-hand and marked as such. §8 lists what the 1981 paper must be checked for when a copy is in hand.

## Verdict

1. **There is no theory of the effect to test.** No document read contains an equation, coupling, or Lagrangian term that connects nuclear spin order, or its relaxation, to weight. Alzofon's own 2010 paper does not mention nuclear orientation at all. The bridge exists only as a verbal analogy to adiabatic demagnetization.
2. **The formalism that does exist does not generate mass or gravity.** It is a flat eight-dimensional interval with two time-like directions. Its mass relation is an algebraic identity that holds for any motion, with the mass inserted by hand (§2).
3. **The gravity model is a verbal argument that fails three independent checks:** it has no parameter that can produce `G m_p²/ħc = 5.9 × 10⁻³⁹`, its mechanism is short-range by construction, and under its natural reading the interaction energy has the wrong sign for attraction (§3).
4. **Taken at its word, the bridge predicts an effect at least six orders of magnitude below the claim.** If spin-disorder energy is drawn from the sample–Earth gravitational energy, the fractional weight change is `2.2 × 10⁻⁹` at complete polarization and `3.7 × 10⁻¹²` at the room-temperature DNP ceiling. The 1994 claim is `2.2 × 10⁻³` (§4).
5. **Three mutually incompatible theories travel under one name** (Alzofon, Ionescu, Falcon/Chester). None supplies a magnitude, sign, time course, or scaling law (§5).
6. **Falcon's published trace is inconsistent with the claim's own scaling.** It is bipolar where a polarization law gives a one-signed dip, and about `10⁴` times larger than a relaxation-rate law calibrated on Alzofon's 1994 number allows (§6).

**Status:** Alzofon's gravity model `constrained`; the spin–weight bridge `unresolved` only in the sense that no stated law exists to exclude; evidence rating **D**. Judgment, not derivation: probability that the theory as formulated is a viable account of gravity, under 0.1%; probability that a milligram-scale DNP weight effect is real, under 0.1%.

## 1. The three claims being bundled

The name "Alzofon theory" covers three separate propositions with separate burdens:

- **(I) Inertial mass** arises from a fluctuating internal motion of a unified matter–radiation field.
- **(II) Gravity** is the mutual contraction of overlapping particle fields, not spacetime curvature.
- **(III) Control:** ordering nuclear spins and letting them relax temporarily reduces weight.

(III) does not follow from (I) and (II) in any document read. An experiment on (III) is not a test of (I) or (II).

## 2. The formalism (Alzofon 2010, eqs. 1–11)

### 2.1 Reconstruction

Each light-signal arrival is given a random offset `(x₀, y₀, z₀, t₀)` with zero mean. Substituting into the Minkowski interval and averaging gives

\[
\langle S^2\rangle = r^2 - c^2t^2 + \langle r_0^2\rangle - c^2\langle t_0^2\rangle. \tag{A2}
\]

The paper then replaces the metric by

\[
S^2 = r^2 - c^2t^2 + r_0^2 - c^2t_0^2, \qquad
dS^2 = dr^2 - c^2dt^2 + dr_0^2 - c^2dt_0^2, \tag{A3, A6}
\]

and separately asserts invariance of

\[
S^2 = X^2+Y^2+Z^2-c^2T^2, \qquad X = x-x_0,\ \ldots,\ T=t-t_0. \tag{A5}
\]

Momenta and energies are defined with the ordinary proper time `dτ² = dt² − dr²/c²`:

\[
\mathbf p = m\frac{d\mathbf r}{d\tau},\quad
\mathbf p_0 = m\frac{d\mathbf r_0}{d\tau},\quad
E = mc^2\frac{dt}{d\tau},\quad
E_0 = mc^2\frac{dt_0}{d\tau}. \tag{A7, A8}
\]

Imposing `dS = 0` yields

\[
p^2 + p_0^2 = (E/c)^2 + (E_0/c)^2, \tag{A9}
\]

and, for `dr = 0`,

\[
E = mc^2, \qquad p_0^2 - (E_0/c)^2 = (mc)^2. \tag{A10, A11}
\]

`m` is then interpreted as rest mass generated by the fluctuating motion.

### 2.2 Findings

| # | Finding | Kind |
|---|---|---|
| F1 | **(A3) is postulated, not derived.** The averages in (A2) are constants. They shift `S²` by a number and leave every interval between events, and the differential form, exactly Minkowskian. Turning four random offsets into four new coordinates is a new assumption. The result is a flat space of signature `(+,+,+,−,+,+,+,−)`: six space-like and two time-like directions | Algebra |
| F2 | **(A3) and (A5) are different quadratic forms.** (A5) contains the cross term `−2 r·r₀ + 2c²tt₀`, which (A3) drops. They agree only on average (checked numerically). The paper uses them interchangeably | Algebra |
| F3 | **The mass relation is an identity.** From (A7)–(A8) alone, `(E/c)² − p² ≡ (mc)²` for any motion, because `dτ` was defined that way. With `dS = 0`, (A11) then holds for *every* state of motion, not only `dr = 0` (checked over 10⁴ random cases, residual `< 10⁻¹³`). (A10) and (A11) therefore carry no dynamical content; `m` is a free input | Algebra |
| F4 | **The hidden displacement is always space-like.** (A11) requires `|dr₀| > c|dt₀|`. The "internal motion" said to generate mass is tachyonic in the theory's own variables. The paper does not remark on this | Algebra |
| F5 | **No dynamics are given.** No distribution for the offsets (deferred to the unread references), no field equation, no action, no interaction term, no source. Planck's constant is absent from the formalism and enters only when a particle size `h/mc` is assigned by hand in §7 | Scope |
| F6 | **Structural reading.** Null motion in a flat higher-dimensional space, with rest mass equal to the invariant norm of momentum in the hidden block, is the algebraic device familiar from Kaluza–Klein-type mass generation. Here the hidden block carries a second time-like direction, which in a field theory ordinarily signals negative-norm or tachyonic modes | `project-inference` |

A possible arithmetic slip in the dark-energy section (the ratio `p₀c/E₀` for `E₀ = 2mc²` is `√5/2`, where the text appears to quote `√5`) is not scored, because the text extraction lost symbols.

**Result for claim (I):** not established. The formalism restates the special-relativistic mass shell in eight coordinates.

## 3. The gravity model (Alzofon 2010, §7; 1981 version via Stark et al.)

### 3.1 The argument as given

| Step | Statement | Status |
|---|---|---|
| G1 | A particle is a bound field state with most of its mass inside a sphere of diameter `h/mc` | Assumption; `h` inserted by hand |
| G2 | A second particle nearby raises the first particle's inertial mass to `m + δm` | No expression for `δm` as a function of the second mass or the separation |
| G3 | By Le Chatelier's principle the equilibrium diameter shrinks to `h/(m+δm)c`, mass-energy flows inward, and the second particle is drawn in | Heuristic. Le Chatelier describes the direction of an equilibrium shift; it is not a force law |
| G4 | The theory's equations of motion for a static point source give a potential proportional to `1/r` | Not shown in this paper. A `1/r` static potential is generic to any massless field |
| G5 | It is a "plausible assumption" that the resulting force, beyond a Compton wavelength, is Newtonian gravity | Identification, not derivation |

Stark et al. describe the 1981 and book versions in the same terms: overlapping energy distributions, a shared-mass increase, a compressed Compton wavelength, and a resulting attraction. No force law is reported there either.

### 3.2 Checks

**Strength.** The mechanism's only scales are `h`, `c`, and the particle masses. Any force built from them has a dimensionless coupling of order one. Newtonian gravity between two protons needs

\[
\frac{G m_p^2}{\hbar c} = 5.9\times10^{-39}.
\]

Nothing in G1–G5 supplies 38 orders of magnitude. Either `G` is inserted by hand, in which case nothing is explained, or the natural strength is wrong by that factor.

**Range.** The overlap of two distributions confined within `h/mc` vanishes beyond that distance: `1.3 fm` for a proton, `2.4 pm` for an electron. The long-range `1/r` behaviour comes from G4, which is a separate statement about a massless static field and is not connected to the overlap mechanism. The mechanism and the force law are two different things joined by assertion.

**Sign** (`project-inference`, under the natural reading). If bringing a second particle near *raises* the pair's total mass-energy, the interaction energy `U(r) = δm c²` grows as `r` falls, which is a repulsive force. Real gravitational binding *lowers* it: `δm = −Gmm′/(rc²)`. If instead mass is only transferred between the two with the total unchanged, there is no potential energy and no conservative force. Neither reading yields attraction.

**Universality and the classic tests.** The mechanism is defined for subatomic particles at rest. It says nothing about binding energy, kinetic energy, or light. The metric (A3) is flat, so the formalism contains no gravitational redshift, light deflection, or perihelion advance. The paper relies instead on external claims (Schiff 1960; Buenker 2008) that special relativity alone reproduces all three. Schiff's light-deflection argument is contested in the literature (Rindler, *Am. J. Phys.* 36, 540 (1968); citation verified, text not read). None of the three results is derived within the theory.

**Composition dependence** (conditional). Any version in which the source is a count or orientation of nucleons, rather than total stress-energy, predicts a free-fall difference between materials of order the difference in mass per nucleon: `2.4 × 10⁻³` for beryllium against titanium. The measured value is `(0.3 ± 1.8) × 10⁻¹³` (Schlamminger et al., *Phys. Rev. Lett.* 100, 041101 (2008)). That is an exclusion by ten orders of magnitude. Alzofon's text does not commit to this reading; Ionescu's (§5) effectively does.

**Result for claim (II):** `constrained`. A verbal mechanism with no force law, no source of `G`, and a sign problem.

## 4. The bridge from spin order to weight

### 4.1 Where it is stated

Not in the 2010 paper, which never mentions nuclear orientation. The bridge is available only second-hand:

- **Stark et al., summarising the 1981 paper and book:** an externally ordered system that relapses into disorder draws on, and thereby weakens, the gravitational interaction with its surroundings.
- **Hathaway, quoted in Ionescu 2021:** cyclic polarization is treated as akin to adiabatic demagnetization. When aligned spins de-align in an adiabatic environment, the only available energy is said to come from the local gravitational field, which is temporarily depleted, with a slight hysteresis so that repeated cycles accumulate. The text allows a decrease *or increase* in weight.

No equation accompanies either statement.

### 4.2 Taking the energy statement at its word

For ²⁷Al (`I = 5/2`, `γ/2π = 11.103 MHz/T`) at Alzofon's `0.33 T` and `300 K`:

| Quantity | Value |
|---|---:|
| Zeeman level spacing | `1.5 × 10⁻⁸ eV` |
| Thermal nuclear polarization | `6.8 × 10⁻⁷` |
| Electron polarization | `7.4 × 10⁻⁴` |
| Maximum DNP enhancement `γ_e/γ_n` | `2524` |
| Nuclear polarization at the DNP ceiling | `1.7 × 10⁻³` |
| Spin order energy at complete polarization | `1.35 × 10⁻⁴ J/g` |
| Sample–Earth gravitational energy `mgR_E` | `6.2 × 10⁴ J/g` |

If the spin order energy is taken from the gravitational energy, the fractional weight change is their ratio:

| Polarization | Predicted `Δw/w` | 1994 claim ÷ prediction |
|---|---:|---:|
| Complete (`P = 1`) | `2.2 × 10⁻⁹` | `1.0 × 10⁶` |
| DNP ceiling (`1.7 × 10⁻³`) | `3.7 × 10⁻¹²` | `5.9 × 10⁸` |
| Thermal, 300 K | `1.5 × 10⁻¹⁵` | — |

The 1994 claim is `1.1 mg` on about `0.5 g` of aluminium, a fraction `2.2 × 10⁻³`. The only quantitative reading the bridge permits therefore undershoots the claim by six to nine orders. For a `0.5 g` sample at the DNP ceiling the predicted change is about two picograms.

### 4.3 The premise fails for a room-temperature metal

- **The lattice is a vastly larger reservoir.** Thermal energy in aluminium at 300 K is roughly `270 J/g`, about `2 × 10⁶` times the spin order energy even at complete polarization. Nothing is adiabatic about a metal powder in epoxy at room temperature.
- **The relaxation channel is known and closed.** Nuclear spin–lattice relaxation in aluminium follows the Korringa law, `T₁T = 1.85 ± 0.05 s·K`, constant over three decades of temperature and due entirely to conduction electrons. At 300 K that gives `T₁ = 6.2 ms`. Alzofon's 6 ms pulse is this number. The relaxation he proposed to feed from gravity is fully accounted for by a measured electronic mechanism, leaving no residual channel at the percent level.
- **Standard mass-energy bookkeeping gives nothing.** Complete spin ordering changes the sample's rest energy by `1.5 × 10⁻¹⁸` of `mc²`. Even counting the entire spin entropy term `T·S = NkT ln 6` as if it were mass gives `1.8 × 10⁻¹²`.

### 4.4 The 1994 record contradicts the bridge's own timing

- Per Stark et al. and Prutchi, the recorded weight change appeared *during* microwave excitation and tracked microwave delivery. The bridge places the effect in the relaxation *after* the microwaves stop.
- Per Prutchi, the same trace appeared with the magnet current off, and vanished only when the microwaves were also off. Without the field there is no resonance and no orientation.
- `project-inference`: a laboratory force-compensation balance settles in roughly a second. It cannot mechanically resolve a 6 ms force step; a real step would appear attenuated and smeared over the settling time. A millisecond-resolved "weight" signal synchronous with a microwave pulse is the signature of electrical pickup in the readout. The balance model is not known to this audit, so this is an inference rather than a finding.

### 4.5 The static-orientation variant is already excluded

Ionescu's reading (§5) has oriented nuclei gravitate less, as a static property. Duan et al. dropped ⁸⁷Rb atoms prepared in `m_F = +1` and `m_F = −1` and found `η = (0.2 ± 1.2) × 10⁻⁷` (*Phys. Rev. Lett.* 117, 023001 (2016)). In those states the nuclear spin projection is `⟨I_z⟩ = ±1.25` out of a maximum 1.5, so the nuclei are about 83% oriented. A static effect of `2 × 10⁻³` at a polarization of `10⁻³`, scaled linearly to that orientation, is excluded by more than seven orders; with no scaling at all it is still excluded by four. The further spin–gravity limits in the intrinsic-spin report (§8.3) apply as well.

**Result for claim (III):** no stated law; the one quantitative reading available is `10⁶`–`10⁹` below the claim; the static variant is excluded.

## 5. Three theories under one name

| | Alzofon (1981–2010) | Ionescu (2021) | Falcon / Chester (2024 poster) |
|---|---|---|---|
| What gravity is | Mutual contraction of overlapping particle fields with fluctuating internal motion | Residual of a direction-dependent Coulomb law between quark charges, averaged over nucleon orientations | Not stated; mass attributed to gluon binding energy and zitterbewegung |
| Why spin order matters | Order relapsing to disorder draws on gravitational energy | Pumping nuclei into the upper of two nearly degenerate orientation states "cools" the gravitational potential, by analogy with a maser | Reducing nuclear entropy may reduce a component of apparent mass; torsion sourced by spin density |
| Equations for the effect | None | None. The paper asks physicists for help with the mechanism, states that the DNO mechanism is unclear to the author, and closes by saying the equations remain to be written | None |
| Magnitude, sign, time course | None | None | None |
| Errors of fact | §2–§3 above | Gives `S = kT` as Boltzmann's law; asks why the EPR frequency depends on field | Says minimal coupling of fermions to curved spacetime *requires* torsion; ordinary general relativity couples Dirac fields through the spin connection without it |
| Response to the magnet-off control | Attributes it to an unmeasured residual field and a wide bandwidth | Proposes that the sample and laboratory stay "correlated" after the field is removed, by analogy with a car that keeps running without its battery | Not addressed |

The three do not share a mechanism. Ionescu's is not a derivation of Alzofon's, and Falcon's is neither. Zitterbewegung and Einstein–Cartan torsion are real topics, but the poster's own text concedes the torsion effects are negligible at planetary scales, and nothing connects micro-electron-volt nuclear Zeeman energies to the mega-electron-volt scale of nuclear binding.

## 6. What this means for Falcon's experiment

### 6.1 Corrections to the intrinsic-spin report

- That report describes an "approximately 8 mg valley". The poster's plot shows a **bipolar** feature: from a baseline near `1.722 g` the reading rises to about `1.726–1.727 g` around `3.2–3.5 kG`, falls steeply through about `3.6–3.7 kG` to about `1.718 g` near `3.8–3.9 kG`, and recovers to about `1.721 g` by `4.3 kG`. The 8 mg is peak-to-trough; the excursion is roughly `+4.5 mg` and `−4 mg` about the baseline. Values are read from the figure.
- The cycles said to form the control (39–41, amplifier fault) are not in the per-cycle panel, whose axis ends at 38. The control is not shown.

### 6.2 The trace against the claim's own scaling

| Assumed law | Predicted shape in a slow field sweep | Predicted size at Falcon | Observed |
|---|---|---|---|
| Weight change ∝ polarization `P` | One-signed dip centred on resonance | Unspecified | Bipolar, with an apparent weight *gain* below resonance |
| Weight change ∝ `dP/dt`, calibrated on the 1994 number | Bipolar, antisymmetric about line centre | `≈ 0.3 μg`: the sweep crosses the feature in about 80 s against 6 ms, a rate ratio of `1.3 × 10⁴` | About 4 mg, `1.4 × 10⁴` times larger |
| Spin energy drawn from gravitational energy (§4.2) | — | `≈ 6 pg` at the DNP ceiling | About 4 mg |

No reading of the Alzofon claim gives both the shape and the size. The sweep-rate estimate assumes a one-way sweep and continuous microwaves; the poster does not state the modulation. The feature also appears in three of 38 plotted cycles, which argues against any steady mechanism, conventional or otherwise, and for an intermittent apparatus condition.

### 6.3 Conventional scales (order of magnitude)

- **Static magnetic force.** The sample holds `34 mg` of iron. Below saturation at the resonance field its moment is about `3.7 × 10⁻³ A·m²`, so a gradient of `1.1 G/cm` produces a force equal to the full 4 mg. Sokol's reported practice of seating the sample at a field "saddle point" shows the group knows this force is present.
- **Microwave force on a conducting sample.** With a 250 W amplifier, an assumed loaded `Q` of 1000 and an assumed 2 cm cavity height, the stored energy is about `4 × 10⁻⁶ J` and the gradient force on a `0.7 cm³` conducting sample is of order 6 mg. This scales with `Q` and delivered power and vanishes at a symmetric position, so it is a scale, not a prediction. A dispersive line shape is the natural form for a reactive force, or for any power-dependent force when the sample's resonance pulls the cavity off the source frequency.
- **Radiation pressure alone** is `0.09 mg` at 250 W and is negligible by comparison.

Three conventional channels sit at the milligram scale. The claim sits there too. The theory sits between six and nine orders below.

### 6.4 Discriminating tests

1. Move the sample above and below the magnet midplane: a magnetic force reverses, a weight change does not.
2. Iron-free aluminium sample, same geometry.
3. Vary microwave power: a stored-energy force is linear in power; record forward and reflected power and cavity lock alongside weight.
4. Detune the source by several linewidths at fixed field sweep.
5. Plot every cycle, including the fault cycles.

## 7. What a testable version would need

A statement of the form "weight change equals a stated coefficient times a stated function of `P`, `dP/dt`, nucleus, and temperature", with a sign and a conservation ledger. None exists. Until one does, an Alzofon-type experiment is an anomaly search, and the only operational template is the relaxation-rate fit (H2) already defined in the intrinsic-spin report. This audit adds a calibration for it: an H2 coefficient fixed by the 1994 claim predicts sub-microgram signals in any slow continuous-wave sweep.

## 8. Open items for the 1981 paper

When a copy is available, check:

1. whether any equation relates nuclear orientation, entropy, or relaxation rate to a force or potential, and what magnitude it gives for the 1994 parameters;
2. the statistical distribution assigned to the offsets, and whether a field equation or action appears;
3. how the static `1/r` potential is obtained and whether `G` is derived or inserted;
4. whether the 0.22% figure is a prediction or only a measurement;
5. whether the paper addresses the second time-like direction.

A positive answer to item 1 would reopen §4 and is the only item that could change the verdict on claim (III).

## Verification note

Primary texts were extracted with `pdftotext` and read in full; the Falcon poster was read as text and image. Citations added by this audit and checked against publisher or arXiv records on 2026-11-09: Duan et al. 2016 (value confirmed), Schlamminger et al. 2008 (value confirmed), the aluminium Korringa constant (`1.85 ± 0.05 s·K`, via arXiv:1207.3702 and arXiv:1504.06992 as reported by search), Rindler 1968 (citation confirmed; text not read). Stark et al.'s Table 6 polarization for ²⁷Al at 9 T and 5 K is reproduced by the check script. The AIAA record could not be opened.

### Sources

- F. E. Alzofon, [*A "New and Simple Idea", Dark Matter-Energy and the Crisis in Physical Theory*](https://vixra.org/abs/1007.0008), viXra:1007.0008 (2010).
- F. Alzofon, [*Anti-Gravity with Present Technology: Implementation and Theoretical Foundation*](https://doi.org/10.2514/6.1981-1608), AIAA-81-1608 (1981). **Not read.**
- W. Stark, H.-J. Grafe, M. Tajmar, [*Investigation of the Alzofon weight reduction experiment using NMR spectroscopy*](https://arxiv.org/abs/2402.15529), Measurement 237, 115075 (2024).
- D. Prutchi, [*An Unbiased Critique of Dr. Fredrick Alzofon's 1994 Experiments…*](https://www.diyphysics.com/wp-content/uploads/2019/07/Prutchi-Critique-of-Alzofon-Gravity-Control-Experiments.pdf), diyPhysics Technical Note 2019-1.
- L. M. Ionescu, [*What Gravity Is: Alzofon-Ionescu Theory…*](https://doi.org/10.4236/jhepgc.2021.73069), JHEPGC 7, 1182–1189 (2021); [*Alzofon-Ionescu Theory of Gravity*](https://vixra.org/abs/2106.0056), viXra:2106.0056 (2021).
- M. Sokol, D. Chester, M. Perrone, [*Investigating a Purported Connection Between DNO and Mass*](https://www.falconspace.org/wp-content/uploads/2024/12/Investigating-a-Purported-connection-between-DNO-and-Mass.pdf), Falcon Space poster (2024).
- T. Ventura, [*Mark Sokol: Anti-Gravity with Present Technology*](https://www.altsci.net/mark-sokol-anti-gravity-with-present-technology/), AltSci (2026-04-21). Secondary; read through a fetch agent.
- X.-C. Duan et al., [*Test of the Universality of Free Fall with Atoms in Different Spin Orientations*](https://arxiv.org/abs/1602.06377), Phys. Rev. Lett. 117, 023001 (2016).
- S. Schlamminger et al., [*Test of the Equivalence Principle Using a Rotating Torsion Balance*](https://arxiv.org/abs/0712.0607), Phys. Rev. Lett. 100, 041101 (2008).
- W. Rindler, *Counterexample to the Lenz–Schiff Argument*, Am. J. Phys. 36, 540 (1968). Citation only.
