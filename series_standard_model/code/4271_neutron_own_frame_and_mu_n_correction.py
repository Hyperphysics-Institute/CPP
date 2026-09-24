#!/usr/bin/env python3
"""4271 -- the neutron in its own frame (TODO-4234-DELTA, 4270 owed (b)), and a correction to mu_n since 4244.
(1) Frame.  Founder seat rules (4270: up 2/4 minus only, down 4/4) + the SU(3) story's beta decay ("its +qCP core
    migrates to the open minus eCP vertex -- udd becomes uud"): the neutron has u on the -qCP, the two d's on the two
    plus vertices (+qCP, +eCP), the -eCP open.  It is the proton's mirror: the LIKE pair (dd) on the repulsive
    plus-plus edge, the ODD quark (u) at the apex.  SS-2's force balance for the like-pair edge with d charges:
    [1 + alpha/9 - (2/3) alpha_geom] vs the proton's [1 + 4 alpha/9 - (2/3) alpha_geom].
    Modes by role (4244/4262 rule, mirrored): like-pair quarks -- radial, diagonal (the other like-sign vertex),
    sideways to the odd quark; odd quark -- radial, sideways to both.  Route (H) widths do not depend on binding
    strength (4262), so the neutron's R_like, R_odd equal the proton's R_u, R_d to the geometry difference, and the
    d-d exchange equals the proton's u-u exchange (same overlap).
(2) Correction.  Since 4244 the scripts computed mu_n as (4 mu_d - mu_u)/3 with S_d = the proton's ODD-quark S and
    S_u = the proton's LIKE-pair S -- i.e. by flavour.  In the neutron's own frame the d's are the like pair and the
    u is the odd quark: mu_n = (4 (-1/3) x S_like + ... ) must use S_like for the d's and S_odd for the u.
    mu_p is unaffected.
(3) Free nucleon.  4270: the d bonds to the +eCP vertex when it is open ("similar to" its other bonds); in a free
    proton the +eCP is the open binding site (SS-2), so the odd quark gets a diagonal mode toward it -- the mirror of
    the u's diagonal mode (4262).  In the free neutron the u gets the same toward the open -eCP.  The open vertex's
    position is not on file (it is off the quark plane), so the mode's direction is scanned from the plane normal to
    in-plane toward the like pair.  Anchored, route (H), independent modes as 4244."""
import numpy as np
al=1/137.036; ag=1/np.sqrt(5)
rp=1.071; rn=rp*np.sqrt((1+al/9-2/3*ag)/(1+4*al/9-2/3*ag))
print(f"(1) like-pair edge: proton uu {rp:.4f} fm, neutron dd {rn:.4f} fm ({100*(rn/rp-1):+.2f}%) -- the mirror holds to 0.2%\n")
MN=938.919; mq0=938.272/3; gA_t,mup_t,mun_t=1.2754,2.79285,-1.91304
def mom(Rl,Ro,mq):
    x=MN/mq; Sl,So=(1+Rl)/2,(1+Ro)/2
    mp=(4*(2/3)*x*Sl+(1/3)*x*So)/3
    mn_old=(4*(-1/3)*x*So-(2/3)*x*Sl)/3          # as scripted since 4244 (flavour-assigned)
    mn_new=(4*(-1/3)*x*Sl-(2/3)*x*So)/3          # neutron's own frame (role-assigned, mirror)
    return mp,mn_old,mn_new
print("(2) mu_n, as scripted since 4244 vs neutron's own frame:")
for lab,Rl,Ro in (("4244 (founder mode rule, before 4262)",0.8502,0.8163),("4262 ruled state, u-u exchange (= 4269 L1)",0.7781,0.8162)):
    for mlab,mq in (("m_q = m_p/3",mq0),("m_q fitted to mu_p",None)):
        if mq is None: mq=mq0*mom(Rl,Ro,mq0)[0]/mup_t
        mp,mo,mn=mom(Rl,Ro,mq)
        print(f"  {lab:44s} {mlab:20s} m_q={mq:5.1f}  mu_p={mp:.3f}  mu_n scripted {mo:.3f} ({100*(mo/mun_t-1):+4.1f}%)  -> own frame {mn:.3f} ({100*(mn/mun_t-1):+4.1f}%)  mu_n/mu_p {mn/mp:.4f} (meas {mun_t/mup_t:.4f})")
from scipy.linalg import eigh_tridiagonal
rng=np.random.default_rng(4271); N=2_000_000
rZ=197.327/mq0; duu,dud=1.071/rZ,0.620/rZ; h=np.sqrt(dud**2-(duu/2)**2)
u1=np.array([-duu/2,0,0]); d=np.array([0,h,0]); u2=np.array([duu/2,0,0]); e=lambda a,b:(b-a)/np.linalg.norm(b-a); z=np.array([0,0,1.])
def ground(kin,Mpot):
    p=np.linspace(-14,14,7000); dp=p[1]-p[0]; a=0.5*Mpot
    E,V=eigh_tridiagonal(kin(p)+2*a/dp**2,-a/dp**2*np.ones(len(p)-1),select='i',select_range=(0,0)); P=V[:,0]**2; return p,P/P.sum()
MA=ground(lambda p:np.sqrt(p*p+1)-1,1.0); MS=ground(lambda p:2*(np.sqrt(p*p+1)-1),0.5); dr=lambda M:rng.choice(M[0],size=N,p=M[1])
Rf=lambda K:1/3+2/3*np.mean(1/np.sqrt((K**2).sum(1)+1))
KD=dr(MA)[:,None]*z+dr(MS)[:,None]*e(d,u1)+dr(MS)[:,None]*e(d,u2); Rl=0.7781
print("\n(3) free nucleon: odd quark's diagonal mode toward the open like-sign vertex (like pair: 4262 state, u-u exchange)")
print(f"    without it (4262/4269 L1): R_odd = {Rf(KD):.4f}")
for ang in (0,30,60,90):
    a=np.radians(ang); n=np.cos(a)*z+np.sin(a)*e(d,(u1+u2)/2); Ro=Rf(KD+dr(MA)[:,None]*n)
    g=4/3*Rl+Ro/3; mqf=mq0*mom(Rl,Ro,mq0)[0]/mup_t; mp,_,mn=mom(Rl,Ro,mqf)
    print(f"    direction {ang:2d} deg from the plane normal: R_odd={Ro:.4f}  g_A={g:.4f} ({100*(g/gA_t-1):+4.1f}%)  m_q(mu_p)={mqf:.1f}  mu_n={mn:.3f} ({100*(mn/mun_t-1):+4.1f}%)")
print("\n-> The neutron's own frame is the proton's mirror, so d-d exchange = u-u exchange and no new calculation is needed")
print("   beyond assigning S by role.  Corrected, the 4262 state predicts mu_n = -1.871 (-2.2%) at m_q fitted to mu_p;")
print("   with the odd quark's diagonal mode (free nucleon, 4270) g_A = 1.294-1.297 (+1.4 to +1.7%), direction bracketed.")
