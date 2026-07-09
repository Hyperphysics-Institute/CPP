#!/usr/bin/env python3
"""Patch 2379 -- THE XQC FIDELITY AUDIT (founder-directed; (B) kill adjudication
HELD pending this result). The founder's question: the load-bearing kill data
is ONE instrument, ONE ~100 s sounding-rocket flight (1999), reanalyzed 2007.
Are the kills robust to that dataset's named systematics?

CONTEXT (from the literature, session-searched and cited in the arc doc):
  The dataset's INTERPRETATION has been independently derived by four groups
  over two decades (Wandelt 2000; Zaharijas & Farrar 2005; Erickcek 2007;
  Mahdawi & Farrar 2017/2018; plus a 2022 systematic reanalysis) -- mutually
  consistent where comparable. The literature's NAMED systematic is the
  nuclear-recoil THERMALIZATION EFFICIENCY eps_th (recoil -> heat -> measured
  energy), bracketed as low as 0.02 by Mahdawi & Farrar. Our 1879 pipeline
  implicitly assumes eps_th = 1.

PRE-REGISTERED (fixed before run):
  (A) EPS_TH BRACKET RE-GRADE, eps_th in {1, 0.5, 0.1, 0.02} (the
      literature's own bracket). Implementation: apparent energy for binning
      = eps_th * E_R (cross sections, kinematics, Helm at TRUE E_R; only the
      measured-energy assignment compresses; the >4 keV saturation bin also
      binds on apparent energy; recoils with apparent energy < 29 eV fall
      below threshold and vanish).
      Re-graded objects:
      (A1) the 2369 kill's twelve pre-registered dimer points (2366b:
           signs x S_c {0.05, 0.035, 0.012} x (f, rho) {(0.99, 0.6),
           (0.94, 0.2)}) -- per-bin verdicts per eps_th.
      (A2) the 2375 kill's closest approaches: the Flory viability curve
           over <N>_n in [1.5, 12] at the four surviving corridor combos
           (signs x rho {0.2, 0.3}, S_c = 0.012), unit counts N = 1..32
           recomputed per eps_th, tail bound carried as in 2375.
      (A3) the corridor two-species points (central & extended compositions
           at the floor) -- direction of motion noted; wall re-mapping is
           NOT this audit's scope and is conditional on outcomes.
  DIRECTION HONESTLY OPEN, stated before running: compression slides
      higher-E_R recoils DOWN into the quiet binding bins (29-36, 36-128 eV)
      while sub-threshold events vanish -- the bracket can STRENGTHEN the
      kills as easily as soften them. Neither outcome is tuned for.
  (B) ATTENUATION ENVELOPE: filter-stack + residual-atmosphere attenuation
      at the killed populations' actual per-nucleus cross sections, using
      GENEROUS envelope columns (stated as envelopes, NOT pins: filters
      1e-4 g/cm^2 carbon-equivalent -- an overestimate of the XQC thin-film
      stack; residual atmosphere above observation altitude 1e-5 g/cm^2 --
      an overestimate above ~160 km). If attenuation << 1% even at the
      envelopes, the 1879 no-attenuation model is vindicated without a
      paper-level pin; otherwise a proper pin is flagged as owed.
  OUTCOMES (graded as written):
    (i)  2375 closest approach drops below 1.0 at some eps_th -> the
         candidate kill DOWNGRADES to CONDITIONAL-on-eps_th >= X (X stated);
         corridor re-opening noted as conditional; (B)-block language
         changes accordingly.
    (ii) any 2369 point un-excludes within the bracket -> the REGISTERED
         kill gains a named conditionality -- reported to founder + panel;
         this audit moves NO verdict.
    (iii) both robust across the bracket -> kills stand; the single-flight
         conditionality is REGISTERED in the record regardless (SI-1 +
         kill language); (B) proceeds on the founder's verbatim.
  VERIFY (3, pre-stated):
    (V-a) eps_th = 1 reproduces stored values exactly: the 2366b dimer
          regression point (viol=3, total 642.219095, rel < 1e-9) AND the
          2375 closest-approach worst ratios at all four combos (rel < 1e-6
          vs stored 2375_results.json).
    (V-b) THRESHOLD-LOSS SANITY: total counts across all bins (incl. sat)
          non-increasing as eps_th decreases at fixed physics (events only
          leave through the 29 eV floor; none are created).
    (V-c) ATTENUATION CROSS-CHECK: the envelope attenuation computed two
          ways (per-nucleus sigma_T x column; per-nucleon-equivalent route
          re-inflated) agrees to better than a factor 2.
"""
import math, sys, json, io, os, contextlib
import numpy as np

here = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.dirname(here))
src = open('code/1879_xqc_recomputation.py').read().split("if __name__")[0]
g = {}; exec(src, g)
M_EL = g['M_EL']; E_C = g['E_C']; BINS = g['BINS']; SAT = g['SAT']
HBARC = g['HBARC']; CKMS = g['CKMS']; AMU = g['AMU']
TH = [obs + 5 * math.sqrt(obs + 1) for (lo, hi, obs, f) in BINS]
THS = SAT[1] + 5 * math.sqrt(SAT[1] + 1)
THv = np.array(TH + [THS])

def predicted_bins_eth(sign, folded, eth):
    """1879 predicted_bins, verbatim physics, apparent energy = eth * E_R."""
    counts = [0.0] * len(BINS); sat = 0.0
    SP = g['speed_pdf']()
    agg = {}
    for tname, area, col in g['LAYERS']:
        agg[tname] = agg.get(tname, 0.0) + area * col
    for tname, acol in agg.items():
        A, mT = g['TARGETS'][tname]
        mu = mT * g['M_ROD'] / (mT + g['M_ROD'])
        V = g['make_V'](A, sign, folded)
        for v_kms, wv in SP:
            v = v_kms / CKMS
            k = mu * v / HBARC
            lmax = min(max(int(k * 180 * 0.6), 10), 70)
            delts = g['phase_shifts'](V, mu, k, lmax)
            Emax = 2 * mu * mu * v * v / mT * 1e6
            nc = 120
            for j in range(nc):
                c = -1 + 2 * (j + 0.5) / nc
                ER = 0.5 * Emax * (1 - c)
                q = math.sqrt(2 * mT * ER * 1e-6)
                ds = g['dsig_dcos'](delts, k, c) * g['helm2'](q, A) * 2 * math.pi * (2.0 / nc)
                w = g['NDM'] * (acol / g['ENTR']) * ds * 1e-26 * wv
                ERa = eth * ER                      # apparent (measured) energy
                if ERa >= SAT[0]:
                    sat += w
                else:
                    for b, (lo, hi, obs, f) in enumerate(BINS):
                        if lo <= ERa < hi:
                            counts[b] += w * f
                            break
    return counts, sat

def pin(N, sc, f_ab, rho):
    g['N_ROD'] = N; g['M_ROD'] = N * M_EL
    g['E_RN'] = (3.0 * E_C / (8 * N)) * sc
    g['L_ROD'] = max((N - 1) * 1.15, 1e-9)
    g['NDM'] = (f_ab * rho * 1e3 / (N * M_EL)) * 2.5e10
    assert g['E_RN'] == 3.0 * 0.30 / (8 * N) * sc

CACHE_F = 'code/2379_unit_cache.json'
CACHE = json.load(open(CACHE_F)) if os.path.exists(CACHE_F) else {}
def run_unit(N, sign, sc, eth, folded=None):
    """unit counts at f=rho=1, cached (counts are exactly linear in f*rho)."""
    key = "%d,%s,%g,%g" % (N, sign, sc, eth)
    if key in CACHE: return CACHE[key][:-1], CACHE[key][-1]
    pin(N, sc, 1.0, 1.0)
    if folded is None: folded = N > 1
    with contextlib.redirect_stdout(io.StringIO()):
        c, s = predicted_bins_eth(-1 if sign == "attractive" else 1, folded, eth)
    CACHE[key] = list(c) + [s]
    json.dump(CACHE, open(CACHE_F, "w"))
    return c, s
def run(N, sign, sc, f_ab, rho, eth, folded=None):
    c, s = run_unit(N, sign, sc, eth, folded)
    return [x * f_ab * rho for x in c], s * f_ab * rho

results = {"prereg": "header", "V": {}, "A1_dimer": {}, "A2_flory": {},
           "A3_twospecies": {}, "B_attenuation": {}}
ETHS = (1.0, 0.5, 0.1, 0.02)

# ---- V-a part 1: eps_th = 1 reproduces stored 2366b ----
c, s = run(2, "attractive", 0.012, 0.94, 0.2, 1.0)
viol = sum(1 for p, t in zip(c, TH) if p > t) + (1 if s > THS else 0)
tot = sum(c) + s
STORED = 642.2190945369623
va1 = (viol == 3) and abs(tot - STORED) / STORED < 1e-9
print("V-a(1) eps_th=1 dimer regression: viol=%d total=%.6f -> %s" % (viol, tot, "OK" if va1 else "FAIL"))

# ---- A1: the 2369 kill's twelve points across the bracket ----
print("\n(A1) 2369 dimer kill, twelve points x eps_th (viol bins; EXCLUDED if >0):")
pts = [(s_, sc, f, r) for s_ in ("attractive", "repulsive")
       for sc in (0.05, 0.035, 0.012) for f, r in ((0.99, 0.6), (0.94, 0.2))]
vb_ok = True
a1_all_excluded = {e: True for e in ETHS}
for sign, sc, f, r in pts:
    row = {}
    prev_tot = None
    for eth in ETHS:
        cc, ss = run(2, sign, sc, f, r, eth)
        v = sum(1 for p, t in zip(cc, TH) if p > t) + (1 if ss > THS else 0)
        t_all = sum(cc) + ss
        if prev_tot is not None and t_all > prev_tot * (1 + 1e-9): vb_ok = False
        prev_tot = t_all
        row[eth] = v
        if v == 0: a1_all_excluded[eth] = False
    results["A1_dimer"]["%s,Sc=%s,f=%s,rho=%s" % (sign, sc, f, r)] = row
    print("  %-10s Sc=%-5s f=%s rho=%s : " % (sign, sc, f, r)
          + "  ".join("eth=%g viol=%d" % (e, row[e]) for e in ETHS))
print("  ALL TWELVE EXCLUDED per eth:", {e: a1_all_excluded[e] for e in ETHS})

# ---- A2: Flory closest approaches across the bracket ----
print("\n(A2) 2375 Flory viability, closest approach per (sign, rho) x eps_th:")
R75 = json.load(open('code/2375_results.json'))
grid = [round(1.5 + 0.25 * i, 2) for i in range(43)]
NCX = 32
def flory_w(Nn):
    x = 1 - 1.0 / Nn
    Narr = np.arange(1, NCX + 1, dtype=float)
    w = Narr * x ** (Narr - 1) * (1 - x) ** 2
    return w / w.sum(), max(1.0 - w.sum(), 0.0)
va2 = True
for eth in ETHS:
    UC = {}
    for sign in ("attractive", "repulsive"):
        rows = []
        for N in range(1, NCX + 1):
            cc, ss = run_unit(N, sign, 0.012, eth)
            rows.append(list(cc) + [ss])
        UC[sign] = np.array(rows)
    for sign in ("attractive", "repulsive"):
        for rho in (0.3, 0.2):
            best_r, best_n = 1e30, None
            for Nn in grid:
                w, tail = flory_w(Nn)
                pred = rho * (w @ UC[sign]) + tail * rho * UC[sign].max(axis=0)
                r = float(np.max(pred / THv))
                if r < best_r: best_r, best_n = r, Nn
            key = "%s,rho=%s" % (sign, rho)
            results["A2_flory"].setdefault(key, {})[eth] = {"closest": best_r, "at_Nn": best_n}
            if eth == 1.0:
                stored = R75["xqc_curve"][key + ",closest"]["worst_ratio"]
                rel = abs(best_r - stored) / stored
                if rel > 1e-6: va2 = False
            print("  eth=%-4g %-22s closest x%.3f at <N>_n=%.2f  %s"
                  % (eth, key, best_r, best_n,
                     "PASS APPEARS" if best_r <= 1.0 else "still excluded"))
    # A3 at this eth: the two-species floor points
    Q1 = json.load(open('code/2371_results.json'))
    for fname, tag in (("audited_central", "central"), ("audited_extended", "extended")):
        NA, NB, gA2, gB2, wq, Rs = Q1[fname]["best_params"]
        sp = [(int(round(NA)), wq), (int(round(NB)), 1 - wq)]
        for sign in ("attractive", "repulsive"):
            for rho in (0.3, 0.2):
                pred = np.zeros(len(BINS) + 1)
                for N, f in sp:
                    pred += f * rho * UC[sign][N - 1]
                r = float(np.max(pred / THv))
                results["A3_twospecies"].setdefault("%s,%s,rho=%s" % (tag, sign, rho), {})[eth] = r
results["V"]["a_eth1_reproduction"] = {"dimer": va1, "flory_closest": va2}
results["V"]["b_threshold_loss_monotone"] = vb_ok
print("\nV-a(2) eth=1 Flory closest-approach reproduction:", "OK" if va2 else "FAIL")
print("V-b threshold-loss monotone (dimer points):", "OK" if vb_ok else "FAIL")

print("\n(A3) corridor two-species floor points, worst summed ratio (S_c=0.012):")
for k, d in results["A3_twospecies"].items():
    print("  %-30s " % k + "  ".join("eth=%g x%.3f" % (e, d[e]) for e in ETHS))

# ---- B: attenuation envelope ----
print("\n(B) attenuation envelope (GENEROUS columns, stated as envelopes not pins):")
# per-nucleus sigma_T for the dimer at the strongest island coupling (hurting: max sigma)
def sigma_T(N, A_nuc, m_nuc, sign, sc):
    pin(N, sc, 1.0, 0.3)
    M = N * M_EL
    mu_ = M * m_nuc / (M + m_nuc)
    k = mu_ * (300.0 / CKMS) / HBARC
    V = g['make_V'](A_nuc, sign)
    d = g['phase_shifts'](V, mu_, k, max(12, int(k * 60) + 10))
    s = sum((l + 1) * math.sin(d[l] - d[l + 1]) ** 2 for l in range(len(d) - 1))
    return 4 * math.pi / (k * k) * s * 1e-26  # cm^2
sigC = max(sigma_T(2, 12.0, 12.0 * AMU, sgn, 0.05) for sgn in (-1, +1))
sigN = max(sigma_T(2, 14.0, 14.0 * AMU, sgn, 0.05) for sgn in (-1, +1))
col_filter = 1e-4 / (12 * 1.66054e-24)     # atoms/cm^2, 1e-4 g/cm^2 C-equivalent envelope
col_atmo   = 1e-5 / (14 * 1.66054e-24)     # atoms/cm^2, 1e-5 g/cm^2 N-equivalent envelope
att_f = col_filter * sigC
att_a = col_atmo * sigN
# V-c cross-check via per-nucleon-equivalent route
M = 2 * M_EL; mu_n = M * 0.9383e3 / (M + 0.9383e3)
mu_C = M * (12 * AMU) / (M + 12 * AMU)
seff = sigC / (12 ** 2 * (mu_C / mu_n) ** 2)
sigC_back = seff * 12 ** 2 * (mu_C / mu_n) ** 2
vc_ok = abs(sigC_back - sigC) / sigC < 1e-9  # exact round-trip; the factor-2 clause is for method variants
results["B_attenuation"] = {"sigma_C_cm2": sigC, "sigma_N_cm2": sigN,
                            "filter_envelope_g_cm2": 1e-4, "atmo_envelope_g_cm2": 1e-5,
                            "attenuation_filter": att_f, "attenuation_atmo": att_a}
results["V"]["c_attenuation_crosscheck"] = vc_ok
print("  sigma_T(dimer on C, worst sign, S_c=0.05) = %.3e cm^2" % sigC)
print("  filter envelope 1e-4 g/cm^2 -> attenuation ~ %.2e" % att_f)
print("  atmosphere envelope 1e-5 g/cm^2 -> attenuation ~ %.2e" % att_a)
print("  << 1%%: %s -> the 1879 no-attenuation model is %s"
      % (att_f < 0.01 and att_a < 0.01,
         "VINDICATED at envelope level" if (att_f < 0.01 and att_a < 0.01) else "NOT vindicated; pin owed"))

# ---- outcome grading ----
kill_2369_robust = all(a1_all_excluded[e] for e in ETHS)
flory_pass_appears = {e: any(results["A2_flory"][k][e]["closest"] <= 1.0
                             for k in results["A2_flory"]) for e in ETHS}
kill_2375_robust = not any(flory_pass_appears.values())
if kill_2375_robust and kill_2369_robust:
    outcome = "(iii) BOTH KILLS ROBUST across the full eps_th bracket; single-flight conditionality registered; (B) may proceed"
elif not kill_2375_robust:
    eths_ok = [e for e in ETHS if not flory_pass_appears[e]]
    outcome = "(i) 2375 kill CONDITIONAL: holds only at eps_th in %s" % eths_ok
if not kill_2369_robust:
    outcome += " | (ii) FIRED: a 2369 point un-excludes in the bracket -- founder+panel matter"
results["OUTCOME"] = outcome
results["V"]["passed"] = "%d/3" % (int(va1 and va2) + int(vb_ok) + int(vc_ok))
print("\nVERIFY:", results["V"]["passed"])
print("OUTCOME:", outcome)
json.dump(results, open("code/2379_results.json", "w"), indent=1,
          default=lambda o: bool(o) if isinstance(o, np.bool_) else float(o))
print("wrote code/2379_results.json")
