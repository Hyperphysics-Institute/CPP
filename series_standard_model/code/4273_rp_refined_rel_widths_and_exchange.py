#!/usr/bin/env python3
"""4273 -- r_p refined (4272 owed): relativistic position widths and the u-u Pauli exchange acting on positions.
REL: each mode's <x^2> from its Salpeter ground state in momentum space, <x^2> = int |d psi/dp|^2 dp (x = i d/dp);
the u-d relative mode's share per quark is <x_rel^2>/4.  Exchange: the two u's one-body POSITION density is the
2-orbital Slater density of their seat Gaussians (covariance = summed mode widths), which pushes them apart.
Free-proton ruled state (4271: odd-quark diagonal at 45 deg); SS-2 frame and formula; origin at the quark centroid;
delta = 0.  Units r_ZBW (0.631 fm); printed r_p in fm (measured 0.8409)."""
import numpy as np
from scipy.linalg import eigh_tridiagonal
rng=np.random.default_rng(20); N=2_000_000
mq=938.272/3; rZ=197.327/mq; duu,dud=1.071/rZ,0.620/rZ; h=np.sqrt(dud**2-(duu/2)**2)
u1=np.array([-duu/2,0,0]); d=np.array([0,h,0]); u2=np.array([duu/2,0,0]); e=lambda a,b:(b-a)/np.linalg.norm(b-a); z=np.array([0,0,1.])
cen=(u1+u2+d)/3
def ground(kin,Mpot,w):
    p=np.linspace(-30,30,12000); dp=p[1]-p[0]; a=0.5*Mpot*w*w
    E,V=eigh_tridiagonal(kin(p)+2*a/dp**2,-a/dp**2*np.ones(len(p)-1),select='i',select_range=(0,0)); psi=V[:,0]/np.sqrt(dp)
    x2=np.sum(np.gradient(psi,dp)**2)*dp; return x2
O=lambda v:np.outer(v,v)
for w in (1.0,1.2,1.4,1.6,2.0):
    for rel in (False,True):
        if rel: xa=ground(lambda p:np.sqrt(p*p+1)-1,1.0,w); xs=ground(lambda p:2*(np.sqrt(p*p+1)-1),0.5,w)/4
        else: xa=1/(2*w); xs=1/(4*w)
        a=np.radians(45); n=np.cos(a)*z+np.sin(a)*e(d,(u1+u2)/2)
        Su=lambda u,o: xa*O(z)+xa*O(e(u,o))+xs*O(e(u,d))
        Sd=xa*O(z)+xs*O(e(d,u1))+xs*O(e(d,u2))+xa*O(n)
        # no exchange
        r2u=lambda u,S: np.sum((u-cen)**2)+np.trace(S)
        base=(2/3)*(r2u(u1,Su(u1,u2))+r2u(u2,Su(u2,u1)))-(1/3)*r2u(d,Sd)
        # exchange on u positions: Slater of real Gaussians
        S1,S2=Su(u1,u2),Su(u2,u1); L1=np.linalg.cholesky(S1); L2=np.linalg.cholesky(S2)
        X=np.vstack([u1+rng.normal(size=(N//2,3))@L1.T, u2+rng.normal(size=(N//2,3))@L2.T])
        def lg(X,m,S): I=np.linalg.inv(S); D=X-m; return -0.5*np.einsum('ni,ij,nj->n',D,I,D)-0.5*np.log(np.linalg.det(2*np.pi*S))
        La,Lb=lg(X,u1,S1),lg(X,u2,S2); q=0.5*(np.exp(La)+np.exp(Lb)); A,B=np.exp(0.5*La),np.exp(0.5*Lb)
        s=np.mean(A*B/q); rho=(A*A+B*B-2*s*A*B)/(2*(1-s*s)); wgt=rho/q
        r2ex=np.sum(wgt*((X-cen)**2).sum(1))/np.sum(wgt)
        exch=(4/3)*r2ex-(1/3)*r2u(d,Sd)
        rn,rx=np.sqrt(base)*rZ,np.sqrt(exch)*rZ
        print(f"  omega={w:.1f} {'REL' if rel else 'NR '}  <x^2> anchored {xa:.3f}, u-d share {xs:.3f}   r_p no exchange {rn:.4f} fm ({100*(rn/0.8409-1):+5.1f}%)   with u-u exchange {rx:.4f} fm ({100*(rx/0.8409-1):+5.1f}%)  [position overlap {s:.3f}]")
print("\n-> REL widths shrink r_p; the u-u exchange pushes the ups apart and grows it.  With both (the consistent state),")
print("   r_p is closed near omega ~1.35-1.4 and is +11.6% at route (H); g_A (with the same exchange) asks ~1.12.")
print("   The tension survives the refinements.  r_p is dominated by the frame term (sum e|r|^2 = 0.382 fm^2 of ~0.71),")
print("   and SS-2's frame size comes from a force balance written with fractional charges (founder 4263: effective only).")
