#!/usr/bin/env python3
"""4306 -- a scale-free, positional candidate for the band: a DI-bit that always steps outward reaches, after many
straight steps, a Euclidean radius that depends on direction: the lattice's outward front is N x the convex hull of the
neighbour set; front radius in direction u = N h(u), h(u) = max_d (d . u).  The spread of h over directions is a fixed
geometric number, independent of N (no dial).  Computed for the FCC 12 (pass 3's instrument) and the icosahedral 12
(the founder's, pass 4's lattice)."""
import numpy as np
rng=np.random.default_rng(1); U=rng.normal(size=(400000,3)); U/=np.linalg.norm(U,axis=1)[:,None]
fcc=np.array([(a,b,0) for a in (1,-1) for b in (1,-1)]+[(a,0,b) for a in (1,-1) for b in (1,-1)]+[(0,a,b) for a in (1,-1) for b in (1,-1)],float)
phi=(1+5**0.5)/2; ico=np.array([(0,a,b*phi) for a in (1,-1) for b in (1,-1)]+[(a,b*phi,0) for a in (1,-1) for b in (1,-1)]+[(b*phi,0,a) for a in (1,-1) for b in (1,-1)],float)
for name,D in (("FCC 12 (cuboctahedral)",fcc),("icosahedral 12",ico)):
    D=D/np.linalg.norm(D,axis=1)[:,None]; h=(U@D.T).max(1)
    print(f"{name:24s}: front radius per step spans {h.min():.4f}..{h.max():.4f} of a unit step; rms/mean over directions = {h.std()/h.mean():.4f}  (4 pi alpha = 0.0917)")
print("-> the icosahedral front is far rounder than the FCC one; neither spread is near 0.09 by this measure.")
