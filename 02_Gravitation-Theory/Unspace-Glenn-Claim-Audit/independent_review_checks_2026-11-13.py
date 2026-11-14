"""Independent checks for the 13 November 2026 review of the Opus assessments.

Run with Python 3 and numpy. Reads the existing Table 3 transcription as an AST
literal (does not execute or modify the original audit). Table values used below
were checked against p. 21 of the local Lentz et al. source PDF. No solver runs.
Prints JSON; does not write or overwrite other files.
"""
from pathlib import Path
import ast
import json
import math
import numpy as np

HERE = Path(__file__).resolve().parent
tree = ast.parse((HERE / 'unspace_glenn_claim_checks.py').read_text(encoding='utf-8'))
rows = next(ast.literal_eval(node.value) for node in tree.body
            if isinstance(node, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == 'table3' for t in node.targets))
w = np.array([row[0] for row in rows])
rot = np.abs([row[5] for row in rows])
rest = np.abs([row[4] for row in rows])

G = 6.67430e-11
c = 299792458.0
m, M, arm, rp, distance = 0.0383, 1.692, 0.05, 0.00819, 0.0466
inertia = 2 * m * (arm**2 + 0.4 * rp**2)
k = 4 * math.pi**2 * inertia / 492**2
U_rest = 0.5 * k * rest.mean()**2
GMm_over_r = G * M * m / distance
force = k * rot[-2:].mean() / (2 * arm)
stokes_speed = force / (6 * math.pi * 1.81e-5 * rp)
freefall_dT = stokes_speed**2 / (9.81 / 295 * 0.05)

out = {
    'input': 'Table 3 transcription from unspace_glenn_claim_checks.py; source PDF p.21',
    'k_Nm_per_rad': k,
    'mean_static_rad': float(rest.mean()),
    'crossing_of_published_quadratic_and_mean_static_rad_s': math.sqrt(rest.mean() / 1.35e-9),
    'selected_table3_pairs': [
        {'omega_rad_s': float(w[i]), 'rotation_rad': rot[i:i+2].tolist(),
         'static_rad': float(rest[i]),
         'pair_mean_rotation_over_same_pair_static': float(rot[i:i+2].mean()/rest[i])}
        for i in range(0, len(rows), 2) if 1000 < w[i] < 3000
    ],
    'ribbon_rest_energy_J': U_rest,
    'one_near_source_GMm_over_r_J': GMm_over_r,
    'gravitational_energy_over_ribbon_energy': GMm_over_r / U_rest,
    'A4_radicand_with_table6_positive_energy': 4.90235e-13 / (-GMm_over_r),
    'stokes_equivalent_speed_m_s': stokes_speed,
    'test_sphere_Re_at_stokes_speed': stokes_speed * 2 * rp / 1.5e-5,
    'inviscid_freefall_temperature_K_not_a_cavity_prediction': freefall_dT,
    'Rayleigh_for_5cm_at_that_temperature': 9.81/295*freefall_dT*0.05**3/(1.5e-5*2.2e-5),
    'correct_clearance_m_if_p11_00325_is_rad': 0.00936 - 0.00325*arm,
    'free_quadratic_fit_abc': np.polyfit(w, rot, 2).tolist(),
    'refitted_zero_intercept_quadratic_coefficient_s2': float(np.dot(w*w, rot)/np.dot(w*w, w*w)),
    'amplitude_decay_time_s_from_Table5': 2*inertia/3.4e-8,
    'amplitude_remaining_after_3h_under_Table5_linear_model': math.exp(-10800/(2*inertia/3.4e-8)),
}

# Glenn: constants in the assessment; hypothetical uniform, isobaric gas heating.
def air_refractivity(wavelength_um):
    sigma2 = 1 / wavelength_um**2
    return (5792105/(238.0185-sigma2) + 167917/(57.362-sigma2))*1e-8
out['air_refractivity_ratio_532_650'] = air_refractivity(0.532)/air_refractivity(0.650)
out['150nm_double_pass_index_change_5mm'] = 150e-9/(2*0.005)
out['150nm_double_pass_linearized_heating_5mm_K'] = 150e-9/(2*0.005)/2.77e-4*295
out['150nm_double_pass_linearized_heating_20mm_K'] = 150e-9/(2*0.02)/2.77e-4*295
out['Glenn_velocity_SI_missing_normalization_factor_c_squared'] = c**2
print(json.dumps(out, indent=2))
