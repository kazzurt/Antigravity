# The Electromagnetic Meissner Effect: State of the Art, Anomalies, and Research Frontiers

**Date:** 17 July 2026  
**Project:** Phase-Gated Gravity Control  
**Scope:** The established electromagnetic Meissner effect in superconductors, its real and alleged anomalies, and the parts of the modern research frontier that are relevant before attempting a gravitational analogy.

---

## Executive verdict

The Meissner effect is not merely the passive persistence of a pre-existing zero magnetic field. It is the equilibrium electromagnetic response of a phase-coherent charged condensate: screening currents form within a finite penetration layer, redistribute magnetic flux around the body, and lower the appropriate thermodynamic potential below the critical field. The field is not annihilated. It is displaced, its energy is exchanged with the superconducting condensate and external field source, and mechanical forces are transmitted through electromagnetic stress.

That makes it a richer and more useful model for gravity-control thinking than a simple “force cancellation” metaphor. Its full causal structure is

> external magnet or driven coil → applied field → superconducting phase and response kernel → surface screening current → altered exterior field → Maxwell stress on both bodies → energy and momentum exchange with the source, supports, and electromagnetic field.

Several genuine nonclassical Meissner responses exist:

- field-cooled **paramagnetic** Meissner signals;
- **nonlinear** field dependence of the penetration depth;
- **nonreciprocal** screening in parity-mixed or symmetry-broken systems;
- local paramagnetic response associated with **odd-frequency** proximity pairs;
- nonlocal Pippard electrodynamics and quantum-geometric contributions to superfluid stiffness;
- incomplete expulsion, flux trapping, vortex entry, and strongly geometry-dependent screening.

None of these is evidence that magnetic energy or momentum disappears, and none is a demonstrated coupling to gravity.

Two frontier claims require special caution. First, transient magnetic-field expulsion reported in optically driven YBa₂Cu₃O₆.₄₈ is experimentally real, but its identification as a transient Meissner state is no longer unique: a Physical Review X paper accepted on 15 July 2026 derives a flux-Floquet instability that can reproduce a same-direction exterior field transient without requiring light-induced superconductivity. Second, high-pressure hydride and nickelate measurements have advanced from indirect transport signatures to spatially resolved diamagnetic and trapped-flux imaging, but extreme-pressure sample inhomogeneity remains central to interpretation.

No reproducible “gravitational Meissner effect” is presently part of superconductivity. The 1992 rotating-YBCO weight-loss claim remains unreplicated, conventional weight-transition tests are null, and a 2025 cryogenic torsion balance constrained differential acceleration of superconducting niobium and copper to an Eötvös parameter no larger than \(2.0\times10^{-9}\) at 95% confidence.

### Correction to the project’s kinematic language

The project should use the following distinction:

- **Ordinary free fall:** gravity is unmodified and the craft follows a geodesic of the ambient physical metric.
- **Cancellation or exclusion of the local downward gravitational response:** if a craft initially at rest relative to Earth experiences zero net downward acceleration while Earth and the atmosphere continue to define the local frame, the intended result is **levitation**, not ordinary free fall.
- **Uniform added upward force:** can also support a body, but does not by itself establish a low-tidal, metric-protected worldtube.

The open question is therefore not whether levitation would require a rocket exhaust in every conceivable theory. Earth can be the external interaction partner in a hovering architecture. The hard question is whether any material phase can generate the required universal boundary response, field stress, and exterior reaction while remaining consistent with gravity experiments.

---

## 1. What the Meissner effect actually is

### 1.1 Operational definition

Meissner and Ochsenfeld found in 1933 that tin and lead entering the superconducting state in an applied magnetic field expelled flux from their bulk. In a sufficiently large, simply connected specimen, at fields below the relevant critical threshold,

\[
\mathbf B_{\rm bulk}\rightarrow 0
\]

apart from a surface layer of thickness comparable to the magnetic penetration depth. The field outside is correspondingly distorted and concentrated around the specimen.

The defining observation is not simply low resistivity. It is that the equilibrium magnetic state below the transition is largely independent of whether the field was applied before or after cooling, provided the sample can reach equilibrium and vortices or trapped flux do not prevent it.

### 1.2 Why a perfect conductor is not enough

For an ideal conductor with conductivity \(\sigma\rightarrow\infty\), Ohm’s law and Faraday’s law imply

\[
\frac{\partial \mathbf B}{\partial t}=0
\]

inside the material. Magnetic flux is frozen into its initial configuration. A sample cooled in a pre-existing field would retain that field.

A superconductor instead selects a phase-coherent thermodynamic state with a finite electromagnetic stiffness. Its screening current is an equilibrium response, not merely an eddy current left over from induction. This is why field cooling was conceptually decisive.

Real samples complicate this clean distinction:

- a type-II material may admit quantized vortices;
- defects can pin flux and block equilibration;
- multiply connected samples can retain quantized fluxoids;
- demagnetizing fields can make the exterior response highly nonuniform;
- rapid transitions can freeze metastable current patterns.

Thus “a superconductor expels all field” is a useful bulk idealization, not a universal description of every field, geometry, protocol, and material.

### 1.3 The field is excluded over a finite length

The London penetration depth is

\[
\lambda_L=\sqrt{\frac{m^\ast}{\mu_0 n_s q^{\ast 2}}},
\]

where

- \(m^\ast\) is the effective condensate carrier mass;
- \(q^\ast\) is its charge, normally \(-2e\) for a Cooper pair;
- \(n_s\) is the superfluid number density;
- \(\mu_0\) is the vacuum permeability.

For a flat surface occupying \(x>0\) and an applied field parallel to the surface,

\[
B(x)=B(0)e^{-x/\lambda_L}.
\]

Typical bulk penetration depths are tens to hundreds of nanometres, although low-density, anisotropic, disordered, two-dimensional, and multiband superconductors can have much larger effective lengths.

“Zero field in the interior” therefore means attenuation by many penetration depths. It is not a singular boundary condition at the atomic surface.

---

## 2. Controlled theoretical description

### 2.1 Gauge-invariant condensate response

Write the superconducting order parameter as

\[
\Psi(\mathbf x)=|\Psi|e^{i\theta}.
\]

The gauge-invariant superfluid velocity and current are

\[
\mathbf v_s=\frac{1}{m^\ast}\left(\hbar\nabla\theta-q^\ast\mathbf A\right),
\qquad
\mathbf J_s=n_s q^\ast\mathbf v_s.
\]

For a simply connected equilibrium region without phase winding,

\[
\nabla\times\mathbf J_s
=-\frac{n_s q^{\ast 2}}{m^\ast}\mathbf B
=-\frac{1}{\mu_0\lambda_L^2}\mathbf B .
\]

Combining this second London equation with

\[
\nabla\times\mathbf B=\mu_0\mathbf J_s,
\qquad
\nabla\cdot\mathbf B=0
\]

gives

\[
\nabla^2\mathbf B=\frac{\mathbf B}{\lambda_L^2}.
\]

The photon has not acquired a vacuum rest mass. The condensate produces a material response kernel that makes transverse electromagnetic fields massive inside the superconducting phase, in the same practical sense that a plasma changes electromagnetic propagation. This condensed-matter Anderson–Higgs response ends at the material boundary.

The first London equation,

\[
\frac{\partial\mathbf J_s}{\partial t}
=\frac{n_s q^{\ast 2}}{m^\ast}\mathbf E,
\]

describes acceleration of the condensate in an electric field in its simplest local form. It is not, by itself, the equation that distinguishes a superconductor from a hypothetical perfect conductor; the phase-stiffness relation and the second London equation do that.

### 2.2 Ginzburg–Landau free energy

Near the transition, a controlled phenomenological description is

\[
\mathcal F[\Psi,\mathbf A]
=\int d^3x\left[
\alpha|\Psi|^2+\frac{\beta}{2}|\Psi|^4
+\frac{1}{2m^\ast}\left|(-i\hbar\nabla-q^\ast\mathbf A)\Psi\right|^2
+\frac{\mathbf B^2}{2\mu_0}
\right].
\]

Varying with respect to \(\Psi^\ast\) gives

\[
\alpha\Psi+\beta|\Psi|^2\Psi
+\frac{1}{2m^\ast}(-i\hbar\nabla-q^\ast\mathbf A)^2\Psi=0.
\]

Varying with respect to \(\mathbf A\) gives the supercurrent

\[
\mathbf J_s
=\frac{q^\ast}{m^\ast}
\operatorname{Re}\!\left[
\Psi^\ast(-i\hbar\nabla-q^\ast\mathbf A)\Psi
\right].
\]

Two material lengths emerge:

\[
\xi=\sqrt{\frac{\hbar^2}{2m^\ast|\alpha|}},
\qquad
\lambda=\sqrt{\frac{m^\ast}{\mu_0 q^{\ast 2}|\Psi_0|^2}},
\qquad
\kappa=\frac{\lambda}{\xi}.
\]

- \(\kappa<1/\sqrt 2\): type-I behavior, with a positive normal–superconducting interface energy and a thermodynamic critical field \(H_c\).
- \(\kappa>1/\sqrt 2\): type-II behavior, with stable vortices between \(H_{c1}\) and \(H_{c2}\).

The clean Meissner state is the vortex-free free-energy minimum below the first relevant critical field. Surface barriers can keep it metastable above that equilibrium threshold, up to a superheating or vortex-entry field.

### 2.3 Microscopic origin and limits of the London model

BCS theory derives the electromagnetic response from a paired fermionic ground state. The static linear current response has the schematic form

\[
J_i(\mathbf q)=-K_{ij}(\mathbf q)A_j(\mathbf q),
\]

where \(K_{ij}\) contains diamagnetic and paramagnetic contributions. Gauge invariance requires the complete kernel; retaining only one term can produce spurious results.

The local London limit assumes that the vector potential varies slowly on the pair-correlation scale. Pippard showed that in clean superconductors the response may be nonlocal:

\[
J_i(\mathbf x)
=-\int d^3x'\,K_{ij}(\mathbf x-\mathbf x')A_j(\mathbf x').
\]

Nonlocality can make the field profile non-exponential and, under suitable conditions, weakly nonmonotonic. It does not create field or energy. It redistributes the response over the coherence scale and changes how penetration-depth data must be interpreted.

Modern multiband theory further separates a conventional intraband superfluid weight from a geometric interband term. In flat or narrow bands, ordinary band velocity can be small while quantum metric contributions keep the phase stiffness and Meissner response finite.

### 2.4 Fluxoid quantization

Single-valuedness of the condensate phase requires

\[
\oint\nabla\theta\cdot d\mathbf l=2\pi n.
\]

Therefore

\[
\oint \left(m^\ast\mathbf v_s+q^\ast\mathbf A\right)\cdot d\mathbf l=nh.
\]

Deep in a thick superconducting ring, where \(\mathbf v_s\) is negligible,

\[
\Phi=n\Phi_0,
\qquad
\Phi_0=\frac{h}{2e}
=2.067833848\ldots\times10^{-15}\ {\rm Wb}.
\]

The distinction between flux and fluxoid matters in thin, small, or current-carrying structures. Trapped quantized flux is not a failure of superconductivity; it is another consequence of condensate phase coherence.

### 2.5 Thin films and the Pearl length

For a film of thickness \(d\ll\lambda\), screening currents are distributed across the thickness and magnetic fields spread far into the surrounding vacuum. A common two-dimensional screening scale is

\[
\Lambda=\frac{2\lambda^2}{d}.
\]

This Pearl length can greatly exceed the bulk penetration depth. Consequently a micron-scale two-dimensional superconductor may screen only a tiny fraction of a uniform applied field while still possessing a genuine condensate and measurable local superfluid stiffness.

---

## 3. Energy, force, and momentum closure

### 3.1 Field exclusion is field displacement

Magnetic flux lines do not terminate at a superconducting surface because

\[
\nabla\cdot\mathbf B=0.
\]

They bend around the sample or enter as vortices. In a simple Meissner geometry, the surface current creates a field that cancels the applied field in the bulk and reinforces it in portions of the exterior. A local detector near an edge can therefore see a field larger than the applied field even though the sample is diamagnetic.

This exterior enhancement is not amplification in the energetic sense. It is the necessary spatial redistribution of flux.

### 3.2 Magnetic energy and pressure

The vacuum magnetic energy density is

\[
u_B=\frac{B^2}{2\mu_0}.
\]

The same expression sets the characteristic magnetic pressure:

\[
p_B=\frac{B^2}{2\mu_0}.
\]

Reference values are

| Field | Energy density / pressure |
|---:|---:|
| \(0.01\ {\rm T}\) | \(39.8\ {\rm J\,m^{-3}}=39.8\ {\rm Pa}\) |
| \(0.1\ {\rm T}\) | \(3.98\times10^3\ {\rm J\,m^{-3}}=3.98\ {\rm kPa}\) |
| \(1\ {\rm T}\) | \(3.98\times10^5\ {\rm J\,m^{-3}}=398\ {\rm kPa}\) |
| \(10\ {\rm T}\) | \(3.98\times10^7\ {\rm J\,m^{-3}}=39.8\ {\rm MPa}\) |

Excluding \(1\ {\rm T}\) from \(1\ {\rm cm^3}\) corresponds to a magnetic-energy scale of about \(0.398\ {\rm J}\). The exact work performed during insertion or phase switching depends on geometry and on what the external magnet or current supply holds fixed.

A steady superconducting current does not require continuous electrical power, but establishing, changing, or destroying the state exchanges energy. The condensation energy, kinetic energy of the supercurrent, magnetic field, heat bath, and source circuit all participate.

### 3.3 Force is obtained from stress, not from “missing field”

In vacuum the Maxwell stress tensor is

\[
T_{ij}^{\rm EM}
=\frac{1}{\mu_0}
\left(B_iB_j-\frac{1}{2}\delta_{ij}B^2\right)
+\epsilon_0
\left(E_iE_j-\frac{1}{2}\delta_{ij}E^2\right).
\]

The net electromagnetic force on a body can be evaluated from

\[
F_i=\oint_{\partial V}T_{ij}^{\rm EM}n_j\,dA
-\frac{d}{dt}\int_V g_i^{\rm EM}\,dV,
\qquad
\mathbf g_{\rm EM}=\epsilon_0\mathbf E\times\mathbf B.
\]

For a static configuration the field-momentum derivative vanishes, leaving a surface-stress integral. A field gradient or asymmetric geometry is required for net force. An ideal diamagnet in a perfectly uniform field can experience torque or surface stress without a net translational force.

Levitation above a magnet occurs because the distorted field has lower and higher energy regions and the Maxwell stress is asymmetric. The magnet, its mount, or its source coil experiences the equal reaction. Flux pinning can add restoring forces and stable lateral positioning.

### 3.4 Conservation during the transition

The local energy balance is schematically

\[
\partial_t(u_{\rm EM}+u_{\rm matter})
+\nabla\cdot(\mathbf S+\mathbf S_{\rm matter})=0,
\qquad
\mathbf S=\frac{1}{\mu_0}\mathbf E\times\mathbf B.
\]

Momentum balance has the corresponding form

\[
\partial_t(\mathbf g_{\rm EM}+\mathbf g_{\rm matter})
+\nabla\cdot(\mathbf T_{\rm EM}+\mathbf T_{\rm matter})=0.
\]

During flux expulsion, time-dependent magnetic fields generate electric fields; electromagnetic forces accelerate condensate, normal carriers, and lattice degrees of freedom; Poynting flux and mechanical stress carry energy and momentum across the boundary. Time-dependent Ginzburg–Landau theory is an effective description of much of this nonequilibrium evolution.

There is an active minority debate about whether the conventional account makes the reversible microscopic transfer of angular momentum at a moving normal–superconducting boundary sufficiently explicit. J. E. Hirsch argues that radial charge flow and hole-like normal carriers are required. A. V. Nikulov and the conventional literature reject that necessity and point to phase quantization and standard electromagnetic response. This is a legitimate foundational dispute in the literature, but it is not an observed failure of energy or momentum conservation, nor is there a reproducible anomalous impulse associated with an ordinary Meissner transition.

### 3.5 What this means for the word “momentum sink”

“Momentum sink” is misleading if it suggests a dissipative dump or mandatory exhaust. The better requirement is **momentum-exchange closure**:

- In magnetic levitation, the magnet or coil is the external partner.
- In Earth-hovering gravity control, Earth and the modified gravitational or new-field configuration could in principle be the partner.
- In deep space, an Earth-coupled mechanism fades unless it couples to another external field, radiates momentum, or interacts with distant matter.
- A closed craft cannot obtain center-of-mass acceleration solely by rearranging internal stresses.

The Meissner effect satisfies this closure transparently because its field stress and reaction partner are measurable.

---

## 4. What real superconductors do

### 4.1 Type-I superconductors

Below the thermodynamic critical field, a macroscopic type-I sample favors the Meissner state. Demagnetization can generate an intermediate state of normal and superconducting domains before the entire sample becomes normal. Domain geometry, surface energy, defects, and thermal history determine the observed pattern.

The statement \(B=0\) in the bulk is best realized in thick, clean, simply connected type-I material at fields well below the critical field.

### 4.2 Type-II superconductors

For \(H<H_{c1}\), a type-II material can be in a Meissner state. Between \(H_{c1}\) and \(H_{c2}\), magnetic flux penetrates as vortices carrying approximately one flux quantum each. Each vortex has a normal or strongly suppressed core of radius set by \(\xi\), surrounded by circulating supercurrent over a scale set by \(\lambda\).

Defects pin vortices. The resulting metastability produces

- hysteretic magnetization;
- trapped flux after the applied field is removed;
- critical currents;
- levitation with strong positional stability;
- losses when vortices move under alternating force.

“Quantum locking” demonstrations are therefore a combined result of superconductivity, vortices, and pinning. They should not be identified with pure Meissner expulsion.

### 4.3 Cooling protocol

- **Zero-field cooling (ZFC):** cool below \(T_c\), then apply the field. This typically maximizes diamagnetic shielding.
- **Field cooling (FC):** cool through \(T_c\) with field present. Equilibrium type-I material expels field, but type-II materials may trap vortices and display much smaller diamagnetism or even a positive magnetic moment.
- **Field warming and remanence:** reveal hysteresis, vortex escape, and trapped-flux relaxation.

Any claim of anomalous Meissner behavior is incomplete without stating the protocol, field magnitude, sweep rate, sample geometry, demagnetizing correction, and detector position.

### 4.4 Susceptibility is geometry dependent

The ideal shorthand \(\chi=-1\) in SI applies only after specifying the internal field and geometry. For a finite body,

\[
\mathbf H_{\rm int}=\mathbf H_{\rm applied}-\mathbf N\mathbf M,
\]

where \(\mathbf N\) is the demagnetizing tensor. Raw magnetic moment divided by applied field can appear more negative than \(-1\), or vary sharply with orientation, without any anomalous permeability.

This is a frequent source of false “over-screening” claims.

### 4.5 State-of-the-art probes

Modern work increasingly combines global and local measurements:

- SQUID magnetometry and susceptometry;
- scanning SQUID and nano-SQUID-on-tip microscopy;
- low-energy muon spin rotation for depth profiles;
- magnetic force microscopy for local Meissner force;
- magneto-optical imaging;
- microwave surface impedance and kinetic inductance;
- nitrogen-vacancy centres in diamond for wide-field vector magnetometry;
- simultaneous transport, magnetic imaging, stress mapping, and chemical mapping.

The frontier has moved from “does a bulk moment change?” to spatially resolved tests of where screening occurs, how much of the sample participates, and whether flux exclusion, resistance, structure, and order parameter change together.

---

## 5. Anomaly taxonomy

### 5.1 Summary table

| Phenomenon | Experimental status | Best current interpretation | Does it violate the standard conservation picture? | Relevance to gravity analogy |
|---|---|---|---|---|
| Paramagnetic Meissner effect / Wohlleben effect | Reproduced in granular cuprates, conventional samples, mesoscopic disks, and hybrids | Flux compression, metastable giant vortices, surface barriers, \(\pi\)-junction networks, or odd-frequency proximity response depending on system | No | Shows that state history and boundary topology can reverse a measured moment without producing energy |
| Nonlinear Meissner effect | Predicted in 1992; directly resolved in clean nodal superconductors in 2022 | Field-induced quasiparticles modify \(n_s\), hence \(\lambda(B)\) | No | A phase-gated response need not be linear; nonlinear thresholds can diagnose the microscopic gap |
| Nonreciprocal Meissner response | Strong theoretical basis; closely related nonreciprocal transport observed | Broken inversion and time-reversal symmetries permit direction-dependent stiffness; ordinary Meissner and asymmetric vortex barriers can mimic exotic diode effects | No | Directional response is possible, but geometry and vortices must be excluded before assigning new physics |
| Odd-frequency paramagnetic response | Local low-energy muon evidence in Au/Ho/Nb; theory continues to develop | Induced odd-frequency pair correlations can add paramagnetic terms; total stability depends on all even- and odd-frequency channels | No | Local sign reversal is allowed without a bulk anti-screen or universal repulsion |
| Nonlocal and nonmonotonic penetration | Established Pippard physics; material-specific modern tests | Current depends on the vector potential over a coherence-sized region | No | A useful screening kernel can be nonlocal; a gravitational analogue must specify its kernel and causal domain |
| Incomplete expulsion and trapped flux | Ubiquitous in type-II and defective materials | Vortices, pinning, surface barriers, finite cooling rate | No | Apparent shielding fraction is not a material constant and levitation is often pinning-dominated |
| Microscopic momentum-transfer puzzle | Active theoretical dispute, not a unique experimental anomaly | Conventional phase-stiffness/electrodynamic account versus proposed radial-charge-flow account | No observed violation | Highlights exactly why a proposed gravity analogue must track boundary stress and transient momentum |
| Optically driven YBCO exterior-field transient | Peer-reviewed measurement; interpretation contested as of July 2026 | Initially interpreted as transient flux expulsion; a newly accepted flux-Floquet model produces a competing non-Meissner explanation | No | Excellent example of why exterior-field shape and phase switching alone do not uniquely identify a Meissner state |
| High-pressure hydride/nickelate diamagnetism | Increasingly strong local imaging plus transport and trapped flux | Superconductivity with substantial micron-scale heterogeneity; material and pressure dependence remain active | No | Demonstrates powerful spatial validation methods under difficult conditions |
| Superconductor gravity/weight anomalies | Original claims exist; no accepted replication; modern precision tests null | Experimental systematics or unsupported claims under present evidence | No credible anomaly established | Not evidence for gravitational screening |

### 5.2 Paramagnetic Meissner effect

Braunisch and collaborators reported in 1992 that field-cooled Bi-based high-\(T_c\) samples developed a positive moment below the superconducting transition. The effect is real but is not a single universal mechanism.

Important mechanisms include:

1. **Flux compression.** Superconductivity nucleates at the boundary while interior flux is temporarily trapped. The shrinking normal region compresses flux, and the resulting current distribution can yield a positive net moment.
2. **Surface and geometrical barriers.** Vortex entry and exit are not symmetric. A metastable field-cooled distribution can have a moment opposite to the equilibrium Meissner moment.
3. **Giant vortex states in mesoscopic samples.** Confined geometry can stabilize multi-quantum states whose magnetization is paramagnetic over a finite range.
4. **\(\pi\)-junction networks.** In granular unconventional superconductors, sign-changing order parameters can create frustrated loops and spontaneous currents.
5. **Odd-frequency proximity pairing.** In superconductor–magnet heterostructures, induced pair amplitudes can contribute a local paramagnetic kernel.

A positive field-cooled moment does not imply that the entire sample has a stable negative superfluid density. A homogeneous equilibrium phase with an unbounded paramagnetic kernel would generally be unstable. The total free energy and the complete response kernel decide stability.

### 5.3 Nonlinear Meissner effect

The linear London relation assumes that the condensate density is independent of superflow. In a nodal superconductor, screening flow Doppler-shifts low-energy quasiparticles:

\[
\delta E\sim \mathbf v_s\cdot\mathbf p_F.
\]

This reduces the superfluid density and produces, in the ideal clean low-temperature limit,

\[
\Delta\lambda(B)\propto |B|.
\]

Yip and Sauls predicted this for cuprates in 1992. Wilcox and collaborators reported a clear observation in CeCoIn₅ and LaFePO in 2022, while using the response to distinguish nodes from deep gap minima.

The nonlinear Meissner effect is an intrinsic spectroscopy tool. Extrinsic weak links, vortices, heating, and surface defects can also produce nonlinear inductance, so experimental geometry and field range remain essential.

### 5.4 Nonreciprocal response and the superconducting diode

When both inversion and time-reversal symmetries are broken, the free energy may contain terms odd in superflow. Screening or critical current can then depend on direction. Theory predicts a nonreciprocal penetration depth in parity-mixed superconductors.

However, Hou and collaborators showed in 2023 that a large diode effect, reaching 65% in an EuS-coupled device, can arise in otherwise conventional thin films from Meissner screening combined with asymmetric vortex edge and surface barriers. Thus a striking directional transport signal is not automatically evidence for exotic finite-momentum pairing.

This is a general methodological lesson: first calculate the conventional boundary-current and vortex contribution in the actual geometry.

### 5.5 Odd-frequency pairing

Odd-frequency superconducting correlations change sign under exchange of the pair time or frequency coordinate. They are commonly induced at magnetic or multiband interfaces.

Low-energy muon measurements in an Au/Ho/Nb trilayer found a small local field enhancement in Au below the Nb transition, consistent with an intrinsic paramagnetic response from odd-frequency correlations. Yet the complete device remained thermodynamically stable.

The 2026 quantum-geometric analysis by Bhattacharya and Black-Schaffer further weakens the old rule of thumb that odd-frequency pairing must be paramagnetic. In two-band models, geometric interband processes yield a diamagnetic odd-frequency contribution, which can dominate in flat bands.

The correct conclusion is not “odd-frequency pairs attract magnetic field.” It is that the sign and magnitude of the Meissner kernel depend on band curvature, interband geometry, pair symmetry, and all coexisting condensate components.

### 5.6 The dynamics and momentum debate

Equilibrium London, Ginzburg–Landau, and BCS response is extremely well tested. The more subtle question is how a real finite sample reaches that equilibrium during a transition while transferring the mechanical momentum of the emerging surface current.

Hirsch’s 2025–2026 papers argue that conventional theory omits a necessary radial charge flow and propose sample geometries intended to distinguish it. Nikulov’s 2026 response argues that phase quantization already explains the persistent current and that radial flow is neither necessary nor compatible with the full set of macroscopic quantum phenomena.

This debate should remain visible rather than being overstated in either direction:

- it concerns microscopic transition dynamics and interpretation;
- it has not exposed a failure of the static Meissner equations;
- it has not produced a reproducible anomalous force;
- it offers testable geometry-dependent proposals;
- it reinforces the need to instrument source current, exterior field, body recoil, heat, and charge transients simultaneously.

### 5.7 Light-driven field expulsion

Fava and collaborators used an ultrafast magneto-optic detector near YBa₂Cu₃O₆.₄₈. Mid-infrared pumping above equilibrium \(T_c\) produced a same-direction exterior field transient of roughly \(B_{\rm ext}/1000\) at 100 K, lasting about 1 ps, with a smaller signal at 300 K. Magnetostatic modelling related the signal to a transient diamagnetic region.

This was an important advance because it measured a magnetic response rather than inferring superconductivity from optical conductivity alone.

As of this report, it is not a unique demonstration of a transient Meissner state. Michael, De Santis, Demler, and Lee developed a driven bilayer phase model with a flux-Floquet instability that can generate a transient exterior magnetic field with the observed sign. Their paper was accepted by Physical Review X on 15 July 2026.

The decisive next measurements are spatially resolved field maps on multiple sides of the sample, pump-polarization and frequency scaling, simultaneous conductivity and phase-sensitive response, and a quantitative comparison of the complete field topology with both models.

### 5.8 High-pressure superconductors

Transport under pressure can show a resistance drop without establishing bulk superconductivity. The modern frontier is therefore direct local magnetometry inside diamond anvil cells.

Key advances include:

- trapped-flux measurements in H₃S and LaH₁₀;
- NV-centre imaging of diamagnetism and flux trapping in CeH₉ at megabar pressure;
- micrometre-resolved NV maps of Hg-1223 under pressure;
- simultaneous mapping of diamagnetism, trapped flux, stress, composition, and transport in La₃Ni₂O₇.

These experiments show that superconductivity can occupy only selected micron-scale regions controlled by stress and stoichiometry. They strengthen some high-pressure claims while also demonstrating why a global transport trace or background-subtracted magnetic moment is insufficient.

### 5.9 Gravity-adjacent claims are not Meissner anomalies

Podkletnov and Nieminen reported a \(0.05\%\)–\(0.3\%\) apparent weight reduction above a rotating YBCO disk in 1992. The paper did not provide a covariant gravity model, a source of the claimed field, or a conservation-complete response, and the effect has not achieved accepted independent replication.

More controlled work found no weight anomaly during YBCO or BSCCO transitions, rotation, or low-frequency excitation. The 2025 Eöt-Wash cryogenic torsion-balance experiment compared superconducting niobium with copper and obtained

\[
|\eta_{\mathrm{Nb^\ast-Cu}}|\le 2.0\times10^{-9}
\quad (95\%\ {\rm confidence}).
\]

The same paper reported a much weaker direct constraint on a speculative Cooper-pair-specific anomaly because Cooper-pair condensation energy is only a small fraction of the test-body mass.

These results do not prove that every explicit new universal field is impossible. They do show that “superconductivity itself screens gravity” is not an observed extension of the electromagnetic Meissner effect.

---

## 6. Where the cutting edge is in 2026

### 6.1 Quantum geometry and superfluid weight

In an ordinary dispersive band, phase stiffness is tied intuitively to carrier density and effective mass. In flat and multiband systems, Bloch-wavefunction geometry adds an interband contribution. Peotta and Törmä showed that a topologically nontrivial flat band can possess finite superfluid weight even when its conventional group velocity vanishes.

Current work is making this connection microscopic and local:

- Hu and Huang identify pair-transfer and virtual interband processes behind geometric superfluid weight.
- Porlles and Chen express multiband Meissner weight in terms of the quasiparticle quantum metric and define a real-space superfluid-weight marker that can handle disorder.
- Bhattacharya and Black-Schaffer show that quantum geometry can stabilize a diamagnetic odd-frequency response.

This frontier concerns the origin and distribution of electromagnetic stiffness. It does not imply an enlarged coupling to gravity, but it is directly relevant to material-state gating because it shows that a response kernel can change strongly while ordinary mass and charge change very little.

### 6.2 Direct imaging in atomically thin and high-pressure systems

As of March 2026, a preprint reports direct nano-SQUID imaging of static fringe fields in rhombohedral graphene. The sample screened only about \(100\) parts per million of the applied field, yet nanotesla imaging resolved the onset of diamagnetism, vortex entry, and local superfluid stiffness.

The important methodological result is that a tiny global shielding fraction need not mean an absent condensate in a two-dimensional micron-scale device. Field topology, geometry, and local stiffness must be modelled together.

NV-centre diamond-anvil work provides the complementary extreme-pressure frontier: local magnetic response can be correlated pixel by pixel with stress, chemistry, and transport.

### 6.3 Cavity-altered equilibrium superconductivity

Keren and collaborators interfaced a molecular superconductor with hexagonal boron nitride whose hyperbolic phonon-polariton modes resonate with a molecular vibration implicated in pairing. Magnetic-force microscopy measured a strong local suppression of superfluid density under the resonant hBN layer, whereas nonresonant control interfaces did not.

This is one of the closest established electromagnetic analogues to the project’s “phase gate” concept:

> engineered electromagnetic environment → modified molecular mode → changed superconducting ground-state stiffness → changed Meissner force.

The effect suppresses rather than enhances stiffness in the demonstrated device, and it remains electromagnetic condensed-matter physics. Still, it shows that boundary environment and zero-point electromagnetic modes can measurably alter a phase response without continuous optical pumping.

### 6.4 Nonequilibrium superconductivity

Ultrafast driving can transiently modify Josephson plasma modes, optical conductivity, phase fluctuations, and magnetic response. The frontier question is no longer whether light can create superconducting-like spectra; it is which observables jointly establish a driven superconducting state.

A strong claim now requires, ideally:

- a phase-sensitive response;
- magnetic screening with the correct spatial topology;
- a stiffness or inductive signature;
- a gap or pair-correlation signature;
- temporal coincidence among them;
- exclusion of nonlinear optical, thermal, Floquet, and magnetic alternatives.

### 6.5 Nonlinear and nonreciprocal screening as spectroscopy

Penetration depth is increasingly used as a probe of

- nodes versus deep gap minima;
- parity mixing;
- finite-momentum pairing;
- odd-frequency components;
- nonlocality;
- multiband quantum geometry.

The practical challenge is to separate intrinsic condensate response from weak links, edge barriers, vortex entry, heating, and demagnetization. Same-device reversal of field, current, crystal axis, and magnetic order is the high-information strategy.

### 6.6 Vortex entry and radio-frequency limits

Superconducting radio-frequency cavities seek to preserve a vortex-free Meissner state at the largest possible surface field. Current research focuses on

- surface defects that nucleate vortices below the ideal superheating field;
- multilayers that redistribute screening current;
- nitrogen or impurity profiles that change the superheating field;
- trapped-vortex microwave losses;
- direct depth-resolved muon and near-field microwave measurements.

This engineering frontier is valuable for the gravity project because it treats the boundary layer as a load-bearing field-control structure with explicit instability thresholds, rather than as an ideal zero-field material.

---

## 7. What can and cannot be carried into a gravity analogy

### 7.1 The disciplined mapping

| Electromagnetic superconductor | Required gravitational or universal-field analogue |
|---|---|
| Gauge potential \(A_\mu\) | A specified metric, scalar, vector, connection, or other covariant field |
| Charged condensate phase \(\theta\) | A material order parameter with an explicit invariant coupling to that field |
| Gauge-invariant momentum \(\hbar\nabla\theta-q^\ast\mathbf A\) | A derived covariant momentum or strain combination, not an analogy coefficient |
| Response kernel \(J_i=-K_{ij}A_j\) | A causal, stable field-response kernel derived from an action |
| London length \(\lambda^{-2}=\mu_0n_sq^{\ast2}/m^\ast\) | A derived penetration or screening length with stated source, units, and material dependence |
| Surface supercurrent | A real stress-energy, scalar charge, vector charge, or boundary degree of freedom |
| Exterior flux redistribution | A solved exterior metric or new-field profile |
| Maxwell stress | A conserved stress tensor for the new field and matter |
| Magnet or source coil | Earth, another astronomical source, background field reservoir, or radiation channel |
| Critical fields and vortex entry | Stability, nonlinear threshold, domain, defect, and breakdown limits |

### 7.2 Magnetic screening is not gravitoelectric screening

The Meissner effect screens the magnetic field using circulating electric current. In the weak-field decomposition of general relativity, ordinary terrestrial weight is dominated by the gravitoelectric potential,

\[
\nabla^2\Phi=4\pi G\rho,
\qquad
\mathbf g=-\nabla\Phi.
\]

Gravitomagnetism is sourced by mass current and is normally much smaller. Even a hypothetical enhancement of a gravitomagnetic response would not automatically cancel Earth’s Newtonian gravitoelectric acceleration.

A gravitational analogue must therefore say which of the following it modifies:

1. the gravitoelectric field or physical metric;
2. the coupling of matter to that metric;
3. an additional nearly universal field whose force cancels weight;
4. inertial response;
5. only the much smaller gravitomagnetic sector.

Calling all five “gravitational Meissner effects” hides the central physical distinction.

### 7.3 Field cancellation versus coupling cancellation

**Field cancellation or redirection** would create an interior region with reduced physical gravitational acceleration or curvature. It should generally alter the exterior field and exert a reaction on Earth or another source through the new field stress.

**Coupling cancellation** would leave the ambient field in place but change how selected matter responds. It risks composition dependence and does not automatically make hull, occupants, air, clocks, and payload share one physical metric.

For a craft worldtube, the minimum target is stronger than supporting one test mass. A successful mechanism must make the hull, occupants, payload, and internal atmosphere share the same low-acceleration, low-tidal trajectory or must explicitly support each component without damaging differential stress.

### 7.4 Why Earth can be the reaction partner for hover

If a new field creates an upward force on a craft by coupling it to Earth, Earth receives the opposite impulse. No propellant exhaust is required for static hover, just as a superconducting levitator needs no exhaust while interacting with a magnet.

This does not make the configuration free:

- the field and boundary layer carry stress;
- the apparatus must be switched into the levitating state;
- Earth’s source field or a background may supply or absorb energy depending on the trajectory;
- changing altitude changes field energy and potential energy;
- reaction forces exist even if Earth’s acceleration is immeasurably small;
- a deep-space craft loses the same interaction unless another external reservoir is present.

Thus the conservation question is not “where is the exhaust?” It is “what covariant field and external body carry the equal momentum, and what work is done during switching and motion?”

### 7.5 What an actual gravitational Meissner proposal must derive

A technically meaningful proposal needs all of the following:

1. **Field definition.** Identify the metric or new field whose invariant produces the downward acceleration.
2. **Action.** Give a covariant, stable action for that field, matter, and the material order parameter.
3. **Order-parameter coupling.** Derive the analogue of \(\hbar\nabla\theta-qA\) or \(K_{ij}\); do not insert an unexplained gravitational permeability.
4. **Boundary solution.** Solve the interior, penetration layer, and exterior profile for a finite geometry.
5. **Universality.** Show why hull, occupants, payload, and clocks respond consistently.
6. **Tidal response.** Calculate curvature or differential acceleration, not just the center-of-mass force.
7. **Stress tensor.** Identify boundary pressure and structural load.
8. **Momentum exchange.** Calculate the reaction on Earth or the momentum radiated.
9. **Energy accounting.** Track switching work, stored field energy, motion through a gradient, and dissipation.
10. **Stability and constraints.** Check ghosts, gradient instabilities, superluminality, fifth-force tests, equivalence principle, PPN bounds, and laboratory nulls.
11. **Distinctive experiment.** Predict a phase-reversible field or force topology that conventional electromagnetic, thermal, acoustic, and mechanical effects cannot reproduce.

Until those exist, “gravity behaves like the Meissner effect” is a design prompt, not a mechanism.

---

## 8. Project implications and recommended next work

### 8.1 What survives the deeper study

The strongest transferable ideas are:

- a material phase can change a field-response kernel by orders of magnitude relative to its normal state;
- a thin boundary layer can control the field in a much larger interior;
- equilibrium field control can persist without continuous drive;
- exterior field redistribution and stress provide the reaction path;
- geometry, topology, defects, and history can dominate the observable;
- nonlinear thresholds and domains can make naive linear scaling fail;
- the same sample can be state-reversed, enabling unusually strong differential experiments.

The weakest transferable ideas are:

- “zero resistance causes field exclusion”;
- “a superconductor has permeability exactly zero in every geometry”;
- “magnetic levitation is pure Meissner expulsion”;
- “field cancellation removes the need for energy or reaction”;
- “the London moment demonstrates electromagnetic-to-gravitational transduction”;
- “an emergent or analog metric is physical spacetime curvature.”

### 8.2 A useful electromagnetic precursor experiment

Before building any gravity extension, the project would benefit from a conservation-complete Meissner benchmark in which one apparatus measures:

1. the three-dimensional exterior field before and after the superconducting transition;
2. source-coil current, voltage, and returned electrical energy;
3. force on the superconducting sample;
4. equal reaction force on the magnet or source coil;
5. sample temperature and heat flow;
6. trapped flux and vortex entry;
7. geometry and demagnetizing response;
8. the normal/superconducting state reversal at fixed apparatus geometry.

The purpose would not be to discover a new electromagnetic anomaly. It would produce a validated source–field–stress–reaction accounting template against which any claimed gravitational analogue can be judged.

### 8.3 Highest-value frontier to monitor

For phase-gated field control, the most relevant continuing electromagnetic lanes are ranked:

1. **Cavity- and interface-altered superfluid stiffness** — direct example of an engineered environment changing the equilibrium Meissner kernel.
2. **Quantum-geometric superfluid weight** — a microscopic route by which collective stiffness can be large or sign-structured without simple carrier-mass scaling.
3. **Ultrafast magnetic topology of driven states** — valuable if experiments distinguish true transient screening from flux-Floquet and optical alternatives.
4. **Local Meissner imaging in 2D and high-pressure systems** — the best measurement technology for small, heterogeneous, phase-gated responses.
5. **Nonreciprocal and odd-frequency response** — useful for directional gating, but especially vulnerable to conventional edge, vortex, and geometry artifacts.

### 8.4 Decision

**Go** on a focused Meissner-state research lane as a boundary-response and conservation template.

**No-go** on treating electromagnetic superconductivity itself as evidence of gravitational shielding.

**Next milestone:** construct the minimum covariant analogue of a London response and prove whether a stable material-dependent penetration length for the relevant gravitoelectric or universal field can exist without violating equivalence-principle and fifth-force constraints. The model must reproduce the full electromagnetic logic—interior, boundary, exterior, stress, energy, and reaction—not merely its visual signature of levitation.

---

## 9. Evidence map and verification status

The project literature-verification helper was not present in the local skill installation. Each item below was therefore checked against an official publisher page, journal archive, PubMed/OSTI/CERN record, or the current arXiv record. “Publisher verified” means bibliographic identity and status were confirmed at the journal or DOI landing page; it does not mean independent replication.

| Work | Venue and status | Method | Main result used here | Relevance | Verification |
|---|---|---|---|---|---|
| Meissner & Ochsenfeld (1933) | Naturwissenschaften; peer-reviewed primary | Field distribution around Sn and Pb through transition | Bulk flux expulsion | Discovery and operational definition | DOI/index verified |
| London & London (1935) | Proc. Royal Society A; peer-reviewed primary theory | Phenomenological electrodynamics | London equations and finite penetration | Minimum classical response scaffold | Publisher/index verified |
| Ginzburg & Landau (1950) | ZhETF; peer-reviewed primary theory | Order-parameter free energy | Coherence length, penetration depth, interface physics | Finite-geometry and stability framework | CERN/OSTI archive verified; no DOI assigned |
| Pippard (1953) | Proc. Royal Society A; peer-reviewed primary | Penetration-depth experiments and nonlocal kernel | Local London theory is incomplete in clean materials | Nonlocal boundary response | Publisher/index verified |
| Bardeen, Cooper & Schrieffer (1957) | Physical Review; peer-reviewed primary theory | Microscopic paired-electron theory | Microscopic condensate and electromagnetic response | Established microscopic basis | APS verified |
| Abrikosov (1957) | Soviet Physics JETP; peer-reviewed primary theory | GL vortex solution | Type-II mixed state and quantized vortices | Separates Meissner expulsion from flux penetration | JETP/OSTI archive verified; no DOI assigned |
| Braunisch et al. (1992) | PRL; peer-reviewed primary experiment | Field-cooled magnetometry of Bi cuprates | Positive field-cooled moment | Original modern PME observation | APS/PubMed verified |
| Yip & Sauls (1992) | PRL; peer-reviewed primary theory | Nodal quasiparticle response | Linear-in-field low-\(T\) correction to \(\lambda\) | Nonlinear Meissner prediction | APS/PubMed and arXiv verified |
| Koshelev & Larkin (1995) | PRB; peer-reviewed primary theory | Field-cooled plate model | Flux compression can produce PME | Conventional explanation for sign reversal | APS/PubMed verified |
| Di Bernardo et al. (2015) | PRX; peer-reviewed primary experiment | Depth-resolved low-energy muon probe of Au/Ho/Nb | Local field enhancement consistent with odd-frequency pairs | Intrinsic local paramagnetic response | APS/DOI and arXiv verified |
| Peotta & Törmä (2015) | Nature Communications; peer-reviewed primary theory | Multiband flat-band response | Quantum metric supplies finite superfluid weight | Foundation of geometric stiffness frontier | Publisher verified |
| Wilcox et al. (2022) | Nature Communications; peer-reviewed primary experiment | Field-dependent penetration depth | Observation of nonlinear Meissner response in nodal materials | Accepted anomalous response | Publisher/PubMed verified |
| Watanabe, Daido & Yanase (2022) | PRB; peer-reviewed primary theory | Symmetry analysis and response calculation | Nonreciprocal penetration depth in parity-mixed states | Directional screening | APS and arXiv verified |
| Hou et al. (2023) | PRL; peer-reviewed primary experiment/theory | Thin-film critical currents and controls | Meissner current plus asymmetric vortex barriers produces large diode effect | Strong conventional confound | APS/PubMed verified |
| Minkov et al. (2023) | Nature Physics; peer-reviewed primary experiment | Trapped-flux protocol in H₃S and LaH₁₀ | High-pressure remanent flux and inferred parameters | Hydride evidence and controversy | Publisher and arXiv verified |
| Fava et al. (2024) | Nature; peer-reviewed primary experiment | Ultrafast magneto-optic field sensing | Picosecond exterior-field transient after MIR drive | Contested photoinduced Meissner evidence | Publisher verified |
| Bhattacharyya et al. (2024) | Nature; peer-reviewed primary experiment | NV magnetometry plus transport in CeH₉ | Local diamagnetism and flux trapping at megabar pressure | Direct high-pressure Meissner imaging | Publisher verified |
| Røising, Kreisel & Andersen (2024) | PRB; peer-reviewed primary theory | Nonlocal multiband penetration-depth calculation | Nonlocality changes low-\(T\) power laws in Sr₂RuO₄ | Modern Pippard frontier | APS/institutional record and arXiv verified |
| Davydova, Geier & Fu (2024) | Science Advances; peer-reviewed primary theory | Nonreciprocal quasiparticle and Andreev response | General framework for nonreciprocal superconductivity | Separates intrinsic nonreciprocity from diode artifacts | Publisher/PubMed Central verified |
| Hu & Huang (2025) | PRB; peer-reviewed primary theory | Microscopic multiband response | Interband pair transfer and virtual processes generate geometric stiffness | Microscopic gain mechanism | APS and arXiv verified |
| Dailledouze et al. (2025) | Physical Review Applied; peer-reviewed primary experiment | Wide-field NV imaging of Hg-1223 at 4 GPa | Spatial \(T_c\), diamagnetism, and pinning maps | Local heterogeneity diagnostics | APS and arXiv verified |
| Porlles & Chen (2025) | PRB; peer-reviewed primary theory | Quantum-metric response and real-space marker | Geometric Meissner weight and disorder-resolved marker | Current quantum-geometry frontier | APS and arXiv verified |
| Ross et al. (2025) | PRD; peer-reviewed primary experiment | Cryogenic torsion balance, Nb–Cu composition dipole | \(|\eta_{\mathrm{Nb^\ast-Cu}}|\le2.0\times10^{-9}\) | Direct gravity constraint on a superconductor | APS/NSF/INSPIRE verified |
| Hirsch (2025, 2026) | Physica C and J. Phys. Condens. Matter; peer-reviewed argument/review | Conservation analysis and proposed geometry tests | Claims radial charge flow is required | Minority transition-dynamics challenge | Publisher/PubMed and arXiv verified |
| Keren et al. (2026) | Nature; peer-reviewed primary experiment/theory | MFM, nano-optics, molecular dynamics | Resonant hBN interface suppresses equilibrium superfluid density | Closest demonstrated phase/environment gate | Publisher and arXiv verified |
| Bhattacharya & Black-Schaffer (2026) | PRB; peer-reviewed primary theory | General two-band analysis and models | Quantum-geometric odd-frequency response can be diamagnetic | Revises old sign rule | APS and arXiv verified |
| Nikulov (2026) | Physica C; peer-reviewed response | Macroscopic quantum/quantization argument | Disputes necessity of radial charge flow | Counterpoint in dynamics debate | Publisher/INSPIRE and arXiv verified |
| Mandyam et al. (2026) | Nature; peer-reviewed primary experiment | NV field/stress maps, EDX, transport | Micron-scale superconductivity tracks stress and stoichiometry in La₃Ni₂O₇ | Multimodal frontier | Publisher verified |
| Zhang et al. (2026) | arXiv:2603.25807; **preprint** | Nano-SQUID imaging of rhombohedral graphene | Direct \(100\)-ppm screening, vortex entry, local stiffness | 2D imaging frontier | Current arXiv record verified; not yet peer-reviewed |
| Michael et al. (2026) | Physical Review X; **accepted 15 July 2026**, issue publication pending | Driven bilayer sine-Gordon/Floquet theory | Alternative to photoinduced Meissner interpretation | Materially changes Fava assessment | Official APS accepted-paper record verified |

---

## 10. Primary bibliography

1. W. Meissner and R. Ochsenfeld, “Ein neuer Effekt bei Eintritt der Supraleitfähigkeit,” *Naturwissenschaften* **21**, 787–788 (1933). [DOI: 10.1007/BF01504252](https://doi.org/10.1007/BF01504252). Peer-reviewed primary experiment; DOI verified.
2. F. London and H. London, “The Electromagnetic Equations of the Supraconductor,” *Proceedings of the Royal Society A* **149**, 71–88 (1935). [DOI: 10.1098/rspa.1935.0048](https://doi.org/10.1098/rspa.1935.0048). Peer-reviewed primary theory; DOI verified.
3. V. L. Ginzburg and L. D. Landau, “On the Theory of Superconductivity,” *Zh. Eksp. Teor. Fiz.* **20**, 1064–1082 (1950). [CERN record](https://cds.cern.ch/record/486430). Peer-reviewed primary theory; archive verified; no DOI assigned.
4. A. B. Pippard, “An Experimental and Theoretical Study of the Relation between Magnetic Field and Current in a Superconductor,” *Proceedings of the Royal Society A* **216**, 547–568 (1953). [DOI: 10.1098/rspa.1953.0040](https://doi.org/10.1098/rspa.1953.0040). Peer-reviewed primary experiment/theory; DOI verified.
5. J. Bardeen, L. N. Cooper, and J. R. Schrieffer, “Theory of Superconductivity,” *Physical Review* **108**, 1175–1204 (1957). [DOI: 10.1103/PhysRev.108.1175](https://doi.org/10.1103/PhysRev.108.1175). Peer-reviewed primary theory; APS verified.
6. A. A. Abrikosov, “On the Magnetic Properties of Superconductors of the Second Group,” *Soviet Physics JETP* **5**, 1174–1182 (1957). [JETP archive](https://www.jetp.ras.ru/cgi-bin/e/index/e/5/6/p1174?a=list). Peer-reviewed primary theory; archive verified; no DOI assigned.
7. W. Braunisch et al., “Paramagnetic Meissner Effect in Bi High-Temperature Superconductors,” *Physical Review Letters* **68**, 1908–1911 (1992). [DOI: 10.1103/PhysRevLett.68.1908](https://doi.org/10.1103/PhysRevLett.68.1908). Peer-reviewed primary experiment; DOI verified.
8. S. K. Yip and J. A. Sauls, “Nonlinear Meissner Effect in CuO Superconductors,” *Physical Review Letters* **69**, 2264–2267 (1992). [DOI: 10.1103/PhysRevLett.69.2264](https://doi.org/10.1103/PhysRevLett.69.2264); [arXiv:cond-mat/9207021](https://arxiv.org/abs/cond-mat/9207021). Peer-reviewed primary theory.
9. A. E. Koshelev and A. I. Larkin, “Paramagnetic Moment in Field-Cooled Superconducting Plates: Paramagnetic Meissner Effect,” *Physical Review B* **52**, 13559–13562 (1995). [DOI: 10.1103/PhysRevB.52.13559](https://doi.org/10.1103/PhysRevB.52.13559). Peer-reviewed primary theory; DOI verified.
10. A. K. Geim et al., “Paramagnetic Meissner Effect in Small Superconductors,” *Nature* **396**, 144–146 (1998). [DOI: 10.1038/24110](https://doi.org/10.1038/24110). Peer-reviewed primary experiment; publisher verified.
11. A. Di Bernardo et al., “Intrinsic Paramagnetic Meissner Effect Due to s-Wave Odd-Frequency Superconductivity,” *Physical Review X* **5**, 041021 (2015). [DOI: 10.1103/PhysRevX.5.041021](https://doi.org/10.1103/PhysRevX.5.041021); [arXiv:1605.02199](https://arxiv.org/abs/1605.02199). Peer-reviewed primary experiment.
12. S. Peotta and P. Törmä, “Superfluidity in Topologically Nontrivial Flat Bands,” *Nature Communications* **6**, 8944 (2015). [DOI: 10.1038/ncomms9944](https://doi.org/10.1038/ncomms9944); [arXiv:1506.02815](https://arxiv.org/abs/1506.02815). Peer-reviewed primary theory.
13. J. A. Wilcox et al., “Observation of the Non-linear Meissner Effect,” *Nature Communications* **13**, 1201 (2022). [DOI: 10.1038/s41467-022-28790-y](https://doi.org/10.1038/s41467-022-28790-y); [arXiv:2008.04050](https://arxiv.org/abs/2008.04050). Peer-reviewed primary experiment.
14. H. Watanabe, A. Daido, and Y. Yanase, “Nonreciprocal Meissner Response in Parity-Mixed Superconductors,” *Physical Review B* **105**, L100504 (2022). [DOI: 10.1103/PhysRevB.105.L100504](https://doi.org/10.1103/PhysRevB.105.L100504); [arXiv:2109.14874](https://arxiv.org/abs/2109.14874). Peer-reviewed primary theory.
15. Y. Hou et al., “Ubiquitous Superconducting Diode Effect in Superconductor Thin Films,” *Physical Review Letters* **131**, 027001 (2023). [DOI: 10.1103/PhysRevLett.131.027001](https://doi.org/10.1103/PhysRevLett.131.027001); [arXiv:2205.09276](https://arxiv.org/abs/2205.09276). Peer-reviewed primary experiment/theory.
16. V. S. Minkov et al., “Magnetic Flux Trapping in Hydrogen-Rich High-Temperature Superconductors,” *Nature Physics* **19**, 1293–1300 (2023). [DOI: 10.1038/s41567-023-02089-1](https://doi.org/10.1038/s41567-023-02089-1); [arXiv:2206.14108](https://arxiv.org/abs/2206.14108). Peer-reviewed primary experiment.
17. S. Fava et al., “Magnetic Field Expulsion in Optically Driven YBa₂Cu₃O₆.₄₈,” *Nature* **632**, 75–80 (2024). [DOI: 10.1038/s41586-024-07635-2](https://doi.org/10.1038/s41586-024-07635-2); [arXiv:2405.00848](https://arxiv.org/abs/2405.00848). Peer-reviewed primary experiment; interpretation contested.
18. P. Bhattacharyya et al., “Imaging the Meissner Effect in Hydride Superconductors Using Quantum Sensors,” *Nature* **627**, 73–79 (2024). [DOI: 10.1038/s41586-024-07026-7](https://doi.org/10.1038/s41586-024-07026-7). Peer-reviewed primary experiment.
19. H. S. Røising, A. Kreisel, and B. M. Andersen, “Nonlocal Electrodynamics and the Penetration Depth of Superconducting Sr₂RuO₄,” *Physical Review B* **110**, 094511 (2024). [DOI: 10.1103/PhysRevB.110.094511](https://doi.org/10.1103/PhysRevB.110.094511); [arXiv:2404.19365](https://arxiv.org/abs/2404.19365). Peer-reviewed primary theory.
20. M. Davydova, M. Geier, and L. Fu, “Nonreciprocal Superconductivity,” *Science Advances* **10**, eadr4817 (2024). [DOI: 10.1126/sciadv.adr4817](https://doi.org/10.1126/sciadv.adr4817); [arXiv:2407.01681](https://arxiv.org/abs/2407.01681). Peer-reviewed primary theory.
21. Y.-J. Hu and W. Huang, “Quantum Geometric Superfluid Weight in Multiband Superconductors: A Microscopic Interpretation,” *Physical Review B* **111**, 134511 (2025). [DOI: 10.1103/PhysRevB.111.134511](https://doi.org/10.1103/PhysRevB.111.134511); [arXiv:2409.12254](https://arxiv.org/abs/2409.12254). Peer-reviewed primary theory.
22. C. Dailledouze et al., “Imaging the Meissner Effect and Flux Trapping of Superconductors under High Pressure Using N-V Centers,” *Physical Review Applied* **23**, 064067 (2025). [DOI: 10.1103/PhysRevApplied.23.064067](https://doi.org/10.1103/PhysRevApplied.23.064067); [arXiv:2501.14504](https://arxiv.org/abs/2501.14504). Peer-reviewed primary experiment.
23. D. Porlles and W. Chen, “Quantum Geometric Origin of the Meissner Effect and Superfluid Weight Marker,” *Physical Review B* **112**, 054511 (2025). [DOI: 10.1103/9fsf-9j53](https://doi.org/10.1103/9fsf-9j53); [arXiv:2505.17349](https://arxiv.org/abs/2505.17349). Peer-reviewed primary theory.
24. M. P. Ross et al., “Test of the Equivalence Principle for Superconductors,” *Physical Review D* **111**, L021101 (2025). [DOI: 10.1103/PhysRevD.111.L021101](https://doi.org/10.1103/PhysRevD.111.L021101); [arXiv:2407.21232](https://arxiv.org/abs/2407.21232). Peer-reviewed primary experiment.
25. J. E. Hirsch, “Does the Meissner Effect Require Radial Charge Flow?” *Physica C* **633**, 1354724 (2025). [DOI: 10.1016/j.physc.2025.1354724](https://doi.org/10.1016/j.physc.2025.1354724). Peer-reviewed theoretical argument.
26. I. Keren et al., “Cavity-Altered Superconductivity,” *Nature* **650**, 864–868 (2026). [DOI: 10.1038/s41586-025-10062-6](https://doi.org/10.1038/s41586-025-10062-6); [arXiv:2505.17378](https://arxiv.org/abs/2505.17378). Peer-reviewed primary experiment/theory.
27. A. Bhattacharya and A. M. Black-Schaffer, “Diamagnetic Meissner Response of Odd-Frequency Superconducting Pairing from Quantum Geometry,” *Physical Review B* **113**, 094501 (2026). [DOI: 10.1103/c57s-skv9](https://doi.org/10.1103/c57s-skv9); [arXiv:2509.02243](https://arxiv.org/abs/2509.02243). Peer-reviewed primary theory.
28. A. V. Nikulov, “The Meissner Effect Does Not Require Radial Charge Flow,” *Physica C* **645**, 1354858 (2026). [DOI: 10.1016/j.physc.2026.1354858](https://doi.org/10.1016/j.physc.2026.1354858); [arXiv:2605.10945](https://arxiv.org/abs/2605.10945). Peer-reviewed theoretical response.
29. S. V. Mandyam et al., “Uncovering Origins of Heterogeneous Superconductivity in La₃Ni₂O₇,” *Nature* **651**, 54–60 (2026). [DOI: 10.1038/s41586-025-10095-x](https://doi.org/10.1038/s41586-025-10095-x). Peer-reviewed primary experiment.
30. R. Zhang et al., “Imaging the Meissner Effect and Local Superfluid Stiffness in a Graphene Superconductor,” [arXiv:2603.25807](https://arxiv.org/abs/2603.25807) (2026). Preprint; not yet peer-reviewed as of 17 July 2026.
31. M. H. Michael, D. De Santis, E. A. Demler, and P. A. Lee, “Flux-Floquet Instability in Fluctuating Superconductors,” *Physical Review X*, accepted 15 July 2026. [DOI: 10.1103/tq9r-g727](https://doi.org/10.1103/tq9r-g727). Accepted peer-reviewed primary theory; issue assignment pending.
32. E. Podkletnov and R. Nieminen, “A Possibility of Gravitational Force Shielding by Bulk YBa₂Cu₃O₇−x Superconductor,” *Physica C* **203**, 441–444 (1992). [DOI: 10.1016/0921-4534(92)90055-H](https://doi.org/10.1016/0921-4534(92)90055-H). Peer-reviewed anomalous claim; unreplicated.
33. M. Tajmar, F. Plesescu, and B. Seifert, “Measuring the Dependence of Weight on Temperature in the Low-Temperature Regime Using a Magnetic Suspension Balance,” *Measurement Science and Technology* **21**, 015111 (2010). [DOI: 10.1088/0957-0233/21/1/015111](https://doi.org/10.1088/0957-0233/21/1/015111). Peer-reviewed primary null experiment.

---

## Bottom line

The Meissner effect supports the user’s central intuition in one important respect: **field exclusion can produce levitation through an external-field interaction without propellant exhaust, because the source body and field carry the reaction**.

It also imposes a stricter standard on any gravity extension. A real Meissner analogue is not defined by a low-field interior alone. It requires a phase stiffness, an induced boundary current or stress, a penetration law, an exterior field redistribution, a finite energy budget, a reaction on the source, and measured instability thresholds. No superconducting gravity proposal currently supplies that complete structure at useful strength.
