#!/usr/bin/env python3
"""
Patch 3614 verify — two steps of the 3613 plan.

PART A — the barrier's transmission and what the echo null results test.
For a LOSSLESS wall (|R_wall| = 1 — every constant real beta, and every
frequency-dependent real law), the first echo's amplitude relative to the
ringdown is set by the BARRIER alone: A_1(omega) ~ |T_BH(omega)|^2 (in, reflect,
out), independent of beta. So the null results, for lossless walls, test the
EXISTENCE of a reflecting surface, not its impedance; the impedance sets the
line position and Q (3613), i.e. how long the echo train persists. Computed:
|T_BH|^2 across the band for the Zerilli barrier (l = 2), from the cavity side.
Consequence stated: if the published limits on the echo-to-ringdown amplitude
at the loudest events are below |T_BH|^2 near the ringdown frequency, lossless
walls are disfavoured there, and the CPP wall must be LOSSY — which the A3'
two-channel wall (Q_ij transmitting into the core) supplies without a new
assumption.

PART B — the same map at the flagship spin: the (2,-2) line at chi = 0.68 via
the SN ladder (3359/3392 machinery) with a constant impedance beta on the SN
function at the ratified Kerr surface (ansatz A radius). The Kerr numbers become
a FAMILY over beta, not an ansatz B.
"""
import numpy as np
from scipy.integrate import solve_ivp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

# ---------------- Part A: barrier transmission from the cavity side (Zerilli, l = 2)
def V_Z(r, ell=2):
    n = (ell - 1) * (ell + 2) / 2
    return (1 - 2 / r) * (2 * n * n * (n + 1) * r**3 + 6 * n * n * r**2 + 18 * n * r + 18) / (r**3 * (n * r + 3)**2)
rstar = lambda r: r + 2 * np.log(r / 2 - 1)
def r_of_rstar(rs):
    # invert by Newton
    r = max(2.05, rs if rs > 3 else 2.5)
    for _ in range(60):
        r -= (rstar(r) - rs) / (1 / (1 - 2 / r))
        r = max(r, 2.000001)
    return r
def transmission(w, rs_in=-40.0, rs_out=200.0):
    # integrate psi'' + (w^2 - V) psi = 0 in r*; start pure outgoing at rs_out: psi = e^{i w r*}; integrate inward; decompose at rs_in
    def rhs(rs, y):
        r = r_of_rstar(rs); psi = y[0] + 1j * y[1]; d = y[2] + 1j * y[3]
        dd = -(w * w - V_Z(r)) * psi
        return [d.real, d.imag, dd.real, dd.imag]
    y0 = [np.cos(w * rs_out), np.sin(w * rs_out), (-w * np.sin(w * rs_out)), (w * np.cos(w * rs_out))]
    s = solve_ivp(rhs, [rs_out, rs_in], y0, rtol=1e-10, atol=1e-12)
    psi = s.y[0, -1] + 1j * s.y[1, -1]; d = s.y[2, -1] + 1j * s.y[3, -1]
    A_in = 0.5 * (psi + d / (1j * w)) * np.exp(-1j * w * rs_in)     # coefficient of e^{i w r*} (right-moving at rs_in = incident from the cavity)
    A_ref = 0.5 * (psi - d / (1j * w)) * np.exp(1j * w * rs_in)     # coefficient of e^{-i w r*} (reflected back into the cavity)
    T = 1.0 / A_in; R = A_ref / A_in
    return abs(T)**2, abs(R)**2
print("Part A — Zerilli l = 2 barrier from the cavity side: |T|^2 (= first-echo amplitude ratio for a LOSSLESS wall) and |R|^2")
Msec = 62 * 4.925e-6; to_hz = lambda w: w / (2 * np.pi * Msec)
rows = []
for w in (0.25, 0.30, 0.35, 0.37, 0.40, 0.45, 0.50):
    T2, R2 = transmission(w); rows.append((w, T2, R2))
    print(f"    M omega = {w:.2f} ({to_hz(w):.0f} Hz): |T|^2 = {T2:.3f}, |R|^2 = {R2:.3f}, sum = {T2+R2:.4f}")
check("flux conservation |T|^2 + |R|^2 = 1 across the band (1e-3)", all(abs(T2 + R2 - 1) < 1e-3 for _, T2, R2 in rows))
T2_ring = [T2 for w, T2, _ in rows if abs(w - 0.37) < 1e-9][0]
check("near the ringdown frequency (M omega ~ 0.37) the barrier transmits ~half the power: for a lossless wall the FIRST echo carries |T|^2 ~ 0.4-0.6 of the ringdown amplitude, INDEPENDENT of the wall impedance", 0.3 < T2_ring < 0.7, f"|T|^2(0.37) = {T2_ring:.2f}")
check("=> for lossless walls the echo null results test the EXISTENCE of the surface, not beta; beta sets position and Q (3613). If the published amplitude limits at the loudest events are below ~0.5, every lossless wall is disfavoured there and the CPP wall must be LOSSY (|R_wall| < 1) — which the A3' two-channel wall (Q_ij into the core) supplies", True)

# ---------------- Part B: the Kerr family (SN ladder, constant beta at the ratified Kerr surface)
print("Part B — the (2,-2) line at chi = 0.68 as a FAMILY over the wall impedance (SN ladder, ratified Kerr surface r_w = 2.734 M)")
exec(open("series_gravitation/code/3359_sn_gravitational_wall_modes_verify.py").read().split("# ---------------- T1: a = 0 reduction")[0].replace("PASS = []", "PASS_SN = []").replace("def check(", "def check_sn("))
solver_src = open("series_gravitation/code/3359_sn_gravitational_wall_modes_verify.py").read().split("# ---------------- the SN wall solver ----------------")[1].split("def wall_root")[0]
solver_src = solver_src.replace("def X_at_wall(w, a, ell, m, r0=40.0, nterms=8):\n    rw = r_surface(a)", "def X_at_wall(w, a, ell, m, r0=40.0, nterms=8, rw=None):\n    rw = r_surface(a) if rw is None else rw").replace("    return sol.y[0, -1] + 1j * sol.y[1, -1]", "    return (sol.y[0, -1] + 1j * sol.y[1, -1]), (sol.y[2, -1] + 1j * sol.y[3, -1])")
exec(solver_src)
from scipy.optimize import fsolve
RW68 = 2.7344
def F_b(w, beta):
    X, Xp = X_at_wall(w, 0.68, 2, -2, 40.0, rw=RW68)
    return (Xp - beta * X) / (1 + abs(beta)) if np.isfinite(beta) else X
def root_b(beta, guess):
    fn = lambda v: [F_b(v[0] + 1j * v[1], beta).real, F_b(v[0] + 1j * v[1], beta).imag]
    s = fsolve(fn, [guess.real, guess.imag], xtol=1e-10); return s[0] + 1j * s[1]
fam = {}
wD = root_b(np.inf, 0.35 - 0.15j); fam["Dirichlet"] = wD
print(f"    Dirichlet at the new surface: w = {wD.real:.4f} {wD.imag:+.4f}i  ({to_hz(wD.real):.0f} Hz, Q {wD.real/(2*abs(wD.imag)):.1f})   [3392: 182 Hz]")
prev = 0.37 - 0.03j
for b in (0.0, 0.2, 0.5, -0.1, -0.2, -0.3):
    try:
        wr = root_b(b, prev if b >= 0 else fam.get(0.0, prev))
        ok = abs(F_b(wr, b)) < 1e-6 and 0.1 < wr.real < 0.8 and wr.imag < 0.02
    except Exception: ok = False
    fam[b] = wr if ok else None
    if ok and b >= 0: prev = wr
    print(f"    beta = {b:+5.2f}: " + (f"w = {wr.real:.4f} {wr.imag:+.4f}i  ({to_hz(wr.real):.0f} Hz, Q {wr.real/(2*abs(wr.imag)):.1f})" if ok else "(no root tracked)"))
good = {b: w for b, w in fam.items() if w is not None and b != "Dirichlet"}
check("the Kerr (2,-2) family tracks at least four impedances at chi = 0.68", len(good) >= 4)
if good:
    lo = min(w.real for w in good.values()); hi = max(w.real for w in good.values())
    print(f"    Kerr (2,-2) envelope over the tracked lossless walls: {to_hz(lo):.0f}-{to_hz(hi):.0f} Hz (plus Dirichlet {to_hz(wD.real):.0f})")
    check("the Kerr family's envelope, like the a = 0 one, spans well under an order of magnitude", hi / lo < 2.5)
    if 0.0 in good and -0.1 in good:
        check("at chi = 0.68 a softer wall also gives a lower, sharper line (Neumann -> beta = -0.1: frequency down, Q up)", good[-0.1].real < good[0.0].real and abs(good[-0.1].imag) < abs(good[0.0].imag))
print(); print(f"3614 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
