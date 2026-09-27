#!/usr/bin/env python3
"""4309 -- the filling rule as whole DI-bits: each sub-moment a DI-bit steps to one of its neighbours with an OUTWARD
component, chosen at random with equal probability (the whole-bit form of R-OUTWARD-FANOUT's equal shares).  It fills
every outward GP in the average, never beams.  Landing after L unit steps: mean radius and relative spread."""
import numpy as np
phi=(1+5**0.5)/2
ico=np.array([(0,a,b*phi) for a in (1,-1) for b in (1,-1)]+[(a,b*phi,0) for a in (1,-1) for b in (1,-1)]+[(b*phi,0,a) for a in (1,-1) for b in (1,-1)],float)
D=ico/np.linalg.norm(ico,axis=1)[:,None]; rng=np.random.default_rng(3); M=20000
X=rng.normal(size=(M,3)); X/=np.linalg.norm(X,axis=1)[:,None]; X*=1e-3
print(f"{'steps L':>8} {'<r>/L':>7} {'rms/<r>':>9} {'x sqrt(L)':>10}")
for step in range(1,3001):
    rhat=X/np.linalg.norm(X,axis=1)[:,None]; gain=rhat@D.T
    allowed=gain>0; u=rng.random((M,12))*allowed; pick=u.argmax(1)   # uniform among outward neighbours
    X=X+D[pick]
    if step in (10,100,1000,3000):
        r=np.linalg.norm(X,axis=1); f=r.std()/r.mean(); print(f"{step:8d} {r.mean()/step:7.4f} {f:9.4f} {f*np.sqrt(step):10.3f}")
print("-> the shell is solid in the average (every outward GP reachable), the landing radius is a fixed fraction c0 of the")
print("   summed path, and the relative band width falls as 1/sqrt(L): at L ~ 1e30 GP steps it is ~1e-15.")
print("   crowding: whole DI-bits fill shells solid out to r = sqrt(N/4 pi) GPs (= 4304's PSR_min), then thin to one per")
print("   (4 pi r^2/N) GPs -- 'solid' beyond that only in the average, i.e. by re-radiation over Moments.")
# asymptote: mean progress per step in a fixed direction u = average of (d.u) over neighbours with d.u > 0
U=rng.normal(size=(200000,3)); U/=np.linalg.norm(U,axis=1)[:,None]; G=U@D.T; Gp=np.where(G>0,G,0); g=Gp.sum(1)/(G>0).sum(1)
print(f"direction-dependent mean progress per step: spans {g.min():.4f}..{g.max():.4f}, mean {g.mean():.4f}, rms/mean = {g.std()/g.mean():.4f}")
X=rng.normal(size=(3000,3)); X/=np.linalg.norm(X,axis=1)[:,None]; X*=1e-3
for step in range(1,30001):
    rhat=X/np.linalg.norm(X,axis=1)[:,None]; gain=rhat@D.T; allowed=gain>0; u=rng.random((3000,12))*allowed; X=X+D[u.argmax(1)]
    if step in (10000,30000):
        r=np.linalg.norm(X,axis=1); print(f"{step:8d} {r.mean()/step:7.4f} {r.std()/r.mean():9.4f}")
print("-> the band width settles at the direction-anisotropy floor, a fixed fraction independent of the GP count.")
