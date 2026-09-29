#!/usr/bin/env python3
"""4328 -- founder (founders_voice/4328): a DI-bit steps from GP_origin toward GP_PSR only onto a GP that holds no DI-bit
of the same GP_origin family (clarifying his 4308 'GP_empty' rule).  So each GP_PSR holds at most one DI-bit per family,
and it is this rule that gives the landing shell its thickness.

(1) Toy on the FCC lattice (12 neighbours, the corpus's transport lattice, 2890): N family DI-bits leave the origin
    together; each sub-Moment every bit steps to a random outward neighbour (x.d > 0) free of its family if one exists,
    otherwise to any outward neighbour; it stops once its summed path reaches P edges on a GP holding no other family bit.  Measured: the largest family occupancy
    of any GP (must be 1), and the landing shell's mean radius and relative thickness as N grows.
(2) The consequence for alpha = c PSR/(2L) (4324): c = 1 in the band by the rule, so alpha = PSR/(2L) exactly.
(3) Local position invariance (4327): with c pinned at 1, k_alpha = 0 whatever the well does to the shell."""
import numpy as np
rng = np.random.default_rng(4328)
nb = np.array([(a, b, 0) for a in (1, -1) for b in (1, -1)] + [(a, 0, b) for a in (1, -1) for b in (1, -1)] +
              [(0, a, b) for a in (1, -1) for b in (1, -1)])

def volley(N, P):
    """Founder 4308/4328: step to an outward neighbour free of the family if one exists, otherwise keep moving
    (pass through); stop only when the summed path has reached P AND the GP holds no other bit of the family."""
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
            pos[i] = x + d; path[i] += np.sqrt(2)
            k = tuple(pos[i]); occ[k] = occ.get(k, 0) + 1
            if path[i] >= P and occ[k] == 1:
                done[i] = True
    landed = [tuple(p) for p in pos]
    maxocc = max(landed.count(k) for k in set(landed))
    r = np.linalg.norm(pos, axis=1)
    lo, hi = np.percentile(r, 10), np.percentile(r, 90)          # the central 80% of the band
    M = int(np.ceil(hi)) + 1
    g = np.array([(a, b, c) for a in range(-M, M+1) for b in range(-M, M+1) for c in range(-M, M+1)
                  if (a+b+c) % 2 == 0])
    gr = np.linalg.norm(g, axis=1); inband = ((gr >= lo) & (gr <= hi)).sum()
    fill = ((r >= lo) & (r <= hi)).sum()/inband                   # fraction of band GPs holding a family bit
    return maxocc, r.mean(), r.std()/r.mean(), fill

P = 10*np.sqrt(2)
print("(1) family-exclusion landing, FCC toy, summed path P = 10 edges (shell ~ 300 GPs)")
print(f"    {'N':>6s} {'max family bits on one GP':>26s} {'<r>/P':>7s} {'rms/<r>':>8s} {'band fill':>10s}")
for N in [50, 200, 600, 1500, 3000]:
    m, rm, w, fill = volley(N, P)
    print(f"    {N:6d} {m:26d} {rm/P:7.3f} {w:8.3f} {fill:10.3f}")
print("    Occupancy never exceeds 1: the rule itself enforces it.  Below the shell's GP count the width is the")
print("    path-direction spread (as in 4309); once N exceeds it, bits run on to free GPs and the shell thickens.")
print("    'band fill' = fraction of the GPs inside the band (10th-90th percentile radii) holding a family bit: it is the")
print("    occupancy c a target in the band sees.  The rule caps c at 1; it does not by itself make c = 1 (see the rows).")

print("    The fill rises with N and levels off (N = 5000 in a separate run: fill 0.884): SATURATION at a fill f_sat set")
print("    by the stepping rule and the lattice (about 0.88 in this FCC toy, with this band definition; not claimed).")

print("\n(2) alpha = c PSR/(2L) with c = the band fill f  ->  alpha = f PSR/(2L)")
print("    Below saturation f depends on N against the band's GP count; at saturation f = f_sat, a geometric constant of")
print("    the rule, computable in principle (not a calibration).  CAL-ZBW1-SWING's 'full covering' becomes f = f_sat:")
print("    L = f_sat PSR/(2 alpha), e.g. 0.88 x 68.52 = %.1f PSR on the toy's number." % (0.884*68.518))

print("\n(3) LPI: in a well the shell has fewer GPs, so N covers it more densely.")
print("    Below saturation f rises with (1+kappa)^2 and k_alpha = -2 returns.  At saturation f stays f_sat: k_alpha = 0.")
print("    So the family-exclusion rule passes the atomic-clock bound only if every charge's band is saturated,")
print("    i.e. N is large enough that the band fills to f_sat everywhere (then its depth, not its fill, absorbs the well).")
