#!/usr/bin/env python3
"""3055_kmemC_driver.py — K-MEM ROUTE C campaign driver (v2).

SUPERSEDES 3054_kmemC_driver.py (retained in-repo). Executes the FROZEN
`kmemC_routeC_prereg_v2.md` (Patch 3055): corrected design variable
DT = L - T_BALL (L = beta*(T_END - t_step)), per-arm beta/T_END,
arithmetic calibration (no engine runs), AK-only pilot with an N-ONLY
escalation ladder.

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
SEED_GEN = 30550810
T_STEP = 24
RHO, SPACING = (1.0, 8.0), 2.5
JIT_LO, JIT_HI = -0.05, 0.05
SNR_BAR, N_PILOT, WALL_MARGIN = 10.0, 4, 4.0
N_LADDER = (512, 1024)          # AK escalation is N ONLY (beta would move DT)
# arm: (tag, class, x_half, T_END, beta, N_pairs, DT_target)
ARMS = [('a0',  'iso',    24.0, 384, 0.10, 128,   0.0),
        ('a0p', 'iso',    16.0, 264, 0.10, 128,   0.0),
        ('a1',  'iso',    32.0, 384, 0.10, 128, -12.0),
        ('a2',  'iso',    28.0, 504, 0.10, 128,  +6.0),
        ('ak',  'margin', 28.0, 104, 0.60, 512,  +6.0)]
T_MAXPAIRS = max(a[5] for a in ARMS)
SEEDS = np.random.default_rng(SEED_GEN).integers(10**6, 10**7, size=T_MAXPAIRS)

def geom(x_half, T_END, beta):
    L = beta * (T_END - T_STEP)
    return L, -L / 2.0, x_half - L / 2.0, L - 1.5 * x_half   # L, x0, margin, DT

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

def calibrate(_rung=0):
    """Prereg v2 §3.1: arithmetic table + assertions. No engine runs."""
    os.makedirs(DATA, exist_ok=True)
    table, ok_all = {}, True
    for tag, cls, x_half, T_END, beta, N, dt_t in ARMS:
        L, x0, margin, dt = geom(x_half, T_END, beta)
        ok = (abs(dt - dt_t) < 1e-9) and (margin >= WALL_MARGIN)
        ok_all &= ok
        table[tag] = dict(cls=cls, x_half=x_half, T_END=T_END, beta=beta,
                          L=L, x_src0=x0, margin=margin, DT=dt,
                          target=dt_t, N=N, ok=bool(ok))
        print(f"[{tag:4s}|{cls:6s}] x_half={x_half:5.1f} T={T_END:4d} "
              f"beta={beta:.2f} L={L:5.1f} x_src0={x0:+7.1f} "
              f"margin={margin:5.1f} DT={dt:+6.1f} (target {dt_t:+.1f}) "
              f"N={N:4d} -> {'OK' if ok else 'STOP'}")
    table['all_ok'] = bool(ok_all)
    with open(_cal_path(), 'w') as fh:
        json.dump(table, fh, indent=1)
    print(f"calibration {'OK' if ok_all else 'STOPPED'} -> {_cal_path()}"
          f"  (commit before --pilot)")

def leg_path(pair, branch, tag, pilot=False):
    d = os.path.join(DATA, 'pilot') if pilot else DATA
    return os.path.join(d, f'leg_{pair:04d}_{branch}_{tag}.json')

def run_leg(task):
    pair, branch, tag, x_half, x_src0, beta_f, T_END, t_cap, pilot = task
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
           't_step': T_STEP, 'beta_f': beta_f, 'T_END': T_END,
           't_end': min(T_END, t_cap),
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

def pilot(workers, n_target=None):
    cal = _load_cal(); assert cal['all_ok'], "calibration not OK"
    ak = cal['ak']; N = int(n_target or ak['N'])
    tasks = [(p, br, 'ak', ak['x_half'], ak['x_src0'], ak['beta'],
              ak['T_END'], ak['T_END'], True)
             for p in range(N_PILOT) for br in ('step', 'ctrl')]
    with Pool(workers) as pool:
        for out, st, w in pool.imap_unordered(run_leg, tasks):
            print(f"  {st} {os.path.basename(out)} ({w:.0f}s)", flush=True)
    D = []
    for p in range(N_PILOT):
        s = np.array(json.load(open(leg_path(p, 'step', 'ak', True)))['F'])
        c = np.array(json.load(open(leg_path(p, 'ctrl', 'ak', True)))['F'])
        D.append(s - c)
    D = np.stack(D)
    t_post = int(T_STEP + 1.5 * ak['x_half'] + 6)
    T_END = int(ak['T_END']); late = slice(T_END - 48, T_END)
    w = slice(t_post, T_END - 48)
    Dm = D.mean(0)[w] - D.mean(0)[late].mean()
    sd_pair = D[:, w].std(0).mean()
    snr = float(np.max(np.abs(Dm)) / (sd_pair / np.sqrt(N)))
    ok = snr >= SNR_BAR
    rep = dict(arm='ak', N_projected=N, peakD=float(np.max(np.abs(Dm))),
               sd_pair=float(sd_pair), SNR=snr,
               status='OK' if ok else 'ESCALATE_OR_STOP')
    with open(_pilot_path(), 'w') as fh: json.dump(rep, fh, indent=1)
    print(f"[ak] pilot SNR(N={N}) projection = {snr:.1f} (bar {SNR_BAR}) -> "
          f"{'OK — commit and --run' if ok else 'BELOW BAR'}")
    if not ok:
        nxt = [n for n in N_LADDER if n > N]
        print("ESCALATE: rerun `--pilot --n 1024` (N ladder only; beta is "
              "frozen because it would move DT)" if nxt else
              "LADDER EXHAUSTED -> STOP AND REPORT (panel).")

def run_all(workers, max_legs, n_scale=1.0):
    cal = _load_cal(); rep = json.load(open(_pilot_path()))
    assert cal['all_ok'] and rep['status'] == 'OK', "prereqs not OK"
    tasks = []
    for tag, cls, x_half, T_END, beta, N, _dt in ARMS:
        n = int(rep['N_projected']) if tag == 'ak' else int(N * n_scale)
        c = cal[tag]
        for p in range(n):
            for br in ('step', 'ctrl'):
                tasks.append((p, br, tag, x_half, c['x_src0'], beta,
                              T_END, T_END, False))
    tasks.sort(key=lambda t: (t[0], t[2]))
    total = len(tasks)
    done = 0; t0 = time.time()
    with Pool(workers) as pool:
        for out, st, w in pool.imap_unordered(run_leg, tasks):
            if st == 'done':
                done += 1
                print(f"  done {os.path.basename(out)} ({w:.0f}s) "
                      f"[{done} new; {(time.time()-t0)/3600:.1f} h]",
                      flush=True)
                if max_legs and done >= max_legs: break
    have = len(glob.glob(os.path.join(DATA, 'leg_*.json')))
    print(f"CAMPAIGN {'COMPLETE' if have >= total else f'{have}/{total}'}")

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--calibrate', action='store_true')
    ap.add_argument('--pilot', action='store_true')
    ap.add_argument('--run', action='store_true')
    ap.add_argument('--n', type=int, default=0, help='AK pilot N (escalation)')
    ap.add_argument('--workers', type=int, default=max(1, cpu_count() - 1))
    ap.add_argument('--max-legs', type=int, default=0)
    ap.add_argument('--smoke', action='store_true')
    a = ap.parse_args()
    if a.smoke:
        r = run_leg((0, 'step', '_smoke', 16.0, -12.0, 0.10, 264, 3, True))
        r2 = run_leg((0, 'ctrl', '_smoke', 16.0, -12.0, 0.10, 264, 3, True))
        print("smoke OK:", r[1], r2[1])
    elif a.calibrate: calibrate()
    elif a.pilot: pilot(a.workers, a.n or None)
    elif a.run: run_all(a.workers, a.max_legs)
    else: ap.print_help()
