#!/usr/bin/env python3
"""3044_s2_threshold_selection.py — RES-SF4-STRUCT-1 sub-claim S2:
threshold shell selection under driven entrainment, tested across cost
models. MODEL-GRADE result (panel reviews); nothing asserted beyond
what the inequalities force.

MODEL INPUTS (two, stated openly):
  (I1) Selection rule: DRIVEN ENTRAINMENT — a spinner entrains the
       LARGEST shell it can hold mutually coherent (arcs entrain
       whatever they can phase-lock; enrollment is driven response,
       not energy minimization).
  (I2) Cost family: coherence cost of shell V = tau * f(V) with one
       UNIVERSAL substrate threshold tau (species-independent), f in
       {V, V^2, V(V-1)/2} — the three natural polynomial orders; the
       pairwise form V(V-1)/2 is motivated by SM-1's mutual-coherence
       requirement (one resource per pairwise phase relation).

COUPLINGS (ratified channel structure, AP-4a/AP-4b): eDP writes E only
-> C_e = 1 unit. qDP writes E and S (species by slot; S-weight k) ->
C_q = 1 + k. Pair (qDP+eDP), strict additivity baseline ->
C_pair = 2 + k. k = the AP-4b substrate constant; O-2 identification
candidate k* = 33 + 15*sqrt(5) ~ 66.5410 (founder-recalled ~67).

TARGET ASSIGNMENT (founder ruling 3041): eDP -> V=4 exactly (capped
below 12), qDP -> V=12 exactly (capped below 30), pair -> V=30.

CHECKS:
  V1 PAIRWISE model, eDP+qDP assignment: the tau-window
     max(1/66,(1+k)/435) < tau <= min(1/6,(1+k)/66) is NON-EMPTY at
     k = k*; window printed.
  V2 MODEL DISCRIMINATION: under f = V^2 and f = V the same joint
     assignment (eDP capped at 4 AND qDP capped at 12) admits NO
     tau at k = k* — the pairwise form is the unique survivor of the
     three, selected by consistency rather than chosen.
  V3 k-EXISTENCE BOUND (pairwise): the eDP/qDP assignment admits a
     tau iff 0 < k < 71.5 — an independent UPPER BOUND on the AP-4b
     constant from neutrino shell selection (cross-link to O-2);
     candidate k* = 66.54 sits INSIDE; the naive charged-lepton-like
     value 206.8 would sit OUTSIDE (printed).
  V4 PAIR under strict additivity: the full three-shell assignment
     requires tau in ((1+k)/435, (2+k)/435] — a non-empty but
     ~1.5%-wide sliver (printed): fine-tuned. A COOPERATIVE
     enhancement of the pair coupling by factor >= 435/(6(2+k)) ...
     precisely: any enhancement g with g*(2+k) >= 435*tau for tau up
     to 1/6 needs g >= 72.5/(2+k) ~ 1.058 — just ~6% — to widen the
     sliver to the full V1 window. The pair's route (S3) therefore
     needs only a WEAK cooperative effect (or the FACT-G4
     tetrad-position mode, which bypasses brute pairwise cost
     entirely); requirement quantified, not asserted.
"""
import numpy as np
K = 33 + 15*np.sqrt(5)

def window(f4, f12, f30, Ce, Cq):
    lo = max(Ce/f12, Cq/f30)          # eDP capped below 12; qDP below 30
    hi = min(Ce/f4, Cq/f12)           # eDP affords 4; qDP affords 12
    return lo, hi

def pairwise(V): return V*(V-1)/2
MODELS = [("pairwise V(V-1)/2", pairwise), ("V^2", lambda V: V*V),
          ("linear V", lambda V: float(V))]

results = {}
for name, f in MODELS:
    lo, hi = window(f(4), f(12), f(30), 1.0, 1.0+K)
    results[name] = (lo, hi, hi > lo)
    print(f"  model {name:18s}: tau-window ({lo:.5f}, {hi:.5f}] "
          f"{'NON-EMPTY' if hi>lo else 'EMPTY'}")

pw = results["pairwise V(V-1)/2"]
checks = [
 (f"V1 pairwise window non-empty at k* = {K:.4f}", pw[2]),
 ("V2 discrimination: V^2 and linear EMPTY (pairwise unique survivor)",
  (not results["V^2"][2]) and (not results["linear V"][2])),
]
kmax = 435/6 - 1
c207 = 206.768
checks.append((f"V3 k-existence bound: 0 < k < {kmax:.1f}; k* = {K:.2f} "
               f"INSIDE; charged-lepton-like {c207:.1f} OUTSIDE",
               0 < K < kmax and c207 > kmax))
lo3, hi3 = (1+K)/435, (2+K)/435
g_needed = (435/6)/(2+K)
checks.append((f"V4 pair additive sliver ({lo3:.5f}, {hi3:.5f}] non-empty "
               f"(width {100*(hi3-lo3)/lo3:.1f}%); cooperative factor to "
               f"widen to full window: g >= {g_needed:.3f} (~"
               f"{100*(g_needed-1):.0f}%)", hi3 > lo3 and g_needed < 1.10))
n = 0
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    n += ok
print(f"{n}/{len(checks)} PASS")
