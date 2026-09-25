#!/usr/bin/env python3
"""4295 -- founders_voice/4295: rod -eCP(-d) ... +eCP shuttling ... -eCP(+d), rotating at w.  The +eCP moves at one PSR
per Moment (speed c), so its time is spread uniformly along its track [-L, L], L = d + s (s = overshoot beyond each -eCP).
Units: r_C = hbar/(m_e c), m_e, c, hbar = 1; k e^2 = alpha.  Equal inertia m = 1/3 per CP (4292 default, flagged)."""
import numpy as np
from scipy.optimize import brentq
alpha=1/137.035999
def K(sig):   # time-averaged net INWARD force on the right -eCP, in units k e^2/d^2, overshoot s = sig d
    L=1+sig; return (1/(2*L))*(1/sig-1/(2+sig)) - 0.25
print("(1) average pull of the shuttling +eCP on one pole: the near-field divergences cancel between passing inside and")
print("    outside; what remains is k e^2 [ (1/2L)(1/s - 1/(2d+s)) ] inward, minus the other pole's push k e^2/(2d)^2.")
d=1.0
for sig in (0.3,0.095,0.01):
    s=sig*d; L=d+s; x=np.linspace(-L,L,4_000_001); eps=1e-4
    dx=x-d; F=np.mean(dx/(dx*dx+eps*eps)**1.5)   # outward-positive, softened pass-through
    print(f"  s = {sig:5.3f} d: numeric (softened) inward {-F-0.25:8.3f}   formula {K(sig):8.3f}   vs a plain Coulomb pull at d: 1.000 (+ the push)")
print("  -> a small overshoot gives a pull ~ d/(2s) times the ordinary Coulomb pull at distance d.")
print("\n(2) spin share and g: f = <r_+^2>/(2 d^2 + <r_+^2>), <r_+^2> = L^2/3;  g = 3(1 - 2f)  (4292)")
for sig in (0.0,0.05,0.095445,0.2):
    r2=(1+sig)**2/3; f=r2/(2+r2); print(f"  s = {sig:.4f} d:  f = {f:.4f}  g = {3*(1-2*f):.4f}")
sg=np.sqrt(1.2)-1
print(f"  g = 2 at s = (sqrt(1.2) - 1) d = {sg:.4f} d  (overshoot 9.5%);  no overshoot gives g = 15/7 = {15/7:.4f}")
print("\n(3) the rod's size from force balance with S = hbar/2 = m w (2 d^2 + L^2/3), at the g = 2 overshoot:")
m=1/3; Q=2+(1+sg)**2/3; dd=0.25/(alpha*K(sg)*m*Q*Q); w=0.5/(m*dd*dd*Q)
print(f"  d = {dd:.3f} r_C (half-length), rod {2*dd:.2f} r_C;  poles at {w*dd:.4f} c")
print(f"  shuttle cycles per rotation = {(1/(4*(1+sg)*dd))/(w/(2*np.pi)):.1f};  pole kinetic energy {2*0.5*m*(w*dd)**2:.4f} m_e c^2;"
      f"  Coulomb energy ~ {alpha/dd:.4f} m_e c^2  (small: m_e = 3m holds to < 1%)")
print("  with no overshoot allowance but the same force law, plain Coulomb at distance d (K = 0.75) would balance at")
print(f"  d = {0.25/(alpha*0.75*m*(7/3)**2):.1f} r_C: a symmetric rod needs far less than 4294's dumbbell (154 r_C).")
print("\n(4) with the turnaround at lattice scale (s ~ 1 PSR ~ 1.2e-35 m / 3.9e-13 m = 4e-23 r_C):")
s=4e-23
# balance with sig -> 0: K ~ 1/(2 sig);  alpha/(2 sig d^2) = 0.25/(m d^3 Q^2), Q = 7/3, sig = s/d -> alpha d/(2 s d^2)... solve d
f=lambda d: alpha*K(s/d)/d**2 - 0.25/(m*d**3*(2+(1+s/d)**2/3)**2)
dl=brentq(f,1e-30,1e3); wl=0.5/(m*dl*dl*(2+1/3))
print(f"  d = {dl:.2e} r_C, pole speed {wl*dl:.2e} c  -> far faster than light: an overshoot of one PSR binds far too hard.")
