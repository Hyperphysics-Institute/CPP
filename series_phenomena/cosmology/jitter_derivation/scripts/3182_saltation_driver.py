#!/usr/bin/env python
"""Patch 3182 -- D-SALT-1: the POWERED saltation test.
Prereg: phaseD_saltation_prereg.md (committed BEFORE this file ran).
Order is enforced: POWER GATE -> null control -> engine -> readings.
Usage: python 3182_saltation_driver.py"""
import os
for v in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS","NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(v,"1")
import importlib.util, numpy as np

HERE=os.path.dirname(os.path.abspath(__file__))
SG=os.path.normpath(os.path.join(HERE,"..","..","sea_gravitation","scripts"))
DS,N,SEED=4.636,5,5
T,NCP=1002,250

def eng():
    s=importlib.util.spec_from_file_location("m",os.path.join(SG,"3120_ds_indep_campaign.py"))
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def stats(series):
    """series: (T, NCP) -> per-CP kurtosis & burst, then mean +/- SE across CPs."""
    x=series-series.mean(0)
    m2=(x**2).mean(0); m4=(x**4).mean(0)
    g2=m4/np.maximum(m2,1e-300)**2-3.0
    med=np.median(series,0)
    burst=(series>5*med[None,:]).mean(0)
    n=series.shape[1]
    return (float(g2.mean()), float(g2.std(ddof=1)/np.sqrt(n)),
            float(burst.mean()), float(burst.std(ddof=1)/np.sqrt(n)))

def synth(kind, seed=7):
    rng=np.random.default_rng(seed)
    if kind=="null":
        return np.abs(rng.normal(0,1,(T,NCP)))
    s=np.abs(rng.normal(0,1,(T,NCP)))
    hit=rng.random((T,NCP))<0.02
    s[hit]*=8.0
    return s

import sys
if len(sys.argv)>1 and sys.argv[1]=="sweep":
    # Patch 3183: the FROZEN falsifier of the masking hypothesis.
    # Prediction (frozen before this runs): burst on |F|_nonpartner rises
    # MONOTONICALLY as the drive amplitude falls to zero. A non-monotone or
    # flat result REFUTES the masking account.
    E=eng(); Nc=2*N**3
    print("D-SALT-1 SWEEP -- masking falsifier (frozen: burst must rise monotonically as amp -> 0)")
    print(f"  Gaussian-null burst reference: 0.00078")
    prev=None; mono=True
    for amp in (0.30, 0.20, 0.10, 0.05, 0.0):
        rng=np.random.default_rng(11)
        d=np.zeros((1024,Nc,3)) if amp==0 else rng.normal(0,amp,(1024,Nc,3))
        z=E.run(DS,N,SEED,drive=d,fprobe=True)
        st=stats(z["fp_np"])
        if prev is not None and st[2] < prev - 1e-12: mono=False
        prev=st[2]
        print(f"  drive sigma={amp:.2f}: burst = {st[2]:.5f} +/- {st[3]:.5f}   gamma2 = {st[0]:+.4f} +/- {st[1]:.4f}")
    print(f"  VERDICT (frozen): {'MONOTONE-RISE -> masking account SUPPORTED' if mono else 'NON-MONOTONE -> masking account REFUTED'}")
    raise SystemExit(0)

print("="*70)
print("D-SALT-1  --  POWER GATE FIRST (prereg S3); no engine number before it passes")
print("="*70)
gn=stats(synth("null")); gs=stats(synth("salt"))
sep_g=abs(gs[0]-gn[0])/np.hypot(gs[1],gn[1])
sep_b=abs(gs[2]-gn[2])/np.hypot(gs[3],gn[3])
print(f"  synthetic NULL : gamma2 = {gn[0]:+.4f} +/- {gn[1]:.4f}   burst = {gn[2]:.5f} +/- {gn[3]:.5f}")
print(f"  synthetic SALT : gamma2 = {gs[0]:+.4f} +/- {gs[1]:.4f}   burst = {gs[2]:.5f} +/- {gs[3]:.5f}")
print(f"  separation: gamma2 {sep_g:.1f} SE {'PASS' if sep_g>=5 else 'FAIL -> BLIND'};"
      f"  burst {sep_b:.1f} SE {'PASS' if sep_b>=5 else 'FAIL -> BLIND'}")
g_ok, b_ok = sep_g>=5, sep_b>=5
if not (g_ok or b_ok):
    print("\nBOTH STATISTICS BLIND -> D-SALT-1 VOID (prereg S3). No engine measurement reported.")
    raise SystemExit(0)

print("\n== ENGINE (driven, Gaussian 0.30) and NULL CONTROL (drive = 0) ==")
E=eng()
z=E.run(DS,N,SEED,fprobe=True)
Nc=2*N**3
z0=E.run(DS,N,SEED,drive=np.zeros((1024,Nc,3)),fprobe=True)
out={}
for lab,zz in (("driven",z),("zero-drive",z0)):
    for key,nm in (("fp_np","|F|_nonpartner"),("fp_tot","|F|_total")):
        st=stats(zz[key])
        out[(lab,nm)]=st
        print(f"  {lab:11s} {nm:16s}: gamma2 = {st[0]:+9.4f} +/- {st[1]:.4f}   "
              f"burst = {st[2]:.5f} +/- {st[3]:.5f}")

print("\n== READINGS (prereg S5; primary = |F|_nonpartner, driven) ==")
p=out[("driven","|F|_nonpartner")]
dg=(p[0]-gn[0])/np.hypot(p[1],gn[1])
db=(p[2]-gn[2])/np.hypot(p[3],gn[3])
print(f"  gamma2 vs Gaussian null: {dg:+.1f} SE {'' if g_ok else '[BLIND -- no reading]'}")
print(f"  burst  vs Gaussian null: {db:+.1f} SE {'' if b_ok else '[BLIND -- no reading]'}")
if g_ok and b_ok:
    if dg>=5 and db>=5: r="INTERMITTENT -- the founder's picture SUPPORTED by the engine's own dynamics"
    elif abs(dg)<=3 and abs(db)<=3: r=("NEAR-GAUSSIAN -- picture DAMAGED at Moment cadence; prereg S6 alternatives remain open:\n"
        "     (a) sub-Moment saltation (founder's S3 Q4), (b) saltation only in entity-built Seas, (c) genuinely absent")
    elif (dg>=5)!=(db>=5): r="MIXED -- the two statistics disagree; reported as a result, neither selected (B-5)"
    else: r="UNRESOLVED"
    print(f"  VERDICT (frozen words): {r}")
c=out[("zero-drive","|F|_nonpartner")]
same=abs(c[0]-p[0])<=3*np.hypot(c[1],p[1])
print(f"\n  null control: zero-drive gamma2 = {c[0]:+.4f} vs driven {p[0]:+.4f} -> "
      f"{'AGREE => saltation is the ENGINE dynamics, not the drive' if same else 'DIFFER => the drive contributes'}")
