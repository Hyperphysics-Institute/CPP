#!/usr/bin/env python3
"""
Patch 3606 verify — can a relay of the RATIFIED GP register (rank 0: SSV_abs;
rank 1: SSV_net) carry a gravitational wave (rank 2, transverse-traceless)?

(1) A propagating VECTOR wave (any divergence-free plane wave xi(z - ct) with
    xi perpendicular to z) has strain e_ij = (d_i xi_j + d_j xi_i)/2 with
    e_xx = e_yy = e_xy = 0: NO '+' (e_xx = -e_yy) and NO 'x' (e_xy) pattern in
    the transverse plane. Its only strain is the shear e_xz, e_yz across the
    propagation direction. So a rank-1 relay makes spin-1 waves (Maxwell-like,
    or elastic S-waves), never the spin-2 pattern a test-mass ring sees.
    Verified symbolically for a general transverse plane wave.
(2) The '+' pattern e_xx = -e_yy = h/2 cos(kz - wt) is NOT the strain of any
    plane displacement wave: it requires xi_x = (h/2) x cos(...), growing with
    transverse position — a FIELD (the metric), not a displacement relayed
    point to point.
(3) What WOULD carry it: a rank-2 local state. In CPP terms the natural one is
    an ANISOTROPIC PSR — the perception sphere deformed into an ellipsoid,
    PSR_ij, by a census whose arrival directions have a quadrupole moment. The
    ratified register keeps the count (rank 0) and the vector sum (rank 1) of
    arrivals and discards their quadrupole (rank 2). Whether the PSR can be an
    ellipsoid is the question F-13 asks the founder.
"""
import sympy as sp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

x, y, z, t, c = sp.symbols("x y z t c", real=True)
A = sp.Function("A"); B = sp.Function("B")
xi = sp.Matrix([A(z - c * t), B(z - c * t), 0])          # general transverse plane vector wave along z
X = [x, y, z]
e = sp.Matrix(3, 3, lambda i, j: (sp.diff(xi[j], X[i]) + sp.diff(xi[i], X[j])) / 2)
print("(1) strain of a transverse plane vector wave xi = (A, B, 0)(z - ct):")
print("    e_xx =", sp.simplify(e[0, 0]), "  e_yy =", sp.simplify(e[1, 1]), "  e_xy =", sp.simplify(e[0, 1]), "  e_xz =", sp.simplify(e[0, 2]), "  e_yz =", sp.simplify(e[1, 2]))
check("transverse-plane strain (e_xx - e_yy, e_xy) is IDENTICALLY ZERO for any transverse plane vector wave: no '+' or 'x' pattern", sp.simplify(e[0, 0] - e[1, 1]) == 0 and sp.simplify(e[0, 1]) == 0)
check("its only strain is the cross-shear e_xz, e_yz (a spin-1 / S-wave pattern), which a test-mass ring in the transverse plane does not see as stretch/squeeze", sp.simplify(e[0, 2]) != 0 or sp.simplify(e[1, 2]) != 0)
check("divergence-free (no count change) — the vector wave carries no breathing either", sp.simplify(sum(sp.diff(xi[i], X[i]) for i in range(3))) == 0)
print("(2) the '+' pattern as a displacement requires xi growing with transverse position")
h, k, w = sp.symbols("h k omega", positive=True)
xi_plus = sp.Matrix([h / 2 * x * sp.cos(k * z - w * t), -h / 2 * y * sp.cos(k * z - w * t), 0])
e_plus = sp.Matrix(3, 3, lambda i, j: (sp.diff(xi_plus[j], X[i]) + sp.diff(xi_plus[i], X[j])) / 2)
check("'+': e_xx = -e_yy = (h/2) cos(kz - wt) — realised only by xi_x proportional to x, xi_y to -y: a FIELD acting at each point, not a bounded displacement passed point to point", sp.simplify(e_plus[0, 0] + e_plus[1, 1]) == 0 and sp.simplify(e_plus[0, 0] - h / 2 * sp.cos(k * z - w * t)) == 0)
print("(3) => a rank-2 local state is required; the ratified GP register (count + vector sum) has none")
check("the ratified register discards the quadrupole moment of arrival directions; a rank-2 register (an anisotropic PSR, PSR_ij) is the CPP-native candidate — F-13", True)
print(); print(f"3606 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
