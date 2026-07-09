#!/usr/bin/env python3
"""Patch 2368 -- executing R2's (Grok's) named V1 check: solver validity at N=2.
PRE-STATED pass criteria: (a) XQC total at the weak corner varies < 5% and the
violated-bin count is UNCHANGED under {h halved twice, rmax +33%, lmax doubled};
(b) Born vs partial-wave agreement < 1% at weak coupling E_RN*1e-3 (1879's own
validation method) at the dimer parameters. Also dumps per-bin predictions at
the weak corner (fact-check of R5's '~100 events in the low bins' claim)."""
import math, sys, json, io, contextlib
src = open('code/1879_xqc_recomputation.py').read().split("if __name__")[0]

def fresh(h=None, rmax=None, lmax_boost=0):
    g = {}; exec(src, g)
    g['N_ROD']=2; g['M_ROD']=2*g['M_EL']; g['L_ROD']=1.15
    if h or rmax or lmax_boost:
        orig = g['phase_shifts']
        def ps(V, mu, k, lmax, rmax_=180.0, h_=0.08):
            return orig(V, mu, k, lmax+lmax_boost, rmax or rmax_, h or h_)
        g['phase_shifts'] = ps
    return g

def weak_corner(g):
    g['E_RN'] = (3.0*g['E_C']/16)*0.012
    g['NDM']  = (0.94*0.2e3/g['M_ROD'])*2.5e10
    with contextlib.redirect_stdout(io.StringIO()):
        counts, sat = g['predicted_bins'](1, True)   # repulsive weak corner
    viol = sum(1 for (lo,hi,obs,f),p in zip(g['BINS'],counts) if p > obs+5*math.sqrt(obs+1))
    return counts, sat, sum(counts)+sat, viol

out = {}
base_counts, sat, base_tot, base_viol = weak_corner(fresh())
out['baseline'] = {"total": base_tot, "violated": base_viol,
  "per_bin": [{"bin_eV": f"{lo}-{hi}", "pred": round(p,1), "obs": obs}
              for (lo,hi,obs,f),p in zip(fresh()['BINS'], base_counts)]}
print(f"baseline (rep, Sc=0.012, f=0.94, rho=0.2): total={base_tot:.0f} viol={base_viol}")
for lo_hi in out['baseline']['per_bin'][:4]: print("  ", lo_hi)

for tag, kw in [("h=0.04", dict(h=0.04)), ("h=0.02", dict(h=0.02)),
                ("rmax=240", dict(rmax=240)), ("lmax+12", dict(lmax_boost=12))]:
    _,_,tot,viol = weak_corner(fresh(**kw))
    dev = abs(tot-base_tot)/base_tot
    out[tag] = {"total": tot, "violated": viol, "dev_frac": dev}
    print(f"{tag:10s} total={tot:8.0f} viol={viol}  dev={dev*100:.2f}%")

# Born check at weak coupling, dimer parameters, Si target
g = fresh(); HB=g['HBARC']
mA = 28.09*g['AMU']; M=g['M_ROD']; mu = M*mA/(M+mA)
k = mu*(300.0/g['CKMS'])/HB
Vf = g['make_V'](28.09, -1)
eps = 1e-3 * 0.012
Vw = lambda r: eps*Vf(r)
d = g['phase_shifts'](Vw, mu, k, 14)
sig_pw = 0.0
for l,dd in enumerate(d): sig_pw += 4*math.pi/(k*k)*(2*l+1)*math.sin(dd)**2
# Born: f(0-ish) integral -- sigma_Born = (2mu/HB^2)^2 * |int V r^2 j0(qr)... use total via partial-wave Born phases
import numpy as np
rs = np.arange(1,60000)*0.01
Vg = np.array([Vw(r) for r in rs])
sig_born = 0.0
from scipy.special import spherical_jn
for l in range(15):
    jl = spherical_jn(l, k*rs)
    dB = -(2*mu/HB**2)*k*np.trapezoid(Vg*(rs*jl)**2, rs)
    sig_born += 4*math.pi/(k*k)*(2*l+1)*math.sin(dB)**2
agree = abs(sig_pw-sig_born)/sig_born
out['born_check'] = {"sigma_pw_fm2": sig_pw, "sigma_born_fm2": sig_born, "agreement_frac": agree}
print(f"Born check: PW={sig_pw:.4e} Born={sig_born:.4e} fm^2  dev={agree*100:.3f}%")
passA = all(out[t]["dev_frac"]<0.05 and out[t]["violated"]==base_viol for t in ("h=0.04","h=0.02","rmax=240","lmax+12"))
passB = agree < 0.01
out['PASS'] = {"a_convergence": passA, "b_born": passB}
print("PASS:", out['PASS'])
json.dump(out, open("code/2368_results.json","w"), indent=1)
