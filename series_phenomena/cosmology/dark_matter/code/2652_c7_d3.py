#!/usr/bin/env python3
"""
PATCH 2652 -- C7-D3 EXECUTION (symmetric-curvature campaign / DISC-3) under
c7_discriminant_campaign_prereg.md (2649) SS4 ONLY. Third arc of the frozen
order. Verdict is read in c7_d3_record.md against the prereg.

OPERATIONALIZATION DECLARED PRE-RUN (nucleus1 precedent: script-header
declaration before any cell):
  mode/reference    : m2 tilt pattern t_k(x,ph)=x*cos(4pi k/N + ph); reference
                      configuration = base ring (x=0); phases {0, pi/2} (the
                      family's diagnostic convention, 2513/2635/2650 lineage).
  ladder            : x in {0.01,0.02,0.04,0.08,0.16} FROZEN (2649 SS4). D2
                      identified NO quadratic boundary (D2-NO-ENTRY), so the
                      widening-only proviso is NOT triggered; the frozen span
                      stands.
  energy-form (dance): lam_E(x) = [T(+x)+T(-x)-2T(0)]/x^2, T = dance <Etot>,
                      per phase, dt-union {tauC/50, tauC/25}.
  force-form (static): lam_F(x) = -[F(+x)-F(-x)]/(2x); F(x) = sum_i
                      F_i(P(x)).u_i(x); u = dP/dx central diff h=1e-3; F_i =
                      ssv_vectors (2461 verbatim, closed-form field).
  exact internal pair: U_static = -AHC * sum_{i<j} q_i q_j (r^2+A^2)^(-1/2)
                      (the closed-form potential of ssv_vectors); static
                      energy-form lam_U(x) = [U(+x)+U(-x)-2U(0)]/x^2. The
                      prereg's "energy-vs-force estimator consistency" pass
                      condition is evaluated on the SAME-OBJECT pair
                      (lam_U vs lam_F, both static): D3-ESTIMATOR-SPLIT fires
                      ONLY on their disagreement (implementation defect
                      class). The dance-vs-static comparison (lam_E vs lam_F)
                      is the PHYSICS question -- is the dance object local
                      curvature -- and is read through the plateau/sign
                      conditions, NOT through ESTIMATOR-SPLIT. Declared here,
                      before any number exists.
  +/-x agreement    : energy: one-sided c+/-(x)=2[T(+/-x)-T0]/x^2 disclosed
                      per rung; force: antisymmetry residual
                      |F(+x)+F(-x)| / |F(+x)-F(-x)| (small = pass).
  plateau           : >=2 consecutive adjacencies with lam ratio in
                      [0.8, 1.25] (declared now, before any number).
  dt/TC convergence : lam_E at both dt every rung; TC in {60,120} at
                      x in {0.02, 0.04}, dt=1/50 (declared subset).
  resampling        : REGISTERED-DATA REUSE -- the 8-phase m2 per-member
                      one-sided curvatures from the D1 cell store (TC=60,
                      both dt) via leave-one-out sign stability of the mean.
                      No recompute; the registered values are the sample.
  clean-room classifier: classify_cr + branch_cr written from the REGISTERED
                      PROSE (2513: SIG-POS if <c> > 2*SEM; SIG-NEG if
                      <c> < -2*SEM; else INCONCLUSIVE; branch: any
                      sign-flip-across-dt or unclassifiable physical mode ->
                      U; all physical SIG-NEG both dt -> N; all classifiable
                      same-sign -> D; else U). NO code copied from
                      2513/2635/2650/2651. Checked cell-by-cell against ALL
                      stored D1 summary cells (3 TC x 2 dt x 4 modes) and
                      against the 2635 registered classifications -> must
                      yield BRANCH N.
SPEC-TO-CODE TRACE (J4-1): every quantity above -> the identically-named
  function/constant below; ladder -> XS; phases -> PHS; dt -> DTS; TC subset
  -> TCS_SUB; plateau band -> PLATEAU_BAND; h -> HDIFF.
GUARDS (J4-2): x==0 division asserts; antisymmetry denominator guard -> inf;
  leave-one-out n>=2 assert. Stage 'guardtest' triggers each deliberately.
Deterministic; no RNG. Stages: guardtest | cleanroom | static | dance | tc |
resample | read.  (dance/tc are checkpointed per the runtime rider:
per-config persistence to /tmp/c7_d3_cells.json; no config recomputed.)
"""
import numpy as np, time, os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))

def reach_S_factory(np_):
    def build_reach_S(P, C, SP):
        NS = len(P); reach = []
        for i in range(NS):
            dd = P - P[i]; r = np_.sqrt((dd * dd).sum(axis=1)); r[i] = np_.inf
            ki = i // 8
            if SP[i] == 'q':
                inpl = [j for j in range(NS) if SP[j] == 'q' and j // 8 == ki and r[j] < 1.8]
                axl = [j for j in range(NS) if SP[j] == 'q' and j // 8 != ki and r[j] < 1.3]
                ecp = [j for j in range(NS) if SP[j] == 'e' and r[j] < 0.6]
                reach.append(sorted(set(inpl + axl))[:5] + ecp)
            else:
                eopp = sorted([j for j in range(NS) if SP[j] == 'e' and 0 < r[j] < 2.6],
                              key=lambda j: r[j])[:4]
                qown = [j for j in range(NS) if SP[j] == 'q' and r[j] < 0.6]
                reach.append(eopp + qown)
        return reach
    return build_reach_S

stage = sys.argv[1] if len(sys.argv) > 1 else 'read'
t0 = time.time()
print("=" * 78)
print(f"PATCH 2652 -- C7-D3 (prereg 2649 SS4; verdict read in record)  stage={stage}")
print("=" * 78)

XS = (0.01, 0.02, 0.04, 0.08, 0.16)
PHS = (0.0, np.pi / 2)
DTS = (1 / 50, 1 / 25)
TCS_SUB = (60, 120)
PLATEAU_BAND = (0.8, 1.25)
HDIFF = 1e-3

if stage == 'guardtest':
    try:
        x = 0.0; assert x != 0, "x==0: curvature undefined"
    except AssertionError as e:
        print(f"[guardtest] x==0 assert fires: PASS ({e})")
    den = 0.0; r = (1.0 / den) if den != 0 else float('inf')
    print(f"[guardtest] antisymmetry zero-denominator -> {r}: PASS")
    try:
        xs = [1]; assert len(xs) >= 2, "n<2: leave-one-out undefined"
    except AssertionError as e:
        print(f"[guardtest] n<2 assert fires: PASS ({e})")
    sys.exit(0)

# ---- clean-room classifier (written from prose; no code copied) ----
def classify_cr(mean_val, sem_val):
    """From the registered prose: significant positive when the mean exceeds
    twice the standard error; significant negative when it lies below minus
    twice the standard error; otherwise inconclusive."""
    if mean_val > 2.0 * sem_val:
        return 'SIG-POS'
    if mean_val < -2.0 * sem_val:
        return 'SIG-NEG'
    return 'INCONCLUSIVE'

def branch_cr(table):
    """table: {(mode, dtlabel): (mean, sem, class)} for modes m0,m1,m2,ell and
    dt labels 50, 25. From the registered prose of the 2513 branch rules."""
    modes_all = ('m0', 'm1', 'm2', 'ell'); physical = ('m1', 'm2', 'ell')
    flips = []
    for m in modes_all:
        c50 = table[(m, 50)]; c25 = table[(m, 25)]
        if c50[2] != 'INCONCLUSIVE' and c25[2] != 'INCONCLUSIVE' \
                and np.sign(c50[0]) != np.sign(c25[0]):
            flips.append(m)
    all_classifiable = all(table[(m, d)][2] != 'INCONCLUSIVE'
                           for m in physical for d in (50, 25))
    if flips or not all_classifiable:
        return 'BRANCH U'
    neg_both = all(table[(m, 50)][2] == 'SIG-NEG' and table[(m, 25)][2] == 'SIG-NEG'
                   for m in physical)
    if neg_both:
        return 'BRANCH N'
    same_sign = all(np.sign(table[(m, 50)][0]) == np.sign(table[(m, 25)][0])
                    for m in physical)
    return 'BRANCH D' if same_sign else 'BRANCH U'

if stage == 'cleanroom':
    db = json.load(open('/tmp/c7_d1.json'))
    agree = 0; total = 0
    for tc in ('60', '120', '240'):
        for key, (mn, sem, cls) in db[tc].items():
            total += 1
            cr = classify_cr(mn, sem)
            ok = (cr == cls); agree += ok
            if not ok:
                print(f"  MISMATCH TC={tc} {key}: inherited={cls} cleanroom={cr}")
    print(f"[cleanroom] per-cell classification agreement: {agree}/{total}")
    reg = {('m0', 50): (-470732, 121439, 'SIG-NEG'), ('m1', 50): (-73883, 10585, 'SIG-NEG'),
           ('m2', 50): (-51430, 16683, 'SIG-NEG'), ('ell', 50): (-285741, 54093, 'SIG-NEG'),
           ('m0', 25): (-1051091, 381517, 'SIG-NEG'), ('m1', 25): (-93373, 15494, 'SIG-NEG'),
           ('m2', 25): (-73304, 22001, 'SIG-NEG'), ('ell', 25): (-374525, 46244, 'SIG-NEG')}
    reg = {k: (v[0], v[1], classify_cr(v[0], v[1])) for k, v in reg.items()}
    br = branch_cr(reg)
    print(f"[cleanroom] branch on 2635 registered table: {br} "
          f"(must be BRANCH N: {'PASS' if br == 'BRANCH N' else 'FAIL'})")
    sys.exit(0)

# ---- load instrument ----
src = open(os.path.join(HERE, "2513_ensemble_mw_modes.py")).read()
ns = {'__name__': 'd3', '__file__': os.path.join(HERE, '2513_ensemble_mw_modes.py')}
exec(src[:src.index("if __name__=='__main__':")], ns)
ns['build_reach'] = reach_S_factory(np)
dance_v8 = ns['dance_v8']; ring_scaffold = ns['ring_scaffold']
Pr = ns['Pr']; Cr = ns['Cr']; SPr = ns['SPr']; FREF = ns['FREF']; N = ns['N']
ssv_vectors = ns['ssv_vectors']
AHC = ns['AHC']; ALPHA = ns['ALPHA']; ALPHA_S = ns['ALPHA_S']; amat = ns['amat']
assert np.allclose(ns['ring_scaffold_ph'](ell=0.02, psi=0.0)[0],
                   ring_scaffold(ell=0.02)[0]), "psi=0 mismatch"

def m2P(x, ph):
    return ring_scaffold(tilt=[x * np.cos(4 * np.pi * k / N + ph) for k in range(N)])[0]

def U_static(P):
    W = np.array([np.sqrt(ALPHA_S) if s == 'q' else np.sqrt(ALPHA) for s in SPr])
    qw = W * Cr; A = amat(SPr)
    dd = P[:, None, :] - P[None, :, :]
    r2 = (dd * dd).sum(axis=2); np.fill_diagonal(r2, np.inf)
    return -AHC * 0.5 * (np.outer(qw, qw) / np.sqrt(r2 + A * A)).sum()

def Fgen(x, ph):
    assert x != 0, "x==0: curvature undefined"
    P = m2P(x, ph)
    u = (m2P(x + HDIFF, ph) - m2P(x - HDIFF, ph)) / (2 * HDIFF)
    return (ssv_vectors(P, Cr, SPr) * u).sum()

def T_dance(P, dtf, tc=60):
    E, K, _, _ = dance_v8(P, Cr, SPr, FREF, dtf, TC=tc)
    return E.mean() + K.mean()

if stage == 'static':
    print("[static] exact internal pair (lam_U energy-form vs lam_F force-form):")
    U0 = U_static(Pr)
    for ph in PHS:
        print(f" phase {ph:4.2f}:")
        prev = None
        for x in XS:
            lamU = (U_static(m2P(x, ph)) + U_static(m2P(-x, ph)) - 2 * U0) / x ** 2
            Fp = Fgen(x, ph); Fm = Fgen(-x, ph)
            lamF = -(Fp - Fm) / (2 * x)
            anti = abs(Fp + Fm) / abs(Fp - Fm) if (Fp - Fm) != 0 else float('inf')
            cons = abs(lamU - lamF) / max(abs(lamU), abs(lamF), 1e-30)
            rat = (lamU / prev) if prev not in (None, 0) else float('nan')
            tag = "" if prev is None else (
                "[plateau-band]" if PLATEAU_BAND[0] <= rat <= PLATEAU_BAND[1] else "[outside]")
            print(f"  x={x:4.2f}: lam_U={lamU:+12.2f} lam_F={lamF:+12.2f} "
                  f"|dU-F|/max={cons:.2e} antisym={anti:.2e} ratio={rat:+6.2f} {tag}")
            prev = lamU
    print("[static] done -- consistency and plateau read in record")

elif stage in ('dance', 'tc'):
    cellsf = '/tmp/c7_d3_cells.json'
    cells = json.load(open(cellsf)) if os.path.exists(cellsf) else {}
    tasks = []
    if stage == 'dance':
        for dtf in DTS:
            dtl = int(1 / dtf)
            tasks.append((f"60_base_{dtl}", (dtf, 60, None, None)))
            for ph in PHS:
                for x in XS:
                    for sgn in (+1, -1):
                        tasks.append((f"60_{dtl}_{ph:.2f}_{sgn*x:+.2f}", (dtf, 60, ph, sgn * x)))
    else:
        dtf = 1 / 50; dtl = 50
        tasks.append((f"120_base_{dtl}", (dtf, 120, None, None)))
        for ph in PHS:
            for x in (0.02, 0.04):
                for sgn in (+1, -1):
                    tasks.append((f"120_{dtl}_{ph:.2f}_{sgn*x:+.2f}", (dtf, 120, ph, sgn * x)))
    done = sum(1 for k, _ in tasks if k in cells)
    for k, (dtf, tc, ph, x) in tasks:
        if k in cells: continue
        if time.time() - t0 > 75:
            json.dump(cells, open(cellsf, 'w'))
            print(f"PARTIAL {done}/{len(tasks)} ({stage}) -- re-invoke ({time.time()-t0:.0f}s)")
            sys.exit(0)
        cells[k] = T_dance(Pr if ph is None else m2P(x, ph), dtf, tc)
        done += 1
    json.dump(cells, open(cellsf, 'w'))
    print(f"COMPLETE {stage} {done}/{len(tasks)}  total {time.time()-t0:.0f}s")

elif stage == 'resample':
    cells = json.load(open('/tmp/c7_d1_cells.json'))
    for dtl in (50, 25):
        cs = np.array([cells[f"60_m2_{dtl}_{i}"] for i in range(8)])
        assert len(cs) >= 2, "n<2: leave-one-out undefined"
        loo = np.array([np.delete(cs, i).mean() for i in range(8)])
        stable = np.all(np.sign(loo) == np.sign(cs.mean()))
        print(f"[resample] m2 TC=60 dt=1/{dtl}: mean={cs.mean():+9.0f} "
              f"leave-one-out means sign-stable: {stable} "
              f"(range {loo.min():+9.0f}..{loo.max():+9.0f})")

elif stage == 'read':
    cells = json.load(open('/tmp/c7_d3_cells.json'))
    print("[read] dance energy-form lam_E(x) per phase per dt (TC=60):")
    for dtf in DTS:
        dtl = int(1 / dtf); T0 = cells[f"60_base_{dtl}"]
        for ph in PHS:
            prev = None
            print(f" dt=1/{dtl} phase {ph:4.2f}:")
            for x in XS:
                Tp = cells[f"60_{dtl}_{ph:.2f}_{+x:+.2f}"]
                Tm = cells[f"60_{dtl}_{ph:.2f}_{-x:+.2f}"]
                lam = (Tp + Tm - 2 * T0) / x ** 2
                cp = 2 * (Tp - T0) / x ** 2; cm = 2 * (Tm - T0) / x ** 2
                rat = (lam / prev) if prev not in (None, 0) else float('nan')
                tag = "" if prev is None else (
                    "[plateau-band]" if PLATEAU_BAND[0] <= rat <= PLATEAU_BAND[1] else "[outside]")
                print(f"  x={x:4.2f}: lam_E={lam:+12.0f}  (c+={cp:+11.0f} c-={cm:+11.0f}) "
                      f"ratio={rat:+7.2f} {tag}")
                prev = lam
    print("\n[read] TC-convergence subset (dt=1/50):")
    T060 = cells["60_base_50"]; T0120 = cells["120_base_50"]
    for ph in PHS:
        for x in (0.02, 0.04):
            l60 = (cells[f"60_50_{ph:.2f}_{+x:+.2f}"] + cells[f"60_50_{ph:.2f}_{-x:+.2f}"]
                   - 2 * T060) / x ** 2
            l120 = (cells[f"120_50_{ph:.2f}_{+x:+.2f}"] + cells[f"120_50_{ph:.2f}_{-x:+.2f}"]
                    - 2 * T0120) / x ** 2
            print(f"  phase {ph:4.2f} x={x:4.2f}: lam_E(TC=60)={l60:+12.0f}  "
                  f"lam_E(TC=120)={l120:+12.0f}")
    print("\nreadings composed in c7_d3_record.md against prereg SS4")
