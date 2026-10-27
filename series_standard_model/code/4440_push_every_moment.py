"""Patch 4440 -- founder picks (a): the push acts every Moment, and the electron resists more along its path than across
(4424: gamma m across, gamma^3 m along).

Part 1. GR weak field, isotropic coordinates: total (1 + v^2) across, (1 - 3 v^2) along (L = -m sqrt(A - B v^2)).
        Clock-only motion (B = 1: only clocks slow, rulers unchanged): across and along.
        Space part = total - clock-only.
Part 2. Under (a): a force F every Moment, resisted by 4424's inertia (gamma m across, gamma^3 m along), plus the light-speed part
        (speed follows c/K: -2 v^2 along; turning toward the slower side at HALF the Snell rate: v^2 across).
        F = E g (on the whole energy) matches GR in both directions; F = m g (rest mass) and F = (m/gamma) g fail.
Part 3. Light: clock part g across + space part g across = 2 g (its full refraction by n = K); the limb push (4403) is the clock half.
"""
import sympy as sp
t = sp.symbols('t'); m, eps, gs = sp.symbols('m epsilon g', positive=True)
x, y = sp.Function('x')(t), sp.Function('y')(t)
v = sp.symbols('v', positive=True)
def accel(Bfac):
    U = eps*gs*x
    L = -m*sp.sqrt((1 - 2*U) - Bfac(U)*(sp.diff(x, t)**2 + sp.diff(y, t)**2))
    eqs = [sp.diff(sp.diff(L, sp.diff(q, t)), t) - sp.diff(L, q) for q in (x, y)]
    xd, yd, xdd, ydd = sp.symbols('xd yd xdd ydd')
    eqs = [e.subs({sp.diff(x, t, 2): xdd, sp.diff(y, t, 2): ydd}).subs({sp.diff(x, t): xd, sp.diff(y, t): yd}).subs(x, 0) for e in eqs]
    sol = sp.solve(eqs, [xdd, ydd], dict=True)[0]
    first = lambda e: sp.simplify(sp.series(e, eps, 0, 2).removeO().coeff(eps))
    return first(sol[xdd].subs({xd: 0, yd: v}))/gs, first(sol[xdd].subs({xd: v, yd: 0}))/gs
tot = accel(lambda U: 1 + 2*U); clk = accel(lambda U: 1)
print("Part 1 (toward the mass, / g):")
print("  GR total:      across", tot[0], "  along", tot[1])
print("  clock-only:    across", clk[0], "  along", sp.factor(clk[1]))
print("  space part:    across", sp.simplify(tot[0] - clk[0]), "  along", sp.simplify(tot[1] - clk[1]))
gam = 1/sp.sqrt(1 - v**2)
print("Part 2 (force every Moment over 4424 inertia + speed following c/K (-2v^2 along) + half-Snell turning (v^2 across)):")
for name, F in (("E g (whole energy)", gam*m), ("m g (rest mass)", m), ("(m/gamma) g", m/gam)):
    a_across = sp.simplify(F/(gam*m) + v**2); a_along = sp.simplify(F/(gam**3*m) - 2*v**2)
    ok = sp.simplify(a_across - tot[0]) == 0 and sp.simplify(a_along - tot[1]) == 0
    print(f"  F = {name:20s}: across {sp.simplify(a_across)}, along {sp.expand(sp.simplify(a_along))}  -> matches GR: {ok}")
    print("      " + "  ".join(f"v {vv}: {float(a_across.subs(v, vv)):.3f} {float(a_along.subs(v, vv)):+.3f}" for vv in (0.5, 0.9))
          + f"   (GR v 0.5: {float(tot[0].subs(v, .5)):.3f} {float(tot[1].subs(v, .5)):+.3f}; v 0.9: {float(tot[0].subs(v, .9)):.3f} {float(tot[1].subs(v, .9)):+.3f})")
print("  clock-only along (1 - 2v^2) = push along (1 - v^2) + the clock half of the speed-follows-c/K term (-v^2)")
print("Part 3 (light, v = 1, across): push (on its energy) 1 + half-Snell turning 1 = 2, its full refraction by n = K; the limb push (4403) is the clock half")
