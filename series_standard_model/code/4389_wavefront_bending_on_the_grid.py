#!/usr/bin/env python3
"""Patch 4389 -- founder: light is carried on the GPs (the absolute frame) at one PSR per Moment; at the
Sun's limb the inner side of the wavefront sits in higher SSV_abs, so it advances fewer PSR-lengths per
Moment and lags; the wavefront turns and the photon bends.  "The question is how it is perceived."

Part 1: the wavefront (Huygens) bending for light speed v = 1 - k*U, U = GM/(r c^2): numerical ray
        integral at the solar limb; Shapiro delay coefficient.
Part 2: what the measured 1.75" fixes: k = 2 for LIGHT (speed per universal Moment, ~Earth time).
Part 3: with light 1 - 2U and clocks 1 - U (redshift), the settled-crystal rows of 4388, and the
        registered clock ruling (clock rate = PSR_eff/l_P) tested in lattice and in proper units.
"""
import numpy as np
from scipy.integrate import quad
GM_c2 = 1476.6            # m, Sun
Rsun = 6.957e8
rad2as = 206264.806
def deflection(k, b=Rsun):
    # wavefront turning: delta = -integral of d(ln n)/db along the straight path, n = 1/(1 - kU);
    # substitute x = b tan(t) so the integrand is smooth on (-pi/2, pi/2)
    def f(t):
        x = b*np.tan(t); r = np.hypot(x, b); U = GM_c2/r
        dU_db = -GM_c2*b/r**3
        return k*dU_db/(1 - k*U) * b/np.cos(t)**2
    val, _ = quad(f, -np.pi/2, np.pi/2, limit=200)
    return -val*rad2as
print("Part 1: inner side slower -> wavefront turns toward the Sun (founder's picture = refraction)")
for k in (1, 2):
    print(f"  light speed 1 - {k}U on the grid: bending at the limb = {deflection(k):.4f} arcsec;"
          f" Shapiro delay = {k}/2 of GR")
print("  GR: 4GM/(c^2 R_sun) = 1.751 arcsec; measured to agree (VLBI: gamma - 1 to a few x 1e-4; Cassini Shapiro gamma = 1 +/- 2.3e-5)")


print("\nPart 2: the data fix light's speed on the grid at 1 - 2U (per universal Moment).  They do not by")
print("  themselves fix the PSR: that depends on how many PSRs light advances per Moment.")

print("\nPart 3: rows (first order), light v = 1 - 2U, clock = v / crystal unless stated")
import sympy as sp
U = sp.symbols('U')
lin = lambda e: sp.expand(sp.series(e, U, 0, 2).removeO())
rows = [
 ("3 (4387 B): PSR 1-U; one-PSR steps, (1-U) steps per Moment; crystal = n PSRs", 1-U, (1-U), None),
 ("4 (3386):   PSR 1-2U; one PSR per Moment; crystal shrinks half as much",         (1-U)**2, (1-U), None),
 ("5:          PSR 1-2U; crystal absolute; clock as sqrt (assumed)",               (1-U)**2, sp.Integer(1), sp.sqrt(1-2*U)),
]
v = (1-U)**2
for lab, psr, crystal, clk in rows:
    clock = clk if clk is not None else v/crystal
    psr_proper = psr/crystal                      # PSR measured with the local crystal
    rule_lattice = sp.simplify(lin(psr) - lin(clock)) == 0
    rule_proper = sp.simplify(lin(psr_proper) - lin(clock)) == 0
    print(f"  {lab}\n     PSR(lattice) {lin(psr)}, crystal {lin(crystal)}, clock {lin(clock)}, "
          f"PSR(proper) {lin(psr_proper)}; clock ruling: lattice {rule_lattice}, proper {rule_proper}")
print("  -> row 5 fails the clock ruling in both unit systems (excluded); rows 3 and 4 each satisfy it in")
print("     one system: 3 in lattice units, 4 in proper units.  Units (4387 owed iv) and mechanism decide.")
