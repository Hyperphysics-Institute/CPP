#!/usr/bin/env python3
"""4262 -- the founder's answer to 4261 s5 (founders_voice/4262): each up quark is bound to BOTH minus vertices of the
hTetra -- its own with strong + charge, the other with charge only -- and ZBW-oscillates with each; sideways with the d.
So the u's third mode runs along the u-u line toward the other minus vertex (anchored on a frame vertex, like the
radial), at the Compton frequency (c04) like every ZBW mode.  "At random times" = the modes are independent, which is
the product state used here.  When both u's move toward the d they approach each other; their overlap enters through
the u-u exchange (4261 (C): colour = vertex, SS-1c, 4240 symmetric spin-flavour -> Slater determinant).
Modes as 4244 (REL ground states; independent 1D modes summed as momenta); d unchanged."""
import numpy as np
from scipy.linalg import eigh_tridiagonal
rng=np.random.default_rng(4262); N=2_000_000
MN=938.919; mq=938.272/3; xq=MN/mq; rZ=197.327/mq; gA_t,mup_t,mun_t=1.2754,2.79285,-1.91304
duu,dud=1.071/rZ,0.620/rZ; h=np.sqrt(dud**2-(duu/2)**2)
u1=np.array([-duu/2,0,0]); d=np.array([0,h,0]); u2=np.array([duu/2,0,0]); e=lambda a,b:(b-a)/np.linalg.norm(b-a); z=np.array([0,0,1.])
def ground(kin,Mpot):
    p=np.linspace(-14,14,7000); dp=p[1]-p[0]; a=0.5*Mpot
    E,V=eigh_tridiagonal(kin(p)+2*a/dp**2,-a/dp**2*np.ones(len(p)-1),select='i',select_range=(0,0)); P=V[:,0]**2; return p,P/P.sum()
MA=ground(lambda p:np.sqrt(p*p+1)-1,1.0); MS=ground(lambda p:2*(np.sqrt(p*p+1)-1),0.5); dr=lambda M:rng.choice(M[0],size=N,p=M[1])
R=lambda K:1/3+2/3*np.mean(1/np.sqrt((K**2).sum(1)+1))
def row(lab,Ru,Rd):
    g=4/3*Ru+Rd/3; Su,Sd=(1+Ru)/2,(1+Rd)/2
    mp=(4*(2/3)*xq*Su+(1/3)*xq*Sd)/3; mn=(4*(-1/3)*xq*Sd-(2/3)*xq*Su)/3
    print(f"  {lab:52s} R_u={Ru:.4f} R_d={Rd:.4f}  g_A={g:.4f} ({100*(g/gA_t-1):+5.1f}%)  mu_p={mp:.3f} ({100*(mp/mup_t-1):+5.1f}%)  mu_n={mn:.3f} ({100*(mn/mun_t-1):+5.1f}%)")
    return mp
KD=dr(MA)[:,None]*z+dr(MS)[:,None]*e(d,u1)+dr(MS)[:,None]*e(d,u2); Rd=R(KD)
KU=dr(MA)[:,None]*z+dr(MS)[:,None]*e(u1,d)
KU3=KU+dr(MA)[:,None]*e(u1,u2)
ang=np.degrees(np.arccos(e(u1,d)@e(u1,u2)))
print(f"u's in-plane mode lines: u-d edge and u-u line (toward the other minus vertex), {ang:.1f} deg apart -- the plane is now held")
row("4244: u radial + u-d",R(KU),Rd)
row("u radial + u-d + second minus vertex (founder, 4262)",R(KU3),Rd)
# exchange, Gaussian shapes with the REL rms of each mode
sr,ss=np.sqrt(np.sum(MA[0]**2*MA[1])),np.sqrt(np.sum(MS[0]**2*MS[1]))
cov=lambda u,o:sr**2*np.outer(z,z)+sr**2*np.outer(e(u,o),e(u,o))+ss**2*np.outer(e(u,d),e(u,d))
C1,C2=cov(u1,u2),cov(u2,u1); I1,I2=np.linalg.inv(C1),np.linalg.inv(C2)
p=rng.normal(size=(N,3))@np.linalg.cholesky(C1).T; f=1/np.sqrt((p**2).sum(1)+1)
qf=lambda P,I:np.einsum('ni,ij,nj->n',P,I,P)
rc=np.exp(-(qf(p,I2)-qf(p,I1))/4)*(np.linalg.det(C1)/np.linalg.det(C2))**0.25*np.cos(p@(u2-u1)); s=rc.mean()
Rg=1/3+2/3*f.mean(); Rx=1/3+2/3*(f.mean()-s*np.mean(f*rc))/(1-s*s)
row("  same, Gaussian shapes (check against the row above)",Rg,Rd)
mp=row(f"  + u-u exchange (overlap s = {s:.3f})",Rx,Rd)
row("if u_e has no diagonal pull: one u held, one unheld (equal weights)",(R(KU3)+R(KU))/2,Rd)
print(f"\n  keeping mu_p at this state needs m_q = {mq*mp/mup_t:.1f} MeV (m_p/3 = {mq:.1f})")
print("\n-> The founder's second-minus-vertex binding holds the u in the plane: g_A 1.333 (+4.5%), the same as 4261 (B) at the")
print("   breath's width (1.332); with the u-u exchange, 1.310 (+2.7%).  mu_p falls with it, as in every route (m_q tie).")
