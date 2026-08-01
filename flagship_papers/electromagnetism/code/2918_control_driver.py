#!/usr/bin/env python3
"""PATCH 2918 -- beta=0 CONTROL (frozen at 2917 record s6). Static source
at x = 0, seeds {4,5,6} x classes {A,B} x windows T_meas in {63, 125},
instrumentation UNCHANGED (2914 leg(), beta = 0 => x0 = 0, source
stationary by the primitive itself). Each completed leg is moved from
the shared /tmp/2914_fields.json into /tmp/2918_control.json with its
T_meas recorded, so the round-2 archive is never contaminated and the
two windows never collide. Resumable. Usage: python3 2918_control_driver.py [budget_s]
"""
import sys, os, json, time
import importlib.util
_here = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location("rf", os.path.join(_here, "2914_response_field.py"))
rf = importlib.util.module_from_spec(sp); sp.loader.exec_module(rf)

SHARED = "/tmp/2914_fields.json"
CTRL = "/tmp/2918_control.json"
GRID = [(cls, seed, T) for T in (63, 125) for cls in ("A", "B") for seed in (4, 5, 6)]

def load(fn):
    return json.load(open(fn)) if os.path.exists(fn) else []

def done_set():
    return {(e["cls"], e["seed"], e["T_meas"]) for e in load(CTRL)}

def main(budget=170.0):
    t0 = time.time(); dset = done_set()
    todo = [g for g in GRID if g not in dset]
    print(f"control legs done={len(GRID)-len(todo)}/12  todo={len(todo)}")
    for c, s, T in todo:
        if time.time() - t0 > budget:
            print(f"BUDGET reached -- resume with same command"); return 1
        n_before = len(load(SHARED))
        rf.leg(c, s, 0.0, T)
        db = load(SHARED)
        assert len(db) == n_before + 1
        e = db.pop()                      # remove beta=0 leg from round-2 file
        json.dump(db, open(SHARED, "w"))
        e["T_meas"] = T
        ctl = load(CTRL); ctl.append(e); json.dump(ctl, open(CTRL, "w"))
        print(f"   -> banked control {c}{s} T={T}")
    print("ALL 12 CONTROL LEGS COMPLETE")
    return 0

if __name__ == "__main__":
    sys.exit(main(float(sys.argv[1]) if len(sys.argv) > 1 else 170.0))
