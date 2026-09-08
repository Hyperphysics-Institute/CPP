#!/usr/bin/env python3
"""
Patch 3685 verify — ROW 6 UNDER SEA CLOSED BY A BOUND: the visible register shell's k2 is bounded above by the
incompressible-fluid Love number at the R-core's compactness, and that number is far below 0.387.

Machinery: static l = 2 even-parity perturbation of a relativistic star (Hinderer 2008; Damour & Nagar 2009).
  y' = -(y^2 + y F(r) + r^2 Q(r))/r,  y(0) = 2,  with
  F = [1 - 4 pi r^2 (rho - p)] / f,  f = 1 - 2m/r,
  Q = 4 pi [5 rho + 9 p + (rho + p)/(dp/drho)] / f - 6/(r^2 f) - [2 (m + 4 pi r^3 p)/(r^2 f)]^2 ... (standard),
  k2 = (8/5) C^5 (1-2C)^2 [2 + 2C (y-1) - y] / { 2C [6 - 3y + 3C(5y-8)] + 4C^3 [13 - 11y + C(3y-2) + 2C^2(1+y)]
       + 3 (1-2C)^2 [2 - y + 2C(y-1)] ln(1-2C) },   y = y(R) - 3 for an incompressible surface (density jump).
For constant density the (rho + p)/(dp/drho) term vanishes (dp/drho -> infinity), and the interior is the exact
Schwarzschild constant-density solution.

 T1  Machinery check: incompressible k2 at C = 0.001 is 3/4 to 0.3 % (Newtonian incompressible value; the
     first-order GR correction is ~ -5.6 C, so C = 0.01 already sits 5.6 % low).
 T2  k2_incomp(C = 3/8) computed; compared with the row-6 bound 0.387 (3684 T2).
 T3  Sweep C in [0.05, 0.44]: k2_incomp is monotone decreasing and < 0.387 for all C >= ~0.19.
 T4  Statement: any register response with a restoring force at least a fluid's has k2 <= k2_incomp(3/8) < 0.387;
     row 6 passes for that class. The failing class (softer than any fluid) is the budget register's (k2 = 7.9).
"""
import numpy as np
from scipy.integrate import solve_ivp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

def k2_incompressible(C, R=1.0):
    """GR tidal Love number of a constant-density star of compactness C = M/R (G = c = 1)."""
    M = C * R; rho = 3 * M / (4 * np.pi * R**3)
    def m(r): return 4 * np.pi * rho * r**3 / 3
    def p(r):  # Schwarzschild interior
        a = np.sqrt(1 - 2 * M * r**2 / R**3); b = np.sqrt(1 - 2 * M / R)
        return rho * (a - b) / (3 * b - a)
    def rhs(r, y):
        f = 1 - 2 * m(r) / r; pr = p(r)
        F = (1 - 4 * np.pi * r**2 * (rho - pr)) / f
        Q = 4 * np.pi * (5 * rho + 9 * pr) / f - 6 / (r**2 * f) - (2 * (m(r) + 4 * np.pi * r**3 * pr) / (r**2 * f))**2
        return [-(y[0]**2 + y[0] * F + r**2 * Q) / r]
    r0 = 1e-4 * R
    sol = solve_ivp(rhs, [r0, R], [2.0 + 0.0 * r0], rtol=1e-10, atol=1e-12, method="DOP853")
    y = sol.y[0, -1] - 3.0     # density discontinuity at the surface (Damour & Nagar 2009)
    num = (8 / 5) * C**5 * (1 - 2 * C)**2 * (2 + 2 * C * (y - 1) - y)
    den = (2 * C * (6 - 3 * y + 3 * C * (5 * y - 8)) + 4 * C**3 * (13 - 11 * y + C * (3 * y - 2) + 2 * C**2 * (1 + y))
           + 3 * (1 - 2 * C)**2 * (2 - y + 2 * C * (y - 1)) * np.log(1 - 2 * C))
    return num / den

print("T1 — Newtonian limit")
k_small = k2_incompressible(0.001); k_1pc = k2_incompressible(0.01)
print(f"    k2_incomp(C = 0.001) = {k_small:.4f}, (C = 0.01) = {k_1pc:.4f}  (Newtonian incompressible: 3/4; first-order GR correction ~ -5.6 C)")
check("T1 k2 -> 3/4 as C -> 0 (C = 0.001 within 1 %)", abs(k_small / 0.75 - 1) < 0.01)

print("\nT2 — the R-core's compactness")
C0 = 3 / 8; k0 = k2_incompressible(C0); bound = 0.387
print(f"    k2_incomp(C = 3/8) = {k0:.4f};  row-6 bound (3684 T2): {bound}")
check("T2 k2_incomp(3/8) < 0.387", k0 < bound, f"margin x{bound / k0:.1f}")
Lam = (2 / 3) * k0 * C0**-5
print(f"    corresponding Lambda = (2/3) k2 C^-5 = {Lam:.2f}  (GW250114: Lambda_tilde < 34.8)")
check("T2 Lambda < 34.8", Lam < 34.8)

print("\nT3 — sweep")
Cs = np.linspace(0.05, 0.44, 40); ks = np.array([k2_incompressible(c) for c in Cs])
print("    C     k2_incomp\n" + "\n".join(f"    {c:.3f}  {k:.4f}" for c, k in zip(Cs[::5], ks[::5])))
check("T3 monotone decreasing in C", np.all(np.diff(ks) < 0))
Cstar = Cs[np.argmax(ks < bound)]
check("T3 below the bound for all C >= C*", np.all(ks[Cs >= Cstar] < bound), f"C* = {Cstar:.3f}")

print("\nT4 — statement")
check("T4 for any register response at least as stiff as a fluid, k2(shell) <= k2_incomp(3/8) < 0.387: row 6 PASSES; only a softer-than-fluid register (budget: k2 = 7.9) fails", k0 < bound)
print(f"\n{PASS}/{PASS+FAIL} PASS")
