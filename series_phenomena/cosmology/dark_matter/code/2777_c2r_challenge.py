#!/usr/bin/env python3
"""C2R verification challenge (Patch 2777): prints ONE distinguishing
quantity for VERIFIED-EXECUTED authentication. The expected value is
committed NOWHERE (no record, no packet, no pasted output) -- a seat
reporting it correctly must have executed this script. Worker
re-verifies by re-running at adjudication.
Quantity: corrected-operator (C2R-L2, committed reading) envelope
length on A0 FCC ball R=7 in the CHALLENGE window [0.60, 1.50] fm
(deliberately none of the three frozen windows). Deterministic.
"""
import math, numpy as np
PHI=(1+math.sqrt(5))/2; L_EDGE=0.589/PHI
KAPPA=2.0/L_EDGE; ALPHA=L_EDGE/(math.pi*math.sqrt(2))
pts=[]; R=7
for i in range(-2*R,2*R+1):
    for j in range(-2*R,2*R+1):
        for k in range(-2*R,2*R+1):
            if (i+j+k)%2==0:
                x=np.array([i,j,k])/math.sqrt(2.0)
                if np.linalg.norm(x)<=R: pts.append(x)
P=np.array(pts)*L_EDGE
src=int(np.argmin(np.linalg.norm(P-P.mean(0),axis=1)))
mask=np.ones(len(P),bool); mask[src]=False
Q=P[mask]; r0=np.linalg.norm(Q-P[src],axis=1)
D=np.linalg.norm(Q[:,None,:]-Q[None,:,:],axis=2); np.fill_diagonal(D,np.inf)
Gt=(1.0-np.exp(-KAPPA*D))/D; np.fill_diagonal(Gt,KAPPA)
phi=np.linalg.solve(np.eye(len(Q))+ALPHA*Gt, 1.0/r0)
bins=np.arange(0.3,2.4,0.05); rc,fab=[],[]
for b in bins:
    m=(r0>=b)&(r0<b+0.05)
    if m.sum()>=3: rc.append(r0[m].mean()); fab.append(np.abs(phi[m]).mean())
rc,fab=np.array(rc),np.array(fab)
w=(rc>=0.60)&(rc<=1.50)
c=np.polyfit(rc[w],np.log(fab[w]*rc[w]),1)
print(f"CHALLENGE VALUE: l_L2(A0, R=7, window [0.60,1.50] fm) = {-1.0/c[0]:.4f} fm")
