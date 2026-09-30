#!/usr/bin/env python3
"""4353 -- the founder's DI-bit landing protocol (founders_voice/4353), tested on the 4330 lattices.

PROTOCOL F (founder, 30 Sep 2026): in each submoment of the displace phase 12 DI-bits leave GP_origin toward GP_PSR.
A DI-bit that reaches its GP_PSR stops and occupies it. If its GP_PSR is already occupied by a bit of the same
GP_origin family, it moves inward and occupies the most radial free position in its set of GPs.
Implementation: each bit gets a direction u (12 per submoment: the 12 icosahedral directions under a random rotation);
its "set of GPs" is the lattice sites within perpendicular distance w of its ray; it takes the free site of that set
with the largest radius <= P (w is widened by 0.25 if the set is exhausted).
PROTOCOL F2 (F with the blocked bit's "set of GPs" read as the neighbourhood of its GP_PSR, searched hop by hop).
PROTOCOL S (simpler, order-free): the family occupies the N free sites of largest radius <= P.

Measures: band [r_in, P] with r_in the smallest occupied radius; fill = occupied/available sites in the band; holes;
outer edge; and the same N in a well (P -> 0.9 P, the PSR shrinks; lattice fixed).  Lattices as in 4330 (FCC; GLASS =
random dense packing with hard core 0.85)."""
import sys, importlib, os
import numpy as np
from scipy.spatial import cKDTree
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
lat = importlib.import_module('4330_fsat_lattice_robustness')

PHI = (1 + 5 ** 0.5) / 2
ICO = np.array([(0, s1, s2 * PHI) for s1 in (1, -1) for s2 in (1, -1)] + [(s1, s2 * PHI, 0) for s1 in (1, -1) for s2 in (1, -1)]
               + [(s2 * PHI, 0, s1) for s1 in (1, -1) for s2 in (1, -1)], float)
ICO /= np.linalg.norm(ICO, axis=1)[:, None]

def rand_rot(rng):
    q = rng.normal(size=4); q /= np.linalg.norm(q); a, b, c, d = q
    return np.array([[a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c)], [2*(b*c+a*d), a*a-b*b+c*c-d*d, 2*(c*d-a*b)],
                     [2*(b*d-a*c), 2*(c*d+a*b), a*a-b*b-c*c+d*d]])

def protocol_F(g, r, N, P, rng, w0=0.6):
    occ = np.zeros(len(g), bool); occ[np.argmin(r)] = True          # origin itself not a landing site
    inside = np.where(r <= P + 1e-9)[0]; gi = g[inside]; ri = r[inside]
    landed = []
    while len(landed) < N:
        U = ICO @ rand_rot(rng).T
        for u in U:
            if len(landed) >= N: break
            w = w0
            while True:
                along = gi @ u; perp = np.linalg.norm(gi - np.outer(along, u), axis=1)
                cand = np.where((along > 0) & (perp <= w) & ~occ[inside])[0]
                if len(cand):
                    k = inside[cand[np.argmax(ri[cand])]]; occ[k] = True; landed.append(k); break
                w += 0.25
                if w > P: return np.array(landed)                      # ball full
    return np.array(landed)

def protocol_F2(g, r, nbr, N, P, rng):
    """F with the 'set of GPs' read as the neighbourhood of the blocked GP_PSR: search outward in lattice hops from
    the target; in the first hop-ring holding any free site (radius <= P), take the most radial one."""
    occ = np.zeros(len(g), bool); occ[np.argmin(r)] = True
    ok = r <= P + 1e-9; tr = cKDTree(g); landed = []
    while len(landed) < N:
        for u in ICO @ rand_rot(rng).T:
            if len(landed) >= N: break
            _, t = tr.query(P * u)
            while r[t] > P + 1e-9:                                         # step to an in-ball neighbour
                t = nbr[t][np.argmin(r[nbr[t]])]
            ring, seen = [t], {t}
            while True:
                free = [k for k in ring if ok[k] and not occ[k]]
                if free:
                    k = max(free, key=lambda k: r[k]); occ[k] = True; landed.append(k); break
                nxt = []
                for a in ring:
                    for b in nbr[a]:
                        if b not in seen and ok[b]: seen.add(b); nxt.append(b)
                if not nxt: return np.array(landed)
                ring = nxt
    return np.array(landed)

def protocol_S(r, N, P):
    idx = np.where((r <= P + 1e-9) & (r > 1e-9))[0]
    return idx[np.argsort(-r[idx])][:N]

def band(r, landed, P):
    rin = r[landed].min(); avail = ((r >= rin - 1e-9) & (r <= P + 1e-9)).sum()
    return rin, r[landed].max(), len(landed) / avail, avail - len(landed)

if __name__ == "__main__":
    for kind in ("FCC", "GLASS"):
        for P in (8.0, 12.0):
            g, nbr, o = lat.build(kind, P + 2, 7); g = g - g[o]; r = np.linalg.norm(g, axis=1)
            shell_sites = ((r <= P) & (r > P - 1)).sum()
            for frac in (0.5, 1.5, 3.0):
                N = int(frac * shell_sites)
                rows = []
                for PP in (P, 0.9 * P):
                    LF = protocol_F(g, r, N, PP, np.random.default_rng(1)); LS = protocol_S(r, N, PP)
                    L2 = protocol_F2(g, r, nbr, N, PP, np.random.default_rng(1))
                    rows.append((band(r, LF, PP), band(r, LS, PP), band(r, L2, PP)))
                (fF, fS, f2), (wF, wS, w2) = rows
                print(f"{kind:5s} P={P:4.1f} N={N:5d} ({frac:.1f} x outer-shell sites) | F: band [{fF[0]:.2f},{fF[1]:.2f}] "
                      f"fill {fF[2]:.3f} holes {fF[3]:3d}  well: [{wF[0]:.2f},{wF[1]:.2f}] fill {wF[2]:.3f} | "
                      f"F2: [{f2[0]:.2f},{f2[1]:.2f}] fill {f2[2]:.3f} holes {f2[3]} well [{w2[0]:.2f},{w2[1]:.2f}] fill {w2[2]:.3f} | "
                      f"S: fill {fS[2]:.3f} holes {fS[3]} well fill {wS[2]:.3f}", flush=True)
