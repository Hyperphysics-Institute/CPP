#!/usr/bin/env python3
"""4286 -- 4281's petal model, the orbit that route (H) actually describes, and g.
Same model as 4281 (series_standard_model/code/4281_petal_orbit_magnetic_moment.py): massless pole of charge q at speed c,
|p|c + V(r) = E = mc^2, L = |r x p| = hbar/2, mu = (q/2)<r x v>  =>  g = <E / E_kin(pole)>_time.
Units m = c = hbar = 1: lengths in r_ZBW = hbar/mc, energies in mc^2, frequencies in mc^2/hbar.
Route (H) (4266 (a), 4272 sec 1): swing amplitude r_ZBW = hbar/mc, angular frequency mc^2/hbar, speed c.
Schrodinger's triad / c04's r_th (4272 sec 1): amplitude hbar/2mc, frequency 2mc^2/hbar, speed c.
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
L=0.5; E=1.0

def orbit(V, dV, E=1.0, L=0.5, rmax=60):
    P=lambda r:E-V(r); f=lambda r:P(r)**2-L*L/(r*r)
    rs=np.linspace(1e-4,rmax,400001); s=np.sign(f(rs)); idx=np.where(np.diff(s)!=0)[0]
    if len(idx)<2: return None
    r1=brentq(f,rs[idx[0]],rs[idx[0]+1]); r2=brentq(f,rs[idx[1]],rs[idx[1]+1])
    pr=lambda r:np.sqrt(max(f(r),1e-300))
    # dt/dr = |p|/(c p_r) for H=|p|c+V  (speed c along p_hat); dphi/dr = L/(r^2 p_r)
    T  =quad(lambda r:P(r)/pr(r),r1,r2,limit=500)[0]
    I  =quad(lambda r:1/pr(r),r1,r2,limit=500)[0]                 # integral of dt * (1/|p|) ... -> <1/|p|>*T
    Phi=quad(lambda r:L/(r*r*pr(r)),r1,r2,limit=500)[0]
    rbar=quad(lambda r:r*P(r)/pr(r),r1,r2,limit=500)[0]/T
    ekin=quad(lambda r:P(r)*P(r)/pr(r),r1,r2,limit=500)[0]/T      # <|p|c>
    rVp =quad(lambda r:r*dV(r)*P(r)/pr(r),r1,r2,limit=500)[0]/T    # <r V'>
    return dict(g=E*I/T, r1=r1, r2=r2, rbar=rbar, omega=Phi/T, ekin=ekin, rVp=rVp)

print("(A) circular orbit of radius r at speed c, L = hbar/2, E = mc^2:  E_kin = cL/r,  g = E/E_kin = 2 r / r_ZBW (identity)")
for r,name in ((0.5,"c04's r_th = hbar/2mc (Schrodinger's triad)"),(1.0,"r_ZBW = hbar/mc (route H)")):
    ek=L/r; print(f"  r = {r:.2f} r_ZBW  [{name}]:  E_kin = {ek:.3f} mc^2  omega = c/r = {1/r:.3f} mc^2/hbar  g = {E/ek:.4f}")

print("\n(B) put each power-law well's circle AT r_ZBW (A n = 1/2, from circular equilibrium cL/r^2 = V'(1)):")
print("    then E_kin = 1/2 always, V(1) = A = 1/(2n), E = 1/2 + 1/(2n), and g = E/E_kin = 1 + 1/n.")
for n in (0.5,1.0,2.0,3.0):
    A=0.5/n; rc=(L/(A*n))**(1.0/(n+1)); ek=L/rc; Ec=ek+A*rc**n
    print(f"  n = {n:3.1f}: A = {A:.4f}  circle radius {rc:.4f} r_ZBW  E = {Ec:.4f} mc^2  g = {Ec/ek:.4f}"
          + ("   <- the only one whose energy is the rest energy mc^2" if abs(n-1)<1e-9 else ""))
print("    -> a circle at route (H)'s radius carries E = mc^2 only if the well is locally linear through V(0) = 0 there")
print("       (V(1) = V'(1) = 1/2); that is the same condition as g = 2.  Rest energy + route (H) radius => g = 2.")
print("\n(C) 4281's 'route (H) stiffness' k = 1 (V = k r^2/2, the massive oscillator's well at omega = mc^2/hbar), massless pole:")
o=orbit(lambda r:0.5*r*r, lambda r:r)
print(f"  petals r = {o['r1']:.3f} .. {o['r2']:.3f} r_ZBW, time-mean radius {o['rbar']:.3f}, mean angular rate {o['omega']:.3f} mc^2/hbar,  g = {o['g']:.4f}")
print(f"  virial check (massless, H = |p|c + V): <|p|c> = {o['ekin']:.4f}  <r V'> = {o['rVp']:.4f}")
print("  -> neither route (H)'s radius (1) nor its frequency (1): the orbit's mean radius is smaller and it circulates faster.")

print("\n(D) linear well V = s r (constant force), E = mc^2, L = hbar/2, s scanned; circle where s = 1/2:")
for s in (0.30,0.40,0.45,0.48,0.495,0.4999):
    o=orbit(lambda r,s=s:s*r, lambda r,s=s:s+0*r)
    if o is None: print(f"  s = {s:.4f}: no orbit"); continue
    print(f"  s = {s:.4f}: petals {o['r1']:.4f} .. {o['r2']:.4f}  mean r {o['rbar']:.4f}  omega {o['omega']:.4f}  "
          f"<E_kin> {o['ekin']:.4f} (virial <rV'> {o['rVp']:.4f})  g = {o['g']:.5f}")
print("  s = 0.5000: circle at r = 1.0000, omega = 1.0000, E_kin = 0.5000, g = 2.00000 (limit; A)")

print("\n(E) any well, general statement: on a circle g - 1 = V/(r V') (stored over kinetic); g = 2 <=> V = r V' at the orbit.")
print("    Petals: by Jensen, g = <E/E_kin> >= E/<E_kin>; with the massless virial <E_kin> = <r V'>, for V = A r^n:")
print("    g >= 1 + 1/n, equality on the circle.  Harmonic (n = 2): g >= 1.5;  linear (n = 1): g >= 2.")

print("\n(F) SPIN-1's own spin carrier (series_quantum_mechanics/spin_papers/SPIN-1_..., eqs force_balance, rout, L_total):")
print("    electron core -eCP at 0; captured DP: +eCP at r_in, -eCP at r_out = 2 r_in; each CP mass m_e; circular Coulomb")
print("    orbits, co-rotating; L = hbar/2 fixes r_in = a0/(4(1+sqrt2)^2).  Its magnetic moment, never computed in SPIN-1:")
hb=1.054571817e-34; me=9.1093837015e-31; ec=1.602176634e-19; ke=8.9875517923e9; cc=299792458.0
a0=hb**2/(me*ke*ec**2); rin=a0/(4*(1+np.sqrt(2))**2); rout=2*rin
win=np.sqrt(ke*ec**2/(me*rin**3)); wout=np.sqrt(ke*ec**2/(me*rout**3))
Ls=me*win*rin**2+me*wout*rout**2; muB=ec*hb/(2*me)
mi=+ec*win*rin**2/2; mo=-ec*wout*rout**2/2; mt=mi+mo; gs=abs(mt)/((ec/(2*me))*Ls)
print(f"  r_in = {rin:.4e} m = {rin/(hb/(me*cc)):.3f} r_ZBW;  w_in/w_out = {win/wout:.5f};  v_in/c = {win*rin/cc:.4f}, v_out/c = {wout*rout/cc:.4f}")
print(f"  L = {Ls/(hb/2):.6f} hbar/2")
print(f"  mu(+eCP, inner) = {mi/muB:+.5f} muB   mu(-eCP, outer) = {mo/muB:+.5f} muB   net = {mt/muB:+.5f} muB (antiparallel to L)")
print(f"  g = |mu| / ((e/2m) L) = {gs:.6f} = (sqrt2 - 1)^2 = 3 - 2 sqrt2 = {3-2*np.sqrt(2):.6f}  (constant-free, like SPIN-1's 2 sqrt2)")
print(f"  measured electron: g = 2.0023193, |mu| = 1.00116 muB  ->  SPIN-1's carrier gives {abs(mt)/muB/1.00115965:.4f} of it (1/{1.00115965*muB/abs(mt):.2f})")
print("  -> sign right (net -e at the outer radius dominates), size wrong by ~11.7x.  The neutral DP's two ends nearly cancel.")
