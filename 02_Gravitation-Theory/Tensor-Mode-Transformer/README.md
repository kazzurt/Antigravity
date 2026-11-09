# Static Tensor-Mode Transformer Calculation

Companion to [the Gate 0 derivation](../../01_Reports-and-Syntheses/Tensor-Mode-Transformer-Gate-0-2026.md).

This is a **conditional static plane-symmetric Fierz–Pauli source calculation** derived from the relative mode of singly coupled bimetric gravity. The positive mass profile is prescribed. It is not a material model, a full nonlinear shell solution, or a tensor-wave calculation.

Run from the project root:

```powershell
& 'C:/Python314/python.exe' '02_Gravitation-Theory/Tensor-Mode-Transformer/tensor_mode_transformer.py'
```

Dependencies: NumPy and SciPy. The verified run used Python 3.14, NumPy 2.4.3, and SciPy 1.17.1. No symbolic algebra dependency is required.

Outputs:

- `results.json`: synthetic inputs/results, analytical and independent BVP results, constraint residuals, limits, convergence, and force/recoil ledger.
- `physical_transfers.csv`: the physical acceleration transfer, with the common-mode floor shown separately from massive-mode attenuation.

Validation includes equal-mass/no-wall and zero-thickness limits, vanishing source overlap, long source separation, sourced FP constraints, independent BVP versus closed form, increasing numerical accuracy, smooth-to-step profile convergence, and equal/opposite gate/source forces. Running the script rewrites only its two generated output files.

The key result is that a scalar multiplying the tuned interaction potential changes the relative eigenmode mass while leaving the common massless combination unchanged in the chosen linearization. A large reduction of the massive contribution is therefore not equivalent to a large reduction of the complete physical field.
