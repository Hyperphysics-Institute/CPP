#!/usr/bin/env python3
"""
OPEN-SR-9 / R2: does Z0 = sqrt(mu0/eps0) carry the DP-Sea stiffness C, or is it geometric?

Thomas's mechanism (made decidable): the field is the response of ONE DP whose CENTER is pinned
to its GP (Brick #2); only the internal poles move, under the ONE intra-DP Coulomb binding.
  - E  = RADIAL pole displacement (polarization)         -> electric polarizability alpha_E
  - B  = TANGENTIAL pole motion of the SAME poles          -> magnetic polarizability alpha_B
Both restored by the SAME Coulomb binding (stiffness C); the poles oscillate at the ZBW frequency
omega_0, which in CPP is FIXED by the Absolute Moment (c02): so the pole inertia m = C/omega_0^2.

We extract alpha_E (numerically, driven oscillator) and alpha_B (Larmor diamagnetic response of the
fixed-frequency ZBW orbit), form Z0 ~ sqrt(alpha_B/alpha_E) under the symmetric emergence scheme
(mu0 from alpha_B exactly as eps0 from alpha_E), and SWEEP C. We do NOT assume C cancels.

CIRCULARITY GUARD: we also run the COUNTERFACTUAL where omega_0 is NOT fixed (m fixed instead). If C
cancels in BOTH, the cancellation is by construction and worthless. If C cancels ONLY when omega_0 is
fixed, then the result is forced by a specific, falsifiable CPP input (the Absolute Moment) -- real.
"""
import numpy as np
from scipy.integrate import solve_ivp

q = 1.0; d = 1.0; omega0 = 1.0   # charge, ZBW orbit radius (geometric), fixed Absolute-Moment freq

def alpha_E_numeric(C, m):
    """Electric polarizability: drive 1D oscillator with weak static-ish E, measure dipole/E."""
    E0 = 1e-3; 
    # m x'' = -C x + q E0  ; steady displacement x_ss = qE0/C ; dipole p = q x_ss
    def rhs(t,y): x,v=y; return [v, (-C*x + q*E0)/m]
    # integrate to steady state with light damping to settle
    gamma = 0.5*np.sqrt(C*m)
    def rhsd(t,y): x,v=y; return [v, (-C*x - gamma*v + q*E0)/m]
    s=solve_ivp(rhsd,[0,200/omega0],[0,0],rtol=1e-9,atol=1e-12,dense_output=True)
    x_ss=s.y[0,-1]; p=q*x_ss
    return p/E0   # alpha_E

def alpha_B_larmor(C, m):
    """Magnetic polarizability: Larmor diamagnetic response of the ZBW orbit (textbook 1/m scaling).
       alpha_B = -q^2 <r_perp^2> / (4 m).  <r_perp^2> = d^2 (fixed geometric orbit). Sign = diamagnetic."""
    return -(q**2 * d**2)/(4.0*m)

def run(label, fix_omega0=True):
    print(f"\n[{label}]  {'omega0 FIXED (CPP: m=C/omega0^2)' if fix_omega0 else 'COUNTERFACTUAL: m FIXED, omega0=sqrt(C/m)'}")
    print(f"  {'C':>7} {'m':>9} {'alpha_E':>11} {'alpha_B':>12} {'aB/aE':>10} {'Z0~sqrt(aB/aE)':>15} {'c~1/sqrt(aE aB)':>16}")
    Z0s=[]; cs=[]
    for C in [0.5,1.0,2.0,4.0,8.0]:
        m = C/omega0**2 if fix_omega0 else 1.0
        aE = alpha_E_numeric(C,m)
        aB = alpha_B_larmor(C,m)
        ratio = abs(aB)/aE
        Z0 = np.sqrt(ratio)                 # symmetric scheme: Z0=sqrt(mu0/eps0)=sqrt(alpha_B/alpha_E)
        c  = 1.0/np.sqrt(aE*abs(aB))         # c^2 = 1/(mu0 eps0) ~ 1/(alpha_E alpha_B)
        Z0s.append(Z0); cs.append(c)
        print(f"  {C:>7.2f} {m:>9.4f} {aE:>11.5f} {aB:>12.5f} {ratio:>10.5f} {Z0:>15.6f} {c:>16.5f}")
    Z0s=np.array(Z0s); cs=np.array(cs)
    print(f"  -> Z0 spread over 16x C: {(Z0s.max()-Z0s.min())/Z0s.mean():.2e}   "
          f"c spread: {(cs.max()-cs.min())/cs.mean():.2e}")
    return Z0s, cs

print("="*92); print("OPEN-SR-9 / R2: Z0 C-dependence from the single-DP radial(E) vs tangential(B) response")
print("="*92)
Z0_cpp, c_cpp = run("CPP", fix_omega0=True)
Z0_cf,  c_cf  = run("counterfactual", fix_omega0=False)

print("\n"+"="*92); print("VERDICT:")
flat = (Z0_cpp.max()-Z0_cpp.min())/Z0_cpp.mean() < 1e-6
cvar = (c_cpp.max()-c_cpp.min())/c_cpp.mean() > 0.5
cf_fail = (Z0_cf.max()-Z0_cf.min())/Z0_cf.mean() > 0.5
print(f"  CPP (omega0 fixed):  Z0 geometric? {flat}   c varies with C (VSL)? {cvar}")
print(f"  counterfactual (m fixed): Z0 carries C? {cf_fail}  (if so, the CPP cancellation is NOT by construction)")
if flat and cvar and cf_fail:
    print("  => PASS-pointing: Z0 is C-independent (alpha fixed) BECAUSE alpha_B ~ 1/m ~ 1/C via the")
    print("     FIXED Absolute-Moment omega_0, matching alpha_E ~ 1/C; meanwhile c ~ C varies (VSL lives).")
    print("     The counterfactual FAILS, so this is forced by a specific CPP input, not by construction.")
