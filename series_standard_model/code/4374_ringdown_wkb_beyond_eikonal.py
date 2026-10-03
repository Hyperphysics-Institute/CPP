#!/usr/bin/env python3
"""Patch 4374 - the ringdown estimate beyond the eikonal shortcut (TODO-4365-THIRDORDER (b), first step).

4369/4372 compared Schwarzschild with the steady-percentage exterior (lam = 0: g00 = -e^{-2m/r},
g_ij = e^{2m/r} delta, isotropic) using the eikonal (large-l) light-ring formula: -4.42% in frequency.
Here: the l = 2 fundamental mode of a SCALAR test field, by 3rd-order WKB (Schutz-Will / Iyer-Will, in the form
quoted by Kokkotas/Konoplya), validated on Schwarzschild against the known values.

Static metric ds^2 = -N^2 dt^2 + B dr^2 + R^2 dOmega^2; tortoise dr*/dr = sqrt(B)/N;
scalar potential V = N^2 l(l+1)/R^2 + (1/R) d^2R/dr*^2.
Limits, stated: a scalar test field, not CPP's tensor-wave operator (not derived); non-spinning (GW250114's
remnant has chi_f = 0.68); 3rd-order WKB is good to ~0.1-1% for l = 2, n = 0 in Schwarzschild.
"""
import sympy as sp
from scipy.optimize import minimize_scalar
print(__doc__)

r = sp.symbols('r', positive=True)
m = 1

def wkb3(N, B, R, l, n=0):
    D = lambda f: sp.sqrt(B) ** -1 * N * sp.diff(f, r)       # d/dr*
    V = N**2 * l * (l + 1) / R**2 + D(D(R)) / R
    Vs = [V]
    for _ in range(6):
        Vs.append(sp.simplify(D(Vs[-1])) if len(Vs) < 3 else D(Vs[-1]))
    fV = sp.lambdify(r, V, 'mpmath')
    res = minimize_scalar(lambda x: -float(fV(x)), bounds=(0.6, 6), method='bounded')
    r0 = res.x
    v = [complex(sp.N(Vk.subs(r, r0), 30)).real for Vk in Vs]
    V0, V2, V3, V4, V5, V6 = v[0], v[2], v[3], v[4], v[5], v[6]
    a = n + 0.5
    s = (-2 * V2) ** 0.5
    Lam = (1 / s) * ((1 / 8) * (V4 / V2) * (0.25 + a * a) - (1 / 288) * (V3 / V2) ** 2 * (7 + 60 * a * a))
    Om = (1 / (-2 * V2)) * ((5 / 6912) * (V3 / V2) ** 4 * (77 + 188 * a * a)
                            - (1 / 384) * (V3 ** 2 * V4 / V2 ** 3) * (51 + 100 * a * a)
                            + (1 / 2304) * (V4 / V2) ** 2 * (67 + 68 * a * a)
                            + (1 / 288) * (V3 * V5 / V2 ** 2) * (19 + 28 * a * a)
                            - (1 / 288) * (V6 / V2) * (5 + 4 * a * a))
    w2 = (V0 + s * Lam) - 1j * a * s * (1 + Om)
    w = w2 ** 0.5
    return complex(w.real, -abs(w.imag)), r0

# Schwarzschild in isotropic coordinates
rho = m / (2 * r)
N_s, A_s = (1 - rho) / (1 + rho), (1 + rho) ** 4
# steady-percentage exterior (lam = 0)
N_e, A_e = sp.exp(-m / r), sp.exp(2 * m / r)

ref = {1: 0.2911 - 0.0980j, 2: 0.4832 - 0.0968j}       # 3rd-order WKB, Schwarzschild scalar (Iyer 1987 tables)
exact = {1: 0.2929 - 0.0977j, 2: 0.4836 - 0.0968j}     # numerical (Leaver-type) values
print("   l   Schwarzschild (this code)    ref WKB3         exact          exponential exterior     Re shift   Im shift")
for l in (1, 2, 3):
    ws, _ = wkb3(N_s, A_s, r * A_s ** sp.Rational(1, 2), l)
    we, _ = wkb3(N_e, A_e, r * A_e ** sp.Rational(1, 2), l)
    rs = f"{ref[l].real:.4f}{ref[l].imag:+.4f}i" if l in ref else "      -       "
    ex = f"{exact[l].real:.4f}{exact[l].imag:+.4f}i" if l in exact else "      -       "
    print(f"   {l}   {ws.real:.4f}{ws.imag:+.4f}i          {rs}   {ex}   {we.real:.4f}{we.imag:+.4f}i"
          f"        {100*(we.real/ws.real-1):+6.2f}%   {100*(we.imag/ws.imag-1):+6.2f}%")
print("\n   eikonal (4369): -4.42% in frequency, -4.42% in damping.")
print("   GW250114 box (conv042 L33): frequency +-2.4%, damping (-15, +17)%.")
