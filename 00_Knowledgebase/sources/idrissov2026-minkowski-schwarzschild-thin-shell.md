# Idrissov — Exact Radial Stability Threshold for a Minkowski–Schwarzschild Thin Shell

> **Ingest status (2026-11-10): digest only.** Built from the arXiv v1 PDF, read in full (6 pages). The PDF sits at the project root as `2610.17629v1.pdf` and has not been filed into a topic folder (see [Files](#files)).

## One-line thesis

A thin perfect-fluid shell with flat space inside and Schwarzschild outside, presented as "the simplest model of a subluminal warp drive", cannot be radially stable below `a₀ ≈ 2.3704 M` if its sound speed is at most `c`; a black hole inside the shell only raises that threshold, toward `3M`.

## Identity and provenance

- Anuar Idrissov, single author. Affiliations: Instituto de Ciencias Nucleares, UNAM (Mexico); Fesenkov Astrophysical Institute and Al-Farabi Kazakh National University (Almaty). Acknowledges a SECIHTI postgraduate scholarship.
- **arXiv:2610.17629v1 [gr-qc]**, 13 Oct 2026. No journal reference; not peer reviewed at the time of reading.
- The supporting Mathematica notebook is available "by reasonable request" only. It was not seen.

## Core content

- **Model.** Darmois–Israel junction of `f₋ = 1` to `f₊ = 1 − 2M/r` at areal radius `a`. With `s ≡ √(1 − 2M/a₀)` and `M = 1`, the static shell has `σ₀ = (1−s)²(1+s)/8π`, `p₀ = (1−s)³(1+s)/32πs`, so `p₀/σ₀ = (1−s)/4s`.
- **Energy conditions.** Null, weak and strong hold for all `a₀ > 2M`. Dominant holds only for `a₀ ≥ 25M/12`. `σ₀ = 2p₀` at `a₀ = 9M/4`.
- **Radial stability.** With a barotropic wall, `β² ≡ dp/dσ`, the shell is stable when `β² > β²_crit(s) = (1 + s + s² − 3s³) / [4s²(1 + 3s)]`.
- **Slope identity.** `β²_crit = dp₀/dσ₀` along the sequence of static solutions at fixed `M`, for any pair of bulk metrics `f±`. Marginal stability is the existence of a neighbouring equilibrium, the thin-shell form of the turning-point criterion.
- **Causal threshold.** Setting `β²_crit = 1` gives `15s³ + 3s² − s − 1 = 0`, root `s* = 0.3952950`, so `a_crit = 2.3703931 M` (compactness `2M/a₀ ≈ 0.844`).
- **Black hole inside.** With `f₋ = 1 − 2m/r`, `0 ≤ m < M`, the threshold rises monotonically from `2.3704 M` at `m = 0` to `3M` as `m → M`, and always satisfies `3m < a_crit < 3M`. The flat interior is the most favourable member of the family.
- **Stated limits.** The paper says the boosted shell is the static shell seen from another frame (a diffeomorphism), calls its model "the degenerate member" of the Fuchs et al. class, and states that "the acceleration phase lies outside this construction". It also says the threshold matters only for objects close to their own horizon.

## Verification performed here (2026-11-10)

Re-derived by hand from the junction conditions, without the author's notebook:

- `σ₀`, `p₀`, and the `25M/12` and `9M/4` radii.
- `dσ₀/ds`, `dp₀/ds`, and their ratio, which reproduces `β²_crit(s)`.
- The cubic and its root: `s = 0.3953` gives a residual of order `10⁻⁴`; `a_crit = 2.3704 M`.
- `β²_crit = 0.366` at `a₀ = 3M` and `0.0162` at `a₀ = 25M`.
- The `m → M` factorisation `u(3u − 1)(5u + 3) = 0` and the sign of `∂Φ/∂x` used in step (ii) of the proof.
- One table row (`m/M = 0.5`, `a_crit = 2.5231 M`, `u = 0.3538`): satisfies `Φ = 0` to four decimals.
- **Newtonian limit.** As `s → 1`, `β²_crit → 3(1−s)/8` and `p₀/σ₀ → (1−s)/4`, so the critical adiabatic index `Γ ≡ (σ + p)β²/p → 3/2`. An elementary Newtonian force balance for a pressure-supported shell (outward `2p/a ∝ a^(−2Γ−1)`, inward `σg ∝ a⁻⁴`) gives the same `Γ > 3/2`.

No error was found. Not checked: the remaining table rows, steps (i) and (iii) of the proof in full, and Refs. [18] and [19].

Literature checks (web, abstracts only):

- Pitre, Schneider and Poisson, *Self-gravitating thin shells are dynamically unstable on all angular scales*, arXiv:2604.05980. Exists; its abstract matches the paper's description: same Minkowski-inside, Schwarzschild-outside fluid shell, a growing even-parity mode for all sampled compactnesses, adiabatic indices and multipoles `ℓ ≥ 2`.
- LeMaitre and Poisson, *Equilibrium and stability of thin spherical shells in Newtonian and relativistic gravity*, arXiv:1909.06253, DOI `10.1119/10.0000026`. Its abstract states the link between a maximum on the equilibrium sequence and the onset of dynamical instability for thin shells. **Not cited by Idrissov.**

## Limitations

- **Not a warp drive in any propulsion sense.** By the paper's own Section II the configuration is a massive shell in inertial motion. There is no shift vector that survives a coordinate change, no acceleration mechanism, and no control variable.
- **The threshold does not reach hardware scales.** A shell of radius 10 m at `a_crit` has `M = 4.22 m` in geometric units, about `5.7 × 10²⁷ kg` or 3 Jupiter masses. For `a₀ ≫ M` any wall with nonzero stiffness is radially stable.
- **Novelty is modest** (`project-inference`). Radial stability of Schwarzschild thin shells through a sound-speed parameter goes back to Brady–Louko–Poisson (1991), Poisson–Visser (1995), Ishak–Lake (2002) and Lobo–Crawford (2005), all cited. The slope identity overlaps the uncited LeMaitre–Poisson (2019) result; the degree of overlap is inferred from that paper's abstract, not its text. What appears new is the closed-form causal threshold and the monotonicity proposition.
- **Radial stability is moot for viability.** The same shell is reported unstable to non-radial perturbations (Yang–Bonga–Pan 2023; Pitre–Schneider–Poisson 2026).
- Idealisations: infinitely thin wall, perfect fluid, linear perturbations, isentropic.

## Project use

- A compact, checkable statement that the "physical" or positive-energy warp line (Bobrick–Martire 2021; Fuchs et al. 2024) reduces, in its simplest exact form, to a heavy shell coasting inertially. This is the first fatal constraint already listed on the [warp mechanism page](../mechanisms/warp-and-causal-structure.md): a constant-velocity geometry with no self-acceleration mechanism.
- The junction-condition algebra and the slope identity are reusable benchmarks for any thin-wall worldtube calculation, including the shell-stress work in the [worldtube source theorem report](../../01_Reports-and-Syntheses/Worldtube-Source-Theorem-and-Phase-Localized-Metric-Higgs-Gate-0-2026.md).
- It supplies no source, gate, or reaction reservoir and changes no gate decision in the program.

## Evidence assessment

**Rating: B — single-author preprint; algebra independently re-derived here.** Reliable as a general-relativity benchmark. Zero evidence for propulsion, frame decoupling, or gravity control.

## Reframe tags

- **Capabilities:** none
- **Mechanisms:** thin-shell worldtube benchmark; subluminal "physical warp" class (degenerate member)
- **Assumption dependency:** P3 context only; does not bear on P2 or P5
- **Explains:** which static flat-interior shells are radially stable, and why (turning point of the static sequence)
- **Does not explain:** creation, acceleration, or control of the shell; non-radial stability; any laboratory-scale effect
- **Fatal constraint supplied:** reinforces `constrained` status of the constant-velocity warp-shell route (no self-acceleration; non-radial instability per cited work)
- **Thread priority:** peripheral

## Files

- **PDF: not yet filed.** Local copy at project root as `2610.17629v1.pdf`. Source: <https://arxiv.org/abs/2610.17629>. To complete the ingest, move it to `02_Gravitation-Theory/Idrissov-Exact-Radial-Stability-Threshold-Minkowski-Schwarzschild-Thin-Shell-2026.pdf`, generate the searchable `.md` twin, and add the `INDEX.md` row.
- Related reports: [Warp and breakthrough propulsion — who leads](../../01_Reports-and-Syntheses/Warp-and-Breakthrough-Propulsion-Who-Leads-2026.md) · [Rodal warp review](../../01_Reports-and-Syntheses/Rodal-Warp-and-Breakthrough-Propulsion-2023-2026.md) · [State of the art](../../01_Reports-and-Syntheses/Inertial-and-Gravitational-Propulsion-State-of-the-Art-2026.md)
- Cross-checks: <https://arxiv.org/abs/2604.05980> · <https://arxiv.org/abs/1909.06253>
