#!/usr/bin/env python3
"""Patch 4380 - can the corpus fix kappa (the round-trip clock's leg asymmetry, 4379)?  The founder defers the
magnitude to calculation (3 Oct 2026).

  1. The window GW250114 allows (eikonal, non-spinning): kappa from the -2.4% and +2.4% edges.
  2. Natural-looking normalisations of "the extra leg asymmetry is the extra directly-informed part of the
     sphere", each giving delta_beta = kappa * rho near ordinary space (fill f = (1+rho)^6 / 8, f0 = 1/8):
       a. extra fill fraction           df
       b. extra fill relative to the uninformed remainder   df / (1 - f0)
       c. extra fill relative to the ordinary fill           df / f0
       d. extra band depth (radius fraction)                 d(depth),  depth = 1 - (1 - f)^(1/3)
       e. extra band depth relative to the ordinary depth    d(depth) / depth0
  3. The baseline condition: if ordinary space already has a leg asymmetry beta0, the round trip gives
     X = (1 - (beta0 + db)^2) / (1 - beta0^2), with a FIRST-order term -2 beta0 db / (1 - beta0^2).
"""
import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar, brentq
print(__doc__)

def metric(r, k):
    x = 1 / (2 * r)
    N = np.exp(-(2 / k) * np.arctanh(k * x)) if k > 0 else np.exp(-2 * x)
    return N, (1 - k * k * x * x) / N
def shift(k):
    lo = max(0.55, 0.5 * k + 1e-3)
    bc = minimize_scalar(lambda r: r * metric(r, k)[1] / metric(r, k)[0], bounds=(lo, 10), method='bounded').fun
    return 3 * np.sqrt(3) / bc - 1
kmin = brentq(lambda k: shift(k) + 0.024, 0.0, 1.0)
kmax = brentq(lambda k: shift(k) - 0.024, 1.0, 1.8)
print(f"1. GW250114 window (eikonal, non-spinning): {kmin:.2f} <= kappa <= {kmax:.2f};  kappa = 1 is exact Einstein")

rho = sp.symbols('rho', positive=True)
f = (1 + rho) ** 6 / 8
f0 = sp.Rational(1, 8)
depth = 1 - (1 - f) ** sp.Rational(1, 3)
depth0 = depth.subs(rho, 0)
cands = {
    "a. df": f - f0,
    "b. df / (1 - f0)": (f - f0) / (1 - f0),
    "c. df / f0": (f - f0) / f0,
    "d. d(depth)": depth - depth0,
    "e. d(depth) / depth0": (depth - depth0) / depth0,
}
print("\n2. candidate normalisation          kappa (slope at ordinary space)   inside the window?")
for name, expr in cands.items():
    kap = float(sp.diff(expr, rho).subs(rho, 0))
    ok = "yes" if kmin <= kap <= kmax else "no"
    print(f"   {name:34s}  {kap:8.3f}                          {ok}")
print("   -> the natural-looking choices scatter from ~0.3 to ~6: none is forced, so kappa is NOT derived by any of them.")

b0, db = sp.symbols('beta0 db', positive=True)
Xb = (1 - (b0 + db) ** 2) / (1 - b0 ** 2)
print("\n3. baseline asymmetry beta0: X =", sp.series(Xb, db, 0, 3), "-> first-order term unless beta0 = 0")
print("   Cassini (|a| < 8e-6 on the fill-linear term, 4373) needs beta0 ~ 0: the ordinary-space round trip must be")
print("   symmetric, with all the asymmetry coming from the fill excess (= 4377's 'induced, not standing' condition).")
