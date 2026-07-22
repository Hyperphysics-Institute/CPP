#!/usr/bin/env python3
"""C2R-L3 (Patch 2774): one-shot OBS-class sensitivity bracket.

Evaluate ell under the PREMISE-REJECTED site matching alpha' =
alpha/(S_disc*alpha) = 1.611*alpha, exactly once (charter SS2 L3):
baseline point kernel, A0 FCC ball R=7, middle frozen window
[0.55,1.6] fm. Registered alongside the committed 2688 direct
propagation (0.1679 fm) for the bracket quote. No physics claim.
Deterministic; no seeds.
"""
import math, numpy as np

PHI=(1+math.sqrt(5))/2; L_EDGE=0.589/PHI
KAPPA=2.0/L_EDGE; ALPHA=L_EDGE/(math.pi*math.sqrt(2))
APRIME=1.611*ALPHA
print(f"alpha={ALPHA:.6f} fm  alpha'(site-matched, premise-rejected)={APRIME:.6f} fm")

pts=[]
R=7
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
phi=np.linalg.solve(np.eye(len(Q))+APRIME/D, 1.0/r0)

bins=np.arange(0.3,2.4,0.05); rc,fab=[],[]
for b in bins:
    m=(r0>=b)&(r0<b+0.05)
    if m.sum()>=3: rc.append(r0[m].mean()); fab.append(np.abs(phi[m]).mean())
rc,fab=np.array(rc),np.array(fab)
w=(rc>=0.55)&(rc<=1.6)
c=np.polyfit(rc[w],np.log(fab[w]*rc[w]),1)
y=np.log(fab[w]*rc[w]); yh=np.polyval(c,rc[w])
r2=1-np.sum((y-yh)**2)/np.sum((y-np.mean(y))**2)
neg=(phi[(r0>=0.4)&(r0<=2.0)]<0).mean()
print(f"one-shot: A0 R=7 window [0.55,1.6]: ell(alpha') = {-1.0/c[0]:.4f} fm "
      f"(R2={r2:.3f}, neg-frac={neg:.3f})")
print("committed comparator (2688 L4 direct propagation): 0.1679 fm, R2~0.55")
print("bracket registered OBS-class; no physics claim attaches (charter SS2 L3).")
