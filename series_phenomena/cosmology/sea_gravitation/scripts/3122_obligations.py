#!/usr/bin/env python
"""Patch 3122 -- numerical demonstrations for the obligations note."""
import numpy as np
PHI = (1+5**0.5)/2; ALPHA = 1/137.035999; ALPHA_S = 5/(8*PHI)
k = (ALPHA_S/ALPHA)**0.5
rng = np.random.default_rng(7)

# A. D-CHAN-ADD: single-driver two-register variance
d = rng.standard_normal(200000)
src = d + k*d                      # one displacement drives both registers
print(f"(A) Var(delta + k*delta)/Var(delta) = {src.var()/d.var():.4f}"
      f"  vs (1+k)^2 = {(1+k)**2:.4f}   [COHERENT, machine-exact]")
# cross-dipole incoherence: independent drivers, random signs
N = 200000
a, b = rng.standard_normal(N), rng.standard_normal(N)
print(f"    cross-dipole term <a*b> = {np.mean(a*b):+.5f} -> 0 (N^-1/2 = {N**-0.5:.4f})")

# B. OBL-ARC-FIELD: arc-term magnitude probe at the frozen spacing
import importlib.util
spec = importlib.util.spec_from_file_location(
    "m", __file__.replace("3122_obligations", "3120_ds_indep_campaign"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
# lightweight replica of the field block, 300 Moments, n=3, ds=2.45
ds, n_side, seed, T = 2.45, 3, 5, 300
r_ = np.random.default_rng(seed)
Np = n_side**3; Nc = 2*Np; L = n_side*ds
grid = np.array([[i,j,kk] for i in range(n_side) for j in range(n_side)
                 for kk in range(n_side)], float)*ds + ds/2
X = np.repeat(grid, 2, axis=0) + r_.normal(0, 0.3, (Nc,3))
q = np.tile([1.0,-1.0], Np); qq = np.outer(q,q)
partner = np.arange(Nc); partner[0::2]+=1; partner[1::2]-=1
Gcp = np.repeat(np.where(np.arange(Np)%2==1, 52.94, 1.0), 2)
Disp = np.zeros((Nc,3)); idx = np.arange(Nc)
ratios = []
for t in range(T):
    D = X[:,None,:]-X[None,:,:]; D -= L*np.round(D/L)
    r = np.sqrt(np.einsum('ijk,ijk->ij',D,D)); np.fill_diagonal(r,1.0)
    co = r<1e-6; rs = np.where(co,1.0,r); re = np.maximum(rs,1.0)
    F = np.einsum('ij,ijk->ik', np.where(co,0.0,qq/(re**2*rs)), D)
    nv = np.sqrt(np.einsum('ij,ij->i',Disp,Disp))
    Vc = Disp/np.maximum(nv,1.0)[:,None]
    Bk = np.where(co,0.0,1.0/re**2)[:,:,None]*np.cross(Vc[None,:,:]*q[None,:,None], D/rs[:,:,None])
    np.einsum('iik->ik',Bk)[:] = 0.0
    Fm = q[:,None]*np.cross(Vc, Bk.sum(axis=1))
    fld = q[:,None]*r_.normal(0,0.30,(Nc,3))
    Ftot = F + Fm + fld
    if t > 50:
        ratios.append(np.mean(np.sqrt(np.einsum('ij,ij->i',Fm,Fm)))
                      / np.mean(np.sqrt(np.einsum('ij,ij->i',Ftot,Ftot))))
    Disp = Ftot.copy(); X = (X+Ftot)%L
print(f"(B) arc-term weight |F_arc|/|F_total| at d_s=2.45: {np.mean(ratios):.4f}")

# C. OBL-K-SENS
sens = 0.5*k/(1+k)
print(f"(C) dln c_Li/dln alpha_s = k/(2(1+k)) = {sens:.4f}; +/-10% alpha_s -> +/-{sens*10:.1f}% c_Li")
