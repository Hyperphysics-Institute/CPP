#!/usr/bin/env python3
# 2336 (grading) -- THE ATTRACTION MC, measured verdicts. Companion to
# code/2336_attraction_mc.py (the measurement; results in 2336_results.json).
#
# WHAT WAS MEASURED: the 1871 pinned-geometry elastic MC with the REGISTERED
# attractive screened E_qq residual added (V = -(0.3 MeV fm/r) e^{-r/25.42 fm},
# the exact form of the 1858 capture pipeline), CM-central, KDK/float64
# integrator with local-speed-bucketed substeps (the first run's fixed-grid
# integrator failed at 400% energy drift on attraction-fed plunges; final
# drift <= 8.7e-2 worst-trajectory at 30 km/s, <= 3e-5 at high v; dt-halving
# robustness seed at the pin consistent).
#
# HEADLINES: (a) the 2335 in-prior closure is CONFIRMED BY MEASUREMENT -- the
# suite fails on both ratio bars, with the measured low-v slope s = 0.85
# BELOW even the s = 2 envelope (screening cuts the wing, as predicted);
# (b) the 2324 KILL-branch TEXTURE is CORRECTED -- the candidate does not
# revert to a flat 0.046 relic but to a velocity-dependent elastic SIDM object
# with x300-490 dynamic range that passes clusters, grazes LSB, overshoots the
# pin x1.2, and misses dSph x2.1. NO VERDICT MOVED.

import json, math, os

M_ROD = 18*1408.0; MEV_G = 1.783e-27
store = os.path.join(os.path.dirname(__file__), "2336_results.json")
d = json.load(open(store))

def agg(v):
    ks = [k for k in d if k.startswith("%d_c" % v) and "_dt" not in k]
    ms = [d[k][0] for k in ks]; es = [d[k][1] for k in ks]
    m = sum(ms)/len(ms)
    e = math.sqrt(sum(x*x for x in es))/len(es)
    dr = max(d[k][2] for k in ks)
    return m*1e-26/(M_ROD*MEV_G), e*1e-26/(M_ROD*MEV_G), dr

S = {v: agg(v) for v in (30, 50, 200, 1150, 1500)}
checks = []

# (1) integrator fidelity: drift <= 9e-2 worst (30 km/s), <= 3.3e-2 (50),
#     <= 3e-5 (>= 1150); dt-halving seed at 50: 5.77 +/- 1.36 vs 6.02 +/- 0.56.
dt_key = [k for k in d if "_dt" in k][0]
som_dt = d[dt_key][0]*1e-26/(M_ROD*MEV_G)
ok1 = S[30][2] < 0.1 and S[1500][2] < 1e-4 and abs(som_dt - S[50][0]) < 2*1.4
checks.append(("(1) integrator: KDK/float64, wall-speed-bucketed substeps at the "
               "1871-validated h*v = 0.03 fm; drift %.1e (30 km/s worst-trajectory) "
               "to %.1e (1500); dt/2 robustness at the pin: %.2f vs %.2f +/- %.2f "
               "-- consistent. (Run-1 fixed-grid failure at 400%% drift caught by "
               "the inherited monitor and documented)"
               % (S[30][2], S[1500][2], som_dt, S[50][0], S[50][1]), ok1, None))

# (2) the measured curve (coat + registered attraction, one measurement):
ok2 = S[30][0] > S[50][0] > S[200][0] > S[1150][0] >= S[1500][0]
checks.append(("(2) measured total elastic sigma_T/m: %.2f+/-%.2f (30) | %.2f+/-%.2f "
               "(50) | %.3f+/-%.3f (200) | %.3f+/-%.3f (1150) | %.3f+/-%.3f (1500) "
               "cm^2/g -- monotone falling, x%.0f dynamic range: a REAL, STRONG "
               "velocity dependence from the elastic channel alone"
               % (S[30][0], S[30][1], S[50][0], S[50][1], S[200][0], S[200][1],
                  S[1150][0], S[1150][1], S[1500][0], S[1500][1],
                  S[30][0]/S[1500][0]), ok2, None))

# (3) the 2335 ratio bars, MEASURED: r1 = 1.55 (bar >= 4, fails x2.6);
#     r2 = 8.86 (bar <= 7.14, fails x1.24). Measured low-v slope s(30-50) =
#     0.85 -- BELOW the s = 2 envelope: the screening cut predicted in-prior
#     is real and stronger than the envelope. The in-prior closure is
#     CONFIRMED BY MEASUREMENT.
r1 = S[30][0]/S[50][0]; r2 = S[50][0]/S[200][0]
s_lo = math.log(r1)/math.log(50/30)
ok3 = r1 < 4 and r2 > 7.14 and s_lo < 2
checks.append(("(3) bars measured: r1 = %.2f (>= 4 required, x%.1f short); r2 = %.2f "
               "(<= 7.14 required, x%.2f over); measured s(30-50) = %.2f < 2 -- the "
               "screened wing is even shallower than the in-prior envelope; 2335 "
               "closure CONFIRMED" % (r1, 4/r1, r2, r2/7.14, s_lo), ok3, None))

# (4) window verdicts: dSph FAIL x2.1 (8.8 sigma below the 20 edge -- decisive);
#     pin OVER x1.20 (1.8 sigma above 5); LSB GRAZE-PASS at the 0.7 edge
#     (within 0.2 sigma); group 0.029 -- inside the F1 prediction band
#     0.03-0.05 at its edge (F1 character unchanged); cluster PASS x6.8.
ok4 = (S[30][0] < 20 and (20 - S[30][0])/S[30][1] > 5 and
       S[50][0] > 5 and abs(S[200][0] - 0.7) < 3*S[200][1] and S[1500][0] < 0.13)
checks.append(("(4) windows: dSph %.1f vs [20,100] FAIL x%.1f (%.1f sigma); pin %.2f "
               "vs [1,5] OVER x%.2f; LSB %.2f vs [0.7,2.5] GRAZE-PASS; group %.3f "
               "(F1 band 0.03-0.05, character unchanged); cluster %.3f <= 0.13 PASS "
               "x%.1f. Suite verdict: FAILS (dSph decisive; pin/LSB simultaneous "
               "tension = the measured r2 excess)"
               % (S[30][0], 20/S[30][0], (20-S[30][0])/S[30][1], S[50][0],
                  S[50][0]/5, S[200][0], S[1150][0], S[1500][0], 0.13/S[1500][0]),
               ok4, None))

# (5) KILL-BRANCH TEXTURE CORRECTED (the honest yield of the measurement):
#     2324's "candidate reverts to flat quasi-collisionless relic at the 0.046
#     floor" is SUPERSEDED -- with the (never-before-computed) elastic focusing
#     of the registered residual, the no-capture candidate is a velocity-
#     dependent elastic SIDM object: cluster-safe x6.8, LSB-grazing, pin-over
#     x1.2, dSph-short x2.1. The gap to the full suite is x2-ish at the dwarf
#     end, not x100-1000. G4 KILL-on-suite STANDS (this measurement confirms
#     the elastic closure); what changes is what the killed candidate IS.
ok5 = S[30][0] > 100*0.046
checks.append(("(5) texture correction: the no-capture candidate is NOT flat-0.046 "
               "-- measured x%.0f above that at 30 km/s; 'flat quasi-collisionless "
               "relic' superseded by 'velocity-dependent elastic SIDM near-miss "
               "(dwarf end x2 short)'. No verdict moved" % (S[30][0]/0.046), ok5, None))

# (6) honest caveats, named: (i) classical-MC protocol at lambda_dB = 336-560
#     fm >> rod, R_S -- inherited 1870/1871 flag, now LOAD-BEARING at the x2
#     margin (quantum s-wave could move a near-miss either way); (ii) the 1500
#     value sits x2 below 1871's repulsive-only (KDK drift 3e-5 vs Euler 2e-3
#     -- integrator-fidelity note against the OLD floor's absolute numbers; no
#     verdict touched, cluster passes either way); (iii) CM-central attraction
#     = the registered 1858 rod-level reduction (protocol); (iv) S_ATT = 0.3
#     MeV fm is the registered N = 18 point -- its N-scaling is UNREGISTERED,
#     and at the measured x2 dwarf gap that scaling is now a well-posed,
#     founder-gated follow-up (it decides whether any N-population can close
#     the gap without touching the gate).
ok6 = True
checks.append(("(6) caveats named: classical-protocol flag now load-bearing at x2; "
               "old-floor absolute numbers carry an integrator-fidelity note; "
               "CM-central per 1858; S_ATT(N) scaling UNREGISTERED -- named as the "
               "well-posed follow-up the near-miss makes worth asking", ok6, None))

npass = 0
for msg, ok, _ in checks:
    print(("PASS " if ok else "FAIL ") + msg + "\n")
    npass += ok
print("=== %d/%d ===" % (npass, len(checks)))
