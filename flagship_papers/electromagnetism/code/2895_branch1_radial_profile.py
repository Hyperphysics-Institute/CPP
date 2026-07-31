"""BRANCH 1: DI-bits as travelling conserved entities.
   Does ballistic travel + spherical emission give 1/r^2 ?
   Tested three ways: (a) continuum directions, (b) lattice-binned, (c) 12 FCC rays."""
import numpy as np, math
rng=np.random.default_rng(7)

def emit_dirs(n,mode):
    if mode=="continuum" or mode=="binned":
        v=rng.normal(size=(n,3)); return v/np.linalg.norm(v,axis=1,keepdims=True)
    if mode=="fcc12":
        import itertools
        NN=np.array([d for d in itertools.product((-1,0,1),repeat=3)
                     if sorted(map(abs,d))==[0,1,1]],dtype=float)
        NN/=np.linalg.norm(NN,axis=1,keepdims=True)
        return NN[rng.integers(0,12,size=n)]

def run(mode,T=60,per=20000,c=1.0,bin_lat=False):
    """steady state: emit `per` bits each Moment, all travel ballistically at c"""
    R=[]   # radii of all live bits
    pos=[]
    for t in range(T):
        d=emit_dirs(per,mode)
        pos.append(np.zeros((per,3)))
        for i in range(len(pos)): pos[i]=pos[i]+ (emit_dirs(0,mode) if False else 0)
        # advance all existing bits by c along their own direction
        if t==0:
            dirs=[d]; P=[np.zeros((per,3))]
        else:
            dirs.append(d); P.append(np.zeros((per,3)))
        for i in range(len(P)): P[i]=P[i]+dirs[i]*c
    X=np.vstack(P)
    r=np.linalg.norm(X,axis=1)
    if bin_lat:                      # snap to lattice sites, then recompute radius
        Xl=np.round(X); r=np.linalg.norm(Xl,axis=1)
    return r

print("Steady-state radial density.  Expect rho(r) ~ 1/r^2  => slope -2")
print(f"{'mode':>12} {'slope[5,25]':>13} {'slope[10,40]':>14}")
print("-"*44)
for mode,bl,label in (("continuum",False,"continuum"),
                      ("binned",True,"lattice-binned"),
                      ("fcc12",False,"12 FCC rays")):
    r=run(mode,T=60,per=20000,bin_lat=bl)
    def slope(lo,hi,nb=14):
        edges=np.linspace(lo,hi,nb+1); cnt,_=np.histogram(r,bins=edges)
        mid=0.5*(edges[1:]+edges[:-1]); vol=4*math.pi*mid**2*(edges[1]-edges[0])
        dens=cnt/vol; ok=cnt>30
        return np.polyfit(np.log(mid[ok]),np.log(dens[ok]),1)[0] if ok.sum()>4 else float('nan')
    print(f"{label:>12} {slope(5,25):13.4f} {slope(10,40):14.4f}")
