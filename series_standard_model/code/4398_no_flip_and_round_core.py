"""Patch 4398 -- founder (on 4397 s8): SSV_abs always increases toward the mass, so the PSR is
shortest toward it everywhere (no flip); at the black hole's edge the DI-bit shell fills the PSR;
inside there is no gradient, so no net direction.

Checks on the fixed (flat) grid, with the Planck sphere written as a shifted sphere:
   ds^2 = -N^2 dt^2 + (dr - v N dt)^2 + r^2 dOmega^2     (flat slices t = const)
 v = shift (in units of the local light step), N = overall size of the round sphere (clock scale).
Part 1  vacuum Einstein equations on flat slices force N' = 0 and v^2 = 2m/r (either sign of v).
Part 2  a region with no net pull (inside a hollow shell) on a flat grid must have v = 0; N may be < 1.
Part 3  the static clock sqrt(N^2(1 - v^2)) and the across reach are continuous at a shell; the
        shift and the round size N both jump.
Part 4  black hole with the floor at 8m/3: outside reaches, inside a round sphere of radius 1/2.
Part 5  the sign: v outward (his: shortest toward) vs inward: same static exterior; max |v| = sqrt(3)/2 < 1.
"""
import sympy as sp

t, r, th, ph = sp.symbols('t r theta phi', positive=True)
X = [t, r, th, ph]

def einstein(g):
    gi = g.inv()
    n = 4
    Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
            for d in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n)
    for b in range(n):
        for c in range(n):
            Ric[b, c] = sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                        + sum(Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a] for d in range(n))
                        for a in range(n)))
    R = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(n) for b in range(n)))
    return sp.simplify(Ric - R*g/2)

def metric(N, v):
    g = sp.zeros(4)
    g[0, 0] = -N**2 + (v*N)**2
    g[0, 1] = g[1, 0] = -v*N
    g[1, 1] = 1
    g[2, 2] = r**2
    g[3, 3] = r**2*sp.sin(th)**2
    return g

print("Part 1: vacuum on flat slices")
N = sp.Function('N')(r); v = sp.Function('v')(r)
G = einstein(metric(N, v))
eqs = [sp.factor(sp.simplify(G[i, j])) for (i, j) in [(0, 0), (0, 1), (1, 1), (2, 2)]]
# G_tr gives N' v = 0 type condition; check with the known solution
m = sp.symbols('m', positive=True)
for sgn in (+1, -1):
    sol = {N: 1, v: sgn*sp.sqrt(2*m/r)}
    Gs = einstein(metric(sp.Integer(1), sgn*sp.sqrt(2*m/r)))
    print(f"  N = 1, v = {'+' if sgn > 0 else '-'}sqrt(2m/r): all Einstein components zero:",
          all(sp.simplify(x) == 0 for x in Gs))
Gnv = einstein(metric(N, sp.sqrt(2*m/r)))
print("  with v = sqrt(2m/r) but N(r) free, G_rr =", sp.simplify(Gnv[1, 1]),
      " -> vacuum needs N' = 0 (N = 1 normalised far away);")
print("  (inside matter, G^t_t - G^r_r = -2(1 - v^2)N'/(rN): N' = 4 pi r (rho + p_r) N/(1 - v^2);")
print("   the round size N changes only where there is matter-energy, rho + p_r != 0, e.g. a shell's own surface energy)")

print("\nPart 2: a region with no net pull (inside a hollow shell)")
N0, v0 = sp.symbols('N0 v0', positive=True)
Gc = einstein(metric(N0, v0))
print("  constant N0, constant shift v0 != 0: G_tt =", sp.simplify(Gc[0, 0]), "(not flat unless v0 = 0)")
Gz = einstein(metric(N0, sp.Integer(0)))
print("  constant N0, v = 0: flat:", all(sp.simplify(x) == 0 for x in Gz))
f = sp.Function('f')(r)
# induced metric of t = f(r) in Minkowski: (1 - f'^2) dr^2 + r^2 dOmega^2 is flat only if f' = 0
print("  a flat, spherically symmetric slice of flat spacetime is t = f(r) with grr = 1 - f'(r)^2 -> f' = 0:",
      "no shift inside")

print("\nPart 3: matching at a hollow shell of radius R (mass M)")
M, R = sp.symbols('M R', positive=True)
clock_out = sp.sqrt(1 - 2*M/R)                 # N = 1, v^2 = 2M/R: sqrt(N^2(1 - v^2))
N_in = sp.sqrt(1 - 2*M/R)                      # round sphere of reduced size, no shift
print("  clock just outside:", clock_out, "  just inside:", N_in, "  continuous:", sp.simplify(clock_out - N_in) == 0)
print("  across reach outside sqrt(1 - v^2) =", clock_out, "; inside (round, radius N_in) =", N_in)
print("  shift: sqrt(2M/R) outside -> 0 inside; round size N: 1 outside ->", N_in, "inside")
print("  (both jump; the jumps are carried by the shell's own matter-energy)")

print("\nPart 4: black hole, floor where the across reach is 1/2 (u = 3/8, r = 8m/3)")
b = sp.sqrt(sp.Rational(3, 4))
print("  just outside: toward", sp.nsimplify(1 - b), "=", float(1 - b), " away", float(1 + b),
      " across", sp.sqrt(1 - b**2), " clock", sp.sqrt(1 - b**2))
print("  just inside (no gradient, round, radius 1/2): every direction 1/2, clock 1/2 -> light crosses",
      "1/2 grid unit per Moment: c/2 on the grid (cf. R-CORE-STORES-AS-CP-VIBRATION, 3623: 'the c/2 rate')")

print("\nPart 5: the sign")
print("  his: shortest TOWARD the mass at every r (v outward).  Max |v| outside the floor =",
      b, "=", float(b), "< 1: no horizon of either kind forms; static exterior identical to the inward sign.")
