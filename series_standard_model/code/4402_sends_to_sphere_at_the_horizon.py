"""Patch 4402 -- founder (on 4401): the smaller PSR is the distance a GP SENDS to (it has received more SSV_abs
DI-bits from the mass side); the rule is the same for every mass; the densest packing on the 600-cell has 12 nearest
neighbours; ~10^30 GPs per Planck sphere at STP.

Part 1  what "2M" means: r = 2GM/c^2 (Schwarzschild radius), with numbers.
Part 2  core size if the CPs pack at the finest GP spacing (l_P/10^30, c01/GR-FE-1 read as a radius ratio) vs at
        Planck density (3703); both far inside 2M.
Part 3  a CP never outruns its Planck sphere's leading edge (R-CP-NO-REST-MASS), so its inward step is at most the
        inward reach.  With his sending sign the inward reach is 1 - beta:
          (A) shift follows beta = sqrt(2M/r) all the way: Moments to fall from 8M/3 to 2M + eps diverge (frozen layer);
          (B) shift capped at the floor value sqrt(3)/2 inside 8M/3 (AP-5): inward reach 0.134 per Moment, sideways 1/2
              (= 3703's matter clock 1/2); the CP reaches the centre in finite time.
"""
import numpy as np
from scipy.integrate import quad

G, c, Msun = 6.674e-11, 2.998e8, 1.989e30
lP, mP = 1.616e-35, 2.176e-8
print("Part 1: 2M = 2GM/c^2 (in units G = c = 1, 'M' is a length GM/c^2)")
for name, Ms in (("Sun", 1), ("Earth", 3.0e-6), ("62 Msun merger remnant", 62), ("Sgr A*", 4.3e6)):
    M = Ms*Msun
    print(f"  {name:24s}: M = GM/c^2 = {G*M/c**2:.3e} m, 2M = {2*G*M/c**2:.3e} m, 8M/3 = {8*G*M/(3*c**2):.3e} m")

print("\nPart 2: core radius for a 62 Msun black hole")
M = 62*Msun; r2M = 2*G*M/c**2
r_pl = lP*(3*(M/mP)/(4*np.pi))**(1/3)
print(f"  Planck density (3703):                      {r_pl:.1e} m  ({r_pl/r2M:.0e} of 2M)")
N_cp = 3*M/1.6726e-27     # CPs ~ a few per baryon, one per finest GP
for lab, s_ in (("radius-ratio reading (c01, 4168): spacing l_P/1e30", lP/1e30),
                ("count reading (GR-FE-1, founder): 1e30 per sphere, spacing l_P/1e10", lP/1e10)):
    rf = s_*(3*N_cp/(4*np.pi))**(1/3)
    print(f"  {lab:68s}: {rf:.1e} m ({rf/r2M:.0e} of 2M)")
print("  (a 12-neighbour packing on the 600-cell cannot alternate charges, 4370 section 3)")

print("\nPart 3: time for a CP to fall inward, its step <= the inward reach of its sending sphere (units of M, light speed 1)")
f = lambda r: 1/(1 - np.sqrt(2/r))
for eps in (1e-2, 1e-4, 1e-6, 1e-8):
    T, _ = quad(f, 2 + eps, 8/3, limit=200)
    print(f"  (A) from 8M/3 to 2M + {eps:g}M: {T:7.2f} M of time  (grows without bound as eps -> 0: logarithmic)")
b = np.sqrt(3)/2
print(f"  (B) shift capped at sqrt(3)/2 inside 8M/3: inward reach {1-b:.3f}, sideways {np.sqrt(1-b*b):.3f};")
print(f"      8M/3 to the centre takes {(8/3)/(1-b):.1f} M = {(8/3)/(1-b)*G*62*Msun/c**3*1e3:.1f} ms at 62 Msun"
      f" (3703 at c/2: {2*(8/3)*G*62*Msun/c**3*1e3:.1f} ms)")
print("      but the outward reach stays 1.866: whatever rides that sphere can get out from inside 2M")

print("\nPart 4: picture B on a flat grid: N = 1 with the shift held at sqrt(3)/2 inside 8M/3")
import sympy as sp
r = sp.symbols('r', positive=True)
m = sp.Rational(3, 8)*r        # v^2 = 2m/r = 3/4
rho = sp.diff(m, r)/(4*sp.pi*r**2)
print("  mass inside r: m(r) =", m, "-> energy density", sp.simplify(rho), "(spread as 1/r^2, radial pressure = -rho)")
print("  1 - 2m/r =", sp.simplify(1 - 2*m/r), "everywhere inside: no trapped surface, no horizon")
print("  -> either the interior is not Einstein's, or the mass is spread out rather than in a tiny core")

print("\nPart 5: picture A on a discrete grid: inward waves near 2M are squeezed by e^(-T/4M)")
for ell in (1e-45, 1e-65):
    Tc = 4*np.log(2*G*62*Msun/c**2/ell)       # in units of M
    echo = 8*np.log(G*62*Msun/c**2/ell)
    tM = G*62*Msun/c**3
    print(f"  finest spacing {ell:.0e} m: reaches it after ~{Tc:.0f} M ({Tc*tM:.2f} s at 62 Msun);"
          f" an echo from it would come ~{echo:.0f} M ({echo*tM:.2f} s) later")
print("  the ringdown is Einstein's only if the piled-up layer does not reflect; echoes are the test (none confirmed)")
