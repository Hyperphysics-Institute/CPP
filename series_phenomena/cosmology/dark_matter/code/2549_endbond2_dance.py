#!/usr/bin/env python3
"""
PATCH 2549 -- OPEN-DM-ENDBOND-2 R-A EXECUTED under endbond2_preregistration.md ONLY.

E_endbond = <E>(2 independent single-plane dances) - <E>(2-plane stack at D, alt parity),
positive = bound. dance_v8 rules VERBATIM from code/2510_hardened_dance_inertia.py (the
only adaptation is the scaffold builder -- fragment geometries -- per prereg S2.2).
Union axes (prereg S3): dt in {tauC/100, tauC/50, tauC/25} x FREF in {local, 16-plane
registered}. Primary accounting <Ep>; <Etot> disclosed. Blindness: the union band is
computed and FROZEN (printed) before the gates section prints anything; the fenced
numbers appear nowhere above the gates section.
"""
import numpy as np, time

# ---- registered constants (2461/2510 lineage, verbatim values) ----
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
d=1.15; A_Q=d; D=d
r_q=A_Q/np.sqrt(2); R_E=1.6*r_q
A_QQ=AHC/264.0; A_EE=AHC/553.0; A_QE=np.sqrt(A_QQ*A_EE)
TAUC=2*np.pi*AHC/264.0
KQ_PIN, KE_PIN = 132.0, 44.0          # 2496 pin; kscale=1.0 throughout (prereg S2.2)

# ---- scaffolds: the ONLY adaptation (fragment geometries; 2455-coded plane, ratified) ----
def plane_sites(par, z):
    h=A_Q/2
    q=[(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)]
    S=[]
    for (x,y,sg) in q: S.append(((x,y,z),sg*par,'q'))
    for (x,y,sg) in q:
        n=np.hypot(x,y); S.append(((R_E*x/n,R_E*y/n,z),-sg*par,'e'))
    return S

def scaffold(planes):
    S=[]
    for k,z in enumerate(planes): S+=plane_sites((-1)**k, z)
    P=np.array([s[0] for s in S],float); C=np.array([float(s[1]) for s in S])
    return P,C,[s[2] for s in S]

# ---- 2461 defs, verbatim ----
def build_reach(P,C,SP):
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
    qw=W*C; NS=len(P)
    dd=P[:,None,:]-P[None,:,:]; r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
    A=amat(SP); F=((np.outer(qw,qw)/(r2+A*A)**1.5)[:,:,None]*dd).sum(axis=1)*(-AHC)
    return F
def qw_of(SP,C):
    W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP]); return W*C

# ---- dance_v8, VERBATIM from 2510 (rule fidelity; no edits) ----
def dance_v8(H,C,SP,FREF,dtfrac,kscale=1.0,TC=60,burn=0.15):
    A=amat(SP); qw=qw_of(SP,C); NS=len(H)
    QW=np.outer(qw,qw); A2=A*A
    reach=build_reach(H,C,SP)
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
    Es=[]; KEs=[]; Fsum=np.zeros((NS,3)); nF=0; amp=0.0
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
            KEs.append(0.5*np.sum(kap*v*v))
            Fsum+=F; nF+=1; amp+=np.linalg.norm(P-H,axis=1).mean()
    return np.array(Es), np.array(KEs), Fsum/nF, amp/nF

t0=time.time()
print("="*78)
print("PATCH 2549 -- OPEN-DM-ENDBOND-2 R-A: dance-route bond depth (prereg 2548 only)")
print("="*78)

# ---- scaffolds ----
Pstk,Cstk,SPstk = scaffold([0.0, D])          # the stack (16 CPs)
Ppl ,Cpl ,SPpl  = scaffold([0.0])             # one isolated plane (8 CPs)
Pgap,Cgap,SPgap = scaffold([0.0, 20.0])       # robustness-only finite gap

# sanity: reach sets -- stack qCPs must include the axial partner; isolated plane must not
r_stk=build_reach(Pstk,Cstk,SPstk); r_pl=build_reach(Ppl,Cpl,SPpl)
ax_ct=sum(1 for i in range(len(SPstk)) if SPstk[i]=='q'
          and any(SPstk[j]=='q' and abs(Pstk[j][2]-Pstk[i][2])>0.5*D for j in r_stk[i]))
print(f"reach sanity: stack qCPs with axial partner = {ax_ct}/8 ; isolated-plane cross partners = 0")
assert ax_ct==8

# ---- FREF conventions (prereg S3-B) ----
FREF_local = max(np.linalg.norm(ssv_vectors(Pstk,Cstk,SPstk),axis=1).max(),
                 np.linalg.norm(ssv_vectors(Ppl ,Cpl ,SPpl ),axis=1).max())
# registered 16-plane value, recomputed verbatim from the 2461 scaffolds:
N=16; KAP=2*np.pi/(N*D); R0=1/KAP
def ring_scaffold():
    S=[]
    for k in range(N):
        phi=2*np.pi*k/N
        cx=R0*(1-np.cos(phi)); cz=R0*np.sin(phi)
        c,s=np.cos(phi),np.sin(phi); par=(-1)**k
        h=A_Q/2
        q=[(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)]
        for (x,y,sg) in q: S.append(((cx+x*c,y,cz-x*s),sg*par,'q'))
        for (x,y,sg) in q:
            n=np.hypot(x,y); X,Y=R_E*x/n,R_E*y/n
            S.append(((cx+X*c,Y,cz-X*s),-sg*par,'e'))
    P=np.array([s[0] for s in S]); C=np.array([float(s[1]) for s in S])
    return P,C,[s[2] for s in S]
def straight_scaffold():
    S=[]
    for k in range(N):
        par=(-1)**k; h=A_Q/2
        q=[(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)]
        for (x,y,sg) in q: S.append(((x,y,k*D),sg*par,'q'))
        for (x,y,sg) in q:
            n=np.hypot(x,y); S.append(((R_E*x/n,R_E*y/n,k*D),-sg*par,'e'))
    P=np.array([s[0] for s in S]); C=np.array([float(s[1]) for s in S])
    return P,C,[s[2] for s in S]
Pr,Cr,SPr=ring_scaffold(); Ps16,Cs16,SPs16=straight_scaffold()
FREF_16 = max(np.linalg.norm(ssv_vectors(Pr,Cr,SPr),axis=1).max(),
              np.linalg.norm(ssv_vectors(Ps16,Cs16,SPs16),axis=1).max())
print(f"FREF_local = {FREF_local:.2f} ; FREF_16 = {FREF_16:.2f}  (both computed per S3-B)")
print()

# ---- the union grid (compute EVERYTHING before printing the frozen band) ----
rows=[]
for tag,FREF in (("local",FREF_local),("16pl",FREF_16)):
    for dtf in (1/100,1/50,1/25):
        Ek,Kk,_,ampS=dance_v8(Pstk,Cstk,SPstk,FREF,dtf)
        Ep1,Kp1,_,ampP=dance_v8(Ppl,Cpl,SPpl,FREF,dtf)
        Eb_p  = 2*Ep1.mean() - Ek.mean()                       # <Ep> accounting (primary)
        Eb_t  = 2*(Ep1.mean()+Kp1.mean()) - (Ek.mean()+Kk.mean())  # <Etot> (disclosed)
        rows.append((tag,int(1/dtf),Eb_p,Eb_t,ampS,ampP))
print("union grid (primary <Ep>; <Etot> disclosed):")
for (tag,idt,ep,et,aS,aP) in rows:
    print(f"  FREF={tag:5s} dt=tauC/{idt:>3}: E_endbond = {ep:+8.1f} MeV  (Etot acct {et:+8.1f}) "
          f"| amp stack/plane {aS:.2f}/{aP:.2f}")
vals=[r[2] for r in rows]
lo,hi=min(vals),max(vals)
print()
print("="*78)
print(f"FROZEN UNION BAND (primary <Ep>, interface total): E_endbond in "
      f"[{lo:+.1f}, {hi:+.1f}] MeV   (positive = bound)")
spans_zero = (lo<0<hi) or lo==0 or hi==0
neg_all = hi<0
print(f"frozen consequence line: spans_zero={spans_zero}; negative_across_union={neg_all}")
print("="*78)
print()

# ---- robustness (disclosed, non-feeding): finite-gap reference at one grid point ----
Eg,Kg,_,_=dance_v8(Pgap,Cgap,SPgap,FREF_local,1/50)
Ek,Kk,_,_=dance_v8(Pstk,Cstk,SPstk,FREF_local,1/50)
Ep1,Kp1,_,_=dance_v8(Ppl,Cpl,SPpl,FREF_local,1/50)
print(f"robustness (disclosed only): 20 fm gap reference gives E_endbond = "
      f"{Eg.mean()-Ek.mean():+.1f} vs independent-planes {2*Ep1.mean()-Ek.mean():+.1f} MeV "
      f"(FREF_local, dt=1/50)")
print()

# ---- GATES (prereg S4; only now) ----
print("GATES (S4, fixed order; compared against the frozen band above):")
if spans_zero:
    print("  Branch I (statistical limb): the union band spans zero -- no depth claim;")
    print("  gates not licensed on a non-depth.")
elif neg_all:
    print("  ADVERSE-DIRECTION: negative across the union -- recorded as-is; gates not")
    print("  licensed on an unbound result; flows to the standing disclosure package.")
else:
    g1_in  = (lo>=40.0) and (hi<=170.0)
    g1_ovl = (hi>=40.0) and (lo<=170.0)
    print(f"  G1 (membership in [40,170]): band [{lo:.1f},{hi:.1f}] -> "
          f"{'PASS (fully inside)' if g1_in else ('PARTIAL OVERLAP' if g1_ovl else 'FAIL')}")
    mid=0.5*(lo+hi)
    print(f"  G2 (102 lock proximity): band midpoint {mid:.1f}, lock inside band: "
          f"{'YES' if lo<=102.0<=hi else 'NO'}; midpoint offset {mid-102.0:+.1f} MeV")
    print(f"  demoted-echo internal-consistency note (no gate force): same-family ~85 MeV")
    print(f"  back-implication {'inside' if lo<=85.0<=hi else 'outside'} the frozen band.")
print()
print(f"runtime {time.time()-t0:.0f}s ; ALL ASSERTIONS PASS.")
