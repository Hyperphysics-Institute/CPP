#!/usr/bin/env python3
# 2349 audits (run after the engine, before grading): (A) pass DEPTH per audited
# frame (interior margin, not mere feasibility); (B) minimum-p profile -- the
# measured steepness the S(N) rent leg must survive; (C) S0 box-edge robustness
# annex (post-registered, labeled: extends log10 S0 to -9; the pre-reg box
# already contains passes, this only maps the region); (D) channel audit at the
# reported passing points: extrapolation share, floor share, carrying pairs;
# (E) truncation audit at the long-rod point.

import json, math, os
import numpy as np
from scipy.optimize import minimize
import importlib.util as iu

here = os.path.dirname(os.path.abspath(__file__))
spec = iu.spec_from_file_location("eng", os.path.join(here, "2349_g1_engine.py"))
eng = iu.module_from_spec(spec); spec.loader.exec_module(eng)

FRAMES = eng.FRAMES
res = json.load(open(os.path.join(here, "2349_results.json")))

def depth(tot, frame):
    """interior margin: min over windows of min(tot/lo, hi/tot); >1 = inside."""
    d = np.inf
    for vel, (lo, hi) in frame.items():
        x = tot[vel]
        if lo > 0: d = min(d, x / lo)
        d = min(d, hi / x)
    return d

def dist_at(la):
    N, f, Ln, merr, _ = eng.distribution(10.0 ** la)
    keep = f >= 1e-6
    return N[keep], f[keep] / f[keep].sum(), Ln, merr

out = {}

# (A) depth maximization per audited frame, alpha on a local grid, S0 floor -9
for fk in ("audited_central", "audited_extended"):
    fr = FRAMES[fk]; b = res["refined_best"][fk]
    best = {"depth": -np.inf}
    for la in np.linspace(b["la"] - 1.0, b["la"] + 1.0, 9):
        la = float(np.clip(la, -2, 6))
        Narr, warr, Ln, merr = dist_at(la)
        def obj(x):
            ls, p, rs = x
            if not (-9 <= ls <= 2 and 0 <= p <= 16 and 20 <= rs <= 120):
                return 50.0
            return -math.log(depth(eng.totals_K(Narr, warr, 10.0**ls, p, rs), fr))
        r = minimize(obj, [b["ls"], b["p"], b["rs"]], method="Nelder-Mead",
                     options={"maxiter": 600, "xatol": 1e-4, "fatol": 1e-7})
        d = math.exp(-r.fun)
        if d > best["depth"]:
            tot = eng.totals_K(Narr, warr, 10.0**r.x[0], r.x[1], r.x[2])
            best = {"depth": d, "la": la, "ls": float(r.x[0]), "p": float(r.x[1]),
                    "rs": float(r.x[2]), "tot": tot, "Ln": Ln}
    out[fk + "_depth"] = best
    print(fk, "max depth %.4f at alpha=%.3g p=%.2f S0=1e%.2f Rs=%.1f Ln=%.2f"
          % (best["depth"], 10**best["la"], best["p"], best["ls"],
             best["rs"], best["Ln"]))
    print("   totals:", {k: round(v, 3) for k, v in best["tot"].items()})

# (B) minimum-p profile: smallest p with a pass (viol <= 1+1e-9), per frame
for fk in ("audited_central", "audited_extended"):
    fr = FRAMES[fk]
    pmin = None; prof = []
    for p in np.arange(0.0, 16.001, 1.0):
        bestv = np.inf
        for la in np.linspace(-2, 6, 17):
            Narr, warr, _, _ = dist_at(la)
            def obj(x):
                ls, rs = x
                if not (-9 <= ls <= 2 and 20 <= rs <= 120): return 50.0
                return math.log(eng.violation(
                    eng.totals_K(Narr, warr, 10.0**ls, p, rs), fr))
            r = minimize(obj, [-4.0, 30.0], method="Nelder-Mead",
                         options={"maxiter": 300, "xatol": 1e-4, "fatol": 1e-7})
            bestv = min(bestv, math.exp(r.fun))
        prof.append({"p": float(p), "best_viol": bestv})
        if bestv <= 1.0 + 1e-9 and pmin is None:
            pmin = float(p)
    out[fk + "_p_profile"] = prof
    out[fk + "_p_min"] = pmin
    print(fk, "p_min =", pmin, " profile:",
          [(d["p"], round(d["best_viol"], 3)) for d in prof if d["p"] <= (pmin or 16) + 2])

# (C) box-edge robustness: does the pre-reg box (ls >= -6) contain a pass
#     strictly interior for both frames? evaluate at ls = -5.5 near optimum.
for fk in ("audited_central", "audited_extended"):
    fr = FRAMES[fk]; b = res["refined_best"][fk]
    Narr, warr, _, _ = dist_at(b["la"])
    def obj(x):
        ls, p, rs = x
        if not (-5.5 <= ls <= 2 and 0 <= p <= 16 and 20 <= rs <= 120): return 50.0
        return math.log(eng.violation(eng.totals_K(Narr, warr, 10.0**ls, p, rs), fr))
    r = minimize(obj, [-5.4, b["p"], b["rs"]], method="Nelder-Mead",
                 options={"maxiter": 500, "xatol": 1e-4, "fatol": 1e-7})
    out[fk + "_interior_ls55"] = {"viol": math.exp(r.fun), "ls": float(r.x[0]),
                                  "p": float(r.x[1]), "rs": float(r.x[2])}
    print(fk, "interior (ls>=-5.5) best viol:", round(math.exp(r.fun), 4))

# (D) channel audit at the DEPTH points: extrapolation share and floor share
for fk in ("audited_central", "audited_extended"):
    b = out[fk + "_depth"]
    Narr, warr, _, _ = dist_at(b["la"])
    S = 10.0**b["ls"] * (Narr / 2.0) ** b["p"]
    M = Narr * eng.M_EL
    i, j = np.triu_indices(len(Narr))
    Sij = np.sqrt(S[i] * S[j]); mu = M[i]*M[j]/(M[i]+M[j])
    wfac = np.where(i == j, warr[i]*warr[j]/M[i],
                    warr[i]*warr[j]*(1.0/M[i]+1.0/M[j]))
    aud = {}
    for v in eng.VELS:
        bb = (v/eng.C)**2
        eps = Sij / (0.5*mu*bb*b["rs"])
        sig = b["rs"]**2 * eng.F_of_eps(eps)
        contrib = wfac * sig * eng.CONV0
        tot_int = contrib.sum()
        ext_share = contrib[eps > 9.9e3].sum() / tot_int if tot_int > 0 else 0.0
        fl = eng.FL[int(v)]
        k = np.argsort(contrib)[::-1][:3]
        aud[int(v)] = {
            "floor_share": fl / (tot_int + fl),
            "extrap_share_of_interactions": float(ext_share),
            "top_pairs": [(int(Narr[i[m]]), int(Narr[j[m]]),
                           float(contrib[m]/tot_int)) for m in k]}
    out[fk + "_channel_audit"] = aud
    print(fk, "channel audit:")
    for v, a in aud.items():
        print("  v=%d floor %.3f extrap %.2g top" % (v, a["floor_share"],
              a["extrap_share_of_interactions"]), a["top_pairs"])

# (E) truncation audit at the long-rod point (alpha ~ 1e-2): NCAP and weight floor
la = out["audited_extended_depth"]["la"]
N, f, Ln, merr, c1f = eng.distribution(10.0**la, ncap=400)
N2, f2_, Ln2, merr2, _ = eng.distribution(10.0**la, ncap=700)
out["truncation_audit"] = {
    "alpha": 10.0**la, "mass_err_ncap400": merr, "mass_err_ncap700": merr2,
    "Ln_400": Ln, "Ln_700": Ln2, "tail_mass_beyond_keep": float(f[f < 1e-6].sum())}
print("truncation: Ln 400 vs 700 = %.4f / %.4f, mass_err %.2e / %.2e, dropped %.2e"
      % (Ln, Ln2, merr, merr2, f[f < 1e-6].sum()))

json.dump(out, open(os.path.join(here, "2349_audits.json"), "w"), indent=1)
print("audits saved")
