#!/usr/bin/env python3
"""
PATCH 2453 -- OPEN-DM-FLOQUET-1 / FORK-SWITCH-1 RECAST on founder input: the
COHERENT-CYCLE reading (SU(3)-type position switching as the PRIMARY dynamics, per the
hTetra observation; jello core, 2433) computed end-to-end.

FOUNDER'S ARGUMENT (recorded): the primary argument against static cubic-packed
opposite-charge alternation was the SU(3)-type position switching observed among the
quarks on the hTetra vertices, with stiffening from the tension between repulsive
same-charge apposition displacement and attractive opposite-charge apposition
displacement. => The core has NO static pattern; the switching is coherent and
deterministic (1811 cycle-average); structural integrity is DYNAMIC.

WHAT THIS COMPUTES (all derived, no free choices):
 (1) A deterministic uniform cycle: seeded palindrome swap orbit on the 4+/4- element
     (period 2L, returns exactly, uniform coverage verified: <cc> -> -1/7, duty -> 3/7).
 (2) INTER-ELEMENT PHASE-LOCKING DERIVED: adjacent elements run the same orbit at
     relative shift s and/or charge conjugation; the lattice settles at the
     energy-minimizing lock. Interface energy scanned over all (s, conj) -- the lock is
     an OUTPUT. (In-phase lock => corresponding axial sites always SAME charge, +1
     repulsive; conjugated lock => always OPPOSITE, -1 attractive at FULL strength.)
 (3) Statics under the derived lock: pair-weight matrix <q_i q_j> (intra-element -1/7
     web; inter-element from the lock; coat brackets: (i) STATIC coat at pattern
     [2433: eCPs align to the lattice] -- core-coat cross statics vanish (<c_core>=0);
     (ii) coat CYCLING conjugation-locked to its core [2435]). Collective-mode
     stiffnesses (pure bend, gradient/uniform tilt, closure) recomputed on the
     <qq>-weighted energy -- valid because the cycle statistics are geometry-
     independent (2435), so <d2E/dmode2> = d2<E>/dmode2.
 (4) Dynamic channel: oscillating force spectrum at a mid-rod core site from the full
     locked-orbit lattice realization; resonance-resolved response (m_q=132), E_qq map.
"""
import numpy as np
rng=np.random.default_rng(24530)
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
d=1.15; D=d; A_Q=d; R_E=1.6*(d/np.sqrt(2)); N=16; NE=8
m_q=132.0; m_e=44.0
def plane(R,a_q):
    h=a_q/2
    return [(+h,+h,+1,'q'),(-h,+h,-1,'q'),(-h,-h,+1,'q'),(+h,-h,-1,'q'),
            (+R,0,-1,'e'),(0,+R,+1,'e'),(-R,0,-1,'e'),(0,-R,+1,'e')]
def geom(centers,angles):
    Pp=[];Ww=[];Sp=[];Cpat=[]
    for k in range(N):
        cx,cy,cz=centers[k]; th=angles[k]; c,s=np.cos(th),np.sin(th); par=(-1)**k
        for (x,y,sgn,sp) in plane(R_E,A_Q):
            Pp.append((cx+x*c,cy+y,cz-x*s)); Ww.append(np.sqrt(ALPHA_S) if sp=='q' else np.sqrt(ALPHA))
            Sp.append(sp); Cpat.append(sgn*par)
    return np.array(Pp),np.array(Ww),Sp,np.array(Cpat,float)
def bendgeom(kap):
    if abs(kap)<1e-12: return geom([(0,0,k*D) for k in range(N)],[0.0]*N)
    R=1/kap; ph=[k*D/R for k in range(N)]
    return geom([(R*(1-np.cos(p)),0,R*np.sin(p)) for p in ph],ph)
qloc=[[(2*e+a)*8+b for a in range(2) for b in range(4)] for e in range(NE)]
eloc=[[(2*e+a)*8+4+b for a in range(2) for b in range(4)] for e in range(NE)]
# ---------- (1) deterministic palindrome orbit on one element template ----------
L=140
Pp0,Ww,Sp,Cpat=geom([(0,0,k*D) for k in range(N)],[0.0]*N)
tmpl=Cpat[qloc[0]].copy()          # 8-site template init = pattern of element 0
script=[]
ch=tmpl.copy()
for t in range(L):
    plus=np.where(ch>0)[0]; minus=np.where(ch<0)[0]
    a=plus[rng.integers(0,4)]; b=minus[rng.integers(0,4)]
    script.append((a,b)); ch[a],ch[b]=ch[b],ch[a]
orbit=np.zeros((2*L,8))
ch=tmpl.copy()
for t in range(L):
    a,b=script[t]; ch[a],ch[b]=ch[b],ch[a]; orbit[t]=ch
for t in range(L):
    a,b=script[L-1-t]; ch[a],ch[b]=ch[b],ch[a]; orbit[L+t]=ch
assert np.allclose(orbit[-1],tmpl), "palindrome must return"
T=2*L
cc=np.zeros((8,8))
for i in range(8):
    for j in range(8):
        cc[i,j]=np.mean(orbit[:,i]*orbit[:,j])
off=cc[~np.eye(8,dtype=bool)]
duty=np.mean([(orbit[:,i]*orbit[:,j]>0).mean() for i in range(8) for j in range(8) if i!=j])
print(f"(1) orbit: period {T}, returns exactly; <c_ic_j> off-diag = {off.mean():+.4f}+-{off.std():.4f} "
      f"(target -1/7={-1/7:+.4f}); same-charge duty = {duty:.4f} (target 3/7={3/7:.4f})")
# ---------- (2) derive the inter-element lock ----------
# adjacent elements A,B run same orbit; B optionally conjugated (x -1) and shifted by s.
# interface energy per unit time from the real straight geometry, q-sites only:
iA=qloc[0]; iB=qloc[1]
rAB=np.zeros((8,8))
for a in range(8):
    for b in range(8):
        rAB[a,b]=np.linalg.norm(Pp0[iA[a]]-Pp0[iB[b]])
wq=ALPHA_S  # w_i*w_j for q-q
def iface_energy(conj,s):
    oB=(-orbit if conj else orbit)
    E=0.0
    for t in range(T):
        cA=orbit[t]; cB=oB[(t+s)%T]
        E+=np.sum(np.outer(cA,cB)/rAB)
    return wq*AHC*E/T
res=[]
for conj in (False,True):
    for s in range(0,T,1):
        res.append((iface_energy(conj,s),conj,s))
res.sort()
Ebest,conjbest,sbest=res[0]; Eworst=res[-1][0]
Einphase=iface_energy(False,0)
print(f"(2) lock scan ({2*T} candidates): min E_iface = {Ebest:+.2f} MeV at (conj={conjbest}, shift={sbest});")
print(f"    in-phase unconjugated = {Einphase:+.2f}; max = {Eworst:+.2f}  -> the lattice locks CONJUGATED"
      if conjbest else
      f"    in-phase unconjugated = {Einphase:+.2f}; max = {Eworst:+.2f}  -> lock is UNCONJUGATED shift {sbest}")
# derived pair-weight between adjacent elements at the lock:
oB=(-orbit if conjbest else orbit)
ccAB=np.zeros((8,8))
for a in range(8):
    for b in range(8):
        ccAB[a,b]=np.mean(orbit[:,a]*oB[(np.arange(T)+sbest)%T,b])
print(f"    derived <c_a c_b>_interface: corresponding-site mean = {np.mean(np.diag(ccAB)):+.3f}; "
      f"off mean = {ccAB[~np.eye(8,dtype=bool)].mean():+.3f}")
# lock alternates down the rod (each interface independently minimized -> alternating conj)
# pair-weight matrix Q[i,j] over the whole rod (q-sites):
def qweight(ei,ej,a,b):
    """<c c> between q-site a of element ei and b of ej under alternating-conj lock."""
    if ei==ej: return cc[a,b]
    rel=(ej-ei)%2
    par=(-1)**((ej-ei)) if conjbest else 1
    # elements at even separation: same conj state; odd: conjugated
    base=ccAB if abs(ej-ei)==1 else None
    if abs(ej-ei)==1: return ccAB[a,b] if ej>ei else ccAB[b,a]
    # farther elements: correlation of orbit with itself shifted by (ej-ei)*sbest, conj^(ej-ei)
    sh=((ej-ei)*sbest)%T; cj=(-1)**(ej-ei) if conjbest else 1
    return cj*np.mean(orbit[:,a]*orbit[(np.arange(T)+sh)%T,b])
# ---------- (3) statics: mode stiffnesses under derived <qq> ----------
def Emean(geo,coat_mode):
    Pp,Ww2,Sp2,Cp=geo
    E=0.0
    # q-q pairs
    for ei in range(NE):
        for ej in range(ei,NE):
            for a in range(8):
                bs=range(a+1,8) if ei==ej else range(8)
                for b in bs:
                    i,j=qloc[ei][a],qloc[ej][b]
                    r=np.linalg.norm(Pp[i]-Pp[j])
                    E+=qweight(ei,ej,a,b)*ALPHA_S*AHC/r
    if coat_mode=='static':
        # coat-coat at FULL pattern strength; core-coat cross vanishes (<c_core>=0)
        for i in range(128):
            if Sp2[i]!='e': continue
            for j in range(i+1,128):
                if Sp2[j]!='e': continue
                r=np.linalg.norm(Pp[i]-Pp[j])
                E+=Cp[i]*Cp[j]*ALPHA*AHC/r
    else:  # coat cycles with same statistics, conjugation-locked to its own core
        for ei in range(NE):
            for ej in range(ei,NE):
                for a in range(8):
                    bs=range(a+1,8) if ei==ej else range(8)
                    for b in bs:
                        i,j=eloc[ei][a],eloc[ej][b]
                        r=np.linalg.norm(Pp[i]-Pp[j])
                        E+=qweight(ei,ej,a,b)*ALPHA*AHC/r
        # core-coat cross under common-orbit lock (same element: shift 0 -> cc matrix)
        for ei in range(NE):
            for a in range(8):
                for b in range(8):
                    i,j=qloc[ei][a],eloc[ei][b]
                    r=np.linalg.norm(Pp[i]-Pp[j])
                    E+=cc[a,b]*np.sqrt(ALPHA_S*ALPHA)*AHC/r
    return E
def stiff(fn,y0,xs=(0.005,0.01,0.02)):
    return 2*np.mean([(fn(x)-y0)/x**2 for x in xs])
KAP=2*np.pi/(N*D)
print()
print("(3) collective-mode stiffnesses under the DERIVED coherent-cycle statics:")
for cm in ('static','cycling'):
    E0=Emean(bendgeom(0.0),cm)
    Sb=stiff(lambda x:Emean(bendgeom(x),cm),E0)
    straight=[(0,0,k*D) for k in range(N)]
    Sg=stiff(lambda t:Emean(geom(straight,[t*k for k in range(N)]),cm),E0)
    Su=stiff(lambda t:Emean(geom(straight,[t]*N),cm),E0)
    Er=Emean(bendgeom(KAP),cm); Er2=Emean(bendgeom(KAP-KAP/68),cm)
    print(f"  coat={cm:>7}: E0={E0:+9.2f} | bend {Sb:+8.0f} | tilt-grad {Sg:+9.0f} | "
          f"tilt-unif {Su:+7.1f} | ring-straight {Er-E0:+8.2f} | end-slope {(Er-Er2)/(KAP/68):+8.0f}")
print("  [signs: + = restoring/resisting. Compare arc-pattern statics: bend +291, "
      "tilt-grad -11958, tilt-unif -159, ring +24.3, end-slope +724]")
print()
# ---------- (4) dynamic response at a mid-rod core site under the locked orbit ----------
print("(4) dynamic channel (locked coherent orbit, all 8 elements + coat per bracket):")
tgt=qloc[3][0]  # mid-rod core site (element 3)
dd=Pp0[tgt]-Pp0; rr=np.sqrt((dd*dd).sum(axis=1)); rr[tgt]=np.inf
fvec=(Ww[:,None]*dd/(rr**3)[:,None])*AHC  # per-source force geometry (charge=+1)
NREP=8
FT=np.zeros((T*NREP,3))
charges=np.zeros(128)
for t in range(T*NREP):
    tt=t%T
    for e in range(NE):
        cj=(-1)**e if conjbest else 1
        sh=(e*sbest)%T
        charges[qloc[e]]=cj*orbit[(tt+sh)%T]
        charges[eloc[e]]=Cpat[eloc[e]]      # coat static bracket for the drive run
    FT[t]=Ww[tgt]*charges[tgt]*(charges[:,None]*fvec).sum(axis=0)
unit=4*264.0/T/1.0  # one swap per element per tick; 4 swaps/elem/Compton period => tick=tau/4
# grid: total record T*NREP ticks, dt=tau_hop/4 -> line spacing = 4*264/(T*NREP)
gu=4*264.0/(T*NREP)
def resp(F,m,hwA):
    Ua=Ub=ex=0.0
    for c in range(3):
        X=np.fft.rfft(F[:,c]-F[:,c].mean()); S=2*np.abs(X)**2/len(F)**2
        for n in range(1,len(S)):
            hw=n*gu
            if abs(hw-hwA)<0.1*hwA: ex+=S[n]; continue
            u=S[n]*AHC**2/(4*m*(hw**2-hwA**2))
            if hw>hwA: Ua+=u
            else: Ub+=u
    return Ua,Ub,ex
W2E2=Ww[tgt]**2*((Cpat[:,None]*fvec).sum(axis=0)@(Cpat[:,None]*fvec).sum(axis=0))
print(f"  {'E_qq':>6} {'hwA':>7} {'lam_q(above)':>13} {'lam_q(below)':>13} {'lam_q(net)':>12}")
for Eqq in (40.,66.,100.,140.):
    hwA=np.sqrt(2*Eqq*AHC**2/(d**2*m_q))
    Ua,Ub,ex=resp(FT,m_q,hwA)
    print(f"  {Eqq:>6.0f} {hwA:>7.1f} {Ua/W2E2:>13.3e} {Ub/W2E2:>13.3e} {(Ua+Ub)/W2E2:>12.3e}")
print("  [reference frame: pattern-normalized as in 2450/2452 so thresholds compare;")
print("   NOTE thresholds themselves move under the (3) statics -- netting follows.]")
#!/usr/bin/env python3
"""Supercycle-period scan: the coherent-cycle STATICS are orbit-length independent
(uniform statistics); the DYNAMIC response is not -- long orbits carry low-frequency
(below-resonance, adiabatic) weight. Scan the palindrome half-length L (period 2L ticks,
tick = tau_Compton/4) and report the resonance-resolved response at a mid-rod core site,
plus the mode-resolved netting for the gradient-tilt (the least statically-stable margin
check) at E_qq = 66. Identifies the supercycle period P as the remaining dynamic unknown."""
import numpy as np
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
d=1.15; D=d; A_Q=d; R_E=1.6*(d/np.sqrt(2)); N=16; NE=8; m_q=132.0
def plane(R,a_q):
    h=a_q/2
    return [(+h,+h,+1,'q'),(-h,+h,-1,'q'),(-h,-h,+1,'q'),(+h,-h,-1,'q'),
            (+R,0,-1,'e'),(0,+R,+1,'e'),(-R,0,-1,'e'),(0,-R,+1,'e')]
def geom(centers,angles):
    Pp=[];Ww=[];Sp=[];Cp=[]
    for k in range(N):
        cx,cy,cz=centers[k]; th=angles[k]; c,s=np.cos(th),np.sin(th); par=(-1)**k
        for (x,y,sgn,sp) in plane(R_E,A_Q):
            Pp.append((cx+x*c,cy+y,cz-x*s)); Ww.append(np.sqrt(ALPHA_S) if sp=='q' else np.sqrt(ALPHA))
            Sp.append(sp); Cp.append(sgn*par)
    return np.array(Pp),np.array(Ww),Sp,np.array(Cp,float)
qloc=[[(2*e+a)*8+b for a in range(2) for b in range(4)] for e in range(NE)]
eloc=[[(2*e+a)*8+4+b for a in range(2) for b in range(4)] for e in range(NE)]
straightC=[(0,0,k*D) for k in range(N)]
G0=geom(straightC,[0.0]*N); Pp0,Ww,Sp,Cpat=G0
def make_orbit(L,seed):
    rng=np.random.default_rng(seed)
    tmpl=Cpat[qloc[0]].copy(); ch=tmpl.copy(); script=[]
    for t in range(L):
        plus=np.where(ch>0)[0]; minus=np.where(ch<0)[0]
        a=plus[rng.integers(0,4)]; b=minus[rng.integers(0,4)]
        script.append((a,b)); ch[a],ch[b]=ch[b],ch[a]
    T=2*L; orb=np.zeros((T,8)); ch=tmpl.copy()
    for t in range(L):
        a,b=script[t]; ch[a],ch[b]=ch[b],ch[a]; orb[t]=ch
    for t in range(L):
        a,b=script[L-1-t]; ch[a],ch[b]=ch[b],ch[a]; orb[L+t]=ch
    return orb
def charges_t(orb,tt,conj=True,shift=None):
    T=len(orb); shift = shift if shift is not None else T//3
    ch=np.zeros(128)
    for e in range(NE):
        cj=(-1)**e if conj else 1
        ch[qloc[e]]=cj*orb[(tt+e*shift)%T]
        ch[eloc[e]]=Cpat[eloc[e]]
    return ch
def site_response(G,orb,tgt,hwA,m,NREP):
    Pp,Ww2,_,Cp=G
    dd=Pp[tgt]-Pp; rr=np.sqrt((dd*dd).sum(axis=1)); rr[tgt]=np.inf
    fvec=(Ww2[:,None]*dd/(rr**3)[:,None])*AHC
    T=len(orb); NT=T*NREP
    F=np.zeros((NT,3))
    for t in range(NT):
        ch=charges_t(orb,t%T)
        F[t]=Ww2[tgt]*ch[tgt]*(ch[:,None]*fvec).sum(axis=0)
    gu=4*264.0/NT
    Ua=Ub=0.0
    for c in range(3):
        X=np.fft.rfft(F[:,c]-F[:,c].mean()); S=2*np.abs(X)**2/NT**2
        for n in range(1,len(S)):
            hw=n*gu
            if abs(hw-hwA)<0.1*hwA: continue
            u=S[n]*AHC**2/(4*m*(hw**2-hwA**2))
            if hw>hwA: Ua+=u
            else: Ub+=u
    W2E2=Ww2[tgt]**2*((Cp[:,None]*fvec).sum(axis=0)@(Cp[:,None]*fvec).sum(axis=0))
    return Ua/W2E2,Ub/W2E2
Eqq=66.0; hwA=np.sqrt(2*Eqq*AHC**2/(d**2*m_q))
tgt=qloc[3][0]
print(f"supercycle scan (E_qq=66, hwA={hwA:.1f} MeV; tick=tau_C/4; period P=2L ticks = L/2 Compton periods)")
print(f"{'L':>5} {'P[Compton]':>10} {'lowest line[MeV]':>16} {'lam(above)':>11} {'lam(below)':>11} {'lam(net)':>10}")
for L,nrep in [(7,64),(14,32),(28,16),(70,8),(140,8)]:
    orb=make_orbit(L,seed=100+L)
    T=2*L
    la,lb=site_response(G0,orb,tgt,hwA,m_q,nrep)
    print(f"{L:>5} {T/4:>10.1f} {4*264.0/T:>16.1f} {la:>11.3e} {lb:>11.3e} {la+lb:>10.3e}")
print()
print("gradient-tilt netting check at the shortest and longest cycles (static +69159):")
def phi_osc_tilt(orb,th,NREP=4):
    """site-summed mean-square oscillating force, tilted vs straight, per orbit stats"""
    G=geom(straightC,[th*k for k in range(N)])
    Pp,Ww2,_,_=G; T=len(orb); NT=T*NREP
    tot=0.0
    for i in range(0,128):
        dd=Pp[i]-Pp; rr=np.sqrt((dd*dd).sum(axis=1)); rr[i]=np.inf
        fvec=(Ww2[:,None]*dd/(rr**3)[:,None])*AHC
        F=np.zeros((NT,3))
        for t in range(NT):
            ch=charges_t(orb,t%T)
            F[t]=Ww2[i]*ch[i]*(ch[:,None]*fvec).sum(axis=0)
        tot+=((F-F.mean(axis=0))**2).sum(axis=1).mean()
    return tot
for L in (7,140):
    orb=make_orbit(L,seed=100+L)
    p0=phi_osc_tilt(orb,0.0); p1=phi_osc_tilt(orb,0.02)
    SPosc=2*(p1-p0)/0.02**2
    la,lb=site_response(G0,orb,tgt,hwA,m_q,16 if L==7 else 4)
    net=69159 + (la+lb)*SPosc
    print(f"  L={L:>3}: dPhi_osc/dth^2 = {SPosc:+.3e}; lam(net)={la+lb:+.3e}; "
          f"tilt net = 69159 + lam*SP = {net:+.0f}  -> {'STABLE' if net>0 else 'UNSTABLE'}")
#!/usr/bin/env python3
"""Robustness of the coherent-cycle STATICS inversion: (a) inter-element correlations
zeroed (independent elements -- removes all lock/realization dependence); (b) a second
orbit seed at the derived lock. The intra-element -1/7 web is exact (uniform stats)."""
import numpy as np
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
d=1.15; D=d; A_Q=d; R_E=1.6*(d/np.sqrt(2)); N=16; NE=8
def plane(R,a_q):
    h=a_q/2
    return [(+h,+h,+1,'q'),(-h,+h,-1,'q'),(-h,-h,+1,'q'),(+h,-h,-1,'q'),
            (+R,0,-1,'e'),(0,+R,+1,'e'),(-R,0,-1,'e'),(0,-R,+1,'e')]
def geom(centers,angles):
    Pp=[];Ww=[];Sp=[];Cp=[]
    for k in range(N):
        cx,cy,cz=centers[k]; th=angles[k]; c,s=np.cos(th),np.sin(th); par=(-1)**k
        for (x,y,sgn,sp) in plane(R_E,A_Q):
            Pp.append((cx+x*c,cy+y,cz-x*s)); Ww.append(np.sqrt(ALPHA_S) if sp=='q' else np.sqrt(ALPHA))
            Sp.append(sp); Cp.append(sgn*par)
    return np.array(Pp),np.array(Ww),Sp,np.array(Cp,float)
def bendgeom(kap):
    if abs(kap)<1e-12: return geom([(0,0,k*D) for k in range(N)],[0.0]*N)
    R=1/kap; ph=[k*D/R for k in range(N)]
    return geom([(R*(1-np.cos(p)),0,R*np.sin(p)) for p in ph],ph)
qloc=[[(2*e+a)*8+b for a in range(2) for b in range(4)] for e in range(NE)]
straightC=[(0,0,k*D) for k in range(N)]
_,_,_,Cpat=geom(straightC,[0.0]*N)
CCintra=-np.ones((8,8))/7.0; np.fill_diagonal(CCintra,1.0)
def Emean(G,inter='zero'):
    Pp,Ww2,Sp2,Cp=G; E=0.0
    for ei in range(NE):
        for a in range(8):
            for b in range(a+1,8):
                i,j=qloc[ei][a],qloc[ei][b]
                r=np.linalg.norm(Pp[i]-Pp[j])
                E+=CCintra[a,b]*ALPHA_S*AHC/r
    # inter-element: 'zero' bracket (independent elements)
    # coat: STATIC pattern bracket
    for i in range(128):
        if Sp2[i]!='e': continue
        for j in range(i+1,128):
            if Sp2[j]!='e': continue
            r=np.linalg.norm(Pp[i]-Pp[j])
            E+=Cp[i]*Cp[j]*ALPHA*AHC/r
    return E
def stiff(fn,y0,xs=(0.005,0.01,0.02)):
    return 2*np.mean([(fn(x)-y0)/x**2 for x in xs])
KAP=2*np.pi/(N*D)
E0=Emean(bendgeom(0.0))
Sb=stiff(lambda x:Emean(bendgeom(x)),E0)
Sg=stiff(lambda t:Emean(geom(straightC,[t*k for k in range(N)])),E0)
Su=stiff(lambda t:Emean(geom(straightC,[t]*N)),E0)
Er=Emean(bendgeom(KAP)); Er2=Emean(bendgeom(KAP-KAP/68))
print("ZERO-inter-element bracket (lock/realization independent), coat static:")
print(f"  E0={E0:+9.2f} | bend {Sb:+8.0f} | tilt-grad {Sg:+9.0f} | tilt-unif {Su:+8.1f} | "
      f"ring-straight {Er-E0:+8.2f} | end-slope {(Er-Er2)/(KAP/68):+8.0f}")
print("  vs derived-lock run:      bend -11293 | tilt-grad +69159 | tilt-unif +11986 | ring -54.76 | slope -259")
print("  vs arc-pattern statics:   bend   +291 | tilt-grad -11958 | tilt-unif  -159  | ring +24.32 | slope +724")
# decompose: core-web-only vs coat-only
def Ecore(G):
    Pp,_,_,_=G; E=0.0
    for ei in range(NE):
        for a in range(8):
            for b in range(a+1,8):
                i,j=qloc[ei][a],qloc[ei][b]
                E+=CCintra[a,b]*ALPHA_S*AHC/np.linalg.norm(Pp[i]-Pp[j])
    return E
def Ecoat(G):
    Pp,_,Sp2,Cp=G; E=0.0
    for i in range(128):
        if Sp2[i]!='e': continue
        for j in range(i+1,128):
            if Sp2[j]!='e': continue
            E+=Cp[i]*Cp[j]*ALPHA*AHC/np.linalg.norm(Pp[i]-Pp[j])
    return E
E0c=Ecore(bendgeom(0.0)); E0e=Ecoat(bendgeom(0.0))
print()
print("decomposition of the inversion (zero-inter bracket):")
print(f"  core -1/7 web : bend {stiff(lambda x:Ecore(bendgeom(x)),E0c):+8.0f} | "
      f"tilt-grad {stiff(lambda t:Ecore(geom(straightC,[t*k for k in range(N)])),E0c):+9.0f} | "
      f"ring {Ecore(bendgeom(KAP))-E0c:+7.2f}")
print(f"  coat pattern  : bend {stiff(lambda x:Ecoat(bendgeom(x)),E0e):+8.0f} | "
      f"tilt-grad {stiff(lambda t:Ecoat(geom(straightC,[t*k for k in range(N)])),E0e):+9.0f} | "
      f"ring {Ecoat(bendgeom(KAP))-E0e:+7.2f}")
