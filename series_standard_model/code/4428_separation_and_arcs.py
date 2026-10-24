"""Patch 4428 -- founder: energy stored largely to the side, where separation is greatest and the arc-velocity differential most
rapid; forward the PSR shrinks by the Lorentz factor, with no DP-arc storage forward but some separation.

CPP mapping (4416: E fields orient/separate DPs; B fields speed the arcs): separation <-> electric field energy E^2/8 pi,
arcs <-> magnetic field energy B^2/8 pi. For a uniformly moving charge (census = Lienard-Wiechert, 4411, conditional),
at present distance r and angle t from the motion, relative to the rest field E0 = q/r^2:
   separation (E^2/E0^2) = (1 - v^2)^2 / (1 - v^2 sin^2 t)^3
   arcs       (B^2/E0^2) = v^2 sin^2 t * (1 - v^2)^2 / (1 - v^2 sin^2 t)^3      (B = v x E: zero along the axis)
Part 1: forward (t = 0) and side (t = 90 deg) values.
Part 2: totals outside the core contracted by 1/gamma along the motion (rest field energy U0 = 0.5): separation and arc shares.
"""
import numpy as np
from scipy.integrate import dblquad
print("Part 1 (energy density relative to rest at the same present distance):")
for v in (0.3, 0.6, 0.9):
    g = 1/np.sqrt(1 - v**2)
    sep_f, arc_f = (1 - v**2)**2, 0.0
    sep_s = (1 - v**2)**2/(1 - v**2)**3; arc_s = v**2*sep_s
    print(f"  v {v}: forward  separation x{sep_f:.4f} (= gamma^-4)  arcs x{arc_f:.1f}   |   side  separation x{sep_s:.4f} (= gamma^2)  arcs x{arc_s:.4f} (= v^2 gamma^2)")
U0 = 0.5
def totals(v):
    g = 1/np.sqrt(1 - v**2)
    def d(rp, t, which):
        x = rp*np.cos(t)/g; rho = rp*np.sin(t); r = np.hypot(x, rho); s2 = (rho/r)**2
        E2 = ((1 - v**2)/(r**2*(1 - v**2*s2)**1.5))**2
        val = E2 if which == 0 else v**2*s2*E2
        return val/(8*np.pi)*2*np.pi*rp**2*np.sin(t)/g
    Es = dblquad(lambda t, rp: d(rp, t, 0), 1, 400, 0, np.pi, epsabs=1e-10, epsrel=1e-8)[0]
    Ea = dblquad(lambda t, rp: d(rp, t, 1), 1, 400, 0, np.pi, epsabs=1e-10, epsrel=1e-8)[0]
    return Es, Ea
print("Part 2 (totals outside the contracted core; U0 = 0.5; cutoff costs ~0.25%):")
for v in (0.0, 0.3, 0.6, 0.9, 0.99):
    Es, Ea = totals(v); g = 1/np.sqrt(1 - v**2)
    print(f"  v {v:4.2f}: separation {Es:.4f}  arcs {Ea:.4f}  total {Es+Ea:.4f} (gamma U0 (1+v^2/3) = {g*U0*(1+v**2/3):.4f})  arc share {Ea/(Es+Ea):.3f}")
print("  arcs grow from nothing at rest toward half the stored energy as v -> 1 (electric and magnetic energies equalize);")
print("  both are concentrated to the side; forward there is only (reduced) separation and no arc energy.")
print("Part 3 (closed forms and the low-speed split):")
for v in (0.1, 0.3, 0.9):
    g = 1/np.sqrt(1 - v**2)
    UE, UB = g*U0*(1 - v**2/3), 2/3*g*U0*v**2
    print(f"  v {v}: separation gamma U0 (1 - v^2/3) = {UE:.4f}, arcs (2/3) gamma U0 v^2 = {UB:.4f};"
          f" arcs' share of the rise over rest = {UB/(UE + UB - U0):.3f}")
print("  low speed: total rises by (5/6) U0 v^2 (energy-based mass (5/3) U0); arcs take (2/3) U0 v^2 = 4/5 of it,")
print("  matching (1/2)(4/3 U0) v^2, the momentum-based mass; the 4/3 problem is (5/3) vs (4/3), i.e. gamma(1 + v^2/3) vs gamma.")
