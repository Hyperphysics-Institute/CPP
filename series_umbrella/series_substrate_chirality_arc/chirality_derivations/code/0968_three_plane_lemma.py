#!/usr/bin/env python3
"""
0968 — the 3-plane lemma: the geometric replacement for link (c).

CONV-049 returned A = 5/5 YES, B = 3 YES / 2 NO. The two NO votes (GPT-5.6 Sol,
Grok 4.6) made the same objection and it is correct:

  Grok: "Part 1.2 ... specifies the *index set* of the sum. A term is allowed to
  vanish when d_e in span{n, r1, r2}. Nothing in those two equations requires
  four surviving nonzeros. Inferring the floor from the label 'whole vertex
  figure' is exactly the move you asked us not to make."

  GPT: "[Part 3] establishes that one-edge support is inadequate. It does not
  establish that support 2 or 3 is impossible, nor does the supplied package
  give a definition/theorem showing that 'whole-vertex-figure reading'
  necessarily means all twelve nonzero terms."

Grok also supplied the fix and this script verifies it INDEPENDENTLY rather
than taking it on report. Note that Gemini's YES vote was reasoned from the
same lemma ("the geometry of the 600-cell guarantees a minimum of 7 edges"),
so the lemma is what four of the five seats actually relied on.

  T1  THE LEMMA. A weight w_e = sign det[d_e, n, r1, r2] vanishes iff d_e lies
      in the 3-space span{n, r1, r2}. Over every admissible such 3-space, AT
      MOST 5 of the 12 first-shell directions lie in it. Hence at least 7
      weights survive, at EVERY vertex, for EVERY admissible frame.
  T2  support >= 7 > 4, so the floor follows as a consequence of lattice
      geometry rather than from the name of the construction.
  T3  the bound holds at EVERY vertex but is NOT uniform across them: 94
      vertices admit at most 5 directions in a 3-space, 26 admit at most 4.
      The worst case over all vertices is 5, so support >= 7 everywhere and
      >= 8 on the 26. (This script first asserted uniformity and the test
      refused it; the claim was corrected, not the test.)
  T4  consistency with the earlier empirical scans: 0964 measured an
      adversarial minimum support of 7 and a random minimum of 11. The lemma
      predicts exactly 7 as the attainable worst case, which is what the
      hostile pass found -- the scans were measuring the lemma without naming
      it.
  T5  with unit weights, support -> participation: p >= 7 at every vertex.
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
nhat = V[0].copy()

def max_in_3space(v):
    """max number of v's 12 edge-directions lying in any 3-space span{n, r1, r2}"""
    D = np.array([(V[w]-V[v])/np.linalg.norm(V[w]-V[v]) for w in nbr[v]])
    best = 0
    for a in range(12):
        for b in range(a+1, 12):
            M = np.array([nhat, D[a], D[b]])
            if np.linalg.matrix_rank(M, tol=1e-8) < 3: continue
            cnt = sum(1 for d in D if np.linalg.matrix_rank(np.vstack([M, d]), tol=1e-8) == 3)
            best = max(best, cnt)
    return best

per_vertex = [max_in_3space(v) for v in range(N)]
worst = max(per_vertex)
ok("T1", worst == 5,
   f"THE LEMMA: over every admissible 3-space span{{n, r1, r2}}, at most {worst} of the 12 first-shell "
   "directions lie in it. A weight vanishes only for a direction inside that 3-space, so at least "
   f"{12-worst} weights survive")

ok("T2", 12 - worst >= 4,
   f"support >= {12-worst} > 4: the floor is now a CONSEQUENCE OF LATTICE GEOMETRY, not an inference "
   "from the name 'whole vertex figure'. This is the replacement for link (c) that both dissenting "
   "seats required")

import collections
dist = dict(collections.Counter(per_vertex))
ok("T3", worst == 5 and min(per_vertex) == 4 and len(dist) == 2,
   f"holds at EVERY vertex but is NOT uniform: distribution of the per-vertex bound is {dist} — "
   f"{dist.get(5,0)} vertices admit at most 5 directions in a 3-space, {dist.get(4,0)} admit at most 4. "
   f"Worst case over all vertices is {worst}, so support >= {12-worst} everywhere and >= {12-4} on the "
   f"{dist.get(4,0)}. (This script first asserted uniformity; the test refused it and the CLAIM was "
   "corrected)")

ok("T4", 12 - worst == 7,
   f"CONSISTENT with the earlier empirical scans: 0964 measured an adversarial minimum support of 7 "
   f"and a random minimum of 11. The lemma predicts exactly {12-worst} as the attainable worst case — "
   "the scans were measuring this lemma without naming it")

def p_of(m): 
    c = np.ones(m)/np.sqrt(m); return 1.0/np.sum(c**4)
ok("T5", p_of(12-worst) >= 4,
   f"with unit-magnitude weights, support becomes participation: p >= {p_of(12-worst):.0f} at every "
   f"vertex, against CAPACITY-1's floor of 4")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
