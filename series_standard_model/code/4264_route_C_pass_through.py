#!/usr/bin/env python3
"""4264 -- 4243 route (C) re-run under the founder's pass-through ZBW (founders_voice/4264, proposal pending ruling).
4243 (C) modelled the classical breath as fall-reset-return (4231; R-ARC-CANCEL-TURNAROUND, 3134): the quark falls
from rest at A to superposition, stops, and returns on the SAME side -- one period = 2 x fall time.
Pass-through: the quark crosses the vertex at full speed and turns on the FAR side -- one period = 4 x fall time.
Idealisation: the far side is taken symmetric (-a/|x|); the founder's far side is the hTetra interior (vertex
attraction behind, like-charge vertices ahead), which only makes that half-turn sooner.  Period = Compton period
(c04), couplings as 4243 (SS-2 colour coefficients); one line; R = 1/3 + (2/3)<1/gamma> time-averaged; g_A = (5/3)R."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
rz=197.327/(938.272/3); gA_t=1.2754
def gam(x,A,a): return 1+a*(1/x-1/A)
def per(A,a,w=lambda g:1.0):   # 2 x fall time from rest at A to 0, time-weighted by w
    f=lambda th: 2*A*np.sin(th)*np.cos(th)/np.sqrt(1-1/gam(A*np.sin(th)**2,A,a)**2)*w(gam(A*np.sin(th)**2,A,a))
    return 2*quad(f,1e-9,np.pi/2,limit=400)[0]
print("Compton period = 2 pi (units hbar/m_const c^2).  u-d edge = 0.620 fm.\n")
for a,name in [((2/3)/np.sqrt(5),"(2/3) alpha_geom"),(1/np.sqrt(5),"alpha_geom"),((4/3)/np.sqrt(5),"(4/3) alpha_geom")]:
    for lab,T in (("reset, 2 falls/period (4243 C)",2*np.pi),("pass-through, 4 falls/period",np.pi)):
        A=brentq(lambda A: per(A,a)-T,1e-4,50); R=1/3+2/3*per(A,a,lambda g:1/g)/per(A,a)
        print(f"  a = {name:17s} ({a:.3f})  {lab:32s} amplitude {A*rz:.3f} fm  {'inside' if A*rz<0.620 else 'OUTSIDE'} the frame;  one line g_A = {5/3*R:.4f} ({100*(5/3*R/gA_t-1):+5.1f}%)")
print("\n-> Pass-through halves the fall time at a fixed period, so the amplitude shrinks to ~0.6 of its value (2^(-2/3) non-relativistically): the")
print("   classical breath now fits inside the frame (0.47-0.56 fm), removing the reason 4243 rejected route (C), and")
print("   its one-line g_A drops to 1.34-1.43.")
