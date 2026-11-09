# Ning Li, Superconductors, and Gravitomagnetism — Deep Dive

**Date:** 2026-07-15  
**Scope:** Ning Li and Douglas Torr's 1991–1993 superconducting-gravity theory, Li's 1997 static YBCO test, published critiques, and the public NASA/Army follow-up record.  
**Project question:** Can superconducting quantum coherence produce a gravitomagnetic or electromagnetic-to-gravitational response materially larger than the response of the same ordinary stress-energy in general relativity?

## Executive assessment

Ning Li's program is worth studying because it is unusually specific. It does not merely say that superconductors are “quantum” and might affect gravity. It proposes a chain:

1. a superconducting condensate couples to electromagnetic and weak gravitational vector potentials through canonical momentum;
2. the condensate and ionic lattice support compensating charge currents but reinforcing mass currents;
3. superconducting magnetic attenuation can therefore be represented by an anomalous material gravitomagnetic permeability;
4. the resulting response amplifies gravitomagnetic and gravitoelectric fields to potentially measurable levels.

The first step is a legitimate weak-field starting point. The rest of the chain is not established. The decisive weakness is the transfer of superconducting phase quantization from the Cooper-pair condensate to the individual lattice ions. Li and Torr use that transfer to infer coherent ionic angular momentum, use the uncertainty principle to exclude zero circulation, and then use the resulting “bound” ionic current to construct a large mass current and relative gravitomagnetic permeability. Those steps do not follow from conventional superconductivity or quantum mechanics.

My current verdict is therefore:

> **Li identified a valuable research question and a potentially testable response channel, but her published derivation does not establish the claimed amplification. The exact load-bearing mechanism — quantized coherent ionic mass current — should be considered unsupported unless it can be re-derived from a covariant microscopic or effective theory.**

This does **not** close the broader superconductivity–gravity question. It separates two propositions that should not be allowed to travel together without proof:

- **Open research proposition:** a coherent superconducting state may possess a gravitational or mixed electromagnetic–gravitational response not obvious from a classical lumped-mass description.
- **Unsupported Li–Torr proposition:** the Meissner state produces a large relative gravitomagnetic permeability through quantized lattice-ion rotation and nearly vanishing magnetic permeability.

The next move should be theoretical, not experimental: reconstruct the response from an action or Hamiltonian, identify the actual stress-energy and response kernel, and determine whether any enhancement remains after gauge invariance, conservation, and known null results are imposed.

## Confidence map

| Component | Assessment | Confidence |
|---|---|---|
| Weak-field gravitoelectromagnetic starting point | Legitimate approximation when conventions and gauge limits are controlled | High |
| Gravitational vector potential in superconducting canonical momentum | Legitimate weak-coupling ingredient; by itself predicts extremely small effects | High |
| Condensate phase quantization | Established for the collective superconducting order parameter | High |
| Quantization of every lattice ion's circulation from the condensate phase | Not derived; conflicts with the ownership of the superconducting order parameter | High |
| Uncertainty principle forces winding number `n >= 1` | Incorrect; uncertainty does not forbid a zero-circulation state | High |
| Bound ionic charge current cancels Cooper-pair current while mass currents add | Not established for a stationary superconducting lattice | High |
| `μ_g / μ_g0 ~ 10^4` material response | Unsupported because it depends on the preceding steps and a problematic permeability analogy | High |
| Detectable induced `E_g` or `B_g` | Not established | High |
| Static gravitational shielding by YBCO | Directly constrained by Li's 1997 null result to less than 2 parts in `10^8` of local `g` for that apparatus | High |
| Dynamic superconducting gravity coupling in general | Not decisively tested by the static null or the unfinished NASA apparatus | Medium-high |
| Public experimental confirmation of Li's mechanism | None identified | High |

## 1. What Li and Torr actually proposed

### 1.1 The legitimate starting point: canonical momentum

In a weak gravitational field and at low velocity, gravitoelectromagnetic notation can be used to introduce a gravitational scalar and vector potential. For a superconducting carrier, a schematic canonical-momentum relation is

\[
\hbar \nabla\theta
= m^*\mathbf v_s + q^*\mathbf A + m^*\mathbf A_g,
\]

where `θ` is the condensate phase, `m*` and `q*` are the Cooper-pair mass and charge, `A` is the electromagnetic vector potential, and `A_g` is a convention-dependent weak-field gravitational vector potential. Signs and numerical factors depend on the GEM convention; the physical comparison must ultimately be expressed through invariant observables.

Taking a curl connects condensate vorticity, magnetic field, and gravitomagnetic field. This is a reasonable way to ask how rotation or frame dragging changes flux quantization and superconducting phase. It is not yet an amplification mechanism. With ordinary gravitational coupling, the effect is minuscule because the gravitational field still comes from the system's actual stress-energy and angular momentum.

### 1.2 The 1991 paper: coupled penetration and an introduced material parameter

In *Effects of a Gravitomagnetic Field on Pure Superconductors* (1991), Li and Torr combine linearized gravity, Maxwell equations, and London equations. Deep in the superconductor, their equations drive a combination of the electromagnetic and gravitomagnetic fields toward zero rather than requiring each field independently to vanish. They introduce gravitational material quantities analogous to electromagnetic permittivity and permeability and note that the predicted residual fields depend on a ratio involving `μ_g / μ`.

The paper's durable contribution is the coupled-field question. Its unresolved issue is that `μ_g` is introduced phenomenologically. No microscopic or covariant constitutive theory is supplied that would let a superconductor acquire a large gravitational susceptibility.

### 1.3 The 1992 paper: the lattice-ion bridge

*Gravitational Effects on the Magnetic Attenuation of Superconductors* (1992) attempts to supply that missing bridge. It divides the system into:

- “free” Cooper-pair currents; and
- “bound” lattice-ion currents.

The key derivation assigns the superconducting phase to an ion canonical momentum, schematically

\[
\mathbf p_i = 2\hbar\nabla_i\phi,
\]

and integrates it around a closed path to obtain quantized ionic circulation. The paper then invokes the uncertainty principle to argue that the winding integer cannot be zero, concluding that each lattice ion carries uniformly quantized angular momentum. These ionic currents are then made to interact with the condensate over a coherence length.

This is the central break in the argument:

1. The macroscopic phase is the phase of the superconducting condensate. It does not automatically define a single-valued wavefunction in the coordinate of each lattice ion.
2. A topological winding number may be zero. The uncertainty relation does not force a nonzero circulation quantum.
3. An Abrikosov vortex is a phase-winding and supercurrent structure in the condensate, with a core and quantized flux. It is not literal coherent rotation of all ions in the lattice.

Without a separately derived ionic collective mode carrying real angular momentum, the large “bound” mass current does not exist.

### 1.4 The 1993 paper: the amplification claim

*Gravitoelectric-Electric Coupling via Superconductivity* (1993) makes the proposed payoff explicit. Li and Torr argue that free and bound **charge** currents largely cancel, while their **mass** currents add because gravitational mass has only one sign. From gyromagnetic ratios they estimate

\[
\mu_g \approx \frac{\gamma_e}{\gamma_i}\mu_{g0}
\approx 10^4\mu_{g0}.
\]

They then predict an electrically induced gravitoelectric response of the form

\[
\mathbf E_g^{\mathrm{ind}}
\propto \frac{\mu_g}{\mu}\frac{m}{q}
\frac{\partial \mathbf A}{\partial t},
\]

and a gravitomagnetic response proportional to an applied magnetic field. The paper estimates a single-ion gravitomagnetic contribution and then sums over roughly `10^28` coherently participating ions to obtain a potentially detectable result.

This is a coherent hypothesis, but the magnitude is inherited from the disputed ionic current and permeability model. Coherence can make amplitudes or phases add in a defined collective observable. It does not allow a system to possess angular momentum or stress-energy that is absent from its physical state. A valid calculation must show where that angular momentum resides, how it is prepared, and how the complete stress-energy tensor changes.

## 2. The load-bearing problems

### 2.1 Order-parameter ownership

Fluxoid quantization arises from single-valuedness of the condensate order parameter. Lattice ions participate in the crystal and in phonon dynamics, and their interaction with electrons is essential to conventional pairing, but this does not make each ion a carrier of the condensate phase. The Li–Torr assignment needs an independent many-body derivation. None appears in the papers reviewed.

### 2.2 Misuse of the uncertainty principle

The uncertainty relation constrains variances of conjugate observables. It does not set a topological winding number and does not require a ring or condensate ground state to circulate. `n = 0` is an ordinary allowed state. The asserted universal nonzero ionic angular momentum therefore has no demonstrated basis.

### 2.3 Conflating Meissner screening with small constitutive permeability

The Meissner effect is not well represented as an ordinary magnetic medium whose local constitutive permeability simply tends to zero. It is a dynamical, geometry-dependent screening response encoded by London or more microscopic nonlocal electrodynamics. Mark Kowitt's 1994 critique attacks precisely this point: using the permeability associated with magnetic attenuation as the denominator in the gravitational estimate grossly overstates the result.

This distinction matters because the claimed amplification is built from a ratio. If the small denominator is not a legitimate local material permeability, the large ratio is not a physical gain.

### 2.4 Unproved cancellation of charge current and survival of mass current

The Meissner screening current is a condensate current. A static lattice is not automatically a counter-flowing ionic charge current. To produce the Li–Torr result, one needs an actual ionic velocity field that cancels charge transport but contributes a large same-signed mass current. That motion should have mechanical angular momentum, kinetic energy, phonon or rotational signatures, and a preparation mechanism. The papers do not supply them.

### 2.5 Gyromagnetic ratio is not gravitational susceptibility

A mass-to-charge or gyromagnetic ratio converts between descriptions of a carrier that genuinely carries both charge and angular momentum. It does not create an independent gravitational constitutive response. In general relativity the source is the total stress-energy tensor. An enhancement beyond that source requires new dynamics, not a relabeling of electromagnetic current.

### 2.6 Coherence is not an energy multiplier

“Coherent” must name a specific correlator or order parameter. It may produce macroscopic quantum occupation, phase rigidity, interference, suppressed noise, or collective response. It does not by itself multiply gravitational source strength. The open question is whether a superconducting state has a nontrivial **mixed response kernel**, not whether a large number of particles can be declared phase aligned.

### 2.7 Missing covariant response theory

A material `μ_g` should emerge from a theory that respects diffeomorphism invariance, stress-energy conservation, and the relevant electromagnetic gauge symmetry. At minimum the calculation must specify an action, identify all dynamical degrees of freedom, derive `T_{μν}`, and compute a gauge-consistent response. The Li–Torr papers instead import a Maxwell-material analogy at the point where a gravitational derivation is most needed.

## 3. Published critical response

### Mark Kowitt (1994)

Kowitt's *Gravitomagnetism and Magnetic Permeability in Superconductors* states that Li and Torr grossly overestimated the effect by misinterpreting the magnetic permeability used to describe the Meissner state. This is not a peripheral objection: it removes the small electromagnetic denominator that drives the proposed amplification.

### Edward G. Harris (1999)

Harris's published comment on the 1993 paper concludes that unrealistic assumptions make the predicted fields too large by many orders of magnitude. The publisher abstract supports that general conclusion. A precise numerical discrepancy sometimes attributed to Harris could not be checked against a full publicly accessible copy during this review, so it is not used here as a verified number.

### Claus Kiefer and Carsten Weber (2005)

Kiefer and Weber review how mesoscopic quantum systems couple to gravity. Their analysis retains the real canonical coupling but finds ordinary effects extraordinarily small; a representative DeWitt-type estimate gives an induced current around `10^-29 A` for their stated example. Their conclusion is methodologically aligned with this report: before more rotating-superconductor experiments, the theoretical electro-gravitomagnetic coupling must be made substantially more precise.

The critiques converge on a useful distinction: **the weak coupling term is real; the enormous material enhancement is the unsupported part.**

## 4. What was actually tested

### 4.1 Li et al. 1997: static YBCO test

Li, David Noever, Tony Robertson, Ron Koczor, and Whitt Brantley tested large type-II YBCO superconductors with a gravimeter and controls for magnetic, thermal, and vibration effects. They found no static gravity change larger than 2 parts in `10^8` of local `g`.

This is a meaningful direct null for static shielding, absorption, or a static weight-like field in that configuration. It does not directly test the 1993 term proportional to a time-varying vector potential. It should therefore constrain the static branch without being generalized into “superconductors cannot couple anomalously to gravity.”

### 4.2 NASA rotating-field work

A 1998 NASA-associated experiment applied rotating magnetic fields to bulk YBCO disks and reported no gravity modification within its sensitivity. The apparatus did not achieve the fully levitated, high-speed rotating-superconductor state envisioned in the broader program, and the applied fields were modest. It is a relevant null for that implemented condition, not a definitive test of every dynamic Li configuration.

### 4.3 NASA Cooperative Agreement NCC8-124

The official final report states that the University of Alabama in Huntsville effort began in December 1996, produced two usable 12-inch YBCO disks, and built the required materials and characterization capability. The intended final experiments involved levitated rotating disks, potentially with radio-frequency excitation and gravity instrumentation.

The same report is explicit that technical and funding difficulties prevented the final integrated experiments. The disks were never used in the desired all-up tests. The correct knowledgebase status is **planned but not completed**, not secret success, failure, or replication.

### 4.4 Army prototype agreement

The Department of Defense FY2001 report on Other Transactions records agreement `DAAH01-01-9-R001`, “Gravito–Electro Magnetic Superconductivity Experiment,” with AC Gravity, effective 25 April 2001 to 25 September 2002, with `US$448,970` in government funding. The stated objective was to attempt experimental confirmation of Li's theory using a type-II superconducting disk in an external magnetic field.

The award document establishes funding and intent. No public final technical result was located in this review. “Outcome unavailable” is the only warranted status.

### 4.5 2003 conference abstract

A conference schedule documents a Ning Li presentation titled *Measurability of AC Gravity Fields*. A recovered abstract describes induced nuclear angular dipole moments and high-frequency gravitational-field generation/detection. No complete, peer-reviewed proceedings paper or validating data set was located. This is grey-literature evidence that her theoretical emphasis may have shifted from literal bulk lattice rotation toward nuclear angular momentum; it is not experimental confirmation.

### 4.6 Adjacent replication: Hathaway, Cleveland, and Bao (2003)

This experiment targeted the Podkletnov rotating-superconductor/RF claim rather than Li's exact response equation. It found no weight modification to `0.001%` sensitivity, while also failing to reach the proposed high-frequency levitated rotation. It constrains a neighboring implementation and its accessible parameter range; it is not a clean direct falsification of the Li–Torr mechanism.

## 5. Claim-to-evidence audit

| Claim | Best supporting basis | Best constraint | Current status |
|---|---|---|---|
| Weak gravity enters superconducting phase/canonical momentum | Standard weak-field minimal coupling | Convention and gauge care required | Retain |
| Superconductivity is an unusually sensitive probe of rotation/gravity | Macroscopic phase coherence and precision flux/phase measurements | Sensitivity does not imply source amplification | Retain as a measurement strategy |
| Every lattice ion possesses quantized nonzero circulation | Li–Torr 1992 construction | Order parameter belongs to condensate; `n = 0` allowed | Reject unless re-derived |
| Ionic and condensate charge currents cancel while mass currents add | Li–Torr two-current picture | No demonstrated ionic counterflow or stress-energy accounting | Unsupported |
| Superconductor has `μ_g ~ 10^4 μ_g0` | Gyromagnetic-ratio and permeability argument | Kowitt, Harris, missing covariant constitutive theory | Unsupported |
| Applied/time-varying EM fields create measurable `E_g` or `B_g` | Li–Torr 1993 prediction | No public successful direct measurement; standard estimates tiny | Open only as a new-theory hypothesis |
| Static YBCO shields or changes gravity | Early superconducting anomaly context | Li et al. 1997 null below `2 × 10^-8 g` | Constrained for tested apparatus |
| NASA completed a decisive Li test | Intended NCC8-124 program | Official report says final experiment not completed | False |
| Army funding confirms the effect | Documented prototype award | Funding is not a result; no public outcome located | False inference |

## 6. The viable thread that remains

The most productive reformulation is:

> **Does a superconducting coherent state possess a gravitational susceptibility or mixed electromagnetic–gravitational response beyond the response calculated from its ordinary total stress-energy tensor?**

This wording preserves the user's central intuition — quantum coherence may matter — while removing the unsupported assumption that coherence must take Li's lattice-ion form.

There are several physically distinct possibilities that must remain siloed:

1. **Measurement enhancement:** the condensate phase is an exquisitely sensitive detector of ordinary rotation or weak gravity. No gravity generation is implied.
2. **Known-state stress-energy:** condensation energy, supercurrents, magnetic fields, lattice strain, and angular momentum source gravity exactly as standard theory predicts. The effect is real but tiny.
3. **Mixed linear response:** an electromagnetic perturbation changes the expectation value of stress-energy through a calculable material response. This can be nontrivial without violating conservation, but it may remain extremely small.
4. **New gravitational constitutive response:** the coherent state carries an additional low-energy coupling or collective mode that enhances gravity beyond the standard stress-energy result. This is the extraordinary and presently unestablished branch.
5. **Macroscopic inertial-frame control:** even a measured anomalous susceptibility would still need a separate scaling and geometry bridge to craft-scale inertial separation.

Keeping these levels separate prevents a sensitive quantum detector from being mistaken for a strong gravity source.

## 7. Recommended next work: a “repair or retire” theory audit

No apparatus should be selected yet. The next deliverable should be a self-contained derivation that either recovers a genuine enhancement or retires Li's mechanism while preserving any valid ingredients.

**Completed follow-up:** [Ning Li — Annotated Derivation Audit](Ning-Li-Annotated-Derivation-Audit-2026.md). It reconstructs the 1991–1993 equations step by step and separates Li's original chain, the strongest conventional reconstruction, and the minimum new laws needed for a coherent Li-like mechanism.

### Step 1 — Define the target response

Use a dimensionless, frequency- and wavevector-dependent enhancement rather than the ambiguous phrase “gravitomagnetic permeability”:

\[
\eta(\omega,\mathbf k)
= \frac{\text{material gravitational or mixed response}}
{\text{ordinary GR response of the same complete stress-energy}}.
\]

`η = 1` is the ordinary baseline. Any `η >> 1` claim must identify the new degree of freedom and its energy, momentum, and symmetry constraints.

### Step 2 — Start from a covariant action or controlled Hamiltonian

Include, at minimum:

- the superconducting order parameter;
- electromagnetic fields;
- lattice displacement/phonon fields;
- any nuclear-spin or ionic angular-momentum mode being claimed;
- weak metric perturbations or a tetrad/spin connection;
- all interaction terms allowed by the material symmetries.

This prevents the response coefficient from being inserted by analogy.

### Step 3 — Compute the complete source

Derive the total `T_{μν}` including condensate, quasiparticles, lattice, electromagnetic field, binding/condensation energy, and mechanical supports. Explicitly separate:

- condensate phase winding;
- Cooper-pair mass current;
- lattice displacement and rotation;
- nuclear spin polarization;
- electromagnetic momentum and stresses.

If the theory claims a large mass current with little charge current, it must exhibit the actual neutral counterflow mode and its kinetic energy.

### Step 4 — Calculate a mixed response kernel

A useful object is a Kubo-type susceptibility, schematically

\[
\chi_{T J}^{\mu\nu,\alpha}(\omega,\mathbf k)
= \frac{\delta\langle T^{\mu\nu}\rangle}
{\delta A_\alpha},
\]

supplemented by the gravitational response `δ<T>/δg`. Ward identities should enforce charge conservation, stress-energy conservation, and gauge consistency. This is the rigorous version of Li's proposed `E -> E_g` bridge.

### Step 5 — Re-derive or eliminate the ionic mode

Ask directly:

- What operator represents the claimed ionic angular momentum?
- What is its eigenstate, excitation gap, coherence time, and preparation mechanism?
- Is it a phonon, rigid-body rotation, nuclear-spin polarization, orbital current, or something else?
- What observable besides gravity proves the mode is populated?

If no such mode exists, the original `μ_g` amplification is retired.

### Step 6 — Apply present constraints before designing hardware

The theory should reproduce:

- the 1997 static null in the appropriate limit;
- the absence of a large ordinary gravitational field from persistent supercurrents;
- standard equivalence-principle and gravitomagnetic limits;
- electromagnetic, thermal, mechanical, and magnetic side effects implied by any ionic motion.

Only after a nonzero, conservation-complete residual prediction survives should an apparatus be chosen.

## 8. What this means for the overall project

Ning Li should move near the front of the project's **theory-selection** queue, not because her claimed `10^4` enhancement is credible as published, but because her work exposes the correct bottleneck: a material bridge from controllable quantum matter to a gravitational source or inertial-frame response.

The project should not yet optimize resonators, rotating disks, or craft requirements around her equations. It should first answer three numerical questions:

1. What is `η(ω,k)` in standard superconducting effective theory when every contribution to `T_{μν}` is included?
2. What additional term or collective mode would be required to make `η` materially exceed unity without violating Ward identities, equivalence-principle bounds, or energy accounting?
3. If an anomalous `η` exists, what invariant gravitational observable follows — tidal response, frame dragging, phase shift, acceleration, or boundary geometry — and how far is it from inertial-frame control?

This is a better-defined thread than “build an antigravity superconductor.” It gives the hypothesis a fair chance while making the point of failure explicit.

## 9. Open questions

1. Did Li ever publish or circulate a full derivation replacing the 1992 lattice-ion phase assignment, especially in the referenced 1994 preprint *Lattice Ion Rotations and the Dipole Gravitomagnetic Field of Superconductors*?
2. What exactly was meant by “AC gravity” in her final work: bulk ionic rotation, nuclear-spin ordering, an induced gravitoelectric field, or gravitational radiation?
3. Is there a public final report, data package, or closeout record for Army agreement `DAAH01-01-9-R001`?
4. Can modern covariant superconducting effective field theory produce any mixed `T–J` response not already accounted for by ordinary stress-energy?
5. Are there material phases — neutral superfluids, spin-triplet superconductors, exciton condensates, supersolids — that isolate mass coherence from charge screening more cleanly than YBCO?

## 10. Sources and verification

### Local primary papers reviewed in full

- Ning Li and D. G. Torr, “Effects of a Gravitomagnetic Field on Pure Superconductors,” *Physical Review D* **43**, 457–459 (1991), DOI [`10.1103/PhysRevD.43.457`](https://doi.org/10.1103/PhysRevD.43.457). Local file: [Gravitomagnetic field on SCs.pdf](../02_Gravitation-Theory/Ning-Li-Superconductivity-Program/Gravitomagnetic%20field%20on%20SCs.pdf).
- Ning Li and D. G. Torr, “Gravitational Effects on the Magnetic Attenuation of Superconductors,” *Physical Review B* **46**, 5489–5495 (1992), DOI [`10.1103/PhysRevB.46.5489`](https://doi.org/10.1103/PhysRevB.46.5489). Local file: [Gravitational effects on magnetic attenuation SCs PhysRevB.46.5489.pdf](../02_Gravitation-Theory/Ning-Li-Superconductivity-Program/Gravitational%20effects%20on%20magnetic%20attenuation%20SCs%20PhysRevB.46.5489.pdf).
- D. G. Torr and Ning Li, “Gravitoelectric-Electric Coupling via Superconductivity,” *Foundations of Physics Letters* **6**, 371–383 (1993), DOI [`10.1007/BF00665654`](https://doi.org/10.1007/BF00665654). Local file: [cupdf.com_torr-and-li-1993-gravitoelectric-electric-coupling.pdf](../02_Gravitation-Theory/Ning-Li-Superconductivity-Program/cupdf.com_torr-and-li-1993-gravitoelectric-electric-coupling.pdf).
- Ning Li et al., “Static Test for a Gravitational Force Coupled to Type II YBCO Superconductors,” *Physica C* **281**, 260–267 (1997), DOI [`10.1016/S0921-4534(97)01462-7`](https://doi.org/10.1016/S0921-4534(97)01462-7). Local file: [Static test Gravitational Force YBCO.pdf](../02_Gravitation-Theory/Ning-Li-Superconductivity-Program/Static%20test%20Gravitational%20Force%20YBCO.pdf).

### Critiques and broader theory

- Mark Kowitt, “Gravitomagnetism and Magnetic Permeability in Superconductors,” *Physical Review B* **49**, 704 (1994), DOI [`10.1103/PhysRevB.49.704`](https://doi.org/10.1103/PhysRevB.49.704).
- Edward G. Harris, “Comments on ‘Gravitoelectric-Electric Coupling via Superconductivity’ by D. G. Torr and Ning Li,” *Foundations of Physics Letters* **12**, 201–208 (1999), DOI [`10.1023/A:1021621425670`](https://doi.org/10.1023/A:1021621425670).
- Claus Kiefer and Carsten Weber, “On the Interaction of Mesoscopic Quantum Systems with Gravity,” *Annalen der Physik* **14**, 253–278 (2005), DOI [`10.1002/andp.200410119`](https://doi.org/10.1002/andp.200410119); [arXiv:gr-qc/0408010](https://arxiv.org/abs/gr-qc/0408010).

### Experimental and administrative record

- NASA, “Activities of UAH,” final report for Cooperative Agreement NCC8-124 (2000), [NASA NTRS 20000038203](https://ntrs.nasa.gov/citations/20000038203).
- Tony Robertson et al., “Superconductor-Mediated Modification of Gravity? AC Motor Experiments with Bulk YBCO Disks in Rotating Magnetic Fields” (1998), [NASA NTRS 19990019627](https://ntrs.nasa.gov/citations/19990019627).
- G. E. Hathaway, B. Cleveland, and Y. Bao, “Gravity Modification Experiment Using a Rotating Superconducting Disk and Radio Frequency Fields,” *Physica C* **385**, 488–500 (2003), DOI [`10.1016/S0921-4534(02)02284-0`](https://doi.org/10.1016/S0921-4534(02)02284-0).
- U.S. Department of Defense, *FY2001 Annual Report on Other Transactions*, archived award record for `DAAH01-01-9-R001`, [archived official document](https://web.archive.org/web/20210801183915/https://www.acq.osd.mil/dpap/Docs/FY01RPT.doc).
- 2003 Gravitational-Wave Conference schedule, [conference program](https://www.integrityresearchinstitute.org/Gravity-Meeting-Schedule.pdf).

### Verification note

Bibliographic metadata for the journal papers was checked against DOI/publisher or arXiv records. NASA project status was checked against NTRS records and the official final report. Army funding was checked against the archived DoD award report. The research-literature skill's automated `verify_papers.py` helper was not present in this workspace, so verification was completed manually against these primary records. No Ning Li-authored gravity patent was identified in the sources searched; later patents that cite Li and Torr should not be misattributed to her.
