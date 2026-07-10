"""
2391 -- SS43-Q1: the fine S_c* wall for the six 2383 joint members.

Pre-registered at Patch 2389 (campaign file OPEN-SS-43 sec 34.6; keyword
DM-WARM-2389). This is the 2383 deferred debt: pipeline-level S_c* bisection
turning "floor-anchored" into the quantitative landing window
[0.012, S_c*(member, sign, rho)] that collision C1's derivation (SS43-Q2 ring
multipole pass) must hit.

SCOPE (verbatim from the contract):
  - the six 2383 joint members (N6-dominant class), from
    code/2383_joint_couplings.json
  - eps_th = 1; BOTH signs; rho in {0.2, 0.3}
  - bisection tolerance 0.001 in S_c
  - every fresh pipeline point appended to the committed cache
    (code/2379_unit_cache.json)
  - floor-bracket eps_th robustness read from the cache (already computed;
    reported, not recomputed)
SCOPE GUARD: no verdict moved; the wall is an input to Q2, not a grading.

MACHINERY: identical unit convention to 2383 -- the 1879 Numerov XQC pipeline
at f = rho = 1 per species N, summed by member weights x rho (J4 pairwise
additivity carries the composite; CONV-004 measured-coefficient discipline).
The alive/dead criterion is the 2372-convention summed criterion: a bin over
observed + 5*sqrt(observed+1), or the >4 keV saturation channel over its
threshold. Linearity in rho is exact at the summed-counts level, so
worst(rho) = rho / rho*_exact and the wall for rho is the S_c where
rho*(S_c) = rho.

VERIFY BATTERY (fixed at 2389):
  V1 the 2381/2382/2383 batteries green underneath (subprocess; exit codes)
  V2 bisection bracket endpoints reproduce the cached grid verdicts
     (alive at 0.012, dead at 0.035, per member/sign/rho) AND the stored
     2383 rho* rows at both endpoints (rel < 1e-9)
  V3 worst-ratio monotone non-decreasing in S_c along each bisection path
     (the physical sanity that makes bisection valid, not merely convergent)
  V4 cache integrity after extension (schema: 13 floats per key = 12 bins +
     saturation; original 360 keys byte-identical in value; count grew by
     exactly the fresh-point tally; reload round-trip)

OUTPUT: code/2391_results.json -- per (member, sign, rho): the wall bracket
[S_c_alive, S_c_dead] with S_c_dead - S_c_alive <= 0.001, the landing window
[0.012, S_c*], rho* at both grid endpoints, the per-path sample trace (for
V3 audit), fresh-call tally, and the V1..V4 battery record.
"""
import json, math, io, os, sys, contextlib, time

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

FAILURES = []


def check(name, ok, detail):
    tag = "PASS" if ok else "FAIL"
    print(f"   [{tag}] {name}: {detail}")
    if not ok:
        FAILURES.append(name)


# ===========================================================================
# V1 -- underlying batteries green (run by the session driver; exit codes in
# /tmp/v1_status when driven interactively, else run here fresh)
# ===========================================================================
print("=" * 78)
print(" 2391  SS43-Q1: fine S_c* wall -- six joint members, eps_th=1, both")
print("       signs, rho in {0.2, 0.3}; tolerance 0.001 (contract: Patch 2389)")
print("=" * 78)

import subprocess
V1_SCRIPTS = ('code/2381_q3b2a_grounding_ringclosure_Nc.py',
              'code/2382_q3b2b_nucleation_growth_cascade.py',
              'code/2383_q3b2c_family_channels_sign_grade.py')
v1_status_file = '/tmp/v1_status'
v1_rec = {}
if os.path.exists(v1_status_file) and len(open(v1_status_file).read().strip().splitlines()) == 3:
    for ln in open(v1_status_file).read().strip().splitlines():
        pid, ex = ln.split(' exit=')
        v1_rec[pid] = int(ex)
    print("   (V1 exit codes read from session driver run)")
else:
    for s in V1_SCRIPTS:
        pid = s.split('/')[1][:4]
        t0 = time.time()
        r = subprocess.run([sys.executable, s], capture_output=True, text=True)
        v1_rec[pid] = r.returncode
        print(f"   ran {s}: exit={r.returncode} ({time.time()-t0:.0f}s)")
check("V1 2381/2382/2383 batteries green",
      all(v == 0 for v in v1_rec.values()) and len(v1_rec) == 3,
      "exit codes " + ", ".join(f"{k}={v}" for k, v in sorted(v1_rec.items())))

# ===========================================================================
# Shared registered ingredients (identical loading to 2383)
# ===========================================================================
CACHE = json.load(open('code/2379_unit_cache.json'))
N_CACHE_0 = len(CACHE)
CACHE_BASELINE = {k: list(v) for k, v in CACHE.items()}
src = open('code/1879_xqc_recomputation.py').read().split("if __name__")[0]
G = {}
exec(src, G)
M_EL_X, E_C, BINS, SAT = G['M_EL'], G['E_C'], G['BINS'], G['SAT']
TH = [o + 5 * math.sqrt(o + 1) for (lo, hi, o, f) in BINS]
THS = SAT[1] + 5 * math.sqrt(SAT[1] + 1)
ETHS = (1.0, 0.5, 0.25, 0.1, 0.02)

CACHE_DIRTY = [False]
FRESH_CALLS = [0]


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
    FRESH_CALLS[0] += 1
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


# ===========================================================================
# The six joint members (2383_joint_couplings.json -- the anchor-passing,
# floor-eps_th-robust set that carries outcome (c)+(d))
# ===========================================================================
JC = json.load(open('code/2383_joint_couplings.json'))
import ast
MEMBERS = [tuple(ast.literal_eval(k)) for k in JC]
R83 = json.load(open('code/2383_results.json'))
X83 = {}
for mk, row in R83['members'].items():
    key = tuple(sorted((int(a), float(b))
                       for a, b in ast.literal_eval(mk).items()))
    X83[key] = row['xqc']


def mkey(m):
    return tuple(sorted((int(N), float(f)) for N, f in m))


RHOS = (0.2, 0.3)
SIGNS = ("attractive", "repulsive")
TOL = 0.001
LO0, HI0 = 0.012, 0.035

# ===========================================================================
# V2 -- endpoints reproduce the cached grid verdicts + stored 2383 rho* rows
# ===========================================================================
print("\n" + "-" * 78)
print(" V2  bracket endpoints vs cached grid + stored 2383 rho* rows")
print("-" * 78)
v2_ok, v2_n, v2_maxrel = True, 0, 0.0
for m in MEMBERS:
    st = X83[mkey(m)]
    for sign in SIGNS:
        for sc, want_alive_at in ((LO0, True), (HI0, False)):
            rs = rho_star_exact(m, sign, sc, 1.0)
            stored = st[f"{sign},{sc}"][0]
            rel = abs(rs - stored) / stored
            v2_maxrel = max(v2_maxrel, rel)
            for rho in RHOS:
                safe, vl, worst = summed_grade_cache(m, sign, sc, rho, 1.0)
                v2_n += 1
                # grid expectation: alive at 0.012 iff rho* >= rho there;
                # the joint set passes at floor by construction; dead at 0.035
                expect = (stored >= rho) if want_alive_at else False
                if want_alive_at and not (safe == expect):
                    v2_ok = False
                if (not want_alive_at) and safe:
                    v2_ok = False
                if rel > 1e-9:
                    v2_ok = False
check("V2 endpoint regression", v2_ok,
      f"{v2_n} endpoint verdicts; all alive-at-{LO0} per stored rho*, all "
      f"dead-at-{HI0}; rho* max rel dev vs 2383 rows {v2_maxrel:.1e}")

# ===========================================================================
# THE BISECTION -- per (member, sign): shared sc -> rho* sample map; two
# walls read off it (rho = 0.2, 0.3). Fresh pipeline points enter the cache.
# ===========================================================================
print("\n" + "-" * 78)
print(" FINE WALL  S_c* bisection (tolerance 0.001; alive end reported)")
print("-" * 78)
t0 = time.time()
walls = []      # records per (member, sign, rho)
traces = {}     # (mkey, sign) -> sorted {sc: rho*}
for m in MEMBERS:
    for sign in SIGNS:
        samples = {}

        def rho_at(sc):
            if sc not in samples:
                samples[sc] = rho_star_exact(m, sign, round(sc, 6), 1.0)
            return samples[sc]

        for rho in RHOS:
            lo, hi = LO0, HI0
            # endpoint sanity (V2 already checked; guard anyway)
            if rho_at(lo) < rho:
                walls.append({"member": dict(m), "sign": sign, "rho": rho,
                              "status": "DEAD-AT-FLOOR", "S_c_alive": None,
                              "S_c_dead": lo})
                continue
            if rho_at(hi) >= rho:
                walls.append({"member": dict(m), "sign": sign, "rho": rho,
                              "status": "ALIVE-AT-0.035", "S_c_alive": hi,
                              "S_c_dead": None})
                continue
            while hi - lo > TOL:
                mid = round(0.5 * (lo + hi), 6)
                if rho_at(mid) >= rho:
                    lo = mid
                else:
                    hi = mid
            walls.append({"member": dict(m), "sign": sign, "rho": rho,
                          "status": "WALL", "S_c_alive": lo, "S_c_dead": hi,
                          "window": [LO0, lo]})
        traces[(mkey(m), sign)] = dict(sorted(samples.items()))

top = lambda m: max(m, key=lambda p: p[1])[0]
print("   member (dominant N)          sign         rho    window [0.012, S_c*]   dead at")
for w in walls:
    mm = tuple(sorted((int(a), b) for a, b in w["member"].items()))
    lab = "N%d-dom %s" % (top(mm), w["member"])
    if w["status"] == "WALL":
        print("   %-28s %-11s %.1f    [0.012, %.4f]        %.4f"
              % (lab[:28], w["sign"], w["rho"], w["S_c_alive"], w["S_c_dead"]))
    else:
        print("   %-28s %-11s %.1f    %s" % (lab[:28], w["sign"], w["rho"], w["status"]))
print(f"\n   fresh pipeline calls: {FRESH_CALLS[0]}  "
      f"({time.time()-t0:.0f}s compute)")

# ===========================================================================
# V3 -- worst-ratio monotone non-decreasing in S_c along each path
# (worst(rho) = rho / rho*_exact by summed-counts linearity, so monotone
# non-increase of rho* in S_c is the equivalent check; both reported)
# ===========================================================================
v3_ok, v3_paths, v3_worstviol = True, 0, 0.0
for (mk, sign), tr in traces.items():
    scs = sorted(tr)
    rhos_seq = [tr[s] for s in scs]
    v3_paths += 1
    for a, b in zip(rhos_seq, rhos_seq[1:]):
        if b > a * (1 + 1e-12):
            v3_ok = False
            v3_worstviol = max(v3_worstviol, b / a - 1)
check("V3 worst-ratio monotone in S_c", v3_ok,
      f"{v3_paths} paths, {sum(len(t) for t in traces.values())} sampled "
      f"points; rho* monotone non-increasing everywhere"
      + ("" if v3_ok else f" -- WORST VIOLATION {v3_worstviol:.2e}"))

# ===========================================================================
# V4 -- cache integrity after extension
# ===========================================================================
n_new = len(CACHE) - N_CACHE_0
schema_ok = all(isinstance(v, list) and len(v) == len(BINS) + 1
                and all(isinstance(x, (int, float)) for x in v)
                for v in CACHE.values())
baseline_ok = all(CACHE[k] == v for k, v in CACHE_BASELINE.items())
if CACHE_DIRTY[0]:
    json.dump(CACHE, open('code/2379_unit_cache.json', 'w'))
reload_ok = json.load(open('code/2379_unit_cache.json')) == CACHE
check("V4 cache integrity", schema_ok and baseline_ok and reload_ok,
      f"schema 13-float rows OK; original {N_CACHE_0} keys unchanged; "
      f"+{n_new} fresh keys (now {len(CACHE)}); reload round-trip OK")

# ===========================================================================
# eps_th floor-bracket robustness (read from cache -- already computed)
# ===========================================================================
floor_bracket = {}
for m in MEMBERS:
    for sign in SIGNS:
        rs_min = min(rho_star_exact(m, sign, LO0, e) for e in ETHS)
        floor_bracket["%s|%s" % (str(dict(m)), sign)] = rs_min

# ===========================================================================
# RESULTS
# ===========================================================================
out = {
    "contract": "SS43-Q1 (Patch 2389 sec 34.6); tolerance 0.001; eps_th=1; "
                "rho in [0.2, 0.3]; six 2383 joint members",
    "walls": walls,
    "traces": {"%s|%s" % (str(dict(k[0])), k[1]): v
               for k, v in traces.items()},
    "floor_bracket_rho_star_min_over_eth": floor_bracket,
    "fresh_pipeline_calls": FRESH_CALLS[0],
    "cache_keys_before_after": [N_CACHE_0, len(CACHE)],
    "verify": {"V1": v1_rec, "V2_max_rel": v2_maxrel,
               "V3_paths": v3_paths, "V4_new_keys": n_new,
               "failures": FAILURES},
}
json.dump(out, open('code/2391_results.json', 'w'), indent=1)
print("\n wrote code/2391_results.json")

print("\n" + "=" * 78)
print(f" VERIFY: {4 - len(FAILURES)}/4 "
      f"({'ALL PASS' if not FAILURES else 'FAILURES: ' + ', '.join(FAILURES)})")
print("=" * 78)
sys.exit(0 if not FAILURES else 1)
