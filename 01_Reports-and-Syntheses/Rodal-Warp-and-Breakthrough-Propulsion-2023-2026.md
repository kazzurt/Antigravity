# José J. A. Rodal — Warp & Breakthrough-Propulsion Physics (2023–mid-2026)

**Scope:** deep technical review of José Rodal's publications in warp-drive / gravitational / inertial (breakthrough) propulsion physics, newest first, ~2023–mid-2026. arXiv preprints and refereed journal articles are treated as primary; forum/blog activity is background only; every citation verified against publisher + arXiv + ADS/INSPIRE.

**Date:** June 2026.

**Method:** parallel literature reviews (bibliography + verification, warp-metric deep dive, Mach-effect deep dive, field reception) followed by primary-source verification of the citations and the contested energy-condition claims.

> **Provenance:** this is the **canonical** document, merged 2026-06-19 from two earlier overlapping reports (a deep-research synthesis and a separate Word write-up). Where they disagreed, conflicts were resolved against primary sources and noted inline (see the two ⚠️ flags below). The superseded originals are kept in `_archive/`.

---

## Bottom line

José Rodal is an **independent, MIT-trained (PhD Aero/Astro) researcher** — President of Rodal Consulting (Cary, NC) and a former **NASA NIAC Mach-Effect / MEGA-drive team member** — who over 2023–2026 has become one of the most technically rigorous, and notably *skeptical*, voices in warp/propulsion theory. He is not offering pop-sci "warp works now" claims; he is trying to identify which **geometrical features actually control exoticity**, with irrotationality and Hawking–Ellis algebraic type in the starring roles.

His program has two prongs:

- **Constructive.** He built the first fully explicit, analytic **irrotational ("zero-vorticity") warp metric** that is *globally Hawking–Ellis Type I* — a well-defined, frame-invariant proper energy density everywhere — which **reduces but does not remove** the exotic-matter requirement (peak energy deficit ~38× below Alcubierre). It is best read as the **"least-bad known classical metric in this narrow class," not an escape from the no-go theorems.**
- **Destructive (from inside the camp).** He published rigorous covariant arguments that **two propulsion shortcuts don't work** — "low-energy" warp via engineered metamaterials, and the **Woodward Mach-effect thruster** he himself once helped model.

The throughline is one methodological conviction: judge these spacetimes by *coordinate-invariant* curvature/eigenstructure, not by observer-dependent energy density — and when you do, the exotic-matter problem is **sharpened, not solved.** Crucially, he is explicit that he does **not evade** the warp no-go theorems; he minimizes within them.

---

## Verified publications (newest first)

| # | Title | Type / Venue | Date | DOI / arXiv | Peer review |
|---|---|---|---|---|---|
| 1 | Weakly birefringent screening disfavors fast Hawking–Ellis Type I warp drives via low-velocity cubic tilt scaling | Preprint | 22 Mar 2026 | arXiv:2603.21352 | Preprint |
| 2 | A Machian wave effect in conformal, scalar–tensor gravitational theory | Preprint (covariant expansion of his 2019 GRG paper) | 27 Dec 2025 | arXiv:2512.22687 | Preprint\* |
| 3 | **A warp drive with predominantly positive invariant energy density and global Hawking–Ellis Type I** | *Gen. Rel. Grav.* 58, Art. 1 | publ. 17 Dec 2025 (online); arXiv 19 Dec 2025 | 10.1007/s10714-025-03495-x · arXiv:2512.18008 | **Refereed** ★ |
| 4 | On the Infeasibility of Low-Energy Warp Drive via Metamaterial Gravitational Coupling | Preprint (+ Zenodo) | 13 Jul 2025 | arXiv:2507.09724 | Preprint |
| 5 | A Closer Look at Natário's Zero-Expansion Warp Drive | *Int. J. Theor. Phys.* 63, Art. 168 | publ. 8 Jul 2024; arXiv mirror 22 Dec 2025 | 10.1007/s10773-024-05700-0 · arXiv:2512.19837 | **Refereed** |
| 6 | Visualization and analysis of the curvature invariants in the Alcubierre warp-drive spacetime | *Gen. Rel. Grav.* 55, Art. 134 | publ. 18 Nov 2023; arXiv mirror 23 Dec 2025 | 10.1007/s10714-023-03182-9 · arXiv:2512.20738 | **Refereed** |

\*Item 2's journal-reference/DOI point to his **2019** GRG paper (*Gen. Rel. Grav.* 51:64, "A Machian wave effect…" electroelasticity Mach-effect model); the Dec-2025 posting is a covariant re-derivation/expansion of that foundational work, not a new journal article.

**These six are the distinct in-scope works** — **three refereed journal articles** (GRG 2023, IJTP 2024, GRG 2026) and **three preprints** (metamaterial 2025, Machian 2025, birefringent 2026).

**Note on the Dec-2025 arXiv cluster.** Items 2, 3, 5, 6 all carry December-2025 arXiv IDs (2512.18008 / .19837 / .20738 / .22687). This is Rodal posting/mirroring his journal papers (2023 GRG, 2024 IJTP, 2019 GRG) to arXiv around the same time he released his new 2026 GRG paper — so the arXiv mirrors do **not** represent additional distinct results. No separate 2023–mid-2026 conference proceeding or recorded talk was verifiable with publication-grade bibliographic metadata, though Rodal is independently documented on the Space Studies Institute / NASA NIAC Mach-effect effort.

> ⚠️ **Attribution correction (resolved against arXiv, 2026-06-19).** One source report listed **arXiv:2603.21352** as "by other authors." It is **Rodal's own paper** (item 1). The genuinely other-authored 2026 warp papers that merely *cite* Rodal are **arXiv:2602.16495** (Lyon classification/no-go) and **arXiv:2605.25417** ("boundary cost of source-consistent warp shells").

---

## 1. "Weakly birefringent screening disfavors fast Hawking–Ellis Type I warp drives…" (Mar 2026)

Rodal's newest identifiable propulsion item — and the least mature, furthest from the standard GR warp literature. Rather than proposing a new ADM warp metric, it asks whether the residual mixed-sector transport of his irrotational Type I background can be **"screened"** inside the **weakly birefringent area-metric closure** framework of Schneider, Schüller, Stritzelberger & Wolz. The question is no longer "can classical GR alone do it?" but whether a more general constitutive geometry with weak vacuum birefringence could absorb/tame the transport structure while staying locally hyperbolic — i.e. an exploratory embedding/screening study, not a conventional warp solution.

**Technical content.** A naive rank-one uniaxial constitutive deformation **fails** as a screening mechanism; the smallest successful "container" within the reduced ansatz is a symmetric meridional 3×3 bivector block whose image occupies **six** weakly birefringent variables in the Schneider–Schüller–Stritzelberger–Wolz parametrization. Coupling that reduced model to the exact irrotational background and integrating at representative angles θ = 0, π/4, π/2: the coupled **θ = π/4** case behaves approximately cubically only for mild velocities (v ≲ 1), departs strongly at higher velocity, and even **changes sign** in one variable between v = 2 and v = 3; the θ = π/2 benchmark tracks the decoupled cubic law. Rodal hedges carefully: the evidence **disfavors fast walls** within the reduced perturbative model, smaller subluminal velocities look less strained, and the result is explicitly **not** a theorem-level existence proof or no-go.

**How strong is it?** Moderate at best, strictly conditional: a preprint, limited to a reduced six-variable perturbative ansatz, inheriting the interpretive burden of the area-metric/weak-birefringence framework. Its main value is as **trajectory evidence** — Rodal's newest move is not to declare victory over exotic matter but to ask whether his best classical background can be embedded in a richer constitutive structure that screens its remaining bad features. The program is shifting from *"find a less exotic metric"* toward *"can the remaining obstruction be screened by a broader effective geometry?"*

## 2. "A Machian wave effect in conformal, scalar–tensor gravitational theory" (Dec 2025) — the Mach-effect verdict

**What it tests.** The Woodward Mach-effect thruster rests on a transient rest-mass fluctuation whose leading term is **∝ ∂²ₜM(t)**, claimed (via Sciama's relational inertia) to be amplified by an order-unity cosmic potential Φ/c² ~ −1 — roughly 10¹¹× larger than naïve E = mc² bookkeeping — then rectified against synchronized actuation to yield steady thrust. Rodal asks, covariantly: does any honest field-theoretic rewriting actually contain a usable source ∝ ∂²ₜM at leading order for laboratory driving?

**Two frameworks.**
- *Einstein gravity (Landau–Lifshitz form).* Using 𝔥^{μν} = √(−g)g^{μν} − η^{μν} in harmonic gauge, the ∂²ₜM-type term appears inside the nonlinear source Λ^{μν} ⊃ −(𝔥⁰⁰/c²)∂²ₜ𝔥^{μν}. Key point: **this is not an independent matter source** — it is the quadratic remainder from expanding the *curved* d'Alembertian about flat space. Restoring it to the left-hand side simply rebuilds the genuine principal part of the harmonic Einstein operator. It is bookkeeping, suppressed by **~(U_N/c²)(ωL/c)² ≪ 1**, where U_N/c² is the *local* device potential (~10⁻²⁵ for a lab apparatus, **not** the cosmic Φ) and (ωL/c)² is the near-zone retardation factor.
- *Hoyle–Narlikar conformal scalar–tensor gravity* (a covariant realization of Mach's principle). The inertial-mass scalar obeys ∇²m + (R/6)m = λN, sourced by conserved **particle-number (baryon) density** N; for a localized lab source it responds Poisson-like (instantaneous near-field), with no resonant cosmological enhancement.

**The decisive result.** **Baryon-number conservation fixes the scalar charge, so the rest-mass monopole cannot oscillate** — a radiating (time-varying) monopole is forbidden for number-conserving matter. Any residual radiating monopole can come only from *nonconservative internal-energy* variation (thermal/binding), doubly suppressed by E_int/(Mc²) and by M_device/M_Hubble. The Sciama potential therefore enters covariant HN **as a suppressing ratio, not an order-unity amplifier.** Rodal labels Woodward's amplification a **"variable-constant fallacy"** — treating ϕ as the constant c² when convenient and as a dynamical field when convenient — and flags a non-covariant shortcut in Fearn's HN derivation.

**Why it carries weight.** Rodal authored the most detailed MET dynamical model (the 2019 GRG >200-term piezo-stack electroelasticity system), and Woodward published a formal "reply to Rodal" (2020). This is a **negative verdict from a long-standing insider/interlocutor**, corroborating the experimental record (Tajmar/TU Dresden's 2021 nulls attributing MET "thrust" to thermal/vibration artifacts), and it strengthens/modernizes his own 2019 conclusion that the effect is too small for practical travel "unless one were near a neutron star or black hole." **Caveat Rodal himself draws:** he does *not* claim the term is absent — it exists as a high-order post-Newtonian effect — and bounds his conclusion to weak-field, near-zone lab conditions, noting a regime (ωL/c → 1) where the hierarchy could differ.

**Verdict tier:** rigorous, mainstream-consistent, and effectively closes the theoretical case for practical Mach-effect thrust under ordinary conditions.

## 3. "A warp drive with predominantly positive invariant energy density and global Hawking–Ellis Type I" (*GRG* 2026) — the flagship

**Construction.** A standard 3+1 ADM line element with **unit lapse (α ≡ 1)** and **flat, static spatial slices** (γ_ij = δ_ij). The defining move is making the shift vector **kinematically irrotational** (vorticity 2-form ω = dβ♭ = 0), which on simply-connected slices forces **potential flow**, β♭ = −dΦ. He uses an axisymmetric ansatz with form function **f(r) = 1 − f_Alcubierre(r)** (the Natário "rest-at-center" complement) and derives a genuinely **closed-form** transverse profile g(r) from sinh/cosh/log terms, with scalar potential Φ = v(t)·r·g(r)·cosθ. The pivotal choice: he **keeps curl β = 0 but does *not* also impose Natário's div β = 0** — requiring both would force a harmonic potential that cannot localize a bubble, so relaxing divergence-free enlarges the design space and lowers the negative-energy magnitudes.

**Why it is globally Type I (the core theorem).** With α = 1 and flat static slices, the extrinsic curvature is the spatial Hessian of Φ and the momentum constraint G₀î vanishes *identically* (covariant derivatives commute on a flat slice). The Einstein tensor then block-diagonalizes into a real symmetric spatial block plus a real **timelike** eigenvalue with a timelike eigenvector — the definition of Hawking–Ellis **Type I** — giving a **frame-invariant proper energy density defined everywhere**. By contrast, Alcubierre and Natário contain **Type IV** regions (complex-conjugate eigenvalue pairs, no rest frame, *automatic* NEC violation). This operationalizes Santiago–Schuster–Visser's existence-level Type-I observation into an explicit geometry.

**What's genuinely new (two things).** (1) Santiago et al. had the *algebraic mechanism* but no concrete explicit continuous analytic construction of this sort; **Rodal supplies that construction.** (2) He turns vorticity into a causal/mechanistic comparison via a **"fixed-smoothing vortical ablation"**: add modest vorticity while holding the smoothing profile fixed, and the positive/negative energy balance worsens sharply — a stronger argument than comparing differently-shaped named metrics. If the ablation holds up, **vorticity itself** (not ad hoc profile tuning) is the main source of the improvement.

**Quantitative results (verified; correcting earlier loose figures).** Peak proper-energy *deficit* is **~38× smaller than Alcubierre** and **~2.6×10³ smaller than Natário**; separately, peak **NEC violation is >60× smaller than Natário** (two different metrics — don't conflate them). A far-field tail extrapolation gives net proper energy **|E₊ − E₋|/(E₊ + E₋) ≈ 0.04%** — consistent with zero to four decimals — but this is a near-perfect **cancellation** of E₋ ≈ 1.3×10⁴⁴ J against a comparable E₊, *not* an absence of negative energy. The controlled vortical ablation (reintroducing curl via a parameter η) makes E₋ grow **>500×**, establishing the gain is *causally* due to curl-free kinematics. Methods: a Cartan-tetrad pipeline with 50-digit-precision eigenanalysis and explicit tolerances.

**What it does *not* solve (Rodal is explicit).** (i) **Foliation-dependent** — the global energy integrals are slice quantities, invariant under spatial coordinate/tetrad changes but not under reslicing. (ii) Global Type I rests on α ≡ 1 *and static slices*; a live, accelerating v(t) bubble breaks the static-slice assumption, so **the acceleration phase is not covered** by the theorem. (iii) **WEC is still violated locally** (proper density dips negative near the equator) — "predominantly positive" is literal. (iv) **Superluminal travel is unsolved** (numerics restricted to v = c; superluminal bubbles generically have Cauchy horizons). (v) It is a **reverse-engineered metric** — no physical matter source or actuator is proposed. (vi) Irrotationality is *sufficient, not necessary* for Type I.

**Net:** a genuine, careful advance in the *character and localization* of the exotic matter — the cleanest (globally Type I), best-behaved warp geometry to date — that nonetheless leaves the three real obstructions (acceleration, superluminal/Cauchy horizons, matter source) untouched and still needs ~10⁴⁴ J of negative energy that merely cancels in the integral. Early attention is modest but real: at time of crawl the Springer article page showed **101 accesses and 5 Altmetric mentions**, and the metric was promptly benchmarked independently (see `warpax`, below).

## 4. "On the Infeasibility of Low-Energy Warp Drive via Metamaterial Gravitational Coupling" (Jul 2025)

A sharp **veto paper** (not a new solution) against "low-energy" warp proposals (associated with Sarfatti/Taylor) that replace the constant gravitational coupling κ₀ with a spatially varying κ(x) engineered via a metamaterial's EM response. The scheme fails either before or immediately after it is made respectable:

- **Non-dynamical version:** a prescribed κ(x) in G^{μν} = κ(x)T^{μν} clashes with the contracted **Bianchi identity** ∇_μG^{μν} ≡ 0 (geometric, non-negotiable), forcing ∇_μT^{μν} ≠ 0 — i.e. violating local stress-energy conservation.
- **Dynamical completion:** κ becomes a scalar field and the theory degenerates into **scalar–tensor gravity** with a new long-range scalar force, strongly constrained by experiment.

The experimental side is orthodox and strong: Solar-System and pulsar-timing bounds restrict **|γ − 1| ≲ 10⁻⁵**; any sharp interface where κ changes produces a **delta-function stress-energy layer** (junction-condition analysis), while even steep-but-continuous profiles are constrained by **torsion-balance tests, lunar-laser ranging, and spacecraft Doppler** data. Punch line: make the trick GR-consistent and you hit scalar-tensor bounds; don't, and you break local conservation. Together with the Mach-effect paper, this forms the **"loophole-closure" branch** of his program. (This is the paper cited elsewhere as the "Bianchi identity" objection to metamaterial-G schemes — it is Rodal's.)

## 5. "A Closer Look at Natário's Zero-Expansion Warp Drive" (*IJTP* 2024) — the diagnostic predecessor

An invariants-based 3+1 analysis of Natário's div β = 0 drive that sets up the 2026 construction. Four results: (1) supplies the previously-undetermined **Petrov classification** (**type I**; and it is **not** a Class-B warped product, contrary to some literature); (2) shows the **Weyl** curvature is significant because the form function is sharply wall-localized (prior work tracked only Ricci/T_μν); (3) argues **momentum density**, not volume expansion/contraction, sets the drive's trajectory (pushing back on the "front/back expansion-contraction" shorthand); (4) **rebuts the claim that Natário is "more realistic" than Alcubierre** — at identical parameters its curvature-invariant amplitudes are **~35× larger**, and it flags Mattingly et al. for underestimating these by **~21 orders of magnitude**. The methodological lesson — use invariant curvature/eigenstructure, and div β = 0 *worsens* rather than tames the geometry — is exactly the premise the 2026 paper acts on by switching from **divergence-free to curl-free**.

## 6. "Visualization and analysis of the curvature invariants in the Alcubierre warp-drive spacetime" (*GRG* 2023) — the foundation

The earliest in-window work and the root of the program — **diagnostic, not constructive.** It studies the Weyl-derived scalar I, the Ricci trace R, and the quadratic/cubic trace-adjusted Ricci invariants r₁, r₂, mapping how these scalars describe the bubble wall, and analyzes the Kretschmann decomposition. Signature claims: the Alcubierre bubble requires **four distinct layers of anisotropic stress-energy**; earlier visualizations (esp. Mattingly et al.) **under-represented curvature by 8–16 orders of magnitude**; the bubble-wall curvature is benchmarked against a **Saturn-mass Schwarzschild black hole** (an intentionally dramatic but invariantly grounded scale); and Alcubierre spacetime is **not** a Class-B warped product. This established Rodal's signature method — coordinate-invariant curvature analysis and direct Einstein-tensor interpretation over observer-dependent quantities — which carries forward almost mechanically into the 2024 Natário paper and, more ambitiously, the 2026 irrotational Type-I construction.

---

## Field positioning & reception

**He minimizes within the no-go theorems; he does not claim to evade them.** Rodal's own abstract describes "predominantly positive" energy density with "significantly reduced" (not eliminated) NEC/WEC stress, and net energy "consistent with zero to four decimal places." This is squarely the *minimization* program around **Santiago–Schuster–Visser** ("Generic warp drives violate the NEC," PRD 2022, arXiv:2105.03079) and the **Schuster–Santiago–Visser** ADM-mass follow-up (explicit generic Natário-class examples violating the energy conditions). The 2026 **Lyon** group broadens the critique: **Barzegar–Buchert–Vigneron** ("demystification") argue most "physical warp drive" claims need reassessment for missing dynamical/covariant ingredients, and **Buchert–Frackowiak** add an instability result for one later realization. (Keep the references straight: "Generic warp drives violate the NEC" = arXiv:2105.03079; the Lyon classification/no-go is the *separate* arXiv:2602.16495.)

**Independent verification — `warpax` — confirms the headline *and* sharpens the caveat.** An T. Le's observer-robust, autodiff-based energy-condition toolkit (arXiv:2602.18023) implemented and stress-tested the Rodal metric against Alcubierre, Lentz, Van Den Broeck and Natário. It **confirms the Rodal metric is the unique, 100% Hawking–Ellis Type I** case in the suite (no Type II/IV points), and identifies **vorticity of the ADM shift** — not zero expansion — as the control parameter separating it from the Type IV bubble walls of the others.

> ⚠️ **Statistic corrected.** A circulating figure that single-frame analysis "misses ~72% of WEC violations" **does not appear in the paper** (it was repeated in one of the source reports). The verified `warpax` numbers: under boosted-observer optimization, a standard single-frame (Eulerian) analysis misses violations at **>28% of grid points for the DEC and >15% for the WEC**, with total violated fractions ~**87%** (NEC/WEC/SEC) and **99.9%** (DEC). The takeaway is the important part: being globally Type I means the violations are **algebraically exact and certified**, *not* small — under all-observer optimization the Rodal metric shows the **largest hidden-violation gap** in the set even as it is the **mildest** violator by the chosen invariant ranking (~70× less exotic than the bubble-wall drives). Every analyzed drive violates the averaged NEC as tested.

So `warpax` validates Rodal's best structural insight (global Type I; vorticity as the control parameter) while simultaneously invalidating any temptation to oversell the metric as energy-condition-clean. **Right interpretation: best-in-class reduction of exoticity inside a narrow classical warp class, not a refutation of the no-go theorems.** Engagement is real but early — `warpax`'s reproduction is the strongest uptake; the Lyon no-go papers are the surrounding literature his construction must answer; popular coverage (Popular Mechanics / Yahoo "loophole" pieces) is visibility, not citation. Formal citation counts remain near zero given the Dec-2025/2026 timeline.

---

## Trajectory & open questions

**The arc is unusually coherent:** 2023 (diagnose Alcubierre's curvature honestly) → 2024 (show Natário's div β = 0 is *worse*, not better) → 2026 (construct the curl β = 0, globally-Type-I alternative) → 2026 (ask whether the residual obstruction can be *screened* in a broader weakly-birefringent constitutive geometry) — a steady search for the least-pathological warp geometry by invariant criteria. In parallel, on the inertial-propulsion side he moves the opposite way — from earlier Machian exploration to a blunt verdict that realistic Mach-effect thrust is negligible. The unifying theme is not optimism; it is a search for which structures are **mathematically admissible** versus merely wishful reinterpretations.

**Open questions / what to watch.**
1. Does a *dynamical* (accelerating) irrotational bubble retain any Type-I benefit, or does G₀î ≠ 0 destroy it? (This is the acceleration phase his own caveats flag, where exotic matter is expected to reassert itself.)
2. Can the global E₋ ≈ 10⁴⁴ J cancellation be made physically meaningful, or is it a coordinate artifact of the foliation?
3. Will the Lyon no-go theorems (obstructions "beyond energy conditions") subsume his construction?
4. Does his Mach-effect verdict draw a published response from the Woodward/Fearn/SSI side, as his 2019 work did?
5. The deeper physics question has shifted from *"can one reduce the violations?"* (yes) to *"is there any mathematically clean route left to **eliminating** them without abandoning the current GR warp-drive framework?"*

**Confidence.** *High* on the bibliography (dates, venues, DOIs/arXiv IDs, peer-review status of the six works) and on the technical content of the 2023, 2024, 2025-metamaterial, 2025-Machian, and 2026 irrotational-Type-I papers — all directly recoverable from journal metadata, arXiv abstracts, and INSPIRE/ADS, and corroborated by the `warpax` reproduction. *High* that he does not claim to evade the no-go theorems. *Medium* only on fine-grained interpretation of the **2026 weakly-birefringent preprint**, which has a stable abstract but no comparably stable browser-parsed full text, so it is analyzed at the abstract/programmatic level. The earlier characterization "survives independent verification" should be read precisely: the *classification* (global Type I) survives, but the metric remains energy-condition-violating under boosted observers — by the widest margin in the test set.

---

## Sources

- Weakly birefringent screening (warp), arXiv:2603.21352 — https://arxiv.org/abs/2603.21352
- A Machian wave effect in conformal scalar–tensor gravity (Mach-effect verdict), arXiv:2512.22687 — https://arxiv.org/abs/2512.22687
- Warp drive, global Hawking–Ellis Type I (GRG 2026), arXiv:2512.18008 · DOI 10.1007/s10714-025-03495-x — https://arxiv.org/abs/2512.18008 · https://doi.org/10.1007/s10714-025-03495-x
- Infeasibility of low-energy / metamaterial warp, arXiv:2507.09724 — https://arxiv.org/abs/2507.09724
- A Closer Look at Natário's Zero-Expansion Warp Drive (IJTP 2024), DOI 10.1007/s10773-024-05700-0 · arXiv:2512.19837 — https://doi.org/10.1007/s10773-024-05700-0 · https://arxiv.org/abs/2512.19837
- Curvature invariants in Alcubierre (GRG 2023), DOI 10.1007/s10714-023-03182-9 · arXiv:2512.20738 — https://doi.org/10.1007/s10714-023-03182-9 · https://ui.adsabs.harvard.edu/abs/2023GReGr..55..134R/abstract
- Santiago–Schuster–Visser, generic warp drives violate the NEC (PRD 2022), arXiv:2105.03079 — https://arxiv.org/abs/2105.03079
- Lyon no-go / classification (2026), arXiv:2602.16495 — https://arxiv.org/abs/2602.16495
- `warpax` observer-robust energy-condition verification (2026), arXiv:2602.18023 · code — https://arxiv.org/abs/2602.18023 · https://github.com/anindex/warpax
- Background: 2019 GRG Mach-effect electroelasticity model — https://www.researchgate.net/publication/333107400
- Background: NASA NIAC MEGA-drive (Woodward/Fearn, Rodal team) — https://ntrs.nasa.gov/citations/20190000915
