"""Static, constrained planar bimetric Gate 0; all examples are synthetic.

Reproduce with Python 3.14 + NumPy/SciPy:
    python tensor_mode_transformer.py

This is the reduced static Fierz-Pauli source problem derived in the companion
report, NOT a transverse gravitational-wave calculation or a material model.
The gate is a prescribed positive mass-squared profile. The massless mode is
analytical and unchanged. JSON/CSV output is written beside this script.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import simpson, solve_bvp


OUT = Path(__file__).resolve().parent
G_REF = 6.67430e-11  # Synthetic choice G_infinity = CODATA G, not a parameter fit.
C_LIGHT = 299792458.0
HBAR_C_EV_M = 1.973269804593025e-7


def exact_slab(mu0: float, muwall: float, d: float) -> dict[str, float]:
    """Finite positive-mass barrier, matching field AND derivative.

    Incident field at z=0 is normalized to 1. D is field at z=d.
    R is the source-side reflected amplitude, not an energy reflectance.
    """
    if min(mu0, muwall) <= 0 or d < 0:
        raise ValueError("Masses must be positive; thickness nonnegative.")
    x = muwall * d
    den = 2 * mu0 * np.cosh(x) + (muwall + mu0**2 / muwall) * np.sinh(x)
    outgoing = 2 * mu0 / den
    reflected = (mu0**2 / muwall - muwall) * np.sinh(x) / den
    return {
        "outgoing": float(outgoing),
        "R": float(reflected),
        "Tm": float(outgoing * np.exp(mu0 * d)),
    }


def physical_response(alpha: float, mu0: float, d: float, a: float, b: float,
                      tm: float) -> dict[str, float]:
    epsilon = 4 * alpha**2 / 3
    r = epsilon * np.exp(-mu0 * (a + d + b))
    return {"epsilon": epsilon, "massive_to_massless_before": float(r),
            "physical_transfer": float((1 + r * tm) / (1 + r)),
            "massless_floor": float(1 / (1 + r))}


def smooth_profile(z: np.ndarray, mu0: float, muwall: float, d: float,
                   ramp: float) -> tuple[np.ndarray, np.ndarray]:
    """C1 sin-squared ramps, flat top; returns mu^2 and its derivative."""
    if not 0 < ramp <= d / 2:
        raise ValueError("ramp must lie in (0, d/2]")
    z = np.asarray(z)
    weight = np.ones_like(z)
    deriv = np.zeros_like(z)
    left = z < ramp
    right = z > d - ramp
    weight[left] = np.sin(np.pi * z[left] / (2 * ramp))**2
    deriv[left] = np.pi * np.sin(np.pi * z[left] / ramp) / (2 * ramp)
    weight[right] = np.sin(np.pi * (d - z[right]) / (2 * ramp))**2
    deriv[right] = -np.pi * np.sin(np.pi * (d - z[right]) / ramp) / (2 * ramp)
    delta = muwall**2 - mu0**2
    return mu0**2 + delta * weight, delta * deriv


def bvp_gate(mu0: float, muwall: float, d: float, ramp: float | None,
             nodes: int = 201, tol: float = 1e-9) -> dict:
    """Solve the derived static equations with source/outgoing Robin data."""
    z = np.linspace(0, d, nodes)

    def ode(x, y):
        m2 = (np.full_like(x, muwall**2) if ramp is None else
              smooth_profile(x, mu0, muwall, d, ramp)[0])
        return np.vstack((y[1], m2 * y[0]))

    def bc(yl, yr):
        return np.array([yl[1] - mu0 * yl[0] + 2 * mu0,
                         yr[1] + mu0 * yr[0]])

    guess = np.vstack((np.exp(-mu0 * z), -mu0 * np.exp(-mu0 * z)))
    sol = solve_bvp(ode, bc, z, guess, tol=tol, max_nodes=50000)
    if not sol.success:
        raise RuntimeError(sol.message)
    reflection = float(sol.sol(0)[0] - 1)
    outgoing = float(sol.sol(d)[0])
    # Dense off-mesh sampling checks the actual differential equation.
    checkz = np.linspace(0, d, 10007)
    y = sol.sol(checkz)
    yprime = sol.sol(checkz, 1)
    m2 = (np.full_like(checkz, muwall**2) if ramp is None else
          smooth_profile(checkz, mu0, muwall, d, ramp)[0])
    ode_residual = float(np.max(np.abs(yprime[1] - m2 * y[0])) /
                         max(1.0, np.max(np.abs(m2 * y[0]))))
    # Planar vacuum reconstruction: A=2B, C=0, trace=0.
    # G00=-B'', Gxx=(B''-A'')/2, Gzz=0. Include all nonzero equations.
    bfield, bsecond = y[0] / 2, yprime[1] / 2
    fp00 = -bsecond + m2 * (2 * bfield) / 2
    fpxx = -bsecond / 2 + m2 * bfield / 2
    constraint_scale = max(1.0, float(np.max(np.abs(m2 * bfield))))
    fp_residual = float(max(np.max(np.abs(fp00)), np.max(np.abs(fpxx))) /
                        constraint_scale)
    if ramp is None:
        force_integral = (muwall**2 - mu0**2) * (
            float(sol.sol(0)[0])**2 - outgoing**2)
    else:
        # Integrate each smooth segment separately so narrow ramps are resolved.
        force_integral = 0.0
        for lo, hi in [(0, ramp), (ramp, d - ramp), (d - ramp, d)]:
            if hi <= lo:
                continue
            zz = np.linspace(lo, hi, 4001)
            m2prime = smooth_profile(zz, mu0, muwall, d, ramp)[1]
            force_integral += float(simpson(m2prime * sol.sol(zz)[0]**2, x=zz))
    force_expected = -4 * mu0**2 * reflection
    force_error = abs(force_integral - force_expected) / max(1e-15, abs(force_expected))
    return {"R": reflection, "outgoing": outgoing,
            "Tm": outgoing * np.exp(mu0 * d), "nodes_final": int(sol.x.size),
            "ode_relative_residual": ode_residual,
            "fp_relative_residual": fp_residual,
            "force_integral": force_integral, "force_expected": force_expected,
            "force_relative_error": force_error,
            "max_boundary_residual": float(np.max(np.abs(bc(sol.sol(0), sol.sol(d)))))}


def source_constraint_check() -> dict[str, float]:
    """Independent manufactured smooth SOURCE check of every planar FP equation.

    Pick B(z), define rho=3/2*(mu^2 B - B''), Mg=1, then reconstruct A,C.
    This is an algebra/constraint test, not an observed source density profile.
    It specifically tests the nonzero source trace/contact component C.
    """
    z = np.linspace(-1, 1, 1001)
    b = np.exp(-z**2)
    bpp = (4 * z**2 - 2) * b
    m2 = 4 + 0.3 * np.sin(2 * z)
    rho = 1.5 * (m2 * b - bpp)
    a, c = 2 * b, 2 * rho / (3 * m2)
    trace = -a + 2 * b + c
    eq00 = -bpp + 0.5 * m2 * (2 * b + c) - rho
    eqxx = -0.5 * bpp + 0.5 * m2 * (a - b - c)
    eqzz = 0.5 * m2 * (a - 2 * b)
    # The variable-mass divergence is identically derivative of zero.
    divergence_primitive = m2 * (c - trace)
    trace_eq = -1.5 * m2 * trace + rho
    return {"minimum_manufactured_rho": float(np.min(rho)),
            "maximum_equation_residual": float(max(np.max(np.abs(v)) for v in
                [eq00, eqxx, eqzz, divergence_primitive, trace_eq]))}


def finite_source_check(mu0: float, muwall: float, d: float, a: float,
                        ramp: float = 0.01, halfwidth: float = 0.01) -> dict:
    """Solve a regular finite-density source AND smooth gate on one domain.

    rho_hat = cos^2(pi(z+a)/(2s))/s on |z+a|<s has unit integral.
    A''-mu^2 A=-rho_hat, so rho/Mg^2=3*rho_hat/4 and C=rho_hat/(2mu^2).
    Both outer Robin conditions are exact decaying-vacuum conditions.
    """
    left, right = -a - halfwidth - 0.1, d + 0.1

    def matter(x):
        value = np.zeros_like(x)
        inside = np.abs(x + a) < halfwidth
        value[inside] = np.cos(np.pi * (x[inside] + a) / (2 * halfwidth))**2 / halfwidth
        return value

    def mass2(x):
        value = np.full_like(x, mu0**2)
        inside = (x >= 0) & (x <= d)
        value[inside] = smooth_profile(x[inside], mu0, muwall, d, ramp)[0]
        return value

    def ode(x, y):
        return np.vstack((y[1], mass2(x) * y[0] - matter(x)))

    def bc(yl, yr):
        return np.array([yl[1] - mu0 * yl[0], yr[1] + mu0 * yr[0]])

    mesh = np.unique(np.concatenate((np.linspace(left, right, 701),
        np.array([-a-halfwidth, -a, -a+halfwidth, 0, ramp, d-ramp, d]))))
    guess = np.vstack((np.exp(-mu0*np.abs(mesh+a))/(2*mu0),
        -np.sign(mesh+a)*np.exp(-mu0*np.abs(mesh+a))/2))
    sol = solve_bvp(ode, bc, mesh, guess, tol=1e-9, max_nodes=50000)
    if not sol.success:
        raise RuntimeError(sol.message)
    x = mu0 * halfwidth
    form_factor = (np.sinh(x)/x) * np.pi**2 / (np.pi**2 + x*x)
    incident = np.exp(-mu0*a) * form_factor / (2*mu0)
    wall = bvp_gate(mu0, muwall, d, ramp)
    expected_right = incident * wall["outgoing"]
    error = abs(float(sol.sol(d)[0])/expected_right - 1)
    zz = np.linspace(left, right, 16001)
    ah, app = sol.sol(zz)[0], sol.sol(zz, 1)[1]
    bh, bpp = ah/2, app/2
    m2, rh = mass2(zz), matter(zz)
    ch = rh/(2*m2)
    fp00 = -bpp + m2*(2*bh+ch)/2 - 0.75*rh
    fpxx = -bpp/2 + m2*(bh-ch)/2
    residual = max(float(np.max(np.abs(fp00))), float(np.max(np.abs(fpxx))))
    residual /= max(1.0, float(np.max(rh)))
    assert error < 1e-8 and residual < 1e-7
    # SI contact-metric condition for the illustrative alpha=1, Sigma=100 case.
    rho_peak_si = 100/halfwidth
    g_g = 2 * G_REF
    c_peak = 16*np.pi*g_g*rho_peak_si/(3*C_LIGHT**2*mu0**2)
    return {"source_profile": "unit-integral compact cos-squared; smooth finite density",
        "halfwidth_m": halfwidth, "source_form_factor": float(form_factor),
        "source_peak_kg_m3_if_Sigma_100": rho_peak_si,
        "max_contact_C_if_alpha_1_Sigma_100": float(c_peak),
        "right_face_relative_error_vs_source_moment_and_wall": error,
        "reconstructed_FP_relative_residual": residual,
        "nodes_final": int(sol.x.size)}


def run() -> dict:
    mu0, d, a, b = 1.0, 0.1, 0.2, 0.2
    muwall = np.log(100) / d
    exact = exact_slab(mu0, muwall, d)
    numerical = bvp_gate(mu0, muwall, d, ramp=None)
    assert abs(numerical["Tm"] / exact["Tm"] - 1) < 1e-8
    assert abs(numerical["R"] - exact["R"]) < 1e-9
    assert numerical["force_relative_error"] < 1e-8
    assert numerical["fp_relative_residual"] < 1e-7

    limits = []
    for m in [0.01, 1.0, 30.0]:
        value = exact_slab(m, m, d)
        assert abs(value["Tm"] - 1) < 1e-12 and abs(value["R"]) < 1e-12
        limits.append({"check": "no_barrier", "mass_per_m": m, **value})
    zero_d = exact_slab(mu0, muwall, 0)
    assert zero_d["Tm"] == 1 and zero_d["R"] == 0
    assert physical_response(0, mu0, d, a, b, 0)["physical_transfer"] == 1
    far = physical_response(1, mu0, d, 30, b, 0)
    assert abs(far["physical_transfer"] - 1) < 1e-12

    # Constant-mass BVP accuracy under tighter tolerances/initial meshes.
    convergence = []
    for nodes, tol in [(21, 1e-5), (41, 1e-7), (81, 1e-9)]:
        row = bvp_gate(mu0, muwall, d, None, nodes=nodes, tol=tol)
        row.update({"nodes_initial": nodes, "tol": tol,
                    "Tm_relative_error": abs(row["Tm"] / exact["Tm"] - 1)})
        convergence.append(row)
    assert convergence[-1]["Tm_relative_error"] < convergence[0]["Tm_relative_error"]

    # Physical smooth gates approach the finite-step analytic solution.
    smooth = []
    for fraction in [0.25, 0.1, 0.04, 0.01]:
        row = bvp_gate(mu0, muwall, d, d * fraction)
        row.update({"ramp_fraction": fraction, "ramp_m": d * fraction,
                    "distance_from_sharp_Tm": abs(row["Tm"] - exact["Tm"])})
        assert row["force_relative_error"] < 1e-7
        assert row["fp_relative_residual"] < 1e-7
        smooth.append(row)
    assert all(smooth[i + 1]["distance_from_sharp_Tm"] <
               smooth[i]["distance_from_sharp_Tm"] for i in range(len(smooth)-1))

    rows = []
    for alpha in [0.1, 1, 10]:
        for source_gap in [a, 5, 20]:
            response = physical_response(alpha, mu0, d, source_gap, b, exact["Tm"])
            assert response["massless_floor"] <= response["physical_transfer"] <= 1
            rows.append({"alpha": alpha, "source_gap_m": source_gap,
                         "detector_gap_m": b, "Tm": exact["Tm"], **response})

    # Force/stress/recoil reference, per unit area; no finite craft is inferred.
    alpha, sigma = 1.0, 100.0
    gy = G_REF * 4 * alpha**2 / 3
    incident_phi = -2 * np.pi * gy * sigma / mu0 * np.exp(-mu0 * a)
    source_force = 2 * np.pi * gy * sigma**2 * exact["R"] * np.exp(-2 * mu0 * a)
    gate_force = incident_phi**2 / (8 * np.pi * gy) * numerical["force_integral"]
    assert abs((gate_force + source_force) / source_force) < 1e-8
    g_common = 2 * np.pi * G_REF * sigma
    response = physical_response(alpha, mu0, d, a, b, exact["Tm"])
    sourced = source_constraint_check()
    assert sourced["maximum_equation_residual"] < 1e-12
    regular_source = finite_source_check(mu0, muwall, d, a)
    result = {
        "status": "All assertions passed; conditional prescribed-profile calculation only.",
        "numpy": np.__version__, "scipy": scipy.__version__,
        "reference": {"mu_out_per_m": mu0, "mu_wall_per_m": muwall,
                      "mu_wall_energy_eV": muwall * HBAR_C_EV_M,
                      "wall_m": d, "source_gap_m": a, "detector_gap_m": b,
                      "surface_density_kg_m2": sigma,
                      "G_infinity_synthetic": G_REF,
                      "common_acceleration_m_s2": g_common,
                      "before_acceleration_m_s2": g_common * (1 + response["massive_to_massless_before"]),
                      "after_acceleration_m_s2": g_common * (1 + response["massive_to_massless_before"] * exact["Tm"]),
                      "source_force_N_m2": source_force, "gate_force_N_m2": gate_force,
                      "gate_support_force_N_m2": -gate_force,
                      "source_support_force_N_m2": -source_force,
                      "force_ledger_relative_error": abs((gate_force + source_force) / source_force)},
        "exact_step_slab": exact, "independent_bvp": numerical,
        "source_constraint_check": sourced, "limits": limits,
        "finite_source_and_smooth_gate": regular_source,
        "bvp_convergence": convergence, "smooth_to_step": smooth,
        "physical_transfers": rows,
    }
    (OUT / "results.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    with (OUT / "physical_transfers.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({"status": result["status"], "reference": result["reference"],
                      "exact_step_slab": exact, "physical_transfers": rows,
                      "bvp_convergence": convergence, "smooth_to_step": smooth}, indent=2))
    return result


if __name__ == "__main__":
    run()
