#!/usr/bin/env python3
"""4297 -- the +eCP shuttle of 4296 (fixed poles at +-d, k e^2 = m = d = 1 scaled): its closed-loop action in units of hbar
(physical scale sqrt(m alpha d), m = m_e/3, d from 4296 rows B), and where along the track it is fastest."""
import numpy as np, warnings
from scipy.integrate import quad
from scipy.optimize import brentq
warnings.filterwarnings("ignore")
alpha=1/137.035999; m=1/3
def turn(e): return brentq(lambda s: 1/s+1/(2+s)-e,1e-12,1e6)
for delta,d in ((1e-3,42.09),(7.37e-5,38.56)):
    e=2-delta; X=1+turn(e); v=lambda x: np.sqrt(max(2*(-e+1/abs(x-1)+1/abs(x+1)),0))
    Js=4*(quad(v,0,1,limit=500)[0]+quad(v,1,X,limit=500)[0])       # scaled closed-loop action  (k e^2 = m = d = 1)
    J=Js*np.sqrt(m*alpha*d)                                          # physical, in units of hbar
    print(f"delta {delta:.2e}: shuttle action per cycle = {J:.4f} hbar = {J/(2*np.pi):.4f} h")
# where is the +eCP fastest?  speed at centre vs near a pole (x = 1 +- 0.05)
e=2-7.37e-5; sp=lambda x: np.sqrt(max(2*(-e+1/abs(x-1)+1/abs(x+1)),0))
print(f"speed at centre {sp(0.0):.4f}, at 0.95 d {sp(0.95):.3f}, at 1.05 d {sp(1.05):.3f}, at the turning point {sp(1+turn(e)):.4f}  (scaled units)")
