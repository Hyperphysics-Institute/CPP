#!/usr/bin/env python3
"""
PATCH 2557 -- RE-REGISTRATION EXECUTION under the 2556 founder adjudication.

Re-runs the registered ring-context dance observables under reach-S (in-plane = plane
membership, the spec-faithful classifier). Scope: (1) the ENDBOND-3 <Ep>(kappa) curve
(7-point grid, 3 dt, both FREF conventions); (2) the FORM-L-1 E_close(L) table (7 L,
3 dt). Straight-rod and single-plane runs recomputed alongside (reach-S == reach-G there
by construction; equality is ASSERTED numerically as a control).

PRE-REGISTERED READINGS (frozen here, before any output):
  P1: the ENDBOND-3 knob-free extraction re-applies verbatim (grid argmax; barrier-free
      => E_close = <E>(0)-<E>(ring)). The corrected pin band REPLACES [128.9,137.5] in
      the registered lineage; the reach-G band is annotated superseded-by-correction.
      G1/G2 are re-stated for the corrected band (same gates, same order -- this is the
      pre-registered re-gating, not post-hoc): G1 = [40,170] membership; G2 = 102.
  P2: the FORM-L-1 frozen readings re-apply verbatim (floor +/-2; sign-change bracket;
      union-stable argmax). Structure statements update to the corrected table.
  P3: no other quantity moves; kT_form untouched; 79.5% untouched (direction favorable;
      promotion basis = ring-rod sign consistency, which can only strengthen or hold).
"""
import numpy as np, time

AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
d=1.15; A_Q=d; D=d
r_q=A_Q/np.sqrt(2); R_E=1.6*r_q
A_QQ=AHC/264.0; A_EE=AHC/553.0; A_QE=np.sqrt(A_QQ*A_EE)
TAUC=2*np.pi*AHC/264.0
KQ_PIN, KE_PIN = 132.0, 44.0
FLOOR=2.0

def scaffold_L(L, kap):
    S=[]; h=A_Q/2
    q=[(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)]
    for k in range(L):
        if abs(kap)<1e-12: cx,cz,phi=0.0,k*D,0.0
        else:
            R=1.0/kap; phi=k*D/R; cx=R*(1-np.cos(phi)); cz=R*np.sin(phi)
        c,s=np.cos(phi),np.sin(phi); par=(-1)**k
        for (x,y,sg) in q: S.append(((cx+x*c,y,cz-x*s),sg*par,'q'))
        for (x,y,sg) in q:
            n=np.hypot(x,y); X,Y=R_E*x/n,R_E*y/n
            S.append(((cx+X*c,Y,cz-X*s),-sg*par,'e'))
    P=np.array([s[0] for s in S],float); C=np.array([float(s[1]) for s in S])
    return P,C,[s[2] for s in S]

def build_reach_S(P,C,SP):   # SPEC-FAITHFUL (2556 adjudication): in-plane = plane index
    NS=len(P); reach=[]
    for i in range(NS):
        dd=P-P[i]; r=np.sqrt((dd*dd).sum(axis=1)); r[i]=np.inf
        ki=i//8
        if SP[i]=='q':
            inpl=[j for j in range(NS) if SP[j]=='q' and j//8==ki and r[j]<1.8]
            axl=[j for j in range(NS) if SP[j]=='q' and j//8!=ki and r[j]<1.3]
            ecp=[j for j in range(NS) if SP[j]=='e' and r[j]<0.6]
            reach.append(sorted(set(inpl+axl))[:5]+ecp)
        else:
            eopp=sorted([j for j in range(NS) if SP[j]=='e' and 0<r[j]<2.6],key=lambda j:r[j])[:4]
            qown=[j for j in range(NS) if SP[j]=='q' and r[j]<0.6]
            reach.append(eopp+qown)
    return reach

def build_reach_G(P,C,SP):   # superseded-for-rings geometric proxy (control equality on rods)
    NS=len(P); reach=[]
    for i in range(NS):
        dd=P-P[i]; r=np.sqrt((dd*dd).sum(axis=1)); r[i]=np.inf
        if SP[i]=='q':
            inpl=[j for j in range(NS) if SP[j]=='q' and abs(P[j][2]-P[i][2])<0.5*D and r[j]<1.8]
            axl=[j for j in range(NS) if SP[j]=='q' and j not in inpl and r[j]<1.3]
            ecp=[j for j in range(NS) if SP[j]=='e' and r[j]<0.6]
            reach.append(sorted(set(inpl+axl))[:5]+ecp)
        else:
            eopp=sorted([j for j in range(NS) if SP[j]=='e' and 0<r[j]<2.6],key=lambda j:r[j])[:4]
            qown=[j for j in range(NS) if SP[j]=='q' and r[j]<0.6]
            reach.append(eopp+qown)
    return reach

def soft_a(si,sj):
    if si=='q' and sj=='q': return A_QQ
    if si=='e' and sj=='e': return A_EE
    return A_QE
def amat(SP):
    NS=len(SP); A=np.zeros((NS,NS))
    for i in range(NS):
        for j in range(NS): A[i,j]=soft_a(SP[i],SP[j])
    return A
def ssv_vectors(P,C,SP):
    W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP])
    qw=W*C
    dd=P[:,None,:]-P[None,:,:]; r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
    A=amat(SP); return ((np.outer(qw,qw)/(r2+A*A)**1.5)[:,:,None]*dd).sum(axis=1)*(-AHC)
def qw_of(SP,C):
    W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP]); return W*C

def dance_v8(H,C,SP,FREF,dtfrac,reachfn,kscale=1.0,TC=60,burn=0.15):
    A=amat(SP); qw=qw_of(SP,C); NS=len(H)
    QW=np.outer(qw,qw); A2=A*A
    reach=reachfn(H,C,SP)
    oppr=[np.array([j for j in reach[i] if C[j]*C[i]<0],dtype=int) for i in range(NS)]
    for i in range(NS):
        if len(oppr[i])==0: oppr[i]=np.where(C*C[i]<0)[0]
    isE=np.array([s=='e' for s in SP])
    kap=np.where(isE, KE_PIN, KQ_PIN)*kscale
    mu=1.0/FREF
    dt=TAUC*dtfrac; nst=int(TC*TAUC/dt)
    eA=np.exp(-dt/(kap*mu)) if kscale>0 else np.zeros(NS)
    P=H.copy()
    tgt=np.array([oppr[i][np.argmin(np.linalg.norm(H[oppr[i]]-H[i],axis=1))] for i in range(NS)])
    last=-np.ones(NS,int); out=np.ones(NS,bool)
    v=np.zeros(NS)
    Es=[]
    for st in range(nst):
        dd=P[:,None,:]-P[None,:,:]
        r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
        r=np.sqrt(r2)
        F=(((QW/(r2+A2)**1.5))[:,:,None]*dd).sum(axis=1)*(-AHC)
        Fm=np.linalg.norm(F,axis=1)
        v=v*eA+np.minimum(mu*Fm,1.0)*(1-eA)
        v=np.minimum(v,1.0)
        idx=np.arange(NS)
        o=idx[out]
        if len(o):
            rij=r[o,tgt[o]]; hit=rij<A[o,tgt[o]]
            for m,i in enumerate(o):
                if hit[m]: continue
                j=tgt[i]
                atj=np.where(r[:,j]<A[:,j])[0]
                atj=atj[atj!=i]
                if len(atj) and (r[i,atj]<A[i,atj]).any(): hit[m]=True
            eT=isE[tgt[o]]&~hit
            for m,i in enumerate(o):
                if eT[m]:
                    j=tgt[i]; col=r[:,j].copy(); col[i]=np.inf
                    if col.min()<A[i,j]: hit[m]=True
            for m,i in enumerate(o):
                if hit[m]: last[i]=tgt[i]; out[i]=False
        b=idx[~out]
        if len(b):
            dh=np.linalg.norm(P[b]-H[b],axis=1)
            arr=dh<np.maximum(0.05,v[b]*dt)
            for m,i in enumerate(b):
                if arr[m]:
                    cand=oppr[i][oppr[i]!=last[i]]
                    if len(cand)==0: cand=oppr[i]
                    u=(P[cand]-P[i]); un=np.maximum(np.linalg.norm(u,axis=1),1e-9)
                    pr=(u/un[:,None])@F[i]
                    tgt[i]=cand[int(np.argmax(pr))]; out[i]=True
        dest=np.where(out[:,None],P[tgt],H)
        u=dest-P; un=np.maximum(np.linalg.norm(u,axis=1),1e-9)
        P=P+(v/un)[:,None]*u*dt
        if st>=int(burn*nst):
            Es.append(0.5*np.sum(QW/np.sqrt(r2+A2))*AHC)
    return np.array(Es)

t0=time.time()
print("="*78)
print("PATCH 2557 -- RE-REGISTRATION under reach-S (2556 adjudication)")
print("="*78)

# ---- CONTROL: reach-S == reach-G on straight rods (spec drift is ring-only) ----
Ps16,Cs16,SPs16=scaffold_L(16,0.0)
rS=build_reach_S(Ps16,Cs16,SPs16); rG=build_reach_G(Ps16,Cs16,SPs16)
same=all(sorted(a)==sorted(b) for a,b in zip(rS,rG))
print(f"CONTROL: reach-S == reach-G on the straight 16-rod: {same}")
assert same
print()

# ---- (1) ENDBOND-3 curve under reach-S ----
FRACS=[0.0,1/5,2/5,3/5,4/5,15/16,1.0]
KAP_RING=2*np.pi/(16*D)
scaffs=[scaffold_L(16,f*KAP_RING) for f in FRACS]
FREF_grid=max(np.linalg.norm(ssv_vectors(P,C,SP),axis=1).max() for (P,C,SP) in scaffs)
FREF_16 =max(np.linalg.norm(ssv_vectors(*scaffs[-1]),axis=1).max(),
             np.linalg.norm(ssv_vectors(*scaffs[0]),axis=1).max())
print(f"(1) ENDBOND-3 curve, reach-S (FREF grid {FREF_grid:.2f} / 16pl {FREF_16:.2f}):")
ecl=[]; kstars=set()
for tag,FREF in (("grid",FREF_grid),("16pl",FREF_16)):
    for dtf in (1/100,1/50,1/25):
        eps=[]
        for (P,C,SP) in scaffs:
            eps.append(dance_v8(P,C,SP,FREF,dtf,build_reach_S).mean())
        istar=int(np.argmax(eps)); kstars.add(FRACS[istar])
        if istar==0: ec=eps[0]-eps[-1]
        elif istar==len(FRACS)-1: ec=float('nan')
        else: ec=eps[istar]-eps[-1]
        ecl.append(ec)
        cs=" ".join(f"{e:+9.1f}" for e in eps)
        print(f"  [{tag:4s} dt=1/{int(1/dtf):>3}] {cs}  k*={FRACS[istar]:.3f} E_close={ec:+7.1f}"
              f"  ({time.time()-t0:.0f}s)")
lo,hi=min(ecl),max(ecl)
print(f"  FROZEN corrected pin (P1): E_close(16) union [{lo:+.1f}, {hi:+.1f}] MeV ; "
      f"kappa* set {sorted(kstars)}")
print()

# ---- (2) FORM-L table under reach-S ----
print("(2) FORM-L E_close(L) table, reach-S:")
GRID=[8,10,12,14,16,20,24]
tab={}
for L in GRID:
    kapL=2*np.pi/(L*D)
    Pr,Cr,SPr=scaffold_L(L,kapL); Ps,Cs,SPs=scaffold_L(L,0.0)
    FREF=max(np.linalg.norm(ssv_vectors(Pr,Cr,SPr),axis=1).max(),
             np.linalg.norm(ssv_vectors(Ps,Cs,SPs),axis=1).max())
    for dtf in (1/100,1/50,1/25):
        Er=dance_v8(Pr,Cr,SPr,FREF,dtf,build_reach_S)
        Es_=dance_v8(Ps,Cs,SPs,FREF,dtf,build_reach_S)
        tab[(L,int(1/dtf))]=Es_.mean()-Er.mean()
    print(f"  L={L:2d}: {tab[(L,100)]:+8.1f} {tab[(L,50)]:+8.1f} {tab[(L,25)]:+8.1f}"
          f"   ({time.time()-t0:.0f}s)")
signchg=[]
for i in range(len(GRID)-1):
    for idt in (100,50,25):
        a=tab[(GRID[i],idt)]; b=tab[(GRID[i+1],idt)]
        if (a>FLOOR and b<-FLOOR) or (a<-FLOOR and b>FLOOR): signchg.append((GRID[i],GRID[i+1],idt))
argm=set()
for idt in (100,50,25):
    vals=[tab[(L,idt)] for L in GRID]
    argm.add(GRID[int(np.argmax(vals))])
print(f"  FROZEN corrected readings (P2): sign changes {signchg if signchg else 'NONE'} ; "
      f"argmax set {sorted(argm)}")
print()

# ---- GATES on the corrected pin (P1 pre-registered re-gating) ----
print("GATES (P1; corrected pin band):")
if np.isnan(lo) or np.isnan(hi):
    print("  adverse/nan cell present -- gates not licensed.")
else:
    g1=(lo>=40.0) and (hi<=170.0)
    print(f"  G1 [40,170] membership: [{lo:.1f},{hi:.1f}] -> {'PASS' if g1 else 'FAIL/PARTIAL'}")
    print(f"  G2 102 lock: inside band: {'YES' if lo<=102.0<=hi else 'NO'}; "
          f"midpoint offset {0.5*(lo+hi)-102.0:+.1f} MeV")
print()
print(f"runtime {time.time()-t0:.0f}s ; ALL ASSERTIONS PASS.")
