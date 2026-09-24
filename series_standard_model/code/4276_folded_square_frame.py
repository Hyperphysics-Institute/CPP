#!/usr/bin/env python3
"""4276 -- the founder's folded-square frame (founders_voice/4276).
The hTetra is a 2eCP-2qCP element: a square whose four edges are the attractive pairs (e-e+, q-q+, e+q-, e-q+) and
whose two diagonals are the like-sign pairs (e-q-, e+q+), which repel, so the bare square lies flat.  It folds into
an (irregular) tetrahedron only when quarks bond to its corners.  Proton: the ups on the two minus corners, the d on
the +qCP corner, the +eCP corner open.  So:  u-d = an attractive EDGE, length a;  u-u = the minus DIAGONAL, between
a (fully folded, regular) and sqrt2 a (flat);  the d's diagonal mode (4271) points across the plus diagonal to the
open +eCP corner.  The fold is taken symmetric (plus diagonal = minus diagonal); its angle follows from the ratio.
Nothing fixes a yet (4275), so a is fitted to r_p = 0.8409 fm (one fit) and g_A is then a prediction.
Route (H); free-nucleon ruled state; u-u exchange in momentum and position; REL widths (4273-4274 machinery).
Not yet included (4275 owed): the vertex CPs' own swing; the shorter inner swing."""
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.optimize import brentq
rng=np.random.default_rng(21); N=1_500_000
mq=938.272/3; rZ=197.327/mq; e=lambda a,b:(b-a)/np.linalg.norm(b-a); z=np.array([0,0,1.]); O=lambda v:np.outer(v,v)
def gs(kin,Mpot):
    p=np.linspace(-30,30,12000); dp=p[1]-p[0]; a=0.5*Mpot
    E,V=eigh_tridiagonal(kin(p)+2*a/dp**2,-a/dp**2*np.ones(len(p)-1),select='i',select_range=(0,0)); psi=V[:,0]/np.sqrt(dp)
    return p,psi**2*dp,np.sum(np.gradient(psi,dp)**2)*dp
pa,Pa,xa=gs(lambda p:np.sqrt(p*p+1)-1,1.0); ps,Ps,xs2=gs(lambda p:2*(np.sqrt(p*p+1)-1),0.5); xs=xs2/4
sr=np.sqrt(np.sum(pa**2*Pa)); ss=np.sqrt(np.sum(ps**2*Ps))
U=[rng.random(N) for _ in range(4)]; smp=lambda p,P,u:np.interp(u,np.cumsum(P),p)
def geo(k):
    duu,dud=k[0]/rZ,k[1]/rZ; h=np.sqrt(dud**2-(duu/2)**2)
    return np.array([-duu/2,0,0]),np.array([duu/2,0,0]),np.array([0,h,0])
def slater_w(X,m1,S1,m2,S2,q=None):
    def lg(X,m,S): I=np.linalg.inv(S); D=X-m; return -0.5*np.einsum('ni,ij,nj->n',D,I,D)-0.5*np.log(np.linalg.det(2*np.pi*S))
    return lg(X,m1,S1),lg(X,m2,S2)
def run(k,nd=None):
    u1,u2,d=geo(k); cen=(u1+u2+d)/3
    a=np.radians(45); n=np.cos(a)*z+np.sin(a)*e(d,(u1+u2)/2)
    if nd is not None: n=nd
    # r_p
    Su=lambda u,o: xa*O(z)+xa*O(e(u,o))+xs*O(e(u,d)); Sd=xa*O(z)+xs*O(e(d,u1))+xs*O(e(d,u2))+xa*O(n)
    S1,S2=Su(u1,u2),Su(u2,u1)
    X=np.vstack([u1+rng.normal(size=(N//2,3))@np.linalg.cholesky(S1).T,u2+rng.normal(size=(N//2,3))@np.linalg.cholesky(S2).T])
    La,Lb=slater_w(X,u1,S1,u2,S2); q=0.5*(np.exp(La)+np.exp(Lb)); A,B=np.exp(0.5*La),np.exp(0.5*Lb)
    s=np.mean(A*B/q); w=(A*A+B*B-2*s*A*B)/(2*(1-s*s))/q
    r2u=np.sum(w*((X-cen)**2).sum(1))/np.sum(w); r2d=np.sum((d-cen)**2)+np.trace(Sd)
    rp=np.sqrt((4/3)*r2u-(1/3)*r2d)*rZ
    # g_A (momentum-space exchange as 4262; d diagonal 45 deg as 4271)
    KD=smp(pa,Pa,U[0])[:,None]*z+smp(ps,Ps,U[1])[:,None]*e(d,u1)+smp(ps,Ps,U[2])[:,None]*e(d,u2)+smp(pa,Pa,U[3])[:,None]*n
    Rd=1/3+2/3*np.mean(1/np.sqrt((KD**2).sum(1)+1))
    cov=lambda u,o:sr**2*O(z)+sr**2*O(e(u,o))+ss**2*O(e(u,d)); C1,C2=cov(u1,u2),cov(u2,u1); I1,I2=np.linalg.inv(C1),np.linalg.inv(C2)
    p=rng.normal(size=(N,3))@np.linalg.cholesky(C1).T; f=1/np.sqrt((p**2).sum(1)+1); qq=lambda P,I:np.einsum('ni,ij,nj->n',P,I,P)
    rc=np.exp(-(qq(p,I2)-qq(p,I1))/4)*(np.linalg.det(C1)/np.linalg.det(C2))**0.25*np.cos(p@(u2-u1)); sp=rc.mean()
    Ru=1/3+2/3*(f.mean()-sp*np.mean(f*rc))/(1-sp*sp)
    return rp,4/3*Ru+Rd/3,s,sp,Ru,Rd
def fold(ratio,a):
    D=ratio*a; rho=np.sqrt(a*a-D*D/4); th=2*np.arcsin(min(1,D/(2*rho)))
    P1=np.array([0,rho,0]); P2=np.array([0,rho*np.cos(th),rho*np.sin(th)])
    return D,(P2-P1)/np.linalg.norm(P2-P1),th
from scipy.optimize import brentq
for ratio in (1.0,1.2,2**0.5-1e-6):
    def f(a):
        D,n,th=fold(ratio,a); return run((D,a),n)[0]-0.8409
    a0=brentq(f,0.15,0.8,xtol=2e-3); D,n,th=fold(ratio,a0); rp,g,s_,sp,Ru,Rd=run((D,a0),n)
    x=938.919/mq; Sl,So=(1+Ru)/2,(1+Rd)/2; mp=(4*(2/3)*x*Sl+(1/3)*x*So)/3; mqf=mq*mp/2.79285; mn=(4*(-1/3)*x*Sl-(2/3)*x*So)/3*mq/mqf
    print(f"ratio u-u/u-d={ratio:.3f}: a (u-d) = {a0:.3f} fm, u-u = {D:.3f} fm, fold angle {np.degrees(th):.0f} deg -> r_p={rp:.4f}  g_A={g:.4f} ({100*(g/1.2754-1):+.2f}%)  m_q(mu_p)={mqf:.1f}  mu_n={mn:.3f} ({100*(mn/-1.91304-1):+.1f}%)  overlaps x {s_:.2f} p {sp:.2f}")
print("\n-> Across the founder's whole allowed shape range (regular to flat), fitting the size to r_p puts u-u at 0.60-0.62 fm")
print("   and predicts g_A = 1.267-1.270 (-0.4% to -0.7%).  SS-2's 120-degree shape (u-u = 1.73 u-d) lies outside the range.")
