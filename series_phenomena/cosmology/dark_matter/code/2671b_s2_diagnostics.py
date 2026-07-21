#!/usr/bin/env python3
"""FA-SEA-GREEN S2 diagnostics (Patch 2671).

D1: spectrum of the assembled operator M = I + alpha*G on the registered
    I1 arena -- is the sign-oscillating field a resonant/near-singular
    resolvent, or benign compactness contamination?
D2: the IDENTICAL derived operator (same alpha, same 1/r couplings, same
    kappa; zero free parameters) on an extended z=12 FCC instrument
    lattice with a genuine asymptotic regime: does a clean exponential
    decay emerge, and with what l?
"""
import itertools, math
import numpy as np

PHI = (1 + math.sqrt(5)) / 2
L_UNIT = 0.589
L_EDGE = L_UNIT / PHI
D_REG = 1.15
kappa = 2.0 / L_EDGE
alpha = L_EDGE / (math.pi * math.sqrt(2))

# ---- rebuild I1 (as in 2671) ----
verts = []
for signs in itertools.product([0.5, -0.5], repeat=4):
    verts.append(signs)
for i in range(4):
    for s in (1.0, -1.0):
        v = [0.0]*4; v[i] = s; verts.append(tuple(v))
even_perms = [(0,1,2,3),(0,2,3,1),(0,3,1,2),(1,0,3,2),(1,2,0,3),(1,3,2,0),
              (2,0,1,3),(2,1,3,0),(2,3,0,1),(3,0,2,1),(3,1,0,2),(3,2,1,0)]
base = (PHI/2, 0.5, 1/(2*PHI), 0.0)
seen = set()
for perm in even_perms:
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                v = [0.0]*4
                vals = (s1*base[0], s2*base[1], s3*base[2], 0.0)
                for k in range(4): v[perm[k]] = vals[k]
                t = tuple(round(x,9) for x in v)
                if t not in seen:
                    seen.add(t); verts.append(t)
V = np.array(verts); assert len(V) == 120
D4 = np.linalg.norm(V[:,None,:]-V[None,:,:], axis=2) * L_UNIT

G = np.zeros((119,119))
resp = np.arange(1,120)
for a in range(119):
    for b in range(119):
        if a != b: G[a,b] = 1.0/D4[resp[a],resp[b]]
M = np.eye(119) + alpha*G
ev = np.linalg.eigvalsh((M+M.T)/2)
print(f"D1: I1 operator spectrum: min = {ev.min():.4f}, max = {ev.max():.4f}, "
      f"negative eigenvalues = {(ev<0).sum()}")
print("    (min << 1 or < 0 => strong multiple-scattering / non-positive "
      "resolvent on the compact arena)")

# ---- D2: extended FCC instrument, same operator, zero free parameters ----
R = 9  # ball radius in nn units
pts = []
for i in range(-2*R, 2*R+1):
    for j in range(-2*R, 2*R+1):
        for k in range(-2*R, 2*R+1):
            if (i+j+k) % 2 == 0:
                x = np.array([i,j,k])/math.sqrt(2.0)  # nn distance = 1
                r = np.linalg.norm(x)
                if r <= R:
                    pts.append(x)
P = np.array(pts) * L_EDGE   # physical units, nn = l_edge
N = len(P)
print(f"D2: extended instrument sites N = {N} (ball R = {R} nn units)")

r_src = np.linalg.norm(P, axis=1)
src = int(np.argmin(r_src))  # site at origin
mask = np.ones(N, bool); mask[src] = False
Q = P[mask]
r0 = np.linalg.norm(Q - P[src], axis=1)
phi_ext = 1.0/r0

diff = Q[:,None,:]-Q[None,:,:]
Dm = np.linalg.norm(diff, axis=2)
np.fill_diagonal(Dm, np.inf)
Gx = 1.0/Dm
Mx = np.eye(N-1) + alpha*Gx
phi = np.linalg.solve(Mx, phi_ext)

# shell-average in radial bins, fit Yukawa form in an interior window
rb = np.arange(0.3, 2.4, 0.1)
rc, fm = [], []
for lo in rb:
    m = (r0 >= lo) & (r0 < lo+0.1)
    if m.sum() > 3:
        rc.append(r0[m].mean()); fm.append(phi[m].mean())
rc, fm = np.array(rc), np.array(fm)
win = (rc >= 0.7) & (rc <= 1.6) & (fm > 0)
cy = np.polyfit(rc[win], np.log(fm[win]*rc[win]), 1)
l_yuk = -1.0/cy[0]
neg = (fm[(rc>=0.5)&(rc<=2.0)] <= 0).sum()
print(f"    sign-negative shells in [0.5,2.0] fm: {neg}")
print(f"    l (Yukawa fit, window 0.7-1.6 fm) = {l_yuk:.4f} fm")
print(f"    beta_d = d_reg/l = {D_REG/l_yuk:.4f}")
print(f"    reference: 1/kappa = {1/kappa:.4f} fm ; l_edge = {L_EDGE:.4f} ; "
      f"l_unit = {L_UNIT:.4f} ; l_edge/2 = {L_EDGE/2:.4f}")
