"""Numerical checks for the Alzofon theory derivation audit (2026-11-09).

Standard library only. Every number quoted in
01_Reports-and-Syntheses/Alzofon-Theory-Derivation-Audit-2026.md is produced
here and asserted against a stated expectation. Run:

    python alzofon_theory_audit_checks.py

Writes results.json next to this file. Inputs that are assumptions rather than
measured apparatus values are marked ASSUMED in the output.
"""

import json
import math
import random
from pathlib import Path

# ---------------------------------------------------------------- constants
h = 6.62607015e-34          # J s (exact)
hbar = h / (2 * math.pi)
c = 299792458.0             # m/s (exact)
kB = 1.380649e-23           # J/K (exact)
G = 6.67430e-11             # m^3 kg^-1 s^-2 (CODATA 2018)
mu0 = 4 * math.pi * 1e-7    # T m/A (to 1e-9)
muB = 9.2740100783e-24      # J/T
NA = 6.02214076e23
u = 1.66053906660e-27       # kg
m_p = 1.67262192369e-27     # kg
m_e = 9.1093837015e-31      # kg
g0 = 9.80665                # m/s^2
R_E = 6.371e6               # m, mean Earth radius

# 27Al nuclear data
I_Al = 2.5
gamma_Al = 11.103e6         # Hz/T (gamma/2pi)
A_Al = 26.9815385           # g/mol
gamma_e = 28.02495e9        # Hz/T (free electron, gamma/2pi)

out = {}


def close(a, b, rel):
    return abs(a - b) <= rel * abs(b)


# ------------------------------------------------- 1. formalism (eqs 1-11)
# Alzofon 2010 eq. (6): dS^2 = dr^2 - c^2 dt^2 + dr0^2 - c^2 dt0^2, with
# dS = 0 imposed; eq. (7)-(8) define p, E, p0, E0 using the ORDINARY proper
# time dtau^2 = dt^2 - dr^2/c^2.  Check that the mass shell E^2/c^2 - p^2 =
# (mc)^2 holds identically from the definitions, that eq. (11) then holds
# for any motion (not only dr = 0), and that the hidden displacement is
# always spacelike.
random.seed(20261109)
m = 1.0
worst_shell = worst_11 = 0.0
spacelike = True
for _ in range(10000):
    dt = random.uniform(0.5, 2.0)
    v = [random.uniform(-0.55, 0.55) * c for _ in range(3)]
    dr = [vi * dt for vi in v]
    dr2 = sum(x * x for x in dr)
    dtau = math.sqrt(dt * dt - dr2 / c ** 2)
    # choose hidden interval freely except for the null condition dS = 0
    dt0 = random.uniform(-2.0, 2.0)
    need = c * c * dt * dt - dr2 + c * c * dt0 * dt0   # = |dr0|^2
    n = [random.gauss(0, 1) for _ in range(3)]
    norm = math.sqrt(sum(x * x for x in n))
    dr0 = [math.sqrt(need) * x / norm for x in n]
    p2 = m * m * dr2 / dtau ** 2
    E = m * c * c * dt / dtau
    p02 = m * m * sum(x * x for x in dr0) / dtau ** 2
    E0 = m * c * c * dt0 / dtau
    shell = (E / c) ** 2 - p2                 # should equal (mc)^2
    eq11 = p02 - (E0 / c) ** 2                # should equal (mc)^2
    worst_shell = max(worst_shell, abs(shell / (m * c) ** 2 - 1))
    worst_11 = max(worst_11, abs(eq11 / (m * c) ** 2 - 1))
    spacelike &= sum(x * x for x in dr0) > (c * dt0) ** 2
assert worst_shell < 1e-9 and worst_11 < 1e-9 and spacelike
out["formalism"] = {
    "mass_shell_is_identity_max_rel_residual": worst_shell,
    "eq11_holds_for_all_motions_max_rel_residual": worst_11,
    "hidden_interval_always_spacelike": spacelike,
    "signature_of_eq3": "(+,+,+,-,+,+,+,-): six space-like, two time-like",
}

# Eq. (3) and eq. (5) are different quadratic forms: (5) contains the cross
# term -2 x.x0 + 2 c^2 t t0 that (3) drops.  They agree only on average.
N = 200000
acc = 0.0
single = None
x, t = 1.0, 0.3e-8
for i in range(N):
    x0 = random.gauss(0, 0.2)
    t0 = random.gauss(0, 0.2) / c
    S5 = (x - x0) ** 2 - c * c * (t - t0) ** 2
    S3 = x * x - c * c * t * t + x0 * x0 - c * c * t0 * t0
    acc += S5 - S3
    if i == 0:
        single = S5 - S3
assert abs(single) > 1e-3 and abs(acc / N) < 5e-3
out["formalism"]["eq5_minus_eq3_single_draw"] = single
out["formalism"]["eq5_minus_eq3_mean"] = acc / N

# ------------------------------------------- 2. gravity model (Section 7)
alpha_G = G * m_p ** 2 / (hbar * c)
lam_p = h / (m_p * c)
lam_e = h / (m_e * c)
assert close(alpha_G, 5.906e-39, 2e-3)
assert close(lam_p, 1.3214e-15, 1e-3) and close(lam_e, 2.4263e-12, 1e-3)
out["gravity_model"] = {
    "G_mp^2_over_hbar_c": alpha_G,
    "orders_of_magnitude_missing": -math.log10(alpha_G),
    "proton_compton_wavelength_m": lam_p,
    "electron_compton_wavelength_m": lam_e,
    "note": "h, c and m alone give a dimensionless coupling of order one; "
            "nothing in the stated mechanism supplies 5.9e-39",
}

# Composition dependence if the source counted nucleons rather than energy.
mass_per_nucleon = {
    "Be9": 9.0121831 / 9,
    "Al27": 26.9815385 / 27,
    "Ti48": 47.9479463 / 48,
}
eta_BeTi = 2 * (mass_per_nucleon["Be9"] - mass_per_nucleon["Ti48"]) / (
    mass_per_nucleon["Be9"] + mass_per_nucleon["Ti48"])
eta_BeAl = 2 * (mass_per_nucleon["Be9"] - mass_per_nucleon["Al27"]) / (
    mass_per_nucleon["Be9"] + mass_per_nucleon["Al27"])
assert 2.0e-3 < eta_BeTi < 2.8e-3 and 1.7e-3 < eta_BeAl < 2.4e-3
out["gravity_model"]["nucleon_count_source_eta_Be_Ti"] = eta_BeTi
out["gravity_model"]["nucleon_count_source_eta_Be_Al"] = eta_BeAl
out["gravity_model"]["measured_limit_Be_Ti_Schlamminger2008"] = "(0.3 +/- 1.8)e-13"
out["gravity_model"]["excluded_by_orders"] = math.log10(eta_BeTi / 1.8e-13)

# --------------------------------- 3. spin bridge: energy and polarization
def al_numbers(B, T):
    dE = h * gamma_Al * B                       # adjacent-level spacing, J
    P_th = (I_Al + 1) / 3 * dE / (kB * T)       # high-T polarization <Iz>/I
    return dE, P_th


# Cross-check against Stark, Grafe, Tajmar Table 6 (9 T, 5 K, gamma = 11.094):
Iz_stark = (h * 11.094e6 * 9.0) * I_Al * (I_Al + 1) / (3 * kB * 5.0)
assert close(Iz_stark, 2.8e-3, 0.03)

B_alz, T_room = 0.33, 300.0
dE, P_th = al_numbers(B_alz, T_room)
P_e = math.tanh(muB * B_alz / (kB * T_room))
enh_max = gamma_e / gamma_Al
P_dnp_ceiling = P_th * enh_max
n_per_g = NA / A_Al
E_spin_full_per_g = n_per_g * I_Al * dE         # J/g at P = 1
E_grav_per_g = 1e-3 * g0 * R_E                  # J/g, |U| = m g R
E_lattice_per_g = 0.897 * T_room                # J/g, c_p * T, rough
assert close(dE / 1.602176634e-19, 1.515e-8, 0.01)
assert close(P_th, 6.8e-7, 0.03) and close(enh_max, 2524, 0.01)
assert close(E_spin_full_per_g, 1.355e-4, 0.01)
assert close(E_grav_per_g, 6.25e4, 0.01)

claim_alzofon = 1.1e-3 / 0.5                    # 1.1 mg on ~0.5 g Al
claim_falcon = 4.0e-3 / 1.72                    # ~4 mg half-swing on 1.72 g
pred = {
    "P=1": E_spin_full_per_g / E_grav_per_g,
    "P=DNP ceiling": P_dnp_ceiling * E_spin_full_per_g / E_grav_per_g,
    "P=thermal 300 K": P_th * E_spin_full_per_g / E_grav_per_g,
}
assert close(pred["P=1"], 2.2e-9, 0.03)
out["spin_bridge"] = {
    "Al27_level_spacing_eV_at_0.33T": dE / 1.602176634e-19,
    "thermal_nuclear_polarization_300K": P_th,
    "electron_polarization_300K": P_e,
    "max_DNP_enhancement_gamma_e_over_gamma_n": enh_max,
    "nuclear_polarization_DNP_ceiling": P_dnp_ceiling,
    "spin_energy_J_per_g_at_P1": E_spin_full_per_g,
    "earth_gravitational_energy_J_per_g": E_grav_per_g,
    "lattice_thermal_energy_J_per_g_rough": E_lattice_per_g,
    "lattice_over_spin_energy_at_P1": E_lattice_per_g / E_spin_full_per_g,
    "fractional_weight_change_if_spin_energy_drawn_from_gravity": pred,
    "claimed_fraction_alzofon_1994": claim_alzofon,
    "claimed_fraction_falcon_2024_half_swing": claim_falcon,
    "claim_over_prediction_at_DNP_ceiling": claim_alzofon / pred["P=DNP ceiling"],
    "claim_over_prediction_at_P1": claim_alzofon / pred["P=1"],
}
assert out["spin_bridge"]["claim_over_prediction_at_P1"] > 5e5

# Korringa relaxation: T1*T = 1.85 +/- 0.05 s K for aluminium metal.
T1_300 = 1.85 / 300.0
assert close(T1_300, 6.0e-3, 0.05)
out["spin_bridge"]["korringa_T1_at_300K_s"] = T1_300
out["spin_bridge"]["alzofon_pulse_s"] = 6.0e-3

# Mass-energy change from complete spin ordering, standard physics.
dm_over_m_zeeman = E_spin_full_per_g / (1e-3 * c * c)
TS_per_g = n_per_g * kB * T_room * math.log(2 * I_Al + 1)
dm_over_m_TS = TS_per_g / (1e-3 * c * c)
assert close(dm_over_m_zeeman, 1.5e-18, 0.02) and close(dm_over_m_TS, 1.84e-12, 0.02)
out["spin_bridge"]["standard_dm_over_m_zeeman_P1"] = dm_over_m_zeeman
out["spin_bridge"]["standard_dm_over_m_T_times_spin_entropy"] = dm_over_m_TS
out["spin_bridge"]["falcon_claim_over_TS_bound"] = claim_falcon / dm_over_m_TS

# ------------------------- 4. what a dP/dt law implies for a slow CW sweep
cycle_s = 8 * 3600 / 41                      # poster: 41 cycles in 8 hours
sweep_G_per_s = 3500 / cycle_s               # 2000 -> 5500 G, one-way ASSUMED
feature_width_G = 400                        # peak-to-trough, read off plot
feature_time_s = feature_width_G / sweep_G_per_s
rate_ratio = feature_time_s / 6.0e-3         # same delta-P assumed
al_mass_falcon = 1.72 * 0.98                 # g, upper bound (ignores epoxy)
pred_falcon_mg = 1.1 * (al_mass_falcon / 0.5) / rate_ratio
assert 600 < cycle_s < 800 and 1e4 < rate_ratio < 2e4
out["falcon_scaling"] = {
    "cycle_time_s": cycle_s,
    "sweep_rate_G_per_s_ASSUMED_one_way": sweep_G_per_s,
    "feature_width_G_read_from_plot": feature_width_G,
    "time_through_feature_s": feature_time_s,
    "dPdt_ratio_alzofon_over_falcon": rate_ratio,
    "predicted_falcon_signal_mg_under_dPdt_law": pred_falcon_mg,
    "observed_half_swing_mg": 4.0,
    "observed_over_predicted": 4.0 / pred_falcon_mg,
}

# --------------------- 5. conventional forces on the Falcon sample (scale)
F_4mg = 4.0e-6 * g0
m_fe = 1.72e-3 * 0.02                        # kg iron
V_fe = m_fe / 7874.0
B_res = 9.88e9 / gamma_e                     # T, g = 2
M_unsat = 3 * B_res / mu0                    # A/m, sphere below saturation
M_sat = 1.71e6
moment = min(M_unsat, M_sat) * V_fe
grad_for_4mg = F_4mg / moment                # T/m
assert close(B_res, 0.3525, 0.002) and M_unsat < M_sat
assert 0.5e-2 < grad_for_4mg < 2e-2
# RF force on a conducting sample: F ~ 1.5 * V_s * grad(u), u = stored
# energy density.  Q, delivered power, cavity height, sample density and the
# gradient length are ASSUMED; this is an order-of-magnitude scale only.
Q, P_rf, f_rf = 1000.0, 250.0, 9.88e9
a_cav = 3.8317 * c / (2 * math.pi * f_rf)    # TM110 radius
h_cav = 0.02
U = Q * P_rf / (2 * math.pi * f_rf)
u_mean = U / (math.pi * a_cav ** 2 * h_cav)
V_s = 1.72e-6 / 2.4                          # m^3 at 2.4 g/cm^3
F_rf = 1.5 * V_s * (3 * u_mean) / 0.01
assert close(a_cav, 1.851e-2, 0.005)
out["conventional_forces"] = {
    "force_of_4mg_N": F_4mg,
    "resonance_field_T_g2_at_9.88GHz": B_res,
    "iron_mass_g": m_fe * 1e3,
    "iron_moment_A_m2_unsaturated_sphere": moment,
    "dc_gradient_for_4mg_T_per_m": grad_for_4mg,
    "dc_gradient_for_4mg_G_per_cm": grad_for_4mg * 100,
    "TM110_radius_cm": a_cav * 100,
    "rf_stored_energy_J_ASSUMED_Q1000_250W": U,
    "rf_force_scale_mg_ASSUMED": F_rf / g0 * 1e6,
    "radiation_pressure_P_over_c_mg": P_rf / c / g0 * 1e6,
}
assert 0.5 < out["conventional_forces"]["rf_force_scale_mg_ASSUMED"] < 50

Path(__file__).with_name("results.json").write_text(
    json.dumps(out, indent=2), encoding="utf-8")
print("all assertions passed")
