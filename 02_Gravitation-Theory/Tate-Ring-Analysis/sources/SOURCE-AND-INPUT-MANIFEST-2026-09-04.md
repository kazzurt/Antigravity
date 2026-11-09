# Tate ring: primary-source and input manifest

**Checked:** 2026-09-04 local project date. **Scope:** source retrieval and verified inputs; no new fit, digitization, or replication.

## Outcome

The original 1989 and 1990 journal identities and published mass ratio are verified. The 1990 full paper, full Tate thesis, raw measurements, and calibration covariance were not obtained. A publicly indexed 1989 scan could not be downloaded because its host repeatedly timed out. Available primary material supports the observable and apparatus class, but not a numerical reconstruction of the complete Tate ring/readout system.

Three public PDFs were downloaded: Liu's 1998 theory, Jiang-Liu's 2001 theory, and Stanford's institutional collection of thesis abstracts. The relevant pages were rendered and visually checked. Extracted `.txt` files carry explicit PDF page markers. `download_manifest.json` records URLs, sizes, SHA-256 hashes, and retrieval status. Metadata snapshots are identified separately below.

## Source availability

| ID | Primary source | Local evidence and access status |
|---|---|---|
| T89 | J. Tate, B. Cabrera, S. B. Felch, J. T. Anderson, *Precise Determination of the Cooper-Pair Mass*, PRL **62**, 845-848 (1989), [DOI](https://doi.org/10.1103/PhysRevLett.62.845) | APS abstract accessible; publisher full text requires authorization. Search-indexed first-page text from an archival mirror corroborates identity and result, but the PDF was **not obtained or visually checked**. |
| T90 | J. Tate, S. B. Felch, B. Cabrera, *Determination of the Cooper-pair mass in niobium*, PRB **42**, 7885-7893 (1990), [DOI](https://doi.org/10.1103/PhysRevB.42.7885) | [APS abstract](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.42.7885) accessible; full text requires authorization. `Tate-1990-openalex.json` records a closed-access status and no repository full text; this is an access-index result, not proof that no public copy exists. |
| TH | Janet Tate, thesis completed October 1987, *A precise determination of the mass of a Cooper pair of electrons in superconducting niobium* | `Stanford-HEPL-Thesis-Abstracts.pdf` and `.txt`; [institutional original](https://einstein.stanford.edu/content/sci_papers/abstracts.pdf). The title/date are on PDF p39 (printed p38), abstract on PDF p40 (printed p39). This is **an abstract collection, not the thesis**. |
| CAL | J. Tate, D. H. McIntyre, B. Cabrera, *Absolute measurement of the diameter of a fused quartz hemisphere at 6 K*, RSI **60**, 985-992 (1989), [DOI](https://doi.org/10.1063/1.1140291) | `Tate-McIntyre-Cabrera-1989-RSI-crossref.json` contains publisher-deposited abstract and bibliographic metadata. Full PDF not obtained. The [author's institutional publication list](https://sites.science.oregonstate.edu/~mcintyre/cv_dmc.html) independently confirms identity. |
| L98 | M. Liu, *Rotating Superconductors and the Frame-independent London Equation*, PRL **81**, 3223 (1998), [arXiv](https://arxiv.org/abs/cond-mat/9806300) | `Liu-1998-arxiv.pdf` and `.txt`, 4 pages. Relevant PDF p2 visually checked. |
| JL01 | Y. Jiang and M. Liu, *Rotating Superconductors and the London Moment: Thermodynamics versus Microscopics*, PRB **63**, 184506 (2001), [arXiv](https://arxiv.org/abs/cond-mat/0010260) | `Jiang-Liu-2001-arxiv.pdf` and `.txt`, 8 pages. PDF pp6-8 visually checked, including equation labels, signs, and unit conventions. |
| H20 | L. P. Hoang et al., *High-precision measurement of Cooper-pair mass using rotating spherical-shell superconductor*, Materials Letters **262**, 127176 (2020), [DOI](https://doi.org/10.1016/j.matlet.2019.127176) | Publisher/search preview found; full article, supplement, material results table, and raw data not obtained. No Hoang numerical result is admitted as a measurement input here. |
| HC20 | Hoang et al., corrigendum, Materials Letters **281**, 128597 (2020), [publisher text](https://www.sciencedirect.com/science/article/abs/pii/S0167577X20313045), DOI `10.1016/j.matlet.2020.128597` | Public publisher text checked; `Hoang-2020-corrigendum-crossref.json` saves bibliographic metadata. It changes the first author's affiliation only. It neither supplies calibration data nor corrects the reported mass values. |

The failed T89 mirror URL is preserved in `download_manifest.json` and `retrieve_sources.py`. No authenticated session, paywall circumvention, or author contact was used.

## Verified experimental inputs

| Input | Value or description | Evidence | Use boundary |
|---|---|---|---|
| Published normalized observable mass | `m_app/(2 m_e) = 1.000084(21)` | T90 APS abstract; T89 indexed p845 text | Published summary, not individual observations. |
| Published theory comparator | `0.999992` | T89 APS abstract | Preserve separately from the bare `1.000000` comparison. |
| Later reported precision/accuracy | `5 ppm` precision, `21 ppm` accuracy | T89 APS abstract | Full decomposition and covariance unavailable. |
| Measured observables | Enclosed ring area and spacing of successive zero-flux rotation frequencies | T89/T90 abstracts | The readout's exact subtraction and zero estimator remain unverified. |
| Historical apparatus class | Thin-film Nb equatorial ring on precision quartz hemispherical rotor | TH PDF p40, printed p39 | Does not establish film dimensions. |
| Temperature and bearing | `6 K`; precision helium gas bearing | TH same page | Historical thesis description. |
| Magnetic readout | SQUID monitors ring flux versus rotation rate | TH same page | Pickup geometry and mutual inductances unavailable. |
| Area metrology | Two perpendicular equatorial diameters at 6 K; room-temperature roundness | TH same page | No actual diameter readings or covariance supplied. |
| Optical frequency reference | Tunable dye laser; Doppler-free molecular tellurium and iodine lines | TH same page | Actual line list and fitted frequencies unavailable. |
| Diameter method accuracy | `200 nm`, stated as `4 ppm`, at room and liquid-helium temperature | CAL publisher-deposited abstract | A metrology performance statement, **not** a measured rotor diameter. |
| Historical thesis uncertainty | `84 +/- 30 ppm`; statistical `5 ppm`, systematic `30 ppm` | TH same page | Earlier thesis result; do not replace the later journal `21 ppm` uncertainty. |

No numerical radius, film width, film thickness, penetration depth, pickup-loop area, rotor charge, rotation spacing, or temperature dependence is admitted as a measured Tate input. The approximately 50 mm diameter one could infer from `200 nm / 4 ppm` is only a rounded-scale inference and is not used as data.

## Frequency convention: exact normalization

Define angular speed `Omega` in rad/s and cyclic frequency `nu = Omega/(2 pi)` in Hz. For the standard one-component circulation law with signed pair charge `q` and pair mass parameter `m`,

\[
\Phi+L_k I=n\frac{h}{q}-\frac{2m}{q}\Omega S.
\]

At successive ideal current-null states with unchanged background,

\[
\Delta\Omega=\frac{h}{2mS},\qquad
\Delta\nu=\frac{h}{4\pi mS},\qquad
\frac{h}{2\pi m}=2S\Delta\nu.
\]

This is an explicit normalization derivation, not a new extraction from Tate observations. The T90 APS abstract's `h/(2 pi m') = 2 S Delta nu` is consistent with frequency in Hz. A search-indexed scan can lose the bar on `hbar`; do not treat its plain-text `h/m` form as an alternative experimental normalization. Raw pickup-flux zero and background-subtracted circulating-current zero cannot be identified from the available abstracts alone.

## Theory equations checked against PDF pages

### Liu 1998

PDF p2, Eqs (3)-(6), uses `gamma=e/(mc)` in the paper's convention and `gamma=e/m` in SI:

\[
\nabla\times\nabla\times\mathbf H_0
=-\rho_s\gamma(\gamma\mathbf B/\eta+2\boldsymbol\Omega),
\quad\eta=1+\mu_{\rm chem}/c^2,
\]

\[
\nabla\times\mathbf H_0=\gamma\mathbf j_s,
\quad\mathbf j_s=\rho_s(\mathbf v_s/\eta-\mathbf v_n).
\]

The bulk limit is `B=-2 eta Omega/gamma`. The chemical potential here is neutral-atom addition energy per total mass; its estimated fractional correction is of order `10^-10`. This supplies the bulk baseline, not a complete finite-ring pickup model.

### Jiang-Liu 2001

**Unit warning:** PDF p8, footnote 2, specifies rationalized Heaviside-Lorentz units. Convert fields, charges, and currents consistently before using these equations in SI.

PDF p6, Eqs (56)-(58):

\[
\Delta\mathbf A=\mathbf A^{out}-\mathbf A^{int}
=-\frac{\Delta\Phi}{c}\mathbf v,
\quad \oint\Delta\mathbf A\cdot d\mathbf s
=-\frac{2\pi R^2\Delta\Phi\Omega}{c},
\]

\[
m_{obs}=(1+\zeta)(1-\alpha)m_e.
\]

PDF p7, Eq (75), gives `alpha=-e DeltaPhi/(m_e* c^2)`. The work-function scale discussed on p6 is about `-4 eV`; the external-flux correction remains approximately `-8 ppm` even when the bulk correction is approximately `-10^-10`.

PDF pp6-7, Eqs (60)-(73), provide cylindrical Bessel solutions and boundary matching:

\[
B=2\gamma^*\Omega+C_1I_0(r/\lambda)+C_2K_0(r/\lambda),
\]

\[
A=\gamma^*\Omega r-n\phi_0/r
+\lambda[C_1I_1(r/\lambda)-C_2K_1(r/\lambda)].
\]

Here `gamma*=-m_e* c/e`, and their `phi0=-hbar c/(2e)` is the coefficient of the `1/r` potential term. Its contour integral introduces `2 pi`; it must not be confused with the full SI flux quantum. Eq (74) retains both winding integers and surface-dependent rotation response. The illustrative two-cylinder geometry on p7 is a **proposal**, not Tate's apparatus. The p8 conclusion explicitly leaves the experimental discrepancy unresolved.

## Missing data and permitted next analysis

The following remain missing:

- Original frequency/flux sweeps, winding-state assignments, zero estimators, acquisition times, temperature and spin histories.
- Complete film profile and coverage, actual diameter/roundness observations, thermal geometry mapping, and their covariance.
- Pickup coupling, magnetic shield and background terms, residual-flux history, charge-related corrections, rotor-position histories, and any fitted nuisance parameters.
- Published T90 systematic table and its links to individual observations; no full error budget is reconstructed from secondary slides.
- Unrounded experimental `h/m_app`, reference constants, and covariance needed for a defensible conversion to a newer constants adjustment.
- Hoang's full results, supplement, calibration history, and independent reproduction.

A finite-ring theory, dimensional checks, analytic limiting cases, and parameter sensitivity calculations can proceed with explicitly hypothetical geometry. They must not be labeled a re-fit of Tate or a numerical explanation of the `92 ppm` residual. At present the data identify a published scalar summary, not the separate surface, geometry, charge, penetration, or extra-component contributions.

## Local knowledgebase correction

At retrieval time, `01_Reports-and-Syntheses/Tate-London-Moment-Permeability-and-Collective-Modes-2026.md`, line 109, stated that no Hoang correction existed as of July 2026. HC20 disproves that absolute bibliographic claim. Its affiliation-only scope leaves the experimental-evidence assessment unchanged. This finding was sent to the coordinating agent; this source-retrieval work does not edit the report.

## Verification notes

- Rendered and inspected TH PDF p40, L98 PDF p2, JL01 PDF pp6-8. Poppler printed missing-font notices for TH/L98; the relevant rendered text and formulas were legible.
- All downloaded PDF page counts and SHA-256 hashes are recorded. No failed HTML response was stored under a `.pdf` extension.
- Access snapshots describe this retrieval session, not a universal claim about all libraries or future availability.
