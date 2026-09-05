#!/usr/bin/env python3
"""
Patch 3632 verify — OPEN-GR-SHELL-DATUM-1 rung 2: the census closure made relativistic, and where it stops.
 (1) Convention: the corpus's k2 is Hinderer's. Hinderer's k2 = lambda/(2 R^5) exactly for the decaying amplitude lambda
     (r^3 H_D -> 1, H_G -> r^2) — checked against the closed formula at four lambdas. In the Newtonian limit Hinderer's
     formula gives k2 = (2-y)/(2(y+3)); the incompressible body (y -> -1 with the density-jump correction) gives 3/4.
     So 3631 §5's "k2 = 3/2" was Love's convention; in the corpus's convention Kelvin's homogeneous body is k2 = 3/4.
 (2) The far-field dictionary: -(1+g_tt)/2 = f H Y/2 -> v_pert = -(r^2/2) Y - (lambda/2) Y/r^3 at large r (register v = -(1+g_tt)/2
     to leading order). The census of a uniform-count region (density rho_c = 3M/(4 pi Rbar^3), lattice radius Rbar = 3M/2)
     whose boundary moves by dbar Y (lattice coordinates) is v_ind = (3/5) M Rbar dbar Y / rbar^3. Equating: lambda = -(6/5) M Rbar dbar.
     Newtonian check: with the Newtonian lapse pin (self + layer + tide level set) this closure returns k2 = 3/4.
 (3) The relativistic closure needs ONE lattice-frame number: dbar = (drbar/dr) xi_RW - zeta^r(R), the level-set displacement in
     lattice coordinates, where zeta is the static gauge vector from RW gauge to the lattice frame (3611: the harmonic-pattern
     frame; residual at the wall = F-16, open). Two bracketing identifications are computed: (A) zeta^r(R) = 0 [3611's stated
     residual choice, 'GPs do not move'] -> dbar = (9/8) xi_RW; (B) the level-set sphere's areal radius mapped by the background
     -> dbar = (9/8) delta r_areal. They give k2 of OPPOSITE sign. The datum has moved from 'the shell's stress' to
     'the lattice-frame location of the level set' — OPEN-GR-LATTICE-FRAME-1's static face.
"""
import numpy as np, sympy as sp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
M = 1; R = sp.Rational(8, 3); C = M / R; Rbar = sp.Rational(3, 2)
r, lam, y = sp.symbols("r lambda y")
HG = r * (r - 2 * M)
HD = -5 * (r - 2) * (6 * r**3 - 3 * r**2 * (sp.log(r) - sp.log(r - 2)) * (r**2 - 4 * r + 4) - 18 * r**2 + 8 * r + 4) / (16 * r * (r**2 - 4 * r + 4))   # 3631 closed form
def k2_hinderer(C, y):
    C = float(C); y = float(y)
    return (8 * C**5 / 5) * (1 - 2 * C)**2 * (2 + 2 * C * (y - 1) - y) / (2 * C * (6 - 3 * y + 3 * C * (5 * y - 8)) + 4 * C**3 * (13 - 11 * y + C * (3 * y - 2) + 2 * C**2 * (1 + y)) + 3 * (1 - 2 * C)**2 * (2 - y + 2 * C * (y - 1)) * np.log(1 - 2 * C))
H = HG + lam * HD
yl = sp.simplify((R * sp.diff(H, r) / H).subs(r, R))
# (1) convention
ok = all(abs(k2_hinderer(C, yl.subs(lam, lv)) - float(lv) / (2 * float(R)**5)) < 1e-9 for lv in [0, 1, -21.6196, 3.2521])
check("(1a) Hinderer's k2 = lambda/(2 R^5) exactly (four lambdas, 1e-9) — the far-field induced coefficient IS the Love number", ok)
Cs = sp.symbols("C", positive=True)
k2sym = (8 * Cs**5 / 5) * (1 - 2 * Cs)**2 * (2 + 2 * Cs * (y - 1) - y) / (2 * Cs * (6 - 3 * y + 3 * Cs * (5 * y - 8)) + 4 * Cs**3 * (13 - 11 * y + Cs * (3 * y - 2) + 2 * Cs**2 * (1 + y)) + 3 * (1 - 2 * Cs)**2 * (2 - y + 2 * Cs * (y - 1)) * sp.log(1 - 2 * Cs))
k2_newt = sp.simplify(sp.limit(k2sym, Cs, 0))
check("(1b) Newtonian limit of Hinderer's formula: k2 = (2 - y)/(2(y + 3))", sp.simplify(k2_newt - (2 - y) / (2 * (y + 3))) == 0, str(k2_newt))
check("(1c) incompressible body (y = 2 - 3 = -1): k2 = 3/4 in the corpus's convention — 3631 §5's '3/2' was Love's convention (h2 = 1 + 2 k2_H = 5/2)", sp.simplify(k2_newt.subs(y, -1)) == sp.Rational(3, 4))
# (2) the closure and its Newtonian check
G_, rho, Rb = sp.symbols("G rho R_b", positive=True); E, d = sp.symbols("E d", real=True)
# far-field: v_tide = a r^2 Y, v_ind = b Y / r^3;  Hinderer-normalised k2 = b/(2 a R^5)  [since (a, b) = (-1/2, -lambda/2) gives lambda/(2R^5)]
g_surf = sp.Rational(4, 3) * sp.pi * G_ * rho * Rb; layer = -4 * sp.pi * G_ * rho * d * Rb / 5
d_sol = sp.solve(sp.Eq(g_surf * d + layer + E * Rb**2, 0), d)[0]          # Newtonian level set (potential Phi = -v)
b_over_a = sp.simplify((-G_ * 4 * sp.pi * rho * Rb**4 * d_sol / 5) / E)  # induced potential coefficient / tidal coefficient
check("(2a) the census closure (uniform count to the moved level set) with the NEWTONIAN level set returns k2 = b/(2 a R^5) = 3/4", sp.simplify(b_over_a / (2 * Rb**5)) == sp.Rational(3, 4))
# the closure written for the R-core: lambda = -(6/5) M Rbar dbar   (v_ind = (3/5) M Rbar dbar Y / rbar^3 = -(lambda/2) Y / r^3 at far field)
closure = lambda dbar: -sp.Rational(6, 5) * M * Rbar * dbar
# (3) the lattice-frame number, two brackets (3631 values per unit tide, affine in lambda)
xi_RW = -1.5802469 - 0.31765831 * lam
dr_areal = -8.3950617 - 0.6328723 * lam
drbar_dr = 1 - (sp.Rational(2, 3))**2 / 4                                   # dr/drbar = 1 - v^2/4 = 8/9 at v = 2/3 -> drbar/dr = 9/8
check("(3a) background map areal -> lattice at the surface: drbar/dr = 9/8", sp.simplify(1 / drbar_dr - sp.Rational(9, 8)) == 0)
res = {}
for nm, dbar in [("(A) zeta^r(R) = 0 [3611 residual: GPs do not move]: dbar = (9/8) xi_RW", xi_RW / drbar_dr),
                 ("(B) areal radius of the level-set sphere mapped by the background: dbar = (9/8) delta r_areal", dr_areal / drbar_dr)]:
    lv = sp.solve(sp.Eq(lam, closure(dbar)), lam)[0]
    k2 = float(lv) / (2 * float(R)**5); res[nm] = (float(lv), k2)
    print(f"     {nm}\n         lambda = {float(lv):9.4f}   k2 = {k2:+.4f}   Lambda = {(2/3)*k2/float(C)**5:+.2f}")
k2A, k2B = res[list(res)[0]][1], res[list(res)[1]][1]
check("(3b) bracket (A) is positive, of the order of the family's magnitude (k2 ~ +0.03)", 0.01 < k2A < 0.1, f"{k2A:+.4f}")
check("(3c) bracket (B) is negative and larger (k2 ~ -0.2): the two lattice-frame identifications differ in SIGN — the sign of the theory's Love number is now a question about zeta^r(R), the static residual of the harmonic-pattern frame at the wall (F-16), not about the shell", k2B < 0 and abs(k2B) > abs(k2A))
# sensitivity: k2 as a function of zeta^r(R) per unit tide
zr = sp.symbols("zeta_r")
lv_z = sp.solve(sp.Eq(lam, closure((xi_RW - zr) / drbar_dr)), lam)[0]
k2_z = sp.expand(lv_z / (2 * R**5))
print(f"     k2(zeta^r(R)) = {sp.N(k2_z, 5)}   (zeta^r in areal units per unit tide; zero crossing at zeta^r = {sp.N(sp.solve(k2_z, zr)[0], 5)})")
z0 = sp.solve(k2_z, zr)[0]
check("(3d) k2 is linear in zeta^r(R); its zero is at zeta^r = xi_RW|_(lambda=0) = -1.580, i.e. where the lattice-frame level set does not move at all (dbar = 0 -> no induced field -> the black hole) — the residual decides the sign", abs(float(z0) - float(xi_RW.subs(lam, 0))) < 1e-6 and sp.Poly(k2_z, zr).degree() == 1, f"zero at zeta^r = {float(z0):.4f}")
print(); print(f"3632 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
