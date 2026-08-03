#!/usr/bin/env python3
"""Patch 2968 — K-MEM-MEAS-1 frozen analysis (prereg 2967 §4/§5 verbatim).
Reads /tmp/kmem_{L1,L2,L3}_done.json, archives them to data/, applies the
frozen statistics and branch readings. No thresholds altered."""
import json, shutil
import numpy as np

legs = {}
for leg in ('L1', 'L2', 'L3'):
    shutil.copy(f"/tmp/kmem_{leg}_done.json", f"data/2968_kmem_{leg}.json")
    legs[leg] = json.load(open(f"data/2968_kmem_{leg}.json"))

# ---- control: noise floor and static offset (2967 §3 L2) ----------------
F2 = np.array(legs['L2']['F'])
w2 = F2[24:144]
sigma_ctrl = float(np.std(w2))
F_stat = float(np.mean(w2))
print(f"L2 control: sigma_ctrl={sigma_ctrl:.3e}, static offset F_stat={F_stat:+.3e}")

def movmean5(x):
    k = np.ones(5) / 5
    return np.convolve(x, k, mode='same')

def analyze(leg):
    L = legs[leg]
    F = np.array(L['F']); ts, Tb, te = L['t_step'], L['T_ball'], L['t_end']
    F0 = float(np.mean(F[ts-12:ts]))
    Wt = slice(ts + 4*Tb, min(ts + 6*Tb, te))
    Finf = float(np.mean(F[Wt]))
    S = abs(Finf - F0)
    thr = max(0.10 * S, 3 * sigma_ctrl)
    resid = np.abs(F - Finf)
    exceed = np.where(resid[ts+1:te] > thr)[0]
    t_settle = int(exceed[-1] + 1) if len(exceed) else 0
    r_tail = float(np.max(np.abs(movmean5(F)[Wt] - Finf)))
    return dict(F0=F0, Finf=Finf, S=S, thr=thr, t_settle=t_settle,
                r_tail=r_tail, Tb=Tb)

A = {leg: analyze(leg) for leg in ('L1', 'L3')}
for leg, a in A.items():
    print(f"{leg}: F0={a['F0']:+.3e} Finf={a['Finf']:+.3e} S={a['S']:.3e} "
          f"thr={a['thr']:.3e} t_settle={a['t_settle']} (T_ball={a['Tb']}) "
          f"r_tail={a['r_tail']:.3e}")

# ---- frozen branch reading (2967 §5) ------------------------------------
floor = {leg: A[leg]['S'] < 3 * sigma_ctrl for leg in A}
if any(floor.values()):
    print("READING: UNRESOLVED-BY-FLOOR in", [k for k, v in floor.items() if v])
else:
    mps = all(A[l]['t_settle'] <= 2.0 * A[l]['Tb'] and
              A[l]['r_tail'] <= A[l]['thr'] for l in A)
    ratio = A['L1']['t_settle'] / max(A['L3']['t_settle'], 1)
    scaling_ok = 0.9 <= ratio <= 2.7
    tail = all(A[l]['r_tail'] > 0.5 * A[l]['S'] for l in A)
    print(f"scaling ratio t_settle(L1)/t_settle(L3) = {ratio:.2f} "
          f"(band [0.9, 2.7]: {'IN' if scaling_ok else 'OUT'})")
    if mps and scaling_ok:
        print("READING: B-MPS — Markovian-plus-stiffness supported at toy grade")
    elif tail:
        print("READING: B-TAIL — FALSIFIER-CLASS: HALT, pre-action review")
    else:
        print("READING: B-INT — registered as-is, routed to CONV-011")
