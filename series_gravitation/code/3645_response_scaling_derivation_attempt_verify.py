#!/usr/bin/env python3
"""
Patch 3645 verify — OPEN-GR-SURFACE-IMPEDANCE-1, derivation attempt 1 (from the repo root; reuses 3644's machinery).
Question: does THEO-PCD-BUDGET, taken more faithfully than 3643 took it, produce the surface wave impedance the
ringdown demands (admittance ~0.31, |R| ~ 0.55 at the QNM frequency; 3644 §2)? 3643 put the wave on the effective
metric only. The law also scales the register's RESPONSE per Moment by chi = K/D. Two readings of that scaling:
  'amp': the register displacement is chi x the metric-wave amplitude, u = chi * Phi (adds chi'/chi to the wall law);
  'imp': the medium's impedance is 1/chi x the metric's at fixed speed, (P/chi Phi')' + (Q/chi) Phi = 0.
Each is priced lossless and with an absorber at depth (3644 reading C), l = 2, a = 0, against GW150914's box.
Result: NEITHER changes the verdict — the damping stays 31-37% too fast. The attempt FAILS; the target stays open.
"""
import io, contextlib, numpy as np
from scipy.integrate import solve_ivp
PASS = FAIL = 0
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond); PASS += ok; FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
src = open('series_gravitation/code/3644_ledger_row7_reflectivity_returned_bits_verify.py').read().split('print("(1) a = 0 machinery')[0]
ns = {}
with contextlib.redirect_stdout(io.StringIO()): exec(src, ns)
NP, CAP, RB, J, v_in, root0, dev0, BOX, wGR = (ns[k] for k in ("NP", "CAP", "RB", "J", "v_in", "root0", "dev0", "BOX", "wGR"))
chi = lambda rb: CAP / v_in(rb)
def interior(wc, ell, mode, absorb_at=None, r_in=1e-3):
    def rhs(rb, y):
        N, psi = NP(rb); h = 1e-6
        Np, pp = NP(rb + h); Nm, pm = NP(rb - h)
        P = N * psi**2 * rb**2; dP = (Np * pp**2 * (rb + h)**2 - Nm * pm**2 * (rb - h)**2) / (2 * h)
        Q = wc * wc * psi**6 * rb**2 / N - N * psi**2 * ell * (ell + 1)
        if mode == 'imp':
            dchi = (chi(rb + h) - chi(rb - h)) / (2 * h); dP = dP - P * dchi / chi(rb)
        Phi = y[0] + 1j * y[1]; dPhi = y[2] + 1j * y[3]; d2 = -(dP * dPhi + Q * Phi) / P
        return [dPhi.real, dPhi.imag, d2.real, d2.imag]
    if absorb_at is None:
        y0 = [r_in**ell, 0, ell * r_in**(ell - 1), 0]; start = r_in
    else:
        N, psi = NP(absorb_at); k = wc * psi**2 / N; Phi0 = 1 / absorb_at; dPhi0 = (-1j * k - Phi0) / absorb_at
        y0 = [Phi0.real, Phi0.imag, dPhi0.real, dPhi0.imag]; start = absorb_at
    s = solve_ivp(rhs, [start, RB], y0, rtol=1e-11, atol=1e-14, method="DOP853")
    Phi = s.y[0, -1] + 1j * s.y[1, -1]; dPhi = s.y[2, -1] + 1j * s.y[3, -1]
    u = RB * Phi; du = Phi + RB * dPhi
    if mode == 'amp':
        h = 1e-6; dchi = (chi(RB) - chi(RB - h)) / h; du = du + dchi * u     # chi(RB) = 1, chi' = 2/3
    return du / u / J
print(f"chi = cap/v: 1 at the surface, slope chi'(R) = {(chi(RB)-chi(RB-1e-6))/1e-6:.3f}, 2/3 at the centre")
for mode in ('amp', 'imp'):
    w = root0(lambda wc: interior(wc, 2, mode), 0.42 - 0.10j); d = dev0(w)
    print(f"  {mode} lossless: {w:.4f}  df {d[0]:+.1f}%  dtau {d[1]:+.1f}%")
    check(f"({mode}) lossless: outside the box (as 3643's metric-only wall: df +23%)", not BOX(d))
    fam = {}
    for ra in (1.4, 1.2, 1.0, 0.8):
        w = root0(lambda wc, ra=ra: interior(wc, 2, mode, absorb_at=ra), 0.38 - 0.10j); fam[ra] = dev0(w)
        print(f"  {mode} absorb at rbar = {ra}: {w:.4f}  df {fam[ra][0]:+.1f}%  dtau {fam[ra][1]:+.1f}%  {'IN' if BOX(fam[ra]) else 'out'}")
    check(f"({mode}) absorber-at-depth family: no member in the box; damping stays -27% to -38%", not any(BOX(d) for d in fam.values()),
          f"dtau range {min(d[1] for d in fam.values()):+.0f}% .. {max(d[1] for d in fam.values()):+.0f}%")
check("derivation attempt 1 FAILS: the K/D response scaling, in either reading, does not supply the surface impedance (~3x, |R| ~ 0.55) the ringdown demands. OPEN-GR-SURFACE-IMPEDANCE-1 stays open; s stays UNEXPLAINED (bracket [2.5, 5]), not adopted", True)
print(); print(f"3645 verify: {PASS} passed, {FAIL} failed")
if FAIL: raise SystemExit(1)
