#!/usr/bin/env python3
"""3060_fcli1_confrontation.py — F-CLI-1: the three-way confrontation
with current expansion data (Patch 3060).

COEFFICIENT MAPPING (correcting the 3058 C4 conflation ON THE RECORD):
Li convention: rho_L = 3 c_Li^2 c^4 / (8 pi G L^2). The arc's derived
chain: rho_L = (1/8pi) rho_P (l_P/L)^2 = c^4/(8 pi G L^2)  [using
l_P^2 = hbar G/c^3]. Equating: 3 c_Li^2 = 1  =>  c_Li = 1/sqrt(3).
The 3058 C4 statement "L = R_h => c_Li = 1" CONFLATED the geometric
scale statement (L = R_h, which stands) with the energy coefficient
(which the Step-C derivation fixes at 1/8pi => c_Li = 0.5774). The
scale freedom is gone (the clique theorem); the entire remaining
freedom is the mode-counting coefficient — now confronted.

HDE relations (Li 2004), flat, Omega_L today = 0.685:
  w(x)   = -1/3 - (2/3) sqrt(Om)/c
  dOm/dx = Om (1-Om) (1 + 2 sqrt(Om)/c),  x = ln a
  CPL: w(a) = w0 + wa (1-a);  wa = -dw/da|_1 = -dw/dx|_0.
"""
import numpy as np
OM_L = 0.685

def hde_point(c):
    s = np.sqrt(OM_L)
    w0 = -1/3 - (2/3) * s / c
    dOm = OM_L * (1 - OM_L) * (1 + 2 * s / c)
    dw = -(1 / (3 * c)) * dOm / s
    return w0, -dw

# The triangle
pts = {
  'derived chain (1/8pi + L=R_h): c=1/sqrt3': hde_point(1/np.sqrt(3)),
  'Step-D fitted: c=0.80':                    hde_point(0.80),
  'founder rebound (naive de Sitter)':        (-1.0, 0.0),
}
# Current data (DESI DR2 + CMB + PantheonPlus; arXiv:2503.14738 era)
W0, SW0, WA, SWA = -0.838, 0.055, -0.62, 0.205
# BAO+CMB-alone endpoint (-0.42, -1.75) defines the degeneracy direction
slope = (-1.75 - WA) / (-0.42 - W0)     # dwa/dw0 along the contour axis

print(f"data: DESI DR2+CMB+SNe (w0,wa) = ({W0}±{SW0}, {WA}+0.22/-0.19); "
      f"degeneracy slope ≈ {slope:.2f}; evolving-DE preference >3σ "
      f"(robustness contested, arXiv:2504.15222)")
for name, (w0, wa) in pts.items():
    dz0 = (w0 - W0) / SW0
    dza = (wa - WA) / SWA
    wa_line = WA + slope * (w0 - W0)     # contour-axis wa at this w0
    off = wa - wa_line
    print(f"  {name:44s} (w0,wa)=({w0:+.3f},{wa:+.3f})  "
          f"marginal: {abs(dz0):.1f}σ/{abs(dza):.1f}σ  "
          f"off-degeneracy Δwa={off:+.2f}")
print()
print("Factor the data demand of the mode-counting (to move the derived")
print("chain onto the fitted point): rho ratio = (0.80/0.5774)^2 =",
      f"{(0.80/np.sqrt(1/3))**2:.2f}", "≈ 2 — the June '~2x' gap,")
print("now localized ENTIRELY in one derivable coefficient (scale freedom")
print("eliminated by the clique theorem). Deriving it post hoc from the")
print("data is FORBIDDEN; it must come from the construction's own mode")
print("structure or F-CLI-1 stands FIRED against the naive counting.")
