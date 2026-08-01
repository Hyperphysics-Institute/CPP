#!/usr/bin/env python3
"""PATCH 2907 -- round-3 driver: symmetric classes + mirrored-jitter
ensemble, per sketches/mobile_sea_round3_prereg.md.
Usage: leg <tag> <class:A|B> <seed> <beta> <T_meas> <mobile:0|1>"""
import sys, os, json, time, pickle
import numpy as np
import importlib.util
_here = os.path.dirname(__file__)
spec = importlib.util.spec_from_file_location("eng", os.path.join(_here, "2902_mobile_sea_engine.py"))
eng = importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
spec2 = importlib.util.spec_from_file_location("k6", os.path.join(_here, "2906_ensemble_driver.py"))
k6 = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(k6)

D0, PSR = eng.D0, eng.PSR

def build_sea_sym(cls, seed, rho_min=1.0, rho_max=8.0, x_half=15.0, spacing=2.5):
    """Symmetric-class grid with mirror-symmetrised jittered separations."""
    off = 0.0 if cls == "A" else 1.25
    kx = int(np.floor((x_half - off) / spacing))
    xs = np.concatenate([-(off + spacing*np.arange(kx+1))[::-1],
                         (off + spacing*np.arange(kx+1))]) if off > 0 else \
         spacing*np.arange(-kx, kx+1)
    xs = np.unique(np.round(xs, 6))
    ky = int(np.floor(rho_max/spacing))
    ys = spacing*np.arange(-ky, ky+1)
    rng = np.random.default_rng(seed)
    jit = {}
    centres, orient, seps = [], [], []
    for x in xs:
        for y in ys:
            for z in ys:
                rho = np.hypot(y, z)
                if rho_min <= rho <= rho_max:
                    key = (round(abs(x), 6), round(y, 6), round(z, 6))
                    if key not in jit:
                        jit[key] = rng.uniform(-0.05, 0.05)
                    centres.append((x, y, z))
                    orient.append((0.0, y/rho, z/rho))
                    seps.append(D0 + jit[key])
    centres = np.array(centres); orient = np.array(orient)
    seps = np.array(seps)[:, None]
    plus = centres + 0.5*seps*orient
    minus = centres - 0.5*seps*orient
    pos = np.concatenate([plus, minus])
    q = np.concatenate([np.ones(len(plus)), -np.ones(len(plus))])
    return pos, q

def leg(tag, cls, seed, beta, T_meas, mobile):
    T_EQ = 40
    CK = f"/tmp/ck3_{tag}_{cls}_{seed}_{beta}.pkl"
    T_max = np.sqrt(52.0**2+16.0**2)+5
    if os.path.exists(CK):
        st = pickle.load(open(CK, "rb"))
        pos, q, tr, t0m, Dx, AB = (st[k] for k in ("pos","q","tr","t","Dx","AB"))
        hist = eng.History(pos, beta, int(np.ceil(T_max))+2, T_EQ+T_meas)
        hist.H = st["H"]; hist.t_now = st["t_now"]
    else:
        sea, qs = build_sea_sym(cls, seed)
        x0 = -0.5*beta*(T_EQ+T_meas)
        pos = np.concatenate([[[x0, 0.0, 0.0]], sea])
        q = np.concatenate([[1.0], qs])
        hist = eng.History(pos, beta, int(np.ceil(T_max))+2, T_EQ+T_meas)
        tr, t0m, Dx, AB = None, 0, [], []
    t_start = time.time()
    for t in range(t0m, T_EQ+T_meas):
        pos, sn, sa, tr = k6.moment_step_fast(pos, q, hist, t, T_max, beta,
                                              bool(mobile), tr)
        hist.append(pos)
        if t >= T_EQ:
            Dx.append(sn[0]); AB.append(sa)
        if time.time()-t_start > 235 and t < T_EQ+T_meas-1:
            pickle.dump(dict(pos=pos, q=q, tr=tr, t=t+1, H=hist.H,
                             t_now=hist.t_now, Dx=Dx, AB=AB), open(CK, "wb"))
            print(f"[{tag} {cls}{seed} b={beta}] ckpt {t+1}/{T_EQ+T_meas}")
            return
    Dx = np.array(Dx)
    D = float(Dx.mean()); sd = float(Dx.std())
    tt = np.arange(len(Dx)) - (len(Dx)-1)/2
    slope = float((tt*Dx).sum()/(tt*tt).sum())
    res = dict(tag=tag, cls=cls, seed=seed, beta=beta, D=D, sd=sd,
               ab=float(np.mean(AB)), trend=slope, T_meas=T_meas,
               mobile=int(mobile))
    db = json.load(open("/tmp/2903_results.json"))
    db.append(res); json.dump(db, open("/tmp/2903_results.json","w"), indent=1)
    if os.path.exists(CK): os.remove(CK)
    print(f"[{tag} {cls}{seed} b={beta} mob={mobile}] DONE D={D:+.6e} sd={sd:.2e} trend={slope:+.1e}")

if __name__ == "__main__":
    leg(sys.argv[2], sys.argv[3], int(sys.argv[4]), float(sys.argv[5]),
        int(sys.argv[6]), int(sys.argv[7]))
