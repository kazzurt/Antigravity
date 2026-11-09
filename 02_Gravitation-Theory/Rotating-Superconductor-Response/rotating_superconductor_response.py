"""Reproduce the rotating-superconductor response and Tate inversions.

The model uses two independently phase-rigid components with signed
charge-to-mass ratios Q_s and Q_chi and a positive stiffness matrix

    R / rho_s = [[1, x],
                 [x, r]].

Here x = rho_s_chi / rho_s, r = rho_chi / rho_s, and
y = Q_chi / Q_s.  The fractional shift of the rotation-induced
magnetic field from the one-component London value is

    delta = (1-y)(x+r*y) / (1+2*x*y+r*y*y).

An ordinary elastic lattice is not a second phase-rigid component and
must not be inserted into this formula as chi.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isclose


M_E = 9.109_383_713_9e-31
U = 1.660_539_068_92e-27
M_NB = 92.906_37 * U


def field_shift(x: float, r: float, y: float) -> float:
    """Return B/B_one_component - 1."""
    denominator = 1.0 + 2.0 * x * y + r * y * y
    return (1.0 - y) * (x + r * y) / denominator


def invert_x(delta: float, r: float, y: float) -> float:
    """Solve the response formula for x at fixed delta, r, and y."""
    denominator = (1.0 - y) - 2.0 * delta * y
    return (delta * (1.0 + r * y * y) - r * y * (1.0 - y)) / denominator


def positive_definite(x: float, r: float) -> bool:
    """Check positivity of [[1,x],[x,r]]."""
    return r > 0.0 and x * x < r


@dataclass(frozen=True)
class Residual:
    label: str
    delta: float

    @property
    def ppm(self) -> float:
        return self.delta * 1.0e6

    @property
    def neutral_x(self) -> float:
        return self.delta

    @property
    def minimum_r(self) -> float:
        return self.delta * self.delta

    @property
    def pair_inertia_kg(self) -> float:
        return 2.0 * M_E * self.delta

    @property
    def niobium_atom_fraction_per_pair(self) -> float:
        return self.pair_inertia_kg / M_NB


RESIDUALS = (
    Residual("Tate relative to bare 2m_e", 84.0e-6),
    Residual("Tate relative to 0.999992 baseline", 92.0e-6),
    Residual("Hoang secondary-summary value", 18.0e-6),
)


def verify_symbolic_identities() -> None:
    for residual in RESIDUALS:
        x = residual.neutral_x
        r = max(1.0e-6, 2.0 * residual.minimum_r)
        reconstructed = field_shift(x=x, r=r, y=0.0)
        assert isclose(reconstructed, residual.delta, rel_tol=0.0, abs_tol=1e-18)
        assert positive_definite(x, r)

    examples = (
        (92.0e-6, 2.0e-3, -0.2),
        (84.0e-6, 1.0e-2, 0.05),
        (18.0e-6, 4.0e-4, -0.01),
    )
    for delta, r, y in examples:
        x = invert_x(delta=delta, r=r, y=y)
        reconstructed = field_shift(x=x, r=r, y=y)
        assert isclose(reconstructed, delta, rel_tol=1e-12, abs_tol=1e-15)


def main() -> None:
    verify_symbolic_identities()

    measured_ratio = 1.000_084
    cabrera_peskin_jiang_liu_observed_baseline = 0.999_992
    print(f"Tate measured m_app/(2m_e) = {measured_ratio:.6f}")
    print(
        "Tate shift from bare 2m_e = "
        f"{(measured_ratio - 1.0) * 1e6:.1f} ppm"
    )
    print(
        "Tate discrepancy from 0.999992 baseline = "
        f"{(measured_ratio - cabrera_peskin_jiang_liu_observed_baseline) * 1e6:.1f} ppm"
    )
    print()

    header = (
        f"{'Residual':43s} {'ppm':>8s} {'x (neutral)':>14s} "
        f"{'r_min':>12s} {'Delta m_pair [kg]':>20s} {'M_Nb fraction':>16s}"
    )
    print(header)
    print("-" * len(header))
    for residual in RESIDUALS:
        print(
            f"{residual.label:43s} "
            f"{residual.ppm:8.1f} "
            f"{residual.neutral_x:14.6e} "
            f"{residual.minimum_r:12.6e} "
            f"{residual.pair_inertia_kg:20.6e} "
            f"{residual.niobium_atom_fraction_per_pair:16.6e}"
        )

    print()
    print("General inversion:")
    print(
        "x = [delta(1 + r y^2) - r y(1-y)] / "
        "[(1-y) - 2 delta y]"
    )
    print("All identity and inversion checks passed.")


if __name__ == "__main__":
    main()
