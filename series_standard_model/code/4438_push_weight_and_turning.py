"""Patch 4438 -- why the push weakens with speed in CPP's split, and the two balls.

Part 1. GR first-order coordinate acceleration (weak field, isotropic coordinates, c = 1), derived from
        L = -m sqrt(A - B v^2), A = 1 - 2U, B = 1 + 2U:  across (1 + v^2) g, along (1 - 3 v^2) g.  GR fixes only these totals.
Part 2. The 4436 step rule: the CP stores f (its step as a fraction of the local light speed c/K); coordinate speed v = f c/K;
        its direction turns toward the slower side at the Snell rate; the push changes f by W g per unit time (W = push weight).
        Across: W + 2 v^2.  Along: W - 2 v^2 (the speed follows c/K).  Given this full Snell-rate turning (assumed), matches GR in both directions only for W = 1 - f^2.
        In register terms (4425: SSV_abs <-> E, |SSV_net| <-> p) 1 - f^2 = (S^2 - V^2)/S^2 = (m/E)^2.
        Alternatives shown failing: W = 1 with full turning (a CP near c would get 3 g), and the 'per-cycle' force (m/gamma) g
        with 4424's inertia (gamma m across, gamma^3 m along), which fits across but not along.
Part 3. Two balls of rest mass m at +/-0.6c recorded in the lab: 2 gamma m c^2 = 2.5 m c^2 = 1.25 x their rest energy 2 m c^2.
"""
import sympy as sp
t = sp.symbols('t'); m, eps, gs = sp.symbols('m epsilon g', positive=True)
x, y = sp.Function('x')(t), sp.Function('y')(t)
U = eps*gs*x                                   # U grows toward +x (the mass side); g = |grad U|
L = -m*sp.sqrt((1 - 2*U) - (1 + 2*U)*(sp.diff(x, t)**2 + sp.diff(y, t)**2))
eqs = [sp.diff(sp.diff(L, sp.diff(q, t)), t) - sp.diff(L, q) for q in (x, y)]
xd, yd, xdd, ydd = sp.symbols('xd yd xdd ydd')
eqs = [e.subs({sp.diff(x, t, 2): xdd, sp.diff(y, t, 2): ydd}).subs({sp.diff(x, t): xd, sp.diff(y, t): yd}).subs(x, 0) for e in eqs]
sol = sp.solve(eqs, [xdd, ydd], dict=True)[0]
v = sp.symbols('v', positive=True)
first = lambda e: sp.simplify(sp.series(e, eps, 0, 2).removeO().coeff(eps))
across = first(sol[xdd].subs({xd: 0, yd: v}))/gs
along = first(sol[xdd].subs({xd: v, yd: 0}))/gs
print("Part 1 (GR, toward the mass, / g):  across", across, "  along", along)
print("Part 2 (4436 step rule; push weight W):")
W = 1 - v**2
print("  W = 1 - f^2 = (S^2 - V^2)/S^2:  across", sp.expand(W + 2*v**2), "  along", sp.expand(W - 2*v**2),
      "  matches GR:", sp.simplify(W + 2*v**2 - across) == 0 and sp.simplify(W - 2*v**2 - along) == 0)
print("  W = 1 (push not weakened):      across", 1 + 2*v**2, "  along", 1 - 2*v**2, "  -> a CP near c with full turning would get 3 g across; light gets 2 g")
gam = 1/sp.sqrt(1 - v**2)
pc_across, pc_along = sp.simplify((m/gam)/(gam*m)), sp.simplify((m/gam)/(gam**3*m))
print("  per-cycle force (m/gamma) g with 4424 inertia: push across", pc_across, " along", pc_along)
print("     totals: across", sp.expand(pc_across + 2*v**2), " along", sp.expand(pc_along - 2*v**2), "(GR along 1 - 3v^2: fails)")
for vv in (0.5, 0.9):
    print(f"  v {vv}: GR across {float(across.subs(v, vv)):.3f} along {float(along.subs(v, vv)):+.3f} | W=1-f^2 {1-vv**2+2*vv**2:.3f} {1-vv**2-2*vv**2:+.3f}"
          f" | W=1 {1+2*vv**2:.3f} {1-2*vv**2:+.3f} | per-cycle along {float((pc_along - 2*v**2).subs(v, vv)):+.3f}")
print("Part 3 (two balls of rest mass m at +/-0.6c, recorded in the lab):")
g6 = 1/(1 - 0.36)**0.5
print(f"  total {2*g6:.3f} m c^2 = {g6:.3f} x the two balls' rest energy 2 m c^2; kinetic part {2*(g6-1):.3f} m c^2")
