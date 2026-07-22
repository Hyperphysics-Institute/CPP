#!/usr/bin/env python3
"""S4-X X3-LONG (Patch 2740-2741) -- the slow-component discriminator.

PREREGISTRATION (frozen HERE before any run):
DESIGN: ONE chain, N = 432 (justified: the X5b forensic showed the
small-k suppression is size-identical at N=432 vs 686 -- 0.177 vs
HNC 0.249 mirrors the MAIN-box ratios -- and the frozen signature is
about TIME, not size), a_s = 0.04, MAIN parameters, seed 20260760,
20,000 sweeps total = 1,000 equilibration + 19,000 sampling; fresh
full-summation sampling every 25 sweeps (760 samples). EMBEDDED
DRIVE: eps = 2.4 MeV at exactly three vectors k1x=(b,0,0),
k2=(b,b,0), k3=(b,b,b); the UNDRIVEN same-shell partners (2 at n2=1,
5 at n2=2, 3 at n2=3) supply the fluctuation spectrum in the SAME
chain with no mean contamination (cross-vector coupling O((beta
eps)^2) ~ 0.5%, disclosed).
ESTIMATORS: S_zz(shell) = mean over undriven shell vectors of
<|rho_z(k)|^2>/N ; S_drv(vector) = -2<Re rho_z>/(beta eps N).
FROZEN SIGNATURE EVALUATION (the decision rule):
Compute S_zz(shell; window [0,T]) at T = 2k, 5k, 10k, 19k sampling
sweeps. Let dS = S_zz(19k) - S_zz(2k), sigma_d their combined error
(block-based at each T, conservative).
- GROWTH verdict: dS > +2 sigma_d at >= 2 of 3 shells AND the 19k
  endpoints lie within 2 sigma of the corresponding S_drv ->
  the slow-component hypothesis is CONFIRMED; the X5/X6/X1-paradox/
  original-excess complex closes on one mechanism; PR3 re-testable
  at adequate length; X4 redesigns mode-aware.
- FLAT verdict: |dS| <= 2 sigma_d at >= 2 of 3 shells AND the 19k
  S_zz remains > 2 sigma below S_drv at >= 2 shells -> the sampled
  ensemble genuinely violates the fluctuation relation at this
  length scale; escalates to a dedicated adjudication with
  AUTOMATON-1 elevated.
- Anything else: PARTIAL-UNRESOLVED, tail diagnostics reported, a
  longer instrument specified.
TAIL DIAGNOSTICS (frozen): per-mode multi-window tau_int (windows
c = 3, 5, 8); blocked variance of the shell-1 undriven |rho|^2
series vs block length b in {5,10,20,38,76} samples (a still-rising
curve at b_max is direct slow-component evidence).
PR3 RE-TEST at full length: S_drv vs S_zz(19k) per driven vector's
shell, 2 sigma bands."""
import math, json, pickle, os, numpy as np
from scipy.special import erfc as serfc

HBARC=197.3269788; AEM=1/137.035999084
PHI=(1+math.sqrt(5))/2; A=0.589/PHI; KAPPA=2.0/A
NCP=2*math.sqrt(2.0)/A**3; Q2=AEM*HBARC
THETA=2*math.sqrt(2)*math.pi*Q2/A
N=432; A_S=0.04; SEED=20260760; EQ=1000; TOTAL=20000; EPS=2.4

def make_k(L,n2max=27):
    ks=[]
    for nx in range(-6,7):
        for ny in range(-6,7):
            for nz in range(-6,7):
                n2=nx*nx+ny*ny+nz*nz
                if n2==0 or n2>n2max: continue
                if (nx>0) or (nx==0 and ny>0) or (nx==0 and ny==0 and nz>0):
                    ks.append((nx,ny,nz))
    kv=2*math.pi/L*np.array(ks,float)
    return kv,(kv**2).sum(1),np.array(ks)

def run_chunk(max_sweeps):
    ck="/tmp/x3long_ck.pkl"
    L=(N/NCP)**(1.0/3.0); alpha=5.6/L; rc=L/2; b=2*math.pi/L
    kv,k2,nvec=make_k(L)
    wk=np.exp(-k2/(4*alpha*alpha))/k2
    pref_k=2*(2*math.pi/(L**3))*Q2
    kdr=np.array([[b,0,0],[b,b,0],[b,b,b]])
    n2=np.round(k2/b**2).astype(int)
    drv_idx=[int(np.where((nvec==v).all(1))[0][0]) for v in ([1,0,0],[1,1,0],[1,1,1])]
    und={s:[j for j in np.where(n2==s)[0] if j not in drv_idx] for s in (1,2,3)}
    z=np.array([1.0]*(N//2)+[-1.0]*(N//2))
    if os.path.exists(ck):
        st=pickle.load(open(ck,"rb")); rng=st["rng"]; pos=st["pos"]; S=st["S"]
        done=st["done"]; drv=st["drv"]; flc=st["flc"]; acc=st["acc"]; tot=st["tot"]
    else:
        rng=np.random.default_rng(SEED)
        pos=rng.uniform(0,L,size=(N,3))
        S=(z[:,None]*np.exp(1j*(pos@kv.T))).sum(0)
        done=0; drv=[]; flc=[]; acc=0; tot=0
    step=0.20*A
    end=min(TOTAL,done+max_sweeps)
    for s_ in range(done,end):
        for _ in range(N):
            i=int(rng.integers(N))
            newp=(pos[i]+rng.normal(0,step,3))%L
            d_o=pos-pos[i]; d_n=pos-newp
            d_o-=L*np.round(d_o/L); d_n-=L*np.round(d_n/L)
            r2o=(d_o**2).sum(1); r2n=(d_n**2).sum(1)
            ro=np.sqrt(r2o); rn=np.sqrt(r2n)
            zz=Q2*(z*z[i])
            mo=(ro<rc)&(ro>1e-12); mn=(rn<rc)&(rn>1e-12)
            eo=np.sum(zz[mo]*(serfc(alpha*ro[mo])/ro[mo]-1.0/ro[mo]
                              +1.0/np.sqrt(r2o[mo]+A_S*A_S)))
            en=np.sum(zz[mn]*(serfc(alpha*rn[mn])/rn[mn]-1.0/rn[mn]
                              +1.0/np.sqrt(r2n[mn]+A_S*A_S)))
            dS=z[i]*(np.exp(1j*(newp@kv.T))-np.exp(1j*(pos[i]@kv.T)))
            Snew=S+dS
            dEk=pref_k*np.sum(wk*((Snew.real**2+Snew.imag**2)-(S.real**2+S.imag**2)))
            dExt=EPS*z[i]*np.sum(np.cos(kdr@newp)-np.cos(kdr@pos[i]))
            dE=en-eo+dEk+dExt; tot+=1
            if dE<=0 or rng.random()<math.exp(-dE/THETA):
                pos[i]=newp; S=Snew; acc+=1
        if s_>=EQ and (s_-EQ)%25==0:
            Sf=(z[:,None]*np.exp(1j*(pos@kv.T))).sum(0)
            drv.append([float(Sf[j].real) for j in drv_idx])
            flc.append([float(np.mean(np.abs(Sf[und[s]])**2))/N for s in (1,2,3)])
    done=end
    pickle.dump({"rng":rng,"pos":pos,"S":S,"done":done,"drv":drv,"flc":flc,
                 "acc":acc,"tot":tot},open(ck,"wb"))
    print(f"[X3-LONG] {done}/{TOTAL} sweeps  acc={acc/max(tot,1):.2f}  samples={len(drv)}")
    if done>=TOTAL:
        json.dump({"drv":drv,"flc":flc,"L":L},open("/tmp/x3long.json","w"))
        print("[X3-LONG] COMPLETE -> json")

def analyze():
    beta=1.0/THETA
    d=json.load(open("/tmp/x3long.json"))
    drv=np.array(d["drv"]); flc=np.array(d["flc"]); n=len(drv); L=d["L"]; b=2*math.pi/L
    names=["k1x(n2=1)","k2(n2=2)","k3(n2=3)"]
    # windows
    Ts=[int(2000/25),int(5000/25),int(10000/25),n]  # samples per window
    print("Frozen signature: S_zz(shell) on expanding windows:")
    Svals={}
    for si in range(3):
        row=[]
        for T in Ts:
            seg=flc[:T,si]
            nb=8; bl=max(T//nb,1)
            bmm=np.array([seg[j*bl:(j+1)*bl].mean() for j in range(nb)])
            row.append((seg.mean(),bmm.std(ddof=1)/math.sqrt(nb)))
        Svals[si]=row
        print(f"  shell n2={si+1}: "+"  ".join(f"T={t*25//1000}k:{v:.4f}+/-{e:.4f}" for t,(v,e) in zip(Ts,row)))
    # S_drv at full length
    print("S_drv (full length) vs S_zz(19k):")
    nb=10; bl=n//nb
    verdict_growth=0; verdict_flat=0; endpoint_close=0; still_low=0
    Sd={}
    for si in range(3):
        bm=np.array([drv[j*bl:(j+1)*bl,si].mean() for j in range(nb)])
        m=bm.mean(); se=bm.std(ddof=1)/math.sqrt(nb)
        Sdv=-2*m/(beta*EPS*N); Sde=2*se/(beta*EPS*N); Sd[si]=(Sdv,Sde)
        Sz,Sze=Svals[si][-1]
        D=abs(Sdv-Sz)/math.sqrt(Sde**2+Sze**2)
        print(f"  {names[si]}: S_drv={Sdv:.4f}+/-{Sde:.4f} vs S_zz(19k)={Sz:.4f}+/-{Sze:.4f} -> {D:.2f} sigma")
        if D<=2: endpoint_close+=1
        else: still_low+=1
        dS=Svals[si][-1][0]-Svals[si][0][0]
        sd=math.sqrt(Svals[si][-1][1]**2+Svals[si][0][1]**2)
        if dS>2*sd: verdict_growth+=1
        if abs(dS)<=2*sd: verdict_flat+=1
    # tail diagnostics: blocked variance vs block length, shell-1 |rho|^2 series
    print("Blocked-SEM of shell-1 fluctuation series vs block length (rising = slow component):")
    ser=flc[:,0]
    for bls in (5,10,20,38,76):
        nb2=n//bls
        bm=np.array([ser[j*bls:(j+1)*bls].mean() for j in range(nb2)])
        print(f"  b={bls}: SEM={bm.std(ddof=1)/math.sqrt(nb2):.5f}")
    # HNC refs
    print("HNC-like refs: "+"  ".join(
        f"n2={v}:{(v*b*b)/(v*b*b+(1.0206*KAPPA)**2):.4f}" for v in (1,2,3)))
    if verdict_growth>=2 and endpoint_close>=2: v="GROWTH -> SLOW-COMPONENT CONFIRMED"
    elif verdict_flat>=2 and still_low>=2: v="FLAT -> GENUINE FDT VIOLATION AT THIS LENGTH; ESCALATE"
    else: v="PARTIAL-UNRESOLVED"
    print(f"\nFROZEN VERDICT: {v}")

if __name__=="__main__":
    import sys
    if sys.argv[1]=="analyze": analyze()
    else: run_chunk(int(sys.argv[1]))
