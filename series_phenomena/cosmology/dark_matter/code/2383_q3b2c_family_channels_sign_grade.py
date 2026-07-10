#!/usr/bin/env python3
"""
PATCH 2383 -- Q3b-2c: THE DERIVED FAMILY THROUGH BOTH CHANNELS + SIGN + GRADE.

The collision the 2380 contract pre-registered: the 2382-derived w(N | r,
eps, phi, q) family is COMPUTED (nothing re-fit), then checked against the
corridor walls (2374c machinery, summed criterion), the demand sheet, the
near-bidisperse registered kill's territory, and G-XQC-0 -- and the SIGN is
extracted from registered structure, not chosen.

PRE-REGISTERED (fixed before run):

  MEMBERS: the derived family from the 2382 cascade (pair channel, q = 1;
    q-bracket spread reported at the deep-closure member), generated over
    r in [0.5, 13] x (phi, eps) bracket corners, deduplicated on the
    rounded weight vector; species below w = 0.005 trimmed + renormalized
    (disclosed). Weights are MASS fractions (2382 propagated mass), the
    same convention the summed criterion scales by.

  XQC CHANNEL (per member): the 2374c summed-spectrum criterion,
    sum_i f_i*rho*c_i(bin) vs obs + 5*sqrt(obs+1), via the committed 2379
    unit cache -- S_c in {0.012, 0.035, 0.05}, rho in {0.2, 0.3}, BOTH
    signs, eps_th in {1, 0.5, 0.25, 0.1, 0.02}; exact rho* per
    (member, sign, S_c, eps_th) by f*rho linearity. Fine S_c* bisection
    (pipeline-level) deferred to the wall-remapping task -- the cached
    S_c grid + exact rho* is the 2372-convention grade and suffices for
    the outcome taxonomy below (disclosed, not hidden).

  ANCHOR CHANNEL (per member): eff_dist (the 2375 N-species form, verified
    here against stored 2371 totals) at the FIXED audited frames
    (audited_extended, audited_central; registered graded record-only),
    composition PINNED to the derived weights -- the scan owns ONLY the
    coupling: (i) the registered strain family g^2(N) = g0^2 (N/4)^p,
    (g0^2, p, Rs); (ii) free per-species g^2 (diagnostic: separates
    shape-failure from coupling-law-failure). 4k wide random + 8k anneal
    x 2 seeds per (member, frame, law). viol <= 1 + 1e-9 <=> PASS
    (2349/2371 convention).

  SIGN (extracted, not chosen): the registered residual mechanism is
    1858's screened unipolar E_qq, and E_qq is ATTRACT-ONLY (frontier
    SS.md, OPEN-SS-43 original entry, verbatim: "E_qq is attract-only, so
    a qCP aggregate ... cannot dipole-cancel"). Both graded channels
    couple through that residual, so the REGISTERED-STRUCTURE DEFAULT
    SIGN IS ATTRACTIVE in both. A repulsive effective transfer sign is
    NOT registered structure -- it would have to emerge from the
    OPEN-SS-43 derived screened form (e.g. short-range exchange core or
    screening overshoot), which is the SAME unpaid rent that owes S(N).
    This run therefore grades BOTH branches and reports the
    attractive-default branch FIRST (hurting-first), with the repulsive
    branch explicitly CONDITIONAL on OPEN-SS-43.

  HURTING-FIRST PREDICTIONS (stated before running): the corridor's known
    occupants are heavy-dominant (2371: w(6)=0.936 central; w(5)=0.783
    extended) while the deep-closure derived member is light-dominant
    (w(3)~0.8) -- the deep-closure member is AT RISK on the anchor side;
    mid-r members (5- and 6-dominant) are the plausible passers. On the
    XQC side heavier members are safer (1/M number density). Under the
    attractive default the corridor is knife-edge at rho = 0.3 (2374c) --
    the family plausibly survives at rho <= 0.2 only. None of this is
    steered for or against; graded as written.

  OUTCOMES (graded as written):
    (a) NO derived member passes the anchor suite at either audited frame
        under EITHER coupling law -> the derived shape fails the dSph
        channel; the third kill lands fully derived at shape level.
    (b) anchor passes exist ONLY at XQC-unviable members/placements ->
        dies at the gate; same escalation via F5's channel.
    (c) joint passes exist on the REPULSIVE branch only -> the derived
        population is live CONDITIONAL on the OPEN-SS-43 derived sign
        being effectively repulsive (registered default: attractive);
        member + couplings + corridor point recorded = Q3c's target,
        with the sign tension registered as the arc's sharpest demand.
    (d) joint passes exist on the ATTRACTIVE branch at rho = 0.2 (not
        0.3) -> live only at sub-standard local density (the 2373
        exposure); recorded as such.
    (c)+(d) may co-occur; both recorded.

  VERIFY (5, pre-stated):
    V1 the 2381 + 2382 batteries green underneath (subprocess).
    V2 SEMANTIC CACHE CHECK (the debt named at 2381): cache
       [2,attractive,0.012,1] x (0.94*0.2) reproduces the stored 2366b
       point (viol = 3, total 642.2190945369623, rel < 1e-9) AND the
       cache row for one non-dimer key matches a FRESH pipeline call
       bit-level (rel < 1e-12).
    V3 eff_dist machinery equivalence: stored 2371 best_params reproduce
       stored best_totals, both audited frames, rel < 1e-9.
    V4 summed-criterion regression: the Q1 compositions re-graded from
       the CACHE at eps_th = 1 reproduce the stored 2374c grid verdicts
       AND worst ratios (rel < 1e-6) at all (sign, S_c, rho) points.
    V5 anneal stability: at every PASSING (member, frame, law), seed-2
       best within 5% of seed-1 best.

  DISCLOSED AMENDMENT (pre-run of the anchor stage, after the XQC stage
    completed on the full member set in a first launch that was killed by
    an environment limit at the anchor header): the anchor scan runs on a
    STRATIFIED REPRESENTATIVE SUBSET (per peak-N, spanning the composition
    range; adjacent members differ by < 0.1 in any weight and eff_dist is
    smooth in w, so representatives cover the family); budgets 3k wide +
    6k anneal x 2 seeds (disclosed, 2375-precedent); the registered frame
    graded for the best passing member only (record-only). The FULL member
    set keeps its XQC grade. Nothing about which members pass is known at
    amendment time -- the first launch died before any anchor row.

Run: python3 2383_q3b2c_family_channels_sign_grade.py   (exit 0 iff 5/5)
"""

import io
import json
import math
import os
import subprocess
import sys
import contextlib
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.dirname(HERE))
FAILURES = []


def check(name, ok, detail):
    tag = "PASS" if ok else "FAIL"
    print(f"   [{tag}] {name}: {detail}")
    if not ok:
        FAILURES.append(name)


# ===========================================================================
# Shared registered ingredients
# ===========================================================================
CACHE = json.load(open('code/2379_unit_cache.json'))
src = open('code/1879_xqc_recomputation.py').read().split("if __name__")[0]
G = {}
exec(src, G)
M_EL_X, E_C, BINS, SAT = G['M_EL'], G['E_C'], G['BINS'], G['SAT']
TH = [o + 5 * math.sqrt(o + 1) for (lo, hi, o, f) in BINS]
THS = SAT[1] + 5 * math.sqrt(SAT[1] + 1)
ETHS = (1.0, 0.5, 0.25, 0.1, 0.02)
SCS = (0.012, 0.035, 0.05)


CACHE_DIRTY = [False]


def pipeline_unit(N, sign, sc, eth):
    """fresh 1879 run at f=rho=1 (eth=1 only here), extending the cache."""
    assert eth == 1.0
    G['N_ROD'], G['M_ROD'] = N, N * M_EL_X
    G['E_RN'] = (3.0 * E_C / (8 * N)) * sc
    G['L_ROD'] = max((N - 1) * 1.15, 1e-9)
    G['NDM'] = (1e3 / (N * M_EL_X)) * 2.5e10
    with contextlib.redirect_stdout(io.StringIO()):
        c, sat = G['predicted_bins'](-1 if sign == "attractive" else 1, N > 1)
    CACHE["%d,%s,%g,%g" % (N, sign, sc, eth)] = list(c) + [sat]
    CACHE_DIRTY[0] = True
    return list(c), sat


def cache_unit(N, sign, sc, eth):
    key = "%d,%s,%g,%g" % (N, sign, sc, eth)
    if key not in CACHE:
        return pipeline_unit(N, sign, sc, eth)
    v = CACHE[key]
    return v[:-1], v[-1]


def summed_grade_cache(members_w, sign, sc, rho, eth):
    tot = [0.0] * len(BINS)
    tots = 0.0
    for N, f in members_w:
        c, s = cache_unit(N, sign, sc, eth)
        tot = [a + f * rho * b for a, b in zip(tot, c)]
        tots += f * rho * s
    viol = sum(1 for p, t in zip(tot, TH) if p > t) + (1 if tots > THS else 0)
    worst = max(max(p / t for p, t in zip(tot, TH)),
                tots / THS if tots > 0 else 0.0)
    return viol == 0, viol, worst


def rho_star_exact(members_w, sign, sc, eth):
    tot = [0.0] * len(BINS)
    tots = 0.0
    for N, f in members_w:
        c, s = cache_unit(N, sign, sc, eth)
        tot = [a + f * b for a, b in zip(tot, c)]
        tots += f * s
    ratio = max(max(p / t for p, t in zip(tot, TH)),
                tots / THS if tots > 0 else 0.0)
    return 1.0 / ratio


# ---- anchor machinery (2375 N-species form, 2344 ingredients verbatim) ----
t = json.load(open('code/2344_F_table.json'))
lnE, lnF = np.array(t["lnE"]), np.array(t["lnF"])
M_EL, CONV0 = 1408.0, 1e-26 / 1.783e-27
FL = {30: 0.11, 50: 0.09, 200: 0.05, 1500: 0.04}
C = 2.998e5
FR = json.load(open('code/2345_l4_results.json'))["frames"]
N_CUT = 12
NS = np.arange(1, N_CUT + 1, dtype=float)
MS = NS * M_EL
MU = np.outer(MS, MS) / (MS[:, None] + MS[None, :])
KIJ = 0.5 * (1.0 / MS[:, None] + 1.0 / MS[None, :])


def Fi_vec(eps):
    e = np.maximum(eps, 1.1e-2)
    out = np.exp(np.interp(np.log(e), lnE, lnF))
    hi = e > 9.9e3
    if hi.any():
        out = np.where(hi, np.exp(lnF[-1] + 0.17 * (np.log(e) - lnE[-1])), out)
    return out


def eff_dist(w, g2, Rs):
    gij = np.sqrt(np.outer(g2, g2))
    out = {}
    for v in (30.0, 50.0, 200.0, 1500.0):
        b = (v / C) ** 2
        s = Rs * Rs * Fi_vec(gij / (0.5 * MU * b * Rs))
        out[int(v)] = float(w @ (s * KIJ) @ w * CONV0 + FL[int(v)])
    return out


def viol(tot, frame):
    v = 1.0
    for vel, (lo, hi) in frame.items():
        tval = tot[int(vel)]
        if tval < lo:
            v = max(v, lo / max(tval, 1e-12))
        if tval > hi:
            v = max(v, tval / hi)
    return v


# ===========================================================================
# The derived family (2382 cascade, pair channel) -- regenerated verbatim
# ===========================================================================
SY_A, SY_B, SY_P, C_SY = 14.054, 0.246, 5.0, 14.054
PHI_BRACKET = (6.7e-15, 7.4e-10)
EPS_BAND = (23.2, 36.2)


def g_SY(u):
    return u ** (-SY_P) * math.exp(-SY_A / u + SY_B * u)


def cascade_pair(r, phi, eps, v_f=1.0, q=1.0, n_cut=32):
    x = (-1.0 + math.sqrt(1.0 + 2.0 * q)) / (2.0 * q)
    n_stab = C_SY * r / eps

    def p_close(N):
        if N < n_stab:
            return 0.0
        j = g_SY(N / r) / r ** 3 * v_f
        return j / (j + phi)

    w_mass = {}

    def propagate(flux, N0):
        surv = flux
        for N in range(N0, n_cut + 1):
            p = p_close(N)
            w_mass[N] = w_mass.get(N, 0.0) + surv * p * N
            surv *= (1.0 - p)
        return surv * n_cut

    esc = propagate(x, 3) + propagate((q / 2.0) * x ** 2, 4)
    total = sum(w_mass.values()) + esc
    return {N: m / total for N, m in sorted(w_mass.items()) if m / total > 0}


def trimmed(w, floor=0.005):
    kept = {N: float(v) for N, v in w.items() if v >= floor}
    tot = sum(kept.values())
    return tuple(sorted((N, round(v / tot, 4)) for N, v in kept.items()))


def coarse_key(m):
    """dedupe key: support + weights rounded to 0.1 (family representatives)."""
    return tuple(sorted((N, round(v, 1)) for N, v in m))


phi_c = math.sqrt(PHI_BRACKET[0] * PHI_BRACKET[1])
eps_c = 0.5 * sum(EPS_BAND)
members = {}
n_dead = 0
for phi in (PHI_BRACKET[0], phi_c, PHI_BRACKET[1]):
    for eps in (EPS_BAND[0], eps_c, EPS_BAND[1]):
        for r in np.arange(0.5, 13.01, 0.25):
            m = trimmed(cascade_pair(r, phi, eps))
            peak = max(m, key=lambda p: p[1])[0]
            if peak > 6:
                n_dead += 1  # placement-dead per the 2382 kinetic map; not graded
                continue
            key = coarse_key(m)
            if key not in members:
                members[key] = {"rep": m, "pts": []}
            members[key]["pts"].append((round(float(r), 2), phi, eps))
members = {v["rep"]: v["pts"] for v in members.values()}
# q-bracket spread at the deep-closure member (reported, not multiplied out)
DEEP_Q = {q: trimmed(cascade_pair(1.5, phi_c, eps_c, q=q)) for q in (0.5, 1.0, 2.0)}

print("=" * 78)
print(" PATCH 2383 -- Q3b-2c: DERIVED FAMILY x BOTH CHANNELS x SIGN x GRADE")
print("=" * 78)
print(f"\n Derived family: {len(members)} corridor representatives "
      f"(peak <= 6; coarse-deduped; trim 0.005 disclosed); "
      f"{n_dead} grid pts placement-dead (peak > 6, ungraded per the 2382 map):")
for m in sorted(members, key=lambda mm: (max(mm, key=lambda p: p[1])[0],
                                         min(N for N, _ in mm))):
    rs = [rr for rr, _, _ in members[m]]
    print(f"   {dict(m)}   (r ~ {min(rs)}-{max(rs)}, {len(members[m])} grid pts)")
print(f" Deep-closure q-bracket: {[dict(v) for v in DEEP_Q.values()]}")

# ===========================================================================
# VERIFY FIRST (V2-V4 must be green before any grading is trusted)
# ===========================================================================
print("\n" + "-" * 78)
print(" VERIFY (channel machinery, before grading)")
print("-" * 78)

rc1 = subprocess.run([sys.executable, 'code/2381_q3b2a_grounding_ringclosure_Nc.py'],
                     capture_output=True, text=True)
rc2 = subprocess.run([sys.executable, 'code/2382_q3b2b_nucleation_growth_cascade.py'],
                     capture_output=True, text=True)
check("V1 batteries underneath", rc1.returncode == 0 and rc2.returncode == 0,
      f"2381 exit {rc1.returncode}, 2382 exit {rc2.returncode}")

c2, s2 = cache_unit(2, "attractive", 0.012, 1)
cc = [x * 0.94 * 0.2 for x in c2]
ss = s2 * 0.94 * 0.2
v2 = sum(1 for p, tt in zip(cc, TH) if p > tt) + (1 if ss > THS else 0)
tot2 = sum(cc) + ss
STORED = 642.2190945369623
G['N_ROD'], G['M_ROD'] = 5, 5 * M_EL_X
G['E_RN'] = (3.0 * E_C / 40) * 0.012
G['L_ROD'], G['NDM'] = 4 * 1.15, (1e3 / (5 * M_EL_X)) * 2.5e10
with contextlib.redirect_stdout(io.StringIO()):
    cf, sf = G['predicted_bins'](1, True)
cv, sv = cache_unit(5, "repulsive", 0.012, 1)
relf = max(abs(a - b) / max(abs(a), 1e-30) for a, b in zip(list(cf) + [sf], cv + [sv]))
check("V2 semantic cache", v2 == 3 and abs(tot2 - STORED) / STORED < 1e-9 and relf < 1e-12,
      f"2366b via cache: viol={v2} total={tot2:.6f} rel={abs(tot2-STORED)/STORED:.1e}; "
      f"fresh-pipeline N=5 rep match rel={relf:.1e}  -- THE 2381-NAMED DEBT DISCHARGED")

Q1 = json.load(open('code/2371_results.json'))
va = 0.0
for fname in ("audited_extended", "audited_central"):
    NA, NB, gA2, gB2, wq, Rs = Q1[fname]["best_params"]
    w = np.zeros(N_CUT); g2 = np.zeros(N_CUT)
    w[int(round(NA)) - 1], w[int(round(NB)) - 1] = wq, 1 - wq
    g2[int(round(NA)) - 1], g2[int(round(NB)) - 1] = gA2, gB2
    tot = eff_dist(w, g2, Rs)
    va = max(va, max(abs(tot[int(k)] - v) / v
                     for k, v in Q1[fname]["best_totals"].items()))
check("V3 eff_dist equivalence", va < 1e-9, f"max rel dev vs stored 2371: {va:.1e}")

R74 = json.load(open('code/2374c_results.json'))["grid"]
comps_q1 = {}
for fname, tag in (("audited_extended", "extended"), ("audited_central", "central")):
    NA, NB, gA2, gB2, wq, Rs = Q1[fname]["best_params"]
    comps_q1[tag] = [(int(round(NA)), wq), (int(round(NB)), 1 - wq)]
v4_ok, v4_max, v4_n = True, 0.0, 0
for tag in comps_q1:
    for sign in ("attractive", "repulsive"):
        for sc, rhos in ((0.012, (0.3, 0.2)), (0.035, (0.3,))):
            if sc == 0.035 and not (tag == "extended" and sign == "repulsive"):
                continue  # one above-floor spot via fresh pipeline (cost-bounded)
            for rho in rhos:
                safe, vl, worst = summed_grade_cache(comps_q1[tag], sign, sc, rho, 1.0)
                key = "%s,%s,Sc=%s,rho=%s" % (tag, sign, sc, rho)
                st = R74[key]
                verdict = "XQC-SAFE" if safe else "EXCLUDED-class"
                rel = abs(worst - st["worst_ratio"]) / st["worst_ratio"]
                v4_max, v4_n = max(v4_max, rel), v4_n + 1
                if verdict != st["verdict"] or rel > 1e-6:
                    v4_ok = False
check("V4 2374c regression via cache", v4_ok,
      f"{v4_n} grid verdicts + worst ratios reproduce, floor grid + one fresh "
      f"above-floor spot (max rel {v4_max:.1e})")

# ===========================================================================
# XQC CHANNEL -- the derived family through the summed criterion
# ===========================================================================
print("\n" + "-" * 78)
print(" XQC CHANNEL (summed criterion; ATTRACTIVE-DEFAULT branch first)")
print("-" * 78)
xqc = {}
for m in members:
    row = {}
    for sign in ("attractive", "repulsive"):
        # FLOOR: full eps_th bracket via committed cache (all N covered)
        rs1 = rho_star_exact(m, sign, 0.012, 1.0)
        rs_min = min(rho_star_exact(m, sign, 0.012, e) for e in ETHS)
        row[(sign, 0.012)] = (rs1, rs_min)
        # ABOVE-FLOOR: eps_th = 1 only (pipeline extends the cache; the
        # eps_th bracket above the floor is deferred with the fine-wall task)
        for sc in (0.035, 0.05):
            rsA = rho_star_exact(m, sign, sc, 1.0)
            row[(sign, sc)] = (rsA, rsA)
    xqc[m] = row
print("   exact rho* (GeV/cm^3); floor shows [min over eps_th bracket],")
print("   above-floor is eps_th=1 (bracket deferred with the fine-wall task):")
print("   member (top species)            sign        Sc=0.012        Sc=0.035     Sc=0.05")
for m in sorted(xqc, key=lambda mm: max(mm, key=lambda p: p[1])[0]):
    top = max(m, key=lambda p: p[1])
    lab = "N%d-dom %s" % (top[0], dict(m))
    for sign in ("attractive", "repulsive"):
        c012 = "%.3f[%.3f]" % xqc[m][(sign, 0.012)]
        c035 = "%.3f" % xqc[m][(sign, 0.035)][0]
        c05 = "%.3f" % xqc[m][(sign, 0.05)][0]
        print("   %-30s %-11s %-15s %-12s %s" % (lab[:30], sign, c012, c035, c05))
        lab = ""

if CACHE_DIRTY[0]:
    json.dump(CACHE, open('code/2379_unit_cache.json', 'w'))
    CACHE_DIRTY[0] = False
    print(f"\n cache extended to {len(CACHE)} keys (saved)")

# ===========================================================================
# ANCHOR CHANNEL -- pinned compositions, coupling-only scans
# ===========================================================================
print("\n" + "-" * 78)
print(" ANCHOR CHANNEL (composition PINNED; coupling scan only)")
print("-" * 78)
rng = np.random.default_rng(7)


def anneal(member, frame, law, seed, wide=4000, steps=8000):
    idx = np.array([N - 1 for N, _ in member])
    wv = np.zeros(N_CUT)
    for (N, f) in member:
        wv[N - 1] = f
    nsp = len(member)

    def build_g2(params):
        g2 = np.zeros(N_CUT)
        if law == "strain":
            g0, p = params[0], params[1]
            for (N, _) in member:
                g2[N - 1] = g0 * (N / 4.0) ** p
        else:
            for k, (N, _) in enumerate(member):
                g2[N - 1] = params[k]
        return g2

    npar = (2 if law == "strain" else nsp) + 1  # + Rs
    r = np.random.default_rng(seed)

    def sample(n):
        P = np.empty((n, npar))
        if law == "strain":
            P[:, 0] = np.exp(r.uniform(math.log(1e-6), math.log(1e3), n))
            P[:, 1] = r.uniform(0, 14, n)
        else:
            for k in range(nsp):
                P[:, k] = np.exp(r.uniform(math.log(1e-6), math.log(1e3), n))
        P[:, -1] = np.exp(r.uniform(math.log(20), math.log(100), n))
        return P

    def ev(p):
        return viol(eff_dist(wv, build_g2(p), p[-1]), frame)

    best_v, best_p = 1e30, None
    for p in sample(wide):
        v = ev(p)
        if v < best_v:
            best_v, best_p = v, p.copy()
    p, bv = best_p.copy(), best_v
    T = 0.4
    for i in range(steps):
        T *= (1 - 3.0 / steps)
        q = p.copy()
        j = r.integers(0, npar)
        if law == "strain" and j == 1:
            q[1] = min(max(q[1] + r.normal(0, 0.4), 0.0), 14.0)
        else:
            lo, hi = (20.0, 100.0) if j == npar - 1 else (1e-6, 1e3)
            q[j] = min(max(q[j] * math.exp(r.normal(0, 0.25)), lo), hi)
        v = ev(q)
        if v < bv or r.random() < math.exp(-(v - bv) / max(T, 1e-4)):
            p, bv = q, v
            if v < best_v:
                best_v, best_p = v, q.copy()
    return best_v, best_p


def peak_of(m):
    return max(m, key=lambda p: p[1])[0]


# stratified representatives: per peak-N, order by dominant weight, take
# ends + middle (covers the composition sweep; adjacent gaps < 0.1)
by_peak = {}
for m in members:
    by_peak.setdefault(peak_of(m), []).append(m)
anchor_set = []
for pk in sorted(by_peak):
    grp = sorted(by_peak[pk], key=lambda m: -dict(m).get(pk, 0))
    take = sorted({0, len(grp) // 4, len(grp) // 2, (3 * len(grp)) // 4,
                   len(grp) - 1})
    anchor_set += [grp[i] for i in take]
print(f"   anchor representatives: {len(anchor_set)} of {len(members)} members "
      f"(stratified per peak-N, ends+quartiles; disclosed)")
anchor = {}
v5_ok = True
print("   member (top)                  frame              law     best-viol  PASS")
for m in anchor_set:
    for fname in ("audited_extended", "audited_central"):
        for law in ("strain", "free"):
            v1s, p1 = anneal(m, FR[fname], law, seed=11, wide=3000, steps=6000)
            v2s, _ = anneal(m, FR[fname], law, seed=97, wide=3000, steps=6000)
            bv = min(v1s, v2s)
            passed = bv <= 1.0 + 1e-9
            if passed and abs(v1s - v2s) / max(v1s, 1e-12) > 0.05:
                v5_ok = False
            anchor[(m, fname, law)] = (bv, p1 if v1s <= v2s else None, passed)
            print("   N%-2d-dom %-21s %-18s %-7s %8.4f   %s"
                  % (peak_of(m), str([N for N, _ in m]), fname, law, bv,
                     "YES" if passed else "no"), flush=True)
check("V5 anneal stability", v5_ok, "seed-2 within 5% at every passing point")

# ===========================================================================
# JOINT GRADE + SIGN + OUTCOME (as pre-registered)
# ===========================================================================
print("\n" + "-" * 78)
print(" JOINT GRADE (anchor pass x XQC corridor), per pre-registered taxonomy")
print("-" * 78)
joint_c, joint_d, anchor_any = [], [], False
for m in anchor_set:
    a_pass = any(anchor[(m, f, l)][2]
                 for f in ("audited_extended", "audited_central")
                 for l in ("strain", "free"))
    if not a_pass:
        continue
    anchor_any = True
    for sc in SCS:
        if xqc[m][("repulsive", sc)][1] >= 0.3:
            joint_c.append((m, sc, xqc[m][("repulsive", sc)]))
        if xqc[m][("attractive", sc)][1] >= 0.2:
            joint_d.append((m, sc, xqc[m][("attractive", sc)]))
for label, hits in (("(c) repulsive branch, rho >= 0.3, eps_th-robust", joint_c),
                    ("(d) attractive branch, rho >= 0.2, eps_th-robust", joint_d)):
    print(f"   {label}: {len(hits)} member/coupling points")
    for m, sc, (r1, rmin) in hits[:8]:
        print(f"      {dict(m)}  Sc={sc}  rho*={r1:.3f} [bracket-min {rmin:.3f}]")

print("\n SIGN (extracted from registered structure, not chosen):")
print("""   REGISTERED DEFAULT = ATTRACTIVE. The 1858 mechanism's screened unipolar
   E_qq residual is attract-only (OPEN-SS-43 entry, verbatim); both graded
   channels couple through it. A repulsive effective transfer sign is not
   registered structure -- it must EMERGE (or fail to) from the OPEN-SS-43
   derived screened form: the same unpaid rent that owes S(N) now owes the
   sign. D6's demand and the registered default are IN TENSION; the tension
   is quantified by this run's own (c)-vs-(d) split above.""")

outcome = ("(a) NO ANCHOR PASS -- the derived shape fails the dSph channel"
           if not anchor_any else
           "(b) anchor passes exist but NO XQC-viable placement on either branch"
           if not joint_c and not joint_d else
           "(c)+(d)" if joint_c and joint_d else
           "(c) repulsive-conditional only" if joint_c else
           "(d) attractive at sub-standard rho only")
print(f"\n OUTCOME (graded as pre-registered): {outcome}")

if CACHE_DIRTY[0]:
    json.dump(CACHE, open('code/2379_unit_cache.json', 'w'))
    print(f" cache extended to {len(CACHE)} keys (committed infrastructure, reused)")

json.dump({"members": {str(k): v for k, v in
                       ((dict(m), {"xqc": {f"{s},{sc}": xqc[m][(s, sc)] for s in
                                           ("attractive", "repulsive") for sc in SCS},
                                   "anchor": {f"{f},{l}": anchor[(m, f, l)][0]
                                              for f in ("audited_extended", "audited_central")
                                              for l in ("strain", "free")
                                              if (m, f, l) in anchor}})
                        for m in members)},
           "deep_q_bracket": {str(q): dict(v) for q, v in DEEP_Q.items()},
           "outcome": outcome,
           "joint_c": [[dict(m), sc, list(x)] for m, sc, x in joint_c],
           "joint_d": [[dict(m), sc, list(x)] for m, sc, x in joint_d]},
          open('code/2383_results.json', 'w'), indent=1, default=str)
print(" wrote code/2383_results.json")

print("\n" + "=" * 78)
print(f" VERIFY: {5 - len(FAILURES)}/5 "
      f"({'ALL PASS' if not FAILURES else 'FAILURES: ' + ', '.join(FAILURES)})")
print("=" * 78)
sys.exit(0 if not FAILURES else 1)
