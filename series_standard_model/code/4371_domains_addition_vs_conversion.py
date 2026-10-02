#!/usr/bin/env python3
"""Patch 4371 - the founder's domains (2 Oct 2026): the addition law changes once PSR spheres touch,
once they are fully populated, and once they fully overlap.  Where can that act on the ringdown?

  1. ADDITION in empty space.  The relay updates each GP from an average over its neighbourhood: a thin
     shell (sphere partly filled) or the whole ball (sphere fully populated).  Does the change of
     averaging region change how a body's stress falls off?  Test the mean of 1/r over a shell and over
     a ball about a point outside the source (Newton/Gauss mean-value property).
  2. CONVERSION.  How full a GP's own sphere is with its DI-bits: fill f = N / (GPs in its sphere)
     = 1/(8 q^3) (R-DIBIT-COUNT-AT-FLOOR, n_inf/N = 8).  Fill in ordinary space, at the photon sphere
     (both curves) and at the cap.
  3. The speed-up Einstein's curve needs over the steady-percentage curve,
     S = (d ln q/d eps)_Pade / (d ln q/d eps)_exp = 1/(1 - eps^2/4), at those points.
"""
import numpy as np
import sympy as sp
print(__doc__)

# 1. mean-value property (exact, sympy) for a point at distance d > a from the origin
r_, a, d, t = sp.symbols('r a d t', positive=True)
dist = sp.sqrt(d**2 + r_**2 - 2 * d * r_ * t)            # t = cos(theta)
shell = sp.simplify(sp.integrate(1 / dist, (t, -1, 1)) / 2)  # mean of 1/|x| over a sphere of radius r about the point
vals = [(3, 1), (5, 2), (7, sp.Rational(13, 2))]
print("1. exact mean of 1/|x| over a sphere of radius a about a point at distance d > a, minus 1/d:",
      [sp.nsimplify(sp.simplify(shell.subs({r_: aa, d: dd}) - sp.Rational(1, 1) / dd)) for dd, aa in vals])
ball = sp.integrate(shell.subs(r_, r_) * 4 * sp.pi * r_**2, (r_, 0, a)) / (sp.Rational(4, 3) * sp.pi * a**3)
print("   mean over the whole ball of radius a:", sp.simplify(ball.subs(d, 3 * a)), "at d = 3a (expect 1/(3a))")
# numeric cross-check with Monte Carlo (ball, filled)
rng = np.random.default_rng(0)
pts = rng.normal(size=(400000, 3)); pts /= np.linalg.norm(pts, axis=1)[:, None]
rad = rng.random(400000) ** (1 / 3)
x0 = np.array([3.0, 0, 0])
ballpts = x0 + pts * rad[:, None]
band = rng.random(400000) * (1 - 0.5**3) + 0.5**3
bandpts = x0 + pts * (band ** (1 / 3))[:, None]
print(f"   Monte Carlo, centre 3, radius 1: full ball {np.mean(1/np.linalg.norm(ballpts,axis=1)):.5f},"
      f" band 0.5-1 {np.mean(1/np.linalg.norm(bandpts,axis=1)):.5f}, thin shell {np.mean(1/np.linalg.norm(x0+pts,axis=1)):.5f}; 1/3 = {1/3:.5f}")
print("   -> any averaging region, shell, band or full ball, leaves 1/r unchanged outside the source:")
print("      in empty space the stress keeps adding as before, whatever the fill. (GR-1j T-2.)")

# 2-3. fill and the required speed-up
e = sp.Symbol('epsilon', positive=True)
q_exp = sp.exp(-e)
q_pade = (1 - e / 2) / (1 + e / 2)
S = sp.simplify(sp.diff(sp.log(q_pade), e) / sp.diff(sp.log(q_exp), e))
print("\n2-3. Einstein's speed-up over the steady curve: S(eps) =", S)
cap_pade = sp.solve(sp.Eq(q_pade, sp.Rational(1, 2)), e)[0]
rows = [("ordinary space", 0.0, 0.0),
        ("photon sphere, steady curve", 0.5, None),
        ("photon sphere, Einstein (eps = 2*rho, rho = 1/(2*1.866))", None, float(1 / (1 + np.sqrt(3) / 2))),
        ("cap, steady curve (eps = ln 2)", float(np.log(2)), None),
        ("cap, Einstein (q = 1/2)", None, float(cap_pade))]
print("   point                                                    q       fill f    S (Einstein's speed-up)")
for name, eexp, epad in rows:
    if eexp is not None:
        qv = float(q_exp.subs(e, eexp)); ev = eexp
    else:
        qv = float(q_pade.subs(e, epad)); ev = epad
    Scol = f"{float(S.subs(e, ev)):7.4f}" if epad is not None else "    -  "
    print(f"   {name:56s} {qv:6.4f}   {1/(8*qv**3):7.3f}    {Scol}")
print(f"   Einstein's curve reaches the floor q = 1/2 at eps = {cap_pade} = AP-5's ratified cap v = 2/3 (consistent).")
print("   Fill rises from 1/8 in ordinary space to about 0.56-0.65 at the photon sphere and 1 at the cap; Einstein")
print("   needs the PSR to shrink ~8% faster per unit stress at the photon sphere and 12.5% faster at the cap.")
print("   Background price (4365): any S != 1 brings back an eps0^2-order residual in local G, unobservable; in alpha")
print("   only if alpha's reading carries the lapse sensitivity (TODO-4364-EPSABS).")
