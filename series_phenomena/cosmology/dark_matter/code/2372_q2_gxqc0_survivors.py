#!/usr/bin/env python3
"""Patch 2372 -- Q2: G-XQC-0 ON THE Q1 SURVIVORS (the S(N) arc's second cheap kill).
Question: do the dimer-free passing compositions clear the gate the dimer failed?

PRE-REGISTERED (fixed before run):
  Species: BOTH 2371 passing compositions, loaded from 2371_results.json (not
    hand-typed): extended (NA,NB,w) and central (NA,NB,w); w = mass fraction of
    species A per the 2344 eff() convention (verified against source pre-run).
  Bridge (registered, arc doc + 2366 precedent): per species N --
    M = N*1408 MeV; L = (N-1)*1.15 fm (J8 pin); E_rN = 3*E_c/(8N) * S_c
    (island convention per 1888); XQC-side mediator range stays the REGISTERED
    R_s = r_c/chi = 25.4 fm -- the Q1 mixture Rs (27, 90.6) is the OPEN-SS-43
    dSph-side screening parameter, a DIFFERENT quantity; the bridge rescales
    coupling and geometry only. Stated here so the convention is auditable.
  Grid (2366 bracket carried): sign in {attractive, repulsive};
    S_c in {0.012, 0.035, 0.05} (post-DAMIC island edges + ruling point);
    rho in {0.2, 0.3, 0.6} GeV/cm^3. Abundance per species: its Q1 mass
    fraction f x rho -- NDM = (f*rho*1e3/M)*2.5e10 (Erickcek normalization).
  Criterion: 1879's OWN per-bin conservative test, verbatim -- a bin with
    predicted > observed + 5*sqrt(observed+1) => EXCLUDED-class; all bins
    (incl. >4 keV) under => XQC-SAFE. No new criterion is introduced.
  Composition verdict at a (sign, S_c, rho) point: EXCLUDED-class if EITHER
    species violates at its required fraction; XQC-SAFE only if BOTH clear.
  HURTING-FIRST: the claim under test is survival, so the most-killing corner
    (S_c=0.05, rho=0.6) is computed first per species. The kill-side question
    (wholesale death) is decided at the weakest corner (S_c=0.012, rho=0.2);
    if a species is EXCLUDED at every grid point, an S_c boundary scan to
    0.006 (below the island floor; 2366b precedent) documents persistence.
  Physics stated both ways before running: heavier species deposit recoils in
    XQC's POPULATED bins (softer per-bin demand than the dimer's quiet-bin
    kill) but carry 1/M number density and larger per-particle sigma --
    genuinely open; neither direction is assumed.
  OUTCOMES (graded as written; (a) is the arc-hurting one):
    (a) every grid point EXCLUDED for BOTH compositions -> the small-N
        successor family dies wholesale at the same gate as the dimer; Q3 is
        NOT opened; the search escalates honestly.
    (b) at least one full composition XQC-SAFE at >=1 island point -> Q3 gets
        a live, gate-cleared target (composition + surviving points recorded).
    (c) mixed (one composition survives, one dies) -> the survivor defines
        Q3's target; the casualty is recorded.
  Alongside (record, not verdict): Stage-1 ceiling map -- sigma_T at 300 km/s
    on {atm 14.5, rock 22, Si 28.09}, per-nucleon-equivalent sigma_eff
    (Stage-1 convention), vs the 2365 ceilings {SNOLAB 8.9e-32, LSM 1.1e-31,
    MINOS 2.3e-30, surface 6.7e-29 cm^2} -- the underground-visibility
    question per species.
  VERIFY (3, pre-stated):
    (V-a) REGRESSION ANCHOR: the pipeline re-run at N=2 (attractive,
      S_c=0.012, f=0.94, rho=0.2) reproduces stored 2366b: violated_bins == 3
      AND total within 0.1% of 642.2190945369623.
    (V-b) BRIDGE: E_rN inside the pipeline equals the independent expression
      3*0.30/(8*N)*S_c at every evaluated species-point (exact).
    (V-c) CONVERGENCE (2368 audit class): at the heaviest species' hurting
      corner (N=NB_central, attractive, S_c=0.05, rho=0.6), violated-bin
      count unchanged and total rel dev <= 1% under each of: h 0.08->0.05,
      rmax 180->240, lmax cap +20.
"""
import math, sys, json, io, os, contextlib

here = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.dirname(here))  # dark_matter/ so 'code/...' paths match 2366 pattern

src = open('code/1879_xqc_recomputation.py').read().split("if __name__")[0]
g = {}; exec(src, g)
M_EL = g['M_EL']; E_C = g['E_C']; BINS = g['BINS']; SAT = g['SAT']
AMU = g['AMU']; HBARC = g['HBARC']; CKMS = g['CKMS']
PS_ORIG = g['phase_shifts']

Q1 = json.load(open('code/2371_results.json'))
comps = {}
for fname, tag in (("audited_extended", "extended"), ("audited_central", "central")):
    NA, NB, gA2, gB2, w, Rs = Q1[fname]["best_params"]
    comps[tag] = [(int(round(NA)), w), (int(round(NB)), 1.0 - w)]
print("Compositions loaded from 2371_results.json:")
for tag, sp in comps.items():
    print("  %-8s: " % tag + " + ".join("N=%d f=%.4f (M=%.0f MeV)" % (n, f, n*M_EL)
                                         for n, f in sp))

results = {"prereg": "header", "compositions": {t: [[n, f] for n, f in sp]
                                                for t, sp in comps.items()},
           "V": {}, "perbin": {}, "sigma_T": {}, "boundary_scan": {}}

def pin(N, sc, f_ab, rho_gev):
    g['N_ROD'] = N
    g['M_ROD'] = N * M_EL
    g['E_RN']  = (3.0 * E_C / (8 * N)) * sc
    g['L_ROD'] = (N - 1) * 1.15
    g['NDM']   = (f_ab * rho_gev * 1e3 / (N * M_EL)) * 2.5e10
    # V-b bridge assertion, exact
    assert g['E_RN'] == 3.0 * 0.30 / (8 * N) * sc

def perbin(N, sign, sc, f_ab, rho_gev):
    pin(N, sc, f_ab, rho_gev)
    with contextlib.redirect_stdout(io.StringIO()):
        counts, sat = g['predicted_bins'](-1 if sign == "attractive" else 1, True)
    viol = sum(1 for (lo, hi, obs, f), p in zip(BINS, counts)
               if p > obs + 5 * math.sqrt(obs + 1))
    sviol = bool(sat > SAT[1] + 5 * math.sqrt(SAT[1] + 1))
    vbins = [(lo, hi, round(p, 1), obs) for (lo, hi, obs, f), p in zip(BINS, counts)
             if p > obs + 5 * math.sqrt(obs + 1)]
    return viol, sviol, sum(counts) + sat, vbins

# ---- V-a: regression anchor (the dimer at 2366b's stored weak point) ----
v, sv, tot, _ = perbin(2, "attractive", 0.012, 0.94, 0.2)
STORED = 642.2190945369623
va_ok = (v == 3) and (not sv) and (abs(tot - STORED) / STORED < 1e-3)
results["V"]["a_regression"] = {"viol": v, "total": tot, "stored": STORED,
                                "rel_dev": abs(tot - STORED) / STORED, "ok": va_ok}
print("\nV-a regression anchor (dimer, attractive, Sc=0.012, f=0.94, rho=0.2): "
      "viol=%d (stored 3), total=%.3f (stored %.3f, rel dev %.1e) -> %s"
      % (v, tot, STORED, abs(tot - STORED) / STORED, "OK" if va_ok else "FAIL"))

# ---- main grid, hurting-first ----
SCS = (0.05, 0.035, 0.012)           # descending: most-killing first
RHOS = (0.6, 0.3, 0.2)
print("\n" + "=" * 96)
print(" G-XQC-0 per species (1879 per-bin criterion at required abundance)")
print("=" * 96)
species_all_excluded = {}
for tag, sp in comps.items():
    for N, f in sp:
        excl_everywhere = True
        for sign in ("attractive", "repulsive"):
            for sc in SCS:
                for rho in RHOS:
                    v, sv, tot, vb = perbin(N, sign, sc, f, rho)
                    verdict = "EXCLUDED-class" if (v > 0 or sv) else "XQC-SAFE"
                    if verdict == "XQC-SAFE": excl_everywhere = False
                    key = "%s,N=%d,f=%.4f,%s,Sc=%s,rho=%s" % (tag, N, f, sign, sc, rho)
                    results["perbin"][key] = {"violated_bins": v, "sat_violated": sv,
                                              "total": tot, "verdict": verdict,
                                              "worst_bins": vb[:3]}
                    print("%-9s N=%d f=%.3f %-10s Sc=%-5s rho=%-3s  viol=%2d sat=%-5s "
                          "total=%9.1f  %s" % (tag, N, f, sign, sc, rho, v, sv, tot, verdict))
        species_all_excluded["%s,N=%d" % (tag, N)] = excl_everywhere

# ---- composition verdicts per grid point ----
print("\n" + "=" * 96)
print(" COMPOSITION verdicts (EXCLUDED if either species violates at its fraction)")
print("=" * 96)
results["composition_verdicts"] = {}
comp_safe_points = {t: [] for t in comps}
for tag, sp in comps.items():
    for sign in ("attractive", "repulsive"):
        for sc in SCS:
            for rho in RHOS:
                bad = False
                for N, f in sp:
                    key = "%s,N=%d,f=%.4f,%s,Sc=%s,rho=%s" % (tag, N, f, sign, sc, rho)
                    if results["perbin"][key]["verdict"] == "EXCLUDED-class": bad = True
                verdict = "EXCLUDED-class" if bad else "XQC-SAFE"
                results["composition_verdicts"]["%s,%s,Sc=%s,rho=%s" % (tag, sign, sc, rho)] = verdict
                if not bad: comp_safe_points[tag].append((sign, sc, rho))
                print("%-9s %-10s Sc=%-5s rho=%-3s  %s" % (tag, sign, sc, rho, verdict))

# ---- Stage-1 ceiling map (record) ----
VREF = 300.0
CEIL = {"SNOLAB": 8.9e-32, "LSM": 1.1e-31, "MINOS": 2.3e-30, "surface": 6.7e-29}
targets = {"atm14.5": (14.5, 14.5 * AMU), "rock22": (22.0, 22.0 * AMU),
           "Si28": (28.09, 28.09 * AMU)}
def sigma_T(N, A_nuc, m_nuc, sign, sc):
    pin(N, sc, 1.0, 0.3)  # abundance irrelevant to sigma
    M = N * M_EL
    mu_ = M * m_nuc / (M + m_nuc)
    k = mu_ * (VREF / CKMS) / HBARC
    V = g['make_V'](A_nuc, sign)
    lmax = max(12, int(k * 60) + 10)
    d = PS_ORIG(V, mu_, k, lmax)
    s = sum((l + 1) * math.sin(d[l] - d[l + 1]) ** 2 for l in range(len(d) - 1))
    return 4 * math.pi / (k * k) * s  # fm^2

print("\n" + "=" * 96)
print(" Stage-1 ceiling map (sigma_eff per-nucleon-equivalent, cm^2; ceilings: "
      "SNOLAB 8.9e-32 LSM 1.1e-31 MINOS 2.3e-30 surface 6.7e-29)")
print("=" * 96)
Ns_unique = sorted({N for sp in comps.values() for N, f in sp})
for N in Ns_unique:
    M = N * M_EL
    mu_n = M * 0.9383e3 / (M + 0.9383e3)
    for sign, sgn in (("attractive", -1), ("repulsive", +1)):
        for sc in (0.012, 0.035, 0.05):
            row = {}
            for tn, (A, mA) in targets.items():
                st = sigma_T(N, A, mA, sgn, sc) * 1e-26
                mu_A = M * mA / (M + mA)
                seff = st / (A ** 2 * (mu_A / mu_n) ** 2)
                row[tn] = seff
            smin, smax = min(row.values()), max(row.values())
            above_all = smin > CEIL["surface"]
            below_deep = smax < CEIL["SNOLAB"]
            tagc = ("OVERBURDEN-BLIND (above surface ceiling)" if above_all else
                    ("below deep ceilings (underground-visible window)" if below_deep
                     else "straddles ceilings"))
            results["sigma_T"]["N=%d,%s,Sc=%s" % (N, sign, sc)] = \
                {"sigma_eff_cm2": row, "class": tagc}
            print("N=%d %-10s Sc=%-5s  sigma_eff %.2e - %.2e  %s"
                  % (N, sign, sc, smin, smax, tagc))

# ---- boundary scan for any species excluded everywhere ----
for skey, dead in species_all_excluded.items():
    if not dead: continue
    tag, Ns = skey.split(","); N = int(Ns.split("=")[1])
    f = dict((n, ff) for n, ff in comps[tag])[N]
    print("\nboundary scan (%s N=%d, weakest corner f=%.4f rho=0.2):" % (tag, N, f))
    for sign in ("attractive", "repulsive"):
        for sc in (0.012, 0.010, 0.008, 0.006):
            v, sv, tot, _ = perbin(N, sign, sc, f, 0.2)
            lab = "island" if sc >= 0.012 else "BELOW-island"
            results["boundary_scan"]["%s,N=%d,%s,Sc=%s" % (tag, N, sign, sc)] = \
                {"violated_bins": v, "total": tot}
            print("  %-10s Sc=%-6s viol=%2d total=%9.1f [%s]" % (sign, sc, v, tot, lab))

# ---- V-c: convergence audit at heaviest species' hurting corner ----
Nh = max(Ns_unique)
fh = None
for tag, sp in comps.items():
    for N, f in sp:
        if N == Nh: fh = f
base_v, base_sv, base_tot, _ = perbin(Nh, "attractive", 0.05, fh, 0.6)
vc = {"base": {"viol": base_v, "total": base_tot}}
variations = {
    "h_0.05":    lambda V, mu, k, lmax: PS_ORIG(V, mu, k, lmax, rmax=180.0, h=0.05),
    "rmax_240":  lambda V, mu, k, lmax: PS_ORIG(V, mu, k, lmax, rmax=240.0, h=0.08),
    "lmax_+20":  lambda V, mu, k, lmax: PS_ORIG(V, mu, k, min(lmax + 20, 90), rmax=180.0, h=0.08),
}
vc_ok = True
for name, fn in variations.items():
    g['phase_shifts'] = fn
    v, sv, tot, _ = perbin(Nh, "attractive", 0.05, fh, 0.6)
    g['phase_shifts'] = PS_ORIG
    rel = abs(tot - base_tot) / base_tot
    ok = (v == base_v) and (rel <= 0.01)
    vc_ok &= ok
    vc[name] = {"viol": v, "total": tot, "rel_dev": rel, "ok": ok}
    print("V-c %-9s: viol=%d (base %d) total=%.1f rel_dev=%.2e -> %s"
          % (name, v, base_v, tot, rel, "OK" if ok else "FAIL"))
results["V"]["c_convergence"] = vc
results["V"]["b_bridge_asserted"] = True   # every pin() asserted; reaching here = passed
results["V"]["passed"] = "%d/3" % (int(va_ok) + 1 + int(vc_ok))

# ---- outcome grading, as written ----
ext_safe = comp_safe_points["extended"]; cen_safe = comp_safe_points["central"]
if not ext_safe and not cen_safe:
    outcome = "(a) WHOLESALE: every grid point EXCLUDED for both compositions"
elif ext_safe and cen_safe:
    outcome = "(b) BOTH compositions XQC-SAFE at >=1 island point"
elif ext_safe or cen_safe:
    survivor = "extended" if ext_safe else "central"
    outcome = "(c) MIXED: %s survives; the other composition dies at the gate" % survivor
results["safe_points"] = {t: [list(x) for x in v] for t, v in comp_safe_points.items()}
results["OUTCOME"] = outcome
print("\nVERIFY:", results["V"]["passed"], "| OUTCOME:", outcome)
json.dump(results, open("code/2372_results.json", "w"), indent=1)
print("wrote code/2372_results.json")
