#!/usr/bin/env python3
"""
Patch 3620 verify — THE BRACKET. The R-core's line set between its two ends:
the LOSSLESS end (beta = -0.025 real, the ringdown-calibrated impedance without
absorption) and the HORIZON-EQUIVALENT end (beta_Kerr(omega): the ingoing-at-horizon
solution's log-derivative at the wall — a surface that absorbs as a horizon does,
i.e. a black hole). The theory's A3' wall lies between (JUNCTION-1 places it).
Computed for (2,-2), (3,-3) and the prograde (2,+2) at chi = 0.68, r_w = 2.734 M,
at s = 0 (lossless), 0.5 (half-absorbing), 1 (horizon). 62 Msun.
"""
import numpy as np
from scipy.optimize import fsolve
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
Msec = 62 * 4.925e-6; to_hz = lambda w: w / (2 * np.pi * Msec)
exec(open("series_gravitation/code/3359_sn_gravitational_wall_modes_verify.py").read().split("# ---------------- T1: a = 0 reduction")[0].replace("PASS = []", "PASS_SN = []").replace("def check(", "def check_sn("))
solver_src = open("series_gravitation/code/3359_sn_gravitational_wall_modes_verify.py").read().split("# ---------------- the SN wall solver ----------------")[1].split("def wall_root")[0]
solver_src = solver_src.replace("def X_at_wall(w, a, ell, m, r0=40.0, nterms=8):\n    rw = r_surface(a)", "def X_at_wall(w, a, ell, m, r0=40.0, nterms=8, rw=None):\n    rw = r_surface(a) if rw is None else rw").replace("    return sol.y[0, -1] + 1j * sol.y[1, -1]", "    return (sol.y[0, -1] + 1j * sol.y[1, -1]), (sol.y[2, -1] + 1j * sol.y[3, -1])")
exec(solver_src)
RW68 = 2.7344; A = 0.68
def beta_kerr(w, ell, m, a=A):
    Aang = A_leaver(a * w, ell, m); lam = Aang + a * a * w * w - 2 * a * m * w
    rp = 1 + np.sqrt(1 - a * a); OmH = a / (2 * rp); k = w - m * OmH
    r_start = rp + 1e-3; X0 = np.exp(-1j * k * rstar(r_start, a)); Xp0 = -1j * k * X0
    def rhs(t, y):
        r = y[4]; D = r * r - 2 * r + a * a; F, U = sn_FU(r, a, w, m, lam)
        X = y[0] + 1j * y[1]; Xp = y[2] + 1j * y[3]; return [Xp.real, Xp.imag, (F * Xp + U * X).real, (F * Xp + U * X).imag, D / (r * r + a * a)]
    sol = solve_ivp(rhs, [rstar(r_start, a), rstar(RW68, a)], [X0.real, X0.imag, Xp0.real, Xp0.imag, r_start], rtol=1e-11, atol=1e-13, method="DOP853")
    return (sol.y[2, -1] + 1j * sol.y[3, -1]) / (sol.y[0, -1] + 1j * sol.y[1, -1])
def F_k(w, beta, ell, m):
    X, Xp = X_at_wall(w, A, ell, m, 40.0, rw=RW68); return (Xp - beta * X) / (1 + abs(beta))
def root_k(beta_fn, ell, m, guess):
    fn = lambda v: [F_k(v[0] + 1j * v[1], beta_fn(v[0] + 1j * v[1]), ell, m).real, F_k(v[0] + 1j * v[1], beta_fn(v[0] + 1j * v[1]), ell, m).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-10); return s[0] + 1j * s[1]
print("chi = 0.68, wall 2.734 M — the line set along the path from the lossless calibrated wall (s = 0) to the horizon (s = 1)")
res = {}
for (ell, m), g in (((2, -2), 0.305 - 0.043j), ((3, -3), 0.49 - 0.034j), ((2, 2), 0.508 - 0.10j)):
    prev = g
    for sfrac in (0.0, 0.5, 1.0):
        w = root_k(lambda wc, sf=sfrac, e=ell, mm=m: (1 - sf) * (-0.025) + sf * beta_kerr(wc, e, mm), ell, m, prev); prev = w; res[(ell, m, sfrac)] = w
        print(f"    ({ell},{m:+d})  s = {sfrac:.1f}: {w.real:.4f} {w.imag:+.4f}i  ({to_hz(w.real):.0f} Hz, Q {w.real/(2*abs(w.imag)):.1f})")
check("all nine roots converged (residual < 1e-5)", all(abs(F_k(res[k], (1 - k[2]) * (-0.025) + k[2] * beta_kerr(res[k], k[0], k[1]), k[0], k[1])) < 1e-5 for k in res))
# the horizon end must be the Kerr QNM of each mode (a black hole): sanity on the (2,+2)
w22K = res[(2, 2, 1.0)]
check("the horizon end of the prograde (2,2) is the Kerr QNM (0.524 - 0.081i, 3619)", abs(w22K - (0.5242 - 0.0810j)) < 0.01)
for (ell, m) in ((2, -2), (3, -3)):
    f0 = to_hz(res[(ell, m, 0.0)].real); f1 = to_hz(res[(ell, m, 1.0)].real)
    Q0 = res[(ell, m, 0.0)].real / (2 * abs(res[(ell, m, 0.0)].imag)); Q1 = res[(ell, m, 1.0)].real / (2 * abs(res[(ell, m, 1.0)].imag))
    print(f"    ({ell},{m:+d}): frequency lossless -> horizon: {f0:.0f} -> {f1:.0f} Hz ({100*(f0/f1-1):+.1f}%);  Q: {Q0:.1f} -> {Q1:.1f}")
check("the FREQUENCIES barely move along the path (< 6%): the R-core's lines sit at Kerr's retrograde QNM frequencies", all(abs(to_hz(res[(l, m, 0.0)].real) / to_hz(res[(l, m, 1.0)].real) - 1) < 0.06 for l, m in ((2, -2), (3, -3))))
check("the Q's are what the surface changes: the lossless wall makes the lines 2-3x longer-lived than a black hole's; the R-core's signature is longer-lived modes, by an amount set by its absorption", all(res[(l, m, 0.0)].real / (2 * abs(res[(l, m, 0.0)].imag)) > 1.5 * res[(l, m, 1.0)].real / (2 * abs(res[(l, m, 1.0)].imag)) for l, m in ((2, -2), (3, -3))))
print(); print(f"3620 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
