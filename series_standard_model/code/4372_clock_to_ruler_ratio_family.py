#!/usr/bin/env python3
"""Patch 4372 - where Einstein's black hole lives in the corpus: the ratio of clock to ruler.

GR-1c's self-consistency (the lapse N is harmonic in the effective geometry; static vacuum R_00 = 0,
conformally flat rulers g_ij = A delta) gives, for a spherical body,
    d/dr ( r^2 sqrt(A) dN/dr ) = 0   =>   r^2 sqrt(A) N' = m.
The census rho = k Delta / 2 = m/(2r) is flat-harmonic (GR-1j).  Write the clock-to-ruler ratio
    N * sqrt(A) = (1 - rho^2)^lam
  lam = 0 : clocks and rulers shrink together (one PSR, founder 4362)  ->  N = exp(-2 rho) = e^{-eps}
  lam = 1 : clocks slow by an extra (1 - rho^2)                         ->  N = (1-rho)/(1+rho), A = (1+rho)^4:
            GR-1c's boxed theorem (exact isotropic Schwarzschild) and its Form A, N = -2 artanh(k Delta/2).
Then ln N = -2 * Integral_0^rho dx / (1 - x^2)^lam.
For lam in [0, 1]: photon sphere, shadow, eikonal ringdown frequency and damping vs Schwarzschild, and the
lam needed to bring the frequency inside GW250114's +-2.4% box (eikonal, non-spinning).
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize_scalar, brentq
print(__doc__)

def lnN(rho, lam):
    return -2 * quad(lambda x: (1 - x * x) ** (-lam), 0, rho)[0]

def metric(r, lam, m=1.0):
    rho = m / (2 * r)
    N = np.exp(lnN(rho, lam))
    sqrtA = (1 - rho * rho) ** lam / N
    return N, sqrtA

def b_of_r(r, lam):                       # impact parameter of a circular photon orbit: areal / lapse
    N, sA = metric(r, lam)
    return r * sA / N

def ring(lam):
    lo = 0.5 + 1e-6 if lam > 0 else 0.3   # rho < 1 required for lam > 0
    # photon sphere = extremum of b(r) (minimum of b over r outside the throat)
    res = minimize_scalar(lambda r: b_of_r(r, lam), bounds=(max(lo, 0.55), 10), method='bounded')
    rp = res.x; bc = res.fun
    # Lyapunov exponent: lambda_L^2 = -(A_t/A_r) V''/(2V), V = N^2/C, C = areal^2, A_t = N^2, A_r = A
    h = 1e-4
    def V(r):
        N, sA = metric(r, lam); return N * N / (r * sA) ** 2
    Vpp = (V(rp + h) - 2 * V(rp) + V(rp - h)) / h ** 2
    N, sA = metric(rp, lam)
    lyap = np.sqrt(-(N * N / sA ** 2) * Vpp / (2 * V(rp)))
    areal = rp * sA
    return areal, bc, lyap

b_gr, ly_gr = 3 * np.sqrt(3), 1 / (3 * np.sqrt(3))
print("check lam = 1 reproduces Schwarzschild:", [round(float(v), 6) for v in ring(1.0)], " (3, 5.196152, 0.19245)")
print("check lam = 0 reproduces the exponential (4365/4369):", [round(float(v), 5) for v in ring(0.0)], " (3.2974, 5.4366, 0.18394)")
print("\n   lam    photon sphere   shadow vs GR   ringdown freq vs GR   damping vs GR")
for lam in (0.0, 0.25, 0.5, 0.75, 1.0):
    a, bc, ly = ring(lam)
    print(f"   {lam:4.2f}      {a:6.4f} m      {100*(bc/b_gr-1):+6.2f}%          {100*(b_gr/bc-1):+6.2f}%            {100*(ly/ly_gr-1):+6.2f}%")
lam_box = brentq(lambda L: (b_gr / ring(L)[1] - 1) + 0.024, 0.0, 1.0)
print(f"\n   frequency inside GW250114's -2.4% edge needs lam >= {lam_box:.2f}"
      " (eikonal, non-spinning; indicative only)")
rho_ph = 1 / (2 * 1.866)
print(f"   size of the extra clock factor at Einstein's photon sphere: 1 - rho^2 = {1 - rho_ph**2:.4f}"
      f" (clocks slow {100*rho_ph**2:.1f}% more than rulers shrink); weak field: rho^2 ~ U^2/4, unobservable")

# weak field: lam leaves first and second order untouched; it enters at third order in the lapse
import sympy as sp
x, rho, L, e = sp.symbols('x rho lam epsilon', positive=True)
lnN_ser = sp.series(-2 * sp.integrate(sp.series((1 - x**2) ** (-L), x, 0, 4).removeO(), (x, 0, rho)), rho, 0, 4).removeO()
N_eps = sp.expand(sp.series(sp.exp(lnN_ser.subs(rho, e / 2)), e, 0, 4).removeO())
print("\n   N(eps) =", N_eps, "-> eps^2 coefficient 1/2 for every lam (Mercury);",
      "third order -1/6 - lam/12 (lam = 1: -1/4)")
print("   background residual in local G: 1 + (lam/4) eps0^2 (4365 sec 4); unobservable for G, alpha per TODO-4364-EPSABS")
