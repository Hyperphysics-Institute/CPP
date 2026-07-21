#!/usr/bin/env python3
"""S2 readout robustness: lattice-size (R) and fit-window variants for the
envelope decay constant. Instrument-uncertainty band, not FG-BAND."""
import math
import numpy as np

PHI = (1+math.sqrt(5))/2
L_UNIT = 0.589; L_EDGE = L_UNIT/PHI; D_REG = 1.15
alpha = L_EDGE/(math.pi*math.sqrt(2))

def solve(R):
    pts = []
    for i in range(-2*R, 2*R+1):
        for j in range(-2*R, 2*R+1):
            for k in range(-2*R, 2*R+1):
                if (i+j+k) % 2 == 0:
                    x = np.array([i,j,k])/math.sqrt(2.0)
                    if np.linalg.norm(x) <= R:
                        pts.append(x)
    P = np.array(pts)*L_EDGE
    N = len(P)
    src = int(np.argmin(np.linalg.norm(P, axis=1)))
    mask = np.ones(N, bool); mask[src] = False
    Q = P[mask]
    r0 = np.linalg.norm(Q-P[src], axis=1)
    Dm = np.linalg.norm(Q[:,None,:]-Q[None,:,:], axis=2)
    np.fill_diagonal(Dm, np.inf)
    phi = np.linalg.solve(np.eye(N-1)+alpha/Dm, 1.0/r0)
    shells = np.unique(np.round(r0,6))
    rc, fab = [], []
    for s in shells:
        m = np.abs(r0-s) < 1e-6
        rc.append(s); fab.append(np.abs(phi[m]).mean())
    return np.array(rc), np.array(fab), N

def fit(rc, fab, lo, hi):
    w = (rc >= lo) & (rc <= hi)
    c = np.polyfit(rc[w], np.log(fab[w]*rc[w]), 1)
    return -1.0/c[0]

res = []
for R in (7, 9, 11):
    rc, fab, N = solve(R)
    for (lo, hi) in [(0.45, 1.3), (0.55, 1.6), (0.7, 1.8)]:
        if hi < rc.max()*0.85:
            l = fit(rc, fab, lo, hi)
            res.append(l)
            print(f"R={R:2d} (N={N:5d})  window {lo:.2f}-{hi:.2f} fm : "
                  f"l_env = {l:.4f} fm  beta_d = {D_REG/l:.3f}")
res = np.array(res)
print(f"\nband: l_env = {res.mean():.4f} +/- {res.std():.4f} fm  "
      f"(beta_d = {D_REG/res.mean():.2f}; spread = instrument uncertainty)")
print(f"comparators: d_DP/4 = l_edge/4 = {L_EDGE/4:.4f} fm ; "
      f"1/(2*kappa) = {L_EDGE/4:.4f} fm (identical) ; "
      f"l_edge = {L_EDGE:.4f} ; l_unit = {L_UNIT:.4f}")
