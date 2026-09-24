#!/usr/bin/env python3
"""4272 -- a second observable for the breath's frequency: the proton charge radius.
Under R-ZBW-PASS-THROUGH the CP crosses its partner at its top speed; if that speed is c (the lattice limit),
omega x amplitude = c, so the frequency and the swing's size are one choice:
   amplitude r_ZBW = hbar/mc (SS-2's orbit radius)   <-> omega = mc^2/hbar  (route (H));
   amplitude r_th  = hbar/2mc (c04's resonance radius) <-> omega = 2mc^2/hbar (Schrodinger's triad: amplitude
   hbar/2mc, frequency 2mc^2/hbar, speed c).  At omega = 2mc^2/hbar the harmonic ground-state width is exactly r_th.
g_A is m_q-independent but omega-dependent (4266); the charge radius measures the breath's WIDTH directly.
r_p: SS-2's formula r_p^2 = (1/Q) sum e_i (|r_i|^2 + s_i^2), origin at the quark centroid (reproduces SS-2's 0.883 fm
with uniform s^2 = r_ZBW^2), with s_i^2 now the quark's summed mode widths (NR ground states: anchored 1/(2 omega),
each quark's share of a u-d relative mode 1/(4 omega), units r_ZBW^2):  u = radial + diagonal + sideways;
d = radial + two sideways (+ diagonal toward the open +eCP in a free proton, 4271).  delta = 0 (no eCP displacement);
exchange not applied to r_p.  g_A: free-nucleon ruled state (4271), odd-quark diagonal at 45 deg, u-u exchange,
REL ground states at each omega (units m_q c^2/hbar)."""
import numpy as np
from scipy.optimize import brentq
from scipy.linalg import eigh_tridiagonal
rng=np.random.default_rng(12); N=1_200_000
mq=938.272/3; rZ=197.327/mq; duu,dud=1.071/rZ,0.620/rZ; h=np.sqrt(dud**2-(duu/2)**2)
u1=np.array([-duu/2,0,0]); d=np.array([0,h,0]); u2=np.array([duu/2,0,0]); e=lambda a,b:(b-a)/np.linalg.norm(b-a); z=np.array([0,0,1.])
cen=(u1+u2+d)/3; r2=lambda v:np.sum((v-cen)**2)*rZ**2
Ser2=(2/3)*r2(u1)+(2/3)*r2(u2)-(1/3)*r2(d)
def rp(w,ddiag=True):
    su=1.25/w; sd=(1.5 if ddiag else 1.0)/w
    return np.sqrt(Ser2+((4/3)*su-(1/3)*sd)*rZ**2)
print(f'SS-2 check (uniform s^2 = r_ZBW^2, delta = 0): r_p = {np.sqrt(Ser2+rZ**2):.4f} fm (SS-2: 0.883); measured 0.8409\n')
def ground(kin,Mpot,w):
    p=np.linspace(-30,30,9000); dp=p[1]-p[0]; a=0.5*Mpot*w*w
    E,V=eigh_tridiagonal(kin(p)+2*a/dp**2,-a/dp**2*np.ones(len(p)-1),select='i',select_range=(0,0)); P=V[:,0]**2; return p,P/P.sum()
U=[rng.random(N) for _ in range(5)]
def gA(w,ang=45):
    MA=ground(lambda p:np.sqrt(p*p+1)-1,1.0,w); MS=ground(lambda p:2*(np.sqrt(p*p+1)-1),0.5,w)
    cdf=lambda M:np.cumsum(M[1]); s=lambda M,u:np.interp(u,cdf(M),M[0])
    sr=np.sqrt(np.sum(MA[0]**2*MA[1])); ss=np.sqrt(np.sum(MS[0]**2*MS[1]))
    a=np.radians(ang); n=np.cos(a)*z+np.sin(a)*e(d,(u1+u2)/2)
    KD=s(MA,U[0])[:,None]*z+s(MS,U[1])[:,None]*e(d,u1)+s(MS,U[2])[:,None]*e(d,u2)+s(MA,U[3])[:,None]*n
    Rd=1/3+2/3*np.mean(1/np.sqrt((KD**2).sum(1)+1))
    O=lambda v:np.outer(v,v); cov=lambda u,o:sr**2*O(z)+sr**2*O(e(u,o))+ss**2*O(e(u,d))
    C1,C2=cov(u1,u2),cov(u2,u1); I1,I2=np.linalg.inv(C1),np.linalg.inv(C2)
    p=rng.normal(size=(N,3))@np.linalg.cholesky(C1).T; f=1/np.sqrt((p**2).sum(1)+1)
    q=lambda P,I:np.einsum('ni,ij,nj->n',P,I,P)
    rc=np.exp(-(q(p,I2)-q(p,I1))/4)*(np.linalg.det(C1)/np.linalg.det(C2))**0.25*np.cos(p@(u2-u1)); sv=rc.mean()
    Ru=1/3+2/3*(f.mean()-sv*np.mean(f*rc))/(1-sv*sv)
    return 4/3*Ru+Rd/3,Ru,Rd,sv
gA_t,rp_t=1.2754,0.8409
for w in (1.0,1.2,1.4,1.6,2.0):
    g=gA(w); print(f"  omega = {w:.1f} mc^2/hbar:  g_A = {g[0]:.4f} ({100*(g[0]/gA_t-1):+5.1f}%)   r_p = {rp(w):.4f} fm ({100*(rp(w)/rp_t-1):+5.1f}%)   [u-u overlap {g[3]:.3f}]")
wg=brentq(lambda w:gA(w)[0]-gA_t,1.0,1.5,xtol=2e-3); wr=brentq(lambda w:rp(w)-rp_t,1.0,2.0)
print(f"\n  omega that closes g_A: {wg:.2f} mc^2/hbar;  omega that closes r_p: {wr:.2f} mc^2/hbar")
print("\n-> No single frequency closes both.  Route (H) (omega = 1): g_A +1.6%, r_p +9.4%.  Schrodinger's triad (omega = 2):")
print("   g_A -8.6%, r_p -6.8%.  The two observables ask for 1.1 and 1.4 -- a tension, recorded, not resolved.")
