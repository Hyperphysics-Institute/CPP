#!/usr/bin/env python3
"""4266 -- TODO-4264-PASSTHROUGH step 8: which frequency does the ZBW breath run at, and how much does g_A care?
Three conventions sit in the corpus for "the Compton frequency":
  (a) route (H), 4243-4263: angular omega = mc^2/hbar  <=> one full pass-through swing takes h/mc^2 (the Compton
      period lambda_C/c); consistent with E = h nu = hbar omega for the swing.
  (b) Schrodinger's ZBW: angular 2mc^2/hbar -- the beat of the +E and -E parts of a Dirac state (energy gap 2mc^2).
  (c) c04 Prop. (mc^2): T_C = 2 r_th/c = hbar/mc^2 used as the PERIOD, i.e. angular 2 pi mc^2/hbar.
g_A and the tied moments are recomputed for 4244's mode set and for the founder-ruled set (4262: + second minus
vertex), REL ground states, independent modes summed as 4244; before exchange.  Units m_const c = 1."""
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq
rng=np.random.default_rng(4266); N=1_500_000
MN=938.919; mq=938.272/3; xq=MN/mq; gA_t,mup_t,mun_t=1.2754,2.79285,-1.91304
rZ=197.327/mq; duu,dud=1.071/rZ,0.620/rZ; h=np.sqrt(dud**2-(duu/2)**2)
u1=np.array([-duu/2,0,0]); d=np.array([0,h,0]); u2=np.array([duu/2,0,0]); e=lambda a,b:(b-a)/np.linalg.norm(b-a); z=np.array([0,0,1.])
G=[rng.random(N) for _ in range(6)]
def ground(kin,Mpot,w):
    p=np.linspace(-40,40,12000); dp=p[1]-p[0]; a=0.5*Mpot*w*w
    E,V=eigh_tridiagonal(kin(p)+2*a/dp**2,-a/dp**2*np.ones(len(p)-1),select='i',select_range=(0,0)); P=V[:,0]**2; return p,np.cumsum(P/P.sum())
def samp(M,u): return np.interp(u,M[1],M[0])
R=lambda K:1/3+2/3*np.mean(1/np.sqrt((K**2).sum(1)+1))
def gA(w):
    MA=ground(lambda p:np.sqrt(p*p+1)-1,1.0,w); MS=ground(lambda p:2*(np.sqrt(p*p+1)-1),0.5,w)
    KD=samp(MA,G[0])[:,None]*z+samp(MS,G[1])[:,None]*e(d,u1)+samp(MS,G[2])[:,None]*e(d,u2)
    KU=samp(MA,G[3])[:,None]*z+samp(MS,G[4])[:,None]*e(u1,d); KU3=KU+samp(MA,G[5])[:,None]*e(u1,u2)
    return R(KU),R(KU3),R(KD)
def row(lab,Ru,Rd):
    g=4/3*Ru+Rd/3; Su,Sd=(1+Ru)/2,(1+Rd)/2; mp=(4*(2/3)*xq*Su+(1/3)*xq*Sd)/3; mn=(4*(-1/3)*xq*Sd-(2/3)*xq*Su)/3
    print(f"    {lab:24s} g_A={g:.4f} ({100*(g/gA_t-1):+6.1f}%)  mu_p={mp:.3f} ({100*(mp/mup_t-1):+5.1f}%)  mu_n={mn:.3f} ({100*(mn/mun_t-1):+5.1f}%)"); return g
for lab,w in (("(a) route H, mc^2/hbar",1.0),("(b) Schrodinger, 2mc^2/hbar",2.0),("(c) c04 T_C literal, 2 pi mc^2/hbar",2*np.pi)):
    Ru,Ru3,Rd=gA(w); print(f"{lab}   (omega = {w:.3f} mc^2/hbar)"); row("4244 mode set",Ru,Rd); row("founder-ruled set (4262)",Ru3,Rd)
print()
for lab,i in (("4244 set",0),("ruled set",1)):
    f=lambda w: 4/3*gA(w)[i]+gA(w)[2]/3-gA_t; w0=brentq(f,1.0,2.5,xtol=1e-3); print(f"  omega that closes g_A, {lab}: {w0:.3f} mc^2/hbar")
print("\n-> g_A's dependence on the frequency convention (1.33 / 1.19 / far below for the ruled set) is larger than the")
print("   residual itself.  (a) is the reading consistent with E = hbar omega for the swing; (b) is an energy-gap beat")
print("   (2mc^2) of the Dirac formalism, which the pass-through cycle shows as its speed maximum twice per swing; (c) is")
print("   c04's h-vs-hbar slip in T_C (2 r_th/c = hbar/mc^2 is 2 pi short of the Compton period h/mc^2).")
