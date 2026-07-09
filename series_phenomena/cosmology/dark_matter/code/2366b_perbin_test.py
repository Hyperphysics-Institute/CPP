#!/usr/bin/env python3
"""2366 follow-on (correction pre-stated): the B1 criterion in 2366_dimer_stage2
used the F5 REFLIGHT kill-high (314) -- a band for testing the rod's 46-event
prediction on a future flight -- NOT an exclusion criterion for a dimer
contribution to the already-observed 2007 spectrum. The registered conservative
exclusion criterion is 1879's own, PER-BIN: predicted > observed + 5*sqrt(obs+1)
=> EXCLUDED-class; all bins under observed => XQC-SAFE. Run that, per
pre-registered point, plus an S_c boundary scan at the weak corner."""
import math, sys, json, io, contextlib
src = open('code/1879_xqc_recomputation.py').read().split("if __name__")[0]
g = {}; exec(src, g)
g['N_ROD']=2; g['M_ROD']=2*g['M_EL']; g['L_ROD']=1.15
M=g['M_ROD']; BINS=g['BINS']; SAT=g['SAT']

def perbin(sign, sc, f_ab, rho_gev):
    g['E_RN'] = (3.0*g['E_C']/16)*sc
    g['NDM']  = (f_ab*rho_gev*1e3/M)*2.5e10
    with contextlib.redirect_stdout(io.StringIO()):
        counts, sat = g['predicted_bins'](-1 if sign=="attractive" else 1, True)
    g['E_RN'] = 3.0*g['E_C']/16
    viol = 0
    for (lo,hi,obs,f),p in zip(BINS,counts):
        if p > obs + 5*math.sqrt(obs+1): viol += 1
    sviol = sat > SAT[1] + 5*math.sqrt(SAT[1]+1)
    return viol, bool(sviol), sum(counts)+sat

pts = [(s,sc,f,r) for s in ("attractive","repulsive")
       for sc,f,r in [(0.05,0.99,0.6),(0.05,0.94,0.2),(0.035,0.99,0.6),
                      (0.035,0.94,0.2),(0.012,0.99,0.6),(0.012,0.94,0.2)]]
out={}
print(f"{'point':44s} viol-bins sat  total   verdict")
for s,sc,f,r in pts:
    v,sv,tot = perbin(s,sc,f,r)
    verdict = "EXCLUDED-class" if (v>0 or sv) else "XQC-SAFE"
    out[f"{s},Sc={sc},f={f},rho={r}"]={"violated_bins":v,"sat_violated":sv,"total":tot,"verdict":verdict}
    print(f"{s:11s} Sc={sc:<5} f={f} rho={r}   {v:2d}      {str(sv):5s} {tot:8.0f}  {verdict}")
# weak-corner boundary scan: where does EXCLUDED end along S_c (island floor 0.012)?
print("\nboundary scan (f=0.94, rho=0.2):")
for s in ("attractive","repulsive"):
    for sc in (0.012, 0.010, 0.008, 0.006):
        v,sv,tot = perbin(s,sc,0.94,0.2)
        tag = "island" if sc>=0.012 else "BELOW-island"
        print(f"  {s:11s} Sc={sc:<6} viol={v:2d} sat={str(sv):5s} total={tot:7.0f}  [{tag}]")
        out[f"scan,{s},Sc={sc}"]={"violated_bins":v,"sat_violated":sv,"total":tot}
json.dump(out, open("code/2366b_results.json","w"), indent=1)
