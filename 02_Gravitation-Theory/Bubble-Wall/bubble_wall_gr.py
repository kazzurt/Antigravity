"""Bubble wall in static weak-field general relativity.

Metric: ds^2 = -(1 + 2 Phi/c^2) c^2 dt^2 + (1 - 2 Psi/c^2) dx^2  (scalar part).
Static linearised Einstein equations with energy density rho and stress T_ij:

    lap Psi = 4 pi G rho                              (rulers: energy only)
    lap Phi = 4 pi G (rho + T_kk / c^2)               (clocks and slow masses)
    (delta_ij lap - d_i d_j)(Phi - Psi) = (8 pi G / c^2) T_ij

A static, self-supporting stress field obeys d_j T_ij = 0 to leading order and
can be written T_ij = (delta_ij lap - d_i d_j) S. Then Phi - Psi = (8 pi G/c^2) S.

Pure-stress wall (rho = 0):  S = b z chi(r), chi = 1 in the cabin, 0 outside,
b = -g0 c^2 / (8 pi G).  Then Phi_wall = -g0 z chi: Earth's pull is cancelled
in the cabin and nothing changes outside.  Stress components (theta from up):

    T_rr = 2 b chi' cos(theta)
    T_tt = T_pp = b (r chi'' + 3 chi') cos(theta)
    T_rt = b chi' sin(theta)

Ordinary-matter alternative: energy density rho = (sigma0/d)(1 + cos theta),
no significant stress: a lopsided massive shell.

Run:  python bubble_wall_gr.py   (writes fig4_gr_wall.png, results_gr.json)
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
g0 = 9.80665
R = 5.0
SIGMA0 = 3 * g0 / (4 * math.pi * G)
B = -g0 * c ** 2 / (8 * math.pi * G)          # Pa m
HERE = Path(__file__).parent


def chi_funcs(r, d):
    """Quintic smooth step from 1 (r <= R) to 0 (r >= R + d), with r-derivatives."""
    x = np.clip((r - R) / d, 0.0, 1.0)
    chi = 1 - (6 * x ** 5 - 15 * x ** 4 + 10 * x ** 3)
    dchi = -(30 * x ** 4 - 60 * x ** 3 + 30 * x ** 2) / d
    ddchi = -(120 * x ** 3 - 180 * x ** 2 + 60 * x) / d ** 2
    return chi, dchi, ddchi


def stress(r, d):
    """Radial amplitudes: T_rr = trr cos, T_tt = T_pp = ttt cos, T_rt = trt sin."""
    chi, dchi, ddchi = chi_funcs(r, d)
    return 2 * B * dchi, B * (r * ddchi + 3 * dchi), B * dchi, chi


def principal(trr, ttt, trt, ct, st):
    """Principal stresses of the (r, theta) block and the phi stress."""
    a, b_, o = trr * ct, ttt * ct, trt * st
    mean, rad = 0.5 * (a + b_), np.sqrt(0.25 * (a - b_) ** 2 + o ** 2)
    return mean + rad, mean - rad, ttt * ct


out = {"b_Pa_m": B, "sigma0_kg_m2": SIGMA0, "cases": {}}
THICK = [0.05, 0.1, 0.2, 0.5, 1.0, 2.5, 5.0]
theta = np.linspace(0, math.pi, 721)
CT, ST = np.cos(theta), np.sin(theta)
for d in THICK:
    n = 20001
    r = np.linspace(R, R + d, n)
    dr = r[1] - r[0]
    trr, ttt, trt, chi = stress(r, d)

    # 1. the stress field is self-supporting: both equilibrium equations vanish
    dtrr = np.gradient(trr, dr)
    dtrt = np.gradient(trt, dr)
    eq_r = dtrr + 2 * trr / r + 2 * trt / r - 2 * ttt / r          # coefficient of cos
    eq_t = dtrt + 3 * trt / r - ttt / r                            # coefficient of sin
    scale = np.max(np.abs(ttt)) / d
    assert np.max(np.abs(eq_r[5:-5])) < 2e-3 * scale
    assert np.max(np.abs(eq_t[5:-5])) < 2e-3 * scale

    # 2. active density f cos(theta) = T_kk / c^2 reproduces the quiet wall
    f = (trr + 2 * ttt) / c ** 2
    I0 = np.sum(0.5 * (f[1:] + f[:-1])) * dr
    I3 = np.sum(0.5 * ((f * r ** 3)[1:] + (f * r ** 3)[:-1])) * dr
    g_wall_inside = (4 * math.pi * G / 3) * I0          # upward field in the cabin
    assert abs(g_wall_inside / g0 - 1) < 1e-4
    assert abs((4 * math.pi * G / 3) * I3 / (g0 * R ** 3)) < 1e-4   # no exterior dipole

    # 3. energy conditions with rho = 0, and the density needed to restore them
    RR, _ = np.meshgrid(r, theta, indexing="ij")
    p1, p2, p3 = principal(trr[:, None], ttt[:, None], trt[:, None], CT[None, :], ST[None, :])
    pmax = np.maximum(np.abs(p1), np.maximum(np.abs(p2), np.abs(p3)))
    most_negative = min(p1.min(), p2.min(), p3.min())
    dth = theta[1] - theta[0]
    m_dec = 2 * math.pi * np.sum(pmax / c ** 2 * RR ** 2 * ST[None, :]) * dr * dth
    out["cases"][f"d{d}"] = {
        "peak_radial_stress_Pa": float(np.max(np.abs(trr))),
        "peak_tangential_stress_Pa": float(np.max(np.abs(ttt))),
        "peak_shear_stress_Pa": float(np.max(np.abs(trt))),
        "most_negative_principal_stress_Pa": float(most_negative),
        "benchmark_g0c2_over_8piGd_Pa": float(g0 * c ** 2 / (8 * math.pi * G * d)),
        "peak_field_in_wall_over_g0": float(np.max(np.abs(chi + r * chi_funcs(r, d)[1]))),
        "mass_needed_to_restore_dominant_energy_condition_kg": float(m_dec),
        "its_pull_at_10m_from_centre_over_g0": float(G * m_dec / 100.0 / g0),
    }

# checks against known numbers
c01 = out["cases"]["d0.1"]
assert abs(c01["benchmark_g0c2_over_8piGd_Pa"] - 5.25e27) / 5.25e27 < 0.01
assert c01["most_negative_principal_stress_Pa"] < 0          # null energy condition fails
assert 1.5 < c01["peak_radial_stress_Pa"] / (2 * c01["benchmark_g0c2_over_8piGd_Pa"]) < 2.0

# ordinary-matter lopsided shell
M_shell = 4 * math.pi * R ** 2 * SIGMA0
out["ordinary_matter_shell"] = {
    "mass_kg": M_shell,
    "field_just_above_top_over_g0": 6.0,
    "field_just_below_bottom_over_g0": 0.0,
    "pull_at_10m_above_centre_m_s2": G * M_shell / 100 + g0 * (1 + 2 * (R / 10) ** 3),
    "weight_of_shell_N": M_shell * g0,
}
assert abs(G * M_shell / R ** 2 / g0 - 3) < 1e-9

# ---- figure
fig, ax = plt.subplots(2, 2, figsize=(12, 9.5))
cols = {0.2: "C0", 1.0: "C2", 2.5: "C1"}
for d, col in cols.items():
    r = np.linspace(R - 0.5, R + d + 0.5, 4001)
    trr, ttt, trt, chi = stress(r, d)
    ax[0, 0].plot(r - R, trr, color=col, label=f"radial, d = {d} m")
    ax[0, 0].plot(r - R, ttt, "--", color=col, label=f"tangential, d = {d} m")
    ax[0, 1].plot(r - R, (g0 * r - g0 * r * chi) / (g0 * R), color=col, label=f"clock potential, d = {d} m")
ax[0, 0].set_yscale("symlog", linthresh=1e26)
ax[0, 0].set_xlabel("distance from inner wall face (m)")
ax[0, 0].set_ylabel("stress at the top of the bubble (Pa); positive = pressure")
ax[0, 0].set_title("Stress the wall must carry (energy density zero)")
ax[0, 0].legend(fontsize=7)
rr = np.linspace(R - 0.5, R + 3.0, 50)
ax[0, 1].plot(rr - R, rr / R, "k:", label="ruler potential (unchanged)")
ax[0, 1].set_xlabel("distance from inner wall face (m)")
ax[0, 1].set_ylabel("potential on the vertical axis / (g0 R)")
ax[0, 1].set_title("Clocks and rulers separate inside the bubble")
ax[0, 1].legend(fontsize=7)
ds = np.array(THICK)
ax[1, 0].loglog(ds, [out["cases"][f"d{d}"]["peak_tangential_stress_Pa"] for d in THICK], "o-", label="peak tangential")
ax[1, 0].loglog(ds, [out["cases"][f"d{d}"]["peak_radial_stress_Pa"] for d in THICK], "s-", label="peak radial")
ax[1, 0].loglog(ds, g0 * c ** 2 / (8 * math.pi * G * ds), "k:", label="g0 c² / (8πG d)")
ax[1, 0].set_xlabel("wall thickness d (m)"); ax[1, 0].set_ylabel("stress (Pa)")
ax[1, 0].set_title("Peak stress against thickness"); ax[1, 0].legend(fontsize=8)
ax[1, 1].loglog(ds, [out["cases"][f"d{d}"]["mass_needed_to_restore_dominant_energy_condition_kg"] for d in THICK], "o-", color="C3")
ax[1, 1].axhline(M_shell, color="k", ls=":", label="ordinary-matter lopsided shell")
ax[1, 1].set_xlabel("wall thickness d (m)"); ax[1, 1].set_ylabel("mass (kg)")
ax[1, 1].set_title("Mass needed to make the stressed wall obey the energy conditions")
ax[1, 1].legend(fontsize=8)
fig.suptitle("Bubble wall in weak-field general relativity, 5 m cabin, 1 g cancelled")
fig.tight_layout()
fig.savefig(HERE / "fig4_gr_wall.png", dpi=140)
(HERE / "results_gr.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
print("all assertions passed")
