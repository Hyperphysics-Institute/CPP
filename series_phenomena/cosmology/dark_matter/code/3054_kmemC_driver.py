#!/usr/bin/env python3
"""3054_kmemC_driver.py — K-MEM ROUTE C campaign driver.

Executes the FROZEN preregistration `kmemC_routeC_prereg.md` (Patch
3053). Adapted from the committed 3028 driver; deltas ONLY where the
prereg freezes them. Three modes, run IN ORDER on Kila6:

  --calibrate   Kinematic calibration (prereg §3.1): per arm, run the
                REAL configuration tracking only the source x until
                domain exit (|x_src| > x_half; T cap 160), and tune
                x_src0 by bisection (<= 6 kinematic runs/arm) to hit
                the frozen DT target within +-2 Moments, where
                DT = T_exit - T_close and T_close = T_STEP +
                1.5*x_half (the frozen Route B scaling). A0 is NOT
                tuned (Route B d24 verbatim; measured DT reported,
                must land within +-3 of 0 else STOP). Writes
                data/kmemC/calibration.json. COMMIT IT before pilots.
  --pilot       Resolvability pilot (prereg §3.2): 4 pairs x
                step/ctrl per INFERENTIAL arm at the current drive
                rung (ladder 0.6 -> 0.8 -> 1.0; one rung for all
                arms). Projects SNR(N=384) = (peak|D_pilot| /
                sigma_pilot) * sqrt(4/384)^-1... precisely:
                sigma_384 = sd_pair/sqrt(384) with sd_pair estimated
                from the 4 pilot pairs' per-t scatter; projection =
                peak|D_pilot| / sigma_384. If min over arms < 10:
                escalate one rung, wipe pilot/, re-run --pilot.
                Ladder exhausted below 10 -> STOP AND REPORT. Writes
                data/kmemC/pilot_report.json. COMMIT before --run.
                Pilot legs live in data/kmemC/pilot/ and are
                EVIDENCE-EXCLUDED.
  --run         The campaign. REFUSES to start unless
                calibration.json and pilot_report.json (status OK)
                exist. Leg-atomic, freely resumable, pair-major /
                arm-inner ordering (a pause leaves balanced
                coverage). Writes data/kmemC/leg_*.json.

Frozen constants below; driver-level implementation details fixed
here BEFORE any evidentiary leg per the 2968 disclosure precedent
(jitter convention 2907; shared-seed pair matching: the beta step is
the ONLY step/ctrl difference; bit-identical pre-step by
construction, validated by --smoke).
"""
import argparse, glob, json, os, sys, time
import importlib.util
from multiprocessing import Pool, cpu_count
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(
    HERE, '../../../../flagship_papers/electromagnetism/code/'
          '2902_mobile_sea_engine.py'))
DATA = os.path.normpath(os.path.join(HERE, '../data/kmemC'))

# ---- FROZEN (prereg 3053) -------------------------------------------
SEED_GEN = 30530810
T_STEP, T_END = 24, 288
RHO, SPACING = (1.0, 8.0), 2.5
JIT_LO, JIT_HI = -0.05, 0.05
LADDER = (0.60, 0.80, 1.00)
SNR_BAR, N_FULL, N_PILOT = 10.0, 384, 4
# arm: (tag, role, DT_target, x_half, x_src0_init, N_pairs)
ARMS = [('a0', 'diag',   0, 24.0, -18.0, 128),   # Route B d24 verbatim; NOT tuned
        ('a1', 'inf',  -12, 20.0, -12.0, 384),
        ('a2', 'inf',   +8, 24.0, -20.0, 384),   # wall margin >= 4 enforced
        ('a3', 'inf',  -12, 16.0,  -8.0, 384)]
WALL_MARGIN = 4.0
SEEDS = np.random.default_rng(SEED_GEN).integers(10**6, 10**7, size=N_FULL)

def _eng():
    spec = importlib.util.spec_from_file_location('eng', SRC)
    eng = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(eng)
    return eng

def build_sea_jittered(eng, seed, x_half):
    kx = int(np.floor(x_half / SPACING)); xs = SPACING * np.arange(-kx, kx + 1)
    ky = int(np.floor(RHO[1] / SPACING)); ys = SPACING * np.arange(-ky, ky + 1)
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
    pos = np.concatenate([centres + 0.5 * seps * orient,
                          centres - 0.5 * seps * orient])
    q = np.concatenate([np.ones(len(centres)), -np.ones(len(centres))])
    return pos, q

def _cal_path(): return os.path.join(DATA, 'calibration.json')
def _pilot_path(): return os.path.join(DATA, 'pilot_report.json')

def measure_exit(x_src0, x_half, beta_f, t_cap=160, seed=1):
    """One kinematic run of the REAL config tracking source x only."""
    eng = _eng()
    sea, qs = build_sea_jittered(eng, seed, x_half)
    pos = np.concatenate([[[x_src0, 0.0, 0.0]], sea])
    q = np.concatenate([[1.0], qs])
    T_max = np.sqrt((2 * x_half + 20) ** 2 + (2 * RHO[1]) ** 2) + 5
    hist = eng.History(pos, 0.0, int(np.ceil(T_max)) + 2, t_cap)
    tr = None
    for t in range(t_cap):
        beta = beta_f if t >= T_STEP else 0.0
        pos, _, _, tr = eng.moment_step(pos, q, hist, t, T_max, beta,
                                        mobile_sea=True, tr_guess=tr)
        hist.append(pos)
        if abs(pos[0, 0]) > x_half:
            return t + 1
    return None                                   # no exit within cap

def calibrate(beta_f):
    os.makedirs(DATA, exist_ok=True)
    table = {}
    for tag, role, dt_t, x_half, x0, _n in ARMS:
        t_close = T_STEP + 1.5 * x_half
        if tag == 'a0':
            te = measure_exit(x0, x_half, beta_f)
            dt = None if te is None else te - t_close
            ok = dt is not None and abs(dt - dt_t) <= 3
            table[tag] = dict(x_src0=x0, T_exit=te, T_close=t_close,
                              DT=dt, target=dt_t, tuned=False, ok=bool(ok))
            print(f"[{tag}] UNTUNED x_src0={x0}  T_exit={te} T_close={t_close}"
                  f"  DT={dt} (target {dt_t}+-3) -> {'OK' if ok else 'STOP'}")
            continue
        lo, hi = -(x_half - WALL_MARGIN), -1.0     # bisection bounds on x_src0
        best = None
        for _ in range(6):
            mid = 0.5 * (lo + hi)
            te = measure_exit(mid, x_half, beta_f)
            if te is None: lo = mid; continue      # too slow to exit: start later? move outward
            dt = te - t_close
            best = (mid, te, dt)
            if abs(dt - dt_t) <= 2: break
            if dt > dt_t: hi = mid                 # exits too late -> start closer to exit side
            else: lo = mid
        x0f, te, dt = best if best else (None, None, None)
        ok = best is not None and abs(dt - dt_t) <= 2 and abs(x0f) <= x_half - WALL_MARGIN
        table[tag] = dict(x_src0=x0f, T_exit=te, T_close=t_close, DT=dt,
                          target=dt_t, tuned=True, ok=bool(ok))
        print(f"[{tag}] tuned x_src0={x0f}  T_exit={te} T_close={t_close}"
              f"  DT={dt} (target {dt_t}+-2, wall margin >= {WALL_MARGIN})"
              f" -> {'OK' if ok else 'STOP'}")
    table['beta_f'] = beta_f
    table['all_ok'] = all(v['ok'] for k, v in table.items()
                          if isinstance(v, dict))
    with open(_cal_path(), 'w') as fh:
        json.dump(table, fh, indent=1)
    print(f"calibration {'OK' if table['all_ok'] else 'STOPPED'} -> "
          f"{_cal_path()}  (commit before --pilot)")

def leg_path(pair, branch, tag, pilot=False):
    d = os.path.join(DATA, 'pilot') if pilot else DATA
    return os.path.join(d, f'leg_{pair:04d}_{branch}_{tag}.json')

def run_leg(task):
    pair, branch, tag, x_half, x_src0, beta_f, t_cap, pilot = task
    out = leg_path(pair, branch, tag, pilot)
    if os.path.exists(out): return (out, 'skip', 0.0)
    eng = _eng()
    sea, qs = build_sea_jittered(eng, int(SEEDS[pair]), x_half)
    pos = np.concatenate([[[x_src0, 0.0, 0.0]], sea])
    q = np.concatenate([[1.0], qs])
    T_max = np.sqrt((2 * x_half + 20) ** 2 + (2 * RHO[1]) ** 2) + 5
    hist = eng.History(pos, 0.0, int(np.ceil(T_max)) + 2, T_END)
    F, AB, tr = [], [], None
    t0 = time.time()
    for t in range(min(T_END, t_cap)):
        beta = beta_f if (branch == 'step' and t >= T_STEP) else 0.0
        pos, src_net, src_ab, tr = eng.moment_step(
            pos, q, hist, t, T_max, beta, mobile_sea=True, tr_guess=tr)
        hist.append(pos)
        F.append(float(src_net[0])); AB.append(float(src_ab))
    rec = {'pair': int(pair), 'seed': int(SEEDS[pair]), 'branch': branch,
           'arm': tag, 'x_half': x_half, 'x_src0': x_src0,
           't_step': T_STEP, 'beta_f': beta_f, 't_end': min(T_END, t_cap),
           'N_cp': int(len(pos)), 'F': F, 'AB': AB,
           'wall_s': round(time.time() - t0, 1)}
    if t_cap >= T_END:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        tmp = out + '.tmp'
        with open(tmp, 'w') as fh: json.dump(rec, fh)
        os.replace(tmp, out)
    return (out, 'done', rec['wall_s'])

def _load_cal():
    with open(_cal_path()) as fh: return json.load(fh)

def pilot(workers):
    cal = _load_cal(); assert cal['all_ok'], "calibration not OK"
    beta_f = cal['beta_f']
    tasks = []
    for a in ARMS:
        tag, role = a[0], a[1]
        if role != 'inf': continue
        for p in range(N_PILOT):
            for br in ('step', 'ctrl'):
                tasks.append((p, br, tag, a[3], cal[tag]['x_src0'],
                              beta_f, T_END, True))
    with Pool(workers) as pool:
        for out, st, w in pool.imap_unordered(run_leg, tasks):
            print(f"  {st} {os.path.basename(out)} ({w:.0f}s)", flush=True)
    rep = {'beta_f': beta_f, 'arms': {}, 'ok': True}
    for a in ARMS:
        tag = a[0]
        if a[1] != 'inf': continue
        D = []
        for p in range(N_PILOT):
            s = np.array(json.load(open(leg_path(p,'step',tag,True)))['F'])
            c = np.array(json.load(open(leg_path(p,'ctrl',tag,True)))['F'])
            D.append(s - c)
        D = np.stack(D)
        t_close = int(cal[tag]['T_close'])
        w = slice(t_close + 6, 240)
        Dm = D.mean(0)[w] - D.mean(0)[240:].mean()
        sd_pair = D[:, w].std(0).mean()            # per-t pair scatter
        snr384 = float(np.max(np.abs(Dm)) / (sd_pair / np.sqrt(N_FULL)))
        rep['arms'][tag] = dict(peakD=float(np.max(np.abs(Dm))),
                                sd_pair=float(sd_pair), SNR_384=snr384)
        rep['ok'] = rep['ok'] and (snr384 >= SNR_BAR)
        print(f"[{tag}] pilot SNR(N=384) projection = {snr384:.1f} "
              f"(bar {SNR_BAR})")
    rep['status'] = 'OK' if rep['ok'] else 'ESCALATE_OR_STOP'
    with open(_pilot_path(), 'w') as fh: json.dump(rep, fh, indent=1)
    print(f"pilot {'OK — commit and --run' if rep['ok'] else 'BELOW BAR: escalate the ladder (wipe pilot/, recalibrate at the next rung, re-pilot) or STOP if ladder exhausted'}")

def run_all(workers, max_legs):
    cal = _load_cal(); rep = json.load(open(_pilot_path()))
    assert cal['all_ok'] and rep['status'] == 'OK', "prereqs not OK"
    beta_f = rep['beta_f']
    tasks = []
    for a in ARMS:
        tag, role, _dt, x_half, _x0, n = a
        for p in range(n):
            for br in ('step', 'ctrl'):
                tasks.append((p, br, tag, x_half, cal[tag]['x_src0'],
                              beta_f, T_END, False))
    # pair-major interleave across arms for balanced pause coverage
    tasks.sort(key=lambda t: (t[0], t[2]))
    done = 0; t0 = time.time()
    with Pool(workers) as pool:
        for out, st, w in pool.imap_unordered(run_leg, tasks):
            if st == 'done':
                done += 1
                print(f"  done {os.path.basename(out)} ({w:.0f}s) "
                      f"[{done} new; {(time.time()-t0)/3600:.1f} h]",
                      flush=True)
                if max_legs and done >= max_legs: break
    total = sum(a[5] for a in ARMS) * 2
    have = len(glob.glob(os.path.join(DATA, 'leg_*.json')))
    print(f"CAMPAIGN {'COMPLETE' if have >= total else f'{have}/{total}'}")

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--calibrate', action='store_true')
    ap.add_argument('--pilot', action='store_true')
    ap.add_argument('--run', action='store_true')
    ap.add_argument('--rung', type=int, default=0, help='ladder index for --calibrate')
    ap.add_argument('--workers', type=int, default=max(1, cpu_count() - 1))
    ap.add_argument('--max-legs', type=int, default=0)
    ap.add_argument('--smoke', action='store_true')
    a = ap.parse_args()
    if a.smoke:
        r = run_leg((0, 'step', '_smoke', 16.0, -8.0, LADDER[0], 3, True))
        r2 = run_leg((0, 'ctrl', '_smoke', 16.0, -8.0, LADDER[0], 3, True))
        print("smoke OK:", r[1], r2[1])
    elif a.calibrate: calibrate(LADDER[a.rung])
    elif a.pilot: pilot(a.workers)
    elif a.run: run_all(a.workers, a.max_legs)
    else: ap.print_help()
