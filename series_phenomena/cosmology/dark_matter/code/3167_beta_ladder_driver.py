#!/usr/bin/env python3
"""3167_beta_ladder_driver.py — THE β-LADDER CALIBRATION CAMPAIGN (Kila6).

Executes the FROZEN `beta_ladder_prereg.md` (Patch 3167) verbatim.
Written at Patch 3173, AFTER MemTest86 returned 4 passes / 0 errors
(prereg §5.4 acceptance condition SATISFIED — this campaign is NOT
provisional) and BEFORE any leg has run.

FROZEN DESIGN (prereg §2)
  Geometry: x_half = 28.0, x_src0 = -24.0 (the a2/AK configuration).
  Horizon:  T_END = 264 at EVERY rung (LATE window 216:264 sits 192
            Moments post-step, 2.8x AK's entire horizon).
  Ladder:   beta in {0.10, 0.20, 0.40, 0.60}; N = 128 pairs per rung;
            1024 evidentiary legs + 16 duplicate re-runs.
  Statistic: the corrected Route B recipe VERBATIM from Patch 3164 —
            sust_B = D[LATE] - D[PRE(12:24)], SIGNED, bootstrap over
            pairs, 10000 resamples, seed 30530811, det = signed 99%
            CI excludes 0. No new statistic.

DRIVER-LEVEL IMPLEMENTATION DETAILS, FIXED HERE BEFORE ANY EVIDENTIARY
LEG (the 2968 disclosure precedent; per-patch reasoning fragment
reasoning/3173.md):

  D-1  DRIVE PROTOCOL: beta is applied from T_STEP through T_END,
       identically to every existing arm (run_leg semantics of the
       committed 3055 driver; the engine's beta is prescribed source
       advection, 2902 line 158). No drive-off mechanism is introduced
       — the prereg introduces no new instrument mechanics.
  D-2  KINEMATIC CONSEQUENCE, DISCLOSED: with the drive on throughout,
       the source path length is L = 240*beta per rung:
         beta 0.10 -> L =  24 (ends x =   0.0, inside the Sea)
         beta 0.20 -> L =  48 (ends x = +24.0 — the a2/AK path and
                               endpoint EXACTLY; the prereg's
                               "L = 48.0, Delta = +6" line is realized
                               verbatim at this rung)
         beta 0.40 -> L =  96 (crosses x = +28 near t ~ 154; the LATE
                               window measures the source beyond the
                               Sea's built extent)
         beta 0.60 -> L = 144 (crosses x = +28 near t ~ 111; ditto)
       These are kinematic estimates (the source also responds to
       fields). The founder was shown this table before "go".
  D-3  DUPLICATE SET (prereg §5.1), frozen: per rung, pairs {0, 127}
       x branches {step, ctrl} = 4 legs/rung, 16 total. First copies
       are the evidentiary legs themselves; the SECOND copies are
       produced by `--run-duplicates` in a separate invocation after
       at least one machine restart, into data/beta_ladder/dup/.
  D-4  BIT-IDENTITY (prereg §5.2-5.3): `--verify-duplicates` compares
       the full F and AB arrays element-exact (parsed float64
       equality). ANY mismatch -> CAMPAIGN VOID, written to
       duplicates_verified.json. `--analyze` REFUSES to run unless
       that file exists with status PASS.
  D-5  DETERMINISM GUARD: BLAS/OMP threads pinned to 1 (also the 3143
       oversubscription fix). Each leg is a single-threaded,
       fully-seeded computation; parallelism is across legs only.

MODES (run IN ORDER on Kila6, from this file's directory or anywhere):
  --calibrate        arithmetic kinematics table only (no engine runs)
  --run              the 1024 evidentiary legs (resumable, leg-atomic)
  --run-duplicates   the 16 duplicate re-runs (AFTER a machine restart)
  --verify-duplicates  the hard gate (prereg §5.3)
  --analyze          per-rung sust_B + frozen readings (§3); refuses
                     without a PASS from --verify-duplicates
"""
import os
for _v in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
           'NUMEXPR_NUM_THREADS'):
    os.environ.setdefault(_v, '1')
import argparse, glob, json, sys, time
import importlib.util
from multiprocessing import Pool, cpu_count
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(
    HERE, '../../../../flagship_papers/electromagnetism/code/'
          '2902_mobile_sea_engine.py'))
DATA = os.path.normpath(os.path.join(HERE, '../data/beta_ladder'))
DUP = os.path.join(DATA, 'dup')

# ---- FROZEN (prereg 3167) -------------------------------------------
SEED_GEN = 31670817
T_STEP = 24
T_END = 264
X_HALF, X_SRC0 = 28.0, -24.0
RHO, SPACING = (1.0, 8.0), 2.5
JIT_LO, JIT_HI = -0.05, 0.05
RUNGS = (0.10, 0.20, 0.40, 0.60)
N_PAIRS = 128
NBOOT, BOOT_SEED = 10000, 30530811
PRE = slice(12, 24)                       # Route B PRE_W, verbatim (3164)
K_PRED = 0.026                            # the 2918 prediction, s = K*beta
DUP_PAIRS = (0, 127)                      # D-3
SEEDS = np.random.default_rng(SEED_GEN).integers(10**6, 10**7, size=N_PAIRS)


def rtag(beta):
    return f"b{int(round(beta * 100)):03d}"


def windows(x_half, t_end):
    """Verbatim from the committed 3055/3164 window rule."""
    t_post = int(T_STEP + 1.5 * x_half) + 6
    return t_post, max(12, min(48, (t_end - t_post) // 3))


def _eng():
    spec = importlib.util.spec_from_file_location('eng', SRC)
    eng = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(eng)
    return eng


def build_sea_jittered(eng, seed, x_half):
    """Verbatim from the committed 3055 driver."""
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


def leg_path(pair, branch, beta, dup=False):
    d = DUP if dup else DATA
    return os.path.join(d, f'leg_{pair:04d}_{branch}_{rtag(beta)}.json')


def run_leg(task):
    pair, branch, beta_f, dup = task
    out = leg_path(pair, branch, beta_f, dup)
    if os.path.exists(out):
        return (out, 'skip', 0.0)
    eng = _eng()
    sea, qs = build_sea_jittered(eng, int(SEEDS[pair]), X_HALF)
    pos = np.concatenate([[[X_SRC0, 0.0, 0.0]], sea])
    q = np.concatenate([[1.0], qs])
    T_max = np.sqrt((2 * X_HALF + 20) ** 2 + (2 * RHO[1]) ** 2) + 5
    hist = eng.History(pos, 0.0, int(np.ceil(T_max)) + 2, T_END)
    F, AB, tr = [], [], None
    t0 = time.time()
    for t in range(T_END):
        beta = beta_f if (branch == 'step' and t >= T_STEP) else 0.0
        pos, src_net, src_ab, tr = eng.moment_step(
            pos, q, hist, t, T_max, beta, mobile_sea=True, tr_guess=tr)
        hist.append(pos)
        F.append(float(src_net[0])); AB.append(float(src_ab))
    rec = {'pair': int(pair), 'seed': int(SEEDS[pair]), 'branch': branch,
           'beta_f': beta_f, 'x_half': X_HALF, 'x_src0': X_SRC0,
           't_step': T_STEP, 'T_END': T_END, 'duplicate_copy': bool(dup),
           'N_cp': int(len(pos)), 'F': F, 'AB': AB,
           'wall_s': round(time.time() - t0, 1)}
    os.makedirs(os.path.dirname(out), exist_ok=True)
    tmp = out + '.tmp'
    with open(tmp, 'w') as fh:
        json.dump(rec, fh)
    os.replace(tmp, out)
    return (out, 'done', rec['wall_s'])


def calibrate():
    print(f"{'rung':>5} {'L=240*beta':>10} {'x_end(kin.)':>11} "
          f"{'exits x=+28?':>13} {'t_exit(kin.)':>12}")
    for b in RUNGS:
        L = b * (T_END - T_STEP)
        xe = X_SRC0 + L
        ex = xe > X_HALF
        te = T_STEP + (X_HALF - X_SRC0) / b if ex else float('nan')
        print(f"{b:5.2f} {L:10.1f} {xe:+11.1f} {str(ex):>13} "
              f"{te:12.1f}" if ex else
              f"{b:5.2f} {L:10.1f} {xe:+11.1f} {str(ex):>13} {'—':>12}")
    t_post, base = windows(X_HALF, T_END)
    print(f"windows: PRE 12:24 · t_post {t_post} · LATE {T_END - base}:"
          f"{T_END} ({base} Moments, {T_END - base - T_STEP} post-step)")
    print("No engine runs. This table is the D-2 disclosure.")


def _dup_tasks():
    return [(p, br, b, True) for b in RUNGS for p in DUP_PAIRS
            for br in ('step', 'ctrl')]


def run_all(workers, duplicates=False):
    if duplicates:
        tasks = _dup_tasks()
        print(f"DUPLICATE PASS: {len(tasks)} legs -> {DUP}")
        print("(prereg §5.1: this invocation must be separated from --run "
              "by at least one machine restart)")
    else:
        tasks = [(p, br, b, False) for p in range(N_PAIRS) for b in RUNGS
                 for br in ('step', 'ctrl')]
        tasks.sort(key=lambda t: (t[0], t[2]))     # pair-major, rung-inner
    total, done, t0 = len(tasks), 0, time.time()
    with Pool(workers) as pool:
        for out, st, w in pool.imap_unordered(run_leg, tasks):
            if st == 'done':
                done += 1
                print(f"  done {os.path.basename(out)} ({w:.0f}s) "
                      f"[{done} new; {(time.time() - t0) / 3600:.1f} h]",
                      flush=True)
    d = DUP if duplicates else DATA
    have = len(glob.glob(os.path.join(d, 'leg_*.json')))
    print(f"{'DUPLICATES' if duplicates else 'CAMPAIGN'} "
          f"{'COMPLETE' if have >= total else f'{have}/{total}'}")


def verify_duplicates():
    """Prereg §5.2-5.3: the HARD GATE, checked before any statistic."""
    results, all_ok, missing = [], True, 0
    for (p, br, b, _d) in _dup_tasks():
        a_path = leg_path(p, br, b, dup=False)
        b_path = leg_path(p, br, b, dup=True)
        if not (os.path.exists(a_path) and os.path.exists(b_path)):
            missing += 1
            results.append((os.path.basename(a_path), 'MISSING'))
            continue
        A = json.load(open(a_path)); B = json.load(open(b_path))
        okF = np.array_equal(np.array(A['F']), np.array(B['F']))
        okA = np.array_equal(np.array(A['AB']), np.array(B['AB']))
        ok = bool(okF and okA)
        all_ok &= ok
        results.append((os.path.basename(a_path),
                        'BIT-IDENTICAL' if ok else 'MISMATCH'))
    for name, st in results:
        print(f"  {st:14s} {name}")
    if missing:
        print(f"GATE INCOMPLETE: {missing} duplicate pair(s) missing — "
              f"run --run and --run-duplicates to completion first.")
        status = 'INCOMPLETE'
    elif all_ok:
        print("GATE PASS: all 16 duplicate pairs bit-identical across a "
              "machine restart.")
        status = 'PASS'
    else:
        print("*** GATE FAIL: BIT-IDENTITY BROKEN. THE ENTIRE CAMPAIGN IS "
              "VOID (prereg §5.2 — no partial rescue). ***")
        status = 'VOID'
    with open(os.path.join(DATA, 'duplicates_verified.json'), 'w') as fh:
        json.dump({'status': status,
                   'results': [{'leg': n, 'state': s} for n, s in results]},
                  fh, indent=1)
    return status


def analyze():
    gate_p = os.path.join(DATA, 'duplicates_verified.json')
    if not os.path.exists(gate_p):
        print("REFUSING TO ANALYZE: run --verify-duplicates first "
              "(prereg §5.3).")
        return
    gate = json.load(open(gate_p))
    if gate['status'] != 'PASS':
        print(f"REFUSING TO ANALYZE: duplicate gate status is "
              f"{gate['status']} (prereg §5.2-5.3).")
        return
    t_post, base = windows(X_HALF, T_END)
    LATE = slice(T_END - base, T_END)
    rng = np.random.default_rng(BOOT_SEED)
    print("=" * 78)
    print("THE β-LADDER — sust_B = D[LATE] - D[PRE(12:24)], SIGNED "
          "(3164 recipe verbatim)")
    print("MemTest86: 4 passes, 0 errors, 2026-08-18 — prereg §5.4 "
          "acceptance SATISFIED")
    print("=" * 78)
    per, rows = {}, []
    for b in RUNGS:
        S, C = [], []
        for p in range(N_PAIRS):
            ps, pc = leg_path(p, 'step', b), leg_path(p, 'ctrl', b)
            if not (os.path.exists(ps) and os.path.exists(pc)):
                continue
            S.append(np.array(json.load(open(ps))['F']))
            C.append(np.array(json.load(open(pc))['F']))
        D = np.stack(S) - np.stack(C)
        m = D.shape[0]
        pp = D[:, LATE].mean(axis=1) - D[:, PRE].mean(axis=1)
        s = float(pp.mean())
        boots = np.array([pp[rng.integers(0, m, m)].mean()
                          for _ in range(NBOOT)])
        lo, hi = (float(np.percentile(boots, 0.5)),
                  float(np.percentile(boots, 99.5)))
        per[b] = dict(pp=pp, s=s, lo=lo, hi=hi, m=m, boots=boots)
        k = s / b
        rows.append((b, m, s, lo, hi, k, k / K_PRED))
    print(f"{'beta':>5} {'m':>4} {'sust_B':>12} {'99% CI':>26} "
          f"{'k=s/beta':>10} {'k/0.026':>8}")
    for b, m, s, lo, hi, k, r in rows:
        print(f"{b:5.2f} {m:4d} {s:12.4e} [{lo:.3e},{hi:.3e}] "
              f"{k:10.4e} {r:8.2f}")

    # ratio s(0.60)/s(0.10), bootstrap over pairs independently per rung
    rr = np.random.default_rng(BOOT_SEED + 1)
    p10, p60 = per[0.10]['pp'], per[0.60]['pp']
    ratios = np.array([
        p60[rr.integers(0, len(p60), len(p60))].mean()
        / p10[rr.integers(0, len(p10), len(p10))].mean()
        for _ in range(NBOOT)])
    r_lo, r_hi = (float(np.percentile(ratios, 0.5)),
                  float(np.percentile(ratios, 99.5)))
    print(f"\nratio s(0.60)/s(0.10) = "
          f"{per[0.60]['s'] / per[0.10]['s']:.3f}  99% CI "
          f"[{r_lo:.3f}, {r_hi:.3f}]   (contains 1.0: "
          f"{r_lo <= 1.0 <= r_hi}; contains 6.0: {r_lo <= 6.0 <= r_hi})")

    # through-origin fit, bootstrap-SE weighted
    betas = np.array(RUNGS)
    svals = np.array([per[b]['s'] for b in RUNGS])
    ses = np.array([per[b]['boots'].std() for b in RUNGS])
    w = 1.0 / ses ** 2
    k_hat = float((w * betas * svals).sum() / (w * betas ** 2).sum())
    inband = [per[b]['lo'] <= k_hat * b <= per[b]['hi'] for b in RUNGS]
    print(f"through-origin fit: k_hat = {k_hat:.4e}  "
          f"(prediction {K_PRED:.3e}); every rung's 99% CI contains "
          f"k_hat*beta: {all(inband)} {['%.2f:%s' % (b, i) for b, i in zip(RUNGS, inband)]}")

    has1, has6 = r_lo <= 1.0 <= r_hi, r_lo <= 6.0 <= r_hi
    if all(inband) and has6 and not has1:
        reading = 'BETA-LINEAR'
    elif has1 and not has6:
        reading = 'BETA-FLAT'
    elif not has1 and not has6:
        reading = 'BETA-SUBLINEAR'
        lb = np.log(np.abs(svals)); lx = np.log(betas)
        expo = float(np.polyfit(lx, lb, 1)[0])
        print(f"  exponent (log-log fit over rungs): {expo:.3f} — reported, "
              f"no band re-sited (prereg §3)")
    else:
        reading = 'BETA-UNRESOLVED'
        need = int(np.ceil(N_PAIRS * (max(ses) * 3
                   / max(abs(per[0.10]['s']), 1e-30)) ** 2))
        print(f"  required N estimate from measured scatter: ~{need} "
              f"pairs/rung (reported per §3)")
    print(f"\n>>> FROZEN READING: {reading}")

    # coefficient reading, reported alongside, NOT used to re-site any band
    excl = [not (per[b]['lo'] <= K_PRED * b <= per[b]['hi']) for b in RUNGS]
    if all(excl):
        print(">>> COEFFICIENT-OVERPREDICTED: every rung's 99% CI excludes "
              "0.026*beta — a finding about CPP's own 2918 prediction; "
              "REGISTERED, not adopted (prereg §3).")
    else:
        print(f"coefficient vs 0.026*beta: rung CIs exclude the prediction "
              f"at {sum(excl)}/4 rungs — no COEFFICIENT-OVERPREDICTED flag.")
    print("This campaign does NOT re-run the frozen tree (prereg §4).")
    print("=" * 78)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--calibrate', action='store_true')
    ap.add_argument('--run', action='store_true')
    ap.add_argument('--run-duplicates', action='store_true')
    ap.add_argument('--verify-duplicates', action='store_true')
    ap.add_argument('--analyze', action='store_true')
    ap.add_argument('--workers', type=int, default=min(32, cpu_count()))
    ap.add_argument('--smoke', action='store_true')
    a = ap.parse_args()
    if a.smoke:
        # 3-Moment truncated leg, written nowhere near evidentiary paths
        eng = _eng()
        sea, qs = build_sea_jittered(eng, 1234567, X_HALF)
        pos = np.concatenate([[[X_SRC0, 0.0, 0.0]], sea])
        q = np.concatenate([[1.0], qs])
        T_max = np.sqrt((2 * X_HALF + 20) ** 2 + (2 * RHO[1]) ** 2) + 5
        hist = eng.History(pos, 0.0, int(np.ceil(T_max)) + 2, T_END)
        tr = None
        for t in range(3):
            pos, sn, sa, tr = eng.moment_step(pos, q, hist, t, T_max,
                                              0.0, True, tr)
            hist.append(pos)
        print(f"smoke OK: N_cp={len(pos)}, F0={sn[0]:+.3e}")
    elif a.calibrate:
        calibrate()
    elif a.run:
        run_all(a.workers, duplicates=False)
    elif a.run_duplicates:
        run_all(a.workers, duplicates=True)
    elif a.verify_duplicates:
        verify_duplicates()
    elif a.analyze:
        analyze()
    else:
        ap.print_help()
