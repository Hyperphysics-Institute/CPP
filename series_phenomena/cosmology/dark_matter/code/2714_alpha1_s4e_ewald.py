#!/usr/bin/env python3
"""ALPHA-1 S4-E execution (Patch 2714) under the FROZEN 2713 prereg.
Ewald (tinfoil) two-species MC; criteria C1-C5 are the seats' own.
Runs execute individually (run_one) with JSON checkpoints; analyze()
computes the criteria. Side computation: RD Voronoi self-cell fraction."""
import math, json, sys, numpy as np
from scipy.special import erfc as serfc
from scipy.optimize import curve_fit

HBARC=197.3269788; ALPHA_EM=1/137.035999084
PHI=(1+math.sqrt(5))/2; A=0.589/PHI; KAPPA=2.0/A
NCP=2*math.sqrt(2.0)/A**3; Q2=ALPHA_EM*HBARC
THETA=2*math.sqrt(2)*math.pi*Q2/A
RUNS={"MAIN-A":(686,0.04,20260731,600,2400),"MAIN-B":(686,0.04,20260732,600,2400),
      "SIZE-S":(432,0.04,20260733,400,1600),"SIZE-L":(1024,0.04,20260734,400,1600),
      "CORE":(432,0.02,20260735,400,1600)}

def voronoi_rd():
    rng0=np.random.default_rng(7)
    nn=np.array([[1,1,0],[1,-1,0],[-1,1,0],[-1,-1,0],[1,0,1],[1,0,-1],[-1,0,1],[-1,0,-1],
                 [0,1,1],[0,1,-1],[0,-1,1],[0,-1,-1]],float)/math.sqrt(2.0)
    pts=rng0.uniform(-0.75*A,0.75*A,size=(800000,3))
    inside=np.max(np.abs(pts@nn.T),axis=1)<=A/2+1e-12
    P=pts[inside]; V_RD=(1.5*A)**3*inside.mean()
    r=np.linalg.norm(P,axis=1)
    frac=(KAPPA**2/(4*math.pi))*V_RD*np.mean(np.exp(-KAPPA*r)/r)
    return V_RD/(A**3/math.sqrt(2)),frac

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

def run_one(label):
    N,a_s,seed,eq,sw=RUNS[label]
    rng=np.random.default_rng(seed)
    L=(N/NCP)**(1.0/3.0); alpha=5.6/L; rc=L/2
    kv,k2=make_k(L); wk=np.exp(-k2/(4*alpha*alpha))/k2
    pref_k=2*(2*math.pi/(L**3))*Q2
    z=np.array([1.0]*(N//2)+[-1.0]*(N//2))
    pos=rng.uniform(0,L,size=(N,3))
    S=(z[:,None]*np.exp(1j*(pos@kv.T))).sum(0)
    step=0.20*A; acc=0; tot=0
    nb=90; rmax=min(rc,0.9); profs=[]; szz=np.zeros(len(k2)); ns=0
    for s_ in range(eq+sw):
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
                              +1.0/np.sqrt(r2o[mo]+a_s*a_s)))
            en=np.sum(zz[mn]*(serfc(alpha*rn[mn])/rn[mn]-1.0/rn[mn]
                              +1.0/np.sqrt(r2n[mn]+a_s*a_s)))
            dS=z[i]*(np.exp(1j*(newp@kv.T))-np.exp(1j*(pos[i]@kv.T)))
            Snew=S+dS
            dEk=pref_k*np.sum(wk*((Snew.real**2+Snew.imag**2)-(S.real**2+S.imag**2)))
            dE=en-eo+dEk; tot+=1
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
            szz+=(S.real**2+S.imag**2); ns+=1
    out={"label":label,"N":N,"a_s":a_s,"L":L,"acc":acc/tot,"ns":ns,
         "profs":profs,"szz":(szz/(ns*N)).tolist(),"k2":k2.tolist(),"rmax":rmax,"nb":nb}
    json.dump(out,open(f"/tmp/s4e_{label}.json","w"))
    print(f"[{label}] done: N={N} L={L:.3f} acc={acc/tot:.2f} samples={ns}")

def analyze():
    vr,frac=voronoi_rd()
    print(f"[Voronoi] V_RD check={vr:.4f} (exact 1) ; RD self-cell fraction = {frac:.4f} "
          f"(sphere 0.3029 ; L4 r<a 0.5940)")
    res={}
    for label in RUNS:
        d=json.load(open(f"/tmp/s4e_{label}.json"))
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
    kA,eA=res['MAIN-A'][0],res['MAIN-A'][1]; kB,eB=res['MAIN-B'][0],res['MAIN-B'][1]
    kmain=0.5*(kA+kB)
    C1=(abs(kmain/KAPPA-1)<=0.02) and res['MAIN-A'][2]==0 and res['MAIN-B'][2]==0
    C2=all(abs(res[r][4]/KAPPA-1)<=0.10 for r in ('MAIN-A','MAIN-B'))
    C3=all(res[r][3]<2 for r in res)
    ks=[res['SIZE-S'][0],kmain,res['SIZE-L'][0]]
    C4=(max(ks)-min(ks))/KAPPA<=0.05
    C5=abs(kA-kB)<=2*math.sqrt(eA*eA+eB*eB)
    print(f"\nMAIN combined kappa_fit = {kmain:.3f} ({kmain/KAPPA:.4f} x kappa_D) ; "
          f"|A-B|={abs(kA-kB):.3f} vs 2*comb_err={2*math.sqrt(eA*eA+eB*eB):.3f}")
    for n,v in zip("12345",[C1,C2,C3,C4,C5]): print(f"C{n}={'PASS' if v else 'FAIL'}",end="  ")
    print(f"->  S4-E {'PASS' if all([C1,C2,C3,C4,C5]) else 'FAIL'}")

if __name__=="__main__":
    if sys.argv[1]=="analyze": analyze()
    else: run_one(sys.argv[1])

# ---- chunked execution with checkpointing (environment call-limit workaround;
# ---- chartered totals preserved; disclosed in the record) ----
import pickle, os
def run_chunk(label, max_sweeps_this_call):
    N,a_s,seed,eq,sw=RUNS[label]; total=eq+sw
    ck=f"/tmp/s4e_ck_{label}.pkl"
    if os.path.exists(ck):
        st=pickle.load(open(ck,"rb"))
        rng=st["rng"]; pos=st["pos"]; S=st["S"]; done=st["done"]
        profs=st["profs"]; szz=st["szz"]; ns=st["ns"]; acc=st["acc"]; tot=st["tot"]
    else:
        rng=np.random.default_rng(seed)
        pos=None; S=None; done=0; profs=[]; ns=0; acc=0; tot=0
    L=(N/NCP)**(1.0/3.0); alpha=5.6/L; rc=L/2
    kv,k2=make_k(L); wk=np.exp(-k2/(4*alpha*alpha))/k2
    pref_k=2*(2*math.pi/(L**3))*Q2
    z=np.array([1.0]*(N//2)+[-1.0]*(N//2))
    if pos is None:
        pos=rng.uniform(0,L,size=(N,3))
        S=(z[:,None]*np.exp(1j*(pos@kv.T))).sum(0)
        szz=np.zeros(len(k2))
    step=0.20*A; nb=90; rmax=min(rc,0.9)
    end=min(total,done+max_sweeps_this_call)
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
                              +1.0/np.sqrt(r2o[mo]+a_s*a_s)))
            en=np.sum(zz[mn]*(serfc(alpha*rn[mn])/rn[mn]-1.0/rn[mn]
                              +1.0/np.sqrt(r2n[mn]+a_s*a_s)))
            dS=z[i]*(np.exp(1j*(newp@kv.T))-np.exp(1j*(pos[i]@kv.T)))
            Snew=S+dS
            dEk=pref_k*np.sum(wk*((Snew.real**2+Snew.imag**2)-(S.real**2+S.imag**2)))
            dE=en-eo+dEk; tot+=1
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
            szz+=(S.real**2+S.imag**2); ns+=1
    done=end
    pickle.dump({"rng":rng,"pos":pos,"S":S,"done":done,"profs":profs,
                 "szz":szz,"ns":ns,"acc":acc,"tot":tot},open(ck,"wb"))
    print(f"[{label}] {done}/{total} sweeps  acc={acc/max(tot,1):.2f}  samples={ns}")
    if done>=total:
        out={"label":label,"N":N,"a_s":a_s,"L":L,"acc":acc/tot,"ns":ns,
             "profs":profs,"szz":(szz/(ns*N)).tolist(),"k2":k2.tolist(),
             "rmax":rmax,"nb":nb}
        json.dump(out,open(f"/tmp/s4e_{label}.json","w"))
        print(f"[{label}] COMPLETE -> json")
