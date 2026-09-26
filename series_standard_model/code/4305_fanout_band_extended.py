#!/usr/bin/env python3
"""4305 -- extend pass 3 (scripts/3133_subpsr_cascade.py, Patch 3135) to larger hop counts with a sparse-matrix relay.
Same rule: FCC lattice (12 neighbours), single volley at the origin, at each hop a site's DI-bits split EQUALLY among
neighbours with strictly positive outward radial component (x . d > 0); at the origin all 12.  Band thickness as in the
pass-3 table: rms(r)/<r> over the pulse's occupancy after N hops.  Comparison value: 4 pi alpha = 0.09170."""
import numpy as np, scipy.sparse as sp, sys
RMAX=int(sys.argv[1]) if len(sys.argv)>1 else 60
g=np.arange(-RMAX-2,RMAX+3); L=len(g)
I,J,K=np.meshgrid(g,g,g,indexing='ij'); m=((I+J+K)%2==0)
P=np.stack([I[m],J[m],K[m]],1); n=len(P)
lin=lambda p:((p[:,0]+RMAX+2)*L+(p[:,1]+RMAX+2))*L+(p[:,2]+RMAX+2)
idx=-np.ones(L**3,dtype=np.int64); idx[lin(P)]=np.arange(n)
NB=np.array([(a,b,0) for a in (1,-1) for b in (1,-1)]+[(a,0,b) for a in (1,-1) for b in (1,-1)]+[(0,a,b) for a in (1,-1) for b in (1,-1)])
R=np.linalg.norm(P,axis=1); origin=int(np.where(R<1e-9)[0][0])
rows=[];cols=[]
for d in NB:
    q=P+d; ok=np.all(np.abs(q)<=RMAX+2,axis=1); j=np.full(n,-1); j[ok]=idx[lin(q[ok])]
    outward=(P@d>0)|(np.arange(n)==origin); keep=(j>=0)&outward
    rows.append(j[keep]); cols.append(np.where(keep)[0])
rows=np.concatenate(rows); cols=np.concatenate(cols)
deg=np.bincount(cols,minlength=n).astype(float); w=1.0/deg[cols]
M=sp.csr_matrix((w,(rows,cols)),shape=(n,n))
cur=np.zeros(n); cur[origin]=1.0
print(f"lattice R_MAX = {RMAX}, {n} sites;  4 pi alpha = {4*np.pi/137.035999:.5f}")
print(f"{'N':>4} {'<r>':>8} {'rms':>7} {'rms/<r>':>8} {'4pi/f=1/a':>10}")
for N in range(1,2*RMAX-3):
    cur=M@cur
    if N in (6,10,14,18,22) or (N>22 and N%8==0):
        mm=cur>1e-300; wgt=cur[mm]; r=R[mm]; mr=(wgt*r).sum()/wgt.sum(); rms=np.sqrt((wgt*(r-mr)**2).sum()/wgt.sum())
        f=rms/mr; print(f"{N:4d} {mr:8.3f} {rms:7.3f} {f:8.4f} {4*np.pi/f:10.1f}")
# fine scan of small N for the crossing f = 4 pi alpha, and the decline exponent
cur=np.zeros(n); cur[origin]=1.0; fs={}
for N in range(1,80):
    cur=M@cur
    mm=cur>1e-300; wgt=cur[mm]; r=R[mm]; mr=(wgt*r).sum()/wgt.sum(); fs[N]=np.sqrt((wgt*(r-mr)**2).sum()/wgt.sum())/mr
tgt=4*np.pi/137.035999
xs=[N for N in range(2,79) if (fs[N]-tgt)*(fs[N+1]-tgt)<=0]
print("crossings of f = 4 pi alpha at N =",xs, "  f(7..10) =",[round(fs[k],4) for k in (7,8,9,10)])
Ns=np.array([24,32,40,48,56,64,72]); ex=np.polyfit(np.log(Ns),np.log([fs[k] for k in Ns]),1)[0]
print(f"decline exponent over N = 24..72: f ~ N^{ex:.2f} (no plateau); extrapolated to N = 1e30 GP-steps: f ~ {fs[72]*(1e30/72)**ex:.1e}")
