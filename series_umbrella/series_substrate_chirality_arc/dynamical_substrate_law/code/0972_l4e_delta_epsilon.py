#!/usr/bin/env python3
"""
0972 — L4-E: the delta-epsilon relation, and the physical commitment hiding in it.

F.1 states the relation is "not pinned" and takes delta and epsilon as
independent inputs. Patch 0949 T7 noted that Reading C's edge-length
perturbation is the SAME reversal-odd first-harmonic covariant as MA.1's rate
law, and that constant-speed traversal maps one to the other with
delta = -epsilon. This patch works that out, and finds the relation IS pinned --
but only given a physical commitment that has never been stated as one.

Reading C (Capotauro v2.0 SS2.3, quoted in F.1):
    l(e_hat) = l_0 (1 + epsilon * e_hat . n_hat)
described as "edges of the 600-cell substrate acquire effective lengths".

  T1   THE PARITY PROBLEM. e_hat . n_hat is reversal-ODD, so l(e_hat) is not
       equal to l(-e_hat): the same edge has two different "lengths" depending
       on which way it is traversed. A metric length cannot do that. So
       Reading C's l is not a length -- it is a DIRECTED TRAVERSAL COST, and
       the substrate it describes is NON-RECIPROCAL. That is a physical
       commitment, not a geometric one, and F.1 does not flag it.
  T2   GIVEN that formula, constant-speed traversal (one Displace per Absolute
       Moment at c, A6'/A3') gives rate = c/l, hence
       r = r_0 (1 - epsilon (e.n) + epsilon^2 (e.n)^2 - ...), so
       DELTA = -EPSILON exactly at first order. 0949 T7 reproduced.
  T3   THE SECOND-ORDER BONUS. The same expansion fixes the quadratic term as
       +epsilon^2 (e.n)^2 -- which is reversal-EVEN. The reversal-ODD quadratic
       (e.n)(m.n), the dangerous channel found at 0955 and shown superadditive
       at 0957, has coefficient ZERO under this picture. Constant-speed
       traversal does not generate it.
  T4   THE COUNTERFACTUAL THAT MATTERS. If l were a genuine (reversal-even)
       length -- depending on the edge midpoint m.n rather than the traversal
       direction -- then r = c/l would be reversal-EVEN, generating the A-term
       and NOT delta. Then delta = 0 and MA.1's whole reversal-odd first
       harmonic would vanish. SO MA.1's FORM REQUIRES NON-RECIPROCITY: the
       reversal-odd rate law cannot come from a metric length perturbation.
  T5   the size of what an even length perturbation would generate instead,
       computed, so the two pictures can be told apart rather than conflated.
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
edges = [(i, int(j)) for i in range(N) for j in nbr[i] if i < j]

def cdir(u, w):
    d = V[w] - V[u]; return float((d/np.linalg.norm(d)) @ nhat)
def cmid(u, w):
    return float(((V[u] + V[w])/2) @ nhat)

eps = 1e-3
L  = lambda c: 1.0*(1 + eps*c)            # Reading C as written: direction-dependent
u0, w0 = edges[0]
c_fwd, c_bwd = cdir(u0, w0), cdir(w0, u0)
ok("T1", abs(c_bwd + c_fwd) < 1e-12 and abs(L(c_fwd) - L(c_bwd)) > 1e-9,
   f"PARITY PROBLEM: e.n is reversal-odd ({c_fwd:+.4f} forward, {c_bwd:+.4f} backward), so Reading C's "
   f"l differs by traversal direction ({L(c_fwd):.6f} vs {L(c_bwd):.6f}). A metric LENGTH cannot do "
   "that. Reading C's l is a DIRECTED TRAVERSAL COST and the substrate is NON-RECIPROCAL — a physical "
   "commitment F.1 does not flag as one")

cs = np.array([cdir(u, w) for u, w in edges] + [cdir(w, u) for u, w in edges])
r = 1.0/(1 + eps*cs)
nzc0 = np.abs(cs) > 1e-9
delta_eff = (r[nzc0] - 1.0)/cs[nzc0]
ok("T2", np.allclose(delta_eff, -eps, atol=5e-6),
   f"GIVEN that formula, constant-speed traversal (rate = c/l) gives r = r0(1 - eps(e.n) + ...), so "
   f"DELTA = {delta_eff.mean():+.6f} = -EPSILON at first order. The relation IS pinned; 0949 T7 "
   "reproduced over all 1440 directed edges")

quad = (r[nzc0] - (1 - eps*cs[nzc0]))/(eps**2 * cs[nzc0]**2)
ok("T3", np.allclose(quad, 1.0, atol=2e-3),
   f"SECOND-ORDER BONUS: the same expansion fixes the quadratic coefficient at +eps^2 (e.n)^2 "
   f"(measured {quad.mean():.4f} x eps^2 (e.n)^2), which is reversal-EVEN. **The reversal-ODD quadratic "
   "(e.n)(m.n) — the dangerous channel found at 0955 and shown superadditive at 0957 — has coefficient "
   "ZERO under this picture.** Constant-speed traversal does not generate it")

ms = np.array([cmid(u, w) for u, w in edges] + [cmid(w, u) for u, w in edges])
r_even = 1.0/(1 + eps*ms)
nzm = np.abs(ms) > 1e-9          # equatorial edges have m.n = 0 exactly; excluded from the ratio
nzc = np.abs(cs) > 1e-9
d_from_even = (r_even[nzc] - 1.0)/cs[nzc]
A_from_even = (r_even[nzm] - 1.0)/ms[nzm]
ok("T4", np.abs(np.mean(d_from_even)) < 0.2*eps and np.allclose(A_from_even, -eps, atol=5e-6),
   f"THE COUNTERFACTUAL: if l were a genuine reversal-EVEN length (depending on the midpoint m.n), "
   f"then r = c/l is reversal-even and generates the A-term at {A_from_even.mean():+.6f} = -eps "
   f"(over the {int(nzm.sum())} directed edges with m.n != 0; the {int((~nzm).sum())} equatorial ones have "
   f"m.n = 0 exactly and are unperturbed), while "
   f"the reversal-odd delta it generates averages {np.mean(d_from_even):+.2e} ~ 0. **MA.1's reversal-odd "
   "form REQUIRES non-reciprocity: it cannot come from a metric length perturbation**")

ok("T5", abs(A_from_even.mean() + eps) < 5e-6,
   f"so the two pictures are distinguishable, not interchangeable: a directed traversal cost gives "
   f"delta = -eps and A = 0; a metric length gives A = -eps and delta = 0. F.1 treats l as a 'length' "
   "in words while using it as a directed cost in the equation")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
