#!/usr/bin/env python3
"""Patch 4376 - does spin move the ringdown shift?  A first look, and why it is not yet decidable.

Equatorial ds^2 = -N^2 dt^2 + A dr^2 + R^2 (dphi - w dt)^2 (isotropic r, R areal), J = chi m^2, m = 1.
Prograde circular photon orbit: Omega = w + N/R with -N' + R' N/R - R w' = 0 (outermost root).
Eikonal l = m = 2 frequency: 2 Omega.  The exponential (lam = 0) exterior is compared with EXACT Kerr.
All three frame-dragging profiles below have the same far-field Lense-Thirring tail (GR-1b) and differ only
in the near zone, which no rotating CPP field equation yet fixes (4376 critic):
  A: w = 2J/R^3                                   (areal Lense-Thirring)
  B: w = 2J/(r_iso R^2), i.e. g_tphi = -2J/r_iso   (the isotropic weak-field form)
  C: dw/dr = -6 J N sqrt(A) / R^4                  (GR's t-phi operator on the background; = A for Schwarzschild)
Limits: first order in J at chi up to 0.68; eikonal; real part only.
"""
import numpy as np
from scipy.integrate import quad
print(__doc__)

def schw(r):
    rho = 1 / (2 * r); return (1 - rho) / (1 + rho), r * (1 + rho) ** 2, (1 + rho) ** 2
def expo(r):
    return np.exp(-1 / r), r * np.exp(1 / r), np.exp(1 / r)

def wfun(metric, profile, J):
    if profile == "A":
        return lambda r: 2 * J / metric(r)[1] ** 3
    if profile == "B":
        return lambda r: 2 * J / (r * metric(r)[1] ** 2)
    def wC(r):
        f = lambda s: 6 * J * metric(s)[0] * metric(s)[2] / metric(s)[1] ** 4
        return quad(f, r, np.inf, limit=200)[0]
    return wC

def light_ring(metric, profile, chi, rmin):
    w = wfun(metric, profile, chi)
    h = 1e-5
    def cond(r):
        N, R, _ = metric(r)
        Np = (metric(r + h)[0] - metric(r - h)[0]) / (2 * h)
        Rp = (metric(r + h)[1] - metric(r - h)[1]) / (2 * h)
        wp = (w(r + h) - w(r - h)) / (2 * h)
        return -Np + Rp * N / R - R * wp
    grid = np.linspace(8, rmin, 1500)
    vals = [cond(x) for x in grid]
    for i in range(len(grid) - 1):
        if vals[i] * vals[i + 1] < 0:
            a, b = grid[i + 1], grid[i]
            for _ in range(60):
                c = 0.5 * (a + b)
                if cond(c) * cond(a) < 0: b = c
                else: a = c
            r0 = 0.5 * (a + b)
            N, R, _ = metric(r0)
            return r0, R, w(r0) + N / R
    return None

def kerr(chi):
    r = 2 * (1 + np.cos(2 / 3 * np.arccos(-chi)))
    return 2 / (r ** 1.5 + chi)

print("check: GR + LT (profile A) against exact Kerr, prograde 2*Omega")
for chi in (0.2, 0.4, 0.68):
    g = light_ring(schw, "A", chi, 0.55)
    print(f"   chi {chi:4.2f}: GR+LT {2*g[2]:.5f}  exact Kerr {kerr(chi):.5f}  ({100*(2*g[2]/kerr(chi)-1):+.2f}%)")
print("\n   profile  chi    exp light ring (iso r, areal)   exp 2*Omega   shift vs exact Kerr   note")
for prof in ("A", "C", "B"):
    for chi in (0.0, 0.2, 0.4, 0.68):
        e = light_ring(expo, prof, chi, 0.3)
        note = ""
        if e[0] < 1 / np.log(2): note = "inside the cap (iso 1.443)"
        if e[0] < 1.0: note = "inside the throat (iso 1.0)"
        print(f"      {prof}    {chi:4.2f}     {e[0]:6.3f}, {e[1]:6.3f}            {2*e[2]:7.5f}      {100*(2*e[2]/kerr(chi)-1):+7.2f}%      {note}")
print("\n   The sign of the spin trend depends on the near-zone frame dragging, which no rotating CPP exterior yet fixes.")
print("   Only the static result (4374: l = 2, -4.06%) stands as a number; the spin extension is indicative only.")
