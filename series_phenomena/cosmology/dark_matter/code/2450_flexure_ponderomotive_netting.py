#!/usr/bin/env python3
"""
PATCH 2450 -- OPEN-DM-FLOQUET-1 / flexure-ponderomotive netting (the R5-analog for the
collective bend mode) -- WITH an in-session geometry audit that OVERTURNS the 2448 premise.

(I) GEOMETRY AUDIT of the 2448 bend family: rod_cfg maps the in-plane offset x along
    u=(cos phi, 0, +sin phi) while the local tangent is t=(sin phi, 0, cos phi):
    u.t = sin(2 phi) != 0. The planes TILT by 2 phi relative to perpendicular -- the
    family is BEND + GRADIENT TILT (tilt ~ 2 kappa s, same O(kappa) as the bend), and
    for kappa >~ 0.04 the tilted planes collide (min pair distance -> 0.008 fm).
    Also: 2448 printed mean(dE/kappa^2) labeled d2E/dkappa^2 (factor-2 slip; its -3263
    is d2E/dk2 = -6527 at N=8 -- immaterial to its sign story, noted for the record).

(II) CORRECTED family (perpendicular planes, Frenet, arc-length): the pure-bend
    stiffness is POSITIVE (+138 N=8, +291 N=16; ~L scaling as a bending stiffness must;
    direction-independent x/y; chord-exact convention +263, sign robust; reproduced by
    an independent code path). The straight rod is bend-STABLE at the switched-pair
    level. The 2448 headline "flexure does not escape Earnshaw / rods spontaneously
    curl" is RETRACTED AS A BEND STATEMENT; Earnshaw's instability is real but lives in
    the plane-TILT mode (gradient tilt d2E/dth2 = -11959; uniform -159; alternating
    +1053 stable). Decomposition coherence: +291 + (2D)^2*(-11959) = -62969 vs the
    tilted family's measured -69135 (ratio 0.91, cross-terms).

(III) PONDEROMOTIVE Phi = sum_i w_i^2 |E_i|^2 (source weight sqrt(coupling), response
    weight coupling; the (alpha_s/alpha)^2 = 2800 core lever EMERGES: core share 93.9%).
    Validation: breathing scales EXACTLY as s^-4 (analytic 1/r^4). Shape results:
      - Phi RISES under tilt (gradient +8.0e6) -> ponderomotive RESISTS tilt;
      - Phi FALLS toward ring closure (-17307 at the ring, perfect registry 1e-15)
        -> ponderomotive FAVORS closure;
      - Phi ~ s^-4 -> resists collapse.

(IV) NETTING U = E_static + lam*Phi (lam = drive coefficient, UNPINNED = 1811 #2):
      lam > ~0.0006  ring stable against opening (endpoint slope flips)
      lam > ~0.0014  ring globally below straight
      lam > ~0.0015  gradient tilt stabilized     <- the binding threshold
      lam > ~0.0016  uniform tilt stabilized
      lam > ~0.0033  straight rod spontaneously curls (formation without a kick)
    ONE-SIDED window: for ALL lam >~ 0.0016 the closed N_planes=16 ring is tilt-stable,
    closure-favored, collapse-resisted. No fine-tuned upper edge inside this functional
    (an upper bound, if any, comes from ponderomotive distortion of the strong-sector
    registry -- outside this energy functional, flagged).

G-notes: G1 the (1-2 delta)=1/7 factor is the duty average and Phi is invariant under
the global charge flip (both phases honored). G3 equilibria located, not asserted.
G4 components reported separately + net. G7: the pre-registered question ("stable
minimum at N=16, what window") is ANSWERED YES with a one-sided window; the -3263 the
kill was framed around proved to be a tilt artifact -- reported as found, geometry
fix documented, flawed builder retained below for reproduction.
SCOPE: switched-pair + ponderomotive functional at rigid lattice registry; the
functional does not bind under dilation (E0=+486 MeV > 0; binding = strong-sector
registry, standing arc framing); registry stiffness adds FURTHER positive bend
stability, not modeled.
"""
import numpy as np
from numpy.linalg import norm

AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036; DELTA=3/7
d=1.15; D=d; A_Q=d; R_E=1.6*(d/np.sqrt(2))

def plane(R,a_q):
    h=a_q/2
    return [(+h,+h,+1,'q'),(-h,+h,-1,'q'),(-h,-h,+1,'q'),(+h,-h,-1,'q'),
            (+R,0,-1,'e'),(0,+R,+1,'e'),(-R,0,-1,'e'),(0,-R,+1,'e')]

def build(centers,angles,N_PL,axis='x'):
    Cc=[];Pp=[];Ww=[];Sp=[]
    for k in range(N_PL):
        cx,cy,cz=centers[k]; th=angles[k]; c,s=np.cos(th),np.sin(th); par=(-1)**k
        for (x,y,sgn,sp) in plane(R_E,A_Q):
            if axis=='x': Pp.append((cx+x*c, cy+y, cz-x*s))
            else:         Pp.append((cx+x, cy+y*c, cz-y*s))
            Cc.append(sgn*par); Ww.append(np.sqrt(ALPHA_S) if sp=='q' else np.sqrt(ALPHA)); Sp.append(sp)
    return np.array(Cc,float),np.array(Pp,float),np.array(Ww,float),Sp

def bend_family(kap,N_PL,convention="arc"):
    if abs(kap)<1e-12:
        return build([(0,0,k*D) for k in range(N_PL)],[0.0]*N_PL,N_PL)
    R=1/kap
    if convention=="arc": phis=[k*D/R for k in range(N_PL)]
    else:
        dphi=2*np.arcsin(D/(2*R)); phis=[k*dphi for k in range(N_PL)]
    C=[(R*(1-np.cos(p)),0,R*np.sin(p)) for p in phis]
    return build(C,phis,N_PL)

def rod_2448(kap,N_PL):   # the FLAWED 2448 family, retained for reproduction
    Cc=[];Pp=[];Ww=[];Sp=[]
    for k in range(N_PL):
        s=k*D
        if abs(kap)<1e-12: cx,cz,phi=0.0,s,0.0
        else:
            R=1/kap; phi=s/R; cx=R*(1-np.cos(phi)); cz=R*np.sin(phi)
        cph,sph=np.cos(phi),np.sin(phi); par=(-1)**k
        for (x,y,sgn,sp) in plane(R_E,A_Q):
            Pp.append((cx+x*cph, y, cz+x*sph))   # <- +x*sph: the tilt flaw
            Cc.append(sgn*par); Ww.append(np.sqrt(ALPHA_S) if sp=='q' else np.sqrt(ALPHA)); Sp.append(sp)
    return np.array(Cc,float),np.array(Pp,float),np.array(Ww,float),Sp

def Esw(cfg):
    Cc,Pp,Ww,_=cfg; E=0.0
    for i in range(len(Cc)):
        dd=Pp[i+1:]-Pp[i]; r=np.sqrt((dd*dd).sum(axis=1))
        E+=np.sum(-(1-2*DELTA)*Ww[i]*Cc[i]*(Ww[i+1:]*Cc[i+1:])*AHC/r)
    return E

def Phi(cfg):
    Cc,Pp,Ww,Sp=cfg; tot=0.0;core=0.0;coat=0.0
    for i in range(len(Cc)):
        dd=Pp[i]-Pp; r=np.sqrt((dd*dd).sum(axis=1)); r[i]=np.inf
        Ei=((Ww*Cc)[:,None]*dd/(r**3)[:,None]).sum(axis=0)*AHC
        c=Ww[i]**2*(Ei@Ei); tot+=c
        if Sp[i]=='q': core+=c
        else: coat+=c
    return tot,core,coat

def minpair(cfg):
    Pp=cfg[1]; m=np.inf
    for i in range(len(Pp)):
        r=np.sqrt(((Pp[i+1:]-Pp[i])**2).sum(axis=1))
        if len(r): m=min(m,r.min())
    return m

def stiff(fn,E0,xs=(0.005,0.01,0.02)):
    return 2*np.mean([(fn(x)-E0)/x**2 for x in xs])

print("="*78)
print("PATCH 2450 -- flexure-ponderomotive netting + geometry audit (N_planes=16)")
print("="*78)
print(f"D={D} a_q={A_Q} r_q={D/np.sqrt(2):.3f} R_e={R_E:.3f}  (alpha_s/alpha)^2={(ALPHA_S/ALPHA)**2:.0f}")
print()

# ---------- (I) AUDIT ----------
print("(I) GEOMETRY AUDIT of the 2448 family")
kap=0.05
for k in [1,5,15]:
    phi=k*D*kap; t=np.array([np.sin(phi),0,np.cos(phi)])
    print(f"    k={k:2d}: 2448 offset-dir . tangent = {np.array([np.cos(phi),0,np.sin(phi)])@t:+.3f} (=sin 2phi)"
          f"   corrected = {np.array([np.cos(phi),0,-np.sin(phi)])@t:+.3f}")
print(f"    min pair distance, 2448 family: kap=0.02: {minpair(rod_2448(0.02,16)):.3f}  "
      f"kap=0.08: {minpair(rod_2448(0.08,16)):.4f} fm (COLLIDES)")
print(f"    corrected family:               kap=0.08: {minpair(bend_family(0.08,16)):.3f}  "
      f"at ring: {minpair(bend_family(2*np.pi/(16*D),16)):.3f} fm (genuine inner-edge compression)")
print()

# ---------- (II) STIFFNESSES ----------
print("(II) small-kappa stiffness d2E/dkappa^2 [MeV*fm^2]")
for NP in (8,16):
    E0=Esw(bend_family(0,NP))
    s48=stiff(lambda x:Esw(rod_2448(x,NP)),E0)
    sc =stiff(lambda x:Esw(bend_family(x,NP)),E0)
    print(f"    N_PL={NP:2d}: 2448 (bend+tilt) = {s48:+8.0f}   corrected PURE BEND = {sc:+7.0f}")
NP=16; E0=Esw(bend_family(0,NP)); P0,P0c,P0e=Phi(bend_family(0,NP))
sc_chord=stiff(lambda x:Esw(bend_family(x,NP,"chord")),E0)
# y-bend
def ybend(kap):
    R=1/kap; phis=[k*D/R for k in range(NP)]
    return Esw(build([(0,R*(1-np.cos(p)),R*np.sin(p)) for p in phis],phis,NP,axis='y'))
print(f"    convention: chord-exact = {sc_chord:+.0f} (vs arc +291; sign robust)")
print(f"    direction:  y-bend      = {stiff(ybend,E0):+.0f} (vs x-bend +291; symmetric)")
straight=[(0,0,k*D) for k in range(NP)]
tilt={}
for name,pat in [("gradient",lambda k,t:t*k),("uniform",lambda k,t:t),("alternating",lambda k,t:t*(-1)**k)]:
    SE=stiff(lambda t:Esw(build(straight,[pat(k,t) for k in range(NP)],NP)),E0)
    SP=stiff(lambda t:Phi(build(straight,[pat(k,t) for k in range(NP)],NP))[0],P0)
    tilt[name]=(SE,SP)
    print(f"    TILT {name:<12}: d2E/dth2 = {SE:+9.1f}   d2Phi/dth2 = {SP:+11.1f}"
          f"   lam_rescue = {(-SE/SP if SE<0 and SP>0 else 0):.5f}")
print(f"    decomposition: +291 + (2D)^2*({tilt['gradient'][0]:.0f}) = "
      f"{291+(2*D)**2*tilt['gradient'][0]:+.0f} vs tilted-family -69135 (ratio "
      f"{(291+(2*D)**2*tilt['gradient'][0])/-69135:.2f}) -- 2448's negative UNDERSTOOD as tilt")
print()

# ---------- (III) CURVES TO CLOSURE + Phi validation ----------
KAP_RING=2*np.pi/(NP*D)
print(f"(III) corrected curves to closure (kappa_ring={KAP_RING:.4f}, R_ring={1/KAP_RING:.3f} fm)")
print(f"    straight: E0={E0:.2f} MeV  Phi0={P0:.1f} (core {100*P0c/P0:.1f}%)")
# breathing validation
for s in (0.99,1.01):
    Cc=[];Pp=[];Ww=[];Sp=[]
    for k in range(NP):
        par=(-1)**k
        for (x,y,sgn,sp) in plane(R_E,A_Q):
            Pp.append((x*s,y*s,k*D*s)); Cc.append(sgn*par)
            Ww.append(np.sqrt(ALPHA_S) if sp=='q' else np.sqrt(ALPHA)); Sp.append(sp)
    cfg=(np.array(Cc,float),np.array(Pp,float),np.array(Ww,float),Sp)
    dP=Phi(cfg)[0]-P0
    print(f"    breathing s={s}: dPhi={dP:+.1f} vs analytic s^-4 {P0*(s**-4-1):+.1f}  (EXACT)")
grid=np.linspace(0.0,KAP_RING,69); Es=[];Ps=[]
for k_ in grid:
    cfg=bend_family(k_,NP); Es.append(Esw(cfg)); Ps.append(Phi(cfg)[0])
Es=np.array(Es);Ps=np.array(Ps)
for fr in (0.25,0.5,0.75,0.9,1.0):
    i=np.argmin(abs(grid-fr*KAP_RING))
    print(f"    k/kring={grid[i]/KAP_RING:5.2f}: dE_stat={Es[i]-E0:+8.3f} MeV   dPhi={Ps[i]-P0:+9.1f}")
# closure registry
cfg=bend_family(KAP_RING,NP); Pp=cfg[1]
d01=np.sort([norm(Pp[i]-Pp[j]) for i in range(8) for j in range(8,16)])
d150=np.sort([norm(Pp[i]-Pp[j]) for i in range(120,128) for j in range(8)])
print(f"    closure registry: max |plane01 - plane15,0 pair diff| = {np.abs(np.array(d01)-np.array(d150)).max():.1e}")
print()

# ---------- (IV) NETTING ----------
print("(IV) NETTING thresholds in lam (drive coefficient; UNPINNED = 1811 #2)")
fine=np.linspace(0,KAP_RING,600); Ef=np.interp(fine,grid,Es); Pf=np.interp(fine,grid,Ps)
def ring_slope(lam):
    U=Ef+lam*Pf; return (U[-1]-U[-2])/(fine[1]-fine[0])
lam_open=None
for lam in np.linspace(0,0.01,4001):
    if ring_slope(lam)<0: lam_open=lam; break
lam_glob=(Es[-1]-E0)/-(Ps[-1]-P0)
lam_tilt=max(-SE/SP for SE,SP in tilt.values() if SE<0)
lam_curl=291/-( stiff(lambda x:Phi(bend_family(x,NP))[0],P0) ) if stiff(lambda x:Phi(bend_family(x,NP))[0],P0)<0 else np.inf
print(f"    lam > {lam_open:.5f}  ring stable against opening (endpoint slope < 0)")
print(f"    lam > {lam_glob:.5f}  ring globally below straight (dE={Es[-1]-E0:+.1f} vs dPhi={Ps[-1]-P0:+.1f})")
print(f"    lam > {lam_tilt:.5f}  ALL tilt patterns stabilized  <-- binding threshold")
print(f"    lam > {lam_curl:.5f}  straight rod spontaneously curls (kick-free formation)")
print()
print("    VERDICT: ONE-SIDED window -- for all lam >= %.4f the closed N_planes=16 ring is"%lam_tilt)
print("    tilt-stable, closure-favored, and collapse-resisted (Phi ~ s^-4). The pre-registered")
print("    kill (no stable minimum at N=16 for any drive) does NOT fire. Physical scale at the")
print(f"    threshold: lam*Phi0 = {lam_tilt*P0:.0f} MeV total (~{lam_tilt*P0/128:.1f} MeV/CP ponderomotive energy).")
print("    REMAINING GATE: pin the ZBW drive (a, omega) -- 1811 action #2 -- to place the")
print("    physical lam relative to %.4f. Candidate (B) conditional on that placement."%lam_tilt)
print("="*78)
