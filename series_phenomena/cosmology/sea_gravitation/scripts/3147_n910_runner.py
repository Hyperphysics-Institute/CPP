#!/usr/bin/env python
"""Patch 3147 -- the CONV-021-mandated pass: n = 9 and n = 10 with
scale-invariant diagnostics. Decision rule FROZEN in
conv021_2026-08_returns_adjudication.md S3 BEFORE this ran.
Usage:  python 3147_n910_runner.py run 9      (~3 h, 16 workers)
        python 3147_n910_runner.py run 10     (~6-8 h, 8 workers)
        python 3147_n910_runner.py run anom   (Q5 fine grid, n=8,9)
        python 3147_n910_runner.py analyze
"""
import os
for _v in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS","NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import sys, json, importlib.util
from multiprocessing import Pool
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, "3147_n910_state.json")
GRID = [1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0]
FINE = [1.75,1.90,2.10,2.25]
SEEDS = [5,11]
PRIOR_PEAK = {3:3.420, 4:3.338, 5:3.106, 6:2.649, 7:2.617, 8:2.6143}

def _mod(n):
    s = importlib.util.spec_from_file_location("m", os.path.join(HERE, n))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def cell(a):
    ds, n, sd = a
    return (f"{n}:{ds}:{sd}", _mod("3120_ds_indep_campaign.py").run(ds, n, sd))

def save(st): json.dump(st, open(STATE,"w"))

def cmd_run(which):
    st = json.load(open(STATE)) if os.path.exists(STATE) else {}
    if which == "fb":            # Patch 3170: the 3166 prereg's execution mode
        FBGRID = [1.9, 2.0, 2.1, 2.2, 2.3]
        todo = [(ds,n,sd) for n in (7,8,9,10,11) for ds in FBGRID
                for sd in SEEDS if f"{n}:{ds}:{sd}" not in st]; nw = 16
    elif which == "anom":
        todo = [(ds,n,sd) for n in (8,9) for ds in FINE for sd in SEEDS
                if f"{n}:{ds}:{sd}" not in st]; nw = 16
    elif which == "cross":       # Patch 3156: the Binder-crossing confirmation
        todo = [(ds,n,sd) for n in (8,9,10) for ds in (1.78,1.82,1.86)
                for sd in SEEDS if f"{n}:{ds}:{sd}" not in st]; nw = 12
    elif which == "anom11":      # Patch 3155: the spot-check at n=11
        todo = [(ds,11,sd) for ds in (1.9,2.0,2.1,2.2) for sd in SEEDS
                if f"11:{ds}:{sd}" not in st]; nw = 8
    elif which == "anom10":      # Patch 3154: the spike's size-scaling at n=10
        todo = [(ds,10,sd) for ds in FINE for sd in SEEDS
                if f"10:{ds}:{sd}" not in st]; nw = 8
    else:
        n = int(which)
        todo = [(ds,n,sd) for ds in GRID for sd in SEEDS if f"{n}:{ds}:{sd}" not in st]
        nw = 16 if n <= 9 else 8      # memory headroom at n=10
    print(f"cells remaining: {len(todo)}; workers: {min(nw,max(1,len(todo)))}")
    with Pool(min(nw, max(1,len(todo)))) as p:
        for k,z in p.imap_unordered(cell, todo):
            st[k]=z; save(st)
            print(f"  done {k}: f_b={z['f_b']:.4f} binder={z['binder']}")
    print("RUN COMPLETE.")

def peak(xs, ys):
    x=np.asarray(xs,float); y=np.asarray(ys,float)
    if np.isnan(y).any() or len(y)<3: return None
    g=np.abs(np.gradient(y,x)); i=int(np.argmax(g))
    if i==0 or i==len(x)-1: return None
    A=np.vstack([x[i-1:i+2]**2, x[i-1:i+2], np.ones(3)]).T
    a,b,_=np.linalg.solve(A,g[i-1:i+2])
    return float(-b/(2*a)) if a<0 else float(x[i])

def cmd_analyze():
    st=json.load(open(STATE))
    have=sorted({int(k.split(":")[0]) for k in st})
    fbn={}; bdn={}
    for n in have:
        ds=[d for d in GRID if f"{n}:{d}:5" in st and f"{n}:{d}:11" in st]
        if len(ds)<len(GRID): continue
        fbn[n]=(ds,[np.mean([st[f"{n}:{d}:{s}"]["f_b"] for s in SEEDS]) for d in ds])
        bdn[n]=(ds,[np.mean([st[f"{n}:{d}:{s}"]["binder"] for s in SEEDS]) for d in ds])
    pk=dict(PRIOR_PEAK)
    for n,(ds,v) in fbn.items():
        p=peak(ds,v); pk[n]=p
        print(f"n={n}: peak = {p if p is None else f'{p:.4f}'}")
    # E1 + frozen convergence test
    seq=[pk[n] for n in sorted(pk) if pk[n] is not None]
    steps=[seq[i+1]-seq[i] for i in range(len(seq)-1)]
    ok = (len(seq)>=6 and abs(steps[-1])<=0.02 and abs(steps[-2])<=0.02
          and abs(sum(steps[-3:]))<=0.03)
    # DeepSeek (CONV-021 independent return): stricter drift diagnostic,
    # amended in BEFORE any n=9 data existed; REPORTED, and a disagreement
    # with the primary test is itself a REMAINS-OPEN trigger (Patch 3148).
    strict = (len(seq)>=6 and abs(steps[-1])<=0.005 and abs(steps[-2])<=0.005)
    E1=seq[-1]
    print(f"E1 peak-convergence = {E1:.4f}; last steps {[f'{s:+.4f}' for s in steps[-3:]]}")
    print(f"   primary test (<=0.02): {'PASS' if ok else 'FAIL'};  "
          f"strict test (<=0.005, DeepSeek): {'PASS' if strict else 'FAIL'}"
          f"{'   [DISAGREE -> REMAINS-OPEN trigger]' if ok != strict else ''}")
    # E2 Binder crossings between adjacent sizes n>=6
    ns=sorted([n for n in bdn if n>=6]); cross=[]
    for a,b in zip(ns,ns[1:]):
        d=np.array(bdn[a][0]); ua=np.array(bdn[a][1]); ub=np.array(bdn[b][1])
        f=ua-ub
        for i in range(len(d)-1):
            if f[i]*f[i+1]<0:
                cross.append(float(d[i]+f[i]*(d[i+1]-d[i])/(f[i]-f[i+1]))); break
    print(f"E2 Binder crossings {['%.4f'%c for c in cross]}")
    E2=float(np.mean(cross[-2:])) if len(cross)>=2 else (cross[-1] if cross else None)
    # E3 global data collapse over n>=6
    def collapse(exclude_anom):
      best=None
      for dc in np.arange(1.8,3.4,0.005):
        for nu in np.arange(0.4,3.01,0.02):
            pts=[]
            for n in [x for x in fbn if x>=6]:
                ds,v=fbn[n]
                for d,val in zip(ds,v):
                    if exclude_anom and 1.7 <= d <= 2.3: continue
                    pts.append(((d-dc)*n**(1.0/nu), val))
            pts.sort()
            x=np.array([p[0] for p in pts]); y=np.array([p[1] for p in pts])
            m=(x>-8)&(x<8)
            if m.sum()<10: continue
            r=float(np.mean(np.abs(np.diff(y[m]))))     # collapse roughness
            if best is None or r<best[0]: best=(r,float(dc),float(nu))
      return best
    b_all = collapse(False); b_ex = collapse(True)
    E3 = b_all[1] if b_all else None
    E3x = b_ex[1] if b_ex else None
    print(f"E3 collapse d_c = {E3} (nu = {b_all[2] if b_all else None});  "
          f"excluding the d_s=2.0 region (DeepSeek/Copilot): {E3x} "
          f"(nu = {b_ex[2] if b_ex else None})")
    if E3 is not None and E3x is not None and abs(E3-E3x) > 0.05:
        print("   [collapse SHIFTS when the anomaly region is removed -> Q5 CONFOUNDING confirmed]")
    Es=[e for e in (E1,E2,E3) if e is not None]
    spread=max(Es)-min(Es); Dres=float(np.mean(Es))
    print(f"\nestimator spread = {spread:.4f}; D_res = {Dres:.4f}")
    print("=== VERDICT (frozen, adjudication S3) ===")
    if (not ok) or (ok != strict) or spread>0.10:
        print("REMAINS-OPEN -> back to panel with all three numbers")
    elif abs(Dres-2.450)<=0.182:
        print(f"|{Dres:.3f} - 2.450| = {abs(Dres-2.450):.3f} <= 0.182: CHALLENGE RESOLVES-CONFIRMING")
    else:
        print(f"|{Dres:.3f} - 2.450| = {abs(Dres-2.450):.3f} > 0.182: CHALLENGE STANDS-QUANTIFIED at {Dres:.3f}")
    print("[frozen 2.450 unrevised in every branch; calibration untouched]")

def cmd_analyze_fb():
    """Patch 3170 -- the 3166 prereg S4/S5 statistics and frozen readings."""
    st=json.load(open(STATE))
    FBGRID=[1.9,2.0,2.1,2.2,2.3]
    print("=== 3166 f_b n-scaling: loc(n), depth(n), var_fb(n), per seed ===")
    res={}
    for n in (7,8,9,10,11):
        per={}
        for sd in SEEDS:
            v=[st.get(f"{n}:{d}:{sd}") for d in FBGRID]
            if any(x is None for x in v): per[sd]=None; continue
            fb=[x["f_b"] for x in v]
            i=int(np.argmin(fb)); i=min(max(i,1),len(FBGRID)-2)
            x=np.array(FBGRID[i-1:i+2]); y=np.array(fb[i-1:i+2])
            A=np.vstack([x**2,x,np.ones(3)]).T
            a,b,c=np.linalg.solve(A,y)
            loc=float(-b/(2*a)) if a>0 else float(FBGRID[int(np.argmin(fb))])
            depth=float(a*loc*loc+b*loc+c) if a>0 else float(min(fb))
            var=st[f"{n}:{FBGRID[int(np.argmin(fb))]}:{sd}"]["m2"]
            per[sd]=(loc,depth,var)
        res[n]=per
        if all(per[sd] for sd in SEEDS):
            l=[per[sd][0] for sd in SEEDS]; d=[per[sd][1] for sd in SEEDS]; m=[per[sd][2] for sd in SEEDS]
            print(f"  n={n}: loc {np.mean(l):.4f} (seeds {l[0]:.4f}/{l[1]:.4f})  "
                  f"depth {np.mean(d):.4f} (Δseed {abs(d[0]-d[1]):.4f})  var_fb {np.mean(m):.3e}")
        else:
            print(f"  n={n}: INCOMPLETE (missing cells)")
    ns=[n for n in (7,8,9,10,11) if all(res[n][sd] for sd in SEEDS)]
    if len(ns)<5: print("\n[cells missing -- run fb first]"); return
    locs=[np.mean([res[n][sd][0] for sd in SEEDS]) for n in ns]
    deps=[np.mean([res[n][sd][1] for sd in SEEDS]) for n in ns]
    def steps(a): return [a[i+1]-a[i] for i in range(len(a)-1)]
    sl,sd_=steps(locs),steps(deps)
    print(f"\n  loc steps:   {['%+.4f'%x for x in sl]}")
    print(f"  depth steps: {['%+.4f'%x for x in sd_]}")
    # UNDERPOWERED gate (S4): seed diff > 20% of size-to-size change
    under=[]
    for name,arr,stp in (("loc",locs,sl),("depth",deps,sd_)):
        sdiff=np.mean([abs(res[n][5][0 if name=="loc" else 1]-res[n][11][0 if name=="loc" else 1]) for n in ns])
        sig=np.mean(np.abs(stp))
        if sig>0 and sdiff>0.2*sig: under.append(name)
        print(f"  {name}: mean seed diff {sdiff:.4f} vs mean step {sig:.4f} "
              f"{'-> UNDERPOWERED' if name in under else '-> adequate'}")
    def stab(stp): return abs(stp[-1])<=0.2*abs(stp[-2]) and stp[-1]*stp[-2]>=0 if abs(stp[-2])>0 else abs(stp[-1])<1e-9
    def drift(stp): return all(x*stp[0]>0 for x in stp) and abs(stp[-1])>=abs(stp[-2])
    print("\n=== VERDICT (3166 S5 frozen words) ===")
    if under:
        print(f"UNDETERMINED-PERSISTS ({'/'.join(under)} UNDERPOWERED)")
    else:
        L_stab,D_stab=stab(sl),stab(sd_)
        L_dr,D_dr=drift(sl),drift(sd_)
        if L_stab and D_stab: print("PHYSICAL-FEATURE (both quantities approach stable limits)")
        elif L_dr or D_dr:
            if L_stab or D_stab: print("UNDETERMINED-PERSISTS (the two quantities disagree)")
            else: print("FINITE-SIZE-EFFECT (systematic drift, non-decelerating)")
        else: print("UNDETERMINED-PERSISTS (neither frozen pattern matches cleanly)")
    print("[frozen d_s* = 2.450 untouched; calibration untouched; no Binder anywhere]")

if __name__=="__main__":
    if sys.argv[1]=="run": cmd_run(sys.argv[2])
    elif len(sys.argv)>2 and sys.argv[2]=="fb": cmd_analyze_fb()
    else: cmd_analyze()
