#!/usr/bin/env python3
"""4242 -- g_A's reduction R from the founder's motion: each quark's +qCP core breathes in and out against its
vertex of the bonding hTetra (State 1 away / State 2 superimposed) and hops between vertices on the colour force
(founders_voice/4242; phenomenon_su3_colour_and_quark_switching.md step 3).
A spin-1/2 core moving with momentum k, averaged over directions (the frame is isotropic relative to the spin
axis in the L = 0 ground state, 4134 Result 4):
   axial projection            R   = 1 - (2/3)(1 - m/E)  = 1/3 + (2/3) m/E
   spin magnetisation factor   S_M = 2/3 + (1/3) m/E     = (1 + R)/2      <- 4240's B2 estimate, now identified
The one-quark Dirac current adds a convection (orbital-current) term; computed below for the same state.
Inputs: m_const = m_p/3 (SS-2, assigned); SS-2 smearing <r^2> = r_ZBW^2 = (hbar c/m_const)^2 (the r_p formula)."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import spherical_jn as jn
hc=197.327; MN=938.919; muN=hc/(2*MN); mq=938.272/3; rz=hc/mq
gA_t, mup_t, mun_t = 1.2754, 2.79285, -1.91304
def pct(a,b): return 100*(a/b-1)
def avg_mE(sp, dim):
    w=(lambda k: k*k*np.exp(-k*k/(2*sp*sp))) if dim==3 else (lambda k: np.exp(-k*k/(2*sp*sp)))
    N=quad(w,0,12*sp)[0]; return quad(lambda k: w(k)*mq/np.hypot(k,mq),0,12*sp)[0]/N
def row(name, sp, dim):
    mE=avg_mE(sp,dim); R=1/3+2/3*mE; SM=2/3+mE/3
    print(f"  {name:44s} sigma_p={sp:6.1f} MeV  g_A={5/3*R:.4f} ({pct(5/3*R,gA_t):+5.1f}%)  "
          f"mu_p={3*SM:.3f} ({pct(3*SM,mup_t):+5.1f}%)  mu_n={-2*SM:.3f} ({pct(-2*SM,mun_t):+5.1f}%)")
    return R
print("="*100); print("1. Identity: (1+R)/2 = 2/3 + m/(3E) exactly -- 4240's B2 moment IS the spin magnetisation of a moving core"); print("="*100)
for mE in [1.0,0.8,0.6137,0.5]: print(f"  m/E={mE:.4f}: (1+R)/2 = {(1+1/3+2/3*mE)/2:.6f}   2/3+m/3E = {2/3+mE/3:.6f}")
print("\n"+"="*100); print("2. Spin-magnetisation-only moment (no orbital current from the core's motion), by reading of the SS-2 smearing"); print("="*100)
row("3D spread, <r^2> = r_ZBW^2", hc/(2*rz/np.sqrt(3)), 3)
row("1D breathing along one line, <x^2> = r_ZBW^2", hc/(2*rz), 1)
row("1D breathing, <x^2> = r_ZBW^2/3", hc/(2*rz/np.sqrt(3)), 1)
f=lambda sx: 1/3+2/3*avg_mE(hc/(2*sx),1)-gA_t*3/5
s1=brentq(f,0.01,2); print(f"  1D: g_A = 1.2754 needs sigma_x = {s1:.3f} fm = {s1/rz:.3f} r_ZBW (sigma_p = {hc/(2*s1):.0f} MeV = {hc/(2*s1)/mq:.2f} m_const)")
g=lambda r: 1/3+2/3*avg_mE(hc/(2*r/np.sqrt(3)),3)-gA_t*3/5
s3=brentq(g,0.1,3); print(f"  3D: g_A = 1.2754 needs <r^2>^1/2 = {s3:.3f} fm = {s3/rz:.3f} r_ZBW")
row("1D at that sigma_x", hc/(2*s1), 1); row("3D at that spread", hc/(2*s3/np.sqrt(3)), 3)
print("\n"+"="*100); print("3. The FULL one-quark Dirac current (spin + convection) for the 3D state -- what 4240 B1 actually excluded"); print("="*100)
mf=mq/hc; sx=rz/np.sqrt(3); spf=1/(2*sx)
k=np.linspace(1e-4,14*spf,3000); dk=k[1]-k[0]; phi=np.exp(-k*k/(4*spf*spf)); E=np.sqrt(k*k+mf*mf)
F=phi*np.sqrt((E+mf)/(2*E)); G=phi*k/np.sqrt(2*E*(E+mf))
r=np.linspace(1e-4,12*rz,3000); dr=r[1]-r[0]
fr=np.array([np.sum(F*jn(0,k*x)*k*k)*dk for x in r]); gr=np.array([np.sum(G*jn(1,k*x)*k*k)*dk for x in r])
Nf=np.sum(fr*fr*r*r)*dr; Ng=np.sum(gr*gr*r*r)*dr; N=Nf+Ng; RA=(Nf-Ng/3)/N; mu=(2/3)*np.sum(fr*gr*r**3)*dr/N/muN
print(f"  same state: g_A = {5/3*RA:.4f};  full-current mu_p = {mu:.3f} ({pct(mu,mup_t):+.1f}%)  vs spin-only {3*(2/3+avg_mE(hc/(2*sx),3)/3):.3f}")
print(f"  -> the one-quark current's p-wave convection term costs ~{3*(2/3+avg_mE(hc/(2*sx),3)/3)-mu:.2f} mu_N; it is present for ANY kappa=-1 spinor,")
print("     cavity or not. 4240's B1/B2 split is therefore NOT cavity vs sharing: it is 'convection current present' vs 'absent'.")
print("  -> the measured pair (g_A, mu_p) needs the motion that reduces the axial projection to carry NO orbital current.")
print("     A core breathing straight in and out against its vertex has no circulation about it -- the founder's motion is of that kind.")
