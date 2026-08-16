#!/usr/bin/env python
"""Patch 3140 -- the n=7 critical-FSS campaign runner for VideoCPU.
Prereg: n7_critical_fss_prereg.md (frozen BEFORE any n=7 cell ran).
Usage:  python 3140_n7_videocpu_runner.py run      (14 workers, ~1-2 h)
        python 3140_n7_videocpu_runner.py analyze  (prints the summary)
"""
import sys, os, json, importlib.util
from multiprocessing import Pool
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "3140_n7_state.json")
GRID = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
SEEDS = [5, 11]

def _load_mod():
    spec = importlib.util.spec_from_file_location(
        "m", os.path.join(HERE, "3120_ds_indep_campaign.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def one_cell(args):
    ds, seed = args
    m = _load_mod()
    z = m.run(ds, 7, seed)
    return (f"{ds}:{seed}", z)

def cmd_run():
    st = json.load(open(STATE)) if os.path.exists(STATE) else {}
    todo = [(ds, sd) for ds in GRID for sd in SEEDS
            if f"{ds}:{sd}" not in st]
    print(f"n=7 cells remaining: {len(todo)}")
    with Pool(min(14, max(1, len(todo)))) as p:
        for key, z in p.imap_unordered(one_cell, todo):
            st[key] = z
            json.dump(st, open(STATE, "w"))
            print(f"  done {key}: " + " ".join(
                f"{k}={v:.4f}" if isinstance(v, float) else f"{k}={v}"
                for k, v in z.items()))
    print("RUN COMPLETE. Now: python 3140_n7_videocpu_runner.py analyze")

def peak(ds_arr, vals):
    v = np.asarray(vals, float); d = np.asarray(ds_arr, float)
    if np.isnan(v).any() or len(v) < 3:
        return None
    g = np.abs(np.gradient(v, d))
    i = int(np.argmax(g))
    if i == 0 or i == len(d)-1:
        return None
    x = d[i-1:i+2]; y = g[i-1:i+2]
    A = np.vstack([x**2, x, np.ones(3)]).T
    a, b, _ = np.linalg.solve(A, y)
    return float(-b/(2*a)) if a < 0 else float(d[i])

def crit_fit(ns, ds_stars):
    ns = np.asarray(ns, float); y = np.asarray(ds_stars, float)
    best = None
    for nu in np.arange(0.40, 4.001, 0.02):
        x = ns**(-1.0/nu)
        A = np.vstack([x, np.ones_like(x)]).T
        coef, res, *_ = np.linalg.lstsq(A, y, rcond=None)
        sse = float(res[0]) if len(res) else float(((A@coef - y)**2).sum())
        if best is None or sse < best[0]:
            best = (sse, nu, float(coef[1]), float(coef[0]))
    return best  # (sse, nu, d_inf, a)

def cmd_analyze():
    st = json.load(open(STATE))
    # expects the earlier sizes' peaks as constants (frozen record values)
    prior = {"f_b": {3: 3.42, 4: 3.338, 5: 3.106, 6: 2.649},
             "f_dwell": {3: 2.40, 4: 2.388, 5: 2.338}}
    print("== n = 7 per-size peaks (both-seed means) ==")
    n7 = {}
    for par in ("f_b", "f_dwell"):
        vals = []
        for ds in GRID:
            cells = [st[f"{ds}:{sd}"][par] for sd in SEEDS]
            vals.append(float(np.mean(cells)))
        p7 = peak(GRID, vals)
        n7[par] = p7
        print(f"  {par}: peak(n=7) = {p7 if p7 is None else f'{p7:.3f}'}")
    print("== the frozen critical fits: d*(n) = d_inf + a n^(-1/nu) ==")
    d_infs = []
    for par in ("f_b", "f_dwell"):
        pts = dict(prior[par])
        if n7[par] is not None:
            pts[7] = n7[par]
        if len(pts) < 3:
            print(f"  {par}: insufficient (dropped per rule)"); continue
        sse, nu, d_inf, a = crit_fit(list(pts), list(pts.values()))
        d_infs.append(d_inf)
        print(f"  {par}: nu = {nu:.2f}  d_inf = {d_inf:.3f}  (sse {sse:.2e})")
    comb = float(np.mean(d_infs)); spread = max(d_infs)-min(d_infs)
    D = abs(comb - 2.450)
    print(f"COMBINED: d_inf = {comb:.3f} (spread {spread:.3f});  D = |{comb:.3f} - 2.450| = {D:.3f}")
    print("VERDICT (frozen words): " + (
        "CHALLENGE RESOLVES-CONFIRMING" if D <= 0.182 else "CHALLENGE STANDS-QUANTIFIED"))
    print("[Either way: the frozen 2.450 stands unrevised pending panel; full package -> CONV-021]")

if __name__ == "__main__":
    {"run": cmd_run, "analyze": cmd_analyze}[sys.argv[1]]()
