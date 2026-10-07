#!/usr/bin/env python3
"""Patch 4388 -- founder: absolute time (Moments) and space (GPs) are unaffected; clocks slow because
moving from A to B takes more Moments when the PSR is smaller ("PSR halves -> twice the Moments");
CP positions do not change if SSV_abs changes suddenly; "length and time vary together".

Bookkeeping as 4387: r = crystal's absolute size, v = signal speed (lattice distance per Moment),
c = clock rate = v/r (NOT the speed of light).  Solar-system tests need r = 1-U, v = 1-2U, c = 1-U (first order).
Here p = the PSR's LATTICE (absolute) size factor; in 3386's proper units row 4's PSR is 1 - U.  Settled (static) state near the Sun.
"""
import sympy as sp
U = sp.symbols('U', positive=True)
lin = lambda e: sp.expand(sp.series(e, U, 0, 2).removeO())
def row(label, r, v, p):
    c = v/r
    ok = (lin(r) == 1-U, lin(v) == 1-2*U, lin(c) == 1-U)
    print(f"{label}\n   PSR {lin(p)}, crystal {lin(r)}, signal {lin(v)}, clock {lin(c)}  "
          f"-> crystal shrink {ok[0]}, light bending/Shapiro {ok[1]}, redshift {ok[2]}")
print("The founder's example: PSR halves -> twice the Moments from A to B.\n")
row("1. crystal keeps its absolute size (his example, settled); one PSR per Moment", 1, 1-U, 1-U)
print("   clocks slow correctly; light slows only as much as clocks -> half the bending (gamma = 0)\n")
row("2. crystal shrinks with the PSR; one PSR per Moment", 1-U, 1-U, 1-U)
print("   the crystal is the same number of PSRs, crossed in the same Moments -> clocks do not slow\n")
row("3. crystal shrinks with the PSR; each PSR step takes 1/q Moments (4387 B)", 1-U, (1-U)**2, 1-U)
print("   passes; needs a reason for the longer step (3385's withdrawn knob unless the founder supplies it)\n")
row("4. PSR shrinks twice as fast as the crystal (3386's reading, 4387 C); one PSR per Moment", 1-U, (1-U)**2, (1-U)**2)
print("   passes; needs a reason the crystal settles at an in-between size")
print("   keeps his 'more Moments' mechanism literally: the PSR shrinks faster than A-B.  In proper units")
print("   (3386; clock ruling N = PSR_eff/l_P) the PSR is 1 - U and his 'PSR halves -> clocks halve' stands;")
print("   only in lattice units, extending the square-root form to finite size, would it be 1/sqrt2.\n")
print("5. crystal keeps its absolute size; light slows 2U; clocks slow as the square root (4386 (b))")
print(f"   PSR {lin(1-2*U)}, crystal 1, signal {lin(1-2*U)}, clock {lin(sp.sqrt(1-2*U))} (assumed, not v/r)")
print("   -> light bending/Shapiro True, redshift True, crystal shrink False; but the")
print("   locally measured light speed is lower near a mass: cavity-vs-atomic-clock swing ~3.3e-10/yr (bounds owed)\n")
print("His mechanism (more Moments to cross a FIXED absolute distance) is exactly the clock half.")
print("The other half of light bending needs the crystal to be smaller in the settled state; and if it")
print("shrinks with the PSR, the fixed-distance clock mechanism stops working unless 3 or 4 holds.")
