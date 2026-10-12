"""Patch 4401 -- founder retracts STOP (4400): no force opposes the SSV_abs gradient inside, so the CPs fall to the
finest GP spacing and fill the innermost GPs at the ultimate density, without superposing (ZBW force gradient).
The core is tiny and the space outside it is empty: DRAIN (3703), with 4370's six-neighbour Planck-density end state.

Checks:
Part 1  size of the core at one CP per Planck volume (order of magnitude), against 2M.
Part 2  with the mass inside 2M, the empty space outside is Schwarzschild down to the core; the shift
        beta = sqrt(2M/r) reaches 1 at r = 2M and exceeds it inside.
Part 3  the sign: reaches of a unit Planck sphere shifted by beta
          his 4398 sign (shortest TOWARD the mass, centre displaced outward): toward 1 - beta, away 1 + beta
          the draining sign (centre displaced inward, carried with the falling sea): toward 1 + beta, away 1 - beta
        At r = 2M the first can no longer reach inward (nothing can fall in: a white hole); the second can no longer
        reach outward (nothing gets out; everything inside falls to the core: a black hole).
Part 4  the field equations on a flat grid see only v^2, so in Einstein's terms the sign could flip outside 2M without
        matter (a jump in the time slicing); at 2M the draining sign is required.
"""
import numpy as np
import sympy as sp

G, c, hbar, Msun = 6.674e-11, 2.998e8, 1.055e-34, 1.989e30
lP = np.sqrt(hbar*G/c**3); mP = np.sqrt(hbar*c/G)
print("Part 1: core radius, packed at one unit per Planck volume, r = l_P (3N/4pi)^(1/3)")
mp_baryon = 1.6726e-27
for Ms in (10, 62, 4.3e6):
    M = Ms*Msun; r2M = 2*G*M/c**2
    N_pl = M/mP                              # Planck density: each unit carries ~ one Planck mass
    N_cp = 3*M/mp_baryon                     # CP count ~ a few per baryon (3 used here)
    for lab, N in (("Planck density", N_pl), ("one CP per Planck volume", N_cp)):
        rc = lP*(3*N/(4*np.pi))**(1/3)
        print(f"  M = {Ms:g} Msun, {lab:26s}: radius ~ {rc:.1e} m, 2M = {r2M:.1e} m, ratio {rc/r2M:.0e}")
print("  (3703: radius ~1.8e-22 m at 62 Msun on the Planck-density count; either way the core is far inside 2M;")
print("   the packing (R-EXCL-RETIRED, spacing at the PSR floor) changes only an order-one factor)")

print("\nPart 2-3: reaches per Moment of a unit Planck sphere, mass inside 2M (M = 1)")
print("   r     beta    his sign: toward  away   |  draining sign: toward  away")
for r in (8/3, 2.4, 2.1, 2.0, 1.5):
    b = np.sqrt(2/r)
    print(f"  {r:4.2f}  {b:5.3f}        {1-b:+6.3f}  {1+b:6.3f}   |              {1+b:6.3f}  {1-b:+6.3f}")
print("  his sign: at r = 2M the inward reach is 0, inside it negative: nothing can move inward -> no drain")
print("  draining sign: at r = 2M the outward reach is 0, inside it negative: everything falls to the core")
print("  outside 2M both signs give identical round-trip and static measurements (4397); one-way times under")
print("  universal Moments differ, and the ringdown needs the absorbing horizon, i.e. the draining sign at 2M")
print("  receiver reading: the sphere a GP LISTENS from (points whose broadcasts reach it in one Moment) is, in the")
print("  draining chart, 1 - beta toward the mass and 1 + beta away: shortest toward the mass, his shape")

print("\nPart 4: can the sign flip somewhere outside 2M?")
print("  With N = 1 the field equations on a flat grid depend on v only through v^2:")
print("    G^t_t = G^r_r = -(r v^2)'/r^2,  G^th_th = -[ d/dr( r (v^2)' ) + (v^2)' ] / (2r)   (sympy, 4398 machinery)")
print("  so v = +sqrt(2M/r) and v = -sqrt(2M/r) are both empty space, and a flip at some r0 > 2M needs no matter in")
print("  Einstein's terms: it is a crease in the time slicing (one-way coordinate speeds jump), not a source.")
print("  At r = 2M itself the two signs cannot be joined (one reach is zero on each side), so the drain needs the")
print("  draining sign at and near 2M.  Far out, the sign is fixed by neither the data nor the field equations;")
print("  in CPP a flip would be an abrupt reversal of the Planck sphere's displacement in empty space, with no cause.")
