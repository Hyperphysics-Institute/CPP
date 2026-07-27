#!/usr/bin/env python3
"""PR3-R (Patch 2821) under the frozen re-prereg: symmetric amplitude
ladder, slope fit, simultaneous multi-mode driving, cross-talk control."""
import math, sys
import numpy as np
_src=open('code/2790_x4_execution.py').read()
_head=_src[:_src.index('def gate_v2')].replace('RUNS={','RUNS={"PR3R":(432,0.02,20260831,300,1800),')
G={}; exec(_head,G)
geom=G['geom']; total_E=G['total_E']; dE_A_fixed=G['dE_A_fixed']; THETA=G['THETA']; A_L=G['A']
NBLK=24; NBOOT=2000
def bb(x,seed):
    bl=len(x)//NBLK; B=[x[j*bl:(j+1)*bl] for j in range(NBLK)]
    rng=np.random.default_rng(seed); v=[np.mean(np.concatenate([B[i] for i in rng.integers(0,NBLK,NBLK)])) for _ in range(NBOOT)]
    return float(np.mean(np.concatenate(B))), float(np.std(v,ddof=1))
def run(amp,seed,eq=300,prod=1800,every=6):
    N,a_s,_,_,_,L,alpha,rc,kv,k2,wk,pref_k,z=geom("PR3R")
    beta=1.0/THETA
    n2=np.round(k2/(2*math.pi/L)**2).astype(int)
    ks=[kv[np.where(n2==j)[0][0]] for j in (1,2,3,4)]   # 4th = cross-talk control (undriven)
    rng=np.random.default_rng(seed)
    pos=rng.uniform(0,L,size=(N,3))
    S=(z[:,None]*np.exp(1j*(pos@kv.T))).sum(0)
    K=np.array(ks)                      # (4,3)
    R=np.array([float((z*np.cos(pos@k)).sum()) for k in K])   # Re rho per shell, tracked
    def dR(i,newp,oldp):
        return z[i]*(np.cos(K@newp)-np.cos(K@oldp))
    rec=[[] for _ in range(4)]; acc=0; tot=0
    for sw in range(eq+prod):
        for _ in range(N):
            i=int(rng.integers(N))
            newp=(pos[i]+rng.normal(0,0.12*A_L,3))%L
            dE,Snew=dE_A_fixed(i,newp,pos,z,L,alpha,rc,a_s,kv,wk,pref_k,S)
            old=pos[i].copy()
            d_=dR(i,newp,old); dX=amp*float(d_[:3].sum()); tot+=1
            if (dE+dX)<=0 or rng.random()<math.exp(-beta*(dE+dX)):
                pos[i]=newp; S=Snew; R=R+d_; acc+=1
        if sw>=eq and (sw-eq)%every==0:
            for j in range(4): rec[j].append(float(R[j]))
    return [np.array(r) for r in rec], N, beta, acc/tot
if __name__=="__main__":
    amps=[-1.32,-0.66,0.66,1.32]; seeds=[20260831,20260832,20260833,20260834]
    res={}
    for a,sd in zip(amps,seeds):
        rec,N,beta,ar=run(a,sd)
        res[a]=[bb(r,700+int(abs(a)*10)) for r in rec]
        print(f"A={a:+.2f}: " + "  ".join(f"n2={j+1}:{res[a][j][0]:+.3f}+/-{res[a][j][1]:.3f}" for j in range(4)) + f"  acc={ar:.2f}")
    np.save('/tmp/pr3r.npy',np.array([[res[a][j] for j in range(4)] for a in amps]))
    print("saved")
