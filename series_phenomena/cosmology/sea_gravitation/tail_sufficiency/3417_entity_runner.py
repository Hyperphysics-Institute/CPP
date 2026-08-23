#!/usr/bin/env python3
"""Patch 3417 -- D-ENTITY-1 runner. Prereg D_ENTITY_1_prereg.md (3416),
frozen before any cluster datum existed.
Usage: python 3417_entity_runner.py run      (8 cells, ~20-30 min)
       python 3417_entity_runner.py analyze"""
import os
for v in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS","NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(v,"1")
import sys, json, importlib.util
import numpy as np
HERE=os.path.dirname(os.path.abspath(__file__))
SG=os.path.normpath(os.path.join(HERE,"..","scripts"))
sp=importlib.util.spec_from_file_location("m",os.path.join(SG,"3120_ds_indep_campaign.py"))
E=importlib.util.module_from_spec(sp); sp.loader.exec_module(E)
DS,N,T=4.636,5,1024; Nc=2*N**3
SIGS=(0.15,0.30,0.60,1.20); SEEDS=(5,11); RLAB=("1.2ds","1.5ds","2.0ds")
ST=os.path.join(HERE,"3417_entity_state.json")

def cmd_run():
    for sig in SIGS:
        for sd in SEEDS:
            st=json.load(open(ST)) if os.path.exists(ST) else {}
            k=f"{sig}:{sd}"
            if k in st: continue
            rng=np.random.default_rng(2000+sd)
            d=rng.normal(0,sig,(T,Nc,3))
            z=E.run(DS,N,sd,drive=d,cluster=True)
            st[k]={"f_b":z["f_b"],"clus":z["clus"]}
            json.dump(st,open(ST,"w"))
            print(f"  done {k}: N_clus={[round(c['N'],2) for c in z['clus']]}", flush=True)
    print("RUN COMPLETE. Now: analyze")

def cmd_analyze():
    st=json.load(open(ST))
    print("sigma   T        f_b      " + "  ".join(f"N({r})  <k>({r})" for r in RLAB))
    tab={}
    for sig in SIGS:
        fb=np.mean([st[f"{sig}:{s}"]["f_b"] for s in SEEDS])
        row=[]
        for ri in range(3):
            Nv=np.mean([st[f"{sig}:{s}"]["clus"][ri]["N"] for s in SEEDS])
            kv=np.mean([st[f"{sig}:{s}"]["clus"][ri]["k"] for s in SEEDS])
            row.append((Nv,kv))
        tab[sig]=row
        print(f" {sig:4.2f}  {sig*sig:7.4f}  {fb:.4f}   " +
              "  ".join(f"{n:7.2f} {k:6.2f}" for n,k in row))
    print("\nfrozen rule: sign of p must agree at ALL THREE thresholds")
    ps=[]
    for ri,r in enumerate(RLAB):
        y=np.array([tab[s][ri][0] for s in SIGS])
        if (y<=0).any(): print(f"  {r}: degenerate (zero clusters)"); ps.append(None); continue
        p=2*np.polyfit(np.log(SIGS),np.log(y),1)[0]; ps.append(p)
        print(f"  r_clus={r}: p = {p:+.4f}  -> w = {-1+p/3:+.4f}")
    good=[p for p in ps if p is not None]
    if len(good)<3: print("\nVERDICT: THRESHOLD-ARTEFACT (degenerate threshold) -- no reading")
    elif all(p>0 for p in good): print(f"\nVERDICT (frozen): QUINTESSENCE-SIDE  w = {-1+np.mean(good)/3:+.4f}")
    elif all(p<0 for p in good): print(f"\nVERDICT (frozen): PHANTOM-SIDE  w = {-1+np.mean(good)/3:+.4f}")
    else: print("\nVERDICT (frozen): THRESHOLD-ARTEFACT -- sign differs across thresholds, no reading")
    print("[no cosmological claim from this patch alone -- prereg S6]")

if __name__=="__main__":
    (cmd_run if sys.argv[1]=="run" else cmd_analyze)()
