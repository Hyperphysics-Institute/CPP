#!/usr/bin/env python3
"""4243 -- the breath's size CALCULATED from the founder's picture (founders_voice/4243):
the quark-vertex breath is the ZBW oscillation of opposite charges; the same oscillation runs sideways between
opposite-charge quarks; the modes follow the colour combinations. Mode rule used (proton): each quark has one radial
mode against its vertex; sideways modes only along edges to OPPOSITE-charge quarks -> u: radial + 1 (u-d);
d: radial + 2 (d-u1, d-u2). u-u is same-sign: no sideways mode.
Frequency: c04 -- a ZBW cycle of mass m runs at the Compton frequency, omega = m c^2/hbar (4238: identical to 4231/4233).
Size, two independent calculations:
  (H) quantum ground state of each mode at omega (harmonic, the founders_vision 'dynamic stiffness' reading);
  (C) classical 1D fall-reset-return (4231) under -a hbar c/|x| from rest at A, A fixed by period = Compton period.
Axial per quark (4242): R = 1/3 + (2/3)<m/E>; g_A = (4/3) R_u + (1/3) R_d (the 4240 state); moment tie (4242):
spin magnetisation S = (1+R)/2 per quark, mu_u = (2/3)(M_N/m) S_u, mu_d = -(1/3)(M_N/m) S_d.
Inputs: m = m_const = m_p/3 (SS-2, assigned); alpha_geom = 1/sqrt5 (SS-2's value; SS-1 carries 0.559 -- not used)."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
hc=197.327; MN=938.919; m=938.272/3; rz=hc/m
gA_t,mup_t,mun_t=1.2754,2.79285,-1.91304
rng=np.random.default_rng(4243); N=2_000_000
Z=[rng.standard_normal(N) for _ in range(3)]
def R_modes(sig):
    k2=sum((s*Z[i])**2 for i,s in enumerate(sig)); return 1/3+2/3*np.mean(m/np.sqrt(k2+m*m))
def report(name,su,sd):
    Ru,Rd=R_modes(su),R_modes(sd); gA=4/3*Ru+1/3*Rd
    Su,Sd=(1+Ru)/2,(1+Rd)/2; mu_u,mu_d=(2/3)*(MN/m),-(1/3)*(MN/m)
    mp=(4*mu_u*Su-mu_d*Sd)/3; mn=(4*mu_d*Sd-mu_u*Su)/3
    print(f"  {name:52s} R_u={Ru:.4f} R_d={Rd:.4f}  g_A={gA:.4f} ({100*(gA/gA_t-1):+5.1f}%)  mu_p={mp:.3f} ({100*(mp/mup_t-1):+5.1f}%)  mu_n={mn:.3f} ({100*(mn/mun_t-1):+5.1f}%)")
    return gA
print("="*120); print("(H) harmonic ground state at the Compton frequency, founder's mode rule"); print("="*120)
fixed=m/np.sqrt(2)            # sigma_p for a mode whose partner is anchored (the frame vertex): sqrt(m hbar w/2) = m c/sqrt2
equal=m/2                     # relative mode of two equal masses (u-d), reduced mass m/2, same omega
print(f"  per-mode position spread, anchored partner: sigma_x = r_ZBW/sqrt2 = {rz/np.sqrt(2):.3f} fm; u quark (2 modes) <r^2> = r_ZBW^2 exactly -- SS-2's smearing, as a CHECK not an input")
report("radial anchored, sideways anchored",[fixed,fixed],[fixed,fixed,fixed])
report("radial anchored, sideways u-d both moving",[fixed,equal],[fixed,equal,equal])
f=brentq(lambda s: 4/3*R_modes([s*fixed,s*fixed])+1/3*R_modes([s*fixed]*3)-gA_t,1.0,4.0)
report(f"needed: every mode's sigma_p x {f:.3f}",[f*fixed]*2,[f*fixed]*3)
print(f"  -> the measured g_A needs each mode's momentum spread {100*(f-1):.0f}% above the Compton ground state (sigma_x {rz/np.sqrt(2)/f:.3f} fm per mode)")
print("\n"+"="*120); print("(C) classical fall-reset-return along one line, period = Compton period (4231 mechanism, c04 frequency)"); print("="*120)
def gam(x,A,a): return 1+a*(1/x-1/A)
def per(A,a,w=lambda g:1.0):
    f=lambda th: 2*A*np.sin(th)*np.cos(th)/np.sqrt(1-1/gam(A*np.sin(th)**2,A,a)**2)*w(gam(A*np.sin(th)**2,A,a))
    return 2*quad(f,1e-9,np.pi/2,limit=400)[0]
for a,name in [((2/3)/np.sqrt(5),"(2/3) alpha_geom  (SS-2 qq colour coefficient)"),(1/np.sqrt(5),"alpha_geom"),((4/3)/np.sqrt(5),"(4/3) alpha_geom")]:
    A=brentq(lambda A: per(A,a)-2*np.pi,1e-3,50); mE=per(A,a,lambda g:1/g)/per(A,a); R=1/3+2/3*mE
    print(f"  a = {name:46s} ({a:.3f}): amplitude A = {A:.3f} r_ZBW = {A*rz:.3f} fm  vs u-d edge 0.620 fm;  one line: g_A = {5/3*R:.4f} ({100*(5/3*R/gA_t-1):+.1f}%)")
print("  -> a single-line Coulomb breath with the ZBW period is as large as the frame (0.78-0.94 fm > 0.62 fm) and still gives g_A 1.43-1.50.")
print("\n"+"="*120); print("(T) the 4242 tie inverted, one R for u and d: measured g_A and mu_p together fix m_q"); print("="*120)
R=gA_t*3/5; S=(1+R)/2; x=mup_t/S
print(f"  R={R:.4f}, S={S:.4f}; M_N/m_q={x:.4f} -> m_q={MN/x:.1f} MeV (m_p/3 = {m:.1f}); then mu_n={-(2/3)*x*S:.3f} vs -1.913 ({100*(-(2/3)*x*S/mun_t-1):+.1f}%)")
print("\n"+"="*120); print("(Q) sensitivity to the mode rule: sideways along u-u too (colour attraction, SS-2's (2/3) alpha_geom term), all three quarks 3 modes"); print("="*120)
report("u-u included, all anchored",[fixed]*3,[fixed]*3)
report("u-u included, sideways both moving",[fixed,equal,equal],[fixed,equal,equal])
