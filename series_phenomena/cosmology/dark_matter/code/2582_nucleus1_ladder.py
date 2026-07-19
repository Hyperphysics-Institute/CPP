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

t0=time.time(); DTS=(1/100,1/50,1/25)
print("="*78); print("PATCH 2582 -- NUCLEUS-1: controls, then the ladder"); print("="*78)

# CTRL-N1 singleton
P0=np.array([[0.,0.,0.]]); C0=np.array([+1.]); S0=['q']
r=n1_run(P0,C0,S0,1/50,'HA')
print(f"CTRL-N1 singleton at rest: |V|={np.linalg.norm(r['Vh']):.2e}, drift={np.linalg.norm(r['P'][0]):.2e}  "
      f"{'PASS' if np.linalg.norm(r['Vh'])<1e-9 and np.linalg.norm(r['P'][0])<1e-6 else 'FAIL'}")

# CTRL-N2 pinned regression (coupling=0) on each rung
print("CTRL-N2 pinned regression (coupling=0):")
n2ok=True
for rg in (1,2,3):
    H0,C,SP=rung(rg)
    res=n1_run(H0,C,SP,1/50,'HA',coupling=0.0)
    cl=classify(res); n2ok&= (cl=='HOLD')
    print(f"  RUNG-{rg}: {cl}  (Rw/R0={res['Rw']/res['R0']:.3f})")
print(f"  {'PASS' if n2ok else 'FAIL'}")

# CTRL-N3 the pair must NOT hold (both conventions)
print("CTRL-N3 pair continuity (must NOT hold):")
n3ok=True
Hp,Cp,Sp=pair_config()
for conv in ('HA','HB'):
    row=[]
    for dtf in DTS:
        res=n1_run(Hp,Cp,Sp,dtf,conv)
        cl=classify(res); row.append(cl)
        if cl=='HOLD': n3ok=False
    print(f"  {conv}: "+" ".join(row))
print(f"  {'PASS' if n3ok else 'FAIL'}")

# CTRL-N4 momentum (H-B, asymmetric RUNG-1)
H0,C,SP=rung(1); H0=H0+0.0
H0[0]+=np.array([0.07,0.03,0.0])   # asymmetric perturbation of one home
m=np.array([KQ]*4)
res=n1_run(H0,C,SP,1/100,'HB')
Ptot=np.linalg.norm((m[:,None]*res['Vh']).sum(axis=0))
print(f"CTRL-N4 momentum (H-B asym): |P_tot|={Ptot:.3e} MeV  "
      f"{'PASS' if Ptot<1e-3*KQ else 'FAIL'}")

# ---- THE LADDER (truncation union: DIST primary, FULL secondary) ----
for tm in ('DIST','FULL'):
  trunc_mode=tm
  print(f"\n===== truncation member: {tm} =====")
  for rg in (1,2,3):
    H0,C,SP=rung(rg)
    print(f"### RUNG-{rg}  (N={len(H0)} CPs)")
    for conv in ('HA','HB'):
        row=[]
        for dtf in DTS:
            res=n1_run(H0,C,SP,dtf,conv)
            cl=classify(res); clw=classify(res,widened=True)
            row.append(f"dt=1/{int(1/dtf)}:{cl}{'' if cl==clw else '('+clw+'w)'}"
                       f"[Rw/R0={res['Rw']/max(res['R0'],1e-9):.2f},Dm/D0={res['Dmaxw']/max(res['Dmax0'],1e-9):.2f}]")
        print(f"  {conv}: "+"  ".join(row))
print(f"\n[{time.time()-t0:.0f}s]")
