#!/usr/bin/env python3
"""4329 -- founder (founders_voice/4329): only the family-exclusion rule is specified; no stop criterion is.  Let the
empirics decide solid vs partly empty, if it matters.

Two questions, pressed:
 (A) Does the fill matter for alpha?  alpha = f PSR/(2L) (4328): f and L enter only as L/f, so alpha fixes L/f and no
     measurement of alpha can separate them.  What matters for LPI is only that f does NOT change in a well (saturation).
 (B) Does saturation depend on the unspecified stop criterion?  Two natural criteria, matching 4309's two readings of the
     PSR:  S1 PATH  -- stop once the summed path reaches P edges, on a family-free GP (4328's toy);
           S2 RADIUS -- stop once the distance from GP_origin reaches R, on a family-free GP.
     For each: the band fill as N grows, and the fill in a 'well' (the same N into a shell with P, R shrunk by 10%,
     i.e. fewer GPs).  Saturated means the fill no longer changes with N or with the well."""
import numpy as np
rng = np.random.default_rng(4329)
nb = np.array([(a, b, 0) for a in (1, -1) for b in (1, -1)] + [(a, 0, b) for a in (1, -1) for b in (1, -1)] +
              [(0, a, b) for a in (1, -1) for b in (1, -1)])
E = np.sqrt(2)

def volley(N, P, R, crit):
    pos = np.zeros((N, 3), int); path = np.zeros(N); done = np.zeros(N, bool)
    occ = {(0, 0, 0): N}
    while not done.all():
        for i in rng.permutation(np.where(~done)[0]):
            x = pos[i]
            out = [d for d in nb if np.dot(x + 0.0, d) > 0] if x.any() else list(nb)
            free = [d for d in out if occ.get(tuple(x + d), 0) == 0]
            cand = free if free else out
            d = cand[rng.integers(len(cand))]
            occ[tuple(x)] -= 1
            pos[i] = x + d; path[i] += E
            k = tuple(pos[i]); occ[k] = occ.get(k, 0) + 1
            reached = path[i] >= P if crit == "S1" else np.linalg.norm(pos[i]) >= R
            if reached and occ[k] == 1:
                done[i] = True
    r = np.linalg.norm(pos, axis=1)
    lo, hi = np.percentile(r, 10), np.percentile(r, 90)
    M = int(np.ceil(hi)) + 1
    g = np.array([(a, b, c) for a in range(-M, M+1) for b in range(-M, M+1) for c in range(-M, M+1) if (a+b+c) % 2 == 0])
    gr = np.linalg.norm(g, axis=1)
    fill = ((r >= lo) & (r <= hi)).sum()/((gr >= lo) & (gr <= hi)).sum()
    return fill, r.std()/r.mean()

P0 = 8*E; R0 = 0.7*P0
print(f"{'crit':>4s} {'N':>5s} {'fill':>6s} {'fill in well (P,R x0.9)':>24s} {'change':>8s} {'band rms':>9s}")
for crit in ["S1", "S2"]:
    for N in [200, 800, 2000]:
        f0, w0 = volley(N, P0, R0, crit)
        f1, _ = volley(N, 0.9*P0, 0.9*R0, crit)
        print(f"{crit:>4s} {N:5d} {f0:6.3f} {f1:24.3f} {f1-f0:+8.3f} {w0:9.3f}", flush=True)
print("Saturation (LPI-safe) = fill independent of N AND unchanged in the well.")
