"""CORRECT observable: a CP sits AT a GP. Compare bit counts ACROSS GPs at the
same radius -- not across solid-angle patches, which at small r contain no
lattice sites at all and register as spurious anisotropy."""
import numpy as np, math, itertools
from collections import defaultdict
rng=np.random.default_rng(37)
NN=np.array([d for d in itertools.product((-1,0,1),repeat=3)
             if sorted(map(abs,d))==[0,1,1]],dtype=float)
NNu=NN/np.linalg.norm(NN,axis=1,keepdims=True)

def route(nbits,R,beta):
    v=rng.normal(size=(nbits,3)); tgt=v/np.linalg.norm(v,axis=1,keepdims=True)*R
    pos=np.zeros((nbits,3)); live=np.ones(nbits,bool)
    visits=defaultdict(float)
    for step in range(int(4*R)+30):
        if not live.any(): break
        idx=np.where(live)[0]
        for p in pos[idx]:
            visits[(int(p[0]),int(p[1]),int(p[2]))]+=1.0
        rem=tgt[idx]-pos[idx]
        rn=rem/np.maximum(np.linalg.norm(rem,axis=1,keepdims=True),1e-12)
        proj=rn@NNu.T
        if beta is None: pick=np.argmax(proj,axis=1)
        else:
            w=np.exp(beta*proj); w/=w.sum(axis=1,keepdims=True)
            cw=np.cumsum(w,axis=1); u=rng.random((len(idx),1))
            pick=(u>cw).sum(axis=1)
        pos[idx]=pos[idx]+NN[pick]
        live[idx[np.linalg.norm(tgt[idx]-pos[idx],axis=1)<math.sqrt(2)]]=False
    return visits

def gp_cv(visits,r0,tol=0.35):
    """variation across GPs at radius ~r0 -- the observable a CP actually samples"""
    vals=[v for (x,y,z),v in visits.items()
          if abs(math.sqrt(x*x+y*y+z*z)-r0)<tol]
    if len(vals)<8: return float('nan'),len(vals)
    a=np.array(vals); return float(a.std()/a.mean()), len(vals)

R=24
for lab,beta in (("greedy",None),("softmax beta=3",3.0)):
    vis=route(40000,R,beta)
    print(f"\n{lab}:  variation ACROSS GPs at fixed radius")
    print(f"  {'r':>7} {'nGP':>5} {'CV':>9}")
    for r0 in (math.sqrt(2),2.0,math.sqrt(6),2*math.sqrt(2),math.sqrt(10),4.0,6.0,8.0):
        cv,n=gp_cv(vis,r0)
        print(f"  {r0:7.3f} {n:5d} {cv:9.4f}")
