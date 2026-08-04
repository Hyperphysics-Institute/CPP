#!/usr/bin/env python3
"""2976_t2_parity_sweep.py — T-2 v1.1 verifies: Lemma T-2.P (parity/sense degeneracy),
the declared dE = v.dp definitional-with-consistency route, and the M-vs-anchored-content
sweep (Copilot 2974). Toy units only; no physical value of any open quantity is minted;
the proportionality coefficient is deliberately not minted (slope is TOY-SPECIFIC).
"""

import numpy as np

PASS = 0; FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    tag = "PASS" if cond else "FAIL"
    PASS += cond; FAIL += (not cond)
    print(f"[{tag}] {name}" + (f"  ({detail})" if detail else ""))

rng = np.random.default_rng(2976)

# ---------------------------------------------------------------- stencil + parity
phi = (1 + np.sqrt(5)) / 2
verts = []
for s1 in (+1, -1):
    for s2 in (+1, -1):
        base = np.array([0.0, s1*1.0, s2*phi])
        for k in range(3):
            verts.append(np.roll(base, k))
verts = np.array(verts); verts /= np.linalg.norm(verts, axis=1, keepdims=True)

# CHECK 1 — inversion is in the stencil symmetry: the 12-direction set is centrally
# symmetric (every direction's antipode is present) — the group-theoretic fact
# (I_h = I x {+-1}) at stencil level.
antipodal = all(np.min(np.linalg.norm(verts + v, axis=1)) < 1e-12 for v in verts)
check("CHECK 1  central symmetry: the 12-direction stencil contains every antipode",
      antipodal)

# ---------------------------------------------------------------- toy energy functional
def energy(config_pos, config_sense, v):
    """I_h-invariant toy stored-energy functional of a configuration:
    positions (N,3), per-element arc senses (N,3) as PSEUDOVECTORS, and composite
    velocity v (3,). Built ONLY from even contractions in the pseudovectors and
    rotation/inversion-invariant scalars — the G1 class. Anharmonic on purpose."""
    r2 = np.einsum('ij,ij->i', config_pos, config_pos)
    s2 = np.einsum('ij,ij->i', config_sense, config_sense)
    rs = np.einsum('ij,ij->i', config_pos, config_sense)   # vector.pseudovector: P-ODD (pos flips, sense does not)
    v2 = v @ v
    # rs is P-odd; admissible functional uses rs ONLY in even powers:
    return np.sum(0.5*r2 + 0.4*s2 + 0.15*rs**2 + 0.05*r2**2) + 0.5*np.sum(s2)*v2

def parity(config_pos, config_sense, v):
    """Sea parity (the inversion element): positions -> -positions, velocity ->
    -velocity (true vectors); senses UNCHANGED -- a rotation sense is a
    PSEUDOVECTOR, inversion-EVEN. (First run wrongly flipped the senses; the
    negative control refused to fire and exposed the error -- the toy corrected
    the worker on the transformation law itself; see reasoning/2976.md.)"""
    return -config_pos, config_sense, -v

# CHECK 2 — Lemma T-2.P: E invariant under the FULL parity map incl. sense reversal,
# across random configurations.
max_dev = 0.0
for _ in range(500):
    N = int(rng.integers(3, 40))
    pos = rng.normal(size=(N, 3)); sen = rng.normal(size=(N, 3))
    v = rng.normal(size=3)
    E1 = energy(pos, sen, v)
    E2 = energy(*parity(pos, sen, v))
    max_dev = max(max_dev, abs(E2 - E1) / max(1.0, abs(E1)))
check("CHECK 2  Lemma T-2.P: E(P.config) = E(config) under the inversion map (500 random configs)",
      max_dev < 1e-14, f"max rel dev = {max_dev:.1e}")

# CHECK 3 — hence E(v) = E(-v): direct check on the velocity slot with fixed config.
pos = rng.normal(size=(12, 3)); sen = rng.normal(size=(12, 3))
devs = [abs(energy(pos, sen, v) - energy(*parity(pos, sen, v)))
        for v in rng.normal(size=(50, 3))]
check("CHECK 3  E(v) = E(-v) on the mapped state pair (50 velocities)",
      max(devs) < 1e-10, f"max dev = {max(devs):.1e}")

# CHECK 4 — the Remark's failure mode is REAL: adding a chiral (P-odd) term breaks
# the degeneracy (negative control: the lemma's premise does work).
def energy_chiral(pos, sen, v):
    rs = np.einsum('ij,ij->i', pos, sen)
    return energy(pos, sen, v) + 0.1*np.sum(rs)   # rs to the FIRST power: P-odd
E1 = energy_chiral(pos, sen, np.array([0.3, 0, 0]))
E2 = energy_chiral(*parity(pos, sen, np.array([0.3, 0, 0])))
check("CHECK 4  NEGATIVE CONTROL: a P-odd (chiral) term breaks the degeneracy",
      abs(E2 - E1) > 1e-3, f"|dE| = {abs(E2-E1):.2e}")

# ---------------------------------------------------------------- dE = v.dp route
# Toy composite: E(v) = E0 + 0.5*M*v^2 with M from an anchored-content model
# M(N_a) = m1 * N_a (per-DP additivity toy). Book momentum p defined as cumulative
# external impulse from v=0 (definitional route); consistency: along an adiabatic
# ramp, dE and v*dp must agree pointwise with the SAME M.
m1_toy = 0.7

def ramp_consistency(N_a, steps=4001, v_max=0.5):
    M = m1_toy * N_a
    v = np.linspace(0.0, v_max, steps)
    E = 0.5 * M * v**2
    p = M * v                      # book momentum: cumulative external impulse
    dE = np.diff(E)
    vdp = 0.5*(v[1:] + v[:-1]) * np.diff(p)   # midpoint v against dp
    return np.max(np.abs(dE - vdp)) / np.max(np.abs(dE))

# CHECK 5 — dE = v.dp holds identically along the ramp (definitional consistency)
r = ramp_consistency(N_a=8)
check("CHECK 5  dE = v.dp identity along the adiabatic ramp (midpoint rule, rel)",
      r < 1e-10, f"max rel dev = {r:.1e}")

# CHECK 6 — the SAME M appears in both books: extract M from E-curvature and from
# p-slope independently; they must agree.
N_a = 8; M_true = m1_toy * N_a
v = np.linspace(-0.4, 0.4, 2001)
E = 0.5 * M_true * v**2 + 0.03 * v**4          # quartic contamination allowed
M_from_E = np.polyfit(v, E, 4)[2] * 2.0        # curvature at 0
p = M_true * v
M_from_p = np.polyfit(v, p, 1)[0]
check("CHECK 6  same M from E-curvature and from p-slope",
      abs(M_from_E - M_from_p) < 1e-8 * M_true,
      f"M_E = {M_from_E:.10f}, M_p = {M_from_p:.10f}")

# ---------------------------------------------------------------- M vs anchored content
# Copilot 2974: sweep M against N_a with uncertainties; linear fit through origin.
N_as = np.array([3, 5, 8, 12, 18, 27, 40])
M_est = []; M_err = []
for N_a in N_as:
    # per-run noisy curvature extraction; bootstrap over noisy replicas
    reps = []
    for _ in range(200):
        vv = np.linspace(-0.3, 0.3, 401)
        EE = 0.5 * m1_toy * N_a * vv**2 + 0.02 * vv**4
        EE_noisy = EE + rng.normal(scale=2e-5 * (1 + 0.1*N_a), size=vv.shape)  # heteroskedastic
        reps.append(np.polyfit(vv, EE_noisy, 4)[2] * 2.0)
    reps = np.array(reps)
    M_est.append(reps.mean()); M_err.append(reps.std(ddof=1))
M_est = np.array(M_est); M_err = np.array(M_err)

# weighted least squares through origin: M = slope * N_a
w = 1.0 / M_err**2
slope = np.sum(w * N_as * M_est) / np.sum(w * N_as**2)
resid = M_est - slope * N_as
chi2 = np.sum(w * resid**2); dof = len(N_as) - 1
ss_tot = np.sum(w * (M_est - np.average(M_est, weights=w))**2)
R2 = 1.0 - chi2 / ss_tot

check("CHECK 7  M vs anchored content: weighted through-origin fit, slope recovered",
      abs(slope - m1_toy) < 3 * np.sqrt(1.0/np.sum(w*N_as**2)) + 1e-3,
      f"slope = {slope:.6f} (toy m1 = {m1_toy}), chi2/dof = {chi2/dof:.2f}")
check("CHECK 8  proportionality quality: R^2 within 1e-3 of unity; residuals within errors",
      R2 > 0.999 and np.all(np.abs(resid) < 4*M_err),
      f"R^2 = {R2:.6f}, max |resid|/err = {np.max(np.abs(resid)/M_err):.2f}")

# CHECK 9 — intercept consistency with zero: free-intercept fit's intercept ~ 0
A = np.vstack([N_as, np.ones_like(N_as)]).T
coef, *_ = np.linalg.lstsq(A * np.sqrt(w)[:, None], M_est * np.sqrt(w), rcond=None)
b = coef[1]
b_err = np.sqrt(np.linalg.inv((A * w[:, None]).T @ A)[1, 1])
check("CHECK 9  free-intercept audit: intercept consistent with zero",
      abs(b) < 3 * b_err, f"b = {b:.2e} +- {b_err:.2e}")

print("-" * 72)
print(f"{PASS}/{PASS+FAIL} PASS")
print("Lemma T-2.P content: inversion in I_h + the G1 class excludes P-odd terms;")
print("senses are inversion-EVEN pseudovectors; chiral negative control included.")
print("The dE = v.dp route is the DECLARED definitional-with-consistency route;")
print("the proportionality coefficient is deliberately not minted. No open-quantity")
print("value is computed. Toy units only.")
