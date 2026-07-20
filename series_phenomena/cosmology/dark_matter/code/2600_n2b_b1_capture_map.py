#!/usr/bin/env python3
"""
PATCH 2582 -- NUCLEUS-1 EXECUTION under nucleus1_preregistration.md (2581) ONLY.
Controls first (gating), then the ladder in charter order. Verdicts are read from the
prereg against raw outputs (the 2579 rule); the script prints observables and the
prereg-mapped classification, and the patch document performs the reading.
Citations: engine = 2573 (physical force -grad U); dance layer = 2557 verbatim;
H-A home law = dance v-update (2557) applied to homes per charter clause; H-B = K1a
cycle-impulse lineage (2573).
"""
import numpy as np, time
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
A_QQ=AHC/264.0; A_EE=AHC/553.0; A_QE=np.sqrt(A_QQ*A_EE)
TAUC=2*np.pi*AHC/264.0; D=1.15; A_Q=D; r_q=A_Q/np.sqrt(2); R_E=1.6*r_q
KQ,KE=132.0,44.0; FLOOR=2.0
def soft_a(si,sj): return A_QQ if si==sj=='q' else (A_EE if si==sj=='e' else A_QE)
def amat(SP):
    NS=len(SP); A=np.zeros((NS,NS))
    for i in range(NS):
        for j in range(NS): A[i,j]=soft_a(SP[i],SP[j])
    return A
def qw_of(SP,C):
    W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP]); return W*C
trunc_mode='DIST'
def build_reach_S(P,C,SP):     # 2557 radii/rules verbatim; truncation per 2574 remedy
    NS=len(P); reach=[]
    for i in range(NS):
        dd=P-P[i]; r=np.sqrt((dd*dd).sum(axis=1)); r[i]=np.inf
        ki=i//8
        if SP[i]=='q':
            inpl=[j for j in range(NS) if SP[j]=='q' and j//8==ki and r[j]<1.8]
            axl=[j for j in range(NS) if SP[j]=='q' and j//8!=ki and r[j]<1.3]
            ecp=[j for j in range(NS) if SP[j]=='e' and r[j]<0.6]
            qset=list(set(inpl+axl))
            # 2574 guard FIRED on dynamic positions (RUNG-3, live lists) -> the
            # registered remedy (2574 S3: index-order truncation IS the defect;
            # R-B item 1's convention union is the fix): DIST = nearest-5 by
            # distance; FULL = untruncated. Index-ordered member EXCLUDED by
            # citation. trunc_mode set per run; both union members executed.
            if trunc_mode=='DIST':
                qset=sorted(qset,key=lambda j:r[j])[:5]
            reach.append(sorted(qset)+ecp)
        else:
            eopp=sorted([j for j in range(NS) if SP[j]=='e' and 0<r[j]<2.6],key=lambda j:r[j])[:4]
            qown=[j for j in range(NS) if SP[j]=='q' and r[j]<0.6]
            reach.append(eopp+qown)
    return reach

def plane(par,z,coated):
    h=A_Q/2; q=[(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)]
    P=[];C=[];S=[]
    for (x,y,sg) in q: P.append((x,y,z));C.append(sg*par);S.append('q')
    if coated:
        for (x,y,sg) in q:
            n=np.hypot(x,y); P.append((R_E*x/n,R_E*y/n,z));C.append(-sg*par);S.append('e')
    return P,C,S
def rung(n):
    if n==1: P,C,S=plane(+1,0,False)
    elif n==2: P,C,S=plane(+1,0,True)
    else:
        P1,C1,S1=plane(+1,0,True); P2,C2,S2=plane(-1,D,True)
        P,C,S=P1+P2,C1+C2,S1+S2
    return np.array(P,float),np.array(C,float),S
def pair_config():   # CTRL-N3: the 2573/2575 two-qDP configuration, per-CP homes
    h=A_QQ/2
    P=[(-h,0,0),(+h,0,0),(-h,0,A_QQ),(+h,0,A_QQ)]
    C=[+1.,-1.,-1.,+1.]; S=['q']*4
    return np.array(P,float),np.array(C,float),S

def n1_run(H0,C,SP,dtf,conv='HA',coupling=1.0,TC=60):
    """Per-CP dynamical homes. conv: 'HA' (SF-6 relaxation, 2557 v-law on homes) or
    'HB' (Newtonian cycle impulse)."""
    NS=len(H0); A=amat(SP); qw=qw_of(SP,C); QW=np.outer(qw,qw); A2=A*A
    isE=np.array([s=='e' for s in SP]); kap=np.where(isE,KE,KQ)
    m=np.where(isE,KE,KQ)
    dt=TAUC*dtf; nst=int(TC*TAUC/dt); spc=max(1,int(round(1.0/dtf)))
    H=H0.copy(); P=H.copy()
    reach=build_reach_S(H,C,SP)
    def opp_of(reach):
        o=[np.array([j for j in reach[i] if C[j]*C[i]<0],dtype=int) for i in range(NS)]
        for i in range(NS):
            if len(o[i])==0:
                cand=np.where(C*C[i]<0)[0]
                o[i]=cand if len(cand) else np.array([i],dtype=int)
        return o
    oppr=opp_of(reach)
    tgt=np.array([oppr[i][np.argmin(np.linalg.norm(H[oppr[i]]-H[i],axis=1))] for i in range(NS)])
    last=-np.ones(NS,int); out=np.ones(NS,bool); v=np.zeros(NS)
    Vh=np.zeros((NS,3)); accF=np.zeros((NS,3))
    # FREF from initial configuration (prereg S4)
    dd=H[:,None,:]-H[None,:,:]; r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
    FREF=np.linalg.norm((((QW/(r2+A2)**1.5))[:,:,None]*dd).sum(axis=1)*(-AHC),axis=1).max()
    FREF=max(FREF,1e-6)
    mu=1.0/FREF; eA=np.exp(-dt/(kap*mu))
    Rrms=[]; Dmax=[]
    assert_hb=True
    for st in range(nst):
        dd=P[:,None,:]-P[None,:,:]; r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
        Fp=((QW/(r2+A2)**1.5))[:,:,None]*dd*(-AHC)      # dance-internal (2557)
        F=Fp.sum(axis=1); Fm=np.linalg.norm(F,axis=1)
        Fphys=(-Fp).sum(axis=1)                          # physical -grad U (2573)
        if coupling>0:
            accF+=Fphys*dt
            if (st+1)%spc==0:
                Fbar=accF/(spc*dt)
                if conv=='HB':
                    dV=coupling*(Fbar*TAUC)/m[:,None]
                    if np.linalg.norm(dV,axis=1).max()>=0.5: assert_hb=False
                    Vh=Vh+dV
                else:  # H-A: registered SF-6 relaxation toward capped force-set velocity
                    Fbm=np.linalg.norm(Fbar,axis=1)
                    vt=np.minimum(mu*Fbm,1.0)
                    dirn=Fbar/np.maximum(Fbm,1e-12)[:,None]
                    Vt=vt[:,None]*dirn
                    eAc=np.exp(-TAUC/(kap*mu))[:,None]
                    Vh=Vh*eAc+Vt*(1-eAc)
                accF[:]=0.0
        H=H+Vh*dt
        # CP layer (2557 verbatim)
        v=v*eA+np.minimum(mu*Fm,1.0)*(1-eA); v=np.minimum(v,1.0)
        idx=np.arange(NS); o=idx[out]; r=np.sqrt(r2)
        if len(o):
            rij=r[o,tgt[o]]; hit=rij<A[o,tgt[o]]
            for k,i in enumerate(o):
                if hit[k]: continue
                j=tgt[i]
                atj=np.where(r[:,j]<A[:,j])[0]; atj=atj[atj!=i]
                if len(atj) and (r[i,atj]<A[i,atj]).any(): hit[k]=True
            eT=isE[tgt[o]]&~hit
            for k,i in enumerate(o):
                if eT[k]:
                    j=tgt[i]; col=r[:,j].copy(); col[i]=np.inf
                    if col.min()<A[i,j]: hit[k]=True
            for k,i in enumerate(o):
                if hit[k]: last[i]=tgt[i]; out[i]=False
        b=idx[~out]
        if len(b):
            dh=np.linalg.norm(P[b]-H[b],axis=1)
            arr=dh<np.maximum(0.05,v[b]*dt)
            for k,i in enumerate(b):
                if arr[k]:
                    cand=oppr[i][oppr[i]!=last[i]]
                    if len(cand)==0: cand=oppr[i]
                    u=(P[cand]-P[i]); un=np.maximum(np.linalg.norm(u,axis=1),1e-9)
                    pr=(u/un[:,None])@F[i]
                    tgt[i]=cand[int(np.argmax(pr))]; out[i]=True
        reach=build_reach_S(P,C,SP); oppr=opp_of(reach)    # live lists (2572 primary)
        dest=np.where(out[:,None],P[tgt],H)
        u=dest-P; un=np.maximum(np.linalg.norm(u,axis=1),1e-9)
        P=P+(v/un)[:,None]*u*dt
        cen=P.mean(axis=0); dc=np.linalg.norm(P-cen,axis=1)
        Rrms.append(np.sqrt((dc*dc).mean())); Dmax.append(dc.max())
    Rrms=np.array(Rrms); Dmax=np.array(Dmax)
    n=len(Rrms); wsl=slice(int(0.75*n),n)
    return {'R0':Rrms[0],'Dmax0':Dmax[0],'Rw':Rrms[wsl].mean(),'Dmaxw':Dmax[wsl].max(),
            'Rend':Rrms[-1],'hb_ok':assert_hb,'P':P,'H':H,'Vh':Vh}

def classify(res, widened=False):
    lo,hi,dm=(0.33,3.0,4.5) if widened else (0.5,2.0,3.0)
    if not res['hb_ok']: return 'UNRES-NUM'
    R0=max(res['R0'],1e-9)
    if res['Rw']<lo*R0: return 'COLLAPSE'
    if res['Rw']>hi*R0 or res['Dmaxw']>dm*max(res['Dmax0'],1e-9): return 'DISPERSE'
    if lo*R0<=res['Rw']<=hi*R0 and res['Dmaxw']<=dm*max(res['Dmax0'],1e-9): return 'HOLD'
    return 'UNRES'


# ===== PATCH 2584 -- N1 R-B: the COMPLETED interaction (2583 rider) =====
EQQ=ALPHA_S*AHC/D          # 66.25 MeV [1812]
def strong_FU(H,SP,betad):
    """Morse qq-only on the HOME layer [2583 S2]: returns (Fstrong per home, Ustrong)."""
    NS=len(H); beta=betad/D
    F=np.zeros((NS,3)); U=0.0
    qi=[i for i,s in enumerate(SP) if s=='q']
    for a in range(len(qi)):
        for b in range(a+1,len(qi)):
            i,j=qi[a],qi[b]
            dv=H[i]-H[j]; r=max(np.linalg.norm(dv),1e-9)
            e=np.exp(-beta*(r-D))
            U+=EQQ*((1-e)**2-1)
            dUdr=2*EQQ*beta*e*(1-e)
            fv=-dUdr*dv/r
            F[i]+=fv; F[j]-=fv
    return F,U

def n1_rb(H0,C,SP,dtf,member,betad,coupling=1.0,TC=60):
    """member: 'atP' (electric at CP positions + strong at homes) or 'atH' (both at homes)."""
    NS=len(H0); A=amat(SP); qw=qw_of(SP,C); QW=np.outer(qw,qw); A2=A*A
    isE=np.array([s=='e' for s in SP]); kap=np.where(isE,KE,KQ)
    dt=TAUC*dtf; nst=int(TC*TAUC/dt); spc=max(1,int(round(1.0/dtf)))
    H=H0.copy(); P=H.copy()
    dd=H[:,None,:]-H[None,:,:]; r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
    FREF=np.linalg.norm((((QW/(r2+A2)**1.5))[:,:,None]*dd).sum(axis=1)*(-AHC),axis=1).max()
    mu=1.0/max(FREF,1e-6); eA=np.exp(-dt/(kap*mu))
    reach=build_reach_S(H,C,SP)
    def opp_of(reach):
        o=[np.array([j for j in reach[i] if C[j]*C[i]<0],dtype=int) for i in range(NS)]
        for i in range(NS):
            if len(o[i])==0:
                cand=np.where(C*C[i]<0)[0]; o[i]=cand if len(cand) else np.array([i],int)
        return o
    oppr=opp_of(reach)
    tgt=np.array([oppr[i][np.argmin(np.linalg.norm(H[oppr[i]]-H[i],axis=1))] for i in range(NS)])
    last=-np.ones(NS,int); out=np.ones(NS,bool); v=np.zeros(NS)
    Vh=np.zeros((NS,3)); accF=np.zeros((NS,3)); Rr=[]; Dm=[]
    for st in range(nst):
        # home-layer force per member + strong (always at homes) [2583 S2]
        Fs,_=strong_FU(H,SP,betad)
        if member=='atH':
            ddh=H[:,None,:]-H[None,:,:]; r2h=(ddh*ddh).sum(axis=2); np.fill_diagonal(r2h,np.inf)
            Fe=(-((QW/(r2h+A2)**1.5))[:,:,None]*ddh*(-AHC)).sum(axis=1)
        else:
            ddp=P[:,None,:]-P[None,:,:]; r2p=(ddp*ddp).sum(axis=2); np.fill_diagonal(r2p,np.inf)
            Fe=(-((QW/(r2p+A2)**1.5))[:,:,None]*ddp*(-AHC)).sum(axis=1)
        accF+=(Fe+Fs)*dt
        if (st+1)%spc==0:
            Fbar=accF/(spc*dt); Fbm=np.linalg.norm(Fbar,axis=1)
            vt=np.minimum(mu*Fbm,1.0); dirn=Fbar/np.maximum(Fbm,1e-12)[:,None]
            eAc=np.exp(-TAUC/(kap*mu))[:,None]
            Vh=Vh*eAc+(vt[:,None]*dirn)*(1-eAc)
            if coupling==0.0: Vh[:]=0.0
            accF[:]=0.0
        H=H+Vh*dt
        # CP layer verbatim (electric choreography untouched) [2583 S2]
        dd=P[:,None,:]-P[None,:,:]; r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
        Fp=((QW/(r2+A2)**1.5))[:,:,None]*dd*(-AHC)
        F=Fp.sum(axis=1); Fm=np.linalg.norm(F,axis=1)
        v=v*eA+np.minimum(mu*Fm,1.0)*(1-eA); v=np.minimum(v,1.0)
        idx=np.arange(NS); o=idx[out]; r=np.sqrt(r2)
        if len(o):
            rij=r[o,tgt[o]]; hit=rij<A[o,tgt[o]]
            for k,i in enumerate(o):
                if hit[k]: continue
                j=tgt[i]; atj=np.where(r[:,j]<A[:,j])[0]; atj=atj[atj!=i]
                if len(atj) and (r[i,atj]<A[i,atj]).any(): hit[k]=True
            eT=isE[tgt[o]]&~hit
            for k,i in enumerate(o):
                if eT[k]:
                    j=tgt[i]; col=r[:,j].copy(); col[i]=np.inf
                    if col.min()<A[i,j]: hit[k]=True
            for k,i in enumerate(o):
                if hit[k]: last[i]=tgt[i]; out[i]=False
        b=idx[~out]
        if len(b):
            dh=np.linalg.norm(P[b]-H[b],axis=1)
            arr=dh<np.maximum(0.05,v[b]*dt)
            for k,i in enumerate(b):
                if arr[k]:
                    cand=oppr[i][oppr[i]!=last[i]]
                    if len(cand)==0: cand=oppr[i]
                    u=(P[cand]-P[i]); un=np.maximum(np.linalg.norm(u,axis=1),1e-9)
                    pr=(u/un[:,None])@F[i]
                    tgt[i]=cand[int(np.argmax(pr))]; out[i]=True
        reach=build_reach_S(P,C,SP); oppr=opp_of(reach)
        dest=np.where(out[:,None],P[tgt],H)
        u=dest-P; un=np.maximum(np.linalg.norm(u,axis=1),1e-9)
        P=P+(v/un)[:,None]*u*dt
        cen=P.mean(axis=0); dc=np.linalg.norm(P-cen,axis=1)
        Rr.append(np.sqrt((dc*dc).mean())); Dm.append(dc.max())
    Rr=np.array(Rr); Dm=np.array(Dm); n=len(Rr); wsl=slice(int(0.75*n),n)
    return {'R0':Rr[0],'Dmax0':Dm[0],'Rw':Rr[wsl].mean(),'Dmaxw':Dm[wsl].max(),'hb_ok':True}


def n1_hc(H0,C,SP,dtf,member,betad,coupling=1.0,TC=60):
    """H-C: per-step Newtonian homes at pinned masses [2585 S1]. Semi-implicit Euler."""
    NS=len(H0); A=amat(SP); qw=qw_of(SP,C); QW=np.outer(qw,qw); A2=A*A
    isE=np.array([s=='e' for s in SP]); kap=np.where(isE,KE,KQ); m=np.where(isE,KE,KQ)
    dt=TAUC*dtf; nst=int(TC*TAUC/dt)
    H=H0.copy(); P=H.copy()
    dd=H[:,None,:]-H[None,:,:]; r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
    FREF=np.linalg.norm((((QW/(r2+A2)**1.5))[:,:,None]*dd).sum(axis=1)*(-AHC),axis=1).max()
    mu=1.0/max(FREF,1e-6); eA=np.exp(-dt/(kap*mu))
    reach=build_reach_S(H,C,SP)
    def opp_of(reach):
        o=[np.array([j for j in reach[i] if C[j]*C[i]<0],dtype=int) for i in range(NS)]
        for i in range(NS):
            if len(o[i])==0:
                cand=np.where(C*C[i]<0)[0]; o[i]=cand if len(cand) else np.array([i],int)
        return o
    oppr=opp_of(reach)
    tgt=np.array([oppr[i][np.argmin(np.linalg.norm(H[oppr[i]]-H[i],axis=1))] for i in range(NS)])
    last=-np.ones(NS,int); out=np.ones(NS,bool); v=np.zeros(NS)
    Vh=np.zeros((NS,3))
    try:
        if _KICK is not None: Vh=Vh+_KICK; globals()['_KICK']=None
    except NameError: pass
    Rr=[]; Dm=[]; rel_ok=True; E0=None; Edrift=0.0
    for st in range(nst):
        Fs,Us=strong_FU(H,SP,betad)
        if member=='atH':
            ddh=H[:,None,:]-H[None,:,:]; r2h=(ddh*ddh).sum(axis=2); np.fill_diagonal(r2h,np.inf)
            Fe=(-((QW/(r2h+A2)**1.5))[:,:,None]*ddh*(-AHC)).sum(axis=1)
            Ue=(np.triu(QW/np.sqrt(r2h+A2),1)).sum()*AHC
        else:
            ddp=P[:,None,:]-P[None,:,:]; r2p=(ddp*ddp).sum(axis=2); np.fill_diagonal(r2p,np.inf)
            Fe=(-((QW/(r2p+A2)**1.5))[:,:,None]*ddp*(-AHC)).sum(axis=1)
            Ue=(np.triu(QW/np.sqrt(r2p+A2),1)).sum()*AHC
        if coupling>0:
            Vh=Vh+((Fe+Fs)/m[:,None])*dt
            if np.linalg.norm(Vh,axis=1).max()>=0.9: rel_ok=False
        H=H+Vh*dt
        KEh=0.5*(m*(Vh*Vh).sum(axis=1)).sum()
        Etot=KEh+Us+Ue
        if E0 is None: E0=Etot
        Edrift=max(Edrift,abs(Etot-E0))
        # CP layer verbatim
        dd=P[:,None,:]-P[None,:,:]; r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
        Fp=((QW/(r2+A2)**1.5))[:,:,None]*dd*(-AHC)
        F=Fp.sum(axis=1); Fm=np.linalg.norm(F,axis=1)
        v=v*eA+np.minimum(mu*Fm,1.0)*(1-eA); v=np.minimum(v,1.0)
        idx=np.arange(NS); o=idx[out]; r=np.sqrt(r2)
        if len(o):
            rij=r[o,tgt[o]]; hit=rij<A[o,tgt[o]]
            for k,i in enumerate(o):
                if hit[k]: continue
                j=tgt[i]; atj=np.where(r[:,j]<A[:,j])[0]; atj=atj[atj!=i]
                if len(atj) and (r[i,atj]<A[i,atj]).any(): hit[k]=True
            eT=isE[tgt[o]]&~hit
            for k,i in enumerate(o):
                if eT[k]:
                    j=tgt[i]; col=r[:,j].copy(); col[i]=np.inf
                    if col.min()<A[i,j]: hit[k]=True
            for k,i in enumerate(o):
                if hit[k]: last[i]=tgt[i]; out[i]=False
        b=idx[~out]
        if len(b):
            dh=np.linalg.norm(P[b]-H[b],axis=1)
            arr=dh<np.maximum(0.05,v[b]*dt)
            for k,i in enumerate(b):
                if arr[k]:
                    cand=oppr[i][oppr[i]!=last[i]]
                    if len(cand)==0: cand=oppr[i]
                    u=(P[cand]-P[i]); un=np.maximum(np.linalg.norm(u,axis=1),1e-9)
                    pr=(u/un[:,None])@F[i]
                    tgt[i]=cand[int(np.argmax(pr))]; out[i]=True
        reach=build_reach_S(P,C,SP); oppr=opp_of(reach)
        dest=np.where(out[:,None],P[tgt],H)
        u=dest-P; un=np.maximum(np.linalg.norm(u,axis=1),1e-9)
        P=P+(v/un)[:,None]*u*dt
        cen=P.mean(axis=0); dc=np.linalg.norm(P-cen,axis=1)
        Rr.append(np.sqrt((dc*dc).mean())); Dm.append(dc.max())
    Rr=np.array(Rr); Dm=np.array(Dm); n=len(Rr); wsl=slice(int(0.75*n),n)
    return {'R0':Rr[0],'Dmax0':Dm[0],'Rw':Rr[wsl].mean(),'Dmaxw':Dm[wsl].max(),
            'hb_ok':rel_ok,'Edrift':Edrift,'Vh':Vh,'m':m}

# ===== H-C-PRIME SUCCESSOR RIDER (in-patch, disclosed): G-SP failed BY LETTER at the
# pre-flagged marginal cell (bd=4, atP, dt=1/25: omega*dt=0.92 cannot resolve the
# 1.3 fm/c bond period -> relativity assert). Integrator mathematics, not law validity
# (11/12 cells HOLD, energy exact). The dt union was registered for the CHOREOGRAPHY
# timescale (2510 lineage); a law resolving faster motion requires dt below its own
# stability edge (the 2573 CTRL-4 lesson). H-C-prime = the identical law under the
# stiffness-qualified union {1/200, 1/100, 1/50} -- strictly FINER (tightens
# resolution; forced by pre-flagged stability math), three cells preserved.
# Everything else verbatim. Full gate battery re-runs first.

def n1_hc_kick(H0,C,SP,dtf,member,betad,dV0=None,coupling=1.0,TC=60):
    """n1_hc with initial home velocities dV0 (B-1b kicks / B-1c boost). Identical
    law; the only change is Vh initialization -- disclosed, cited to 2591 S1(b,c)."""
    global _KICK; _KICK=dV0
    return n1_hc(H0,C,SP,dtf,member,betad,coupling=coupling,TC=TC)


# ==================== PATCH 2596 -- N2-A: THE SINK + ADMISSION GATES ====================
# Derived (this patch, analytic core): oscillatory-KE shed fraction per Moment cycle
# eta in [0.5, 1.0] (R-A2 bounds), R-A1 interior estimates 0.68-0.74 (width-stable).
# Instrument expression (C-SR-exact BY CONSTRUCTION): at each Moment-cycle boundary,
# per home: Vdrift = cycle-mean of Vh; Vh <- Vdrift + sqrt(1-eta)*(Vh - Vdrift);
# Sea_deposit += eta * (1/2) m |Vh - Vdrift|^2. Uniform translation sheds ZERO exactly.
import time as _t
def n1_sink(H0,C,SP,dtf,betad,eta,coupling=1.0,TC=60,V0=None):
    NS=len(H0); A=amat(SP); qw=qw_of(SP,C); QW=np.outer(qw,qw); A2=A*A
    isE=np.array([s=='e' for s in SP]); m=np.where(isE,KE,KQ)
    dt=TAUC*dtf; nst=int(TC*TAUC/dt); spc=max(1,int(round(1.0/dtf)))
    H=np.array(H0,float).copy(); Vh=np.zeros((NS,3))
    if V0 is not None: Vh=Vh+V0
    Vacc=np.zeros((NS,3)); Sea=0.0; E0=None; Edrift=0.0; Rr=[]; Dm=[]; rel_ok=True
    for st in range(nst):
        ddh=H[:,None,:]-H[None,:,:]; r2h=(ddh*ddh).sum(axis=2); np.fill_diagonal(r2h,np.inf)
        Fe=(-((QW/(r2h+A2)**1.5))[:,:,None]*ddh*(-AHC)).sum(axis=1)
        Fs,Us=strong_FU(H,SP,betad)
        Ue=(np.triu(QW/np.sqrt(r2h+A2),1)).sum()*AHC
        Vh=Vh+((Fe+Fs)/m[:,None])*dt
        if np.linalg.norm(Vh,axis=1).max()>=0.9: rel_ok=False
        Vacc+=Vh
        if (st+1)%spc==0:
            Vbar=Vacc/spc; Vosc=Vh-Vbar
            KEpre=0.5*(m*(Vh*Vh).sum(axis=1)).sum()
            Vh=Vbar+np.sqrt(1-eta)*Vosc if eta<1.0 else Vbar.copy()
            KEpost=0.5*(m*(Vh*Vh).sum(axis=1)).sum()
            dep=KEpre-KEpost      # EXACT ledger: deposit = actual KE removed (2596
            Sea+=dep; Vacc[:]=0.0 # defect fix: the drift-osc cross term was unbooked)
        H=H+Vh*dt
        KEh=0.5*(m*(Vh*Vh).sum(axis=1)).sum()
        Etot=KEh+Us+Ue+Sea
        if E0 is None: E0=Etot
        Edrift=max(Edrift,abs(Etot-E0))
        cen=H.mean(axis=0); dc=np.linalg.norm(H-cen,axis=1)
        Rr.append(np.sqrt((dc*dc).mean())); Dm.append(dc.max())
    Rr=np.array(Rr); Dm=np.array(Dm); n=len(Rr); wsl=slice(int(0.75*n),n)
    return {'R0':Rr[0],'Dmax0':Dm[0],'Rw':Rr[wsl].mean(),'Dmaxw':Dm[wsl].max(),
            'hb_ok':rel_ok,'Edrift':Edrift,'Sea':Sea,'Vh':Vh,'m':m,'Rend':Rr[-1],'H':H}
# (Home-layer closed system: the sink acts on homes; the choreography layer is not the
#  energy carrier here and is omitted from these gate cells -- classifier on HOMES,
#  matching the replication-spec TIER-1 core. Declared.)

# ==================== PATCH 2600 -- N2-B B1: THE CAPTURE MAP ====================
# Under n2b_preregistration.md (2598) S1 only. Incident qCP (charge -1) from (b,0,4D)
# with velocity -v zhat onto the registered square at rest. Classifiers per prereg.
import time as _t, sys
t0=_t.time(); trunc_mode='DIST'
H4,C4,S4=rung(1)
SEEDS=(20260720,20260721,20260722)
def b1_cell(b,v,bd,eta,dtf,TC=120):
    H0=np.vstack([H4,[b*D,0.0,4*D]]); C0=np.append(C4,-1.0); S0=S4+['q']
    V0=np.zeros((5,3)); V0[4]=[0,0,-v]
    res=n1_sink(H0,C0,S0,dtf,bd,eta,TC=TC,V0=V0)
    return res
def b1_classify(res,H4ref):
    if not res['hb_ok']: return 'UNRES-REL'
    # final positions: res carries Vh and final H? n1_sink returns Rw/Dmaxw of whole
    # system; need per-particle final state -> extended return required.
    return None

def b1_run(b,v,bd,eta,dtf,TC=120):
    H0=np.vstack([H4,[b*D,0.0,4*D]]); C0=np.append(C4,-1.0); S0=S4+['q']
    V0=np.zeros((5,3)); V0[4]=[0,0,-v]
    res=n1_sink(H0,C0,S0,dtf,bd,eta,TC=TC,V0=V0)
    if not res['hb_ok']: return 'UNRES-REL',res
    Hf=res['H']; Vf=res['Vh']
    cen4=Hf[:4].mean(axis=0)
    d_inc=np.linalg.norm(Hf[4]-cen4)
    vr_inc=np.dot(Vf[4]-Vf[:4].mean(axis=0),(Hf[4]-cen4)/max(d_inc,1e-9))
    # square survival: its own members within 3D of its centroid
    d4=np.linalg.norm(Hf[:4]-cen4,axis=1)
    square_ok=(d4.max()<3*D)
    if d_inc<3*D and square_ok and res['Sea']>0: return 'CAPTURED',res
    if d_inc>4*D and vr_inc>0 and square_ok:     return 'SCATTERED',res
    if not square_ok:                            return 'FRAGMENTED',res
    return 'UNRES',res
BGRID=(0.0,0.5,1.0); VGRID=(0.05,0.10,0.20,0.30)
stage=sys.argv[1] if len(sys.argv)>1 else '100'
dtf={'100':1/100,'200':1/200}.get(stage,1/100)
if stage!='b3':
 if stage!="b3":
    print(f"=== B1 capture map, dt=tau/{int(1/dtf)} ===")
if stage!="b3":
  for eta in (0.5,0.7):
    for bd in (2.0,4.0):
        print(f"[eta={eta} bd={bd}]")
        for b in BGRID:
            row=[]
            for v in VGRID:
                cl,res=b1_run(b,v,bd,eta,dtf)
                tag={'CAPTURED':'CAP','SCATTERED':'SCA','FRAGMENTED':'FRG','UNRES-REL':'REL','UNRES':'UNR'}[cl]
                row.append(f"v={v}:{tag}(Sea={res['Sea']:.0f})")
            print(f"  b={b}D: "+"  ".join(row))
print(f"[{_t.time()-t0:.0f}s]")

# ---- B3: basin re-runs under the sink (prereg S3), reference-anchored ----
if stage=='b3':
    print("=== B3 basin re-runs under the sink ===")
    cen=H4.mean(axis=0); dc=np.linalg.norm(H4-cen,axis=1)
    R0_REF=float(np.sqrt((dc*dc).mean())); D0_REF=float(dc.max())
    def basin_cl(res):
        if not res['hb_ok']: return 'REL'
        if 0.5*R0_REF<=res['Rw']<=2.0*R0_REF and res['Dmaxw']<=3.0*D0_REF: return 'CONV'
        return 'AWAY' if res['Rw']>2.0*R0_REF else ('COLL' if res['Rw']<0.5*R0_REF else 'UNR')
    for dtf in (1/100,1/200):
        print(f"[dt=tau/{int(1/dtf)}]")
        for eta in (0.5,0.7):
            for bd in (2.0,4.0):
                row=[]
                for lbl,fac in (('x1.5',1.5),('x2.0',2.0),('x3.0',3.0),('x0.7',0.7),('x0.5',0.5)):
                    H0=cen+(H4-cen)*fac
                    res=n1_sink(H0,C4,S4,dtf,bd,eta,TC=120)
                    row.append(f"{lbl}:{basin_cl(res)}(S={res['Sea']:.0f},E={res['Edrift']:.1f})")
                for k,sd in enumerate(SEEDS):
                    rng=np.random.default_rng(sd+77)
                    H0=rng.uniform(-1.5*D,1.5*D,size=(4,3))
                    res=n1_sink(H0,C4,S4,dtf,bd,eta,TC=120)
                    row.append(f"r{k}:{basin_cl(res)}(S={res['Sea']:.0f})")
                print(f"  eta={eta} bd={bd}: "+" ".join(row))
        print(f"  [{_t.time()-t0:.0f}s]")
