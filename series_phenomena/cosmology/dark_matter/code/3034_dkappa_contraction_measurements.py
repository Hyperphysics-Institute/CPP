#!/usr/bin/env python3
"""3034_dkappa_contraction_measurements.py — D-KAPPA (CONV-013 Q1(iii))
INTERIM instrument: the [COP] route-(b) spectral-radius test executed on
the COMMITTED leg dynamics, with the corrected contraction objects
measured after the v1 finding.

V1 DISCLOSURE (nothing buried): the first frozen design (preserved in the
Patch 3034 record, §2) ran the spectral-radius power iteration in the
POINT-STATE metric (Euclidean over per-CP positions) and MEASURED
amplification: per-block ratios ~4.5e6 over 16 Moments, i.e. a
per-Moment micro-Lyapunov factor ~2.6 > 1. That is a genuine property of
the committed primitive (step = min(|net|/abs,1)*PSR*unit(net):
unit(net) is hypersensitive at near-cancellation CPs). CONSEQUENCE: the
panel's "is kappa < 1 smuggled?" probe was well-aimed — L-6's proof step
(ii) as worded (the per-Moment map "contracts the existing deviation")
is FALSE in the point-state metric, and any Jacobian spectral radius in
a point-state metric returns rho > 1. This script therefore measures the
CORRECTED objects and reports the micro finding as a finding.

MEASUREMENTS (frozen design v2; SEED_GEN below; x_half=8, beta=0 legs —
the static anchored fixed point, the cleanest instance):
  M1  Micro-Lyapunov (the route-(b) number, honest): one 16-Moment
      finite-difference twin block from the settled state, DELTA0=1e-6;
      reported as rho_micro per Moment. EXPECTED > 1; reported, not
      pass/failed against a wish.
  M2  Attractor confinement (the bounded-neighborhood object): finite
      perturbations d0 in {1e-2, 1e-3}; the state deviation must
      SATURATE at a d0-INDEPENDENT micro-mixing scale (ratio of the two
      late-time saturation levels within [0.67, 1.5]) — the neighborhood
      is a realization CLASS of finite micro-width (~ the step scale),
      not a point.
  M3  Response decorrelation (the load-bearing object — the source-felt
      force is what the B-1 operator construction consumes): the
      late-window triangle
        f_base = RMS |F_src| of one realization (beta=0: pure floor),
        f_seed = RMS |dF_src| between two INDEPENDENT realizations
                 (expected ~ sqrt(2)*f_base, quadrature),
        f_twin = RMS |dF_src| between base and its finite-perturbation
                 twin, late window.
      NO SYSTEMATIC MEMORY above floor <=> f_twin / f_seed in
      [0.3, 1.5]: the perturbed system has become an independent
      realization; the perturbation's trace has fully decorrelated.
  C1  CONTROL (memory reachable; design v2.1 — the v2 design and its
      failure are disclosed in the Patch 3034 record §4): frozen Sea
      (PSR -> 0, relaxation off). The perturbation then persists as a
      static offset. FINDING that forced the redesign: the persistent
      imprint's MAGNITUDE is tiny (the direct linear field of a static
      micro-offset, ~3e-4 per unit perturbation), 10^4 x SMALLER than
      the mobile twin's realization-noise dF — so the v2 check
      (persistence >= 3x mobile magnitude) tested the wrong signature.
      The honest discriminator is CHARACTER, not magnitude:
        (i)  persistence: frozen late dF shows no decay (late/onset
             ratio in [0.5, 2]) — the memory never leaves;
        (ii) constancy vs noise: frozen late dF is CONSTANT
             (coefficient of variation < 0.2) while mobile late dF is
             noise-like (CoV > 0.4) — a persistent systematic imprint
             and realization noise are distinguishable IN this
             instrument;
        (iii) linearity: frozen late dF scales ~linearly with d0
             (ratio for d0 10x apart in [5, 20]) — it is the direct
             imprint, not an artifact floor.
      Additionally kappa_state,frozen = 1 EXACTLY by construction
      (positions never move) — the no-relaxation limit realizes
      kappa = 1, so the state-metric instrument has the failure point
      in range.

WHAT THIS DOES AND DOES NOT DISCHARGE: it discharges the route-(b)
measurement obligation and pins WHERE the contraction lives
(realization-class confinement + response decorrelation, both measured
with controls). It does NOT mint the final kappa <= 1-delta margin for
the SYSTEMATIC (ensemble-mean) channel: that channel's long-time decay
is literally the MEAS-3 preregistered question (OPEN-KMEM-TAIL-1; the
registered cross-falsifier already states "a measured tail kills L-4 and
L-6 together"). The final margin therefore attaches to the MEAS-3
disposition; an L-6 metric amendment candidate rides to the panel in the
same round. No value of xi_2, zeta, eta, d_DP, n_DP, or N is computed.

KEY (KEY-DESIGN RULE clause (c)): KEY-L = the full-precision state
deviation of the d0=1e-3 leg at Moment index 25 of the post-perturbation
window (an interior instrument value, unprinted; stdout rounds all
deviations to 3 significant figures; not theoretically anticipated).
"""
import os, time, copy, importlib.util
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(
    HERE, '../../../../flagship_papers/electromagnetism/code/'
          '2902_mobile_sea_engine.py'))
spec = importlib.util.spec_from_file_location('eng', SRC)
eng = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eng)

SEED_GEN = 30340808
SP, RHO, X0, XH = 2.5, (1.0, 8.0), -10.8, 8.0
SETTLE, WIN = 48, 40
LATE = slice(20, 40)          # late window inside the 40-Moment run
D0S = (1e-2, 1e-3)
rng_master = np.random.default_rng(SEED_GEN)
SEED_A, SEED_B, SEED_PROBE = (int(x) for x in
                              rng_master.integers(10**6, 10**7, size=3))

def build(seed):
    kx = int(np.floor(XH / SP)); xs = SP * np.arange(-kx, kx + 1)
    ky = int(np.floor(RHO[1] / SP)); ys = SP * np.arange(-ky, ky + 1)
    r = np.random.default_rng(seed); C, O, S = [], [], []
    for x in xs:
        for y in ys:
            for z in ys:
                rho = np.hypot(y, z)
                if RHO[0] <= rho <= RHO[1]:
                    C.append((x, y, z)); O.append((0.0, y/rho, z/rho))
                    S.append(eng.D0 + r.uniform(-0.05, 0.05))
    C = np.array(C); O = np.array(O); S = np.array(S)[:, None]
    pos = np.concatenate([C + 0.5*S*O, C - 0.5*S*O])
    q = np.concatenate([np.ones(len(C)), -np.ones(len(C))])
    return pos, q

class Sys:
    def __init__(self, seed, T, psr_scale=1.0):
        sea, qs = build(seed)
        self.pos = np.concatenate([[[X0, 0.0, 0.0]], sea])
        self.q = np.concatenate([[1.0], qs])
        self.Tm = np.sqrt((2*XH + 20)**2 + (2*RHO[1])**2) + 5
        self.hist = eng.History(self.pos, 0.0,
                                int(np.ceil(self.Tm)) + 2, T)
        self.t, self.tr, self.psr = 0, None, psr_scale
    def step(self):
        p0 = eng.PSR
        try:
            eng.PSR = p0 * self.psr
            self.pos, sn, sa, self.tr = eng.moment_step(
                self.pos, self.q, self.hist, self.t, self.Tm, 0.0,
                mobile_sea=True, tr_guess=self.tr)
        finally:
            eng.PSR = p0
        self.hist.append(self.pos); self.t += 1
        return sn

def settled(seed, extra, psr_scale=1.0):
    S = Sys(seed, SETTLE + extra + 2, psr_scale)
    if psr_scale == 0.0:
        # frozen Sea: positions never move; the settle's only effect is
        # populating the history with the (static) configuration — no
        # field evaluation is needed. Measurement-identical, free.
        for _ in range(SETTLE):
            S.hist.append(S.pos); S.t += 1
        return S
    for _ in range(SETTLE):
        S.step()
    return S

def branch(base):
    tw = copy.copy(base)
    tw.pos = base.pos.copy(); tw.hist = copy.deepcopy(base.hist)
    tw.tr = None
    return tw

def perturb(S, d0):
    pr = np.random.default_rng(SEED_PROBE).normal(size=S.pos[1:].shape)
    pr *= d0 / np.linalg.norm(pr)
    S.pos = S.pos.copy(); S.pos[1:] += pr

def run_pair(base, twin, n):
    dS, dF = [], []
    for _ in range(n):
        fb = base.step(); ft = twin.step()
        dS.append(float(np.linalg.norm(twin.pos[1:] - base.pos[1:])))
        dF.append(float(np.linalg.norm(ft - fb)))
    return np.array(dS), np.array(dF)

def run_pair_capture(base, twin, n):
    dS, dF, FA = [], [], []
    for _ in range(n):
        fb = base.step(); ft = twin.step()
        FA.append(fb.copy())
        dS.append(float(np.linalg.norm(twin.pos[1:] - base.pos[1:])))
        dF.append(float(np.linalg.norm(ft - fb)))
    return np.array(dS), np.array(dF), np.array(FA)

def main():
    t0 = time.time()
    print("D-KAPPA contraction measurements v2 "
          f"(SEED_GEN={SEED_GEN}; SETTLE={SETTLE}; WIN={WIN}; x_half={XH})")

    # ---- shared settle for all seed-A mobile measurements --------------
    ROOT_A = settled(SEED_A, max(16, WIN))
    # ---- M1: micro-Lyapunov, one 16-Moment block, DELTA0=1e-6 ----------
    b = branch(ROOT_A); tw = branch(b); perturb(tw, 1e-6)
    din = np.linalg.norm(tw.pos[1:] - b.pos[1:])
    for _ in range(16):
        b.step(); tw.step()
    dout = np.linalg.norm(tw.pos[1:] - b.pos[1:])
    rho_micro = (dout / din) ** (1/16)
    print(f"M1 micro-Lyapunov: block ratio {dout/din:.3g} over 16 Moments"
          f" -> rho_micro = {rho_micro:.3f} per Moment (point-state"
          f" metric; the v1 finding, reproduced)")

    # ---- M2 + M3(twin): finite perturbations ---------------------------
    sat, key_slot = {}, []
    twin_late = None
    FA_from_M2 = None
    for d0 in D0S:
        b = branch(ROOT_A); tw = branch(b); perturb(tw, d0)
        dS, dF, FAcap = run_pair_capture(b, tw, WIN)
        if d0 == 1e-3:
            FA_from_M2 = FAcap
        sat[d0] = dS[LATE].mean()
        if d0 == 1e-3:
            key_slot.append(dS[25])              # KEY-L, unprinted
            twin_late = np.sqrt((dF[LATE]**2).mean())
            twin_dF_late = dF[LATE]
        print(f"M2 d0={d0:g}: |dState| t+1/10/20/40 = "
              f"{dS[0]:.3g} {dS[9]:.3g} {dS[19]:.3g} {dS[39]:.3g}"
              f"  late-mean {sat[d0]:.3g}")
    sat_ratio = sat[D0S[0]] / sat[D0S[1]]

    # ---- M3: the floor triangle ---------------------------------------
    # FA = the unperturbed seed-A trajectory captured during M2 (the
    # d0=1e-3 base leg): identical by determinism to a fresh run.
    FA = FA_from_M2
    bB = settled(SEED_B, WIN)
    FB = []
    for _ in range(WIN):
        FB.append(bB.step())
    FB = np.array(FB)
    f_base = float(np.sqrt((FA[LATE]**2).sum(1)).mean())
    f_seed = float(np.sqrt(((FA[LATE]-FB[LATE])**2).sum(1)).mean())
    f_twin = float(twin_late)
    print(f"M3 floor triangle (late window): f_base={f_base:.4g}  "
          f"f_seed={f_seed:.4g} (quadrature exp ~{np.sqrt(2)*f_base:.4g})"
          f"  f_twin={f_twin:.4g}  f_twin/f_seed={f_twin/f_seed:.3f}")

    # ---- C1: frozen-Sea memory control (v2.1 design) -------------------
    fz = {}
    for d0 in (1e-3, 1e-2):
        b = settled(SEED_A, WIN, psr_scale=0.0)
        tw = branch(b); perturb(tw, d0)
        _, dFz = run_pair(b, tw, WIN)
        fz[d0] = dFz
    z = fz[1e-3]
    fz_late = z[LATE]
    persist = float(fz_late.mean() / max(z[9], 1e-30))     # late vs onset
    cov_frozen = float(fz_late.std() / fz_late.mean())
    cov_mobile = float(twin_dF_late.std() / twin_dF_late.mean())
    lin_ratio = float(fz[1e-2][LATE].mean() / fz[1e-3][LATE].mean())
    print(f"C1 frozen-Sea: late mean dF={fz_late.mean():.4g}  "
          f"persist(late/onset)={persist:.3f}  CoV_frozen={cov_frozen:.3f}"
          f"  CoV_mobile={cov_mobile:.3f}  linearity(10x d0)="
          f"{lin_ratio:.2f}x")

    # ---- verdicts ------------------------------------------------------
    checks = [
        ("M1 rho_micro > 1 REPORTED (point-state metric amplifies; the "
         "v1 finding stands)", rho_micro > 1.0),
        ("M2 saturation d0-independent (ratio in [0.67,1.5]): bounded "
         "realization-class neighborhood", 0.67 <= sat_ratio <= 1.5),
        ("M3 quadrature sanity: f_seed within 25% of sqrt(2)*f_base",
         abs(f_seed - np.sqrt(2)*f_base) <= 0.25*np.sqrt(2)*f_base),
        ("M3 no systematic memory above floor: f_twin/f_seed in "
         "[0.3,1.5]", 0.3 <= f_twin/f_seed <= 1.5),
        ("C1(i) frozen memory persists: late/onset in [0.5,2]",
         0.5 <= persist <= 2.0),
        ("C1(ii) character discriminator: CoV_frozen < 0.2 < 0.4 < "
         "CoV_mobile", cov_frozen < 0.2 and cov_mobile > 0.4),
        ("C1(iii) frozen imprint linear in d0: 10x d0 -> [5,20]x dF",
         5.0 <= lin_ratio <= 20.0),
    ]
    n = 0
    for name, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        n += ok
    print(f"{n}/{len(checks)} PASS   wall = {time.time()-t0:.0f}s")
    assert len(key_slot) == 1   # KEY-L retained unprinted

if __name__ == '__main__':
    main()
