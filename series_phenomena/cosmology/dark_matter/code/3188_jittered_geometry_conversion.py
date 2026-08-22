#!/usr/bin/env python3
"""Patch 3188 -- OPEN-BAND-CONV-1b: F_MAP recomputed on the geometry the
campaign arms ACTUALLY used (build_sea_jittered). Prereg 3187, committed
before this ran."""
import os, json
import numpy as np, importlib.util
HERE=os.path.dirname(os.path.abspath(__file__))
EM=os.path.normpath(os.path.join(HERE,"..","..","..","..","flagship_papers","electromagnetism","code"))
DATA=os.path.normpath(os.path.join(EM,"..","data","2914_response_fields.json"))
sp=importlib.util.spec_from_file_location("eng",os.path.join(EM,"2902_mobile_sea_engine.py"))
eng=importlib.util.module_from_spec(sp); sp.loader.exec_module(eng)
SOFT2=eng.SOFT2
# campaign constants, verbatim from 3167_beta_ladder_driver.py
SEED_GEN=31670817; RHO,SPACING=(1.0,8.0),2.5; JIT_LO,JIT_HI=-0.05,0.05
X_HALF,X_SRC0=28.0,-24.0
SEEDS=np.random.default_rng(SEED_GEN).integers(10**6,10**7,size=8)
XB=np.arange(-12.0,12.0+1e-9,1.0); RB=[(1.0,3.0),(3.0,5.0),(5.0,8.0)]

def build_sea_jittered(seed):
    kx=int(np.floor(X_HALF/SPACING)); xs=SPACING*np.arange(-kx,kx+1)
    ky=int(np.floor(RHO[1]/SPACING)); ys=SPACING*np.arange(-ky,ky+1)
    rng=np.random.default_rng(seed); c,o,s=[],[],[]
    for x in xs:
        for y in ys:
            for z in ys:
                rho=np.hypot(y,z)
                if RHO[0]<=rho<=RHO[1]:
                    c.append((x,y,z)); o.append((0.0,y/rho,z/rho))
                    s.append(eng.D0+rng.uniform(JIT_LO,JIT_HI))
    c=np.array(c); o=np.array(o); s=np.array(s)[:,None]
    return c+0.5*s*o, c-0.5*s*o, c

def axial_force(plus,minus,src):
    out=0.0
    for arr,qe in ((plus,+1.0),(minus,-1.0)):
        d=src[None,:]-arr; R=np.linalg.norm(d,axis=1)
        amp=1.0/(4*np.pi*(R*R+SOFT2)); ux=d[:,0]/np.where(R>0,R,1.0)
        out+=float(np.sum(qe*amp*ux))
    return out

def bins(xi,rho):
    ib=np.digitize(xi,XB)-1; idx=np.full(len(xi),-1,int)
    for ri,(rl,rh) in enumerate(RB):
        m=(rho>=rl)&(rho<rh)&(ib>=0)&(ib<len(XB)-1)
        idx[m]=ib[m]+ri*(len(XB)-1)
    return idx

def main():
    f=json.load(open(DATA))["fields"]
    src=np.array([X_SRC0,0.0,0.0])
    print("="*74); print("OPEN-BAND-CONV-1b -- CAMPAIGN GEOMETRY (build_sea_jittered)")
    print(f"X_HALF={X_HALF} RHO={RHO} SPACING={SPACING} source x={X_SRC0}"); print("="*74)
    F_MAP_SYM={"0.05":1.3905e-04,"0.1":5.9711e-04,"0.2":8.2175e-04}
    for beta in ("0.05","0.1","0.2"):
        e=f[beta]; m=np.array(e["m"]); se=np.array(e["se"])
        vals,hi,lo=[],[],[]
        for seed in SEEDS[:6]:
            plus,minus,cen=build_sea_jittered(int(seed))
            rho=np.hypot(cen[:,1],cen[:,2]); xi=cen[:,0]-X_SRC0
            idx=bins(xi,rho); ok=idx>=0
            F0=axial_force(plus,minus,src)
            for prof,acc in ((m,vals),(m+se,hi),(m-se,lo)):
                dp=np.zeros(len(cen)); dp[ok]=prof[idx[ok]]
                p2,m2=plus.copy(),minus.copy()
                p2[:,0]+=0.5*dp; m2[:,0]-=0.5*dp
                acc.append(axial_force(p2,m2,src)-F0)
        v=np.array(vals); F=v.mean(); se_g=v.std(ddof=1)/np.sqrt(len(v))
        se_m=abs(np.array(hi).mean()-np.array(lo).mean())/2
        ratio=max(se_g,se_m)/max(min(se_g,se_m),1e-300)
        stable=bool(np.all(np.sign(v)==np.sign(v[0])))
        usable=ratio<=3 and stable
        Fs=F_MAP_SYM[beta]
        print(f"\nbeta={beta}: pairs in map {int(ok.sum())}/{len(cen)}")
        print(f"  F_JIT = {F:+.4e}   floors: geom {se_g:.3e} | archive {se_m:.3e}  ratio {ratio:.2f}"
              f"  sign {'STABLE' if stable else 'UNSTABLE'} -> {'USABLE' if usable else 'UNSTABLE'}")
        print(f"  F_SYM (3186) = {Fs:+.4e}   ->  F_JIT/F_SYM = {F/Fs:.2f}x"
              f"   [prereg S5: >2x or <0.5x means the geometries DIFFER MATERIALLY]")
        print(f"  per-seed: {' '.join(f'{x:+.2e}' for x in v)}")
    print("\n[arm re-comparison: prereg S4 requires >=3 admissible arms; reported in the record]")
if __name__=="__main__": main()
