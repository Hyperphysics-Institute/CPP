#!/usr/bin/env python3
"""3167_beta_ladder_driver.py — THE β-LADDER CALIBRATION CAMPAIGN (Kila6).

v2 (Patch 3174): R-INSIDE-SEA — the founder ruled no rung may measure with
the source outside the built Sea; ladder rescoped to {0.05, 0.10, 0.15,
0.20} (every path ends at or inside x = +24; the 0.20 rung IS the a2/AK
geometry verbatim). Ratio endpoints 0.05/0.20, proportional reference 4.0.
Any v1 legs are auto-quarantined to data/beta_ladder_void_3173/ on first
v2 --run. Phase 2 (long-Sea beta = 0.60) is chartered CONDITIONAL in
prereg §8 and is NOT this driver. Everything else in the v1 header stands.

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
# Patch 3175: on Windows, redirecting stdout to a file switches Python to the
# legacy cp1252 codec, which cannot encode the Greek beta in the analyze
# header -- --analyze crashed on its FIRST print line under `> out.txt`.
# Force UTF-8 on both streams so file capture works without PYTHONIOENCODING.
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
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
RUNGS = (0.05, 0.10, 0.15, 0.20)   # v2 (Patch 3174, prereg §8)
N_PAIRS = 128
# --- Phase 1B (Patch 3180, prereg beta_ladder_phase1b_prereg.md) ---------
N_PAIRS_1B = 685          # required-N from Phase 1's measured scatter
RUNG_1B = 0.05            # the underpowered rung; NO other rung is extended
DUP_PAIRS_1B = (128, 684) # frozen duplicate membership for Phase 1B
BAND_VOID = True          # 3176: SUST_REF comparator VOID pending OPEN-BAND-CONV-1
NBOOT, BOOT_SEED = 10000, 30530811
PRE = slice(12, 24)                       # Route B PRE_W, verbatim (3164)
K_PRED = 0.026                            # the 2918 prediction, s = K*beta
DUP_PAIRS = (0, 127)                      # D-3
# Drawn at size=N_PAIRS_1B: numpy draws sequentially, so SEEDS[:128] is
# BIT-IDENTICAL to the Phase 1 size=128 table (verified before freezing).
# Phase 1 legs therefore remain valid members of the extended ensemble.
SEEDS = np.random.default_rng(SEED_GEN).integers(10**6, 10**7,
                                                 size=N_PAIRS_1B)
assert len(SEEDS) == N_PAIRS_1B and len(set(SEEDS.tolist())) == N_PAIRS_1B


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


VOID_DIR = os.path.normpath(os.path.join(HERE, '../data/beta_ladder_void_3173'))
V1_TAGS = ('b040', 'b060')     # v1-only rungs; b010/b020 v1 legs are also void
                               # (different protocol vintage) — ALL pre-v2 legs
                               # are moved by timestamped sweep below.


def quarantine_v1():
    """Prereg §8: any leg written under the v1 protocol is EVIDENCE-
    EXCLUDED. v2 starts from an empty evidentiary directory; anything
    already in DATA/DUP is swept to VOID_DIR before v2 writes a leg."""
    moved = 0
    for d in (DATA, DUP):
        for f in glob.glob(os.path.join(d, 'leg_*.json')):
            os.makedirs(VOID_DIR, exist_ok=True)
            os.replace(f, os.path.join(VOID_DIR, os.path.basename(f)))
            moved += 1
    if moved:
        print(f"QUARANTINED {moved} v1 leg(s) -> {VOID_DIR} "
              f"(prereg §8: evidence-excluded)")


def run_all(workers, duplicates=False):
    if not os.path.exists(os.path.join(DATA, '.v2_started')):
        quarantine_v1()
        os.makedirs(DATA, exist_ok=True)
        open(os.path.join(DATA, '.v2_started'), 'w').write('3174\n')
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
    p10, p60 = per[RUNGS[0]]['pp'], per[RUNGS[-1]]['pp']
    ratios = np.array([
        p60[rr.integers(0, len(p60), len(p60))].mean()
        / p10[rr.integers(0, len(p10), len(p10))].mean()
        for _ in range(NBOOT)])
    r_lo, r_hi = (float(np.percentile(ratios, 0.5)),
                  float(np.percentile(ratios, 99.5)))
    R_PROP = RUNGS[-1] / RUNGS[0]          # 4.0 under the v2 ladder
    print(f"\nratio s({RUNGS[-1]})/s({RUNGS[0]}) = "
          f"{per[RUNGS[-1]]['s'] / per[RUNGS[0]]['s']:.3f}  99% CI "
          f"[{r_lo:.3f}, {r_hi:.3f}]   (contains 1.0: "
          f"{r_lo <= 1.0 <= r_hi}; contains {R_PROP}: "
          f"{r_lo <= R_PROP <= r_hi})")

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

    has1, has6 = r_lo <= 1.0 <= r_hi, r_lo <= R_PROP <= r_hi
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
                   / max(abs(per[RUNGS[0]]['s']), 1e-30)) ** 2))
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


# =====================  PHASE 1B  (Patch 3180)  =========================
DATA_1B = os.path.normpath(os.path.join(HERE, '../data/beta_ladder_1b'))
DUP_1B = os.path.join(DATA_1B, 'dup')


def leg_path_1b(pair, branch, dup=False):
    """Phase 1 pairs (<128) live in the Phase 1 tree and are REUSED
    byte-for-byte; only the new pairs are written under DATA_1B."""
    if pair < N_PAIRS and not dup:
        return leg_path(pair, branch, RUNG_1B, dup=False)
    return os.path.join(DUP_1B if dup else DATA_1B,
                        f'leg_{pair:04d}_{branch}_{rtag(RUNG_1B)}.json')


def _tasks_1b(duplicates=False):
    if duplicates:
        return [(p, br, RUNG_1B, 'dup1b') for p in DUP_PAIRS_1B
                for br in ('step', 'ctrl')]
    return [(p, br, RUNG_1B, '1b') for p in range(N_PAIRS, N_PAIRS_1B)
            for br in ('step', 'ctrl')]


def run_leg_1b(task):
    pair, branch, beta_f, mode = task
    out = leg_path_1b(pair, branch, dup=(mode == 'dup1b'))
    if os.path.exists(out):
        return (out, 'skip', 0.0)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    # identical engine path to run_leg; only the destination differs
    saved = (DATA, DUP)
    try:
        return _run_leg_to(task, out)
    finally:
        del saved


def _run_leg_to(task, out):
    pair, branch, beta_f, _mode = task
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
           't_step': T_STEP, 'T_END': T_END, 'phase': '1B',
           'N_cp': int(len(pos)), 'F': F, 'AB': AB,
           'wall_s': round(time.time() - t0, 1)}
    tmp = out + '.tmp'
    with open(tmp, 'w') as fh:
        json.dump(rec, fh)
    os.replace(tmp, out)
    return (out, 'done', rec['wall_s'])


def calibrate_1b():
    n_new = (N_PAIRS_1B - N_PAIRS) * 2
    print(f"PHASE 1B — beta = {RUNG_1B} only, N: {N_PAIRS} -> {N_PAIRS_1B}")
    print(f"  new evidentiary legs : {n_new}")
    print(f"  reused Phase 1 legs  : {N_PAIRS * 2} (byte-for-byte, not recomputed)")
    print(f"  duplicate set        : pairs {DUP_PAIRS_1B} x (step, ctrl) = 4")
    print(f"  seed prefix identical to Phase 1: "
          f"{np.array_equal(SEEDS[:N_PAIRS], np.random.default_rng(SEED_GEN).integers(10**6, 10**7, size=N_PAIRS))}")
    print(f"  est. wall @32 workers: {n_new * 7700 / 32 / 3600:.1f} h")
    print(f"  kinematics unchanged : L = {RUNG_1B * (T_END - T_STEP):.1f}, "
          f"x_end = {X_SRC0 + RUNG_1B * (T_END - T_STEP):+.1f} (inside Sea)")
    print("  ratio endpoints FROZEN at s(0.20)/s(0.05); re-siting forbidden.")
    print("  COEFFICIENT READING SUSPENDED (3176: comparator VOID).")
    print("No engine runs.")


def run_1b(workers, duplicates=False):
    tasks = _tasks_1b(duplicates)
    if duplicates:
        print(f"PHASE 1B DUPLICATE PASS: {len(tasks)} legs -> {DUP_1B}")
        print("(prereg §3: must be separated from --run-1b by a restart)")
    else:
        print(f"PHASE 1B: {len(tasks)} new legs at beta = {RUNG_1B}")
    done, t0 = 0, time.time()
    with Pool(workers) as pool:
        for out, st, w in pool.imap_unordered(run_leg_1b, tasks):
            if st == 'done':
                done += 1
                print(f"  done {os.path.basename(out)} ({w:.0f}s) "
                      f"[{done} new; {(time.time() - t0) / 3600:.1f} h]",
                      flush=True)
    # Patch 3199: count files before declaring, as Phase 1's run_all does.
    # The 3180 version printed COMPLETE unconditionally at the end of the
    # task loop, so a fully-skipped invocation announced success without
    # evidence. Caught on 25 Aug when a post-crash relaunch printed
    # COMPLETE instantly; completeness had to be verified by hand.
    if duplicates:
        have = len(glob.glob(os.path.join(DUP_1B, 'leg_*.json')))
        want = len(_tasks_1b(True))
        print("PHASE 1B DUPLICATES COMPLETE" if have >= want
              else f"PHASE 1B DUPLICATES INCOMPLETE: {have}/{want}")
        return
    have = sum(os.path.exists(leg_path_1b(p_, br))
               for p_ in range(N_PAIRS_1B) for br in ('step', 'ctrl'))
    want = N_PAIRS_1B * 2
    print(f"PHASE 1B CAMPAIGN COMPLETE ({have}/{want} legs present)"
          if have >= want
          else f"PHASE 1B INCOMPLETE: {have}/{want} legs present — "
               f"re-run --run-1b")


def verify_duplicates_1b():
    results, all_ok, missing = [], True, 0
    for (p, br, _b, _m) in _tasks_1b(duplicates=True):
        a_p, b_p = leg_path_1b(p, br), leg_path_1b(p, br, dup=True)
        if not (os.path.exists(a_p) and os.path.exists(b_p)):
            missing += 1
            results.append((os.path.basename(a_p), 'MISSING')); continue
        A, B = json.load(open(a_p)), json.load(open(b_p))
        ok = bool(np.array_equal(np.array(A['F']), np.array(B['F']))
                  and np.array_equal(np.array(A['AB']), np.array(B['AB'])))
        all_ok &= ok
        results.append((os.path.basename(a_p),
                        'BIT-IDENTICAL' if ok else 'MISMATCH'))
    for n, st in results:
        print(f"  {st:14s} {n}")
    status = ('INCOMPLETE' if missing else 'PASS' if all_ok else 'VOID')
    print({'PASS': "GATE PASS: all 4 Phase 1B duplicate pairs bit-identical "
                   "across a machine restart.",
           'VOID': "*** GATE FAIL: PHASE 1B IS VOID (prereg §3). Phase 1's "
                   "own gate is undisturbed. ***",
           'INCOMPLETE': f"GATE INCOMPLETE: {missing} pair(s) missing."}[status])
    os.makedirs(DATA_1B, exist_ok=True)
    with open(os.path.join(DATA_1B, 'duplicates_1b_verified.json'), 'w') as fh:
        json.dump({'status': status,
                   'results': [{'leg': n, 'state': s} for n, s in results]},
                  fh, indent=1)
    return status


def analyze_1b():
    gate_p = os.path.join(DATA_1B, 'duplicates_1b_verified.json')
    if not os.path.exists(gate_p) or json.load(open(gate_p))['status'] != 'PASS':
        print("REFUSING TO ANALYZE: Phase 1B duplicate gate not PASS "
              "(prereg §3). Run --verify-duplicates-1b first.")
        return
    missing = [p for p in range(N_PAIRS_1B) for br in ('step', 'ctrl')
               if not os.path.exists(leg_path_1b(p, br))]
    if missing:
        print(f"REFUSING TO ANALYZE: {len(missing)} beta={RUNG_1B} leg(s) "
              f"missing. Prereg §6 forbids analysis on partial data.")
        return
    t_post, base = windows(X_HALF, T_END)
    LATE = slice(T_END - base, T_END)
    rng = np.random.default_rng(BOOT_SEED)
    print("=" * 78)
    print("PHASE 1B — sust_B = D[LATE] - D[PRE(12:24)], SIGNED "
          "(3164 recipe verbatim); ratio endpoints FROZEN s(0.20)/s(0.05)")
    print("COEFFICIENT READING SUSPENDED — SUST_REF comparator VOID per "
          "Patch 3176, pending OPEN-BAND-CONV-1")
    print("=" * 78)
    per = {}
    for b in RUNGS:
        S, C = [], []
        n = N_PAIRS_1B if b == RUNG_1B else N_PAIRS
        for p in range(n):
            ps = (leg_path_1b(p, 'step') if b == RUNG_1B
                  else leg_path(p, 'step', b))
            pc = (leg_path_1b(p, 'ctrl') if b == RUNG_1B
                  else leg_path(p, 'ctrl', b))
            if not (os.path.exists(ps) and os.path.exists(pc)):
                continue
            S.append(np.array(json.load(open(ps))['F']))
            C.append(np.array(json.load(open(pc))['F']))
        D = np.stack(S) - np.stack(C); m = D.shape[0]
        pp = D[:, LATE].mean(axis=1) - D[:, PRE].mean(axis=1)
        boots = np.array([pp[rng.integers(0, m, m)].mean()
                          for _ in range(NBOOT)])
        per[b] = dict(pp=pp, s=float(pp.mean()), m=m, boots=boots,
                      lo=float(np.percentile(boots, 0.5)),
                      hi=float(np.percentile(boots, 99.5)))
    print(f"{'beta':>5} {'m':>5} {'sust_B':>12} {'99% CI':>26} "
          f"{'k=s/beta (VOID cmp)':>20}")
    for b in RUNGS:
        d = per[b]
        print(f"{b:5.2f} {d['m']:5d} {d['s']:12.4e} "
              f"[{d['lo']:.3e},{d['hi']:.3e}] {d['s'] / b:20.4e}")
    rr = np.random.default_rng(BOOT_SEED + 1)
    p_lo, p_hi = per[RUNGS[0]]['pp'], per[RUNGS[-1]]['pp']
    ratios = np.array([p_hi[rr.integers(0, len(p_hi), len(p_hi))].mean()
                       / p_lo[rr.integers(0, len(p_lo), len(p_lo))].mean()
                       for _ in range(NBOOT)])
    r_lo, r_hi = (float(np.percentile(ratios, 0.5)),
                  float(np.percentile(ratios, 99.5)))
    R_PROP = RUNGS[-1] / RUNGS[0]
    print(f"\nratio s({RUNGS[-1]})/s({RUNGS[0]}) = "
          f"{per[RUNGS[-1]]['s'] / per[RUNGS[0]]['s']:.3f}  99% CI "
          f"[{r_lo:.3f}, {r_hi:.3f}]  (contains 1.0: {r_lo <= 1.0 <= r_hi}; "
          f"contains {R_PROP}: {r_lo <= R_PROP <= r_hi})")
    betas = np.array(RUNGS)
    svals = np.array([per[b]['s'] for b in RUNGS])
    ses = np.array([per[b]['boots'].std() for b in RUNGS])
    w = 1.0 / ses ** 2
    k_hat = float((w * betas * svals).sum() / (w * betas ** 2).sum())
    inband = [per[b]['lo'] <= k_hat * b <= per[b]['hi'] for b in RUNGS]
    print(f"through-origin fit: k_hat = {k_hat:.4e}; every rung's 99% CI "
          f"contains k_hat*beta: {all(inband)} {list(zip(RUNGS, inband))}")
    has1, hasP = r_lo <= 1.0 <= r_hi, r_lo <= R_PROP <= r_hi
    if all(inband) and hasP and not has1:
        reading = 'BETA-LINEAR'
    elif has1 and not hasP:
        reading = 'BETA-FLAT'
    elif not has1 and not hasP:
        reading = 'BETA-SUBLINEAR'
        print(f"  exponent (log-log): "
              f"{float(np.polyfit(np.log(betas), np.log(np.abs(svals)), 1)[0]):.3f}"
              f" — reported, no band re-sited")
    else:
        reading = 'BETA-UNRESOLVED'
        need = int(np.ceil(N_PAIRS_1B * (max(ses) * 3
                   / max(abs(per[RUNGS[0]]['s']), 1e-30)) ** 2))
        print(f"  required N estimate: ~{need} pairs/rung. **STOP** — "
              f"prereg §4 forbids further extension without a fresh prereg "
              f"(no optional stopping).")
    print(f"\n>>> FROZEN READING: {reading}")
    print("Pre-declared expectation was BETA-LINEAR (a recorded REVERSAL of "
          "Phase 1's BETA-FLAT/SUBLINEAR call).")
    print("No coefficient claim. No tree movement. DISP-I3 stands.")
    print("=" * 78)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--calibrate', action='store_true')
    ap.add_argument('--run', action='store_true')
    ap.add_argument('--run-duplicates', action='store_true')
    ap.add_argument('--verify-duplicates', action='store_true')
    ap.add_argument('--analyze', action='store_true')
    ap.add_argument('--workers', type=int, default=min(32, cpu_count()))
    ap.add_argument('--calibrate-1b', dest='calibrate_1b', action='store_true')
    ap.add_argument('--run-1b', dest='run_1b', action='store_true')
    ap.add_argument('--run-duplicates-1b', dest='run_dup_1b', action='store_true')
    ap.add_argument('--verify-duplicates-1b', dest='verify_1b', action='store_true')
    ap.add_argument('--analyze-1b', dest='analyze_1b', action='store_true')
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
    elif a.calibrate_1b:
        calibrate_1b()
    elif a.run_1b:
        run_1b(a.workers, duplicates=False)
    elif a.run_dup_1b:
        run_1b(a.workers, duplicates=True)
    elif a.verify_1b:
        verify_duplicates_1b()
    elif a.analyze_1b:
        analyze_1b()
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
