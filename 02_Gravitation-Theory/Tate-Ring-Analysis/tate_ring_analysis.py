"""Finite-ring mapping of a specified London stiffness kernel.

All annulus dimensions and sensitivity budgets below are SYNTHETIC.
This is an analytic/numerical verification, not an empirical Tate fit.
Run with Python, NumPy and SciPy; writes results beside this script.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np
from scipy.linalg import solve
from scipy.special import ellipk, ellipe

H = 6.62607015e-34  # SI exact
E = 1.602176634e-19  # SI exact
MU0 = 1.25663706127e-6
ME = 9.1093837139e-31
MS = 2 * ME
QS = -2 * E
OUT = Path(__file__).resolve().parent


def kernel(R, charge_to_mass, masses, winding):
    """Return D, bulk K, and winding-source flux Psi in SI."""
    R, Q = np.asarray(R, float), np.asarray(charge_to_mass, float)
    masses, winding = np.asarray(masses, float), np.asarray(winding, float)
    if not np.allclose(R, R.T) or np.linalg.eigvalsh(R).min() <= 0:
        raise ValueError("Stiffness must be symmetric positive definite")
    D = float(Q @ R @ Q)
    if D <= 0:
        raise ValueError("At least one component must be charged")
    K = float(Q @ R @ np.ones(len(Q)) / D)
    psi = float(Q @ R @ (H * winding / masses) / D)
    return D, K, psi


def spacing_mass(R, Q, masses, winding_step):
    """Signed branch-spacing coefficient h K / DeltaPsi; undefined at DeltaPsi=0."""
    _, K, delta_psi = kernel(R, Q, masses, winding_step)
    if delta_psi == 0:
        raise ValueError("This winding step has no magnetic spacing")
    return H * K / delta_psi


def mutual_loop(a, b, z=0.0):
    """Coaxial filament mutual inductance from the Neumann integral.

    Distinct loops only; complete elliptic integrals use parameter m=k^2.
    """
    a, b, z = np.asarray(a), np.asarray(b), np.asarray(z)
    parameter = 4*a*b / ((a+b)**2 + z*z)
    if np.any(parameter >= 1):
        raise ValueError("Coincident filament singularity needs a self term")
    return MU0*np.sqrt(a*b)*((2-parameter)*ellipk(parameter)-2*ellipe(parameter))/np.sqrt(parameter)


def annulus_operator(radius, width, thickness, penetration, pickup_radius, pickup_z, cells):
    """Thin-film axisymmetric strip quadrature, constant lambda and stiffness ratios.

    Approximation: t << lambda, dr << r, w << r. Current is uniform through t.
    L_ii uses geometric mean distance exp(-3/2)*dr of a zero-thickness strip.
    Off diagonal terms use midpoint filaments with cell-averaged leading-log
    singularity correction. Mesh refinement is reported.
    """
    dr = width/cells
    radii = radius-width/2+(np.arange(cells)+0.5)*dr
    Lg = np.zeros((cells, cells))
    def log_primitive(value):
        return 0.0 if value == 0 else .5*value*value*np.log(abs(value))-.75*value*value
    for i in range(cells):
        for j in range(i):
            offset = i-j
            average_log = log_primitive(offset+1)-2*log_primitive(offset)+log_primitive(offset-1)
            correction = MU0*np.sqrt(radii[i]*radii[j])*(np.log(offset)-average_log)
            Lg[i,j] = Lg[j,i] = mutual_loop(radii[i], radii[j])+correction
        gmd = np.exp(-1.5)*dr
        Lg[i,i] = MU0*radii[i]*(np.log(8*radii[i]/gmd)-2)
    Lk = MU0*penetration**2 * 2*np.pi*radii / (thickness*dr)
    L = Lg+np.diag(Lk)
    areas = np.pi*radii**2
    pickup = mutual_loop(pickup_radius, radii, pickup_z)
    weights = solve(L, pickup, assume_a="pos")  # reciprocity L = L^T
    U = float(weights @ np.ones(cells))
    V = float(weights @ areas)
    return dict(L=L, radii=radii, areas=areas, pickup=pickup,
                U=U, V=V, area_effective=V/U,
                min_eigenvalue=float(np.linalg.eigvalsh(L).min()))


def fit_zero_sequence(indices, frequencies, covariance):
    """Generalized least squares nu_n = intercept + spacing*n."""
    X = np.column_stack([np.ones(len(indices)), indices])
    ci_x = solve(covariance, X, assume_a="pos")
    ci_y = solve(covariance, frequencies, assume_a="pos")
    pcov = np.linalg.inv(X.T @ ci_x)
    estimate = pcov @ X.T @ ci_y
    return estimate, pcov


def verify():
    checks = []
    qom = QS/MS
    # 1. Single-component circulation, sign, and cyclic/angular factor.
    D, K, psi = kernel([[3.2]], [qom], [MS], [1])
    np.testing.assert_allclose(K, MS/QS, rtol=2e-15)
    np.testing.assert_allclose(psi, H/QS, rtol=2e-15)
    area = np.pi*0.01**2
    delta_omega = psi/(2*K*area)
    delta_nu = delta_omega/(2*np.pi)
    np.testing.assert_allclose(H/(4*np.pi*area*delta_nu), MS, rtol=2e-15)
    # Arbitrary positive inductance changes amplitude, never zero in a single loop.
    for inductance in [1e-10, 1e-8, 1e-6]:
        for winding in [-3, 0, 4]:
            root = winding*psi/(2*K*area)
            residual = (winding*psi-2*K*root*area)/inductance
            assert abs(residual) < 1e-18
    checks.append("one-component fluxoid, frequency normalization and inductance-independent narrow-loop zeros")

    # 2. Neutral winding and the conditional x inversion.
    x, r, mchi = 92e-6, 2e-3, 20*MS
    R = np.array([[1, x], [x, r]])
    D, Kn, psi_s = kernel(R, [qom, 0], [MS, mchi], [1, 0])
    _, _, psi_chi = kernel(R, [qom, 0], [MS, mchi], [0, 1])
    np.testing.assert_allclose(Kn/(MS/QS), 1+x, rtol=2e-15)
    np.testing.assert_allclose(psi_s, H/QS, rtol=2e-15)
    np.testing.assert_allclose(psi_chi/psi_s, x*MS/mchi, rtol=2e-15)
    np.testing.assert_allclose(spacing_mass(R, [qom,0], [MS,mchi], [1,0])/MS, 1+x, rtol=2e-15)
    # If the neutral phase follows the same circulation increment (here an
    # exactly commensurate synthetic mass ratio), the apparent shift cancels.
    np.testing.assert_allclose(spacing_mass(R, [qom,0], [MS,mchi], [1,20])/MS, 1, rtol=2e-15)
    checks.append("neutral fixed-winding branch retains m_spacing/m_s = 1+x")

    # 3. General charged branch is NOT the bulk-field coefficient.
    rng = np.random.default_rng(6112026)
    for _ in range(200):
        x = rng.uniform(-0.02, 0.02)
        r = x*x+rng.uniform(0.001, 0.1)
        y = rng.uniform(-0.3, 0.3)
        R = np.array([[1,x],[x,r]])
        value = spacing_mass(R, [qom,qom*y], [MS,20*MS], [1,0])/MS
        exact = (1+x+y*(x+r))/(1+x*y)
        np.testing.assert_allclose(value, exact, rtol=3e-15)
    checks.append("200 positive-stiffness charged examples verify winding-spacing denominator 1+xy")

    # 4. Equal Q and equal masses: common winding recovers standard law;
    # changing just one component is a different, possibly inaccessible sector.
    R = np.array([[1,.03],[.03,.2]])
    np.testing.assert_allclose(spacing_mass(R,[qom,qom],[MS,MS],[1,1]), MS, rtol=2e-15)
    checks.append("equal charge/mass with common winding reduces to the ordinary single-phase spacing")

    # 5. Fixed external flux changes intercept, not spacing.
    x = 92e-6
    R = np.array([[1,x],[x,.002]])
    _, K, psi = kernel(R,[qom,0],[MS,20*MS],[1,0])
    flux_ext = .37*psi
    frequencies = (np.arange(-3,4)*psi-flux_ext)/(4*np.pi*K*area)
    np.testing.assert_allclose(np.diff(frequencies), psi/(4*np.pi*K*area), rtol=2e-15)
    checks.append("stationary applied/trapped-flux offset leaves branch spacing invariant")

    # 6. GLS common-mode frequency offset does not inflate slope uncertainty;
    # a common scale calibration does and must be added outside point noise.
    n = np.arange(-4,5, dtype=float)
    sigma = 2e-6
    covariance = sigma*sigma*np.eye(len(n))+(20e-6)**2*np.ones((len(n),len(n)))
    estimated, pcov = fit_zero_sequence(n, 0.1+0.037*n, covariance)
    np.testing.assert_allclose(estimated,[.1,.037],rtol=1e-12)
    np.testing.assert_allclose(pcov[1,1],sigma*sigma/(n@n),rtol=1e-12)
    checks.append("correlated-intercept GLS leaves centered slope variance sigma^2/sum(n^2)")

    # 7. Multiple zero spacings cannot distinguish x, area scale, surface offset.
    # log mass = log(1+x) + log area_ratio - alpha + ... locally.
    degenerate = np.tile([1/(1+92e-6), 1.0, -1.0], (5,1))
    assert np.linalg.matrix_rank(degenerate) == 1
    with_controls = np.vstack([degenerate,[0,1,0],[0,0,1]])
    assert np.linalg.matrix_rank(with_controls) == 3
    checks.append("spacing-only x/area/surface design has rank 1; independent area and surface controls restore rank 3")
    return checks


def synthetic_annulus_study():
    # NO parameter below is a claimed Tate apparatus dimension.
    parameters = dict(radius=.010, width=.0002, thickness=5e-9,
                      pickup_radius=.008, pickup_z=.001)
    nominal_area = np.pi*parameters["radius"]**2
    rows = []
    for penetration in [50e-9, 100e-9, 200e-9]:
        previous = None
        for cells in [32,64,128,256,512]:
            op = annulus_operator(**parameters, penetration=penetration, cells=cells)
            A = op["area_effective"]
            rows.append(dict(label="SYNTHETIC; not Tate data", lambda_nm=penetration*1e9,
                cells=cells, area_effective_m2=A,
                area_bias_ppm=(A/nominal_area-1)*1e6,
                refinement_change_ppm=None if previous is None else (A/previous-1)*1e6,
                minimum_eigenvalue_H=op["min_eigenvalue"]))
            previous = A
        assert abs(rows[-1]["refinement_change_ppm"]) < .25
        # Direct solution at the pickup-zero root: residual pickup vanishes,
        # while the film generally still contains oppositely signed currents.
        psi = H/QS
        K = MS/QS
        root = psi/(2*K*A)
        current = solve(op["L"], psi*np.ones(cells)-2*K*root*op["areas"], assume_a="pos")
        reference = max(abs(op["pickup"] @ solve(op["L"],psi*np.ones(cells),assume_a="pos")),1e-30)
        assert abs(op["pickup"] @ current)/reference < 1e-12
        assert current.min() < 0 < current.max()
    # Radial-collapse check uses the general operator identity with all S equal.
    op = annulus_operator(**parameters, penetration=100e-9, cells=64)
    ident_area = float(op["pickup"] @ solve(op["L"], nominal_area*np.ones(64), assume_a="pos") / op["U"])
    np.testing.assert_allclose(ident_area,nominal_area,rtol=2e-15)
    return parameters, rows


def sensitivity_budget():
    # Log-coefficient uncertainty: vector is [log area, log spacing, alpha].
    # Covariance is synthetic and illustrative, never Tate's actual covariance.
    sigmas_ppm = np.array([8.0,5.0,3.0])
    jacobian = np.array([-1.0,-1.0,1.0])
    results = []
    for correlation in [-.8,0,.8]:
        cov = np.diag(sigmas_ppm**2)
        cov[0,1]=cov[1,0]=correlation*sigmas_ppm[0]*sigmas_ppm[1]
        results.append(dict(label="SYNTHETIC; not Tate uncertainty", area_spacing_correlation=correlation,
                            inferred_shift_sigma_ppm=float(np.sqrt(jacobian@cov@jacobian))))
    return results


def main():
    checks = verify()
    parameters, rows = synthetic_annulus_study()
    checks.append("thin-film annulus refinement, pickup-zero/current distinction, and narrow-ring area identity")
    sensitivity = sensitivity_budget()
    examples = []
    for x,r,y in [(92e-6,.002,0),(.01,.02,.2)]:
        bulk=(1+x+y*(x+r))/(1+2*x*y+r*y*y)
        spacing=(1+x+y*(x+r))/(1+x*y)
        examples.append(dict(label="SYNTHETIC kernel",x=x,r=r,y=y,
                             bulk_field_ratio=bulk,spacing_mass_ratio=spacing))
    result = dict(status="All bounded-model checks passed; no empirical fit performed",
        checks=checks, synthetic_annulus_parameters_SI=parameters,
        synthetic_annulus=rows, synthetic_uncertainty=sensitivity,
        synthetic_kernel_examples=examples,
        published_comparison=dict(measured_ratio=1.000084, reported_uncertainty=21e-6,
            bare_difference_ppm=84, corrected_baseline=0.999992, baseline_difference_ppm=92,
            note="Published comparison only; no reconstructed covariance or significance claim"))
    (OUT/"verification_results.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    with (OUT/"synthetic_annulus_sensitivity.csv").open("w",newline="",encoding="utf-8") as stream:
        writer=csv.DictWriter(stream,fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps(dict(status=result["status"],checks=len(checks),
        final_mesh_rows=[r for r in rows if r["cells"]==512],
        synthetic_uncertainty=sensitivity,synthetic_kernel_examples=examples),indent=2))


if __name__ == "__main__":
    main()
