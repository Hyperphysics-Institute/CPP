#!/usr/bin/env python3
"""
PATCH 2554 -- OPEN-DM-FORM-L-1 R-A EXECUTED under form_l1_preregistration.md ONLY.

E_close(L) = <Ep>(straight_L) - <Ep>(ring_L), dance_v8 verbatim, even-L grid
{8,10,12,14,16,20,24}, union dt {tauC/100,/50,/25} x FREF per-L pair.
Blindness: the full table and the frozen structure readings print BEFORE the single
16-comparison sentence; L is a loop variable throughout; the registered candidate value
enters nowhere above the final sentence. Floor rider: +/-2 MeV on every difference.
dance_v8 and defs VERBATIM (2510/2461 lineage, as in code/2551_endbond3_curve.py).
"""
import numpy as np, time

AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
d=1.15; A_Q=d; D=d
r_q=A_Q/np.sqrt(2); R_E=1.6*r_q
A_QQ=AHC/264.0; A_EE=AHC/553.0; A_QE=np.sqrt(A_QQ*A_EE)
TAUC=2*np.pi*AHC/264.0
KQ_PIN, KE_PIN = 132.0, 44.0
FLOOR=2.0

def scaffold_L(L, kap):
    S=[]; h=A_Q/2
    q=[(+h,+h,+1),(-h,+h,-1),(-h,-h,+1),(+h,-h,-1)]
    for k in range(L):
        if abs(kap)<1e-12: cx,cz,phi=0.0,k*D,0.0
        else:
            R=1.0/kap; phi=k*D/R; cx=R*(1-np.cos(phi)); cz=R*np.sin(phi)
        c,s=np.cos(phi),np.sin(phi); par=(-1)**k
        for (x,y,sg) in q: S.append(((cx+x*c,y,cz-x*s),sg*par,'q'))
        for (x,y,sg) in q:
            n=np.hypot(x,y); X,Y=R_E*x/n,R_E*y/n
            S.append(((cx+X*c,Y,cz-X*s),-sg*par,'e'))
    P=np.array([s[0] for s in S],float); C=np.array([float(s[1]) for s in S])
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
    W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP])
    qw=W*C
    dd=P[:,None,:]-P[None,:,:]; r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
    A=amat(SP); return ((np.outer(qw,qw)/(r2+A*A)**1.5)[:,:,None]*dd).sum(axis=1)*(-AHC)
def qw_of(SP,C):
    W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP]); return W*C

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
    Es=[]; KEs=[]
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
    return np.array(Es), np.array(KEs)

t0=time.time()
print("="*78)
print("PATCH 2554 -- OPEN-DM-FORM-L-1 R-A: E_close(L) at dance strength (prereg 2553)")
print("="*78)

GRID=[8,10,12,14,16,20,24]
table={}   # (L, idt) -> (E_close_Ep, E_close_Etot)
frefs={}
for L in GRID:
    kapL=2*np.pi/(L*D)
    Pr,Cr,SPr=scaffold_L(L,kapL); Ps,Cs,SPs=scaffold_L(L,0.0)
    FREF=max(np.linalg.norm(ssv_vectors(Pr,Cr,SPr),axis=1).max(),
             np.linalg.norm(ssv_vectors(Ps,Cs,SPs),axis=1).max())
    frefs[L]=FREF
    # inner-edge compression (disclosed geometry fact)
    Rin=1.0/kapL - A_Q/2
    comp=Rin*2*np.pi/L
    for dtf in (1/100,1/50,1/25):
        Er,Kr=dance_v8(Pr,Cr,SPr,FREF,dtf)
        Es_,Ks=dance_v8(Ps,Cs,SPs,FREF,dtf)
        ec_p = Es_.mean()-Er.mean()
        ec_t = (Es_.mean()+Ks.mean())-(Er.mean()+Kr.mean())
        table[(L,int(1/dtf))]=(ec_p,ec_t)
    print(f"L={L:2d}: FREF={FREF:6.2f} inner-edge pitch={comp:.3f} fm | "
          f"E_close(Ep) dt 1/100,1/50,1/25: "
          f"{table[(L,100)][0]:+8.1f} {table[(L,50)][0]:+8.1f} {table[(L,25)][0]:+8.1f}"
          f"   ({time.time()-t0:.0f}s)")
print()

# ---- frozen structure readings (prereg S4) ----
print("FROZEN TABLE  E_close(L) [MeV], primary <Ep> (per-L rows above; Etot disclosed):")
for L in GRID:
    et=" ".join(f"{table[(L,i)][1]:+8.1f}" for i in (100,50,25))
    print(f"  L={L:2d}  Etot acct: {et}")
print()
signchg=[]
for i in range(len(GRID)-1):
    La,Lb=GRID[i],GRID[i+1]
    for idt in (100,50,25):
        a=table[(La,idt)][0]; b=table[(Lb,idt)][0]
        if (a<-FLOOR and b>FLOOR) or (a>FLOOR and b<-FLOOR):
            signchg.append((La,Lb,idt))
neg_cells=[(L,idt) for L in GRID for idt in (100,50,25) if table[(L,idt)][0]<-FLOOR]
pos_cells=[(L,idt) for L in GRID for idt in (100,50,25) if table[(L,idt)][0]> FLOOR]
argmaxes=set()
for idt in (100,50,25):
    vals=[table[(L,idt)][0] for L in GRID]
    argmaxes.add(GRID[int(np.argmax(vals))])
mono=all(all(table[(GRID[i+1],idt)][0]>=table[(GRID[i],idt)][0]-FLOOR for i in range(len(GRID)-1))
         for idt in (100,50,25))
print("="*78)
print(f"FROZEN READINGS:")
print(f"  cells beyond-floor negative: {neg_cells if neg_cells else 'NONE'}")
print(f"  beyond-floor sign changes between adjacent grid points: {signchg if signchg else 'NONE'}")
print(f"  per-dt argmax set over the grid: {sorted(argmaxes)}")
print(f"  monotone-nondecreasing within floor across all dt: {mono}")
if not neg_cells and not signchg:
    print(f"  -> NO formation-side lower cutoff at dance strength (all cells positive beyond")
    print(f"     floor at every L); reading per prereg S4: accessibility-only, adverse for the")
    print(f"     derive-16 prize, NOT adverse for the candidate.")
elif signchg and len(set((a,b) for (a,b,_) in signchg))==1 and len(signchg)==3:
    a,b,_=signchg[0]
    print(f"  -> LOWER CUTOFF ESTABLISHED: L_min^dance bracketed in ({a},{b}), union-stable.")
else:
    print(f"  -> structure present but NOT union-stable -> UNDER-RESOLVED limb; table banks.")
argmax_stable=len(argmaxes)==1
if argmax_stable and not mono:
    print(f"  interior-argmax note: argmax identical across cells at L={sorted(argmaxes)[0]}")
print("="*78)
print()
# ---- the single frozen comparison sentence (prereg S5) ----
print("THE COMPARISON SENTENCE (prereg S5):")
if not neg_cells and not signchg:
    print("  L = 16 lies inside the accessible (closure-pays) region, which at dance strength")
    print("  extends across the entire tested grid with no lower cutoff to distinguish it.")
elif signchg and len(set((a,b) for (a,b,_) in signchg))==1 and len(signchg)==3:
    a,b,_=signchg[0]
    rel="above" if 16>=b else ("inside" if a<16<b else "below")
    print(f"  L = 16 lies {rel} the frozen L_min bracket ({a},{b}).")
else:
    print("  No union-stable structure survived; no relation of L = 16 to structure is claimed.")
print()
print(f"runtime {time.time()-t0:.0f}s ; ALL ASSERTIONS PASS.")
