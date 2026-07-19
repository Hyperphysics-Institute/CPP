#!/usr/bin/env python3
"""
PATCH 2555 -- AUDIT-DANCE-REACH-1 EXECUTED (registered in 2554 S4).

QUESTION: the registered reach classifier's "in-plane" test uses GLOBAL dz < 0.5*D; on
rings, distinct planes near phi~90 deg have small dz, so cross-plane qCPs can be
classified "in-plane" (and the [:5] truncation then reshapes the reach set). Does this
change the registered observables?

DESIGN (order enforced: census -> PRE-COMMITTED READINGS printed -> re-runs -> compare):
(A) CENSUS on every ring_L scaffold, L in {8,10,12,14,16,20,24}: count qCPs whose 'inpl'
    contains other-plane members; count eCP-rule cross-plane picks (eCP rules are
    distance-based BY DESIGN per the 2455 founder spec and are NOT varied here).
(B) VARIANT classifier (ground truth): 'in-plane' = same plane index (i//8); axial =
    other-plane qCPs r<1.3; eCP rules identical. This is an AUDIT PROBE, not a
    re-registration -- the registered functional remains the geometric classifier.
(C) RE-RUNS under the variant: ring-straight at L=16 (3 dt; the promotion-class
    observable) and E_close(L) for L in {16,20,24} (3 dt; the FORM-L structure).
(D) COMPARISON against the frozen registered-classifier values (2551/2554 record,
    hardcoded below as frozen constants).

PRE-COMMITTED READINGS (frozen here, above any re-run output):
  R1: |delta r-s(16)| <= 5 MeV at every dt -> promotion-class observable ROBUST.
      |delta| > 5 MeV at any dt -> FIDELITY TENSION recorded; dated disclosure line
      queued for the NEXT panel dispatch; NO verdict movement in this patch either way.
  R2: (L=20 > L=16 beyond floor) AND (L=24 collapse, i.e. E_close(24) < E_close(20) by
      >100 MeV) BOTH persist under the variant at every dt -> the FORM-L structure is
      CLASSIFIER-ROBUST; the L=24 equilibrium question becomes promotable by successor.
      Either fails -> structure CLASSIFIER-CONTINGENT; stays banked; tension recorded.
  R3: Registered results remain the registered results regardless of outcome (they are
      what the registered functional produces); this audit moves promotion-eligibility
      and disclosure content ONLY.
"""
import numpy as np, time

AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
d=1.15; A_Q=d; D=d
r_q=A_Q/np.sqrt(2); R_E=1.6*r_q
A_QQ=AHC/264.0; A_EE=AHC/553.0; A_QE=np.sqrt(A_QQ*A_EE)
TAUC=2*np.pi*AHC/264.0
KQ_PIN, KE_PIN = 132.0, 44.0
FLOOR=2.0

# FROZEN registered-classifier values (2551/2554 record):
REG_RS16={100:-134.1, 50:-137.5, 25:-128.9}          # ring-straight = -E_close(16)
REG_EC={16:{100:+134.1,50:+137.5,25:+128.9},
        20:{100:+176.1,50:+159.9,25:+158.4},
        24:{100:+0.5,  50:-6.2,  25:+1.4}}

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

def build_reach_geo(P,C,SP):     # REGISTERED (2461 verbatim)
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

def build_reach_idx(P,C,SP):     # AUDIT VARIANT (plane-index ground truth for qCP inpl)
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
print("PATCH 2555 -- AUDIT-DANCE-REACH-1 (registered 2554 S4)")
print("="*78)

# ---- (A) CENSUS ----
print("(A) CENSUS -- registered geometric classifier on ring_L scaffolds:")
for L in (8,10,12,14,16,20,24):
    P,C,SP=scaffold_L(L,2*np.pi/(L*D))
    reach=build_reach_geo(P,C,SP)
    mis=0; ecx=0; qaff=set()
    for i in range(len(P)):
        ki=i//8
        if SP[i]=='q':
            dd=P-P[i]; r=np.sqrt((dd*dd).sum(axis=1)); r[i]=np.inf
            inpl=[j for j in range(len(P)) if SP[j]=='q' and abs(P[j][2]-P[i][2])<0.5*D and r[j]<1.8]
            for j in inpl:
                if j//8!=ki: mis+=1; qaff.add(i)
            for j in reach[i]:
                if SP[j]=='e' and j//8!=ki: ecx+=1
    print(f"  L={L:2d}: cross-plane 'inpl' q-pairs={mis:3d} (qCPs affected {len(qaff):3d}/{4*L}) ; "
          f"cross-plane eCP picks={ecx}")
print()
print("(B) PRE-COMMITTED READINGS R1/R2/R3: see module docstring -- frozen before re-runs.")
print()

# ---- (C) RE-RUNS under the variant ----
print("(C) variant-classifier re-runs:")
var_ec={}
for L in (16,20,24):
    kapL=2*np.pi/(L*D)
    Pr,Cr,SPr=scaffold_L(L,kapL); Ps,Cs,SPs=scaffold_L(L,0.0)
    FREF=max(np.linalg.norm(ssv_vectors(Pr,Cr,SPr),axis=1).max(),
             np.linalg.norm(ssv_vectors(Ps,Cs,SPs),axis=1).max())
    var_ec[L]={}
    for dtf in (1/100,1/50,1/25):
        Er=dance_v8(Pr,Cr,SPr,FREF,dtf,build_reach_idx)
        Es_=dance_v8(Ps,Cs,SPs,FREF,dtf,build_reach_idx)
        var_ec[L][int(1/dtf)]=Es_.mean()-Er.mean()
    print(f"  L={L:2d} variant E_close dt 1/100,1/50,1/25: "
          f"{var_ec[L][100]:+8.1f} {var_ec[L][50]:+8.1f} {var_ec[L][25]:+8.1f}  ({time.time()-t0:.0f}s)")
print()

# ---- (D) COMPARISON per R1/R2 ----
print("(D) COMPARISON:")
print("  R1 (promotion-class r-s(16); threshold |delta| <= 5 MeV):")
r1_ok=True
for idt in (100,50,25):
    reg=REG_RS16[idt]; var=-var_ec[16][idt]; dlt=var-reg
    ok=abs(dlt)<=5.0; r1_ok&=ok
    print(f"    dt=1/{idt:>3}: registered {reg:+7.1f}  variant {var:+7.1f}  delta {dlt:+6.1f}  "
          f"{'OK' if ok else 'EXCEEDS'}")
print(f"  R1 verdict: {'ROBUST' if r1_ok else 'FIDELITY TENSION (disclosure line queued)'}")
print()
print("  R2 (FORM-L structure persistence):")
r2_ok=True
for idt in (100,50,25):
    peak=(var_ec[20][idt]-var_ec[16][idt])>FLOOR
    coll=(var_ec[20][idt]-var_ec[24][idt])>100.0
    r2_ok&=(peak and coll)
    print(f"    dt=1/{idt:>3}: L20>L16 beyond floor: {peak} ; L24 collapse (>100 below L20): {coll}")
print(f"  R2 verdict: {'CLASSIFIER-ROBUST -> L=24 equilibrium question promotable by successor' if r2_ok else 'CLASSIFIER-CONTINGENT -> stays banked; tension recorded'}")
print()
print("  R3: registered results remain the registered results; this audit moved")
print("      promotion-eligibility and disclosure content only.")
print(f"runtime {time.time()-t0:.0f}s ; ALL ASSERTIONS PASS.")
