#!/usr/bin/env python3
"""S4-X B-CHECK-80 (Patch 2753) -- DRIVE-AUDIT-1 fourth act.

Prereg frozen in s4x_bcheck80_prereg.md BEFORE any run. Independent
brute-force B sampler (2746 design: per move, TOTAL energy of the
proposed configuration rebuilt from nothing; carried current energy;
no shared state machinery with path A) at N = 80, the smallest size
inside the onset window (64, 80]. Frozen seed 20260795. 1k eq + 12k
sampling sweeps, sample every 10. k-space convention: FULL prefactor
E_k = PREF * sum(WK*|S|^2), matching path A's incremental
dEk = PREF * delta (per the documented 2747 fix; see prereg par.5
disclosure on the committed 2746 file).

Commands:
  gate            -- Hamiltonian-identity gate (seed 1, 5 moves,
                     blocking precondition; reads no observable)
  bench           -- timing benchmark (seed 1, 3 sweeps, discarded)
  run  MAXSWEEPS  -- chunked production (checkpoint /tmp/bcheck80)
  analyze         -- frozen I-fork readout vs archived comparators
"""
import math, json, pickle, os, sys, gzip, time
import numpy as np
from scipy.special import erfc as serfc

HBARC=197.3269788; AEM=1/137.035999084
PHI=(1+math.sqrt(5))/2; A=0.589/PHI
NCP=2*math.sqrt(2.0)/A**3; Q2=AEM*HBARC
THETA=2*math.sqrt(2)*math.pi*Q2/A
N=80; A_S=0.04; EPS=2.4
SEED=20260795
L=(N/NCP)**(1.0/3.0); B_=2*math.pi/L

ks=[]
for nx in range(-6,7):
    for ny in range(-6,7):
        for nz in range(-6,7):
            n2=nx*nx+ny*ny+nz*nz
            if n2==0 or n2>27: continue
            if (nx>0) or (nx==0 and ny>0) or (nx==0 and ny==0 and nz>0):
                ks.append((nx,ny,nz))
KV=2*math.pi/L*np.array(ks,float); K2=(KV**2).sum(1)
ALPHA=5.6/L; RC=L/2
WK=np.exp(-K2/(4*ALPHA*ALPHA))/K2
PREF=2*(2*math.pi/(L**3))*Q2
Z=np.array([1.0]*(N//2)+[-1.0]*(N//2))
KD=np.array([B_,0.0,0.0])

# ---- B sampler: totals rebuilt from nothing every evaluation ----
def total_energy_B(x):
    E=0.0
    for i in range(N-1):
        d=x[i+1:]-x[i]
        d-=L*np.round(d/L)
        rr2=(d*d).sum(1); rr=np.sqrt(rr2)
        keep=(rr<RC)
        E+=float(np.sum(Q2*(Z[i+1:]*Z[i])[keep]*(serfc(ALPHA*rr[keep])/rr[keep]
                 -1.0/rr[keep]+1.0/np.sqrt(rr2[keep]+A_S*A_S))))
    Sf=(Z[:,None]*np.exp(1j*(x@KV.T))).sum(0)
    E+=float(PREF*np.sum(WK*(Sf.real**2+Sf.imag**2)))  # FULL prefactor
    return E

def total_B(x):
    return total_energy_B(x)+EPS*float(np.sum(Z*np.cos(x@KD)))

# ---- path-A incremental machinery (gate reference only) ----
def dE_A(pos,S,i,newp):
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
    dE+=EPS*Z[i]*(math.cos(float(KD@newp))-math.cos(float(KD@pos[i])))
    return float(dE)

def gate():
    rng=np.random.default_rng(1)
    x=rng.uniform(0,L,size=(N,3))
    S=(Z[:,None]*np.exp(1j*(x@KV.T))).sum(0)
    E0=total_B(x); step=0.20*A; ok=True
    for t in range(5):
        j=int(rng.integers(N))
        xn=x.copy(); xn[j]=(xn[j]+rng.normal(0,step,3))%L
        dB=total_B(xn)-E0
        dA=dE_A(x,S,j,xn[j])
        rel=abs(dB-dA)/max(1.0,abs(dA))
        print(f"gate move {t}: dE_B={dB:+.10f}  dE_A={dA:+.10f}  rel={rel:.2e}")
        ok&=(rel<=1e-8)
    print("GATE:", "PASS" if ok else "FAIL -- BLOCKING")
    return ok

def bench():
    rng=np.random.default_rng(1)
    x=rng.uniform(0,L,size=(N,3))
    E=total_B(x); step=0.20*A
    t0=time.time()
    for _ in range(3):
        for _ in range(N):
            j=int(rng.integers(N))
            xn=x.copy(); xn[j]=(xn[j]+rng.normal(0,step,3))%L
            En=total_B(xn)
            if En-E<=0 or rng.random()<math.exp(-(En-E)/THETA):
                x=xn; E=En
    dt=(time.time()-t0)/3
    print(f"benchmark: {dt:.3f} s/sweep -> {(13000*dt)/3600:.2f} h for 1k+12k (discarded, no observable)")

def run(max_sweeps,ckdir="/tmp/bcheck80"):
    os.makedirs(ckdir,exist_ok=True)
    ck=f"{ckdir}/B80.pkl"
    if os.path.exists(ck):
        st=pickle.load(open(ck,"rb")); rng=st["rng"]; x=st["x"]; done=st["done"]; ser=st["ser"]
    else:
        rng=np.random.default_rng(SEED)
        x=rng.uniform(0,L,size=(N,3)); done=0; ser=[]
    hop=0.20*A; eq=1000; sw=12000; total=eq+sw
    end=min(total,done+max_sweeps)
    E_cur=total_B(x)   # recomputed from scratch at every resume (drift-proof)
    for s_ in range(done,end):
        for _ in range(N):
            j=int(rng.integers(N))
            xn=x.copy()
            xn[j]=(xn[j]+rng.normal(0,hop,3))%L
            E_new=total_B(xn)
            if E_new-E_cur<=0 or rng.random()<math.exp(-(E_new-E_cur)/THETA):
                x=xn; E_cur=E_new
        if s_>=eq and (s_-eq)%10==0:
            ser.append(float(np.sum(Z*np.cos(x@KD))))
        if (s_+1)%100==0:
            pickle.dump({"rng":rng,"x":x,"done":s_+1,"ser":ser},open(ck,"wb"))
    done=end
    pickle.dump({"rng":rng,"x":x,"done":done,"ser":ser},open(ck,"wb"))
    print(f"[B80] {done}/{total}  samples={len(ser)}",flush=True)
    if done>=total:
        json.dump(ser,open(f"{ckdir}/B80.json","w")); print("[B80] COMPLETE",flush=True)

def analyze(ckdir="/tmp/bcheck80",
            arch="data/x7nscan"):
    beta=1.0/THETA
    serB=np.array(json.load(open(f"{ckdir}/B80.json")))
    nb=10; bl=len(serB)//nb
    bm=np.array([serB[j*bl:(j+1)*bl].mean() for j in range(nb)])
    mB=bm.mean(); eB=bm.std(ddof=1)/math.sqrt(nb)
    sU=np.array(json.load(gzip.open(f"{arch}/x7nscan_N80-UND.json.gz","rt")))
    sD=np.array(json.load(gzip.open(f"{arch}/x7nscan_N80-DRV.json.gz","rt")))
    bmD=np.array([sD[j*(len(sD)//nb):(j+1)*(len(sD)//nb)].mean() for j in range(nb)])
    mD=bmD.mean(); eD=bmD.std(ddof=1)/math.sqrt(nb)
    w=np.exp(-beta*EPS*(sU-sU.mean()))
    tilt=float(np.sum(sU*w)/np.sum(w))
    blU=len(sU)//nb; jk=[]
    for j in range(nb):
        m=np.ones(len(sU),bool); m[j*blU:(j+1)*blU]=False
        jk.append(np.sum(sU[m]*w[m])/np.sum(w[m]))
    jk=np.array(jk); te=math.sqrt((nb-1)/nb*np.sum((jk-jk.mean())**2))
    sAB=math.sqrt(eB*eB+eD*eD); sBt=math.sqrt(eB*eB+te*te)
    rB=mB/tilt; erB=abs(rB)*math.sqrt((eB/mB)**2+(te/tilt)**2)
    print(f"B-DRV(80): <A>={mB:+.3f}+/-{eB:.3f}  Var={serB.var(ddof=1):.2f}  samples={len(serB)}")
    print(f"comparators: tilt={tilt:+.3f}+/-{te:.3f}  A-DRV={mD:+.3f}+/-{eD:.3f}")
    print(f"r_B = {rB:.3f}+/-{erB:.3f}   (A-path r = 1.622+/-0.237)")
    dAB=abs(mB-mD)/sAB; dBt=abs(mB-tilt)/sBt
    print(f"B vs A-DRV: {dAB:.2f} sigma | B vs tilt: {dBt:.2f} sigma")
    if dAB<=2 and dBt>2:
        v="I1 REPRODUCED -> (a) dies at onset; (b) finite-size-onset ergodicity failure is the finding; AUTOMATON-1 arbiter"
    elif dBt<=2 and dAB>2:
        v="I2 TILT-LEVEL -> incremental path impeached at onset; mechanical diff + fix + re-verification"
    else:
        v="I3 OTHER -> PARTIAL; extend (24k prereg) or hand to AUTOMATON-1"
    print("FROZEN FORK:",v)

if __name__=="__main__":
    a=sys.argv[1]
    if a=="gate": gate()
    elif a=="bench": bench()
    elif a=="run": run(int(sys.argv[2]))
    elif a=="analyze":
        analyze(arch=sys.argv[2] if len(sys.argv)>2 else "data/x7nscan")
