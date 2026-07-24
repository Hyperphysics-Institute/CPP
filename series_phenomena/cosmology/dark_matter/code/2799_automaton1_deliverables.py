#!/usr/bin/env python3
"""AUTOMATON-1 DELIVERABLES (Patch 2799) under frozen 2796 SS4.
Per R: theta calibration (two thermometers), Gibbs reference at
theta_H (committed 2761-lineage Metropolis on the lattice H proxy),
D-(i)..(vi) with frozen bands. Usage: stage R"""
import sys, math, pickle, json
import numpy as np

M=24; N=432; NBLK=24; NBOOT=2000
RBINS=np.arange(0.5,12.6,1.0); RC=0.5*(RBINS[:-1]+RBINS[1:])
sx=np.where(np.arange(M)<=M//2,np.arange(M),np.arange(M)-M)

def pdist(pos):
    d=pos[:,None,:]-pos[None,:,:]
    d=(d+M//2)%M-M//2
    return np.sqrt((d**2).sum(2))

def obs(pos,sig):
    D=pdist(pos); iu=np.triu_indices(N,1)
    dv=D[iu]; ss=(sig[:,None]*sig[None,:])[iu]
    H=float((ss/np.maximum(dv,1.0)).sum())  # d_min floor 1 (same GP pairs at d=1 eff) -- committed engine convention
    hl,_=np.histogram(dv[ss>0],RBINS); hu,_=np.histogram(dv[ss<0],RBINS)
    Ncl=int((dv<=2).sum())
    dip=np.array([ (sig*sx[pos[:,a]]).mean() for a in range(3)])
    return H,hl,hu,Ncl,float(np.linalg.norm(dip))

def series(samples,sig):
    Hs=[];HL=[];HU=[];NC=[];DP=[]
    for p in samples:
        H,hl,hu,nc,dp=obs(p.astype(int),sig)
        Hs.append(H);HL.append(hl);HU.append(hu);NC.append(nc);DP.append(dp)
    return np.array(Hs),np.array(HL),np.array(HU),np.array(NC),np.array(DP)

def gzz(HL,HU):
    tot=HL.mean(0)+HU.mean(0)
    g=(HL.mean(0)-HU.mean(0))/np.maximum(tot,1)
    return g

def kappa_fit(HL,HU):
    g=gzz(HL,HU); m=(RC>=2)&(RC<=6)&(np.abs(g)>0)
    co=np.polyfit(RC[m],np.log(np.abs(g[m])),1)
    return -co[0]

def contrast(HL,HU):
    m=(RC>=2)&(RC<=6)
    return float((HU.mean(0)[m]/np.maximum(HL.mean(0)[m],1)).mean())

def boot(fn,arrs,seed):
    n=len(arrs[0]); bl=n//NBLK
    ids=[np.arange(j*bl,(j+1)*bl) for j in range(NBLK)]
    rng=np.random.default_rng(seed); vals=[]
    for _ in range(NBOOT):
        pick=rng.integers(0,NBLK,NBLK)
        sel=np.concatenate([ids[p] for p in pick])
        try: vals.append(fn(*[a[sel] for a in arrs]))
        except Exception: pass
    return float(np.std(vals,ddof=1))

def metropolis(theta,sweeps,warm,sample_every,seed):
    rng=np.random.default_rng(seed)
    pos=rng.integers(0,M,size=(N,3)); sig=np.array([1]*(N//2)+[-1]*(N//2))
    D=pdist(pos)
    def dE(i,newp):
        d=pos-newp; d=(d+M//2)%M-M//2
        dn=np.sqrt((d**2).sum(1)); dn[i]=np.inf
        do=D[i].copy(); do[i]=np.inf
        return float((sig[i]*sig*(1/np.maximum(dn,1.0)-1/np.maximum(do,1.0))).sum())
    S=[]
    for sw in range(sweeps):
        for _ in range(N):
            i=int(rng.integers(N))
            newp=(pos[i]+rng.integers(-2,3,3))%M
            de=dE(i,newp)
            if de<=0 or rng.random()<math.exp(-de/theta):
                pos[i]=newp
                d=pos-pos[i]; d=(d+M//2)%M-M//2
                dn=np.sqrt((d**2).sum(1)); D[i,:]=dn; D[:,i]=dn
        if sw>=warm and (sw-warm)%sample_every==0: S.append(pos.copy())
    return S,sig

if __name__=="__main__":
    R=int(sys.argv[1]); stage=sys.argv[2] if len(sys.argv)>2 else "all"
    st=pickle.load(open(f"/tmp/auto1/run_R{R}.pkl","rb"))
    sig=st["sig"]; samples=st["samples"]
    if stage=="auto":
        Hs,HL,HU,NC,DP=series(samples,sig)
        print(f"[R={R}] automaton: <H>={Hs.mean():.3f}+/-{Hs.std(ddof=1)/math.sqrt(len(Hs)):.3f}  C={contrast(HL,HU):.4f}  kappa={kappa_fit(HL,HU):.4f}")
        pickle.dump({"Hs":Hs,"HL":HL,"HU":HU,"NC":NC,"DP":DP},open(f"/tmp/auto1/obs_R{R}.pkl","wb"))
    elif stage.startswith("grid"):
        ob=pickle.load(open(f"/tmp/auto1/obs_R{R}.pkl","rb")); Ht=ob["Hs"].mean()
        half=int(stage[4:])
        grid=[0.3,0.6,1.0,1.8][:] if half==0 else [3.0,5.0,8.0]
        out={}
        for th in grid:
            S,_=metropolis(th,700,250,3,1000+int(th*10))
            h2,hl2,hu2,_,_=series(np.array(S),sig)
            out[th]=(float(h2.mean()),contrast(hl2,hu2))
            print(f"   Gibbs theta={th}: <H>={h2.mean():.3f}  C={out[th][1]:.4f}")
        json.dump(out,open(f"/tmp/auto1/grid{half}_R{R}.json","w"))
