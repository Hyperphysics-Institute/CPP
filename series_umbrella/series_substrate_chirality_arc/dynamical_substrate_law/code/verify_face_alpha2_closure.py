#!/usr/bin/env python3
"""
Patch 0615 -- face-aligned alpha_2 (THEO-DSL-9 candidate) CLOSURE verification
              + anti-erasure correction to THEO-DSL-8 (Patch 0597).

Closes OPEN-FP-F1-5 Sequence-2B: the O(delta^2) face-aligned substrate-current
coefficients, using the SAME Mechanism-A 2-edge-path assembly as the vertex
(THEO-DSL-5) and edge (THEO-DSL-7) closures, with n = n_Fperp (the face-centroid
direction, i.e. the substrate primitive of face-aligned Reading C).

    j_2(v_host) = sum over the 144 directed 2-edge paths v_host -> u_i -> v'  of
                  (e1 . n)(e2 . n)  *  e1                       (n = n_Fperp)

KEY STRUCTURAL FINDING (corrects THEO-DSL-8 / Patch 0597):
  The true residual symmetry of (v_host + n_Fperp) is the Klein four-group
  V_4 = {e, sigma_E, sigma_face, C_2} of ORDER 4, NOT C_s of order 2.
    * sigma_E   : reflection in (u_i - u_j)^perp; swaps u_i<->u_j; fixes n_Fperp.
    * sigma_face: reflection through the 3-flat span{v_host,u_i,u_j}; fixes
                  v_host,u_i,u_j; flips n_perp3 (the normal to that 3-flat);
                  FIXES n_Fperp (because n_Fperp = (v_host+u_i+u_j)/|.| lies in
                  the 3-flat). THEO-DSL-8 line 132 wrongly assumed this element
                  flips n_Fperp.
  All three non-trivial V_4 elements fix the centroid direction n_Fperp, hence
  preserve Mechanism A's rate function. The V_4-invariant subspace of R^4 at
  v_host is therefore the 2D span{n_rho, n_ax}, NOT the 3D (u_i-u_j)^perp:
    * sigma_E   kills the n_diff = (u_i-u_j) direction;
    * sigma_face kills the n_perp3 direction.
  Additionally, THEO-DSL-8's claimed 3-vector basis {n_rho, n_ax, n_Fperp} is
  DEGENERATE: n_Fperp = ((1+phi) n_rho + |P| n_ax)/|.| lies in span{n_rho,n_ax},
  so those three vectors span only 2D (a second, independent error).

  ==> Dimensional-growth pattern across Reading-C variants is 1 -> 2 -> 2
      (I_h -> D_5 -> V_4), NOT the previously-recorded 1 -> 2 -> 3.

RESULT (exact in Q[phi]), in the orthonormal basis {n_rho, n_ax, n_perp3}:
    alpha_2^(rho) = -14 + 7 phi = -7/phi^2   ~ -2.674
    alpha_2^(ax)  =  -6 + 2 phi              ~ -2.764
    alpha_2^(perp3) = 0   (forced by sigma_face in V_4, all orders)
    alpha_2^(diff)  = 0   (forced by sigma_E   in V_4, all orders; = THEO-DSL-8)

The script:
  (1) builds the explicit 120-vertex unit-circumradius 600-cell;
  (2) reproduces the vertex cross-check alpha_2 = -9/phi^2 (mandatory);
  (3) verifies V_4 = {e,sigma_E,sigma_face,C_2} are 600-cell automorphisms that
      fix v_host and n_Fperp, and that the V_4-invariant subspace is 2D;
  (4) computes the face-aligned assembly and decomposes it in {n_rho,n_ax,n_perp3};
  (5) reports the per-shell-class (B.1..B.4) decomposition;
  (6) confirms robustness over all 30 triangular faces incident to v_host;
  (7) confirms n_Fperp is coplanar with {n_rho,n_ax} (the THEO-DSL-8 basis error).
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
def check_bool(label, cond):
    global ok
    ok = ok and bool(cond)
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}: {bool(cond)}")

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

def j2_by_class(nhat):
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

def as_qphi(x, md=64):
    """Express x ~ p + q*phi with small rationals p,q (for readable closed forms)."""
    best = None
    for q in (Fraction(a, b) for b in range(1, md+1) for a in range(-24*b, 24*b+1)):
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
jc, _ = j2_by_class(vh)
jv = sum(jc.values())
alpha2_vertex = jv @ vh
perp = np.linalg.norm(jv - alpha2_vertex * vh)
check("alpha_2 (vertex)        = -9/phi^2", alpha2_vertex, -9/phi**2)
check("vertex j_2 parallel n   (perp ~ 0)", perp, 0.0)

# ---------------------------------------------------- faces incident to host
faces = [(S1[a], S1[b]) for a in range(len(S1)) for b in range(a+1, len(S1))
         if abs(verts[S1[a]] @ verts[S1[b]] - phi/2) < 1e-9]
print(f"\n== triangular faces incident to host: {len(faces)} (expect 30) ==")
check_bool("30 incident faces", len(faces) == 30)

def face_frame(ui, uj):
    nrho = vh.copy()
    ax = verts[ui] + verts[uj] - 2*vh; ax = ax - (ax @ vh)*vh
    nax = ax / np.linalg.norm(ax)
    M = np.array([vh, verts[ui], verts[uj]])
    nperp3 = np.linalg.svd(M)[2][-1]; nperp3 = nperp3 / np.linalg.norm(nperp3)
    nF = vh + verts[ui] + verts[uj]; nF = nF / np.linalg.norm(nF)
    ndiff = verts[ui] - verts[uj]; ndiff = ndiff / np.linalg.norm(ndiff)
    return nrho, nax, nperp3, nF, ndiff

# ----------------------------------------- (3) V_4 residual-symmetry verification
print("\n== (3) RESIDUAL SYMMETRY = V_4 (order 4), correcting THEO-DSL-8 C_s ==")
ui, uj = faces[0]
nrho, nax, nperp3, nF, ndiff = face_frame(ui, uj)
def is_auto(R):
    W = verts @ R.T
    return all(np.any(np.all(np.abs(verts - w) < 1e-9, axis=1)) for w in W)
R_E    = np.eye(4) - 2*np.outer(ndiff, ndiff)     # sigma_E   : flips n_diff
R_face = np.eye(4) - 2*np.outer(nperp3, nperp3)   # sigma_face: flips n_perp3
R_C2   = R_E @ R_face                              # C_2 = sigma_E . sigma_face
check_bool("sigma_E    is a 600-cell automorphism", is_auto(R_E))
check_bool("sigma_face is a 600-cell automorphism", is_auto(R_face))
check_bool("C_2        is a 600-cell automorphism", is_auto(R_C2))
check_bool("sigma_E    fixes v_host & n_Fperp", np.allclose(R_E@vh, vh) and np.allclose(R_E@nF, nF))
check_bool("sigma_face fixes v_host & n_Fperp", np.allclose(R_face@vh, vh) and np.allclose(R_face@nF, nF))
check_bool("C_2        fixes v_host & n_Fperp", np.allclose(R_C2@vh, vh) and np.allclose(R_C2@nF, nF))
# generate the group + invariant-subspace dimension
def group_inv_dim(gens):
    grp = [np.eye(4)]; changed = True
    while changed:
        changed = False
        for g in list(grp):
            for h in gens:
                gh = h @ g
                if not any(np.allclose(gh, x, atol=1e-9) for x in grp):
                    grp.append(gh); changed = True
    Pavg = sum(grp) / len(grp)
    return len(grp), np.linalg.matrix_rank(Pavg, tol=1e-9)
order, dim = group_inv_dim([R_E, R_face])
check_bool("group <sigma_E, sigma_face> has order 4 (V_4)", order == 4)
check_bool("V_4-invariant subspace is 2D (= span{n_rho,n_ax})", dim == 2)

# ----------------------------------------- (7) THEO-DSL-8 basis degeneracy
print("\n== (7) THEO-DSL-8 basis {n_rho,n_ax,n_Fperp} is DEGENERATE (spans 2D) ==")
B3 = np.array([nrho, nax, nF])
check_bool("rank{n_rho,n_ax,n_Fperp} == 2 (not 3)", np.linalg.matrix_rank(B3, tol=1e-9) == 2)
check("n_Fperp . n_perp3 (=> n_Fperp in span{n_rho,n_ax})", nF @ nperp3, 0.0)

# ----------------------------------------- (4) face-aligned closure
print("\n== (4) FACE-ALIGNED CLOSURE  n = n_Fperp,  basis {n_rho,n_ax,n_perp3} ==")
jc, cnt = j2_by_class(nF)
jf = sum(jc.values())
a_rho, a_ax, a_p3 = jf @ nrho, jf @ nax, jf @ nperp3
a_diff = jf @ ndiff
check("alpha_2^(rho)   = -14 + 7 phi (= -7/phi^2)", a_rho, -14 + 7*phi)
check("   cross-form    -7/phi^2", a_rho, -7/phi**2)
check("alpha_2^(ax)    =  -6 + 2 phi", a_ax, -6 + 2*phi)
check("alpha_2^(perp3) =  0  (sigma_face / V_4)", a_p3, 0.0)
check("alpha_2^(diff)  =  0  (sigma_E   / V_4; THEO-DSL-8)", a_diff, 0.0)
recon = a_rho*nrho + a_ax*nax + a_p3*nperp3
check("|j_2^face - reconstruction| ~ 0", np.linalg.norm(jf - recon), 0.0)

# ----------------------------------------- (5) per-shell-class decomposition
print("\n== (5) PER-PATH-CLASS DECOMPOSITION (basis {n_rho, n_ax, n_perp3}) ==")
print("  class   #          coeff n_rho         coeff n_ax        coeff n_perp3")
tot = np.zeros(3)
for c in ('B1', 'B2', 'B3', 'B4'):
    v = jc[c]; cc = np.array([v @ nrho, v @ nax, v @ nperp3]); tot += cc
    print(f"  {c}    {cnt[c]:3d}   {as_qphi(cc[0]):>16s}   {as_qphi(cc[1]):>16s}   {as_qphi(cc[2]):>10s}")
print(f"  TOTAL {sum(cnt.values()):3d}   {as_qphi(tot[0]):>16s}   {as_qphi(tot[1]):>16s}   {as_qphi(tot[2]):>10s}")

# ----------------------------------------- (6) robustness over 30 faces
print("\n== (6) ROBUSTNESS over all 30 incident faces ==")
A = []
for (ui, uj) in faces:
    nrho, nax, nperp3, nF, ndiff = face_frame(ui, uj)
    jc, _ = j2_by_class(nF); jf = sum(jc.values())
    A.append([jf @ nrho, jf @ nax, jf @ nperp3, jf @ ndiff])
A = np.array(A)
check("alpha_2^(rho)  invariant (std~0)", A[:, 0].std(), 0.0)
check("alpha_2^(ax)   invariant (std~0)", A[:, 1].std(), 0.0)
check("alpha_2^(perp3) == 0 over all faces (max|.|~0)", np.abs(A[:, 2]).max(), 0.0)
check("alpha_2^(diff)  == 0 over all faces (max|.|~0)", np.abs(A[:, 3]).max(), 0.0)
print(f"        means: rho={A[:,0].mean():+.6f}, ax={A[:,1].mean():+.6f}")

print("\n" + ("RESULT: ALL CHECKS PASS" if ok else "RESULT: SOME CHECKS FAILED"))
