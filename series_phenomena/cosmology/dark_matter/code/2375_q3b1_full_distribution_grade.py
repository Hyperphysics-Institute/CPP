#!/usr/bin/env python3
"""Patch 2375 -- Q3b-1: THE FULL-DISTRIBUTION GRADE (Flory family through BOTH
channels). Question: does ANY equilibrium-shaped (Flory/isodesmic) population
pass the anchor suite at the audited frames AND the summed-spectrum XQC gate
at the corridor? This is the computation the 2374 demand sheet named
cheap-first-and-can-kill: the isodesmic N>6 tail (67% of mass at <N>_n=6) was
ungraded in both channels.

PRE-REGISTERED (fixed before run):
  DISTRIBUTION: Flory mass fractions w(N) = N x^(N-1) (1-x)^2, x = 1-1/<N>_n,
    truncated at N_cut=32 and RENORMALIZED (conditioned on N<=N_cut); tail
    mass reported. Species N=1..32 (monomer POINT potential, as 2374).
  STRUCTURE (design fact, stated): the XQC side depends ONLY on the mass
    fractions -- the registered bridge uses island S_c, not the anchor
    couplings -- so XQC viability is a 1-D curve over <N>_n, computed FIRST;
    the anchor scan then runs over the XQC-viable window. Coupling
    consistency between anchor-side g^2 (machinery units) and XQC-side S_c
    is NOT enforced here because no registered map exists (2371 honest-limit
    carried); Q3c owns that joint, as it owns the absolute coupling.
  XQC SIDE: summed-spectrum per-bin criterion (2374c, verbatim) at the
    corridor floor S_c=0.012, rho in {0.2, 0.3}, both signs; per-species
    unit counts x Flory weights; truncation handled in the HURTING direction
    by a conservative additive tail bound: tail_mass * rho * max_N c_N(bin)
    added to every bin before grading. Curve over <N>_n in [1.5, 12],
    step 0.25.
  ANCHOR SIDE: eff() generalized to the distribution -- the exact N-species
    form implied by 2344's own two-species expression:
      sigma/m(v) = sum_ij w_i w_j s_ij(v) K_ij * CONV0 + FL[v],
      K_ij = (1/M_i + 1/M_j)/2,  s_ij = Rs^2 Fi(g_ij/(0.5 mu_ij b Rs)),
      g_ij = sqrt(g_i^2 g_j^2)   (reduces exactly to 2344 eff() at 2 species).
    Coupling law (the registered strain family): g^2(N) = g0^2 (N/4)^p.
    Scan: <N>_n uniform over the XQC-viable window (or [1.5,12] if that
    window is empty -- graded for the record); g0^2 log-uniform [1e-6,1e3];
    p uniform [0,14]; Rs log-uniform [20,100]. 30k wide + 6k anneal x2
    seeds from the best, per frame (budget reduced from 150k/20k for
    tractability at N_cut=96, DISCLOSED; seed-stability check retained);
    registered frame graded record-only. Per-eval species set adaptively
    trimmed to tail mass < 5e-4 then renormalized (V-c validates the final
    best point against N_cut=128). Violation = 2349-style factor via the 2345 frames (2371
    convention; viol <= 1 <=> pass).
  OUTCOMES (graded as written, hurting-first):
    (a) NO Flory point passes the anchor suite at either audited frame
        (any <N>_n) -> the equilibrium SHAPE fails the dSph channel; passing
        populations require a non-equilibrium distribution; death mode (ii)
        is REARMED at population level and Q3c is gated on deriving a
        non-Flory mechanism.
    (b) anchor passes exist ONLY at XQC-unviable <N>_n -> the family dies at
        the gate instead; same escalation, via F5's channel. CANDIDATE
        grading only -- panel verification before any registered claim.
    (c) joint passes exist -> Q3c inherits a fully-specified target
        (<N>_n, p, g0^2, Rs) + corridor point; the demanded steepness p is
        recorded against the registered strain family (2344's N^12; G1
        central p>=13).
  FIRST-RUN CATCH (documented per 2344's own precedent -- the verify
    machinery caught its author): with anchor-side N_cut=32 the extended-frame
    scan returned a "pass" at <N>_n=11.1 that V-c exposed as a TRUNCATION
    ARTIFACT (N_cut 32->48 shifted totals x1.42). Anchor-side N_cut raised to
    96 (tail at <N>_n=12: x^96 ~ 2e-4) BEFORE any result was recorded; the
    XQC side is unaffected (its additive tail bound is hurting-direction by
    construction).
  VERIFY (3, pre-stated):
    (V-a) TWO-SPECIES LIMIT: eff_dist with weight concentrated on the 2371
      best compositions (per-N g^2 injected directly, bypassing the power
      law) reproduces stored 2371 best_totals to rel < 1e-9, BOTH frames'
      compositions.
    (V-b) XQC SINGLE-SPECIES LIMIT: the summed machinery at the 2366b point
      reproduces viol=3, total 642.219095 (rel < 1e-9).
    (V-c) TRUNCATION + STABILITY: at the best anchor point, N_cut 32->48
      changes all four totals by < 0.5%; anneal seed-2 best within 5%.
"""
import math, sys, json, io, os, contextlib
import numpy as np

here = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.dirname(here))

# ---------- anchor-side machinery (2344 ingredients, verbatim) ----------
t = json.load(open('code/2344_F_table.json'))
lnE, lnF = np.array(t["lnE"]), np.array(t["lnF"])
M_EL, CONV0 = 1408.0, 1e-26 / 1.783e-27
FL = {30: 0.11, 50: 0.09, 200: 0.05, 1500: 0.04}
C = 2.998e5
FR = json.load(open('code/2345_l4_results.json'))["frames"]

def Fi_vec(eps):
    e = np.maximum(eps, 1.1e-2)
    out = np.exp(np.interp(np.log(e), lnE, lnF))
    hi = e > 9.9e3
    if hi.any():
        out = np.where(hi, np.exp(lnF[-1] + 0.17 * (np.log(e) - lnE[-1])), out)
    return out

N_CUT_X = 32          # XQC side (conservative tail bound handles the remainder)
N_CUT = 96            # anchor side (raised from 32 after the first-run V-c catch)
NS = np.arange(1, N_CUT + 1, dtype=float)
MS = NS * M_EL
MU = np.outer(MS, MS) / (MS[:, None] + MS[None, :])
KIJ = 0.5 * (1.0 / MS[:, None] + 1.0 / MS[None, :])

def flory_w(Nn, ncut=N_CUT):
    x = 1 - 1.0 / Nn
    Narr = np.arange(1, ncut + 1, dtype=float)
    w = Narr * x ** (Narr - 1) * (1 - x) ** 2
    tail = 1.0 - w.sum()
    return w / w.sum(), max(tail, 0.0)

def eff_dist(w, g2, Rs, mu=MU, kij=KIJ):
    gij = np.sqrt(np.outer(g2, g2))
    out = {}
    for v in (30.0, 50.0, 200.0, 1500.0):
        b = (v / C) ** 2
        s = Rs * Rs * Fi_vec(gij / (0.5 * mu * b * Rs))
        out[int(v)] = float(w @ (s * kij) @ w * CONV0 + FL[int(v)])
    return out

def viol(tot, frame):
    v = 1.0
    for vel, (lo, hi) in frame.items():
        tval = tot[int(vel)]
        if tval < lo: v = max(v, lo / max(tval, 1e-12))
        if tval > hi: v = max(v, tval / hi)
    return v

results = {"prereg": "header", "V": {}, "xqc_curve": {}, "anchor": {}}

# ---------- V-a: two-species limit vs stored 2371 ----------
Q1 = json.load(open('code/2371_results.json'))
va_ok = True
for fname in ("audited_extended", "audited_central"):
    NA, NB, gA2, gB2, wq, Rs = Q1[fname]["best_params"]
    iA, iB = int(round(NA)) - 1, int(round(NB)) - 1
    w = np.zeros(N_CUT); w[iA], w[iB] = wq, 1 - wq
    g2 = np.ones(N_CUT); g2[iA], g2[iB] = gA2, gB2
    tot = eff_dist(w, g2, Rs)
    st = Q1[fname]["best_totals"]
    rel = max(abs(tot[int(k)] - v) / v for k, v in st.items())
    va_ok &= rel < 1e-9
    print("V-a two-species limit (%s): max rel dev %.1e" % (fname, rel))
results["V"]["a_two_species_limit"] = va_ok
print("V-a ->", "OK" if va_ok else "FAIL")

# ---------- XQC side: unit counts N=1..32 ----------
src = open('code/1879_xqc_recomputation.py').read().split("if __name__")[0]
g = {}; exec(src, g)
E_C = g['E_C']; BINS = g['BINS']; SAT = g['SAT']
TH = [obs + 5 * math.sqrt(obs + 1) for (lo, hi, obs, f) in BINS]
THS = SAT[1] + 5 * math.sqrt(SAT[1] + 1)

def unit_counts(N, sign):
    g['N_ROD'] = N; g['M_ROD'] = N * M_EL
    g['E_RN'] = (3.0 * E_C / (8 * N)) * 0.012
    g['L_ROD'] = max((N - 1) * 1.15, 1e-9)
    g['NDM'] = (1.0 * 1e3 / (N * M_EL)) * 2.5e10
    assert g['E_RN'] == 3.0 * 0.30 / (8 * N) * 0.012
    folded = N > 1
    with contextlib.redirect_stdout(io.StringIO()):
        c, s = g['predicted_bins'](-1 if sign == "attractive" else 1, folded)
    return np.array(c + [s])

UCF = 'code/2375_unit_counts.json'
if os.path.exists(UCF):
    _u = json.load(open(UCF))
    UC = {k: np.array(v) for k, v in _u.items()}
    print("\nXQC unit counts loaded from cache (%s)" % UCF)
else:
    print("\ncomputing XQC unit counts N=1..%d, both signs..." % N_CUT_X)
    UC = {}
    for sign in ("attractive", "repulsive"):
        UC[sign] = np.array([unit_counts(N, sign) for N in range(1, N_CUT_X + 1)])
    json.dump({k: v.tolist() for k, v in UC.items()}, open(UCF, "w"))

# V-b: single-species limit vs 2366b (dimer att, S_c=0.012, f=0.94, rho=0.2)
tot2 = UC["attractive"][1] * 0.94 * 0.2
viols = sum(1 for p, th in zip(tot2[:-1], TH) if p > th) + (1 if tot2[-1] > THS else 0)
total2 = tot2.sum()
STORED = 642.2190945369623
vb_ok = (viols == 3) and abs(total2 - STORED) / STORED < 1e-9
results["V"]["b_single_species_limit"] = {"viol": viols, "total": float(total2), "ok": vb_ok}
print("V-b single-species limit: viol=%d total=%.6f -> %s" % (viols, total2, "OK" if vb_ok else "FAIL"))

THv = np.array(TH + [THS])
def xqc_pass(Nn, sign, rho):
    w, tail = flory_w(Nn, N_CUT_X)
    pred = rho * (w @ UC[sign])
    bound = tail * rho * UC[sign].max(axis=0)      # hurting-direction tail bound
    return bool(np.all(pred + bound <= THv)), tail

print("\nXQC-viability curve (summed criterion + tail bound; floor S_c=0.012):")
grid = [round(1.5 + 0.25 * i, 2) for i in range(43)]
viable = {}
for sign in ("attractive", "repulsive"):
    for rho in (0.3, 0.2):
        ok_list = [Nn for Nn in grid if xqc_pass(Nn, sign, rho)[0]]
        key = "%s,rho=%s" % (sign, rho)
        viable[key] = ok_list
        results["xqc_curve"][key] = ok_list
        # closest approach: min over grid of the worst bin ratio (tail bound included)
        best_r, best_n, best_bin = 1e30, None, None
        for Nn in grid:
            w, tail = flory_w(Nn, N_CUT_X)
            pred = rho * (w @ UC[sign]) + tail * rho * UC[sign].max(axis=0)
            ratios = pred / THv
            i = int(np.argmax(ratios))
            if ratios[i] < best_r:
                best_r, best_n = float(ratios[i]), Nn
                best_bin = ("%d-%d" % (BINS[i][0], BINS[i][1])) if i < len(BINS) else ">4keV"
        results["xqc_curve"][key + ",closest"] = {"worst_ratio": best_r, "at_Nn": best_n,
                                                  "binding_bin": best_bin}
        if ok_list:
            print("  %-22s viable <N>_n: [%.2f, %.2f] (%d grid pts)"
                  % (key, min(ok_list), max(ok_list), len(ok_list)))
        else:
            print("  %-22s viable <N>_n: NONE (closest approach x%.3f at <N>_n=%.2f, bin %s)"
                  % (key, best_r, best_n, best_bin))
all_viable = sorted({n for v in viable.values() for n in v})
window = (min(all_viable), max(all_viable)) if all_viable else None
print("  union window:", window)

# ---------- anchor scan over the union window ----------
lo_w, hi_w = window if window else (1.5, 12.0)
rng = np.random.default_rng(7)
NWIDE = 30_000
def sample(n):
    Nn = rng.uniform(lo_w, hi_w, n)
    g0 = np.exp(rng.uniform(math.log(1e-6), math.log(1e3), n))
    p = rng.uniform(0, 14, n)
    Rs = np.exp(rng.uniform(math.log(20), math.log(100), n))
    return np.stack([Nn, g0, p, Rs], axis=1)

def evalp(q):
    Nn, g0, p, Rs = q
    wfull, _ = flory_w(Nn)
    cum = np.cumsum(wfull)
    m = int(np.searchsorted(cum, 1.0 - 5e-4)) + 1
    m = min(max(m, 4), N_CUT)
    w = wfull[:m] / wfull[:m].sum()
    g2 = g0 * (NS[:m] / 4.0) ** p
    return eff_dist(w, g2, Rs, mu=MU[:m, :m], kij=KIJ[:m, :m])

def scan(frame):
    P = sample(NWIDE)
    bv, bp = 1e30, None
    for q in P:
        v = viol(evalp(q), frame)
        if v < bv: bv, bp = v, q.copy()
    return bv, bp

def anneal(p0, frame, steps=6000, seed=11):
    r = np.random.default_rng(seed)
    p = p0.copy(); bv = viol(evalp(p), frame); best = (bv, p.copy())
    T = 0.4
    lo = np.array([lo_w, 1e-6, 0.0, 20.0]); hi = np.array([hi_w, 1e3, 14.0, 100.0])
    for i in range(steps):
        T *= (1 - 3.0 / steps)
        q = p.copy(); j = r.integers(0, 4)
        if j in (1, 3): q[j] = np.clip(q[j] * math.exp(r.normal(0, 0.25)), lo[j], hi[j])
        else: q[j] = np.clip(q[j] + r.normal(0, 0.3 if j == 0 else 0.5), lo[j], hi[j])
        v = viol(evalp(q), frame)
        if v < bv or r.random() < math.exp(-(v - bv) / max(T, 1e-4)):
            p, bv = q, v
            if v < best[0]: best = (v, q.copy())
    return best

print("\nANCHOR SCAN over <N>_n in [%.2f, %.2f] (Flory shape, g^2(N)=g0^2 (N/4)^p):" % (lo_w, hi_w))
vc_stab = True
for fname in ("audited_extended", "audited_central", "registered"):
    F = FR[fname]
    v1, p1 = scan(F)
    bv, bp = anneal(p1, F, seed=11)
    bv2, _ = anneal(p1, F, seed=97)
    stab = abs(bv - bv2) / max(bv, 1e-12) < 0.05
    if fname != "registered": vc_stab &= stab
    PASS = bool(bv <= 1.0 + 1e-9)
    results["anchor"][fname] = {"wide_best": float(v1), "anneal_best": float(bv),
                                "anneal_seed2": float(bv2),
                                "best_params": [float(x) for x in bp],
                                "best_totals": {k: float(v) for k, v in evalp(bp).items()},
                                "PASS": PASS}
    print("  %-18s wide=%.4f anneal=%.4f (seed2 %.4f) PASS=%s  best <N>_n=%.2f g0^2=%.3g p=%.2f Rs=%.1f"
          % (fname, v1, bv, bv2, PASS, bp[0], bp[1], bp[2], bp[3]))

# V-c: truncation robustness at the best audited point + seed stability
bestf = min(("audited_extended", "audited_central"),
            key=lambda f: results["anchor"][f]["anneal_best"])
bp = np.array(results["anchor"][bestf]["best_params"])
Nn, g0, p, Rs = bp
w48, _ = flory_w(Nn, 128)
NS48 = np.arange(1, 129, dtype=float); MS48 = NS48 * M_EL
MU48 = np.outer(MS48, MS48) / (MS48[:, None] + MS48[None, :])
K48 = 0.5 * (1.0 / MS48[:, None] + 1.0 / MS48[None, :])
g248 = g0 * (NS48 / 4.0) ** p
t32 = evalp(bp)
t48 = eff_dist(w48, g248, Rs, mu=MU48, kij=K48)
relc = max(abs(t48[k] - t32[k]) / t32[k] for k in t32)
vc_ok = (relc < 0.005) and vc_stab
results["V"]["c_truncation_and_stability"] = {"ncut_rel_dev": float(relc),
                                              "seed_stable": vc_stab, "ok": vc_ok}
print("\nV-c truncation (N_cut 96->128 at best %s point): max rel dev %.2e; seed stability %s -> %s"
      % (bestf, relc, vc_stab, "OK" if vc_ok else "FAIL"))

# ---------- outcome grading ----------
ap = {f: results["anchor"][f]["PASS"] for f in ("audited_extended", "audited_central")}
if not any(ap.values()):
    outcome = ("(a) NO Flory-shape pass at either audited frame within the XQC-viable "
               "window -- the equilibrium shape FAILS the dSph channel; non-equilibrium "
               "distribution required (death mode (ii) REARMED at population level)")
elif window is None:
    outcome = "(b) anchor passes exist but NO <N>_n is XQC-viable -- family dies at the gate (CANDIDATE)"
else:
    passing = [f for f, ok in ap.items() if ok]
    outcome = "(c) JOINT PASS EXISTS at %s -- Q3c target fully specified" % ",".join(passing)
results["OUTCOME"] = outcome
results["V"]["passed"] = "%d/3" % (int(va_ok) + int(vb_ok) + int(vc_ok))
print("\nVERIFY:", results["V"]["passed"])
print("OUTCOME:", outcome)
json.dump(results, open("code/2375_results.json", "w"), indent=1,
           default=lambda o: bool(o) if isinstance(o, np.bool_) else float(o))
print("wrote code/2375_results.json")
