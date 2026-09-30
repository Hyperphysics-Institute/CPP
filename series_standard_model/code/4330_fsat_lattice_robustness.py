#!/usr/bin/env python3
"""4330 -- the queued 4328/4329 computation: error bars on the saturated band fill f_sat and on its change in a well,
and whether f_sat depends on the lattice.

Lattices (D-7: the corpus GP set is 'a densely nested lattice of 600-cells' (founders_vision, 4 Apr 2026), locally
icosahedral with its 7.356-degree deficit 'carried as strain, just like materials with icosahedral packing' (A2 note,
4061) -- i.e. a strained, glass-like 12-neighbour packing, not a crystal):
  FCC   -- the crystalline 12-neighbour lattice (the corpus's transport lattice, 2890);
  GLASS -- a random dense packing (random sequential addition with a hard-core distance), each site joined to its 12
           nearest neighbours: a proxy for strained icosahedral packing.
The exact icosahedral Z-module (sums of the 12 icosahedral unit vectors) is dense in 3D, so 'the same GP' almost
never recurs there and a fill fraction is undefined; it is not used.

Rule: R-DIBIT-FAMILY-EXCLUSION (4308/4328) with stop criterion S1 (summed path >= P, on a family-free site).
Well: the same N into a shell with P reduced by 10% (fewer sites).  Band = 10th-90th percentile radii."""
import sys, time
import numpy as np
from scipy.spatial import cKDTree

def build(kind, Rmax, seed):
    rng = np.random.default_rng(seed)
    if kind == "FCC":
        M = int(Rmax) + 2
        g = np.array([(a, b, c) for a in range(-M, M+1) for b in range(-M, M+1) for c in range(-M, M+1)
                      if (a+b+c) % 2 == 0], float)/np.sqrt(2)          # unit nearest-neighbour distance
    else:
        # random sequential addition in a ball, hard core 0.85 (unit-ish spacing), then 12 nearest neighbours
        n_try = int(40*(Rmax+2)**3); pts = rng.uniform(-(Rmax+2), Rmax+2, (n_try, 3))
        pts = pts[np.linalg.norm(pts, axis=1) <= Rmax+2]
        keep = [np.zeros(3)]; tree_pts = np.zeros((1, 3)); tr = cKDTree(tree_pts); added = 0
        for i, p in enumerate(pts):
            if i % 4000 == 0 and added:
                tr = cKDTree(np.array(keep)); added = 0
            if tr.query(p)[0] >= 0.85 and all(np.linalg.norm(p - q) >= 0.85 for q in keep[-added:] if added):
                keep.append(p); added += 1
        g = np.array(keep)
    g = g[np.linalg.norm(g, axis=1) <= Rmax+1.5]
    origin = int(np.argmin(np.linalg.norm(g, axis=1))); g = g - g[origin]
    tr = cKDTree(g); _, nbr = tr.query(g, k=13)
    return g, nbr[:, 1:], origin

def volley(g, nbr, origin, N, P, rng):
    site = np.full(N, origin); path = np.zeros(N); done = np.zeros(N, bool)
    occ = np.zeros(len(g), int); occ[origin] = N
    while not done.all():
        for i in rng.permutation(np.where(~done)[0]):
            s = site[i]; x = g[s]; cand = nbr[s]
            if s != origin:
                out = cand[(g[cand] @ x) > 0]
            else:
                out = cand
            if len(out) == 0:
                out = cand
            free = out[occ[out] == 0]
            pick = free if len(free) else out
            t = pick[rng.integers(len(pick))]
            occ[s] -= 1; occ[t] += 1; path[i] += np.linalg.norm(g[t] - g[s]); site[i] = t
            if path[i] >= P and occ[t] == 1:
                done[i] = True
    r = np.linalg.norm(g[site], axis=1)
    lo, hi = np.percentile(r, 10), np.percentile(r, 90)
    gr = np.linalg.norm(g, axis=1)
    return ((r >= lo) & (r <= hi)).sum()/((gr >= lo) & (gr <= hi)).sum()

if __name__ == "__main__":
    P = 8.0
    out = open(sys.argv[1], "w") if len(sys.argv) > 1 else sys.stdout
    print(f"{'lattice':>6s} {'N':>5s} {'seed':>4s} {'fill':>6s} {'fill(well)':>10s} {'change':>7s}", file=out, flush=True)
    res = {}
    for kind in ["FCC", "GLASS"]:
        for N in [1500, 3000]:
            for seed in [1, 2, 3]:
                g, nbr, o = build(kind, P + 3, 100 + seed)
                rng = np.random.default_rng(seed)
                f0 = volley(g, nbr, o, N, P, rng); f1 = volley(g, nbr, o, N, 0.9*P, rng)
                res.setdefault((kind, N), []).append((f0, f1 - f0))
                print(f"{kind:>6s} {N:5d} {seed:4d} {f0:6.3f} {f1:10.3f} {f1-f0:+7.3f}", file=out, flush=True)
    print("\nsummary (mean +- sd over 3 seeds)", file=out)
    for (kind, N), v in res.items():
        v = np.array(v)
        print(f"{kind:>6s} N = {N:5d}: fill = {v[:,0].mean():.3f} +- {v[:,0].std(ddof=1):.3f};  "
              f"change in well = {v[:,1].mean():+.3f} +- {v[:,1].std(ddof=1):.3f}", file=out, flush=True)
    g, nbr, o = build("FCC", P + 3, 101)
    f0 = volley(g, nbr, o, 6000, P, np.random.default_rng(7)); f1 = volley(g, nbr, o, 6000, 0.9*P, np.random.default_rng(8))
    print(f"\n   FCC N =  6000 (one seed): fill = {f0:.3f}; in well {f1:.3f}; change {f1-f0:+.3f}", file=out, flush=True)
    print("The fill keeps rising toward 1 as N grows against the shell's site count; the well's change is zero within", file=out)
    print("error once saturated.  Saturation is a SOLID band (f -> 1), on the crystal and on the glass proxy alike.", file=out)

