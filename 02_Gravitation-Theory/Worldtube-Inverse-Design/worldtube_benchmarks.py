"""Benchmark scales for the 1 g, 10 m protected-worldtube inverse design."""

from __future__ import annotations

import math


G = 6.67430e-11
C = 299_792_458.0
G0 = 9.80665
R_EARTH = 6.378_137e6
M_EARTH = 5.9722e24
HBAR_C_EV_M = 1.973_269_804e-7
MPL_REDUCED_EV = 2.435e27


def smoothstep_complement(s: float) -> tuple[float, float, float]:
    """chi, dchi/ds, d2chi/ds2 for chi: 1 -> 0 with C2 endpoints."""
    chi = 1.0 - 10.0 * s**3 + 15.0 * s**4 - 6.0 * s**5
    chi_s = -30.0 * s**2 + 60.0 * s**3 - 30.0 * s**4
    chi_ss = -60.0 * s + 180.0 * s**2 - 120.0 * s**3
    return chi, chi_s, chi_ss


def main() -> None:
    length = 10.0
    radius = length / 2.0
    wall = 0.1
    outer_radius = radius + wall

    delta_phi = G0 * length
    delta_lapse = delta_phi / C**2
    delta_g00 = 2.0 * delta_lapse
    allowed_tide = 0.01 * G0 / length
    earth_radial_tide = 2.0 * G0 / R_EARTH
    shell_tide_scale = G0 / wall

    # Static flat-spatial-metric lapse shell: transverse pressure scale.
    pressure_scale = C**2 * G0 / (8.0 * math.pi * G * wall)
    integrated_stress = pressure_scale * wall

    volume = 4.0 * math.pi * radius**3 / 3.0
    field_energy_density = G0**2 / (8.0 * math.pi * G)
    field_energy = field_energy_density * volume

    # Two concentric l=1 Newtonian surface layers: quiet exterior and uniform
    # interior counterfield. sigma(theta)=sigma_1*cos(theta).
    ratio = (radius / outer_radius) ** 3
    sigma_inner = 3.0 * G0 / (4.0 * math.pi * G * (1.0 - ratio))
    sigma_outer = -sigma_inner * ratio
    abs_mass_inner = 2.0 * math.pi * radius**2 * abs(sigma_inner)
    abs_mass_outer = 2.0 * math.pi * outer_radius**2 * abs(sigma_outer)

    # Smooth volume-shell source rho = -g(r chi'' + 4 chi')cos(theta)/(4piG).
    max_rho = 0.0
    max_source_factor = 0.0
    for index in range(100_001):
        s = index / 100_000.0
        _, chi_s, chi_ss = smoothstep_complement(s)
        r = radius + wall * s
        chi_r = chi_s / wall
        chi_rr = chi_ss / wall**2
        source_factor = abs(r * chi_rr + 4.0 * chi_r)
        max_source_factor = max(max_source_factor, source_factor)
        max_rho = max(max_rho, G0 * source_factor / (4.0 * math.pi * G))

    print(f"gL = {delta_phi:.9e} m^2 s^-2")
    print(f"Delta N = gL/c^2 = {delta_lapse:.9e}")
    print(f"|Delta g_00| = {delta_g00:.9e}")
    print(f"allowed tidal eigenvalue = {allowed_tide:.9e} s^-2")
    print(f"Earth radial tidal eigenvalue = {earth_radial_tide:.9e} s^-2")
    print(f"shell tidal scale g/d = {shell_tide_scale:.9e} s^-2")
    print(f"flat-slice pressure scale = {pressure_scale:.9e} Pa")
    print(f"integrated shell stress = {integrated_stress:.9e} N m^-1")
    print(f"uniform-field energy-density magnitude = {field_energy_density:.9e} J m^-3")
    print(f"uniform-field energy magnitude in R=5 m ball = {field_energy:.9e} J")
    print(f"field-energy mass equivalent = {field_energy/C**2:.9e} kg")
    print(f"two-shell sigma_inner amplitude = {sigma_inner:.9e} kg m^-2")
    print(f"two-shell sigma_outer amplitude = {sigma_outer:.9e} kg m^-2")
    print(f"inner layer L1 mass = {abs_mass_inner:.9e} kg")
    print(f"outer layer L1 mass = {abs_mass_outer:.9e} kg")
    print(f"paired-layer L1 mass = {abs_mass_inner + abs_mass_outer:.9e} kg")
    print(f"smooth-shell max |r chi'' + 4chi'| = {max_source_factor:.9e} m^-1")
    print(f"smooth-shell max |rho_eff| = {max_rho:.9e} kg m^-3")
    print(f"photon momentum power per craft kg at 1 g = {G0*C:.9e} W kg^-1")
    print(f"Earth recoil per craft kg = {G0/M_EARTH:.9e} m s^-2 kg^-1")

    # Phase-localized massive-spin-2 diagnostic: 99% attenuation through d.
    attenuation = 0.01
    m_geometric = math.log(1.0 / attenuation) / wall
    m_ev = HBAR_C_EV_M * m_geometric
    lambda3_ev = (m_ev**2 * MPL_REDUCED_EV) ** (1.0 / 3.0)
    metric_amplitude = 2.0 * G0 * radius / C**2
    shell_volume = 4.0 * math.pi * radius**2 * wall
    einstein_prefactor = C**4 / (8.0 * math.pi * G)
    mass_term_energy_density = (
        einstein_prefactor * m_geometric**2 * metric_amplitude**2
    )
    mass_term_energy = mass_term_energy_density * shell_volume
    print(f"99%-attenuation m_geom = {m_geometric:.9e} m^-1")
    print(f"99%-attenuation m_g c^2 = {m_ev:.9e} eV")
    print(f"dRGT Lambda_3 = {lambda3_ev:.9e} eV")
    print(f"inverse-wall energy = {HBAR_C_EV_M/wall:.9e} eV")
    print(f"metric amplitude across R = {metric_amplitude:.9e}")
    print(f"mass-term energy-density scale = {mass_term_energy_density:.9e} J m^-3")
    print(f"mass-term shell-energy scale = {mass_term_energy:.9e} J")

    # Alcubierre shift-shell energy for the same quintic profile.
    profile_integral = 10.0 / 7.0
    for velocity in (1.0, G0, 1_000.0):
        shift_energy = -(
            C**2
            * velocity**2
            * profile_integral
            * radius**2
            / (12.0 * G * wall)
        )
        print(f"Alcubierre energy at v={velocity:g} m/s = {shift_energy:.9e} J")


if __name__ == "__main__":
    main()
