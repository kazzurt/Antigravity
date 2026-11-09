"""Reproducible checks for the coupled London--GEM eigenmode theorem.

The conventions follow Inan (2022): mu_G = 4*pi*G/c^2 and the
stationary field equations are

    laplacian(B)   = a B - b B_G
    laplacian(B_G) = c B - d B_G.

This script verifies the rank-one response, evaluates the fixed
gravitomagnetic/electromagnetic source ratio, and checks the closed-form
finite-slab solution against the differential equations.
"""

from __future__ import annotations

import math


G = 6.67430e-11  # m^3 kg^-1 s^-2
C = 299_792_458.0  # m s^-1
MU_0 = 1.256_637_062_12e-6  # N A^-2
E = 1.602_176_634e-19  # C
M_E = 9.109_383_7139e-31  # kg
R_EARTH = 6.378_137e6  # m
M_EARTH = 5.9722e24  # kg
OMEGA_EARTH = 7.292_115_0e-5  # rad s^-1
EARTH_MOI_FACTOR = 0.3307


def slab_solution(
    z: float,
    thickness: float,
    kappa: float,
    b: float,
    r: float,
    b_left: float,
    bg_left: float,
    b_right: float,
    bg_right: float,
) -> tuple[float, float]:
    """Return B and B_G in a planar slab with Dirichlet data at both faces."""
    c_left = bg_left - r * b_left
    c_right = bg_right - r * b_right
    c_harmonic = c_left + (c_right - c_left) * z / thickness
    q_left = b_left - b * c_left / kappa**2
    q_right = b_right - b * c_right / kappa**2
    denominator = math.sinh(kappa * thickness)
    screened = (
        q_left * math.sinh(kappa * (thickness - z))
        + q_right * math.sinh(kappa * z)
    ) / denominator
    magnetic = b * c_harmonic / kappa**2 + screened
    gravitomagnetic = c_harmonic + r * magnetic
    return magnetic, gravitomagnetic


def main() -> None:
    mu_g = 4.0 * math.pi * G / C**2
    r = mu_g * M_E / (MU_0 * E)
    beta = 4.0 * M_E / E

    earth_j = EARTH_MOI_FACTOR * M_EARTH * R_EARTH**2 * OMEGA_EARTH
    bg_earth_pole = 2.0 * G * earth_j / (C**2 * R_EARTH**3)
    b_boundary_match = bg_earth_pole / r
    b_current_reversal = beta * bg_earth_pole

    print(f"mu_G = {mu_g:.12e} m kg^-1")
    print(f"r = B_G/B = {r:.12e} C kg^-1")
    print(f"beta = 4 m_e/e = {beta:.12e} kg C^-1")
    print(f"Earth J = {earth_j:.12e} kg m^2 s^-1")
    print(f"Earth polar B_G scale = {bg_earth_pole:.12e} s^-1")
    print(f"B for harmonic-mode elimination = {b_boundary_match:.12e} T")
    print(f"B for London-current sign reversal = {b_current_reversal:.12e} T")
    print(
        "separation of the two conditions = "
        f"{b_boundary_match / b_current_reversal:.12e}"
    )

    # Dimensionless finite-slab check.  Choose a=1.0, d=1e-6, so that
    # kappa^2=a-d and r=d/b.  b=0.2 gives c=r*a and det(M)=0.
    a = 1.0
    d = 1.0e-6
    b = 0.2
    r_test = d / b
    c = r_test * a
    kappa = math.sqrt(a - d)
    determinant = -a * d + b * c
    print(f"det(response matrix) = {determinant:.12e}")
    print(f"eigenvalues = 0, {kappa**2:.12e}")

    thickness = 10.0
    args = dict(
        thickness=thickness,
        kappa=kappa,
        b=b,
        r=r_test,
        b_left=1.0,
        bg_left=0.4,
        b_right=-0.3,
        bg_right=0.1,
    )
    z = 4.0
    b_zero, bg_zero = slab_solution(z, **args)
    c_left = args["bg_left"] - r_test * args["b_left"]
    c_right = args["bg_right"] - r_test * args["b_right"]
    q_left = args["b_left"] - b * c_left / kappa**2
    q_right = args["b_right"] - b * c_right / kappa**2
    screened = (
        q_left * math.sinh(kappa * (thickness - z))
        + q_right * math.sinh(kappa * z)
    ) / math.sinh(kappa * thickness)
    b_second = kappa**2 * screened
    bg_second = r_test * b_second
    residual_b = b_second - (a * b_zero - b * bg_zero)
    residual_bg = bg_second - (c * b_zero - d * bg_zero)
    print(f"finite-slab B-equation residual = {residual_b:.6e}")
    print(f"finite-slab B_G-equation residual = {residual_bg:.6e}")


if __name__ == "__main__":
    main()
