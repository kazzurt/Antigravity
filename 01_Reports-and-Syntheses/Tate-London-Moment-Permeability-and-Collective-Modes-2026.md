# Tate, the London Moment, Gravitomagnetic Permeability, and Collective Modes

**Date:** 2026-07-15  
**Corrected:** 2026-07-16 — three factual corrections from the comprehensive review (Hoang documentation criticism was misattributed in §1.5; "31" → "30" orders in §1.4; the phonon-angular-momentum measurement is by H. Zhang et al., not "Parsonnet et al.", §§8–9). See `Project-Technical-and-Strategic-Review-2026.md` §11.  
**Purpose:** Follow up three questions raised by the Ning Li derivation audit:

1. Could Li's charge-canceling, mass-adding counterflow be related to the niobium Cooper-pair mass anomaly reported by Tate?
2. Has more recent literature developed Li's idea of a material gravitomagnetic permeability?
3. What real ionic, spin, or neutral collective fields could replace Li's unsupported assignment of the superconducting phase to lattice ions?

## Executive conclusion

The Tate result and Li's intuition overlap in a precise but limited way. A London-moment experiment measures the electromechanical response of a condensate **relative to a rotating ionic lattice**. It is therefore a legitimate probe of condensate–lattice entrainment or an omitted neutral collective mode. It is not a direct measurement of free Cooper-pair rest mass, ionic circulation, or a gravitational field.

Tate measured

\[
\frac{m_{\rm app}}{2m_e}=1.000084(21),
\]

while the then-used theoretical value was approximately `0.999992`. The often-quoted numbers describe two different comparisons:

- `+84 ppm` relative to `2m_e`;
- approximately `+92 ppm` relative to the theoretical prediction.

If the residual were represented as an unmodeled ionic inertial contribution, its size would be surprisingly small. A niobium atom has a mass of roughly `1.69 × 10^5 m_e`; an apparent pair-mass increase of `92 ppm` corresponds to only

\[
f_{\rm Nb}\sim
\frac{2m_e(92\times10^{-6})}{M_{\rm Nb}}
\approx 1.1\times10^{-9}
\]

of one niobium atom's inertia per Cooper pair. This is **only a parameterization**, not evidence that such a fraction of an ion actually co-moves. It shows, however, that a very weak condensate–lattice cross-response could be visible in a ppm-level London-moment measurement without requiring wholesale rotation of the lattice ions.

The more important theoretical result is that Li's counterflow idea has a sound modern replacement:

> A multicomponent coherent medium can possess a neutral hydrodynamic eigenmode for which electric charge current cancels while mass or angular-momentum current remains nonzero.

This is not merely hypothetical. Different portions of the statement are established in different systems:

- two-component superconducting/superfluid theories with oppositely charged mobile condensates support dissipationless neutral mass flow;
- exciton condensates support charge-neutral coherent flow and can convert charged superconducting current into neutral supercurrent at a designed interface;
- Carlson–Goldman modes produce out-of-phase normal and superfluid motion with little charge accumulation;
- Leggett modes are observed neutral relative-phase modes of multiband superconductors;
- axial/chiral phonons carry real ionic angular momentum, now measured mechanically;
- superconducting altermagnets are predicted to support charge-canceling persistent spin counterflow.

No known niobium state combines all required ingredients. The strongest next theory is therefore **not** “ordinary niobium ions inherit the Cooper-pair phase.” It is a two-field or multicomponent response theory in which an independently justified neutral mode couples to the condensate. The gravitational response must then be calculated from its complete stress-energy. A large scalar `μ_g` should be an output, if it exists, not an input.

## 1. What Tate actually measured

### 1.1 The observable

For a simply connected rotating superconductor, the London field is schematically

\[
\mathbf B_L=-\frac{2m_*}{q_*}\boldsymbol\Omega,
\]

up to sign conventions. Tate, Cabrera, Felch, and Anderson used flux quantization in a rotating niobium ring to determine the ratio `h/m_app`. Their `m_app` is the inertial coefficient appearing in the rotating superconducting constitutive relation after the experiment's electromagnetic, geometric, and solid-state corrections have been applied.

This is a powerful measurement, but “Cooper-pair mass” is shorthand. The inferred coefficient can absorb:

- the condensate's response relative to the lattice;
- electrostatic and chemical-potential terms;
- surface double layers and work-function physics;
- band and interaction corrections;
- geometry, penetration depth, trapped flux, and charging systematics;
- any genuinely new rotation–condensate or gravity–condensate term.

It is not a direct weighing of two isolated electrons.

### 1.2 The conventional condensate–lattice structure

Jiang and Liu's thermodynamic treatment makes the lattice role explicit. A rotating solid has a lattice velocity

\[
\mathbf v_n=\boldsymbol\Omega\times\mathbf r,
\]

and the superconducting free energy depends on a gauge-invariant combination involving the condensate velocity relative to that lattice. Their analysis argues that large microscopic relativistic corrections cancel against electrostatic and interaction terms, leaving the ordinary London expression accurate to approximately `10^-10` under their assumptions.

This is directly relevant to Li. It establishes that the London moment is already a **two-subsystem electromechanical problem** even in standard theory. What it does not establish is a mobile ionic superfluid, a charge-canceling ionic current, or a gravitational enhancement.

### 1.3 Does Tate coincide with Li?

**Structurally: yes.** Both questions live in the relation among rotation, condensate phase, lattice motion, and electromagnetic response. A hidden condensate–lattice entrainment coefficient could appear experimentally as an anomalous `m_app`.

**Dynamically: not yet.** Tate did not measure an ionic velocity, mass flow, mechanical angular momentum, or external gravitomagnetic field. The experiment therefore cannot identify the carrier of the residual.

**Quantitatively: Li's published mechanism does not follow.** Li's claimed gravitational gain depends on a nearly complete charge-current cancellation, a massive surviving ionic current, and an extremely small electromagnetic `μ_r`. A `92 ppm` London residual could instead arise from a tiny cross-response. Those are very different regimes.

### 1.4 The proposed gravitomagnetic interpretation

If a gravitomagnetic vector potential is added to the superconducting canonical momentum, then a gravitomagnetic field can mimic a change in the London coefficient. In the convention used by Tajmar and de Matos, explaining the Tate residual requires approximately

\[
B_g \simeq 2\Omega\frac{\Delta m}{m}
\simeq 1.84\times10^{-4}\Omega.
\]

The authors themselves state that their measured couplings are about `30` orders of magnitude larger than what general relativity predicts for the rotating ring (gr-qc/0603033). Tate can therefore be read as a **target residual** for a new coupling, but it is not evidence that the new coupling is gravitomagnetic. A gravitational interpretation must independently produce that coefficient and survive non-gravitational explanations.

### 1.5 Later measurement claim

Hoang and collaborators published a 2020 spherical-shell method and reported measurements on six type-I superconductors. Tajmar, Neunzig, and Kößling summarize its niobium result as an approximately `18 ppm` discrepancy with a claimed `2.1 ppm` uncertainty—smaller than Tate's residual, but statistically significant under the quoted error model.

This result should be treated as **important but not yet a secure independent replication**. The publication is paywalled with no preprint or accessible results table, so the six-material claim and the `18 ppm` niobium figure are known here only secondhand through Tajmar, Neunzig, and Kößling's 2022 summary. *(Correction 2026-07-16: an earlier version of this paragraph said Tajmar's review notes missing photographic documentation of Hoang's apparatus; in the verified text that criticism concerns Podkletnov, not Hoang. A 2020 corrigendum does exist (DOI `10.1016/j.matlet.2020.128597`); its stated change is the first author's affiliation, not the results. The full measurement and supplementary-data package still requires audit, and the abstract's "type-I superconductors" description requires checking against the actual materials and sample conditions. This scope correction was verified on 2026-09-04.)* The raw data, complete supplement, calibration history, and independent reproduction should be obtained before using the `18 ppm` number as a hard anchor.

The difference between `92 ppm` and `18 ppm` is itself informative: it argues against treating the effect as a universal extra rest mass. It favors a material-, geometry-, surface-, or response-dependent residual.

## 2. The attractive part of the permeability analogy

### 2.1 Why the analogy is appealing

In electromagnetic matter, a constitutive relation packages an enormous amount of microscopic physics into a response function. In a simple static isotropic limit,

\[
\mathbf B=\mu\mathbf H.
\]

It is natural to ask whether coherent matter has an analogous gravitomagnetic response. Li and Torr introduced gravitational permittivity and permeability parameters for exactly this reason. The intuition is productive: the field equations alone do not specify how a complicated quantum medium responds.

### 2.2 Where the literal analogy breaks

The gravitational constant appearing in weak-field gravitoelectromagnetic equations,

\[
\mu_{g,0}\sim\frac{4\pi G}{c^2},
\]

is fixed by the Einstein equations, subject to convention-dependent numerical factors. It is not automatically a vacuum constitutive coefficient that matter can renormalize in the same way that spin and orbital magnetization renormalize magnetic permeability.

A medium can certainly possess a gravitational **response**, but the clean object is generally a nonlocal kernel such as

\[
\delta T^{0i}(\omega,\mathbf k)
=\chi^{ij}_{TA}(\omega,\mathbf k)\,\delta A_{g,j}(\omega,\mathbf k),
\]

with the induced stress-energy then sourcing the metric through the gravitational Green function. The response depends on frequency, wavevector, geometry, boundary conditions, dissipation, and the chosen observable. Conservation and diffeomorphism invariance constrain it.

A scalar `μ_{g,r}` is at best a special low-frequency, long-wavelength projection of this kernel. Treating it as a universal material number hides the mechanism and makes it easy to double-count screening or confuse a convention-dependent field with an invariant observable.

### 2.3 What the newer literature says

The post-Li literature continues to investigate superconductor–gravity response, but it has **not** produced a generally accepted derivation or measurement of a large material `μ_{g,r}`.

- Ummarino and Gallerati's 2017–2025 program combines gravito-Maxwell notation with time-dependent Ginzburg–Landau theory. It predicts small, transient, material- and geometry-dependent alterations under transitions, vortices, or laser drive. These papers calculate effective response while retaining the ordinary weak-gravity coupling; they do not independently establish Li's `μ_{g,r} ~ 10^4`.
- Inan's 2022 derivation starts from linearized Einstein equations and London constitutive equations. It finds that a gravitomagnetic field alone is not exponentially expelled by a neutral superfluid; the characteristic spatial scale for niobium is of order `10^13 m`. It identifies sign errors in several earlier gravito-Meissner derivations. This weighs against treating superconductivity as an ordinary medium with a simple gravity-screening permeability.
- Inan, Thompson, and Chiao describe gravitational-wave response using a gravitational shear modulus and a tensor penetration problem. Their formulation explicitly models both condensate and ionic phonons and finds the lattice response larger than the Cooper-pair-density response. That is closer to a proper response-kernel treatment than to a single scalar permeability.
- Koizumi's 2021 Berry-connection theory addresses the free-electron mass appearing in the London moment by changing the superconducting many-body description. It is a non-gravitational alternative and is not established consensus, but it illustrates why the London residual must be solved at the electromechanical level before being assigned to gravity.
- Ummarino and Gallerati's 2024 laser-film paper and 2025 conference paper continue the same generalized-TDGL line. They provide theory predictions but no confirming gravitational measurement.

The useful conclusion is:

> Keep the permeability analogy as a prompt to search for anomalous response, but replace the scalar `μ_g` with an explicitly derived, frequency- and wavevector-dependent stress-energy response kernel.

## 3. Real candidates for the missing collective field

The following candidates are ranked by four requirements:

1. a distinct coherent degree of freedom;
2. real mass or angular momentum;
3. suppressed electrical signature or charge cancellation;
4. demonstrated coupling to a superconducting condensate.

| Candidate | What is established | What it supplies | What remains missing | Rank for a Li replacement |
|---|---|---|---|---:|
| Oppositely charged multicomponent condensates | Controlled theory; projected for liquid metallic hydrogen/deuterium | Exact neutral, mass-carrying superfluid eigenmode; altered rotational response | No accessible demonstrated material state; not ordinary niobium | 1 |
| Ionic axial/chiral phonons | Real ionic angular momentum predicted, transported, and mechanically measured | The missing physical ionic angular-momentum carrier | No demonstrated phase locking to an ordinary superconducting condensate; usually driven or symmetry-selected, not universal DC circulation | 2 |
| Carlson–Goldman mode | Observed historically; modern response theory | Charge-neutral out-of-phase motion of superfluid and normal components | Narrow near-`T_c` window, damping, primarily electronic quasiparticle counterflow rather than heavy-ion mass flow | 3 |
| Exciton condensate coupled to superconductors | Neutral coherent flow and theoretical charged-to-neutral supercurrent conversion | Concrete interface mechanism that converts charged supercurrent to neutral massive flow | Exciton mass is electronic-scale; not a bulk ionic mode; gravity coupling ordinary unless new law added | 4 |
| Entrainment / Andreev–Bashkin drag | Firm multicomponent hydrodynamic theory; active detection proposals | Correct cross-stiffness language for one coherent flow dragging another | Direct bulk observation remains difficult; ordinary niobium lacks two independent superfluids | 5 |
| Leggett relative-phase mode | Observed in MgB2 and other multiband devices | A neutral condensate degree of freedom that survives electromagnetic gapping | Relative phase does not generically carry net mass or angular momentum; niobium-specific mode not established | 6 |
| Superconducting spin counterflow | Recent theory predicts persistent pure spin supercurrent in superconducting altermagnets | Charge currents cancel while spin currents add | Predicted rather than demonstrated; equal-mass counterflows cancel mass current; not conventional niobium | 7 |
| Higgs–phonon or charge-density-wave hybrid | Observed condensate–lattice collective-mode mixing in materials such as NbSe2 | Demonstrates that a condensate mode can hybridize with a lattice mode | Primarily amplitude dynamics, not a neutral DC mass current or ionic circulation | 8 |

### 3.1 Strongest candidate: a genuine multicomponent charged quantum fluid

Babaev and Ashcroft studied a projected two-component superconductor in liquid metallic hydrogen or deuterium. In that system, electronic Cooper pairs and protonic or deuteronic pairs are both mobile quantum components with opposite electric charges and very different masses.

Such a medium naturally separates into:

- a **charged mode**, which couples strongly to electromagnetism;
- a **neutral mode**, in which the charge contributions cancel but the two positive mass contributions remain.

The related metallic-superfluid phase can be unable to carry dissipationless charge current while still carrying dissipationless mass flow. This is the cleanest known realization of Li's kinematic insight. It also produces nonstandard rotational response and violations of the ordinary single-component London law.

The conceptual correction to Li is decisive:

- Li tried to obtain a second component by assigning the electronic condensate phase to a stationary lattice.
- Multicomponent hydrodynamics begins with two independently justified mobile coherent fields and derives their charged and neutral eigenmodes.

Liquid metallic hydrogen is an extreme-pressure theoretical platform, not an immediate apparatus suggestion. Its value here is as a proof of principle and a template for the correct mathematics.

### 3.2 Ionic angular momentum: axial and chiral phonons

A circularly or elliptically polarized lattice vibration carries

\[
\mathbf J_{\rm ph}
=\sum_{l\alpha}M_\alpha\,\mathbf u_{l\alpha}\times\dot{\mathbf u}_{l\alpha},
\]

where `u` is the ionic displacement. This is actual mechanical angular momentum of nuclei about equilibrium positions, not merely a label on the superconducting phase.

Important developments include:

- Zhang and Niu's 2014 derivation of phonon angular momentum and its contribution to the Einstein–de Haas balance;
- 2024 evidence for chirality-selective phonon angular-momentum transport in quartz;
- a 2025 cantilever-torque measurement giving direct mechanical evidence for phonon angular momentum in tellurium;
- 2024–2026 work on large phonon magnetic moments and direct momentum-resolved chiral acoustic phonons.

This literature repairs Li's most specific missing object: **ions can support a coherent collective excitation with measurable angular momentum**.

It does not validate Li's ground-state claim. A phonon mode has a frequency, polarization, occupation, damping, wavevector, preparation channel, and angular-momentum balance. Time-reversal and crystal symmetries often make opposite chiralities cancel in equilibrium. To use this path, one must identify a superconducting material or heterostructure in which a selected axial phonon:

1. couples coherently to the condensate phase or current;
2. persists long enough to create a narrow response;
3. produces a charge-neutral mass/angular-momentum channel;
4. has an independently measurable phonon signature.

This is much more defensible than universal static ionic rotation.

### 3.3 Carlson–Goldman counterflow

Near `T_c`, a superconductor contains abundant normal quasiparticles capable of screening condensate-density fluctuations. The normal and superfluid components can oscillate out of phase so that little net charge accumulates. This is the Carlson–Goldman mode.

It validates a crucial part of the replacement principle: a charged superconductor can support a low-energy, approximately charge-neutral collective mode. However:

- the counterflow is mainly among electronic normal and superfluid components;
- it is damped and normally survives only in a restricted temperature and wavevector regime;
- its mass currents need not add as in an electron–heavy-ion pair.

It is therefore a useful **control model** for how electromagnetic screening exposes a neutral phase mode, not yet the desired large mass-current channel.

### 3.4 Leggett modes

In a multiband superconductor, two condensate phases can oscillate oppositely while the total phase remains nearly fixed. The resulting Leggett mode is neutral with respect to the common electromagnetic phase and has been observed spectroscopically in MgB2 and inferred in other multiband devices.

This is a clean example of a collective field `Θ` that is distinct from the overall superconducting phase `φ`. It is exactly the sort of extra order-parameter coordinate that Li's derivation lacked.

But a Leggett mode transfers pairs between bands or oscillates their relative phase. It does not automatically carry net mechanical angular momentum or a large total mass current. A material-specific coupling to rotation, lattice chirality, spin, or strain would have to be shown.

### 3.5 Entrainment

The Andreev–Bashkin effect describes dissipationless drag between two superfluids. Its hydrodynamic energy contains a cross term,

\[
F_{\rm kin}
=\frac12\rho_{11}v_1^2
+\rho_{12}\mathbf v_1\cdot\mathbf v_2
+\frac12\rho_{22}v_2^2.
\]

The current of either component is therefore not determined solely by its own velocity. This is the right formal concept for “a condensate drags another coherent subsystem.” Modern cold-atom work proposes interferometric detection, and cavity optomechanical signatures continue to be studied.

For this project, entrainment should replace the vague word “locking.” The questions become quantitative:

- What are the diagonal and cross stiffnesses `ρ_ab`?
- What eigenmode cancels charge?
- What is its mass and angular-momentum density?
- What are its gap, damping, and critical velocity?

### 3.6 Spin counterflow

Monkman and collaborators' 2026 theory of superconducting altermagnets provides a striking analog: spin-up and spin-down condensates can counterflow so that charge current cancels while spin current adds. This proves that superconducting order can, in principle, protect a persistent non-charge current.

It does not give Li's mass current. The two electronic components have essentially the same mass, so opposite velocities that cancel charge also cancel ordinary mass flow. Spin may couple to rotation or gravity through angular momentum, but that coupling must be calculated and is normally extremely weak.

## 4. The deeper replacement principle

The most productive reformulation is:

> Search for a neutral eigenmode of a multicomponent coherent medium that carries stress-energy or angular momentum while its electromagnetic current is screened or canceled.

Let each coherent component have phase `θ_a`, charge `q_a`, and mass `m_a`. Define a gauge-invariant velocity-like field

\[
\mathbf u_a
=\nabla\theta_a
-\frac{q_a}{\hbar}\mathbf A
-\frac{m_a}{\hbar}\mathbf A_g.
\]

The most general quadratic long-wavelength kinetic energy has a stiffness matrix,

\[
F_{\rm kin}
=\frac12\sum_{ab}\rho_{ab}\,
\mathbf u_a\cdot\mathbf u_b.
\]

The electromagnetic and mass responses follow by variation:

\[
\mathbf j_e=-\frac{\delta F}{\delta\mathbf A},
\qquad
\mathbf j_m=-\frac{\delta F}{\delta\mathbf A_g}.
\]

A Li-like matter mode is an eigenvector `e_N` of the stiffness matrix satisfying, schematically,

\[
q^T\rho e_N\approx0,
\qquad
m^T\rho e_N\ne0.
\]

This states the desired physics without assuming it. It cleanly separates three questions:

1. **Existence:** Does the material possess the second coherent component and neutral eigenmode?
2. **Matter gain:** How large are its mass and angular-momentum response relative to its electric response?
3. **Gravity gain:** Does gravity couple only to its ordinary stress-energy, or is there a new source-to-metric kernel?

Only after the first two are derived should an effective gravitomagnetic permeability be defined. In this language, `μ_g(ω,k)` is a compressed description of the calculated `j_m–A_g` response, not an assumed constant.

## 5. Implications for the Tate anomaly

The Tate measurement can constrain part of this response matrix. Rotation couples to the lattice and to the total angular momentum; the London field reads out the condensate's electromagnetic adjustment. A hidden neutral mode could therefore renormalize the `B/Ω` coefficient.

The decisive discriminants are not “gravity or no gravity” at the outset. They are:

- **isotope scaling:** an ionic contribution should change predictably with nuclear mass while electronic band structure changes more weakly;
- **material scaling:** residuals should correlate with electron–phonon coupling, phonon angular momentum, multiband structure, or entrainment stiffness rather than being universal;
- **temperature and frequency:** a collective mode should produce a pole, threshold, or damping signature, not a featureless constant offset;
- **geometry and surface dependence:** an electrostatic or penetration-depth systematic will scale differently from a bulk neutral mode;
- **rotation reversal and chirality:** an angular-momentum mode should have definite parity under reversal;
- **independent mechanical signature:** real ionic angular momentum should appear in torque, phonon spectroscopy, strain, or angular-momentum transfer;
- **gravitational independence:** a claimed `B_g` should affect a non-electromagnetic probe with the same inferred coupling.

This suggests that Tate is best treated as a **response-spectroscopy problem** before it is treated as a gravity experiment.

## 6. Recommended next work

### Priority 1 — Reconstruct the London-moment residual as a response matrix

Write the rotating-superconductor free energy with condensate phase, lattice displacement/rotation, electrostatic potential, electromagnetic field, and one candidate neutral field. Derive the measured `B/Ω` coefficient. Determine which combination of stiffness or entrainment coefficients would produce `92 ppm` and `18 ppm` residuals.

This directly tests the user's Tate–Li connection without presuming the answer.

**Completed 2026-07-24:** [Rotating-Superconductor Ionic Current, Response Matrix, and Tate Inversion](../DERIVATION_PACKAGE.md). The derivation proves that a clamped elastic lattice supplies no superconductivity-induced equilibrium bulk ionic current, derives the multicomponent result

\[
B=-2\Omega\frac{Q^TR\mathbf 1}{Q^TRQ},
\]

and finds that a neutral independently phase-rigid component would require `ρ_sχ/ρ_s = 9.2 × 10^-5` to reproduce the `92 ppm` comparison, with `ρ_χ/ρ_s > 8.46 × 10^-9` from positive definiteness. No such component is established in niobium.

### Priority 2 — Use the multicomponent-superconductor model as the clean template

Reproduce the Babaev–Ashcroft charged/neutral mode decomposition and then ask what minimal change would make it relevant to a solid:

- a mobile ionic condensate;
- a superconducting–exciton hybrid;
- a condensate–axial-phonon polariton;
- an unconventional two-component superconductor with rotation-sensitive relative phase.

The point is not to build liquid metallic hydrogen. It is to inherit a logically complete counterflow theory.

### Priority 3 — Investigate condensate–axial-phonon coupling

Search specifically for superconducting materials or heterostructures that combine:

- strong electron–phonon coupling;
- an infrared-active or Raman-active axial phonon;
- broken inversion, chirality, or magnetic order that selects one phonon angular momentum;
- a documented Higgs, Leggett, or phase-mode hybridization;
- an isotope series.

This is the most literal modern repair of Li's ionic intuition.

### Priority 4 — Obtain and audit the Hoang data package

The six-material data could distinguish ionic-mass, band, surface, and geometry hypotheses. Before using it, obtain the full article, supplementary methods, raw `B(Ω)` slopes, penetration-depth inputs, material purities, and uncertainty covariance. The lack of independent apparatus documentation makes this an evidence-quality task, not a settled result.

### Priority 5 — Keep gravity as a separate response block

Once a neutral mass/angular-momentum mode is established, calculate its ordinary GR field from the full stress-energy. Define an enhancement factor only as

\[
\eta_g(\omega,k)
=\frac{\text{observed metric or inertial response}}
{\text{response predicted from the same measured stress-energy in GR}}.
\]

This preserves the project's openness to a paradigm-level gravitational coupling without allowing matter-side uncertainties to masquerade as gravity gain.

## 7. Bottom line

The user's suggested Tate connection is worth pursuing. The best version is not “Tate measured Li's heavy ionic current.” It is:

> Tate may be a ppm-sensitive measurement of an incomplete condensate–lattice response law. Li's surviving intuition tells us what kind of omitted eigenmode to seek: electrically quiet but mechanically massive.

The literature now provides much better building blocks than Li had:

- a rigorous multicomponent route to neutral mass superflow;
- experimentally real ionic angular momentum in phonons;
- observed neutral phase modes in superconductors;
- a formal entrainment framework;
- modern precision constraints and null results.

What remains missing is the bridge that puts these ingredients in one material and one conserved theory. That—not a guessed scalar permeability—is the strongest thread to pull.

## 8. Candidate-paper analysis and verification status

The literature workflow's deterministic `verify_papers.py` helper was not available at its canonical local paths. Per the workflow contract, every candidate therefore retains `⚠ UNVERIFIED` status below. The DOI/arXiv metadata were separately checked against publisher or arXiv pages during this review; manual checking does not override the missing deterministic gate. Scratch records are in `.aris/verify-papers/`.

| Paper | Problem / method | Result used here | Relevance | Source | Verification status |
|---|---|---|---|---|---|
| Tate et al. 1989, *Precise Determination…* | Rotating-ring flux quantization measures `h/m_app` | `m_app/2m_e = 1.000084(21)` | Primary anomaly | Web/publisher | ⚠ UNVERIFIED — helper unavailable; DOI manually checked |
| Tate et al. 1990, *Determination…niobium* | Full experimental treatment | Detailed niobium result and systematics | Primary anomaly | Web/publisher | ⚠ UNVERIFIED — helper unavailable; DOI manually checked |
| Jiang & Liu 2001 | Thermodynamic/microscopic London-moment reconciliation | Lattice, electrostatic, and interaction terms; conventional correction near `10^-10` | Standard condensate–lattice baseline | Web/APS/arXiv | ⚠ UNVERIFIED — helper unavailable; DOI/arXiv manually checked |
| Hoang et al. 2020 | Rotating spherical-shell measurement across type-I superconductors | Reported six-material data; niobium residual summarized later as `18 ± 2.1 ppm` | Possible later replication/data set | Web/Elsevier | ⚠ UNVERIFIED — helper unavailable; DOI manually checked |
| Tajmar et al. 2022 | Cryogenic thrust balance for supercurrents | No anomalous force above about `100 nN` for currents to `15 A`; summarizes Hoang | Constraint and evidence-quality caution | Web/Frontiers | ⚠ UNVERIFIED — helper unavailable; DOI manually checked |
| Inan 2022 | Linearized-GR plus London constitutive equations | No isolated gravito-Meissner expulsion; enormous spatial scale; sign critique | Modern permeability/response assessment | Web/Frontiers | ⚠ UNVERIFIED — helper unavailable; DOI manually checked |
| Ummarino & Gallerati 2024 | Generalized TDGL for a laser-driven film | Predicts small transient generalized-field changes; no data | Recent gravity–superconductor theory | Web/Springer | ⚠ UNVERIFIED — helper unavailable; DOI manually checked |
| Babaev & Ashcroft 2007 | Rotational response of two oppositely charged condensates | Charged and neutral modes; nonstandard London response | Strongest clean replacement principle | Web/Nature/arXiv | ⚠ UNVERIFIED — helper unavailable; DOI/arXiv manually checked |
| Dolcini et al. 2010 | Superconductor–exciton-condensate junction theory | Charged supercurrent can convert to neutral counterflow | Engineered neutral-mode bridge | Web/APS/PubMed/arXiv | ⚠ UNVERIFIED — helper unavailable; DOI/arXiv manually checked |
| Carlson & Goldman 1975 | Microwave study of superconducting films | Propagating out-of-phase collective mode | Established neutral counterflow control | Web/APS metadata | ⚠ UNVERIFIED — helper unavailable; DOI manually checked |
| Sun et al. 2020 | Modern near-field response theory | Carlson–Goldman mode is charge-neutral normal/superfluid counterflow | Modern mode characterization | Web/APS | ⚠ UNVERIFIED — helper unavailable; DOI manually checked |
| Giorgianni et al. 2019 | THz control of multiband relative phase | Coherent Leggett-mode control in MgB2 | Observed distinct condensate field | Web/Nature | ⚠ UNVERIFIED — helper unavailable; DOI manually checked |
| Zhang & Niu 2014 | Quantum theory of lattice angular momentum | Phonons carry angular momentum and affect Einstein–de Haas balance | Ionic-field foundation | Web/APS | ⚠ UNVERIFIED — helper unavailable; DOI manually checked |
| Ohe et al. 2024 | Thermal transport in chiral quartz | Chirality-selective phonon angular-momentum transport | Ionic angular-momentum control | Web/APS | ⚠ UNVERIFIED — helper unavailable; DOI manually checked |
| H. Zhang et al. 2025 (previously misattributed here as “Parsonnet et al.”) | Cantilever torque under thermal gradient in tellurium | Direct mechanical evidence for phonon angular momentum (τ ≈ 10⁻¹¹ N·m) | Strongest ionic evidence | Web/Nature | ✔ Verified 2026-07-16 against Nature Physics 21, 1387 and arXiv:2409.13462 |
| Hossain et al. 2022 | Ring-interferometer proposal for superfluid entrainment | Quantitative detection protocol for cross-stiffness | Formal condensate-drag framework | Web/APS | ⚠ UNVERIFIED — helper unavailable; DOI manually checked |
| Monkman et al. 2026 | Microscopic and GL theory of superconducting altermagnets | Persistent pure spin current in charge-counterflow regime | Spin analog; not mass flow | Web/APS/arXiv | ⚠ UNVERIFIED — helper unavailable; DOI/arXiv manually checked |
| Koizumi 2021 | Berry-connection many-body theory | Non-gravitational explanation of free-electron mass in London moment | Alternative electromechanical explanation | Web/Springer/arXiv | ⚠ UNVERIFIED — helper unavailable; DOI/arXiv manually checked |

## 9. Primary links

- J. Tate et al., “Precise Determination of the Cooper-Pair Mass,” *Physical Review Letters* **62**, 845 (1989), [DOI](https://doi.org/10.1103/PhysRevLett.62.845).
- J. Tate, S. B. Felch, and B. Cabrera, “Determination of the Cooper-pair mass in niobium,” *Physical Review B* **42**, 7885 (1990), [DOI](https://doi.org/10.1103/PhysRevB.42.7885).
- Y. Jiang and M. Liu, “Rotating superconductors and the London moment: Thermodynamics versus microscopics,” *Physical Review B* **63**, 184506 (2001), [DOI](https://doi.org/10.1103/PhysRevB.63.184506), [arXiv](https://arxiv.org/abs/cond-mat/0010260).
- L. P. Hoang et al., “High-precision measurement of Cooper-pair mass using rotating spherical-shell superconductor,” *Materials Letters* **262**, 127176 (2020), [DOI](https://doi.org/10.1016/j.matlet.2019.127176).
- M. Tajmar, O. Neunzig, and M. Kößling, “Measurement of Anomalous Forces From a Cooper-Pair Current…,” *Frontiers in Physics* **10**, 892215 (2022), [DOI](https://doi.org/10.3389/fphy.2022.892215).
- N. A. Inan, “Superconductor Meissner Effects for Gravito-Electromagnetic Fields…,” *Frontiers in Physics* **10**, 823592 (2022), [DOI](https://doi.org/10.3389/fphy.2022.823592).
- G. A. Ummarino and A. Gallerati, “Gravitational effects in a superconducting film struck by a laser pulse,” *European Physical Journal C* **84** (2024), [DOI](https://doi.org/10.1140/epjc/s10052-024-12506-1).
- E. Babaev and N. W. Ashcroft, “Violation of the London law and Onsager–Feynman quantization in multicomponent superconductors,” *Nature Physics* **3**, 530 (2007), [DOI](https://doi.org/10.1038/nphys646), [arXiv](https://arxiv.org/abs/0706.2411).
- E. Babaev, A. Sudbø, and N. W. Ashcroft, “A superconductor to superfluid phase transition in liquid metallic hydrogen,” *Nature* **431**, 666 (2004), [arXiv](https://arxiv.org/abs/cond-mat/0410408).
- F. Dolcini et al., “Blockade and Counterflow Supercurrent in Exciton-Condensate Josephson Junctions,” *Physical Review Letters* **104**, 027004 (2010), [DOI](https://doi.org/10.1103/PhysRevLett.104.027004).
- Z. Sun et al., “Collective modes and terahertz near-field response of superconductors,” *Physical Review Research* **2**, 023413 (2020), [DOI](https://doi.org/10.1103/PhysRevResearch.2.023413).
- F. Giorgianni et al., “Leggett mode controlled by light pulses,” *Nature Physics* **15**, 341 (2019), [DOI](https://doi.org/10.1038/s41567-018-0385-4).
- L. Zhang and Q. Niu, “Angular Momentum of Phonons and the Einstein–de Haas Effect,” *Physical Review Letters* **112**, 085503 (2014), [DOI](https://doi.org/10.1103/PhysRevLett.112.085503).
- K. Ohe et al., “Chirality-Induced Selectivity of Phonon Angular Momenta in Chiral Quartz Crystals,” *Physical Review Letters* **132**, 056302 (2024), [DOI](https://doi.org/10.1103/PhysRevLett.132.056302).
- H. Zhang, N. Peshcherenko, F. Yang, T. Z. Ward, P. Raghuvanshi, L. Lindsay, C. Felser, Y. Zhang, J.-Q. Yan, and H. Miao, “Measurement of phonon angular momentum,” *Nature Physics* **21**, 1387 (2025), [DOI](https://doi.org/10.1038/s41567-025-02952-3), [arXiv:2409.13462](https://arxiv.org/abs/2409.13462). *(Author list corrected 2026-07-16; previously misattributed as “N. Parsonnet et al.”)*
- K. Hossain, S. Gupta, and M. M. Forbes, “Detecting entrainment in Fermi-Bose mixtures,” *Physical Review A* **105**, 063315 (2022), [DOI](https://doi.org/10.1103/PhysRevA.105.063315).
- K. Monkman et al., “Persistent Spin Currents in Superconducting Altermagnets,” *Physical Review X* **16**, 011057 (2026), [DOI](https://doi.org/10.1103/52wh-1z5y).
- H. Koizumi, “London Moment, London's Superpotential, Nambu-Goldstone Mode, and Berry Connection from Many-Body Wave Functions,” *Journal of Superconductivity and Novel Magnetism* **34**, 1361 (2021), [DOI](https://doi.org/10.1007/s10948-021-05827-9).

## 10. Local-source contribution

- G. A. Ummarino and A. Gallerati, *Possible Alterations of Local Gravitational Field Inside a Superconductor* (2021), local PDF `02_Gravitation-Theory/Ummarino-Gallerati-Possible-Alterations-Local-Gravity-Superconductor-2021.pdf`, DOI [`10.3390/e23020193`](https://doi.org/10.3390/e23020193).
- Ning Li and Douglas Torr primary-paper set in `02_Gravitation-Theory/Ning-Li-Superconductivity-Program/`.

**Search channels that contributed sources:** local project files and web/publisher search. No native `research-wiki/` directory, Zotero library, or Obsidian vault was present, so this report was integrated into the project's existing `00_Knowledgebase/` structure.
