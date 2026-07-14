#!/usr/bin/env python3
"""ZBW dance v3 -- HOME-ANCHORED REBOUND (founder: 'reverse direction' = superposition-
rebound, 2433). Each CP oscillates home->partner->home, next leg to a different partner
(SSV-weighted), contention via target reservation. The mode-resolved MEAN DANCE ENERGY
is the single stability object (BO-valid: leg time ~ fm/c << mode timescales; the
founder's same/opposite apposition tension is inside the trajectory ensemble).
Common random numbers: one leg schedule generated on the straight scaffold, replayed on
displaced scaffolds (paired differences -> tight curvatures)."""
import numpy as np
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
d=1.15; A_Q=d; D=d; N=16
r_q=A_Q/np.sqrt(2); R_E=1.6*r_q
def scaffold(centers,angles):
    S=[]
    for k in range(N):
        cx,cy,cz=centers[k]; th=angles[k]; c,s=np.cos(th),np.sin(th); par=(-1)**k
        h=A_Q/2
        q=[(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)]
        for (x,y,sg) in q:
            S.append(((cx+x*c,cy+y,cz-x*s),sg*par,'q',k))
        for (x,y,sg) in q:
            n=np.hypot(x,y); X,Y=R_E*x/n,R_E*y/n
            S.append(((cx+X*c,cy+Y,cz-X*s),-sg*par,'e',k))
    P=np.array([s[0] for s in S]); C=np.array([float(s[1]) for s in S])
    return P,C,[s[2] for s in S],np.array([s[3] for s in S])
straightC=[(0,0,k*D) for k in range(N)]
P0,C0,SP,PL=scaffold(straightC,[0.0]*N); NS=len(P0)
W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP])
reach=[]
for i in range(NS):
    dd=P0-P0[i]; r=np.sqrt((dd*dd).sum(axis=1)); r[i]=np.inf
    if SP[i]=='q':
        cand=[j for j in range(NS) if C0[j]*C0[i]<0 and ((SP[j]=='q' and r[j]<2.1) or (SP[j]=='e' and r[j]<0.6))]
    else:
        cand=[j for j in range(NS) if C0[j]*C0[i]<0 and ((SP[j]=='e' and r[j]<2.6) or (SP[j]=='q' and r[j]<0.6))]
    reach.append(cand)
print("partner counts (interior qCP):",sorted(set(len(reach[i]) for i in range(NS) if SP[i]=='q' and 2<=PL[i]<=13)))
# ---- generate the leg SCHEDULE on the straight scaffold ----
def make_schedule(vc,TC,seed):
    rr=np.random.default_rng(seed)
    tauC=2*np.pi*AHC/264.0; Ttot=TC*tauC
    att0=[np.array([W[i]*W[j]/np.linalg.norm(P0[i]-P0[j])**2 for j in reach[i]]) for i in range(NS)]
    tnow=np.zeros(NS); lastp=-np.ones(NS,int)
    resv_until=np.zeros(NS)
    legs=[]  # (i, j, t_start, t_out, t_back)  out-and-back
    heap=list(range(NS)); 
    while True:
        i=int(np.argmin(tnow))
        if tnow[i]>=Ttot: break
        t=tnow[i]
        cand=[k for k,j in enumerate(reach[i]) if j!=lastp[i] and resv_until[j]<=t]
        if not cand:
            cand=[k for k,j in enumerate(reach[i]) if resv_until[j]<=t]
        if not cand:
            tnow[i]=t+0.05; continue
        w=att0[i][cand]; k=cand[rr.choice(len(cand),p=w/w.sum())]
        j=reach[i][k]
        r=np.linalg.norm(P0[i]-P0[j]); tau=r/vc
        legs.append((i,j,t,tau))
        resv_until[j]=t+tau          # visitor slot reserved for the outbound
        lastp[i]=j; tnow[i]=t+2*tau  # out and back
    return legs,Ttot
vc=1.0; TC=120; seed=42
legs,Ttot=make_schedule(vc,TC,seed)
print(f"schedule: {len(legs)} legs over {TC} Compton periods")
# ---- replay on a scaffold; sample positions; mean pair energy ----
def mean_energy(P,nsamp=1200):
    ts=np.linspace(0.02*Ttot,Ttot*0.999,nsamp)
    # build per-CP leg lookup
    bycp=[[] for _ in range(NS)]
    for (i,j,t,tau) in legs: bycp[i].append((t,tau,j))
    E=np.zeros(nsamp)
    pos=np.tile(P[None,:,:],(nsamp,1,1)).astype(float)
    for i in range(NS):
        for (t,tau,j) in bycp[i]:
            m=(ts>=t)&(ts<t+2*tau)
            if not m.any(): continue
            f=(ts[m]-t)/tau; f=np.where(f<=1,f,2-f)   # out then back
            pos[m,i]=P[i][None,:]*(1-f[:,None])+P[j][None,:]*f[:,None]
    qw=(W*C0)
    for s in range(nsamp):
        dd=pos[s][:,None,:]-pos[s][None,:,:]
        r=np.sqrt((dd*dd).sum(axis=2)); np.fill_diagonal(r,np.inf)
        r=np.maximum(r,0.05)
        E[s]=0.5*np.sum(np.outer(qw,qw)/r)*AHC
    return E,pos
def geom_bend(kap):
    if abs(kap)<1e-12: return scaffold(straightC,[0.0]*N)[0]
    R=1/kap; ph=[k*D/R for k in range(N)]
    return scaffold([(R*(1-np.cos(p)),0,R*np.sin(p)) for p in ph],ph)[0]
def geom_tilt(th):
    return scaffold(straightC,[th*k for k in range(N)])[0]
KAP=2*np.pi/(N*D)
E_s,pos_s=mean_energy(P0)
print(f"straight: <E_dance> = {E_s.mean():+.2f} MeV (sample sd {E_s.std():.2f})")
print()
print("mode curvatures from PAIRED differences (same schedule):")
res={}
for name,gen,xs in [("tilt-grad",geom_tilt,[0.02,0.04]),
                    ("bend",geom_bend,[0.01,0.02])]:
    vals=[]
    for x in xs:
        Ep,_=mean_energy(gen(x))
        dE=(Ep-E_s)                      # paired
        vals.append((2*dE.mean()/x**2, 2*dE.std()/np.sqrt(len(dE))/x**2))
    for x,(v,er) in zip(xs,vals):
        print(f"  {name:>9} x={x}: d2E/dx2 = {v:+9.0f} +- {er:.0f}")
    res[name]=vals[0][0]
Er,_=mean_energy(geom_bend(KAP)); dEr=(Er-E_s)
Er2,_=mean_energy(geom_bend(KAP*67/68)); dslope=(Er-Er2).mean()/(KAP/68)
print(f"  ring-straight: {dEr.mean():+.2f} +- {dEr.std()/np.sqrt(len(dEr)):.2f} MeV ; "
      f"end-slope {dslope:+.0f}")
print()
print("[reference: coherent-cycle site statics gave ring -29..-55, bend -432..-11293,")
print(" tilt-grad lock-contingent -16560..+69159; the dance ANSWERS the lock question.]")
#!/usr/bin/env python3
"""Sensitivity of the v3 dance results to (a) close-approach regularization (hard floor
vs soft-core; the physical scale = ZBW superposition saturation, a founder input),
(b) partner set (7 emergent vs founder's 5+1: far axial diagonals excluded)."""
import numpy as np
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
d=1.15; A_Q=d; D=d; N=16
r_q=A_Q/np.sqrt(2); R_E=1.6*r_q
def scaffold(centers,angles):
    S=[]
    for k in range(N):
        cx,cy,cz=centers[k]; th=angles[k]; c,s=np.cos(th),np.sin(th); par=(-1)**k
        h=A_Q/2
        q=[(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)]
        for (x,y,sg) in q: S.append(((cx+x*c,cy+y,cz-x*s),sg*par,'q',k))
        for (x,y,sg) in q:
            n=np.hypot(x,y); X,Y=R_E*x/n,R_E*y/n
            S.append(((cx+X*c,cy+Y,cz-X*s),-sg*par,'e',k))
    P=np.array([s[0] for s in S]); C=np.array([float(s[1]) for s in S])
    return P,C,[s[2] for s in S],np.array([s[3] for s in S])
straightC=[(0,0,k*D) for k in range(N)]
P0,C0,SP,PL=scaffold(straightC,[0.0]*N); NS=len(P0)
W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP])
def build_reach(qmax):
    reach=[]
    for i in range(NS):
        dd=P0-P0[i]; r=np.sqrt((dd*dd).sum(axis=1)); r[i]=np.inf
        if SP[i]=='q':
            cand=[j for j in range(NS) if C0[j]*C0[i]<0 and ((SP[j]=='q' and r[j]<qmax) or (SP[j]=='e' and r[j]<0.6))]
        else:
            cand=[j for j in range(NS) if C0[j]*C0[i]<0 and ((SP[j]=='e' and r[j]<2.6) or (SP[j]=='q' and r[j]<0.6))]
        reach.append(cand)
    return reach
def make_schedule(reach,vc,TC,seed):
    rr=np.random.default_rng(seed)
    tauC=2*np.pi*AHC/264.0; Ttot=TC*tauC
    att0=[np.array([W[i]*W[j]/np.linalg.norm(P0[i]-P0[j])**2 for j in reach[i]]) for i in range(NS)]
    tnow=np.zeros(NS); lastp=-np.ones(NS,int); resv=np.zeros(NS); legs=[]
    while True:
        i=int(np.argmin(tnow))
        if tnow[i]>=Ttot: break
        t=tnow[i]
        cand=[k for k,j in enumerate(reach[i]) if j!=lastp[i] and resv[j]<=t]
        if not cand: cand=[k for k,j in enumerate(reach[i]) if resv[j]<=t]
        if not cand: tnow[i]=t+0.05; continue
        w=att0[i][cand]; k=cand[rr.choice(len(cand),p=w/w.sum())]
        j=reach[i][k]; tau=np.linalg.norm(P0[i]-P0[j])/vc
        legs.append((i,j,t,tau)); resv[j]=t+tau; lastp[i]=j; tnow[i]=t+2*tau
    return legs,Ttot
def positions(P,legs,Ttot,nsamp=900):
    ts=np.linspace(0.02*Ttot,0.999*Ttot,nsamp)
    pos=np.tile(P[None,:,:],(nsamp,1,1)).astype(float)
    bycp=[[] for _ in range(NS)]
    for (i,j,t,tau) in legs: bycp[i].append((t,tau,j))
    for i in range(NS):
        for (t,tau,j) in bycp[i]:
            m=(ts>=t)&(ts<t+2*tau)
            if not m.any(): continue
            f=(ts[m]-t)/tau; f=np.where(f<=1,f,2-f)
            pos[m,i]=P[i][None,:]*(1-f[:,None])+P[j][None,:]*f[:,None]
    return pos
def energy(pos,reg,a):
    qw=(W*C0); E=np.zeros(len(pos))
    for s in range(len(pos)):
        dd=pos[s][:,None,:]-pos[s][None,:,:]
        r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
        if reg=='floor': r=np.maximum(np.sqrt(r2),a)
        else: r=np.sqrt(r2+a*a)          # soft-core (superposition saturation)
        E[s]=0.5*np.sum(np.outer(qw,qw)/r)*AHC
    return E
def geom_bend(kap):
    if abs(kap)<1e-12: return P0
    R=1/kap; ph=[k*D/R for k in range(N)]
    return scaffold([(R*(1-np.cos(p)),0,R*np.sin(p)) for p in ph],ph)[0]
def geom_tilt(th): return scaffold(straightC,[th*k for k in range(N)])[0]
KAP=2*np.pi/(N*D); vc=1.0; TC=100
print(f"{'partners':>8} {'reg':>6} {'a[fm]':>6} {'tilt-grad(0.04)':>16} {'ring-straight':>14} {'E0':>9}")
for qmax,label in [(2.1,'7'),(1.3,'5')]:
    reach=build_reach(qmax)
    legs,Ttot=make_schedule(reach,vc,TC,seed=42)
    pos_s=positions(P0,legs,Ttot); pos_t=positions(geom_tilt(0.04),legs,Ttot)
    pos_r=positions(geom_bend(KAP),legs,Ttot)
    for reg,a in [('floor',0.05),('floor',0.15),('soft',0.15),('soft',0.30)]:
        Es=energy(pos_s,reg,a); Et=energy(pos_t,reg,a); Er=energy(pos_r,reg,a)
        st=2*(Et-Es).mean()/0.04**2; ste=2*(Et-Es).std()/np.sqrt(len(Es))/0.04**2
        rg=(Er-Es).mean(); rge=(Er-Es).std()/np.sqrt(len(Es))
        print(f"{label:>8} {reg:>6} {a:>6.2f} {st:>+11.0f}+-{ste:<4.0f} {rg:>+9.1f}+-{rge:<4.1f} {Es.mean():>+9.0f}")
#!/usr/bin/env python3
"""THE make-or-break under the founder's dance: stability of the CLOSED N=16 ring
against its own deformation modes. Schedule generated ON the ring (closure-interface
partners included); paired replay across deformations. Modes: uniform tilt (m=0),
tilt wave m=1, m=2 (the ring analog of the gradient tilt), ellipticity, breathing.
Sensitivity bracket: (partners, regularization) in {(7,soft0.15),(5,soft0.15),(7,floor0.05)}."""
import numpy as np
AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
d=1.15; A_Q=d; D=d; N=16
r_q=A_Q/np.sqrt(2); R_E=1.6*r_q; KAP=2*np.pi/(N*D); R0=1/KAP
def ring_scaffold(tilt=None,ell=0.0,scale=1.0):
    """plane k at angle phi_k=2pi k/16 on radius R0*scale*(1+ell*cos 2phi);
       plane normal = tangent; extra tilt_k about global y."""
    S=[]
    for k in range(N):
        phi=2*np.pi*k/N
        R=R0*scale*(1+ell*np.cos(2*phi))
        cx,cz=R*(1-np.cos(phi))+ (R0-R)*0 ,R*np.sin(phi)
        # keep center on the (possibly elliptic) curve about the same circle origin:
        cx=R0*scale*(1+ell*np.cos(2*phi)); cxx=cx*(1-np.cos(phi)); cz=cx*np.sin(phi); cx=cxx
        th=phi+(tilt[k] if tilt is not None else 0.0)
        c,s=np.cos(th),np.sin(th); par=(-1)**k
        h=A_Q/2
        q=[(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)]
        for (x,y,sg) in q: S.append(((cx+x*c,y,cz-x*s),sg*par,'q'))
        for (x,y,sg) in q:
            n=np.hypot(x,y); X,Y=R_E*x/n,R_E*y/n
            S.append(((cx+X*c,Y,cz-X*s),-sg*par,'e'))
    P=np.array([s[0] for s in S]); C=np.array([float(s[1]) for s in S])
    return P,C,[s[2] for s in S]
P0,C0,SP=ring_scaffold(); NS=len(P0)
W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP])
def build_reach(qmax):
    reach=[]
    for i in range(NS):
        dd=P0-P0[i]; r=np.sqrt((dd*dd).sum(axis=1)); r[i]=np.inf
        if SP[i]=='q':
            cand=[j for j in range(NS) if C0[j]*C0[i]<0 and ((SP[j]=='q' and r[j]<qmax) or (SP[j]=='e' and r[j]<0.6))]
        else:
            cand=[j for j in range(NS) if C0[j]*C0[i]<0 and ((SP[j]=='e' and r[j]<2.6) or (SP[j]=='q' and r[j]<0.6))]
        reach.append(cand)
    return reach
def schedule(reach,vc,TC,seed):
    rr=np.random.default_rng(seed)
    tauC=2*np.pi*AHC/264.0; Ttot=TC*tauC
    att=[np.array([W[i]*W[j]/np.linalg.norm(P0[i]-P0[j])**2 for j in reach[i]]) for i in range(NS)]
    tn=np.zeros(NS); lp=-np.ones(NS,int); rv=np.zeros(NS); legs=[]
    while True:
        i=int(np.argmin(tn))
        if tn[i]>=Ttot: break
        t=tn[i]
        cand=[k for k,j in enumerate(reach[i]) if j!=lp[i] and rv[j]<=t]
        if not cand: cand=[k for k,j in enumerate(reach[i]) if rv[j]<=t]
        if not cand: tn[i]=t+0.05; continue
        w=att[i][cand]; k=cand[rr.choice(len(cand),p=w/w.sum())]
        j=reach[i][k]; tau=np.linalg.norm(P0[i]-P0[j])/vc
        legs.append((i,j,t,tau)); rv[j]=t+tau; lp[i]=j; tn[i]=t+2*tau
    return legs,Ttot
def positions(P,legs,Ttot,nsamp=800):
    ts=np.linspace(0.02*Ttot,0.999*Ttot,nsamp)
    pos=np.tile(P[None,:,:],(nsamp,1,1)).astype(float)
    bycp=[[] for _ in range(NS)]
    for (i,j,t,tau) in legs: bycp[i].append((t,tau,j))
    for i in range(NS):
        for (t,tau,j) in bycp[i]:
            m=(ts>=t)&(ts<t+2*tau)
            if not m.any(): continue
            f=(ts[m]-t)/tau; f=np.where(f<=1,f,2-f)
            pos[m,i]=P[i][None,:]*(1-f[:,None])+P[j][None,:]*f[:,None]
    return pos
def energy(pos,reg,a):
    qw=(W*C0); E=np.zeros(len(pos))
    for s in range(len(pos)):
        dd=pos[s][:,None,:]-pos[s][None,:,:]
        r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
        r=np.maximum(np.sqrt(r2),a) if reg=='floor' else np.sqrt(r2+a*a)
        E[s]=0.5*np.sum(np.outer(qw,qw)/r)*AHC
    return E
vc=1.0; TC=90
modes={
 'tilt m=0 (0.04)': dict(tilt=[0.04]*N),
 'tilt m=1 (0.04)': dict(tilt=[0.04*np.cos(2*np.pi*k/N) for k in range(N)]),
 'tilt m=2 (0.04)': dict(tilt=[0.04*np.cos(4*np.pi*k/N) for k in range(N)]),
 'ellipt (0.02)':   dict(ell=0.02),
 'breathe (+0.02)': dict(scale=1.02),
 'breathe (-0.02)': dict(scale=0.98),
}
amps={'tilt m=0 (0.04)':0.04,'tilt m=1 (0.04)':0.04,'tilt m=2 (0.04)':0.04,
      'ellipt (0.02)':0.02,'breathe (+0.02)':0.02,'breathe (-0.02)':-0.02}
for qmax,label,reg,a in [(2.1,'7','soft',0.15),(1.3,'5','soft',0.15),(2.1,'7','floor',0.05)]:
    reach=build_reach(qmax)
    legs,Ttot=schedule(reach,vc,TC,seed=42)
    pos0=positions(P0,legs,Ttot); E0=energy(pos0,reg,a)
    print(f"[partners={label}, {reg} a={a}] ring <E>={E0.mean():+.0f} MeV")
    for name,kw in modes.items():
        P,_,_=ring_scaffold(**kw)
        Ep=energy(positions(P,legs,Ttot),reg,a)
        x=amps[name]; dE=(Ep-E0)
        cur=2*dE.mean()/x**2; er=2*dE.std()/np.sqrt(len(dE))/x**2
        print(f"   {name:<17} d2E/dx2 = {cur:+9.0f} +- {er:<7.0f} {'STABLE' if cur>0 else 'UNSTABLE'}")
    print()
