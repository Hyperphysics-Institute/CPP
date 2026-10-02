#!/usr/bin/env python3
"""Patch 4370 - the founder's black-hole interior picture (2 Oct 2026): PSR overlap, the halt when each CP
has 6 opposite-charge neighbours at PSR distance with V_i cancelling.

  1. Can the overlap change the ringdown/shadow?  The photon sphere lies in the vacuum exterior, whose
     census is u = C2/r fixed by the enclosed total (GR-1j T-2, exact).  Compare the photon sphere with
     the matter's outer edge under each corpus picture.
  2. "Every neighbour of opposite charge" (founder 4358, alternating +/- lattice) is a 2-colouring of the
     neighbour graph: possible only if the graph has no odd cycles.  Check triangles in simple-cubic
     (z = 6, the founder's count), FCC (z = 12) and the 600-cell vertex graph (z = 12).
"""
import itertools
import numpy as np
print(__doc__)

# 1. photon sphere vs matter edge (areal radii in units of m)
print("1. Photon sphere vs where matter sits (areal radius / m):")
ph_exp = (2.0) * np.exp(0.5)          # isotropic r = 2m -> areal r e^{m/r} = 2 e^{1/2}
cap = (1 / np.log(2)) * np.exp(np.log(2))
for name, val in (("photon sphere, GR", 3.0), ("photon sphere, exponential exterior", ph_exp),
                  ("STOP surface (3390, held)", 8 / 3), ("cap at eps = ln 2 (4369 reading)", cap),
                  ("DRAIN core (3703)", 0.0)):
    print(f"   {name:38s} {val:7.4f}")
print("   Every matter edge lies inside the photon sphere, so the ringdown and shadow are set by the vacuum")
print("   exterior: by the total census and the SSV_abs -> PSR curve only. Overlap inside the matter adds")
print("   linearly to the census (two CPs = twice the stress), which the count already contains; it can change")
print("   the interior and the total, not the exterior curve's shape.")

# 2. odd cycles
def triangles(points, d, tol=1e-6):
    P = np.array(points, float)
    n = len(P)
    D = np.linalg.norm(P[:, None, :] - P[None, :, :], axis=-1)
    A = (np.abs(D - d) < tol)
    z = A.sum(1)
    tri = int(np.trace(np.linalg.matrix_power(A.astype(np.int64), 3)) // 6)
    return int(z.max()), tri          # interior coordination (edge points of a finite grid have fewer)

g = range(-2, 3)
sc = [p for p in itertools.product(g, g, g)]
fcc = [p for p in itertools.product(g, g, g) if sum(p) % 2 == 0]
phi = (1 + 5 ** 0.5) / 2
v600 = set()
for i in range(4):
    for s in (1, -1):
        e = [0, 0, 0, 0]; e[i] = s; v600.add(tuple(e))
for s in itertools.product((0.5, -0.5), repeat=4):
    v600.add(s)
even = [p for p in itertools.permutations(range(4))
        if sum(1 for a in range(4) for b in range(a + 1, 4) if p[a] > p[b]) % 2 == 0]
base = (phi / 2, 0.5, 1 / (2 * phi), 0.0)
for sg in itertools.product((1, -1), repeat=3):
    b = (sg[0] * base[0], sg[1] * base[1], sg[2] * base[2], 0.0)
    for p in even:
        v600.add(tuple(round(b[p[k]], 12) + 0.0 for k in range(4)))
v600 = list(v600)
print(f"\n2. Neighbour graphs (interior coordination z, triangle count):")
for name, pts, d in (("simple cubic (z = 6)", sc, 1.0), ("FCC (z = 12)", fcc, 2 ** 0.5),
                     (f"600-cell vertices ({len(v600)})", v600, 1 / phi)):
    z, t = triangles(pts, d)
    verdict = "bipartite-compatible: an alternating +/- lattice is possible" if t == 0 else \
        "contains triangles: every neighbour opposite is impossible"
    print(f"   {name:24s} z = {z:2d}, triangles = {t:5d}  -> {verdict}")
print("   The founder's 6 opposite-charge neighbours is exactly the coordination at which his 4358")
print("   alternating lattice can exist (the rock-salt arrangement); a 12-neighbour packing cannot alternate.")
