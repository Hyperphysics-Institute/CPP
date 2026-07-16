#!/usr/bin/env python3
"""DM hardening probe (Patch 2510) -- SF-6 inertia + full qCP-target contention added to
the founder-reach Momentwise dance (2467 D), per the 2470 deferral charter. Coefficient
FROM THE PIN (2496): kappa_q=132, kappa_e=44 MeV/c^2 (Laue coefficient-1 on the 2452
in-situ masses), scanned {0.25,0.5,1,2}, headline at the pinned center (G7: never fit,
never selected). Retardation sigma/c per species (a_qq, a_ee). Pre-registration in
reasoning/2510.md SS2-4, committed before this ran. Deterministic, no RNG.

Modes: repro (verbatim 2467 dance_M5 continuity check) | dt (hardened, pinned kappa,
3 dt) | scan (kappa multipliers, dt=1/50) | modes (m0/m1/m2/ell, pinned, 2 dt).
Requires 2461 defs (same dir). Flags verbatim-in-force: matched-pair (KE = sum 1/2 k s^2
only), not-registry-canonical, W2 caveat, scalar-toy debt (b) avoided by construction
(scalar along-axis drive)."""
import numpy as np, time, sys
exec(open(__file__.replace("2510_hardened_dance_inertia","2461_ssv_kinematics")).read().split("if __name__")[0])

KQ_PIN, KE_PIN = 132.0, 44.0   # MeV/c^2 -- 2452 in-situ, Laue coeff-1 (2496 concl. 6)

def qw_of(SP,C):
    W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP]); return W*C

# ---------------- verbatim 2467 dance_M5 (memoryless) -- harness continuity ----------------
def dance_M5(H,C,SP,FREF,dtfrac,TC=60,burn=0.15):
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

# -------- v8 HARDENED (final): dance choreography + SF-6 speed memory + pile contention --------
# Probe findings preserved (reasoning/2510 SS2.5, SS5): (v6) signed velocity on the rotating
# commitment axis = parametric pump, ill-posed; (v7) fully unscripted 3-D inertial MD
# collapses (opposite-charge soft core has its minimum at r=0) -- an independent empirical
# re-confirmation that HOME-ANCHORING IS LOAD-BEARING SPEC (2454/2467 reading (B)).
# v8 = the minimal well-posed completion: the promoted 2467-D choreography is kept EXACTLY
# (direction always toward commitment; home-anchoring intact; eCP preemption unchanged);
# the SPEED MAGNITUDE carries the sea's memory per the 2496 pin:
#     kappa dv/dt = |F_net| - v/mu ,  mu = 1/FREF ,  0 <= v <= c  (exact exp integrator)
# kappa_q=132, kappa_e=44 MeV/c^2 (Laue coeff-1 on the 2452 in-situ masses; scan x{.25,.5,1,2},
# headline pinned). Speed CARRIES across commitment switches (sea-stored momentum; direction
# re-choreography is the dance's kinematic idiom, as memoryless). kappa->0 recovers 2467-D
# EXACTLY. Contention completion: OUT ends on superposition with the TARGET or with any CP
# already superposed AT that target (many-toward-one pile stacking) -- native-structure-safe.
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
    eA=np.exp(-dt/(kap*mu)) if kscale>0 else np.zeros(NS)   # kscale=0 -> memoryless limit
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
        v=v*eA+np.minimum(mu*Fm,1.0)*(1-eA)          # speed memory; kscale=0 -> v=min(mu|F|,1)
        v=np.minimum(v,1.0)
        idx=np.arange(NS)
        o=idx[out]
        if len(o):
            rij=r[o,tgt[o]]; hit=rij<A[o,tgt[o]]
            # pile contention at qCP targets: superposed with a CP that is itself at my target
            for m,i in enumerate(o):
                if hit[m]: continue
                j=tgt[i]
                atj=np.where(r[:,j]<A[:,j])[0]        # CPs superposed at target j
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
            arr=dh<np.maximum(0.05,v[b]*dt)           # crossing-based arrival (inertial step)
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
            KEs.append(0.5*np.sum(kap*v*v))           # matched-pair: 1/2 kappa v^2
            Fsum+=F; nF+=1; amp+=np.linalg.norm(P-H,axis=1).mean()
    return np.array(Es), np.array(KEs), Fsum/nF, amp/nF

def qidx(k,c): return 8*k+c
def stretch(Favg,Pref,closed):
    st=[];L0=[]
    for k in range(N if closed else N-1):
        for c in range(4):
            i,j=qidx(k,c),qidx((k+1)%N,c)
            u=(Pref[j]-Pref[i])/np.linalg.norm(Pref[j]-Pref[i])
            st.append(np.dot(Favg[j]-Favg[i],u)); L0.append(np.linalg.norm(Pref[i]-Pref[j]))
    return np.array(st),np.array(L0)

Pr,Cr,SPr=ring_scaffold(); Ps,Cs,SPs=straight_scaffold()
Fr=ssv_vectors(Pr,Cr,SPr); Fs=ssv_vectors(Ps,Cs,SPs)
FREF=max(np.linalg.norm(Fr,axis=1).max(),np.linalg.norm(Fs,axis=1).max())
mode=sys.argv[1]; t0=time.time()

if mode=='repro':
    print(f"FREF={FREF:.2f}; 2467-D published ring-rod: -143.9/-132.1/-74.4 at dt 1/100,1/50,1/25")
    for dtf in (1/100,1/50,1/25):
        Er,_,ampr=dance_M5(Pr,Cr,SPr,FREF,dtf)
        Es_,_,amps=dance_M5(Ps,Cs,SPs,FREF,dtf)
        print(f"repro dt=tauC/{int(1/dtf):>3}: ring<E>={Er.mean():+8.1f} rod<E>={Es_.mean():+8.1f} "
              f"r-s={Er.mean()-Es_.mean():+7.1f} | amp {ampr:.2f}/{amps:.2f} | {time.time()-t0:.0f}s")
elif mode=='dt':
    for dtf in (1/100,1/50,1/25):
        Er,Kr,Favg_r,ampr=dance_v8(Pr,Cr,SPr,FREF,dtf)
        Es_,Ks,Favg_s,amps=dance_v8(Ps,Cs,SPs,FREF,dtf)
        str_r,L0=stretch(Favg_r,Pr,True); str_s,_=stretch(Favg_s,Ps,False)
        inner=str_r[L0<1.05].mean(); outer=str_r[L0>1.25].mean()
        dP=Er.mean()-Es_.mean(); dT=(Er.mean()+Kr.mean())-(Es_.mean()+Ks.mean())
        print(f"HARD dt=tauC/{int(1/dtf):>3} k=1.0: ring Ep={Er.mean():+8.1f} KE={Kr.mean():6.1f} | "
              f"rod Ep={Es_.mean():+8.1f} KE={Ks.mean():6.1f} | r-s Ep={dP:+7.1f} Etot={dT:+7.1f} | "
              f"amp {ampr:.2f}/{amps:.2f} | Q1 inner {inner:+5.2f} outer {outer:+5.2f} rod {str_s.mean():+5.2f} | {time.time()-t0:.0f}s")
elif mode=='scan':
    dtf=1/50
    for ks in (0.0,0.25,0.5,1.0,2.0):   # ks=0 = memoryless nesting check vs 2467-D
        Er,Kr,_,ampr=dance_v8(Pr,Cr,SPr,FREF,dtf,kscale=ks)
        Es_,Ks,_,amps=dance_v8(Ps,Cs,SPs,FREF,dtf,kscale=ks)
        dP=Er.mean()-Es_.mean(); dT=(Er.mean()+Kr.mean())-(Es_.mean()+Ks.mean())
        tag=" <- PINNED (headline)" if ks==1.0 else ""
        print(f"scan k={ks:4.2f}: r-s Ep={dP:+8.1f} Etot={dT:+8.1f} | ring KE={Kr.mean():6.1f} "
              f"amp {ampr:.2f}/{amps:.2f} | {time.time()-t0:.0f}s{tag}")
elif mode=='modes':
    for dtf in (1/50,1/25):
        E0,K0,_,_=dance_v8(Pr,Cr,SPr,FREF,dtf)
        T0=E0.mean()+K0.mean()
        print(f"modes dt=tauC/{int(1/dtf)}: base ring Etot={T0:+.1f} ({time.time()-t0:.0f}s)")
        for nm,kw,x in [('m0',dict(tilt=[0.04]*N),0.04),
                        ('m1',dict(tilt=[0.04*np.cos(2*np.pi*k/N) for k in range(N)]),0.04),
                        ('m2',dict(tilt=[0.04*np.cos(4*np.pi*k/N) for k in range(N)]),0.04),
                        ('ell',dict(ell=0.02),0.02)]:
            Ep,Kp,_,_=dance_v8(ring_scaffold(**kw)[0],Cr,SPr,FREF,dtf)
            Tp=Ep.mean()+Kp.mean()
            print(f"  {nm}: d2Etot/dx2 = {2*(Tp-T0)/x**2:+9.0f}  (Ep-part {2*(Ep.mean()-E0.mean())/x**2:+9.0f})  ({time.time()-t0:.0f}s)")
