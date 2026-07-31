"""What is the BEST achievable isotropy on the FCC lattice?
   Ideal: perfectly uniform continuum directions, snapped to nearest GP.
   That is the floor discreteness imposes -- routing cannot beat it."""
import numpy as np, math, itertools
from collections import defaultdict
rng=np.random.default_rng(41)
# FCC sites: integer triples with even coordinate sum
def gp_cv_from_points(P,r0,tol=0.35):
    v=defaultdict(float)
    for p in P: v[(int(p[0]),int(p[1]),int(p[2]))]+=1.
    vals=[c for (x,y,z),c in v.items() if abs(math.sqrt(x*x+y*y+z*z)-r0)<tol]
    if len(vals)<8: return float('nan'),len(vals)
    a=np.array(vals); return float(a.std()/a.mean()),len(vals)

N=400000
print("IDEAL FLOOR: uniform continuum directions snapped to nearest FCC site")
print(f"{'r':>7} {'nGP':>5} {'ideal CV':>10}   {'softmax b=3':>12}  {'ratio':>7}")
soft={1.414:0.0132,2.449:0.0313,2.828:0.4342,3.162:0.4196,4.0:0.2556,6.0:0.2318,8.0:0.2108}
for r0 in (1.414,2.449,2.828,3.162,4.0,6.0,8.0):
    d=rng.normal(size=(N,3)); d/=np.linalg.norm(d,axis=1,keepdims=True)
    P=d*r0
    # snap to nearest FCC site (even coordinate sum)
    R=np.round(P)
    bad=(R.sum(axis=1)%2!=0)
    # fix parity by shifting the coordinate with largest rounding residual
    res=np.abs(P-R); j=np.argmax(res[bad],axis=1)
    R[np.where(bad)[0],j]+=np.sign(P[bad,j]-R[bad,j])
    cv,n=gp_cv_from_points(R,r0)
    s=soft.get(r0,float('nan'))
    print(f"{r0:7.3f} {n:5d} {cv:10.4f}   {s:12.4f}  {s/cv if cv==cv and cv>0 else float('nan'):7.2f}")
