#!/usr/bin/env python3
"""Patch 4396 -- founder: light IS the leading edge of the Planck sphere, so it always advances exactly one PSR
per Moment; the original conception (P-ORIGINAL-DIRECTIONAL-PSR, Patch 3607) is a different PSR radius in each
direction from each GP.

Test: let the fixed GP grid be the coordinate system, u = m/r the flat-harmonic census (r = grid radius),
light advance exactly one PSR per Moment in its direction, PSR_r (radial) and PSR_t (tangential) free.
Part 1: Schwarzschild in its areal (grid-circumference) form: PSR_r = 1 - 2u, PSR_t = sqrt(1 - 2u).
        Check clocks (radial and tangential light-crossing) and rulers; local light speed; isotropy.
Part 2: weak field and the founder's 4395 squeeze: PSR along V = PSR_t * PSR_t.
Part 3: light bending (numerical null geodesic in this metric) and the floor (PSR_t = 1/2).
Part 4: relation to the ratified R-PSR-LAW-LOG (written for the isotropic census eps).
"""
import numpy as np, sympy as sp
from scipy.integrate import solve_ivp
u, U, eps = sp.symbols('u U epsilon', positive=True)
PSR_r = 1 - 2*u
PSR_t = sp.sqrt(1 - 2*u)
print("Part 1: PSR_r = 1 - 2u, PSR_t = sqrt(1 - 2u); light = one PSR per Moment in its direction")
ruler_r = PSR_t          # a radial ruler of fixed proper length spans dr = L*sqrt(1-2u) of grid
ruler_t = sp.Integer(1)  # tangential rulers unchanged (grid circles have proper circumference 2 pi r)
clk_r = sp.simplify(PSR_r/ruler_r); clk_t = sp.simplify(PSR_t/ruler_t)
print("  clock from a radial light-crossing:", clk_r, " from a tangential one:", clk_t, " -> same: isotropic")
print("  local light speed, radial:", sp.simplify(PSR_r/(ruler_r*clk_r)), " tangential:", sp.simplify(PSR_t/(ruler_t*clk_t)))
print("  metric: g_tt = -PSR_t^2 =", -PSR_t**2, "; g_rr = 1/PSR_t^2 =", sp.simplify(1/PSR_t**2), "; g_angular = r^2")
print("  = Schwarzschild exactly, written on the fixed grid (areal coordinates).")

print("\nPart 2: weak field (u = U)")
print("  PSR_r =", sp.series(PSR_r.subs(u, U), U, 0, 2).removeO(), "; PSR_t =", sp.series(PSR_t.subs(u, U), U, 0, 2).removeO())
print("  clocks 1 - U; radial rulers 1 - U; tangential rulers 1; light 1 - 2U radially, 1 - U tangentially")
print("  squeeze rule (4395): PSR along V = PSR_t x PSR_t:", sp.simplify(PSR_t*PSR_t - PSR_r) == 0)

print("\nPart 3: light bending, numerical null geodesic in this metric (m = 1; a check: it is GR's orbit equation)")
def deflection(b, m=1.0):
    # orbit equation for Schwarzschild: d^2w/dphi^2 = -w + 3 m w^2, w = 1/r
    sol = solve_ivp(lambda p, y: [y[1], -y[0] + 3*m*y[0]**2], [0, np.pi + 1], [0.0, 1/b],
                    events=lambda p, y: y[0] if p > 0.1 else 1, rtol=1e-12, atol=1e-14, max_step=1e-3)
    return sol.t_events[0][0] - np.pi
for b in (1e4, 1e5):
    print(f"  b = {b:.0e} m: deflection {deflection(b):.4e}  vs 4m/b = {4/b:.4e}")
GM_c2, Rsun = 1476.6, 6.957e8
print(f"  Sun's limb: 4GM/(c^2 R) = {4*GM_c2/Rsun*206264.806:.3f} arcsec (the geodesic in this metric gives GR's value)")
floor = sp.solve(sp.Eq(PSR_t, sp.Rational(1, 2)), u)
print("  floor PSR_t = 1/2 at u =", floor, "-> r = 8m/3 (same as 3390 and 4385); PSR_r there =", PSR_r.subs(u, floor[0]))
print("  light ring r = 3m (u = 1/3) is outside the floor; horizon u = 1/2 lies inside it.")

print("\nPart 4: relation to R-PSR-LAW-LOG (written for the isotropic census eps = m/rho)")
u_eps = eps/(1 + eps/2)**2
print("  PSR_t in terms of eps:", sp.series(sp.sqrt(1 - 2*u_eps), eps, 0, 3).removeO(), " (= 1 - eps + eps^2/2: the ratified 1/2)")
print("  PSR_t in terms of the grid census u:", sp.series(PSR_t, u, 0, 3).removeO(), " (coefficient -1/2 in u)")
print("  -> the ratified law is the same physics; its 1/2 refers to the isotropic census.  If the grid is areal,")
print("     the census on the grid is u, and the law reads PSR_t = sqrt(1 - 2u).")

print("\nPart 5: oblique rays -- is the PSR ellipsoid (radii PSR_r, PSR_t) the coordinate null-cone section?")
th = sp.symbols('theta', real=True)
v = sp.symbols('v', positive=True)
# null condition: -(1-2u) dt^2 + dr^2/(1-2u) + r^2 dphi^2 = 0, with dr = v cos(th) dt, r dphi = v sin(th) dt
vnull = sp.solve(sp.Eq(-(1-2*u) + (v*sp.cos(th))**2/(1-2*u) + (v*sp.sin(th))**2, 0), v)[0]
# ellipse radius along angle th with semi-axes a = PSR_r (radial), b = PSR_t (tangential)
a_, b_ = PSR_r, PSR_t
vell = 1/sp.sqrt(sp.cos(th)**2/a_**2 + sp.sin(th)**2/b_**2)
for uv in (0.05, 0.2, 0.35):
    for tv in (0.3, 0.8, 1.2):
        d = float((vnull - vell).subs({u: uv, th: tv}))
        assert abs(d) < 1e-12
print("  null-cone speed = ellipse radius at every angle tested (u = 0.05, 0.2, 0.35; theta = 0.3, 0.8, 1.2): True")
print("\nNote: clocks and crystals following this geometry is the metric-universality premise (founder 4385"
      " 'same physics in every frame'), assumed, not derived here.")
