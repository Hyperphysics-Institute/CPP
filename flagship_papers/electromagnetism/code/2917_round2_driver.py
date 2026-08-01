#!/usr/bin/env python3
"""PATCH 2917 -- HYBRID PIPELINE ROUND 2 batch driver (frozen at 2914 s4, windows PINNED at 2916).
Grid: seeds {4..9} x classes {A,B} x beta {0.04,0.07,0.10,0.14,0.20},
matched windows {125,107,100,89,63}, T_eq = 40. Legs run via the UNCHANGED
2914 leg() instrumentation; this driver only batches them in ONE process
(numba JIT paid once) with wall-clock guard + resume (skips legs already
in /tmp/2914_fields.json). Usage: python3 2917_round2_driver.py [budget_s]
"""
import sys, os, json, time
import importlib.util
_here = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location("rf", os.path.join(_here, "2914_response_field.py"))
rf = importlib.util.module_from_spec(sp); sp.loader.exec_module(rf)

WIN = {0.04: 125, 0.07: 107, 0.10: 100, 0.14: 89, 0.20: 63}   # pinned Patch 2916
GRID = [(cls, seed, b) for b in (0.04, 0.07, 0.10, 0.14, 0.20)
        for cls in ("A", "B") for seed in range(4, 10)]

def done_set():
    fn = "/tmp/2914_fields.json"
    if not os.path.exists(fn): return set()
    return {(e["cls"], e["seed"], round(e["beta"], 4)) for e in json.load(open(fn))}

def main(budget=270.0):
    t0 = time.time(); dset = done_set()
    todo = [(c, s, b) for (c, s, b) in GRID if (c, s, round(b, 4)) not in dset]
    print(f"legs done={len(GRID)-len(todo)}/60  todo={len(todo)}  budget={budget:.0f}s")
    for c, s, b in todo:
        if time.time() - t0 > budget:
            print(f"BUDGET reached at {time.time()-t0:.0f}s -- resume with same command")
            return 1
        rf.leg(c, s, b, WIN[b])
    print("ALL 60 LEGS COMPLETE")
    return 0

if __name__ == "__main__":
    sys.exit(main(float(sys.argv[1]) if len(sys.argv) > 1 else 270.0))
