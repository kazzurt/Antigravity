# Ross et al. (Eöt-Wash) — Test of the Equivalence Principle for Superconductors

## One-line thesis

A cryogenic torsion balance with superconducting-niobium and copper test bodies finds free fall toward the sun universal to `η_Nb*-Cu ≤ 2.0 × 10^-9` (95% confidence), the strongest direct constraint on anomalous gravitational response of superconducting matter and, rescaled, `η_CP-ee ≤ 9.2 × 10^-4` for Cooper pairs.

## Identity and provenance

- M.P. Ross, S.M. Fleischer, I.A. Paulson, P. Lamb, B.M. Iritani, E.G. Adelberger, C.A. Hagedorn, K. Venkateswara, C. Gettings, E.A. Shaw, S.K. Apple, J.H. Gundlach — Eöt-Wash group (CENPA, University of Washington) with Western Washington University, Carleton College, and Columbia.
- arXiv:2407.21232 (v3, 19 Aug 2024, gr-qc); published as *Phys. Rev. D* **111**, L021101 (2025), DOI `10.1103/PhysRevD.111.L021101` (identity re-verified against APS 2026-07-17).
- Analysis code public at `github.com/EotWash/SuperEP`; data stated available on request.
- This is the paper the 2026-07-16 comprehensive review flagged for ingestion as a constraint source.

## Core content

- **Motivation:** published proposals (de Matos 2010; Quach 2015 gravitational-Casimir; Minter–Wegter-McNelly–Chiao 2010 "GW mirrors") argue the non-local quantum character of Cooper pairs yields WEP violations, sometimes dramatic (strong reflection of gravitational waves). Only two prior experiments probed superconductor gravity: Jain–Lukens–Tsai 1987 (charged-particle SQUID test) and Tajmar–Plesescu–Seifert 2009, whose weight-vs-temperature comparison gave `η_Nb*-Cu < 4.0 × 10^-7`.
- **Apparatus:** one of the very few cryogenic torsion balances ever operated (Fleischer et al., *Rev. Sci. Instrum.* 93, 064505 (2022)). Composition dipole of eight 9.5 g test bodies — four OFHC copper, four 99.9% niobium — on a pendulum hung from a 30 µm × 16.5 cm tungsten fiber; lever arm `2.3 cm`; `κ = 8.7 × 10^-8 N m/rad`; `ω₀ = 2π × 5.1 mHz`; multi-slit autocollimator readout. Inner thermal shield at ~5 K wrapped in lead (superconducting magnetic shield) plus Co-NETIC AA mu-metal outside; 0.4 mPa helium exchange gas thermally couples the pendulum below niobium's `T_c = 9 K`.
- **State verification (reusable technique):** pendulum temperature cannot be measured directly without spoiling the balance, so superconductivity was demonstrated *in situ* by magnetic-field injection: an interior-coil drive at `ω` produces a Meissner-expulsion torque at `2ω` (torque ∝ B², plus an enhanced `1ω` pinned-flux response), and the exterior-coil response vanishes when the lead shield goes superconducting. A conservative pendulum temperature bound of 8 K gives a two-fluid Cooper-pair fraction `N_CP/N_v = 1 − (T/T_c)^4 = 0.38`.
- **Method:** 22 usable days (26 Mar – 22 Apr 2024) searching for a solar-direction, daily-modulated differential torque. Pendulum flipped 180° between week-long sets so a real composition signal reverses sign while environmental dailies do not. Inner-shield temperature coupling (`4.6 × 10^-11 N m/K`) and tilt couplings subtracted; magnetic coupling bounded `< 10^-11 N m/Gauss` (`< 0.1 fN m`). Day-long cuts fitted to in-phase/out-of-phase projections of the sun's position (Astropy ephemerides), inverse-variance averaged.
- **Result:** `τ_in = −1.3 ± 5.2 fN m` and `τ_out = −2.1 ± 5.2 fN m` — no violation. Via `η = τ_in/(m r a_g)`: **`η_Nb*-Cu ≤ 2.0 × 10^-9`** and **`η_CP-ee ≤ 9.2 × 10^-4`** (95% confidence), improving Tajmar et al. by more than two orders of magnitude. The authors conclude the experiment "places strong constraints on any enhanced gravitational effects of superconductors."

## Why it matters here

This closes the **response side** of the superconductor–gravity question at the ppb level: bulk superconducting niobium gravitates (passively) like normal copper. Together with Li's 1997 static null (`< 2 × 10^-8 g`, **source side**) it brackets the demoted superconducting-amplification lane from both directions, and it directly undercuts the theoretical family (de Matos, Quach, Minter–Chiao) that motivated "superconductors reflect gravitational waves." For the current program it is a standing gate: any phase-gated material portal that changes a superconductor's *universal* gravitational coupling must hide below `2 × 10^-9` in bulk solar free fall, live in a dynamic/AC channel, or act on the source side — a constraint far tighter than the phase-transition discriminator experiments the project has considered.

## Scope — what it does and does not constrain

- **Constrains:** composition-dependent static/DC gravitational response of the superconducting state toward the sun (horizontal projection), over ~day timescales; bulk Nb at `2 × 10^-9`; Cooper pairs at `9.2 × 10^-4`.
- **Does not constrain:** source-side field *generation* (Li's claim class); AC, transient, or frequency-dependent couplings; above-disk "shielding" geometries (Podkletnov-type claims act on other bodies, not the superconductor's own fall); anomalies coupling only to Earth's vertical field (a torsion balance is insensitive to uniform vertical forces); and any Cooper-pair anomaly below `~10^-3`.
- **Sensitivity note (Tate):** the Cooper-pair limit `9.2 × 10^-4` sits one order of magnitude above the `9.2 × 10^-5` (92 ppm) scale of Tate's London-moment residual, so a hypothetical gravitational reading of that residual is *not yet* excluded by this test — and Tate's `m_app` is an electromechanical response coefficient, so any mapping onto `η` is model-dependent anyway.
- **Conventional-physics note:** ordinary condensation-energy mass shifts are `ΔE/c² ~ 10^-17` of rest mass, ~8 orders below even this sensitivity; the null therefore confirms expectation and cuts only "enhanced/remarkable effect" claims.
- **Caveats:** pendulum temperature bounded, not measured (mitigated by the Meissner verification and the conservative 8 K assumption); niobium is type-II and carried pinned flux during operation; the Cooper-pair conversion inherits the two-fluid estimate.

## Evidence assessment

`A` — precision primary null experiment from the leading torsion-balance group, peer-reviewed as a PRD Letter, with published apparatus paper, stated systematics budget, sign-reversing dipole flips, and open analysis code. Strongest available direct free-fall constraint on superconductors; its limits are narrower than its title suggests (response-side, solar-direction, DC), and the digest above records those scopes explicitly.

## Reframe tags

- **Capabilities:** (constraint) passive gravitational response of coherent quantum matter is standard at `10^-9`
- **Mechanisms:** gravitomagnetic amplification (response branch closed at ppb); phase-gated material portals (universality gate); GW-mirror/gravitational-Casimir claims (motivating regime excluded)
- **Assumption dependency:** premise-independent constraint input to P3 mechanism analysis
- **Explains:** why "superconductors fall differently" claims have no surviving bulk, static support
- **Does not explain:** source-side, dynamic, or sub-`10^-3` Cooper-pair physics; the Tate residual
- **Fatal constraint supplied:** any mechanism needing order-unity — or even `10^-8` bulk — anomalous free fall of a superconductor is dead; GW-mirror-scale WEP violation excluded
- **Thread priority:** standing constraint baseline for the phase-gated laboratory lane and for every superconducting discriminator experiment

## Files

- [Source PDF](../../03_Propulsion-and-Anomalies/Ross-Test-of-the-Equivalence-Principle-for-Superconductors-PRD-2025.pdf)
- [Source text](../../03_Propulsion-and-Anomalies/Ross-Test-of-the-Equivalence-Principle-for-Superconductors-PRD-2025.md)
