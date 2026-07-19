#!/usr/bin/env python3
"""
PATCH 2565 -- NB-S3a-1 K1 R-0: THE RP-GATE, executed under nbs3a1_k1_preregistration.md ONLY.

INSTRUMENT: dance_v8 definitions VERBATIM from code/2557_reregistration_reach_s.py.
THE MINIMAL EXTENSION (the only admissible change, prereg S1): the home scaffold H
translates rigidly at the initialized velocity -- implemented as H <- H + Hvel*dt per step,
dest logic otherwise byte-identical. No new forces, no modified contention, no altered
arrest logic.

PRE-COMMITTED GATE READINGS (frozen here, before any run):
 G-READ-1 (C-1 free flight): PASS iff the DP centroid net displacement is within 10% of
   u*T_run (tolerance DECLARED here, resolving the prereg's floor-units gap: 10% covers the
   arrest-scale discretization max(0.05, v*dt)) AND internal cohesion holds (max |P-H| < 2 fm).
 G-READ-2 (C-2 over-barrier, E_rel = 500 MeV): PASS iff NOT CAPTURED under BOTH CL-A and CL-B.
   E<->v mapping DECLARED: relativistic per-DP, KE_tot = 2*(gamma-1)*m_qDP, m_qDP = 264 MeV
   (the nonrelativistic mapping is superluminal at 500 MeV, hence not defensible there).
 G-READ-3 (C-3 bound-state recovery): PASS iff CAPTURED under BOTH CL-A and CL-B.
   A C-3 failure indicts the CLASSIFIER, not the physics (prereg S1).
 G-READ-4 (structural representability census; the production-relevance test): under the
   registered instrument's LETTER, reach lists are built ONCE at initialization. CENSUS: at
   the production initial condition (separation 6*a_qq), does ANY cross-DP index appear in
   ANY oppr list (incl. the oppr-empty fallback)? If NO -- cross-DP retargeting is impossible
   for the whole run, sigma_cap == 0 STRUCTURALLY (representation, not physics) -- then the
   RP-GATE FAILS FOR PRODUCTION regardless of C-1..C-3, and prereg reading 6(a) applies:
   K1 CLOSED BLOCKED, Branch I, founder-routed, named gap "unbound-state representation",
   with the isolated spec question: is reach a REGISTRATION-TIME STATIC object (the letter;
   all prior campaigns had static geometry so the question never arose) or a definition
   EVALUATED ON CURRENT POSITIONS (live reach)? This is a 2555/2556-class operationalization
   question and belongs to the founder's spec authority.
 DIAGNOSTIC (labeled, NON-REGISTERED, run only AFTER the gate verdict is printed; informs
   adjudication, promoted nowhere): the same controls + one low-E head-on probe
   (E_rel = 5 MeV) under LIVE reach (the identical reach-S rule re-evaluated every step).

CLASSIFIERS (prereg S3, verbatim): CL-A separation (final-25% time-avg cross-DP center
separation < 1.5*a_qq AND no monotone growth => CAPTURED; final sep > initial with monotone
final-25% growth => ESCAPED; else UNRESOLVED). CL-B energy (final-25% time-avg cross-DP
interaction energy < -4 MeV persistently => CAPTURED; within +/-2 of 0 => ESCAPED; else
UNRESOLVED).

RUN CONVENTIONS (prereg S2.3): dt union {1/100, 1/50, 1/25}*TAUC; TC = 60; burn 0.15;
FREF union over the two defensible two-body conventions: FREF_sys (max initial SSV of the
full configuration) and FREF_dp (max SSV of an isolated DP).
"""
import numpy as np, time

# ---- VERBATIM CONSTANTS AND HELPERS (2557) ----
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
d=1.15; A_Q=d; D=d
A_QQ=AHC/264.0; A_EE=AHC/553.0; A_QE=np.sqrt(A_QQ*A_EE)
TAUC=2*np.pi*AHC/264.0
KQ_PIN, KE_PIN = 132.0, 44.0
FLOOR=2.0
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
def build_reach_S(P,C,SP):   # VERBATIM (2556 adjudicated spec-faithful classifier)
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

# ---- dance_v8 with the MINIMAL EXTENSION (marked lines only; else byte-identical) ----
def dance_v8_k1(H,C,SP,FREF,dtfrac,reachfn,Hvel=None,kscale=1.0,TC=60,burn=0.15,
                live_reach=False, groupA=None):
    A=amat(SP); qw=qw_of(SP,C); NS=len(H)
    QW=np.outer(qw,qw); A2=A*A
    reach=reachfn(H,C,SP)
    def opp_of(reach):
        o=[np.array([j for j in reach[i] if C[j]*C[i]<0],dtype=int) for i in range(NS)]
        for i in range(NS):
            if len(o[i])==0: o[i]=np.where(C*C[i]<0)[0]
        return o
    oppr=opp_of(reach)
    isE=np.array([s=='e' for s in SP])
    kap=np.where(isE, KE_PIN, KQ_PIN)*kscale
    mu=1.0/FREF
    dt=TAUC*dtfrac; nst=int(TC*TAUC/dt)
    eA=np.exp(-dt/(kap*mu)) if kscale>0 else np.zeros(NS)
    H=H.copy()                                   # EXTENSION: home is mutable state
    Hvel=np.zeros_like(H) if Hvel is None else Hvel
    P=H.copy()
    tgt=np.array([oppr[i][np.argmin(np.linalg.norm(H[oppr[i]]-H[i],axis=1))] for i in range(NS)])
    last=-np.ones(NS,int); out=np.ones(NS,bool)
    v=np.zeros(NS)
    trA=[]; trB=[]; Ecross=[]
    gA=np.array(groupA); gB=np.array([i for i in range(NS) if i not in set(groupA)]) if groupA is not None else None
    for st in range(nst):
        H=H+Hvel*dt                              # EXTENSION: rigid home translation
        if live_reach:                           # DIAGNOSTIC BRANCH ONLY (not the gate's letter)
            reach=reachfn(P,C,SP); oppr=opp_of(reach)
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
        if gB is not None:
            cA=P[gA].mean(axis=0); cB=P[gB].mean(axis=0)
            trA.append(cA.copy()); trB.append(cB.copy())
            Ec=0.0
            for i in gA:
                for j in gB:
                    rij2=((P[i]-P[j])**2).sum()
                    Ec+=QW[i,j]/np.sqrt(rij2+A2[i,j])
            Ecross.append(Ec*AHC)
        else:
            trA.append(P.mean(axis=0))
    out_d={'P':P,'H':H,'trA':np.array(trA)}
    if gB is not None: out_d['trB']=np.array(trB); out_d['Ecross']=np.array(Ecross)
    return out_d

# ---- geometry builders (declared in prereg S2.4 and here) ----
def qDP(center, sign=+1):
    """qDP: two qCPs, charges (+,-)*sign, internal axis x, separation a_qq."""
    h=A_QQ/2
    P=[(center[0]-h,center[1],center[2]),(center[0]+h,center[1],center[2])]
    return np.array(P,float), np.array([+1.0*sign,-1.0*sign]), ['q','q']

def two_qdp(sep_z, signB=-1):
    Pa,Ca,Sa=qDP((0,0,0),+1); Pb,Cb,Sb=qDP((0,0,sep_z),signB)
    return np.vstack([Pa,Pb]), np.concatenate([Ca,Cb]), Sa+Sb

def classify(res, sep0):
    """CL-A and CL-B per prereg S3. Returns (clA, clB) in {CAP, ESC, UNR}."""
    trA,trB,Ec=res['trA'],res['trB'],res['Ecross']
    n=len(Ec); w=slice(int(0.75*n),n)
    sep=np.linalg.norm(trA-trB,axis=1)
    sw=sep[w]; ew=Ec[w]
    grow=np.all(np.diff(sw)>=-1e-9) and (sw[-1]-sw[0])>0.05
    if sw.mean()<1.5*A_QQ and not grow: clA='CAP'
    elif sep[-1]>sep0 and grow: clA='ESC'
    else: clA='UNR'
    if np.mean(ew)<-2*FLOOR and np.max(ew)<-2*FLOOR: clB='CAP'
    elif abs(np.mean(ew))<FLOOR: clB='ESC'
    else: clB='UNR'
    return clA,clB

t0=time.time()
print("="*78); print("PATCH 2565 -- K1 R-0: THE RP-GATE"); print("="*78)
DTS=(1/100,1/50,1/25)

# FREF conventions (two-body union, declared in header)
Pdp,Cdp,Sdp=qDP((0,0,0))
FREF_dp=np.linalg.norm(ssv_vectors(Pdp,Cdp,Sdp),axis=1).max()
P2,C2,S2=two_qdp(6*A_QQ)
FREF_sys=np.linalg.norm(ssv_vectors(P2,C2,S2),axis=1).max()
print(f"FREF union: dp={FREF_dp:.2f}, sys={FREF_sys:.2f}")
FREFS={'dp':FREF_dp,'sys':FREF_sys}

# ---- G-READ-4 FIRST IN PRINT ORDER? No: census is computed pre-run but the gate order
# in the prereg is C-1..C-3 then production-relevance; census computed now, verdict after.
reach0=build_reach_S(P2,C2,S2)
opp0=[[j for j in reach0[i] if C2[j]*C2[i]<0] for i in range(4)]
cross0=any((i<2)!=(j<2) for i in range(4) for j in opp0[i])
# fallback check: does any oppr go empty (=> global fallback incl. cross)?
fallback=any(len(o)==0 for o in opp0)
print(f"[census] production init (6 a_qq): cross-DP contention possible = {cross0}; "
      f"oppr-empty fallback fires = {fallback}")

# ---- C-1: free flight (single qDP, u = 0.2c along z) ----
print("\nC-1 free flight (u = 0.2c):")
c1_pass=True
for fk,FREF in FREFS.items():
    for dtf in DTS:
        Hv=np.tile([0,0,0.2],(2,1))
        res=dance_v8_k1(Pdp.copy(),Cdp,Sdp,FREF,dtf,build_reach_S,Hvel=Hv,groupA=None)
        T=60*TAUC; exp_d=0.2*T
        disp=np.linalg.norm(res['trA'][-1]-res['trA'][0]) if len(res['trA'])>1 else 0.0
        coh=np.abs(np.linalg.norm(res['P']-res['H'],axis=1)).max()
        ok=(abs(disp-exp_d)/exp_d<0.10) and (coh<2.0)
        c1_pass&=ok
        print(f"  FREF={fk} dt=1/{int(1/dtf)}: disp={disp:7.2f} (exp {exp_d:6.2f}) "
              f"cohesion={coh:5.3f} fm  {'PASS' if ok else 'FAIL'}")

# ---- C-2: over-barrier pass-through, E_rel = 500 MeV ----
g=1+250/264.0; u2=np.sqrt(1-1/g**2)
print(f"\nC-2 over-barrier (E_rel=500 MeV, u_each={u2:.3f}c):")
c2_pass=True
for fk,FREF in FREFS.items():
    for dtf in DTS:
        P0,C0,S0=two_qdp(6*A_QQ)
        Hv=np.vstack([np.tile([0,0,+u2],(2,1)),np.tile([0,0,-u2],(2,1))])
        res=dance_v8_k1(P0,C0,S0,FREF,dtf,build_reach_S,Hvel=Hv,groupA=[0,1])
        clA,clB=classify(res,6*A_QQ)
        ok=(clA!='CAP') and (clB!='CAP')
        c2_pass&=ok
        print(f"  FREF={fk} dt=1/{int(1/dtf)}: CL-A={clA} CL-B={clB}  {'PASS' if ok else 'FAIL'}")

# ---- C-3: bound-state recovery (contact, v=0) ----
print("\nC-3 bound recovery (sep=a_qq, v=0):")
c3_pass=True
for fk,FREF in FREFS.items():
    for dtf in DTS:
        P0,C0,S0=two_qdp(A_QQ)
        res=dance_v8_k1(P0,C0,S0,FREF,dtf,build_reach_S,Hvel=None,groupA=[0,1])
        clA,clB=classify(res,A_QQ)
        ok=(clA=='CAP') and (clB=='CAP')
        c3_pass&=ok
        print(f"  FREF={fk} dt=1/{int(1/dtf)}: CL-A={clA} CL-B={clB}  {'PASS' if ok else 'FAIL'}")

# ---- GATE VERDICT (pre-committed logic, header) ----
print("\n"+"="*78)
print(f"C-1 {'PASS' if c1_pass else 'FAIL'} | C-2 {'PASS' if c2_pass else 'FAIL'} | "
      f"C-3 {'PASS' if c3_pass else 'FAIL'} | cross-DP contention at production init: {cross0}")
if not cross0:
    print("G-READ-4 FIRES: sigma_cap == 0 STRUCTURALLY under the instrument's letter "
          "(static reach). RP-GATE: FAILS FOR PRODUCTION -> prereg 6(a): K1 CLOSED BLOCKED, "
          "Branch I, founder-routed, named gap 'unbound-state representation'. Spec question "
          "isolated: static (registration-time) reach vs live (current-position) reach.")
GATE_BLOCKED = not cross0
print("="*78)

# ---- DIAGNOSTIC (non-registered; informs adjudication only) ----
print("\nDIAGNOSTIC (live reach -- same rule, re-evaluated per step; NOT the gate):")
for lbl,(sep,uu,sB) in {'C-2-live (500 MeV)':(6*A_QQ,u2,-1),
                        'probe-live (5 MeV head-on)':(6*A_QQ,np.sqrt(1-1/(1+2.5/264)**2),-1),
                        'C-3-live (contact)':(A_QQ,0.0,-1)}.items():
    for fk,FREF in FREFS.items():
        row=[]
        for dtf in DTS:
            P0,C0,S0=two_qdp(sep,signB=sB)
            Hv=None if uu==0 else np.vstack([np.tile([0,0,+uu],(2,1)),np.tile([0,0,-uu],(2,1))])
            res=dance_v8_k1(P0,C0,S0,FREF,dtf,build_reach_S,Hvel=Hv,groupA=[0,1],live_reach=True)
            clA,clB=classify(res,sep)
            row.append(f"{clA}/{clB}")
        print(f"  {lbl:28s} FREF={fk}: "+"  ".join(row))
print(f"\n[{time.time()-t0:.0f}s]")
