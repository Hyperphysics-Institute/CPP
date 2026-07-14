#!/usr/bin/env python3
"""ZBW dance v4 -- founder's four confirmations implemented (Patch 2455):
(1) reach = {2 in-plane edge + 1 in-plane diagonal + 2 axial} qCP + 1 radial eCP
(2) plane geometry: eCP-qCP-qCP-eCP on both diagonals (confirmed = 2454 implementation)
(3) asymmetric preemption: eCP target exclusive (preempt -> rebound home, repick);
    qCP target NON-exclusive (strong-force continuation -> multi-CP superposition
    pile-ups; same-charge targeting of currently-superposed qCP sites enabled)
(4) species-derived soft-core: a_qq = hc/264 = 0.747, a_ee = hc/553 = 0.357 (=registered
    lambda-bar, 1814), a_qe = 0.516 fm; contact-depth check alpha_s*hc/a_qq = 102 MeV
    in the E_qq deep branch [40,170] -- consistency lock.
Decisive outputs: ring-straight; ring's own modes (tilt m=0,1,2; ellipticity)."""
import numpy as np
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
d=1.15; A_Q=d; D=d; N=16
r_q=A_Q/np.sqrt(2); R_E=1.6*r_q; KAP=2*np.pi/(N*D); R0=1/KAP
A_QQ=AHC/264.0; A_EE=AHC/553.0; A_QE=np.sqrt(A_QQ*A_EE)
print(f"derived soft-cores: a_qq={A_QQ:.3f}, a_ee={A_EE:.3f} (=1814 lambda-bar 0.357), a_qe={A_QE:.3f} fm")
print(f"contact-depth check: alpha_s*hc/a_qq = {ALPHA_S*AHC/A_QQ:.1f} MeV vs E_qq deep branch [40,170]")
print()
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
            # founder set: all in-plane qCPs (2 edge + 1 diagonal) + axial-direct (r<1.3
            # inter-plane) + radial eCP -- select by shells:
            inpl=[j for j in range(NS) if SP[j]=='q' and abs(P[j][2]-P[i][2])<0.5*D and r[j]<1.8]
            axl=[j for j in range(NS) if SP[j]=='q' and 0.5*D<abs(P[j][2]-P[i][2]) and r[j]<1.3]
            # (for the ring, 'axial' = along the arc: use r<1.3 non-in-plane)
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
def run_and_energy(P,C,SP,geoms,vc=1.0,TC=90,seed=42,nsamp=800):
    """schedule on base scaffold P with v4 rules; replay positions on each geometry in
       geoms (list of P arrays); return list of energy sample arrays (paired)."""
    NS=len(P); rr=np.random.default_rng(seed)
    W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP])
    reach=build_reach(P,C,SP)
    tauC=2*np.pi*AHC/264.0; Ttot=TC*tauC
    att=[np.array([W[i]*W[j]/max(0.3,np.linalg.norm(P[i]-P[j]))**2 for j in reach[i]]) for i in range(NS)]
    tn=np.zeros(NS); lp=-np.ones(NS,int)
    resv=np.zeros(NS)                  # eCP exclusivity only
    sup_until=np.zeros(NS)             # qCP site superposed while visitors present
    legs=[]
    while True:
        i=int(np.argmin(tn))
        if tn[i]>=Ttot: break
        t=tn[i]
        cands=[]
        for k,j in enumerate(reach[i]):
            if j==lp[i]: continue
            opp = C[j]*C[i]<0
            if SP[j]=='e':
                if opp and resv[j]<=t: cands.append((k,att[i][k]))
            else:
                if opp: cands.append((k,att[i][k]))
                elif sup_until[j]>t: cands.append((k,att[i][k]*ALPHA_S))  # strong-force pull to pile-up
        if not cands:
            cands=[(k,att[i][k]) for k,j in enumerate(reach[i]) if C[j]*C[i]<0]
            if not cands: tn[i]=t+0.05; continue
        w=np.array([c[1] for c in cands]); k=cands[rr.choice(len(cands),p=w/w.sum())][0]
        j=reach[i][k]; tau=np.linalg.norm(P[i]-P[j])/vc
        legs.append((i,j,t,tau))
        if SP[j]=='e': resv[j]=t+tau
        else: sup_until[j]=max(sup_until[j],t+tau+0.3*tau)   # pile-up window
        lp[i]=j; tn[i]=t+2*tau
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
        qw=W*C; E=np.zeros(nsamp)
        Amat=np.zeros((NS,NS))
        for i in range(NS):
            for j in range(NS):
                Amat[i,j]=soft_a(SP[i],SP[j])
        for s in range(nsamp):
            dd=pos[s][:,None,:]-pos[s][None,:,:]
            r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
            r=np.sqrt(r2+Amat*Amat)
            E[s]=0.5*np.sum(np.outer(qw,qw)/r)*AHC
        out.append(E)
    return out,len(legs)
# ---- ring-straight (paired via separate schedules on own scaffolds; report both) ----
Pr,Cr,SPr=ring_scaffold(); Ps,Cs,SPs=straight_scaffold()
(Es,),nl1=run_and_energy(Ps,Cs,SPs,[Ps])
(Er,),nl2=run_and_energy(Pr,Cr,SPr,[Pr])
print(f"[v4, derived a] straight <E>={Es.mean():+.1f}+-{Es.std()/np.sqrt(len(Es)):.1f} ; "
      f"ring <E>={Er.mean():+.1f}+-{Er.std()/np.sqrt(len(Er)):.1f}")
print(f"  ring-straight = {Er.mean()-Es.mean():+.1f} +- {np.sqrt(Es.var()+Er.var())/np.sqrt(len(Es)):.1f} MeV")
print(f"  (legs: {nl1}/{nl2}; pile-up channel active)")
print()
# ---- ring's own modes (paired replay, one schedule on the ring) ----
modes={'tilt m=0':(dict(tilt=[0.04]*N),0.04),
       'tilt m=1':(dict(tilt=[0.04*np.cos(2*np.pi*k/N) for k in range(N)]),0.04),
       'tilt m=2':(dict(tilt=[0.04*np.cos(4*np.pi*k/N) for k in range(N)]),0.04),
       'ellipt  ':(dict(ell=0.02),0.02)}
geoms=[Pr]+[ring_scaffold(**kw)[0] for kw,_ in modes.values()]
Elist,_=run_and_energy(Pr,Cr,SPr,geoms)
E0=Elist[0]
print("ring's own modes (v4, derived a):")
for (name,(kw,x)),Ep in zip(modes.items(),Elist[1:]):
    dE=Ep-E0; cur=2*dE.mean()/x**2; er=2*dE.std()/np.sqrt(len(dE))/x**2
    print(f"  {name}  d2E/dx2 = {cur:+9.0f} +- {er:<7.0f} {'STABLE' if cur>er else ('MARGINAL' if abs(cur)<2*er else 'UNSTABLE')}")
