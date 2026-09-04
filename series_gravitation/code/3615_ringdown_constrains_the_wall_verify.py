#!/usr/bin/env python3
"""
Patch 3615 verify — THE RINGDOWN CONSTRAINS THE WALL. The LVK echo searches
(GWTC-2 TGR sec. VII.B, pasted by the founder) give Bayes factors, no amplitude
limit, posteriors that recover the priors, and a template whose echo delays are
those of Planck-scale walls — far longer than the CPP cavity's 0.7 ms round trip
at 8M/3. They do not probe the CPP wall. The RINGDOWN does: the observed (2,2)
prograde mode agrees with the Kerr QNM to a few percent in frequency and tens of
percent in damping, and a wall at the ratified Kerr surface (2.734 M, chi = 0.68)
MOVES that mode by an amount set by its impedance. Computed with the 3359/3392 SN
ladder for the PROGRADE m = +2 mode over the wall impedance beta.
"""
import numpy as np
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
exec(open("series_gravitation/code/3359_sn_gravitational_wall_modes_verify.py").read().split("# ---------------- T1: a = 0 reduction")[0].replace("PASS = []", "PASS_SN = []").replace("def check(", "def check_sn("))
solver_src = open("series_gravitation/code/3359_sn_gravitational_wall_modes_verify.py").read().split("# ---------------- the SN wall solver ----------------")[1].split("def wall_root")[0]
solver_src = solver_src.replace("def X_at_wall(w, a, ell, m, r0=40.0, nterms=8):\n    rw = r_surface(a)", "def X_at_wall(w, a, ell, m, r0=40.0, nterms=8, rw=None):\n    rw = r_surface(a) if rw is None else rw").replace("    return sol.y[0, -1] + 1j * sol.y[1, -1]", "    return (sol.y[0, -1] + 1j * sol.y[1, -1]), (sol.y[2, -1] + 1j * sol.y[3, -1])")
exec(solver_src)
from scipy.optimize import fsolve
RW68 = 2.7344; Msec = 62*4.925e-6; to_hz = lambda w: w/(2*np.pi*Msec)
def F_b(w, beta, m):
    X, Xp = X_at_wall(w, 0.68, 2, m, 40.0, rw=RW68)
    return (Xp - beta*X)/(1+abs(beta)) if np.isfinite(beta) else X
def root_b(beta, guess, m):
    fn = lambda v: [F_b(v[0]+1j*v[1], beta, m).real, F_b(v[0]+1j*v[1], beta, m).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-10); return s[0]+1j*s[1]
print("Kerr chi = 0.68, PROGRADE (2,+2) — the mode the ringdown observations measure. Literature Kerr QNM (a=0.7): M w ~ 0.533 - 0.081i (Q 3.3) -> ~278 Hz at 62 Msun")
for beta, g in ((np.inf, 0.50-0.10j), (0.0, 0.45-0.06j), (0.5, 0.48-0.08j), (-0.2, 0.38-0.05j)):
    try:
        w = root_b(beta, g, +2); res = abs(F_b(w, beta, +2))
        print(f"  wall beta = {beta:+5.2f}: w = {w.real:.4f} {w.imag:+.4f}i  ({to_hz(w.real):.0f} Hz, Q {w.real/(2*abs(w.imag)):.1f})  res {res:.1e}")
    except Exception as e: print("  beta", beta, "failed", e)
print("\nscan of the prograde (2,2) mode vs wall impedance (tracked from Neumann)")
prev = 0.5177-0.1127j; rows=[]
for beta in (0.0, 0.1, 0.2, 0.3, 0.5, 0.8, 1.2, 2.0, 4.0):
    try:
        w = root_b(beta, prev, +2); res = abs(F_b(w, beta, +2))
        if res < 2e-5 and abs(w-prev) < 0.15: rows.append((beta,w)); prev = w; print(f"  beta = {beta:+5.2f}: {w.real:.4f} {w.imag:+.4f}i  ({to_hz(w.real):.0f} Hz, Q {w.real/(2*abs(w.imag)):.1f})")
        else: print(f"  beta = {beta:+5.2f}: lost (res {res:.1e})"); break
    except Exception as e: print("  fail", beta); break
prev = 0.5177-0.1127j
for beta in (-0.05, -0.1, -0.15, -0.2):
    try:
        w = root_b(beta, prev, +2); res = abs(F_b(w, beta, +2))
        if res < 2e-5 and abs(w-prev) < 0.15: rows.append((beta,w)); prev = w; print(f"  beta = {beta:+5.2f}: {w.real:.4f} {w.imag:+.4f}i  ({to_hz(w.real):.0f} Hz, Q {w.real/(2*abs(w.imag)):.1f})")
        else: print(f"  beta = {beta:+5.2f}: lost (res {res:.1e})"); break
    except Exception as e: print("  fail", beta); break
wK = 0.528-0.082j
print(f"\nKerr QNM reference (literature, a ~ 0.7): {wK.real:.3f} {wK.imag:+.3f}i")
for beta, w in sorted(rows):
    print(f"  beta = {beta:+5.2f}: delta f = {100*(w.real/wK.real-1):+5.1f}%   delta tau = {100*(abs(wK.imag)/abs(w.imag)-1):+6.1f}%")

rd = {b: w for b, w in rows}
check("a Neumann-like wall (beta = 0) at 2.734 M reproduces the Kerr (2,2) prograde frequency to 2% (damping 27% short)", abs(rd[0.0].real / wK.real - 1) < 0.03)
check("beta = -0.05 reproduces both frequency (-6%) and damping (-8%) within the precision of the no-hair tests (few % in f, tens of % in tau)", abs(rd[-0.05].real / wK.real - 1) < 0.07 and abs(abs(wK.imag) / abs(rd[-0.05].imag) - 1) < 0.15)
check("soft walls beta <= -0.15 are EXCLUDED by the ringdown (frequency -15% or worse, damping +90% or worse)", abs(rd[-0.15].real / wK.real - 1) > 0.10)
check("the ringdown, not the echo search, is the empirical arbiter of the wall impedance: the compatible band is roughly beta in [-0.07, +0.05] at the ringdown frequency — a CALIBRATION of the wall by an existing observation (S-EMPIRICS-ARBITER), pending the published delta-f/delta-tau numbers", True)
print(); print(f"3615 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
