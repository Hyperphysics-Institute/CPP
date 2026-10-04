#!/usr/bin/env python3
"""Patch 4382 -- founder's picture: a photon's CPs land half on attracting, half on
repelling GPs (opposite / like origin charge), so half its transit is slowed and half
sped by the thick DI-bit shell.  What net slowing does that give, and what must hold?

Part 1: net effect = curvature of the per-landing time response tau(delta).
Part 2: Monte Carlo along a path of random-sign landings (checks Part 1, shows bias term).
Part 3: first-order (Cassini) bounds on sign bias b and shell asymmetry s.
Part 4: universality and local light speed.
Part 5: a one-sided (hold-only) escape: a rotating, stretchable DP couples at first order only
        through its permanent dipole, which averages to zero over rotation; the induced
        (stretch) part is second order and always the same sign.
"""
import sympy as sp, random, math

d, b, s, x = sp.symbols('delta b s x', real=True)

print("Part 1: time per unit path, averaged over equal attracting/repelling shares")
cases = {
 "A speed scaled by (1-/+delta), fixed crossing length (hiking-over-hills)": 1/(1 - d),
 "B fixed extra/less hold time +/-delta per landing":                         1 + d,
 "C step length scaled, fixed time per Moment (time per length = 1/(1+-d))":   None,
 "D energy-conserving crossing of +/-x potential, v ~ sqrt(1 -/+ x)":          1/sp.sqrt(1 - x),
}
# A: attracting site -> speed 1-d -> time 1/(1-d); repelling -> 1/(1+d)
tA = sp.Rational(1,2)*(1/(1-d) + 1/(1+d))
print("  A:", sp.simplify(tA), "->", sp.series(tA, d, 0, 5).removeO(),
      "  (net speed = 1 - delta^2 exactly: the 4379 round-trip form)")
tB = sp.Rational(1,2)*((1+d) + (1-d))
print("  B:", sp.simplify(tB), "  (no net slowing)")
# C: per Moment the CP advances 1+-d; per landing count is per Moment, so mean advance per Moment:
advC = sp.Rational(1,2)*((1-d) + (1+d))
print("  C: mean advance per Moment =", sp.simplify(advC), "  (no net slowing: landings counted per Moment)")
tD = sp.Rational(1,2)*(1/sp.sqrt(1-x) + 1/sp.sqrt(1+x))
print("  D:", sp.series(tD, x, 0, 5).removeO(), "  (illustrative only: massive-particle kinematics; time +3/8 x^2, speed -3/8 x^2 to leading order)")
print("  General: tau = 1 + a*delta + c*delta^2 -> mean 1 + c*delta^2; net slowing needs c > 0")
print("  (the hold-up at an attracting site exceeds the gain at a repelling one).")

print("\nPart 2: Monte Carlo, N landings with random sign, case A")
random.seed(4382)
for delta in (0.05, 0.1, 0.2):
    for bias in (0.0, 0.01):
        N = 400000; T = 0.0
        for _ in range(N):
            att = random.random() < 0.5*(1+bias)
            T += 1/(1-delta) if att else 1/(1+delta)
        v = N/T
        pred = 1/(1 + delta**2/(1-delta**2) + bias*delta/(1-delta**2))
        print(f"  delta={delta:4.2f} bias={bias:4.2f}: v_MC={v:.5f}  v_pred={pred:.5f}  1-delta^2={1-delta**2:.5f}")

print("\nPart 3: first-order terms (Cassini bound |a| < 8e-6 on a first-order clock/light term a*eps, as used in 4373/4378)")
tbias = sp.Rational(1,2)*((1+b)/(1-d) + (1-b)/(1+d))
print("  sign bias b:      tau =", sp.series(tbias, d, 0, 3).removeO())
tasym = sp.Rational(1,2)*(1/(1-d*(1+s)) + 1/(1+d*(1-s)))
print("  shell asym s:     tau =", sp.expand(sp.series(tasym, d, 0, 3).removeO()))
print("  With delta = kappa*rho, rho ~ eps/2: first-order term ~ (b or s)*kappa*eps/2.")
for kap in (0.7, 1.0, 1.21):
    print(f"   kappa={kap:4.2f}: need |b|,|s| < {2*8e-6/kap:.1e}")
print("  A charge-balanced GP sea gives b ~ 1/sqrt(N_landings) -> negligible; s must vanish by")
print("  symmetry (shell excess the same around + and - origin GPs near a neutral mass).")

print("\nPart 4: universality.  Light speed measured locally = (rulers crossed)/(clock ticks).")
for X in (1.0, 0.99, 0.9):
    print(f"   X={X}: both slowed -> c_local = {X/X:.3f};  clock only -> {1/X:.3f};  light only -> {X:.3f}")
print("  Local Lorentz invariance requires the same X for light and clocks.  A per-landing")
print("  mechanism acting on every CP (photon DP or ZBW cloud) gives that, provided delta depends")
print("  only on the local shell, not on the composite the CP belongs to.")

print("\nPart 5: rotating DP with permanent dipole p0 and induced dipole alpha*E")
th, p0, al, E = sp.symbols('theta p0 alpha E', positive=True)
U = -(p0*sp.cos(th) + al*E)*E          # energy along E, DP at angle theta
Uav = sp.integrate(U, (th, 0, 2*sp.pi))/(2*sp.pi)
print("  <U> over rotation =", sp.simplify(Uav), " (first-order p0 term averages out; induced term ~E^2, one sign)")
print("  So a hold-only response proportional to the induced part would be second order with no")
print("  speed-up needed.  This is Claude's construction, not on file; it would act on neutral DPs")
print("  (photons) but a single unpaired charge has no rotation average, so for matter clocks the")
print("  first-order question (Part 3, s) remains.")

print("  Caveat: if ordinary space already has a site field E0 and the well adds dE, then")
print("  E^2 changes by 2*E0*dE + dE^2: FIRST order in the shell excess unless E0's holding is zero.")
print("  This is 4380's beta0 condition again: the escape needs no holding in ordinary space.")
