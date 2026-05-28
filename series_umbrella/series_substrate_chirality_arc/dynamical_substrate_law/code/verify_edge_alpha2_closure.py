#!/usr/bin/env python3
"""
Patch 0613 — edge-aligned alpha_2 (THEO-DSL-7 candidate) CLOSURE verification.

Closes the open computation of OPEN-FP-F1-5 Sequence-2A: the O(delta^2) edge-aligned
substrate-current coefficients in the 2D D_5-invariant subspace span{n_rho, n_edge}
established at THEO-DSL-6 (candidate; Patch 0596).

Method (parallels the vertex-aligned THEO-DSL-5 computation, Patch 0591):
    j_2(v_host) = sum over the 144 directed 2-edge paths v_host -> u_i -> v'  of
                  (e1 . n)(e2 . n)  *  e1
with n = n_rho = v_host  (vertex-aligned cross-check) or
     n = n_edge = (u_1 - v_host)/|u_1 - v_host|  (edge-aligned closure).

The script:
  (1) builds the explicit 120-vertex unit-circumradius 600-cell from first principles;
  (2) REPRODUCES the vertex result alpha_2 = -9/phi^2 with the same code path
      (the mandatory cross-check from the Session-146 handover);
  (3) computes the edge-aligned 2D vector assembly and decomposes it in the
      non-orthogonal basis {n_rho, n_edge}, giving
          alpha_2^(rho)  = 9/(2 phi)  ~ +2.781
          alpha_2^(edge) = 9 phi - 12 ~ +2.562;
  (4) reports the per-path-class (B.1..B.4) decomposition;
  (5) confirms robustness over all 12 choices of the edge neighbour u_1;
  (6) confirms the THEO-DSL-6 prediction that j_2^edge lies in span{n_rho, n_edge}.

RESULT (sign-suspicion resolved): the same machinery that yields the NEGATIVE
vertex coefficient -9/phi^2 yields POSITIVE edge coefficients. The positive sign
is a genuine geometric consequence of the D_5 (not I_h) orbit structure — in
particular the B.2 first-shell-trans class, which vanishes identically at
vertex-aligned (G1.2 perpendicularity), is NON-ZERO at edge-aligned. The reverted
Patch-0605 values 9/(2 phi), 9 phi - 12 were therefore CORRECT.
"""
import numpy as np
import itertools
from fractions import Fraction

phi = (1 + np.sqrt(5)) / 2
ok = True
def check(label, got, want):
    global ok
    p = abs(got - want) < 1e-9
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
assert len(verts) == 120, len(verts)
assert np.allclose(np.linalg.norm(verts, axis=1), 1.0)

def neighbours(i):                       # adjacency: dot == phi/2 (edge length 1/phi)
    d = verts @ verts[i]
    return [j for j in range(120) if j != i and abs(d[j] - phi/2) < 1e-9]

assert all(len(neighbours(i)) == 12 for i in range(120))   # 12-regular, 720 edges

def edge_dir(a, b):
    e = verts[b] - verts[a]
    return e / np.linalg.norm(e)

HOST = 0
vh = verts[HOST]
dots = verts @ vh
S1 = [j for j in range(120) if abs(dots[j] - phi/2) < 1e-9]      # 12 first-shell
assert len(S1) == 12

def shell(vp):
    d = verts[vp] @ vh
    if abs(d - 1) < 1e-9:        return 'B1'   # back to host
    if abs(d - phi/2) < 1e-9:    return 'B2'   # S1
    if abs(d - 0.5) < 1e-9:      return 'B3'   # S2
    if abs(d - 1/(2*phi)) < 1e-9:return 'B4'   # S3
    return None

def j2_by_class(nhat, u1):
    """O(delta^2) assembly  sum_P (e1.n)(e2.n) e1, split by endpoint-shell class."""
    j = {c: np.zeros(4) for c in ('B1', 'B2', 'B3', 'B4')}
    cnt = {c: 0 for c in ('B1', 'B2', 'B3', 'B4')}
    for ui in S1:
        e1 = edge_dir(HOST, ui); w1 = e1 @ nhat
        for vp in neighbours(ui):
            c = shell(vp)
            if c is None: continue
            e2 = edge_dir(ui, vp); w2 = e2 @ nhat
            j[c] += (w1 * w2) * e1; cnt[c] += 1
    return j, cnt

def basis_decomp(vec, n_edge):
    """Solve vec = a_rho n_rho + a_edge n_edge in the non-orthogonal basis."""
    g = vh @ n_edge
    G = np.array([[1.0, g], [g, 1.0]])
    return np.linalg.solve(G, np.array([vec @ vh, vec @ n_edge]))

def as_qphi(x, md=64):
    """Express x ~ p + q*phi with small rationals p,q (for readable closed forms)."""
    best = None
    for q in (Fraction(a, b) for b in range(1, md+1) for a in range(-15*b, 15*b+1)):
        p = x - float(q)*phi
        fp = Fraction(p).limit_denominator(md)
        if abs(float(fp) - p) < 1e-7:
            cost = abs(fp.numerator)+fp.denominator+abs(q.numerator)+q.denominator
            if best is None or cost < best[0]:
                best = (cost, fp, q)
    if not best: return f"{x:+.6f}"
    _, p, q = best
    if q == 0: return f"{p}"
    if p == 0: return f"({q})*phi"
    return f"{p} + ({q})*phi"

# ---------------------------------------------------- (2) VERTEX cross-check
print("== (2) VERTEX-ALIGNED CROSS-CHECK (same code path)  n = v_host ==")
jc, _ = j2_by_class(vh, S1[0])
jv = sum(jc.values())
alpha2_vertex = jv @ vh
perp = np.linalg.norm(jv - alpha2_vertex * vh)
check("alpha_2 (vertex)        = -9/phi^2", alpha2_vertex, -9/phi**2)
print(f"        |component perp to n_rho| = {perp:.2e}  (expect 0 by I_h / THEO-DSL-4)")

# ---------------------------------------------------- (3) EDGE closure
print("\n== (3) EDGE-ALIGNED CLOSURE  n = n_edge = (u_1 - v_host)/|.| ==")
u1 = S1[0]
n_edge = edge_dir(HOST, u1)
check("n_rho . n_edge          = -1/(2phi)", vh @ n_edge, -1/(2*phi))
jce, cnte = j2_by_class(n_edge, u1)
J = sum(jce.values())
a_rho, a_edge = basis_decomp(J, n_edge)
check("alpha_2^(rho)           = 9/(2phi)", a_rho, 9/(2*phi))
check("alpha_2^(edge)          = 9phi - 12", a_edge, 9*phi - 12)
recon = a_rho * vh + a_edge * n_edge
print(f"        |j_2^edge outside span{{n_rho,n_edge}}| = {np.linalg.norm(J-recon):.2e}"
      f"  (expect 0 by THEO-DSL-6)")

# ---------------------------------------------------- (4) per-class table
print("\n== (4) PER-PATH-CLASS DECOMPOSITION (basis {n_rho, n_edge}) ==")
print(f"  {'class':5s} {'#':>3s}   {'coeff n_rho':>18s}   {'coeff n_edge':>18s}")
for c in ('B1', 'B2', 'B3', 'B4'):
    ar, ae = basis_decomp(jce[c], n_edge)
    print(f"  {c:5s} {cnte[c]:3d}   {as_qphi(ar):>18s}   {as_qphi(ae):>18s}")
print(f"  {'TOTAL':5s} {sum(cnte.values()):3d}   {as_qphi(a_rho):>18s}   {as_qphi(a_edge):>18s}")
print("  (note B.2 coeff n_rho = +5/2 is NON-ZERO — contrast vertex B.2 = 0 by G1.2)")

# ---------------------------------------------------- (5) robustness
print("\n== (5) ROBUSTNESS over all 12 edge-neighbour choices of u_1 ==")
R = []
for u1 in S1:
    ne = edge_dir(HOST, u1)
    R.append(basis_decomp(sum(j2_by_class(ne, u1)[0].values()), ne))
R = np.array(R)
check("alpha_2^(rho)  invariant (std~0)", R[:, 0].std(), 0.0)
check("alpha_2^(edge) invariant (std~0)", R[:, 1].std(), 0.0)
print(f"        means: rho={R[:,0].mean():+.6f}, edge={R[:,1].mean():+.6f}")

# ---------------------------------------------------- (6) reference
print("\n== reference: edge alpha_1 (THEO-DSL-6 / Patch 0600) ==")
print(f"        alpha_1^(rho)  = 4/phi^2   = {4/phi**2:+.6f}")
print(f"        alpha_1^(edge) = 2(2+phi)  = {2*(2+phi):+.6f}")
print(f"        ratio alpha_2/alpha_1 per component:"
      f"  rho {a_rho/(4/phi**2):+.4f}   edge {a_edge/(2*(2+phi)):+.4f}")

print("\nRESULT:", "ALL CHECKS PASS" if ok else "FAILURE")
import sys; sys.exit(0 if ok else 1)
