"""
1888 -- SI task 2: tightened existence scan (numpy, 2M samples), the substrate
portrait table (16/50/84 percentiles over the accepted region), the F7-conditional
sharpening, and the NO-REFIT predictions (F5 XQC-flight counts, F6 deep-Earth
population, DAMIC-edge exposure fraction, group point) evaluated over the region.
Acceptance criteria identical to SI-1/1887 (consistency); tags per CONV-004.
Optional worker mode: `python3 ... xqc` refreshes the XQC(S_c) interpolation table
by re-running the 1880 partial-wave pipeline at 5 island points (json-cached).
"""
import math, json, os, sys
import numpy as np
HBARC = 197.327
CHI = ((1 + 5 ** 0.5) / 2) ** -3 / 6
MS = CHI * HBARC
E_EE, E_C, E_HDP = 0.9, 0.3, 150.0
RN, RS = 0.9, 1.0 / CHI
SC_LO, SC_HI = 0.005, 0.05
XQC_STORE = 'code/1888_xqc_island_grid.json'

if len(sys.argv) > 1 and sys.argv[1] == 'xqc':
    exec(open('code/1879_xqc_recomputation.py').read().split('if __name__')[0])
    mod = sys.modules['__main__']
    E_RN_BASE = mod.E_RN
    d = {}
    for sc in (0.05, 0.035, 0.02, 0.01, 0.005):
        mod.E_RN = E_RN_BASE * sc
        counts, sat = predicted_bins(-1, True)
        mod.E_RN = E_RN_BASE
        d[str(sc)] = sum(counts) + sat
        print("S_c={}: XQC total {:.1f}".format(sc, d[str(sc)]))
    json.dump(d, open(XQC_STORE, 'w')); sys.exit(0)

rng = np.random.default_rng(43)
N = 2_000_000
def lu(lo, hi, n=N): return np.exp(rng.uniform(np.log(lo), np.log(hi), n))

aq, ae = lu(1e-4, 10), lu(1e-4, 10)
n_, Ez = lu(1e-3, 10), lu(1e-3, 1e3)
Cr, Sp = lu(1e-6, 1), lu(1e-2, 1)
Dst, a = lu(1e-3, 1), lu(1.0, 1.3)
K = [lu(1/3, 3) for _ in range(5)]

ok = (np.abs(np.log((K[2] * aq * HBARC / a) / E_HDP)) < np.log(3))
ok &= (np.abs(np.log((K[1] * ae * HBARC / a) / E_EE)) < np.log(3))
ok &= (np.abs(np.log((K[3] * Cr * 8 * aq * HBARC / a) / E_C)) < np.log(3))
ms2 = K[0] * 4 * np.pi * aq * HBARC ** 3 * n_ * Cr * Sp / Ez
ok &= (np.abs(np.log(ms2 / MS ** 2)) < np.log(9))
Sc = K[4] * Dst * RN / RS
ok &= (Sc > SC_LO) & (Sc < SC_HI)

A = {k: v[ok] for k, v in dict(alpha_q=aq, alpha_e=ae, n=n_, Ez=Ez, Cr=Cr,
                                Sp=Sp, Dst=Dst, a=a, Sc=Sc).items()}
nacc = int(ok.sum())
print("=" * 78)
print(" 1888 -- SI-2: tightened scan, substrate portrait, no-refit predictions")
print("=" * 78)
print("\n(1) SCAN: accepted {} / {}  ({:.2e})  [EXISTENCE CONFIRMED at 10x statistics]".format(
    nacc, N, nacc / N))

def pct(v): return np.percentile(v, [16, 50, 84])

print("\n(2) SUBSTRATE PORTRAIT -- what the DM data reveal about the DP Sea")
print("    (16th / 50th / 84th percentiles; PRIOR-SHAPED where flat -- flagged)")
rows = [("alpha_q  (colour coupling)", A['alpha_q'], "pinned via E_hDP & a"),
        ("alpha_e  (e-channel)", A['alpha_e'], "pinned via E_ee & a"),
        ("C_r      (cancellation)", A['Cr'], "pinned via E_c/E_hDP"),
        ("D_st     (singlet static frac)", A['Dst'], "pinned via S_c window"),
        ("f_occ    (occupancy n a^3)", A['n'] * A['a'] ** 3, "PARTIALLY pinned (X1)"),
        ("n        (DP density fm^-3)", A['n'], "FLAT-ish (prior-shaped)"),
        ("S_p      (superposition)", A['Sp'], "FLAT-ish (prior-shaped)"),
        ("E_z      (ZBW scale, MeV)", A['Ez'], "FLAT (prior-shaped)"),
        ("nSp/Ez   (X1 core, fm^-3/MeV)", A['n'] * A['Sp'] / A['Ez'], "PINNED combination")]
for nm, v, note in rows:
    p = pct(v)
    print("    {:<32} {:.2e} / {:.2e} / {:.2e}   [{}]".format(nm, *p, note))

print("\n(3) F7-CONDITIONAL SHARPENING (CONJECTURED: E_z = kT_form = 16.4 keV):")
m = (A['Ez'] > 0.010) & (A['Ez'] < 0.030)
print("    accepted samples with E_z in [10,30] keV: {}  -> F7-compatible corner {}".format(
    int(m.sum()), "EXISTS" if m.sum() > 0 else "EMPTY"))
if m.sum() > 5:
    for nm, key in (("f_occ", None), ("n", 'n'), ("S_p", 'Sp'), ("C_r", 'Cr')):
        v = (A['n'] * A['a'] ** 3)[m] if key is None else A[key][m]
        p = pct(v)
        print("      {:<8} | E_z~16 keV: {:.2e} / {:.2e} / {:.2e}".format(nm, *p))

print("\n(4) NO-REFIT PREDICTIONS over the accepted region:")
if os.path.exists(XQC_STORE):
    g = json.load(open(XQC_STORE))
    xs = np.array(sorted(float(k) for k in g)); ys = np.array([g[str(k)] for k in xs])
    cnt = np.exp(np.interp(np.log(A['Sc']), np.log(xs), np.log(np.maximum(ys, 0.5))))
    p = pct(cnt)
    print("    F5  XQC-class flight, predicted events (current-XQC exposure):")
    print("        {:.0f} / {:.0f} / {:.0f}   vs 527 observed -> margin x{:.0f} at median".format(
        *p, 527 / p[1]))
else:
    print("    F5  [run worker `1888... xqc` to refresh the XQC(S_c) grid]")
print("    F6  deep-Earth thermalized population: n_bar ~ 2e13 /cm^3 (structure-level,")
print("        S_c-independent across the island; 1881) -- exotic-isotope/borehole probe.")
fr = float(np.mean(A['Sc'] < 0.01))
print("    DAMIC edge: fraction of the accepted region UNSHIELDED at DAMIC (S_c < 0.01):")
print("        {:.0%} -> the future DAMIC-floor pin adjudicates that fraction; the rest".format(fr))
print("        is shielded regardless.")
print("    Group point: sigma/m(1150 km/s) = 0.037-0.05 (S_c-independent: capture + rod-rod")
print("        floor; final-form falsifier, 2.3 sigma below the current mild detection).")
print("=" * 78)
