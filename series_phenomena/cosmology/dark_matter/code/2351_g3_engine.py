#!/usr/bin/env python3
# 2351 -- G3 PER-dSPH LIKELIHOOD (engine). Protocol/outcomes pre-registered in
# code/2351_PREREG.md before this ran. Source: Correa 2021 (MNRAS 503, 920;
# arXiv:2007.02958) read in full this session -- exact anchors (in-text <v> +
# Table 2 ranges, which already include her factor-2 model uncertainty):
#   LeoII  <v>=21 km/s  sigma in [90,150];  Carina <v>=48  [40,50];
#   Draco  <v>=58  [20,30].   Tolerance U=2 pre-registered.
# Demand curve from her verbatim fit parameters (computed, not digitized):
#   sigma_C(v) = sigma0/(1+(v/w)^2), m_chi=0.648+-0.154 GeV,
#   m_phi=0.636+-0.055 MeV, alpha_chi=0.01.

import json, math, os
import numpy as np
from scipy.optimize import minimize
import importlib.util as iu

here = os.path.dirname(os.path.abspath(__file__))
spec = iu.spec_from_file_location("g2", os.path.join(here, "2350_g2_engine.py"))
g2 = iu.module_from_spec(spec); spec.loader.exec_module(g2)
g1 = g2.g1

# ---- Correa demand (verbatim parameters -> derived curve) ----
def correa_pars(m_chi, m_phi, alpha=0.01):
    s0 = 0.0275 * (alpha/0.01)**2 * (m_chi/10.0) * (10.0/m_phi)**4   # cm^2/g
    w = 30.0 * (m_phi/10.0) * (10.0/m_chi)                            # km/s
    return s0, w
S0C, WC = correa_pars(0.648, 0.636)          # central: ~108.9, ~29.4
S0C_hi, WC_hi = correa_pars(0.648+0.154, 0.636-0.055)
S0C_lo, WC_lo = correa_pars(0.648-0.154, 0.636+0.055)
def sigma_correa(v, s0=S0C, w=WC):
    return s0 / (1.0 + (v/w)**2)

ANCHORS = {"LeoII": (21.0, 90.0, 150.0),
           "Carina": (48.0, 40.0, 50.0),
           "Draco": (58.0, 20.0, 30.0)}
U = 2.0
TABLE2 = {"UM": (40,50), "Draco": (20,30), "Carina": (40,50), "Sextans": (70,120),
          "CVnI": (50,80), "Sculptor": (30,40), "Fornax": (30,50),
          "LeoII": (90,150), "LeoI": (50,70)}   # verbatim, ranges only (no <v>)

def anchor_viol(sig_of_v):
    out = {}
    for name, (v, lo, hi) in ANCHORS.items():
        s = sig_of_v(v)
        out[name] = max(lo/(U*s), s/(U*hi), 1.0)
    return out

# pin/LSB/cluster windows per frame variant (dSph aggregate REPLACED by anchors)
def rest_windows(frame):
    fr = dict(g1.FRAMES[frame]); fr.pop(30)
    return fr

def rest_viol(sig_of_v, frame):
    v = 1.0
    for vel, (lo, hi) in rest_windows(frame).items():
        s = sig_of_v(float(vel))
        if s < lo: v = max(v, lo/s)
        if s > hi: v = max(v, s/hi)
    return v

def kin_sig(la, S0, p, Rs, envelope=False):
    N, f, Ln, merr, _ = g1.distribution(10.0 ** la)
    keep = f >= 1e-6
    Narr, warr = N[keep], f[keep]/f[keep].sum()
    return lambda v: g2.sigma_eff(Narr, warr, S0, p, Rs, v, envelope)[0]

def grade_point(sig_of_v, frame):
    av = anchor_viol(sig_of_v)
    rv = rest_viol(sig_of_v, frame)
    mono = sig_of_v(21.0) >= sig_of_v(48.0) >= sig_of_v(58.0)
    band = {}
    for v in (21.0, 30.0, 48.0, 58.0):
        s = sig_of_v(v); c = sigma_correa(v)
        band[v] = {"sig": s, "correa": c, "in_band": (c/2.0 <= s <= 3.0*c),
                   "ratio": s/c}
    return {"anchors": av, "joint_anchor_viol": max(av.values()),
            "rest_viol": rv, "joint": max(max(av.values()), rv),
            "monotone_shape": bool(mono), "band": band}

if __name__ == "__main__":
    out = {"correa_fit": {"sigma0": S0C, "w": WC,
                          "sigma0_1sig": [S0C_lo, S0C_hi], "w_1sig": [WC_lo, WC_hi]},
           "anchors": {k: list(v) for k, v in ANCHORS.items()}, "U": U}

    # (A) as-stored evaluation of the G1/G2 passing points (2345 P4 discipline)
    nat = json.load(open(os.path.join(here, "2349_naturalness.json")))
    aud = json.load(open(os.path.join(here, "2349_audits.json")))
    xe = nat["audited_extended@alpha=1 (natural)"]["x"]
    bc = aud["audited_central_depth"]
    stored = {
      "kin_extended_natural": (0.0, 10**xe[0], xe[1], xe[2], "audited_extended"),
      "kin_central_depth": (bc["la"], 10**bc["ls"], bc["p"], bc["rs"], "audited_central")}
    out["as_stored"] = {}
    for name, (la, S0, p, rs, fr) in stored.items():
        gp = grade_point(kin_sig(la, S0, p, rs), fr)
        out["as_stored"][name] = gp
        print("[as-stored] %s: joint-anchor x%.2f (LeoII %.2f / Carina %.2f / "
              "Draco %.2f) rest x%.2f shape %s"
              % (name, gp["joint_anchor_viol"], gp["anchors"]["LeoII"],
                 gp["anchors"]["Carina"], gp["anchors"]["Draco"], gp["rest_viol"],
                 gp["monotone_shape"]))

    # (B) joint re-search: three anchors (U=2) + pin/LSB/cluster, per frame variant
    out["research"] = {}
    for frame in ("audited_central", "audited_extended"):
        best = {"joint": np.inf}
        for la in np.linspace(-2, 6, 9):
            sigf_cache = {}
            N, f, Ln, merr, _ = g1.distribution(10.0**la)
            keep = f >= 1e-6
            Narr, warr = N[keep], f[keep]/f[keep].sum()
            def obj(x):
                ls, p, rs = x
                if not (-6 <= ls <= 2 and 0 <= p <= 16 and 20 <= rs <= 120):
                    return 50.0
                sf = lambda v: g2.sigma_eff(Narr, warr, 10.0**ls, p, rs, v, False)[0]
                av = anchor_viol(sf); rv = rest_viol(sf, frame)
                return math.log(max(max(av.values()), rv))
            for seed in ([-4, 8, 25], [-5, 14, 30], [-3, 5, 40], [-4.5, 12, 60],
                         [-2.5, 10, 21]):
                r = minimize(obj, seed, method="Nelder-Mead",
                             options={"maxiter": 500, "xatol": 1e-4, "fatol": 1e-7})
                jv = math.exp(r.fun)
                if jv < best["joint"]:
                    sf = kin_sig(float(la), 10.0**r.x[0], float(r.x[1]), float(r.x[2]))
                    gp = grade_point(sf, frame)
                    best = {"joint": jv, "la": float(la), "ls": float(r.x[0]),
                            "p": float(r.x[1]), "rs": float(r.x[2]), "grade": gp}
        out["research"][frame] = best
        g = best["grade"]
        print("[re-search %s] joint x%.3f at alpha=1e%.2f S0=1e%.2f p=%.2f Rs=%.1f"
              % (frame, best["joint"], best["la"], best["ls"], best["p"], best["rs"]))
        print("   anchors: LeoII x%.2f Carina x%.2f Draco x%.2f | rest x%.2f | "
              "sig(21/48/58)=%.1f/%.1f/%.1f vs demand %.0f/%.0f/%.0f"
              % (g["anchors"]["LeoII"], g["anchors"]["Carina"], g["anchors"]["Draco"],
                 g["rest_viol"], g["band"][21.0]["sig"], g["band"][48.0]["sig"],
                 g["band"][58.0]["sig"], sigma_correa(21), sigma_correa(48),
                 sigma_correa(58)))

    # (C) envelope-on robustness row at each frame's best point
    out["envelope_row"] = {}
    for frame, b in out["research"].items():
        sf = kin_sig(b["la"], 10.0**b["ls"], b["p"], b["rs"], envelope=True)
        gp = grade_point(sf, frame)
        out["envelope_row"][frame] = {"joint": gp["joint"],
                                      "joint_anchor_viol": gp["joint_anchor_viol"]}
        print("[envelope-on %s] joint x%.3f (anchors x%.3f)"
              % (frame, gp["joint"], gp["joint_anchor_viol"]))

    json.dump(out, open(os.path.join(here, "2351_results.json"), "w"), indent=1)
    print("saved 2351_results.json")
