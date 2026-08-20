#!/usr/bin/env python3
"""Patch 3234 verify script — Spin III V0.

Four checks, each independent of the committed cpp_spin3_eigenvalues.py
implementation where that is possible:

  1. ANALYTIC + FD REPRODUCTION. Rebuild the open-closed radial FD problem
     from scratch (own matrix construction) and compare eigenvalues against
     the COMMITTED data/spin3_eigenvalues.csv. The committed CSV was also
     regenerated bit-identically from the committed script this session
     (recorded in reasoning/3234.md); this check adds an independent
     construction route.
  2. MODE-2 GEOMETRY. From the independently computed Mode-2 eigenvector:
     interior antinode at R/3, interior node at 2R/3, ratio 2 — the exact
     result the arc rests on.
  3. THE SCALE-BRIDGE IDENTITY. r_in(Spin I)/r_in(Spin II)
     = 6/[4*alpha*(1+sqrt(2))^2] EXACTLY, given a0 = r_C/alpha and
     r_th = r_C/2. Verified as an algebraic identity numerically to 1e-12,
     and against the value 35.267491 quoted in the committed script.
  4. THE PART-3 DIAGNOSIS, MADE REPRODUCIBLE. Rebuild the committed
     24-cell kNN graph Laplacian (same construction, same seed, reduced
     n for runtime) and assert the finding reported in Spin III V0 §5:
     (a) the lowest nontrivial modes form a 4-fold near-degenerate group
         (4D dipole modes of the closed/Neumann-like problem), and
     (b) NO mode among the lowest ten has exactly one interior radial
         sign change under the committed script's own diagnostic —
     i.e. the committed instrument does not (and, solving the closed
     problem, cannot) exhibit the open-closed Mode 2.

Run: python3 3234_verify_spin3_v0.py            (checks 1-3, fast)
     python3 3234_verify_spin3_v0.py --with-p3  (adds check 4, ~1 min)
"""

import argparse
import math
import os
import sys

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "..", "data", "spin3_eigenvalues.csv")

# constants (CODATA, as in the committed script)
HBAR = 1.054571817e-34
C_LT = 2.99792458e8
M_E = 9.1093837015e-31
ALPHA = 7.2973525693e-3
L_P = 1.616255e-35
R_C = HBAR / (M_E * C_LT)
R_TH = R_C / 2.0

passes = []
def check(name, ok, detail=""):
    passes.append((name, ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


# ---------------------------------------------------------------- check 1+2
print("== 1+2. Independent FD reconstruction vs committed CSV; Mode-2 geometry ==")
# Independent construction: the SYMMETRIC lumped-mass Neumann formulation
# (generalized problem M u = k^2 B u with half mass at the Neumann node),
# second-order accurate — a genuinely different route from the committed
# script's plain forward-difference ghost, so agreement is a two-route check.
N = 6000
R = 1.0
h = R / N
main = np.full(N, 2.0) / h**2
off = np.full(N - 1, -1.0) / h**2
main[-1] = 1.0 / h**2                      # stiffness at the free end
M = sp.diags([off, main, off], [-1, 0, 1], format="csr")
bdiag = np.ones(N); bdiag[-1] = 0.5        # lumped half mass at r = R
B = sp.diags(bdiag, format="csr")
vals, vecs = spla.eigsh(M, k=12, M=B, which="SM", tol=1e-14)
order = np.argsort(vals)
k_fd = np.sqrt(np.abs(vals[order]))[:8]
vecs = vecs[:, order]

rows = []
with open(CSV) as f:
    next(f)
    for line in f:
        m, kt, kc, e = line.strip().split(",")
        rows.append((int(m), float(kt), float(kc), float(e)))
k_theory = np.array([r[1] for r in rows])
k_committed = np.array([r[2] for r in rows])

worst_theory = float(np.max(np.abs(k_fd - k_theory) / k_theory))
worst_committed = float(np.max(np.abs(k_fd - k_committed) / k_committed))
check("independent FD vs analytic k_n (<0.02%)", worst_theory < 2e-4,
      f"max rel {worst_theory:.2e}")
check("independent FD vs committed CSV (<0.05%)", worst_committed < 5e-4,
      f"max rel {worst_committed:.2e} (two FD routes, different Neumann ghosts)")

r = np.arange(1, N + 1) * h
psi2 = vecs[:, 1]
# antinode: max |psi| in interior; node: sign change
i_anti = int(np.argmax(np.abs(psi2[: int(0.6 * N)])))
sc = np.where(np.diff(np.sign(psi2)))[0]
r_node = None
for i in sc:
    rr = r[i] + h * abs(psi2[i]) / (abs(psi2[i]) + abs(psi2[i + 1]))
    if 0.1 < rr < 0.95:
        r_node = rr
        break
r_anti = r[i_anti]
check("Mode-2 antinode at R/3", abs(r_anti - 1 / 3) < 2e-3, f"{r_anti:.5f}")
check("Mode-2 node at 2R/3", r_node is not None and abs(r_node - 2 / 3) < 2e-3,
      f"{r_node:.5f}")
ratio = r_node / r_anti
check("r_out/r_in = 2 (exact target)", abs(ratio - 2.0) < 5e-3, f"{ratio:.6f}")

# ---------------------------------------------------------------- check 3
print("\n== 3. Scale-bridge identity ==")
A_BOHR = R_C / ALPHA                      # a0 = r_C / alpha (exact relation)
r_in_I = A_BOHR / (4 * (1 + math.sqrt(2)) ** 2)
r_in_II = R_TH / 3.0
lhs = r_in_I / r_in_II
rhs = 6.0 / (ALPHA * 4 * (1 + math.sqrt(2)) ** 2)
check("r_in(I)/r_in(II) == 6/[4 alpha (1+sqrt2)^2] (1e-12)",
      abs(lhs - rhs) / rhs < 1e-12, f"{lhs:.9f} vs {rhs:.9f}")
check("value matches committed 35.267491", abs(lhs - 35.267491) < 5e-6,
      f"{lhs:.6f}")
corr = (L_P / R_TH) ** 2
check("discreteness bound (l_P/r_th)^2 ~ 7e-45", 6e-45 < corr < 8e-45,
      f"{corr:.3e}")

# ---------------------------------------------------------------- check 4
ap = argparse.ArgumentParser()
ap.add_argument("--with-p3", action="store_true")
args = ap.parse_args()
if args.with_p3:
    print("\n== 4. Part-3 diagnosis (committed instrument, reduced n, same seed) ==")
    # Reproduce the committed construction verbatim in miniature.
    verts = set()
    for i in range(4):
        for j in range(i + 1, 4):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [0, 0, 0, 0]; v[i] = si; v[j] = sj
                    verts.add(tuple(v))
    V = np.array(sorted(verts), dtype=float)
    V /= np.linalg.norm(V[0])
    rng = np.random.default_rng(42)
    n_pts = 6000
    pts = []
    while sum(len(p) for p in pts) < n_pts:
        cands = rng.uniform(-1, 1, size=(n_pts * 8, 4))
        mask = np.max(np.abs(cands @ V.T), axis=1) <= 1.0 + 1e-9
        pts.append(cands[mask])
    pts = np.vstack([np.zeros((1, 4)), np.vstack(pts)[:n_pts]])

    from scipy.spatial import cKDTree
    tree = cKDTree(pts)
    dists, nbrs = tree.query(pts, k=21)
    sigma = np.mean(dists[:, 1]) * 1.5
    n = len(pts)
    rowsI, colsI, w = [], [], []
    for i in range(n):
        for ki in range(1, 21):
            j = nbrs[i, ki]
            rowsI.append(i); colsI.append(j)
            w.append(math.exp(-dists[i, ki] ** 2 / (2 * sigma ** 2)))
    W = sp.csr_matrix((w, (rowsI, colsI)), shape=(n, n))
    W = (W + W.T).multiply(0.5)
    deg = np.array(W.sum(axis=1)).flatten()
    dinv = sp.diags(1.0 / np.sqrt(np.where(deg > 0, deg, 1.0)))
    L = sp.eye(n, format="csr") - dinv @ W @ dinv
    ev, Q = spla.eigsh(L, k=14, which="SM", tol=1e-10)
    m = ev > 1e-8
    ev, Q = np.sort(ev[m])[:10], Q[:, m][:, :10]

    grp = ev[:4]
    spread = (grp.max() - grp.min()) / grp.mean()
    gap = ev[4] / grp.mean()
    check("lowest nontrivial modes: 4-fold near-degenerate dipole group",
          spread < 0.15 and gap > 1.5,
          f"group spread {spread:.2%}, gap ratio {gap:.2f}")

    def radial_profile_zeros(vec):
        rr = np.linalg.norm(pts, axis=1)
        edges = np.linspace(0, rr.max(), 81)
        prof = np.zeros(80); cnt = np.zeros(80)
        bi = np.clip(np.searchsorted(edges, rr) - 1, 0, 79)
        np.add.at(prof, bi, vec); np.add.at(cnt, bi, 1)
        prof[cnt > 0] /= cnt[cnt > 0]
        p = prof[np.abs(prof) > 0.02 * np.max(np.abs(prof))]
        return int(np.sum(np.abs(np.diff(np.sign(p))) > 0))

    zero_counts = [radial_profile_zeros(Q[:, i]) for i in range(10)]
    check("NO mode among lowest 10 with exactly one radial zero "
          "(committed diagnostic)", 1 not in zero_counts,
          f"zero counts {zero_counts}")
else:
    print("\n(check 4 skipped; run with --with-p3)")

# ---------------------------------------------------------------- verdict
print("\n== SUMMARY ==")
n_ok = sum(1 for _, ok in passes if ok)
for name, ok in passes:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"{n_ok}/{len(passes)} checks pass")
sys.exit(0 if n_ok == len(passes) else 1)
