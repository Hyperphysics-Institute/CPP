#!/usr/bin/env python3
"""OPEN-DM-CONTINUOUS-PCD-1 (Patch 2467): the reading landscape of Momentwise PCD
dynamics, run to discharge the promotion-round forks by computation. Four readings:
(A) naive net-SSV flow (Gemini Q2 literal): ALL structure disintegrates at every dt
    (ring/rod bonds -> 12-40 fm, E -> +75k); dt->0 limit = frozen statics (no ZBW).
    Self-falsifying as a reading of the spec: reproduces no bound matter.
(B) homeless target-chase (rebound retarget, no home return): ALL structure
    collapses (bonds -> 0.0-0.04 fm). Self-falsifying.
(C) Momentwise home-anchored dance, GENERIC reach (any opposite < 2 fm):
    structure holds (amp ~0.5 fm) but ROD favored (+41..+152, dt-consistent).
(D) Momentwise home-anchored dance, FOUNDER reach sets (the spec): structure holds,
    RING favored (-74..-144, dt-consistent) -- reproduces #1 legless/capless/waitless.
(C)-vs-(D) isolates the load-bearing element: the founder reach STRUCTURE (spec),
not the 2461 wait rule (which does no outcome work and EMERGES Momentwise).
Q1 derivation: pattern-level bond-stretch forces on the dancing ring: inner -0.9,
outer +3.1 vs rod common-mode +1.3 MeV/fm -- the dynamics pushes AWAY from uniform
1.15 on both edges: hypothesis (i) straight-registry is CONTRADICTED; the derived
reference is at-least-as-curvature-differentiated as ring-native (ii)-class.
Mode curvatures Momentwise: dt-sign-flips (deterministic-pair decorrelation) ->
UNRESOLVED at this treatment; the leg-based #1+#2 mode record stands operative;
ensemble-mode methodology = registered follow-up. Deterministic throughout (no RNG).
Sections below concatenate the run scripts verbatim: naive map probe, v4 generic-
reach, v5 founder-reach (the decisive computation). Requires 2461 defs (same dir).
Runtime ~10 min total."""
import numpy as np, time, sys
exec(open(__file__.replace("2467_continuous_pcd","2461_ssv_kinematics")).read().split("if __name__")[0])
# ============ (A) naive net-SSV map probe ============
def qw_of(SP):
    W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP]); return W
def forces(P,qw,A):
    dd=P[:,None,:]-P[None,:,:]
    r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
    den=(r2+A*A)**1.5
    coef=np.outer(qw,qw)/den
    return (coef[:,:,None]*dd).sum(axis=1)*(-AHC)
def energy(P,qw,A):
    dd=P[:,None,:]-P[None,:,:]
    r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
    return 0.5*np.sum(np.outer(qw,qw)/np.sqrt(r2+A*A))*AHC
def run_map(P0,C,SP,FREF,dtfrac,TC=90,burn=0.1):
    A=amat(SP); qw=qw_of(SP)*C
    dt=TAUC*dtfrac; nst=int(TC*TAUC/dt)
    P=P0.copy(); Es=[]; Ps_acc=None; nacc=0
    for s in range(nst):
        F=forces(P,qw,A); Fm=np.linalg.norm(F,axis=1)
        v=np.minimum(Fm/FREF,1.0)
        step=np.where(Fm[:,None]>0, (v/np.maximum(Fm,1e-30))[:,None]*F*dt, 0.0)
        P=P+step
        if s>=int(burn*nst):
            Es.append(energy(P,qw,A))
            Ps_acc = P.copy() if Ps_acc is None else Ps_acc+P; nacc+=1
    return np.array(Es), Ps_acc/nacc, P
def qidx(k,c): return 8*k+c
def bondsB(closed):
    B=[]
    for k in range(N if closed else N-1):
        for c in range(4): B.append((qidx(k,c),qidx((k+1)%N,c)))
    return B
Pr,Cr,SPr=ring_scaffold(); Ps,Cs,SPs=straight_scaffold()
Fr=ssv_vectors(Pr,Cr,SPr); Fs=ssv_vectors(Ps,Cs,SPs)
FREF=max(np.linalg.norm(Fr,axis=1).max(),np.linalg.norm(Fs,axis=1).max())
Br=bondsB(True); Bs=bondsB(False)
Lr0=np.array([np.linalg.norm(Pr[i]-Pr[j]) for i,j in Br])
print(f"FREF={FREF:.2f} (pre-registered, as #1); initial ring bonds min/med/max = "
      f"{Lr0.min():.3f}/{np.median(Lr0):.3f}/{Lr0.max():.3f}; rod bonds all 1.150")
for dtf in (1/200,1/50,1/20):
    Er,PrM,_=run_map(Pr,Cr,SPr,FREF,dtf)
    Es_,PsM,_=run_map(Ps,Cs,SPs,FREF,dtf)
    LrM=np.array([np.linalg.norm(PrM[i]-PrM[j]) for i,j in Br])
    LsM=np.array([np.linalg.norm(PsM[i]-PsM[j]) for i,j in Bs])
    # radius check: is the ring still closed / same size?
    cen=PrM[[qidx(k,0) for k in range(N)]]  # corner-0 qCPs around the ring
    print(f"dt=tauC/{int(1/dtf)}: ring <E>={Er.mean():+9.1f} (drift {Er[-1]-Er[0]:+.1f}) ; "
          f"rod <E>={Es_.mean():+9.1f} ; ring-rod = {Er.mean()-Es_.mean():+8.1f}")
    print(f"   emergent ring bonds min/med/max = {LrM.min():.3f}/{np.median(LrM):.3f}/{LrM.max():.3f}"
          f"  (native init {Lr0.min():.3f}/{np.median(Lr0):.3f}/{Lr0.max():.3f}; straight-registry 1.150)")
    print(f"   emergent rod bonds med = {np.median(LsM):.3f}")
# ============ (C) v4 generic-reach Momentwise dance ============
def dance_M(H,C,SP,FREF,dtfrac,TC=60,burn=0.15):
    """Momentwise home-anchored dance. H = fixed home pattern. Deterministic.
       OUT: toward tgt; rebound (r<a_ij) or eCP-preemption -> BACK (toward home);
       arrive home (r<0.05) -> pick next tgt = max F-projection among opposite in reach, != last.
       Speed every Moment = min(|F|/FREF,1) -- no freeze, no cap, no legs."""
    A=amat(SP); qw=qw_of(SP,C); NS=len(H)
    QW=np.outer(qw,qw); A2=A*A
    dt=TAUC*dtfrac; nst=int(TC*TAUC/dt)
    P=H.copy()
    opp=[np.where(C*C[i]<0)[0] for i in range(NS)]
    tgt=np.array([opp[i][np.argmin(np.linalg.norm(H[opp[i]]-H[i],axis=1))] for i in range(NS)])
    last=-np.ones(NS,int); out=np.ones(NS,bool)
    isE=np.array([s=='e' for s in SP])
    Es=[]; Fsum=np.zeros((NS,3)); nF=0; slowfrac=0; amp=0.0
    for s in range(nst):
        dd=P[:,None,:]-P[None,:,:]
        r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
        r=np.sqrt(r2)
        F=(((QW/(r2+A2)**1.5))[:,:,None]*dd).sum(axis=1)*(-AHC)
        Fm=np.linalg.norm(F,axis=1); v=np.minimum(Fm/FREF,1.0)
        idx=np.arange(NS)
        # OUT->BACK: superposition rebound or eCP preemption
        o=idx[out]
        if len(o):
            rij=r[o,tgt[o]]; hit=rij<A[o,tgt[o]]
            eT=isE[tgt[o]]&~hit
            for m,i in enumerate(o):
                if eT[m]:
                    j=tgt[i]; col=r[:,j].copy(); col[i]=np.inf
                    if col.min()<A[i,j]: hit[m]=True
            for m,i in enumerate(o):
                if hit[m]: last[i]=tgt[i]; out[i]=False
        # BACK->OUT: arrived home
        b=idx[~out]
        if len(b):
            dh=np.linalg.norm(P[b]-H[b],axis=1)
            for m,i in enumerate(b):
                if dh[m]<0.05:
                    cand=opp[i][opp[i]!=last[i]]
                    dcand=np.linalg.norm(H[cand]-H[i],axis=1); near=cand[dcand<2.0]
                    cc=near if len(near) else cand
                    u=(P[cc]-P[i]); un=np.maximum(np.linalg.norm(u,axis=1),1e-9)
                    pr=(u/un[:,None])@F[i]
                    tgt[i]=cc[int(np.argmax(pr))]; out[i]=True
        dest=np.where(out[:,None],P[tgt],H)
        u=dest-P; un=np.maximum(np.linalg.norm(u,axis=1),1e-9)
        P=P+(v/un)[:,None]*u*dt
        if s>=int(burn*nst):
            Es.append(0.5*np.sum(QW/np.sqrt(r2+A2))*AHC)
            Fsum+=F; nF+=1; slowfrac+=(v<0.05).mean(); amp+=np.linalg.norm(P-H,axis=1).mean()
    return np.array(Es), Fsum/nF, slowfrac/nF, amp/nF
Pr,Cr,SPr=ring_scaffold(); Ps,Cs,SPs=straight_scaffold()
Fr=ssv_vectors(Pr,Cr,SPr); Fs=ssv_vectors(Ps,Cs,SPs)
FREF=max(np.linalg.norm(Fr,axis=1).max(),np.linalg.norm(Fs,axis=1).max())
def qidx(k,c): return 8*k+c
mode=sys.argv[1]
t0=time.time()
if mode=='dt':
    for dtf in (1/100,1/50,1/25):
        Er,Favg_r,slr,ampr=dance_M(Pr,Cr,SPr,FREF,dtf)
        Es_,Favg_s,sls,amps=dance_M(Ps,Cs,SPs,FREF,dtf)
        # Q1 observable: pattern-level bond-stretch force on ring axial bonds
        st=[]
        for k in range(N):
            for c in range(4):
                i,j=qidx(k,c),qidx((k+1)%N,c)
                u=(Pr[j]-Pr[i])/np.linalg.norm(Pr[j]-Pr[i])
                st.append(np.dot(Favg_r[j]-Favg_r[i],u))   # >0 = stretch toward longer
        st=np.array(st); L0=np.array([np.linalg.norm(Pr[qidx(k,c)]-Pr[qidx((k+1)%N,c)]) for k in range(N) for c in range(4)])
        inner=st[L0<1.05]; outer=st[L0>1.25]
        print(f"dt=tauC/{int(1/dtf):>3}: ring<E>={Er.mean():+8.1f} rod<E>={Es_.mean():+8.1f} "
              f"r-s={Er.mean()-Es_.mean():+7.1f} | amp {ampr:.2f}/{amps:.2f} fm | slow-frac "
              f"{slr:.2f}/{sls:.2f} | Q1 stretch: inner {inner.mean():+6.2f} outer {outer.mean():+6.2f} "
              f"all {st.mean():+6.2f} MeV/fm | {time.time()-t0:.0f}s")
else:
    dtf=1/50
    modes={'m0':dict(tilt=[0.04]*N),'m1':dict(tilt=[0.04*np.cos(2*np.pi*k/N) for k in range(N)]),
           'm2':dict(tilt=[0.04*np.cos(4*np.pi*k/N) for k in range(N)]),'ell':dict(ell=0.02)}
    E0,_,_,_=dance_M(Pr,Cr,SPr,FREF,dtf)
    print(f"base ring <E> = {E0.mean():+.1f} ({time.time()-t0:.0f}s)")
    for nm,kw in modes.items():
        x=0.02 if nm=='ell' else 0.04
        Ep,_,_,_=dance_M(ring_scaffold(**kw)[0],Cr,SPr,FREF,dtf)
        cur=2*(Ep.mean()-E0.mean())/x**2
        # deterministic: dt-spread is the uncertainty proxy; report raw here
        print(f"  {nm}: <E>={Ep.mean():+8.1f}  d2E/dx2 = {cur:+9.0f}  ({time.time()-t0:.0f}s)")
# ============ (D) v5 FOUNDER-reach Momentwise dance (decisive) ============
def dance_M5(H,C,SP,FREF,dtfrac,TC=60,burn=0.15):
    """Momentwise home-anchored dance with FOUNDER REACH SETS (build_reach from the
       2461 defs: in-plane + axial qCPs + radial eCP per qCP; 4 eCP + own qCP per eCP).
       Legless, capless: direction re-chosen on rebound/home-arrival; speed from
       instantaneous SSV every Moment. Deterministic."""
    A=amat(SP); qw=qw_of(SP,C); NS=len(H)
    QW=np.outer(qw,qw); A2=A*A
    reach=build_reach(H,C,SP)
    oppr=[np.array([j for j in reach[i] if C[j]*C[i]<0],dtype=int) for i in range(NS)]
    for i in range(NS):
        if len(oppr[i])==0: oppr[i]=np.where(C*C[i]<0)[0]
    dt=TAUC*dtfrac; nst=int(TC*TAUC/dt)
    P=H.copy()
    tgt=np.array([oppr[i][np.argmin(np.linalg.norm(H[oppr[i]]-H[i],axis=1))] for i in range(NS)])
    last=-np.ones(NS,int); out=np.ones(NS,bool)
    isE=np.array([s=='e' for s in SP])
    Es=[]; Fsum=np.zeros((NS,3)); nF=0; amp=0.0
    for s in range(nst):
        dd=P[:,None,:]-P[None,:,:]
        r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
        r=np.sqrt(r2)
        F=(((QW/(r2+A2)**1.5))[:,:,None]*dd).sum(axis=1)*(-AHC)
        Fm=np.linalg.norm(F,axis=1); v=np.minimum(Fm/FREF,1.0)
        idx=np.arange(NS)
        o=idx[out]
        if len(o):
            rij=r[o,tgt[o]]; hit=rij<A[o,tgt[o]]
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
            for m,i in enumerate(b):
                if dh[m]<0.05:
                    cand=oppr[i][oppr[i]!=last[i]]
                    if len(cand)==0: cand=oppr[i]
                    u=(P[cand]-P[i]); un=np.maximum(np.linalg.norm(u,axis=1),1e-9)
                    pr=(u/un[:,None])@F[i]
                    tgt[i]=cand[int(np.argmax(pr))]; out[i]=True
        dest=np.where(out[:,None],P[tgt],H)
        u=dest-P; un=np.maximum(np.linalg.norm(u,axis=1),1e-9)
        P=P+(v/un)[:,None]*u*dt
        if s>=int(burn*nst):
            Es.append(0.5*np.sum(QW/np.sqrt(r2+A2))*AHC)
            Fsum+=F; nF+=1; amp+=np.linalg.norm(P-H,axis=1).mean()
    return np.array(Es), Fsum/nF, amp/nF
Pr,Cr,SPr=ring_scaffold(); Ps,Cs,SPs=straight_scaffold()
Fr=ssv_vectors(Pr,Cr,SPr); Fs=ssv_vectors(Ps,Cs,SPs)
FREF=max(np.linalg.norm(Fr,axis=1).max(),np.linalg.norm(Fs,axis=1).max())
def qidx(k,c): return 8*k+c
mode=sys.argv[1]; t0=time.time()
if mode=='dt':
    for dtf in (1/100,1/50,1/25):
        Er,Favg_r,ampr=dance_M5(Pr,Cr,SPr,FREF,dtf)
        Es_,Favg_s,amps=dance_M5(Ps,Cs,SPs,FREF,dtf)
        # Q1: bond-stretch pattern forces, ring (inner vs outer) AND rod (common-mode ref)
        str_r=[]; L0=[]
        for k in range(N):
            for c in range(4):
                i,j=qidx(k,c),qidx((k+1)%N,c)
                u=(Pr[j]-Pr[i])/np.linalg.norm(Pr[j]-Pr[i])
                str_r.append(np.dot(Favg_r[j]-Favg_r[i],u)); L0.append(np.linalg.norm(Pr[i]-Pr[j]))
        str_s=[]
        for k in range(N-1):
            for c in range(4):
                i,j=qidx(k,c),qidx(k+1,c)
                u=(Ps[j]-Ps[i])/np.linalg.norm(Ps[j]-Ps[i])
                str_s.append(np.dot(Favg_s[j]-Favg_s[i],u))
        str_r=np.array(str_r); L0=np.array(L0); str_s=np.array(str_s)
        inner=str_r[L0<1.05].mean(); outer=str_r[L0>1.25].mean()
        print(f"dt=tauC/{int(1/dtf):>3}: ring<E>={Er.mean():+8.1f} rod<E>={Es_.mean():+8.1f} "
              f"r-s={Er.mean()-Es_.mean():+7.1f} | amp {ampr:.2f}/{amps:.2f} | Q1 ring stretch "
              f"inner {inner:+5.2f} outer {outer:+5.2f} vs rod common {str_s.mean():+5.2f} MeV/fm | {time.time()-t0:.0f}s")
else:
    dtf=float(sys.argv[2]) if len(sys.argv)>2 else 1/50
    E0,_,_=dance_M5(Pr,Cr,SPr,FREF,dtf)
    print(f"base ring <E> = {E0.mean():+.1f}")
    for nm,kw,x in [('m0',dict(tilt=[0.04]*N),0.04),('m1',dict(tilt=[0.04*np.cos(2*np.pi*k/N) for k in range(N)]),0.04),
                    ('m2',dict(tilt=[0.04*np.cos(4*np.pi*k/N) for k in range(N)]),0.04),('ell',dict(ell=0.02),0.02)]:
        Ep,_,_=dance_M5(ring_scaffold(**kw)[0],Cr,SPr,FREF,dtf)
        print(f"  {nm}: d2E/dx2 = {2*(Ep.mean()-E0.mean())/x**2:+9.0f}   ({time.time()-t0:.0f}s)")
