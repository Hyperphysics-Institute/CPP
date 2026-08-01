#!/usr/bin/env python3
"""PATCH 2904 -- checkpointed differential execution (amendment bands).
Usage: python3 2904_differential_driver.py <tag> <beta> <T_meas> <mobile:0|1>
Resumes from /tmp/ck_<tag>_<beta>.pkl if present; appends result to
/tmp/2903_results.json when the run completes."""
import sys, os, json, time, pickle, importlib.util
import numpy as np
spec = importlib.util.spec_from_file_location(
    "eng", os.path.join(os.path.dirname(__file__), "2902_mobile_sea_engine.py"))
eng = importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)

TAG, BETA, T_MEAS, MOBILE = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), bool(int(sys.argv[4]))
T_EQ = 40
CK = f"/tmp/ck_{TAG}_{BETA}.pkl"
BUDGET = 235.0

if os.path.exists(CK):
    st = pickle.load(open(CK, "rb"))
    pos, q, tr, t0m, Dx, AB, drift_sum = (st[k] for k in
        ("pos", "q", "tr", "t", "Dx", "AB", "drift"))
    T_max = np.sqrt(52.0 ** 2 + 16.0 ** 2) + 5
    hist = eng.History(pos, BETA, int(np.ceil(T_max)) + 2, T_EQ + T_MEAS)
    hist.H = st["H"]; hist.t_now = st["t_now"]
    print(f"[{TAG} b={BETA}] resume at Moment {t0m}")
else:
    sea, qs, _ = eng.build_sea()
    x0 = -0.5 * BETA * (T_EQ + T_MEAS)
    pos = np.concatenate([[[x0, 0.0, 0.0]], sea])
    q = np.concatenate([[1.0], qs])
    T_max = np.sqrt(52.0 ** 2 + 16.0 ** 2) + 5
    hist = eng.History(pos, BETA, int(np.ceil(T_max)) + 2, T_EQ + T_MEAS)
    tr, t0m, Dx, AB, drift_sum = None, 0, [], [], None

T_max = np.sqrt(52.0 ** 2 + 16.0 ** 2) + 5
t_start = time.time()
for t in range(t0m, T_EQ + T_MEAS):
    prev = pos.copy()
    pos, sn, sa, tr = eng.moment_step(pos, q, hist, t, T_max, BETA, MOBILE, tr)
    hist.append(pos)
    if t >= T_EQ:
        Dx.append(sn[0]); AB.append(sa)
        sx = pos[1:, 0] - prev[1:, 0]
        drift_sum = sx if drift_sum is None else drift_sum + sx
    if time.time() - t_start > BUDGET and t < T_EQ + T_MEAS - 1:
        pickle.dump(dict(pos=pos, q=q, tr=tr, t=t + 1, H=hist.H,
                         t_now=hist.t_now, Dx=Dx, AB=AB,
                         drift=drift_sum), open(CK, "wb"))
        print(f"[{TAG} b={BETA}] checkpoint at Moment {t+1}/{T_EQ+T_MEAS}")
        sys.exit(0)

D = float(np.mean(Dx)); sd = float(np.std(Dx)); ab = float(np.mean(AB))
drift = (drift_sum / max(len(Dx), 1)) if drift_sum is not None else np.zeros(1)
res = dict(tag=TAG, beta=BETA, D=D, sd=sd, ab=ab, T_meas=T_MEAS,
           mobile=int(MOBILE), drift_mean=float(np.mean(drift)))
db = json.load(open("/tmp/2903_results.json"))
db.append(res); json.dump(db, open("/tmp/2903_results.json", "w"), indent=1)
if os.path.exists(CK):
    os.remove(CK)
print(f"[{TAG} b={BETA} mobile={int(MOBILE)}] DONE  D={D:+.6e}  sd={sd:.2e}  ab={ab:.3f}")
