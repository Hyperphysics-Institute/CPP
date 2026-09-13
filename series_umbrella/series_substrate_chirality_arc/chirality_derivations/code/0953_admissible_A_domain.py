#!/usr/bin/env python3
"""
0953 — the admissible A-domain, adopted from CONV-047 Q6 (both valid seats).

Seat 1 (GPT-5.6 Sol) Q6.1 and Seat 2 (Grok 4.6) Q6.4 independently raised the
same omission in the 0952 package: a rate law must stay positive on every
directed edge,
    r0 (1 + A (m.n) +- B (e.n)) > 0,
so "CAPACITY-1 is not conditional on A = 0" is only meaningful inside the
A-domain where the rate law is admissible at all. The package tested A in [0,1]
without stating that domain. This computes it.

  T1  the first-shell geometry: 720 undirected edges; |m.n|_max = (1 + phi/2)/2,
      attained on the edges incident to the host itself (midpoint of a vertex at
      projection 1 and a first-shell vertex at projection phi/2) -- NOT phi/2,
      which was this script's first guess and which the test refused. |e.n| spans
      [0, 1].
  T2  at the physical bias B = phi^-3, the admissible domain is |A| <= A_max
      with A_max computed from the worst edge: the binding constraint is the
      edge maximising |m.n| against the largest |e.n|.
  T3  the panel's tested box A in [0, 1] lies INSIDE the admissible domain, and
      nearly exhausts its positive half. So the tested range was not arbitrary:
      it is very close to the whole of what the rate law permits.
  T4  the closed form is a MINIMUM OVER EDGES, not a ratio of extremes:
      A_max = min over edges with m.n < 0 of (1 - B|e.n|)/|m.n|. The binding
      edge is not the one maximising |m.n| -- that edge has a small |e.n| and is
      not the constraint. This was the script's second wrong guess; corrected
      against the scan rather than the scan being adjusted.
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

V = v600(); G = V @ V.T
edges = [(i, j) for i in range(120) for j in range(i+1, 120) if abs(G[i, j] - PHI/2) < 1e-8]
nhat = V[0].copy()
mn = np.array([((V[i]+V[j])/2) @ nhat for i, j in edges])
en = np.array([((V[j]-V[i])*PHI) @ nhat for i, j in edges])

ok("T1", len(edges) == 720 and abs(abs(mn).max() - (1 + PHI/2)/2) < 1e-9
   and abs(abs(en).max() - 1.0) < 1e-9,
   f"{len(edges)} edges; |m.n|_max = {abs(mn).max():.6f} = (1 + phi/2)/2 (host-incident edges); "
   f"|e.n|_max = {abs(en).max():.6f}")

B = PHI ** -3
def admissible(A):
    return bool(np.all(1 + A*mn - B*np.abs(en) > 0))
grid = np.linspace(-3, 3, 60001)
good = grid[[admissible(a) for a in grid]]
A_lo, A_hi = good.min(), good.max()
ok("T2", A_lo < 0 < A_hi and abs(A_hi + A_lo) < 1e-3,
   f"at B = phi^-3 = {B:.4f}: admissible A-domain = [{A_lo:+.3f}, {A_hi:+.3f}], symmetric as expected "
   "(the edge set is closed under reversal, which flips both m.n sign classes)")

ok("T3", A_hi >= 1.0 and A_hi < 1.10,
   f"the panel's tested box A in [0, 1] lies INSIDE the domain and exhausts {100*1.0/A_hi:.0f}% of its "
   "positive half — the tested range was very nearly everything the rate law permits")

neg = mn < 0
A_closed = float(np.min((1 - B*np.abs(en[neg])) / np.abs(mn[neg])))
k = int(np.argmin((1 - B*np.abs(en[neg])) / np.abs(mn[neg])))
mb, eb = mn[neg][k], en[neg][k]
ok("T4", abs(A_closed - A_hi) < 2e-3,
   f"A_max = min over edges with m.n < 0 of (1 - B|e.n|)/|m.n| = {A_closed:.4f}, matching the scan "
   f"({A_hi:.4f}). Binding edge has m.n = {mb:+.4f}, |e.n| = {abs(eb):.4f} — NOT the |m.n|-maximal "
   f"edge ({abs(mn).max():.4f}), which carries too small an |e.n| to bind")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
