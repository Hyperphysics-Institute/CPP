#!/usr/bin/env python3
"""3028_kmem3_driver.py — K-MEM-MEAS-3 (TAIL-1 Route B) campaign driver.

Executes the FROZEN preregistration `kmem_meas3_routeB_prereg.md` (Patch 3027).
Adapted from the committed 2983 driver; deltas ONLY where the prereg
freezes them: three domains {24, 28, 32}, T_END = 384, x_src0 = -18.0,
64 shared-seed pairs, data/kmem3, effort-bound extrapolation printout.
The prereg is authoritative; this driver only sequences the committed 2902
engine. Driver-level frozen constants (implementation details the prereg left
to the driver, fixed here BEFORE any evidentiary leg runs, per the 2968
disclosure precedent):
  - Seed jitter convention = the committed 2907 EM-lane convention: per-DP
    separation D0 + uniform(-0.05, +0.05), drawn from default_rng(seed).
  - Both legs of a pair use the IDENTICAL jittered sea (same seed) and the
    identical source start x_src0 = -10.8 (the 2968 L1 geometry); the step
    flag (beta 0 -> 0.10 at t = 24) is the ONLY difference. Legs are
    bit-identical for t < 24 by construction (validated by --smoke).
  - Control legs run the full 240-Moment window (pair-matched subtraction
    requires matched windows).
  - Domain sub-ensemble (pairs 0..127): x_half doubled 16 -> 32, all else
    identical.

Usage:
  python3 2983_kmem2_driver.py [--workers N] [--max-legs M] [--smoke]

Leg-atomic and freely resumable: each completed leg writes one JSON into
data/kmem2/ and is skipped on restart. Stop/restart any time. NO statistic
across legs is computed here — analysis is a separate script that refuses to
run until the manifest is complete (prereg: no interim looks).
"""
import argparse
import json
import os
import sys
import time
import importlib.util
from multiprocessing import Pool, cpu_count

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(
    HERE, '../../../../flagship_papers/electromagnetism/code/'
          '2902_mobile_sea_engine.py'))
DATA = os.path.normpath(os.path.join(HERE, '../data/kmem3'))

# ---- FROZEN (prereg 3027 + carried driver-level constants) ---------------
SEED_GEN = 30280001
N_PAIRS = 64
DOMAINS = ((24.0, 'd24'), (28.0, 'd28'), (32.0, 'd32'))
T_STEP, BETA_F, T_END = 24, 0.10, 384
RHO = (1.0, 8.0)
X_SRC0 = -18.0
SPACING = 2.5
JIT_LO, JIT_HI = -0.05, 0.05   # 2907 convention, carried
EST_TOTAL_CPU_S = 721 * 3600   # prereg §1 effort-bound reference

SEEDS = np.random.default_rng(SEED_GEN).integers(10**6, 10**7, size=N_PAIRS)


def _eng():
    spec = importlib.util.spec_from_file_location('eng', SRC)
    eng = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(eng)
    return eng


def build_sea_jittered(eng, seed, x_half):
    """2902 build_sea geometry with the 2907 seeded separation jitter."""
    kx = int(np.floor(x_half / SPACING))
    xs = SPACING * np.arange(-kx, kx + 1)
    ky = int(np.floor(RHO[1] / SPACING))
    ys = SPACING * np.arange(-ky, ky + 1)
    rng = np.random.default_rng(seed)
    centres, orient, seps = [], [], []
    for x in xs:
        for y in ys:
            for z in ys:
                rho = np.hypot(y, z)
                if RHO[0] <= rho <= RHO[1]:
                    centres.append((x, y, z))
                    orient.append((0.0, y / rho, z / rho))
                    seps.append(eng.D0 + rng.uniform(JIT_LO, JIT_HI))
    centres = np.array(centres); orient = np.array(orient)
    seps = np.array(seps)[:, None]
    plus = centres + 0.5 * seps * orient
    minus = centres - 0.5 * seps * orient
    pos = np.concatenate([plus, minus])
    q = np.concatenate([np.ones(len(plus)), -np.ones(len(minus))])
    return pos, q


def leg_path(pair, branch, tag):
    return os.path.join(DATA, f'leg_{pair:04d}_{branch}_{tag}.json')


def run_leg(task):
    pair, branch, x_half, tag, t_cap = task
    out = leg_path(pair, branch, tag)
    if os.path.exists(out):
        return (out, 'skip', 0.0)
    eng = _eng()
    sea, qs = build_sea_jittered(eng, int(SEEDS[pair]), x_half)
    pos = np.concatenate([[[X_SRC0, 0.0, 0.0]], sea])
    q = np.concatenate([[1.0], qs])
    T_max = np.sqrt((2 * x_half + 20) ** 2 + (2 * RHO[1]) ** 2) + 5
    t_end = min(T_END, t_cap)
    hist = eng.History(pos, 0.0, int(np.ceil(T_max)) + 2, T_END)
    F, AB, tr = [], [], None
    t0 = time.time()
    for t in range(t_end):
        beta = BETA_F if (branch == 'step' and t >= T_STEP) else 0.0
        pos, src_net, src_ab, tr = eng.moment_step(
            pos, q, hist, t, T_max, beta, mobile_sea=True, tr_guess=tr)
        hist.append(pos)
        F.append(float(src_net[0])); AB.append(float(src_ab))
    rec = {'pair': int(pair), 'seed': int(SEEDS[pair]), 'branch': branch,
           'domain': tag, 'x_half': x_half,
           't_step': T_STEP, 'beta_f': BETA_F, 't_end': t_end,
           'N_cp': int(len(pos)), 'F': F, 'AB': AB,
           'wall_s': round(time.time() - t0, 1)}
    if t_cap >= T_END:                       # only full legs are evidentiary
        tmp = out + '.tmp'
        with open(tmp, 'w') as fh:
            json.dump(rec, fh)
        os.replace(tmp, out)                 # atomic
    return (out, 'done', rec['wall_s'])


def all_tasks():
    tasks = []
    for p in range(N_PAIRS):                 # pair-major, domain-inner:
        for x_half, tag in DOMAINS:          # a pause leaves balanced coverage
            for br in ('step', 'ctrl'):
                tasks.append((p, br, x_half, tag, T_END))
    return tasks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--workers', type=int, default=max(1, cpu_count() - 1))
    ap.add_argument('--max-legs', type=int, default=0,
                    help='stop after completing this many new legs (0 = all)')
    ap.add_argument('--smoke', action='store_true',
                    help='validation only: 1 pair x 3 Moments, NOT archived')
    a = ap.parse_args()

    if a.smoke:
        eng = _eng()
        r1 = run_leg((0, 'step', DOMAINS[0][0], '_smoke', 3))
        # identical-stream validation: step and ctrl bit-identical for t < T_STEP
        sea1, _ = build_sea_jittered(eng, int(SEEDS[0]), DOMAINS[0][0])
        sea2, _ = build_sea_jittered(eng, int(SEEDS[0]), DOMAINS[0][0])
        same = np.array_equal(sea1, sea2)
        print(f"[smoke] leg path exercised ({r1[1]}); paired-sea bit-identity "
              f"for same seed: {same}; N_cp = {len(sea1) + 1}")
        print("[smoke] nothing archived; evidentiary data untouched.")
        return 0

    os.makedirs(DATA, exist_ok=True)
    tasks = all_tasks()
    pending = [t for t in tasks if not os.path.exists(leg_path(t[0], t[1], t[3]))]
    print(f"[campaign] legs total {len(tasks)}, complete "
          f"{len(tasks) - len(pending)}, pending {len(pending)}; "
          f"workers = {a.workers}")
    if a.max_legs:
        pending = pending[:a.max_legs]
    done = 0; cpu = 0.0; t0 = time.time()
    with Pool(a.workers) as pool:
        for out, st, w in pool.imap_unordered(run_leg, pending):
            done += 1; cpu += w
            msg = (f"[{done}/{len(pending)}] {os.path.basename(out)} "
                   f"{st} {w:.0f}s  (elapsed {(time.time()-t0)/60:.0f} min)")
            if done >= 24 and st == 'done':
                proj = cpu / done * len(pending) / 3600
                msg += f"  [effort-bound: projected total ~{proj:.0f} CPU-h"                        f" vs est {EST_TOTAL_CPU_S/3600:.0f}; PAUSE if > 2x]"
            print(msg, flush=True)
    remaining = [t for t in tasks if not os.path.exists(leg_path(t[0], t[1], t[3]))]
    if not remaining:
        print("CAMPAIGN COMPLETE — all 384 legs archived. "
              "Run 3028_kmem3_analysis.py.")
    else:
        print(f"session done; {len(remaining)} legs remain — rerun to resume.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
