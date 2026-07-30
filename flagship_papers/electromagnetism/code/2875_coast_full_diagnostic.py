"""
Patch 2875 — SETTLING 2870's COAST-FIT FLAG BY COMPUTATION.

2870 flagged, narrowly and without asserting error, that 2496's Stage C
coast fit selects its window with

    m = (tv > tv[0] + 6) & (vv > 1e-4)          # 2496 line 139
    tau = -1/np.polyfit(tv[m], np.log(vv[m]), 1)[0]

and that this excludes the region where the sign reversal occurs. 2870
declined a third confident claim about this file. This script makes the
claim unnecessary by measuring the full coast instead of characterising
it.

THE STRUCTURAL POINT 2870 DID NOT STATE: the filter is not only a noise
floor. `np.log(vv)` is undefined for vv <= 0, so a sign-changing signal
CANNOT be fitted by this estimator at all. The filter is therefore doing
double duty -- rejecting a noise floor AND excluding the region that
would break the model being fitted. Whether that matters is an empirical
question about whether v actually changes sign, which is what this
measures.

REPORTED, for mu = 10 and mu = 25:
  1. does v cross zero during the coast, and how many times
  2. the full-coast min/max of v, and v at the end
  3. tau on 2496's filtered window, and how many DECADES of decay that
     window actually spans
  4. a pure-exponential fit vs a damped-oscillation fit on the full
     coast, compared by RMS residual, so the better description is
     decided by number and not by preference

NOTHING HERE TOUCHES eps_mem, the ambient Sea, N, or tau_Sea. This is a
Tier-2 scalar toy measuring a bare point. It is a characterisation
correction to a development sketch, not evidence about 1B.

Run from this directory:  python3 2875_coast_full_diagnostic.py
"""

import importlib.util
import re
import sys
import numpy as np

SRC = "2496_sf6_inertia_impulse.py"


def load_patched_module():
    """Load 2496 with `dynamics` additionally returning the raw coast traces.

    The published estimator is left byte-for-byte intact; we only add an
    export of recC so the full trace can be inspected. Patching in memory
    rather than editing the committed artifact.
    """
    src = open(SRC).read()
    # export the raw coast traces alongside the published aggregates
    patched = src.replace(
        "        out[f'coast_mu{int(mu)}'] = dict(tau=float(tau), kappa_coast=float(tau/mu))",
        "        out[f'coast_mu{int(mu)}'] = dict(tau=float(tau), kappa_coast=float(tau/mu))\n"
        "        out.setdefault('_traces', {})[int(mu)] = (tv.copy(), vv.copy())",
    )
    if "_traces" not in patched:
        sys.exit("PATCH FAILED — 2496 line 141 not matched; inspect the source.")
    spec = importlib.util.spec_from_loader("m2496", loader=None)
    mod = importlib.util.module_from_spec(spec)
    exec(compile(patched, SRC, "exec"), mod.__dict__)
    return mod


def analyse(mu, tv, vv):
    print(f"\n{'='*64}\nCOAST DIAGNOSTIC — mu = {mu}\n{'='*64}")

    # 1. sign behaviour over the FULL coast
    sign_changes = int(np.sum(np.diff(np.sign(vv)) != 0))
    print(f"  zero crossings over full coast      : {sign_changes}")
    print(f"  v at coast start / min / max / end  : "
          f"{vv[0]:+.4e} / {vv.min():+.4e} / {vv.max():+.4e} / {vv[-1]:+.4e}")
    monotone = bool(np.all(np.diff(vv) <= 0))
    print(f"  monotonically decreasing?           : {monotone}")

    # 2. the published window, and how much decay it actually spans
    m = (tv > tv[0] + 6) & (vv > 1e-4)
    n_kept, n_tot = int(m.sum()), len(vv)
    tau_pub = -1 / np.polyfit(tv[m], np.log(vv[m]), 1)[0]
    decades = np.log10(vv[m].max() / vv[m].min()) if m.sum() > 1 else float("nan")
    print(f"  published window keeps             : {n_kept}/{n_tot} samples")
    print(f"  published tau                      : {tau_pub:.3f}   (kappa=tau/mu={tau_pub/mu:.4f})")
    print(f"  DECADES of decay inside window     : {decades:.3f}")
    if decades < 1.0:
        print(f"  >> fitted across UNDER ONE DECADE — 2870's flag CONFIRMED")

    # 3. exponential vs damped oscillation, on the full coast, by residual
    t = tv - tv[0]
    exp_fit = np.polyfit(t[m], np.log(vv[m]), 1)
    v_exp = np.exp(np.polyval(exp_fit, t))
    rms_exp = float(np.sqrt(np.mean((vv - v_exp) ** 2)))

    # damped oscillation v = A exp(-t/tau) cos(w t + p), coarse grid search
    best = None
    for tau_g in np.linspace(0.3 * tau_pub, 8 * tau_pub, 60):
        env = np.exp(-t / tau_g)
        for w in np.linspace(0.0, 3.0, 240):
            B = np.vstack([env * np.cos(w * t), env * np.sin(w * t)]).T
            coef, *_ = np.linalg.lstsq(B, vv, rcond=None)
            r = float(np.sqrt(np.mean((vv - B @ coef) ** 2)))
            if best is None or r < best[0]:
                best = (r, tau_g, w, coef)
    rms_osc, tau_osc, w_osc, _ = best

    print(f"  RMS residual, pure exponential     : {rms_exp:.4e}")
    print(f"  RMS residual, damped oscillation   : {rms_osc:.4e}"
          f"   (tau={tau_osc:.2f}, omega={w_osc:.3f})")
    if rms_exp > 0:
        print(f"  improvement factor                 : {rms_exp/rms_osc:.2f}x")
    verdict = ("DAMPED OSCILLATION describes the coast better"
               if rms_osc < 0.5 * rms_exp else
               "no decisive improvement from an oscillatory model")
    print(f"  VERDICT                            : {verdict}")
    return dict(mu=mu, crossings=sign_changes, monotone=monotone,
                tau_pub=tau_pub, decades=decades,
                rms_exp=rms_exp, rms_osc=rms_osc, omega=w_osc)


if __name__ == "__main__":
    mod = load_patched_module()
    N, c, h, dt, g, vf = 96, 1., 1., 0.35, 8., 0.05
    print("Reproducing 2496 Stage 0/A/B/C at sigma = 1.5 (published parameters)...")
    st = mod.stages_0A(N, 1.5, g, c, h, [0.025, 0.05, 0.1])
    dyn = mod.dynamics(N, 1.5, g, c, h, dt, vf, 30., 40.,
                       mus=(10., 25.), Tc=45., st=st)

    print(f"\npublished tau values reproduced: "
          f"mu=10 -> {dyn['coast_mu10']['tau']:.2f}, "
          f"mu=25 -> {dyn['coast_mu25']['tau']:.2f}")

    results = [analyse(mu, *dyn['_traces'][mu]) for mu in sorted(dyn['_traces'])]

    print(f"\n{'='*64}\nSUMMARY\n{'='*64}")
    for r in results:
        print(f"  mu={r['mu']:2d}: crossings={r['crossings']}  "
              f"monotone={r['monotone']}  tau_pub={r['tau_pub']:.2f}  "
              f"decades={r['decades']:.2f}")
    print("\nSCOPE: Tier-2 scalar toy, bare point. Says nothing about "
          "eps_mem, tau_Sea, N, or the ambient Sea.")
