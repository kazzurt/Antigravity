# Alzofon Theory Audit — calculation package

Checks for [Alzofon's Theory of Gravity — Derivation Audit](../../01_Reports-and-Syntheses/Alzofon-Theory-Derivation-Audit-2026.md) (2026-11-09).

- `alzofon_theory_audit_checks.py` — standard library only; asserts every number quoted in the report.
- `results.json` — generated output.

```bash
python alzofon_theory_audit_checks.py
```

What it checks:

1. The mass-shell relation in Alzofon's 2010 formalism is an identity for any motion, the hidden displacement is always space-like, and his eqs. (3) and (5) differ by a cross term that vanishes only on average.
2. `G m_p²/ħc`, the Compton lengths, and the free-fall difference a nucleon-count source would produce.
3. ²⁷Al polarization and spin energy at 0.33 T and 300 K, the fractional weight change if that energy came from the sample–Earth gravitational energy, the Korringa `T₁`, and the standard mass-energy change from spin ordering. Cross-checked against Stark, Grafe, Tajmar Table 6.
4. What a relaxation-rate law calibrated on the 1994 claim predicts for Falcon Space's slow field sweep.
5. Order-of-magnitude conventional forces on the Falcon sample. Entries marked `ASSUMED` use cavity `Q`, delivered power, cavity height, and sample density that are not known from the poster.

No apparatus data are used beyond the published poster and the cited papers. Third-party PDFs are not stored here.
