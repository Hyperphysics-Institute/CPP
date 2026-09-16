"""4064 (EW lane) -- what U costs if its decoration points are additional GPs (founder ruling 16 Sep).
Measures the decoration's own nearest-neighbour spacing and coordination, against the core's 1/phi and z=12."""
import numpy as np, itertools, sys
sys.argv=['x']; import os; src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "4063_chiral_4d_cluster_z12.py")).read(); exec(src[src.index("import numpy"):src.index("\nR = 1.7")])
rng = np.random.default_rng(4063); R = 1.7
p = rng.normal(size=4); p = R * p / np.linalg.norm(p); O = orbit(p)
P = np.array(list(O.values())); n = len(P)
dmin = np.full(n, np.inf); z = np.zeros(n, int)
for i in range(n):
    d = np.linalg.norm(P - P[i], axis=1); d[i] = np.inf
    dmin[i] = d.min(); z[i] = int(np.sum(np.abs(d - d.min()) < 1e-6))
print(f"decoration GPs: {n}; nearest-neighbour spacing {dmin.min():.4f}..{dmin.max():.4f} (core edge 1/phi = {1/phi:.4f})")
print(f"ratio to core spacing: {dmin.min()/(1/phi):.3f}; coordination on the nearest shell: {sorted(set(z))}")
# a second random p to show the numbers are generic, not seed-specific
p2 = rng.normal(size=4); p2 = R * p2 / np.linalg.norm(p2); P2 = np.array(list(orbit(p2).values()))
d2 = min(np.min(np.delete(np.linalg.norm(P2 - P2[i], axis=1), i)) for i in range(0, n, 50))
print(f"second generic seed: spacing ~{d2:.4f}")
print(f"GP count per cell: core 120 + decoration {n} = {120+n}; density ratio {(120+n)/120:.0f}x")
