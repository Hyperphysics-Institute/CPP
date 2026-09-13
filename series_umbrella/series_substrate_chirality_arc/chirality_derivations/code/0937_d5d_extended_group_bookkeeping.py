#!/usr/bin/env python3
"""
0937 — explicit group bookkeeping on the qDP four-state space, closing the three
flags F1–F3 of OPEN-CHIR-QDP-4STATE-1 (raised at 0936 against Finding C-W46,
THEO-SD-CHIR-2, capotauro.tex §20).

Everything is built numerically from the unit 600-cell, with no character table
typed in by hand: the local point group at the host is generated from the
lattice, the stabiliser of an antipodal first-shell pair is enumerated, its
1-D characters are constructed from the elements themselves, and every
operator on the four-state space is classified and its doublet matrix element
computed.

Tests
  T1  F1 geometry: the inversion of the local point group is p ↦ φ n̂ − p on the
      first shell (icosahedral-centre, R1). It fixes the host and fixes n̂. The
      host-centred inversion 2 v_host − p and the ambient direction −û are not
      first-shell configurations.
  T2  The stabiliser of the pair {v, v′} inside the local group has order 20,
      class structure (1,2,2,5,1,2,2,5) — D5d — and the pseudoscalar
      A_u(I_h) branches to A1u(D5d), not A2u.
  T3  The four-state space {|s,x⟩} under D5d × Z2^C decomposes as
      A1g⁺ ⊕ A1g⁻ ⊕ A2u⁺ ⊕ A2u⁻ (each once); C-W46's doublet
      Ψ⁽¹⁾ = (A1g⁺ + A2u⁻)/√2, Ψ⁽²⁾ = (A1g⁻ + A2u⁺)/√2.
  T4  Operator support: the 16-dimensional operator space on the four-state
      space carries only A1g and A2u of the geometric D5d — every A1u or A2g
      operator is identically zero there. So a pure pseudoscalar of the local
      point group has NO nonzero matrix element in the antipodal-pair space
      (the D5d refinement alone does not rescue the C5v vanishing).
  T5  Doublet selection rule: ⟨Ψ⁽¹⁾|Ô|Ψ⁽²⁾⟩ ≠ 0 iff Ô ∈ A1g⁻ or A2u⁺.
      A1g⁻ is spanned by the charge-sign operator ŝ (and ŝ⊗swap);
      A2u⁺ by the position-parity operator (|v⟩⟨v| − |v′⟩⟨v′|) (and its
      antisymmetric partner). C-W46's literal label A2u ⊗ ζ-odd (= A2u⁻)
      gives zero.
  T6  F3: on the doublet, ŝ ⊗ 1 is diagonal in the configuration basis with
      ⟨Ψ⁽¹⁾|ŝ|Ψ⁽²⁾⟩ = ½[E(+,v) − E(−,v′)] = 1, i.e. a diagonal split, no
      |+,v⟩ ↔ |−,v′⟩ mixing; the only mixing operators with nonzero doublet
      element (the antisymmetric partners) are not diagonalisable as an
      energy that respects the host-slaved dipole d̂ = s û.
  T7  Under R1 the placement energy f(û·n̂) is constant on {v,v′} (A1g⁺) and
      has zero doublet element; the orientation energy s·f(û·n̂) is A1g⁻ and
      reproduces the doublet — the 0936 table, now derived from the group.
"""
import itertools, sys
import numpy as np

PHI = (1 + 5 ** 0.5) / 2
TOL = 1e-9
results = []

def ok(name, cond, note=""):
    results.append(cond)
    print(f"{name} {'PASS' if cond else 'FAIL'}  {note}")

# ---------------------------------------------------------------- 600-cell
def vertices_600():
    V = []
    for signs in itertools.product([1, -1], repeat=4):
        V.append(0.5 * np.array(signs))
    for i in range(4):
        for s in (1, -1):
            e = np.zeros(4); e[i] = s; V.append(e)
    base = [PHI / 2, 0.5, 1 / (2 * PHI), 0.0]
    evens = [p for p in itertools.permutations(range(4))
             if sum(1 for i in range(4) for j in range(i) if p[j] > p[i]) % 2 == 0]
    for p in evens:
        for signs in itertools.product([1, -1], repeat=3):
            v = np.zeros(4)
            vals = [signs[0] * base[0], signs[1] * base[1], signs[2] * base[2], 0.0]
            for k in range(4):
                v[p[k]] = vals[k]
            V.append(v)
    V = np.array(V)
    # dedupe
    U = []
    for v in V:
        if not any(np.allclose(v, u, atol=1e-9) for u in U):
            U.append(v)
    return np.array(U)

V = vertices_600()
assert len(V) == 120
n_hat = np.array([1.0, 0, 0, 0])         # host vertex = n̂ (vertex-aligned Reading C)
host = n_hat.copy()
shell = np.array([v for v in V if abs(v @ host - PHI / 2) < TOL])
assert len(shell) == 12
c = (PHI / 2) * n_hat                    # icosahedral centre
edge = 1 / PHI

def is_shell(p):
    return any(np.allclose(p, s, atol=1e-8) for s in shell)

# ---------------------------------------------------------------- T1 (F1)
v = shell[0]
v_R1 = PHI * n_hat - v                   # icosahedral-centre inversion
v_R2 = 2 * host - v                      # host-centred inversion
u_hat = (v - host) / edge
u_R1 = (v_R1 - host) / edge
proj = u_hat @ n_hat
t1 = (is_shell(v_R1) and not is_shell(v_R2)
      and abs(proj + 1 / (2 * PHI)) < TOL and abs(u_R1 @ n_hat - proj) < TOL
      and not is_shell(host - u_hat * edge))     # ambient −û from host is off-lattice
# the 3-D inversion of the ⟂ space: w ↦ −w with the n̂ component fixed
perp = lambda p: p - (p @ n_hat) * n_hat
v_inv3 = (v @ n_hat) * n_hat - perp(v)
t1 = t1 and np.allclose(v_inv3, v_R1) and np.allclose(perp(host), 0)
ok("T1", t1, f"local inversion = p↦φn̂−p (R1) on the shell; û·n̂ = {proj:+.4f} for both antipodes; "
             f"host-centred 2v_host−v and ambient −û are not shell configurations; n̂ fixed")

# ---------------------------------------------------------------- local point group
# Work in the 3-space ⟂ n̂: coordinates of the shell relative to c.
W = np.array([perp(s) for s in shell])           # 12 points, |w| = const
R_ = np.linalg.norm(W[0])
# generate the symmetry group of the 12-point set: orthogonal 3x3 maps (in an
# orthonormal basis of the ⟂ space) that permute W.
# orthonormal basis of ⟂ n̂
B = np.linalg.svd(np.eye(4) - np.outer(n_hat, n_hat))[0][:, :3]
X = W @ B                                         # 12 x 3
def perm_of(M):
    Y = X @ M.T
    p = []
    for y in Y:
        hits = [i for i, x in enumerate(X) if np.allclose(x, y, atol=1e-7)]
        if len(hits) != 1: return None
        p.append(hits[0])
    return tuple(p)
# Build maps from ordered triples: pick a fixed non-degenerate triple (x0,x1,x2)
# and map it to every ordered triple (y0,y1,y2) with the same Gram matrix.
idx = [0, None, None]
for j in range(1, 12):
    for k in range(j + 1, 12):
        A = np.array([X[0], X[j], X[k]])
        if abs(np.linalg.det(A)) > 1e-6:
            idx = [0, j, k]; break
    if idx[1] is not None: break
A = np.array([X[i] for i in idx])
G_gram = A @ A.T
elems = {}
for trip in itertools.permutations(range(12), 3):
    Y = np.array([X[i] for i in trip])
    if not np.allclose(Y @ Y.T, G_gram, atol=1e-7): continue
    M = np.linalg.solve(A, Y).T                   # M A_i = Y_i  →  M = (A^{-1} Y)^T
    if not np.allclose(M @ M.T, np.eye(3), atol=1e-7): continue
    p = perm_of(M)
    if p is not None: elems[p] = M
Ih = elems
ok("T2a", len(Ih) == 120, f"local point group order {len(Ih)} (I_h)")

# D5d = stabiliser of the pair {v, v'} (indices in `shell`)
i_v = 0
i_vp = [i for i, s in enumerate(shell) if np.allclose(s, v_R1, atol=1e-8)][0]
D5d = {p: M for p, M in Ih.items() if {p[i_v], p[i_vp]} == {i_v, i_vp}}
# classes by conjugation
def mul(p, q):  # (p∘q)(i) = p[q[i]]
    return tuple(p[q[i]] for i in range(12))
def inv(p):
    r = [0] * 12
    for i, pi in enumerate(p): r[pi] = i
    return tuple(r)
classes = []
seen = set()
for g in D5d:
    if g in seen: continue
    cl = {mul(mul(h, g), inv(h)) for h in D5d}
    seen |= cl; classes.append(cl)
class_sizes = sorted(len(cl) for cl in classes)
det = {p: round(np.linalg.det(M)) for p, M in D5d.items()}
identity = tuple(range(12))
inversion = [p for p, M in D5d.items() if np.allclose(M, -np.eye(3))][0]
# 1-D characters built from the elements: g/u from det; 1/2 from the sign on the
# perpendicular C2 axes. A C2 element: proper, order 2, swaps v and v'.
def order(p):
    q, k = p, 1
    while q != identity: q = mul(q, p); k += 1
    return k
C2s = [p for p in D5d if det[p] == 1 and order(p) == 2 and p[i_v] == i_vp]
ok("T2b", len(D5d) == 20 and class_sizes == [1, 1, 2, 2, 2, 2, 5, 5] and len(C2s) == 5,
   f"stabiliser of the pair has order {len(D5d)}, class sizes {class_sizes}, {len(C2s)} perpendicular C2 — D5d")
def rot_part(p):  # proper element with the same permutation action up to inversion
    return p if det[p] == 1 else mul(inversion, p)
def a2(p):        # A2(D5) sign: -1 on the C2 axes, +1 on the C5 subgroup
    r = rot_part(p)
    return -1 if r in C2s else 1
chars = {
    "A1g": {p: 1 for p in D5d},
    "A2g": {p: a2(p) for p in D5d},
    "A1u": {p: det[p] for p in D5d},
    "A2u": {p: a2(p) * det[p] for p in D5d},
}
# pseudoscalar of I_h restricted: A_u(I_h)(g) = det g
Au_restricted = {p: det[p] for p in D5d}
which = [k for k, ch in chars.items() if all(ch[p] == Au_restricted[p] for p in D5d)]
ok("T2c", which == ["A1u"], f"A_u(I_h) ↓ D5d = {which} (C-W46 §20.5 wrote A2u)")
# C-W46's printed character is (1,1,1,-1,-1,-1,-1,1): +1 on C5s, -1 on C2, -1 on i, -1 on S10, +1 on σd
cw46 = {p: (a2(p) * det[p]) for p in D5d}   # that IS A2u by construction
sigma_d = [p for p in D5d if det[p] == -1 and order(p) == 2 and p != inversion]
ok("T2d", all(cw46[p] == 1 for p in sigma_d) and all(cw46[p] == -1 for p in C2s),
   "C-W46's printed character (+1 on σ_d, −1 on C2) is A2u = the character of a polar axial coordinate, "
   "which is EVEN under the C5 rotations and ODD under the perpendicular C2 — a proper-rotation-odd object is not a pseudoscalar")

# ---------------------------------------------------------------- four-state space
# basis order: |+,v>, |+,v'>, |-,v>, |-,v'>
pos_perm = {p: (0 if p[i_v] == i_v else 1) for p in D5d}   # 0: v fixed, 1: v<->v' swapped
def rep(p, cflip):
    M = np.zeros((4, 4))
    for s in (0, 1):          # 0 = +, 1 = −
        for x in (0, 1):      # 0 = v, 1 = v'
            s2 = s ^ cflip
            x2 = x ^ pos_perm[p]
            M[2 * s2 + x2, 2 * s + x] = 1
    return M
G = [(p, cf) for p in D5d for cf in (0, 1)]       # D5d × Z2^C, order 40
def char_G(name, csign):
    return {(p, cf): chars[name][p] * (csign ** cf) for (p, cf) in G}
irreps = {f"{nm}{'+' if cs == 1 else '−'}": char_G(nm, cs)
          for nm in chars for cs in (1, -1)}
def projector(chi):
    P = np.zeros((4, 4))
    for g in G:
        P += chi[g] * rep(*g)
    return P / len(G)
mult = {k: round(np.trace(projector(ch))) for k, ch in irreps.items()}
ok("T3a", {k: v_ for k, v_ in mult.items() if v_} == {"A1g+": 1, "A1g−": 1, "A2u+": 1, "A2u−": 1},
   f"four-state space = {', '.join(k for k, v_ in mult.items() if v_)} (each once)")
def basis_vec(k):
    P = projector(irreps[k]); col = P[:, np.argmax(np.abs(P).sum(axis=0))]
    return col / np.linalg.norm(col)
e = {k: basis_vec(k) for k in ("A1g+", "A1g−", "A2u+", "A2u−")}
Psi1 = np.array([1, 0, 0, 1]) / 2 ** 0.5     # (|+,v> + |-,v'>)/√2
Psi2 = np.array([1, 0, 0, -1]) / 2 ** 0.5    # (|+,v> - |-,v'>)/√2
def sgn(x): return 1 if x > 0 else -1
d1 = {k: abs(e[k] @ Psi1) for k in e}; d2 = {k: abs(e[k] @ Psi2) for k in e}
ok("T3b", abs(d1["A1g+"] - 2 ** -0.5) < TOL and abs(d1["A2u−"] - 2 ** -0.5) < TOL and d1["A1g−"] < TOL and d1["A2u+"] < TOL
   and abs(d2["A1g−"] - 2 ** -0.5) < TOL and abs(d2["A2u+"] - 2 ** -0.5) < TOL and d2["A1g+"] < TOL and d2["A2u−"] < TOL,
   "Ψ⁽¹⁾ = (A1g⁺ + A2u⁻)/√2 ,  Ψ⁽²⁾ = (A1g⁻ + A2u⁺)/√2")

# ---------------------------------------------------------------- operators
# operator space: 16-dim, adjoint action  O ↦ R(g) O R(g)^T
ops_basis = [np.outer(np.eye(4)[i], np.eye(4)[j]) for i in range(4) for j in range(4)]
def op_projector(chi):
    def P(O):
        acc = np.zeros((4, 4))
        for g in G:
            R = rep(*g); acc += chi[g] * (R @ O @ R.T)
        return acc / len(G)
    return P
op_mult = {}
for k, ch in irreps.items():
    P = op_projector(ch)
    Mtx = np.array([P(O).ravel() for O in ops_basis])
    op_mult[k] = round(np.linalg.matrix_rank(Mtx, tol=1e-8))
ok("T4", op_mult["A1u+"] == 0 and op_mult["A1u−"] == 0 and op_mult["A2g+"] == 0 and op_mult["A2g−"] == 0
   and op_mult["A1g+"] == 4 and op_mult["A1g−"] == 4 and op_mult["A2u+"] == 4 and op_mult["A2u−"] == 4,
   f"operator multiplicities {op_mult}: no A1u or A2g operator exists on the four-state space — "
   "a pure pseudoscalar of the local point group is identically zero there")

# doublet element for each irrep component of the operator space
def doublet(O): return Psi1 @ O @ Psi2
sel = {}
for k, ch in irreps.items():
    if op_mult[k] == 0: continue
    P = op_projector(ch)
    vals = [abs(doublet(P(O))) for O in ops_basis]
    sel[k] = max(vals) > 1e-8
ok("T5a", sel == {"A1g+": False, "A1g−": True, "A2u+": True, "A2u−": False},
   f"doublet element nonzero only for operators in {[k for k, s in sel.items() if s]}")
s_hat = np.diag([1, 1, -1, -1])           # charge-sign operator ŝ ⊗ 1
pos_par = np.diag([1, -1, 1, -1])         # 1 ⊗ (|v><v| − |v'><v'|)
lab = lambda O: [k for k, ch in irreps.items() if op_mult[k] and np.allclose(op_projector(ch)(O), O)]
ok("T5b", lab(s_hat) == ["A1g−"] and abs(doublet(s_hat) - 1) < TOL,
   f"ŝ ⊗ 1 ∈ {lab(s_hat)}, ⟨Ψ⁽¹⁾|ŝ|Ψ⁽²⁾⟩ = {doublet(s_hat):+.3f}   (case (c): the charge sign)")
ok("T5c", lab(pos_par) == ["A2u+"] and abs(doublet(pos_par) - 1) < TOL,
   f"1 ⊗ (v-parity) ∈ {lab(pos_par)}, ⟨Ψ⁽¹⁾|·|Ψ⁽²⁾⟩ = {doublet(pos_par):+.3f}   (an operator that tells v from v′)")
ok("T5d", lab(s_hat @ pos_par) == ["A2u−"] and abs(doublet(s_hat @ pos_par)) < TOL,
   f"ŝ ⊗ (v-parity) ∈ {lab(s_hat @ pos_par)} = C-W46's literal 'A2u, ζ-odd': doublet element {doublet(s_hat @ pos_par):+.3f}")

# ---------------------------------------------------------------- T6 (F3)
E_plus_v, E_minus_vp = s_hat[0, 0], s_hat[3, 3]
mixing = np.abs(s_hat - np.diag(np.diag(s_hat))).max()
ok("T6", mixing < TOL and abs(0.5 * (E_plus_v - E_minus_vp) - doublet(s_hat)) < TOL,
   "ŝ is diagonal in the configuration basis: ⟨Ψ⁽¹⁾|ŝ|Ψ⁽²⁾⟩ = ½[E(+,v) − E(−,v′)]; a diagonal split, no mixing")

# ---------------------------------------------------------------- T7 (0936 table from the group)
f = lambda uhat: uhat @ n_hat
E_b = np.diag([f(u_hat), f(u_R1), f(u_hat), f(u_R1)])                 # placement, R1
E_c = np.diag([+f(u_hat), +f(u_R1), -f(u_hat), -f(u_R1)])             # orientation, R1 (d̂ = s û)
ok("T7", lab(E_b) == ["A1g+"] and abs(doublet(E_b)) < TOL
   and lab(E_c) == ["A1g−"] and abs(doublet(E_c) + 1 / (2 * PHI)) < TOL,
   f"R1: placement ∈ {lab(E_b)} doublet {doublet(E_b):+.4f}; orientation ∈ {lab(E_c)} doublet {doublet(E_c):+.4f} = −1/(2φ)")

n = sum(results); print(f"\n{n}/{len(results)}")
sys.exit(0 if n == len(results) else 1)
