#!/usr/bin/env python3
# verify_3430_varc1_step1.py — numeric verification of VARC-1 Step 1 (Patch 3430)
#
# Framework (frozen at 3429 prereg + founder rulings):
#   - Fixed absolute scaffold; comoving DP-Sea flow v(r,t) = r/t (coasting).
#   - Light propagates at c(t) relative to the LOCAL Sea (lensing-channel ruling).
#   - Founder postulate (3429 §6.1): local physics invariant; atomic clock rate
#     scales EXACTLY with local c  <=>  emitted quantum invariant.
#   - c(t) rises monotonically toward asymptote c0 (fossil depletion, 3421 §1b).
#
# Analytic claims under test:
#   R1:  1 + z = t0/t_e exactly, independent of c(t)   [C2 x C3 cancellation
#        emerging in the full wave-crest calculation]
#   D1:  d_L(z) = (1+z) * t0 * INT_{t_e}^{t0} c(t)/t dt, with t_e = t0/(1+z)
#   S1:  d_L^varc(z) < d_L^const-c0(z) for all z > 0  (sources BRIGHTER at
#        given z: log-time average of c/c0 over the flight is < 1)
#   Q1:  q0_app = t0 * cdot(t0)/c0 = eps >= 0 at low z  (deceleration-mimicking)
#
# Photon ODE (inward): dr/dt = r/t - c(t);  crest interval at emission scaled
# by c0/c(t_e) per the clock postulate.

import numpy as np
from scipy.integrate import quad, solve_ivp

t0, c0 = 1.0, 1.0
P0 = 1e-7  # local atomic period today (absolute units)

def cfun(form, A, lam):
    if form == 'exp':
        return (lambda t: c0*(1.0 - A*np.exp(lam*(1.0 - t/t0))),
                A*lam/(1.0-A))              # eps = t0*c'(t0)/c(t0)
    if form == 'pow':
        return (lambda t: c0*(1.0 - A*(t0/t)**lam),
                A*lam/(1.0-A))
    raise ValueError(form)

def v_s(c, t_e):
    return quad(lambda t: c(t)/t, t_e, t0, limit=200)[0]

def arrival_time(c, t_emit, r_emit):
    # integrate dr/dt = r/t - c(t) until r = 0
    hit = lambda t, r: r[0]
    hit.terminal, hit.direction = True, -1
    sol = solve_ivp(lambda t, r: [r[0]/t - c(t)], (t_emit, 10*t0),
                    [r_emit], events=hit, rtol=1e-11, atol=1e-13, max_step=0.01)
    return sol.t_events[0][0]

def check(form, A, lam, zmax):
    c, eps = cfun(form, A, lam)
    # sanity: c positive over range used
    t_min = t0/(1.0+zmax)
    assert c(t_min) > 0, "c went nonpositive in range"

    # --- R1: crest simulation at a few z ---
    r1_err = 0.0
    for z_t in (0.2, 0.8, zmax):
        t_e = t0/(1.0+z_t)
        vs = v_s(c, t_e)
        # crest 1: by construction arrives at t0 (verify)
        t_a1 = arrival_time(c, t_e, vs*t_e)
        # crest 2: emitted one atomic period later (period stretched by c0/c(t_e))
        P_abs = P0 * c0/c(t_e)
        t_e2 = t_e + P_abs
        t_a2 = arrival_time(c, t_e2, vs*t_e2)
        # spectrograph measures the received period against the observer's
        # LOCAL atomic period K/c(t0), K = P0*c0  (clock rate ~ local c)
        z_num = (t_a2 - t_a1)*c(t0)/(P0*c0) - 1.0
        r1_err = max(r1_err, abs((1.0+z_num)/(t0/t_e) - 1.0),
                     abs(t_a1/t0 - 1.0))
    # --- D1/S1: distance ratio over z grid ---
    zg = np.linspace(0.01, zmax, 120)
    ratio = np.array([v_s(c, t0/(1+z)) / (c(t0)*np.log(1+z)) for z in zg])
    s1_ok = bool(np.all(ratio < 1.0)) and bool(np.all(np.diff(ratio) < 0))
    # --- Q1: fit d_L = alpha z + beta z^2 on low z; q0 = 1 - 2 beta/alpha ---
    zl = np.linspace(0.005, 0.12, 60)
    def q0_of(dl):
        M = np.vstack([zl, zl**2, zl**3]).T
        (al, be, _ga), *_ = np.linalg.lstsq(M, dl, rcond=None)
        return 1.0 - 2.0*be/al
    dl_v = np.array([(1+z)*t0*v_s(c, t0/(1+z)) for z in zl])
    dl_c = np.array([(1+z)*t0*c(t0)*np.log(1+z) for z in zl])
    q0_app, q0_null = q0_of(dl_v), q0_of(dl_c)
    return eps, q0_app, q0_null, r1_err, ratio.min(), ratio.max(), s1_ok

print(f"{'form':5s} {'A':>5s} {'lam':>4s} {'eps=t0 c./c':>12s} {'q0_app(fit)':>12s} "
      f"{'q0 null':>8s} {'R1 max err':>10s} {'min ratio':>9s} {'max ratio':>9s} {'S1(<1,mono)':>11s}")
verdict_ok = True
for form, A, lam, zmax in [('exp', 0.05, 1.0, 2.0), ('exp', 0.10, 1.0, 2.0),
                           ('exp', 0.10, 2.0, 1.5), ('pow', 0.05, 1.0, 2.0),
                           ('pow', 0.10, 1.0, 2.0), ('pow', 0.30, 0.5, 1.0)]:
    eps, q0, q0n, r1e, rmin, rmax, s1 = check(form, A, lam, zmax)
    print(f"{form:5s} {A:5.2f} {lam:4.1f} {eps:12.4f} {q0:12.4f} "
          f"{q0n:8.4f} {r1e:10.2e} {rmin:9.4f} {rmax:9.4f} {str(s1):>11s}")
    verdict_ok &= s1 and (q0 > 0) and (r1e < 1e-4) and (abs(q0n) < 5e-3)
    # small-A agreement of q0 with eps (first-order formula):
    if A <= 0.10:
        verdict_ok &= abs(q0 - eps) < 0.15*eps + 0.005

print()
print("R1 (spectrograph z-map c-independent), S1 (brighter at all z, monotone), "
      "Q1 (q0_app > 0, = eps at small A; null control ~ 0):",
      "ALL CONFIRMED" if verdict_ok else "FAILURE")
print("F1 frozen reading: q0_app >= 0 => DEAD. Every tested history gives q0_app > 0.")
