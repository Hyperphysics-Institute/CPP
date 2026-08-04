#!/usr/bin/env python3
"""Patch 2990 — B-1 v1.2 Lemma L-6 (C-5(iii) stationarity-regime) toy checks.

Toy model of the deviation-from-instantaneous-fixed-point recursion that
L-6's proof establishes at mechanism level:

    d_{n+1} = kappa * d_n + C * |v_{n+1} - v_n|          (contraction)

with kappa < 1 supplied structurally by M1 (unanchored content exits the
co-moving neighborhood within tau_b = d_DP/c; no return, no back-scatter),
plus a mildly nonlinear Moment-stepped state toy to check that the
linear-response prediction's residual scales O(v^2) uniformly along
admissible (slow, bounded) drives.

CHECKS (toy units; nothing minted):
  1  Uniform bound: sup_n d_n <= d_0*kappa^n + C*sup|Dv|/(1-kappa) across
     random admissible drives (bound holds with margin, machine-verified).
  2  Linearity scaling: halving drive amplitude quarters the nonlinear
     residual (exponent fit ~2) uniformly along the trajectory -- the
     construction STAYS in the linear-response regime, not just starts there.
  3  NEGATIVE CONTROL (no attraction): kappa -> 1 (a long-time memory tail,
     exactly what a MEAS-2 tail detection would mean) breaks the uniform
     bound -- deviation accumulates secularly. The lemma CAN fail.
  4  NEGATIVE CONTROL (inadmissible drive): a fast drive violating the
     slow-variation condition exceeds the admissible-class bound,
     demonstrating the admissibility condition is load-bearing, not
     decorative.
"""
import numpy as np

rng = np.random.default_rng(29900804)
PASS = []


def contraction_run(kappa, C, dv_seq, d0=0.0):
    d = d0
    trace = []
    for dv in dv_seq:
        d = kappa * d + C * abs(dv)
        trace.append(d)
    return np.array(trace)


# ---- CHECK 1: uniform bound over random admissible drives ----
kappa, C = 0.55, 1.0          # toy attraction rate (tau_b a few Moments)
dv_max = 1e-3                 # slow-variation bound (admissible class)
ok = True
for trial in range(200):
    N = 4000
    dv = rng.uniform(-dv_max, dv_max, N)
    tr = contraction_run(kappa, C, dv)
    bound = C * dv_max / (1.0 - kappa)
    if tr.max() > bound * (1 + 1e-12):
        ok = False
        break
PASS.append(("1 uniform bound (200 random admissible drives)", ok))

# ---- CHECK 2: linearity residual scales O(v^2) along the trajectory ----
def nonlinear_toy(v_seq, eps):
    """Moment-stepped state with finite-memory linear part + quadratic term."""
    K = 6
    g = np.array([0.9, -0.5, -0.25, -0.1, -0.04, -0.01])  # sums to 0 (DC zero)
    g = g - g.mean()                                       # enforce sum=0 exactly
    s_hist = np.zeros(K)
    out = []
    for v in v_seq:
        lin = np.dot(g, s_hist)
        state = v * eps
        s_hist = np.roll(s_hist, 1); s_hist[0] = state + 0.05 * state**2
        out.append(lin)
    return np.array(out)

N = 2000
t = np.arange(N)
v_base = np.sin(2 * np.pi * t / 800.0)          # slow drive, omega << Nyquist
r = []
for eps in (1e-2, 5e-3):
    full = nonlinear_toy(v_base, eps)
    linear_pred = nonlinear_toy(v_base, 1e-6) * (eps / 1e-6)   # linear ref scaled
    r.append(np.abs(full - linear_pred).max())
exponent = np.log(r[0] / r[1]) / np.log(2.0)
PASS.append(("2 linearity residual O(v^2) (exponent %.3f in [1.8,2.2])" % exponent,
             1.8 < exponent < 2.2))

# ---- CHECK 3: negative control -- no attraction (memory tail) ----
tr_tail = contraction_run(1.0, C, rng.uniform(-dv_max, dv_max, 4000))
bound = C * dv_max / (1.0 - kappa)
PASS.append(("3 NEG CONTROL kappa=1 secular growth breaks bound",
             tr_tail.max() > 10 * bound))

# ---- CHECK 4: negative control -- inadmissible (fast) drive ----
dv_fast = rng.uniform(-50 * dv_max, 50 * dv_max, 4000)
tr_fast = contraction_run(kappa, C, dv_fast)
PASS.append(("4 NEG CONTROL fast drive exceeds admissible-class bound",
             tr_fast.max() > 5 * bound))

n_ok = sum(p for _, p in PASS)
for name, p in PASS:
    print(("PASS " if p else "FAIL ") + name)
print(f"{n_ok}/{len(PASS)} PASS")
raise SystemExit(0 if n_ok == len(PASS) else 1)
