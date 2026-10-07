#!/usr/bin/env python3
"""Patch 4387 -- the founder's bookkeeping question: would it work if the distance between CPs were
always the same number of PSRs, and the number of Moments to cover that distance always the same?

Absolute frame: lattice coordinates (never change) and Moments (never change).  At a place where the
PSR is q*l_P (q = 1 - U to first order), three factors fully describe local physics:
  r = absolute length of a material ruler (relative to far away)
  v = absolute speed of a signal (lattice distance per Moment)
  c = clock rate (ticks per Moment); a tick = a signal crossing a ruler, so c = v / r.
GR's weak field (redshift, light bending, Shapiro, local light speed constant) needs
  r = 1 - U,  v = 1 - 2U,  c = 1 - U.
"""
import sympy as sp
U, n = sp.symbols('U n', positive=True)
q = 1 - U
def report(label, r, v):
    c = sp.simplify(v/r)
    lin = lambda e: sp.series(e, U, 0, 2).removeO()
    print(f"{label}\n   ruler {lin(r)}, signal speed {lin(v)}, clock rate {lin(c)}")
    ok = [sp.simplify(lin(r) - (1-U)) == 0, sp.simplify(lin(v) - (1-2*U)) == 0, sp.simplify(lin(c) - (1-U)) == 0]
    print(f"   ruler shrink OK: {ok[0]}   light bending/Shapiro OK: {ok[1]}   redshift OK: {ok[2]}")
print("GR needs: ruler 1 - U, signal 1 - 2U, clock 1 - U\n")
report("(A) the founder's question as worded: ruler = n PSRs; same Moments to cross it (1 PSR per Moment)",
       q, q)
print("   -> a clock near the Sun ticks at the far-away rate in Moments: no gravitational redshift;")
print("      g00 = -1, so in metric terms slow bodies feel no Newtonian pull.  (Local light speed v/(r c) = 1: passes.)")
print("      GPS: gravitational clock gain ~ +45.7 microseconds/day would be absent.\n")
report("(B) ruler = n PSRs; each PSR hop takes 1/q Moments (signal advances q PSRs per Moment)",
       q, q*q)
print("   -> passes at first order; the same number of the CP's OWN steps (local ticks), not universal Moments.")
print("      1/q Moments per hop is not a whole number: a duty cycle, about a fraction U of Moments with no hop.\n")
report("(C) 3386's reading: signal one PSR per Moment with the PSR's absolute size q^2;"
       "\n    ruler a fixed number of proper units (absolute q), i.e. 1/q PSRs", q, q*q)
print("   -> the same FIRST-ORDER metric as (B) (second order not checked here).\n")
report("(D) 4386's absolute rulers, signal 1 PSR per Moment", sp.Integer(1), q)
print("   -> gamma = 0 (half bending), as 4386 found.\n")
print("Metric for (B)/(C): g00 = -q^2, g_ij = q^-2 delta  (the one-PSR class of 4384-4385).")
