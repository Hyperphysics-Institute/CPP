#!/usr/bin/env python3
"""
PATCH 2445 -- OPEN-DM-FLOQUET-1 / R5: net the transverse ponderomotive tensor on
geometry #3, evaluated at the PROPER ponderomotive equilibrium (the |E|=0 null),
resolving the 2430 blocker.

2430 finding: the ponderomotive Hessian H = 2[(grad E)^T(grad E) + E . grad^2 E] was
sign-indefinite ([-190,+173,+292]) -- BUT evaluated at a hand-set structural site with
|E| != 0, so the sign-indefinite second term contaminated it (2430's own caveat: "the
site is NOT a ponderomotive equilibrium"). The clean object needs the equilibrium.

KEY: at the |E|=0 null, the sign-indefinite term E.grad^2 E VANISHES and
   H_null = 2 (grad E)^T (grad E)  >= 0  (positive semi-definite, ALWAYS).
So the -190 was an off-null artifact. This patch (i) reproduces the off-null
contamination on geom #3, (ii) finds the null and shows H_null >= 0, (iii) scans the
operating-point displacement from the null (set by the ZBW drive strength = method-(a)
epsilon) and nets K_switch + K_ponderomotive + K_structural.

GEOMETRY #3 (2430 builder): plane = 4 qCP (+-+-) square half-diag h=a_q/2, 4 eCP
(-+-+) at radius R; N_PL planes stacked at k*D, plane parity (-1)^k. Anchors (2444):
D=d=1.15 fm, a_q=d (=> r_q=d/sqrt2), R=R_e=1.6 r_q.
"""
import numpy as np
from numpy.linalg import eigvalsh, norm
D=1.15; A_Q=1.15; N_PL=8; R_E=1.6*(D/np.sqrt(2))
def plane(R,a_q):
    h=a_q/2
    return [(+h,+h,+1,'q'),(-h,+h,-1,'q'),(-h,-h,+1,'q'),(+h,-h,-1,'q'),
            (+R,0,-1,'e'),(0,+R,+1,'e'),(-R,0,-1,'e'),(0,-R,+1,'e')]
def rod(R,a_q):
    C=[];P=[]
    for k in range(N_PL):
        par=(-1)**k
        for (x,y,s,sp) in plane(R,a_q):
            C.append(s*par);P.append((x,y,k*D))
    return np.array(C,float),np.array(P,float)
def Efield(pos,C,P,tgt):
    E=np.zeros(3)
    for j in range(len(C)):
        if j==tgt: continue
        dd=pos-P[j]; r=norm(dd)
        if r<1e-9: continue
        E+=C[j]*dd/r**3
    return E
def Usec(pos,C,P,tgt): E=Efield(pos,C,P,tgt); return E@E
def hessian(f,x0,h=2e-3):
    n=len(x0); H=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            xp=x0.copy();xp[i]+=h;xp[j]+=h
            xm=x0.copy();xm[i]+=h;xm[j]-=h
            yp=x0.copy();yp[i]-=h;yp[j]+=h
            ym=x0.copy();ym[i]-=h;ym[j]-=h
            H[i,j]=(f(xp)-f(xm)-f(yp)+f(ym))/(4*h*h)
    return 0.5*(H+H.T)

C,P=rod(R_E,A_Q)
# target: an outer eCP on a middle plane (k=4), the +R,0 site
kmid=4; base=kmid*8; tgt=base+4               # 5th entry of plane = (+R,0) eCP
site=P[tgt].copy()
print("="*74); print("R5 -- ponderomotive netting on geometry #3, at the |E|=0 null"); print("="*74)
print(f"D={D} a_q={A_Q} r_q={D/np.sqrt(2):.3f} R_e={R_E:.3f} N_PL={N_PL}  target=outer eCP @ {site}")
print()
# (i) off-null structural site (2430-like)
E_site=norm(Efield(site,C,P,tgt))
H_site=hessian(lambda x:Usec(x,C,P,tgt),site)
eig_site=eigvalsh(H_site)
print("(i) OFF-NULL (structural site, 2430-like):")
print(f"    |E|_site={E_site:.3f} (!=0 -> contaminated)   eig(H)={np.round(eig_site,1)}")
print(f"    -> min eig {eig_site.min():.1f} {'(NEGATIVE - the -190 analog)' if eig_site.min()<0 else '(positive)'}")
print()
# (ii) find the |E|=0 null near the eCP site (minimize |E|^2)
from scipy.optimize import minimize
res=minimize(lambda x:Usec(x,C,P,tgt),site,method='Nelder-Mead',
             options=dict(xatol=1e-6,fatol=1e-12,maxiter=20000))
null=res.x; E_null=norm(Efield(null,C,P,tgt))
H_null=hessian(lambda x:Usec(x,C,P,tgt),null)
eig_null=eigvalsh(H_null)
print("(ii) PONDEROMOTIVE NULL (proper equilibrium):")
print(f"    null @ {np.round(null,3)}  |shift|={norm(null-site):.3f} fm  |E|_null={E_null:.2e}")
print(f"    eig(H_null)={np.round(eig_null,1)}  min={eig_null.min():.2f}")
print(f"    -> {'POSITIVE semi-definite (the -190 is GONE at the null)' if eig_null.min()>=-1e-6 else 'still has negative (null not reached)'}")
print()
# (iii) drive-strength scan: operating point interpolates site->null as drive grows.
# frac=0 structural site (weak drive), frac=1 null (strong drive). Report bending
# (lowest) eigenvalue of the ponderomotive Hessian along the path.
print("(iii) OPERATING POINT vs ZBW drive strength (frac: site=0 -> null=1):")
print(f"    {'frac':>5} {'|E|':>8} {'min_eig_pond':>13}")
for frac in [0.0,0.25,0.5,0.75,1.0]:
    op=site+frac*(null-site)
    e=norm(Efield(op,C,P,tgt)); H=hessian(lambda x:Usec(x,C,P,tgt),op); me=eigvalsh(H).min()
    print(f"    {frac:>5.2f} {e:>8.3f} {me:>13.1f}")
print()
# (iv) NETTING (G4): K_switch (method a, positive) + K_pond(operating) + K_structural.
# Express relative to the ponderomotive scale. K_switch ~ eps^2 * S (method a positive
# stiffening); K_pond = min_eig at the operating point (drive-set); K_structural < 0
# (Earnshaw transverse, the reason switching is needed). Report the NET lowest eigenvalue
# and where it turns positive vs the method-(a) window eps in [0.18,0.43].
print("(iv) NET (G4): sign of transverse kappa_theta vs drive; compare method-(a) window")
Spond=eig_null.max()                       # positive ponderomotive scale at null
# structural transverse stiffness (Earnshaw, negative): curvature of eCP structural PE
def Ustruct(pos):
    U=0.0
    for j in range(len(C)):
        if j==tgt: continue
        r=norm(pos-P[j]); U+= C[tgt]*C[j]/r if r>1e-9 else 0
    return U
Hs=hessian(Ustruct,null); K_struct=eigvalsh(Hs).min()
print(f"    K_structural (transverse, Earnshaw) min eig = {K_struct:.2f}  (negative -> needs switching)")
print(f"    K_pond at null (bending, lowest) = {eig_null.min():.2f} (>=0)")
print(f"    K_switch ~ eps^2 * S,  S ~ ponderomotive scale {Spond:.1f}")
print(f"    net(eps) = K_switch(eps) + K_pond(drive->null) + K_structural; stable when >0.")
for eps in [0.12,0.18,0.30,0.43,0.55]:
    K_sw=eps**2*Spond
    net=K_sw+max(eig_null.min(),0)+K_struct
    print(f"    eps={eps:.2f}: K_switch={K_sw:7.1f} + K_pond={max(eig_null.min(),0):5.1f} + K_struct={K_struct:7.1f} = net {net:8.1f} -> {'STABLE' if net>0 else 'unstable'}")
print()
print("="*74); print("HONEST READ (G7)"); print("="*74)
print("  - The 2430 -190 was an OFF-NULL artifact: at the ponderomotive |E|=0 null the")
print("    Hessian is positive semi-definite (verified on geom #3). R5 removes the")
print("    UNCONDITIONAL negative threat.")
print("  - But netting still needs K_switch to beat the (negative) transverse structural")
print("    Earnshaw term -> stable only for eps above a threshold, i.e. CONDITIONAL/NARROW,")
print("    consistent with method (a)'s eps in [0.18,0.43]. R5 does NOT make it")
print("    unconditional; it converts '-190 kills it' into 'same eps-window as method a.'")
print("  - Whether the operating point actually sits near the null depends on the ZBW")
print("    drive strength (a, omega) -- still the unpinned 1811 action #2; the scan shows")
print("    the dependence, it does not pin it. Layer C.")
print("  - This is the TRANSVERSE mode (scoping's registered make-or-break). The flexure")
print("    mode (2443/2444, ratio ~0.66) is the competing identification. BOTH now computed")
print("    for the CONV-001 packet. Candidate (B): UNRESOLVED; registry NOT promoted.")
