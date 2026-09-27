#!/usr/bin/env python3
"""4308 -- founders_voice/4308: a DI-bit steps, each sub-moment, to the neighbour that advances FARTHEST in radius (never
reverses) and stops when its summed edge length equals one PSR.  With no crowding (see below), each DI-bit is an
independent greedy walker.  Landing radius = Euclidean distance after a path length of one PSR.  The band is the spread
of that radius over directions -- a fixed geometric number, with no hop-count dial."""
import numpy as np
phi=(1+5**0.5)/2
ico=np.array([(0,a,b*phi) for a in (1,-1) for b in (1,-1)]+[(a,b*phi,0) for a in (1,-1) for b in (1,-1)]+[(b*phi,0,a) for a in (1,-1) for b in (1,-1)],float)
fcc=np.array([(a,b,0) for a in (1,-1) for b in (1,-1)]+[(a,0,b) for a in (1,-1) for b in (1,-1)]+[(0,a,b) for a in (1,-1) for b in (1,-1)],float)
rng=np.random.default_rng(7); M=4000
U=rng.normal(size=(M,3)); U/=np.linalg.norm(U,axis=1)[:,None]
def greedy(D,steps=3000):
    D=D/np.linalg.norm(D,axis=1)[:,None]          # unit edges: path length = step count
    X=U*1e-3                                       # start displaced along the launch direction (breaks the origin tie)
    for _ in range(steps):
        rhat=X/np.linalg.norm(X,axis=1)[:,None]
        gain=rhat@D.T                              # radial advance offered by each neighbour
        X=X+D[gain.argmax(1)]
    r=np.linalg.norm(X,axis=1)/steps               # Euclidean radius per unit path length
    return r
for name,D in (("icosahedral 12",ico),("FCC 12",fcc)):
    r=greedy(D)
    print(f"{name:16s}: landing radius / PSR spans {r.min():.4f}..{r.max():.4f};  mean {r.mean():.4f};  rms/mean = {r.std()/r.mean():.4f};"
          f"  full range/mean = {(r.max()-r.min())/r.mean():.3f}")
print("-> a fixed, scale-free band: the same at 3000 steps as at 1e30 (each direction's progress per step is constant).")
N_alpha=4*np.pi/137.035999   # alpha's N in units of PSR/s (4301)
print(f"crowding: a volley of N DI-bits fills a one-GP-deep shell at r = sqrt(N/4 pi) GPs; with alpha's N = {N_alpha:.4f} PSR/s")
for R in (1e30,1e32):
    rf=np.sqrt(N_alpha*R/(4*np.pi)); print(f"  R = {R:.0e}: fill radius = {rf:.2e} GPs = {rf/R:.1e} PSR  (= 4304's PSR_min = sqrt(alpha s PSR))")
