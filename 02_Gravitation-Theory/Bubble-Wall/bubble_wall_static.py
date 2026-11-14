"""Static bubble-wall models in a uniform external gravitational field.

Weak-field (Newtonian / gravitoelectromagnetic) treatment. A spherical cabin
of inner radius R sits in Earth's field g_ext = -g0 z. A wall occupying
R < r < R + d carries an effective mass density rho = f(r) cos(theta).
Because the source is pure l = 1, the shell potential is exactly

    Phi_shell(r, theta) = phi(r) cos(theta)
    phi(r)  = -(4 pi G / 3) [ r I0(r) + r^-2 I3(r) ]
    phi'(r) = -(4 pi G / 3) [ I0(r) - 2 r^-3 I3(r) ]
    I0(r) = int_r^inf f dr',   I3(r) = int_0^r f r'^3 dr'

for ANY radial profile f. Total field: Phi = (g0 r + phi) cos(theta),
g_r = -(g0 + phi') cos(theta), g_theta = (g0 + phi / r) sin(theta).

Two wall models:
  A "screen": single layer, int f dr = sigma0 = 3 g0 / (4 pi G). Interior
     field is zero; the exterior is disturbed by a dipole (3 g0 at the poles).
  B "quiet":  inner and outer sub-layers of opposite sign chosen so that
     int f dr = sigma0 and int f r^3 dr = 0. Interior field is zero AND the
     exterior is undisturbed; the potential steps across the wall.

Gravitomagnetic field (convention: force = m (g + v x B_g),
curl B_g = -(16 pi G / c^2) J):
  translating bubble, velocity v:  B_g = -(4 / c^2) v x g_shell
  rotating bubble, rate Omega about z:  A_phi = a(r) sin(theta) cos(theta),
     a(r) = -(k Omega / 5) [ r^-3 int_0^r f r'^5 dr' + r^2 int_r^inf f dr' ],
     k = 16 pi G / c^2.

Run:  python bubble_wall_static.py     (writes figures, CSV and results.json)
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
R = 5.0                      # cabin inner radius, m
SIGMA0 = 3 * g0 / (4 * math.pi * G)
HERE = Path(__file__).parent
RMAX = 6 * R
N = 240001
r = np.linspace(0.0, RMAX, N)
dr = r[1] - r[0]


def window(lo, hi, smooth):
    """Unit-area radial window on [lo, hi]: top-hat or raised cosine."""
    w = np.zeros_like(r)
    m = (r >= lo) & (r <= hi)
    if smooth:
        x = (r[m] - lo) / (hi - lo)
        w[m] = 1 - np.cos(2 * np.pi * x)
    else:
        w[m] = 1.0
    return w / (np.sum(w) * dr)


def profile(model, d, smooth):
    if model == "A":
        return SIGMA0 * window(R, R + d, smooth)
    w1 = window(R, R + d / 2, smooth)
    w2 = window(R + d / 2, R + d, smooth)
    m1 = np.sum(w1 * r ** 3) * dr
    m2 = np.sum(w2 * r ** 3) * dr
    # alpha + beta = sigma0 ; alpha m1 + beta m2 = 0
    alpha = SIGMA0 * m2 / (m2 - m1)
    beta = SIGMA0 - alpha
    return alpha * w1 + beta * w2


def cumint(y):
    out = np.zeros_like(y)
    out[1:] = np.cumsum(0.5 * (y[1:] + y[:-1])) * dr
    return out


def solve(f):
    c0 = cumint(f)
    I0 = c0[-1] - c0
    I3 = cumint(f * r ** 3)
    I5 = cumint(f * r ** 5)
    rs = np.where(r > 0, r, 1.0)
    k3 = 4 * math.pi * G / 3
    phi = -k3 * (r * I0 + I3 / rs ** 2)
    dphi = -k3 * (I0 - 2 * I3 / rs ** 3)
    a_rot = -(1 / 5) * (I5 / rs ** 3 + r ** 2 * I0)   # times k * Omega
    return {"phi": phi, "dphi": dphi, "a_rot": a_rot, "I0": I0, "I3": I3}


def fields_on_grid(sol, X, Z):
    """Total gravitoelectric field (gx, gz)/g0 and shell-only field on a
    meridional grid (y = 0)."""
    rr = np.hypot(X, Z)
    rr = np.where(rr < 1e-9, 1e-9, rr)
    ct, st = Z / rr, X / rr
    phi = np.interp(rr, r, sol["phi"])
    dphi = np.interp(rr, r, sol["dphi"])
    gs_r, gs_t = -dphi * ct, (phi / rr) * st          # shell only
    gt_r, gt_t = gs_r - g0 * ct, gs_t + g0 * st       # plus Earth
    def cart(vr, vt):
        return (vr * st + vt * ct) / g0, (vr * ct - vt * st) / g0
    return cart(gt_r, gt_t), cart(gs_r, gs_t)


out = {"R_m": R, "g0": g0, "sigma0_kg_m2": SIGMA0, "cases": {}}
THICK = [0.05, 0.2, 1.0, 2.5]
sols = {}
for model in "AB":
    for d in THICK:
        for smooth in (False, True):
            f = profile(model, d, smooth)
            s = solve(f)
            s["f"] = f
            sols[(model, d, smooth)] = s
            i_in = np.searchsorted(r, 0.5 * R)
            i_out = np.searchsorted(r, R + d + 1e-6) + 1
            g_axis = -(g0 + s["dphi"]) / g0            # g_r/g0 at theta = 0
            inventory = 2 * math.pi * np.sum(np.abs(f) * r ** 2) * dr
            out["cases"][f"{model}_d{d}_{'smooth' if smooth else 'tophat'}"] = {
                "interior_g_over_g0_on_axis": float(g_axis[i_in]),
                "g_over_g0_just_outside_pole": float(g_axis[i_out]),
                "exterior_dipole_coefficient_over_g0R3": float(
                    (4 * math.pi * G / 3) * s["I3"][-1] / (g0 * R ** 3)),
                "potential_step_over_g0R": float(
                    (g0 * r[i_out] + s["phi"][i_out]) / (g0 * R)),
                "peak_abs_density_kg_m3": float(np.max(np.abs(f))),
                "absolute_mass_inventory_kg": float(inventory),
            }

# ---- checks
for d in THICK:
    for smooth in (False, True):
        a = out["cases"][f"A_d{d}_{'smooth' if smooth else 'tophat'}"]
        b = out["cases"][f"B_d{d}_{'smooth' if smooth else 'tophat'}"]
        assert abs(a["interior_g_over_g0_on_axis"]) < 1e-3
        assert abs(b["interior_g_over_g0_on_axis"]) < 1e-3
        assert abs(b["exterior_dipole_coefficient_over_g0R3"]) < 1e-6
        assert abs(b["g_over_g0_just_outside_pole"] + 1) < 2e-3   # undisturbed
thin = out["cases"]["A_d0.05_tophat"]
assert abs(thin["g_over_g0_just_outside_pole"] + 3) < 0.1          # -3 g0
assert abs(thin["exterior_dipole_coefficient_over_g0R3"] - 1) < 0.05
assert abs(SIGMA0 - 3.51e10) / 3.51e10 < 0.01
inv_b = out["cases"]["B_d0.2_tophat"]["absolute_mass_inventory_kg"]

# gravitomagnetic scales
v = 300.0
out["gravitomagnetic"] = {
    "translating_interior_Bg_per_s_at_v300": 4 * v * g0 / c ** 2,
    "rotating_Bg_scale_per_s_at_OmegaR_10": (24 / 5) * g0 * 10.0 / c ** 2,
    "earth_frame_dragging_scale_per_s": G * 5.86e33 / (c ** 2 * 6.371e6 ** 3),
    "lapse_step_g0R_over_c2": g0 * R / c ** 2,
}

# ---- figure 1: line charts across the wall, on the polar axis
fig, ax = plt.subplots(3, 2, figsize=(11, 11), sharex="col")
cols = plt.cm.viridis(np.linspace(0.1, 0.85, len(THICK)))
for j, model in enumerate("AB"):
    for d, col in zip(THICK, cols):
        for smooth, ls in ((False, "-"), (True, "--")):
            s = sols[(model, d, smooth)]
            m = (r > R - 1.5) & (r < R + 4.5)
            lab = f"d = {d} m" if not smooth else None
            ax[0, j].plot(r[m] - R, -(g0 + s["dphi"][m]) / g0, ls, color=col, label=lab)
            ax[1, j].plot(r[m] - R, (g0 * r[m] + s["phi"][m]) / (g0 * R), ls, color=col)
            ax[2, j].plot(r[m] - R, s["f"][m] / SIGMA0, ls, color=col)
    ax[0, j].set_title(("Model A: screen (single layer)", "Model B: quiet (paired layers)")[j])
    ax[0, j].axhline(-1, color="0.6", lw=0.8)
    ax[0, j].axhline(0, color="0.6", lw=0.8)
    ax[2, j].set_xlabel("distance from inner wall face, r - R (m)")
ax[0, 0].set_ylabel("radial field on polar axis, g_r / g0")
ax[1, 0].set_ylabel("potential on polar axis, Phi / (g0 R)")
ax[2, 0].set_ylabel("wall density profile f / sigma0 (1/m)")
ax[2, 1].set_yscale("symlog", linthresh=1)
ax[0, 1].set_yscale("symlog", linthresh=1)
ax[0, 0].legend(title="solid: top-hat, dashed: smooth", fontsize=8)
fig.suptitle("Field, potential and source across the bubble wall (top of bubble)")
fig.tight_layout()
fig.savefig(HERE / "fig1_wall_line_profiles.png", dpi=140)
plt.close(fig)

# ---- figure 2: meridional field maps
x = np.linspace(-3 * R, 3 * R, 361)
z = np.linspace(-3 * R, 3 * R, 361)
X, Z = np.meshgrid(x, z)
panels = [("A", 0.2, False, "A: screen, d = 0.2 m"),
          ("A", 2.5, True, "A: screen, d = 2.5 m, smooth"),
          ("B", 1.0, False, "B: quiet, d = 1.0 m")]
fig, ax = plt.subplots(1, 3, figsize=(16, 5.6))
for a, (model, d, smooth, title) in zip(ax, panels):
    (gx, gz), _ = fields_on_grid(sols[(model, d, smooth)], X, Z)
    mag = np.hypot(gx, gz)
    im = a.pcolormesh(X, Z, mag, shading="auto", cmap="magma", vmin=0, vmax=3)
    quiet = mag < 0.03                      # do not draw lines where the field is cancelled
    seeds = np.column_stack([np.linspace(-2.9 * R, 2.9 * R, 41), np.full(41, 2.9 * R)])
    a.streamplot(x, z, np.ma.masked_where(quiet, gx), np.ma.masked_where(quiet, gz),
                 color="w", linewidth=0.6, arrowsize=0.7, start_points=seeds,
                 broken_streamlines=False)
    a.set_xlim(x[0], x[-1]); a.set_ylim(z[0], z[-1])
    for rad in (R, R + d):
        a.add_patch(plt.Circle((0, 0), rad, fill=False, color="cyan", lw=0.8))
    a.set_aspect("equal"); a.set_title(title); a.set_xlabel("x (m)")
ax[0].set_ylabel("z (m), up")
fig.colorbar(im, ax=ax, label="|g| / g0", shrink=0.85)
fig.suptitle("Gravitoelectric field around a 5 m bubble in Earth's field (field lines white)")
fig.savefig(HERE / "fig2_gravitoelectric_maps.png", dpi=140, bbox_inches="tight")
plt.close(fig)

# ---- figure 3: gravitomagnetic field
fig, ax = plt.subplots(1, 3, figsize=(16, 5.2))
for a, (model, d, smooth, title) in zip(ax[:2], [panels[0], panels[2]]):
    _, (sx, sz) = fields_on_grid(sols[(model, d, smooth)], X, Z)
    # v = v xhat ; B = -(4/c^2) v x g_shell ; in the x-z plane B points along y
    By = sz                                   # B_y / (4 v g0 / c^2) = +g_shell,z / g0
    im = a.pcolormesh(X, Z, By, shading="auto", cmap="RdBu_r", vmin=-2, vmax=2)
    for rad in (R, R + d):
        a.add_patch(plt.Circle((0, 0), rad, fill=False, color="k", lw=0.8))
    a.set_aspect("equal"); a.set_xlabel("x (m), direction of travel")
    a.set_title("Translating bubble, " + title)
ax[0].set_ylabel("z (m), up")
fig.colorbar(im, ax=ax[:2], label="B_g,y / (4 v g0 / c^2)", shrink=0.85)
for model, d, smooth, col in (("A", 0.2, False, "C0"), ("A", 2.5, True, "C1"), ("B", 1.0, False, "C2")):
    s = sols[(model, d, smooth)]
    m = (r > 0.02) & (r < 3 * R)
    ax[2].plot(r[m], 2 * s["a_rot"][m] / r[m] / (SIGMA0 * R) * (5 / 2), color=col,
               label=f"{model}, d = {d} m")
ax[2].set_xlabel("r along spin axis (m)")
ax[2].set_ylabel("B_g,z on axis / peak thin-shell value")
ax[2].set_title("Rotating bubble: frame-dragging field on the axis")
ax[2].axvline(R, color="0.6", lw=0.8); ax[2].legend(fontsize=8)
fig.suptitle("Gravitomagnetic (frame-dragging) field produced by the wall's moving mass")
fig.savefig(HERE / "fig3_gravitomagnetic.png", dpi=140, bbox_inches="tight")
plt.close(fig)

# ---- line data
rows = ["r_minus_R_m,model,d_m,profile,g_r_over_g0_axis,Phi_over_g0R_axis,g_tan_over_g0_equator"]
for (model, d, smooth), s in sols.items():
    m = (r > R - 1.5) & (r < R + 4.5)
    step = max(1, int(0.01 / dr))
    for ri, gp, ph in zip(r[m][::step], s["dphi"][m][::step], s["phi"][m][::step]):
        rows.append(f"{ri - R:.3f},{model},{d},{'smooth' if smooth else 'tophat'},"
                    f"{-(g0 + gp) / g0:.6f},{(g0 * ri + ph) / (g0 * R):.6f},{(g0 + ph / ri) / g0:.6f}")
(HERE / "wall_line_profiles.csv").write_text("\n".join(rows), encoding="utf-8")
(HERE / "results.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
print("all assertions passed; inventory B d=0.2:", f"{inv_b:.3e}", "kg")
