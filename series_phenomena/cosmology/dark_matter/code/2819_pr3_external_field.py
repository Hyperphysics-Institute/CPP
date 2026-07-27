#!/usr/bin/env python3
"""PR3 external-field susceptibility (Patch 2819) under the FROZEN 2819 prereg.
Committed 2790 Ewald/Metropolis machinery, unmodified, plus the external
coupling H_ext = A * Re[rho_{-k}] with rho_k = sum_i z_i exp(-i k.x_i).
Statistic: Lambda(k) = [<Re rho_k>_A / A] / [-beta N S_zz(k) / 2]."""
import math, sys
import numpy as np
_src=open('code/2790_x4_execution.py').read()
_head=_src[:_src.index('def gate_v2')]
_head=_head.replace('RUNS={','RUNS={"PR3":(432,0.02,20260820,400,3000),')
G={}; exec(_head,G)
geom=G['geom']; total_E=G['total_E']; dE_A_fixed=G['dE_A_fixed']; THETA=G['THETA']; A_L=G['A']

def run(kidx,amp,seed,eq=400,prod=3000,every=10):
    N,a_s,_,_,_,L,alpha,rc,kv,k2,wk,pref_k,z=geom("PR3")
    beta=1.0/THETA
    n2=np.round(k2/(2*math.pi/L)**2).astype(int)
    shell=np.where(n2==kidx)[0]
    kvec=kv[shell[0]]                      # committed shell direction
    rng=np.random.default_rng(seed)
    pos=rng.uniform(0,L,size=(N,3))
    S=(z[:,None]*np.exp(1j*(pos@kv.T))).sum(0)
    E=total_E(pos,z,L,alpha,rc,a_s,kv,wk,pref_k)
    def rho(p): return complex((z*np.exp(-1j*(p@kvec))).sum())
    def ext(p): return amp*rho(p).real
    Eext=ext(pos)
    acc=0; tot=0; samples=[]
    for sw in range(eq+prod):
        for _ in range(N):
            i=int(rng.integers(N))
            newp=(pos[i]+rng.normal(0,0.12*A_L,3))%L
            dE,Snew=dE_A_fixed(i,newp,pos,z,L,alpha,rc,a_s,kv,wk,pref_k,S)
            old=pos[i].copy(); pos[i]=newp
            dExt=ext(pos)-Eext
            tot+=1
            if (dE+dExt)<=0 or rng.random()<math.exp(-beta*(dE+dExt)):
                S=Snew; Eext=Eext+dExt; acc+=1
            else:
                pos[i]=old
        if sw>=eq and (sw-eq)%every==0:
            samples.append(rho(pos))
    return np.array(samples), N, beta, acc/tot

NBLK=24; NBOOT=2000
def blockboot(x,f,seed):
    bl=len(x)//NBLK
    B=[x[j*bl:(j+1)*bl] for j in range(NBLK)]
    rng=np.random.default_rng(seed); v=[]
    for _ in range(NBOOT):
        sel=np.concatenate([B[i] for i in rng.integers(0,NBLK,NBLK)])
        v.append(f(sel))
    return f(np.concatenate(B)), float(np.std(v,ddof=1))

if __name__=="__main__":
    kidx=int(sys.argv[1]); mode=sys.argv[2]
    if mode=="unpert":
        s,N,beta,ar=run(kidx,0.0,20260820)
        m,e=blockboot(s,lambda a: float(np.mean(np.abs(a)**2)),101)
        print(f"k-shell n2={kidx}: <|rho|^2>_0 = {m:.4f} +/- {e:.4f}  (S_zz={m/N:.4f}) acc={ar:.2f}")
    else:
        amp=float(sys.argv[3]); seed=int(sys.argv[4])
        s,N,beta,ar=run(kidx,amp,seed)
        m,e=blockboot(s,lambda a: float(np.mean(a.real)),202)
        print(f"k-shell n2={kidx} A={amp}: <Re rho>_A = {m:+.4f} +/- {e:.4f}  acc={ar:.2f}")
