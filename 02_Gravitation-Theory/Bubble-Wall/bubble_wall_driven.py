"""Driven (time-periodic) bubble wall: what it can and cannot do.

Argument (weak-field general relativity, harmonic gauge):

  box hbar_mu_nu = -(16 pi G / c^4) T_mu_nu .

For a source that repeats with period P, averaging over P removes the time
derivatives, so the AVERAGED metric obeys the STATIC equations with the
AVERAGED source.  Local conservation gives d_j <T_ij> = 0: the averaged stress
is self-supporting.  Everything proved for the static wall therefore holds for
the averages of a driven wall.

Bound.  The upward pull at the cabin centre from the wall is

    g = G * integral of rho_active * cos(theta) / r^2  dV ,
    rho_active = rho + T_kk / c^2 .

The wall lies at r >= R, so cos(theta)/r^2 <= 1/R^2.  If the wall's matter
obeys the dominant energy condition, |stress| <= rho c^2, so
rho_active <= 4 rho.  Radiation and moving particles have T_kk <= rho c^2
(rho_active <= 2 rho); cold matter has rho_active = rho.  Hence, to cancel g0,

    M >= g0 R^2 / (k G),   k = 4 (energy-condition limit), 2 (radiation), 1 (cold matter),

for a static or a driven wall alike.  The outside then feels at least
G M / r^2 = g0 (R/r)^2 / k at distance r from the centre.

Run:  python bubble_wall_driven.py   (writes fig5_driven_wall.png, results_driven.json)
"""

import json
import math
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

G = 6.67430e-11
c = 299792458.0
hbar = 1.054571817e-34
mu0 = 4 * math.pi * 1e-7
g0 = 9.80665
R = 5.0
HERE = Path(__file__).parent
E_SCHWINGER = 1.32e18            # V/m, critical field for pair creation


def m_min(radius, k):
    return g0 * radius ** 2 / (k * G)


out = {}
for name, k in (("energy_condition_limit", 4), ("radiation_or_moving_particles", 2), ("cold_matter", 1)):
    M = m_min(R, k)
    out[name] = {
        "k": k,
        "min_mass_kg": M,
        "min_energy_J": M * c ** 2,
        "min_outside_pull_at_10m_m_s2": G * M / 10.0 ** 2,
        "min_outside_pull_at_100m_m_s2": G * M / 100.0 ** 2,
    }
assert abs(out["energy_condition_limit"]["min_mass_kg"] - 9.19e11) / 9.19e11 < 0.01
assert abs(out["energy_condition_limit"]["min_outside_pull_at_10m_m_s2"] - g0 / 16) < 1e-9

# numerical check of the kernel bound against the stage-1 screen wall:
# thin lopsided shell, rho = sigma0 (1 + cos) on r = R, cold matter.
sigma0 = 3 * g0 / (4 * math.pi * G)
th = np.linspace(0, math.pi, 20001)
dth = th[1] - th[0]
g_centre = G * np.sum(sigma0 * (1 + np.cos(th)) * np.cos(th) * 2 * math.pi * np.sin(th)) * dth
M_shell = 4 * math.pi * R ** 2 * sigma0
assert abs(g_centre / g0 - 1) < 1e-4                 # it does cancel g0
assert M_shell >= m_min(R, 1)                        # and respects the bound (3x above it)
out["lopsided_shell_over_cold_bound"] = M_shell / m_min(R, 1)

# a wave-filled wall: radiation trapped in R < r < R + d
wave = {}
for d in (0.2, 1.0, 5.0):
    V = 4 / 3 * math.pi * ((R + d) ** 3 - R ** 3)
    u = m_min(R, 2) * c ** 2 / V                     # J/m^3, minimum
    Brms = math.sqrt(mu0 * u)
    wave[f"d{d}"] = {"energy_density_J_m3": u, "B_rms_T": Brms, "E_rms_V_m": c * Brms,
                     "E_over_schwinger": c * Brms / E_SCHWINGER}
out["wave_filled_wall"] = wave
assert wave["d1.0"]["E_over_schwinger"] > 1          # beyond vacuum breakdown

# negative energy: how long quantum field theory lets it last.
# Ford-Roman type bound for a massless field, sampling time tau:
#   |negative energy density| <= 3 hbar / (32 pi^2 c^3 tau^4)
def tau_max(u_neg):
    return (3 * hbar / (32 * math.pi ** 2 * c ** 3 * u_neg)) ** 0.25

out["negative_energy_duration_s"] = {f"{u:.0e}_Pa": tau_max(u) for u in (1e27, 1e28, 1e30)}
assert 1e-23 < tau_max(1e27) < 1e-21

# side effects of driving
def gw_power(M, eps, omega):                         # order of magnitude
    return G * (eps * M * R ** 2) ** 2 * omega ** 6 / c ** 5

def ponderomotive(g_osc, omega):                     # secular push on occupants
    return g_osc ** 2 / (omega ** 2 * R)

M2 = m_min(R, 2)
out["driving_side_effects"] = {
    "gw_power_W_at_1kHz_10pct_modulation": gw_power(M2, 0.1, 2 * math.pi * 1e3),
    "gw_power_W_at_1MHz_10pct_modulation": gw_power(M2, 0.1, 2 * math.pi * 1e6),
    "ponderomotive_over_g0_at_1Hz_for_1g_oscillation": ponderomotive(g0, 2 * math.pi) / g0,
    "ponderomotive_over_g0_at_1kHz_for_1g_oscillation": ponderomotive(g0, 2 * math.pi * 1e3) / g0,
}

# ---- figure
fig, ax = plt.subplots(2, 2, figsize=(12, 9.5))
rad = np.logspace(-1, 2, 100)
for k, lab in ((1, "cold matter"), (2, "radiation or moving particles"), (4, "energy-condition limit")):
    ax[0, 0].loglog(rad, m_min(rad, k), label=lab)
ax[0, 0].axvline(R, color="0.6", lw=0.8)
ax[0, 0].set_xlabel("cabin radius R (m)"); ax[0, 0].set_ylabel("minimum mass-energy of the wall (kg)")
ax[0, 0].set_title("Least mass-energy to cancel 1 g, static or driven"); ax[0, 0].legend(fontsize=8)

dist = np.logspace(math.log10(R), 5, 200)
for k, lab in ((1, "cold matter"), (4, "energy-condition limit")):
    ax[0, 1].loglog(dist, g0 * (R / dist) ** 2 / k, label=lab)
ax[0, 1].axhline(1e-9, color="k", ls=":", label="superconducting gravimeter, roughly")
ax[0, 1].set_xlabel("distance from bubble centre (m)"); ax[0, 1].set_ylabel("least pull on surroundings (m/s²)")
ax[0, 1].set_title("How loud the outside must be (5 m cabin)"); ax[0, 1].legend(fontsize=8)

dd = np.logspace(-2, 1.3, 100)
VV = 4 / 3 * math.pi * ((R + dd) ** 3 - R ** 3)
EE = c * np.sqrt(mu0 * m_min(R, 2) * c ** 2 / VV)
ax[1, 0].loglog(dd, EE, label="wave field needed")
ax[1, 0].axhline(E_SCHWINGER, color="r", ls="--", label="vacuum breaks down into particle pairs")
ax[1, 0].set_xlabel("wall thickness d (m)"); ax[1, 0].set_ylabel("electric field of the wave (V/m)")
ax[1, 0].set_title("A wall made of trapped waves"); ax[1, 0].legend(fontsize=8)

uu = np.logspace(20, 31, 100)
ax[1, 1].loglog(uu, [tau_max(u) for u in uu])
ax[1, 1].axvspan(1e27, 6e30, color="C1", alpha=0.25, label="tension the quiet wall needs")
ax[1, 1].set_xlabel("negative energy density (J/m³)"); ax[1, 1].set_ylabel("longest it can last (s)")
ax[1, 1].set_title("Quantum limit on negative energy"); ax[1, 1].legend(fontsize=8)
fig.suptitle("Driven bubble wall: bounds that hold for any periodic drive")
fig.tight_layout()
fig.savefig(HERE / "fig5_driven_wall.png", dpi=140)
(HERE / "results_driven.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
print("all assertions passed")
