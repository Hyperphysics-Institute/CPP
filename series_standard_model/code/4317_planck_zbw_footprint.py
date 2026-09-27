#!/usr/bin/env python3
"""4317 -- (P'): the coherent footprint of one Planck-level ZBW on the icosahedral neighbourhood, against the
count-rule target G_P = 1/sqrt(alpha) = 11.706 (4313).

Inputs, each resolved against the lane that wrote it (D-7):
  * c04 Def. Level 1: one Planck ZBW = ONE DP (two CPs) oscillating at nu_P = 1/(2 t_P); a half-cycle is one Moment;
    energy per cycle E_P (the Planck-mass unit).  c04 eq. (spatial step): at most l_P of displacement per Moment.
  * 0733 / founders_vision (15 Jun 2026): l_P is the baseline PSR, NOT the GP spacing; R = PSR/s = 1e30 (GR-FE-1)
    or 1e32 (EU budget).
  * 4312/4313: a unit charge = one GP's (one CP's) emission; coupling quadratic per source; G_P = alpha^-1/2.
  * R-OUTWARD-FANOUT (founder, 14 Aug 2026): at every hop a GP's DI-bits split EQUALLY among all neighbours with a
    positive outward radial component, on the twelve icosahedral neighbours.
Candidate footprints are pre-registered below BEFORE any is compared with 11.706 (look-elsewhere guard)."""
import itertools
import numpy as np

alpha = 1/137.035999084
GP_target = alpha**-0.5
phi = (1+5**0.5)/2

# ---- 1. The 600-cell neighbourhood: build the 120 vertices, confirm 12 nearest neighbours forming an icosahedron.
def cell600():
    V = set()
    for s in itertools.product([-1, 1], repeat=4):
        V.add(tuple(0.5*x for x in s))
    for i in range(4):
        for s in [-1, 1]:
            v = [0.0]*4; v[i] = float(s); V.add(tuple(v))
    base = [phi/2, 0.5, 1/(2*phi), 0.0]
    even = [p for p in itertools.permutations(range(4))
            if sum(1 for a in range(4) for b in range(a+1, 4) if p[a] > p[b]) % 2 == 0]
    for p in even:
        for s in itertools.product([-1, 1], repeat=3):
            v = [0.0]*4; k = 0
            for j in range(4):
                val = base[p[j]]
                if val != 0: val *= s[k]; k += 1
                v[j] = val
            V.add(tuple(round(x, 12) for x in v))
    return np.array(sorted(V))

V = cell600()
d = np.linalg.norm(V[:, None]-V[None], axis=2)
edge = np.min(d[d > 1e-9])
nbr = np.where(np.abs(d[0]-edge) < 1e-9)[0]
print(f"600-cell: {len(V)} vertices; nearest neighbours of a vertex: {len(nbr)}; edge = {edge:.6f} (= 1/phi {1/phi:.6f})")
# tangent-space directions of the 12 neighbours (project out the vertex's own radial direction)
v0 = V[0]; T = V[nbr] - np.outer(V[nbr]@v0, v0)
# orthonormal basis of the 3-space perpendicular to v0
Q, _ = np.linalg.qr(np.column_stack([v0, np.eye(4)[:, :3]]))
B = Q[:, 1:4]
u = T@B; u /= np.linalg.norm(u, axis=1)[:, None]
G = u@u.T
angs = sorted(set(np.round(G[0], 6)))
print(f"tangent directions: pairwise cosines {angs}  (icosahedron: +-1/sqrt5 = {1/5**0.5:.6f}, -1, 1)")

# ---- 2. Outward-fanout recipient count (R-OUTWARD-FANOUT, equal shares), orientation-averaged.
rng = np.random.default_rng(4317)
dirs = rng.normal(size=(200000, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
cnt = ((dirs@u.T) > 0).sum(1)
print(f"outward recipients per hop (random direction): mean {cnt.mean():.4f}, values {sorted(set(cnt))}")
# equal shares -> effective recipient number (sum w)^2/sum w^2 equals the count itself
half = cnt.mean()

# ---- 3. Pre-registered candidate footprints (scale-free, corpus-defined objects only).
cands = [
    ("C1 the DP's two CPs (c04 Level 1 counts CPs)",                          2.0),
    ("C2 one GP's outward fan-out recipients (R-OUTWARD-FANOUT)",              half),
    ("C3 the twelve icosahedral neighbours",                                  12.0),
    ("C4 two CPs x outward fan-out recipients",                              2*half),
    ("C5 GP + its twelve neighbours",                                         13.0),
    ("C6 two CPs' GPs + both neighbourhoods (partners >> s apart, disjoint)", 26.0),
]
print(f"\ntarget G_P = 1/sqrt(alpha) = {GP_target:.4f}")
print(f"{'candidate':72s} {'G':>7s} {'G/G_P-1':>9s} {'alpha=1/G^2':>12s} {'alpha err':>9s}")
for name, g in cands:
    print(f"{name:72s} {g:7.3f} {100*(g/GP_target-1):+8.2f}% {'1/%.1f' % (g*g):>12s} {100*(1/(g*g)/alpha-1):+8.1f}%")
within = [n for n, g in cands if abs(g/GP_target-1) < 0.02]
print(f"candidates within 2% of 11.706: {len(within)}  (none reaches it; C3 and C4 land on 12 = 2 x 6: one icosahedral fact, not two)")

# ---- 4. The per-CP requirement implied by c04 Level 1 + 'charge = one GP'.
print(f"\nc04 Level 1 is ONE DP = TWO CPs; with charge = one CP's emission, each CP of a Planck-level DP must organise")
print(f"   G_P/2 = 1/(2 sqrt alpha) = {GP_target/2:.4f} GPs' emission; the outward half-shell is {half:.0f} ({100*(half/(GP_target/2)-1):+.2f}%).")

# ---- 4b. Normalisation: G_P is a RATIO (Planck unit's organised emission / a unit charge's).  Any rule that applies to
# every GP alike (fan-out, neighbour relay) inflates the charge unit by the same factor and cancels.
for name, per_cp in [("bare CP emission", 1.0), ("CP + outward fan-out recipients", 1+half), ("CP + 12 neighbours", 13.0)]:
    print(f"universal rule '{name}': Planck DP / unit charge = {2*per_cp:.0f}/{per_cp:.0f} = {2*per_cp/per_cp:.1f}"
          f"  (needs {GP_target:.3f})")
print("=> under any UNIVERSAL per-GP rule the ratio is the CP count, 2; 11.7 needs something the Planck ZBW does that a")
print("   static charge does not (C2-C6 as absolute counts silently assume the charge does NOT recruit its neighbours).")

# ---- 5. Scale audit: the ZBW's path during one half-cycle (one Moment) on the GP lattice.
for R, lab in [(1e30, "GR-FE-1"), (1e32, "EU budget")]:
    print(f"{lab:9s} R = PSR/s = {R:.0e}: a CP moving l_P per Moment crosses {R:.0e} GPs per half-cycle "
          f"({np.log10(R/GP_target):.1f} orders above 11.7); a path of 11.7 GPs needs v = {GP_target/R:.1e} c")
print("=> the in-step set cannot be the GPs the CP passes through at c; it must be a per-instant set, or the ZBW excursion")
print("   is ~one GP step (speed ~1e-29..1e-31 c), which c04's pass-through-at-top-speed does not state.")
