# Özer — On the Equivalence Principle and a Unified Description of Gravitation and Electromagnetism

> **Ingest status (2026-07-28): digest only — the PDF is not yet in the library.** Built from the arXiv v5 full text and abstract record. Complete the ingest by dropping the PDF into `06_Foundations-and-Frameworks/` (see [Files](#files)).

## One-line thesis

Postulates an *electromagnetic* equivalence principle — a uniform electromagnetic field is locally indistinguishable from an accelerated (or rotating) frame, but only for particles sharing a single charge-to-mass ratio — and from it builds a metric whose `g₀₀` carries an electric term proportional to the **test particle's** `q/m`, so each `q/m` class rides its own geometry instead of the one Reissner–Nordström geometry.

## Identity and provenance

- Murat Özer, single author. No affiliation is carried on the arXiv abstract record.
- **arXiv:gr-qc/9910062.** v1 19 Oct 1999 · v2 27 Oct 1999 · v3 29 Feb 2000 · v4 18 Dec 2017 · v5 8 Jan 2020 (current). Primary class gr-qc; cross-listed astro-ph, hep-ph, math-ph, quant-ph. DOI `10.48550/arXiv.gr-qc/9910062`.
- **No journal reference on the arXiv record.** Preprint-only for ~26 years, with two revisions posted 17–20 years after the original.
- Later-version comment: adds a new argument producing the `g₀₀` outside a charged sphere and points to claimed existing experimental evidence for the proposed electromagnetic equivalence principle. Some versions carry the variant title "…a Unified **Metric** Description…".
- **Companion paper:** arXiv:gr-qc/9910095, *Proposed Experiments to Test the Unified Description of Gravitation and Electromagnetism through a Symmetric Metric* — predicts the photon has a nonzero **effective charge-to-mass ratio**, and should therefore be redshifted in an electric field and deflected in a magnetic field.

## Core content

- **The postulate.** Elevator/rotating-cabin arguments run in parallel to Einstein's: a test particle in a uniform electric field accelerates exactly as one in a uniformly accelerating cabin; a charged particle bent by a magnetic field behaves as one in a rotating frame. The principle is explicitly *not* universal — it holds within a fixed `q/m` class. Where the gravitational EP asserts composition-**in**dependence, this one takes the `q/m` label as fundamental.
- **The metric.** Outside a spherically symmetric mass `M` carrying charge `Q`, for a test particle `(m, q)`:

  `g₀₀ = −(1 − 2GM/c²r + 2(q/m)k_eQ/c²r)`

- **The load-bearing difference.** The electric term is linear in `Q` and scales with the **probe's** `q/m`. Reissner–Nordström instead carries `+GQ²/(4πε₀c⁴r²)` — quadratic in `Q`, sourced by the field's own stress-energy, and identical for every probe. Özer's reading is that the electromagnetic field asserts itself *directly* in the metric rather than only through its energy density, and that this is what makes the description unified.
- **Routes to the result.** Energy considerations for charged particles; Newtonian electromagnetism recast in a Cartan-style curved-spacetime form; a relativistic action integral. A charge-current tensor `T_CC^μν` is introduced, with a weak-field validity condition that the added metric terms stay much smaller than one.
- **Stated restrictions.** Single particles, or groups of particles with identical `q/m`; interparticle interactions neglected; "empty space" taken to mean no neutral *or* charged matter present. The author leaves open whether weak and strong interactions could be housed the same way.

## Leading-order behaviour — what the metric actually buys

Geodesic motion in that `g₀₀` gives, at Newtonian order, an acceleration `−GM/r² + (q/m)k_eQ/r²` — i.e. **exactly the Coulomb term**. The construction therefore cannot conflict with laboratory electrostatics, and equally cannot be *supported* by it: reproducing Coulomb's law geometrically is the design goal, not evidence. All discriminating power lives in the relativistic corrections and in the departure from Reissner–Nordström, which is why the author's own proposed test is the right place to look.

## Claimed empirical support — both weak

- **Witteborn–Fairbank** (PRL **19**, 1049 (1967)): apparent null gravitational force on electrons drifting in a copper tube. The standard account is the **Schiff–Barnhill effect** — the lattice compresses under its own weight and sets up an internal electric field that compensates gravity on the conduction electrons. The result was never independently confirmed, and the modern charge-dependent-EP literature treats Schiff–Barnhill as the dominant systematic background rather than as evidence for new physics.
- **The London moment**, `B = (2mₑ/e)Ω` in a rotating superconductor. Real and precisely measured, but the coefficient *is* `m/q` by construction in ordinary electrodynamics of a rotating charged condensate. Its `q/m` dependence is a consequence of standard theory, not an independent signature of a new geometry. (This project's own `DERIVATION_PACKAGE.md` and the Tate inversion work the same coefficient from the conventional side.)

## Proposed tests

1. **Electron-beam deflection near a charged sphere in vacuum** — the decisive discriminator, since a `q/m`-dependent `g₀₀` and Reissner–Nordström predict different trajectories for the same source.
2. **"Electrical geometry waves"** analogous to gravitational waves.
3. **"Electrical black hole"** — a charged object from which electrons cannot escape, with a radius set by energy conservation; the author suggests it could be built in a laboratory.
4. Via the companion paper: photon redshift in a static electric field; photon deflection in a magnetic field.

## Why it matters here

- It is the sharpest statement in this library of the **"charge-to-mass ratio selects the geometry"** move. The project keeps arriving at `q/m` as the discriminating label from the conventional side — the multicomponent rotation response, the charge-neutral-but-stress-energy-carrying mode, the Tate `92 ppm` inversion — where `q/m` differences are emergent properties of ordinary matter. Özer makes the label *fundamental*. That makes the paper a useful foil: it isolates exactly which step is doing the work in the project's own derivations.
- Both of its cited "evidences" are threads already owned here: the London moment (`DERIVATION_PACKAGE.md`, Tate) and equivalence-principle tests on exotic matter (Ross et al. 2025 digest).
- It sits with Okunev, Stepanovic, Zhu and Dunning-Davies as an alternative unification attempt, but is more disciplined than most of that set: it writes down one explicit metric component and names a falsifiable experiment that separates it from standard theory.

## Scope — what it does and does not deliver

- **Delivers:** an explicit metric component, a stated validity regime, a named discriminating experiment, and an honest restriction to fixed-`q/m` ensembles.
- **Does not deliver:** field equations from a variational principle that yield both Einstein and Maxwell; a demonstration of stress-energy conservation; a PPN analysis; any quantitative prediction (deflection angle, required `Q`, beam energy) for the experiment it proposes; or any treatment of many-particle neutral bulk matter — which is the only regime a propulsion claim could live in.
- **Structural tension to record:** a metric that depends on the probe's `q/m` is not a property of spacetime in the usual sense. It is closer to an effective single-particle geometry (a Finsler- or Kaluza-Klein-flavoured object) than to a spacetime metric, and the paper does not confront that reading.

## Modern constraint context

Charge-dependent equivalence-principle violation is a genuinely under-tested frontier: high-precision torsion-balance tests reach `|Δa/g| < 10⁻¹⁵` but use *electrically neutral* masses (`q/m ≈ 0`) and are therefore blind to it. A 2026 phenomenological treatment (arXiv:2605.12246) defines `Δa/g = κ Δ(q/m)` and extracts a first bound `|κ| < 2.1 × 10⁻⁴ kg C⁻¹` (95% CL). **This does not directly bound Özer**, whose electric term is sourced by a charged body rather than being a universal charge-dependent free-fall anomaly — but it is the right modern reference frame for the class of claim, and it shows the discriminating regime is empirically open rather than closed.

## Evidence assessment

`D` — single-author preprint, no journal venue in 26 years, no derivation of coupled field equations, no quantitative prediction for its own decisive test, and two cited "confirmations" that both have standard explanations (Schiff–Barnhill; ordinary rotating-condensate electrodynamics). Retain for **claim provenance and as a structural foil**, not as a candidate mechanism. Its one durable contribution is a clearly posed question: whether anything in nature makes the *probe's* `q/m` enter the metric, and what experiment would show it.

## Reframe tags

- **Capabilities:** none demonstrated; asserts a `q/m`-selected geometry
- **Mechanisms:** alternative unification; charge-to-mass-ratio-dependent metric
- **Assumption dependency:** P3 candidate mechanism, speculative; fails the covariance/action gate
- **Explains:** Coulomb's law geometrically (by construction); nothing beyond it
- **Does not explain:** neutral bulk matter, many-particle regimes, energy-momentum closure, or why Reissner–Nordström should be wrong
- **Fatal constraint supplied:** none — but supplies a clean falsifiable target (electron deflection near a charged sphere vs RN)
- **Thread priority:** peripheral; foil for the `q/m` structural argument in `DERIVATION_PACKAGE.md`

## Files

- **PDF: not yet in the library.** Source: <https://arxiv.org/abs/gr-qc/9910062> → save as `06_Foundations-and-Frameworks/Ozer-Equivalence-Principle-Unified-Description-Gravitation-Electromagnetism-1999.pdf`, then generate the searchable `.md` twin and add the `INDEX.md` row.
- Companion preprint: <https://arxiv.org/abs/gr-qc/9910095>
- Related digests: [Okunev](okunev-undated-unified-theory.md) · [Stepanovic](stepanovic2019-gravitational-em-field.md) · [Zhu](zhu2018-gravitational-em-interaction.md) · [Ross et al. 2025](ross2025-superconductor-wep-test.md)
