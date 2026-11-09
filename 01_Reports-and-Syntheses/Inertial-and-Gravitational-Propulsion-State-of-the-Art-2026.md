# Inertial & Gravitational-Manipulation Propulsion: State of the Art

**Scope:** the propulsion *mechanism* only — how thrust could be produced without expelling reaction mass, by manipulating inertia or gravity/spacetime. Energy supply is deliberately ignored (assume sufficient power exists). Engineering-oriented: the goal is to identify what, if anything, is a buildable/testable target and what the make-or-break experiment is.

**Date:** June 2026. Prioritizes work through 2025–2026.

**Method:** five parallel literature reviews (warp/metric, Mach-effect, quantized inertia + EmDrive, mechanical drives, patents/defense), then adversarial verification of the load-bearing recent claims against primary sources.

---

## Bottom line up front

The honest state of the art is that **no proposed mechanism for inertial or gravitational propulsion has been physically demonstrated and independently replicated.** Every candidate falls into one of four bins: (1) *forbidden by a proven theorem* (mechanical "reactionless" drives), (2) *requires exotic matter that is a theorem-level dead end* (superluminal/accelerating warp drives), (3) *not forbidden in principle but experimentally debunked as measurement artifacts* (EmDrive; the Woodward Mach-effect thruster as tested), or (4) *not forbidden, but unconfirmed and resting on non-standard physics* (quantized inertia; inertia-modification generally).

If you accept the premise that *some* advanced mechanism must exist and ask where the least-dead engineering target is, the answer is narrow and specific:

> **The only family with a logically valid route to propellantless thrust that does not break a proven conservation law is inertia/gravity manipulation treated as an *open* system — one that exchanges momentum with the gravitational field, distant matter, or the quantum vacuum.** That is the conceptual space occupied by Mach-effect thrusters, quantized inertia, and gravitomagnetic coupling. It is not theorem-forbidden; it is merely *unproven*, and the best independent tests so far are null.

So the single most decision-relevant question underneath this entire topic is not about any device. It is: **what is the origin of inertia, and can it be modified by local means?** Everything buildable hinges on that. The critical experiment is correspondingly concrete (see §7).

The user's working hypothesis — that *negative-energy / exotic-matter approaches are probably a dead end* — is **correct for the useful regime**, and that conclusion is now a theorem reinforced by 2025–2026 work, not an opinion (see §6).

---

## 1. The organizing principle: which approaches are even allowed

Engineering judgment here starts with one filter, because it eliminates most of the field before any experiment.

**Conservation of linear momentum** (which, by Noether's theorem, follows necessarily from the homogeneity of space) says: *no closed system can accelerate its own center of mass using internal forces alone.* Internal forces cancel in equal-and-opposite pairs; the center of mass keeps its velocity no matter what the internal parts do. To change it you must throw mass out the back, or push on something external — a field or a medium.

This gives a hard sort:

- **Mechanical oscillating/rotating-mass "inertial drives"** (Dean drive, gyroscopic "antigravity," inertioids) are *closed systems*. They are forbidden — perpetual-motion-class, not engineering challenges. (Tier: **Forbidden**.)
- **RF-cavity drives** (EmDrive) claim closed-system thrust from internal microwaves. Same prohibition unless they secretly expel photons (negligible) or are mis-measuring. (Tier: **Debunked**.)
- **Field-based schemes** (Mach-effect, quantized inertia, gravitomagnetic, metric engineering) try to be *open* systems: momentum is exchanged with the gravitational field / distant matter / spacetime itself. This is a **genuine, logically sound loophole** — global conservation is preserved even with no propellant. The catch is that the loophole is only real if the claimed inertia/gravity coupling *exists at a usable magnitude*, and that is exactly what is unproven.

Keep this distinction front of mind: a mechanical drive has *no* loophole and is impossible; a field-based drive has a *valid* loophole and is merely unconfirmed. They are not the same kind of claim, even though both are routinely lumped together as "reactionless."

---

## 2. Metric engineering / warp drives (gravity manipulation)

**Principle.** Don't move *through* space; move space itself. The Alcubierre (1994) metric contracts spacetime ahead of a flat "bubble" and expands it behind; the passenger rides a geodesic (weightless, no felt acceleration). Natário's (2001) variant does it with zero expansion (pure "slipping").

**Conservation / energy-condition status.** The Einstein equations run backward here: you specify the geometry you want, then read off the matter needed to source it — and it comes out **negative.** Both Alcubierre and Natário require negative energy density and violate the weak, null, strong, and dominant energy conditions. This is a property of the bubble *geometry*, not of any single ansatz.

**Theoretical maturity.** Very high — this is rigorous, mainstream general relativity, 30 years deep. That maturity is what makes the negative verdict trustworthy.

**Experimental status / best "thrust."** None. There is no laboratory effect of any kind. It is pure theory.

**The two killers (established):**
- *Magnitude.* Original parameters need negative energy of order ~10× the mass-energy of the observable universe (Pfenning–Ford). Van Den Broeck's "neck" trick cut the total to roughly a solar/Jupiter mass, later to vehicle-scale — but it stays negative and exotic.
- *Quantum inequalities.* QFT permits negative energy only in tiny amounts for short times (Ford–Roman). That forces the bubble wall to be ~hundreds of Planck lengths thick with negative energy persisting ~10⁻³³ s — fatal for anything macroscopic.

**The 2021 "positive-energy" wave and its refutation.** Lentz, Bobrick–Martire, and Fell–Heisenberg each claimed positive-energy solitons. **Santiago, Schuster & Visser (2021/22, PRD)** showed the "positive energy" was an artifact of checking only one family of observers; the weak energy condition requires *every* timelike observer to see positive density, and **all physically reasonable warp drives violate the null energy condition** — hence WEC/SEC/DEC too. Lentz's plasma version was independently falsified again in late 2025 (negative density present even in the natural frame, plus derivation errors).

**The one genuine 2024 advance — and why it doesn't help.** The Applied Physics group (Fuchs, Helmerich, Bobrick, Sellers, Melcher, Martire) published a *constant-velocity, strictly subluminal* "physical warp drive" that satisfies **all** energy conditions — by wrapping the warp inside a heavy shell of ordinary positive-mass matter moving inertially. It is real, peer-reviewed (Class. Quantum Grav. 41:095013), and important conceptually. But Bobrick & Martire's own framing gives the propulsion verdict: *"any warp drive… is a shell of regular or exotic material moving inertially… therefore, any warp drive requires propulsion."* It is **not a thruster.** It cannot accelerate itself and cannot exceed light speed; it is a massive object that still needs a conventional rocket to get moving.

**2026 reinforcement.** Buchert & Vigneron (Feb 2026, arXiv:2602.16495) prove **new no-go theorems** and conclude that most "physical warp drive" claims fail when GR is applied correctly — and notably that the obstacles run **deeper than energy-condition violation alone.**

**Gravitomagnetism / frame-dragging (the "real physics" cousin).** GR genuinely predicts that moving/rotating mass drags spacetime (gravitomagnetism), and this is *measured* — Gravity Probe B (2011) and LAGEOS/LARES confirmed it. But for laboratory masses the effect is ~10⁻²¹ of ordinary gravity: real, and uselessly weak as thrust. Tajmar's 2006–07 spinning-superconductor claim of an anomaly ~10²⁰× larger was **never independently replicated** and is best explained by gyroscope systematics.

**Most decisive open question.** Whether the subluminal, energy-condition-satisfying solution can be made to *accelerate* without re-introducing negative energy at the wall — the unsolved acceleration phase is exactly where the no-go results predict exotic matter must reappear. This is theoretical; no experiment is decisive.

**Tier:** **Theoretically forbidden for the useful (FTL/self-accelerating) regime.** Real GR, but a dead end as propulsion with known matter.

---

## 3. Mach-effect / Woodward thruster (inertia modification)

**Principle.** James Woodward's "transient mass fluctuation": any object whose internal energy changes *while* it is being accelerated should experience a tiny oscillating change in rest mass. Drive a pre-stressed PZT piezoelectric stack at acoustic resonance and phase a second actuation so the stack pushes while momentarily heavier and pulls while lighter — the time average is a steady, propellantless thrust.

**Conservation status.** Open-system by design: momentum is claimed to flow to distant matter / the gravitational field via Mach's principle, using Sciama's inertial induction and Hoyle–Narlikar gravity (instantaneous "advanced" interaction with the rest of the universe). The loophole is logically coherent **but requires non-standard physics** (Hoyle–Narlikar conformal gravity, action-at-a-distance) that mainstream GR does not endorse.

**Theoretical maturity.** Developed over ~30 years, with a specific quantitative claim (a Sciama/linearized-GR amplification making the mass wobble up to ~11 orders larger than a naive E=mc² estimate). But the amplification is disputed and the theory is not mainstream-accepted.

**Experimental status / best thrust.** Woodward's own torsion-balance devices showed sub-µN to a few-µN signals for decades; a 2019 mount redesign reportedly jumped to >100 µN (no published independent error bars). Supported by two NASA NIAC grants (Phase I 2017, Phase II 2018, led by Heidi Fearn) — but NIAC funds *concept studies*, not validation, and never confirmed a propulsive effect.

**Independent replication — the decisive evidence.** Martin Tajmar's group (TU Dresden, "SpaceDrive," vacuum, EM-shielded, peer-reviewed) found the signals consistent with **thermal expansion, mounting vibration, and EM effects — not thrust.** The tell: an old Woodward device's ~0.4 µN signal **did not reverse when the device was rotated 180°**, the signature of an artifact rather than a real force; and the apparent effect *shrank* as balance sensitivity improved.

**2025 — undercut from inside.** José Rodal, a former NIAC MEGA team member, posted a covariant analysis (Dec 2025, arXiv:2512.22687) concluding that baryon conservation fixes the scalar charge so the rest-mass monopole *cannot* oscillate, that the effect is not cosmologically amplified, and that "any Mach-effect thrust is far too small for practical propulsion." James Woodward died in August 2025; the work continues at a smaller scale under Fearn / Space Studies Institute.

**Most decisive experiment.** Operate a live, resonating thruster on a high-resolution vacuum balance and reverse its orientation (180° / inverted / null mount). A real propellantless force must flip sign with orientation; an artifact won't. Tajmar effectively ran this with a negative result; the only remaining gap is subjecting the specific 2019 >100 µN device to the same protocol in an independent lab.

**Tier:** **Unconfirmed, trending debunked** — empirically attributable to artifacts and now theoretically challenged from within its own camp. *But* it remains the most-studied embodiment of the one idea that isn't theorem-forbidden (local inertia modification), which is why it stays on the board at all.

---

## 4. Quantized inertia (QI / MiHsC)

**Principle.** Mike McCulloch's theory derives *inertia itself* from Unruh radiation (the thermal bath an accelerating body should see) subject to a Hubble-scale Casimir-like horizon. Reduce the Unruh wavelengths that "fit" in one direction — with a metamaterial, a temperature gradient, or EM fields — and you create an asymmetry in inertia that yields net thrust: a "horizon drive."

**Conservation status.** Open-system (momentum exchanged with the cosmological horizon / vacuum). Like Mach-effect, not theorem-forbidden — but it rests on **Unruh radiation, which has never been directly observed**, and on non-standard assumptions about inertia.

**Theoretical maturity.** It is an actual predictive theory, not an ad-hoc device claim — that is its distinguishing strength. Its strongest evidence is *astrophysical*: it reproduces galaxy rotation curves with no dark matter and no free parameters, and a 2024 MNRAS Letters paper claims it binds Proxima Centauri using visible matter alone. But Renda (MNRAS 2019) identified two flaws in QI's core derivation (an internal inconsistency in the force law) that remain unresolved.

**Experimental status / best thrust.** QI received a **~$1.3M DARPA grant (2018, "Nanowave"/quantised-inertia program)** funding asymmetric-cavity, capacitor, heated-wire, and laser-asymmetry tests. Tajmar's targeted tests of QI's specific predictions (asymmetric resonators, reflective cavities, fiber loops) returned **null at the nanonewton level.** The 2023-launched IVO "Quantum Drive" cubesat (Barry-1) was meant to be the first orbital test, but the host satellite suffered power-bus failures and **contact was lost in February 2024 before the drive was ever operated.** Later (late-2025) claims of "significantly slowed orbital decay" come from advocacy-leaning outlets, show no clean orbit-*raising*, and are confounded by atmospheric-density and ballistic-coefficient differences — inconclusive at best. McCulloch has reportedly pivoted to a precision ground test (talks with the UK National Physical Laboratory, 2026).

**Most decisive experiment.** A clean, independently replicated, confound-controlled **static thrust / levitation measurement on a world-class metrology balance.** QI's advantage as a test subject is that it predicts a *static* propellantless force (unlike Mach-effect's oscillatory signal), so a confirmed levitation — with thermal, EM, and buoyancy confounds excluded and replicated by an independent lab — would be unambiguous either way.

**Tier:** **Unconfirmed / fringe**, but the *least-dead of the genuinely novel options* — it is falsifiable, makes a static prediction, and carries independent astrophysical motivation. Propulsion claims are unproven; ground tests are null; the astrophysics is contested but not dismissed.

---

## 5. EmDrive and other RF-cavity / electrostatic "reactionless" drives

**Principle.** Roger Shawyer's EmDrive: bounce microwaves inside a tapered resonant cavity and claim a net axial thrust from the radiation-pressure asymmetry, with no exhaust.

**Conservation status.** Closed-system → **forbidden** unless it expels something (the photon recoil is many orders too small) or is mis-measuring. There is no valid mechanism.

**Experimental status.** NASA Eagleworks (White, March et al., 2016) reported ~1.2 mN/kW in a peer-reviewed paper — heavily criticized for not ruling out thermal artifacts. **Definitive null:** Tajmar / TU Dresden (2018–2021) reproduced the Eagleworks setup and showed the "thrust" was a **thermal-expansion artifact of the balance mount plus a Lorentz-force interaction between unshielded power cables and Earth's magnetic field** — they could manufacture the NASA-magnitude signal and then make it vanish by moving the suspension point. Their verdict: the data "refute all EmDrive claims by at least three orders of magnitude." Chinese (NWPU) results were retracted on the same Earth-field error.

**Adjacent claims.** Buhler/Exodus Propulsion's electrostatic "1 g" drive (conference talks, 2023–) has no peer-reviewed data, no replication, no space demo, and would violate momentum conservation — fringe.

**Most decisive experiment.** Already done (Tajmar). The book is effectively closed.

**Tier:** **Debunked.**

---

## 6. Mechanical inertial / gyroscopic drives — and the verdict on exotic matter

**Mechanical drives (the hard floor).** Dean drive, Laithwaite's gyroscopes, inertioids, and the endless inventor/"YouTube" devices all fail for the same theorem-level reason in §1. They *appear* to work via friction/"stick-slip" ratcheting against the ground (the ground is the reaction mass), torque misread as linear force, base-tilt, vibration-stiction, or thermal warping of the test stand. On a properly isolated stand — air bearing, torsion pendulum, or free fall — the thrust vanishes. The cleanest demonstration: in free fall the center of mass follows the geodesic unchanged whether the device is powered or not. Eric Laithwaite himself eventually conceded "the mathematics said there were no forces and that was correct." The 2024 peer-reviewed review (Provatidis, *Eng*) confirms the impulse integrates to zero per cycle: no net thrust, none ever. **Tier: Forbidden.**

**The exotic-matter "dead end" — verdict.** You asked me to test whether negative energy / exotic matter is truly a dead end. It is, for anything useful:

- *Superluminal or self-accelerating warp:* exotic matter is **required as a theorem**, not as an engineering gap (Santiago–Schuster–Visser 2022; reinforced by Buchert–Vigneron 2026). Quantum inequalities then make even the required negative energy un-assemblable at macroscopic scale. **Genuine dead end.**
- *Subluminal "physical" warp (2024):* you *can* avoid exotic matter — but the result is a heavy ordinary-matter shell that provides **no propulsion** and still needs a conventional engine. You gain nothing a rocket doesn't already give you.
- *Negative energy does exist* (the Casimir effect is real), but only in tiny, transient amounts bounded by quantum inequalities — nowhere near enough, and not in a form you can pile up into a warp wall.

So: gravity-metric engineering is real, beautiful physics and a **dead end as a propulsion mechanism** with known matter. Your instinct was right. The action, if there is any, is in *inertia* manipulation, not spacetime-metric manipulation.

---

## 7. Comparison table

Scores 0–5 (5 = strongest). "Buildability" = how close this is to a thing an engineer could construct and have work, *assuming energy is free*.

| Mechanism | Physical plausibility | Theoretical maturity | Experimental support | Independent replication | Buildability | Overall tier |
|---|:--:|:--:|:--:|:--:|:--:|---|
| Mechanical inertial / gyroscopic | 0 | 0 | 0 (all artifacts) | Negative | 0 | **Forbidden** |
| EmDrive / RF cavity | 0.5 | 0 | 0 (debunked) | Negative (null) | 0 | **Debunked** |
| Warp / metric — superluminal | 1 | 4 | 0 (pure theory) | N/A | 0 (needs exotic matter) | **Forbidden (useful regime)** |
| Warp / metric — subluminal "physical" (2024) | 4 (as math) | 4 | 0 | N/A | 0 (no thrust mechanism) | **Real result, not propulsion** |
| Gravitomagnetic / frame-dragging | 5 (effect is real) | 5 | Astro-confirmed; lab-propulsion 0 | Tajmar amplification not replicated | 0.5 (magnitude ~10⁻²¹) | **Real physics, negligible** |
| Mach-effect / Woodward | 1.5 | 2 | 1 (sub-µN, at noise) | 0 (Tajmar null, artifact) | 1 | **Unconfirmed → debunked** |
| Quantized inertia (QI) | 1.5 | 2 | 1 (null ground; astro card) | 0 (no confirmed thrust) | 1 | **Unconfirmed / fringe (least-dead novel)** |
| Pais / Navy patents | 0.5 | 0 | 0 ("could not be proven") | 0 | 0 | **Unproven / pseudoscience** |

---

## 8. Patents and defense programs — a reality check

Because these come up constantly in this topic, the cross-cutting finding is worth stating plainly: **no defense or patent effort has produced a demonstrated, replicated effect.**

- **Salvatore Pais / US Navy patents** ("Craft using an inertial mass reduction device," US 10,144,532 B2; "High-frequency gravitational wave generator"; the "Pais effect"). The Navy *tested* this under the HEEMFG program (2016–2019, ~$508K, ~1,600 staff-hours) and concluded the effect **"could not be proven."** No prototype, no transition. The flagship patent **expired in January 2023** for non-payment; others lapsed. The "operable" language was an assertion to a patent examiner (granted after NAWCAD's CTO argued China might develop similar tech), **not** an experimental result. Physicists consulted over two years called it pathological science with no basis in reality.
- **DIA / AAWSAP "Defense Intelligence Reference Documents"** (~38 papers, ~2008–2010), including Eric Davis's warp-drive and wormhole papers and Hal Puthoff's metric-engineering review, are **theoretical literature surveys — Phase I "review the latest concepts" — not hardware.** They demonstrated nothing.
- **NASA Breakthrough Propulsion Physics** (Millis, 1996–2002, ~$1.2M) is the most methodical effort and the most useful precedent. It assessed ~14 concepts, *experimentally* tested several mass/gravity-coupling claims (Schlicher thruster, Podkletnov gravity-shielding, Woodward's effect) and found **nothing** — no breakthrough achievable with current physics. It correctly identified the real obstacles: coupling propulsion to inertia/gravity, conservation-law compliance, and energy. Its conclusions are the honest template for this whole field.

The pattern is uniform: patents filed, mainstream journals declining, no working prototype, government testing returning null.

---

## 9. Engineering synthesis: the least-implausible path and the critical experiment

Given the mechanism-only framing and the premise that *some* advanced inertial/gravitational mechanism could exist, the engineering recommendation is:

**Don't chase a device. Chase the physics question that gates every device: is inertia locally manipulable?**

The reasoning is a process of elimination:
- Mechanical and closed-cavity drives are *forbidden* — abandon entirely.
- Metric/warp engineering is *real GR but a dead end* as propulsion with known matter — interesting for theory, useless to build.
- Gravitomagnetism is *real but ~10⁻²¹ too weak* — only relevant if some unknown amplification exists (no evidence).
- That leaves **inertia modification** (Mach-effect, QI, and any successor) as the *only* family that is simultaneously (a) not theorem-forbidden, (b) tied to a concrete benchtop experiment, and (c) a direct route to the "inertial propulsion" the premise posits.

**The make-or-break experiment** is therefore singular and achievable: a **clean, confound-controlled, independently replicated measurement of a static propellantless force** — a levitation or steady-thrust signal — at national-metrology-lab precision (the McCulloch–NPL-style proposal), combined with the **orientation-reversal vacuum-balance protocol** that has already killed the EmDrive and the Woodward thruster (Tajmar). A *static* force is the cleanest possible signature because it removes the oscillatory/thermal ambiguity that has explained away every prior claim. Two outcomes, both valuable:
- It survives independent replication with confounds excluded → the most important physics result in a century, and inertia engineering becomes real.
- It doesn't → the current device lineage is closed, and attention moves to the foundational question below.

**What "building it" would actually require.** None of the current hardware is a viable starting point — they don't produce confirmed thrust. A real program would be a *physics* program first: precision tests of whether inertial mass can be altered by EM fields, acceleration, or engineered horizons, at sensitivity well below the artifact floor, with independent replication built in from day one. Only if that returns a positive does device engineering begin.

---

## 10. The deepest open question

Whether any of this is possible reduces to an unresolved problem in foundational physics: **the origin of inertia.** The Higgs mechanism gives rest mass to fundamental particles, and QCD binding energy supplies most of the mass of ordinary matter — but the *inertial resistance to acceleration*, and why it exactly equals gravitational mass (the equivalence principle, tested to ~1 part in 10¹⁵), is not fully explained by a local mechanism. **Mach's principle** — the idea that inertia arises from interaction with all the distant matter in the universe — is *not* part of standard general relativity and remains genuinely debated. Every serious inertial-propulsion proposal (Woodward, QI) is, at bottom, a bet that inertia is relational and therefore locally manipulable. Mainstream physics has neither confirmed nor closed that bet. That is the real frontier, and it is why this topic is not simply pseudoscience even though every current device is unconfirmed.

---

## 11. Confidence levels and what would change the verdict

**Separating established physics / inference / speculation:**

*Established (high confidence):* Conservation of momentum forbids closed-system mechanical drives. GR predicts frame-dragging (measured) but it is negligibly weak for lab masses. Alcubierre/Natário metrics require negative energy; superluminal/accelerating warp drives violate the null energy condition as a theorem; quantum inequalities bound negative energy below usable levels. The EmDrive's measured thrust was thermal/EM artifact. Equivalence principle holds to ~10⁻¹⁵.

*Well-supported inference (moderate–high):* The Woodward Mach-effect signal is an artifact (non-reversing under rotation; shrinks with sensitivity). No defense program has produced a real effect. The 2024 subluminal warp solution provides no propulsion.

*Speculation / unconfirmed (low confidence either way):* That inertia is locally modifiable (the Mach-effect/QI premise). The Unruh-horizon mechanism (QI). Hoyle–Narlikar instantaneous absorber response (Woodward). Pais-style inertial-mass reduction via vacuum polarization.

**Confidence in the bottom line:** **High** that no current mechanism is demonstrated and buildable today; **High** that mechanical drives and superluminal warp are dead ends; **Moderate** that inertia-modification is the only family worth a focused experimental bet; **Genuinely open** (low confidence) on whether inertia can be locally modified at all.

**What would change it:** a single, independently replicated, confound-controlled static-thrust/levitation result at metrology-lab precision. That one result — positive or negative — would settle more than any number of new theory papers.

**A note tying back to the UAP framing:** the flight behaviors attributed to UAP (instantaneous acceleration, no inertial signature, no exhaust, trans-medium travel) would require precisely *inertia/gravity manipulation* — the one capability for which there is, as of 2026, no demonstrated mechanism, only a foundational question that remains open. The propulsion physics neither confirms nor explains the sightings; it tells you what would have to be true, and how far we are from showing it can be.

---

## Sources

**Warp / metric engineering & gravitomagnetism**
- Alcubierre 1994 (warp metric): https://arxiv.org/abs/gr-qc/0009013
- Pfenning–Ford (quantum inequalities; energy magnitude): https://arxiv.org/pdf/gr-qc/9702026
- Van Den Broeck (energy reduction): https://arxiv.org/pdf/gr-qc/9905084
- Natário (zero-expansion drive): https://arxiv.org/pdf/gr-qc/0110086
- Bobrick & Martire 2021 (general/physical warp drives): https://arxiv.org/abs/2102.06824
- Santiago, Schuster & Visser 2022 (generic warp drives violate the NEC): https://arxiv.org/abs/2105.03079
- Lentz WEC violation (2025 refutation): https://arxiv.org/pdf/2511.18251
- Fuchs et al. 2024, *Constant velocity physical warp drive solution* (CQG 41:095013): https://arxiv.org/abs/2405.02709
- Warp Factory toolkit 2024: https://arxiv.org/pdf/2404.03095
- Buchert & Vigneron 2026 (new no-go theorems): https://arxiv.org/abs/2602.16495
- Tajmar gravitomagnetic London-moment claim (2006): https://arxiv.org/pdf/gr-qc/0610015

**Mach-effect / Woodward**
- Mach-effect thruster overview: https://encyclopedia.pub/entry/34880
- Tajmar/TU Dresden SpaceDrive (artifact, non-reversing signal): https://www.sciencedirect.com/science/article/abs/pii/S009457651832071X
- Tajmar et al., *Acta Astronautica* 182:531 (2021): https://ui.adsabs.harvard.edu/abs/2021AcAau.182..531M/abstract
- Rodal 2025 (covariant analysis; baryon-conservation prohibition): https://arxiv.org/abs/2512.22687
- NASA NIAC / SSI program note: https://ssi.org/congratulations-team-ssi-niac-phase-ii/

**Quantized inertia & EmDrive**
- McCulloch MiHsC/QI (foundational): https://arxiv.org/pdf/1302.2775
- QI galaxy rotation (no dark matter): https://arxiv.org/pdf/1709.04918
- Renda 2019 (flaws in QI derivation), MNRAS 489:881: https://academic.oup.com/mnras/article/489/1/881/5545603
- QI Proxima Centauri (MNRAS Letters 2024): https://academic.oup.com/mnrasl/article/532/1/L67/7682393
- DARPA QI grant (Plymouth): https://www.plymouth.ac.uk/news/scientists-receive-13-million-to-study-new-propulsion-idea-for-spacecraft
- NASA Eagleworks EmDrive 2016 (White et al.): https://www.sciencealert.com/it-s-official-nasa-s-peer-reviewed-em-drive-paper-has-finally-been-published
- Tajmar EmDrive null (2021): https://phys.org/news/2021-04-comprehensive-emdrive.html
- EmDrive overview / NWPU retraction: https://en.wikipedia.org/wiki/EmDrive
- IVO Quantum Drive / Barry-1 failure: https://thedebrief.org/breaking-satellite-failure-scuttles-first-of-its-kind-in-space-test-of-physics-defying-quantum-drive/

**Mechanical drives & baseline**
- NASA TM-2006-214390, Millis & Thomas, *Responding to Mechanical Antigravity*: https://ntrs.nasa.gov/api/citations/20070004897/downloads/20070004897.pdf
- Provatidis, *Inertial Propulsion Devices: A Review*, *Eng* (MDPI) 2024: https://www.mdpi.com/2673-4117/5/2/46
- Reactionless drive (overview): https://en.wikipedia.org/wiki/Reactionless_drive
- Dean drive: https://en.wikipedia.org/wiki/Dean_drive

**Patents & defense programs**
- US 10,144,532 B2 (inertial mass reduction device): https://patents.google.com/patent/US10144532B2/en
- Navy HEEMFG test ("could not be proven"), The War Zone: https://www.twz.com/39012/the-navy-finally-speaks-up-about-its-bizarre-ufo-patent-experiments
- Patent granted via China-warning argument, The War Zone: https://www.twz.com/28729/docs-show-navy-got-ufo-patent-granted-by-warning-of-similar-chinese-tech-advances
- AAWSAP DIRDs (FOIA reading room): https://locationsunknown.org/foia-reading-room/the-deep-end/ufos-aliens/defense-intelligence-reference-documents
- NASA Breakthrough Propulsion Physics: https://en.wikipedia.org/wiki/Breakthrough_Propulsion_Physics_Project
