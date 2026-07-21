#!/usr/bin/env python3
"""FA-SEA-GREEN S2 — the spectrum readout (Patch 2671).

Assembles the discrete Sea response operator derived at S1a-S1c on the
registered I1 graph (120-vertex 600-cell, SS-2 embedding) and reads the
screening length l in fm via the I6 normalization.

Assembly (all inputs derived upstream, zero free parameters):
  - sites: 120 unit-circumradius 600-cell vertices scaled by
    l_unit = 0.589 fm; edge (min chord) = l_unit/phi = l_edge = 0.364 fm
  - operator: M = I + alpha*G, G_ij = 1/r_ij (S1b: site scattering in
    continuum transport; NOT a hop Laplacian)
  - gap: kappa = 2/d_DP, d_DP = l_edge (S1c, INF-S1C-1)
  - coupling: alpha = kappa^2/(4*pi*n), n = sqrt(2)/l_edge^3 (z=12
    FCC packing density -- the 2527 4D->3D density flag is CONSUMED HERE
    and disclosed)
  - source: external point source at one vertex; response on the other
    119 sites; I6: f normalized to 1 at the shell nearest d = 1.15 fm

Readouts: Yukawa fit A*exp(-r/l)/r and pure-exponential fit A*exp(-r/l)
across chord-distance shells; robustness swap: graph-geodesic distances
(S1b mandatory companion). This stage is where candidate values first
appear, per the charter's blind protocol.
"""

import itertools
import math
import numpy as np

PHI = (1 + math.sqrt(5)) / 2
L_UNIT = 0.589  # fm [SS-2]
L_EDGE = L_UNIT / PHI  # 0.364 fm
D_REG = 1.15  # fm [2433 / I6]

# ---------- 600-cell vertices, unit circumradius ----------
verts = []
for signs in itertools.product([0.5, -0.5], repeat=4):
    verts.append(signs)
for i in range(4):
    for s in (1.0, -1.0):
        v = [0.0] * 4
        v[i] = s
        verts.append(tuple(v))
even_perms = [(0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2), (1, 0, 3, 2),
              (1, 2, 0, 3), (1, 3, 2, 0), (2, 0, 1, 3), (2, 1, 3, 0),
              (2, 3, 0, 1), (3, 0, 2, 1), (3, 1, 0, 2), (3, 2, 1, 0)]
base = (PHI / 2, 0.5, 1 / (2 * PHI), 0.0)
seen = set()
for perm in even_perms:
    for s1 in (1, -1):
        for s2 in (1, -1):
            for s3 in (1, -1):
                v = [0.0] * 4
                vals = (s1 * base[0], s2 * base[1], s3 * base[2], 0.0)
                for k in range(4):
                    v[perm[k]] = vals[k]
                t = tuple(round(x, 9) for x in v)
                if t not in seen:
                    seen.add(t)
                    verts.append(t)
V = np.array(verts)
assert len(V) == 120, len(V)
assert np.allclose(np.linalg.norm(V, axis=1), 1.0, atol=1e-9)

# chord distances, physical units
D4 = np.linalg.norm(V[:, None, :] - V[None, :, :], axis=2) * L_UNIT
offdiag = D4[D4 > 1e-9]
dmin = offdiag.min()
assert abs(dmin - L_EDGE) < 1e-6, dmin
deg = int((np.abs(D4 - dmin) < 1e-6).sum(axis=1).mean())
print(f"instrument: |V|=120, min chord = {dmin:.4f} fm = l_edge, degree at edge = {deg}")

# ---------- derived coupling (zero free parameters) ----------
kappa = 2.0 / L_EDGE                       # S1c
n_density = math.sqrt(2.0) / L_EDGE ** 3   # FCC z=12 packing (2527 FLAG)
alpha = kappa ** 2 / (4 * math.pi * n_density)
print(f"kappa = {kappa:.4f} /fm ; alpha = {alpha:.5f} fm "
      f"(= l_edge/(pi*sqrt2) = {L_EDGE/(math.pi*math.sqrt(2)):.5f})")


def readout(D, label):
    """Solve the scattering system and fit the decay length."""
    src = 0
    resp = np.arange(1, 120)
    r0 = D[src, resp]                    # source-to-site distances
    phi_ext = 1.0 / r0
    G = np.zeros((119, 119))
    for a in range(119):
        for b in range(119):
            if a != b:
                G[a, b] = 1.0 / D[resp[a], resp[b]]
    M = np.eye(119) + alpha * G
    phi = np.linalg.solve(M, phi_ext)

    # shell-average
    shells = sorted(set(np.round(r0, 6)))
    rs, fs = [], []
    for s in shells:
        m = np.abs(r0 - s) < 1e-6
        rs.append(s)
        fs.append(phi[m].mean())
    rs, fs = np.array(rs), np.array(fs)

    # I6 normalization: f = 1 at the shell nearest 1.15 fm
    i_reg = int(np.argmin(np.abs(rs - D_REG)))
    f_norm = fs / fs[i_reg]

    pos = f_norm > 0
    # Yukawa-form fit: ln(f*r) linear in r
    cy = np.polyfit(rs[pos], np.log(f_norm[pos] * rs[pos]), 1)
    l_yuk = -1.0 / cy[0] if cy[0] < 0 else float("inf")
    # pure exponential fit
    ce = np.polyfit(rs[pos], np.log(f_norm[pos]), 1)
    l_exp = -1.0 / ce[0] if ce[0] < 0 else float("inf")

    print(f"\n--- {label} ---")
    print("shells (fm) :", np.array2string(rs, precision=3))
    print("f (I6 norm) :", np.array2string(f_norm, precision=4))
    print(f"norm shell  : r = {rs[i_reg]:.3f} fm (nearest to d_reg = {D_REG} fm)")
    print(f"l (Yukawa fit)      = {l_yuk:.4f} fm   beta_d = d_reg/l = {D_REG/l_yuk:.4f}")
    print(f"l (pure-exp fit)    = {l_exp:.4f} fm   beta_d = d_reg/l = {D_REG/l_exp:.4f}")
    print(f"reference lengths   : l_unit (cell) = {L_UNIT:.4f} fm ; "
          f"l_edge = {L_EDGE:.4f} fm ; l_edge/2 = {L_EDGE/2:.4f} fm ; "
          f"1/kappa = {1/kappa:.4f} fm")
    return l_yuk, l_exp


# ---------- primary: 4D chord distances (2527 flag disclosed) ----------
l1, l1e = readout(D4, "PRIMARY: 4D chord distances")

# ---------- robustness: graph-geodesic distances ----------
A = (np.abs(D4 - dmin) < 1e-6).astype(float)
INF = 1e9
Dg = np.where(A > 0, 1.0, INF)
np.fill_diagonal(Dg, 0.0)
for k in range(120):  # Floyd-Warshall
    Dg = np.minimum(Dg, Dg[:, k][:, None] + Dg[k, :][None, :])
Dg = Dg * L_EDGE
l2, l2e = readout(Dg, "ROBUSTNESS: graph-geodesic distances")

print("\n=== S2 READOUT SUMMARY ===")
print(f"primary   : l_yukawa = {l1:.4f} fm, l_exp = {l1e:.4f} fm")
print(f"robustness: l_yukawa = {l2:.4f} fm, l_exp = {l2e:.4f} fm")
