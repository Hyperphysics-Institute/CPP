#!/usr/bin/env python3
"""
PATCH 2451 -- OPEN-DM-FLOQUET-1 / 1811 action #2 EXECUTED: pin the ZBW drive and place
the physical ponderomotive coefficient lambda against the 2450 threshold band.

IDENTITY (mass-and-clock form; the well stiffness CANCELS):
  U_pond,i = (w_i |E_i|)^2_osc / (4 m omega_sw^2)
  => lambda_phys = f_osc^2 * (hbar c)^2 / (4 * (m c^2) * (hbar omega_sw)^2)   [fm^2/MeV]
  (In method-(a) variables lambda = f^2 eps/(4k) with eps = k/(m omega_sw^2): k cancels.
   The parametric K_switch channel [2440 Meissner tongue] is a SEPARATE positive channel
   omitted from the 2450 netting -- thresholds below are therefore conservative.)

REGISTERED INPUTS:
  f_osc^2 = <(c - cbar)^2> = 1 - (1-2*delta)^2 = 48/49       [delta = 3/7 duty]
  hbar omega_sw = 264 MeV (qDP hop; founder: "SU(3)-type ZBW hop", 2435/2441;
                  eDP hop = 553 MeV; R1 flags possible residence suppression -> slower
                  -> LARGER lambda; bare clock = conservative for this channel)
  mass assignments (registered candidates, NO selection made here):
    88.0 MeV  = per-CP share of the DD-priced element mass (1408/16, 2383 ladder)
    176.0 MeV = per-qCP share if the element dressing loads the 8 qCPs only
    264   MeV = the hopping-constituent (qDP) mass itself
    312.7 MeV = SS-2 constituent m_const (free-cage context, listed for span)

THRESHOLDS from 2450 (total-Phi netting) and the CORE-ONLY conservative variant
(coat carries a slower clock, 553 MeV -> lambda_coat ~ 0.23 lambda_core; dropping the
coat from Phi is the clean conservative bound), recomputed here from the same lattice.
"""
import numpy as np
from numpy.linalg import norm
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036; DELTA=3/7
d=1.15; D=d; A_Q=d; R_E=1.6*(d/np.sqrt(2)); N=16
def plane(R,a_q):
    h=a_q/2
    return [(+h,+h,+1,'q'),(-h,+h,-1,'q'),(-h,-h,+1,'q'),(+h,-h,-1,'q'),
            (+R,0,-1,'e'),(0,+R,+1,'e'),(-R,0,-1,'e'),(0,-R,+1,'e')]
def build(centers,angles):
    Cc=[];Pp=[];Ww=[];Sp=[]
    for k in range(N):
        cx,cy,cz=centers[k]; th=angles[k]; c,s=np.cos(th),np.sin(th); par=(-1)**k
        for (x,y,sgn,sp) in plane(R_E,A_Q):
            Pp.append((cx+x*c, cy+y, cz-x*s)); Cc.append(sgn*par)
            Ww.append(np.sqrt(ALPHA_S) if sp=='q' else np.sqrt(ALPHA)); Sp.append(sp)
    return np.array(Cc,float),np.array(Pp,float),np.array(Ww,float),Sp
def bend(kap):
    if abs(kap)<1e-12: return build([(0,0,k*D) for k in range(N)],[0.0]*N)
    R=1/kap; phis=[k*D/R for k in range(N)]
    return build([(R*(1-np.cos(p)),0,R*np.sin(p)) for p in phis],phis)
def Esw(cfg):
    Cc,Pp,Ww,_=cfg; E=0.0
    for i in range(len(Cc)):
        dd=Pp[i+1:]-Pp[i]; r=np.sqrt((dd*dd).sum(axis=1))
        E+=np.sum(-(1-2*DELTA)*Ww[i]*Cc[i]*(Ww[i+1:]*Cc[i+1:])*AHC/r)
    return E
def Phi(cfg,which='all'):
    Cc,Pp,Ww,Sp=cfg; tot=0.0
    for i in range(len(Cc)):
        if which=='core' and Sp[i]!='q': continue
        dd=Pp[i]-Pp; r=np.sqrt((dd*dd).sum(axis=1)); r[i]=np.inf
        Ei=((Ww*Cc)[:,None]*dd/(r**3)[:,None]).sum(axis=0)*AHC
        tot+=Ww[i]**2*(Ei@Ei)
    return tot
def stiff(fn,y0,xs=(0.005,0.01,0.02)):
    return 2*np.mean([(fn(x)-y0)/x**2 for x in xs])
print("="*78)
print("STEP 2 -- ZBW drive pinning (1811 #2): place lambda_phys vs the 2450 band")
print("="*78)
f2=1-(1-2*DELTA)**2
print(f"f_osc^2 = 1-(1-2d)^2 = {f2:.4f} (=48/49)   (hbar c)^2 = {AHC**2:.1f} MeV^2 fm^2")
lam=lambda m,w: f2*AHC**2/(4*m*w**2)
print()
# ---- thresholds, total-Phi and core-only ----
straight=[(0,0,k*D) for k in range(N)]
E0=Esw(bend(0))
KAP=2*np.pi/(N*D); grid=np.linspace(0,KAP,69)
res={}
for which in ('all','core'):
    P0=Phi(bend(0),which)
    Es=np.array([Esw(bend(k_)) for k_ in grid]); Ps=np.array([Phi(bend(k_),which) for k_ in grid])
    fine=np.linspace(0,KAP,600); Ef=np.interp(fine,grid,Es); Pf=np.interp(fine,grid,Ps)
    lam_open=None
    for L in np.linspace(0,0.02,8001):
        U=Ef+L*Pf
        if (U[-1]-U[-2])<0: lam_open=L; break
    lam_glob=(Es[-1]-E0)/-(Ps[-1]-P0)
    lam_tilt=0.0
    for name,pat in [("gradient",lambda k,t:t*k),("uniform",lambda k,t:t)]:
        SE=stiff(lambda t:Esw(build(straight,[pat(k,t) for k in range(N)])),E0)
        SP=stiff(lambda t:Phi(build(straight,[pat(k,t) for k in range(N)]),which),P0)
        if SE<0: lam_tilt=max(lam_tilt,-SE/SP)
    res[which]=(lam_open,lam_glob,lam_tilt)
    print(f"thresholds ({which:>4}-Phi): anti-open {lam_open:.5f} | ring-global {lam_glob:.5f} | all-tilt {lam_tilt:.5f}")
print()
# ---- lambda placement table ----
W=264.0
print(f"(A) lambda_phys at the registered clock (hbar omega_sw = {W:.0f} MeV, qDP hop):")
print(f"    {'mass assignment':<46} {'m [MeV]':>8} {'lambda':>10}  placement vs [anti-open, all-tilt]")
lo,gl,ti=res['all']; loc,glc,tic=res['core']
def place(l):
    tags=[]
    tags.append("ABOVE all-tilt (fully stabilized)" if l>=ti else
                ("above ring-global" if l>=gl else
                 ("above anti-open only" if l>=lo else "BELOW band (unstabilized)")))
    return tags[0]
for name,m in [("per-CP share of DD-priced element (1408/16)",88.0),
               ("per-qCP if dressing loads 8 qCPs",176.0),
               ("hopping constituent qDP",264.0),
               ("SS-2 free-cage constituent m_const",312.7)]:
    l=lam(m,W)
    print(f"    {name:<46} {m:>8.1f} {l:>10.2e}  {place(l)}")
print()
# ---- inversion ----
print("(B) inversion -- the CP inertia that puts lambda AT each threshold (clock 264):")
for nm,t,tc in [("all-tilt",ti,tic),("ring-global",gl,glc),("anti-open",lo,loc)]:
    print(f"    {nm:<12}: m* = {f2*AHC**2/(4*t*W**2):6.1f} MeV (total-Phi)   {f2*AHC**2/(4*tc*W**2):6.1f} MeV (core-only)")
print(f"    -> the DD-priced per-CP share (88.0 MeV) sits within a few % of the all-tilt")
print(f"       boundary and INSIDE ring-global/anti-open -- boundary-straddling, not decided.")
print()
# ---- clock sensitivity ----
print("(C) clock sensitivity at m = 88.0 MeV:")
for nm,w in [("bare qDP hop",264.0),("residence-suppressed x0.7",0.7*264),
             ("residence-suppressed x0.5",0.5*264),("eDP hop (coat clock)",553.0)]:
    l=lam(88.0,w)
    print(f"    {nm:<28} hbar w = {w:5.0f} MeV: lambda = {l:.2e}  {place(l)}")
print()
print("(D) channels NOT counted in the 2450 thresholds (all favorable-signed):")
print("    - K_switch parametric gain: 2441 deep branch eps = 0.211 IN the Meissner tongue")
print("      [0.179, 0.428]; mid-band k_eff/A ~ 0.12 -- adds stabilization, lowers the")
print("      effective threshold. (Coupled to omega_sw: slower clock raises eps toward the")
print("      tongue top while raising lambda -- the two channels trade off; R1 solves jointly.)")
print("    - strong-sector registry bend stiffness (rigid here) -- positive, unmodeled.")
print("    - coat ponderomotive at its own clock (553): small positive add over core-only.")
print("="*78)
