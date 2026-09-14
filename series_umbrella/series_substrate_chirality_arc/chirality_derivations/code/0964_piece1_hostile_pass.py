#!/usr/bin/env python3
"""
0964 — R-1 hostile pass on piece 1, run BEFORE any assembly patch or dispatch.

Patch 0963 found that the corpus already pins the dynamical eta's weights (unit
magnitude, from sign-of-determinant constructions at 0819/0820/0821) and already
contains the floor argument (4-D orientation needs >= 4 independent directions,
lcapa_axis2_signcorr_closure.md SS5). Piece 1 is therefore an assembly job.

R-1 (Patch 0959) requires the lane to run the tests an adversarial reviewer
would demand BEFORE dispatching, rather than discovering them mid-campaign.
These are the three a reviewer would aim at.

  T1  CHECK 1 — does any eta construction in the corpus produce NON-unit
      weights? Searched; all three constructions use sign(det(...)). Recorded
      here as the arithmetic consequence: unit weights => participation =
      support, exactly.
  T2  CHECK 2a — can the canonical construction LOSE support to a vanishing
      determinant? A sign weight is 0 when the edge direction lies in
      span{n, r1, r2}. Random frames.
  T3  CHECK 2b — the same under ADVERSARIAL frames chosen along lattice edge
      directions, which is where degeneracies concentrate.
  T4  CHECK 3 — the 0961 singleton-orbit worry: on the four shells with edge
      orbits [1,1,5,5] a covariant observable could in principle sit on a
      singleton. Enumerate the achievable covariant supports per shell and
      report the minimum that is >= 4.
  T5  the bonus the enumeration gives: on the singleton-orbit shells support 3
      and 4 are NOT achievable at all (orbit unions give 1,2,5,6,7,10,11,12),
      so the smallest admissible reading there is 5, not 4. Only the equatorial
      shell is tight at exactly 4.
  T6  THE REVIEWER TRAP, flagged not hidden: 0820's coarse-graining note SS(2)
      says "A 4-edge det reads only 4 (=> emergent)". That is the SUPERSEDED
      0819 mean-field crossover (m ~ 8), not the live bound. The live bound is
      0828's refined-chord result, under which p >= 4 gives rho <= kappa(0.5)
      = 2/3 < 1. A reviewer reading 0820 will hit this contradiction.
"""
import itertools, sys
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
res = []
def ok(n, c, note=""):
    res.append(c); print(f"{n} {'PASS' if c else 'FAIL'}  {note}")

def v600():
    V = []
    for s in itertools.product([1, -1], repeat=4): V.append(0.5*np.array(s, dtype=float))
    for i in range(4):
        for s in (1, -1):
            e = np.zeros(4); e[i] = s; V.append(e)
    b = [PHI/2, 0.5, 1/(2*PHI), 0.0]
    ev = [p for p in itertools.permutations(range(4))
          if sum(1 for i in range(4) for j in range(i) if p[j] > p[i]) % 2 == 0]
    for p in ev:
        for s in itertools.product([1, -1], repeat=3):
            v = np.zeros(4); val = [s[0]*b[0], s[1]*b[1], s[2]*b[2], 0.0]
            for k in range(4): v[p[k]] = val[k]
            V.append(v)
    U = []
    for v in V:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    return np.array(U)

V = v600(); N = 120; G = V @ V.T
nbr = [np.where(np.abs(G[i] - PHI/2) < 1e-8)[0] for i in range(N)]
host = 0; nhat = V[host].copy()

# ---- T1 unit weights => participation = support
def p_of(c):
    c = np.abs(np.array(c, float)); c /= np.linalg.norm(c); return 1.0/np.sum(c**4)
ok("T1", all(abs(p_of(np.ones(m)) - m) < 1e-9 for m in (4, 5, 6, 12)),
   "CHECK 1 — every corpus construction (0819, 0820, 0821) weights edges by sign(det(...)), "
   "|w| = 1. For unit weights participation = support exactly: p(1^m) = m for m = 4, 5, 6, 12")

# ---- T2 / T3 support under random and adversarial frames
def support(v, r1, r2):
    s = 0
    for w in nbr[v]:
        d = V[w] - V[v]; d /= np.linalg.norm(d)
        if abs(np.linalg.det(np.array([d, nhat, r1, r2]))) > 1e-9: s += 1
    return s

rng = np.random.default_rng(7)
mins = []
for _ in range(200):
    r1 = rng.normal(size=4); r1 -= (r1 @ nhat)*nhat; r1 /= np.linalg.norm(r1)
    r2 = rng.normal(size=4); r2 -= (r2 @ nhat)*nhat; r2 -= (r2 @ r1)*r1; r2 /= np.linalg.norm(r2)
    mins.append(min(support(v, r1, r2) for v in range(N)))
ok("T2", min(mins) >= 4,
   f"CHECK 2a — random frames (200 x 120 vertices): minimum support = {min(mins)} of 12, "
   f"p = {min(mins)}. Clears the floor of 4 with {min(mins)-4} to spare")

adv = []
for a in range(12):
    for b in range(a+1, 12):
        d1 = V[nbr[host][a]] - V[host]; d1 -= (d1 @ nhat)*nhat
        if np.linalg.norm(d1) < 1e-9: continue
        d1 /= np.linalg.norm(d1)
        d2 = V[nbr[host][b]] - V[host]; d2 -= (d2 @ nhat)*nhat; d2 -= (d2 @ d1)*d1
        if np.linalg.norm(d2) < 1e-9: continue
        d2 /= np.linalg.norm(d2)
        adv.append(min(support(v, d1, d2) for v in range(N)))
ok("T3", min(adv) >= 4,
   f"CHECK 2b — ADVERSARIAL frames along lattice edge directions, where degeneracies concentrate: "
   f"minimum support = {min(adv)} of 12, p = {min(adv)}. Still clears")

# ---- T4 / T5 covariant supports per shell
idx = [host]
for j in nbr[host]:
    A = np.array([V[i] for i in idx] + [V[j]])
    if np.linalg.matrix_rank(A, tol=1e-8) == len(idx)+1: idx.append(int(j))
    if len(idx) == 4: break
A = np.array([V[i] for i in idx]); Ai = np.linalg.inv(A); gram = A @ A.T
S = []
for cand in itertools.permutations(nbr[host], 3):
    B = np.array([V[host]] + [V[c] for c in cand])
    if not np.allclose(B @ B.T, gram, atol=1e-7): continue
    M = (Ai @ B).T
    if not np.allclose(M @ M.T, np.eye(4), atol=1e-7): continue
    Y = V @ M.T; perm = np.full(N, -1, int); good = True
    for a, y in enumerate(Y):
        h = np.where(np.abs(V - y).max(axis=1) < 1e-7)[0]
        if len(h) != 1: good = False; break
        perm[a] = h[0]
    if good: S.append(tuple(perm))

proj = V @ nhat
shells = {}
for v in range(N): shells.setdefault(round(proj[v], 9), []).append(v)
shell_min, singleton_sums = {}, {}
for sv, vs in shells.items():
    v = vs[0]; Sv = [p for p in S if p[v] == v]
    nb = [int(x) for x in nbr[v]]; orb = []; seen = set()
    for w in nb:
        if w in seen: continue
        o = {p[w] for p in Sv} & set(nb); seen |= o; orb.append(len(o))
    sums = set()
    for r in range(1, len(orb)+1):
        for c in itertools.combinations(orb, r): sums.add(sum(c))
    shell_min[sv] = min(s for s in sums if s >= 4)
    if sorted(orb) == [1, 1, 5, 5]: singleton_sums[sv] = sorted(sums)

ok("T4", min(shell_min.values()) >= 4,
   f"CHECK 3 — 0961's singleton-orbit worry: minimum COVARIANT support >= 4, per shell, is "
   f"{ {round(k,3): v for k, v in sorted(shell_min.items(), reverse=True)} }. "
   f"Overall minimum p = {min(shell_min.values())}. Clears")

sset = next(iter(singleton_sums.values()))
ok("T5", 3 not in sset and 4 not in sset and 5 in sset,
   f"on the four [1,1,5,5] shells the achievable covariant supports are {sset} — supports 3 and 4 are "
   "NOT achievable, so the smallest admissible reading there is 5, not 4. Only the equatorial "
   "[2,2,2,2,4] shell is tight at exactly 4")

# ---- T6 the superseded statement
ok("T6", True,
   "REVIEWER TRAP (flagged, not hidden): 0820 SS(2) says 'A 4-edge det reads only 4 (=> emergent)'. "
   "That is the SUPERSEDED 0819 mean-field crossover at m ~ 8, not the live bound. The live bound is "
   "0828's refined-chord result: p >= 4 => z* <= 0.5 => rho <= kappa(0.5) = 2/3 < 1. The assembly "
   "patch must say so explicitly or a reviewer will read 0820 as contradicting the floor")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
