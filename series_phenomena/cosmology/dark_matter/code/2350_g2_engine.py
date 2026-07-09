#!/usr/bin/env python3
# 2350 -- G2 SATELLITE-SURVIVAL COUNTER-CHECK (engine). Protocol and outcomes
# pre-registered in code/2350_PREREG.md BEFORE this ran. Sources (class-level
# bars, provenance carried): Ando+25 arXiv:2503.13650; Nadler+21 2108.03243;
# SIDM Concerto Nadler/Kong/Yang/Yu 2025 arXiv:2503.10748.
# Leg A: evaporation sigma_eff at host-orbit velocities, bar <= 3 cm^2/g @ 300 & 500.
# Leg B: branch placement (velocity power, UFD/dwarf magnitudes vs Concerto class).
# Leg C: the 1856 transport proxy envelope (measured eps(N), 2350_eps_A.json),
#        floors NOT suppressed (the 1870/71 floor MC already carried rod geometry).

import json, math, os
import numpy as np
from scipy.optimize import minimize
import importlib.util as iu

here = os.path.dirname(os.path.abspath(__file__))
spec = iu.spec_from_file_location("g1", os.path.join(here, "2349_g1_engine.py"))
g1 = iu.module_from_spec(spec); spec.loader.exec_module(g1)

# ---- eps(N) proxy from the registered 1856 rig (measured this patch) ----
er = json.load(open(os.path.join(here, "2350_eps_A.json")))
_A = np.array(sorted(float(a) for a in er)); _E = np.array([er[str(a) if str(a) in er else repr(a)]["eps"] if False else er[[k for k in er if float(k)==a][0]]["eps"] for a in _A])
def eps_N(N):
    A = np.asarray(N, dtype=float) / 4.0
    return np.interp(A, _A, _E)          # clamped at ends by np.interp

FL30 = g1.FL  # anchor floors (registered velocities)
def floor_at(v):
    # floors measured at 30/50/200/1500; log-log interp between, clamp outside
    vv = np.array([30.0, 50.0, 200.0, 1500.0])
    ff = np.array([g1.FL[30], g1.FL[50], g1.FL[200], g1.FL[1500]])
    return float(np.exp(np.interp(math.log(v), np.log(vv), np.log(ff))))

def sigma_eff(Narr, warr, S0, p, Rs, v, envelope=False):
    """sigma_T/m at arbitrary velocity v; optional 1856 eps(N) envelope on the
    interaction channels (floors unsuppressed)."""
    Narr = np.asarray(Narr, dtype=float); warr = np.asarray(warr, dtype=float)
    M = Narr * g1.M_EL
    S = S0 * (Narr / 2.0) ** p
    i, j = np.triu_indices(len(Narr))
    Sij = np.sqrt(S[i] * S[j]); mu = M[i]*M[j]/(M[i]+M[j])
    wfac = np.where(i == j, warr[i]*warr[j]/M[i],
                    warr[i]*warr[j]*(1.0/M[i]+1.0/M[j]))
    b = (v / g1.C) ** 2
    ec = Sij / (0.5 * mu * b * Rs)
    sig = Rs * Rs * g1.F_of_eps(ec)
    if envelope:
        sig = sig * np.sqrt(eps_N(Narr[i]) * eps_N(Narr[j]))
    extrap = float((wfac * sig)[ec > 9.9e3].sum() / max((wfac*sig).sum(), 1e-300))
    return float((wfac * sig).sum() * g1.CONV0 + floor_at(v)), extrap

def sigma_eff_free(Ns, Ss, ws, Rs, v, envelope=False):
    """two-delta / free-coupled variant (2344/2345 stored configs)."""
    Narr = np.asarray(Ns, float); S = np.asarray(Ss, float); warr = np.asarray(ws, float)
    M = Narr * g1.M_EL
    i, j = np.triu_indices(len(Narr))
    Sij = np.sqrt(S[i]*S[j]); mu = M[i]*M[j]/(M[i]+M[j])
    wfac = np.where(i == j, warr[i]*warr[j]/M[i],
                    warr[i]*warr[j]*(1.0/M[i]+1.0/M[j]))
    b = (v/g1.C)**2
    ec = Sij/(0.5*mu*b*Rs)
    sig = Rs*Rs*g1.F_of_eps(ec)
    if envelope:
        sig = sig * np.sqrt(eps_N(Narr[i]) * eps_N(Narr[j]))
    return float((wfac*sig).sum()*g1.CONV0 + floor_at(v))

def dist_at(la):
    N, f, Ln, merr, _ = g1.distribution(10.0 ** la)
    keep = f >= 1e-6
    return N[keep], f[keep] / f[keep].sum()

# ---- candidate populations ----
nat = json.load(open(os.path.join(here, "2349_naturalness.json")))
aud = json.load(open(os.path.join(here, "2349_audits.json")))
ext2344 = json.load(open(os.path.join(here, "2344_extended_anneal.json")))
l4 = json.load(open(os.path.join(here, "2345_l4_results.json")))

xe = nat["audited_extended@alpha=1 (natural)"]["x"]
bc = aud["audited_central_depth"]
CANDS = {
 "kin_extended_natural": {"kind": "kin", "la": 0.0, "S0": 10**xe[0], "p": xe[1],
                          "Rs": xe[2], "frame": "audited_extended"},
 "kin_central_depth":    {"kind": "kin", "la": bc["la"], "S0": 10**bc["ls"],
                          "p": bc["p"], "Rs": bc["rs"], "frame": "audited_central"},
 "twodelta_2344":        {"kind": "free", "frame": "audited_extended",
                          "Ns": [ext2344["params"][0], ext2344["params"][1]],
                          "Ss": [ext2344["params"][2], ext2344["params"][3]],
                          "ws": [ext2344["params"][4], 1-ext2344["params"][4]],
                          "Rs": ext2344["params"][5]},
 "twodelta_2345_central":{"kind": "free", "frame": "audited_central",
                          "Ns": [l4["reopt_central"]["params"][0], l4["reopt_central"]["params"][1]],
                          "Ss": [l4["reopt_central"]["params"][2], l4["reopt_central"]["params"][3]],
                          "ws": [l4["reopt_central"]["params"][4], 1-l4["reopt_central"]["params"][4]],
                          "Rs": l4["reopt_central"]["params"][5]},
}

VLEGA = (250.0, 300.0, 400.0, 500.0)
VLEGB = (5.0, 10.0, 30.0, 200.0, 1500.0)
BAR_EVAP = 3.0        # cm^2/g at 300 and 500 (Nadler+21 class, conservative)
BAR_CONCERTO = 150.0  # cm^2/g dwarf-scale ceiling (Concerto sigma0 ~ 147 class)

def evaluate(name, c, envelope):
    if c["kind"] == "kin":
        Narr, warr = dist_at(c["la"])
        sf = lambda v: sigma_eff(Narr, warr, c["S0"], c["p"], c["Rs"], v, envelope)
        curve = {v: sf(v) for v in VLEGA + VLEGB}
        sig = {v: curve[v][0] for v in curve}
        extr = {v: curve[v][1] for v in VLEGB}
    else:
        sf = lambda v: sigma_eff_free(c["Ns"], c["Ss"], c["ws"], c["Rs"], v, envelope)
        sig = {v: sf(v) for v in VLEGA + VLEGB}
        extr = {}
    legA = {"sig": {int(v): sig[v] for v in VLEGA},
            "pass": sig[300.0] <= BAR_EVAP and sig[500.0] <= BAR_EVAP}
    s_lo = math.log(sig[30.0]/sig[200.0]) / math.log(200.0/30.0)
    s_hi = math.log(sig[200.0]/sig[1500.0]) / math.log(1500.0/200.0)
    legB = {"s_eff_30_200": s_lo, "s_eff_200_1500": s_hi,
            "sig5": sig[5.0], "sig10": sig[10.0], "sig30": sig[30.0],
            "extrap_share": extr,
            "B1_vel_dep": s_lo >= 1.0,
            "B2_concerto": sig[10.0] <= BAR_CONCERTO and sig[30.0] <= BAR_CONCERTO,
            "B3_collapse_shape": sig[5.0] >= sig[10.0] >= sig[30.0]}
    legB["pass"] = legB["B1_vel_dep"] and legB["B2_concerto"] and legB["B3_collapse_shape"]
    # anchor windows at the candidate's frame under this envelope setting
    fr = g1.FRAMES[c["frame"]]
    if c["kind"] == "kin":
        tot = {int(v): sig[v] for v in (30.0, 50.0, 200.0, 1500.0) if v in sig}
        tot[50] = sf(50.0)[0]
    else:
        tot = {int(v): sig[v] for v in (30.0, 200.0, 1500.0)}
        tot[50] = sf(50.0)
    viol = g1.violation(tot, fr)
    return {"legA": legA, "legB": legB, "windows_viol": viol,
            "totals": {k: tot[k] for k in sorted(tot)}}

def research_under_envelope(frame):
    """re-search the G1 knob box with the eps(N) envelope ON, for one frame."""
    fr = g1.FRAMES[frame]
    best = {"viol": np.inf}
    for la in np.linspace(-2, 6, 9):
        Narr, warr = dist_at(float(la))
        def obj(x):
            ls, p, rs = x
            if not (-6 <= ls <= 2 and 0 <= p <= 16 and 20 <= rs <= 120): return 50.0
            tot = {int(v): sigma_eff(Narr, warr, 10.0**ls, p, rs, v, True)[0]
                   for v in (30.0, 50.0, 200.0, 1500.0)}
            return math.log(g1.violation(tot, fr))
        for seed in ([-4, 6, 25], [-5.4, 15, 30], [-3, 3, 40]):
            r = minimize(obj, seed, method="Nelder-Mead",
                         options={"maxiter": 400, "xatol": 1e-4, "fatol": 1e-7})
            v = math.exp(r.fun)
            if v < best["viol"]:
                best = {"viol": v, "la": float(la), "ls": float(r.x[0]),
                        "p": float(r.x[1]), "rs": float(r.x[2])}
    return best

if __name__ == "__main__":
    out = {"eps_N_table": {str(int(4*a)): float(e) for a, e in zip(_A, _E)}}
    for env in (False, True):
        key = "envelope_on" if env else "envelope_off"
        out[key] = {}
        for name, c in CANDS.items():
            out[key][name] = evaluate(name, c, env)
            e = out[key][name]
            print("[%s] %s: legA %s (300: %.2f, 500: %.2f) | legB %s (s_lo=%.2f, "
                  "sig10=%.1f) | windows viol %.3f @ %s"
                  % (key, name, "PASS" if e["legA"]["pass"] else "FAIL",
                     e["legA"]["sig"][300], e["legA"]["sig"][500],
                     "PASS" if e["legB"]["pass"] else "FAIL",
                     e["legB"]["s_eff_30_200"], e["legB"]["sig10"],
                     e["windows_viol"], c["frame"]))
    # re-search under envelope for any kinetic frame whose windows broke
    out["research"] = {}
    for name in ("kin_extended_natural", "kin_central_depth"):
        fr = CANDS[name]["frame"]
        if out["envelope_on"][name]["windows_viol"] > 1.0 + 1e-9:
            print("re-searching %s under envelope..." % fr)
            b = research_under_envelope(fr)
            out["research"][fr] = b
            print("  re-search best viol %.4f at alpha=1e%.2f S0=1e%.2f p=%.2f Rs=%.1f"
                  % (b["viol"], b["la"], b["ls"], b["p"], b["rs"]))
            if b["viol"] <= 1.0 + 1e-9:
                Narr, warr = dist_at(b["la"])
                sig = {v: sigma_eff(Narr, warr, 10.0**b["ls"], b["p"], b["rs"], v, True)[0]
                       for v in VLEGA + VLEGB}
                out["research"][fr]["legA_300_500"] = [sig[300.0], sig[500.0]]
                out["research"][fr]["legB_s_lo"] = math.log(sig[30.0]/sig[200.0])/math.log(200.0/30.0)
                out["research"][fr]["sig10"] = sig[10.0]
                print("  re-searched point: legA 300/500 = %.2f/%.2f, s_lo=%.2f, sig10=%.1f"
                      % (sig[300.0], sig[500.0], out["research"][fr]["legB_s_lo"], sig[10.0]))
    json.dump(out, open(os.path.join(here, "2350_results.json"), "w"), indent=1)
    print("saved 2350_results.json")
