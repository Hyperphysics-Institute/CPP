#!/usr/bin/env python3
"""PATCH 2918 -- sign-convention audit: ONE isolated pair at x = -3 beside
a static +1 source. Naive induction predicts p_x < 0 there (+ member
pushed away). Verifies the engine's conventions so the ensemble's
reversed orientation can be attributed to collective physics, not code."""
import numpy as np, importlib.util, os
def load(name, fn):
    sp = importlib.util.spec_from_file_location(name, os.path.join(os.path.dirname(__file__), fn))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
eng = load("eng","2902_mobile_sea_engine.py"); k6 = load("k6","2906_ensemble_driver.py")
d0 = 0.4
pos = np.stack([[0.0,0.0,0.0], [-3.0, 1.0+d0/2, 0.0], [-3.0, 1.0-d0/2, 0.0]])
q = np.array([1.0, 1.0, -1.0])
hist = eng.History(pos, 0.0, 40, 30); tr=None
for t in range(30):
    pos, sn, sa, tr = k6.moment_step_fast(pos, q, hist, t, 38.0, 0.0, True, tr)
    hist.append(pos)
    if t%6==5:
        p = pos[1]-pos[2]
        print(f"t={t:2d}  p_x = {p[0]:+.5f}  (expect < 0 for normal induction)")
