#!/usr/bin/env python3
"""S4-X X7-NSCAN (Patch 2749) -- DRIVE-AUDIT-1 second act.

Campaign path A of 2746_s4x_x5fe.py VERBATIM (the code path under
audit), parameterized by N. Prereg frozen in s4x_x7nscan_prereg.md
BEFORE any run. Sizes 128/216/320; A-path pairs (DRV + UND->tilt);
1k eq + 16k sampling, sample every 10. Frozen seeds:
128:(20260783,20260784) 216:(20260785,20260786) 320:(20260787,20260788).
"""
import math, json, pickle, os, sys, numpy as np
from scipy.special import erfc as serfc

HBARC=197.3269788; AEM=1/137.035999084
PHI=(1+math.sqrt(5))/2; A=0.589/PHI
NCP=2*math.sqrt(2.0)/A**3; Q2=AEM*HBARC
THETA=2*math.sqrt(2)*math.pi*Q2/A
A_S=0.04; EPS=2.4
SEEDS={(128,"DRV"):20260783,(128,"UND"):20260784,
       (216,"DRV"):20260785,(216,"UND"):20260786,
       (320,"DRV"):20260787,(320,"UND"):20260788,
       # X7-NSCAN-EXT (Patch 2750 prereg, frozen before any EXT run)
       (80,"DRV"):20260789,(80,"UND"):20260790,
       (96,"DRV"):20260791,(96,"UND"):20260792,
       (112,"DRV"):20260793,(112,"UND"):20260794}

def setup(N):
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
    return L,KV,K2,ALPHA,RC,WK,PREF,Z,KD

def run_A(N,mode,max_sweeps,ckdir="/tmp/x7nscan"):
    os.makedirs(ckdir,exist_ok=True)
    tag=f"N{N}-{mode}"; drive=(mode=="DRV")
    seed=SEEDS[(N,mode)]
    L,KV,K2,ALPHA,RC,WK,PREF,Z,KD=setup(N)
    ck=f"{ckdir}/{tag}.pkl"
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
        if (s_+1)%500==0:
            pickle.dump({"rng":rng,"pos":pos,"S":S,"done":s_+1,"ser":ser},open(ck,"wb"))
    done=end
    pickle.dump({"rng":rng,"pos":pos,"S":S,"done":done,"ser":ser},open(ck,"wb"))
    print(f"[{tag}] {done}/{total}  samples={len(ser)}",flush=True)
    if done>=total:
        json.dump(ser,open(f"{ckdir}/{tag}.json","w")); print(f"[{tag}] COMPLETE",flush=True)

def stats(tag,ckdir="/tmp/x7nscan"):
    ser=np.array(json.load(open(f"{ckdir}/{tag}.json")))
    n=len(ser); nb=10; bl=n//nb
    bm=np.array([ser[j*bl:(j+1)*bl].mean() for j in range(nb)])
    return ser,bm.mean(),bm.std(ddof=1)/math.sqrt(nb)

def analyze(ckdir="/tmp/x7nscan"):
    beta=1.0/THETA
    print("N     <A>_UND        Var     linear    tilt          <A>_DRV        r=DRV/tilt")
    curve={}
    for N in (int(x) for x in (sys.argv[2].split(',') if len(sys.argv)>2 else ('128','216','320'))):
        sD,mD,eD=stats(f"N{N}-DRV",ckdir)
        sU,mU,eU=stats(f"N{N}-UND",ckdir)
        varU=sU.var(ddof=1)
        w=np.exp(-beta*EPS*(sU-sU.mean()))
        tilt=float(np.sum(sU*w)/np.sum(w))
        nb=10; bl=len(sU)//nb; jk=[]
        for j in range(nb):
            m=np.ones(len(sU),bool); m[j*bl:(j+1)*bl]=False
            jk.append(np.sum(sU[m]*w[m])/np.sum(w[m]))
        jk=np.array(jk); te=math.sqrt((nb-1)/nb*np.sum((jk-jk.mean())**2))
        lin=-beta*EPS*varU
        r=mD/tilt
        er=abs(r)*math.sqrt((eD/mD)**2+(te/tilt)**2)
        curve[N]=(r,er)
        print(f"{N:4d}  {mU:+.3f}±{eU:.3f}  {varU:6.2f}  {lin:+.3f}  "
              f"{tilt:+.3f}±{te:.3f}  {mD:+.3f}±{eD:.3f}  {r:.3f}±{er:.3f}")
    print("anchors: r(64)=1.13±0.12 (X5-FE), r(432)=1.70 (X3-LONG)")
    # frozen classification
    cls={}
    for N,(r,er) in curve.items():
        if (r-1)>2*er and r>=1.40: cls[N]="ENHANCED"
        elif abs(r-1.13)<=2*math.sqrt(er*er+0.12*0.12) and r<1.30: cls[N]="UNENHANCED"
        else: cls[N]="INTERMEDIATE"
    print("classification:",cls)
    if set(curve)!={128,216,320}: return curve,cls
    Ns=[128,216,320]; c=[cls[n] for n in Ns]
    bracket=any(c[i]=="UNENHANCED" and "ENHANCED" in c[i+1:] for i in range(3))
    bad=any(c[i]=="ENHANCED" and "UNENHANCED" in c[i+1:] for i in range(3))
    rs=[curve[n][0] for n in Ns]
    mono=all(rs[i]<=rs[i+1] for i in range(2)) and 1.13<=rs[0]
    if bracket and not bad: v="G1 SHARP THRESHOLD -> B-CHECK at smallest ENHANCED N"
    elif c.count("UNENHANCED")==3: v="G3 FLAT THROUGH 320 -> onset in (320,432]"
    elif mono and not bracket: v="G2 SMOOTH DRIFT -> (a)-like reading; automaton arbiter"
    else: v="G4 OTHER -> PARTIAL; extend"
    print("FROZEN FORK:",v)
    return curve,cls

def analyze_ext(ckdir="/tmp/x7nscan"):
    """X7-NSCAN-EXT frozen H-fork (record 2750 par.3). Sizes 80/96/112;
    anchors r(64)=1.13+/-0.12 (X5-FE), r(128)=1.720+/-0.263 (X7)."""
    import sys as _s
    _argv=_s.argv; _s.argv=[_argv[0],"analyze","80,96,112"]
    curve,cls=analyze(ckdir); _s.argv=_argv
    seq=[(64,"UNENHANCED"),(80,cls[80]),(96,cls[96]),(112,cls[112]),(128,"ENHANCED")]
    print("sequence:",seq)
    c=[x[1] for x in seq]
    bracket=any(c[i]=="UNENHANCED" and "ENHANCED" in c[i+1:] for i in range(len(c)))
    inversion=any(c[i]=="ENHANCED" and "UNENHANCED" in c[i+1:] for i in range(len(c)))
    ext=[cls[80],cls[96],cls[112]]
    if ext==["ENHANCED"]*3: v="H2 ALL ENHANCED -> onset in (64,80]; B-CHECK at 80"
    elif ext==["UNENHANCED"]*3: v="H3 ALL UNENHANCED -> transition compressed into (112,128] OR 128 fluctuation; replicate at 128 (seed 20260795 pair) before any reading"
    elif bracket and not inversion: v="H1 ONSET BRACKETED -> B-CHECK at smallest ENHANCED N"
    else: v="H4 OTHER -> gradual rise ((a)-compatible, recorded not enacted); automaton arbiter"
    print("FROZEN FORK (EXT):",v)

if __name__=="__main__":
    a=sys.argv[1]
    if a=="analyze": analyze()
    elif a=="analyze_ext": analyze_ext()
    else:
        N,mode=a.split("-"); run_A(int(N[1:]),mode,int(sys.argv[2]))
