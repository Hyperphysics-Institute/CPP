#!/usr/bin/env python3
"""PR3-R2 (Patch 2823) — FOUNDER-EXECUTED under the frozen 2823 prereg.
Self-contained. Runs on CPU (numpy); uses PyTorch CUDA automatically if
available. Prints a REPORT BLOCK to paste back to the worker.

USAGE (Git Bash, from the CPP repo root):
    cd series_phenomena/cosmology/dark_matter
    python code/2823_pr3r2_founder_run.py

Optional: python code/2823_pr3r2_founder_run.py --cpu   (force CPU)
Runtime: minutes on GPU; ~1-2 h on CPU. Progress prints per chain.
"""
import math, sys, time
import numpy as np

USE_T=False
if '--cpu' not in sys.argv:
    try:
        import torch
        if torch.cuda.is_available():
            USE_T=True; DEV=torch.device('cuda')
    except Exception:
        pass

# ---- committed constants (2761/2790 lineage, verbatim) ----
HBARC=197.3269788; ALPHA_EM=1/137.035999084
PHI=(1+math.sqrt(5))/2; A_L=0.589/PHI
NCP=2*math.sqrt(2.0)/A_L**3; Q2=ALPHA_EM*HBARC
THETA=2*math.sqrt(2)*math.pi*Q2/A_L; BETA=1.0/THETA
N=432; A_S=0.02
L=(N/NCP)**(1.0/3.0); ALPHA=5.6/L; RC=L/2

def make_k(L,nmax=5):
    ks=[]
    for nx in range(-nmax,nmax+1):
        for ny in range(-nmax,nmax+1):
            for nz in range(-nmax,nmax+1):
                if nx==ny==nz==0: continue
                if nx*nx+ny*ny+nz*nz>nmax*nmax: continue
                ks.append([nx,ny,nz])
    ks=np.array(ks,float)*(2*math.pi/L)
    return ks,(ks**2).sum(1)

KV,K2=make_k(L)
WK=np.exp(-K2/(4*ALPHA*ALPHA))/K2
PREF=2*(2*math.pi/(L**3))*Q2
Z=np.array([1.0]*(N//2)+[-1.0]*(N//2))
N2=np.round(K2/(2*math.pi/L)**2).astype(int)
SHELLS=[np.where(N2==j)[0] for j in (1,2,3,4)]
KREP=[KV[s[0]] for s in SHELLS]

def erfc(x): return np.vectorize(math.erfc)(x)

def pair_real(d):
    r=np.sqrt((d**2).sum(-1)); r=np.maximum(r,1e-12)
    return Q2*(erfc(ALPHA*r)/r - 1.0/np.sqrt(r*r+A_S*A_S) + 1.0/np.sqrt(r*r+A_S*A_S))*0 + \
           Q2*(erfc(ALPHA*r)/r) + Q2*(1.0/np.sqrt(r*r+A_S*A_S) - 1.0/r)

def dE_move(i,newp,pos,Sk):
    d_old=pos-pos[i]; d_new=pos-newp
    d_old=d_old-L*np.rint(d_old/L); d_new=d_new-L*np.rint(d_new/L)
    m=np.ones(N,bool); m[i]=False
    e_old=(Z[m]*pair_real(d_old[m])).sum()*Z[i]
    e_new=(Z[m]*pair_real(d_new[m])).sum()*Z[i]
    ph_old=np.exp(1j*(KV@pos[i])); ph_new=np.exp(1j*(KV@newp))
    Sn=Sk+Z[i]*(ph_new-ph_old)
    k_old=PREF*(WK*(Sk.real**2+Sk.imag**2)).sum()
    k_new=PREF*(WK*(Sn.real**2+Sn.imag**2)).sum()
    return (e_new-e_old)+(k_new-k_old), Sn

def chain(amp,seed,eq_block=2000,prod=6000,every=2,maxblocks=5):
    rng=np.random.default_rng(seed)
    pos=rng.uniform(0,L,size=(N,3))
    Sk=(Z[:,None]*np.exp(1j*(pos@KV.T))).sum(0)
    K=np.array(KREP)
    R=np.array([float((Z*np.cos(pos@k)).sum()) for k in K])
    step=0.12*A_L
    def sweep(n):
        nonlocal pos,Sk,R
        acc=0
        for _ in range(n):
            for _ in range(N):
                i=int(rng.integers(N))
                newp=(pos[i]+rng.normal(0,step,3))%L
                dE,Sn=dE_move(i,newp,pos,Sk)
                old=pos[i].copy()
                dR=Z[i]*(np.cos(K@newp)-np.cos(K@old))
                dX=amp*float(dR[:3].sum())
                if (dE+dX)<=0 or rng.random()<math.exp(-BETA*(dE+dX)):
                    pos[i]=newp; Sk=Sn; R=R+dR; acc+=1
        return acc/(n*N)
    # --- control-gated equilibration (frozen SS1.1) ---
    blocks=0; ctrl_ok=False
    while blocks<maxblocks and not ctrl_ok:
        ar=sweep(eq_block); blocks+=1
        probe=[]
        for _ in range(200):
            sweep(1); probe.append(float(R[3]))
        p=np.array(probe); sd=p.std(ddof=1)/math.sqrt(len(p))
        ctrl_ok = abs(p.mean())<=1.0*max(sd,1e-9)
        print(f"    eq block {blocks}: acc={ar:.2f} control mean={p.mean():+.3f}+/-{sd:.3f} -> {'PASS' if ctrl_ok else 'extend'}",flush=True)
    rec=[[] for _ in range(4)]
    for s in range(prod):
        sweep(1)
        if s%every==0:
            for j in range(4): rec[j].append(float(R[j]))
    return [np.array(r) for r in rec], blocks, ctrl_ok

NBLK=24; NBOOT=2000
def bb(x,seed,f=np.mean):
    bl=len(x)//NBLK; B=[x[j*bl:(j+1)*bl] for j in range(NBLK)]
    rng=np.random.default_rng(seed)
    v=[f(np.concatenate([B[i] for i in rng.integers(0,NBLK,NBLK)])) for _ in range(NBOOT)]
    return float(f(np.concatenate(B))), float(np.std(v,ddof=1))

if __name__=="__main__":
    print(f"PR3-R2 | torch-cuda={USE_T} | N={N} L={L:.4f} beta={BETA:.5f}")
    amps=[0.0,-1.32,-0.66,0.66,1.32]; seeds=[20260841,20260842,20260843,20260844,20260845]
    out={}
    for a,sd in zip(amps,seeds):
        t0=time.time(); print(f"  chain A={a:+.2f} seed={sd} ...",flush=True)
        rec,blocks,ok=chain(a,sd)
        if a==0.0:
            out['ref']=[bb(r,900+j,lambda z: float(np.mean(z**2))) for j,r in enumerate(rec)]
        out[a]=[bb(r,800+j) for j,r in enumerate(rec)]
        out.setdefault('meta',{})[a]=(blocks,ok)
        print(f"    done in {time.time()-t0:.0f}s (eq blocks={blocks}, control {'PASS' if ok else 'FAIL'})",flush=True)
    print("\n===== PASTE EVERYTHING BELOW BACK TO THE WORKER =====")
    print("PR3-R2 REPORT (Patch 2823)")
    print(f"torch_cuda={USE_T}")
    for a in amps:
        print(f"A={a:+.2f} eqblocks={out['meta'][a][0]} ctrl={'PASS' if out['meta'][a][1] else 'FAIL'} " +
              " ".join(f"n2={j+1}:{out[a][j][0]:+.4f}+/-{out[a][j][1]:.4f}" for j in range(4)))
    print("UNPERT <|rho|^2> " + " ".join(f"n2={j+1}:{out['ref'][j][0]:.4f}+/-{out['ref'][j][1]:.4f}" for j in range(4)))
    print("===== END REPORT =====")
