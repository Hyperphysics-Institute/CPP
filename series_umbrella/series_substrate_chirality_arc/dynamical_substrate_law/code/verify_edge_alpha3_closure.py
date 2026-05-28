#!/usr/bin/env python3
"""
Patch 0618 -- edge-aligned alpha_3 (THEO-DSL-10 candidate) CLOSURE verification.

Extends Sequence-2A to k=3: O(delta^3) edge-aligned substrate-current coefficients
in the 2D D_5-invariant subspace span{n_rho, n_edge} established at THEO-DSL-6
(Patch 0596).

Method (parallels THEO-DSL-5 vertex and THEO-DSL-7 edge at k=2):
    j_3(v_host) = sum over the 1728 directed 3-edge paths
                  v_host -> u_1 -> u_2 -> u_3  of
                  (e1 . n)(e2 . n)(e3 . n)  *  e1
with n = n_rho = v_host  (vertex-aligned cross-check) or
     n = n_edge = (u_1^anchor - v_host)/|u_1^anchor - v_host|  (edge-aligned closure).

At k=3, paths reach up to the equator (B4, dot=0); the full 9-shell vertex
classification (B0..B8, dot in {+1, +phi/2, +1/2, +1/(2phi), 0, -1/(2phi), -1/2,
-phi/2, -1}) is needed to keep the path enumeration unfiltered. (At k<=2 only
B0..B3 are reachable; the shell() coarsening used in Patches 0613/0615 missed
B4..B8 paths, which dominate at k=3.)

Closed-form result (exact in Q[phi]):
    alpha_3^(rho)  = -84 + 54 phi  ~ +3.374
    alpha_3^(edge) = (21 phi - 63)/2 = -63/2 + (21/2) phi  ~ -14.511

The signs are mixed: positive radial, negative along-edge -- distinct from k=2
edge (both positive) and k=2 face (both negative). The mandatory vertex cross-
check at k=3 yields
    alpha_3^(vertex) = -126 + 81 phi = 9(9 phi - 14) = 9(4 - phi)/phi^3 ~ +5.061.

The script:
  (1) builds the explicit 120-vertex unit-circumradius 600-cell from first principles;
  (2) reproduces the vertex cross-check alpha_3 = -126 + 81 phi
      (and k=1 alpha_1 = 3/phi^2 = 6 - 3 phi  and  k=2 alpha_2 = -9/phi^2 = -18 + 9 phi);
  (3) computes the edge-aligned 2D vector assembly and decomposes it in the
      D_5-invariant non-orthogonal basis {n_rho, n_edge};
  (4) reports the per-2D-shell-class B(s2, s3) decomposition over all 9 x 9 cells
      (with empty cells suppressed);
  (5) confirms robustness over all 12 choices of the anchor first-shell edge;
  (6) confirms the THEO-DSL-6 prediction that j_3^edge lies in
      span{n_rho, n_edge} (rank-2 D_5-invariant subspace) at k=3.
"""
import numpy as np
import itertools
from fractions import Fraction

phi = (1 + np.sqrt(5)) / 2
ok = True
def check(label, got, want, tol=1e-9):
    global ok
    p = abs(got - want) < tol
    ok = ok and p
    print(f"  [{'PASS' if p else 'FAIL'}] {label}: {got:+.9f}  (target {want:+.9f})")

# ------------------------------------------------------------------ 600-cell
def build_600cell():
    V = []
    for i in range(4):                                   # 16-cell  (8)
        for s in (1, -1):
            v = [0, 0, 0, 0]; v[i] = s; V.append(v)
    for sg in itertools.product((0.5, -0.5), repeat=4): # tesseract (16)
        V.append(list(sg))
    base = [phi/2, 0.5, 1/(2*phi), 0.0]                  # snub 24-cell (96)
    def even(p):
        p = list(p); c = 0
        for i in range(4):
            for j in range(i+1, 4):
                if p[i] > p[j]: c += 1
        return c % 2 == 0
    for perm in itertools.permutations(range(4)):
        if not even(perm): continue
        for sg in itertools.product((1, -1), repeat=4):
            V.append([base[perm[k]]*sg[k] for k in range(4)])
    U = []
    for v in V:
        if not any(np.allclose(v, u, atol=1e-9) for u in U):
            U.append(v)
    return np.array(U)

verts = build_600cell()
assert len(verts) == 120
assert np.allclose(np.linalg.norm(verts, axis=1), 1.0)

def neighbours(i):
    d = verts @ verts[i]
    return [j for j in range(120) if j != i and abs(d[j] - phi/2) < 1e-9]

assert all(len(neighbours(i)) == 12 for i in range(120))   # 12-regular
nbr = {i: neighbours(i) for i in range(120)}

def edge_dir(a, b):
    e = verts[b] - verts[a]
    return e / np.linalg.norm(e)

HOST = 0
vh = verts[HOST]
dots = verts @ vh
S1 = [j for j in range(120) if abs(dots[j] - phi/2) < 1e-9]
assert len(S1) == 12

# ------------------------------------------------- shell classification (9 shells)
# B0 vh (dot=1), B1 S1 (dot=phi/2), B2 S2 (dot=1/2), B3 S3 (dot=1/(2phi)),
# B4 equator (dot=0), B5 (dot=-1/(2phi)), B6 (dot=-1/2), B7 (dot=-phi/2),
# B8 antipode (dot=-1).
SHELL_DOTS = [(1.0, 0), (phi/2, 1), (0.5, 2), (1/(2*phi), 3), (0.0, 4),
              (-1/(2*phi), 5), (-0.5, 6), (-phi/2, 7), (-1.0, 8)]
def shell(vp_idx):
    d = verts[vp_idx] @ vh
    for tgt, lab in SHELL_DOTS:
        if abs(d - tgt) < 1e-9: return lab
    raise ValueError(f"unrecognized dot product {d}")

SHELL_NAME = {0:"B0(host)", 1:"B1(S1)", 2:"B2(S2)", 3:"B3(S3)", 4:"B4(eq)",
              5:"B5", 6:"B6", 7:"B7", 8:"B8(anti)"}

def j3_by_class(nhat):
    """O(delta^3) assembly  sum_P (e1.n)(e2.n)(e3.n) e1,
       classified by (shell of v', shell of v'')."""
    j_total = np.zeros(4)
    j_class = {}
    cnt = {}
    n_paths = 0
    for u1 in S1:
        e1 = edge_dir(HOST, u1); w1 = e1 @ nhat
        for u2 in nbr[u1]:
            s2 = shell(u2)
            e2 = edge_dir(u1, u2); w2 = e2 @ nhat
            for u3 in nbr[u2]:
                s3 = shell(u3)
                e3 = edge_dir(u2, u3); w3 = e3 @ nhat
                f = w1 * w2 * w3
                contrib = f * e1
                j_total += contrib
                key = (s2, s3)
                j_class[key] = j_class.get(key, np.zeros(4)) + contrib
                cnt[key] = cnt.get(key, 0) + 1
                n_paths += 1
    return j_total, j_class, cnt, n_paths

def as_qphi(x, md=64):
    best = None
    for q in (Fraction(a, b) for b in range(1, md+1) for a in range(-24*b, 24*b+1)):
        p = x - float(q)*phi
        fp = Fraction(p).limit_denominator(md)
        if abs(float(fp) - p) < 1e-9:
            cost = abs(fp.numerator)+fp.denominator+abs(q.numerator)+q.denominator
            if best is None or cost < best[0]:
                best = (cost, fp, q)
    if not best: return f"{x:+.6f}"
    _, p, q = best
    if q == 0: return f"{p}"
    if p == 0: return f"({q})*phi"
    return f"{p} + ({q})*phi"

# ---------------------------------------------------- (2) VERTEX cross-check
print("== (2) VERTEX-ALIGNED CROSS-CHECK at k=3  n = v_host ==")
j3v, _, _, np3v = j3_by_class(vh)
print(f"  total path count = {np3v} (expect 1728 = 12^3)")
alpha3v = j3v @ vh
perp = np.linalg.norm(j3v - alpha3v * vh)
check("alpha_3 (vertex) = -126 + 81 phi", alpha3v, -126 + 81*phi)
check("alternate form  = 9*(4-phi)/phi^3", alpha3v, 9*(4-phi)/phi**3)
check("vertex j_3 parallel n_rho (perp ~ 0)", perp, 0.0, tol=1e-12)

def j_full(nhat, k):
    j = np.zeros(4)
    for u1 in S1:
        e1 = edge_dir(HOST, u1); w1 = e1 @ nhat
        if k == 1:
            j += w1 * e1
        else:
            for u2 in nbr[u1]:
                e2 = edge_dir(u1, u2); w2 = e2 @ nhat
                if k == 2:
                    j += (w1 * w2) * e1
                else:
                    for u3 in nbr[u2]:
                        e3 = edge_dir(u2, u3); w3 = e3 @ nhat
                        j += (w1 * w2 * w3) * e1
    return j
a1v = j_full(vh, 1) @ vh
a2v = j_full(vh, 2) @ vh
check("vertex k=1 cross-check alpha_1 = 3/phi^2 = 6 - 3 phi", a1v, 6 - 3*phi)
check("vertex k=2 cross-check alpha_2 = -9/phi^2 = -18 + 9 phi", a2v, -18 + 9*phi)

# ---------------------------------------------------- (3) EDGE k=3 closure
print("\n== (3) EDGE-ALIGNED k=3 CLOSURE  n = n_edge ==")
def basis_decomp_edge(vec, n_edge):
    g = vh @ n_edge
    G = np.array([[1.0, g], [g, 1.0]])
    return np.linalg.solve(G, np.array([vec @ vh, vec @ n_edge]))

u1 = verts[S1[0]]
n_edge = (u1 - vh) / np.linalg.norm(u1 - vh)
j3e, jc_e, cnt_e, np3e = j3_by_class(n_edge)
print(f"  total path count = {np3e} (expect 1728)")
coef = basis_decomp_edge(j3e, n_edge)
recon = coef[0]*vh + coef[1]*n_edge
check("alpha_3^(rho)  = -84 + 54 phi", coef[0], -84 + 54*phi)
check("alpha_3^(edge) = (21 phi - 63)/2 = -63/2 + (21/2) phi", coef[1], -63/2 + 21*phi/2)
check("j_3^edge in span{n_rho, n_edge} (residual ~ 0)", np.linalg.norm(j3e - recon), 0.0, tol=1e-12)

# ---------------------------------------------------- (4) per-2D-shell-class
print("\n== (4) PER-2D-SHELL-CLASS DECOMPOSITION  basis {n_rho, n_edge} ==")
print("  (s_v', s_v'')           #paths      coeff n_rho           coeff n_edge")
tot = np.zeros(2)
ntot = 0
for key in sorted(jc_e.keys()):
    s2, s3 = key
    cc = basis_decomp_edge(jc_e[key], n_edge); tot += cc; ntot += cnt_e[key]
    print(f"  ({SHELL_NAME[s2]:>9s}, {SHELL_NAME[s3]:>9s})   {cnt_e[key]:4d}    {as_qphi(cc[0]):>20s}    {as_qphi(cc[1]):>20s}")
print(f"  {'TOTAL':>23s}    {ntot:4d}    {as_qphi(tot[0]):>20s}    {as_qphi(tot[1]):>20s}")

# ---------------------------------------------------- (5) robustness over 12 anchors
print("\n== (5) ROBUSTNESS over all 12 first-shell anchor choices ==")
all_coef = []
for ux in S1:
    n_e = (verts[ux] - vh) / np.linalg.norm(verts[ux] - vh)
    j_, _, _, _ = j3_by_class(n_e)
    c_ = basis_decomp_edge(j_, n_e)
    all_coef.append(c_)
all_coef = np.array(all_coef)
check("alpha_3^(rho) invariant (std~0)", all_coef[:, 0].std(), 0.0, tol=1e-11)
check("alpha_3^(edge) invariant (std~0)", all_coef[:, 1].std(), 0.0, tol=1e-11)

print("\n" + ("RESULT: ALL CHECKS PASS" if ok else "RESULT: SOME CHECKS FAILED"))
