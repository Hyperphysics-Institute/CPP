#!/usr/bin/env python3
"""PATCH 2903 -- DRESSED-DRIVE EXECUTION against the frozen bands of
sketches/mobile_sea_moving_source_prereg.md. Incremental JSON output.
Usage: python3 2903_dressed_execution.py <tag> <beta> [kw=val ...]"""
import sys, json, os, time, importlib.util
spec = importlib.util.spec_from_file_location(
    "eng", os.path.join(os.path.dirname(__file__), "2902_mobile_sea_engine.py"))
eng = importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)

OUT = "/tmp/2903_results.json"

def record(tag, beta, kw):
    t0 = time.time()
    D, sd, ab, pos, rel, drift = eng.run(beta, **kw)
    res = dict(tag=tag, beta=beta, D=D, sd=sd, ab=ab,
               wall=round(time.time() - t0, 1), kw=kw,
               drift_mean=float(drift.mean()),
               n_sea=len(drift))
    # entrainment profile: mean step_x binned by transverse distance
    import numpy as np
    rho = np.hypot(rel[:, 1], rel[:, 2])
    prof = []
    for lo, hi in [(0, 3), (3, 5), (5, 8), (8, 20)]:
        m = (rho >= lo) & (rho < hi)
        if m.sum():
            prof.append([lo, hi, float(drift[m].mean()), int(m.sum())])
    res["entrain_profile"] = prof
    db = json.load(open(OUT)) if os.path.exists(OUT) else []
    db.append(res); json.dump(db, open(OUT, "w"), indent=1)
    print(f"[{tag}] beta={beta}  D={D:+.6e}  sd={sd:.2e}  ab={ab:.3f}  "
          f"drift={res['drift_mean']:+.2e}  wall={res['wall']}s")

if __name__ == "__main__":
    tag = sys.argv[1]; beta = float(sys.argv[2])
    kw = {}
    for kv in sys.argv[3:]:
        k, v = kv.split("=")
        kw[k] = float(v) if "." in v else int(v)
    record(tag, beta, kw)
