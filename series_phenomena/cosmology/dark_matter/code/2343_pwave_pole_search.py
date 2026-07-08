#!/usr/bin/env python3
# 2343 -- L3-a EXECUTED: direct delta_1(E) pole search (the CONV-001 panel's
# unanimous priority; the self-disclosed soft spot of 2338 check 5).
#
# QUESTION: does the screened residual support a barrier-protected l = 1
# resonance -- a rising pi/2 crossing of delta_1(E) -- inside (or near) the
# SPEC-1 window E_cm in [63, 176] eV, anywhere in the OPEN-SS-43 band, narrow
# enough to deliver r1 >= 4 while holding LSB? Unlike the 2338 sigma-scan
# (all-l but S-grid-sampled), this scans ENERGY directly at fixed potential,
# so a narrow feature cannot hide between strength-grid points: at each
# (S, R_s) the full delta_1(E) curve is traced.
#
# Method: the validated 2338 Numerov engine (hard-sphere/Born exact), soft-coat
# core (the physically motivated variant), lmax = 1, E-grid 60 log points in
# [20, 600] eV per (S, R_s) point; rising-through-pi/2 (mod pi) detection;
# width Gamma = 2 (d delta_1/dE)^{-1} at each crossing; any in-window hit is
# graded against the suite by full sigma_T at the five velocities.

import numpy as np, json, os, sys, math

sys.path.insert(0, os.path.dirname(__file__))
_eng = {}
exec(open(os.path.join(os.path.dirname(__file__), "2338_quantum_engine.py")).read()
     .split('if __name__ == "__main__":')[0], _eng)
phase_shifts, sigma_T, kinematics = _eng['phase_shifts'], _eng['sigma_T'], _eng['kinematics']
MU, CONV, RS0, S0 = _eng['MU'], _eng['CONV'], _eng['RS0'], _eng['S0']

CORE = "yuk"
EV = 1e-6                      # MeV per eV
E_GRID = np.geomspace(20*EV, 600*EV, 60)

def delta1_curve(S, Rs, dr=0.04):
    return np.array([phase_shifts(E, S, Rs, CORE, 1, dr=dr)[1] for E in E_GRID])

def find_crossings(d1):
    """rising pi/2 crossings of delta_1 mod pi; returns list of (E_eV, Gamma_eV)."""
    out = []
    dm = np.mod(d1, math.pi)
    for i in range(len(E_GRID) - 1):
        a, b = dm[i], dm[i+1]
        if a < math.pi/2 <= b and (b - a) < 2.5:      # rising, no branch jump
            # linear interpolation for E_res; slope for width
            t = (math.pi/2 - a)/(b - a)
            Er = E_GRID[i]*(E_GRID[i+1]/E_GRID[i])**t
            slope = (b - a)/(E_GRID[i+1] - E_GRID[i])  # rad/MeV
            out.append((Er/EV, 2.0/slope/EV))
    return out

if __name__ == "__main__":
    store = os.path.join(os.path.dirname(__file__), "2343_results.json")
    d = json.load(open(store)) if os.path.exists(store) else {}
    if len(sys.argv) > 1 and sys.argv[1] == "scan":
        i = int(sys.argv[2])
        Ss = np.linspace(0.15, 0.60, 10)
        Rss = np.linspace(15.0, 30.0, 6)
        S = float(Ss[i])
        row = []
        for Rs in Rss:
            cr = find_crossings(delta1_curve(S, Rs))
            row.append([float(Rs), cr])
        d["scan_%02d" % i] = {"S": S, "rows": row}
        json.dump(d, open(store, "w"))
        hits = [(Rs, c) for Rs, cr in row for c in cr]
        inwin = [(Rs, c) for Rs, c in hits if 63 <= c[0] <= 176]
        print("S=%.3f: %d crossings total, %d in-window %s"
              % (S, len(hits), len(inwin),
                 [("Rs=%.1f E=%.0feV G=%.1feV" % (Rs, c[0], c[1])) for Rs, c in (inwin or hits)[:4]]))
    elif sys.argv[1] == "grade":
        # collect all crossings; grade any in-window hits against the suite
        allhits = []
        for k, v in d.items():
            if not k.startswith("scan_"):
                continue
            for Rs, cr in v["rows"]:
                for E_res, G in cr:
                    allhits.append((v["S"], Rs, E_res, G))
        inwin = [h for h in allhits if 63 <= h[2] <= 176]
        print("TOTAL delta_1 rising pi/2 crossings across the band, E in [20,600] eV: %d"
              % len(allhits))
        print("IN-WINDOW [63,176] eV: %d" % len(inwin))
        for S, Rs, Er, G in sorted(allhits, key=lambda h: h[2])[:10]:
            print("  S=%.3f Rs=%.1f: E_res=%.0f eV, Gamma=%.1f eV" % (S, Rs, Er, G))
        FL = {30: 0.11, 50: 0.09, 200: 0.05, 1500: 0.04}
        for S, Rs, Er, G in inwin:
            tot = {}
            for v in (30.0, 50.0, 200.0, 1500.0):
                E, k = kinematics(v)
                tot[int(v)] = sigma_T(E, S, Rs, CORE)*CONV + FL[int(v)]
            ok = (20 <= tot[30] <= 100 and 1 <= tot[50] <= 5
                  and 0.7 <= tot[200] <= 2.5 and tot[1500] <= 0.13)
            print("  IN-WINDOW hit S=%.3f Rs=%.1f E=%.0f G=%.1f -> suite %s: %s"
                  % (S, Rs, Er, G, "PASS" if ok else "FAIL",
                     {k2: round(x, 2) for k2, x in tot.items()}))
        d["grade"] = {"total": len(allhits), "in_window": len(inwin)}
        json.dump(d, open(store, "w"))
