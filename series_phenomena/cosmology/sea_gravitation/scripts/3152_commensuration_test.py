#!/usr/bin/env python
"""Patch 3152 -- THE COMMENSURATION TEST. Prediction FROZEN before the
run (anomaly_commensuration_prereg.md): if the d_s = 2.0 feature is an
artifact of the swap threshold (d_s/2) coinciding with the Coulomb
softening radius (r_soft = 1.0), then changing r_soft MOVES the feature
to d_s = 2*r_soft. If it is physics, it stays at 2.0.
Usage: python 3152_commensuration_test.py run
       python 3152_commensuration_test.py analyze
"""
import os
for _v in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS","NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v,"1")
import sys, json, importlib.util
from multiprocessing import Pool
import numpy as np

HERE=os.path.dirname(os.path.abspath(__file__))
STATE=os.path.join(HERE,"3152_state.json")
NSIDE=7; SEEDS=[5,11]
DS=[1.4,1.5,1.6,1.9,2.0,2.1,2.4,2.5,2.6]
RSOFT=[0.75,1.25]          # predicted feature locations: 1.5 and 2.5

def cell(a):
    ds,rs,sd=a
    s=importlib.util.spec_from_file_location("m",os.path.join(HERE,"3120_ds_indep_campaign.py"))
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return (f"{rs}:{ds}:{sd}", m.run(ds,NSIDE,sd,r_soft=rs))

def cmd_run():
    st=json.load(open(STATE)) if os.path.exists(STATE) else {}
    todo=[(ds,rs,sd) for rs in RSOFT for ds in DS for sd in SEEDS if f"{rs}:{ds}:{sd}" not in st]
    print(f"cells remaining: {len(todo)}; workers: {min(16,max(1,len(todo)))}")
    with Pool(min(16,max(1,len(todo)))) as p:
        for k,z in p.imap_unordered(cell,todo):
            st[k]=z; json.dump(st,open(STATE,"w"))
            print(f"  done {k}: f_b={z['f_b']:.4f} binder={z['binder']}")
    print("RUN COMPLETE. Now: analyze")

def cmd_analyze():
    st=json.load(open(STATE))
    print("FROZEN RULE: feature location tracks 2*r_soft within +/-0.15 => ARTIFACT;")
    print("             stays at 2.0 +/- 0.15 in BOTH variants => PHYSICS; else AMBIGUOUS -> panel\n")
    locs={}
    for rs in RSOFT:
        fb=[np.mean([st[f"{rs}:{d}:{s}"]["f_b"] for s in SEEDS]) for d in DS]
        bd=[np.mean([st[f"{rs}:{d}:{s}"]["binder"] for s in SEEDS]) for d in DS]
        i=int(np.argmin(fb)); j=int(np.argmax(np.abs(bd)))
        locs[rs]=(DS[i],DS[j])
        print(f"r_soft = {rs} (predicted feature at {2*rs}):")
        for d,f,b in zip(DS,fb,bd): print(f"   d_s={d:4.2f}  f_b={f:.4f}  U={b:+.4f}")
        print(f"   f_b minimum at {DS[i]};  |U| maximum at {DS[j]}\n")
    art=all(abs(locs[rs][0]-2*rs)<=0.15 for rs in RSOFT)
    phys=all(abs(locs[rs][0]-2.0)<=0.15 for rs in RSOFT)
    print("=== VERDICT (frozen words) ===")
    print("ARTIFACT-CONFIRMED (commensuration)" if art else
          "PHYSICS-CONFIRMED (feature is spacing-intrinsic)" if phys else
          "AMBIGUOUS -> panel")
if __name__=="__main__":
    (cmd_run if sys.argv[1]=="run" else cmd_analyze)()
