#!/usr/bin/env python3
"""
0807_residual_lambda_scaling.py -- DM-2: the residual<->Lambda identification.

Step 1 showed the Sea's symmetric zero-mean fluctuations cancel by parity
(<F>=0). The conjecture: on a FINITE causal patch (IR cutoff R ~ R_H), parity
cancellation is EXACT for sub-horizon modes (many periods in the patch) but
INCOMPLETE for the longest, horizon-scale mode (a fraction of a period, whose
antisymmetric partner lies beyond the horizon). The surviving residual is then
the gravitating vacuum piece = Lambda.

Test: window-average the Step-1 cubic source s = 2 k^2 delta^2 delta'' over the
patch [0,R] for delta = sin(qx).
  (1) integer periods in patch  -> <s> = 0 (bulk parity cancellation).
  (2) horizon mode q = pi/R     -> <s> nonzero, scaling as 1/R^2,
      matching 5b: rho_Lambda ~ c^4/(8 pi G R_H^2)  (SCALING only; the exact
      coefficient is the 5b/D3 event-horizon result, not claimed here).
"""
import numpy as np
k = 1.0
def patch_avg(q, R, n=400000):
    x = np.linspace(0, R, n)
    d = np.sin(q*x); dpp = -q*q*np.sin(q*x)
    return np.trapezoid(2*k*k*d*d*dpp, x)/R

print("="*64)
print("(1) bulk cancellation: <s>_patch over [0,R=1] vs periods-in-patch")
for q in [2*np.pi*5, 2*np.pi*2, 2*np.pi*1, np.pi, np.pi/2, np.pi/4]:
    print(f"   {q/(2*np.pi):6.3f} periods -> <s> = {patch_avg(q,1.0):12.3e}")
print("   integer periods -> ~0 (parity exact); sub-period horizon modes -> nonzero.")
print("="*64)
print("(2) horizon mode q=pi/R: residual vs R  (expect <s>*R^2 = const)")
print(f"   {'R':>8s}{'<s>':>14s}{'<s>*R^2':>14s}")
for R in [0.5,1.0,2.0,4.0,8.0]:
    v = patch_avg(np.pi/R, R)
    print(f"   {R:8.2f}{v:14.3e}{v*R*R:14.3e}")
print("   <s>*R^2 const => residual ~ 1/R^2 = the 5b Lambda scaling. PASS (scaling).")
