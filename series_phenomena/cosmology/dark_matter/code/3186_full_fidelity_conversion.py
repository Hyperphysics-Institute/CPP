#!/usr/bin/env python3
"""Patch 3186 -- OPEN-BAND-CONV-1 executed at FULL FIDELITY.
Prereg: openbandconv1_prereg.md (Patch 3185, committed BEFORE this ran).
Uses the MEASURED 72-bin a1 map, not an assumed parity."""
import os, json
import numpy as np
import importlib.util

HERE=os.path.dirname(os.path.abspath(__file__))
EM=os.path.normpath(os.path.join(HERE,"..","..","..","..","flagship_papers","electromagnetism","code"))
DATA=os.path.normpath(os.path.join(EM,"..","data","2914_response_fields.json"))

def _load(name, fn):
    sp=importlib.util.spec_from_file_location(name, os.path.join(EM,fn))
    m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
eng=_load("eng","2902_mobile_sea_engine.py")
_src=open(os.path.join(EM,"2907_round3_driver.py")).read()
_i=_src.index("def build_sea_sym"); _j=_src.index("\ndef ",_i+10)
_ns={"np":np,"eng":eng,"D0":eng.D0}
exec(compile(_src[_i:_j],"2907_build_sea_sym","exec"),_ns)
build_sea_sym=_ns["build_sea_sym"]
SOFT2=eng.SOFT2
XB=np.arange(-12.0,12.0+1e-9,1.0); RB=[(1.0,3.0),(3.0,5.0),(5.0,8.0)]

def axial_force(plus,minus,src=np.zeros(3)):
    out=0.0
    for arr,qe in ((plus,+1.0),(minus,-1.0)):
        d=src[None,:]-arr; R=np.linalg.norm(d,axis=1)
        amp=1.0/(4*np.pi*(R*R+SOFT2)); ux=d[:,0]/np.where(R>0,R,1.0)
        out+=float(np.sum(qe*amp*ux))
    return out

def bin_index(xi,rho):
    ib=np.digitize(xi,XB)-1
    idx=np.full(len(xi),-1,int)
    for ri,(rl,rh) in enumerate(RB):
        m=(rho>=rl)&(rho<rh)&(ib>=0)&(ib<len(XB)-1)
        idx[m]=ib[m]+ri*(len(XB)-1)
    return idx

def main():
    fields=json.load(open(DATA))["fields"]
    print("="*76)
    print("OPEN-BAND-CONV-1 -- FULL-FIDELITY CONVERSION (Patch 3186)")
    print("measured 72-bin a1 map; engine law amp=1/(4pi(R^2+SOFT2)); exact 2-member sum")
    print("="*76)
    for beta in ("0.05","0.1","0.2"):
        e=fields[beta]; m=np.array(e["m"]); se=np.array(e["se"]); N=np.array(e["N"])
        vals=[]; hi=[]; lo=[]
        for cls in ("A","B"):
            for seed in (4,5,6):
                sea,qs=build_sea_sym(cls,seed); Np=len(sea)//2
                plus,minus=sea[:Np].copy(),sea[Np:].copy()
                cen=0.5*(plus+minus)
                rho=np.hypot(cen[:,1],cen[:,2]); xi=cen[:,0]
                idx=bin_index(xi,rho)
                ok=idx>=0
                dp=np.zeros(Np); dp[ok]=m[idx[ok]]
                dhi=np.zeros(Np); dhi[ok]=m[idx[ok]]+se[idx[ok]]
                dlo=np.zeros(Np); dlo[ok]=m[idx[ok]]-se[idx[ok]]
                F0=axial_force(plus,minus)
                for prof,acc in ((dp,vals),(dhi,hi),(dlo,lo)):
                    p2,m2=plus.copy(),minus.copy()
                    p2[:,0]+=0.5*prof; m2[:,0]-=0.5*prof
                    acc.append(axial_force(p2,m2)-F0)
        v=np.array(vals); F=v.mean(); se_geom=v.std(ddof=1)/np.sqrt(len(v))
        se_map=abs(np.array(hi).mean()-np.array(lo).mean())/2
        signs=np.sign(v)
        stable=bool(np.all(signs==signs[0]))
        ratio=max(se_geom,se_map)/max(min(se_geom,se_map),1e-300)
        print(f"\nbeta = {beta}:  pairs in map = {int(ok.sum())}/{Np}")
        print(f"  F_MAP = {F:+.4e}   |F_MAP| = {abs(F):.4e}")
        print(f"  floor 1 (across-geometry SE) = {se_geom:.4e}")
        print(f"  floor 2 (archive per-bin se) = {se_map:.4e}")
        print(f"  floors ratio = {ratio:.2f} ({'OK' if ratio<=3 else 'DISAGREE >3x'});  "
              f"sign across 6 geometries: {'STABLE' if stable else 'UNSTABLE'}")
        print(f"  per-geometry dF: {' '.join(f'{x:+.2e}' for x in v)}")
        old=0.026*float(beta)
        print(f"  OLD transplanted band 0.026*beta = {old:.4e}  ->  ratio old/new = "
              f"{old/abs(F):.1f}x" if abs(F)>0 else "")
        print(f"  VERDICT: {'USABLE' if (ratio<=3 and stable) else 'UNSTABLE -> no arm re-comparison (prereg S3)'}")

if __name__=="__main__":
    main()
