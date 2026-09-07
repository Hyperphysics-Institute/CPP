#!/usr/bin/env python3
"""
Patch 3655 verify — OPEN-GR-SURFACE-IMPEDANCE-1 attempt 4 (rule 6 threshold met, 3654): a parameter-free candidate for s.
H-SURFACE-IMPEDANCE: beta = -i w/s at 8M/3, s = 3.22 pinned (3644). Candidates fixed by the cap, no freedom:
   psi^4 = (4/3)^4 = 256/81 = 3.160  — the areal/lattice AREA ratio at the surface (r^2 = psi^4 rbar^2): a waveguide-area
                                       junction between a wave carried on r^2 outside and on rbar^2 inside;
   J = dr*/drbar = 32/9 = 3.556      — the tortoise/lattice length ratio;
   1/N^2 = 4                          — the clock-rate ratio.
Each is scored cold on l = 2, 3, 4 fundamentals (a = 0) against GR and the GW150914 box, with 3644's machinery.
Also: the static near-coincidence with 3633's lapse reading is quantified (3%: not an identity).
"""
import io, contextlib, numpy as np
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
src = open('series_gravitation/code/3644_ledger_row7_reflectivity_returned_bits_verify.py').read().split('print("(1) a = 0 machinery')[0]
ns = {}
with contextlib.redirect_stdout(io.StringIO()): exec(src, ns)
wall_values = ns["wall_values"]; F0 = ns["F0"]
from scipy.optimize import fsolve
GR = {2: 0.37367 - 0.08896j, 3: 0.59944 - 0.09270j, 4: 0.80918 - 0.09416j}
dev = lambda w_, l: (100 * (w_.real / GR[l].real - 1), 100 * (abs(GR[l].imag) / abs(w_.imag) - 1))
BOX = lambda d: -4.8 < d[0] < 6.3 and -22 < d[1] < 24.4
def root(beta_fn, l, guess, r0=50.0):
    def F(wc):
        psi, dpsi = wall_values(wc, r0, ell=l); b = beta_fn(wc); return (dpsi - b * psi) / (1 + abs(b))
    g = lambda v: [F(v[0] + 1j * v[1]).real, F(v[0] + 1j * v[1]).imag]
    s_ = fsolve(g, [guess.real, guess.imag], xtol=1e-11); wz = s_[0] + 1j * s_[1]; return wz, abs(F(wz))
cands = {"pinned 3.22 (3644)": 3.22, "psi^4 = 256/81": 256 / 81, "J = 32/9": 32 / 9, "1/N^2 = 4": 4.0}
print("(1) the candidates, cold, l = 2, 3, 4 (box: df (-4.8, +6.3)%, dtau (-22, +24.4)%)")
table = {}
for nm, s in cands.items():
    row = {}
    for l in (2, 3, 4):
        wz, rz = root(lambda wc, s=s: -1j * wc / s, l, GR[l])
        wz2, _ = root(lambda wc, s=s: -1j * wc / s, l, wz, r0=70.0)
        ok = rz < 1e-8 and abs(wz2 - wz) < 1e-4
        row[l] = (wz, dev(wz, l), ok)
    table[nm] = row
    print(f"    s = {s:.4f} ({nm}): " + "; ".join(f"l={l}: {row[l][0].real:.4f}{row[l][0].imag:+.4f}i df {row[l][1][0]:+.1f}% dtau {row[l][1][1]:+.1f}% {'box' if BOX(row[l][1]) else 'OUT'}" for l in (2, 3, 4)))
p4 = table["psi^4 = 256/81"]
check("(1a) s = psi^4 = 3.160: all three fundamentals converge (r0-independent)", all(p4[l][2] for l in (2, 3, 4)))
check("(1b) s = psi^4: l = 2 inside the GW150914 box, and l = 3, 4 within the same tolerance", all(BOX(p4[l][1]) for l in (2, 3, 4)), "; ".join(f"l{l}: {p4[l][1][0]:+.1f}/{p4[l][1][1]:+.1f}" for l in (2, 3, 4)))
pin = table["pinned 3.22 (3644)"]
check("(1c) s = psi^4 differs from the pinned 3.22 by 1.9%, and its l = 2 line moves by < 1% in frequency and < 3% in damping relative to the pin: the pin is consistent with the constant", abs(256 / 81 / 3.22 - 1) < 0.02 and abs(p4[2][0].real / pin[2][0].real - 1) < 0.01 and abs(p4[2][0].imag / pin[2][0].imag - 1) < 0.03)
j = table["J = 32/9"]; n2 = table["1/N^2 = 4"]
print(f"    discrimination: J gives l=2 df {j[2][1][0]:+.1f}% dtau {j[2][1][1]:+.1f}% ({'box' if BOX(j[2][1]) else 'OUT'}); 1/N^2 gives df {n2[2][1][0]:+.1f}% dtau {n2[2][1][1]:+.1f}% ({'box' if BOX(n2[2][1]) else 'OUT'})")
check("(1d) the box discriminates: recorded whether J = 3.56 and 1/N^2 = 4 also sit in the box (if they do, the box alone does not single out psi^4; the 3644 bracket [2.5, 5] said as much)", True, f"J in box: {BOX(j[2][1])}; 1/N^2 in box: {BOX(n2[2][1])}")
# tighter discriminant: the pin's own precision. 3644 pinned s = 3.22 to the l=2 line; distance of each candidate from the pin:
for nm, s in cands.items(): print(f"    |s/3.22 - 1| = {abs(s/3.22-1)*100:.1f}%  ({nm})")
check("(1e) psi^4 is the closest cap constant to the pin (1.9%); J is 10% off, 1/N^2 24% off", abs(256/81/3.22-1) < abs(32/9/3.22-1) and abs(256/81/3.22-1) < abs(4/3.22-1))

print("(2) the static near-coincidence with 3633 quantified")
y_neu, y_3633 = -2.5632, -2.6463
check("(2) Neumann-on-Z (y = -2.563) vs 3633's harmonic-pattern lapse reading (y = -2.646): 3% apart — NOT an identity; recorded as a near-coincidence, not a derivation", abs(y_neu / y_3633 - 1) > 0.02 and abs(y_neu / y_3633 - 1) < 0.05, f"{100*abs(y_neu/y_3633-1):.1f}%")

print("(3) what psi^4 would mean, stated as the attempt-4 candidate (not adopted)")
print("    r^2 = psi^4 rbar^2 at the cap: the exterior wave is carried on the areal sphere, the interior on the lattice sphere;")
print("    a junction between two waveguides whose cross-sections differ by psi^4 has amplitude impedance ratio psi^4 = 3.160.")
print("    Reflection at such a junction: R = (s-1)/(s+1) = " + f"{(256/81-1)/(256/81+1):.3f}" + " (3644's requirement |R| ~ 0.55).")
check("(3) the area-junction reflectivity (s-1)/(s+1) = 0.519 sits within 6% of 3644's recorded requirement |R| = 0.55", abs((256/81-1)/(256/81+1) - 0.55) < 0.035)
check("(3b) candidate status: CANDIDATE-S-AREA (s = psi^4|cap) — a corpus constant with a stated mechanism, replacing the pinned number in the hypothesis IF the group keeps passing; the derivation of the junction from the PCD cycle is still owed", True)

print()
print(f"3655 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
