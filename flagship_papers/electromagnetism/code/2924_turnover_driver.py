#!/usr/bin/env python3
"""PATCH 2924 -- TURNOVER TEST batch driver (frozen at 2923). Paired
mobile/frozen 2907-class legs: beta {0.25 (T=50), 0.30 (T=33)} x
classes {A,B} x seeds {4,5,6} = 12 pairs = 24 engine runs. Resumable
(2907 checkpoints + results-file skip). Usage: 2924_turnover_driver.py [budget_s]"""
import sys, os, json, time
import importlib.util
_here = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location("r3", os.path.join(_here, "2907_round3_driver.py"))
r3 = importlib.util.module_from_spec(sp); sp.loader.exec_module(r3)

WIN = {0.25: 50, 0.30: 33}
RUNS = [(cls, seed, b, mob) for b in (0.25, 0.30) for cls in ("A","B")
        for seed in (4,5,6) for mob in (1,0)]

def done():
    db = json.load(open("/tmp/2903_results.json")) if os.path.exists("/tmp/2903_results.json") else []
    return {(e["cls"], e["seed"], round(e["beta"],4), e["mobile"]) for e in db if e.get("tag")=="TO"}

def main(budget=170.0):
    t0 = time.time(); ds = done()
    todo = [r for r in RUNS if (r[0], r[1], round(r[2],4), r[3]) not in ds]
    print(f"runs done={len(RUNS)-len(todo)}/24  todo={len(todo)}")
    for cls, seed, b, mob in todo:
        if time.time()-t0 > budget:
            print("BUDGET reached -- resume with same command"); return 1
        r3.leg("TO", cls, seed, b, WIN[b], mob)
        if (cls, seed, round(b,4), mob) not in done():
            print("   (checkpointed mid-leg; resume)"); return 1
    print("ALL 24 RUNS COMPLETE"); return 0

if __name__ == "__main__":
    sys.exit(main(float(sys.argv[1]) if len(sys.argv)>1 else 170.0))
