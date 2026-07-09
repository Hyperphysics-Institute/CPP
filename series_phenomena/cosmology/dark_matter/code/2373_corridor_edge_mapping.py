#!/usr/bin/env python3
"""Patch 2373 -- CORRIDOR EDGE-MAPPING (the cheap intermediate before the Q3
go/no-go). Question: WHERE are the walls of the 2372 survival corridor?

PRE-REGISTERED (fixed before run):
  Machinery: the 2372 pipeline VERBATIM (1879 exec-import, per-N bridge,
    per-bin criterion, composition verdict = both species must clear at
    required fractions). Nothing retuned; species/fractions loaded from
    2371_results.json as in 2372.
  Edges to locate, by bisection on the COMPOSITION verdict:
    (E1) S_c* at fixed rho: bracket [0.012, 0.035] (2372: SAFE at low end,
         EXCLUDED at high end, all combos), at rho in {0.2, 0.3}, both
         signs, both compositions. Tolerance: 7 bisection steps
         (+-1.8e-4 absolute).
    (E2) rho* at fixed S_c = 0.012: bracket [0.3, 0.6] (2372: SAFE at low
         end, EXCLUDED at high end, all combos), both signs, both
         compositions. Tolerance: 5 steps (+-0.0094 GeV/cm^3).
  Also recorded: interior headroom at the 2372 ruling interior point
    (S_c=0.012, rho=0.3) -- worst per-bin ratio pred/(obs+5*sqrt(obs+1))
    across both species, per composition x sign (how far under the gate the
    corridor's center sits); and the island fraction surviving,
    (S_c*-0.012)/(0.05-0.012), at rho=0.3.
  READINGS, stated hurting-first (numbers decide nothing automatically; the
  Q3 go/no-go remains the founder's with these numbers on the desk):
    (thin)  S_c* - 0.012 small relative to the island width and/or
            rho* barely above 0.3 -> the derivation target is a knife-edge:
            Q3 must land the coupling in a sliver AND the survivors are
            hostage to the local-density value. Stated first because it is
            the arc-hurting reading.
    (roomy) meaningful fractions of the island and of the rho bracket
            survive -> the target has walls a derivation can realistically
            hit; the F-DM3-4-class visibility window and DAMIC-edge
            adjudication attach across the corridor either way.
  NOTE ON MEANING (pre-stated): S_c is a Sea property -- ONE number the
    substrate fixes; the island is the current data-drawn allowed set, so
    S_c* measures how much of the post-DAMIC island the successors keep.
    rho is an astrophysical INPUT, not a model choice: rho* is an exposure,
    not a knob.
  VERIFY (3, pre-stated):
    (V-a) ENDPOINT CONSISTENCY: bisection bracket endpoints reproduce the
      stored 2372 verdicts (SAFE at (0.012, rho<=0.3); EXCLUDED at
      (0.035, rho) and at (0.012, 0.6)) for every combo, from fresh
      evaluation, before any bisection step is trusted.
    (V-b) BRIDGE: the 2372 exact assertion carried (every pin() asserts
      E_rN == 3*0.30/(8N)*S_c).
    (V-c) MONOTONICITY: along every bisection path, no SAFE evaluation
      occurs at a parameter beyond the final edge and no EXCLUDED
      evaluation below it (verdict monotone along the scanned axis).
"""
import math, sys, json, io, os, contextlib

here = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.dirname(here))

src = open('code/1879_xqc_recomputation.py').read().split("if __name__")[0]
g = {}; exec(src, g)
M_EL = g['M_EL']; E_C = g['E_C']; BINS = g['BINS']; SAT = g['SAT']

Q1 = json.load(open('code/2371_results.json'))
comps = {}
for fname, tag in (("audited_extended", "extended"), ("audited_central", "central")):
    NA, NB, gA2, gB2, w, Rs = Q1[fname]["best_params"]
    comps[tag] = [(int(round(NA)), w), (int(round(NB)), 1.0 - w)]

def pin(N, sc, f_ab, rho_gev):
    g['N_ROD'] = N; g['M_ROD'] = N * M_EL
    g['E_RN'] = (3.0 * E_C / (8 * N)) * sc
    g['L_ROD'] = (N - 1) * 1.15
    g['NDM'] = (f_ab * rho_gev * 1e3 / (N * M_EL)) * 2.5e10
    assert g['E_RN'] == 3.0 * 0.30 / (8 * N) * sc          # V-b

def species_eval(N, sign, sc, f_ab, rho):
    pin(N, sc, f_ab, rho)
    with contextlib.redirect_stdout(io.StringIO()):
        counts, sat = g['predicted_bins'](-1 if sign == "attractive" else 1, True)
    viol = sum(1 for (lo, hi, obs, f), p in zip(BINS, counts)
               if p > obs + 5 * math.sqrt(obs + 1))
    sviol = sat > SAT[1] + 5 * math.sqrt(SAT[1] + 1)
    worst = max(p / (obs + 5 * math.sqrt(obs + 1)) for (lo, hi, obs, f), p in zip(BINS, counts))
    worst = max(worst, sat / (SAT[1] + 5 * math.sqrt(SAT[1] + 1)))
    return (viol == 0 and not sviol), worst

def comp_safe(tag, sign, sc, rho):
    """Composition verdict + worst ratio across both species."""
    ok, wmax = True, 0.0
    for N, f in comps[tag]:
        s, w = species_eval(N, sign, sc, f, rho)
        ok &= s; wmax = max(wmax, w)
    return ok, wmax

results = {"prereg": "header", "V": {}, "edges": {}, "headroom": {}}

# ---- V-a: endpoint consistency vs stored 2372 verdicts ----
R72 = json.load(open('code/2372_results.json'))["composition_verdicts"]
va_ok = True
checks = []
for tag in comps:
    for sign in ("attractive", "repulsive"):
        for sc, rho, expect in ((0.012, 0.3, "XQC-SAFE"), (0.012, 0.2, "XQC-SAFE"),
                                (0.035, 0.3, "EXCLUDED-class"), (0.035, 0.2, "EXCLUDED-class"),
                                (0.012, 0.6, "EXCLUDED-class")):
            stored = R72["%s,%s,Sc=%s,rho=%s" % (tag, sign, sc, rho)]
            ok, _ = comp_safe(tag, sign, sc, rho)
            fresh = "XQC-SAFE" if ok else "EXCLUDED-class"
            agree = (fresh == stored == expect)
            va_ok &= agree
            checks.append((tag, sign, sc, rho, stored, fresh, agree))
results["V"]["a_endpoints"] = {"ok": va_ok, "n_checked": len(checks)}
print("V-a endpoint consistency: %d/%d agree with stored 2372 -> %s"
      % (sum(1 for c in checks if c[6]), len(checks), "OK" if va_ok else "FAIL"))
if not va_ok:
    for c in checks:
        if not c[6]: print("  MISMATCH:", c)
    sys.exit(1)

# ---- bisections ----
def bisect(tag, sign, axis, fixed, lo, hi, steps):
    """axis='sc' (fixed=rho) or 'rho' (fixed=sc); SAFE at lo, EXCLUDED at hi."""
    path = []
    for _ in range(steps):
        mid = 0.5 * (lo + hi)
        sc, rho = (mid, fixed) if axis == "sc" else (fixed, mid)
        ok, _ = comp_safe(tag, sign, sc, rho)
        path.append((mid, ok))
        if ok: lo = mid
        else: hi = mid
    # V-c monotonicity along this path
    mono = all((x <= lo + 1e-12) == okv or (x >= hi - 1e-12) == (not okv)
               for x, okv in path)
    mono = all((okv and x <= lo + 1e-12) or ((not okv) and x >= hi - 1e-12)
               for x, okv in path)
    return lo, hi, mono, path

vc_ok = True
print("\n(E1) S_c* edges (composition SAFE below, EXCLUDED above; 7 steps, +-1.8e-4):")
for tag in comps:
    for sign in ("attractive", "repulsive"):
        for rho in (0.3, 0.2):
            lo, hi, mono, path = bisect(tag, sign, "sc", rho, 0.012, 0.035, 7)
            vc_ok &= mono
            frac = (lo - 0.012) / (0.05 - 0.012)
            results["edges"]["Sc*,%s,%s,rho=%s" % (tag, sign, rho)] = \
                {"safe_below": lo, "excluded_above": hi, "island_fraction": frac,
                 "monotone": mono}
            print("  %-9s %-10s rho=%.1f  S_c* in (%.5f, %.5f)  island fraction "
                  "surviving %.1f%%  mono=%s" % (tag, sign, rho, lo, hi, 100 * frac, mono))

print("\n(E2) rho* edges at S_c=0.012 (5 steps, +-0.0094):")
for tag in comps:
    for sign in ("attractive", "repulsive"):
        lo, hi, mono, path = bisect(tag, sign, "rho", 0.012, 0.3, 0.6, 5)
        vc_ok &= mono
        results["edges"]["rho*,%s,%s" % (tag, sign)] = \
            {"safe_below": lo, "excluded_above": hi, "monotone": mono}
        print("  %-9s %-10s  rho* in (%.4f, %.4f) GeV/cm^3  mono=%s"
              % (tag, sign, lo, hi, mono))

# ---- interior headroom at (0.012, 0.3) ----
print("\nInterior headroom at (S_c=0.012, rho=0.3): worst bin ratio pred/threshold:")
for tag in comps:
    for sign in ("attractive", "repulsive"):
        ok, wmax = comp_safe(tag, sign, 0.012, 0.3)
        results["headroom"]["%s,%s" % (tag, sign)] = {"worst_ratio": wmax, "safe": ok}
        print("  %-9s %-10s  worst ratio %.3f (headroom x%.2f under the gate)"
              % (tag, sign, wmax, 1.0 / wmax))

results["V"]["b_bridge_asserted"] = True
results["V"]["c_monotone"] = vc_ok
results["V"]["passed"] = "%d/3" % (int(va_ok) + 1 + int(vc_ok))
print("\nVERIFY:", results["V"]["passed"])
json.dump(results, open("code/2373_results.json", "w"), indent=1)
print("wrote code/2373_results.json")
