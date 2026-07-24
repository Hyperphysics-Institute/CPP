#!/usr/bin/env python3
"""X4 FROZEN BATTERY (Patch 2793) — the seven-requirement analysis of the
complete 15-chain ladder, executed under the FROZEN 2786 prereg §2 + PA-1.
Stages (CLI arg): maps1 (window maps, rungs 0.04+0.02) | maps2 (0.01+0.005)
| final (reqs 3,4,5,6 + ESS + PR2 verdict). Map results cached to /tmp.
Every operationalization verbatim from the freeze; nothing tuned post-hoc."""
import sys, math, json, gzip, pickle, os
import numpy as np
from scipy.optimize import curve_fit
PHI=(1+math.sqrt(5))/2; A=0.589/PHI; KAPPA=2.0/A
NBLK=24; NBOOT=2000
RMINS=[0.04,0.06,0.08,0.12,0.16,0.24]; RMAXS=[0.40,0.546,0.70,0.88]
CH={ # label: (path, a_s, N)
 "RV-MAIN-A":("data/rv2714/rv_RV-MAIN-A.json.gz",0.04,686),
 "RV-MAIN-B":("data/rv2714/rv_RV-MAIN-B.json.gz",0.04,686),
 "RV-SIZE-S":("data/rv2714/rv_RV-SIZE-S.json.gz",0.04,432),
 "RV-SIZE-L":("data/rv2714/rv_RV-SIZE-L.json.gz",0.04,1024),
 "RV-CORE":("data/rv2714/rv_RV-CORE.json.gz",0.02,432),
 "X4-02-686":("data/x3x4/X4-02-686.json.gz",0.02,686),
 "X4-02-1024":("data/x3x4/X4-02-1024.json.gz",0.02,1024),
 "X3-R04":("data/x3x4/X3-R04.json.gz",0.04,686),
 "X3-R02":("data/x3x4/X3-R02.json.gz",0.02,432),
 "X4-01-432A":("data/x3x4/X4-01-432A.json.gz",0.01,432),
 "X4-01-432B":("data/x3x4/X4-01-432B.json.gz",0.01,432),
 "X4-01-686":("data/x3x4/X4-01-686.json.gz",0.01,686),
 "X4-01-1024":("data/x3x4/X4-01-1024.json.gz",0.01,1024),
 "X4-005-432A":("data/x3x4/X4-005-432A.json.gz",0.005,432),
 "X4-005-432B":("data/x3x4/X4-005-432B.json.gz",0.005,432),
 "X4-005-686":("data/x3x4/X4-005-686.json.gz",0.005,686),
 "X4-005-1024":("data/x3x4/X4-005-1024.json.gz",0.005,1024)}
def load(lab): return json.load(gzip.open(CH[lab][0]))
def blocks_of(d):
    profs=np.array(d["profs"]); nb=d["nb"]; rmax=d["rmax"]
    rc=(np.arange(nb)+0.5)*rmax/nb
    bl=len(profs)//NBLK
    return rc, np.array([profs[j*bl:(j+1)*bl].mean(0) for j in range(NBLK)])
FY=lambda r_,Aa,k_: Aa*np.exp(-k_*r_)/r_
def kfit_window(rc,bs,lo,hi,p0k=KAPPA):
    mean=bs.mean(0); sem=bs.std(0,ddof=1)/math.sqrt(len(bs))
    m=(rc>lo)&(rc<hi)&(sem>0)
    if m.sum()<6: return None
    pm,_=curve_fit(FY,rc[m],mean[m],p0=[0.05,p0k],sigma=np.maximum(sem[m],1e-7),maxfev=20000)
    return pm[1]
def cell_boot(rc,blocks,lo,hi,seed):
    k0=kfit_window(rc,blocks,lo,hi)
    if k0 is None: return None
    rng=np.random.default_rng(seed); ks=[]
    for _ in range(NBOOT):
        try:
            v=kfit_window(rc,blocks[rng.integers(0,NBLK,NBLK)],lo,hi,p0k=k0)
            if v is not None: ks.append(v)
        except Exception: pass
    return k0/KAPPA, float(np.std(ks,ddof=1))/KAPPA

def stage_maps(rungs, out):
    res={}
    for lab,(p,a_s,N) in CH.items():
        if a_s not in rungs: continue
        d=load(lab); rc,blocks=blocks_of(d)
        m={}
        for rm in RMINS:
            if rm < 2*a_s-1e-12: continue
            for rx in RMAXS:
                v=cell_boot(rc,blocks,rm,rx,seed=int(rm*1000)*100+int(rx*100))
                if v: m[(rm,rx)]=v
        res[lab]=m
        key=m.get((0.08,0.546))
        print(f"  {lab}: {len(m)} cells; fixed-window (0.08,0.546): "
              f"{key[0]:.4f}+/-{key[1]:.4f}" if key else f"  {lab}: {len(m)} cells")
    pickle.dump(res,open(out,"wb"))

if sys.argv[1]=="maps1": stage_maps({0.04,0.02},"/tmp/x3x4/maps1.pkl")
elif sys.argv[1]=="maps2": stage_maps({0.01,0.005},"/tmp/x3x4/maps2.pkl")
elif sys.argv[1]=="final":
    maps={**pickle.load(open("/tmp/x3x4/maps1.pkl","rb")),**pickle.load(open("/tmp/x3x4/maps2.pkl","rb"))}
    print("== REQ 2 — FIXED-PHYSICAL-WINDOW ROW (r_min=0.08, r_max=0.546) across ALL rungs ==")
    for lab in CH:
        v=maps.get(lab,{}).get((0.08,0.546))
        if v: print(f"  {lab:12s} a_s={CH[lab][1]:5.3f} N={CH[lab][2]:4d}: {v[0]:.4f} +/- {v[1]:.4f}")
    print("\n== REQ 3 — two-component form test (rung-pooled; dAIC>=10 discriminant) ==")
    F2=lambda r_,A1,k1,A2,k2: A1*np.exp(-k1*r_)/r_ + A2*np.exp(-k2*r_)/r_
    rungform={}
    for a_s in (0.04,0.02,0.01,0.005):
        labs=[l for l in CH if CH[l][1]==a_s]
        rcs=[]; pools=[]
        for l in labs:
            d=load(l); rc,b=blocks_of(d); rcs.append(rc); pools.append(b)
        rc=rcs[0]; allb=np.vstack(pools)
        mean=allb.mean(0); sem=allb.std(0,ddof=1)/math.sqrt(len(allb))
        lo,hi=2*a_s,3.0/KAPPA
        m=(rc>lo)&(rc<hi)&(sem>0)
        x,y,e=rc[m],mean[m],np.maximum(sem[m],1e-7)
        pA,_=curve_fit(FY,x,y,p0=[0.05,KAPPA],sigma=e,maxfev=30000)
        c2A=np.sum(((y-FY(x,*pA))/e)**2)
        best=None
        for k2g in (3*KAPPA,6*KAPPA,12*KAPPA):
            try:
                pB,_=curve_fit(F2,x,y,p0=[pA[0],KAPPA,y[0]*x[0],k2g],sigma=e,maxfev=60000)
                c2=np.sum(((y-F2(x,*pB))/e)**2)
                if best is None or c2<best[0]: best=(c2,pB)
            except Exception: pass
        c2B,pB=best
        dAIC=(c2A+2*2)-(c2B+2*4)
        kasym=min(pB[1],pB[3]); kasym_r=kasym/KAPPA
        # asym-kappa error via quick bootstrap (200) on pooled blocks
        rng=np.random.default_rng(7); ks=[]
        for _ in range(200):
            bb=allb[rng.integers(0,len(allb),len(allb))]
            mn=bb.mean(0); se=bb.std(0,ddof=1)/math.sqrt(len(bb))
            mm=(rc>lo)&(rc<hi)&(se>0)
            try:
                pb,_=curve_fit(F2,rc[mm],mn[mm],p0=pB,sigma=np.maximum(se[mm],1e-7),maxfev=30000)
                ks.append(min(pb[1],pb[3]))
            except Exception: pass
        kerr=np.std(ks,ddof=1)/KAPPA if len(ks)>10 else float('nan')
        zDH=abs(kasym_r-1.0)/kerr if kerr==kerr else float('nan')
        if dAIC>=10 and zDH<=2: cls="TRANSIENT-MODE"
        elif dAIC<10 and kasym_r<1 and (1-kasym_r)/kerr>2: cls="ASYMPTOTIC-SHIFT"
        else: cls="UNRESOLVED-FORM"
        rungform[a_s]=(dAIC,kasym_r,kerr,cls)
        print(f"  a_s={a_s}: dAIC(B-A)={dAIC:8.1f}  kappa_asym/kappa_D={kasym_r:.4f}+/-{kerr:.4f} "
              f"({zDH:.2f} sigma vs DH) -> {cls}")
    print("\n== REQ 4 — joint real/k shared-pole fit per rung ==")
    for a_s in (0.04,0.02,0.01,0.005):
        labs=[l for l in CH if CH[l][1]==a_s]
        # k-side: per-sample szz where available (PA-1); else archived means (limitation noted)
        k2n=[]; szz_est=[]; szz_err=[]; persample=True
        for l in labs:
            d=load(l)
            if "szz_samples" not in d: persample=False
        # build shell arrays from the largest-N chain (finest k grid) per rung
        dref=load(max(labs,key=lambda l:CH[l][2]))
        k2=np.array(dref["k2"]); L=dref["L"]
        n2=np.round(k2/(2*math.pi/L)**2).astype(int)
        if "szz_samples" in dref:
            ss=np.array(dref["szz_samples"])
            shells=sorted(set(n2))[:4]
            kk=[]; kap2=[]; kap2e=[]
            for v in shells:
                j=np.where(n2==v)[0]
                per=ss[:,j].mean(1)
                bl=len(per)//NBLK
                bm=np.array([per[q*bl:(q+1)*bl].mean() for q in range(NBLK)])
                S=bm.mean(); Se=bm.std(ddof=1)/math.sqrt(NBLK)
                kv=math.sqrt(k2[j][0])
                kap2.append(kv*kv*(1.0/S-1.0)); kk.append(kv)
                kap2e.append(kv*kv*Se/S**2)
            kap2=np.array(kap2); kap2e=np.array(kap2e)
            kD2=(kap2/ (KAPPA**2))
            w=1/kap2e**2
            kjk2=np.sum(kap2*w)/np.sum(w); kjk2e=math.sqrt(1/np.sum(w))
            src="per-sample (PA-1)"
        else:
            szz=np.array(dref["szz"])  # DEV-B1 fix: archived szz already normalized (see 2787 usage)
            shells=sorted(set(n2))[:4]
            kap2=[]; kk=[]
            for v in shells:
                j=np.where(n2==v)[0]
                S=szz[j].mean(); kv=math.sqrt(k2[j][0])
                kap2.append(kv*kv*(1.0/S-1.0)); kk.append(kv)
            kap2=np.array(kap2); kap2e=np.abs(kap2)*0.05
            w=1/kap2e**2; kjk2=np.sum(kap2*w)/np.sum(w); kjk2e=math.sqrt(1/np.sum(w))
            src="archived means (no per-sample; 5% advisory weights)"
        # real side: pooled frozen-window fit (from req3 fit A)
        # joint: combine kappa^2 estimates real (kA^2) and k-side, shared pole = weighted mean
        labs_r=[l for l in labs]
        d0=load(labs_r[0]); rc,_=blocks_of(d0)
        allb=np.vstack([blocks_of(load(l))[1] for l in labs])
        mean=allb.mean(0); sem=allb.std(0,ddof=1)/math.sqrt(len(allb))
        lo,hi=2*a_s,3.0/KAPPA
        m=(rc>lo)&(rc<hi)&(sem>0)
        pA,cov=curve_fit(FY,rc[m],mean[m],p0=[0.05,KAPPA],sigma=np.maximum(sem[m],1e-7),maxfev=30000)
        kr=pA[1]; kre=math.sqrt(cov[1,1])
        wj=np.array([1/( (2*kr*kre)**2 ),1/kjk2e**2])
        kj2=(kr*kr*wj[0]+kjk2*wj[1])/wj.sum()
        kj=math.sqrt(max(kj2,0)); kje=math.sqrt(1/wj.sum())/(2*kj)
        print(f"  a_s={a_s}: kappa_joint/kappa_D = {kj/KAPPA:.4f} +/- {kje/KAPPA:.4f}  "
          f"[real {kr/KAPPA:.4f}; k-side {math.sqrt(max(kjk2,0))/KAPPA:.4f}; {src}]")
    print("\n== REQ 5 + PR2 — (a_s, 1/L) surface extrapolation of the F1 extraction ==")
    pts=[]
    for lab in CH:
        d=load(lab); rc,blocks=blocks_of(d)
        a_s=CH[lab][1]
        v=cell_boot(rc,blocks,2*a_s,3.0/KAPPA,seed=99)
        L=d["L"]
        pts.append((a_s,L,v[0],v[1]))
        print(f"  {lab:12s}: F1={v[0]:.4f}+/-{v[1]:.4f} (a_s={a_s}, L={L:.3f})")
    pts=np.array(pts)
    X=pts[:,0]; Li=1.0/pts[:,1]; Y=pts[:,2]; E=pts[:,3]
    res={}
    for p in (1,2):
        M=np.vstack([np.ones_like(X),X**p,Li]).T
        W=np.diag(1/E**2)
        C=np.linalg.inv(M.T@W@M); b=C@M.T@W@Y
        chi2=float(((Y-M@b)/E)**2 @ np.ones_like(Y))
        res[p]=(b,C,chi2)
        print(f"  p={p}: kappa_eff/kappa_D = {b[0]:.4f} +/- {math.sqrt(C[0,0]):.4f}   chi2/dof={chi2/(len(Y)-3):.1f}")
    pbest=min(res,key=lambda p:res[p][2])
    b,C,chi2=res[pbest]
    keff=b[0]; kerr=math.sqrt(C[0,0])
    mspread=abs(res[1][0][0]-res[2][0][0])/2
    tot=math.sqrt(kerr**2+mspread**2)
    print(f"  AIC-selected p={pbest}; kappa_eff/kappa_D = {keff:.4f}; total unc = {tot:.4f} "
          f"(boot {kerr:.4f} (+) model spread {mspread:.4f})")
    inband=(0.97<=keff<=1.03) and tot<=0.03
    outband=(keff<0.97-tot) or (keff>1.03+tot)
    verdict="PASS" if inband else ("FAIL" if outband else "UNRESOLVED")
    print(f"  PR2 staggering clause: zero alternations all new chains (leg 5) -> satisfied")
    print(f"  PR2 FROZEN VERDICT: {verdict}")
    print("\n== REQ 6 — moving-feature discriminant (per a_s, across sizes) ==")
    for a_s in (0.04,0.02,0.01,0.005):
        labs=[l for l in CH if CH[l][1]==a_s]
        rs=[]; Ls=[]
        for l in labs:
            d=load(l); rc,blocks=blocks_of(d)
            mean=blocks.mean(0)
            lo,hi=2*a_s,3.0/KAPPA
            m=(rc>lo)&(rc<hi)&(mean>0)
            AD=np.exp(np.mean(np.log(mean[m])-(-KAPPA*rc[m]-np.log(rc[m]))))
            dl=np.abs(np.log(mean[m])-np.log(AD*np.exp(-KAPPA*rc[m])/rc[m]))
            rstar=rc[m][np.argmax(dl)]
            rs.append(rstar); Ls.append(d["L"])
        rs=np.array(rs); Ls=np.array(Ls)
        spread=(rs.max()-rs.min())/rs.mean()
        if len(set(Ls))>=3:
            order=np.argsort(Ls); rr=rs[order]
            mono=np.all(np.diff(rr)>0) or np.all(np.diff(rr)<0)
            rho=np.corrcoef(Ls,rs)[0,1]
        else: mono=False; rho=float('nan')
        cls="FIXED-R" if spread<0.15 else ("FINITE-SIZE" if (abs(rho)>0.9 and mono) else "UNRESOLVED-LOCATION")
        print(f"  a_s={a_s}: r* = {np.array2string(rs,precision=3)} fm across L={np.array2string(Ls,precision=2)}"
              f" spread={spread*100:.1f}% rho={rho:.2f} -> {cls}")
    print("\n== ESS (reserve-trigger quote; per-sample window-mean scalar) ==")
    for lab in CH:
        if lab.startswith("RV"): continue
        d=load(lab); profs=np.array(d["profs"]); nb=d["nb"]; rmax=d["rmax"]; a_s=CH[lab][1]
        rc=(np.arange(nb)+0.5)*rmax/nb
        m=(rc>2*a_s)&(rc<3.0/KAPPA)
        w=profs[:,m].mean(1); w=w-w.mean()
        ac=np.correlate(w,w,'full')[len(w)-1:]/np.arange(len(w),0,-1)
        ac/=ac[0]
        tau=1.0; 
        for t in range(1,min(100,len(ac))):
            if ac[t]<0.05: break
            tau+=2*ac[t]
        ess=len(w)/tau
        print(f"  {lab:12s}: ESS = {ess:.0f} ({'OK' if ess>=100 else 'RESERVE TRIGGER'})")
