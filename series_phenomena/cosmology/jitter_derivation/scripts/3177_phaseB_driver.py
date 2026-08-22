#!/usr/bin/env python
"""Patch 3179 -- D-JITTER-1 PHASE B DRIVER (prereg: phaseB_prereg.md,
Patch 3177, committed BEFORE this file existed -- the freeze).
Usage: python 3177_phaseB_driver.py all       (B-1 gate -> B-2 -> B-3+B-4)
       python 3177_phaseB_driver.py gate|kernel|attractor|intermit
B-1 blocks everything; B-5: both statistics print in EVERY outcome."""
import os
for v in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS","NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(v,"1")
import sys, json, importlib.util
import numpy as np

HERE=os.path.dirname(os.path.abspath(__file__))
SG=os.path.normpath(os.path.join(HERE,"..","..","sea_gravitation","scripts"))
R_A, R_SE = 1.357, 0.097          # Phase A, K=32 (phaseA_record.md)
SIG_STAR = 0.249                  # 3138 fixed point
DS_CAL, N_CAL, SEED_CAL = 4.636, 5, 5   # the calibrated spacing (3138 map cells single-seed)

def mod(name, d=SG):
    s=importlib.util.spec_from_file_location("m", os.path.join(d,name))
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def b1_gate():
    print("== B-1 REGRESSION GATE (drive OFF must be bit-identical) ==")
    eng=mod("3120_ds_indep_campaign.py")
    st_path=os.path.join(SG,"3147_n910_state.json")
    keys=("f_b","rho_swap","f_dwell","r","stat","m2","m4")
    if os.path.exists(st_path):
        st=json.load(open(st_path))
        cells=[k for k in ("9:2.2:5","10:2.0:11","11:2.1:5") if k in st]
        ok=True
        for c in cells:
            n,ds,sd=c.split(":"); z=eng.run(float(ds),int(n),int(sd))
            bad=[k for k in keys if k in st[c] and z[k]!=st[c][k]]
            print(f"  {c}: {'ELEMENT-EXACT' if not bad else 'MISMATCH '+str(bad)}")
            ok &= not bad
    else:
        z1=eng.run(3.0,3,5); z2=eng.run(3.0,3,5)
        ok=all(z1[k]==z2[k] for k in keys)
        print(f"  [no banked state here] OFF/OFF determinism: {'PASS' if ok else 'FAIL'}")
    print(f"B-1: {'PASS' if ok else 'VOID -- Phase B stops here (prereg B-1)'}")
    return ok

def arrival_pool(n_samp=4096, K=16, seed=5):
    """Per-axis arrival samples in ENGINE units at the calibrated spacing:
    Phase A shell-sum vectors (F_nn=1 units) scaled by 1/DS_CAL^2."""
    pa=mod("3168_phaseA_shell_sum.py", HERE)
    rng=np.random.default_rng(seed)
    out=np.empty((n_samp,3))
    for i in range(n_samp):
        F,_,_=pa.one_config(rng, K, 0.47, 0.5)
        out[i]=F
    return out/ DS_CAL**2          # engine field units (Gcp*qp=1 non-partner)

def b2_kernel(pool):
    print("\n== B-2 THE KERNEL (computed, not assumed) ==")
    sig_axis_engine=float(pool.std(axis=0).mean()); se=sig_axis_engine/np.sqrt(2*(len(pool)-1))
    k_emp=sig_axis_engine/R_A
    k_ana=(1.0/np.sqrt(3.0))/DS_CAL**2   # per-axis convention (Phase A R = vector norm of stds) x F_nn
    ratio=max(k_emp,k_ana)/min(k_emp,k_ana)
    print(f"  kappa_empirical = {k_emp:.5f} +/- {se/R_A:.5f}   (sigma_axis^engine {sig_axis_engine:.4f})")
    print(f"  kappa_analytic  = {k_ana:.5f}   [(1/sqrt3)/d_s^2 at d_s = {DS_CAL}]")
    print(f"  agreement factor = {ratio:.3f}  -> {'RESOLVED' if ratio<2 else 'UNRESOLVED-BY-KERNEL (no B-3 reading may be declared)'}")
    return (k_emp, ratio<2, sig_axis_engine)

def b3_attractor(pool, kernel_ok):
    print("\n== B-3 THE ATTRACTOR TEST (drive = computed arrivals, no tuning) ==")
    eng=mod("3120_ds_indep_campaign.py")
    base=eng.run(DS_CAL,N_CAL,SEED_CAL,probe=True)
    print(f"  baseline (Gaussian 0.30, drive OFF): sigma_amb = {base['sig_amb']:.4f}"
          f"   [3138 anchor ~0.246 -- statistic-implementation check]")
    Nc=2*N_CAL**3
    rng=np.random.default_rng(11)
    drive=np.empty((1024,Nc,3))
    idxs=rng.integers(0,len(pool),(1024,Nc))
    for t in range(1024): drive[t]=pool[idxs[t]]
    z=eng.run(DS_CAL,N_CAL,SEED_CAL,drive=drive,probe=True)
    sg=z["sig_amb"]
    print(f"  drive ON: sigma_gen = {sg:.4f}")
    if not kernel_ok:
        print("  READING: UNRESOLVED-BY-KERNEL (frozen B-3)"); return
    if 0.125<=sg<=0.498: print(f"  READING (frozen words): REPRODUCES  (sigma_gen in [0.125, 0.498] around 0.249)")
    elif sg>0.498: print("  READING (frozen words): MISSES-HIGH")
    else: print("  READING (frozen words): MISSES-LOW")

def b4_intermit(pool):
    print("\n== B-4 INTERMITTENCY (the founder's saltatory picture, tested) ==")
    x=(pool-pool.mean(0)).ravel()
    g2=float(np.mean(x**4)/np.mean(x**2)**2-3.0)
    se=np.sqrt(24.0/len(x))
    print(f"  excess kurtosis gamma2 = {g2:+.4f} +/- {se:.4f}  (N = {len(x)})")
    if g2>1 and g2>3*se: print("  READING (frozen words): INTERMITTENT -- the saltatory picture SUPPORTED")
    elif abs(g2)<=1:
        print("  READING (frozen words): NEAR-GAUSSIAN -- damages the picture as expressed by this model;"
              "\n   open alternatives (prereg B-4): the shell-sum is too coarse for saltation, OR"
              "\n   intermittency does not survive superposition over ~1e4 arrivals")
    else: print("  READING: UNRESOLVED")

if __name__=="__main__":
    modes=sys.argv[1] if len(sys.argv)>1 else "all"
    ok=b1_gate()
    if modes=="gate" or not ok: sys.exit(0 if ok else 1)
    pool=arrival_pool()
    k_emp,kok,_=b2_kernel(pool)
    if modes=="kernel": sys.exit(0)
    if modes in ("attractor","all"): b3_attractor(pool,kok)
    if modes in ("intermit","all"): b4_intermit(pool)
    print("\n[B-5: mean-based (B-3) and tail-based (B-4) both reported above; neither selectable.]")
