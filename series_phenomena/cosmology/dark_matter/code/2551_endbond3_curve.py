#!/usr/bin/env python3
"""
PATCH 2551 -- OPEN-DM-ENDBOND-3 R-A EXECUTED under endbond3_preregistration.md ONLY.

<E>(kappa) at dance_v8 strength on the 2450 corrected bend family (arc convention),
N=16 planes, grid kappa/kappa_ring in {0, 1/5, 2/5, 3/5, 4/5, 15/16, 1}.
Union: dt {tauC/100, tauC/50, tauC/25} x FREF {grid-global, registered 16-plane pair}.
Knob-free: kappa* = grid argmax per (FREF,dt) cell; readings per prereg S1/S5.
Blindness: the full union table and the frozen E_close band print BEFORE the gates
section; fenced numbers appear nowhere above the freeze.
dance_v8 and 2461 defs VERBATIM (as in code/2549_endbond2_dance.py, from 2510/2461).
"""
import numpy as np, time

AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
d=1.15; A_Q=d; D=d
r_q=A_Q/np.sqrt(2); R_E=1.6*r_q
A_QQ=AHC/264.0; A_EE=AHC/553.0; A_QE=np.sqrt(A_QQ*A_EE)
TAUC=2*np.pi*AHC/264.0
KQ_PIN, KE_PIN = 132.0, 44.0
N=16; KAP_RING=2*np.pi/(N*D)

# ---- the 2450 corrected bend family (arc convention), 2455-coded plane ----
def bend_scaffold(kap):
    S=[]
    h=A_Q/2
    q=[(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)]
    for k in range(N):
        if abs(kap)<1e-12:
            cx,cz,phi=0.0,k*D,0.0
        else:
            R=1.0/kap; phi=k*D/R; cx=R*(1-np.cos(phi)); cz=R*np.sin(phi)
        c,s=np.cos(phi),np.sin(phi); par=(-1)**k
        for (x,y,sg) in q: S.append(((cx+x*c,y,cz-x*s),sg*par,'q'))
        for (x,y,sg) in q:
            n=np.hypot(x,y); X,Y=R_E*x/n,R_E*y/n
            S.append(((cx+X*c,Y,cz-X*s),-sg*par,'e'))
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
    qw=W*C
    dd=P[:,None,:]-P[None,:,:]; r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
    A=amat(SP); F=((np.outer(qw,qw)/(r2+A*A)**1.5)[:,:,None]*dd).sum(axis=1)*(-AHC)
    return F
def qw_of(SP,C):
    W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP]); return W*C

# ---- dance_v8, VERBATIM from 2510 ----
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
print("PATCH 2551 -- OPEN-DM-ENDBOND-3 R-A: <E>(kappa) at dance strength (prereg 2550)")
print("="*78)

FRACS=[0.0, 1/5, 2/5, 3/5, 4/5, 15/16, 1.0]
scaffs=[bend_scaffold(f*KAP_RING) for f in FRACS]

# closure sanity: kappa_ring scaffold's seam pitch equals the internal pitch
Pring=scaffs[-1][0]
seam=np.linalg.norm(Pring[0:8].mean(axis=0)-Pring[8*(N-1):8*N].mean(axis=0))
print(f"closure sanity: seam center-to-center = {seam:.4f} fm (internal pitch D = {D})")
assert abs(seam-D)<0.02

FREF_grid=max(np.linalg.norm(ssv_vectors(P,C,SP),axis=1).max() for (P,C,SP) in scaffs)
FREF_16  =max(np.linalg.norm(ssv_vectors(*scaffs[-1]),axis=1).max(),
              np.linalg.norm(ssv_vectors(*scaffs[0]),axis=1).max())
print(f"FREF_grid = {FREF_grid:.2f} ; FREF_16(ring/straight) = {FREF_16:.2f}")
print()

results={}
for tag,FREF in (("grid",FREF_grid),("16pl",FREF_16)):
    for dtf in (1/100,1/50,1/25):
        curve=[]
        for (P,C,SP),f in zip(scaffs,FRACS):
            Es,Ks,_,_=dance_v8(P,C,SP,FREF,dtf)
            curve.append((f,Es.mean(),Ks.mean()))
        results[(tag,int(1/dtf))]=curve
        cs=" ".join(f"{ep:+9.1f}" for (_,ep,_) in curve)
        print(f"[FREF={tag:4s} dt=1/{int(1/dtf):>3}] <Ep>(k/kring 0,1/5,2/5,3/5,4/5,15/16,1): {cs}"
              f"  ({time.time()-t0:.0f}s)")
print()

# ---- knob-free extraction per cell, then the frozen unions ----
rows=[]
for key,curve in results.items():
    eps=[ep for (_,ep,_) in curve]
    istar=int(np.argmax(eps)); fstar=FRACS[istar]
    if istar==0:
        Eclose=eps[0]-eps[-1]; Ebar=0.0; kind="barrier-free"
    elif istar==len(FRACS)-1:
        Eclose=float('nan'); Ebar=float('nan'); kind="ADVERSE (max at ring)"
    else:
        Eclose=eps[istar]-eps[-1]; Ebar=eps[istar]-eps[0]; kind=f"interior k*={fstar:.3f}"
    rs=eps[-1]-eps[0]
    rows.append((key,kind,fstar,Eclose,Ebar,rs))
    print(f"  {key}: {kind:22s} E_close={Eclose:+8.1f}  E_barrier={Ebar:+7.1f}  r-s={rs:+8.1f}")
ecl=[r[3] for r in rows if not np.isnan(r[3])]
kstars=set(r[2] for r in rows)
lo,hi=(min(ecl),max(ecl)) if ecl else (float('nan'),float('nan'))
print()
print("="*78)
print(f"FROZEN: E_close union band = [{lo:+.1f}, {hi:+.1f}] MeV (interface total; positive = closure pays)")
print(f"FROZEN: kappa* dt/FREF-stability: distinct kappa* values across cells = {sorted(kstars)}")
spans_zero=(len(ecl)<len(rows)) or (lo<0<hi) or lo==0 or hi==0
print(f"frozen consequence: any-adverse-or-nan={len(ecl)<len(rows)}; spans_zero={lo<0<hi}")
print("="*78)
print()

# ---- GATES (prereg S4; only now) ----
print("GATES (S4, fixed order; against the frozen band):")
if len(ecl)<len(rows) or lo<0<hi or lo==0 or hi==0:
    print("  Branch I / adverse handling per S5 -- gates not licensed on a non-depth.")
else:
    g1_in=(lo>=40.0) and (hi<=170.0); g1_ovl=(hi>=40.0) and (lo<=170.0)
    print(f"  G1 ([40,170] membership): band [{lo:.1f},{hi:.1f}] -> "
          f"{'PASS (fully inside)' if g1_in else ('PARTIAL OVERLAP' if g1_ovl else 'FAIL')}")
    mid=0.5*(lo+hi)
    print(f"  G2 (102 lock): inside band: {'YES' if lo<=102.0<=hi else 'NO'}; "
          f"midpoint offset {mid-102.0:+.1f} MeV")
    kstable=len(kstars)==1
    print(f"  kappa* stability (win-class requirement): {'STABLE' if kstable else 'NOT STABLE'} "
          f"({sorted(kstars)})")
print()
print("internal-consistency sentences (no gate force):")
rs_vals=[r[5] for r in rows]
print(f"  (a) v8 ring-straight on this grid: [{min(rs_vals):+.1f}, {max(rs_vals):+.1f}] MeV "
      f"(registered 2510 family object; same functional family).")
print(f"  (b) echo family: barrier-free E_close = -(r-s) by construction where it occurs; "
      f"zero evidential weight (2550 S2.4).")
print()
print(f"runtime {time.time()-t0:.0f}s ; ALL ASSERTIONS PASS.")
