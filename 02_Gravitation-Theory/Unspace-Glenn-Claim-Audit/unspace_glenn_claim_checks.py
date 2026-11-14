"""Checks for the Unspace radial-stress torsion-balance paper (Lentz et al., Symmetry 2026)
and the Glenn spark-gap interferometry paper (EJ-ENG 2025).

Standard library plus numpy. Every input is quoted from the paper it comes from;
derived quantities are computed here. Writes results.json next to this file.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

G = 6.67430e-11
C = 299_792_458.0
out: dict = {}

# ---------------------------------------------------------------------------
# Unspace (Lentz et al. 2026) — inputs from Tables 2-4 and Section 2
# ---------------------------------------------------------------------------
m_test = 0.0383          # kg, test mass
R_arm = 0.05             # m
R_p = 0.00819            # m, test-mass radius
T_period = 492.0         # s, isochronal period
M_src = 1.692            # kg, mean source mass
R_src = 0.027            # m, source equatorial radius
rho_src = 7800.0         # kg/m^3 as stated (W-Ni-Cu heavy alloy is ~17,000)
E_mod = 2.758e11         # Pa
nu = 0.298
r_rest = 0.0466          # m, test-to-source centre distance at rest
lever = 0.0686           # m, source radius from turntable pivot
theta_s = math.radians(43.2)

# Stated density (Section 2.1, Table 4) versus the stated alloy and masses.
# 90W-6Ni-4Cu heavy alloy is about 17,000 kg/m^3 (ASTM B777 class 1 range 16.85-17.25 g/cm^3).
V_sphere = 4 / 3 * math.pi * R_src**3
out["unspace_sphere_mass_at_7800"] = 7800 * V_sphere
out["unspace_sphere_mass_at_17000"] = 17000 * V_sphere
out["unspace_test_mass_density_from_m_and_Rp"] = m_test / (4 / 3 * math.pi * R_p**3)

I_p = 2 * m_test * (R_arm**2 + 0.4 * R_p**2)
k = 4 * math.pi**2 * I_p / T_period**2
out["unspace_I_p"] = I_p
out["unspace_k"] = k

# Table 3 (omega, position, theta0, theta_rest, dtheta_rest, dtheta_rot)
table3 = [
    (104.82, "CCW", 0.00084, 0.00537, 0.00621, 0.00004),
    (104.82, "CW", -0.00084, -0.00706, -0.00621, -0.00008),
    (263.89, "CCW", -0.00211, 0.00453, 0.00664, 0.00009),
    (263.89, "CW", -0.00211, -0.00875, -0.00664, -0.00017),
    (535.64, "CCW", -0.00254, 0.00378, 0.00632, 0.00024),
    (535.64, "CW", -0.00254, -0.00887, -0.00632, -0.00035),
    (808.96, "CCW", -0.00125, 0.00406, 0.00532, 0.00072),
    (808.96, "CW", -0.00125, -0.00657, -0.00532, -0.00039),
    (1089.09, "CCW", 0.01396, 0.01885, 0.00489, 0.00062),
    (1089.09, "CW", 0.01396, 0.00908, -0.00489, -0.00120),
    (1534.98, "CCW", 0.01332, 0.01972, 0.00641, 0.00140),
    (1534.98, "CW", 0.01332, 0.00691, -0.00641, -0.00122),
    (1755.94, "CCW", 0.01430, 0.01984, 0.00555, 0.00176),
    (1755.94, "CW", 0.01430, 0.00875, -0.00555, -0.00156),
    (2085.09, "CCW", -0.00031, 0.00661, 0.00692, 0.00307),
    (2085.09, "CW", -0.00031, -0.00723, -0.00692, -0.00656),
    (2474.00, "CCW", 0.01426, 0.02150, 0.00724, 0.00607),
    (2474.00, "CW", 0.01426, 0.00702, -0.00724, -0.00806),
    (2751.51, "CCW", 0.01789, 0.02251, 0.00463, 0.00785),
    (2751.51, "CW", 0.01789, 0.01326, -0.00463, -0.00838),
    (2971.63, "CCW", 0.00234, 0.00719, 0.00485, 0.00939),
    (2971.63, "CW", 0.00234, -0.00251, -0.00485, -0.00901),
    (3526.96, "CCW", -0.00208, 0.00379, 0.00587, 0.01878),
    (3526.96, "CW", -0.00208, -0.00795, -0.00587, -0.01865),
    (4170.36, "CCW", -0.00028, 0.00487, 0.00515, 0.02549),
    (4172.45, "CW", -0.00028, -0.00543, -0.00515, -0.02339),
    (4825.85, "CCW", -0.00021, 0.00689, 0.00711, 0.02760),
    (4833.86, "CW", -0.00021, -0.00732, -0.00711, -0.03356),
    (5494.28, "CCW", 0.00023, 0.00678, 0.00655, 0.03583),
    (5462.76, "CW", 0.00023, -0.00633, -0.00655, -0.03703),
]
w = np.array([r[0] for r in table3])
d_rest = np.array([r[4] for r in table3])
d_rot = np.array([r[5] for r in table3])

# Table 3 internal arithmetic: dtheta_rest = theta_rest - theta0 (eq. 13)
resid = [r[3] - r[2] - r[4] for r in table3]
out["unspace_table3_eq13_max_residual_rad"] = max(abs(x) for x in resid)

# --- G "validation" (Section 3.5) ---
CG = k / 2 * r_rest**2 / (M_src * m_test * R_arm)
G_mean = CG * np.mean(np.abs(d_rest))
G_i_abs = CG * np.abs(d_rest)
G_i_signed = CG * d_rest
sd_abs = float(np.std(G_i_abs, ddof=1))
sd_signed_about_abs_mean = float(math.sqrt(np.sum((G_i_signed - G_mean) ** 2) / (len(w) - 1)))
n = len(w)
out["unspace_CG"] = CG
out["unspace_G_mean"] = float(G_mean)
out["unspace_sd_abs"] = sd_abs
out["unspace_sd_signed_about_abs_mean"] = sd_signed_about_abs_mean
out["unspace_Z_paper_method"] = abs(G_mean - G) / (sd_signed_about_abs_mean / math.sqrt(n))
out["unspace_Z_abs_values"] = abs(G_mean - G) / (sd_abs / math.sqrt(n))
# pairs are the same rest value measured once per pair? (CW/CCW share |dtheta_rest|)
pairs_identical = all(abs(abs(table3[i][4]) - abs(table3[i + 1][4])) < 1e-12 for i in range(0, n, 2))
out["unspace_rest_pairs_identical_magnitude"] = pairs_identical
sd_pairs = float(np.std(G_i_abs[::2], ddof=1))
out["unspace_Z_abs_15_independent"] = abs(G_mean - G) / (sd_pairs / math.sqrt(n // 2))

# Geometry: source position from pivot (lever, theta_s) vs test mass at (R_arm, 0)
src = np.array([lever * math.cos(theta_s), lever * math.sin(theta_s)])
tm = np.array([R_arm, 0.0])
near = src - tm
out["unspace_near_source_offset_m"] = near.tolist()
far_src = -src
far = far_src - tm
dist_far = float(np.linalg.norm(far))
# torque per unit (G M m R_arm): near source perpendicular to arm; far source y-component
tq_near = 1 / np.linalg.norm(near) ** 2 * (near[1] / np.linalg.norm(near))
tq_far = 1 / dist_far**2 * (far[1] / dist_far)
out["unspace_far_source_distance_m"] = dist_far
out["unspace_far_source_torque_fraction"] = float(tq_far / tq_near)
out["unspace_G_with_far_source"] = float(G_mean / (1 + tq_far / tq_near))

# --- regression of |dtheta_rot| on omega ---
y = np.abs(d_rot)
A = np.vstack([w**2, w, np.ones_like(w)]).T
coef, res, *_ = np.linalg.lstsq(A, y, rcond=None)
out["unspace_quadfit_abc"] = coef.tolist()
# pure power law fit on points above 500 rad/s
mask = w > 500
p = np.polyfit(np.log(w[mask]), np.log(y[mask]), 1)
resid_pl = np.log(y[mask]) - np.polyval(p, np.log(w[mask]))
s2 = np.sum(resid_pl**2) / (mask.sum() - 2)
X = np.vstack([np.log(w[mask]), np.ones(mask.sum())]).T
cov = s2 * np.linalg.inv(X.T @ X)
out["unspace_powerlaw_exponent"] = float(p[0])
out["unspace_powerlaw_exponent_se"] = float(math.sqrt(cov[0, 0]))
# compare one-parameter w^2 and w^3 models (least squares amplitude)
for n_exp in (2, 3):
    a = np.sum(y * w**n_exp) / np.sum(w ** (2 * n_exp))
    rss = float(np.sum((y - a * w**n_exp) ** 2))
    out[f"unspace_rss_w{n_exp}"] = rss
# rot/rest ratio at the top
out["unspace_rot_over_rest_top"] = float(np.mean(y[-2:]) / np.mean(np.abs(d_rest)))

# --- required force / torque at the top speed ---
theta_top = float(np.mean(y[-2:]))
torque_top = k * theta_top
F_each = torque_top / (2 * R_arm)
out["unspace_torque_top_Nm"] = torque_top
out["unspace_force_per_test_mass_N"] = F_each
out["unspace_force_equiv_mass_ug"] = F_each / 9.80665 * 1e9
out["unspace_test_mass_displacement_mm"] = theta_top * R_arm * 1e3
# air-flow and pressure equivalents
mu_air = 1.81e-5
v_stokes = F_each / (6 * math.pi * mu_air * R_p)
dp_equiv = F_each / (math.pi * R_p**2)
out["unspace_stokes_air_speed_mm_s"] = v_stokes * 1e3
out["unspace_pressure_difference_equiv_Pa"] = dp_equiv
w_top = 5462.76
tip = w_top * R_src
q_dyn = 0.5 * 1.2 * tip**2
out["unspace_tip_speed_m_s"] = tip
out["unspace_dynamic_pressure_Pa"] = q_dyn
out["unspace_pressure_fraction_of_dynamic"] = dp_equiv / q_dyn
out["unspace_reynolds_rotation"] = w_top * R_src**2 / 1.5e-5
# natural-convection temperature scale for that flow over 5 cm (inviscid upper bound on sensitivity)
out["unspace_convection_dT_K"] = v_stokes**2 / (9.81 * (1 / 295.0) * 0.05)

# --- GR expectations ---
I_src = 0.4 * M_src * R_src**2
KE = 0.5 * I_src * w_top**2
out["unspace_KE_J"] = KE
out["unspace_KE_over_Mc2"] = KE / (M_src * C**2)
# stress/(rho c^2) scale (rho as stated)
sigma_scale = rho_src * w_top**2 * R_src**2
out["unspace_stress_scale_Pa"] = sigma_scale
out["unspace_stress_over_rho_c2"] = sigma_scale / (rho_src * C**2)
out["unspace_GR_expected_dtheta_rad"] = float(np.mean(np.abs(d_rest))) * KE / (M_src * C**2)
# their eq. 89 at top speed (r = r_rest)
theta_p = m_test * R_arm * (math.pi * G / (2 * C**2 * r_rest)) * rho_src * w_top**2 * (3 + nu) * R_src**4 / k
out["unspace_eq89_theta_p_top"] = theta_p
out["unspace_eq89_gap_orders"] = math.log10(theta_top / theta_p)
out["unspace_GR_gap_orders"] = math.log10(theta_top / out["unspace_GR_expected_dtheta_rad"])

# Newtonian centrifugal deformation (disk rim displacement, plane stress)
u_rim = (1 - nu) * rho_src * w_top**2 * R_src**3 / (4 * E_mod)
out["unspace_rim_expansion_m"] = u_rim
# quadrupole-scale fractional force change ~ (u/R) (R/r)^2
frac = (u_rim / R_src) * (R_src / r_rest) ** 2
out["unspace_newtonian_deformation_dtheta_rad"] = float(np.mean(np.abs(d_rest))) * frac

# --- acceleration-rate consistency ---
out["unspace_omega_after_500s_at_1666"] = 1.666 * 500
out["unspace_time_to_5462_at_1666_s"] = 5462 / 1.666

# --- their energy "match" (eq. 95/107) and its dependence on units and slice ---
def Es(omega, r_rot, Z, unit=1.0):
    """Eq. 107 as printed: 2 (w/c)^2 * int_0^R int_-Z^Z Trr (1/2pi) ln|r'-r_rot| r'^3 dz dr'.
    unit: lengths are divided by `unit` inside the logarithm only (unit=0.01 -> centimetres)."""
    pref = 0.125 * rho_src * omega**2 * (3 + nu)
    rs = np.linspace(0, R_src, 20001)
    integrand = pref * (R_src**2 - rs**2) / (2 * math.pi) * np.log(np.abs(rs - r_rot) / unit) * rs**3
    radial = np.trapezoid(integrand, rs)
    return 2 * (omega / C) ** 2 * radial * 2 * Z

w_ex = 2085.09
r_rot = 0.0466 - 1.35e-9 * w_ex**2 * R_arm
E_paper = Es(w_ex, 0.0466, R_p)
out["unspace_Es_2085_metres_Z=Rp"] = E_paper
out["unspace_Es_2085_centimetres_Z=Rp"] = Es(w_ex, 0.0466, R_p, unit=0.01)
out["unspace_Es_2085_metres_Z=R"] = Es(w_ex, 0.0466, R_src)
out["unspace_Urot_2085"] = 0.5 * k * (1.35e-9 * w_ex**2) ** 2

# ---------------------------------------------------------------------------
# Glenn (2025)
# ---------------------------------------------------------------------------
r_sp = 0.25e-3
for l_sp in (2.5e-3, 3.5e-3):
    V = math.pi * r_sp**2 * l_sp
    for u in (1.4e9, 2.4e9, 1e11, 1e12):
        out[f"glenn_energy_J_l{l_sp*1e3:.1f}mm_u{u:.1e}"] = u * V
V25 = math.pi * r_sp**2 * 2.5e-3
E_spark = 2.4e9 * V25
out["glenn_spark_volume_m3"] = V25
out["glenn_spark_energy_J_at_2.4GJ"] = E_spark
# GR: static potential and quadrupole-strain scales at 1 cm
r_obs = 0.01
out["glenn_static_potential_over_c2_at_1cm"] = G * (E_spark / C**2) / (r_obs * C**2)
out["glenn_strain_scale_2GE_over_c4r"] = 2 * G * E_spark / (C**4 * r_obs)
h_obs = 160e-9 / 0.725
out["glenn_observed_strain"] = h_obs
out["glenn_gap_orders"] = math.log10(h_obs / out["glenn_strain_scale_2GE_over_c4r"])
# GW wavelength for a 1 ms or 1 us source timescale
out["glenn_gw_wavelength_1ms_km"] = C * 1e-3 / 1e3
out["glenn_gw_wavelength_1us_m"] = C * 1e-6
# Refractive budget: path change 150 nm through hot-air path lengths
n_air_minus_1 = 2.77e-4
for path in (0.005, 0.02):
    dn = 150e-9 / path
    out[f"glenn_dn_needed_path{path*1e3:.0f}mm"] = dn
    out[f"glenn_dT_needed_path{path*1e3:.0f}mm_K"] = dn / n_air_minus_1 * 295.0
# Heating of air within 5 mm by half the spark energy
m_air = 1.2 * 4 / 3 * math.pi * 0.005**3
out["glenn_dT_5mm_sphere_half_energy_K"] = 0.5 * E_spark / (m_air * 1005)
# Air dispersion 532 vs 650 nm (Ciddor-type standard air, (n-1) x 1e8)
def n_minus_1(lam_um):
    s2 = (1 / lam_um) ** 2
    return (5792105 / (238.0185 - s2) + 167917 / (57.362 - s2)) * 1e-8
d532, d650 = n_minus_1(0.532), n_minus_1(0.650)
out["glenn_air_n-1_532"] = d532
out["glenn_air_n-1_650"] = d650
out["glenn_refractive_nm_ratio_532_650"] = d532 / d650
out["glenn_wavelength_ratio_650_532"] = 0.650 / 0.532
out["glenn_fringe_count_ratio_532_650_same_OPL"] = 0.650 / 0.532 * d532 / d650
# Alcubierre prefactor: (v^2/4)(f')^2 with f' = 2 a b (r-r0) e^{..} -> v^2 a^2 b^2 (...)^2 e^{..}
out["glenn_eq12_prefactor_should_be"] = "c^4/(8 pi G)"
out["glenn_eq12_prefactor_printed"] = "c^4/(2 pi G)"
# He index contrast
out["glenn_helium_n-1"] = 3.5e-5
out["glenn_air_minus_helium_index"] = n_air_minus_1 - 3.5e-5

Path(__file__).with_name("results.json").write_text(
    json.dumps(out, indent=2, default=float), encoding="utf-8")
for key, val in out.items():
    print(f"{key} = {val}")
