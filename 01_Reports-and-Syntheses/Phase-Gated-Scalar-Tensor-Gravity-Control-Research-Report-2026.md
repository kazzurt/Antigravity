# Phase-Gated Scalar–Tensor Gravity Control

## Requirements-first downselection, constraint audit, and next experiment

**Date:** 2026-07-16  
**Decision scope:** screened or state-dependent scalar–tensor fields, electromagnetic control, material-state gates, and their extrapolation to a protected craft worldtube  
**Reference case:** occupied length `L = 10 m`, commanded acceleration `a = g₀ = 9.80665 m s⁻²`  
**Evidence cutoff:** primary literature and official records located through 2026-07-16  
**Status labels:** **Established** = reproduced theory or accepted measurement; **limit** = experimental null/exclusion within the stated model; **extension** = explicit physics beyond GR/Standard Model; **working hypothesis** = coherent but unevidenced construction; **speculation** = missing action, source, or conservation closure.

---

## Executive verdict

### Plain-language answer

**No technically defensible craft window was found for phase-gated scalar–tensor control.** A covariant scalar theory can be stable; a scalar can act nearly universally through a physical metric; screening can hide it; an electromagnetic invariant can source it; and a material order parameter can, in principle, change its local mass. Those statements can all be true separately. They do not remain useful when the complete craft requirements are imposed together.

The best explicit architecture is a conformally coupled scalar with a phase-dependent mass barrier,

`electrical drive → material phase → scalar mass/boundary switch → scalar profile → physical-metric response`.

It has a **nonempty laboratory boundary-switch window**, roughly

`m_out ≲ 2 × 10⁻⁸ eV`, `m_wall ≳ 2 × 10⁻⁵ eV`

for a `10 m` interior and a `1 cm` wall. This is a real EFT statement: the field can be long-ranged in the cabin and evanescent in the wall. It is not yet a propulsion mechanism. The switch supplies no directed scalar gradient, no external momentum reservoir, and no gain. If the scalar source is attached to the craft, the forces on field, source, hull, and payload sum to zero. If the field is Earth-sourced, present unscreened scalar–tensor bounds limit the extra Earth acceleration to about `1.2 × 10⁻⁵ g`; screening makes the accessible source charge smaller. If scalar radiation supplies momentum in deep space, the minimum power is `P ≥ M_c a c`, or `2.94 × 10¹⁴ W` for a deliberately modest `10⁵ kg` craft at `1 g`, before inefficiency or interior-frame control.

The material-state part also fails quantitatively. A `1 kg` niobium source changes its conventional mass by only about `2.1 × 10⁻¹⁷ kg` across the zero-field condensation-energy budget. At `5 cm`, its standard gravitational state-reversal signal is only `5.5 × 10⁻²⁵ m s⁻²`. A phase-specific portal large enough to replace that `10⁻¹⁷` switch fraction by an order-one scalar-charge switch is new composition-dependent physics. It must survive the direct superconducting equivalence-principle limit `η_Nb*−Cu ≤ 2.0 × 10⁻⁹`, general WEP tests, short-range fifth-force tests, radiative corrections, and the fact that dense hull and payload bodies are screened in the same models used to hide the source. The 2025 niobium experiment is a null result, not evidence for an anomalous superconducting coupling ([Ross et al. 2025](https://doi.org/10.1103/PhysRevD.111.L021101)).

### Exact incompatibility

The scalar branch stops at the conjunction

> **large controllable universal response + externally quiet screening + unsuppressed craft/source charge + identified energy and momentum reservoir.**

No assessed family supplies all four:

1. **Unscreened conformal scalar:** universal and simple, but PPN/inverse-square bounds make an Earth-sourced field at least `8.7 × 10⁴` too weak for `1 g`; the canonical `1 g` gradient stores at least `5.0 × 10¹⁵ J m⁻³` when the Cassini coupling bound is imposed.
2. **Chameleon/symmetron/dilaton:** can hide external signatures, but their thin-shell or least-coupling behavior also suppresses the scalar charge of the source, hull, occupants, and payload. The basic cosmological chameleon parameter space was experimentally excluded as a dark-energy explanation by a levitated force sensor ([Yin et al. 2022](https://doi.org/10.1038/s41567-022-01706-9)); 2025 symmetron limits improved portions of its three-dimensional parameter space by more than six orders while leaving model-dependent regions open ([Yin et al. 2025](https://doi.org/10.1038/s41550-024-02465-8)). Open parameter space is not a source or reservoir.
3. **Kinetic/Vainshtein screening:** becomes strongest precisely where the engineered gradient is large. It is an actuator suppressor, not a material switch.
4. **Electromagnetic production:** a `10 T` magnetic field carries `3.98 × 10⁷ J m⁻³`, equivalent to `4.43 × 10⁻¹⁰ kg m⁻³`. Even an ideal `1 m³`, `10 T` source at `10 m`, using the model-specific CAST ceiling `βγ = 5.7 × 10¹⁰` and an already extreme `βm = 10⁶`, gives only about `3.4 × 10⁻⁵ m s⁻²` before screening. A travelling plane wave does not help because `FμνF^μν = 0`.
5. **Phase wall or trapped domain:** can switch penetration and stored field energy but cannot accelerate its own closed source–craft system. An external scalar gradient, beam, Earth, or emitted flux must still carry momentum.

### Decision and redirection

**Craft decision: NO-GO for phase-gated scalar–tensor fields as the lead propulsion architecture.**  
**Laboratory decision: CONDITIONAL GO for one necessary-phenomenon experiment:** search for an external, phase-correlated scalar charge that exceeds the known condensation/stress-energy change, reverses in the same apparatus, follows a Yukawa spatial law, and accelerates composition-paired detectors equally. This is a fundamental-force experiment, not a propulsion claim.

The next lead is **requirements-first physical-metric/worldtube inverse design with a complete exterior stress-energy and momentum map**. Its first milestone is to solve the weakest bounded subluminal worldtube geometry—interior, transition shell, exterior, formation history, ADM momentum, and environmental coupling—then test explicit source sectors against the resulting tensor, pressure, and momentum requirements. This lane does not promise easy source engineering; it repairs the scalar branch’s central defect by making the full protected region and conservation closure the object being designed.

---

## 1. Craft-level invariant requirements

### 1.1 The physical target is a worldtube, not a force reading

Let `W` be the occupied spacetime worldtube and `g̃μν` the **physical metric** followed by ordinary matter and clocks. A minimally useful configuration must satisfy all of the following:

1. A reference timelike curve `Γ ⊂ W` changes trajectory relative to the asymptotic exterior.
2. Freely suspended hull elements, occupants, and payload follow nearly the same congruence:

   `uν g̃∇ν uμ ≈ 0` inside `W`.

3. Geodesic deviation is limited throughout the occupied region:

   `d²ξi/dt² = −c² R̃i0j0 ξj`,

   with `||c²R̃i0j0||` below a declared tidal tolerance.
4. The transition shell lies outside occupied volume, because the commanded acceleration must change from its interior value to the exterior value somewhere, and that change creates curvature or field stress.
5. The exterior field, radiation, wake, and momentum flux are specified. Exact compact support is unavailable for a linear massless scalar without compensating surface charge; a massive field has a Yukawa tail.
6. Formation and shutdown are included. A static target metric alone does not say how energy and momentum enter it.

This definition is weaker than a warp drive: it asks only for a bounded, low-tidal, subluminal local frame. It is stronger than a uniform fifth-force demonstration because it includes the hull, biological matter, payload, boundary, environment, and conservation law.

### 1.2 Weak-field requirement for `1 g` over `10 m`

Write the physical weak-field metric as

`d s̃² = −(1 + 2 Φeff/c²)c²dt² + (1 − 2 Ψeff/c²)δij dxi dxj`.

For slow massive matter,

`a = −∇Φeff`.

A nearly uniform `1 g` field over `L = 10 m` therefore requires

`ΔΦeff = aL = 98.0665 m² s⁻²`,

and

`|Δg̃00| = 2aL/c² = 2.18 × 10⁻¹⁵`.

The dimensionless metric difference is small. The hard requirements are its gradient, bounded transition, source, and stress-energy—not a large value of `h00`.

Define a maximum fractional acceleration variation `εT` across the cabin. In the Newtonian limit the electric part of the physical Riemann tensor is

`Eij ≡ c² R̃0i0j ≈ ∂i∂j Φeff`,

so

`||Eij|| ≲ εT a/L`.

For a one-percent tolerance,

`||Eij|| ≲ 9.81 × 10⁻³ s⁻²`.

Across a `2 m` body this permits a differential acceleration of about `0.0196 m s⁻²` (`0.002 g`). A stricter biological or precision-payload limit can be inserted by replacing `εT`.

If the interior acceleration falls to zero across a shell of thickness `δ`, a mean-value bound gives

`|∂a/∂x| ≳ a/δ`.

At `δ = 1 m`, the shell contains a tidal scale near `9.8 s⁻²`, one thousand times the one-percent occupied-region limit. The shell must therefore be outside the occupied volume and its stresses must be explicitly carried.

### 1.3 What a uniform fifth force does—and does not do

A universal scalar force can accelerate freely suspended massive bodies together. If the hull is mechanically compliant or its elements share the same charge-to-inertial-mass ratio, this can greatly reduce internal support loads. That is useful.

It does **not** automatically provide:

- a bounded low-tide transition;
- the same response for a screened bulk hull, unscreened atoms, liquids, and biological tissue;
- control of photons, air, plasma, dust, or incoming projectiles;
- a field source that moves the craft’s center of mass;
- an external momentum sink;
- low proper acceleration when ordinary radiation recoil or a mechanical source accelerates only the hull.

A purely conformal scalar also leaves electromagnetic null cones unchanged in four dimensions at leading order. Massive matter can share a scalar acceleration while light and environmental radiation do not receive the same scalar force. A fifth-force cabin is therefore not yet a protected environmental worldtube.

### 1.4 Exterior and boundary conditions

For a field of mass `mφ`, range

`λφ = ħ/(mφ c)`,

craft-scale penetration requires

`mφ ≲ ħ/(cL) = 1.97 × 10⁻⁸ eV`.

A localized source then has an exterior Yukawa tail `e^(−r/λφ)/r`. A wall can attenuate it if the in-wall mass satisfies `mwall d/(ħc) ≳ 1`, but the wall feels the corresponding scalar stress. A localized, approximately uniform interior gradient also needs asymmetric boundary values or opposite effective scalar charges. Ordinary positive mass with a single-sign universal coupling supplies only one sign of scalar charge; two such walls do not make a localized dipole field without an additional sector or a coupling that crosses zero.

### 1.5 Universality requirement

The strongest implementation is universal minimal coupling to one physical metric `g̃μν`. Then every Standard Model matter field used in the hull, occupants, and payload derives its motion from the same action. Approximate universality must cover:

- nuclei with different neutron fractions and binding energies;
- electrons and electromagnetic binding energy;
- normal and superconducting electrons;
- magnetic and unpolarized material;
- gases, fluids, biological tissue, and structural solids;
- macroscopic bodies whose screening factor may depend on radius and density.

Composition-dependent scalar charges are fifth forces, not metric gravity. MICROSCOPE’s result,

`η(Ti,Pt) = [−1.5 ± 2.3(stat) ± 1.5(syst)] × 10⁻¹⁵`,

strongly limits differences of scalar charge-to-mass ratios, but it does not exclude a mathematically perfect universal coupling by itself ([Touboul et al. 2022](https://doi.org/10.1103/PhysRevLett.129.121102)). Universal models are instead limited by inverse-square tests, PPN parameters, source strength, and radiation.

### 1.6 Hovering and terrestrial acceleration

At fixed altitude a craft is not on an Earth geodesic. A protected hover requires an upward effective gradient of approximately `g`, not merely “gravity cancellation.” Turning off the craft’s response to Earth would produce local inertial motion—free fall relative to the surface—unless another interaction supplies upward acceleration.

Three conservation-complete terrestrial cases exist:

1. **Earth-coupled scalar sail:** Earth and craft exchange momentum through a scalar field. The force direction and sign are determined by scalar charges. An ordinary attractive universal scalar adds downward acceleration; upward force needs opposite effective charge or an externally maintained field.
2. **Ground/external projector:** the projector recoils and supplies field energy. This is propulsion relative to infrastructure, not a closed craft drive.
3. **Directed radiation:** scalar, electromagnetic, or matter radiation carries momentum. The craft recoils and must separately protect its interior from proper acceleration.

Steady ideal hovering need not perform mechanical work on a stationary craft, but field establishment, losses, and momentum transfer remain physical. The Earth or projector receives the opposite momentum.

### 1.7 Deep-space acceleration

In asymptotically empty space a closed, stationary internal scalar configuration cannot change total center-of-mass momentum. The integrated conservation law is

`dPcraft/dt = − ∮ (Tfield + Tradiation)i j nj dA`,

where the surface encloses craft and internal sources. Nonzero thrust requires flux through the surface or interaction with an external field/source.

For collimated massless radiation, `F ≤ P/c`; for massive emitted quanta, `E/p = c²/v ≥ c`, so the power bound is no better:

`P ≥ F c = Mc a c`.

At `a = g₀`:

| Craft mass `Mc` | Minimum directed-radiation power |
|---:|---:|
| `10⁵ kg` | `2.94 × 10¹⁴ W` |
| `10⁶ kg` | `2.94 × 10¹⁵ W` |

This is a momentum bound, independent of scalar model details. An external background can evade the onboard radiation power bound only by becoming the named energy/momentum reservoir.

---

## 2. Minimum viable covariant scaffold

### 2.1 Frame choice, units, and fields

Use signature `(-,+,+,+)`. Derivations in this section use `ħ = c = 1`; numerical evaluations restore SI units. The reduced Planck mass is

`MPl = (8πG)⁻¹/² = 2.435 × 10¹⁸ GeV`.

Choose an Einstein-frame basis to avoid counting both a variable `F(φ)R` and a conformal matter factor as independent observables:

`S = ∫ d⁴x √−g [ MPl²R/2 − (∂q)²/2 − V(q) − BF(q)FμνF^μν/4 − Ugate(q,Ψ) ]`

`    + Sgate[Ψ, Aμ, gμν, uμ] + Sm[g̃μν, ψm]`,

with

`g̃μν = A²(q)[gμν + D(q)∂μq∂νq/MD⁴]`.

Definitions:

- `gμν`: Einstein-frame metric; `R` is its Ricci scalar.
- `g̃μν`: physical metric seen universally by ordinary matter in the baseline model.
- `q`: canonically normalized real scalar, mass dimension one.
- `V(q)`: scalar potential, mass dimension four.
- `A(q)`: positive dimensionless conformal factor.
- `D(q)/MD⁴`: optional disformal coefficient, mass dimension minus four after `D` is chosen dimensionless.
- `Aμ`, `Fμν = 2∂[μAν]`: electromagnetic potential and field strength.
- `BF(q) > 0`: dimensionless electromagnetic kinetic function. `BF = 1` in standard electrodynamics.
- `Ψ`: a covariantly represented material order parameter or set of medium fields.
- `uμ`: material four-velocity, required because a condensed-matter state itself selects a rest frame even when the fundamental action is covariant.
- `Ugate`: explicit scalar–material interaction energy density.
- `ψm`: all other matter fields.

The minimal downselection sets `D = 0`. Disformal coupling is evaluated separately because its derivative force vanishes or is velocity/gradient suppressed in the static smooth limit that the craft needs.

Define the dimensionless conformal coupling

`β(q) ≡ MPl d ln A/dq`.

For comparison with the common Damour–Esposito-Farèse convention, `αDEF = √2 β` when their dimensionless scalar has kinetic term `−2(∂ϕ)²` inside `c³/(16πG)`.

### 2.2 Relation to a Jordan-frame `F(φ)R` action

Starting from

`MPl²F(φ)R/2 − Z(φ)(∂φ)²/2`,

a conformal transformation to the Einstein frame is allowed where `F > 0`. The scalar has a healthy kinetic term only if

`K(φ) = Z/F + (3MPl²/2)(F′/F)² > 0`.

The observable matter conformal factor becomes the combination `Amatter/√F`. Thus “varying the Planck mass,” “adding a conformal fifth force,” and “changing the tensor coupling” are frame-dependent descriptions of overlapping physics unless the physical matter metric is fixed first. A genuine time- or space-dependent effective Planck mass also changes post-Newtonian gravity and gravitational-wave propagation/amplitude and is not a free gain coefficient.

### 2.3 Field equations for the conformal baseline

Define Einstein-frame stress tensors by variation with respect to `gμν`, and let `Tm = gμνTmμν`. With `D = 0`, variation gives

`MPl²Gμν = T(q)μν + BF T(EM)μν + T(gate+portal)μν + Tmμν`,

where

`T(q)μν = ∂μq∂νq − gμν[(∂q)²/2 + V]`,

while `T(gate+portal)μν` is the variation of `Sgate − ∫√−g Ugate`. This assignment includes the portal once and retains any metric dependence carried by the medium fields and `uμ`. Also,

`T(EM)μν = FμαFν α − gμν FαβF^αβ/4`.

The scalar equation is

`□q = V,q + Ugate,q + BF,q FμνF^μν/4 − [β(q)/MPl] Tm`.

For nonrelativistic matter, `Tm ≈ −ρE`, so a positive `β` sources the scalar with `+βρE/MPl`, as required by the usual chameleon effective potential. Here `ρE` is rest-energy density; in natural units it is normally denoted simply `ρ`, while in SI `ρE ≈ ρmass c²`. The Maxwell equation is

`∇μ[BF(q)Fμν] = Jν`,

with additional material polarization currents contained in `Jν` or `Sgate`.

The Einstein-frame matter tensor is not separately conserved:

`∇μTmμν = [β(q)/MPl] Tm ∇νq`.

The scalar divergence carries the opposite exchange, and the `BF` and `Ugate` terms exchange energy–momentum with the electromagnetic and gate sectors. Diffeomorphism invariance enforces

`∇μ T(total)μν = 0`.

This conservation identity is the required accounting ledger. A material switch can redirect energy and momentum among sectors; it cannot create either.

### 2.4 Physical-metric and fifth-force response

Matter follows geodesics of `g̃μν = A²gμν`. In the Einstein frame, a massive point body obeys

`uν∇νuμ = −[β/MPl](gμν + uμuν)∇νq`.

In the weak, slow limit,

`a = −∇ΦN − c²[β(q)/MPl]∇q`.

For a constant ambient coupling and an unscreened source/test pair, the potential is

`V12(r) = −Gm1m2/r [1 + 2β1β2 e^(−mqr)]`,

and

`aφ/aN = 2βsβt (1 + r/λq)e^(−r/λq)`.

If the same `A(q)` applies to all matter, this is a scalar part of a universal physical metric. If `βi` depends on composition, phase, spin, or species, it is a nonmetric fifth force. Screening can make the macroscopic `βeff` body-size dependent even when the microscopic action is universal; that is a practical violation of craft universality.

### 2.5 Electromagnetic production is an explicit new interaction

Expand

`BF(q) = 1 + q/Mγ + … = 1 + βγ q/MPl + …`.

Then a static electromagnetic invariant sources `q`. In SI notation,

`FμνF^μν = 2(B² − E²/c²)`

up to the chosen field-unit convention. A travelling plane wave has `E = cB`, `E ⟂ B`, and therefore `F² = 0`; a single ideal laser beam is not a source for the scalar operator `qF²`. Static magnetic fields, capacitors, standing waves, or non-null crossed-field configurations are required. A pseudoscalar operator `qFμνF̃^μν ∝ q E·B` is distinct and does not by itself provide universal metric coupling.

The classical electromagnetic stress tensor is traceless, so a purely conformal `qTm` coupling does not make radiation an efficient scalar source. `BF(q)` is additional physics and also makes the fine-structure constant field dependent, approximately

`δαEM/αEM ≈ −δBF/BF`.

Photon conversion, atomic clocks, varying constants, stellar production, and WEP tests therefore constrain this control channel.

### 2.6 Stability and EFT consistency conditions

An operating point is admissible only if:

- `MPl² > 0` (or `F > 0` in Jordan variables): no graviton ghost;
- the canonical scalar kinetic coefficient is positive;
- `BF(q) > 0`: no photon ghost;
- `meff² = V,qq + Ugate,qq + (BF,qq/4)F² − (T/MPl)β,q` is nonnegative on a stable branch;
- a deliberately tachyonic symmetron/scalarization transition is stabilized by higher terms and has a controlled growth rate;
- the physical metric is Lorentzian and invertible. For a disformal term this requires `A² > 0` and the corresponding determinant factor, schematically `1 + D X/MD⁴`, not to cross zero;
- propagation is hyperbolic. For a k-essence `P(X)`, `PX > 0` and `PX + 2X PXX > 0`, with `cs² = PX/(PX + 2X PXX) > 0`;
- the EFT cutoff exceeds inverse wall thickness, modulation frequency, field gradients, and material excitation scales;
- loops do not raise an intended `10 m` scalar mass far above `2 × 10⁻⁸ eV` without a symmetry or quantified tuning.

The canonical conformal scaffold has tensor speed `c`. It therefore survives the direct GW-speed test that rules out many derivative-curvature scalar–tensor terms: GW170817/GRB 170817A bounded the fractional gravity–light speed difference to approximately `−3 × 10⁻¹⁵` to `+7 × 10⁻¹⁶` ([LIGO/Virgo/Fermi/INTEGRAL 2017](https://doi.org/10.3847/2041-8213/aa920c)). This survival is not evidence for the scalar; it only avoids that particular exclusion.

### 2.7 Role separation

| Role | Mathematical object | What it can do | What it cannot be credited with |
|---|---|---|---|
| Added fifth force | `β∇q/MPl` with species-dependent `βi` | Accelerate selected matter | Metric universality or protected photons/environment |
| Universal physical metric | common `g̃μν` | Make all minimally coupled matter geodesic | Supply a source, low-tide boundary, or momentum sink |
| Effective Planck mass | `F(q)R` in Jordan variables | Change tensor/scalar mixing | Independent gain after frame transformation |
| Environmental screening | `meff(ρ)`, `A,q(ρ)`, or nonlinear kinetic terms | Hide fields or charges | Preserve an unsuppressed source automatically |
| Material gate | `Ugate(q,Ψ)` | Change mass, minimum, or boundary transmission | Create directed field energy or net momentum |
| EM production | `BF,q F²/4` | Convert non-null EM fields into scalar excitation | Free amplification; it is constrained new physics |

---

## 3. Source–gate–field–response–reservoir chain

### 3.1 The only coherent phase-gated chain

The strongest surviving **laboratory** architecture is

`electrical input`

`→ heater/coil changes Ψ`

`→ Ugate changes meff or a boundary value for q`

`→ a pre-existing, stored, Earth-sourced, or pumped q field is transmitted/blocked/reshaped`

`→ g̃μν = A²(q)gμν changes massive-matter motion`

`→ scalar stress, radiation, or an external source receives the opposite momentum`.

Every arrow is explicit in the action. The word **gate** belongs only to the second and third arrows. The energy and momentum reservoir enters at the fourth and sixth arrows.

### 3.2 Where apparent gain could reside

| Claimed gain | Actual reservoir | Viability |
|---|---|---|
| Direct EM-to-scalar conversion | Applied field energy and power supply | Conservation-complete, but source energy density and allowed couplings are too small for the reference craft case |
| Switching a background | Cosmological, Earth, solar, or engineered scalar field | Transistor-like gain is possible in principle; no `1 g` background compatible with known local dynamics has been identified |
| Releasing stored field energy | Scalar domain/cavity plus its charging source | Finite impulse; wall and charging apparatus receive stress and recoil |
| Changing coupling to Earth | Earth is momentum sink | A scalar sail, not closed propulsion; unscreened universal strength is PPN-limited and ordinary sign is attractive |
| Scalar/particle radiation | Emitted momentum flux | Valid propulsion; `P ≥ Fac` and hull recoil does not itself protect occupants |
| Closed internal static field | None | Inconsistent as net propulsion |

### 3.3 Why a phase wall is not an engine

A phase wall with high `meff` can reflect or attenuate a scalar wave and can alter the static field energy in a cavity. The wall feels the equal and opposite scalar pressure. If the wall, source, hull, and payload are included inside one control surface, total momentum changes only by external flux. This remains true if the wall is superconducting, magnetic, ferroelectric, or a Josephson array. A useful experiment can detect the pressure or altered external profile; a useful craft requires an external beam/background or radiation exhaust.

---

## 4. Screening and coupling downselection

### 4.1 What a controllable screen must accomplish

For this project, a screen is useful only if it does all four of the following:

1. permits a long-range field in the occupied and interaction regions;
2. changes state under an engineerable material or electromagnetic variable;
3. leaves enough scalar charge on the external source and enough response in the craft, occupants, and payload;
4. carries its own stress and recoil consistently.

The first three requirements conflict in the standard mechanisms. Environmental screening works by suppressing precisely the charge or gradient that an actuator would need. The conflict is not a theorem for every nonlinear field theory, but it is present in each controlled family below.

### 4.2 Family comparison

| Family | Controlled quantity | Environmental switch | Direction and universality | Source-screening problem | Verdict for active control |
|---|---|---|---|---|---|
| Chameleon / thin shell | `meff(ρ)` and effective scalar charge | Ambient trace density, chamber size | Gradient follows mass/boundary geometry; conformal response can be universal | Dense source and dense craft acquire thin shells, `βeff ≈ 3β ΔR/R` | Strong laboratory target, poor craft actuator; basic dark-energy parameter space tested is closed |
| Symmetron | Vacuum expectation value and coupling `A,q ∝ q` | Symmetry restored above `ρcrit = μ²Ms²` | Gradient follows domains and sources; common conformal metric possible | Dense material drives `q → 0`, suppressing both source and detector coupling | Best mathematical analogue of a phase gate, but an ordinary condensed-matter transition does not move `ρ` enough |
| Dilaton / Damour–Polyakov | Distance from a minimum of `A(q)` | Density-dependent least-coupling point | Approximately universal near the minimum | The mechanism hides the force by making `A,q` small | Excellent evasion mechanism, intrinsically weak actuator unless a new portal moves the minimum |
| K-mouflage | Kinetic coefficient `K′(X)` | Large gradient `X` | Can be conformal and universal; profile need not follow simple Yukawa form | The intended large gradient increases the screening coefficient | No natural material switch; high-gradient operation defeats the desired response |
| Vainshtein / Galileon | Derivative self-interactions | Source mass and Vainshtein radius | Conformal scalar component can be universal | Nonlinear region suppresses scalar gradients around the source | No identified laboratory phase analogue; derivative EFT and radiation require separate control |
| Spontaneous/dynamical scalarization | Tachyonic compact-object mode | Compactness and negative quadratic matter coupling | Effectively metric in scalar–tensor models | Requires relativistic compactness; laboratory matter is too dilute | No laboratory material analogue from known energies |
| Disformal coupling | Derivative part of the physical metric | `∂q`, velocity, or stress background | Formally common metric if universal | Static nonrelativistic response is derivative/velocity suppressed | Useful discriminator, not a source or gate by itself |
| Photon/invariant coupling | `BF,q F²` or pseudoscalar `q F F̃` | Non-null EM invariant | Creates or mixes a scalar; matter response is separately set by `A(q)` | Conversion bounds and varying-constant limits constrain it | Legitimate pump channel, quantitatively inadequate in the benchmark below |

### 4.3 Chameleon: density gating also gates the charge

With, for example, `V(q) = Λ^(4+n)/q^n` and `A(q) ≈ exp(βq/MPl)`, nonrelativistic matter gives

`Veff(q) = V(q) + ρ A(q)`.

Its minimum and mass depend on density. A spherical body of Newtonian surface potential `ΦN` is thin-shell screened when

`ΔR/R ≈ [q∞ − qc]/(6 β MPl ΦN) ≪ 1`,

and its far-field charge is reduced from `β` to approximately `βeff = 3β ΔR/R`. That reduction applies to a source plate, hull, and macroscopic test mass. A vacuum gap may unscreen the field without unscreening the dense bodies that have to source and feel it.

This is no longer a merely qualitative objection. A levitated force sensor excluded the entire physically plausible parameter region of the tested cosmological chameleon model ([Yin et al. 2022](https://doi.org/10.1038/s41567-022-01706-9)). Earlier atom-interferometer, neutron, torsion-balance, and afterglow experiments close complementary regions. Quantum stability supplies another tension: requiring matter-loop corrections not to dominate gives approximately `m ≲ 0.0073 (ρ/10 g cm⁻³)^(1/3) eV`, while laboratory limits required `m ≳ 0.0042 eV` for gravitational-strength coupling in the benchmark analyzed by [Upadhye, Hu, and Khoury](https://doi.org/10.1103/PhysRevLett.109.041301). The narrowness of that historical interval is not a universal exclusion of every chameleon potential, but it illustrates the radiative price of hiding a strong coupling.

**Decision:** do not continue the basic inverse-power dark-energy chameleon as the craft lead. Use chameleon apparatus results as mature constraints and methods for any new phase wall.

### 4.4 Symmetron: the closest mathematical gate, but the wrong state variable

The canonical symmetron has

`V(q) = −μ²q²/2 + λs q⁴/4`, `A(q) ≈ 1 + q²/(2Ms²)`,

so that

`Veff(q) = 1/2 (ρ/Ms² − μ²)q² + λs q⁴/4`.

At `ρ > μ²Ms²`, the symmetric phase `q = 0` is stable and the matter coupling `A,q` vanishes. At lower density, `q = ±μ/√λs` and the coupling turns on. This is a true field-theory gate, but its ordinary control variable is mass density, not superconducting phase, spin order, or Josephson phase. A niobium transition changes the total trace-energy density only at the `~2 × 10⁻¹⁷` level calculated in Section 5. A material-specific portal must therefore be added; the symmetron no longer explains the gate by itself.

Levitated tests published in 2025 improved laboratory symmetron bounds by more than six orders of magnitude in parts of parameter space while leaving model-dependent islands ([Yin et al. 2025](https://doi.org/10.1038/s41550-024-02465-8)). Surviving islands are not automatically actuator windows: dense sources and detectors can remain symmetry-restored and scalar-neutral.

**Decision:** retain a generalized symmetron mass-wall model as the cleanest falsifiable laboratory scaffold, not as a craft-scale solution.

### 4.5 Dilaton / Damour–Polyakov least coupling

Damour–Polyakov models arrange a minimum of the matter-coupling function, schematically

`A(q) ≈ A* [1 + ad (q − q*)²/(2MPl²)]`.

Environmental evolution drives `q` toward `q*`, so the local coupling `β(q) = MPl d ln A/dq` becomes small. This can make a fundamentally strong sector appear weak while producing composition dependence only through residual nonuniversal radiative couplings. It is physically controlled and compatible with a common metric at leading order.

For active control, however, the useful quantity is exactly the one the mechanism minimizes. A phase-dependent term that shifts `q*` by a large amount must be new and material-specific, and it reintroduces WEP and varying-constant constraints during the switched state. The ambient field can provide a reservoir, but no locally allowed ambient gradient close to `1 g` is known.

**Decision:** viable hiding mechanism; no identified gain or directional source.

### 4.6 Kinetic screening: large commanded gradients self-suppress

K-mouflage replaces the canonical kinetic term with `M⁴ K(X)`, where `X = −(∂q)²/(2M⁴)`. In quasistatic form,

`∇·[K′(X)∇q] = βρ/MPl`.

When `K′` grows at large `|X|`, the same source produces a smaller gradient. Stability requires the analogues of `K′ > 0` and `K′ + 2XK″ > 0`; the characteristic speed is not generically luminal, and some otherwise viable examples contain superluminal scalar characteristics. The local field may also fail to align with the Newtonian field in nonspherical configurations ([Brax and Valageas 2014](https://doi.org/10.1103/PhysRevD.90.123521)).

A material phase could in principle change coefficients of `K(X)`, but that is another portal with an EFT cutoff. More importantly, the `1 g` gradient is the regime that triggers the suppression. Kinetic nonlinearities can create thresholds and geometry dependence, but no resonance-like free gain: the nonlinear field stress supplies the missing accounting.

**Decision:** not the phase-gate lead. Revisit only after an experimentally observed scalar exists whose large gradients require control.

### 4.7 Vainshtein screening and Galileon-like sectors

Derivative interactions such as `(∂q)² □q/Λ³` generate a Vainshtein radius around massive sources. Inside it, nonlinear derivative terms dominate and reduce the scalar fraction of the force. This makes a cosmological scalar compatible with Solar-System tests but suppresses laboratory production by the same ordinary source. It is controlled by mass and geometry, not an order parameter. Radiation from binaries or driven sources can be screened differently from the static force, so static screening cannot be assumed to eliminate energy loss.

The exact GW-speed constraint is model dependent: the minimal conformal cubic Galileon is not identical to the derivative-curvature operators excluded after GW170817. Nevertheless, any proposed derivative completion must independently demonstrate luminal tensor propagation, hyperbolicity, a cutoff above the wall scale, and radiative stability.

**Decision:** no credible material switch or laboratory gain; not selected.

### 4.8 Scalarization has no laboratory compactness analogue

In the Damour–Esposito-Farèse construction, a coupling such as `A(q) = exp(βDEF q²/2MPl²)` with sufficiently negative `βDEF` makes the GR-like branch tachyonic inside a compact star. Nonlinear terms stabilize a scalarized star. The trigger is relativistic self-gravity: neutron-star compactness is `GM/(Rc²) ~ 0.1–0.3`, whereas a kilogram-scale, decimetre laboratory body has compactness of order `10⁻²⁶–10⁻²⁷`. Condensation energy and spin polarization do not repair 25 orders of compactness.

Binary-pulsar timing has progressively closed the massless scalarization window for observed neutron-star masses ([Zhao et al. 2022](https://doi.org/10.1088/1361-6382/ac69a3)). Massive or more elaborate scalarization remains possible, but it is an astrophysical nonlinear phenomenon, not a demonstrated condensed-matter analogue.

**Decision:** reject laboratory scalarization analogies unless an explicit portal supplies and stabilizes the negative mass squared; then analyze it as a new phase-gate model, not as inherited neutron-star physics.

### 4.9 Conformal versus disformal response

A universal conformal factor changes clocks, rods, massive-particle trajectories, and binding energies coherently. For a light scalar, however, it also produces a static fifth force and a PPN scalar unless screened. A universal disformal term can preserve a common physical metric, but for a static, slowly varying source its leading effects involve derivatives of `q` and particle velocity. It is therefore not a substitute for a static `1 g` conformal potential. Large disformal gradients face metric-invertibility, causality, cutoff, and radiation constraints ([Koivisto, Mota, and Zumalacárregui 2012](https://doi.org/10.1103/PhysRevLett.109.241102)).

### 4.10 New 2026 model-building developments

Two current results sharpen, but do not overturn, the downselection:

- Bonanno and Glaviano construct a UV-complete scalar–tensor model with a phenomenologically viable parameter wedge ([peer-reviewed, 2026](https://doi.org/10.1103/q1gq-sgy3); [arXiv:2605.10338](https://arxiv.org/abs/2605.10338)). It matters because UV completion and fifth-force viability can coexist. The paper does not supply a material phase gate, a directional local source, or a craft momentum reservoir.
- Homma, Katsuragawa, and Matsuzaki propose a symmetry-based suppression of fifth forces with metre-scale ranges and small dimensionless couplings ([preprint, arXiv:2604.20292](https://arxiv.org/abs/2604.20292)). It is relevant as a new screening idea, but remains a preprint and likewise does not yet close the source–gate–reservoir chain.

These are reasons to keep a tightly defined scalar laboratory lane, not reasons to restore the scalar as the craft architecture.

---

## 5. Material-state gating: operators, ordinary scale, and required new physics

### 5.1 Universal conventional coupling sees total stress-energy

For a conformal scalar, the conventional nonrelativistic source is the trace `T ≈ −ρc²` including rest mass, binding, pressure, and internal energy. Changing a phase therefore changes scalar charge by, at most, its changed total energy divided by `c²`, apart from small pressure terms. Coherence does not multiply this conserved source. The material can have an enormous electromagnetic susceptibility while its gravitational mass changes only by `ΔE/c²`.

For a `10 T` magnetic field,

`uB = B²/(2μ0) = 3.98 × 10⁷ J m⁻³`,

`ρB = uB/c² = 4.43 × 10⁻¹⁰ kg m⁻³`.

That is about `5 × 10⁻¹⁴` of the rest-energy density of a typical solid. It is a real GR and scalar source, but not a hidden amplification.

For niobium, using `ρNb = 8570 kg m⁻³` and a representative thermodynamic critical field `Bc ≈ 0.2 T`,

`ucond ≈ Bc²/(2μ0) = 1.59 × 10⁴ J m⁻³`,

`ucond/(ρNb c²) = 2.07 × 10⁻¹⁷`.

A `1 kg` sample has volume `1.17 × 10⁻⁴ m³`, condensation energy about `1.86 J`, and mass difference only `2.07 × 10⁻¹⁷ kg`. These deliberately favorable order-of-magnitude values already show why a conventional universal coupling cannot make superconducting order a useful source switch.

### 5.2 Candidate-gate operator audit

| Gate | Lorentz- and gauge-invariant operator in a medium EFT | Conventional changed source | What a useful switch additionally requires | Principal discriminator |
|---|---|---|---|---|
| Superconducting amplitude | `Ψ†Ψ`, `(DμΨ)†DμΨ` | Condensation, magnetic, kinetic, strain energy | Large `κSC(Ψ†Ψ)q²` or phase-dependent boundary term not proportional to total energy | Same sample above/below `Tc`, zero trapped flux, calorimetric normalization |
| Superconducting phase / Josephson state | `(DμΨ)†DμΨ`; across a junction `Ψ1* W Ψ2 + c.c.` with Wilson line `W` | Junction and current energy | Explicit portal to gauge-invariant phase difference; absolute phase is not observable | Reverse phase/current at fixed heat and field; distinguish `I`, `I²`, and `cos δ` scaling |
| Magnetic / antiferromagnetic order | `MμMμ`, `LμLμ`, exchange and anisotropy invariants | Zeeman, exchange, magnetostriction energy | Scalar even portal `κM M²q²`; axial linear coupling is spin-dependent, not universal | Reverse order with compensated external field and nonmagnetic detectors |
| Spin polarization / DNP | For a scalar, even combinations such as `SμSμ`; for a pseudoscalar, derivative `∂μq Sμ` | Polarization and hyperfine energy | An anomalously large spin portal; it necessarily distinguishes spin/composition unless metric coupling dominates separately | Polarized/depolarized reversal at fixed mass and temperature |
| Structural / ferroelectric / CDW | `Q²`, `PμPμ`, strain invariants `uμνuμν`, `ρQ*ρQ` | Latent heat, elastic, electronic binding energy | Portal that changes `meff` rather than merely adding `ΔE/c²` | First/second-order transition, hysteresis, domain and orientation scaling |
| Excitonic / superfluid / neutral counterflow | `Ξ†Ξ`, `jμjμ`, `∂μθ∂^μθ` | Gap, flow, and interaction energy | New scalar boundary coupling; electrical neutrality does not cancel mass or stress | Counterflow reversal and geometry without net charge current |
| Phonon / strain / nonequilibrium interface | Strain invariants, occupation-dependent stress, vorticity `ΩμνΩμν` | Pumped mechanical and thermal energy | Resonant portal with a specified scalar mode and linewidth | Frequency, mode shape, `Q`, and off-resonance null |
| Vortex state | Gauge-invariant phase gradient and field/flow energy | Flux, core, and superflow energy | Coupling to vortex density beyond its stress-energy | Equal-field vortex/Meissner comparison and pinning controls |

The order parameters are defined relative to a medium four-velocity `uμ`; the medium already breaks boost invariance spontaneously. This does not license a noncovariant gravity sector. A covariant EFT contains `uμ` and the order parameter explicitly and includes their stress-energy.

Typical structural, ferroelectric, and electronic transition energies are roughly `10⁷–10⁹ J m⁻³` in favorable solids, or `10⁻¹⁴–10⁻¹²` of rest energy. These are scale estimates, not universal bounds. They make such materials better conventional switches than niobium by up to five orders, yet still leave at least twelve orders before an order-unity source change.

An emergent acoustic, optical, or quasiparticle metric describes propagation of excitations in a medium. It is not the `g̃μν` to which hulls, occupants, clocks, and exterior matter universally couple. No analog-curvature factor is counted as physical gravitational gain here.

### 5.3 The explicit portal and its naturalness cost

The proposed shorthand

`Ugate = λ |Ψ|² q²`

is incomplete until the normalization and cutoff of `Ψ` are stated. A model-independent form is

`Ugate = 1/2 [m0² + κi Oi(Ψ,uμ)] q²`,

where `κi Oi` has units of mass squared. It changes the scalar mass, not the scalar source direction by itself. If the gate region has thickness `d`, efficient attenuation requires `mwall c d/ℏ ≳ 1`; a clean on/off contrast normally requires several e-folds.

For a `10 m` interior range and a `1 cm` wall,

`mout ≲ ℏ/(c·10 m) = 1.97 × 10⁻⁸ eV`,

`mwall ≳ ℏ/(c·0.01 m) = 1.97 × 10⁻⁵ eV`.

Thus the phase must change `m²` by at least `10⁶` relative to the long-range mass. This is a nonempty classical boundary-condition window. It says nothing yet about the force magnitude.

If a dimensionless portal `λ` couples `q²` to a gate field with cutoff `Λgate`, a generic one-loop correction is

`δmq² ~ λ Λgate²/(16π²)`.

Demanding `δmq ≲ 1.97 × 10⁻⁸ eV` gives approximately

`λ ≲ 6.1 × 10⁻⁸` for `Λgate = 1 meV`,

`λ ≲ 6.1 × 10⁻¹⁴` for `Λgate = 1 eV`.

If the same order parameter has a scale near the cutoff and must generate `mwall`, the required mass-squared hierarchy is `mwall²/mout² ≳ 10⁶`; keeping the outside field light against the portal loop costs at least order `10⁻⁴` tuning from this loop alone (`10⁶/16π²` inverted), before Standard-Model and material-sector corrections. Exact values depend on normalization and symmetry.

A `q → −q` symmetry forbids a linear tadpole, and `λ → 0` can be multiplicatively natural when the sectors decouple. Neither fact protects a generic ultralight scalar mass against all allowed couplings. A credible model must name the symmetry, cutoff, matching from the microscopic material to `Oi`, and counterterms. The portal is not ruled out categorically; it is a new interaction to measure.

### 5.4 What the laboratory must measure

The necessary intermediate phenomenon is not thrust. It is:

> a reproducible, external, phase-correlated change in scalar charge or scalar transmission that exceeds the phase's known `ΔE/c²`, follows the new field's range and geometry, and is common to composition-paired detectors.

Absent this phenomenon, superconductivity, magnetism, DNP, phonons, and Josephson states remain useful modulation techniques but provide no evidence for the needed gravity gate.

---

## 6. Constraint matrix: parameter-by-parameter

### 6.1 Coupling dictionary

The following table uses the report's canonical normalization:

- `βi = MPl ∂ ln Ai/∂q` is the scalar coupling of species or bulk body `i`;
- an unscreened Yukawa force between source `s` and test `t` has strength `αst = 2βsβt` relative to Newtonian gravity;
- `βγ = MPl ∂ ln BF/∂q`, so `Mγ = MPl/βγ` for a linear photon coupling;
- screening factors `Qs, Qt ∈ [0,1]` replace `βs,t` by `Qs,t βs,t`;
- a material state change is `Δβgate` or `Δ(meff²) = κ ΔO`.

This makes clear why one headline bound cannot be used for all models.

### 6.2 Quantitative constraints

| Constraint / primary result | Range or result | Exact combination constrained | Relevance and limitation |
|---|---|---|---|
| MICROSCOPE final WEP result ([Touboul et al. 2022](https://doi.org/10.1103/PhysRevLett.129.121102)) | Pt/Ti Eötvös parameter at the `10⁻¹⁵` level | `ηAB ≈ 2 βsource (βA−βB)` for a long-range unscreened scalar, with finite-range/screening factors | Constrains differential coupling, not a perfectly common `β`; source and satellite screening are model dependent |
| Eöt-Wash Sun-directed WEP result ([preprint, arXiv:2602.02815](https://arxiv.org/abs/2602.02815)) | Be–Al `abs(η) ≤ 2.1 × 10⁻¹³` at 95% CL | solar-source `2Q☉β☉(QBeβBe−QAlβAl)` | Current terrestrial composition bound; preprint status |
| Superconducting-state WEP test ([Ross et al. 2025](https://doi.org/10.1103/PhysRevD.111.L021101)) | `abs(ηNb*−Cu) ≤ 2.0 × 10⁻⁹`; Cooper-pair/electron comparison `≤ 9.2 × 10⁻⁴`, 95% CL | Earth-source coupling times phase/body differential coupling | Directly constrains a superconducting anomaly, but not a short-range wall-only interaction or perfectly universal state shift |
| Short-range composition test ([Smith et al. 1999](https://doi.org/10.1103/PhysRevD.61.022001); archival [arXiv:2405.10982](https://arxiv.org/abs/2405.10982)) | Cu–Pb differential acceleration `(1.0 ± 2.8) × 10⁻¹³ cm s⁻²` with `9.2 × 10⁻⁵ cm s⁻²` gravitational signal | finite-range composition-dependent `αCu−αPb` down to centimetre scale | Strong discriminator for material-selective sources; the recent arXiv date is an archival upload, not a 2024 experiment |
| Torsion-balance inverse-square tests ([Lee et al. 2020](https://doi.org/10.1103/PhysRevLett.124.101101); [Tan et al. 2020](https://doi.org/10.1103/PhysRevLett.124.051301)) | gravitational-strength Yukawa interactions excluded for ranges down to about `38.6–48 μm` | `αst(λ) = 2QsQtβsβt` | Constrains even perfectly universal finite-range forces; thin shells and nonlinear geometry must be solved, not assumed |
| Atom interferometer, screened fields ([Hamilton et al. 2015](https://doi.org/10.1126/science.aaa8883); [Sabulsky et al. 2019](https://doi.org/10.1103/PhysRevLett.123.061102)) | no anomalous source-mass acceleration | model-specific `β`, `Λ`, chamber boundary, atomic unscreened charge | Atoms can remain unscreened when macroscopic test masses screen |
| Optical-lattice source-mass gravity ([Panda et al. 2024](https://doi.org/10.1038/s41586-024-07561-3)) | measured source attraction `33.3 ± 5.6stat ± 2.7syst nm s⁻²`; acceleration accuracy `6.2 nm s⁻²` | additional finite-range force from a characterized source | Demonstrates controlled micrometre atom/source geometry; not yet the `10⁻¹² m s⁻²` phase-switch target |
| Levitated chameleon sensor ([Yin et al. 2022](https://doi.org/10.1038/s41567-022-01706-9)) | excluded the physically plausible parameter region of the tested cosmological chameleon | inverse-power chameleon `β, Λ` with chamber/source nonlinear solution | Closes that model, not every screened potential |
| Levitated symmetron test ([Yin et al. 2025](https://doi.org/10.1038/s41550-024-02465-8)) | more than six orders improvement in parts of space | `μ, λs, Ms`, chamber boundary and source screening | Leaves model-dependent islands; no material gate tested |
| Levitated milligram sensor ([Fuchs et al. 2024](https://doi.org/10.1126/sciadv.adk2949)) | force noise about `0.5 fN Hz⁻¹/²` for a `0.4 mg` sensor | any modulated force after magnetic/electric calibration | Enabling sensitivity, not by itself a scalar limit |
| Neutron quantum states ([Jenke et al. 2014](https://doi.org/10.1103/PhysRevLett.112.151105); [Lemmel et al. 2015](https://doi.org/10.1016/j.physletb.2015.02.063)) | chameleon exclusions reaching `β > 5.8 × 10⁸` or `β < 1.9 × 10⁷` bounds depending on experiment/model | neutron coupling and nonlinear mirror/vacuum profile | Strong at large matter coupling; neutron response need not equal bulk screened response |
| Neutron symmetron spectroscopy ([Cronenberg et al. 2018](https://doi.org/10.1038/s41567-018-0205-x)) | energy sensitivity about `2 × 10⁻¹⁵ eV` | symmetron `μ, λs, Ms` around material mirrors | Tests a close theoretical relative of the proposed mass wall |
| Casimir-force reinterpretation ([Brax and Davis 2015](https://doi.org/10.1103/PhysRevD.91.063503)) | model- and geometry-dependent screened-field bounds | plate pressure from nonlinear scalar solution | Cannot be translated into one universal Yukawa `α` without solving plates and shields |
| CAST solar chameleon search ([Anastassopoulos et al. 2019](https://doi.org/10.1088/1475-7516/2019/01/032)) | `βγ < 5.7 × 10¹⁰` for `1 < βm < 10⁶` in the quoted model region, 95% CL | product of solar production, propagation, and magnet conversion, parametrized by `βγ, βm` | Used only as a model-specific EM-pump benchmark, not a generic photon-scalar bound |
| CHASE afterglow ([Steffen et al. 2010](https://doi.org/10.1103/PhysRevLett.105.261803)) | null trapped-chameleon afterglow | `βγ` versus effective potential parameters and wall trapping | Directly tests photon production plus environmental mass |
| KWISP membrane force ([Arguedas Cuendis et al. 2019](https://arxiv.org/abs/1906.01084)) | no solar-chameleon force above about `80 pN`; local reach around `βγ ~ 10¹¹` for selected `βm` | solar flux, reflection probability, `βm, βγ` | Preprint/collaboration result; model specific |
| Atomic-clock scalar search ([Filzinger et al. 2023](https://doi.org/10.1103/PhysRevLett.130.253001)) | oscillating-scalar limits over approximately `10⁻²⁴–10⁻¹⁷ eV` | electron/photon coupling combinations through frequency ratios | Constrains varying constants, not the static `10⁻⁸ eV` benchmark directly |
| Torsion-balance scalar reinterpretation ([Qin et al. 2024](https://doi.org/10.1016/j.dark.2024.101481)) | HUST data reach `Λγ ≈ 7 × 10¹⁷ GeV` and `Λe ≈ 1 × 10¹⁷ GeV` in parts of `10⁻⁹–10⁻⁴ eV` | one-at-a-time linear photon or electron scalar coupling scale | Directly overlaps the mass-wall range; translation to `βγ` depends on normalization and simultaneous couplings |
| Cassini Shapiro delay ([Bertotti, Iess, and Tortora 2003](https://doi.org/10.1038/nature01997)) | `γPPN − 1 = (2.1 ± 2.3) × 10⁻⁵` | for an unscreened massless universal scalar, `γ−1 = −4β0²/(1+2β0²)` in this normalization | Gives `β0 ≲ 2.4 × 10⁻³`; environmental/massive screening can evade it, but then local source/response are reduced |
| GW170817/GRB 170817A ([Abbott et al. 2017](https://doi.org/10.3847/2041-8213/aa920c)) | `−3 × 10⁻¹⁵ ≲ (cg−c)/c ≲ 7 × 10⁻¹⁶` | coefficients that change tensor-wave characteristics on the observed background | Canonical conformal scaffold passes; many derivative-curvature extensions do not |
| Binary pulsar scalarization ([Zhao et al. 2022](https://doi.org/10.1088/1361-6382/ac69a3)) | seven pulsars strongly restrict massless spontaneous scalarization | DEF coupling and neutron-star scalar charges through dipole radiation | Compact-object bound, not a direct material test |
| Neutron-star scalar cooling ([Fiorillo et al. 2025](https://doi.org/10.1103/tlqz-713s)) | stringent eV–MeV Higgs-mixed scalar emission; quoted mixing reaches `sin θ ~ 6 × 10⁻¹¹` in parts of the range | Higgs mixing and stellar production/trapping | Not directly a bound on a `10 m` conformal scalar, but excludes many heavier portal continuations |

### 6.3 What remains after the constraints

Three logically distinct regions remain:

1. **Unscreened universal coupling:** WEP can be satisfied, but inverse-square and PPN bounds limit the source strength. It cannot reach the reference field.
2. **Strong coupling with environmental screening:** present experiments leave model-dependent islands, but the dense source and craft response are both suppressed. A state gate can alter a boundary without supplying the missing scalar charge.
3. **Material-specific portal:** short-range or screened islands remain possible, but the portal is composition dependent unless the downstream physical metric dominates. It must be measured against the direct superconducting and phase-paired null tests rather than inferred from coherence.

The surviving laboratory mass-wall window is therefore a window for a new interaction, not a window for craft acceleration.

---

## 7. Benchmark parameter windows and closure tests

### 7.1 Reference-field amplitude

For `a = 9.80665 m s⁻²`, `L = 10 m`, and a universal conformal coupling `β`, the weak-field equation

`aφ = −βc² ∇(q/MPl)`

requires

`|∇(q/MPl)| = a/(βc²) = 1.091 × 10⁻¹⁶ β⁻¹ m⁻¹`,

`|Δq|/MPl = aL/(βc²) = 1.091 × 10⁻¹⁵ β⁻¹`.

The dimensionless field excursion looks small. The gradient energy does not. From the canonical kinetic term,

`ugrad = c⁴/(16πG) |∇(q/MPl)|² = a²/(16πGβ²)`

`= 2.87 × 10¹⁰ β⁻² J m⁻³`.

For a nominal `1000 m³` controlled region, this is `2.87 × 10¹³ β⁻² J` before wall, source, potential, and fringe-field energies. This is not a no-go by itself: a large `β` lowers the required canonical gradient energy. It identifies exactly where the next conflict enters.

For a solar-system-range unscreened scalar, the Cassini result gives, in this normalization,

`β0² ≲ 5.75 × 10⁻⁶`, `β0 ≲ 2.4 × 10⁻³`.

At that value,

`ugrad ≳ 4.99 × 10¹⁵ J m⁻³`,

`Egrad(1000 m³) ≳ 4.99 × 10¹⁸ J`.

Conversely, making `ugrad` no larger than the energy density of a `10 T` field requires `β ≳ 26.8`. The unscreened fifth-force strength is then

`α = 2β² ≳ 1.44 × 10³`,

already far beyond gravitational strength. It must be screened. Even the deliberately weak requirement `αeff < 1` demands a product of source and test screening factors

`QsQt < 1/(2β²) < 6.9 × 10⁻⁴`.

The actual inverse-square and composition limits are stronger over much of the range. The operation requires `QsQt` to return toward unity in the active region while remaining small in every null experiment, in the exterior, and in ordinary matter. No explicit gate model achieves that selectivity for hull, occupants, payload, and source.

### 7.2 Ordinary-matter source requirement

For an unscreened point source at radius `r`,

`aφ = 2β² GM/r²`.

At `r = 10 m`, a `1 g` scalar field needs

`Msource = ar²/(2β²G)`

`= 7.35 × 10¹² β⁻² kg`.

Even taking `β = 1`—already too large for an unscreened long-range scalar and not allowed at `10 m` by existing inverse-square searches—requires trillions of kilograms. Applying the Cassini-strength coupling gives `1.28 × 10¹⁸ kg`.

For an ideal infinite sheet with surface density `Σ`,

`aφ = 4πGβ²Σ`,

so

`Σ1g = 1.17 × 10¹⁰ β⁻² kg m⁻²`.

At the Cassini coupling this becomes `2.03 × 10¹⁵ kg m⁻²`. Finite plates have additional fringe gradients and tides. Screening only increases the required bare mass for a fixed external acceleration.

The Earth cannot supply the missing gain for a solar-system-range, unscreened universal scalar. The maximum scalar fraction under the Cassini benchmark is `2β0² ≲ 1.15 × 10⁻⁵`, corresponding near the surface to only

`aφ,Earth ≲ 1.13 × 10⁻⁴ m s⁻²`,

about `8.7 × 10⁴` short of `1 g`. A `10 m`-range field does not coherently couple to the whole Earth and is instead constrained by local inverse-square measurements.

For comparison, ordinary GR needs

`MGR = ar²/G = 1.47 × 10¹³ kg`

at `10 m`, with rest energy `1.32 × 10³⁰ J`. A crude curvature-energy scale for changing the acceleration across an exterior wall of thickness `δ = 1 m` is

`uGR,wall ~ c²a/(8πGδ) = 5.25 × 10²⁶ J m⁻³`,

equivalent to `5.85 × 10⁹ kg m⁻³`. This is only an Einstein-equation scale estimate, not a unique stress tensor, but it prevents a weak-field interior gradient from being mistaken for a cheap bounded metric.

### 7.3 Electromagnetic pump benchmark

Take an idealized `1 m³`, `10 T` static magnetic source. It stores

`UB = 3.98 × 10⁷ J`, `mB = UB/c² = 4.43 × 10⁻¹⁰ kg`.

For `BF = 1 + βγ q/MPl`, a compact non-null electromagnetic configuration produces, up to an order-unity geometry and invariant factor,

`aφ(r) ≈ 2βmβγ G (UB/c²)/r²`.

Using the CAST model-specific upper benchmark `βγ = 5.7 × 10¹⁰` gives:

| Matter coupling | `aφ` at `1 m` | `aφ` at `10 m` |
|---|---:|---:|
| `βm = 1` | `3.37 × 10⁻⁹ m s⁻²` | `3.37 × 10⁻¹¹ m s⁻²` |
| `βm = 10⁶` | `3.37 × 10⁻³ m s⁻²` | `3.37 × 10⁻⁵ m s⁻²` |

The required product at `10 m` is

`(βmβγ)1g = ar²c²/(2GUB) = 1.66 × 10²²`.

The largest product in the cited CAST parameter strip is `5.7 × 10¹⁶`, leaving a factor `2.9 × 10⁵` in acceleration even before material shielding, source size, stability, and universal-craft response are included. At `βm = 1`, the gap is another factor of one million. This calculation is intentionally optimistic: a real solenoid's `F²` geometry, fringe field, structural energy, and scalar screening must be solved.

Increasing volume or field energy scales the signal linearly, with no hidden coherence factor. Closing the `2.9 × 10⁵` gap using magnetic energy alone requires roughly `1.2 × 10¹³ J` in the same geometry even at `βm = 10⁶`; this strong matter coupling then has to be screened everywhere except the entire craft worldtube.

### 7.4 Superconducting source-switch signal

A `1 kg` niobium sample at `r = 0.10 m` has Newtonian acceleration

`aN = GM/r² = 6.67 × 10⁻⁹ m s⁻²`.

For an unscreened solar-system scalar at the Cassini coupling, the entire sample's maximum scalar acceleration would be

`aφ ≤ 2β0²aN = 7.68 × 10⁻¹⁴ m s⁻²`.

But the conventional phase-correlated fraction is only `2.07 × 10⁻¹⁷`, giving

`Δaφ,SC ≤ 1.59 × 10⁻³⁰ m s⁻²`.

The ordinary GR signal from the condensation mass itself is `1.38 × 10⁻²⁵ m s⁻²`. At `r = 0.05 m`, the corresponding numbers are `aN = 2.67 × 10⁻⁸ m s⁻²`, full-sample Cassini scalar `3.07 × 10⁻¹³ m s⁻²`, and conventional GR phase signal `5.52 × 10⁻²⁵ m s⁻²`.

Therefore any detected phase-correlated external acceleration near `10⁻¹² m s⁻²` would not be an incremental measurement of standard condensation gravity. It would be evidence for a new portal or an unmodelled systematic, separated by at least twelve orders from the conventional phase mass signal.

### 7.5 The nonempty boundary window versus the empty craft window

The generalized phase-mass-wall model has a classical laboratory window:

`10⁻⁷ eV ≲ mout ≲ 10⁻⁵ eV` for centimetre-to-metre exploration,

`mwall/mout ≳ dfield/dwall`,

with, for the craft reference, `mout ≲ 1.97 × 10⁻⁸ eV` and `mwall ≳ 1.97 × 10⁻⁵ eV`.

The gate can therefore measurably change transmission or a cavity mode if a scalar flux exists and the portal is large enough. Its width, cutoff, and loop correction can all be specified. That is the nonempty laboratory window.

The craft window is empty in the minimum scaffold because the following requirements cannot be satisfied together:

| Requirement | Weak-coupling branch | Strong screened branch |
|---|---|---|
| `1 g` source at `10 m` | Requires `≥ 7 × 10¹² kg`, enormous field energy, or an EM product `βmβγ ~ 10²²` | Bare coupling can reduce field energy |
| Existing force/PPN limits | Coupling too small; Earth scalar `≤ 1.1 × 10⁻⁴ m s⁻²` in long-range benchmark | Requires strong screening in ordinary sources and bodies |
| Hull/occupant/payload universality | Common conformal metric can provide it | Dense craft components acquire different thin shells; unscreening all of them restores external signature |
| Material switching | Conventional phase energies change charge by `10⁻¹⁷–10⁻¹²` | A new portal can change a wall mass, but not create directed scalar charge for free |
| Low-tide bounded worldtube | A uniform gradient does not supply its boundary | Nonlinear wall bears stress/recoil and introduces large boundary gradients |
| Momentum closure | External mass/background or radiation required | Same; a closed screened cavity cannot self-accelerate |

The contradiction is not merely “the coupling is constrained.” It is that the coupling must be simultaneously strong and unscreened for the commanded source and all craft contents, but weak or screened for nearby source-mass, inverse-square, PPN, and composition tests. A material-selective portal can choose a wall state; it cannot make universal matter distinguish “craft operation” from the same local field configuration in a null experiment.

### 7.6 Momentum and power floor

If the craft obtains momentum by emitting a collimated scalar flux, a massless flux obeys `P = Fc`; for a massive subluminal flux, `P = Fc²/v ≥ Fc`. Thus a `10⁵ kg` craft at `1 g` needs at least

`Pscalar ≥ Mac = 2.94 × 10¹⁴ W`.

A `10⁶ kg` craft needs `2.94 × 10¹⁵ W`. Coupling to Earth or a pre-existing field can exchange momentum without onboard radiative power of this magnitude, but the external source then must carry the reaction and must provide an allowed gradient. “Changing inertia” does not remove this momentum ledger; it changes the relation between force and acceleration only within a theory that must still conserve total stress-energy.

---

## 8. Decisive experiment: differential phase-gated scalar-charge search

### 8.1 Decision target

The experiment tests the necessary intermediate phenomenon from Section 5:

`phase reversal → external force profile exceeding ΔE/c² → common response across detector compositions`.

It does **not** claim to test propulsion. A null result constrains the portal product; a replicated positive result would justify a second program on field stress, universality, and momentum exchange.

### 8.2 Source and modulation

Use two nominally identical, high-purity `1 kg` niobium source assemblies placed symmetrically on opposite sides of the primary detector. Operate near `Tc ≈ 9.25 K` in nominal zero field. In state A, source 1 is superconducting and source 2 normal; in state B, the states are swapped. Counterphase operation keeps total heat load, helium flow, electrical power, and average thermal expansion approximately constant while reversing the putative scalar dipole.

Baseline parameters are:

- centre-to-detector distances `r = 0.02, 0.05, 0.10 m` in separate geometry runs;
- state modulation `0.2–2 mHz`, slow enough for verified thermal equilibrium and above dominant long-term drift after demodulation;
- four-wire resistance plus low-field susceptibility to certify state;
- a nested, nonmagnetic cryostat with independently temperature-controlled dummy thermal masses;
- source position metrology referenced to the detector frame at sub-nanometre-equivalent force accuracy.

A second campaign can replace niobium with a high-latent-heat structural or ferroelectric transition. Niobium is selected first because the direct phase identity is clean and an existing superconducting WEP null provides an external comparison—not because its conventional source energy is large.

### 8.3 Predicted signal

Let the source's effective scalar coupling change by `ΔβNb`, let detector `d` have coupling `βd`, and let `λq = ℏ/(mqc)`. For a compact source, define

`κd = 2 βd ΔβNb QsQd`.

The counterphase twin-source signal, including a numerically calculated finite-body factor `Ggeom`, is

`Δad(r) = 2 κd [GM/r²] (1 + r/λq)e^(−r/λq) Ggeom(r,λq)`.

The factor of two is the swap of equal sources on opposite sides. A boundary-transmission model replaces `ΔβNb` with the calculated change in scalar reflection/transmission coefficient but retains the range, distance, state, and geometry discriminants.

At `r = 0.05 m`, `GM/r² = 2.67 × 10⁻⁸ m s⁻²`. For `λq ≫ r` and `Ggeom ≈ 1`, a `10⁻¹² m s⁻²` null gives

`|κd| < 1.9 × 10⁻⁵`

at the corresponding confidence level. The target mass scan `mq ≈ 10⁻⁷–10⁻⁵ eV` covers ranges from about `2 m` to `2 cm` and overlaps the phase-wall design region.

The standard-physics phase signal from the two switched condensation masses is only about `1.1 × 10⁻²⁴ m s⁻²` at `5 cm`, plus explicitly calculated thermal, magnetic, electrostatic, acoustic, and mechanical effects. It is negligible as a gravitational background but crucial as a calorimetric normalization.

### 8.4 Detectors and universality check

Use two independent force principles:

1. a cryogenic torsion or optomechanical/levitated sensor with nonmagnetic proof masses and a design acceleration sensitivity `σa ≤ 10⁻¹² m s⁻²` after integration;
2. a spatially separated atom-interferometric or optical-lattice detector viewing the same source reversal.

The published `0.5 fN Hz⁻¹/²` force noise of a `0.4 mg` levitated sensor corresponds to roughly `1.25 × 10⁻⁹ m s⁻² Hz⁻¹/²`, which reaches the target order after about `10⁶ s` only if long-term systematics average down. The target is therefore ambitious but anchored to demonstrated short-term force noise, not assumed.

Use composition-paired solid proof masses—one low-neutron-fraction material such as beryllium and one silica-based dielectric where practical—and, for the atom channel, two species or isotopes. A metric-like candidate must produce the same acceleration within a predeclared `1%` differential tolerance after finite-size corrections. A composition-dependent signal remains interesting new physics but fails the worldtube-universality gate.

A colocated clock or stabilized optical cavity is an optional third channel. Correlated frequency-ratio shifts would constrain `βγ` and electron-mass coupling and help distinguish a metric-like response from magnetic force.

### 8.5 Systematic controls

| Systematic | Required control and reversal |
|---|---|
| Magnetic field and trapped flux | Nested high-permeability and superconducting shields; SQUID/fluxgate maps; zero-field cool and field-cooled runs; nonmagnetic detector; vary trapped flux independently of phase |
| Electrostatic / patch force | Conducting guard enclosure, Kelvin-probe monitoring, polarity and grounding reversals, UV discharge, source-independent electrode injection |
| Thermal radiation / gas | Counterphase heat, dummy resistive sources with identical temperature histories, radiation thermometry, high vacuum, pressure and helium-flow monitors |
| Acoustic / vibration | Seismometers and accelerometers on every stage, mechanical transfer-function injections, off-resonance modulation, blank copper source cycle |
| Thermal expansion / centre of mass | Interferometric source metrology, symmetric mounts, ballast compensation, fixed-state heater cycles |
| Mechanical or magnetic actuation by wiring | Twisted superconducting/normal leads in symmetric return geometry, current-off transition holds, cable-force injection tests |
| Data-analysis leakage | Blind state labels, predeclared phase window, sidebands, null quadratures, and independent pipelines |

### 8.6 Scaling discriminants and falsification

A surviving signal must satisfy all of the following:

- reverse sign on the superconducting/normal source swap;
- follow the calculated finite-body Yukawa or boundary-transmission profile at `2`, `5`, and `10 cm`;
- scale with switched source volume or surface area as predicted by the explicit model;
- remain after equal-temperature and equal-field dummy cycles;
- appear with the correct phase in both force technologies;
- be common to paired detector compositions at the `1%` level if claimed as a worldtube precursor;
- show a consistent clock/cavity signature if the fitted `βγ` predicts one;
- conserve the measured mechanical plus field momentum within uncertainty.

A preregistered benchmark predicting `|Δa| ≥ 10⁻¹¹ m s⁻²` is falsified if the combined 95% upper limit is below `10⁻¹² m s⁻²` at all three distances with no fitted Yukawa profile. More generally the result is reported as a limit on `κd(mq)` and, for the wall model, on `κ ΔO` and the transmission coefficient.

The material-scalar branch is promoted beyond a laboratory discriminator only after an independent replication finds `|Δa| ≥ 10⁻¹² m s⁻²`, the signal exceeds the fully measured `ΔE/c²` prediction, composition universality is better than `1%`, and the spatial profile identifies an external field rather than an apparatus force. The next experiment would then measure scalar pressure and recoil on the source/wall to close the momentum ledger.

---

## 9. Strongest rejection case and strongest continuation case

### 9.1 Strongest rejection case

The minimum action is coherent but contains no allowed source of the required amplitude. Its branches fail for different, explicit reasons:

- With a weak, unscreened universal coupling, ordinary matter or electromagnetic field energy requires astronomically large sources. Earth coupling is at least `8.7 × 10⁴` short in the long-range Cassini benchmark.
- With a strong universal coupling, screening is mandatory. Chameleon, symmetron, K-mouflage, and Vainshtein behavior reduce the scalar charge or gradient of the same dense source and craft that must remain active. No demonstrated order parameter reverses this selectively.
- A direct phase portal can make a wall opaque, but its natural conventional source scale is only the phase energy `ΔE/c²`. An anomalous portal is new physics and brings loop, WEP, fifth-force, and composition constraints.
- A bounded field transfers stress to its wall. A closed wall–source–craft system has no external momentum sink; radiation demands at least `Mac` power.
- A common fifth-force acceleration is not a low-tide worldtube. The physical metric, exterior matching, fringe curvature, environment, and reaction channel remain missing.

The empty craft window is therefore caused by a combined **source–screening–universality–conservation incompatibility**, not by a philosophical rejection of new scalar fields.

### 9.2 Strongest continuation case

The scalar laboratory lane still has four defensible features:

1. The action is explicit, covariant, and falsifiable. A generalized symmetron portal can make `mout` long range and `mwall` short range without an algebraic inconsistency.
2. A phase reversal is an unusually strong systematic discriminator. The same object supplies normal and ordered states, and twin counterphase sources cancel first-order heat load.
3. Existing levitated, neutron, atom, and superconducting tests show that the relevant force sensitivity and environmental control are technically accessible, while not covering every material-specific wall model.
4. A positive external phase-correlated field would be a genuinely new intermediate phenomenon. It would justify measuring universality and recoil before any propulsion extrapolation.

This is a continuation case for one bounded experiment and a microscopic portal calculation. It is not a case for craft development.

---

## 10. Comparison with the next mechanism families

### 10.1 Vector or baryon-coupled fields

A vector can produce directed forces and exchange momentum with an external charge distribution or emitted vector radiation. A new `B−L`-like charge is approximately neutron number, so it is not universal per unit mass. As an order-of-magnitude translation, Earth's normalized `B−L` charge is about `0.5`, while Pt and Ti differ in neutron fraction by about `0.058`. A long-range vector of relative strength `αV` then gives roughly

`ηPt,Ti ~ 0.5 × 0.058 × αV ≈ 0.029 αV`.

Taking a conservative few-`10⁻¹⁵` MICROSCOPE differential limit gives `αV` of order `10⁻¹³` or below, before exact isotope, binding, range, and source modelling. This estimate is not a substitute for a dedicated reinterpretation, but it shows why a vector does not repair universality. A hidden vector with universal mass-proportional charge faces charge-sign, anomaly, and UV-completion questions, as well as inverse-square tests. Vector radiation also obeys a momentum/power ledger.

**Repair offered:** direction and an explicit external interaction. **New failure:** composition dependence and charge neutrality.

### 10.2 Torsion, axial, and spin-dependent interactions

Torsion or an axial mediator couples naturally to spin density and produces monopole–dipole or dipole–dipole potentials rather than a common metric acceleration. Polarized sources provide clean reversal and low conventional mass change. Modern spin-force experiments already use this advantage, including polarized-electron tests of exotic spin couplings ([Zhang et al. 2023](https://doi.org/10.1103/PhysRevLett.130.201401)).

The same feature makes it unsuitable for the craft requirement: ordinary unpolarized hull, tissue, fuel, and payload do not share a common axial charge. Nuclear spin polarization is also a small fraction of all constituents. An axial discovery could become a source or control channel in a larger metric theory, but it is not a protected worldtube by itself.

**Repair offered:** excellent state reversal and directional geometry. **New failure:** nonuniversality and small polarized source fraction.

### 10.3 Variable inertial mass and Mach-effect models

Mach-effect proposals directly target the distinction between proper acceleration and craft trajectory and claim transient mass fluctuations in driven capacitors. That makes them strategically relevant. They lack an accepted covariant action that produces the reported scale while conserving total stress-energy. In a dedicated replication, Monette, Kössling, and Tajmar found signals attributable to vibration and ruled out the predicted mass fluctuations at their sensitivity ([Acta Astronautica 2021](https://doi.org/10.1016/j.actaastro.2021.02.037)).

For scale, photon momentum gives `3.34 nN kW⁻¹`. Claims at `~100 nN kW⁻¹` are only about 30 times photon thrust, so precision balances can test them, but a thrust anomaly without a covariant reservoir is not evidence of inertial-frame control. This lane merits exact replications more than speculative scale-up.

**Repair offered:** addresses inertia directly and is experimentally cheap. **New failure:** no accepted field/reservoir model; existing controlled null.

### 10.4 Vacuum stress, negative energy, warp and tractor/pressor metrics

Requirements-first metric design correctly starts from the desired worldtube rather than a material analogy. Alcubierre-type metrics demonstrate that a bounded low-proper-acceleration region can be written mathematically ([Alcubierre 1994](https://doi.org/10.1088/0264-9381/11/5/001)). Subsequent analyses show that generic warp geometries demand severe stress-energy-condition violations or large stresses, even when subluminal positive-energy shells are separated from the actual transport function ([Bobrick and Martire 2021](https://doi.org/10.1088/1361-6382/abdf6e); [Santiago, Schuster, and Visser 2022](https://doi.org/10.1103/PhysRevD.105.064038)).

Casimir energy illustrates the scale. The ideal parallel-plate density is

`|uCas| = π²ℏc/(720d⁴)`.

It is `4.33 × 10⁻⁴ J m⁻³` at `d = 1 μm` and `4.33 × 10⁸ J m⁻³` even at `d = 1 nm`, versus the rough `5.25 × 10²⁶ J m⁻³` curvature-source scale for the reference `1 m` wall. The gap at `1 nm` is still about `1.2 × 10¹⁸`, before signs, plate stress, quantum inequalities, and macroscopic volume are addressed.

This family nevertheless repairs the scalar program's largest conceptual weakness: it specifies the entire metric and lets Einstein or modified field equations tell us the required stress tensor. The next work should inverse-design the weakest admissible worldtube and then ask whether any stable tensor, vector, scalar, vacuum, or external-field source approximates that stress tensor.

**Repair offered:** directly encodes low proper acceleration, tides, exterior matching, and conservation. **New failure:** known sources are fantastically inadequate and negative energy is constrained.

### 10.5 Ordinary GR source engineering

Ordinary GR is the non-negotiable baseline. It is universal and covariant, and its field momentum is well defined. Its required `1.47 × 10¹³ kg` at `10 m` or corresponding stress scale is impractical. Rotating mass currents add gravitomagnetism only at post-Newtonian order, as the previous project reports correctly concluded; superconducting London response does not convert electromagnetic current into amplified gravitational current.

Ordinary GR remains useful as a calibration architecture and as the low-energy limit any extension must reproduce. External astronomical masses, orbital free fall, and gravity-gradient navigation can change trajectory with low proper acceleration, but they are not a compact local actuator.

**Repair offered:** exact universality and established dynamics. **New failure:** source density and controllability.

### 10.6 Ranked continuing lanes

| Rank | Continuing lane | Why it remains | Mandatory next gate |
|---:|---|---|---|
| **1** | Requirements-first physical-metric/worldtube inverse design, with explicit stress-energy and modified-gravity source audit | It targets the actual invariant requirement and exposes source, tide, exterior, and momentum costs before choosing a material | Derive a least-cost subluminal worldtube family and prove its stress tensor, stability, and junction conditions |
| **2** | Phase-gated generalized symmetron/dilaton laboratory discriminator | A nonempty mass-wall window and decisive same-sample reversal survive; it could reveal the missing intermediate phenomenon | Complete microscopic portal matching and run the twin-source external-charge experiment; no craft extrapolation before a positive replication |
| **3** | External-interaction vector/baryon field | Supplies direction and a momentum sink more naturally than a static scalar cavity | Identify an anomaly-free, nearly mass-universal charge assignment that survives WEP/ISL limits |
| **4** | Variable-inertia/Mach precision replication | Directly tests inertial response with modest apparatus and a clear photon-thrust scale | Pre-registered multisite null/replication plus a covariant energy–momentum model |
| **5** | Torsion/axial/spin interaction as a control or discriminator | Excellent polarization reversal and mature sensors | Demonstrate coupling to unpolarized bulk matter or embed it in a universal physical metric |

Vacuum stress, warp/tractor metrics, and ordinary GR are not discarded; they are folded into rank 1 as target metrics and source baselines. The ranked list contains no more than five active lanes as required.

---

## 11. Go/no-go decision and next milestone

### 11.1 Decision

**NO-GO for phase-gated scalar–tensor gravity as the current craft-control lead.**

No technically defensible parameter window in the minimum covariant scaffold simultaneously provides:

- a `1 g`, `10 m` common physical-metric response;
- an allowed, controllable source;
- unscreened coupling to hull, occupants, and payload;
- a low-tide bounded exterior transition;
- a radiatively stable material gate;
- and an external energy/momentum reservoir.

**CONDITIONAL GO for one laboratory phase-gate program.**

The phase-mass-wall interval is nonempty, the distinctive signal is well defined, and present apparatus can improve direct state-dependent constraints. This program is justified only as a search for the necessary external phase-correlated scalar phenomenon.

### 11.2 Resulting next milestone

The next major theoretical milestone is:

> **Worldtube Source Theorem and Inverse-Design Report:** construct the weakest stationary or slowly accelerated, subluminal physical metric that keeps a `10 m` occupied region below `1%` acceleration nonuniformity, matches to an admissible exterior, and compute the complete effective stress tensor, energy conditions, junction stresses, total field momentum, and scaling with boundary thickness. Then test canonical scalar, vector, tensor/bimetric, and semiclassical-vacuum sources against that one target.

In parallel, but not on the critical craft path:

1. derive a microscopic, gauge-invariant niobium or structural-transition portal including cutoff and loop corrections;
2. publish the predicted `κd(mq)` sensitivity for the twin-source design;
3. proceed to apparatus only if the design can discriminate an anomalous signal at least twelve orders above the standard phase-mass gravity while controlling magnetic and thermal feedthroughs.

The automatic project redirection is therefore from **“find a material that amplifies gravity”** to **“inverse-design the minimum admissible worldtube stress tensor, then search for a source sector”**, while retaining phase transitions as high-quality discriminators.

---

## 12. Primary-source bibliography and verification ledger

### 12.1 Status key and audit scope

All identities below were checked on **2026-07-16** against a DOI-registration/publisher record or the cited arXiv record. Result claims used in the report were checked against the primary abstract, article text, or official collaboration record available online.

- **V-P:** peer-reviewed publication; DOI identity and publication metadata verified.
- **V-A:** arXiv identity and version verified; no peer-reviewed publication verified as of the audit date.
- **V-P/A:** peer-reviewed DOI and associated arXiv record both verified.
- **Null:** the cited result reports no anomalous signal at its stated sensitivity.

The bibliography is intentionally primary-source weighted. A paper's presence verifies its identity and relevance; it does not imply that every model assumption in it is adopted.

### 12.2 Scalar–tensor, screening, and coupling foundations

1. T. Damour and G. Esposito-Farèse, “Nonperturbative strong-field effects in tensor-scalar theories of gravitation,” *Physical Review Letters* **70**, 2220 (1993). [DOI: 10.1103/PhysRevLett.70.2220](https://doi.org/10.1103/PhysRevLett.70.2220). **V-P.** Foundation of spontaneous scalarization.
2. T. Damour and A. M. Polyakov, “The string dilaton and a least coupling principle,” *Nuclear Physics B* **423**, 532–558 (1994). [DOI: 10.1016/0550-3213(94)90143-0](https://doi.org/10.1016/0550-3213%2894%2990143-0). **V-P.** Damour–Polyakov mechanism.
3. J. Khoury and A. Weltman, “Chameleon Fields: Awaiting Surprises for Tests of Gravity in Space,” *Physical Review Letters* **93**, 171104 (2004). [DOI: 10.1103/PhysRevLett.93.171104](https://doi.org/10.1103/PhysRevLett.93.171104); [arXiv:astro-ph/0309300](https://arxiv.org/abs/astro-ph/0309300). **V-P/A.** Chameleon/thin-shell foundation.
4. K. Hinterbichler and J. Khoury, “Screening Long-Range Forces through Local Symmetry Restoration,” *Physical Review Letters* **104**, 231301 (2010). [DOI: 10.1103/PhysRevLett.104.231301](https://doi.org/10.1103/PhysRevLett.104.231301); [arXiv:1001.4525](https://arxiv.org/abs/1001.4525). **V-P/A.** Symmetron foundation.
5. K. Hinterbichler, J. Khoury, A. Levy, and A. Matas, “Symmetron cosmology,” *Physical Review D* **84**, 103521 (2011). [DOI: 10.1103/PhysRevD.84.103521](https://doi.org/10.1103/PhysRevD.84.103521); [arXiv:1107.2112](https://arxiv.org/abs/1107.2112). **V-P/A.** Environmental symmetry-restoration phenomenology.
6. P. Brax, C. van de Bruck, A.-C. Davis, and D. Shaw, “Dilaton and modified gravity,” *Physical Review D* **82**, 063519 (2010). [DOI: 10.1103/PhysRevD.82.063519](https://doi.org/10.1103/PhysRevD.82.063519); [arXiv:1005.3735](https://arxiv.org/abs/1005.3735). **V-P/A.** Environmentally dependent dilaton.
7. T. S. Koivisto, D. F. Mota, and M. Zumalacárregui, “Screening Modifications of Gravity through Disformally Coupled Fields,” *Physical Review Letters* **109**, 241102 (2012). [DOI: 10.1103/PhysRevLett.109.241102](https://doi.org/10.1103/PhysRevLett.109.241102); [arXiv:1205.3167](https://arxiv.org/abs/1205.3167). **V-P/A.** Disformal screening.
8. A. Upadhye, W. Hu, and J. Khoury, “Quantum Stability of Chameleon Field Theories,” *Physical Review Letters* **109**, 041301 (2012). [DOI: 10.1103/PhysRevLett.109.041301](https://doi.org/10.1103/PhysRevLett.109.041301); [arXiv:1204.3906](https://arxiv.org/abs/1204.3906). **V-P/A.** Loop-stability bound.
9. P. Brax and P. Valageas, “Small-scale nonlinear dynamics of K-mouflage theories,” *Physical Review D* **90**, 123521 (2014). [DOI: 10.1103/PhysRevD.90.123521](https://doi.org/10.1103/PhysRevD.90.123521); [arXiv:1408.0969](https://arxiv.org/abs/1408.0969). **V-P/A.** Kinetic screening and nonspherical dynamics.
10. C. Burrage, E. J. Copeland, and P. Millington, “Radiative Screening of Fifth Forces,” *Physical Review Letters* **117**, 211102 (2016). [DOI: 10.1103/PhysRevLett.117.211102](https://doi.org/10.1103/PhysRevLett.117.211102); [arXiv:1604.06051](https://arxiv.org/abs/1604.06051). **V-P/A.** Radiative effects in symmetron-like screening.
11. A. M. Bonanno and E. M. Glaviano, “Fifth-Force Constraints from UV-Complete Scalar-Tensor Gravity,” *Physical Review Letters* **136**, 201501 (2026). [DOI: 10.1103/q1gq-sgy3](https://doi.org/10.1103/q1gq-sgy3); [arXiv:2605.10338v2](https://arxiv.org/abs/2605.10338). **V-P/A.** Current UV-complete parameter wedge.
12. K. Homma, T. Katsuragawa, and S. Matsuzaki, “Technically Natural Suppression of Fifth Force” (2026). [arXiv:2604.20292v1](https://arxiv.org/abs/2604.20292). **V-A; preprint.** Symmetry-suppressed metre-range scalar proposal.

### 12.3 Equivalence principle, inverse-square, and direct phase tests

13. B. Bertotti, L. Iess, and P. Tortora, “A test of general relativity using radio links with the Cassini spacecraft,” *Nature* **425**, 374–376 (2003). [DOI: 10.1038/nature01997](https://doi.org/10.1038/nature01997). **V-P.** PPN `γ` primary result.
14. P. Touboul et al., “MICROSCOPE Mission: Final Results of the Test of the Equivalence Principle,” *Physical Review Letters* **129**, 121102 (2022). [DOI: 10.1103/PhysRevLett.129.121102](https://doi.org/10.1103/PhysRevLett.129.121102); [arXiv:2209.15487](https://arxiv.org/abs/2209.15487). **V-P/A; Null.**
15. M. P. Ross et al., “An Improved Torsion Balance Test of the Equivalence Principle Towards the Sun” (2026). [arXiv:2602.02815v1](https://arxiv.org/abs/2602.02815). **V-A; preprint; Null.** Be–Al result.
16. M. P. Ross et al., “Test of the equivalence principle for superconductors,” *Physical Review D* **111**, L021101 (2025). [DOI: 10.1103/PhysRevD.111.L021101](https://doi.org/10.1103/PhysRevD.111.L021101); [arXiv:2407.14599](https://arxiv.org/abs/2407.14599). **V-P/A; Null.** Direct superconducting-state result.
17. G. L. Smith et al., “Short-range tests of the equivalence principle,” *Physical Review D* **61**, 022001 (1999). [DOI: 10.1103/PhysRevD.61.022001](https://doi.org/10.1103/PhysRevD.61.022001); archival [arXiv:2405.10982](https://arxiv.org/abs/2405.10982). **V-P/A; Null.** The arXiv submission is archival and does not change the experiment date.
18. D. J. Kapner et al., “Tests of the Gravitational Inverse-Square Law below the Dark-Energy Length Scale,” *Physical Review Letters* **98**, 021101 (2007). [DOI: 10.1103/PhysRevLett.98.021101](https://doi.org/10.1103/PhysRevLett.98.021101); [arXiv:hep-ph/0611184](https://arxiv.org/abs/hep-ph/0611184). **V-P/A; Null.**
19. J. G. Lee et al., “New Test of the Gravitational `1/r²` Law at Separations down to `52 μm`,” *Physical Review Letters* **124**, 101101 (2020). [DOI: 10.1103/PhysRevLett.124.101101](https://doi.org/10.1103/PhysRevLett.124.101101); [arXiv:2002.11761](https://arxiv.org/abs/2002.11761). **V-P/A; Null.**
20. W.-H. Tan et al., “Improvement for Testing the Gravitational Inverse-Square Law at the Submillimeter Range,” *Physical Review Letters* **124**, 051301 (2020). [DOI: 10.1103/PhysRevLett.124.051301](https://doi.org/10.1103/PhysRevLett.124.051301). **V-P; Null.**
21. C.-G. Qin et al., “Constraining light scalar field with torsion-balance gravity experiments,” *Physics of the Dark Universe* **44**, 101481 (2024). [DOI: 10.1016/j.dark.2024.101481](https://doi.org/10.1016/j.dark.2024.101481); [arXiv:2212.06032v2](https://arxiv.org/abs/2212.06032). **V-P/A.** Reanalysis of `G`, ISL, and WEP data in electron/photon coupling variables.

### 12.4 Atom, neutron, levitated, Casimir, and photon-channel tests

22. P. Hamilton et al., “Atom-interferometry constraints on dark energy,” *Science* **349**, 849–851 (2015). [DOI: 10.1126/science.aaa8883](https://doi.org/10.1126/science.aaa8883); [arXiv:1502.03888](https://arxiv.org/abs/1502.03888). **V-P/A; Null.**
23. D. O. Sabulsky et al., “Experiment to Detect Dark Energy Forces Using Atom Interferometry,” *Physical Review Letters* **123**, 061102 (2019). [DOI: 10.1103/PhysRevLett.123.061102](https://doi.org/10.1103/PhysRevLett.123.061102); [arXiv:1812.08244](https://arxiv.org/abs/1812.08244). **V-P/A; Null.**
24. C. D. Panda et al., “Measuring gravitational attraction with a lattice atom interferometer,” *Nature* **631**, 515–520 (2024). [DOI: 10.1038/s41586-024-07561-3](https://doi.org/10.1038/s41586-024-07561-3). **V-P.** Source-mass gravity measurement and fifth-force constraint.
25. P. Yin et al., “Experiments with levitated force sensor challenge theories of dark energy,” *Nature Physics* **18**, 1181–1185 (2022). [DOI: 10.1038/s41567-022-01706-9](https://doi.org/10.1038/s41567-022-01706-9). **V-P; Null.** Tested cosmological chameleon exclusion.
26. P. Yin et al., “Experimental constraints on the symmetron field with a magnetically levitated force sensor,” *Nature Astronomy* (2025). [DOI: 10.1038/s41550-024-02465-8](https://doi.org/10.1038/s41550-024-02465-8). **V-P; Null.**
27. T. M. Fuchs et al., “Measuring gravity with milligram levitated masses,” *Science Advances* **10**, eadk2949 (2024). [DOI: 10.1126/sciadv.adk2949](https://doi.org/10.1126/sciadv.adk2949); [arXiv:2303.03545](https://arxiv.org/abs/2303.03545). **V-P/A.** Demonstrated force-noise platform.
28. T. Jenke et al., “Gravity Resonance Spectroscopy Constrains Dark Energy and Dark Matter Scenarios,” *Physical Review Letters* **112**, 151105 (2014). [DOI: 10.1103/PhysRevLett.112.151105](https://doi.org/10.1103/PhysRevLett.112.151105); [arXiv:1404.4099](https://arxiv.org/abs/1404.4099). **V-P/A; Null.**
29. H. Lemmel et al., “Neutron interferometry constrains dark energy chameleon fields,” *Physics Letters B* **743**, 310–314 (2015). [DOI: 10.1016/j.physletb.2015.02.063](https://doi.org/10.1016/j.physletb.2015.02.063); [arXiv:1502.06023](https://arxiv.org/abs/1502.06023). **V-P/A; Null.**
30. G. Cronenberg et al., “Acoustic Rabi oscillations between gravitational quantum states and impact on symmetron dark energy,” *Nature Physics* **14**, 1022–1026 (2018). [DOI: 10.1038/s41567-018-0205-x](https://doi.org/10.1038/s41567-018-0205-x); [arXiv:1902.08775](https://arxiv.org/abs/1902.08775). **V-P/A; Null for symmetron anomaly.**
31. P. Brax and A.-C. Davis, “Casimir, gravitational, and neutron tests of dark energy,” *Physical Review D* **91**, 063503 (2015). [DOI: 10.1103/PhysRevD.91.063503](https://doi.org/10.1103/PhysRevD.91.063503); [arXiv:1412.2080](https://arxiv.org/abs/1412.2080). **V-P/A.** Primary model calculation mapping experiments to screened fields.
32. J. H. Steffen et al., “Laboratory Constraints on Chameleon Dark Energy and Power-Law Fields,” *Physical Review Letters* **105**, 261803 (2010). [DOI: 10.1103/PhysRevLett.105.261803](https://doi.org/10.1103/PhysRevLett.105.261803); [arXiv:1010.0988](https://arxiv.org/abs/1010.0988). **V-P/A; Null.** CHASE afterglow.
33. V. Anastassopoulos et al., “Improved search for solar chameleons with a GridPix detector at CAST,” *Journal of Cosmology and Astroparticle Physics* **2019**(01), 032. [DOI: 10.1088/1475-7516/2019/01/032](https://doi.org/10.1088/1475-7516/2019/01/032); [arXiv:1808.00066](https://arxiv.org/abs/1808.00066). **V-P/A; Null.**
34. S. Arguedas Cuendis et al., “First Results on the Search for Chameleons with the KWISP Detector at CAST” (2019). [arXiv:1906.01084v1](https://arxiv.org/abs/1906.01084). **V-A; collaboration preprint; Null.**
35. M. Filzinger et al., “Improved Limits on the Coupling of Ultralight Bosonic Dark Matter to Photons from Optical Atomic Clock Comparisons,” *Physical Review Letters* **130**, 253001 (2023). [DOI: 10.1103/PhysRevLett.130.253001](https://doi.org/10.1103/PhysRevLett.130.253001); [arXiv:2301.03433](https://arxiv.org/abs/2301.03433). **V-P/A; Null.**

### 12.5 Gravitational-wave, compact-object, and alternative-lane tests

36. B. P. Abbott et al., “Gravitational Waves and Gamma-Rays from a Binary Neutron Star Merger: GW170817 and GRB 170817A,” *Astrophysical Journal Letters* **848**, L13 (2017). [DOI: 10.3847/2041-8213/aa920c](https://doi.org/10.3847/2041-8213/aa920c); [arXiv:1710.05834](https://arxiv.org/abs/1710.05834). **V-P/A.** Tensor-speed constraint.
37. J. Zhao et al., “Closing a spontaneous-scalarization window with binary pulsars,” *Classical and Quantum Gravity* **39**, 11LT01 (2022). [DOI: 10.1088/1361-6382/ac69a3](https://doi.org/10.1088/1361-6382/ac69a3); [arXiv:2201.03771](https://arxiv.org/abs/2201.03771). **V-P/A; Null for dipolar anomaly.**
38. D. F. G. Fiorillo et al., “Leading Bounds on Micrometer to Picometer Fifth Forces from Neutron Star Cooling,” *Physical Review Letters* **135**, 211003 (2025). [DOI: 10.1103/tlqz-713s](https://doi.org/10.1103/tlqz-713s); [arXiv:2506.19906v2](https://arxiv.org/abs/2506.19906). **V-P/A.** Heavier-scalar portal constraint.
39. Y. Zhang et al., “Search for Spin-Dependent Gravitational Interactions at Earth Range,” *Physical Review Letters* **130**, 201401 (2023). [DOI: 10.1103/PhysRevLett.130.201401](https://doi.org/10.1103/PhysRevLett.130.201401). **V-P; Null.**
40. F. Monette, M. Kößling, and M. Tajmar, “Experimental investigation of Mach-Effect thrusters on torsion balances,” *Acta Astronautica* **182**, 531–537 (2021). [DOI: 10.1016/j.actaastro.2021.02.037](https://doi.org/10.1016/j.actaastro.2021.02.037). **V-P; controlled null for predicted mass fluctuation.**
41. M. Alcubierre, “The warp drive: hyper-fast travel within general relativity,” *Classical and Quantum Gravity* **11**, L73–L77 (1994). [DOI: 10.1088/0264-9381/11/5/001](https://doi.org/10.1088/0264-9381/11/5/001); [arXiv:gr-qc/0009013](https://arxiv.org/abs/gr-qc/0009013). **V-P/A.** Metric construction.
42. A. Bobrick and G. Martire, “Introducing physical warp drives,” *Classical and Quantum Gravity* **38**, 105009 (2021). [DOI: 10.1088/1361-6382/abdf6e](https://doi.org/10.1088/1361-6382/abdf6e); [arXiv:2102.06824](https://arxiv.org/abs/2102.06824). **V-P/A.** Stress-energy classification.
43. J. Santiago, S. Schuster, and M. Visser, “Generic warp drives violate the null energy condition,” *Physical Review D* **105**, 064038 (2022). [DOI: 10.1103/PhysRevD.105.064038](https://doi.org/10.1103/PhysRevD.105.064038); [arXiv:2105.03079](https://arxiv.org/abs/2105.03079). **V-P/A.** Energy-condition result.

### 12.6 Verification cautions

- The 2026 Sun-directed WEP and symmetry-suppression papers are preprints; their result status is explicitly not upgraded.
- CAST, CHASE, KWISP, neutron, Casimir, and levitated limits are model dependent. This report does not combine their headline coupling numbers as if they shared one potential or screening solution.
- The Ross superconducting experiment is a direct null on a particular differential free-fall observable. It does not exclude every short-range material wall, but it does eliminate any claim that superconducting order is already known to carry a large anomalous long-range gravitational charge.
- The HUST coupling-scale maxima assume the coupling choices and normalizations in that analysis; they are not universal limits on `βγ`.
- The Alzofon source was consulted only as project history. No unverified Alzofon mechanism or claimed experimental effect is used in the action, constraints, or verdict.

---

## 13. Compact decision record

| Question | Answer |
|---|---|
| Is the proposed covariant scalar scaffold mathematically coherent? | **Yes**, within its EFT domain and stability conditions. |
| Can a material phase create a scalar mass/boundary switch? | **Yes in principle**; the classical mass-wall parameter interval is nonempty, but it requires a new portal and quantified radiative control. |
| Does ordinary superconducting, magnetic, phonon, or transition energy provide useful scalar gain? | **No**; conventional charge changes track `ΔE/c²`, typically `10⁻¹⁷–10⁻¹²` of rest mass. |
| Is there an allowed source/coupling window for `1 g` over `10 m` in the minimum model? | **No**; weak coupling fails magnitude, strong coupling requires screening that suppresses the needed source and universal craft response. |
| Does a uniform fifth force alone produce the desired worldtube? | **No**; it does not supply a low-tide boundary, exterior solution, environment response, or momentum sink. |
| Is a laboratory program justified? | **Yes, conditionally**, as a same-sample search for anomalous external phase-correlated scalar charge/transmission, not propulsion. |
| What becomes the craft-level lead? | **Requirements-first physical-metric/worldtube inverse design with an explicit stress-energy and reservoir audit.** |
