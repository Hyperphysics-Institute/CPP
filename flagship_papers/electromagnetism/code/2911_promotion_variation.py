#!/usr/bin/env python3
"""PATCH 2911 -- promotion variation per the frozen section 4 of
sketches/mobile_sea_sign_round_record.md: rho_max 10.4, x_half 19.5,
all else unchanged. Usage: leg <cls> <seed> <beta> <T_meas> <mobile>"""
import sys, os, json, time, pickle
import numpy as np
import importlib.util
_here = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("eng", os.path.join(_here, "2902_mobile_sea_engine.py"))
eng = importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
spec2 = importlib.util.spec_from_file_location("k6", os.path.join(_here, "2906_ensemble_driver.py"))
k6 = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(k6)
spec3 = importlib.util.spec_from_file_location("r3", os.path.join(_here, "2907_round3_driver.py"))
r3 = importlib.util.module_from_spec(spec3); spec3.loader.exec_module(r3)

RHO_MAX, X_HALF, T_MAX = 10.4, 19.5, 75.0

def leg(cls, seed, beta, T_meas, mobile):
    T_EQ = 40
    CK = f"/tmp/ckv_{cls}_{seed}_{beta}.pkl"
    if os.path.exists(CK):
        st = pickle.load(open(CK, "rb"))
        pos, q, tr, t0m, Dx, AB = (st[k] for k in ("pos","q","tr","t","Dx","AB"))
        hist = eng.History(pos, beta, int(np.ceil(T_MAX))+2, T_EQ+T_meas)
        hist.H = st["H"]; hist.t_now = st["t_now"]
    else:
        sea, qs = r3.build_sea_sym(cls, seed, rho_max=RHO_MAX, x_half=X_HALF)
        x0 = -0.5*beta*(T_EQ+T_meas)
        pos = np.concatenate([[[x0, 0.0, 0.0]], sea])
        q = np.concatenate([[1.0], qs])
        hist = eng.History(pos, beta, int(np.ceil(T_MAX))+2, T_EQ+T_meas)
        tr, t0m, Dx, AB = None, 0, [], []
    t_start = time.time()
    for t in range(t0m, T_EQ+T_meas):
        pos, sn, sa, tr = k6.moment_step_fast(pos, q, hist, t, T_MAX, beta,
                                              bool(mobile), tr)
        hist.append(pos)
        if t >= T_EQ:
            Dx.append(sn[0]); AB.append(sa)
        if time.time()-t_start > 230 and t < T_EQ+T_meas-1:
            pickle.dump(dict(pos=pos, q=q, tr=tr, t=t+1, H=hist.H,
                             t_now=hist.t_now, Dx=Dx, AB=AB), open(CK,"wb"))
            print(f"[var {cls}{seed} b={beta}] ckpt {t+1}/{T_EQ+T_meas}")
            return
    D = float(np.mean(Dx)); sd = float(np.std(Dx))
    res = dict(tag="r3v", cls=cls, seed=seed, beta=beta, D=D, sd=sd,
               ab=float(np.mean(AB)), T_meas=T_meas, mobile=int(mobile))
    db = json.load(open("/tmp/2903_results.json"))
    db.append(res); json.dump(db, open("/tmp/2903_results.json","w"), indent=1)
    if os.path.exists(CK): os.remove(CK)
    print(f"[var {cls}{seed} b={beta} mob={mobile}] DONE D={D:+.6e} sd={sd:.2e}")

if __name__ == "__main__":
    leg(sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
