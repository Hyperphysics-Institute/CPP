#!/usr/bin/env python3
"""4281 -- do the founder's petal loops give the observed magnetic moment?  (founders_voice/4281)
Minimal classical model: the orbital eDP's -eCP pole is a massless point charge q (CPs carry no rest mass; its inertia
is its kinetic energy, SF-6's arc store), moving at c, in a central well V(r) >= 0 with V(0) = 0 at superposition.
Total energy = the particle's rest energy (c04: mass = oscillation energy, KE + PE):  |p| c + V(r) = m c^2.
Angular momentum L = r x p is conserved (central force) and set to hbar/2 (spin carrier).  The orbit is a rosette
(the petal loops) between two turning radii.
Moment: mu = (q/2) <r x v>, v = c p_hat, and |r x p_hat| = L/|p|  =>  mu = (q c/2) L <1/|p|>_time.
Writing mu = g (q/2m) L:   g = m c^2 <1/|p| c>_time = <E_total / E_kin(pole)>_time.
Units m = c = hbar = 1 (length r_ZBW = hbar/mc).  Harmonic well V = k r^2/2; route (H)'s stiffness is k = 1."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
def orbit(V,E=1.0,L=0.5,rmax=60):
    P=lambda r:E-V(r); f=lambda r:P(r)**2-L*L/(r*r)
    rs=np.linspace(1e-4,rmax,400001); idx=np.where(np.diff(np.sign(f(rs)))!=0)[0]
    if len(idx)<2: return None
    r1=brentq(f,rs[idx[0]],rs[idx[0]+1]); r2=brentq(f,rs[idx[1]],rs[idx[1]+1]); pr=lambda r:np.sqrt(max(f(r),1e-300))
    T=quad(lambda r:P(r)/pr(r),r1,r2,limit=500)[0]; I=quad(lambda r:1/pr(r),r1,r2,limit=500)[0]
    return I/T,r1,r2
print("no well (V = 0): circle of radius L/(mc) = hbar/2mc -- c04's r_th -- at speed c:  g = 1 exactly")
print("harmonic well V = k r^2/2, E = mc^2, L = hbar/2:")
for k in (0.02,0.1,0.25,0.5,0.75,1.0,1.1,1.15,1.2):
    o=orbit(lambda r,k=k:0.5*k*r*r)
    tag="  <- route (H) stiffness" if k==1.0 else ""
    print(f"  k = {k:5.2f}: " + ("no orbit with L = hbar/2 at this energy" if o is None else f"g = {o[0]:.3f}   petals between r = {o[1]:.3f} and {o[2]:.3f} r_ZBW{tag}"))
k2=brentq(lambda k:orbit(lambda r:0.5*k*r*r)[0]-2.0,0.05,0.5,xtol=1e-4); o=orbit(lambda r:0.5*k2*r*r)
print(f"  g = 2 (Dirac) at k = {k2:.3f}: petals between r = {o[1]:.3f} and {o[2]:.3f} r_ZBW")
print("\n-> Petal loops give a moment along the spin, of the right size range: g = <E_total/E_kin(pole)>, from 1 for a free")
print("   circle upward as more of the rest energy is stored in the well.  Route (H)'s stiffness (k = 1) gives g = 1.54;")
print(f"   Dirac's g = 2 needs a well ~{1/k2:.0f}x softer (k = {k2:.3f}), whose petals reach out to ~{o[2]:.1f} r_ZBW.")
