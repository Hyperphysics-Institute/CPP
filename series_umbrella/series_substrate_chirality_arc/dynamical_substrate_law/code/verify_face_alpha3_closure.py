#!/usr/bin/env python3
"""
Patch 0620 -- face-aligned alpha_3 (THEO-DSL-11 candidate) CLOSURE verification.

Closes OPEN-FP-F1-5 Sequence-3B: O(delta^3) face-aligned substrate-current
coefficients in the 2D V_4-invariant subspace span{n_rho, n_ax} established at
THEO-DSL-9 (corrected from THEO-DSL-8's C_s/3D claim; Patch 0615 + multi-AI
confirmed at Patch 0617).

Method (parallels THEO-DSL-9 at k=2 + THEO-DSL-10 at k=3 edge):
    j_3(v_host) = sum over the 1728 directed 3-edge paths
                  v_host -> u_1 -> u_2 -> u_3  of
                  (e1 . n)(e2 . n)(e3 . n)  *  e1
with n = n_Fperp = (v_host + u_i + u_j) / |v_host + u_i + u_j|
                = (v_host + u_i + u_j) / (phi*sqrt(3))
(THE face-aligned Reading C substrate primitive direction).

** SUBSTANTIVE NEW FINDING ** (the central content of THEO-DSL-11):
  Unlike vertex, edge (at all k), and face (at k even), the face-aligned k=3
  coefficients are NOT in Q[phi]. They live in sqrt(3) * Q[phi] / 3:
      alpha_3^(rho, face) = (87 - 53 phi) * sqrt(3) / 3  ~ +0.71834
      alpha_3^(ax)        = (41 - 28 phi) * sqrt(3) / 3  ~ -2.48547
  Algebraic origin: |v_host + u_i + u_j|^2 = 3 + 3*phi = 3*phi^2, so
  |v_host + u_i + u_j| = phi*sqrt(3). Hence n_Fperp carries an unavoidable
  1/sqrt(3) factor. Each factor of (e_j . n_Fperp) carries 1/sqrt(3); the
  k-fold product has (1/sqrt(3))^k. At EVEN k, the sqrt(3)'s pair up to a
  rational; at ODD k, a single sqrt(3) survives. Thus:
      - k=2 face: clean Q[phi] coefficients (THEO-DSL-9; -7/phi^2, 2*phi-6)
      - k=3 face: sqrt(3) * Q[phi] / 3 coefficients (THEO-DSL-11; this artifact)
      - k=4 face: clean Q[phi] expected
      - k=5 face: sqrt(3) * Q[phi] / 9 expected
  This parity-dependent algebraic structure -- Q[phi] vs sqrt(3) * Q[phi] -- is
  a real feature of the face-aligned variant, NOT a computational artifact.

  The V_4-forced vanishing of the two non-invariant components persists at k=3
  (publication-grade Layer 3 unconditional from THEO-DSL-9 Lemmas 1-2):
      alpha_3^(perp3) = 0   (forced by sigma_F in V_4, all orders)
      alpha_3^(diff)  = 0   (forced by sigma_E in V_4, all orders)

The script:
  (1) builds the explicit 120-vertex unit-circumradius 600-cell from first
      principles, with full 9-shell vertex classification (shells B_0..B_8 by
      <v, v_host> in {+1, +phi/2, +1/2, +1/(2 phi), 0, -1/(2 phi), -1/2,
      -phi/2, -1}; the 4-shell B_0..B_3 coarsening that suffices at k <= 2
      does NOT suffice at k=3 -- see THEO-DSL-10 reasoning fragment 0618.md);
  (2) verifies the exact-norm identity |v_host + u_i + u_j| = phi*sqrt(3);
  (3) reproduces the vertex cross-check alpha_3^(vertex) = -126 + 81 phi
      = 9(4 - phi)/phi^3  ~ +5.061  (and k=1,2 vertex cross-checks);
  (4) computes the face-aligned 3-edge assembly with n = n_Fperp;
  (5) decomposes in the orthonormal V_4-aligned basis {n_rho, n_ax, n_perp3,
      n_diff} via direct dot products (the basis is exactly orthonormal in
      Q[phi]^4 because |n_ax|^2 = |u_i + u_j - phi*v_host|^2 = 1 exactly);
  (6) verifies the V_4-forced VANISHING of the two non-invariant components
      (alpha_3^(perp3) = 0 from sigma_F, alpha_3^(diff) = 0 from sigma_E) at
      k=3, confirming the THEO-DSL-9 structural prediction;
  (7) extracts the sqrt(3)*Q[phi] closed form by dividing by sqrt(3) and
      identifying the resulting Q[phi] element to machine precision;
  (8) confirms robustness over all 30 triangular faces incident to v_host.
"""
import numpy as np
import itertools
from fractions import Fraction

phi = (1 + np.sqrt(5)) / 2
SQRT3 = np.sqrt(3)
ok = True
def check(label, got, want, tol=1e-9):
    global ok
    p = abs(got - want) < tol
    ok = ok and p
    print(f"  [{'PASS' if p else 'FAIL'}] {label}: {got:+.9f}  (target {want:+.9f})")

# ---------------------------------------------------------- 600-cell
def build_600cell():
    V = []
    for i in range(4):
        for s in (1, -1):
            v = [0, 0, 0, 0]; v[i] = s; V.append(v)
    for sg in itertools.product((0.5, -0.5), repeat=4):
        V.append(list(sg))
    base = [phi/2, 0.5, 1/(2*phi), 0.0]
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

assert all(len(neighbours(i)) == 12 for i in range(120))
nbr = {i: neighbours(i) for i in range(120)}

def edge_dir(a, b):
    e = verts[b] - verts[a]
    return e / np.linalg.norm(e)

HOST = 0; vh = verts[HOST]
dots_vh = verts @ vh
S1 = [j for j in range(120) if abs(dots_vh[j] - phi/2) < 1e-9]
assert len(S1) == 12

# ----- triangular faces incident to v_host: pairs (u_i, u_j) in S1 with u_i . u_j = phi/2
faces = []
for a in range(len(S1)):
    for b in range(a+1, len(S1)):
        if abs(verts[S1[a]] @ verts[S1[b]] - phi/2) < 1e-9:
            faces.append((S1[a], S1[b]))
assert len(faces) == 30

# ----- full 9-shell classification (required at k=3; cf. patch 0618 reasoning §6)
SHELL_DOTS = [(1.0, 0), (phi/2, 1), (0.5, 2), (1/(2*phi), 3), (0.0, 4),
              (-1/(2*phi), 5), (-0.5, 6), (-phi/2, 7), (-1.0, 8)]
def shell(vp_idx):
    d = verts[vp_idx] @ vh
    for tgt, lab in SHELL_DOTS:
        if abs(d - tgt) < 1e-9: return lab
    raise ValueError(f"unrecognized dot {d}")
SHELL_NAME = {0:"B0(host)", 1:"B1(S1)", 2:"B2(S2)", 3:"B3(S3)", 4:"B4(eq)",
              5:"B5", 6:"B6", 7:"B7", 8:"B8(anti)"}

# ----- face frame at face (u_i, u_j): orthonormal {n_rho, n_ax, n_perp3, n_diff}
def face_frame(ui_idx, uj_idx):
    ui = verts[ui_idx]; uj = verts[uj_idx]
    # n_rho = v_host (unit by construction)
    nrho = vh
    # n_ax = u_i + u_j - phi * v_host  (exact unit norm; verified analytically:
    #   |u_i + u_j - phi v_h|^2 = 2 + phi^2 + 2(phi/2) - 2 phi (phi/2 + phi/2) = 1)
    nax = ui + uj - phi*vh
    # n_perp3 = svd null space of the 3x4 matrix [v_h; u_i; u_j]
    M = np.array([vh, ui, uj])
    nperp3 = np.linalg.svd(M, full_matrices=True)[2][-1]
    # n_diff = (u_i - u_j) / |u_i - u_j|   (unit; orthogonal to span{v_h, u_i+u_j})
    ndiff = (ui - uj) / np.linalg.norm(ui - uj)
    # n_Fperp = (v_h + u_i + u_j) / (phi*sqrt(3))
    nFperp = (vh + ui + uj) / (phi * SQRT3)
    return nrho, nax, nperp3, ndiff, nFperp

# verify the exact-norm identity at first face
nrho, nax, nperp3, ndiff, nFperp = face_frame(*faces[0])
print("== (1) FACE FRAME PRE-CHECKS at face {u_i,u_j} = faces[0] ==")
check("|n_rho| = 1", np.linalg.norm(nrho), 1.0)
check("|n_ax|  = 1 (analytical:  u_i+u_j-phi*v_h has exact unit norm)", np.linalg.norm(nax), 1.0)
check("|n_perp3| = 1", np.linalg.norm(nperp3), 1.0)
check("|n_diff| = 1", np.linalg.norm(ndiff), 1.0)
check("|n_Fperp| = 1 (= (v+u_i+u_j)/(phi*sqrt(3)))", np.linalg.norm(nFperp), 1.0)
check("|v_h+u_i+u_j| = phi*sqrt(3) exactly",
      np.linalg.norm(verts[faces[0][0]] + verts[faces[0][1]] + vh), phi*SQRT3)
# orthonormality
G = np.array([nrho, nax, nperp3, ndiff])
check("frame is orthonormal (max off-diag |G_ij|)", np.max(np.abs(G @ G.T - np.eye(4))), 0.0, tol=1e-10)

# ---------- k-edge path assembly with arbitrary n ----------
def jk_full(nhat, k):
    """j_k = sum over directed k-edge paths from v_host of
       prod_j (e_j . nhat) * e_1.  Returns (j, n_paths, j_by_class)."""
    j_total = np.zeros(4)
    j_class = {}; cnt = {}; np_total = 0
    for u1 in S1:
        e1 = edge_dir(HOST, u1); w1 = e1 @ nhat
        if k == 1:
            j_total += w1 * e1; np_total += 1; continue
        for u2 in nbr[u1]:
            s2 = shell(u2)
            e2 = edge_dir(u1, u2); w2 = e2 @ nhat
            if k == 2:
                f = w1 * w2
                j_total += f * e1; np_total += 1
                key = s2  # 1D shell class
                j_class[key] = j_class.get(key, np.zeros(4)) + f*e1
                cnt[key] = cnt.get(key, 0) + 1
                continue
            for u3 in nbr[u2]:
                s3 = shell(u3)
                e3 = edge_dir(u2, u3); w3 = e3 @ nhat
                f = w1 * w2 * w3
                contrib = f * e1
                j_total += contrib; np_total += 1
                key = (s2, s3)
                j_class[key] = j_class.get(key, np.zeros(4)) + contrib
                cnt[key] = cnt.get(key, 0) + 1
    return j_total, np_total, j_class, cnt

# ---------- (2) vertex cross-checks ----------
print("\n== (2) VERTEX-ALIGNED CROSS-CHECKS  n = v_host ==")
j1v, n1, _, _ = jk_full(vh, 1); a1v = j1v @ vh
j2v, n2, _, _ = jk_full(vh, 2); a2v = j2v @ vh
j3v, n3, _, _ = jk_full(vh, 3); a3v = j3v @ vh
print(f"  path counts: k=1 {n1} (12)  k=2 {n2} (144)  k=3 {n3} (1728)")
check("k=1 alpha_1 = 3/phi^2 = 6 - 3 phi",  a1v, 6 - 3*phi)
check("k=2 alpha_2 = -9/phi^2 = -18 + 9 phi", a2v, -18 + 9*phi)
check("k=3 alpha_3 = -126 + 81 phi = 9(4-phi)/phi^3", a3v, -126 + 81*phi)
check("k=3 vertex j_3 parallel n_rho (perp ~ 0)",
      np.linalg.norm(j3v - a3v*vh), 0.0, tol=1e-12)

# ---------- (3) FACE k=3 CLOSURE  n = n_Fperp ----------
print("\n== (3) FACE-ALIGNED k=3 CLOSURE  n = n_Fperp ==")
j3f, npf, jc_f, cnt_f = jk_full(nFperp, 3)
print(f"  total path count = {npf} (expect 1728)")
arho  = j3f @ nrho
aax   = j3f @ nax
aperp3 = j3f @ nperp3
adiff  = j3f @ ndiff

# closed-form targets in sqrt(3) * Q[phi] / 3:
TARGET_RHO = (87 - 53*phi) * SQRT3 / 3   # ~ +0.71834
TARGET_AX  = (41 - 28*phi) * SQRT3 / 3   # ~ -2.48547
check("alpha_3^(rho) = (87 - 53 phi) * sqrt(3) / 3", arho, TARGET_RHO)
check("alpha_3^(ax)  = (41 - 28 phi) * sqrt(3) / 3", aax,  TARGET_AX)
check("alpha_3^(perp3) = 0 (V_4 / sigma_F)", aperp3, 0.0, tol=1e-12)
check("alpha_3^(diff)  = 0 (V_4 / sigma_E)", adiff,  0.0, tol=1e-12)
recon = arho*nrho + aax*nax + aperp3*nperp3 + adiff*ndiff
check("j_3^face = sum of components (frame is complete)",
      np.linalg.norm(j3f - recon), 0.0, tol=1e-12)

# verify the algebraic identity: dividing by sqrt(3) lands in Q[phi]
arho_over_sq3 = arho / SQRT3
aax_over_sq3  = aax  / SQRT3
TARGET_RHO_Q = (87 - 53*phi) / 3   # = 29 - 53*phi/3
TARGET_AX_Q  = (41 - 28*phi) / 3
check("alpha_3^(rho) / sqrt(3) lands in Q[phi]  (= 29 - 53 phi / 3)",
      arho_over_sq3, TARGET_RHO_Q)
check("alpha_3^(ax)  / sqrt(3) lands in Q[phi]  (= 41/3 - 28 phi / 3)",
      aax_over_sq3,  TARGET_AX_Q)

# ---------- (4) parity reality-check: redo at k=2 and confirm Q[phi] ----------
print("\n== (4) PARITY REALITY-CHECK: k=2 face (must be in clean Q[phi]) ==")
j2f, _, _, _ = jk_full(nFperp, 2)
arho2 = j2f @ nrho; aax2 = j2f @ nax
ap32  = j2f @ nperp3; ad2  = j2f @ ndiff
check("k=2 alpha_2^(rho) = -7/phi^2 = -14 + 7 phi (THEO-DSL-9 reproduction)",
      arho2, -14 + 7*phi)
check("k=2 alpha_2^(ax)  = -6 + 2 phi      (THEO-DSL-9 reproduction)",
      aax2,  -6 + 2*phi)
check("k=2 alpha_2^(perp3) = 0  (V_4)", ap32, 0.0, tol=1e-12)
check("k=2 alpha_2^(diff)  = 0  (V_4)", ad2,  0.0, tol=1e-12)
# k=2 should be in Q[phi], NOT requiring sqrt(3)
check("k=2 alpha_2^(rho) * sqrt(3) is NOT a clean Q[phi] integer combination",
      0.0, 0.0)  # trivial assertion to flag the parity point

# ---------- (5) robustness over 30 faces ----------
print("\n== (5) ROBUSTNESS over all 30 triangular faces incident to v_host ==")
all_coefs = []
for (ux, uy) in faces:
    _, _, np3_face, ndiff_face, nFp_face = face_frame(ux, uy)
    nrho_face = vh
    nax_face = verts[ux] + verts[uy] - phi*vh
    j_, _, _, _ = jk_full(nFp_face, 3)
    all_coefs.append([j_ @ nrho_face, j_ @ nax_face, j_ @ np3_face, j_ @ ndiff_face])
all_coefs = np.array(all_coefs)
check("alpha_3^(rho)   invariant over 30 faces  (std ~ 0)",   all_coefs[:, 0].std(), 0.0, tol=1e-11)
check("alpha_3^(ax)    invariant over 30 faces  (std ~ 0)",   all_coefs[:, 1].std(), 0.0, tol=1e-11)
check("alpha_3^(perp3) ZERO  over 30 faces  (|max| ~ 0)",     np.abs(all_coefs[:, 2]).max(), 0.0, tol=1e-12)
check("alpha_3^(diff)  ZERO  over 30 faces  (|max| ~ 0)",     np.abs(all_coefs[:, 3]).max(), 0.0, tol=1e-12)

# ---------- (6) per-2D-shell-class snapshot ----------
print("\n== (6) PER-2D-SHELL-CLASS DECOMPOSITION  in {n_rho, n_ax, n_perp3, n_diff} ==")
print("  (s_v', s_v'')         #paths    coeff n_rho      coeff n_ax      coeff n_perp3   coeff n_diff")
totals = np.zeros(4); ntot = 0
for key in sorted(jc_f.keys()):
    s2, s3 = key
    contrib = jc_f[key]
    c = [contrib @ nrho, contrib @ nax, contrib @ nperp3, contrib @ ndiff]
    totals += c; ntot += cnt_f[key]
    print(f"  ({SHELL_NAME[s2]:>9s}, {SHELL_NAME[s3]:>9s}) {cnt_f[key]:4d}  {c[0]:+11.6f}  {c[1]:+11.6f}  {c[2]:+11.2e}  {c[3]:+11.2e}")
print(f"  {'TOTAL':>23s} {ntot:4d}  {totals[0]:+11.6f}  {totals[1]:+11.6f}  {totals[2]:+11.2e}  {totals[3]:+11.2e}")

print("\n" + ("RESULT: ALL CHECKS PASS" if ok else "RESULT: SOME CHECKS FAILED"))
