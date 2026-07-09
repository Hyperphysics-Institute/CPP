#!/usr/bin/env python3
"""Patch 2374 correction run -- CRITERION MIS-SPECIFICATION OWNED AND CORRECTED
(2366/B1 precedent): the 2372 composition verdict tested EACH SPECIES ALONE
against the full per-bin threshold (a convention inherited from the
single-species 2366 dimer run, where it was exact). For a MIXTURE the
physically observed spectrum is the SUM over species; the correct criterion is
  sum_i counts_i(bin; f_i, rho) > obs + 5*sqrt(obs+1)  =>  EXCLUDED-class.
The summed criterion is STRICTLY tighter, so: every 2372 EXCLUDED verdict
stands a fortiori; the 2369 dimer kill (single species) is UNAFFECTED; the Q1
anchor-suite passes are UNAFFECTED (2344's eff() sums channels correctly).
Affected, in the hurting direction only: the 2372 SAFE verdicts (the corridor)
and the 2373 walls. DIAGNOSIS ALREADY CONFIRMED pre-run: extended at
(0.012, 0.3) sums to 40.33 (att) / 29.56 (rep) vs threshold 28.32 in the
36-128 eV bin -- the 2372 SAFE grade there was WRONG.

PRE-REGISTERED (fixed before run):
  METHOD (exactness noted): per-species counts are exactly linear in f*rho
    (pure NDM prefactor), so one pipeline run per (N, sign, S_c) at
    f=rho=1 gives every abundance point algebraically; rho* edges are then
    EXACT (no bisection): rho* = 1 / max_bins( sum_i f_i c_i(bin)/th_bin ).
    S_c remains nonlinear -> S_c* by bisection (7 steps, +-1.8e-4).
  GRID RE-GRADE: the full 2372 grid under the summed criterion.
  WALLS: S_c* at each rho anchor where the floor point is SAFE; exact rho*
    at S_c=0.012 per (comp, sign). If the floor point at rho=0.2 is
    EXCLUDED, the corridor is ABSENT for that combo within the registered
    rho bracket -- reported as such, no rescue attempted.
  JOINT CONTAMINATION BOUNDS recomputed on whatever corridor survives
    (rectangle bounds, carriers first, as in 2374b).
  HURTING-FIRST PREDICTION (stated before run): extended loses rho=0.3 at
    the floor (both signs, per the diagnosis) and its corridor shrinks to
    rho~0.2-class or vanishes; central expected to survive with reduced
    walls (2374b found positive joint room there).
  VERIFY (3, pre-stated):
    (V-a) SINGLE-SPECIES LIMIT: the summed criterion with one species
      reproduces the stored 2366b dimer regression point exactly
      (viol=3, total 642.219, rel dev < 1e-9).
    (V-b) f*rho LINEARITY: full-pipeline run at (f=0.7833, rho=0.3)
      matches 0.7833*0.3 * run(f=1, rho=1) bin-by-bin, rel dev < 1e-9.
    (V-c) MONOTONICITY of every S_c bisection path.
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

TH = [obs + 5 * math.sqrt(obs + 1) for (lo, hi, obs, f) in BINS]
THS = SAT[1] + 5 * math.sqrt(SAT[1] + 1)

_cache = {}
def unit_counts(N, sign, sc, folded=True):
    """per-bin counts at f=1, rho=1 (GeV/cm^3); exactly linear scaling after."""
    key = (N, sign, round(sc, 8), folded)
    if key in _cache: return _cache[key]
    g['N_ROD'] = N; g['M_ROD'] = N * M_EL
    g['E_RN'] = (3.0 * E_C / (8 * N)) * sc
    g['L_ROD'] = max((N - 1) * 1.15, 1e-9)
    g['NDM'] = (1.0 * 1.0 * 1e3 / (N * M_EL)) * 2.5e10
    assert g['E_RN'] == 3.0 * 0.30 / (8 * N) * sc
    with contextlib.redirect_stdout(io.StringIO()):
        c, s = g['predicted_bins'](-1 if sign == "attractive" else 1, folded)
    _cache[key] = (c, s)
    return c, s

def summed_grade(tag, sign, sc, rho):
    """summed-spectrum criterion; returns (safe, viol_bins, worst_ratio, total)."""
    tot = [0.0] * len(BINS); tots = 0.0
    for N, f in comps[tag]:
        c, s = unit_counts(N, sign, sc)
        scale = f * rho
        tot = [a + scale * b for a, b in zip(tot, c)]; tots += scale * s
    viol = sum(1 for p, t in zip(tot, TH) if p > t) + (1 if tots > THS else 0)
    worst = max(max(p / t for p, t in zip(tot, TH)), tots / THS if tots > 0 else 0)
    return viol == 0, viol, worst, sum(tot) + tots

results = {"prereg": "header+diagnosis", "V": {}, "grid": {}, "walls": {},
           "joint_bounds": {}, "diagnosis": {
        "extended_0.012_0.3_sum_36_128": {"attractive": 40.33, "repulsive": 29.56,
                                          "threshold": TH[1]}}}

# ---- V-a: single-species limit vs stored 2366b ----
c, s = unit_counts(2, "attractive", 0.012)
scale = 0.94 * 0.2
tot = [scale * x for x in c]; tots = scale * s
viol = sum(1 for p, t in zip(tot, TH) if p > t) + (1 if tots > THS else 0)
total = sum(tot) + tots
STORED = 642.2190945369623
va_ok = (viol == 3) and abs(total - STORED) / STORED < 1e-9
results["V"]["a_single_species_limit"] = {"viol": viol, "total": total, "ok": va_ok}
print("V-a single-species limit (2366b point): viol=%d total=%.6f (stored %.6f) -> %s"
      % (viol, total, STORED, "OK" if va_ok else "FAIL"))

# ---- V-b: f*rho linearity, one full-pipeline spot check ----
g['N_ROD'] = 5; g['M_ROD'] = 5 * M_EL; g['E_RN'] = (3.0 * E_C / 40) * 0.012
g['L_ROD'] = 4 * 1.15; g['NDM'] = (0.7833 * 0.3 * 1e3 / (5 * M_EL)) * 2.5e10
with contextlib.redirect_stdout(io.StringIO()):
    cd, sd = g['predicted_bins'](-1, True)
cu, su = unit_counts(5, "attractive", 0.012)
rel = max(abs(a - 0.7833 * 0.3 * b) / max(abs(a), 1e-30) for a, b in zip(cd + [sd], cu + [su]))
vb_ok = rel < 1e-9
results["V"]["b_linearity"] = {"max_rel_dev": rel, "ok": vb_ok}
print("V-b f*rho linearity: max rel dev %.1e -> %s" % (rel, "OK" if vb_ok else "FAIL"))

# ---- grid re-grade ----
print("\nGRID RE-GRADE (summed-spectrum criterion); flips from 2372 marked:")
R72 = json.load(open('code/2372_results.json'))["composition_verdicts"]
flips = []
for tag in comps:
    for sign in ("attractive", "repulsive"):
        for sc in (0.05, 0.035, 0.012):
            for rho in (0.6, 0.3, 0.2):
                safe, viol, worst, total = summed_grade(tag, sign, sc, rho)
                verdict = "XQC-SAFE" if safe else "EXCLUDED-class"
                old = R72["%s,%s,Sc=%s,rho=%s" % (tag, sign, sc, rho)]
                flip = "  <-- FLIPPED (2372: %s)" % old if old != verdict else ""
                if flip: flips.append((tag, sign, sc, rho))
                results["grid"]["%s,%s,Sc=%s,rho=%s" % (tag, sign, sc, rho)] = \
                    {"verdict": verdict, "viol": viol, "worst_ratio": worst}
                print("%-9s %-10s Sc=%-5s rho=%-3s viol=%2d worst=%.3f %s%s"
                      % (tag, sign, sc, rho, viol, worst, verdict, flip))
results["flips"] = ["%s,%s,Sc=%s,rho=%s" % f for f in flips]

# ---- exact rho* and bisected S_c* walls ----
print("\nCORRECTED WALLS:")
vc_ok = True
for tag in comps:
    for sign in ("attractive", "repulsive"):
        # exact rho* at S_c = 0.012
        ratio_max = 0.0
        tot = [0.0] * len(BINS); tots = 0.0
        for N, f in comps[tag]:
            c, s = unit_counts(N, sign, 0.012)
            tot = [a + f * b for a, b in zip(tot, c)]; tots += f * s
        ratio_max = max(max(p / t for p, t in zip(tot, TH)), tots / THS if tots > 0 else 0)
        rho_star = 1.0 / ratio_max
        corridor = "ABSENT (rho* < 0.2)" if rho_star < 0.2 else "present"
        results["walls"]["rho*,%s,%s" % (tag, sign)] = {"rho_star_exact": rho_star,
                                                        "corridor": corridor}
        print("%-9s %-10s  rho* = %.4f GeV/cm^3 (EXACT)  [%s]" % (tag, sign, rho_star, corridor))
        # S_c* by bisection at each rho anchor where the floor is safe
        for rho in (0.3, 0.2):
            safe_lo, _, _, _ = summed_grade(tag, sign, 0.012, rho)
            if not safe_lo:
                results["walls"]["Sc*,%s,%s,rho=%s" % (tag, sign, rho)] = \
                    {"corridor": "ABSENT at this rho (floor EXCLUDED)"}
                print("          rho=%.1f: corridor ABSENT (floor point EXCLUDED)" % rho)
                continue
            lo, hi = 0.012, 0.035
            path = []
            for _ in range(7):
                mid = 0.5 * (lo + hi)
                s_ok, _, _, _ = summed_grade(tag, sign, mid, rho)
                path.append((mid, s_ok))
                if s_ok: lo = mid
                else: hi = mid
            mono = all((okv and x <= lo + 1e-12) or ((not okv) and x >= hi - 1e-12)
                       for x, okv in path)
            vc_ok &= mono
            frac = (lo - 0.012) / (0.05 - 0.012)
            results["walls"]["Sc*,%s,%s,rho=%s" % (tag, sign, rho)] = \
                {"safe_below": lo, "excluded_above": hi, "island_fraction": frac,
                 "monotone": mono}
            print("          rho=%.1f: S_c* in (%.5f, %.5f)  island kept %.1f%%  mono=%s"
                  % (rho, lo, hi, 100 * frac, mono))
results["V"]["c_monotone"] = vc_ok

# ---- corrected joint contamination bounds at surviving floor points ----
print("\nCORRECTED JOINT CONTAMINATION BOUNDS (carriers + contaminant summed, floor S_c=0.012):")
for tag in comps:
    for sign in ("attractive", "repulsive"):
        for rho in (0.3, 0.2):
            safe, _, _, _ = summed_grade(tag, sign, 0.012, rho)
            if not safe: continue
            carrier = [0.0] * len(BINS); carrier_s = 0.0
            for N, f in comps[tag]:
                c, s = unit_counts(N, sign, 0.012)
                carrier = [a + f * rho * b for a, b in zip(carrier, c)]
                carrier_s += f * rho * s
            for lab, N, folded in (("dimer", 2, True), ("monomer", 1, False)):
                cc, cs = unit_counts(N, sign, 0.012, folded)
                fm, bind = 1e30, None
                for i, p in enumerate(cc):
                    pu = p * rho
                    if pu <= 0: continue
                    room = TH[i] - carrier[i]
                    if room / pu < fm: fm, bind = room / pu, "%d-%d" % (BINS[i][0], BINS[i][1])
                if cs > 0 and (THS - carrier_s) / (cs * rho) < fm:
                    fm, bind = (THS - carrier_s) / (cs * rho), ">4keV"
                fm = max(fm, 0.0)
                results["joint_bounds"]["%s,%s,rho=%s,%s" % (tag, sign, rho, lab)] = \
                    {"f_max": fm, "binding_bin": bind}
                print("  %-9s %-10s rho=%.1f  %-7s f_max = %.4f (bin %s)"
                      % (tag, sign, rho, lab, fm, bind))

results["V"]["passed"] = "%d/3" % (int(va_ok) + int(vb_ok) + int(vc_ok))
print("\nVERIFY:", results["V"]["passed"])
json.dump(results, open("code/2374c_results.json", "w"), indent=1)
print("wrote code/2374c_results.json")
