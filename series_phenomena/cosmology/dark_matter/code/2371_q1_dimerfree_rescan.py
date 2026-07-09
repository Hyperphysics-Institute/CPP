#!/usr/bin/env python3
"""Patch 2371 -- Q1: THE DIMER-FREE RESCAN (the S(N) arc's first cheap kill).
Question: can any N>=3 mixture pass the anchor suite at the audited frames?

PRE-REGISTERED (fixed before run):
  Machinery: 2344's eff()/F-table verbatim (exec-imported). Frames FIXED per
  the attested Clause 1: audited_extended + audited_central (registered also
  graded, record only). Params (NA,NB,gA2,gB2,w,Rs): NA,NB log-uniform
  [3,2000] (THE FLOOR: N>=3, both species); gA2,gB2 log-uniform [1e-6,1e3];
  w uniform [0,1]; Rs log-uniform [20,100]. Search: 400k wide random +
  small-N integer corner stratum (NA,NB in {3,4,5,6,8,10,15,20}, 100k) +
  30k annealing steps per frame from the 30 best seeds. Grading: 2349-style
  violation factor (viol=1.0 <=> pass).
  VERIFY (3, pre-stated): (V-a) machinery equivalence -- stored reopt_central
  params reproduce stored totals to <1e-6 rel; (V-b) floor enforcement -- no
  evaluated point with min(NA,NB)<3 in the floored scan; (V-c) anneal
  stability -- second-seed best viol within 5% of first.
  OUTCOMES (graded as written): (a) no pass at either audited frame ->
  Q1 NEGATIVE, the wide door CLOSES at current anchor demands; (b) pass(es)
  -> composition + costs recorded = the Q2/Q3 target. Outcome (a) is the
  arc-hurting one and nothing in the search is tuned to avoid it."""
import json, math, os, sys
import numpy as np

here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)
src = open("2344_polydisperse_closure.py").read().split("ext = json.load")[0]
g = {'__file__': os.path.join(here,'2344_polydisperse_closure.py')}; exec(src, g)
eff = g['eff']
FR = json.load(open("2345_l4_results.json"))["frames"]

def viol(tot, frame):
    v = 1.0
    for vel,(lo,hi) in frame.items():
        t = tot[int(vel)]
        if t < lo: v = max(v, lo/max(t,1e-12))
        if t > hi: v = max(v, t/hi)
    return v

# V-a: machinery equivalence
L4 = json.load(open("2345_l4_results.json"))
rp = L4["reopt_central"]["params"]; st = L4["reopt_central"]["totals"]
tot = eff(rp)
va = max(abs(tot[int(k)]-v)/v for k,v in st.items())
print(f"V-a machinery equivalence: max rel dev {va:.2e}")

rng = np.random.default_rng(7)
def sample(n, integer_corner=False):
    if integer_corner:
        Ns = np.array([3,4,5,6,8,10,15,20], float)
        NA = rng.choice(Ns, n); NB = rng.choice(Ns, n)
    else:
        NA = np.exp(rng.uniform(math.log(3), math.log(2000), n))
        NB = np.exp(rng.uniform(math.log(3), math.log(2000), n))
    gA = np.exp(rng.uniform(math.log(1e-6), math.log(1e3), n))
    gB = np.exp(rng.uniform(math.log(1e-6), math.log(1e3), n))
    w  = rng.uniform(0, 1, n)
    Rs = np.exp(rng.uniform(math.log(20), math.log(100), n))
    return np.stack([NA,NB,gA,gB,w,Rs], axis=1)

def best_of(P, frame):
    bv, bp = 1e30, None
    floor_ok = True
    for p in P:
        if min(p[0],p[1]) < 3: floor_ok = False
        v = viol(eff(p), frame)
        if v < bv: bv, bp = v, p.copy()
    return bv, bp, floor_ok

def anneal(p0, frame, steps=30000, seed=11):
    r = np.random.default_rng(seed)
    p = p0.copy(); bv = viol(eff(p), frame); best = (bv, p.copy())
    T = 0.4
    lo = np.array([3,3,1e-6,1e-6,0,20.]); hi = np.array([2000,2000,1e3,1e3,1,100.])
    for i in range(steps):
        T *= (1 - 3.0/steps)
        q = p.copy()
        j = r.integers(0,6)
        if j in (0,1,2,3,5): q[j] = np.clip(q[j]*math.exp(r.normal(0,0.25)), lo[j], hi[j])
        else: q[4] = np.clip(q[4]+r.normal(0,0.05), 0, 1)
        v = viol(eff(q), frame)
        if v < bv or r.random() < math.exp(-(v-bv)/max(T,1e-4)):
            p, bv = q, v
            if v < best[0]: best = (v, q.copy())
    return best

P_wide = sample(400_000); P_corner = sample(100_000, integer_corner=True)
res = {"prereg":"header", "V":{"a_rel_dev":va}}
floor_all = True
for fname in ("audited_extended","audited_central","registered"):
    F = FR[fname]
    v1,p1,f1 = best_of(P_wide, F); v2,p2,f2 = best_of(P_corner, F)
    floor_all &= f1 and f2
    seedp = p1 if v1<v2 else p2
    bv, bp = anneal(seedp, F, seed=11)
    bv2, _ = anneal(seedp, F, seed=97)
    res[fname] = {"wide_best":v1,"corner_best":v2,"anneal_best":bv,
                  "anneal_seed2":bv2,"best_params":[float(x) for x in bp],
                  "best_totals":{k:float(v) for k,v in eff(bp).items()},
                  "PASS": bool(bv <= 1.0 + 1e-9)}
    print(f"{fname:18s} wide={v1:.4f} corner={v2:.4f} anneal={bv:.4f} (seed2 {bv2:.4f}) "
          f"PASS={res[fname]['PASS']}  best N=({bp[0]:.2f},{bp[1]:.2f}) w={bp[4]:.3f} Rs={bp[5]:.1f}")
res["V"]["b_floor_enforced"] = floor_all
sA = res["audited_extended"]["anneal_best"]; sB = res["audited_extended"]["anneal_seed2"]
res["V"]["c_anneal_stable"] = bool(abs(sA-sB)/sA < 0.05)
res["V"]["passed"] = f"{int(va<1e-6)+int(floor_all)+int(res['V']['c_anneal_stable'])}/3"
res["OUTCOME"] = ("(b) PASS EXISTS" if any(res[f]["PASS"] for f in ("audited_extended","audited_central"))
                  else "(a) NO DIMER-FREE PASS AT EITHER AUDITED FRAME")
print("VERIFY:", res["V"]); print("OUTCOME:", res["OUTCOME"])
json.dump(res, open("2371_results.json","w"), indent=1)
