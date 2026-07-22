#!/usr/bin/env python3
"""S4-X B-CHECK-80B (Patch 2755) -- DRIVE-AUDIT-1 fourth act, part 2.

Amended charter frozen in s4x_bcheck80b_prereg.md BEFORE any
production run (2753 production blocked by gate FAIL; defect record
2754). Three clean ensembles at N = 80:
  A-FIX-UND seed 20260796, 1k+16k   (run_A + one-line fix mn[i]=False)
  A-FIX-DRV seed 20260797, 1k+16k
  B-DRV     seed 20260795, 1k+12k   (2746 design, full k prefactor)
Gate v2 (blocking): B totals vs A-FIX increments, 5 seed-1 moves,
<=1e-8 relative. Frozen fork J1-J4 in the prereg par.2.

Commands: gate2 | bench_afix | run TAG MAXSWEEPS | analyze
  TAG in {AFIX-UND, AFIX-DRV, B-DRV}
"""
import math, json, pickle, os, sys, gzip, time
import numpy as np
from scipy.special import erfc as serfc

HBARC=197.3269788; AEM=1/137.035999084
PHI=(1+math.sqrt(5))/2; A=0.589/PHI
NCP=2*math.sqrt(2.0)/A**3; Q2=AEM*HBARC
THETA=2*math.sqrt(2)*math.pi*Q2/A
N=80; A_S=0.04; EPS=2.4
SEEDS={"AFIX-UND":20260796,"AFIX-DRV":20260797,"B-DRV":20260795}
L=(N/NCP)**(1.0/3.0); B_=2*math.pi/L
ks=[(nx,ny,nz) for nx in range(-6,7) for ny in range(-6,7)
    for nz in range(-6,7)
    if 0<nx*nx+ny*ny+nz*nz<=27 and
       ((nx>0) or (nx==0 and ny>0) or (nx==0 and ny==0 and nz>0))]
KV=2*math.pi/L*np.array(ks,float); K2=(KV**2).sum(1)
ALPHA=5.6/L; RC=L/2
WK=np.exp(-K2/(4*ALPHA*ALPHA))/K2
PREF=2*(2*math.pi/(L**3))*Q2
Z=np.array([1.0]*(N//2)+[-1.0]*(N//2))
KD=np.array([B_,0.0,0.0])
CKDIR="/tmp/bcheck80b"

def inc_AFIX(pos,S,i,newp,drive):
    """run_A increment (2749 verbatim) + the ONE-LINE FIX mn[i]=False."""
    d_o=pos-pos[i]; d_n=pos-newp
    d_o-=L*np.round(d_o/L); d_n-=L*np.round(d_n/L)
    r2o=(d_o**2).sum(1); r2n=(d_n**2).sum(1)
    ro=np.sqrt(r2o); rn=np.sqrt(r2n)
    zz=Q2*(Z*Z[i])
    mo=(ro<RC)&(ro>1e-12); mn=(rn<RC)&(rn>1e-12)
    mn[i]=False   # <-- THE FIX (2754 defect: old-new self-pair)
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
    return float(dE),Snew

def total_energy_B(x):
    E=0.0
    for i in range(N-1):
        d=x[i+1:]-x[i]; d-=L*np.round(d/L)
        rr2=(d*d).sum(1); rr=np.sqrt(rr2); keep=(rr<RC)
        E+=float(np.sum(Q2*(Z[i+1:]*Z[i])[keep]*(serfc(ALPHA*rr[keep])/rr[keep]
                 -1.0/rr[keep]+1.0/np.sqrt(rr2[keep]+A_S*A_S))))
    Sf=(Z[:,None]*np.exp(1j*(x@KV.T))).sum(0)
    E+=float(PREF*np.sum(WK*(Sf.real**2+Sf.imag**2)))  # FULL prefactor
    return E

def total_B(x):
    return total_energy_B(x)+EPS*float(np.sum(Z*np.cos(x@KD)))

def gate2():
    rng=np.random.default_rng(1)
    x=rng.uniform(0,L,size=(N,3))
    S=(Z[:,None]*np.exp(1j*(x@KV.T))).sum(0)
    E0=total_B(x); step=0.20*A; ok=True
    for t in range(5):
        j=int(rng.integers(N))
        xn=x.copy(); xn[j]=(xn[j]+rng.normal(0,step,3))%L
        dB=total_B(xn)-E0
        dA,_=inc_AFIX(x,S,j,xn[j],True)
        rel=abs(dB-dA)/max(1.0,abs(dA))
        print(f"gate2 move {t}: dE_B={dB:+.10f}  dE_AFIX={dA:+.10f}  rel={rel:.2e}")
        ok&=(rel<=1e-8)
    print("GATE2:", "PASS" if ok else "FAIL -- BLOCKING")
    return ok

def bench_afix():
    rng=np.random.default_rng(1)
    pos=rng.uniform(0,L,size=(N,3))
    S=(Z[:,None]*np.exp(1j*(pos@KV.T))).sum(0)
    step=0.20*A; t0=time.time()
    for _ in range(20):
        for _ in range(N):
            i=int(rng.integers(N))
            newp=(pos[i]+rng.normal(0,step,3))%L
            dE,Snew=inc_AFIX(pos,S,i,newp,True)
            if dE<=0 or rng.random()<math.exp(-dE/THETA):
                pos[i]=newp; S=Snew
    dt=(time.time()-t0)/20
    print(f"A-FIX benchmark: {dt*1000:.1f} ms/sweep -> {(17000*dt)/60:.1f} min per chain (discarded, no observable)")

def run(tag,max_sweeps):
    os.makedirs(CKDIR,exist_ok=True)
    seed=SEEDS[tag]; drive=tag.endswith("DRV") and not tag.startswith("AFIX-UND")
    drive=(tag!="AFIX-UND")
    ck=f"{CKDIR}/{tag}.pkl"
    if tag=="B-DRV":
        if os.path.exists(ck):
            st=pickle.load(open(ck,"rb")); rng=st["rng"]; x=st["x"]; done=st["done"]; ser=st["ser"]
        else:
            rng=np.random.default_rng(seed)
            x=rng.uniform(0,L,size=(N,3)); done=0; ser=[]
        hop=0.20*A; eq=1000; sw=12000; total=eq+sw
        end=min(total,done+max_sweeps)
        E_cur=total_B(x)
        for s_ in range(done,end):
            for _ in range(N):
                j=int(rng.integers(N))
                xn=x.copy(); xn[j]=(xn[j]+rng.normal(0,hop,3))%L
                E_new=total_B(xn)
                if E_new-E_cur<=0 or rng.random()<math.exp(-(E_new-E_cur)/THETA):
                    x=xn; E_cur=E_new
            if s_>=eq and (s_-eq)%10==0:
                ser.append(float(np.sum(Z*np.cos(x@KD))))
            if (s_+1)%100==0:
                pickle.dump({"rng":rng,"x":x,"done":s_+1,"ser":ser},open(ck,"wb"))
        done=end
        pickle.dump({"rng":rng,"x":x,"done":done,"ser":ser},open(ck,"wb"))
    else:
        if os.path.exists(ck):
            st=pickle.load(open(ck,"rb")); rng=st["rng"]; pos=st["pos"]; S=st["S"]
            done=st["done"]; ser=st["ser"]
        else:
            rng=np.random.default_rng(seed)
            pos=rng.uniform(0,L,size=(N,3))
            S=(Z[:,None]*np.exp(1j*(pos@KV.T))).sum(0)
            done=0; ser=[]
        step=0.20*A; eq=1000; sw=16000; total=eq+sw
        end=min(total,done+max_sweeps)
        for s_ in range(done,end):
            for _ in range(N):
                i=int(rng.integers(N))
                newp=(pos[i]+rng.normal(0,step,3))%L
                dE,Snew=inc_AFIX(pos,S,i,newp,drive)
                if dE<=0 or rng.random()<math.exp(-dE/THETA):
                    pos[i]=newp; S=Snew
            if s_>=eq and (s_-eq)%10==0:
                ser.append(float(np.sum(Z*np.cos(pos@KD))))
            if (s_+1)%500==0:
                pickle.dump({"rng":rng,"pos":pos,"S":S,"done":s_+1,"ser":ser},open(ck,"wb"))
        done=end
        pickle.dump({"rng":rng,"pos":pos,"S":S,"done":done,"ser":ser},open(ck,"wb"))
    print(f"[{tag}] {done}/{eq+sw if tag=='B-DRV' else 17000}  samples={len(ser)}",flush=True)
    total=13000 if tag=="B-DRV" else 17000
    if done>=total:
        json.dump(ser,open(f"{CKDIR}/{tag}.json","w")); print(f"[{tag}] COMPLETE",flush=True)

def blockstats(ser,nb=10):
    n=len(ser); bl=n//nb
    bm=np.array([ser[j*bl:(j+1)*bl].mean() for j in range(nb)])
    return bm.mean(), bm.std(ddof=1)/math.sqrt(nb)

def analyze():
    beta=1.0/THETA
    sF=np.array(json.load(open(f"{CKDIR}/AFIX-DRV.json")))
    sU=np.array(json.load(open(f"{CKDIR}/AFIX-UND.json")))
    sB=np.array(json.load(open(f"{CKDIR}/B-DRV.json")))
    mF,eF=blockstats(sF); mU,eU=blockstats(sU); mB,eB=blockstats(sB)
    varU=sU.var(ddof=1)
    w=np.exp(-beta*EPS*(sU-sU.mean()))
    tilt=float(np.sum(sU*w)/np.sum(w))
    nb=10; bl=len(sU)//nb; jk=[]
    for j in range(nb):
        m=np.ones(len(sU),bool); m[j*bl:(j+1)*bl]=False
        jk.append(np.sum(sU[m]*w[m])/np.sum(w[m]))
    jk=np.array(jk); tF=math.sqrt((nb-1)/nb*np.sum((jk-jk.mean())**2))
    lin=-beta*EPS*varU
    r=mF/tilt; sr=abs(r)*math.sqrt((eF/mF)**2+(tF/tilt)**2)
    sFB=math.sqrt(eF*eF+eB*eB)
    print(f"AFIX-UND: <A>={mU:+.3f}+/-{eU:.3f}  Var={varU:.2f}  linear={lin:+.3f}")
    print(f"tilt_fix = {tilt:+.3f}+/-{tF:.3f}")
    print(f"AFIX-DRV: <A>={mF:+.3f}+/-{eF:.3f}")
    print(f"B-DRV:    <A>={mB:+.3f}+/-{eB:.3f}  Var={sB.var(ddof=1):.2f}")
    print(f"r_fix = {r:.3f}+/-{sr:.3f}")
    dr=abs(r-1)/sr; dFB=abs(mF-mB)/sFB
    dBt=abs(mB-tilt)/math.sqrt(eB*eB+tF*tF)
    print(f"|r_fix-1|: {dr:.2f} sigma | AFIX-DRV vs B-DRV: {dFB:.2f} sigma | B vs tilt_fix: {dBt:.2f} sigma")
    print(f"legacy context: tilt_legacy=-1.185+/-0.144  A-DRV_legacy=-1.922+/-0.157  r_legacy=1.622+/-0.237")
    if dr<=2 and dFB<=2:
        v="J1 DEFECT IS THE MECHANISM -> (a) CONFIRMED (2714 self-pair); reach audit + re-verification charter"
    elif (r-1)>2*sr and dFB<=2:
        v="J2 ENHANCEMENT SURVIVES THE FIX -> (b)-like; AUTOMATON-1 arbiter; no mechanism reading"
    elif dFB>2:
        v="J3 CLEAN SAMPLERS DISAGREE -> residual defect; mechanical diff; no physics reading"
    else:
        v="J4 OTHER -> PARTIAL; extend or automaton"
    print("FROZEN FORK:",v)

if __name__=="__main__":
    a=sys.argv[1]
    if a=="gate2": gate2()
    elif a=="bench_afix": bench_afix()
    elif a=="run": run(sys.argv[2],int(sys.argv[3]))
    elif a=="analyze": analyze()
