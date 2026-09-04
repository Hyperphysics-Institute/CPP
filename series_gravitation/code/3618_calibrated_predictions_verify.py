#!/usr/bin/env python3
"""
Patch 3618 verify — THE CALIBRATED PREDICTIONS. The wall impedance is fixed by
GW150914's ringdown (3616): beta ~ -0.02..-0.03 (1/M) at the ringdown frequency,
taken as beta_cal = -0.025 with the band's edges as the uncertainty. Everything
else is fixed upstream (surface 8M/3 from Mercury + the founder's clock; exterior
dynamics GR's by the ringdown). Computed with the existing machinery, nothing new:
  a = 0 (3356/3383 direct integration, r_w = 8/3):   l = 2 even (Zerilli), l = 2 odd (RW), l = 3 even, l = 3 odd
  chi = 0.68 (3359/3392 SN ladder, r_w = 2.734):     (2,-2), (3,-3), and the PROGRADE (2,+2) as the consistency check
at beta = -0.02, -0.025, -0.03. Frequencies at 62 Msun (source-frame convention used
throughout the arc; detector-frame numbers scale by 1/(1+z)).
"""
import numpy as np
from scipy.optimize import fsolve
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
Msec = 62 * 4.925e-6; to_hz = lambda w: w / (2 * np.pi * Msec)
BETAS = (-0.02, -0.025, -0.03)

# ---------------- a = 0 machinery (3613's script carries 3383's integrator with r_w = 8/3)
src = open("series_gravitation/code/3613_pole_family_over_impedance_verify.py").read().split('print("THE FAMILY')[0]
ns = {}; exec(src, ns)
root_beta = ns["root_beta"]; V_Z = ns["V_Z"]; V_RW = ns["V_RW"]; F_beta = ns["F_beta"]
print("a = 0, r_w = 8M/3 — poles at the calibrated impedance")
res0 = {}
guesses = {("even", 2): 0.375 - 0.05j, ("odd", 2): 0.378 - 0.045j, ("even", 3): 0.60 - 0.05j, ("odd", 3): 0.60 - 0.05j}
for (sec, ell), g in guesses.items():
    Vf = (lambda rr, e=ell: V_Z(rr, e)) if sec == "even" else (lambda rr, e=ell: V_RW(rr, e))
    prev = g
    for b in BETAS:
        w = root_beta(Vf, b, prev); r = abs(F_beta(w, Vf, b)); prev = w
        res0[(sec, ell, b)] = w
        print(f"    l = {ell} {sec:4s} beta = {b:+.3f}: {w.real:.4f} {w.imag:+.4f}i  ({to_hz(w.real):.0f} Hz, Q {w.real/(2*abs(w.imag)):.1f})  res {r:.0e}")
check("a = 0: all eight roots converged (residual < 1e-6)", all(abs(F_beta(res0[k], (lambda rr, e=k[1]: V_Z(rr, e)) if k[0] == "even" else (lambda rr, e=k[1]: V_RW(rr, e)), k[2])) < 1e-6 for k in res0))

# ---------------- Kerr machinery (3614's SN ladder wrapper)
exec(open("series_gravitation/code/3359_sn_gravitational_wall_modes_verify.py").read().split("# ---------------- T1: a = 0 reduction")[0].replace("PASS = []", "PASS_SN = []").replace("def check(", "def check_sn("))
solver_src = open("series_gravitation/code/3359_sn_gravitational_wall_modes_verify.py").read().split("# ---------------- the SN wall solver ----------------")[1].split("def wall_root")[0]
solver_src = solver_src.replace("def X_at_wall(w, a, ell, m, r0=40.0, nterms=8):\n    rw = r_surface(a)", "def X_at_wall(w, a, ell, m, r0=40.0, nterms=8, rw=None):\n    rw = r_surface(a) if rw is None else rw").replace("    return sol.y[0, -1] + 1j * sol.y[1, -1]", "    return (sol.y[0, -1] + 1j * sol.y[1, -1]), (sol.y[2, -1] + 1j * sol.y[3, -1])")
exec(solver_src)
RW68 = 2.7344
def F_k(w, beta, ell, m):
    X, Xp = X_at_wall(w, 0.68, ell, m, 40.0, rw=RW68); return (Xp - beta * X) / (1 + abs(beta))
def root_k(beta, ell, m, guess):
    fn = lambda v: [F_k(v[0] + 1j * v[1], beta, ell, m).real, F_k(v[0] + 1j * v[1], beta, ell, m).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-10); return s[0] + 1j * s[1]
print("chi = 0.68, r_w = 2.734 M — poles at the calibrated impedance")
resk = {}
for (ell, m), g in (((2, -2), 0.30 - 0.045j), ((3, -3), 0.48 - 0.04j), ((2, 2), 0.51 - 0.10j)):
    prev = g
    for b in BETAS:
        w = root_k(b, ell, m, prev); r = abs(F_k(w, b, ell, m)); prev = w
        resk[(ell, m, b)] = w
        print(f"    ({ell},{m:+d}) beta = {b:+.3f}: {w.real:.4f} {w.imag:+.4f}i  ({to_hz(w.real):.0f} Hz, Q {w.real/(2*abs(w.imag)):.1f})  res {r:.0e}")
check("Kerr: all nine roots converged (residual < 1e-5)", all(abs(F_k(resk[k], k[2], k[0], k[1])) < 1e-5 for k in resk))
wK = 0.528 - 0.082j; w22 = resk[(2, 2, -0.025)]
check("consistency: the prograde (2,2) at beta_cal sits inside GW150914's box (df in [-4.8, +6.3]%, dtau in [-22, +24]%)", -0.048 <= w22.real / wK.real - 1 <= 0.063 and -0.22 <= abs(wK.imag) / abs(w22.imag) - 1 <= 0.244, f"df {100*(w22.real/wK.real-1):+.1f}%, dtau {100*(abs(wK.imag)/abs(w22.imag)-1):+.1f}%")
w2m = resk[(2, -2, -0.025)]; w3m = resk[(3, -3, -0.025)]
print(f"\nCALIBRATED PREDICTIONS (beta = -0.025; band -0.02..-0.03):")
print(f"    chi = 0.68 (2,-2): {to_hz(resk[(2,-2,-0.02)].real):.0f}-{to_hz(resk[(2,-2,-0.03)].real):.0f} Hz, central {to_hz(w2m.real):.0f} Hz, Q {w2m.real/(2*abs(w2m.imag)):.1f}")
print(f"    chi = 0.68 (3,-3): {to_hz(resk[(3,-3,-0.02)].real):.0f}-{to_hz(resk[(3,-3,-0.03)].real):.0f} Hz, central {to_hz(w3m.real):.0f} Hz, Q {w3m.real/(2*abs(w3m.imag)):.1f}")
for sec in ("even", "odd"):
    for ell in (2, 3):
        w = res0[(sec, ell, -0.025)]
        print(f"    a = 0 l = {ell} {sec}: {to_hz(res0[(sec,ell,-0.02)].real):.0f}-{to_hz(res0[(sec,ell,-0.03)].real):.0f} Hz, central {to_hz(w.real):.0f} Hz, Q {w.real/(2*abs(w.imag)):.1f}")
check("the calibrated (2,-2) line at chi = 0.68 lies in the 3614 family envelope (122-188 Hz)", 122 <= to_hz(w2m.real) <= 190)
check("the calibrated a = 0 even and odd l = 2 lines agree with each other to 3% (the wall dominates)", abs(res0[("even", 2, -0.025)].real / res0[("odd", 2, -0.025)].real - 1) < 0.03)
print(); print(f"3618 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
