#!/usr/bin/env python3
"""S2 envelope examination: shell-resolved field on the extended
instrument; envelope decay fit; oscillation structure registration."""
import math
import numpy as np

PHI = (1 + math.sqrt(5)) / 2
L_UNIT = 0.589; L_EDGE = L_UNIT/PHI; D_REG = 1.15
kappa = 2.0/L_EDGE; alpha = L_EDGE/(math.pi*math.sqrt(2))

R = 9
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
phi_ext = 1.0/r0
Dm = np.linalg.norm(Q[:,None,:]-Q[None,:,:], axis=2)
np.fill_diagonal(Dm, np.inf)
phi = np.linalg.solve(np.eye(N-1) + alpha/Dm, phi_ext)

# exact lattice shells (unique distances), interior only
shells = np.unique(np.round(r0, 6))
print(" r (fm)    f_mean        |f|_mean      sign")
rows = []
for s in shells[shells <= 2.2]:
    m = np.abs(r0-s) < 1e-6
    fmn = phi[m].mean(); fab = np.abs(phi[m]).mean()
    rows.append((s, fmn, fab))
    print(f"{s:7.4f}  {fmn:+.5e}  {fab:.5e}   {'+' if fmn>0 else '-'}")

rows = np.array(rows)
# envelope fit on |f|*r (Yukawa-envelope), interior window
rc, fab = rows[:,0], rows[:,2]
win = (rc >= 0.55) & (rc <= 1.6)
c = np.polyfit(rc[win], np.log(fab[win]*rc[win]), 1)
l_env = -1.0/c[0]
print(f"\nenvelope l (|f|*r fit, 0.55-1.6 fm) = {l_env:.4f} fm")
print(f"beta_d(envelope) = {D_REG/l_env:.4f}")
print(f"references: 1/kappa = {1/kappa:.4f} ; l_edge = {L_EDGE:.4f} ; "
      f"l_unit = {L_UNIT:.4f} ; l_edge/2 = {L_EDGE/2:.4f} ; "
      f"l_unit/2 = {L_UNIT/2:.4f}")
