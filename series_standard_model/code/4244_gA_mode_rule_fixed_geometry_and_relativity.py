#!/usr/bin/env python3
"""4244 -- g_A under the founder's mode rule, now FIXED (founders_voice/4244: the two u's do not breathe sideways
against each other -- same charge, they repel). Closes two of 4243's critic items:
 (G) real frame geometry instead of orthogonal modes: SS-2 u-u 1.071, u-d 0.620 fm (the triangle of 4134 C3);
     the radial direction is not specified, so it is scanned from the plane normal into the plane;
 (K) relativistic kinematics per mode: ground state of sqrt(p^2+m^2) + (1/2) M w^2 x^2 (spinless Salpeter, solved in
     momentum space) instead of the nonrelativistic Gaussian; w = Compton frequency of m (c04).
Sideways u-d mode: two equal masses, relative coordinate, reduced mass m/2, each quark carries the relative momentum.
Axial R = 1/3 + (2/3)<m/E>; g_A = (4/3)R_u + (1/3)R_d; moment tie S = (1+R)/2 (4242), m_q = m_p/3 (SS-2)."""
import numpy as np
from scipy.linalg import eigh_tridiagonal
MN=938.919; x=MN/(938.272/3); gA_t,mup_t,mun_t=1.2754,2.79285,-1.91304
rng=np.random.default_rng(4244); N=1_500_000
def ground(kin,Mpot):   # units m = c = hbar = w = 1
    p=np.linspace(-14,14,7000); dp=p[1]-p[0]; a=0.5*Mpot
    E,V=eigh_tridiagonal(kin(p)+2*a/dp**2,-a/dp**2*np.ones(len(p)-1),select='i',select_range=(0,0))
    P=V[:,0]**2; return p,P/P.sum()
MODES={'NR anchored':ground(lambda p:p*p/2,1.0),'REL anchored':ground(lambda p:np.sqrt(p*p+1)-1,1.0),
       'NR u-d':ground(lambda p:p*p,0.5),'REL u-d':ground(lambda p:2*(np.sqrt(p*p+1)-1),0.5)}
print("per-mode ground-state spreads (units m_const c):")
for k,(p,P) in MODES.items(): print(f"  {k:13s} sigma_p = {np.sqrt((P*p*p).sum()):.4f}")
duu,dud=1.071,0.620; h=np.sqrt(dud**2-(duu/2)**2)
u1=np.array([-duu/2,0,0]); d=np.array([0,h,0]); u2=np.array([duu/2,0,0])
e=lambda a,b:(b-a)/np.linalg.norm(b-a)
print(f"\nframe: the d's two edge lines meet at {np.degrees(np.arccos(abs(e(d,u1)@e(d,u2)))):.1f} deg (4243 assumed 90)")
def draw(mode): p,P=MODES[mode]; return rng.choice(p,size=N,p=P)
def R(dirs,modes):
    k=sum(draw(mo)[:,None]*np.asarray(v)[None,:] for v,mo in zip(dirs,modes)); k2=(k**2).sum(1)
    return 1/3+2/3*np.mean(1/np.sqrt(k2+1))
def row(lab,kin,side,tilt):
    t=np.radians(tilt); rad=np.array([0,np.sin(t),np.cos(t)])
    Ru=R([rad,e(u1,d)],[f'{kin} anchored',f'{kin} {side}']); Rd=R([rad,e(d,u1),e(d,u2)],[f'{kin} anchored']+[f'{kin} {side}']*2)
    gA=4/3*Ru+1/3*Rd; Su,Sd=(1+Ru)/2,(1+Rd)/2
    mp=(4*(2/3)*x*Su+(1/3)*x*Sd)/3; mn=(4*(-1/3)*x*Sd-(2/3)*x*Su)/3
    print(f"  {lab:44s} R_u={Ru:.4f} R_d={Rd:.4f}  g_A={gA:.4f} ({100*(gA/gA_t-1):+5.1f}%)  mu_p={mp:.3f} ({100*(mp/mup_t-1):+5.1f}%)  mu_n={mn:.3f} ({100*(mn/mun_t-1):+5.1f}%)")
print("\n(G) geometry: radial direction tilted from the plane normal (NR modes)")
for side in ['anchored','u-d']:
    for tilt in [0,45,90]: row(f"NR, sideways {side:8s}, radial tilt {tilt:2d} deg",'NR',side,tilt)
print("\n(K) relativistic mode kinematics, real geometry (radial along the plane normal; tilt moves g_A by < 0.01)")
for side in ['anchored','u-d']: row(f"REL, sideways {side}",'REL',side,0)
print("\n-> geometry: <= 0.8%.  relativity: -2.5%.  Direct reading of the founder's words (sideways = between two quarks, both")
print("   move; relativistic): g_A = 1.406 (+10.2%).  Anchored partner (lower bound): 1.348 (+5.7%).  SU(6) alone: 1.667.")
