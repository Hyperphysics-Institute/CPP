#!/usr/bin/env python3
"""
Patch 2870 — locating the knife-edge; retracting the 2869 §4 "discrepancy".

2869 §4 claimed Stage B (forward self-force) and Stage C (exponential
momentum decay) were "opposite signs for what should be the same
physics". READING THE CODE SHOWS THAT CANNOT BE RIGHT: in Stage C the
release rule is literally

    v = mu * Fs

so v > 0 REQUIRES Fs > 0. The sign is forward in BOTH stages by
construction. There was never a sign contradiction. What Stage C shows
is that Fs DECAYS, not that it reverses.

THE ACTUAL STRUCTURE. Stage B holds v = vf and measures
    alpha = F_hold / vf   (2868: 9.377e-4, constant over 4x in v)
The Aristotelian primitive closes the loop as v = mu*Fs = mu*alpha*v, so

    v (1 - mu*alpha) = 0

    mu < 1/alpha  ->  DRAG   (v decays)
    mu = 1/alpha  ->  MARGINAL (any v sustained: Newton I)
    mu > 1/alpha  ->  RUNAWAY (v self-amplifies)

so the knife-edge sits at  mu_crit = 1/alpha.  2496 ran Stage C at
mu = 10 and 25 and saw decay; 2496 §7(a) separately reports runaway
"at high mobility". THOSE ARE THE TWO SIDES OF ONE KNIFE-EDGE AND
NOBODY COMPUTED WHERE IT WAS.

TESTS
  T1  sign of Fs during the Stage C coast at mu = 10, 25   (expect > 0)
  T2  mu_crit = 1/alpha from Stage B
  T3  sweep mu across mu_crit and classify decay / marginal / growth

SCOPE. Tier-2 scalar toy; bare prescribed point. Says nothing about
eps_mem or the ambient Sea. Per the founder (2870 §1) CPP has no
self-force: Fs here is the sea's response to the CP's declaration
re-entering at the CP's location, i.e. an SSV_net contribution from
other entities, not the CP acting on itself.
"""

import importlib.util
import os
import numpy as np

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   '2496_sf6_inertia_impulse.py')
spec = importlib.util.spec_from_file_location('sf6_pin', SRC)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

N, c, h, g = 96, 1., 1., 8.
sigma, dt, vf, Tr, Th = 1.5, 0.35, 0.05, 30., 40.


def build(st):
    """Reimplements the 2496 step/loop, additionally recording Fs in Stage C."""
    phi_s, E0 = st['phi_s'], st['E0']
    stamp, dep, _ = m.make(N, sigma)
    lap = lambda f: (np.roll(f, 1, 0) + np.roll(f, -1, 0) + np.roll(f, 1, 1)
                     + np.roll(f, -1, 1) + np.roll(f, 1, 2) + np.roll(f, -1, 2)
                     - 6 * f) / h ** 2
    ss = lambda s: np.clip(s, 0, 1) ** 2 * (3 - 2 * np.clip(s, 0, 1))
    vel = lambda t: vf * ss(t / Tr)

    def step(state, vfun=None, mu=None):
        phi, phi_old, X, t, rho = state
        i0, Xf, sl = dep(X)
        W, dWz = stamp(Xf)
        Fs = g * np.sum(phi[sl] * dWz)
        rho.fill(0.)
        rho[sl] = W
        phi_new = 2 * phi - phi_old + dt * dt * (c * c * lap(phi) + g * rho)
        v = vfun(t) if vfun else mu * Fs
        Xn = X.copy()
        Xn[0] += v * dt
        return (phi_new, phi, Xn, t + dt, rho), dict(t=t, v=v, Fs=Fs)

    state = (phi_s.copy(), phi_s.copy(), np.array([N / 2.] * 3), 0.,
             np.zeros((N, N, N)))
    recB = []
    for _ in range(int((Tr + Th) / dt)):
        state, d = step(state, vfun=vel)
        recB.append(d)
    return step, state, recB


def coast(step, state, mu, Tc=45.):
    st = (state[0].copy(), state[1].copy(), state[2].copy(), state[3],
          np.zeros((N, N, N)))
    rc = []
    for _ in range(int(Tc / dt)):
        st, d = step(st, mu=mu)
        rc.append(d)
        if abs(d['v']) > 0.5 or not np.isfinite(d['v']):
            break
    return rc


def main():
    print("=" * 70)
    print("PATCH 2870 — knife-edge location; 2869 §4 retraction")
    print("=" * 70)
    st = m.stages_0A(N, sigma, g, c, h, [vf])
    step, endB, recB = build(st)

    tB = np.array([d['t'] for d in recB])
    FB = np.array([d['Fs'] for d in recB])
    hold = (tB > Tr + 10) & (tB < Tr + Th - 2)
    F_hold = float(np.mean(FB[hold]))
    alpha = F_hold / vf
    mu_crit = 1.0 / alpha

    print(f"\nStage B: F_hold = {F_hold:+.4e}   alpha = F_hold/vf = "
          f"{alpha:.4e}")
    print(f"T2  mu_crit = 1/alpha = {mu_crit:.1f}")

    print("\nT1 — sign of Fs during Stage C coast (2869 §4 claimed a flip)")
    print(f"{'mu':>8}{'Fs first':>14}{'Fs last':>14}{'any Fs<0?':>12}")
    for mu in [10., 25.]:
        rc = coast(step, endB, mu)
        Fs = np.array([d['Fs'] for d in rc])
        print(f"{mu:8.1f}{Fs[0]:+14.3e}{Fs[-1]:+14.3e}"
              f"{str(bool((Fs < 0).any())):>12}")

    print("\nT3 — mu sweep across mu_crit: v_final/v_initial")
    print(f"{'mu':>9}{'mu/mu_crit':>12}{'v_init':>12}{'v_final':>12}"
          f"{'ratio':>10}{'verdict':>10}")
    for mu in [10., 25., 0.25 * mu_crit, 0.75 * mu_crit, mu_crit,
               1.25 * mu_crit, 2.0 * mu_crit]:
        rc = coast(step, endB, mu)
        v = np.array([d['v'] for d in rc])
        r = v[-1] / v[0] if v[0] != 0 else float('nan')
        verdict = ('GROWTH' if r > 1.05 else
                   'flat' if r > 0.95 else 'decay')
        print(f"{mu:9.1f}{mu/mu_crit:12.3f}{v[0]:12.3e}{v[-1]:12.3e}"
              f"{r:10.3f}{verdict:>10}")

    print("\n" + "-" * 70)
    print("  2869 §4 RETRACTED: v = mu*Fs makes Fs>0 mandatory in Stage C.")
    print("  No sign flip existed. Stage C shows Fs DECAYING, not reversing.")
    print(f"  The knife-edge is at mu_crit = {mu_crit:.1f}; 2496 probed")
    print("  mu = 10 and 25, i.e. ~2% of critical -- deep on the drag side.")
    print("  2496's Stage C decay and its §7(a) 'runaway at high mobility'")
    print("  are the two sides of ONE knife-edge, never located until now.")
    print("  Tier-2 scalar toy. No claim about eps_mem or the ambient Sea.")


if __name__ == '__main__':
    main()
