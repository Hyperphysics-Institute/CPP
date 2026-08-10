#!/usr/bin/env python3
"""3052_kappa_sys_margin.py — implements kappa_sys_margin_prereg.md
(Patch 3051) VERBATIM. Reports whatever the frozen pipeline prints."""
import json, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, '../data/kmem2'))
T, TSTEP, TPOST, LATE = 240, 24, 48, slice(200, 240)
NBOOT, SEED, Z99 = 10000, 30510810, 2.576

def census(dom):
    import glob
    return len(glob.glob(f'{DATA}/leg_*_step_{dom}.json'))

def load(dom):
    n = census(dom)
    S = np.empty((n, T)); C = np.empty((n, T))
    for p in range(n):
        S[p] = json.load(open(f'{DATA}/leg_{p:04d}_step_{dom}.json'))['F']
        C[p] = json.load(open(f'{DATA}/leg_{p:04d}_ctrl_{dom}.json'))['F']
    return S - C                                  # paired responses

def pipeline(d):
    """d: (n_pairs, T) paired responses -> (kappa, branch, |W|, t_c)"""
    Db = d.mean(0)
    D = Db - Db[LATE].mean()
    return D

def estimate(D, sig):
    W = []
    for t in range(TPOST, 200):
        if abs(D[t]) > 3 * sig[t]:
            W.append(t)
        else:
            break
    if len(W) >= 8:
        w = np.array(W)
        y = np.log(np.abs(D[w])); wt = (np.abs(D[w]) / sig[w]) ** 2
        s = np.polyfit(w, y, 1, w=np.sqrt(wt))[0]
        return float(np.exp(s)), 'FIT', len(W), None
    tc = None
    for t in range(TPOST - 1, TSTEP, -1):
        if abs(D[t]) > 3 * sig[t]:
            tc = t; break
    if tc is not None:
        kb = (3 * sig[TPOST] / abs(D[tc])) ** (1.0 / (TPOST - tc))
        return float(kb), 'BOUND', len(W), tc
    return np.nan, 'INDETERMINATE', len(W), None

def run(dom, gating):
    d = load(dom)
    n = d.shape[0]
    print(f"[{dom}] pair census: {n} (prereg text said 320 by arithmetic slip; operative word ALL — full ensemble used; the 320-subset first execution is disclosed in the record)")
    rng = np.random.default_rng(SEED)
    # sigma(t) from pair bootstrap of the mean
    boots = np.empty((NBOOT, T))
    idx = rng.integers(0, n, size=(NBOOT, n))
    for b in range(NBOOT):
        boots[b] = d[idx[b]].mean(0)
    sig = boots.std(0)
    D = pipeline(d)
    k, br, nw, tc = estimate(D, sig)
    # full-pipeline bootstrap CI (branch/window reselected per replicate)
    ks = []
    for b in range(NBOOT):
        Db = boots[b]; Dd = Db - Db[LATE].mean()
        kb, brb, _, _ = estimate(Dd, sig)
        if not np.isnan(kb):
            ks.append(kb)
    ks = np.array(ks)
    lo, hi = (np.percentile(ks, 0.5), np.percentile(ks, 99.5)) if len(ks) else (np.nan, np.nan)
    peak = float(np.max(np.abs(D[TSTEP:200])))
    tpk = int(TSTEP + np.argmax(np.abs(D[TSTEP:200])))
    print(f"[{dom}] branch={br} |W|={nw} t_c={tc}  kappa_sys={k:.4f}  "
          f"99% CI [{lo:.4f}, {hi:.4f}]  (replicates resolved: {len(ks)}/{NBOOT})")
    print(f"[{dom}] D(t): peak |D|={peak:.3e} at t={tpk}; sigma(t_post)={sig[TPOST]:.3e}; "
          f"delta = 1 - upper99 = {1-hi:.4f}")
    if gating:
        ok = (br != 'INDETERMINATE') and (hi < 1.0)
        print(f"GATE G1: {'PASS' if ok else 'FAIL'} — "
              f"{'kappa_sys upper-99 < 1, branch resolved' if ok else 'marginal or indeterminate -> Route C executes'}")
    return k, (lo, hi), br

print("kappa_sys margin — frozen pipeline (prereg Patch 3051; seed 30510810)")
run('std', gating=True)
run('dom', gating=False)
