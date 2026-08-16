#!/usr/bin/env python
"""Patch 3143 -- the n=8 leverage campaign + the REDESIGNED frozen
analysis (prereg: n8_redesign_prereg.md, frozen before any n=8 cell
existed). Usage:
    python 3143_n8_runner.py run       (16 cells, 14 workers, ~3-5 h)
    python 3143_n8_runner.py analyze   (prints interval + verdict)
"""
import sys, os, json, importlib.util
from multiprocessing import Pool
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "3143_n8_state.json")
N7_STATE = os.path.join(HERE, "3140_n7_state.json")
GRID = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
SEEDS = [5, 11]
NSIDE = 8

# prior peaks, frozen record values (3119-3142)
PRIOR_FB = {3: 3.42, 4: 3.338, 5: 3.106, 6: 2.649, 7: 2.617}
PRIOR_FD = {3: 2.40, 4: 2.388, 5: 2.338}

def _mod(name):
    spec = importlib.util.spec_from_file_location("m", os.path.join(HERE, name))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def one_cell(args):
    ds, seed = args
    return (f"{ds}:{seed}", _mod("3120_ds_indep_campaign.py").run(ds, NSIDE, seed))

def cmd_run():
    st = json.load(open(STATE)) if os.path.exists(STATE) else {}
    todo = [(ds, sd) for ds in GRID for sd in SEEDS if f"{ds}:{sd}" not in st]
    print(f"n={NSIDE} cells remaining: {len(todo)}  (checkpointed; safe to interrupt)")
    with Pool(min(14, max(1, len(todo)))) as p:
        for key, z in p.imap_unordered(one_cell, todo):
            st[key] = z; json.dump(st, open(STATE, "w"))
            print(f"  done {key}: " + " ".join(
                f"{k}={v:.4f}" if isinstance(v, float) else f"{k}={v}" for k, v in z.items()))
    print(f"RUN COMPLETE. Now: python 3143_n8_runner.py analyze")

def interval(pts):
    """Frozen rule: A = {nu : SSE <= 1.10*SSE_min and d_inf >= 0}; return
    [min,max] of d_inf over A, plus the profile."""
    ns = np.array(sorted(pts), float); y = np.array([pts[n] for n in sorted(pts)])
    prof = []
    for nu in np.arange(0.40, 4.001, 0.02):
        x = ns**(-1.0/nu)
        A = np.vstack([x, np.ones_like(x)]).T
        c, res, *_ = np.linalg.lstsq(A, y, rcond=None)
        sse = float(res[0]) if len(res) else float(((A@c - y)**2).sum())
        prof.append((float(nu), float(c[1]), sse))
    smin = min(p[2] for p in prof)
    adm = [p for p in prof if p[2] <= 1.10*smin and p[1] >= 0.0]
    if not adm:
        return None, prof
    return (min(p[1] for p in adm), max(p[1] for p in adm)), prof

def cmd_analyze():
    st = json.load(open(STATE))
    runner7 = _mod("3140_n7_videocpu_runner.py")
    fb, fd = [], []
    for ds in GRID:
        fb.append(float(np.mean([st[f"{ds}:{s}"]["f_b"] for s in SEEDS])))
        fd.append(float(np.mean([st[f"{ds}:{s}"]["f_dwell"] for s in SEEDS])))
    p8_fb = runner7.peak(GRID, fb); p8_fd = runner7.peak(GRID, fd)
    print(f"n=8 peaks: f_b = {p8_fb}   f_dwell = {p8_fd}")
    pts = dict(PRIOR_FB)
    if p8_fb is not None: pts[8] = p8_fb
    I, prof = interval(pts)
    print(f"\nPRIMARY (f_b, sizes {sorted(pts)}):")
    print("  nu-profile (nu, d_inf, sse) at samples:",
          [(f"{p[0]:.1f}", f"{p[1]:.2f}") for p in prof[::40]])
    print(f"  frozen interval: {'EMPTY' if I is None else f'[{I[0]:.3f}, {I[1]:.3f}]  width {I[1]-I[0]:.3f}'}")
    pts2 = {k: v for k, v in pts.items() if k != 3}
    I2, _ = interval(pts2)
    print(f"SECONDARY (drop n=3): {'EMPTY' if I2 is None else f'[{I2[0]:.3f}, {I2[1]:.3f}]  width {I2[1]-I2[0]:.3f}'}")
    if p8_fd is not None:
        pf = dict(PRIOR_FD); pf[8] = p8_fd
        I3, _ = interval(pf)
        print(f"f_dwell: {'EMPTY' if I3 is None else f'[{I3[0]:.3f}, {I3[1]:.3f}]'}  (union per 3119 rule)")
        if I and I3: I = (min(I[0], I3[0]), max(I[1], I3[1]))
    print("\n=== VERDICT (frozen words, prereg n8_redesign_prereg.md S4) ===")
    if I is None:
        print("NO-VERDICT-PERSISTS -> AVENUE EXHAUSTED -> panel (economy rule)")
    elif I[1]-I[0] > 1.0:
        print(f"width {I[1]-I[0]:.3f} > 1.0: NO-VERDICT-PERSISTS -> AVENUE EXHAUSTED -> panel")
    elif I[0] <= 2.450 <= I[1]:
        print(f"2.450 in [{I[0]:.3f}, {I[1]:.3f}]: CHALLENGE RESOLVES-CONFIRMING")
    else:
        print(f"2.450 outside [{I[0]:.3f}, {I[1]:.3f}]: CHALLENGE STANDS-QUANTIFIED")
    print("[frozen d_s* = 2.450 unrevised pending panel in every branch; calibration untouched]")

if __name__ == "__main__":
    {"run": cmd_run, "analyze": cmd_analyze}[sys.argv[1]]()
