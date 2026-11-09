# Capability Model

This map translates reported performance into physical requirements before selecting a mechanism. A capability is admitted only when the underlying case supports it; otherwise it remains a target hypothesis.

| Reported capability | Minimum physical requirement | Likely supporting requirements | Decisive measurements |
|---|---|---|---|
| Extreme acceleration or abrupt turns | Large change in external trajectory with low interior proper acceleration | Tidal-gradient control; momentum exchange; structural protection; field stability | 3D trajectory, range/range rate, timing, multiple calibrated sensors, independent accelerometry |
| Hovering without visible lift | Force balance or local geodesic control without aerodynamic support | Energy source; station-keeping feedback; wind rejection | Range, wind field, mass/size estimate, downwash/acoustic/thermal data |
| Hypersonic motion without expected shock or heating | Suppressed coupling to the atmosphere or motion of a surrounding boundary region | Flow-field control; heat rejection; ionization/plasma management | Mach geometry, pressure/acoustic arrays, IR spectra, wake and atmospheric data |
| Transmedium transition | Continuous controlled trajectory across a sharp change in medium impedance | Cavitation/drag suppression; pressure management; boundary continuity | Synchronized air/water radar, sonar, EO/IR, splash/cavity/acoustic data |
| Low observable propulsion signature | Energy and momentum transfer outside familiar exhaust channels | Directional radiation, field-mediated exchange, environmental coupling, or signature masking | Broadband RF/optical/IR/acoustic spectra and momentum accounting |
| Apparent shape or signature change | Physical reconfiguration, variable boundary response, or sensor interaction | Plasma/optical effects; aspect changes; processing artifacts as control hypotheses | Raw multi-band imagery, point-spread function, calibration, resolved structure |
| Effective FTL | Change in global causal relationship rather than ordinary local superluminal motion | Stable horizons, navigability, sourceable stress-energy, chronology protection | No near-term observational package is sufficient; requires a consistent predictive theory |

## Capability stack

The minimum stack for the core P2 model is:

1. **Interior protection:** low proper acceleration and bounded tidal stress.
2. **Boundary generation:** creation of a stable, finite transition region.
3. **Trajectory control:** steering, acceleration, and termination of the region.
4. **Conservation closure:** explicit energy and momentum exchange.
5. **Environmental coupling control:** selectable interaction with matter and radiation.
6. **Sensing and navigation:** the ability to observe and control the exterior through the boundary.

FTL adds a seventh layer: **causal-structure control**.

## Case-admission rule

Do not translate screen motion directly into vehicle performance. For transverse motion,

\[
v_{\perp}=R\omega,
\]

so angular rate \(\omega\) is not a speed until range \(R\) and sensor geometry are known. Similar dependencies apply to size, acceleration, turn radius, and medium transition.

## Signature-first research

Each mechanism page should predict signatures before it is used to interpret cases. Examples include field gradients, spectral emissions, polarization changes, time/phase offsets, wake suppression, or correlated sensor disturbances. Retrofitting a mechanism to an already dramatic clip has low discriminatory value.
