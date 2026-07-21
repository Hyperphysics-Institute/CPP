#!/usr/bin/env python3
"""FA-SEA-GREEN S1a GATE G1 instrument (Patch 2668, fork-blind).

Verifies: the LOSSLESS one-Moment kernel (uniform z=12 shell average,
signal-conserving) has a static resolvent superposition whose scalar
channel falls as 1/r and whose gradient (SSV_net) channel falls as 1/r^2
-- the registered inverse-square behavior.

BLIND-GUARD AUDIT: this script contains NO gap parameter, NO screening
length, NO decay-vs-parameter curve, and NEITHER FA-C3 candidate value.
It tests only the lossless limit demanded by GATE G1.

Instrument proxy: periodic FCC lattice (z=12, isotropic second moment) as
the 3D icosahedral-coordination stand-in; consumes only z=12 + shell
isotropy, the same properties pinned at I1 (2665). 2527 4D->3D
packing-inference flag noted; instrument-level only.

Preregistered PASS bands: scalar exponent p_f = 1 +/- 0.10;
gradient exponent p_g = 2 +/- 0.15, fit window r in [3, 8], box L=48.
"""

import numpy as np
from scipy.sparse import coo_matrix, identity
from scipy.sparse.linalg import cg

L = 48  # periodic box edge (lattice units); FCC sites: i+j+k even

# --- enumerate FCC sites ---
idx = {}
sites = []
for i in range(L):
    for j in range(L):
        for k in range(L):
            if (i + j + k) % 2 == 0:
                idx[(i, j, k)] = len(sites)
                sites.append((i, j, k))
N = len(sites)
print(f"sites N = {N}")

# --- z=12 neighbor vectors: permutations of (+-1, +-1, 0) ---
nbrs = []
for perm in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
    for s1 in (1, -1):
        for s2 in (1, -1):
            v = [0, 0, 0]
            v[perm[0]] = s1
            v[perm[1]] = s2
            nbrs.append(tuple(v))
assert len(nbrs) == 12

rows, cols = [], []
for n, (i, j, k) in enumerate(sites):
    for (di, dj, dk) in nbrs:
        m = idx[((i + di) % L, (j + dj) % L, (k + dk) % L)]
        rows.append(n)
        cols.append(m)
A = coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(N, N)).tocsr()

# lossless kernel K = A/12; static operator M = I - K (signal-conserving,
# zero mode = uniform; neutralizing background handles it)
M = (identity(N) - A / 12.0).tocsr()

# --- neutralized point source at origin ---
src = idx[(0, 0, 0)]
b = np.full(N, -1.0 / N)
b[src] += 1.0

f, info = cg(M, b, rtol=1e-10, maxiter=5000)
assert info == 0, f"CG failed: {info}"
f -= f.mean()  # fix zero mode

# --- shell-average f(r), minimum-image distances ---
coords = np.array(sites, dtype=float)
d = coords - coords[src]
d -= L * np.round(d / L)
r = np.linalg.norm(d, axis=1)

rbins = np.arange(1.0, 14.0, 0.5)
rc, fm = [], []
for lo in rbins:
    m = (r >= lo) & (r < lo + 0.5)
    if m.sum() > 0:
        rc.append(r[m].mean())
        fm.append(f[m].mean())
rc, fm = np.array(rc), np.array(fm)

# subtract far-field offset (periodic box background) via 1/r + B fit on
# the window, then fit pure power law on (fm - B)
win = (rc >= 3.0) & (rc <= 8.0)
X = np.vstack([1.0 / rc[win], np.ones(win.sum())]).T
coef, *_ = np.linalg.lstsq(X, fm[win], rcond=None)
Aamp, B = coef
g = fm - B
mpos = win & (g > 0)
p_f = -np.polyfit(np.log(rc[mpos]), np.log(g[mpos]), 1)[0]

# gradient channel: numerical derivative of shell means
dg = np.gradient(g, rc)
mg = win & (np.abs(dg) > 0)
p_g = -np.polyfit(np.log(rc[mg]), np.log(np.abs(dg[mg])), 1)[0]

print(f"scalar exponent  p_f = {p_f:.4f}   (PASS band 1.00 +/- 0.10)")
print(f"gradient exponent p_g = {p_g:.4f}   (PASS band 2.00 +/- 0.15)")

ok_f = abs(p_f - 1.0) < 0.10
ok_g = abs(p_g - 2.0) < 0.15
print("G1 scalar channel:", "PASS" if ok_f else "FAIL")
print("G1 SSV_net channel:", "PASS" if ok_g else "FAIL")
print("GATE G1:", "ALL PASS" if (ok_f and ok_g) else "FAIL")
