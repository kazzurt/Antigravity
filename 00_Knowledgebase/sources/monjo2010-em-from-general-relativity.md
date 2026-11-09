# Monjo — An Approach to Electromagnetism from the General Relativity

## One-line thesis

The energy of the electromagnetic interaction is itself treated as a source of spacetime curvature, so that a small electric perturbation `A^αβ` added to the Minkowski metric approximately reproduces Maxwell's equations, the Lorentz force, and the electromagnetic terms of the Klein–Gordon and Dirac equations.

## Provenance

- Robert Monjo i Agut, Department of Earth Physics and Thermodynamics, Faculty of Physics, University of Valencia. 14 pages, A4, no journal reference on the document.
- Held copy is a Ghostscript re-print dated `2014-02-13`, obtained from the Academia.edu mirror (record `3880024`; matching ResearchGate record `48172439`).
- **Very likely arXiv:1012.4730v1 (December 2010) under its original title.** This is inferred from the matching title on both mirrors, the `1012` submission month, and the abstract's subject match; it is *not* directly confirmed, because arXiv serves the current abstract for every version URL of that identifier.
- **Superseded by the author's own peer-reviewed successor.** The same arXiv identifier evolved through v7 (October 2024) into *From colored gravity to electromagnetism*, by Monjo, Rodríguez-Abella, and Campoamor-Stursberg, published in **Gen. Relativ. Gravit. 56, 117 (2024)**, and followed by *Weak mixing angle under U(1,3) colored gravity*, **JHEP 06 (2025) 207** (arXiv:2502.11236). The mature program is a teleparallel/`SU(1,3)` Yang–Mills gauge construction and shares almost nothing with the draft held here beyond the event-horizon-referenced potential origin.

This is the only entry in the project's alternative-unification cluster whose lineage actually reached refereed literature. The document in the library is the abandoned early draft, not that result.

## Core content

- Postulates a scalar electric field `Δζ₂` from a source charge and defines a perturbation energy `m_q1 ≡ q₁Δζ₂` (eq. 2.1), with potentials referenced to an apparent minimum radius `r_m` rather than to infinity (eq. 2.3).
- Builds an energy-momentum-charge tensor `P^αβ = P_m^αβ + J^αβ` (eq. 2.14) and splits the metric into gravitational and electromagnetic perturbations, `g_λσ ≈ η_λσ + Φ_λσ + A_λσ` (eq. 3.1), with both assumed small.
- Splits the linearized Einstein equation accordingly and identifies an "electromagnetic part," `R̃^αβ ≈ −8π(J^αβ − ½Jg^αβ)` (eq. 3.16).
- With the ansatz `A^αβ ≈ 2ζ_1m ζ₂ u^α u^β` (eq. 4.1) and a gauge choice, recovers the inhomogeneous Maxwell equation `∂^γF_γβ ≈ 4πρ_q u_β` (eq. 4.9) and its retarded Green's-function solution (eq. 4.11).
- Recovers the homogeneous Maxwell equation `∇_αF_βγ + ∇_βF_γα + ∇_γF_αβ ≡ 0` (eq. 4.21) directly from the first Bianchi identity.
- Recovers the Lorentz force in a gravitational field from the geodesic equation, up to a residual term `q₁u₁^α u_α d_τ Ã^μ` the author states is usually zero (eq. 4.38).
- Fixes `r_m1 = m₁` by matching `g₀₀` to the Newtonian limit, hence `ζ_m1 = q₁/m₁` (eqs. 4.15–4.16).
- Estimates the perturbation size in hydrogen: `|A^αβ| ~ 10⁻⁷` (proton) and `~10⁻⁴` (electron) at the Bohr radius, consistent with the assumed smallness (§5.1).
- Shows the construction is compatible with the Klein–Gordon and Dirac equations in the presence of an electromagnetic field (§5.3), and suggests an extra gravitational term in strong fields.

## Key claims to audit

**Charge–energy identification via an imaginary mass.** The paper proposes `q₁ζ₂ = m̃₁φ̃₂` with `m ↔ i√(k/G)·m̃` (eq. 5.3), making the electric and gravitational `00` metric components formally interchangeable. The author flags this himself as possibly "too daring."

**Gravitational variation of the fundamental charge — the one falsifiable prediction.** Equation 5.23 gives `q' = q(1 − GM/rc²)`, i.e. a charge that depends on the local gravitational potential. Since `α ≡ ke²/ħc ∝ q²`, this implies a sensitivity coefficient of `Δα/α = −2Δφ`, with deeper potential giving smaller `α`. The paper offers this as a partial explanation of reported spatial variation of the fine-structure constant (its Table 1, `Δα/α` between `±10⁻⁷` and `±10⁻³`).

## Evidence assessment

**Rating `D`.** Unvalidated early preprint, superseded by the author's own refereed successor, with a load-bearing circularity the author concedes.

**The derivation is circular by the author's own admission (§5.4).** To reproduce classical electromagnetism, the construction must presuppose the electromagnetic interaction, since the source energy is *defined* as `m_q1 ≡ q₁Δζ₂`. Maxwell's equations are therefore recovered, not derived; the paper states this premise "should be deduced from a more general form." That is the whole load-bearing gap.

**Structural defect: the metric depends on the test particle.** `A^αβ ≈ 2ζ_1m ζ₂ u^α u^β` depends on *both* charges — `ζ_1m = q₁/m₁` is a property of the probe. A metric that changes with the charge-to-mass ratio of the particle traversing it is not a field of the source alone, and there is no single spacetime for a region containing differently charged probes. This is the same defect the project already recorded for Özer (see that digest's `q/m`-selects-the-geometry note), and it is the reason the equivalence-principle structure does not survive.

**The one testable prediction is in tension with existing data — no new experiment required.** White-dwarf photospheric spectroscopy directly bounds the gravitational dependence of `α`. Berengut et al., *PRL* **111**, 010801 (2013), measured G191-B2B at a dimensionless potential `Δφ ≈ 5×10⁻⁵` relative to Earth and obtained `Δα/α = (4.2 ± 1.6)×10⁻⁵` from Fe V and `(−6.1 ± 5.8)×10⁻⁵` from Ni V. Equation 5.23 predicts `Δα/α = −2Δφ ≈ −1.0×10⁻⁴` at that potential. The Fe V result excludes this at roughly `9σ` and with the opposite sign; the noisier Ni V result is compatible with it. The two measurements are mutually discrepant and systematics-limited (see the later Fe V reanalysis, *MNRAS* **500**, 1466 (2020)), so this is a strong tension rather than a clean kill — but the prediction sits at or beyond the edge of the existing bound, and better white-dwarf or atomic-clock data would settle it outright.

**A position-dependent fundamental charge is also theoretically expensive**, since it breaks exact charge conservation and the gauge invariance that enforces it. The paper acknowledges the non-conservation ("the charge is not entirely conserved") without supplying a mechanism or a modified continuity equation.

**Scale relevance is nil for the project's purposes.** The `10⁻⁴`–`10⁻⁷` metric perturbations quoted in §5.1 are just ordinary atomic electrostatic energy re-expressed geometrically. They are not an anomalous EM-to-gravity coupling and imply no gain, actuator, or control channel.

## Why it matters here

Three uses, all narrow:

1. **Claim provenance and an anti-repeat marker** for the "electromagnetism is really geometry" family (with Stepanovic, Okunev, Özer, and Zhu). Monjo is the cleanest worked example of the family's characteristic failure: assuming the interaction you claim to derive.
2. **A worked falsification target.** The `Δα/α = −2Δφ` prediction is a rare instance of an alternative-unification paper committing to a number that existing precision astronomy already constrains — useful as a template for how this project should demand discriminants from candidate frameworks.
3. **A pointer into real literature.** The successor program (GRG 2024, JHEP 2025) is refereed and is the version worth reading if the colored-gravity/teleparallel route to EM–gravity structure is ever pursued. Neither successor claims a gravity-control mechanism.

## Reframe tags

- **Capabilities:** none claimed; electromagnetism re-expressed as metric perturbation
- **Mechanisms:** alternative unification (geometrized electromagnetism)
- **Assumption dependency:** P3 candidate framework — formalism and provenance only; circular at its foundation
- **Explains:** approximate Maxwell equations, Lorentz force, and Klein–Gordon/Dirac EM terms, given a presupposed EM interaction
- **Does not explain:** the origin of the electromagnetic interaction it assumes, a single probe-independent metric, charge conservation under its own eq. 5.23, or any actuator
- **Fatal constraint supplied:** self-admitted circularity; probe-dependent metric; `Δα/α = −2Δφ` in tension with white-dwarf spectroscopy at `~10⁻⁵`
- **Thread priority:** peripheral — provenance and discriminant-template value only

## Files

- [Source PDF](../../06_Foundations-and-Frameworks/Monjo-Approach-to-Electromagnetism-from-General-Relativity-2010.pdf)
- [Source text](../../06_Foundations-and-Frameworks/Monjo-Approach-to-Electromagnetism-from-General-Relativity-2010.md)
- [Archived original download](../../_archive/root-ingest-2026-08-01/MANIFEST.md)
