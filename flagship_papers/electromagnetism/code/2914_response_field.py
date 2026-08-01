#!/usr/bin/env python3
"""PATCH 2914 -- Stage-1 instrumented legs: measure the Sea's response
field in co-moving bins. Usage: leg <cls> <seed> <beta> <T_meas>"""
import sys, os, json, time
import numpy as np
import importlib.util
_here = os.path.dirname(__file__)
def _load(name, fn):
    sp = importlib.util.spec_from_file_location(name, os.path.join(_here, fn))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
eng = _load("eng", "2902_mobile_sea_engine.py")
k6 = _load("k6", "2906_ensemble_driver.py")
r3 = _load("r3", "2907_round3_driver.py")

XB = np.arange(-12.0, 12.0 + 1e-9, 1.0)        # 24 xi bins
RB = [(1.0, 3.0), (3.0, 5.0), (5.0, 8.0)]

def leg(cls, seed, beta, T_meas):
    T_EQ = 40
    T_max = np.sqrt(52.0**2 + 16.0**2) + 5
    sea, qs = r3.build_sea_sym(cls, seed)
    Np = len(sea)//2
    x0 = -0.5*beta*(T_EQ+T_meas)
    pos = np.concatenate([[[x0, 0.0, 0.0]], sea])
    q = np.concatenate([[1.0], qs])
    hist = eng.History(pos, beta, int(np.ceil(T_max))+2, T_EQ+T_meas)
    tr = None
    cen0 = 0.5*(sea[:Np] + sea[Np:])
    rho = np.hypot(cen0[:,1], cen0[:,2])
    rhat = np.zeros((Np,3)); rhat[:,1] = cen0[:,1]/rho; rhat[:,2] = cen0[:,2]/rho
    prad0 = np.einsum('ij,ij->i', sea[:Np]-sea[Np:], rhat)   # baseline radial dipole
    nb = (len(XB)-1)*len(RB)
    S_px = np.zeros(nb); S_pr = np.zeros(nb); S_ux = np.zeros(nb); Nct = np.zeros(nb)
    S2_px = np.zeros(nb)
    for t in range(T_EQ+T_meas):
        pos, sn, sa, tr = k6.moment_step_fast(pos, q, hist, t, T_max, beta, True, tr)
        hist.append(pos)
        if t >= T_EQ:
            plus, minus = pos[1:1+Np], pos[1+Np:]
            cen = 0.5*(plus+minus)
            p = plus - minus
            px = p[:,0]
            pr = np.einsum('ij,ij->i', p, rhat) - prad0
            ux = cen[:,0] - cen0[:,0]
            xi = cen0[:,0] - pos[0,0]
            ib = np.digitize(xi, XB) - 1
            for ri,(rl,rh) in enumerate(RB):
                m = (rho>=rl)&(rho<rh)&(ib>=0)&(ib<len(XB)-1)
                idx = ib[m] + ri*(len(XB)-1)
                np.add.at(S_px, idx, px[m]); np.add.at(S2_px, idx, px[m]**2)
                np.add.at(S_pr, idx, pr[m]); np.add.at(S_ux, idx, ux[m])
                np.add.at(Nct, idx, 1.0)
    out = dict(cls=cls, seed=seed, beta=beta,
               S_px=list(S_px), S2_px=list(S2_px), S_pr=list(S_pr),
               S_ux=list(S_ux), N=list(Nct))
    fn = "/tmp/2914_fields.json"
    db = json.load(open(fn)) if os.path.exists(fn) else []
    db.append(out); json.dump(db, open(fn, "w"))
    print(f"[fld {cls}{seed} b={beta}] DONE  samples={int(Nct.sum())}")

if __name__ == "__main__":
    leg(sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]))
