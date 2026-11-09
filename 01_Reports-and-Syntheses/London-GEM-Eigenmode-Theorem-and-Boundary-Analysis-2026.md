# London–GEM Eigenmode Theorem and Finite-Boundary Analysis

**Date:** 2026-07-17  
**Status:** **COHERENT AFTER REFRAMING** — the minimally coupled London–GEM equations are coherent as a weak-field response model, but they screen only one mixed field combination. Their second eigenmode is harmonic. Generic simultaneous expulsion of independent magnetic and gravitomagnetic boundary fields does not follow.  
**Decision:** close ordinary single-condensate London gravitomagnetism as a gravity-control gain mechanism; retain the theorem as a reusable boundary-condition test for multicomponent and genuinely new gravitational media.

## Executive result

The coupled equations used by Li and Torr and, in a different normalization, by Inan have an exact structural property that settles the apparent disagreement over “residual fields.” The electromagnetic and gravitomagnetic equations are driven by the same Cooper-pair current. Their two-by-two response matrix therefore has rank one:

\[
\det M=0.
\]

Consequently there are exactly two stationary eigenmodes:

1. one London-screened combination with inverse length \(\kappa\simeq\lambda_L^{-1}\);
2. one zero-eigenvalue combination satisfying Laplace's equation.

For the Inan conventions, the unscreened combination is

\[
\boxed{\ \mathbf C\equiv\mathbf B_G-r\mathbf B,\qquad
\nabla^2\mathbf C=0\ },
\]

where

\[
r=\frac{\mu_Gm_e}{\mu_0e}=4.22224\times10^{-32}\ {\rm C\,kg^{-1}}.
\]

In a half-space, both fields decay to zero only if their surface values are already locked to

\[
\boxed{\ \mathbf B_{G0}=r\mathbf B_0\ }.
\]

For an Earth-frame-dragging scale \(B_G\sim3.35\times10^{-14}\ {\rm s^{-1}}\), that condition requires

\[
B_0\sim7.9\times10^{17}\ {\rm T}.
\]

This is not the much smaller magnetic field at which the algebraic London-current combination changes sign. The two conditions differ by about \(10^{42}\). The first is the condition that removes the harmonic boundary mode; the second merely reverses a current term.

The result is stronger than a planar counterexample. In any finite source-free region governed by the same local, isotropic, single-current equations, \(\mathbf C\) is fixed by its boundary data and topology. Geometry can reshape this harmonic mode but cannot give it a London penetration length. A single charged condensate can gap at most one independent field combination.

This still does not address terrestrial weight. The paper's \(\mathbf B_G\) is a coordinate-dependent gravitomagnetic quantity; its published treatment explicitly finds no Meissner effect for the stationary gravitoelectric/Newtonian field. Even a successful invariant frame-dragging attenuation would therefore not levitate a stationary craft in Earth's field.

## Target

Determine whether conventional superconducting phase stiffness, coupled to linearized gravitoelectromagnetism through the ordinary Cooper-pair charge and mass current, produces a genuine finite-geometry gravitational Meissner effect capable of suppressing an independently imposed gravitomagnetic field.

The target observable must ultimately be invariant: a change in gyroscope precession, matter-wave phase, or the magnetic Weyl tensor relative to a specified observer congruence. The harmonic-coordinate field \(\mathbf B_G\) is used here only to audit the internal claim of the London–GEM model.

## Assumptions

1. Weak, stationary gravity from nonrelativistic sources; linearized GR in the harmonic-coordinate GEM convention used by Inan.
2. A homogeneous, isotropic, simply connected London superconductor away from surfaces and vortices.
3. One independent mobile carrier current. Charge and mass currents are proportional:

   \[
   \mathbf J_m=\frac{m_e}{e}\mathbf J_e
   \]

   in the single-electron normalization used by the paper. Cooper-pair normalization changes both numerator and denominator together and leaves the ratio unchanged.
4. Constant \(n_s\), \(\alpha\), and \(\beta\) within each homogeneous region.
5. No anomalous gravitational permeability, hidden susceptibility, extra mass current, or new field equation is inserted.
6. The equations are treated as a stationary boundary-value model, not as a complete covariant matter-plus-gravity action.

## Notation and conventions

| Symbol | Definition | Units |
|---|---|---:|
| \(\mathbf B\) | electromagnetic magnetic field | T |
| \(\mathbf B_G\) | Inan harmonic-coordinate gravitomagnetic field | s\(^{-1}\) |
| \(\mu_0\) | vacuum magnetic permeability | kg m C\(^{-2}\) |
| \(\mu_G=4\pi G/c^2\) | GEM coupling in the adopted convention | m kg\(^{-1}\) |
| \(\Lambda_L=n_se^2/m_e\) | London stiffness in Inan's normalization | SI |
| \(\alpha\) | \(1+\phi_G/c^2\) to the stated order | dimensionless |
| \(\beta\) | approximately \(4m_e/e\) when the EM scalar potential is negligible | kg C\(^{-1}\) |
| \(r\) | fixed gravitomagnetic-to-magnetic field ratio produced by the same current | C kg\(^{-1}\) |
| \(\kappa^{-1}\) | penetration length of the one screened eigenmode | m |

Factors of two or four in GEM definitions vary across the literature. They move the numerical values by order-unity factors and do not change the rank, zero mode, or the roughly \(10^{18}\)-tesla boundary requirement.

## Derivation strategy

1. Preserve the two coupled second-order equations rather than replacing them separately by fourth-order equations.
2. Write their response matrix and diagonalize it before imposing asymptotic boundary conditions.
3. Identify the screened and harmonic combinations.
4. Solve half-space and finite-slab boundary problems without assuming that every field vanishes at infinite depth.
5. Generalize the result to finite geometry by elliptic uniqueness.
6. Translate the algebra into source strength, invariant-observable, and craft-relevance tests.

## Main derivation

### 1. Coupled London–GEM equations

Inan's stationary equations can be written

\[
\nabla^2\mathbf B
=\mu_0\Lambda_L(\alpha\mathbf B-\beta\mathbf B_G),
\]

\[
\nabla^2\mathbf B_G
=\mu_Gn_se(\alpha\mathbf B-\beta\mathbf B_G).
\]

Define

\[
a=\mu_0\Lambda_L\alpha,\quad
b=\mu_0\Lambda_L\beta,\quad
c=\mu_Gn_se\alpha,\quad
d=\mu_Gn_se\beta.
\]

Then

\[
\nabla^2
\begin{pmatrix}\mathbf B\\ \mathbf B_G\end{pmatrix}
=
M
\begin{pmatrix}\mathbf B\\ \mathbf B_G\end{pmatrix},
\qquad
M=
\begin{pmatrix}
a&-b\\ c&-d
\end{pmatrix}.
\]

Both rows are proportional because both fields are sourced by the same current combination. Explicitly,

\[
\frac ca=\frac db
=\frac{\mu_Gn_se}{\mu_0\Lambda_L}
=\frac{\mu_Gm_e}{\mu_0e}
\equiv r.
\]

Therefore

\[
\det M=-ad+bc=0.
\]

The eigenvalues are

\[
\lambda_0=0,
\qquad
\lambda_s=a-d\equiv\kappa^2.
\]

For an ordinary superconductor, \(a\simeq\lambda_L^{-2}\) and \(d/a\) is negligible, so \(\kappa^2>0\) and \(\kappa^{-1}\simeq\lambda_L\).

### 2. Exact harmonic combination

Multiply the first equation by \(r\) and subtract it from the second:

\[
\nabla^2(\mathbf B_G-r\mathbf B)=0.
\]

Thus

\[
\boxed{\mathbf C=\mathbf B_G-r\mathbf B}
\]

is an unscreened harmonic field. The screened eigenvector satisfies \(\mathbf B_G=r\mathbf B\). The null/current-free eigenvector satisfies

\[
\alpha\mathbf B-\beta\mathbf B_G=0,
\qquad
\mathbf B_G=\frac{\alpha}{\beta}\mathbf B.
\]

These are different statements. The first gives the field ratio of the mode sourced by the common current; the second gives a field combination that drives no London current.

### 3. Half-space solution

Let a planar superconductor occupy \(z\ge0\), with bounded fields as \(z\rightarrow\infty\). Boundedness removes the linearly growing harmonic solution but not its constant value:

\[
\mathbf C(z)=\mathbf C_0
=\mathbf B_{G0}-r\mathbf B_0.
\]

The magnetic equation becomes

\[
\mathbf B''-\kappa^2\mathbf B=-b\mathbf C_0.
\]

Therefore

\[
\mathbf B(z)=\mathbf B_\infty
+(\mathbf B_0-\mathbf B_\infty)e^{-\kappa z},
\]

\[
\mathbf B_G(z)=\mathbf C_0+r\mathbf B(z),
\]

with

\[
\mathbf B_\infty=\frac b{\kappa^2}\mathbf C_0,
\qquad
\mathbf B_{G\infty}=\frac a{\kappa^2}\mathbf C_0.
\]

Because \(d/a\ll1\),

\[
\mathbf B_\infty\simeq
\frac\beta\alpha(\mathbf B_{G0}-r\mathbf B_0),
\]

\[
\mathbf B_{G\infty}\simeq
\mathbf B_{G0}-r\mathbf B_0.
\]

The necessary and sufficient condition for both asymptotic fields to vanish is

\[
\boxed{\mathbf C_0=0
\iff \mathbf B_{G0}=r\mathbf B_0.}
\]

Imposing \(\mathbf B\rightarrow0\) and \(\mathbf B_G\rightarrow0\) at the start is therefore not an innocent version of “bounded at depth.” It selects the special boundary subspace \(\mathbf C_0=0\) and discards the zero eigenmode whose existence the equations require for generic data.

### 4. Finite slab theorem

Let a slab occupy \(0\le z\le D\), with boundary values \((\mathbf B_L,\mathbf B_{GL})\) and \((\mathbf B_R,\mathbf B_{GR})\). Define

\[
\mathbf C_L=\mathbf B_{GL}-r\mathbf B_L,
\qquad
\mathbf C_R=\mathbf B_{GR}-r\mathbf B_R.
\]

The harmonic mode is

\[
\mathbf C(z)=\mathbf C_L+
\frac zD(\mathbf C_R-\mathbf C_L).
\]

Since \(\mathbf C''=0\), an exact solution is

\[
\begin{aligned}
\mathbf B(z)=&\frac b{\kappa^2}\mathbf C(z)\\
&+\left(\mathbf B_L-\frac b{\kappa^2}\mathbf C_L\right)
\frac{\sinh[\kappa(D-z)]}{\sinh(\kappa D)}\\
&+\left(\mathbf B_R-\frac b{\kappa^2}\mathbf C_R\right)
\frac{\sinh(\kappa z)}{\sinh(\kappa D)},
\end{aligned}
\]

\[
\mathbf B_G(z)=\mathbf C(z)+r\mathbf B(z).
\]

For \(D\gg\kappa^{-1}\), the exponential boundary layers become thin but the harmonic interpolation remains throughout the bulk. A thicker superconductor suppresses the massive eigenmode more completely; it does not suppress \(\mathbf C\).

### 5. Finite-geometry form

In any homogeneous source-free domain \(\Omega\),

\[
\nabla^2\mathbf C=0.
\]

Component-wise Dirichlet data, or the corresponding well-posed Maxwell/GEM boundary data with divergence constraints, determine \(\mathbf C\) by the elliptic boundary-value problem. In multiply connected domains additional harmonic vector fields may occur; topology adds zero-mode sectors rather than removing them.

**Single-carrier rank theorem.** If two gauge-like stationary fields couple to only one independent material current, and the material response depends on one linear combination of those fields, the local static response matrix has rank at most one. At most one independent field combination acquires a London mass. Gapping both combinations requires at least two independent current/order-parameter responses with linearly independent charge-to-mass coupling vectors, or genuinely modified gravitational dynamics.

This is why a neutral counterflow or multicomponent condensate is mathematically interesting: it can raise the response rank. It does not, by itself, strengthen the ordinary gravitational source coupling or shield the Newtonian metric.

## Quantitative boundary test

Using

\[
\mu_G=\frac{4\pi G}{c^2}
=9.33199\times10^{-27}\ {\rm m\,kg^{-1}},
\]

gives

\[
r=\frac{\mu_Gm_e}{\mu_0e}
=4.22224\times10^{-32}\ {\rm C\,kg^{-1}}.
\]

For Earth,

\[
J_E\simeq0.3307M_ER_E^2\Omega_E
=5.86\times10^{33}\ {\rm kg\,m^2\,s^{-1}},
\]

and a polar weak-field estimate is

\[
B_{G,E}\sim\frac{2GJ_E}{c^2R_E^3}
=3.35\times10^{-14}\ {\rm s^{-1}}.
\]

Eliminating the harmonic mode requires

\[
B_0=\frac{B_{G,E}}r
=7.94\times10^{17}\ {\rm T}.
\]

In contrast, the sign of the current-driving combination changes when

\[
\alpha B_0-\beta B_{G,E}=0,
\quad
\beta\simeq\frac{4m_e}{e}
=2.27425\times10^{-11}\ {\rm kg\,C^{-1}},
\]

so

\[
B_{\rm reverse}\simeq\beta B_{G,E}
=7.63\times10^{-25}\ {\rm T}.
\]

The ratio is

\[
\frac{B_0}{B_{\rm reverse}}=1.04\times10^{42}.
\]

Current reversal is therefore not field cancellation. It says which way the common current flows; it does not say that this extraordinarily weak mass current can generate the independent gravitomagnetic boundary field needed to remove \(\mathbf C\).

The calculation is reproducible with [gem_london_eigenmodes.py](../02_Gravitation-Theory/GEM-London-Eigenmode-Theorem/gem_london_eigenmodes.py).

## Relation to Li–Torr and the residual-field literature

Li and Torr's equations can be written in combinations equivalent to

\[
\mathbf B_1=\mathbf B+\frac mq\mathbf B_g,
\qquad
\nabla^2\mathbf B_1\simeq\lambda_L^{-2}\mathbf B_1,
\]

and

\[
\mathbf B_2=\mathbf B+
\frac{q\mu}{m\mu_g}\mathbf B_g,
\qquad
\nabla^2\mathbf B_2=0.
\]

Their constant residual fields are the same zero mode in different conventions. Kowitt and Harris correctly objected to treating a phenomenological gravitational permeability as a freely amplifying material coefficient. Inan improved several sign and coordinate issues and explicitly recognized that some prior solutions contained residual constants, but then rejected them by imposing the stronger condition that both fields vanish at infinite depth. The matrix proof shows that the residual is not created by a poor surface-current convention. It is the generic solution of the rank-one field equations.

## Invariant-observable audit

The linearized potentials and \(\mathbf B_G\) used in harmonic-coordinate GEM are gauge dependent. The model becomes an empirical gravitational claim only after it predicts a change in an invariant or operational quantity, such as

\[
H_{\mu\nu}={}^{\star}C_{\mu\alpha\nu\beta}u^\alpha u^\beta,
\]

the magnetic part of the Weyl tensor relative to observer four-velocity \(u^\mu\), or a closed-loop gyroscope/matter-wave observable with the apparatus worldlines specified.

Nothing in the rank-one London equations demonstrates attenuation of \(H_{\mu\nu}\). The result established here is narrower: even the coordinate-dependent model used to claim expulsion retains a generic zero mode.

## Craft relevance

### Terrestrial hovering

Stationary weight is controlled primarily by the gravitoelectric/lapse sector, not by Earth's tiny frame-dragging field. Inan's expanded peer-reviewed paper explicitly concludes that the time-independent gravitoelectric/Newtonian field is not expelled. Therefore:

- the model does not cancel \(g\);
- it does not create a protected low-tide cavity;
- it does not support hull, occupants, and payload;
- it does not specify an exterior stress that transfers \(Mg\) to Earth.

### Deep space

Even ideal gravitomagnetic attenuation would only reshape an applied rotational field. A closed static device has no independent momentum reservoir. Translation would still require an external source, radiation, or another field carrying momentum.

## Strongest rejection case

The rejection does not depend on the general weakness of gravity alone. It is the conjunction of four exact or direct failures:

1. **Rank failure:** one carrier current produces a rank-one response and leaves a harmonic mode.
2. **Boundary failure:** generic independent applied \(\mathbf B\) and \(\mathbf B_G\) do not satisfy \(\mathbf B_G=r\mathbf B\).
3. **Magnitude failure:** satisfying that relation for Earth's frame dragging requires roughly \(10^{18}\) T.
4. **Sector failure:** the model does not screen stationary gravitoelectric gravity, which is the sector required for levitation.

Ordinary single-condensate London–GEM coupling should therefore be closed as a gravity-control or propulsion mechanism.

## Strongest continuation case

The useful surviving result is a design rule:

> A Meissner-like gravitational medium needs enough independent, covariantly derived material responses to gap every physical gravitational mode relevant to the target boundary-value problem, while retaining the Hamiltonian constraints and a well-defined exterior stress.

A multicomponent charged/neutral counterflow could test the response-rank part of this rule. A phase-localized metric-Higgs model tests the more important possibility that a physical metric mode acquires an in-medium gap. Both must be evaluated against the gravitoelectric worldtube requirement, not against \(\mathbf B_G\) alone.

## Decision and next milestone

**No-go for conventional London–GEM gain.** Do not spend the next experimental cycle looking for Earth-weight shielding or large gravitomagnetic expulsion from an ordinary superconductor on the basis of these equations.

**Proceed to the requirements-first worldtube inverse design.** The next calculation must specify the physical lapse/shift/curvature profile for a \(10\) m, \(1g\), low-tide cavity, derive its complete effective stress tensor and boundary conditions, and then ask whether a phase-localized covariant metric response can supply that tensor without an unscreened constraint mode. The present zero-mode theorem is the boundary-condition template for that Gate 0.

## Boundaries and non-claims

- This report does not claim that superconductors modify spacetime curvature.
- It does not claim that residual coordinate \(\mathbf B_G\) is itself observable.
- It does not exclude every multicomponent medium or new gravitational field.
- It does not generalize the London rank theorem to a theory with additional independent currents or modified gravitational equations.
- It does not use Podkletnov-type claims as evidence.
- It does not infer a thrust limit directly from the Tajmar–Neunzig–Kößling null; that experiment constrains anomalous force per current in its own geometry.

## Primary references and verification status

1. B. S. DeWitt, “Superconductors and Gravitational Drag,” *Physical Review Letters* **16**, 1092–1093 (1966), DOI [10.1103/PhysRevLett.16.1092](https://doi.org/10.1103/PhysRevLett.16.1092). **Peer reviewed; publisher identity verified.**
2. N. Li and D. G. Torr, “Effects of a Gravitomagnetic Field on Pure Superconductors,” *Physical Review D* **43**, 457–459 (1991), DOI [10.1103/PhysRevD.43.457](https://doi.org/10.1103/PhysRevD.43.457). **Peer reviewed; local primary PDF and DOI identity verified.**
3. N. Li and D. G. Torr, “Gravitational Effects on the Magnetic Attenuation of Superconductors,” *Physical Review B* **46**, 5489–5495 (1992), DOI [10.1103/PhysRevB.46.5489](https://doi.org/10.1103/PhysRevB.46.5489). **Peer reviewed; local primary PDF and DOI identity verified.**
4. D. G. Torr and N. Li, “Gravitoelectric-Electric Coupling via Superconductivity,” *Foundations of Physics Letters* **6**, 371–383 (1993), DOI [10.1007/BF00665654](https://doi.org/10.1007/BF00665654). **Peer reviewed; local primary PDF and DOI identity verified.**
5. M. Kowitt, “Gravitational Meissner Effect,” *Physical Review B* **49**, 704–705 (1994), DOI [10.1103/PhysRevB.49.704](https://doi.org/10.1103/PhysRevB.49.704). **Peer reviewed; bibliographic identity verified.**
6. E. G. Harris, “Comments on ‘Gravitational Effects on the Magnetic Attenuation of Superconductors,’” *Foundations of Physics Letters* **12**, 201–208 (1999), DOI [10.1023/A:1021621425670](https://doi.org/10.1023/A:1021621425670). **Peer reviewed; bibliographic identity verified.**
7. N. A. Inan, “Superconductor Meissner Effects for Gravito-Electromagnetic Fields in Harmonic Coordinates Due to Non-Relativistic Gravitational Sources,” *Frontiers in Physics* **10**, 823592 (2022), DOI [10.3389/fphy.2022.823592](https://doi.org/10.3389/fphy.2022.823592), arXiv:[2201.12969](https://arxiv.org/abs/2201.12969). **Peer reviewed; local arXiv v1 read in full; published version and equations checked.**
8. M. Tajmar, O. Neunzig, and M. Kößling, “Measurement of Anomalous Forces From a Cooper-Pair Current in High-\(T_c\) Superconductors With Nano-Newton Precision,” *Frontiers in Physics* **10**, 892215 (2022), DOI [10.3389/fphy.2022.892215](https://doi.org/10.3389/fphy.2022.892215). **Peer-reviewed null result; reports no force within approximately 100 nN for currents to 15 A in the tested apparatus.**

