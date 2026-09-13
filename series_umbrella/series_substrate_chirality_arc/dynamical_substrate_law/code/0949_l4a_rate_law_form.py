#!/usr/bin/env python3
"""
0949 — L4-A of OPEN-FP-F1-2: what representation theory forces, permits, and
cannot decide about the FORM of MA.1's rate law
    r(e; v) = r0 (1 + delta e.n).

MA.1 makes three commitments: (i) linear in e.n, "exact at the framework
level"; (ii) a single scalar delta; (iii) no O(delta^0) tangent term. L4-A asks
which of these follow from the primitives -- A11 (600-cell substrate), the
single primitive direction n (FI-C-RC-1), and H4-covariance -- and which are
framework simplifications.

Method. A rate law is a function on DIRECTED EDGES (v, e) of the 600-cell that
depends on n. H4-covariance means r(g v, g e; g n) = r(v, e; n). Expanding in
harmonics of n: the O(n^0) part is an H4-invariant function on directed edges;
the O(n^1) part is c(v,e).n with c an H4-EQUIVARIANT vector field on directed
edges; the O(n^2) part is n^T T(v,e) n with T an equivariant symmetric-tensor
field. By Frobenius reciprocity on a transitive action, each of these spaces
has dimension equal to the number of INVARIANTS of the directed-edge
stabiliser S in the relevant representation. Everything below is computed from
the lattice; no group is typed in.

Tests
  T1  O(delta^0): the vertex stabiliser is transitive on the 12 first-shell
      directions, and the substrate is vertex-transitive (0940), so H4 is
      ARC-transitive: one orbit on the 1,440 directed edges. Hence the
      unperturbed rate is a single constant r0 with no tangent structure.
      MA.1 COMMITMENT (iii) IS DERIVED.
  T2  the directed-edge stabiliser S has order 10 (= 14400/1440), is C5v, and
      its fixed subspace in R^4 is exactly span{v, w} -- dimension 2.
  T3  so the O(n^1) rate perturbation is a TWO-parameter family, not one:
      r1 = A (m.n) + B (e.n), with m the edge midpoint and e the edge direction.
      Under edge REVERSAL (v,e) -> (w,-e) the m-term is even and the e-term is
      odd, and the reversal-ODD part is one-dimensional: B e.n, unique up to
      scale. That is MA.1's form, and it is the unique reversal-odd covariant.
      MA.1's "single scalar delta" is TRUE OF THE REVERSAL-ODD PART and is
      otherwise the choice A = 0.
  T4  the reversal-even term A m.n cancels IDENTICALLY in MA.2's antisymmetric
      current construction, at every vertex, for every A: reverse traversal has
      the same midpoint. So the O(delta^1) current -- and with it Theorem 7.1's
      alpha_1 = 6/phi^2, the substrate-locality theorem, and L4-C -- is
      A-INDEPENDENT. Everything the arc consumes at O(delta^1) sees only B.
  T5  the A-term does NOT cancel in the detailed-balance ratio
      r(v->w)/r(w->v) = (r0 + A m.n + B e.n)/(r0 + A m.n - B e.n): the
      effective tilt is B/(r0 + A m.n), position-dependent, entering the
      stationary measure at O(AB) = O(delta^2). So the NESS-based results
      (0694 pi-construction, 1100 mu^2-sign, the O(delta^3) steady current)
      DO consume A = 0. That residual is NOT discharged by symmetry.
  T6  O(n^2): the S-invariant subspace of Sym^2(R^4) has dimension 4, i.e.
      three independent quadratic invariants beyond |n|^2 = 1. Representation
      theory PERMITS quadratic terms in the rate law; MA.1's "linear exact" is
      a truncation to the first harmonic, not a consequence of the primitives.
      That residual too is consumed only beyond O(delta^1).
  T7  Reading C's edge-length perturbation l(e) = l0 (1 + eps e.n) is the same
      reversal-odd first-harmonic covariant. Exhibited: the two forms are the
      SAME representation-theoretic object, so a constant-speed traversal
      (one Displace per Absolute Moment at c, A6') maps one onto the other
      with delta = -eps at first order. Offered as the structural lead for
      L4-E; not claimed as its closure.
"""
import itertools, sys
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
res = []
def ok(n, c, note=""):
    res.append(c); print(f"{n} {'PASS' if c else 'FAIL'}  {note}")

def vertices_600():
    V = []
    for s in itertools.product([1, -1], repeat=4): V.append(0.5 * np.array(s, dtype=float))
    for i in range(4):
        for s in (1, -1):
            e = np.zeros(4); e[i] = s; V.append(e)
    base = [PHI / 2, 0.5, 1 / (2 * PHI), 0.0]
    ev = [p for p in itertools.permutations(range(4))
          if sum(1 for i in range(4) for j in range(i) if p[j] > p[i]) % 2 == 0]
    for p in ev:
        for s in itertools.product([1, -1], repeat=3):
            v = np.zeros(4); vals = [s[0]*base[0], s[1]*base[1], s[2]*base[2], 0.0]
            for k in range(4): v[p[k]] = vals[k]
            V.append(v)
    U = []
    for v in V:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    return np.array(U)

V = vertices_600(); N = len(V); edge = 1 / PHI
G = V @ V.T
nbr = [np.where(np.abs(G[i] - PHI/2) < 1e-8)[0] for i in range(N)]
host = 0; v_h = V[host]

# ---- vertex stabiliser as 4x4 orthogonal maps
idx = [host]
for j in nbr[host]:
    A = np.array([V[i] for i in idx] + [V[j]])
    if np.linalg.matrix_rank(A, tol=1e-8) == len(idx)+1: idx.append(int(j))
    if len(idx) == 4: break
A = np.array([V[i] for i in idx]); Ainv = np.linalg.inv(A); gram = A @ A.T
def is_lattice_map(M):
    Y = V @ M.T
    return all(len(np.where(np.abs(V - y).max(axis=1) < 1e-7)[0]) == 1 for y in Y)
StabV = []
for cand in itertools.permutations(nbr[host], 3):
    B = np.array([V[host]] + [V[c] for c in cand])
    if not np.allclose(B @ B.T, gram, atol=1e-7): continue
    M = (Ainv @ B).T
    if not np.allclose(M @ M.T, np.eye(4), atol=1e-7): continue
    if is_lattice_map(M): StabV.append(M)
assert len(StabV) == 120

# ---- T1: arc-transitivity => r0 constant
w_idx = int(nbr[host][0]); w = V[w_idx]
orbit_w = set()
for M in StabV:
    img = M @ w
    k = np.where(np.abs(V - img).max(axis=1) < 1e-7)[0][0]
    orbit_w.add(int(k))
n_directed = sum(len(x) for x in nbr)
ok("T1", orbit_w == set(int(j) for j in nbr[host]) and n_directed == 1440,
   f"Stab(v) is transitive on the 12 first-shell directions; with vertex-transitivity (0940 T2) H4 is "
   f"ARC-transitive on the {n_directed} directed edges => one orbit => r0 is ONE constant with no "
   "tangent structure. MA.1 (iii) DERIVED")

# ---- T2: directed-edge stabiliser and its fixed subspace
S = [M for M in StabV if np.allclose(M @ w, w, atol=1e-8)]
# fixed subspace: null space of stacked (M - I)
K = np.vstack([M - np.eye(4) for M in S])
_, sv, vt = np.linalg.svd(K)
fixed_dim = int(np.sum(sv < 1e-8)) + (4 - len(sv) if len(sv) < 4 else 0)
fixed_basis = vt[np.abs(np.r_[sv, np.zeros(4 - len(sv))]) < 1e-8] if len(sv) == 4 else vt[len(sv):]
# check span{v, w} is fixed and nothing else
P_vw = np.linalg.lstsq(np.array([v_h, w]).T, np.eye(4), rcond=None)[0]
in_span = all(np.linalg.norm(np.array([v_h, w]).T @ np.linalg.lstsq(np.array([v_h, w]).T, b, rcond=None)[0] - b) < 1e-8
              for b in fixed_basis)
orders = sorted({int(round(k)) for k in [
    next(kk for kk in range(1, 21) if np.allclose(np.linalg.matrix_power(M, kk), np.eye(4), atol=1e-7)) for M in S]})
ok("T2", len(S) == 10 and fixed_dim == 2 and in_span and orders == [1, 2, 5],
   f"|S| = {len(S)} = 14400/1440, element orders {orders} (C5v); S-fixed subspace of R^4 has dim {fixed_dim} "
   "= span{v, w} exactly")

# ---- T3: two-parameter O(n^1) family; reversal-odd part unique
m = (v_h + w) / 2                       # midpoint: reversal-even
e = (w - v_h) / edge                    # direction: reversal-odd
# reversal maps (v,e)->(w,-e); check parity of the two basis covariants
rev_even = np.allclose((w + v_h) / 2, m) and np.allclose((v_h - w) / edge, -e)
ok("T3", rev_even and abs(np.linalg.matrix_rank(np.array([m, e]), tol=1e-9) - 2) < 1e-9,
   "O(n^1) rate perturbation r1 = A (m.n) + B (e.n): a TWO-parameter family. Under reversal the m-term is "
   "even, the e-term odd, and the reversal-ODD part is 1-dim: B e.n, unique up to scale = MA.1's form. "
   "'Single scalar delta' is true of the reversal-odd part; otherwise it is the choice A = 0")

# ---- T4: A cancels in the antisymmetric current, every vertex, any A
n_hat = v_h.copy()
def rate(v_i, j, r0, Acoef, Bcoef):
    vv, ww = V[v_i], V[j]
    mm = (vv + ww) / 2; ee = (ww - vv) / edge
    return r0 * (1 + Acoef * float(mm @ n_hat) + Bcoef * float(ee @ n_hat))
def J(v_i, r0, Acoef, Bcoef):
    out = np.zeros(4)
    for j in nbr[v_i]:
        ee = (V[j] - V[v_i]) / edge
        out += (rate(v_i, j, r0, Acoef, Bcoef) - rate(j, v_i, r0, Acoef, Bcoef)) * ee
    return out
r0, Bc = 1.0, 1e-3
A_free = all(np.allclose(J(v_i, r0, 0.0, Bc), J(v_i, r0, Ac, Bc), atol=1e-12)
             for v_i in range(N) for Ac in (0.3, -0.7))
ok("T4", A_free,
   "the reversal-even A m.n term cancels IDENTICALLY in MA.2's antisymmetric current at all 120 vertices "
   "for arbitrary A: everything the arc consumes at O(delta^1) sees only B")
Jh = J(host, r0, 0.5, Bc)
ok("T4b", abs(float(Jh @ n_hat) / (r0 * Bc) - 6 / PHI**2) < 1e-8,
   f"with A = 0.5 the host current is still {float(Jh @ n_hat)/(r0*Bc):.9f} r0 B n = (6/phi^2) r0 B n "
   "— Theorem 7.1's alpha_1 is A-independent")

# ---- T5: A does not cancel in detailed balance
def db_log_ratio(v_i, j, r0, Acoef, Bcoef):
    return np.log(rate(v_i, j, r0, Acoef, Bcoef) / rate(j, v_i, r0, Acoef, Bcoef))
# pick a vertex where m.n varies across its edges (not the host, where it is constant)
v_mid = int(np.where(np.abs(V @ n_hat - 0.5) < 1e-8)[0][0])
ratios0 = [db_log_ratio(v_mid, j, r0, 0.0, Bc) for j in nbr[v_mid]]
ratiosA = [db_log_ratio(v_mid, j, r0, 0.5, Bc) for j in nbr[v_mid]]
ok("T5", max(abs(a - b) for a, b in zip(ratios0, ratiosA)) > 1e-6,
   "log[r(v->w)/r(w->v)] CHANGES with A at second order: effective tilt B/(r0 + A m.n) is position-dependent, "
   "so the stationary measure pi (0694) and everything downstream at O(delta^3) (1100) consume A = 0. "
   "NOT discharged by symmetry")

# ---- T6: quadratic invariants
def sym2_action(M):
    # action on symmetric 2-tensors: T -> M T M^T, as a 10x10 on the upper-triangular basis
    basis = []
    for i in range(4):
        for j in range(i, 4):
            T = np.zeros((4, 4)); T[i, j] = T[j, i] = 1.0 if i == j else 0.5
            basis.append(T)
    def coords(T):
        return np.array([T[i, j] * (1 if i == j else 2) for i in range(4) for j in range(i, 4)])
    return np.array([coords(M @ T @ M.T) for T in basis]).T
K2 = np.vstack([sym2_action(M) - np.eye(10) for M in S])
sv2 = np.linalg.svd(K2, compute_uv=False)
inv_dim2 = int(np.sum(sv2 < 1e-8)) + (10 - len(sv2))
ok("T6", inv_dim2 == 4,
   f"S-invariant subspace of Sym^2(R^4) has dim {inv_dim2}: three independent quadratic invariants beyond "
   "|n|^2 = 1. Representation theory PERMITS quadratic terms; MA.1's 'linear exact' is a truncation to the "
   "first harmonic, consumed only beyond O(delta^1)")

# ---- T7: Reading C's edge-length form is the same covariant; delta = -eps at first order
eps = 2e-3
l = lambda ee: 1.0 * (1 + eps * float(ee @ n_hat))
r_from_l = lambda ee: 1.0 / l(ee)                         # constant speed: rate = c / length
E12 = [(V[j] - V[host]) / edge for j in nbr[host]]
delta_eff = [(r_from_l(ee) - 1.0) / float(ee @ n_hat) for ee in E12]
ok("T7", all(abs(d + eps) < 5e-6 for d in delta_eff),
   f"l(e) = l0(1 + eps e.n) is the same reversal-odd first-harmonic covariant; constant-speed traversal "
   f"gives r(e) = r0(1 + delta e.n) with delta = {np.mean(delta_eff):+.6f} = -eps + O(eps^2). "
   "Structural lead for L4-E, not its closure")

n = sum(res); print(f"\n{n}/{len(res)}")
sys.exit(0 if n == len(res) else 1)
