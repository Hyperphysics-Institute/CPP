"""Patch 4442 -- founder: the slower space turns the fast electron's mixed cloud as it turns light's wavefront.

Part 1. Path 1 (4441): push on the whole energy, E g, over 4424 inertia, plus a turning.  Sideways, toward the mass, / g:
        with the space-half turning (index 1 + U): 1 + v^2 (GR);  with light's full wavefront turning (index K = 1 + 2U): 1 + 2 v^2
        (overshoot; at light speed 3).  So "push + light's full wavefront" double counts.
Part 2. The wave alone.  A wave of rest mass m and energy E in WC-DP-SEA-PV (clocks K^-1/2, rulers K^1/2) has the index
        n_J^2 = K^2 - K (m/E)^2  (the Jacobi / matter-wave index).  Its sideways ray acceleration v^2 d(ln n_J)/dx is (1 + v^2) g:
        GR's sideways acceleration (path shape) at every speed; the along motion needs energy conservation in the same metric.  At v -> 1 (m/E -> 0) n_J -> K: light's index.  At v -> 0 it gives g: the fall.
Part 3. Derived: the index splits literally as 2 g - g (m/E)^2; the two bookkeepings are regroupings of that total:
        4436: light's full turning 2 v^2 + rest-mass term (m/E)^2;   4440/4441: push 1 + space half v^2.
"""
import sympy as sp
U, v, x, gs = sp.symbols('U v x g', positive=True)
print("Part 1 (Path 1 push E g over gamma m = g sideways, plus a turning):")
for vv in (0.5, 0.9, 1.0):
    print(f"  v {vv}: space-half turning -> {1 + vv**2:.3f} (GR {1 + vv**2:.3f});  light's full wavefront turning -> {1 + 2*vv**2:.3f}")
K = 1 + 2*gs*x                          # U = g x, increasing toward +x (the mass side)
mE2 = 1 - v**2                          # (m/E)^2 for a body moving at speed v (flat-space value at the point)
nJ = sp.sqrt(K**2 - K*mE2)
acc = sp.simplify(sp.series(v**2*sp.diff(sp.log(nJ), x), gs, 0, 2).removeO().subs(x, 0)/gs)
print("Part 2 (matter-wave index n_J^2 = K^2 - K (m/E)^2): sideways acceleration / g =", sp.expand(acc))
for vv in (0.0, 0.5, 0.9, 1.0):
    print(f"  v {vv}: {float(acc.subs(v, vv)):.3f}" + ("  (light: index K)" if vv == 1.0 else "  (slow fall: g)" if vv == 0.0 else ""))
print("Part 3 (derived from n^2: K^2 part and rest-mass part separately, then two regroupings):")
nK2 = K**2; nM2 = -K*mE2
d = lambda e: sp.simplify(sp.series(sp.Rational(1, 2)*sp.diff(e, x), gs, 0, 2).removeO().subs(x, 0)/gs)
partK, partM = d(nK2), d(nM2)
print("  literal split: K^2 part", partK, "+ rest-mass part", sp.expand(partM), "=", sp.expand(partK + partM))
print("  4436 regrouping: 2 v^2 + (m/E)^2 =", sp.expand(2*v**2 + mE2), "; 4440/4441 regrouping: 1 + v^2 (push 1 + space half v^2)")
print("  (the splits are regroupings of one total, not term-by-term readings of the index)")
