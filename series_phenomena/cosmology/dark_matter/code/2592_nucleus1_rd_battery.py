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

# ============================ PATCH 2592 -- R-D BATTERY ============================
# Under nucleus1_rd_preregistration.md (2591) only. Member: atH (the admissible set,
# 2588 G-CONS). PRE-RUN DECLARATIONS (this header, before any cell):
#  * Truncation union: for every battery configuration (<=5 qCPs, and the RUNG-1
#    square), per-step max |inpl+axl| is TRACKED; if it never exceeds 5, DIST==FULL
#    BY CONSTRUCTION (the cutoff is inert) and the union collapses legitimately --
#    the analytic-collapse lesson (2577) applied in the benign direction, asserted
#    not assumed.
#  * G-SP count reconciliation: the 2591 S0 "(12 cells)" was drafted from the 2585
#    two-member shape; the admissible set is {atH} (2588), so the full G-SP set for
#    the member in use is 6 cells (2 widths x 3 dt). Disclosed.
#  * B-4 classifier operationalization (declared BEFORE any B-4 cell): the 2581
#    bands anchor on a run's own R0, which is unfit for basin runs (an expansion x2
#    start converging to the square would read COLLAPSE against its own inflated
#    R0). The S4 intent ("does the melee PULL the configuration into the hold") is
#    operationalized REFERENCE-ANCHORED: convergence iff the final window satisfies
#    the 2581 bands measured against the REGISTERED SQUARE's R0/Dmax0. Non-basin
#    items (B-1/B-2/B-3) keep the verbatim self-anchored bands.
#  * Seeds fixed per prereg: {20260720, 20260721, 20260722}.
import time as _t
MAXCNT=[0]
_orig_build=build_reach_S
def build_reach_S(P,C,SP):
    NS=len(P)
    for i in range(NS):
        if SP[i]!='q': continue
        dd=P-P[i]; r=np.sqrt((dd*dd).sum(axis=1)); r[i]=np.inf
        ki=i//8
        inpl=[j for j in range(NS) if SP[j]=='q' and j//8==ki and r[j]<1.8]
        axl=[j for j in range(NS) if SP[j]=='q' and j//8!=ki and r[j]<1.3]
        MAXCNT[0]=max(MAXCNT[0],len(set(inpl+axl)))
    return _orig_build(P,C,SP)

t0=_t.time(); DTS=(1/200,1/100,1/50); SEEDS=(20260720,20260721,20260722)
import sys; STAGE=sys.argv[1] if len(sys.argv)>1 else "all"
trunc_mode='DIST'
print("="*78); print("PATCH 2592 -- R-D: THE CONFIRMATION BATTERY"); print("="*78)

# reference square metrics for B-4 anchoring
H4,C4,S4=rung(1)
cen=H4.mean(axis=0); dc=np.linalg.norm(H4-cen,axis=1)
R0_REF=float(np.sqrt((dc*dc).mean())); D0_REF=float(dc.max())

def run(H0,C,SP,dtf,bd,TC=60,V0=None):
    if V0 is not None:
        # boost: implemented as initial home velocities (n1_hc reads Vh=0; extend inline)
        pass
    return n1_hc(np.array(H0,float),np.array(C,float),SP,dtf,'atH',bd,TC=TC)

# --- gates ---
print("[gates]")
gok=True
def Upair(r,bd):
    e=np.exp(-(bd/D)*(r-D)); return -ALPHA_S*AHC/np.sqrt(r*r+A_QQ*A_QQ)+EQQ*((1-e)**2-1)
for bd in (2.0,4.0):
    rs=np.linspace(0.3,3.0,2701); req=rs[int(np.argmin([Upair(r,bd) for r in rs]))]
    row=[]
    for dtf in DTS:
        res=run([[0,0,0],[0,0,req]],[+1,-1],['q','q'],dtf,bd)
        cl=classify(res); row.append(cl); gok&=(cl=='HOLD')
        gok&=(res['Edrift']<FLOOR)
    print(f"  G-SP bd={bd}: {row}  Edrift ok")
r=run([[0,0,0]],[+1],['q'],1/100,4.0)
gok&=(np.linalg.norm(r['Vh'])<1e-12); print(f"  G-N1: |V|={np.linalg.norm(r['Vh']):.1e}")
for rg in (1,2,3):
    H0,C,SP=rung(rg); res=n1_hc(H0,C,SP,1/100,'atH',4.0,coupling=0.0)
    gok&=(classify(res)=='HOLD')
print(f"  G-N2: HOLD x3   GATES {'ALL PASS' if gok else 'FAIL -> HALT'}")
assert gok

if STAGE in ('1','all'):
 _=0
# --- B-1a noise ---
print("\n[B-1a] position noise (eps x seeds; both widths; dt union):")
edge=None
for eps in (0.02,0.05,0.10):
    fails=0; cells=0
    for sd in SEEDS:
        rng=np.random.default_rng(sd)
        dH=rng.normal(size=(4,3)); dH=dH/np.linalg.norm(dH,axis=1)[:,None]*eps*D
        for bd in (2.0,4.0):
            for dtf in DTS:
                res=run(H4+dH,C4,S4,dtf,bd); cells+=1
                if classify(res)!='HOLD': fails+=1
    print(f"  eps={eps:.2f}D: {cells-fails}/{cells} HOLD")
    if fails and edge is None: edge=eps
print(f"  edge eps* = {edge if edge else 'not reached (<=0.10D all hold)'}")

# --- B-1b kicks ---
print("[B-1b] velocity kicks:")
vedge=None
for vk in (0.01,0.03,0.05):
    fails=0; cells=0
    for sd in SEEDS:
        rng=np.random.default_rng(sd+7)
        dV=rng.normal(size=(4,3)); dV=dV/np.linalg.norm(dV,axis=1)[:,None]*vk
        for bd in (2.0,4.0):
            for dtf in DTS:
                # inject initial velocities via a thin wrapper: shift homes by dV*dt0? no --
                # extend n1_hc minimally: emulate by first-step impulse: add dV to Vh via
                # a pre-step: use H0 and set initial Vh through monkey state:
                res=n1_hc_kick(H4.copy(),C4,S4,dtf,'atH',bd,dV0=dV); cells+=1
                if classify(res)!='HOLD': fails+=1
    print(f"  v={vk:.2f}c: {cells-fails}/{cells} HOLD")
    if fails and vedge is None: vedge=vk
print(f"  edge v* = {vedge if vedge else 'not reached (<=0.05c all hold)'}")

# --- B-1c boost ---
print("[B-1c] Galilean boost (verdict + R must match rest frame within floor-equivalents):")
rest={}
for bd in (2.0,4.0):
    res=run(H4,C4,S4,1/100,bd); rest[bd]=res['Rw']/res['R0']
for V in (0.1,0.3):
    for dvec,nm in (((0,0,1),'z'),((1/np.sqrt(2),1/np.sqrt(2),0),'diag')):
        for bd in (2.0,4.0):
            res=n1_hc_kick(H4.copy(),C4,S4,1/100,'atH',bd,dV0=np.tile(np.array(dvec)*V,(4,1)))
            ok=(classify(res)=='HOLD') and abs(res['Rw']/res['R0']-rest[bd])<0.05
            print(f"  V={V}c {nm} bd={bd}: {classify(res)} dR={res['Rw']/res['R0']-rest[bd]:+.4f} {'PASS' if ok else 'FAIL'}")

# --- B-2 endurance ---
print("[B-2] endurance:")
for bd in (2.0,4.0):
    for dtf in DTS:
        res=run(H4,C4,S4,dtf,bd,TC=300)
        print(f"  TC=300 bd={bd} dt=1/{int(1/dtf)}: {classify(res)} R={res['Rw']/res['R0']:.2f} Edrift={res['Edrift']:.3f}")
for bd in (2.0,4.0):
    res=run(H4,C4,S4,1/100,bd,TC=600)
    print(f"  TC=600 bd={bd}: {classify(res)} R={res['Rw']/res['R0']:.2f} Edrift={res['Edrift']:.3f}")

# --- B-3 minimality census ---
print("[B-3] minimality census:")
h=A_Q/2
cfg={'2':( [[-0,0,0],[0,0,D]], [+1,-1], ['q','q']),
     '3':( [[+h,+h,0],[-h,+h,0],[-h,-h,0]], [+1,-1,+1], ['q','q','q']),
     '4c':(H4.tolist(), C4.tolist(), S4),
     '5':( H4.tolist()+[[+h,+h,D]], C4.tolist()+[-1], S4+['q'])}
for nm,(P0,C0,S0) in cfg.items():
    row=[]
    for bd in (2.0,4.0):
        for dtf in DTS:
            res=run(P0,C0,S0,dtf,bd)
            row.append(classify(res))
    u=set(row)
    print(f"  {nm}: {'HOLD x6' if u=={'HOLD'} else row}")

# --- B-4 basin (REFERENCE-ANCHORED per header) ---
def basin_classify(res):
    if not res['hb_ok']: return 'UNRES-NUM'
    if 0.5*R0_REF<=res['Rw']<=2.0*R0_REF and res['Dmaxw']<=3.0*D0_REF: return 'CONVERGED'
    if res['Rw']<0.5*R0_REF: return 'COLLAPSED'
    if res['Rw']>2.0*R0_REF: return 'AWAY'
    return 'UNRES'
print("[B-4] basin (reference-anchored):")
for lbl,fac in (('x1.5',1.5),('x2.0',2.0),('x3.0',3.0),('x0.7',0.7),('x0.5',0.5)):
    row=[]
    for bd in (2.0,4.0):
        for dtf in DTS:
            cen=H4.mean(axis=0)
            H0=cen+(H4-cen)*fac
            res=run(H0,C4,S4,dtf,bd)
            row.append(basin_classify(res))
    u=set(row)
    print(f"  {lbl}: {'CONVERGED x6' if u=={'CONVERGED'} else row}")
print("  random-in-box (3D, seeds, charges +-+-):")
for sd in SEEDS:
    rng=np.random.default_rng(sd+77)
    row=[]
    for bd in (2.0,4.0):
        H0=rng.uniform(-1.5*D,1.5*D,size=(4,3))
        res=run(H0,C4,S4,1/100,bd,TC=120)
        row.append(basin_classify(res))
    print(f"   seed {sd}: {row}")
print(f"\n[trunc] max in-reach count across ALL battery runs: {MAXCNT[0]} "
      f"({'<=5 -> DIST==FULL by construction, union collapses legitimately' if MAXCNT[0]<=5 else 'BINDS -> FULL member required'})")
print(f"[{_t.time()-t0:.0f}s]")
