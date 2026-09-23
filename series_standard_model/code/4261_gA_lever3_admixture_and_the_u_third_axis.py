#!/usr/bin/env python3
"""4261 -- TODO-4234-DELTA lever 3 (excited-mode admixture), and what the search for its source turned up.
(A) Admixture as filed: any excitation raises every mode's momentum spread.  Scale all of 4244's REL mode momenta by f
    and find the f that gives g_A = 1.2754; report the mean excitation n ~ (f^2-1)/2 per mode and the tied moments.
(B) 4244's u quark has modes only along radial (plane normal) and its u-d edge; along the third axis (in plane, normal
    to its u-d edge) it carries ZERO momentum -- i.e. it is unlocalised there -- while 4243's <r^2> = r_ZBW^2 check
    counted zero POSITION spread there.  Both cannot hold.  Localise the u on its vertex along that axis with width w
    (minimum uncertainty, sigma_p = hbar/2w) and recompute R_u.
(C) Colour is which vertex the quark sits on (founders_voice/phenomenon_su3_colour_and_quark_switching.md); colour is
    antisymmetric (SS-1c) and 4240 has the u's spin-flavour symmetric; so the two u's vertex-attached breath states
    enter as a Slater determinant.  One-body density n(p) = [|g_a|^2+|g_b|^2 - 2 s Re(g_a* g_b)] / 2(1-s^2),
    s = <g_a|g_b>.  u-u only; u-d exchange changes the frame geometry and is not included (filed).
(B),(C) use Gaussian mode shapes with 4244's REL per-mode rms (0.7917 radial, 0.5353 u-d); R_d held at 4244's 0.8163.
Units: momentum m_const c, length r_ZBW = hbar c/m_const = 0.631 fm."""
import numpy as np
from scipy.linalg import eigh_tridiagonal
rng=np.random.default_rng(4261); N=2_000_000
MN=938.919; mq=938.272/3; xq=MN/mq; rZ=197.327/mq; gA_t,mup_t,mun_t=1.2754,2.79285,-1.91304
def mu(Ru,Rd):
    Su,Sd=(1+Ru)/2,(1+Rd)/2; return (4*(2/3)*xq*Su+(1/3)*xq*Sd)/3,(4*(-1/3)*xq*Sd-(2/3)*xq*Su)/3
def row(lab,Ru,Rd):
    g=4/3*Ru+Rd/3; mp,mn=mu(Ru,Rd)
    print(f"  {lab:46s} R_u={Ru:.4f} R_d={Rd:.4f}  g_A={g:.4f} ({100*(g/gA_t-1):+5.1f}%)  mu_p={mp:.3f} ({100*(mp/mup_t-1):+5.1f}%)  mu_n={mn:.3f} ({100*(mn/mun_t-1):+5.1f}%)")
duu,dud=1.071/rZ,0.620/rZ; h=np.sqrt(dud**2-(duu/2)**2)
u1=np.array([-duu/2,0,0]); d=np.array([0,h,0]); u2=np.array([duu/2,0,0]); e=lambda a,b:(b-a)/np.linalg.norm(b-a)
z=np.array([0,0,1.])
# ---------------- (A)
def ground(kin,Mpot):
    p=np.linspace(-14,14,7000); dp=p[1]-p[0]; a=0.5*Mpot
    E,V=eigh_tridiagonal(kin(p)+2*a/dp**2,-a/dp**2*np.ones(len(p)-1),select='i',select_range=(0,0))
    P=V[:,0]**2; return p,P/P.sum()
MA=ground(lambda p:np.sqrt(p*p+1)-1,1.0); MS=ground(lambda p:2*(np.sqrt(p*p+1)-1),0.5)
dr=lambda M:rng.choice(M[0],size=N,p=M[1])
KU=dr(MA)[:,None]*z+dr(MS)[:,None]*e(u1,d); KD=dr(MA)[:,None]*z+dr(MS)[:,None]*e(d,u1)+dr(MS)[:,None]*e(d,u2)
Rf=lambda K,f:1/3+2/3*np.mean(1/np.sqrt(f*f*(K**2).sum(1)+1))
print("(A) excited-mode admixture: every mode's momentum scaled by f (4244 REL modes)")
row("f = 1 (4244)",Rf(KU,1),Rf(KD,1))
lo,hi=1.0,2.0
for _ in range(30):
    m=(lo+hi)/2; lo,hi=(m,hi) if 4/3*Rf(KU,m)+Rf(KD,m)/3>gA_t else (lo,m)
row(f"f = {lo:.3f} (closes g_A; n ~ {(lo*lo-1)/2:.2f} quanta/mode)",Rf(KU,lo),Rf(KD,lo))
mp,_=mu(Rf(KU,lo),Rf(KD,lo)); print(f"  -> at m_q = m_p/3 the tie costs mu_p; keeping mu_p needs m_q = {mq*mp/mup_t:.1f} MeV (4243 (T): 296.7)\n")
# ---------------- (B),(C)
sr,ss=0.7917,0.5353; Rd0=0.8163
def uR(w,exch):
    sf=1/(2*w) if w else 1e-9
    A1=np.stack([z,e(u1,d),np.cross(z,e(u1,d))]); A2=np.stack([z,e(u2,d),np.cross(z,e(u2,d))]); sg=np.array([sr,ss,sf])
    p=(rng.normal(size=(N,3))*sg)@A1; f=1/np.sqrt((p**2).sum(1)+1)
    if not exch: return 1/3+2/3*f.mean(),None
    lg=lambda P,A:-((P@A.T)**2/(4*sg**2)).sum(1); rc=np.exp(lg(p,A2)-lg(p,A1))*np.cos(p@(u2-u1)); s=rc.mean()
    return 1/3+2/3*(f.mean()-s*np.mean(f*rc))/(1-s*s),s
print("(B) the u localised on its vertex along its third axis, width w; (C) plus u-u exchange (colour = vertex)")
row("w = infinite (4244's u, Gaussian shapes)",uR(0,False)[0],Rd0)
for w in (2.0,1.0,1/np.sqrt(2),0.5):
    RB,_=uR(w,False); RC,s=uR(w,True)
    tag=" = r_ZBW/sqrt2, the breath's own width" if abs(w-1/np.sqrt(2))<1e-9 else ""
    row(f"(B) w = {w*rZ:.3f} fm{tag}",RB,Rd0); row(f"(C) w = {w*rZ:.3f} fm, overlap s = {s:.3f}",RC,Rd0)
print("\n-> (A): closing by excitation needs f above; no source of excitation is on file, and at m_q = m_p/3 it costs mu_p.")
print("   (B): 4244's u is unlocalised along one axis; any seat width moves g_A down -- the omitted direction is a real")
print("   part of the residual, of size set by w.  (C): the u-u exchange adds a further ~2% of g_A at the breath's width.")
