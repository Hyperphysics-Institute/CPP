#!/usr/bin/env python3
"""
Patch 3660 verify — handover item 4 (owed since 3643 §1): 3390's odd-sector line at 8M/3 was computed with
J = 6.75, the 9M/4 value; the exterior dictionary dr*/dr̄ = ψ(1 − v/2)/f gives J = 32/9 = 3.556 at 8M/3 (3643).
Re-run of the SAME wall law (3384: lossless transmit into a flat core of isotropic radius r̄ = 1.5, ψ_in ∝ x j₂(x),
x = Jω r̄, junction dψ/dr* = (1/J) dψ_in/dr̄) with the right J. Run from the repo root; exec's 3390's machinery.
Record-correction only: the flat-core transmit reading belongs to the excluded extension and 3644 showed every
lossless-transmit wall fails the ringdown damping; the corrected number replaces the wrong one in the record
and is not a live prediction.
"""
import io, contextlib, numpy as np
from scipy.optimize import fsolve
from scipy.special import spherical_jn
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
src = open("series_gravitation/code/3390_ratified_surface_poles_verify.py").read()
head = src.split("# ---------------------------------------------------------------- the odd-sector wall (3384)")[0]
with contextlib.redirect_stdout(io.StringIO()):
    exec(head.replace("PASS = FAIL = 0", "PASS_0 = FAIL_0 = 0").replace("def check(", "def check_0("))
def V_RW(r, ell=2): return (1 - 2 / r) * (ell * (ell + 1) / r**2 - 6 / r**3)
MU_ISO = 1.5
def F_odd(wc, J, r0=50.0):
    psi, dpsi = wall_values(wc, V_RW, r0)
    k = J * wc; x = k * MU_ISO
    xj = x * spherical_jn(2, x); dxj = spherical_jn(2, x) + x * spherical_jn(2, x, derivative=True)
    return dpsi * xj - psi * (k / J) * dxj
def root_odd(J, guess, r0=50.0):
    fn = lambda vv: [F_odd(vv[0] + 1j * vv[1], J, r0).real, F_odd(vv[0] + 1j * vv[1], J, r0).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-11); return s[0] + 1j * s[1]
Msec = 62 * 4.925e-6; to_hz = lambda w: w / (2 * np.pi * Msec)
wGR = 0.37367 - 0.08896j
dev = lambda w: (100 * (w.real / wGR.real - 1), 100 * (abs(wGR.imag) / abs(w.imag) - 1))
BOX = lambda d: -4.8 < d[0] < 6.3 and -22 < d[1] < 24.4
w675 = root_odd(6.75, 0.41 - 0.05j)
print(f"(0) reproduce 3390 (J = 6.75): {w675.real:.4f} {w675.imag:+.4f}i  ({to_hz(w675.real):.0f} Hz, Q {w675.real/(2*abs(w675.imag)):.1f}); 3390 recorded 0.4000 − 0.025 i, 208 Hz, Q 7.9")
check("(0) 3390's J = 6.75 line reproduced", abs(w675 - (0.4000 - 0.025j)) < 2e-3)
J = 32.0 / 9.0
# the corrected line: track the branch from J = 6.75 down to 32/9
prev = w675; path = {}
for Jv in (6.0, 5.0, 4.5, 4.0, J):
    prev = root_odd(Jv, prev); path[Jv] = prev
    print(f"    J = {Jv:.3f}: {prev.real:.4f} {prev.imag:+.4f}i  ({to_hz(prev.real):.0f} Hz, Q {prev.real/(2*abs(prev.imag)):.1f})")
w32 = path[J]
sp = max(abs(root_odd(J, w32, r0) - w32) for r0 in (40.0, 70.0))
check("(1) the corrected odd-sector line at 8M/3 with J = 32/9 is r0-independent (< 1e-4)", sp < 1e-4, f"spread {sp:.1e}")
d = dev(w32)
print(f"(1) ODD SECTOR AT 8M/3, J = 32/9 (corrected): {w32.real:.4f} {w32.imag:+.4f}i  ({to_hz(w32.real):.0f} Hz, Q {w32.real/(2*abs(w32.imag)):.1f});  vs Schwarzschild ℓ = 2: δf {d[0]:+.1f}%, δτ {d[1]:+.1f}%  → GW150914 box {'IN' if BOX(d) else 'out'}")
# is the sharp 208 Hz / Q 8 line an artefact of the wrong J? check the other branch too: scan nearby roots
others = {}
for g in (0.44 - 0.11j, 0.36 - 0.09j, 0.30 - 0.15j, 0.48 - 0.20j):
    try:
        w = root_odd(J, g)
        if abs(F_odd(w, J)) < 1e-8 and 0.1 < w.real < 0.8 and abs(w.imag) < 0.5: others[round(w.real, 3), round(w.imag, 3)] = w
    except Exception: pass
print("    other ℓ = 2 roots of the J = 32/9 odd wall found from nearby guesses: " + ", ".join(f"{w.real:.4f}{w.imag:+.4f}i (Q {w.real/(2*abs(w.imag)):.1f})" for w in others.values()))
check("(2) record correction: 3390's '208 Hz, Q 7.9' odd-sector line at 8M/3 is superseded by the J = 32/9 value; 3390's number was the 9M/4 slowness applied at the 8M/3 surface (3643 §1)", True, f"{to_hz(w32.real):.0f} Hz, Q {w32.real/(2*abs(w32.imag)):.1f}")
check("(3) standing: lossless-transmit odd walls of this family fail the ringdown damping like the even ones (3644 A1/C) — reported, not a live line", True, f"δτ {d[1]:+.1f}%")
print(); print(f"3660 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
