#!/usr/bin/env python3
"""S4-X X5-FE (Patch 2746-2747) -- OPEN-DM-DRIVE-AUDIT-1, first act.

PREREGISTRATION (frozen HERE before any run):
PURPOSE: localize the B2 inconsistency (driven means 1.6x the exact
tilt response) between three suspects: the campaign code path (A),
the tilt/undriven side, or scale/physics.
DESIGN: N = 64 (32/32), a_s = 0.04, same density (L = 1.030 fm), one
driven mode k1x = (2pi/L)(1,0,0), eps = 2.4 MeV. THREE ensembles:
(A-DRV) the campaign code path (incremental Ewald S, masked erfc
real-space), driven, seed 20260780, 1k eq + 16k sampling sweeps,
sample every 10;
(A-UND) same path, undriven, seed 20260781, same lengths -> the
exact tilt prediction tilt_A = <A e^{-beta eps A}>/<e^{-beta eps A}>;
(B-DRV) an INDEPENDENT sampler written from scratch in a different
style: per move, TOTAL energies of old and new configurations are
recomputed from nothing (full pair sum with the identical masked
erfc+softcore formula; full k-space structure factors rebuilt from
all particles), plus the identical drive term; seed 20260782,
1k + 12k sweeps. No shared state machinery with (A).
ZERO-COST CHECK (existing data): un-tilt symmetry on the X3-LONG
driven series -- reweight by e^{+beta eps A}; a Gibbs(H+epsA) chain
must reproduce undriven <A> ~ 0.
FROZEN FORK (2-sigma bands, combined errors):
F1: B-DRV agrees with tilt_A, A-DRV does not -> the campaign
DRIVEN path is impeached CONCRETELY (a code-path defect under
drive); locate by mechanical diff, fix, re-verify all driven
artifacts.
F2: B-DRV agrees with A-DRV, both disagree with tilt_A -> the two
independent implementations concur; the TILT side goes under audit
(undriven sampler or the reweighting theory as applied).
F3: all three agree at N = 64 -> the inconsistency is
scale-dependent; escalate to the panel with the automaton elevated
to arbiter-of-record.
F4: none of the above -> PARTIAL; extend.
POWER: sigma_A ~ 2.5 at N=64; predicted linear mean ~ -0.4 to -0.5,
enhanced ~ -0.7; SEM targets <= 0.09 (ESS >= 800 per ensemble);
discrimination ~ 3 sigma per comparison. Small-box physics shifts S
itself but all three ensembles share the box exactly."""
import math, json, pickle, os, numpy as np
from scipy.special import erfc as serfc

HBARC=197.3269788; AEM=1/137.035999084
PHI=(1+math.sqrt(5))/2; A=0.589/PHI
NCP=2*math.sqrt(2.0)/A**3; Q2=AEM*HBARC
THETA=2*math.sqrt(2)*math.pi*Q2/A
N=64; A_S=0.04; EPS=2.4
L=(N/NCP)**(1.0/3.0); B_=2*math.pi/L

def make_k(n2max=27):
    ks=[]
    for nx in range(-6,7):
        for ny in range(-6,7):
            for nz in range(-6,7):
                n2=nx*nx+ny*ny+nz*nz
                if n2==0 or n2>n2max: continue
                if (nx>0) or (nx==0 and ny>0) or (nx==0 and ny==0 and nz>0):
                    ks.append((nx,ny,nz))
    kv=2*math.pi/L*np.array(ks,float)
    return kv,(kv**2).sum(1)

KV,K2=make_k()
ALPHA=5.6/L; RC=L/2
WK=np.exp(-K2/(4*ALPHA*ALPHA))/K2
PREF=2*(2*math.pi/(L**3))*Q2
Z=np.array([1.0]*(N//2)+[-1.0]*(N//2))
KD=np.array([B_,0.0,0.0])

def run_A(tag,seed,drive,eq,sw,max_sweeps):
    ck=f"/tmp/x5fe_{tag}.pkl"
    if os.path.exists(ck):
        st=pickle.load(open(ck,"rb")); rng=st["rng"]; pos=st["pos"]; S=st["S"]
        done=st["done"]; ser=st["ser"]
    else:
        rng=np.random.default_rng(seed)
        pos=rng.uniform(0,L,size=(N,3))
        S=(Z[:,None]*np.exp(1j*(pos@KV.T))).sum(0)
        done=0; ser=[]
    step=0.20*A; total=eq+sw
    end=min(total,done+max_sweeps)
    for s_ in range(done,end):
        for _ in range(N):
            i=int(rng.integers(N))
            newp=(pos[i]+rng.normal(0,step,3))%L
            d_o=pos-pos[i]; d_n=pos-newp
            d_o-=L*np.round(d_o/L); d_n-=L*np.round(d_n/L)
            r2o=(d_o**2).sum(1); r2n=(d_n**2).sum(1)
            ro=np.sqrt(r2o); rn=np.sqrt(r2n)
            zz=Q2*(Z*Z[i])
            mo=(ro<RC)&(ro>1e-12); mn=(rn<RC)&(rn>1e-12)
            eo=np.sum(zz[mo]*(serfc(ALPHA*ro[mo])/ro[mo]-1.0/ro[mo]
                              +1.0/np.sqrt(r2o[mo]+A_S*A_S)))
            en=np.sum(zz[mn]*(serfc(ALPHA*rn[mn])/rn[mn]-1.0/rn[mn]
                              +1.0/np.sqrt(r2n[mn]+A_S*A_S)))
            dS=Z[i]*(np.exp(1j*(newp@KV.T))-np.exp(1j*(pos[i]@KV.T)))
            Snew=S+dS
            dEk=PREF*np.sum(WK*((Snew.real**2+Snew.imag**2)-(S.real**2+S.imag**2)))
            dE=en-eo+dEk
            if drive:
                dE+=EPS*Z[i]*(math.cos(float(KD@newp))-math.cos(float(KD@pos[i])))
            if dE<=0 or rng.random()<math.exp(-dE/THETA):
                pos[i]=newp; S=Snew
        if s_>=eq and (s_-eq)%10==0:
            ser.append(float(np.sum(Z*np.cos(pos@KD))))
    done=end
    pickle.dump({"rng":rng,"pos":pos,"S":S,"done":done,"ser":ser},open(ck,"wb"))
    print(f"[{tag}] {done}/{total}  samples={len(ser)}")
    if done>=total:
        json.dump(ser,open(f"/tmp/x5fe_{tag}.json","w")); print(f"[{tag}] COMPLETE")

# ---- ensemble B: written fresh, different style, brute force ----
def total_energy_B(x):
    # real space, all pairs, min image, same formula
    E=0.0
    for i in range(N-1):
        d=x[i+1:]-x[i]
        d-=L*np.round(d/L)
        rr2=(d*d).sum(1); rr=np.sqrt(rr2)
        keep=(rr<RC)
        E+=float(np.sum(Q2*(Z[i+1:]*Z[i])[keep]*(serfc(ALPHA*rr[keep])/rr[keep]
                 -1.0/rr[keep]+1.0/np.sqrt(rr2[keep]+A_S*A_S))))
    # k space, structure factor rebuilt from scratch
    Sf=(Z[:,None]*np.exp(1j*(x@KV.T))).sum(0)
    E+=float(PREF*0.5*np.sum(WK*(Sf.real**2+Sf.imag**2)))*2.0/2.0
    E+=float(PREF*np.sum(WK*(Sf.real**2+Sf.imag**2)))*0.0  # (kept zero; prefactor already full)
    return E

def run_B(tag,seed,eq,sw,max_sweeps):
    ck=f"/tmp/x5fe_{tag}.pkl"
    if os.path.exists(ck):
        st=pickle.load(open(ck,"rb")); rng=st["rng"]; x=st["x"]; done=st["done"]; ser=st["ser"]
    else:
        rng=np.random.default_rng(seed)
        x=rng.uniform(0,L,size=(N,3)); done=0; ser=[]
    hop=0.20*A; total=eq+sw
    end=min(total,done+max_sweeps)
    E_cur=total_energy_B(x)+EPS*float(np.sum(Z*np.cos(x@KD)))
    for s_ in range(done,end):
        for _ in range(N):
            j=int(rng.integers(N))
            xn=x.copy()
            xn[j]=(xn[j]+rng.normal(0,hop,3))%L
            E_new=total_energy_B(xn)+EPS*float(np.sum(Z*np.cos(xn@KD)))
            if E_new-E_cur<=0 or rng.random()<math.exp(-(E_new-E_cur)/THETA):
                x=xn; E_cur=E_new
        if s_>=eq and (s_-eq)%10==0:
            ser.append(float(np.sum(Z*np.cos(x@KD))))
    done=end
    pickle.dump({"rng":rng,"x":x,"done":done,"ser":ser},open(ck,"wb"))
    print(f"[{tag}] {done}/{total}  samples={len(ser)}")
    if done>=total:
        json.dump(ser,open(f"/tmp/x5fe_{tag}.json","w")); print(f"[{tag}] COMPLETE")

def stats(tag):
    ser=np.array(json.load(open(f"/tmp/x5fe_{tag}.json")))
    n=len(ser); nb=10; bl=n//nb
    bm=np.array([ser[j*bl:(j+1)*bl].mean() for j in range(nb)])
    return ser,bm.mean(),bm.std(ddof=1)/math.sqrt(nb)

def analyze():
    beta=1.0/THETA
    sA,mA,eA=stats("A-DRV")
    sU,mU,eU=stats("A-UND")
    sB,mB,eB=stats("B-DRV")
    varU=sU.var(ddof=1)
    w=np.exp(-beta*EPS*(sU-sU.mean()))
    tilt=float(np.sum(sU*w)/np.sum(w))
    nb=10; bl=len(sU)//nb; jk=[]
    for j in range(nb):
        m=np.ones(len(sU),bool); m[j*bl:(j+1)*bl]=False
        jk.append(np.sum(sU[m]*w[m])/np.sum(w[m]))
    jk=np.array(jk); te=math.sqrt((nb-1)/nb*np.sum((jk-jk.mean())**2))
    lin=-beta*EPS*varU
    print(f"A-UND: <A>={mU:+.3f}+/-{eU:.3f}  Var={varU:.2f}  linear pred={lin:+.3f}")
    print(f"tilt_A prediction: {tilt:+.3f}+/-{te:.3f}")
    print(f"A-DRV: <A>={mA:+.3f}+/-{eA:.3f}")
    print(f"B-DRV: <A>={mB:+.3f}+/-{eB:.3f}")
    dAB=abs(mA-mB)/math.sqrt(eA*eA+eB*eB)
    dAt=abs(mA-tilt)/math.sqrt(eA*eA+te*te)
    dBt=abs(mB-tilt)/math.sqrt(eB*eB+te*te)
    print(f"A-DRV vs B-DRV: {dAB:.2f} sigma | A-DRV vs tilt: {dAt:.2f} | B-DRV vs tilt: {dBt:.2f}")
    if dBt<=2 and dAt>2: v="F1: campaign driven path IMPEACHED CONCRETELY -> diff and fix"
    elif dAB<=2 and dAt>2 and dBt>2: v="F2: implementations concur -> TILT side under audit"
    elif dAB<=2 and dAt<=2 and dBt<=2: v="F3: all agree at N=64 -> scale-dependent; escalate w/ automaton"
    else: v="F4: PARTIAL"
    print(f"FROZEN FORK: {v}")

if __name__=="__main__":
    import sys
    a=sys.argv[1]
    if a=="analyze": analyze()
    elif a=="A-DRV": run_A("A-DRV",20260780,True,1000,16000,int(sys.argv[2]))
    elif a=="A-UND": run_A("A-UND",20260781,False,1000,16000,int(sys.argv[2]))
    elif a=="B-DRV": run_B("B-DRV",20260782,1000,12000,int(sys.argv[2]))
