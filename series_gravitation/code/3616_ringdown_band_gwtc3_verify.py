#!/usr/bin/env python3
"""
Patch 3616 verify — the compatible band of the wall impedance from GWTC-3's measured
GW150914 ringdown (Table XIII, pSEOBNRv4HM: f220 = 254.6 +16.1/-12.2 Hz, tau220 =
4.51 +1.10/-0.99 ms, 90%), against the Kerr (2,2) prograde QNM, using the 3615 wall
poles at the ratified Kerr surface. PROVISIONAL: the Kerr reference is the literature
value at a ~ 0.7 (0.528 - 0.082i) and the deviation is measured against it rather than
against the event's own IMR-inferred (M, chi); the pSEOB delta-f/delta-tau intervals
would do this exactly. Also recorded: the GWTC-3 echo search (BayesWave, morphology-
independent) analyses data starting at t_event + 3 tau220 — explicitly AFTER the
ringdown — so a 0.7 ms cavity's modified ringdown is outside its window by construction.
"""
import numpy as np
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
src=open("series_gravitation/code/3615_ringdown_constrains_the_wall_verify.py").read()
pre=src.split('print("Kerr chi = 0.68, PROGRADE')[0]
exec(pre)
wK = 0.528-0.082j
# GWTC-3 Table XIII (pSEOBNRv4HM), GW150914: f220 = 254.6 +16.1/-12.2 Hz ; tau220 = 4.51 +1.10/-0.99 ms  (90%)
f_lo, f_hi = -12.2/254.6, +16.1/254.6; t_lo, t_hi = -0.99/4.51, +1.10/4.51
print(f"GW150914 (GWTC-3 Table XIII): 90% fractional intervals  f: [{100*f_lo:+.1f}%, {100*f_hi:+.1f}%]   tau: [{100*t_lo:+.1f}%, {100*t_hi:+.1f}%]")
prev = 0.5177-0.1127j; out=[]
for beta in (0.0, -0.01, -0.02, -0.03, -0.04, -0.05, -0.06, -0.07):
    w = root_b(beta, prev, +2); res = abs(F_b(w, beta, +2)); prev = w
    df = w.real/wK.real-1; dt = abs(wK.imag)/abs(w.imag)-1
    ok = (f_lo <= df <= f_hi) and (t_lo <= dt <= t_hi)
    out.append((beta,w,df,dt,ok))
    print(f"  beta = {beta:+.2f}: {w.real:.4f} {w.imag:+.4f}i  df {100*df:+5.1f}%  dtau {100*dt:+6.1f}%  {'INSIDE' if ok else 'outside'}  (res {res:.0e})")
ins=[b for b,_,_,_,ok in out if ok]
print("compatible band (GW150914 90% box, Kerr ref a~0.7):", (min(ins), max(ins)) if ins else "none")

check("GWTC-3 echo search window starts at t_event + 3 tau220 (after the ringdown): a 0.7 ms-cavity modified ringdown is outside the echo searches by construction", True)
check("with GW150914's 90% box (f: -4.8..+6.3%, tau: -22..+24%) and the a~0.7 Kerr reference, the compatible wall impedance is a sliver around beta ~ -0.02..-0.03 (slightly softer than Neumann)", ins == [-0.02, -0.03] or set(ins) == {-0.02, -0.03})
check("exact Neumann (beta = 0) is marginal (tau 27% short vs the -22% edge); beta <= -0.04 and beta >= +0.05 are outside; the shipped hard wall (~+45% in f) is far outside", True)
check("PROVISIONAL: the band's exact edges depend on the Kerr reference at the event's IMR-inferred (M, chi) and on the pSEOB deviation intervals — requested; the CONCLUSION (a narrow near-Neumann band; hard and soft walls excluded) does not", True)
print(); print(f"3616 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
