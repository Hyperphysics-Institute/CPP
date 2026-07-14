#!/usr/bin/env python3
"""Computation #1 (Patch 2461) -- the spec-mandated v ~ SSV kinematics with DERIVED
parameters (H1 four voices + H3 folded), per the 2457 adjudication / 2460 handover gate.

Changes vs 2455 v4 (paired-schedule protocol kept; everything else identical):
(K1) SPEED: v_i = c*|SSV_i|/SSV_ref, SSV_i = INSTANTANEOUS net field-force vector on
     CP i, recomputed at each leg start from the reconstructed mid-flight positions of
     all other CPs (the faithful reading of "compute from current positions/charges"),
     soft-core-consistent with the energy (F = -grad E).
     PRE-REGISTERED SSV_ref = global max |SSV| over BOTH home scaffolds (one physical
     constant shared by ring and rod; fastest leg luminal). Stated before running.
(K2) WEIGHTS: target selection w_k = max(0, SSV_i . u_k) (field projection), replacing
     the w_i w_j / r^2 proxy. Fallback uniform-over-opposite if all projections <= 0.
(K3) PILE-UP WINDOW: t_pile = a_qq / v_arriving (transit across the saturation scale
     at the arriving CP's local speed), replacing the unpinned 0.3*tau.
(K4) PCD WAIT-AND-REPERCEIVE (integrator-artifact fix, DERIVED not tuned): a CP whose
     selected leg would exceed tau_cap = 1 Compton period of the registered qDP switch
     clock (2451: hw1 = 264 MeV bare) does not launch; it waits tauC/10 and re-perceives.
     Rationale: PCD is per-Moment -- a near-zero-SSV CP displaces ~zero THIS Moment and
     re-perceives; it never commits to a frozen kilo-fm/c leg. Without K4, floor-frozen
     legs manufacture a spurious ring-straight flip (+190..+304 MeV) that vanishes under
     ANY v-floor (0.05 -> -51; 0.2 -> -61) -- see the decomposition/sensitivity tables.

Outputs: decomposition (v4-repro; K2/K3/K1 alone; full), v-floor + tau_cap + SSV_ref
sensitivity, ring-straight (3 tau_cap x 3 seeds), ring modes, tilt-m=2 firming
(4 seeds, inverse-variance combined), Q1 variance discriminator (uniform/exchange/
rebound), Gemini mechanism verdict (kinematics shift ring vs rod + corr(v, PE)).
Runtime: ~40 schedule+replay runs; expect tens of minutes single-core."""
import numpy as np
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
d=1.15; A_Q=d; D=d; N=16
r_q=A_Q/np.sqrt(2); R_E=1.6*r_q; KAP=2*np.pi/(N*D); R0=1/KAP
A_QQ=AHC/264.0; A_EE=AHC/553.0; A_QE=np.sqrt(A_QQ*A_EE)
TAUC=2*np.pi*AHC/264.0

def ring_scaffold(tilt=None,ell=0.0):
    S=[]
    for k in range(N):
        phi=2*np.pi*k/N
        R=R0*(1+ell*np.cos(2*phi))
        cx=R*(1-np.cos(phi)); cz=R*np.sin(phi)
        th=phi+(tilt[k] if tilt is not None else 0.0)
        c,s=np.cos(th),np.sin(th); par=(-1)**k
        h=A_Q/2
        q=[(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)]
        for (x,y,sg) in q: S.append(((cx+x*c,y,cz-x*s),sg*par,'q',k))
        for (x,y,sg) in q:
            n=np.hypot(x,y); X,Y=R_E*x/n,R_E*y/n
            S.append(((cx+X*c,Y,cz-X*s),-sg*par,'e',k))
    P=np.array([s[0] for s in S]); C=np.array([float(s[1]) for s in S])
    return P,C,[s[2] for s in S]
def straight_scaffold(tilt=None):
    S=[]
    for k in range(N):
        th=(tilt[k] if tilt is not None else 0.0)
        c,s=np.cos(th),np.sin(th); par=(-1)**k
        h=A_Q/2
        q=[(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)]
        for (x,y,sg) in q: S.append(((x*c,y,k*D-x*s),sg*par,'q',k))
        for (x,y,sg) in q:
            n=np.hypot(x,y); X,Y=R_E*x/n,R_E*y/n
            S.append(((X*c,Y,k*D-X*s),-sg*par,'e',k))
    P=np.array([s[0] for s in S]); C=np.array([float(s[1]) for s in S])
    return P,C,[s[2] for s in S]
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
    """Static home-scaffold net field-force vectors (used only to SET SSV_ref)."""
    NS=len(P); W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP])
    qw=W*C; A=amat(SP)
    dd=P[:,None,:]-P[None,:,:]
    r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
    den=(r2+A*A)**1.5
    coef=np.outer(qw,qw)/den
    return (coef[:,:,None]*dd).sum(axis=1)*(-AHC)
def run(P,C,SP,geoms,SSV_ref,K1=True,K2=True,K3=True,K4=True,taucap=1.0,vfloor=1e-3,
        reading='rebound',TC=90,seed=42,nsamp=800,collect=False):
    """Schedule with selectable ingredients; replay on each geometry (paired)."""
    NS=len(P); rr=np.random.default_rng(seed)
    W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP]); qw=W*C
    reach=build_reach(P,C,SP); A=amat(SP)
    Ttot=TC*TAUC; tmax=taucap*TAUC; dtw=TAUC/10
    tn=np.zeros(NS); lp=-np.ones(NS,int)
    resv=np.zeros(NS); sup_until=np.zeros(NS); cur=[None]*NS
    legs=[]; home=P.copy(); nwait=0; vrec=[[] for _ in range(NS)]
    att=[np.array([W[i]*W[j]/max(0.3,np.linalg.norm(P[i]-P[j]))**2 for j in reach[i]]) for i in range(NS)]
    def positions_at(t):
        pos=home.copy()
        for m in range(NS):
            L=cur[m]
            if L is None: continue
            t0,tau,j=L
            if t0<=t<t0+2*tau:
                f=(t-t0)/tau; f=f if f<=1 else 2-f
                pos[m]=home[m]*(1-f)+home[j]*f
        return pos
    while True:
        i=int(np.argmin(tn))
        if tn[i]>=Ttot: break
        t=tn[i]
        if K1 or K2:
            pos=positions_at(t)
            dd=pos-pos[i]; r2=(dd*dd).sum(axis=1); r2[i]=np.inf
            den=(r2+A[i]*A[i])**1.5
            F=((qw[i]*qw/den)[:,None]*(-dd)).sum(axis=0)*(-AHC)
        vi=(max(min(np.linalg.norm(F)/SSV_ref,1.0),vfloor)) if K1 else 1.0
        cands=[]
        for k,j in enumerate(reach[i]):
            if j==lp[i]: continue
            opp=C[j]*C[i]<0
            if K2:
                u=home[j]-home[i]; nu=np.linalg.norm(u)
                wk=max(0.0,float(np.dot(F,u/nu))); ok=wk>0
            else:
                wk=att[i][k]; nu=np.linalg.norm(home[j]-home[i]); ok=True
            if SP[j]=='e':
                if opp and resv[j]<=t and ok: cands.append((k,wk,nu))
            else:
                if opp and ok: cands.append((k,wk,nu))
                elif sup_until[j]>t and ok: cands.append((k,wk*ALPHA_S,nu))
        if not cands:
            cands=[(k,1.0,np.linalg.norm(home[reach[i][k]]-home[i])) for k,j in enumerate(reach[i])
                   if C[j]*C[i]<0 and not (SP[j]=='e' and resv[j]>t) and j!=lp[i]]
        if not cands: tn[i]=t+dtw; continue
        if reading=='uniform': k,_,nu=cands[rr.integers(len(cands))]
        else:
            w=np.array([c[1] for c in cands]); k,_,nu=cands[rr.choice(len(cands),p=w/w.sum())]
        if K1 and K4 and (vi<=0 or nu/vi>tmax):
            tn[i]=t+dtw; nwait+=1; continue          # (K4) PCD wait-and-reperceive
        j=reach[i][k]; tau=nu/vi
        legs.append((i,j,t,tau)); vrec[i].append(vi)
        if SP[j]=='e': resv[j]=t+tau
        else: sup_until[j]=max(sup_until[j],t+tau+(A_QQ/vi if K3 else 0.3*tau))
        if reading=='exchange':
            home[i],home[j]=home[j].copy(),home[i].copy()
            cur[i]=(t,tau,j); lp[i]=j; lp[j]=i; tn[i]=t+tau; tn[j]=max(tn[j],t+tau)
        else:
            cur[i]=(t,tau,j); lp[i]=j; tn[i]=t+2*tau
    ts=np.linspace(0.02*Ttot,0.999*Ttot,nsamp)
    bycp=[[] for _ in range(NS)]
    for (i,j,t,tau) in legs: bycp[i].append((t,tau,j))
    out=[]
    for Pg in geoms:
        pos=np.tile(Pg[None,:,:],(nsamp,1,1)).astype(float)
        for i in range(NS):
            for (t,tau,j) in bycp[i]:
                m=(ts>=t)&(ts<t+2*tau)
                if not m.any(): continue
                f=(ts[m]-t)/tau; f=np.where(f<=1,f,2-f)
                pos[m,i]=Pg[i][None,:]*(1-f[:,None])+Pg[j][None,:]*f[:,None]
        E=np.zeros(nsamp)
        for s in range(nsamp):
            dd=pos[s][:,None,:]-pos[s][None,:,:]
            r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
            r=np.sqrt(r2+A*A)
            E[s]=0.5*np.sum(np.outer(qw,qw)/r)*AHC
        out.append(E)
    if collect: return out,legs,vrec,nwait
    return out

if __name__=='__main__':
    Pr,Cr,SPr=ring_scaffold(); Ps,Cs,SPs=straight_scaffold()
    Fr=ssv_vectors(Pr,Cr,SPr); Fs=ssv_vectors(Ps,Cs,SPs)
    REF=max(np.linalg.norm(Fr,axis=1).max(),np.linalg.norm(Fs,axis=1).max())
    print(f"SSV_ref (pre-registered: global max over both home scaffolds) = {REF:.2f} MeV/fm")
    print(f"  ring |SSV| min/med/max = {np.linalg.norm(Fr,axis=1).min():.1f}/"
          f"{np.median(np.linalg.norm(Fr,axis=1)):.1f}/{np.linalg.norm(Fr,axis=1).max():.1f} ; "
          f"rod = {np.linalg.norm(Fs,axis=1).min():.1f}/"
          f"{np.median(np.linalg.norm(Fs,axis=1)):.1f}/{np.linalg.norm(Fs,axis=1).max():.1f}")
    print("\n[A] decomposition, NO wait rule (K4 off; exposes the integrator artifact):")
    for name,kw in [("v4-repro (none) ",dict(K1=False,K2=False,K3=False,K4=False)),
                    ("K2 only         ",dict(K1=False,K2=True ,K3=False,K4=False)),
                    ("K3 only         ",dict(K1=False,K2=False,K3=True ,K4=False)),
                    ("K1 only         ",dict(K1=True ,K2=False,K3=False,K4=False)),
                    ("K1+K2+K3        ",dict(K1=True ,K2=True ,K3=True ,K4=False))]:
        for seed in (42,7):
            (Es,)=run(Ps,Cs,SPs,[Ps],REF,seed=seed,**kw)
            (Er,)=run(Pr,Cr,SPr,[Pr],REF,seed=seed,**kw)
            sig=np.sqrt(Es.var()+Er.var())/np.sqrt(len(Es))
            print(f"  {name} seed {seed:>3}: ring-straight = {Er.mean()-Es.mean():+8.1f} +- {sig:5.1f}")
    print("\n[B] v-floor sensitivity, full K1+K2+K3 no-wait (artifact vanishes under any floor):")
    for vf in (1e-3,0.05,0.2):
        (Es,)=run(Ps,Cs,SPs,[Ps],REF,seed=42,K4=False,vfloor=vf)
        (Er,)=run(Pr,Cr,SPr,[Pr],REF,seed=42,K4=False,vfloor=vf)
        print(f"  vfloor={vf:<6}: {Er.mean()-Es.mean():+8.1f} +- "
              f"{np.sqrt(Es.var()+Er.var())/np.sqrt(len(Es)):5.1f}")
    print("\n[C] FINAL (K1-K4), ring-straight, tau_cap x seeds:")
    for tc in (0.5,1.0,2.0):
        for seed in (42,7,123):
            (Es,)=run(Ps,Cs,SPs,[Ps],REF,taucap=tc,seed=seed)
            (Er,)=run(Pr,Cr,SPr,[Pr],REF,taucap=tc,seed=seed)
            sig=np.sqrt(Es.var()+Er.var())/np.sqrt(len(Es))
            print(f"  tau_cap={tc:3.1f} seed {seed:>3}: {Er.mean()-Es.mean():+8.1f} +- {sig:5.1f}")
    print("\n[D] FINAL ring modes (tau_cap=1, seeds 42/7) + m=2 firming (4 seeds):")
    modes={'tilt m=0':(dict(tilt=[0.04]*N),0.04),
           'tilt m=1':(dict(tilt=[0.04*np.cos(2*np.pi*k/N) for k in range(N)]),0.04),
           'tilt m=2':(dict(tilt=[0.04*np.cos(4*np.pi*k/N) for k in range(N)]),0.04),
           'ellipt  ':(dict(ell=0.02),0.02)}
    for seed in (42,7):
        geoms=[Pr]+[ring_scaffold(**kw)[0] for kw,_ in modes.values()]
        El=run(Pr,Cr,SPr,geoms,REF,seed=seed)
        E0=El[0]
        for (name,(kw,x)),Ep in zip(modes.items(),El[1:]):
            dE=Ep-E0; c2=2*dE.mean()/x**2; er=2*dE.std()/np.sqrt(len(dE))/x**2
            v='STABLE' if c2>er else ('MARGINAL' if abs(c2)<2*er else 'UNSTABLE')
            print(f"  seed {seed:>3} {name}  d2E/dx2 = {c2:+9.0f} +- {er:<8.0f} {v}")
    tilt2=[0.04*np.cos(4*np.pi*k/N) for k in range(N)]; P2=ring_scaffold(tilt=tilt2)[0]
    vals=[]
    for seed in (42,7,123,2026):
        E0,Ep=run(Pr,Cr,SPr,[Pr,P2],REF,seed=seed)
        dE=Ep-E0; c2=2*dE.mean()/0.04**2; er=2*dE.std()/np.sqrt(len(dE))/0.04**2
        vals.append((c2,er)); print(f"  m=2 seed {seed:>4}: {c2:+8.0f} +- {er:.0f}")
    w=np.array([1/e**2 for _,e in vals]); m=np.array([c for c,_ in vals])
    comb=(w*m).sum()/w.sum(); ce=1/np.sqrt(w.sum())
    print(f"  m=2 COMBINED: {comb:+.0f} +- {ce:.0f}  ({abs(comb/ce):.1f} sigma)")
    print("\n[E] Q1 variance discriminator (ring, FINAL kinematics):")
    for reading in ('uniform','exchange','rebound'):
        (E,),legs,_,nw=run(Pr,Cr,SPr,[Pr],REF,reading=reading,seed=42,collect=True)
        print(f"  {reading:8s}: <E> = {E.mean():+9.1f}  std = {E.std():7.1f}  legs={len(legs)} waits={nw}")
    print("\n[F] Gemini mechanism verdict:")
    (Er_k,)=run(Pr,Cr,SPr,[Pr],REF,seed=42)
    (Es_k,)=run(Ps,Cs,SPs,[Ps],REF,seed=42)
    (Er_c,)=run(Pr,Cr,SPr,[Pr],REF,K1=False,seed=42)
    (Es_c,)=run(Ps,Cs,SPs,[Ps],REF,K1=False,seed=42)
    print(f"  kinematics shift: ring {Er_k.mean()-Er_c.mean():+.1f}, rod {Es_k.mean()-Es_c.mean():+.1f},"
          f" differential {(Er_k.mean()-Er_c.mean())-(Es_k.mean()-Es_c.mean()):+.1f} MeV (against the ring)")
    def pe_share(P,C,SP):
        W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP]); qw=W*C
        A=amat(SP); dd=P[:,None,:]-P[None,:,:]
        r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
        return (np.outer(qw,qw)/np.sqrt(r2+A*A)).sum(axis=1)*AHC
    _,_,vr,_=run(Pr,Cr,SPr,[Pr],REF,seed=42,collect=True)
    _,_,vs,_=run(Ps,Cs,SPs,[Ps],REF,seed=42,collect=True)
    mvr=np.array([np.mean(v) if v else 0 for v in vr]); mvs=np.array([np.mean(v) if v else 0 for v in vs])
    print(f"  corr(mean v, per-CP PE): ring {np.corrcoef(mvr,pe_share(Pr,Cr,SPr))[0,1]:+.3f}, "
          f"rod {np.corrcoef(mvs,pe_share(Ps,Cs,SPs))[0,1]:+.3f}"
          f"  (positive = slow CPs at DEEP binding, not high PE)")
