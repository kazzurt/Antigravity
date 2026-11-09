"""Independent checks and an explanatory figure for the two bounded models.

All figure parameters are illustrative. No measurement fit is performed.
Run with Python, NumPy, SciPy and Matplotlib. Outputs stay beside this file.
"""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import solve_bvp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent


def slab_formula(k0, kw, d):
    return np.exp(k0*d)/(np.cosh(kw*d)+(kw*kw+k0*k0)/(2*k0*kw)*np.sinh(kw*d))


def checks():
    rows = []
    for k0, kw, d in [(0.2,0.2,1),(0.2,1,1),(0.2,4,1),(1,4,0.3),(0.1,8,1)]:
        z = np.linspace(0,d,100)
        def fun(z,y):
            return np.vstack((y[1],kw*kw*y[0]))
        def boundary(left,right):
            return np.array([left[1]-k0*left[0]+2*k0,right[1]+k0*right[0]])
        sol = solve_bvp(fun,boundary,z,np.vstack((np.exp(-k0*z),-k0*np.exp(-k0*z))),
                        tol=1e-10,max_nodes=5000)
        observed = float(sol.sol(d)[0]/np.exp(-k0*d))
        expected = float(slab_formula(k0,kw,d))
        error = abs(observed-expected)/expected
        assert sol.success and error < 2e-8
        rows.append(dict(outside_inverse_range=k0,wall_inverse_range=kw,thickness=d,
                         formula=expected,bvp=observed,relative_error=error))

    rng = np.random.default_rng(42)
    errors = []
    for _ in range(1000):
        x = rng.uniform(-0.3,0.3)
        r = x*x+rng.uniform(.001,1)
        y = rng.uniform(-1,1)
        stiffness = np.array([[1,x],[x,r]])
        charge_to_mass = np.array([1.,y])
        winding_increment = np.array([1.,0.])  # normalized h/m_s = 1
        denominator = charge_to_mass@stiffness@charge_to_mass
        bulk_coefficient = (charge_to_mass@stiffness@np.ones(2))/denominator
        winding_flux = (charge_to_mass@stiffness@winding_increment)/denominator
        mass_period = bulk_coefficient/winding_flux
        formula = (1+x+y*(x+r))/(1+x*y)
        assert np.isclose(mass_period,formula,rtol=1e-11,atol=1e-11)
        errors.append(abs(mass_period-formula))
    return dict(status="Passed; internal model checks, not empirical validation",
                independent_slab_cases=rows,random_kernel_seed=42,
                random_positive_definite_kernel_cases=len(errors),
                maximum_kernel_absolute_error=max(errors))


def figure():
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,
                         "axes.spines.top":False,"axes.spines.right":False,
                         "savefig.facecolor":"white"})
    fig, axes = plt.subplots(1,2,figsize=(11.8,4.8))
    fig.subplots_adjust(left=.075,right=.975,bottom=.28,top=.79,wspace=.30)
    fig.suptitle("Two research results — and what they leave unresolved",
                 x=.075,ha="left",fontsize=17,fontweight="bold",y=.965)
    fig.text(.075,.865,"Illustrative calculations; no material device or Tate data fit",color="#555555")
    strength = np.linspace(.1,10,500)
    k0, d, a, b, alpha = 1.,.1,.2,.2,1.
    massive = slab_formula(k0,strength/d,d)
    ratio = (4/3)*alpha**2*np.exp(-k0*(a+d+b))
    total = (1+ratio*massive)/(1+ratio)
    floor = 1/(1+ratio)
    ax = axes[0]
    ax.plot(strength,massive,color="#949494",ls="--",lw=2,label="Massive component")
    ax.plot(strength,total,color="#216E8A",lw=2.7,label="Total physical field")
    ax.axhline(floor,color="#216E8A",ls=":",lw=1.2)
    ax.text(9.8,floor+.045,f"Common-field floor: {100*floor:.1f}%",ha="right",color="#216E8A",fontsize=9)
    ax.set(xlim=(0,10),ylim=(0,1.06),xlabel="Wall inverse range × thickness",
           ylabel="Field gradient / no-wall gradient")
    ax.set_title("1   Attenuation leaves a common field",loc="left",fontsize=11,fontweight="bold",pad=12)
    ax.grid(axis="y",alpha=.15)
    ax.legend(frameon=False,loc="upper right",fontsize=9)
    ax.text(0,-.34,"Fixed mixing; planar source; imposed mass profile.\nExample: α = 1, μ₀d = 0.1, μ₀(a+d+b) = 0.5.",
            transform=ax.transAxes,fontsize=8.5,color="#555555",va="top")

    ax = axes[1]
    x_ppm = np.linspace(0,150,301)
    target = 1+92e-6
    area_offset = (target/(1+x_ppm*1e-6)-1)*1e6
    ax.plot(x_ppm,area_offset,color="#A45932",lw=2.7)
    ax.scatter([0,92],[92,0],color="#A45932",s=28,zorder=4)
    ax.axhline(0,color="#777777",lw=.8)
    ax.annotate("Same apparent 92 ppm shift",xy=(54,38),xytext=(48,82),
                arrowprops={"arrowstyle":"-","color":"#A45932"},fontsize=9,color="#A45932")
    ax.set(xlim=(-3,153),ylim=(-68,108),xlabel="Assumed neutral entrainment x (ppm)",
           ylabel="Required effective-area offset (ppm)")
    ax.set_title("2   One period does not identify its cause",loc="left",fontsize=11,fontweight="bold",pad=12)
    ax.grid(axis="y",alpha=.15)
    ax.text(0,-.34,"Fixed neutral winding; other corrections held fixed.\nArea ratio = (1 + 92 ppm) / (1 + x); no area error is inferred.",
            transform=ax.transAxes,fontsize=8.5,color="#555555",va="top")
    fig.savefig(OUT/"two-track-results.png",dpi=180,bbox_inches="tight")
    fig.savefig(OUT/"two-track-results.svg",bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    result = checks()
    (OUT/"independent_checks.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    figure()
    print(json.dumps(result,indent=2))
