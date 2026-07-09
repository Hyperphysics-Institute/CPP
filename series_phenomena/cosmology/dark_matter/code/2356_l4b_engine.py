#!/usr/bin/env python3
# 2356 -- L4-b PIN-VELOCITY AUDIT (engine). Pre-registration: code/2356_PREREG.md.
# Provenance: the 1865 J3' ledger (registered; nothing newly sourced). Convention
# map fixed pre-run: <v> = 2.26*sigma_1D, sigma_1D ~ (0.6-0.8)*V_max =>
# <v> ~ (1.4-1.8)*V_max; Elbert V_max=40 => <v> in [56,72].
# ORDER: (1) v1-kill robustness (hurting direction FIRST), (2) collision severity
# vs v_pin, (3) joint BOTH-STRANDS re-search with the pin relocated, (4) G1/G2
# pass re-verification at audited pin.

import json, math, os
import numpy as np
from scipy.optimize import minimize
import importlib.util as iu

here = os.path.dirname(os.path.abspath(__file__))
spec = iu.spec_from_file_location("g3", os.path.join(here, "2351_g3_engine.py"))
g3 = iu.module_from_spec(spec); spec.loader.exec_module(g3)
g2, g1 = g3.g2, g3.g2.g1

FAMILY_MAX = 3.2
VPINS = [50.0, 55.0, 60.0, 64.0, 70.0]
out = {"convention": {"vrel_over_sigma1d": 2.26, "sigma1d_over_vmax": [0.6, 0.8],
                      "v_over_vmax": [1.4, 1.8],
                      "elbert_vmax40_vband": [56.0, 72.0]}}

# ---------- (1) v1-KILL ROBUSTNESS, FIRST ----------
# 2337-corrected measured curve of the killed candidate (campaign ledger, verbatim):
KILL_CURVE = {30.0: 12.63, 50.0: 8.78, 200.0: 2.65, 1150.0: 0.06, 1500.0: 0.062}
def kill_sigma(v):
    vs = sorted(KILL_CURVE)
    lv = [math.log(x) for x in vs]; ls = [math.log(KILL_CURVE[x]) for x in vs]
    return math.exp(np.interp(math.log(v), lv, ls))
V1 = {30: (20.0, 100.0), 50: (1.0, 5.0), 200: (0.7, 2.5), 1500: (0.0, 0.13)}
rob = {}
for vp in VPINS:
    pin_sig = kill_sigma(vp)
    pin_fail = pin_sig / V1[50][1]                 # v1 pin ceiling = 5
    dsph_fail = V1[30][0] / kill_sigma(30.0)       # dSph low edge, pin-INDEPENDENT
    rob[vp] = {"pin_sigma": pin_sig, "pin_over_ceiling": pin_fail,
               "dsph_shortfall": dsph_fail}
out["kill_robustness"] = rob
worst_dsph = min(r["dsph_shortfall"] for r in rob.values())
print("(1) v1-kill robustness: dSph shortfall x%.2f at EVERY audited v_pin "
      "(pin-independent); pin-over-ceiling ranges %.2f..%.2f -> kill class STANDS"
      % (worst_dsph, min(r["pin_over_ceiling"] for r in rob.values()),
         max(r["pin_over_ceiling"] for r in rob.values())))

# ---------- (2) collision severity vs v_pin ----------
sev = {vp: math.log(2.0) / math.log(vp / 48.0) for vp in VPINS}
out["collision_severity"] = {str(int(v)): s for v, s in sev.items()}
v_dissolve = 48.0 * math.exp(math.log(2.0) / FAMILY_MAX)
out["v_dissolve"] = v_dissolve
print("(2) s_req(v_pin):", {int(v): round(s, 2) for v, s in sev.items()},
      "| dissolves (s_req <= %.1f) at v_pin >= %.1f" % (FAMILY_MAX, v_dissolve))

# ---------- (3) joint BOTH-STRANDS re-search with the pin relocated ----------
def windows_with_pin(frame, vpin):
    fr = dict(g1.FRAMES[frame])
    lo, hi = fr.pop(50)
    fr2 = {v: w for v, w in fr.items() if v != 30}   # dSph replaced by anchors
    fr2[vpin] = (lo, hi)
    return fr2

def joint_viol(Narr, warr, S0, p, rs, frame, vpin):
    sf = lambda v: g2.sigma_eff(Narr, warr, S0, p, rs, v, False)[0]
    av = g3.anchor_viol(sf)
    v = max(av.values())
    for vel, (lo, hi) in windows_with_pin(frame, vpin).items():
        s = sf(float(vel))
        if lo > 0 and s < lo: v = max(v, lo / s)
        if s > hi: v = max(v, s / hi)
    return v, av, sf

out["research"] = {}
for frame in ("audited_extended", "audited_central"):
    out["research"][frame] = {}
    for vpin in (55.0, 60.0, 64.0, 70.0):
        best = {"joint": np.inf}
        for la in np.linspace(-2, 6, 9):
            N, f, Ln, merr, _ = g1.distribution(10.0**la)
            keep = f >= 1e-6
            Narr, warr = N[keep], f[keep]/f[keep].sum()
            def obj(x):
                ls, p, rs = x
                if not (-6 <= ls <= 2 and 0 <= p <= 16 and 20 <= rs <= 120):
                    return 50.0
                return math.log(joint_viol(Narr, warr, 10.0**ls, p, rs,
                                           frame, vpin)[0])
            for seed in ([-4, 8, 25], [-5, 14, 30], [-3, 5, 40], [-4.5, 12, 60]):
                r = minimize(obj, seed, method="Nelder-Mead",
                             options={"maxiter": 500, "xatol": 1e-4,
                                      "fatol": 1e-7})
                jv = math.exp(r.fun)
                if jv < best["joint"]:
                    _, av, sf = joint_viol(Narr, warr, 10.0**r.x[0],
                                           float(r.x[1]), float(r.x[2]),
                                           frame, vpin)
                    best = {"joint": jv, "la": float(la), "ls": float(r.x[0]),
                            "p": float(r.x[1]), "rs": float(r.x[2]),
                            "anchors": av,
                            "sig": {str(v): sf(v) for v in
                                    (21.0, 30.0, 48.0, vpin, 58.0, 200.0, 1500.0)}}
        out["research"][frame][str(int(vpin))] = best
        print("(3) [%s @ v_pin=%d] joint x%.3f (LeoII %.2f Carina %.2f Draco %.2f)"
              % (frame, vpin, best["joint"], best["anchors"]["LeoII"],
                 best["anchors"]["Carina"], best["anchors"]["Draco"]))

# ---------- (4) G1/G2 pass points re-verified at the audited pin ----------
nat = json.load(open(os.path.join(here, "2349_naturalness.json")))
aud = json.load(open(os.path.join(here, "2349_audits.json")))
xe = nat["audited_extended@alpha=1 (natural)"]["x"]
bc = aud["audited_central_depth"]
pts = {"kin_extended_natural": (0.0, 10**xe[0], xe[1], xe[2], "audited_extended"),
       "kin_central_depth": (bc["la"], 10**bc["ls"], bc["p"], bc["rs"],
                             "audited_central")}
out["pass_relief"] = {}
for name, (la, S0, p, rs, frame) in pts.items():
    N, f, Ln, merr, _ = g1.distribution(10.0**la)
    keep = f >= 1e-6
    Narr, warr = N[keep], f[keep]/f[keep].sum()
    sf = lambda v: g2.sigma_eff(Narr, warr, S0, p, rs, v, False)[0]
    lo, hi = g1.FRAMES[frame][50]
    row = {str(int(vp)): {"sigma": sf(vp),
                          "viol": max(lo/sf(vp) if sf(vp) < lo else 1.0,
                                      sf(vp)/hi if sf(vp) > hi else 1.0)}
           for vp in VPINS}
    out["pass_relief"][name] = row
    print("(4) %s pin-eval across v_pin: " % name,
          {k: round(v["viol"], 3) for k, v in row.items()})

json.dump(out, open(os.path.join(here, "2356_results.json"), "w"), indent=1)
print("saved 2356_results.json")
