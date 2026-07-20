#!/usr/bin/env python3
"""
PATCH 2658 -- FORM-1 Agenda B HOLDOUT EXECUTION under form1_b_holdout_prereg.md
(2657). Instrument: the 2629 machinery VERBATIM via exec-load through its stage
dispatch (which itself exec-loads the registered 2602 engine through the 2609
cut). Extensions: width/dt values only. Stages: pin | h. One pass per cell.
Predictions read at 2656 S4 / 2657 S3; this script prints observables only.
"""
import numpy as np, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "2629_sink_obs1.py")).read()
cut = src.index("stage=sys.argv[1]")
ns = {'__file__': os.path.join(HERE, '2629_sink_obs1.py')}  # namespace binding for exec-load (2635 precedent)
exec(src[:cut], ns)
cell = ns['cell']; reads2 = ns['reads2']; classify = ns['classify']

def swa(v, w, dtf):
    r = cell(0.0, v, w, 0.5, dtf)
    sWA, sWB, dB, sc, dc = reads2(r)
    return sWA, sc, r['Edrift'], classify(r)

stage = sys.argv[1] if len(sys.argv) > 1 else 'pin'
t0 = time.time()
print("=" * 78)
print(f"PATCH 2658 -- FORM-1 Agenda B holdouts (prereg 2657; predictions 2656 S4)  stage={stage}")
print("=" * 78)

if stage == 'pin':
    print("[PIN] must reproduce the 2629 P1 printed row to the digit:")
    REF = {(2.0, 100): 149.86, (2.0, 200): 151.10, (2.0, 400): 151.72,
           (3.0, 100): 122.68, (3.0, 200): 149.74, (3.0, 400): 161.40,
           (4.0, 100): 228.35, (4.0, 200): 203.85, (4.0, 400): 182.72}
    ok = True
    for w in (2.0, 3.0, 4.0):
        for den in (100, 200, 400):
            S, sc, ed, cl = swa(0.10, w, 1.0 / den)
            match = (f"{S:.2f}" == f"{REF[(w, den)]:.2f}")
            ok = ok and match
            print(f"  w={w} dt=1/{den}: S_WA={S:.2f}  ref={REF[(w,den)]:.2f}  "
                  f"{'MATCH' if match else 'MISMATCH'}  ({cl})")
    print(f"  [PIN verdict-input] ALL-MATCH: {ok}")
    print(f"[{time.time()-t0:.0f}s]")

elif stage == 'h':
    print("[H2] w=4, dtf in {1/400,1/800} (the A/B discriminator):")
    S4 = {}
    for den in (400, 800):
        S, sc, ed, cl = swa(0.10, 4.0, 1.0 / den)
        S4[den] = S
        print(f"  w=4 dt=1/{den}: S_WA={S:.2f} (S_cum={sc:.1f}, Edrift={ed:.1f}, {cl})")
    fi = abs(S4[800] - S4[400]) / max(S4[800], 1e-9)
    print(f"  [H2 verdict-input] final-inc(1/400->1/800) = {fi:.4f}")
    print("[H3] w=2, dtf in {1/400,1/800}:")
    S2 = {}
    for den in (400, 800):
        S, sc, ed, cl = swa(0.10, 2.0, 1.0 / den)
        S2[den] = S
        print(f"  w=2 dt=1/{den}: S_WA={S:.2f} ({cl})")
    fi2 = abs(S2[800] - S2[400]) / max(S2[800], 1e-9)
    print(f"  [H3 verdict-input] final-inc(1/400->1/800) = {fi2:.4f}")
    print("[H1] w=2.5 QUARANTINED diagnostic, full ladder:")
    S25 = {}
    for den in (100, 200, 400):
        S, sc, ed, cl = swa(0.10, 2.5, 1.0 / den)
        S25[den] = S
        print(f"  w=2.5 dt=1/{den}: S_WA={S:.2f} ({cl})")
    fi25 = abs(S25[400] - S25[200]) / max(S25[400], 1e-9)
    print(f"  [H1 verdict-input] final-inc(1/200->1/400) = {fi25:.4f}")
    print(f"[{time.time()-t0:.0f}s]")

print("\nDone. Verdicts are read in form1_b_holdout_record.md against 2657/2656 S4.")
