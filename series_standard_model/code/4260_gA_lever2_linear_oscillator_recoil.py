#!/usr/bin/env python3
"""4260 -- TODO-4234-DELTA lever 2: the down quark's internal linear -eCP oscillator acting on its core.
Picture on file (founders_vision.md s6; SS-2 s6): the d is an up core (+qCP, its own orbital spin ZBW) that captured an
electron; the -eCP binds to the core as a LINEAR hDP ZBW oscillator passing through it; the electron's orbital spin DP
left as the neutrino.  A linear oscillation carries no angular momentum, so the lever can act on g_A only through the
core's RECOIL: extra core momentum along the oscillation line, diluting the d's spin (free-spinor R, as 4244).
The u has no linear oscillator (founders_vision s6 table).  Line direction unspecified -> isotropic over the frame.
Baseline = 4244's REL u-d rows (R_u = 0.8502, d sampled from 4244's three modes); units m_const c = 1."""
import numpy as np
from scipy.linalg import eigh_tridiagonal
rng=np.random.default_rng(4260); N=800_000
MN=938.919; mq=938.272/3; xq=MN/mq; gA_t,mup_t,mun_t=1.2754,2.79285,-1.91304
def ground(kin,Mpot):
    p=np.linspace(-14,14,7000); dp=p[1]-p[0]; a=0.5*Mpot
    E,V=eigh_tridiagonal(kin(p)+2*a/dp**2,-a/dp**2*np.ones(len(p)-1),select='i',select_range=(0,0))
    P=V[:,0]**2; return p,P/P.sum()
MA=ground(lambda p:np.sqrt(p*p+1)-1,1.0); MS=ground(lambda p:2*(np.sqrt(p*p+1)-1),0.5)
draw=lambda M:rng.choice(M[0],size=N,p=M[1])
duu,dud=1.071,0.620; h=np.sqrt(dud**2-(duu/2)**2); u1=np.array([-duu/2,0,0]); d=np.array([0,h,0]); u2=np.array([duu/2,0,0])
e=lambda a,b:(b-a)/np.linalg.norm(b-a)
kd=draw(MA)[:,None]*np.array([0,0,1.])+draw(MS)[:,None]*e(d,u1)+draw(MS)[:,None]*e(d,u2)
Ru=0.8502
def Rd(s):
    n=rng.normal(size=(N,3)); n/=np.linalg.norm(n,axis=1)[:,None]
    k=kd+(s*rng.normal(size=N))[:,None]*n; E=np.sqrt((k**2).sum(1)+1)
    return 1/3+2/3*np.mean(1/E), np.mean(E)
def mu(Ru,Rd):
    Su,Sd=(1+Ru)/2,(1+Rd)/2; return (4*(2/3)*xq*Su+(1/3)*xq*Sd)/3,(4*(-1/3)*xq*Sd-(2/3)*xq*Su)/3
R0,E0=Rd(0.0); need=3*(gA_t-4/3*Ru)
print(f"baseline (4244 REL u-d): R_u={Ru:.4f} R_d={R0:.4f} g_A={4/3*Ru+R0/3:.4f}   <E_d>={E0:.3f} m_const")
print(f"d's share of g_A: (1/3)R_d of (5/3)R -- the lever acts on 1/5 of g_A")
print(f"R_d needed for g_A = 1.2754 with R_u fixed: {need:.4f}   (floor R_d -> 1/3 at infinite recoil gives g_A = {4/3*Ru+1/9:.4f})\n")
print("recoil spread s (Gaussian along the line, units m_const c) -> R_d, g_A, core energy, tied moments:")
for s in (0.0,0.013,0.1,0.5,1.0,2.0,4.0,6.0,8.0):
    R,E=Rd(s); g=4/3*Ru+R/3; mp,mn=mu(Ru,R)
    print(f"  s={s:5.3f} ({s*mq:6.0f} MeV)  R_d={R:.4f}  g_A={g:.4f} ({100*(g/gA_t-1):+5.1f}%)  <E_d>={E:6.3f} m_const ({E*mq:5.0f} MeV)  mu_p={mp:.3f} ({100*(mp/mup_t-1):+5.1f}%)  mu_n={mn:.3f} ({100*(mn/mun_t-1):+5.1f}%)")
lo,hi=2.0,400.0
for _ in range(22):
    mid=(lo+hi)/2; lo,hi=(mid,hi) if Rd(mid)[0]>need else (lo,mid)
R,E=Rd(lo); mp,mn=mu(Ru,R)
print(f"\nclosing value: s = {lo:.2f} m_const c = {lo*mq:.0f} MeV along the line; <E_d> = {E:.2f} m_const = {E*mq:.0f} MeV (M_N = {MN:.0f})")
print(f"  tied moments there: mu_p={mp:.3f} ({100*(mp/mup_t-1):+5.1f}%)  mu_n={mn:.3f} ({100*(mn/mun_t-1):+5.1f}%)")
print("\nscale on file: the d-u mass difference, 2.5 MeV (founders_vision s6: the energy of forming the d from the u) to")
print("4 MeV (SS-2's 340-336); recoil at that scale (s = 0.013 row) moves g_A by < 1e-4. (A deeply bound oscillator's kinetic")
print("energy is not capped by the net mass difference, so the exclusion rests on the closing row, not on this scale.)")
ft=0.04; print(f"eCP trading onto a u (f_trade ~ {ft:.0%}, founders_vision 10 Apr 2026): bound even at infinite recoil, "
      f"|dg_A| <= (4/3) f (R_u - 1/3) = {4/3*ft*(Ru-1/3):.3f}")
print("\n-> Lever 2 cannot close the residual: it reaches only the d's 1/5 share of g_A, so closing needs a d core whose")
print("   mean energy is ~5 M_N, and mu_n falls 18% below measured there; the scale on file moves g_A by < 1e-4.")
