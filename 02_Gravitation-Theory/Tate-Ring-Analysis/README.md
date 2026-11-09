# Tate finite-ring analysis

The [report](../../01_Reports-and-Syntheses/Tate-Finite-Ring-and-Measurement-Audit-2026.md) derives winding-sector spacing from the existing stiffness kernel and a finite pickup operator. It separates a published experimental summary from synthetic sensitivity examples.

Run from the repository root:

```powershell
& 'C:/Python314/python.exe' '02_Gravitation-Theory/Tate-Ring-Analysis/tate_ring_analysis.py'
```

Dependencies: Python, NumPy and SciPy. No global installation or dependency modification is required in the current environment.

- `tate_ring_analysis.py`: derivation checks, finite thin-film annulus calculation, GLS and identifiability checks.
- `verification_results.json`: machine-readable checks and results; all hypothetical numerical geometry/uncertainty examples are labeled synthetic.
- `synthetic_annulus_sensitivity.csv`: mesh/penetration sensitivity, **not Tate data**.
- `sources/SOURCE-AND-INPUT-MANIFEST-2026-09-04.md`: retrieved primary evidence, page references, access limits, and required missing inputs.

No raw Tate observations, empirical re-fit, or microscopic niobium neutral-phase model is present. The finite-width operator is a thin-strip quadrature with mesh refinement; its residual mesh changes do not bound full physical model uncertainty.
