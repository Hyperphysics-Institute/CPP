"""Patch 4399 -- founder (on 4398): 'no net pull inside' meant SSV_net = 0 (charges balanced around every CP).
Gravity (grad SSV_abs) inside a black hole points to the centre, is largest at the edge, zero at the centre, and in
between falls from the edge to the centre.

Part 1  the census u = sum m/r is harmonic, so the outer layers' pull on an interior point cancels exactly (shell
        theorem): a direct numerical sum over a shell.
Part 2  pull inside = m(r)/r^2: largest at the edge only if the mass is spread out (uniform: pull ~ r); a mass drained
        to a central core gives a pull that GROWS inward instead.
Part 3  the shift inside, beta^2 = 2 m(r)/r: zero at the centre, sqrt(3)/2 at the 8m/3 edge, continuous with outside.
Part 4  option A (Einstein's uniform-density interior, positive pressure): clocks keep slowing inward: 1/4 at the centre.
Part 5  option B (Planck sphere pinned at its floor inside, clocks 1/2 throughout): round size N = (1/2)/sqrt(1 - beta^2),
        1 at the edge, 1/2 at the centre; in GR terms a uniform energy density with tension p = -rho/3 and no pull felt
        by a CP held still.
River form on the flat grid: ds^2 = -N^2 dt^2 + (dr - v N dt)^2 + r^2 dOmega^2; static clock = N sqrt(1 - v^2).
"""
import numpy as np
import sympy as sp

print("Part 1: pull of a uniform shell (radius 1) on interior points, inverse-square sum")
rng = np.random.default_rng(1)
pts = rng.normal(size=(400000, 3)); pts /= np.linalg.norm(pts, axis=1)[:, None]
for x in (0.0, 0.3, 0.6, 0.9):
    d = pts - np.array([x, 0, 0]); f = (d / np.linalg.norm(d, axis=1)[:, None]**3).mean(axis=0)
    print(f"  point at {x:.1f}: net pull {np.linalg.norm(f):.4f}  (an outside point at 2.0 would feel {1/4:.4f})")
print("  -> zero within sampling noise (the noise grows near the shell): the outward pull of the layers outside a")
print("     point cancels exactly; only the mass")
print("     inside its radius pulls (the census is harmonic, so the analytic result is exactly zero)")

r, M, R = sp.symbols('r M R', positive=True)
print("\nPart 2: pull inside a ball of radius R")
m_uni = M*r**3/R**3
print("  uniform: pull = m(r)/r^2 =", sp.simplify(m_uni/r**2), "-> zero at the centre, largest (M/R^2) at the edge")
print("  drained to a small central core of radius a: pull = M/r^2 for a < r < R -> largest near the core, not the edge")
print("  'largest at the edge' needs m(r)/r^2 <= M/R^2 everywhere: mass spread through the interior")

print("\nPart 3: the shift inside (uniform, 2M/R = 3/4 at the 8m/3 edge)")
beta = sp.sqrt(2*m_uni/r)
sub = {M: 3, R: 8}
for x in (0, 2, 4, 6, 8):
    print(f"  r = {x}: beta = {float(beta.subs(sub).subs(r, x)):.4f}")
print("  outside at the edge: sqrt(2M/R) =", float(sp.sqrt(sp.Rational(3, 4))), "-> continuous (no jump in the shift)")

print("\nPart 4: option A -- Einstein's uniform-density interior (positive pressure)")
A = sp.sqrt(1 - 2*M/R); B = sp.sqrt(1 - 2*M*r**2/R**3)
clockA = sp.Rational(3, 2)*A - B/2
pA = (B - A)/(3*A - B)     # p/rho
for x in (0, 4, 8):
    print(f"  r = {x}: clock = {float(clockA.subs(sub).subs(r, x)):.4f}, pressure/energy density = {float(pA.subs(sub).subs(r, x)):.3f}")
print("  clocks slow from 1/2 at the edge to 1/4 at the centre: the Planck sphere would go below the floor's 1/2;")
print("  light at the centre c/4 on the grid; central pressure equals the energy density")

print("\nPart 5: option B -- Planck sphere pinned at its floor inside (clock 1/2 throughout)")
v = sp.sqrt(2*M/R**3)*r
N = sp.Rational(1, 2)/sp.sqrt(1 - v**2)
print("  round size N at the edge:", sp.simplify(N.subs(r, R).subs(sub)), " at the centre:", N.subs(r, 0),
      " (outside N = 1: continuous)")
X = [sp.Symbol('t'), r, sp.Symbol('th'), sp.Symbol('ph')]
th = X[2]
g = sp.zeros(4)
g[0, 0] = -N**2*(1 - v**2); g[0, 1] = g[1, 0] = -v*N; g[1, 1] = 1; g[2, 2] = r**2; g[3, 3] = r**2*sp.sin(th)**2
gi = g.inv()
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
        for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
Ric = sp.zeros(4)
for b in range(4):
    for c in range(4):
        Ric[b, c] = sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                    + sum(Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a] for d in range(4)) for a in range(4)))
Rs = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(4) for b in range(4)))
Gm = sp.simplify(gi*(Ric - Rs*g/2))
rho = sp.simplify(-Gm[0, 0]/(8*sp.pi)); p_r = sp.simplify(Gm[1, 1]/(8*sp.pi)); p_t = sp.simplify(Gm[2, 2]/(8*sp.pi))
print("  energy density:", rho, " radial pressure:", p_r, " tangential pressure:", p_t)
print("  -> uniform energy density (total mass M) with isotropic tension p = -rho/3: rho + 3p = 0, so a CP held still")
print("     feels no pull (static clock constant), although the shift (the SSV_abs gradient) follows his curve")
print("  at the edge the radial tension jumps from -rho/3 inside to 0 outside, so option B needs a surface layer at")
print("  the edge (candidate: the AP-5 saturation layer); option A has zero pressure at the edge and needs none")

print("\nPart 6: his curve vs the ringdown bound (3702: >= 90% of M inside 2M)")
x = sp.Rational(3, 4)   # 2M / (8M/3)
print("  pull largest at the edge needs m(r) <= M (r/R)^2; at r = 2M = (3/4)R: m <= ", x**2, "=", float(x**2), "of M")
print("  uniform ball: m(2M) =", x**3, "=", float(x**3), "of M (3702: 42%, excluded)")
print("  -> his filled-core curve and 3702's estimate-grade bound cannot both hold")
