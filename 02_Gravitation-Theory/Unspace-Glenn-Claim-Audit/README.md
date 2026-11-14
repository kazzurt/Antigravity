# Unspace and Glenn assessments - calculations and revision record

Current edition: **13 November 2026, revised and checked with GPT-6 Astra Extra High following independent review**. At Kurt's request, the two previous assessment PDFs were overwritten in place; no backup PDF editions were created. The original research papers and raw published measurements remain unchanged.

## Current reports and editable sources

| Report | Editable source / knowledgebase digest |
| --- | --- |
| [Unspace revised assessment, 6 pages](../../01_Reports-and-Syntheses/Unspace-Radial-Stress-Torsion-Balance-Technical-Assessment-2026-11-13.pdf) | [Unspace source text](../../00_Knowledgebase/sources/lentz2026-unspace-radial-stress-torsion-balance.md) |
| [Glenn revised assessment, 5 pages](../../01_Reports-and-Syntheses/Glenn-Spark-Gap-Interferometry-Technical-Assessment-2026-11-13.pdf) | [Glenn source text](../../00_Knowledgebase/sources/glenn2025-spark-gap-interferometry.md) |

The digests are now the authoring source for the PDFs, avoiding separate prose copies that can diverge. HTML page/figure comments control layout; inline subscript/superscript tags preserve equation typography.

## Reproduce

Verified environment: `C:/Python314/python.exe`, with numpy, matplotlib, reportlab, pypdf and the DejaVu fonts in `C:/Windows/Fonts`. The bundled Codex Python had numpy/reportlab/pypdf but lacked matplotlib; it was not modified.

From this directory:

```powershell
& C:/Python314/python.exe unspace_glenn_claim_checks.py
& C:/Python314/python.exe independent_review_checks_2026-11-13.py
& C:/Python314/python.exe build_assessment_pdfs.py
```

- `unspace_glenn_claim_checks.py` contains the published Table 3 transcription and original arithmetic checks; it writes `results.json`.
- `independent_review_checks_2026-11-13.py` reads that transcription without executing the original script and prints supplementary JSON. Checks include the corrected crossover, Appendix A energy mismatch/sign, flow-regime limits, clearance conversion, refitted coefficient, damping time and double-pass optical budget.
- `build_assessment_pdfs.py` reads the two digests, results and Table 3, runs the supplementary checks, draws the two figures, and overwrites the current PDF filenames. It verifies page counts and page-start headings. It does not create archive copies.

Numerical values in the authoring text are rounded from these checks or explicitly attributed to the papers. Editing source assumptions requires reconciling the prose with regenerated calculations. The older result keys containing `expected` or `strain` are legacy calculation labels, not assertions that a complete physical prediction was performed.

## Evidence boundaries

The reports distinguish measured values, numerical substitutions into published formulas, rough physical scales and untested artifact hypotheses. No calculation in this package is an FEA solver run. The rotational-energy comparison is not a full finite-source GR solution; the disk deformation estimate is not a solved sphere model; airflow/heating scales do not identify an artifact; the Glenn metric scale is not a detector-strain prediction.

Current Zenodo contents were not independently reverified because retrieval failed. The initial audit's account of a summary-only deposit is identified as historical, not promoted into a fresh verification.

## Revision milestone

The [independent review](Independent-Review-of-Opus-Assessments-2026-11-13.md) is a historical decision record whose assessment-page references refer to the replaced editions. Its findings are incorporated into the current PDFs and digests:

- Unspace: corrected crossover and abstract characterization; qualified artifact/statistical scales; added the wrong metric-component force conversion, kernel/unit discontinuity, energy/force-law problem, complex and detector-dependent metric, flyby conservation objection, readout controls, damping time and clearance/refit checks.
- Glenn: distinguished compatibility with refraction from identification; corrected near-zone, ringing, range and control overclaims; added double-pass calibration, source quadrupole/conservation, electrical energy measurement, image-analysis artifacts and Alcubierre velocity units.
- Retained E for gravitational attribution and Unspace's C for apparatus description. The actual conventional cause remains unresolved in both cases.

Validation: both calculation scripts ran; the PDF builder's 6/5-page and page-heading checks passed; all 11 pages were rendered with Poppler and visually inspected for readable text, equations, charts, tables, references and pagination. No original assessment PDF copies remain in the project. Source papers remain in `03_Propulsion-and-Anomalies/`.

Next step only if further evidence arrives: inspect the complete Unspace time series/workbook, compare the preprint with the published version, or evaluate new calibrated control data. No experimental claim was validated by this revision.
