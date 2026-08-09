#!/usr/bin/env python3
"""3034_dkappa_spectral_radius.py — D-KAPPA (CONV-013 Q1(iii) deliverable):
seeded deterministic Jacobian spectral-radius test on the COMMITTED leg
dynamics, with the SF-6 linear-sensitivity uniform-boundedness diagnostic.

WHAT THIS MEASURES (the [COP] route-(b) specification, verbatim basis
`reviews/conv013_returns/copilot_return.md`): "a seeded deterministic test
returning the Jacobian spectral radius for representative legs with a
uniform-boundedness (SF-6 linear-sensitivity) diagnostic."

THE MAP, THE METRIC, THE MARGIN (the route-(a) naming, supplied alongside):
  - Map: T_v^B = the B-Moment composition of the committed per-Moment update
    (2902 eng.moment_step, the SAME engine the MEAS-2 evidentiary legs ran),
    linearized at the co-moving trajectory S(v) — acting on the FULL delay
    state (positions + retarded history window; the twin-propagation below
    perturbs the state and lets the perturbation populate its own history,
    so the measured object is the delay-map spectral radius, not a
    frozen-history surrogate).
  - Metric: d(X, X') = ||pos - pos'||_2 over all Sea CPs (the source is
    prescribed identically in both twins, so the deviation is purely the
    Sea's response — the exact object of L-6's recursion).
  - Margin: kappa_M = rho(D T_v)^(1/M) estimated matrix-free by seeded
    power iteration (finite-difference twin propagation with per-block
    renormalization; repeated application converges to the dominant
    eigenvalue magnitude of the block map). delta = 1 - kappa_M is the
    measured margin. NOTHING IS ASSUMED: unlike the 2990 toy (kappa an
    input), here kappa is an OUTPUT of the committed dynamics.

FROZEN DESIGN (fixed before any evidentiary run; 2968 disclosure precedent):
  BLOCK = 16 Moments; N_ITER = 5 power blocks (ratios reported per block;
  the LAST-BLOCK ratio is the converged estimate); SETTLE = 48 Moments;
  DELTA0 = 1e-6 (perturbation seeded on all Sea CPs, isotropic Gaussian,
  renormalized to DELTA0); measurement window keeps the source inside the
  Sea for every leg. Representative legs (seeds from default_rng(30340808)):
    L1  x_half=8,  beta=0.00  (static anchored fixed point)
    L2  x_half=8,  beta=0.10  (co-moving, the MEAS-2 step value)
    L3  x_half=8,  beta=0.10, second seed (jitter-realization robustness)
    L4  x_half=16, beta=0.10  (the STANDARD MEAS-2 evidentiary geometry)
  CONTROLS (reachable failure, house rule):
    C1  frozen Sea (relaxation off): measured ratio must be ~1.0 exactly —
        the instrument CAN return no-contraction; kappa<1, when found, is
        physics, not artifact.
    C2  step-scaled Sea (PSR x 0.1): kappa must move TOWARD 1 — the
        measured rate tracks the physical relaxation strength.
  SF-6 DIAGNOSTIC: settle at beta in {0.000,0.025,0.050,0.075,0.100}
  (x_half=8, common seed, T=SETTLE), shift-compensate each configuration
  by its source displacement, and report the adjacent-pair sensitivity
  C_i = ||shift-compensated dS||/dbeta. UNIFORM BOUNDEDNESS = the C_i are
  mutually consistent (max/min < 2) across the range — the L-6 step-(i)
  ingredient dist(S(v),S(v')) <= C|v-v'| with one C for the whole class.

KEY (KEY-DESIGN RULE, amended clause (c) — no theoretically anticipated
values): KEY-K = the full-precision deviation norm of leg L2 at power-block
boundary 2 BEFORE renormalization, an interior instrument value computed
nowhere else and NOT printed (stdout shows only 6-sig-fig block ratios;
the norm depends on the seeded probe direction and is not reconstructible
from the printed ratios, which are norm QUOTIENTS).

No value of any DM observable (xi_2, zeta, eta, d_DP, n_DP, N) is computed
or consumed. Attaches to OPEN-K1-MEMORY-1 per the adjudication (no new
OPEN ID). A measured kappa >= 1 on any committed leg would REFUSE the
deliverable and be reported as such (this script can fail).
"""
import os, sys, time, importlib.util
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(
    HERE, '../../../../flagship_papers/electromagnetism/code/'
          '2902_mobile_sea_engine.py'))
spec = importlib.util.spec_from_file_location('eng', SRC)
eng = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eng)

# ---- FROZEN constants ---------------------------------------------------
SEED_GEN = 30340808
BLOCK, N_ITER, SETTLE, DELTA0 = 16, 5, 48, 1e-6
SPACING, RHO, X_SRC0 = 2.5, (1.0, 8.0), -10.8
JIT = (-0.05, 0.05)
BETAS_SF6 = (0.000, 0.025, 0.050, 0.075, 0.100)
rng_master = np.random.default_rng(SEED_GEN)
SEED_A, SEED_B, SEED_PROBE = rng_master.integers(10**6, 10**7, size=3)

def build(seed, x_half):
    kx = int(np.floor(x_half / SPACING)); xs = SPACING * np.arange(-kx, kx + 1)
    ky = int(np.floor(RHO[1] / SPACING)); ys = SPACING * np.arange(-ky, ky + 1)
    r = np.random.default_rng(seed); C, O, S = [], [], []
    for x in xs:
        for y in ys:
            for z in ys:
                rho = np.hypot(y, z)
                if RHO[0] <= rho <= RHO[1]:
                    C.append((x, y, z)); O.append((0.0, y/rho, z/rho))
                    S.append(eng.D0 + r.uniform(*JIT))
    C = np.array(C); O = np.array(O); S = np.array(S)[:, None]
    pos = np.concatenate([C + 0.5*S*O, C - 0.5*S*O])
    q = np.concatenate([np.ones(len(C)), -np.ones(len(C))])
    return pos, q

class Leg:
    """One evolving copy of the committed dynamics (positions + history)."""
    def __init__(self, seed, x_half, beta, T_total, psr_scale=1.0,
                 frozen=False):
        sea, qs = build(seed, x_half)
        self.pos = np.concatenate([[[X_SRC0, 0.0, 0.0]], sea])
        self.q = np.concatenate([[1.0], qs])
        self.beta, self.frozen, self.psr_scale = beta, frozen, psr_scale
        self.T_max = np.sqrt((2*x_half + 20)**2 + (2*RHO[1])**2) + 5
        self.hist = eng.History(self.pos, 0.0,
                                int(np.ceil(self.T_max)) + 2, T_total)
        self.t, self.tr = 0, None
    def step(self):
        psr0 = eng.PSR
        try:
            if self.frozen or self.psr_scale != 1.0:
                eng.PSR = 0.0 if self.frozen else psr0 * self.psr_scale
            self.pos, sn, sa, self.tr = eng.moment_step(
                self.pos, self.q, self.hist, self.t, self.T_max,
                self.beta, mobile_sea=True, tr_guess=self.tr)
        finally:
            eng.PSR = psr0
        self.hist.append(self.pos); self.t += 1

def dev(a, b):
    return float(np.linalg.norm(a.pos[1:] - b.pos[1:]))

def spectral_radius(seed, x_half, beta, tag, psr_scale=1.0, frozen=False,
                    key_slot=None):
    T_total = SETTLE + BLOCK * N_ITER + 2
    base = Leg(seed, x_half, beta, T_total, psr_scale, frozen)
    for _ in range(SETTLE):
        base.step()
    twin = Leg(seed, x_half, beta, T_total, psr_scale, frozen)
    twin.pos = base.pos.copy(); twin.hist = base.hist  # shared past ...
    # ... but twin needs its OWN history forward: rebuild an independent
    # history seeded with the base past (delay state identical at t=SETTLE).
    import copy
    twin.hist = copy.deepcopy(base.hist); twin.t, twin.tr = base.t, None
    probe = np.random.default_rng(SEED_PROBE).normal(
        size=twin.pos[1:].shape)
    probe *= DELTA0 / np.linalg.norm(probe)
    twin.pos = twin.pos.copy(); twin.pos[1:] += probe
    ratios = []
    for it in range(N_ITER):
        d_in = dev(base, twin)
        for _ in range(BLOCK):
            base.step(); twin.step()
        d_out = dev(base, twin)
        if key_slot is not None and it == 1:
            key_slot.append(d_out)            # KEY-K: unprinted
        ratios.append(d_out / d_in)
        # renormalize twin deviation to DELTA0 along current direction
        delta = twin.pos[1:] - base.pos[1:]
        twin.pos = base.pos.copy()
        twin.pos[1:] += delta * (DELTA0 / np.linalg.norm(delta))
        # re-sync twin history to base (linearized power step: history of
        # the renormalized perturbation is regenerated next block)
        twin.hist = copy.deepcopy(base.hist); twin.tr = None
    r_last = ratios[-1]
    kappa = r_last ** (1.0 / BLOCK)
    print(f"  {tag}: block ratios " +
          " ".join(f"{r:.6g}" for r in ratios) +
          f"  -> kappa/Moment = {kappa:.6f}  (delta = {1-kappa:.6f})")
    return kappa

def sf6_diagnostic():
    print("SF-6 linear-sensitivity uniform-boundedness diagnostic "
          f"(x_half=8, seed A, T={SETTLE}):")
    configs = []
    for b in BETAS_SF6:
        L = Leg(int(SEED_A), 8.0, b, SETTLE + 2)
        for _ in range(SETTLE):
            L.step()
        # shift-compensate by the source displacement (co-moving frame)
        shift = L.pos[0] - np.array([X_SRC0, 0.0, 0.0])
        configs.append(L.pos[1:] - shift[None, :])
    Cs = []
    for i in range(len(BETAS_SF6) - 1):
        dS = np.linalg.norm(configs[i+1] - configs[i])
        db = BETAS_SF6[i+1] - BETAS_SF6[i]
        Cs.append(dS / db)
        print(f"  C[{BETAS_SF6[i]:.3f}->{BETAS_SF6[i+1]:.3f}] = {dS/db:.4f}")
    spread = max(Cs) / min(Cs)
    ok = spread < 2.0
    print(f"  uniform-boundedness: max/min = {spread:.3f}  "
          f"[{'PASS' if ok else 'FAIL'} < 2.0]")
    return ok

def main():
    t0 = time.time()
    print("D-KAPPA seeded Jacobian spectral-radius test "
          f"(SEED_GEN={SEED_GEN}; BLOCK={BLOCK}; N_ITER={N_ITER}; "
          f"SETTLE={SETTLE}; DELTA0={DELTA0})")
    key_slot = []
    print("Representative legs (committed dynamics):")
    k1 = spectral_radius(int(SEED_A), 8.0, 0.00, "L1 x8  beta=0.00 seedA")
    k2 = spectral_radius(int(SEED_A), 8.0, 0.10, "L2 x8  beta=0.10 seedA",
                         key_slot=key_slot)
    k3 = spectral_radius(int(SEED_B), 8.0, 0.10, "L3 x8  beta=0.10 seedB")
    k4 = spectral_radius(int(SEED_A), 16.0, 0.10, "L4 x16 beta=0.10 seedA")
    kappas = [k1, k2, k3, k4]
    print("Controls (reachable failure):")
    c1 = spectral_radius(int(SEED_A), 8.0, 0.10, "C1 frozen Sea      ",
                         frozen=True)
    c2 = spectral_radius(int(SEED_A), 8.0, 0.10, "C2 PSR x 0.1       ",
                         psr_scale=0.1)
    ok_sf6 = sf6_diagnostic()
    print("VERDICT LINES:")
    checks = [
        ("all committed legs kappa < 1 (margin > 0)",
         all(k < 1.0 for k in kappas)),
        ("worst committed margin delta >= 0.01",
         (1.0 - max(kappas)) >= 0.01),
        ("C1 frozen-Sea ratio ~ 1 (|kappa-1| < 0.005): failure reachable",
         abs(c1 - 1.0) < 0.005),
        ("C2 weakened relaxation moves kappa toward 1",
         c2 > max(kappas)),
        ("SF-6 sensitivity uniformly bounded across the beta range",
         ok_sf6),
    ]
    n = 0
    for name, ok in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
        n += ok
    print(f"{n}/{len(checks)} PASS   kappa_max(committed) = "
          f"{max(kappas):.6f}   delta_min = {1-max(kappas):.6f}   "
          f"wall = {time.time()-t0:.0f}s")
    # KEY-K retained in memory only; deliberately not printed.
    assert len(key_slot) == 1

if __name__ == '__main__':
    main()

"""V1 STDOUT (preserved verbatim; the run was stopped after L1 measured amplification — see the Patch 3034 record §2):
D-KAPPA seeded Jacobian spectral-radius test (SEED_GEN=30340808; BLOCK=16; N_ITER=5; SETTLE=48; DELTA0=1e-06)
Representative legs (committed dynamics):
  L1 x8  beta=0.00 seedA: block ratios 4.5556e+06 4.476e+06 4.49727e+06 4.61067e+06 4.01142e+06  -> kappa/Moment = 2.586462  (delta = -1.586462)
"""
