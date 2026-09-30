#!/usr/bin/env python3
"""4352 -- the 4330 volley re-run with the outward rule as the founder states it: a step is allowed only if its
DISPLACEMENT points outward, (g[t]-x).x > 0. 4330 line 44 tested the TARGET POSITION, g[t].x > 0, which lets bits
step back inward and fills a solid ball set by N. Usage: python3 4352_fsat_outward_rule_fixed.py FCC|GLASS
(slow: minutes per N). Results recorded in 4352_fsat_outward_rule_fixed.out."""
import sys, numpy as np
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib; m=importlib.import_module('4330_fsat_lattice_robustness')
def volley(g,nbr,origin,N,P,rng,fixed=True):
    site=np.full(N,origin); path=np.zeros(N); done=np.zeros(N,bool); occ=np.zeros(len(g),int); occ[origin]=N
    while not done.all():
        for i in rng.permutation(np.where(~done)[0]):
            s=site[i]; x=g[s]; cand=nbr[s]
            if s!=origin:
                out=cand[((g[cand]-x)@x)>0] if fixed else cand[(g[cand]@x)>0]
            else: out=cand
            if len(out)==0: out=cand
            free=out[occ[out]==0]; pick=free if len(free) else out
            t=pick[rng.integers(len(pick))]; occ[s]-=1; occ[t]+=1; path[i]+=np.linalg.norm(g[t]-g[s]); site[i]=t
            if path[i]>=P and occ[t]==1: done[i]=True
    r=np.linalg.norm(g[site],axis=1); lo,hi=np.percentile(r,10),np.percentile(r,90); gr=np.linalg.norm(g,axis=1)
    return ((r>=lo)&(r<=hi)).sum()/((gr>=lo)&(gr<=hi)).sum(), lo, hi
P=8.0
kind=sys.argv[1]
for N in [1500,3000,6000]:
    res=[]
    for seed in [1,2,3]:
        g,nbr,o=m.build(kind,P+3,100+seed)
        f0,lo,hi=volley(g,nbr,o,N,P,np.random.default_rng(seed)); f1,lo1,hi1=volley(g,nbr,o,N,0.9*P,np.random.default_rng(seed+10))
        res.append((f0,f1-f0)); print(f"{kind} N={N} seed={seed} fill={f0:.3f} band=[{lo:.2f},{hi:.2f}] well={f1:.3f} band=[{lo1:.2f},{hi1:.2f}]",flush=True)
    v=np.array(res); print(f"  SUMMARY {kind} N={N}: fill={v[:,0].mean():.3f}+-{v[:,0].std(ddof=1):.3f} change={v[:,1].mean():+.3f}+-{v[:,1].std(ddof=1):.3f}",flush=True)
