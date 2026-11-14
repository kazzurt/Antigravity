# Bubble wall, stage 1: static models

**Date:** 2026-11-13. **Status:** calculated and checked; Newtonian weak-field model only.

## Question

What must a wall do to cancel Earth's pull inside a spherical cabin, and what do the gravitoelectric (ordinary gravitational) and gravitomagnetic (frame-dragging) fields look like at and across that wall as its thickness and smoothness change?

## Setup

- Cabin of inner radius `R = 5 m` in a uniform field `g0 = 9.81 m/s²` pointing down.
- The wall occupies `R < r < R + d` and carries an effective mass density `ρ = f(r) cos θ` (θ measured from straight up). This is bookkeeping for what the wall has to emulate. Nothing here says matter can do it.
- Because the source is a pure dipole pattern, the wall's potential is exactly `φ(r) cos θ` for any radial profile `f`, with `φ` given by two one-dimensional integrals (see the script header). Top-hat and smooth profiles and four thicknesses (0.05, 0.2, 1.0, 2.5 m) are solved.

## Two wall models

| | A: screen | B: quiet |
|---|---|---|
| Wall | One layer, positive on the upper half, negative on the lower | Inner and outer layers of opposite sign |
| Inside | Field zero | Field zero |
| Outside | Disturbed by a dipole; field lines end on the wall as on a conductor in an electric field | Completely undisturbed |
| Potential | Continuous | Steps by about `g0 R` across the wall |
| Thin-wall limit | Field jumps at the wall | Potential jumps at the wall (the "discontinuous" bubble) |

## Results

**Screen (A)**

- Needs `σ0 = 3 g0 / (4πG) = 3.5 × 10¹⁰ kg/m²` of effective surface mass, half of it negative. Absolute inventory `5.6 × 10¹²` kg for a thin wall.
- Just outside the top and bottom of the bubble the field is three times Earth's (2.97 g0 at d = 0.05 m), and zero at the equator.
- The outside disturbance falls as `g0 (R/r)³`: about 1.2 × 10⁻⁶ m/s² at 1 km.
- Making the wall thick and smooth lowers the peak (2.2 g0 at d = 2.5 m) and spreads it; the far field grows because the dipole sits further out.

**Quiet (B)**

- Nothing changes outside, at any distance.
- The price is inside the wall. The potential step of about `g0 R` has to happen within the wall, so the field there is about `2R/d` times Earth's: roughly 200 g0 at d = 0.05 m, about 50 g0 at 0.2 m, and a few g0 only when the wall is as thick as the cabin radius.
- Absolute inventory: `7.4 × 10¹⁴` kg at d = 0.05 m, `1.9 × 10¹⁴` at 0.2 m, `4.9 × 10¹³` at 1.0 m, `2.8 × 10¹³` at 2.5 m. The 0.2 m figure reproduces the project's earlier worldtube benchmark.
- The clock-rate step across the wall is `g0 R / c² = 5.5 × 10⁻¹⁶`.

**Thickness and smoothness**

- Outside the wall, and inside the cabin, the answer depends only on two integrals of the profile. Top-hat and smooth walls of the same thickness give nearly the same field there.
- All the difference is inside the wall: a top-hat gives kinks in the field, a smooth profile rounds them.

**Gravitomagnetic field**

It appears only when the wall's mass moves.

- **Bubble translating at speed v:** `B_g = −(4/c²) v × g_wall`. The cabin interior carries a uniform frame-dragging field `4 v g0 / c²`, which is `1.3 × 10⁻¹³ s⁻¹` at 300 m/s. That is several times the scale of Earth's own frame-dragging field at the surface (`1.7 × 10⁻¹⁴ s⁻¹`, order of magnitude only). In the screen model it leaks outside as a dipole pattern; in the quiet model it reverses sign inside the wall and vanishes outside.
- **Bubble rotating about the vertical:** the field is zero at the centre, grows linearly to the wall, and is of order `5 × 10⁻¹⁵ s⁻¹` at a rim speed of 10 m/s.

## What this establishes

1. A static bubble that cancels a uniform pull needs negative effective mass over half the wall. That is the job the driven wall (stage 3) would have to do some other way.
2. Quiet outside and gentle wall cannot both hold for a thin wall. A thin quiet wall contains a field hundreds of times Earth's; anything crossing it passes through that.
3. A moving bubble has a frame-dragging signature inside the cabin that is larger than Earth's, though still far too small to feel.

## Limits

- Newtonian and weak-field. In general relativity the wall's stresses also gravitate; the project's `5 × 10²⁷ Pa` benchmark belongs to that fuller treatment.
- Uniform external field; steady, slow motion for the gravitomagnetic part, described in Earth's frame.
- Sign and factor conventions for `B_g` are stated in the script header.

## Files

- `bubble_wall_static.py` — solver, checks and figures. Needs numpy and matplotlib.
- `fig1_wall_line_profiles.png` — field, potential and wall density along a vertical line through the top of the wall.
- `fig2_gravitoelectric_maps.png` — field strength and field lines in a vertical section.
- `fig3_gravitomagnetic.png` — frame-dragging field for a translating and a rotating bubble.
- `wall_line_profiles.csv`, `results.json` — line data and checked numbers.

---

# Stage 1b: the wall in weak-field general relativity

**Date:** 2026-11-13. Script: `bubble_wall_gr.py`; figure: `fig4_gr_wall.png`; numbers: `results_gr.json`. All checks pass.

## What general relativity adds

Two potentials replace the single Newtonian one:

- the **ruler potential** `Ψ`, sourced by energy density alone;
- the **clock potential** `Φ`, sourced by energy density plus the sum of the stresses. Slow masses and clocks respond to `Φ`.

A wall that supports itself has stresses that balance, and such a stress field can be written with one function `S`. Then `Φ − Ψ = (8πG/c²) S`. Two consequences follow directly:

1. **Stress cannot change the field outside the wall.** Outside, the field is set by energy density only.
2. **Stress can change the clock potential inside the cabin by a uniform slope.** That is exactly what cancelling Earth's pull needs.

## Wall 1: pure stress, no energy density

Take `S = b z χ(r)`, with `χ` falling smoothly from 1 in the cabin to 0 outside and `b = −g0 c² / (8πG)`.

- **It is the quiet bubble.** Earth's pull is cancelled inside and nothing changes outside. The script confirms that its active density reproduces the Newtonian quiet wall of stage 1.
- **It is weightless.** With no energy density, Earth exerts no net force on the wall.
- **Stress it must carry:**

| Thickness d | Peak radial stress | Peak tangential stress | Peak field inside wall |
|---|---|---|---|
| 0.05 m | 3.9 × 10²⁸ Pa | 6.1 × 10³⁰ Pa | 188 g0 |
| 0.1 m | 2.0 × 10²⁸ Pa | 1.5 × 10³⁰ Pa | 94 g0 |
| 0.2 m | 9.9 × 10²⁷ Pa | 3.9 × 10²⁹ Pa | 47 g0 |
| 1.0 m | 2.0 × 10²⁷ Pa | 1.7 × 10²⁸ Pa | 9.9 g0 |
| 2.5 m | 7.9 × 10²⁶ Pa | 3.3 × 10²⁷ Pa | 4.3 g0 |
| 5.0 m | 3.9 × 10²⁶ Pa | 1.1 × 10²⁷ Pa | 2.5 g0 |

- The radial stress scales as `g0 c² / (8πG d)`, the project's earlier benchmark (5.25 × 10²⁷ Pa at 0.1 m), times 3.75 for this smooth profile. The tangential stress is larger by roughly `R/d` and flips sign through the wall. The earlier benchmark understated the stress for a spherical bubble.
- **It breaks the energy conditions.** With zero energy density, any tension violates the null energy condition; half the wall is in tension.
- **Restoring the energy conditions makes it loud.** Adding enough energy density to dominate the stress everywhere needs 1.5 × 10¹³ to 3.5 × 10¹⁴ kg. That mass pulls on everything nearby: 1 to 24 g0 at 10 m from the centre.
- **Clocks and rulers separate inside.** The clock potential is flat in the cabin; the ruler potential keeps Earth's slope. In this model slow matter is weightless inside while light still bends at half its usual rate.

## Wall 2: ordinary matter only

Energy density `(σ0/d)(1 + cos θ)`: a massive shell, twice as heavy at the top as average and empty at the bottom.

- Mass 1.1 × 10¹³ kg. All energy conditions satisfied.
- Cabin weightless.
- Outside: 6 g0 just above the top, zero just below the bottom, about 2 g0 at 10 m above the centre.
- The shell itself weighs 1.1 × 10¹⁴ N and needs supporting.

## What this establishes

1. **Three things cannot all hold:** a quiet outside, a cancelled inside, and the energy conditions. The pure-stress wall gives the first two; the ordinary shell gives the last two.
2. **A bubble isolates; it does not lift.** The quiet wall cancels the pull on the cabin's contents, but the contents still pull on the wall, so the craft as a whole weighs what its payload weighs. Hovering needs either outside support or a craft whose total energy is zero.
3. **The stress scale is about 10³⁰ Pa for a thin wall**, against roughly 10¹¹ Pa for the strongest materials. A thick wall lowers it only to about 10²⁷ Pa.
4. **For the driven wall (stage 3):** the thing to replace is a stress field of this size with zero net energy. A wave that averages to zero energy density but carries large alternating stress is the closest dynamic analogue, and the constraint that stress cannot alter the outside field is what a driven wall would have to live with or evade.

## Limits

- Linear in the potentials; this is accurate to about one part in 10¹⁵ here.
- The gravitational pull on the wall's own stress-energy is neglected in the balance of stresses. It is smaller than the stresses by about 13 orders.
- The smooth profile is one choice. Other profiles change the peak values by factors of order one, not the scalings.
- The light-bending statement holds within this model and has not been checked against a full treatment of the tensor part of the metric.

---

# Stage 3: the driven wall

**Date:** 2026-11-13. Script: `bubble_wall_driven.py`; figure: `fig5_driven_wall.png`; numbers: `results_driven.json`. All checks pass.

## Question

The static quiet wall needs tension with no energy behind it. Can a wall that is driven periodically, such as one that emits or traps a wave, cancel Earth's steady pull without that?

## Result

No, within general relativity and matter that obeys the energy conditions. Driving changes nothing about the requirement.

**Averaging.** In the weak-field equations, averaging over one period of a repeating source removes every time derivative. The averaged metric therefore obeys the static equations with the averaged source, and local conservation makes the averaged stress self-supporting. Every stage 1b result then applies to the averages of a driven wall: the average stress cannot change the average field outside, and the same average stress pattern is needed inside.

**A wave by itself averages to zero.** A wall whose mass distribution sloshes up and down gives the cabin an oscillating field with zero mean. Only quantities quadratic in the wave, its energy and stress, survive averaging.

**Bound.** The wall's upward pull at the cabin centre is `G ∫ ρ_active cos θ / r² dV`. The wall lies outside radius `R`, and the energy conditions cap the active density at four times the energy density. So, for a static or driven wall alike:

| Wall made of | Least mass-energy (5 m cabin) | Least energy | Least pull at 10 m | at 100 m |
|---|---|---|---|---|
| Anything obeying the dominant energy condition | 9.2 × 10¹¹ kg | 8.3 × 10²⁸ J | 0.61 m/s² | 6 × 10⁻³ m/s² |
| Radiation or moving particles | 1.8 × 10¹² kg | 1.7 × 10²⁹ J | 1.2 m/s² | 1.2 × 10⁻² m/s² |
| Cold matter | 3.7 × 10¹² kg | 3.3 × 10²⁹ J | 2.5 m/s² | 2.5 × 10⁻² m/s² |

The general form is `M ≥ g0 R² / (kG)` with `k = 4, 2, 1`, and the outside feels at least `g0 (R/r)² / k`. The stage 1 lopsided shell sits a factor three above the cold-matter bound.

**A wall of trapped waves.** Holding the minimum energy as electromagnetic waves in a wall 1 m thick needs a field of 7 × 10¹⁸ V/m (2 × 10¹⁰ T), about five times the field at which the vacuum breaks down into particle pairs. Even a 5 m wall is above that threshold.

**Negative energy.** Quantum fields can have negative energy density briefly. A bound of the Ford–Roman type limits how long: about 10⁻²² s for the 10²⁷ to 10³⁰ J/m³ the quiet wall needs. The coefficient of that bound is quoted from memory and should be checked against the original papers.

**Side effects of driving.** A wall of this mass modulated by 10% radiates gravitational waves weakly at 1 kHz (about 10⁻⁵ W) and enormously at 1 MHz (about 10¹³ W). A 1 g oscillating field pushes occupants by only 5 × 10⁻⁸ g at 1 kHz.

## What this establishes

1. **Within general relativity, a driven wall is no better than a static one.** The requirement is on averages, and the averages obey the static equations.
2. **Any wall that obeys the energy conditions has at least `g0 R² / (4G)` of mass-energy and cannot be quiet.** At 100 m its pull is still millions of times a gravimeter's resolution.
3. **Under the project's premise of a quiet craft, the bubble cannot be a general-relativistic source built from ordinary energy.** What remains: sustained negative energy beyond the quantum limit, a field that couples to matter more strongly than gravity does, or a mechanism that changes the craft's own response rather than generating a field.

## Limits

- First order in the potentials. Second-order effects of the oscillating field on occupants are the ponderomotive terms estimated above.
- The bound is for the pull at the cabin centre; uniform cancellation across the cabin needs more.
- Periodic steady state is assumed. A wall that is switched on once and radiates away is not covered.
