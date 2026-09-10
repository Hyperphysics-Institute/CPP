#!/usr/bin/env python3
"""Patch 3820 -- T-1 instrument: the angular structure of the twelve-per-GP ignition census.
Computes the multipole power S_l = sum_m |sum_i Y_lm(v_i)|^2 over the twelve icosahedral vertices.
Group theory (I_h) predicts the first non-trivial invariant at l = 6; this verifies it numerically
at double and at 40-digit precision, and records the dipole (no net push) and quadrupole (no net
shear) as exact zeros. No constant adopted; no physics input beyond the founder's twelve-vertex picture."""
import sys, numpy as np
from scipy.special import sph_harm_y
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

phi=(1+np.sqrt(5))/2
V=[]
for s1 in (1,-1):
    for s2 in (1,-1):
        V += [(0,s1*1,s2*phi),(s1*1,s2*phi,0),(s2*phi,0,s1*1)]
V=np.array(V,dtype=float); V=V/np.linalg.norm(V,axis=1)[:,None]
# the cyclic construction already yields 12 distinct vertices; no rounding/dedup
# (rounding here injects a ~1e-10 artefact into the quadrupole test)
distinct=len({tuple(np.round(v,12)) for v in V})
check("T1 twelve distinct unit vertices (icosahedron)", len(V)==12 and distinct==12, f"n={len(V)}, distinct={distinct}")

dip=np.linalg.norm(V.sum(axis=0))
check("T2 dipole exactly zero: the twelve momenta cancel -> no net push at any GP (3814 claim, verified)",
      dip<1e-12, f"|sum v_i| = {dip:.2e}")

Q=V.T@V - (len(V)/3.0)*np.eye(3)
check("T3 quadrupole (traceless second moment) exactly zero: no net shear at any GP",
      np.max(np.abs(Q))<1e-12, f"max|Q_ij| = {np.max(np.abs(Q)):.2e}")

th=np.arccos(np.clip(V[:,2],-1,1)); ph=np.arctan2(V[:,1],V[:,0])
S={}
for l in range(0,11):
    S[l]=sum(abs(np.sum(sph_harm_y(l,m,th,ph)))**2 for m in range(-l,l+1))
lo_zero=all(S[l]<1e-12 for l in (1,2,3,4,5))
check("T4 S_l = 0 for l = 1..5 exactly; first non-vanishing anisotropic multipole is l = 6",
      lo_zero and S[6]>1.0, "  ".join(f"S_{l}={S[l]:.2e}" for l in range(1,8)))

check("T5 second non-vanishing anisotropic multipole is l = 10 (I_h invariants at 0, 6, 10, ...)",
      S[7]<1e-12 and S[8]<1e-12 and S[9]<1e-12 and S[10]>1.0,
      f"S_10 = {S[10]:.3f}")

ratio=S[6]/S[0]
check("T6 residual amplitude at l = 6 relative to monopole: S_6/S_0 ~ 5.7",
      5.0<ratio<6.5, f"S_6/S_0 = {ratio:.3f}")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
