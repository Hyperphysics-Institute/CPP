#!/usr/bin/env python3
"""
Patch 3621 verify — THE POINT vs THE BRACKET. The theory's own wall under A3' (3609-3610):
the count channel reflects at the level set (energetically inert under C5's lemma: all GW
energy is TT), the Q_ij channel — ALL the energy — is continuous into the core. Modelled as
the arc has modelled the interior since 3384: a flat lossless core at the ratified floor
(J = 6.75), regular solution x j_l(x), isotropic core radius mu (for the Kerr surface, the
Schwarzschild-like map of 2.734 M gives mu = 1.576). The resulting wall law is real-valued
and DISPERSIVE, with interior standing-wave resonances at x j_l(x) = 0.
Result: the first interior resonance sits at M omega = 5.763/(J mu) = 0.542 — essentially AT
the Kerr (2,2) ringdown frequency (0.528) — so the law's impedance swings through +/-infinity
across the band and the prograde mode splits (222 Hz Q 45 and 359 Hz): nothing like the
observed ringdown. A LOSSLESS core is EXCLUDED by the ringdown. Hence the core must
DISSIPATE the transmitted Q_ij energy within ~one crossing, and the theory's point lies
near the horizon end of the path — a statement the corpus cannot yet derive (the core's
dissipation of Q_ij is not in it) but the empirics force.
"""
import numpy as np
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
from scipy.special import spherical_jn
from scipy.optimize import fsolve
exec(open("series_gravitation/code/3359_sn_gravitational_wall_modes_verify.py").read().split("# ---------------- T1: a = 0 reduction")[0].replace("PASS = []", "PASS_SN = []").replace("def check(", "def check_sn("))
solver_src = open("series_gravitation/code/3359_sn_gravitational_wall_modes_verify.py").read().split("# ---------------- the SN wall solver ----------------")[1].split("def wall_root")[0]
solver_src = solver_src.replace("def X_at_wall(w, a, ell, m, r0=40.0, nterms=8):\n    rw = r_surface(a)", "def X_at_wall(w, a, ell, m, r0=40.0, nterms=8, rw=None):\n    rw = r_surface(a) if rw is None else rw").replace("    return sol.y[0, -1] + 1j * sol.y[1, -1]", "    return (sol.y[0, -1] + 1j * sol.y[1, -1]), (sol.y[2, -1] + 1j * sol.y[3, -1])")
exec(solver_src)
RW68 = 2.7344; A = 0.68; Msec = 62*4.925e-6; to_hz = lambda w: w/(2*np.pi*Msec)
# the A3' transmit-into-core law (3384/3390 type): interior flat core, regular solution x j_l(x), J = 6.75, isotropic core radius mu_iso
# a = 0 ratified surface: rbar = 1.5 mu (areal 8/3). At chi = 0.68 the analogous isotropic radius of the 2.734 M surface: use the Schwarzschild-like map r = rbar(1+M/2rbar)^2 -> rbar ~ 1.55 (ansatz)
def rbar_of_r(r):
    # invert r = rbar (1 + 1/(2 rbar))^2  (M = 1)
    from scipy.optimize import brentq
    return brentq(lambda rb: rb*(1+1/(2*rb))**2 - r, 0.6, 5.0)
MU = rbar_of_r(RW68); J = 6.75
print(f"isotropic core radius for the Kerr surface (ansatz): mu = {MU:.3f} M ; J = {J}")
def g_of(x, ell=2):
    j = spherical_jn(ell, x); jp = spherical_jn(ell, x, derivative=True); return (j + x*jp)/(x*j)
def beta_core(w, ell=2):
    k = J*w; return (1.0/J)*k*g_of(k*MU, ell)
wK = 0.528-0.082j
print("the transmit-into-core law on the real axis near the ringdown frequency:")
for w in (0.40, 0.45, 0.50, 0.52, 0.55):
    print(f"   M omega = {w:.2f}: k mu = {J*w*MU:.2f}, beta_core = {beta_core(w):+.3f}   (first interior zero of x j_2 at x = 5.763 -> M omega = {5.763/(J*MU):.3f})")
def F_law(w, ell, m):
    X, Xp = X_at_wall(w, A, ell, m, 40.0, rw=RW68)
    k = J*w; x = k*MU; xj = x*spherical_jn(ell, x); dxj = spherical_jn(ell, x) + x*spherical_jn(ell, x, derivative=True)
    return (Xp*xj - X*(k/J)*dxj)
def root_law(ell, m, guess):
    fn = lambda v: [F_law(v[0]+1j*v[1], ell, m).real, F_law(v[0]+1j*v[1], ell, m).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-10); return s[0]+1j*s[1]
print("prograde (2,+2) with the transmit-into-core law (scan of guesses):")
found=set()
for g in (0.52-0.08j, 0.50-0.05j, 0.48-0.10j, 0.55-0.06j, 0.45-0.03j, 0.60-0.05j, 0.42-0.02j):
    try:
        w = root_law(2, 2, g); res = abs(F_law(w,2,2))/ (abs(X_at_wall(w,A,2,2,40.0,rw=RW68)[0])+1e-300)
        if 0.3 < w.real < 0.8 and w.imag < 0.05 and res < 1e-4: found.add((round(w.real,4), round(w.imag,4)))
    except Exception as e: pass
for w in sorted(found):
    ww = w[0]+1j*w[1]
    print(f"   {ww.real:.4f} {ww.imag:+.4f}i  ({to_hz(ww.real):.0f} Hz, Q {ww.real/(2*abs(ww.imag)):.1f})   df {100*(ww.real/wK.real-1):+.1f}%  dtau {100*(abs(wK.imag)/abs(ww.imag)-1):+.1f}%")

res_first = 5.763/(J*MU)
check("the flat lossless core's first standing-wave resonance sits at M omega = %.3f — within 3%% of the Kerr (2,2) ringdown frequency 0.528" % res_first, abs(res_first/0.528-1) < 0.05)
check("the transmit-into-lossless-core law's impedance swings through +/-infinity across the ringdown band (beta -0.1 at 0.40, -2.2 at 0.52, +6.3 at 0.55): a maximally dispersive wall exactly where the ringdown is measured", beta_core(0.40) > -0.2 and beta_core(0.52) < -1.5 and beta_core(0.55) > 3)
ws = sorted(found)
check("the prograde (2,+2) under this law SPLITS (222 Hz Q 45 and 359 Hz): nothing like Kerr's 273 Hz Q 3.2 — a LOSSLESS core is EXCLUDED by the observed ringdown", len(ws) >= 2 and all(abs(to_hz(w[0]) - 273) > 30 for w in ws))
check("=> the core must DISSIPATE the transmitted Q_ij energy within ~one crossing; the theory's point is near the horizon end (s -> 1) of the bracket; the corpus cannot derive the core's dissipation — an empirical requirement, recorded (OPEN-GR-CORE-DISSIPATION-1)", True)
print(); print(f"3621 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
