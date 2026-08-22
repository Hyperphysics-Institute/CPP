#!/usr/bin/env python3
"""Patch 3193 -- D-TAIL-1 executed. Prereg 3192, committed before this ran."""
import os
for v in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS","NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(v,"1")
import importlib.util, numpy as np
HERE=os.path.dirname(os.path.abspath(__file__))
SG=os.path.normpath(os.path.join(HERE,"..","scripts"))
sp=importlib.util.spec_from_file_location("m",os.path.join(SG,"3120_ds_indep_campaign.py"))
E=importlib.util.module_from_spec(sp); sp.loader.exec_module(E)
DS,N=4.636,5; Nc=2*N**3; T=1024; SEEDS=(5,11,17,23); SIG=0.30

def make(kind, sig, seed):
    rng=np.random.default_rng(1000+seed)
    if kind=="G": d=rng.normal(0,sig,(T,Nc,3))
    elif kind=="U":
        h=sig*np.sqrt(3.0); d=rng.uniform(-h,h,(T,Nc,3))
    else:
        p=float(kind[1:])/100.0
        amp=sig/np.sqrt(p)                      # variance = p*amp^2 = sig^2
        hit=rng.random((T,Nc,3))<p
        d=np.where(hit, rng.normal(0,amp,(T,Nc,3)), 0.0)
    return d

def kurt(d):
    x=d.ravel(); return float(np.mean((x-x.mean())**4)/np.mean((x-x.mean())**2)**2-3)

def cell(kind,sig,seed):
    d=make(kind,sig,seed)
    return E.run(DS,N,seed,drive=d,probe=True), float(d.std()), kurt(d)

def agg(rows,key):
    v=np.array([r[key] for r in rows]); return v.mean(), v.std(ddof=1)/np.sqrt(len(v))

print("="*72); print("D-TAIL-1 -- is variance a sufficient drive specification?"); print("="*72)
print("\n== POWER GATE (blocking): control G@0.30 vs G@0.45 ==")
ctrl={}
for sig in (0.30,0.45):
    rows=[]; 
    for s in SEEDS:
        z,sd,k=cell("G",sig,s); rows.append(z)
    ctrl[sig]=rows
    m,se=agg(rows,"f_b"); print(f"  G sigma={sig}: f_b = {m:.5f} +/- {se:.5f}")
m1,s1=agg(ctrl[0.30],"f_b"); m2,s2=agg(ctrl[0.45],"f_b")
sep=abs(m2-m1)/np.hypot(s1,s2)
print(f"  separation: {sep:.1f} SE -> {'PASS (f_b can see drive changes)' if sep>=3 else 'BLIND'}")
gate=sep>=3
if not gate:
    for k in ("rho_swap","f_dwell","sig_amb"):
        a,ae=agg(ctrl[0.30],k); b,be=agg(ctrl[0.45],k)
        s=abs(b-a)/np.hypot(ae,be); print(f"  fallback {k}: {s:.1f} SE")
        gate = gate or s>=3
if not gate:
    print("\nALL STATISTICS BLIND -> D-TAIL-1 VOID (prereg S3)"); raise SystemExit(0)

print("\n== MATCHED-VARIANCE DRIVES (all sigma = 0.30, tails differ) ==")
res={}
for kind in ("G","S2","S05","U"):
    rows=[];sds=[];ks=[]
    for s in SEEDS:
        z,sd,k=cell(kind,SIG,s); rows.append(z); sds.append(sd); ks.append(k)
    res[kind]=rows
    m,se=agg(rows,"f_b")
    print(f"  {kind:4s}: drive sigma={np.mean(sds):.4f} kurt={np.mean(ks):+8.2f} | "
          f"f_b = {m:.5f} +/- {se:.5f}")
print("\n== PAIRWISE vs Gaussian, primary statistic f_b ==")
g,ge=agg(res["G"],"f_b"); maxsep=0
for kind in ("S2","S05","U"):
    m,se=agg(res[kind],"f_b"); s=abs(m-g)/np.hypot(ge,se); maxsep=max(maxsep,s)
    print(f"  G vs {kind:4s}: delta f_b = {m-g:+.5f}   {s:.1f} SE")
print("\n== secondary statistics (reported, all outcomes) ==")
for k in ("rho_swap","f_dwell","sig_amb"):
    line=[]
    for kind in ("G","S2","S05","U"):
        m,se=agg(res[kind],k); line.append(f"{kind}={m:.4f}+/-{se:.4f}")
    print(f"  {k:9s}: "+"  ".join(line))
print("\n=== VERDICT (prereg S4, frozen words) ===")
print(("TAIL-SENSITIVE" if maxsep>=3 else "VARIANCE-SUFFICIENT")+
      f"  (max matched-variance separation {maxsep:.1f} SE; control separated at {sep:.1f} SE)")
