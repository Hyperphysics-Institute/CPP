#!/usr/bin/env python3
"""X3 EXECUTION under the FROZEN 2786 prereg + PA-1 (2788).
Machinery = committed 2761 clean pipeline VERBATIM; only the RUNS
table (X3 chains, seeds 20260803-04), checkpoint dir, and the PA-1
per-sample S_zz archival differ. Gate v2 (CONV-005, BLOCKING) must
PASS before any production sweep."""

import math, json, sys, os, pickle, gzip
import numpy as np
from scipy.special import erfc as serfc
from scipy.optimize import curve_fit

HBARC=197.3269788; ALPHA_EM=1/137.035999084
PHI=(1+math.sqrt(5))/2; A=0.589/PHI; KAPPA=2.0/A
NCP=2*math.sqrt(2.0)/A**3; Q2=ALPHA_EM*HBARC
THETA=2*math.sqrt(2)*math.pi*Q2/A
RUNS={"X3-R04":(686,0.04,20260803,600,4800),"X3-R02":(432,0.02,20260804,400,3200)}
CKDIR="/tmp/x3x4"; os.makedirs(CKDIR,exist_ok=True)
PA1_PER_SAMPLE=True  # Patch 2788 PA-1: archive per-sample S_zz

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
    return kv,(kv**2).sum(1)

def geom(label):
    N,a_s,seed,eq,sw=RUNS[label]
    L=(N/NCP)**(1.0/3.0); alpha=5.6/L; rc=L/2
    kv,k2=make_k(L); wk=np.exp(-k2/(4*alpha*alpha))/k2
    pref_k=2*(2*math.pi/(L**3))*Q2
    z=np.array([1.0]*(N//2)+[-1.0]*(N//2))
    return N,a_s,seed,eq,sw,L,alpha,rc,kv,k2,wk,pref_k,z

def dE_A_fixed(i,newp,pos,z,L,alpha,rc,a_s,kv,wk,pref_k,S):
    """The campaign increment WITH THE FIX (mn[i]=False)."""
    d_o=pos-pos[i]; d_n=pos-newp
    d_o-=L*np.round(d_o/L); d_n-=L*np.round(d_n/L)
    r2o=(d_o**2).sum(1); r2n=(d_n**2).sum(1)
    ro=np.sqrt(r2o); rn=np.sqrt(r2n)
    zz=Q2*(z*z[i])
    mo=(ro<rc)&(ro>1e-12); mn=(rn<rc)&(rn>1e-12)
    mn[i]=False   # <-- THE FIX (2754 defect: old-new self-pair)
    eo=np.sum(zz[mo]*(serfc(alpha*ro[mo])/ro[mo]-1.0/ro[mo]
                      +1.0/np.sqrt(r2o[mo]+a_s*a_s)))
    en=np.sum(zz[mn]*(serfc(alpha*rn[mn])/rn[mn]-1.0/rn[mn]
                      +1.0/np.sqrt(r2n[mn]+a_s*a_s)))
    dS=z[i]*(np.exp(1j*(newp@kv.T))-np.exp(1j*(pos[i]@kv.T)))
    Snew=S+dS
    dEk=pref_k*np.sum(wk*((Snew.real**2+Snew.imag**2)-(S.real**2+S.imag**2)))
    return en-eo+dEk,Snew

def total_E(pos,z,L,alpha,rc,a_s,kv,wk,pref_k):
    """Independent brute-force B total: full pair sum + k-space, no increments."""
    N=len(pos)
    d=pos[:,None,:]-pos[None,:,:]; d-=L*np.round(d/L)
    r2=(d**2).sum(2); rr=np.sqrt(r2)
    iu=np.triu_indices(N,1)
    r=rr[iu]; r2u=r2[iu]
    zz=(Q2*np.outer(z,z))[iu]
    m=(r<rc)&(r>1e-12)
    Er=np.sum(zz[m]*(serfc(alpha*r[m])/r[m]-1.0/r[m]+1.0/np.sqrt(r2u[m]+a_s*a_s)))
    S=(z[:,None]*np.exp(1j*(pos@kv.T))).sum(0)
    Ek=pref_k*np.sum(wk*(S.real**2+S.imag**2))
    return Er+Ek

def gate_v2():
    """CONV-005 v2 BLOCKING gate (panel-ratified Patch 2764): per
    geometry, >=20 random states x >=20 proposed moves (=400 checks),
    mandatorily including boundary-crossing moves, near-core moves,
    particle-index edge cases (i=0, i=N-1), deliberately large
    displacements, and the zero-move identity; |dH_inc - dH_full| <=
    1e-10*max(1,|dH_full|); inverse-move antisymmetry dH(x->x') =
    -dH(x'->x). ANY failure BLOCKS production."""
    for label in RUNS:
        N,a_s,_,_,_,L,alpha,rc,kv,k2,wk,pref_k,z=geom(label)
        g=np.random.default_rng(1)
        worst=0.0; worst_anti=0.0; nchk=0
        for st in range(20):
            pos=g.uniform(0,L,size=(N,3))
            # near-core state variant: every 4th state, plant a close pair
            if st%4==3: pos[1]=(pos[0]+np.array([1.2*a_s,0,0]))%L
            S=(z[:,None]*np.exp(1j*(pos@kv.T))).sum(0)
            E0=total_E(pos,z,L,alpha,rc,a_s,kv,wk,pref_k)
            for mv in range(20):
                if mv==0: i=0
                elif mv==1: i=N-1
                elif mv==2 and st%4==3: i=1          # near-core mover
                else: i=int(g.integers(N))
                if mv==3:
                    newp=pos[i].copy()               # zero-move identity
                elif mv==4:
                    newp=(pos[i]+np.array([0.9*L,0.4*L,0.7*L]))%L  # large/boundary
                elif mv==5:
                    newp=(pos[i]+g.normal(0,0.45*L,3))%L           # large random
                else:
                    newp=(pos[i]+g.normal(0,0.20*A,3))%L
                dA,Snew=dE_A_fixed(i,newp,pos,z,L,alpha,rc,a_s,kv,wk,pref_k,S)
                save=pos[i].copy(); pos[i]=newp
                dB=total_E(pos,z,L,alpha,rc,a_s,kv,wk,pref_k)-E0
                # inverse-move antisymmetry from the moved state
                dAr,_=dE_A_fixed(i,save,pos,z,L,alpha,rc,a_s,kv,wk,pref_k,Snew)
                pos[i]=save
                rel=abs(dA-dB)/max(1.0,abs(dB))
                anti=abs(dA+dAr)/max(1.0,abs(dA))
                worst=max(worst,rel); worst_anti=max(worst_anti,anti); nchk+=1
        ok=(worst<=1e-10) and (worst_anti<=1e-10)
        print(f"GATE v2 {label}: {nchk} checks, worst |dH_inc-dH_full| rel = {worst:.3e}, "
              f"worst antisymmetry = {worst_anti:.3e} -> {'PASS' if ok else 'FAIL'}")
        if not ok:
            print("GATE v2 FAIL -> PRODUCTION BLOCKED (CONV-005 v2). Report the defect.")
            sys.exit(1)
    print("GATE v2: ALL GEOMETRIES PASS. Production licensed.")

def run_chunk(label,max_sweeps_this_call):
    N,a_s,seed,eq,sw,L,alpha,rc,kv,k2,wk,pref_k,z=geom(label)
    total=eq+sw; ck=f"{CKDIR}/ck_{label}.pkl"
    if os.path.exists(ck):
        st=pickle.load(open(ck,"rb"))
        rng=st["rng"]; pos=st["pos"]; S=st["S"]; done=st["done"]
        profs=st["profs"]; szz=st["szz"]; szz_samples=st.get("szz_samples",[]); ns=st["ns"]; acc=st["acc"]; tot=st["tot"]
    else:
        rng=np.random.default_rng(seed)
        pos=rng.uniform(0,L,size=(N,3))
        S=(z[:,None]*np.exp(1j*(pos@kv.T))).sum(0)
        done=0; profs=[]; szz=np.zeros(len(k2)); szz_samples=[]; ns=0; acc=0; tot=0
    step=0.20*A; nb=90; rmax=min(rc,0.9)
    end=min(total,done+max_sweeps_this_call)
    for s_ in range(done,end):
        for _ in range(N):
            i=int(rng.integers(N))
            newp=(pos[i]+rng.normal(0,step,3))%L
            dE,Snew=dE_A_fixed(i,newp,pos,z,L,alpha,rc,a_s,kv,wk,pref_k,S)
            tot+=1
            if dE<=0 or rng.random()<math.exp(-dE/THETA):
                pos[i]=newp; S=Snew; acc+=1
        if s_>=eq and (s_-eq)%5==0:
            zsum=np.zeros(nb); c=np.zeros(nb)
            for i in range(N):
                d=pos-pos[i]; d-=L*np.round(d/L)
                rr=np.sqrt((d**2).sum(1)); rr[i]=1e9
                idx=np.clip((rr/rmax*nb).astype(int),0,nb)
                m=idx<nb
                zsum+=np.bincount(idx[m],weights=-(z*z[i])[m],minlength=nb)
                c+=np.bincount(idx[m],minlength=nb)
            profs.append((np.where(c>0,zsum/np.maximum(c,1),0.0)).tolist())
            row=(S.real**2+S.imag**2); szz+=row; szz_samples.append((row/N).tolist()); ns+=1  # PA-1
    # X5b-spirit drift cross-check: incremental S vs fresh full summation
    Sfresh=(z[:,None]*np.exp(1j*(pos@kv.T))).sum(0)
    drift=float(np.max(np.abs(S-Sfresh)))
    assert drift<1e-6, f"S-drift {drift:.3e} exceeds 1e-6 -- STOP"
    done=end
    pickle.dump({"rng":rng,"pos":pos,"S":Sfresh,"done":done,"profs":profs,
                 "szz":szz,"szz_samples":szz_samples,"ns":ns,"acc":acc,"tot":tot},open(ck,"wb"))
    print(f"[{label}] {done}/{total} sweeps  acc={acc/max(tot,1):.2f}  samples={ns}  Sdrift={drift:.2e}")
    if done>=total:
        out={"label":label,"N":N,"a_s":a_s,"L":L,"acc":acc/tot,"ns":ns,
             "profs":profs,"szz":(szz/(ns*N)).tolist(),"k2":k2.tolist(),
             "rmax":rmax,"nb":nb,"szz_samples":szz_samples}  # PA-1
        json.dump(out,open(f"{CKDIR}/rv_{label}.json","w"))
        print(f"[{label}] COMPLETE -> json")

def analyze():
    """VERBATIM 2714 analyze() logic (frozen 2713 criteria) on RV jsons.
    Label mapping: RV-MAIN-A/-B/-SIZE-S/-SIZE-L/-CORE."""
    res={}
    for label in RUNS:
        d=json.load(open(f"{CKDIR}/rv_{label}.json"))
        profs=np.array(d["profs"]); nb=d["nb"]; rmax=d["rmax"]; a_s=d["a_s"]
        nblk=10; bl=len(profs)//nblk
        bm=np.array([profs[j*bl:(j+1)*bl].mean(0) for j in range(nblk)])
        mean=bm.mean(0); sem=bm.std(0,ddof=1)/math.sqrt(nblk)
        rcen=(np.arange(nb)+0.5)*rmax/nb
        lo,hi=2*a_s,3.0/KAPPA
        m=(rcen>lo)&(rcen<hi)&(sem>0)
        x,y,e=rcen[m],mean[m],np.maximum(sem[m],1e-7)
        fmono=lambda r_,Aa,k_: Aa*np.exp(-k_*r_)/r_
        fosc=lambda r_,Aa,k_,k0,ph: Aa*np.exp(-k_*r_)*np.cos(k0*r_+ph)/r_
        pm,pc=curve_fit(fmono,x,y,p0=[0.05,KAPPA],sigma=e,maxfev=20000)
        km=pm[1]; kerr=math.sqrt(max(pc[1][1],0))
        chi_m=np.sum(((y-fmono(x,*pm))/e)**2)
        try:
            po,_=curve_fit(fosc,x,y,p0=[0.05,KAPPA,8.0,0.0],sigma=e,maxfev=60000)
            chi_o=np.sum(((y-fosc(x,*po))/e)**2)
        except Exception: chi_o=chi_m+100
        daic=(chi_m+4)-(chi_o+8)
        lead=np.sign(y[np.argmax(np.abs(y))])
        viol=int(np.sum((np.sign(y)!=lead)&(np.abs(y)>2*e)))
        k2=np.array(d["k2"]); szz=np.array(d["szz"]); L=d["L"]
        n2=np.round(k2/(2*math.pi/L)**2).astype(int)
        sh={}
        for j,v in enumerate(n2): sh.setdefault(int(v),[]).append(j)
        kk=[];ss=[]
        for v in sorted(sh)[:5]:
            kk.append(math.sqrt(np.mean(k2[sh[v]]))); ss.append(float(np.mean(szz[sh[v]])))
        kk=np.array(kk); ss=np.array(ss)
        ps,_=curve_fit(lambda k_,kq: k_*k_/(k_*k_+kq*kq),kk,ss,p0=[KAPPA],maxfev=10000)
        kS=abs(ps[0])
        res[label]=(km,kerr,viol,daic,kS)
        print(f"[{label}] kappa_fit={km:.3f}+/-{kerr:.3f} ({km/KAPPA:.4f}x) "
              f"alt={viol} dAIC_osc={daic:+.1f} kappa_S={kS:.3f} ({kS/KAPPA:.3f}x)")
    kA,eA=res['RV-MAIN-A'][0],res['RV-MAIN-A'][1]; kB,eB=res['RV-MAIN-B'][0],res['RV-MAIN-B'][1]
    kmain=0.5*(kA+kB)
    C1=(abs(kmain/KAPPA-1)<=0.02) and res['RV-MAIN-A'][2]==0 and res['RV-MAIN-B'][2]==0
    C2=all(abs(res[r][4]/KAPPA-1)<=0.10 for r in ('RV-MAIN-A','RV-MAIN-B'))
    C3=all(res[r][3]<2 for r in res)
    ks=[res['RV-SIZE-S'][0],kmain,res['RV-SIZE-L'][0]]
    C4=(max(ks)-min(ks))/KAPPA<=0.05
    C5=abs(kA-kB)<=2*math.sqrt(eA*eA+eB*eB)
    print(f"\nMAIN combined kappa_fit = {kmain:.3f} ({kmain/KAPPA:.4f} x kappa_D) ; "
          f"|A-B|={abs(kA-kB):.3f} vs 2*comb_err={2*math.sqrt(eA*eA+eB*eB):.3f}")
    for n,v in zip("12345",[C1,C2,C3,C4,C5]): print(f"C{n}={'PASS' if v else 'FAIL'}",end="  ")
    print(f"->  RV S4-E {'PASS' if all([C1,C2,C3,C4,C5]) else 'FAIL'}")

def archive():
    dest=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","data","rv2714")
    os.makedirs(dest,exist_ok=True)
    for label in RUNS:
        src=f"{CKDIR}/rv_{label}.json"
        with open(src,"rb") as f, gzip.open(os.path.join(dest,f"rv_{label}.json.gz"),"wb") as g:
            g.write(f.read())
        print(f"archived rv_{label}.json.gz")

if __name__=="__main__":
    cmd=sys.argv[1]
    if cmd=="gate": gate_v2()
    elif cmd=="chunk": run_chunk(sys.argv[2],int(sys.argv[3]))
    elif cmd=="analyze": analyze()
    elif cmd=="archive": archive()
