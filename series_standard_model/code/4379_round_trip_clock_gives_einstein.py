#!/usr/bin/env python3
"""Patch 4379 - a round-trip clock in the founder's two-sided field gives Einstein's factor exactly.

The corpus's ZBW clock is a radial round trip (c04 development notes L1475-1490: a wave runs out through the
polarisation cloud, reflects at its edge, returns; the round-trip time sets the frequency).  In the founder's
two-sided field (4377: opposite charges drawn in, like pushed out) one leg is helped and the other hindered.
If each leg's rate is modulated by +- kappa*rho (rho = k Delta / 2):
    round-trip time  T = L/(1 + kappa rho) + L/(1 - kappa rho) = 2L / (1 - kappa^2 rho^2)
    clock factor     X = 1 - kappa^2 rho^2                (first order cancels EXACTLY: upstream/downstream)
kappa = 1 gives X = 1 - rho^2: Einstein's factor, to ALL orders (GR-1c's artanh Form A, exact Schwarzschild).
Self-consistency (4372): ln N = -2 Int_0^rho dx / X(x) = -(2/kappa) artanh(kappa rho).
Then: the photon sphere, shadow and eikonal ringdown vs Schwarzschild as functions of kappa, and the kappa the
GW250114 box needs.
"""
import numpy as np
import sympy as sp
from scipy.optimize import minimize_scalar, brentq
print(__doc__)

rho, kap, L = sp.symbols('rho kappa L', positive=True)
T = L / (1 + kap * rho) + L / (1 - kap * rho)
X = sp.simplify(2 * L / T)
print("round trip: X =", X, "; series:", sp.series(X, rho, 0, 5))

def lnN(r, k):
    x = 1 / (2 * r)
    return -2 * x if k == 0 else -(2 / k) * np.arctanh(k * x)

def metric(r, k):
    x = 1 / (2 * r)
    N = np.exp(lnN(r, k))
    sA = (1 - k * k * x * x) / N
    return N, sA

def ring(k):
    lo = max(0.55, 0.5 * k + 1e-3)
    res = minimize_scalar(lambda r: r * metric(r, k)[1] / metric(r, k)[0], bounds=(lo, 10), method='bounded')
    rp, bc = res.x, res.fun
    h = 1e-4
    V = lambda r: metric(r, k)[0] ** 2 / (r * metric(r, k)[1]) ** 2
    Vpp = (V(rp + h) - 2 * V(rp) + V(rp - h)) / h ** 2
    N, sA = metric(rp, k)
    lyap = np.sqrt(-(N * N / sA ** 2) * Vpp / (2 * V(rp)))
    return rp * sA, bc, lyap

bgr, lgr = 3 * np.sqrt(3), 1 / (3 * np.sqrt(3))
print("\n   kappa   photon sphere   shadow vs GR   ringdown freq vs GR   damping vs GR")
for k in (0.0, 0.5, 0.7, 0.85, 1.0):
    a, bc, ly = ring(k)
    print(f"   {k:4.2f}      {a:6.4f} m      {100*(bc/bgr-1):+6.2f}%          {100*(bgr/bc-1):+6.2f}%            {100*(ly/lgr-1):+6.2f}%")
kbox = brentq(lambda k: (bgr / ring(k)[1] - 1) + 0.024, 0.0, 1.0)
print(f"\n   kappa = 0 is the one-PSR (exponential) exterior; kappa = 1 is exact Schwarzschild.")
print(f"   GW250114's -2.4% edge (eikonal, non-spinning) needs kappa >= {kbox:.2f}.")
print("   Weak field: X = 1 - kappa^2 rho^2 enters at second order in the stress: Mercury and Cassini untouched (4373, 4378).")
