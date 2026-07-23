#!/usr/bin/env python3
"""Defect-robustness check for the 2785 record: does repairing D2
(nan envelope from antipodal-vertex deletion) rescue any RB-2 miss?
Recompute envelopes EXCLUDING the 3 antipode-deletion runs (v=119? no —
antipode is g5's single member; find its vertex id) and re-test ratios."""
import itertools, math, numpy as np
PHI=(1+math.sqrt(5))/2; L_UNIT=0.589; A=L_UNIT/PHI; alpha0=A/(math.pi*math.sqrt(2))
verts=[]
for s in itertools.product([0.5,-0.5],repeat=4): verts.append(s)
for i in range(4):
    for s in (1.0,-1.0):
        v=[0.0]*4; v[i]=s; verts.append(tuple(v))
ep=[(0,1,2,3),(0,2,3,1),(0,3,1,2),(1,0,3,2),(1,2,0,3),(1,3,2,0),(2,0,1,3),(2,1,3,0),(2,3,0,1),(3,0,2,1),(3,1,0,2),(3,2,1,0)]
base=(PHI/2,0.5,1/(2*PHI),0.0); seen=set()
for perm in ep:
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                v=[0.0]*4; vals=(s1*base[0],s2*base[1],s3*base[2],0.0)
                for k in range(4): v[perm[k]]=vals[k]
                t=tuple(round(x,9) for x in v)
                if t not in seen: seen.add(t); verts.append(t)
V=np.array(verts)
D4=np.linalg.norm(V[:,None,:]-V[None,:,:],axis=2)*L_UNIT
rg_chord=np.round(D4[0],6)
anti=int(np.argmax(D4[0]))
print(f"antipodal vertex id: {anti} (chord dist {D4[0,anti]:.4f})")
dmin=D4[D4>1e-9].min()
Dg=np.where(np.abs(D4-dmin)<1e-6,1.0,1e9); np.fill_diagonal(Dg,0.0)
for k in range(120): Dg=np.minimum(Dg,Dg[:,k][:,None]+Dg[k,:][None,:])
Dg*=A
rg=np.round(Dg[0],6); gsh=sorted(set(rg[1:]))
gmem=[np.where(np.abs(rg-s)<1e-6)[0] for s in gsh]
def solve_D(D,src,alpha):
    n=len(D); mask=np.ones(n,bool); mask[src]=False
    r0=D[src,mask]; Dq=D[np.ix_(mask,mask)].copy(); np.fill_diagonal(Dq,np.inf)
    return np.linalg.solve(np.eye(n-1)+alpha/Dq,1.0/r0),mask
def gmeans(D,alpha,drop=None):
    keep=np.ones(120,bool)
    if drop is not None: keep[drop]=False
    idx=np.where(keep)[0]; Ds=D[np.ix_(idx,idx)]
    f,mask=solve_D(Ds,int(np.where(idx==0)[0][0]),alpha)
    resp=idx[np.where(mask)[0]]; val=dict(zip(resp,f))
    return np.array([np.mean([val[v] for v in mem if v in val]) for mem in gmem])
runs=[]
for am in (0.969,1.000,1.031):
    a=alpha0*am
    runs.append((None,gmeans(D4,a)))
    for d in range(1,120): runs.append((d,gmeans(D4,a,drop=d)))
finite=[m for d,m in runs if d!=anti]
R=np.array([np.abs(m[1:])/np.abs(m[:-1]) for m in finite])
lo,hi=R.min(0),R.max(0)
tgt=gmeans(Dg,alpha0)
robs=np.abs(tgt[1:])/np.abs(tgt[:-1])
print("D2-repaired envelopes (antipode-deletion runs excluded):")
for k in range(4):
    inb = lo[k]-1e-12<=robs[k]<=hi[k]+1e-12
    print(f"  rho_{k+1}: obs={robs[k]:.4f}  env=[{lo[k]:.4f},{hi[k]:.4f}]  in={inb}")
# g2 sign unanimity check under repair (should be unchanged)
signs=np.sign(np.array(finite))
for g in range(5):
    u=set(signs[:,g].tolist())
    print(f"  g{g+1} predictor sign set (repaired): {sorted(u)}")
