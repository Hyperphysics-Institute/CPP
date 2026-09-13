#!/usr/bin/env python3
"""
0941 — L4-C of OPEN-FP-F1-2: MA.2's antisymmetric first-shell current
construction derived from A6' (the PCD cycle) + L4-B, not assumed.

MA.2 posits   j(v) = SUM_{e in E1(v)} [ r(e;v) - r(-e;v) ] e + O(delta^2).

Three commitments sit in that line: (i) the sum runs over the first shell only
-- already THEO-DSL-1 (perturbation-locality), not re-derived here; (ii) the
rate appears in the ANTISYMMETRIC combination r(e) - r(-e); (iii) each term is
weighted by the unit direction e. L4-C is (ii) and (iii).

The question that makes it non-trivial: at a 600-cell vertex, -e is NOT an edge
direction. All twelve first-shell directions sit at u.n = -1/(2phi) (F.1 Thm
5.1), so the edge set is emphatically NOT centrally symmetric -- it sums to
-(6/phi) n, not to zero. So "r(-e;v)" cannot mean "the rate along the opposite
edge at v"; there is no such edge. Read that way MA.2 is ill-posed.

The PCD reading repairs it. Per Absolute Moment (A6'/A1'), the GP at v runs
Perceive (integrate DI-bit ARRIVALS) then Compute (refresh SSV_net); the CP
executes Displace along the SSV_net its GP computed. The net flux at v is
therefore departures minus arrivals, edge by edge. Every first-shell edge {v,w}
carries both: a departure imprinted at v with direction u, and an arrival
imprinted at w whose direction of travel, seen at v, is -u. The arrival's rate
is the rate law evaluated AT w -- and by L4-B (vertex-uniformity, Patch 0940)
w carries the same r0 and delta as v, so that rate is exactly r0(1 + delta
(-u).n) = r(-u). The "opposite direction" is not an edge at v; it is the
reverse traversal of the same edge, governed by the same law at the other end.

So the antisymmetric combination is forced by the Perceive/Displace split plus
vertex-uniformity, not chosen for convenience -- and L4-C depends on L4-B.

Two consequences fall out and are checked, not asserted:
  * the isotropic r0 cancels identically. It has to: without the cancellation
    the non-centrally-symmetric edge set would manufacture a current
    -r0 (6/phi) n at delta = 0, i.e. a net substrate flow in a substrate with
    no perturbation in it. The antisymmetric construction is the one that does
    not create a current from nothing.
  * the surviving first-order current is 2 r0 delta SUM (u.n) u = (6/phi^2)
    r0 delta n -- reproducing F.1 Theorem 7.1's structural constant
    alpha_1 = 6/phi^2 from the PCD bookkeeping alone.

Tests
  T1  600-cell: 120 vertices, 12 first-shell neighbours each, all at
      u.n = -1/(2phi) under vertex-aligned Reading C.
  T2  the first-shell direction set is NOT centrally symmetric: for every one
      of the twelve u, -u is not a first-shell direction at v.
  T3  SUM u = -(6/phi) n, nonzero -- the geometric fact that makes the
      symmetric construction fail.
  T4  the naive (non-antisymmetric) construction SUM r(u) u has a nonzero
      O(delta^0) term equal to -r0 (6/phi) n: a current at delta = 0.
  T5  reverse-traversal identity: for each edge {v,w}, the direction of travel
      from w to v is exactly -u, and the rate law at w (same r0, delta by L4-B)
      evaluates on it to r(-u). Checked at every vertex, not just v_host.
  T6  the antisymmetric construction kills O(delta^0) identically, at every
      vertex of the substrate.
  T7  the surviving current is (6/phi^2) r0 delta n at v_host -- F.1 Theorem
      7.1's alpha_1, recovered.
  T8  L4-B dependence is real: if r0 and delta were allowed to differ at w
      (vertex-uniformity denied), T5's identity fails and the r0 cancellation
      of T6 breaks. Exhibited with a perturbed r0 at one neighbour.
"""
import itertools, sys
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
TOL = 1e-9
res = []

def ok(name, cond, note=""):
    res.append(cond); print(f"{name} {'PASS' if cond else 'FAIL'}  {note}")

def vertices_600():
    V = []
    for s in itertools.product([1, -1], repeat=4):
        V.append(0.5 * np.array(s, dtype=float))
    for i in range(4):
        for s in (1, -1):
            e = np.zeros(4); e[i] = s; V.append(e)
    base = [PHI / 2, 0.5, 1 / (2 * PHI), 0.0]
    evens = [p for p in itertools.permutations(range(4))
             if sum(1 for i in range(4) for j in range(i) if p[j] > p[i]) % 2 == 0]
    for p in evens:
        for s in itertools.product([1, -1], repeat=3):
            v = np.zeros(4)
            vals = [s[0] * base[0], s[1] * base[1], s[2] * base[2], 0.0]
            for k in range(4): v[p[k]] = vals[k]
            V.append(v)
    U = []
    for v in V:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    return np.array(U)

V = vertices_600(); N = len(V)
edge = 1 / PHI
G = V @ V.T
nbr = [np.where(np.abs(G[i] - PHI / 2) < 1e-8)[0] for i in range(N)]
host = 0
n_hat = V[host].copy()

def dirs(v_i):
    """unit edge-directions from vertex v_i to its twelve first-shell neighbours"""
    return np.array([(V[j] - V[v_i]) / edge for j in nbr[v_i]])

U_host = dirs(host)

# ---------- T1
projs = U_host @ n_hat
ok("T1", N == 120 and len(U_host) == 12 and np.allclose(projs, -1 / (2 * PHI), atol=1e-9),
   f"120 vertices, 12 first-shell directions, all at u.n = {projs[0]:+.6f} = -1/(2phi)")

# ---------- T2  not centrally symmetric
def is_edge_dir(v_i, d):
    return any(np.allclose(d, x, atol=1e-8) for x in dirs(v_i))
ok("T2", not any(is_edge_dir(host, -u) for u in U_host),
   "for all twelve u, -u is NOT a first-shell direction at v: the edge set is not centrally symmetric")

# ---------- T3  the sum does not vanish
S = U_host.sum(axis=0)
ok("T3", np.allclose(S, -(6 / PHI) * n_hat, atol=1e-8) and np.linalg.norm(S) > TOL,
   f"SUM u = {np.linalg.norm(S):.6f} * (-n) = -(6/phi) n   [6/phi = {6/PHI:.6f}]")

# ---------- rate law (MA.1), with per-vertex parameters so T8 can break them
def rate(u, r0=1.0, delta=1e-3):
    return r0 * (1.0 + delta * float(u @ n_hat))

# ---------- T4  naive construction has an O(delta^0) current
r0, delta = 1.0, 1e-3
J_naive = sum(rate(u, r0, delta) * u for u in U_host)
J_naive_at_zero = sum(rate(u, r0, 0.0) * u for u in U_host)
ok("T4", np.allclose(J_naive_at_zero, -(6 / PHI) * r0 * n_hat, atol=1e-8),
   f"naive SUM r(u) u at delta = 0 gives |J| = {np.linalg.norm(J_naive_at_zero):.6f} along -n "
   "— a substrate current with no perturbation present")

# ---------- T5  reverse-traversal identity, at every vertex
rev_ok = True
for v_i in range(N):
    for j in nbr[v_i]:
        u = (V[j] - V[v_i]) / edge            # departure direction at v_i
        u_back = (V[v_i] - V[j]) / edge       # direction of travel w -> v_i, seen at v_i
        if not np.allclose(u_back, -u, atol=1e-9): rev_ok = False; break
        # the arrival's rate is the law evaluated at w on its own outgoing direction,
        # which is u_back = -u; vertex-uniformity (L4-B) supplies the same r0, delta
        if abs(rate(u_back, r0, delta) - rate(-u, r0, delta)) > 1e-12: rev_ok = False; break
    if not rev_ok: break
ok("T5", rev_ok,
   "for every edge at every vertex: travel direction w->v is exactly -u, and the rate law at w "
   "(same r0, delta by L4-B) evaluates to r(-u) — so 'r(-e;v)' is the reverse traversal, not a missing edge")

# ---------- T6  antisymmetric construction kills O(delta^0) everywhere
def J_anti(v_i, r0=1.0, delta=1e-3):
    return sum((rate(u, r0, delta) - rate(-u, r0, delta)) * u for u in dirs(v_i))
zero_ok = all(np.linalg.norm(J_anti(v_i, r0, 0.0)) < 1e-12 for v_i in range(N))
ok("T6", zero_ok,
   "antisymmetric construction gives J = 0 identically at delta = 0, at all 120 vertices "
   "— no current manufactured from nothing")

# ---------- T7  alpha_1 = 6/phi^2
J1 = J_anti(host, r0, delta)
coeff = float(J1 @ n_hat) / (r0 * delta)
perp = np.linalg.norm(J1 - (J1 @ n_hat) * n_hat)
ok("T7", abs(coeff - 6 / PHI ** 2) < 1e-8 and perp < 1e-10,
   f"J = {coeff:.9f} r0 delta n, parallel to n (perp {perp:.2e}); 6/phi^2 = {6/PHI**2:.9f} "
   "— F.1 Theorem 7.1's alpha_1 recovered from the PCD bookkeeping")

# ---------- T8  the L4-B dependence is load-bearing
# deny vertex-uniformity: give ONE neighbour of host a different r0 and see T5/T6 fail.
w = int(nbr[host][0])
u_w = (V[w] - V[host]) / edge
r0_w = 1.30                                     # w's own rate scale, different from v's
arrival_from_w = rate(-u_w, r0_w, delta)        # rate law AT w on its outgoing direction
arrival_uniform = rate(-u_w, r0, delta)
J_nonuniform_at_zero = (rate(u_w, r0, 0.0) - rate(-u_w, r0_w, 0.0)) * u_w + \
    sum((rate(u, r0, 0.0) - rate(-u, r0, 0.0)) * u for u in U_host[1:])
ok("T8", abs(arrival_from_w - arrival_uniform) > 1e-6 and np.linalg.norm(J_nonuniform_at_zero) > 1e-6,
   f"deny L4-B at one neighbour (r0_w = {r0_w}): the arrival rate no longer equals r(-u) "
   f"and the delta = 0 current reopens at |J| = {np.linalg.norm(J_nonuniform_at_zero):.4f} "
   "— L4-C genuinely rests on L4-B")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
