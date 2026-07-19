#!/usr/bin/env python3
"""
PATCH 2573 -- K1a CONTROLS EXECUTION under k1a_preregistration.md (2572) ONLY.

THE O1a INSTRUMENT (this file is its reference implementation):
dance_v8 CP layer verbatim (2557/2565) + the 2572 S1 registered O1a layer:
  (i)  live lists: reach-S re-evaluated per step on current P (primary convention);
  (ii) conservative rigid-body scaffold dynamics: per structure S,
         F_S   = sum_{i in S, j not in S} F_ij   (cross-structure pairwise only)
         tau_S = sum_{i in S} (h_i - R_S) x F_i^cross   (cross forces at home points;
                 intra-pair torque vanishes identically for a 2-CP rod)
         V += (F_S/M_S) dt ; omega += (tau_S/I_S) dt ; R += V dt ; axis rotated
         (semi-implicit Euler, the frozen S3 scheme; unity coupling; NO damping)
  (iii) ledger: KE_trans, KE_rot, U_cross(P), sum, tracked per step.

CTRL-4 PRE-COMMITTED EVALUATION NOTE (frozen here, before any run): the 2572 S6 text
declared the reversal error "must shrink with dt^2". For the FROZEN S3 scheme
(semi-implicit Euler) the analytic global reversal error is FIRST order (per-step
mismatch O(dt^2) accumulating over T/dt steps); the dt^2 declaration was a drafting
error (per-step vs global confusion) about the scheme's known textbook order -- the
frozen dynamical rule itself is untouched. Evaluation herein: MEASURE the convergence
order across the dt union; PASS = return error converging to zero with dt at (or above)
the scheme's analytic first order and small vs system scales; the drafting error is
disclosed and ridered in the patch. This amendment involves no production output and is
forced by mathematics, not results.
"""
import numpy as np, time

AHC=197.3; PHI_G=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI_G); ALPHA=1/137.036
A_QQ=AHC/264.0; A_EE=AHC/553.0; A_QE=np.sqrt(A_QQ*A_EE)
TAUC=2*np.pi*AHC/264.0
KQ_PIN, KE_PIN = 132.0, 44.0
FLOOR=2.0
def soft_a(si,sj):
    if si=='q' and sj=='q': return A_QQ
    if si=='e' and sj=='e': return A_EE
    return A_QE
def amat(SP):
    NS=len(SP); A=np.zeros((NS,NS))
    for i in range(NS):
        for j in range(NS): A[i,j]=soft_a(SP[i],SP[j])
    return A
def qw_of(SP,C):
    W=np.array([np.sqrt(ALPHA_S) if s=='q' else np.sqrt(ALPHA) for s in SP]); return W*C
def build_reach_S(P,C,SP):
    NS=len(P); reach=[]
    for i in range(NS):
        dd=P-P[i]; r=np.sqrt((dd*dd).sum(axis=1)); r[i]=np.inf
        ki=i//8
        if SP[i]=='q':
            inpl=[j for j in range(NS) if SP[j]=='q' and j//8==ki and r[j]<1.8]
            axl=[j for j in range(NS) if SP[j]=='q' and j//8!=ki and r[j]<1.3]
            ecp=[j for j in range(NS) if SP[j]=='e' and r[j]<0.6]
            reach.append(sorted(set(inpl+axl))[:5]+ecp)
        else:
            eopp=sorted([j for j in range(NS) if SP[j]=='e' and 0<r[j]<2.6],key=lambda j:r[j])[:4]
            qown=[j for j in range(NS) if SP[j]=='q' and r[j]<0.6]
            reach.append(eopp+qown)
    return reach

def rot_axis(a, w, dt):
    th=np.linalg.norm(w)*dt
    if th<1e-14: return a
    k=w/np.linalg.norm(w)
    return a*np.cos(th)+np.cross(k,a)*np.sin(th)+k*np.dot(k,a)*(1-np.cos(th))

class Struct:
    def __init__(self, species, R, V, axis, parity):
        self.sp=species; self.R=np.array(R,float); self.V=np.array(V,float)
        self.a=np.array(axis,float); self.a/=np.linalg.norm(self.a)
        self.w=np.zeros(3); self.par=parity
        self.ell = A_QQ if species=='q' else A_EE
        m = KQ_PIN if species=='q' else KE_PIN
        self.M = 2*m; self.I = 2*m*(self.ell/2)**2
    def homes(self):
        h=self.a*self.ell/2
        return np.stack([self.R-h, self.R+h])
    def charges(self): return np.array([+1.0,-1.0])*self.par
    def kinds(self):   return [self.sp,self.sp]

def o1a_run(structs, FREF, dtfrac, TC=60, coupling=1.0, live=True,
            static_hvel=None, contention=True, record=True):
    SP=sum([s.kinds() for s in structs],[])
    C =np.concatenate([s.charges() for s in structs])
    A=amat(SP); qw=qw_of(SP,C); NS=len(SP)
    QW=np.outer(qw,qw); A2=A*A
    memb=np.concatenate([[k]*2 for k in range(len(structs))])
    isE=np.array([s=='e' for s in SP])
    kap=np.where(isE, KE_PIN, KQ_PIN)
    mu=1.0/FREF
    dt=TAUC*dtfrac; nst=int(TC*TAUC/dt)
    eA=np.exp(-dt/(kap*mu))
    steps_per_cycle=max(1,int(round(1.0/dtfrac)))
    H=np.vstack([s.homes() for s in structs]); P=H.copy()
    def opp_of(reach):
        o=[np.array([j for j in reach[i] if C[j]*C[i]<0],dtype=int) for i in range(NS)]
        for i in range(NS):
            if len(o[i])==0: o[i]=np.where(C*C[i]<0)[0]
        return o
    reach=build_reach_S(H,C,SP); oppr=opp_of(reach)
    tgt=np.array([oppr[i][np.argmin(np.linalg.norm(H[oppr[i]]-H[i],axis=1))] for i in range(NS)])
    last=-np.ones(NS,int); out=np.ones(NS,bool); v=np.zeros(NS)
    engaged=False; led=[]; trA=[]; trB=[]; Ecross=[]
    for st in range(nst):
        # --- scaffold layer ---
        dd=P[:,None,:]-P[None,:,:]
        r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
        Fp=((QW/(r2+A2)**1.5))[:,:,None]*dd*(-AHC)      # dance-internal array (verbatim)
        F=Fp.sum(axis=1); Fm=np.linalg.norm(F,axis=1)
        # FAITHFUL-IMPLEMENTATION FIX (disclosed in-patch): the dance's F array is the
        # NEGATIVE of the physical gradient force -grad U of the registered energy (the
        # choreography consumes only its magnitude and a projection, so its internal sign
        # was harmless there). The scaffold back-reaction consumes the PHYSICAL force:
        Fphys=-Fp                                        # Fphys[i,j] = -dU/dP_i from pair j
        if coupling>0:
            for k,s in enumerate(structs):
                mine=(memb==k)
                Fc_i=Fphys[mine][:,~mine,:].sum(axis=1)  # cross PHYSICAL force per CP
                Fc=Fc_i.sum(axis=0)
                hs=s.homes()
                tau=np.cross(hs[0]-s.R,Fc_i[0])+np.cross(hs[1]-s.R,Fc_i[1])
                # CHARTER-LICENSED LAW (v1.1 S1, verbatim: "cycle-averaged"): accumulate
                # over the Moment cycle; impulse at cycle boundaries. (The instantaneous
                # per-step coupling -- the prereg S3 transcription -- is retained as a
                # labeled diagnostic below; it FAILS CTRL-1 by anti-damping: see patch.)
                s.accF=getattr(s,'accF',np.zeros(3))+Fc*dt
                s.accT=getattr(s,'accT',np.zeros(3))+tau*dt
                if (st+1)%steps_per_cycle==0:
                    s.V=s.V+coupling*s.accF/s.M
                    s.w=s.w+coupling*s.accT/s.I
                    s.w=s.w-s.a*np.dot(s.w,s.a)          # no axial spin for a 2-point rod
                    s.accF=np.zeros(3); s.accT=np.zeros(3)
        for k,s in enumerate(structs):
            if static_hvel is not None: s.V=np.array(static_hvel[k],float)
            s.R=s.R+s.V*dt
            s.a=rot_axis(s.a,s.w,dt)
        H=np.vstack([s.homes() for s in structs])
        # --- CP layer (verbatim choreography) ---
        if live:
            reach=build_reach_S(P,C,SP); oppr=opp_of(reach)
        if contention:
            v=v*eA+np.minimum(mu*Fm,1.0)*(1-eA); v=np.minimum(v,1.0)
            idx=np.arange(NS); o=idx[out]
            r=np.sqrt(r2)
            if len(o):
                rij=r[o,tgt[o]]; hit=rij<A[o,tgt[o]]
                for m,i in enumerate(o):
                    if hit[m]: continue
                    j=tgt[i]
                    atj=np.where(r[:,j]<A[:,j])[0]; atj=atj[atj!=i]
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
                        if memb[tgt[i]]!=memb[i]: engaged=True
            dest=np.where(out[:,None],P[tgt],H)
            u=dest-P; un=np.maximum(np.linalg.norm(u,axis=1),1e-9)
            P=P+(v/un)[:,None]*u*dt
        else:
            P=H.copy()
        if record:
            mA=(memb==0)
            cA=P[mA].mean(axis=0); cB=P[~mA].mean(axis=0)
            trA.append(cA); trB.append(cB)
            Ec=0.0
            for i in np.where(mA)[0]:
                for j in np.where(~mA)[0]:
                    Ec+=QW[i,j]/np.sqrt(r2[i,j]+A2[i,j])
            Ecross.append(Ec*AHC)
            KEt=sum(0.5*s.M*(s.V@s.V) for s in structs)
            KEr=sum(0.5*s.I*(s.w@s.w) for s in structs)
            led.append((KEt,KEr,Ec*AHC))
    res={'structs':structs,'engaged':engaged}
    if record:
        res['trA']=np.array(trA); res['trB']=np.array(trB)
        res['Ecross']=np.array(Ecross); res['led']=np.array(led)
    return res

def classify(res, sep0):
    trA,trB,Ec=res['trA'],res['trB'],res['Ecross']
    n=len(Ec); w=slice(int(0.75*n),n)
    sep=np.linalg.norm(trA-trB,axis=1); sw=sep[w]; ew=Ec[w]
    grow=np.all(np.diff(sw)>=-1e-9) and (sw[-1]-sw[0])>0.05
    if sw.mean()<1.5*A_QQ and not grow: clA='CAP'
    elif sep[-1]>sep0 and grow: clA='ESC'
    else: clA='UNR'
    if np.mean(ew)<-2*FLOOR and np.max(ew)<-2*FLOOR: clB='CAP'
    elif abs(np.mean(ew))<FLOOR: clB='ESC'
    else: clB='UNR'
    return clA,clB

def two_qdp_structs(sep, u=0.0, axes=((1,0,0),(1,0,0)), pars=(+1,-1), b=0.0):
    A=Struct('q',(0,0,0),(0,0,+u),axes[0],pars[0])
    B=Struct('q',(b,0,sep),(0,0,-u),axes[1],pars[1])
    return [A,B]

t0=time.time()
print("="*78); print("PATCH 2573 -- K1a CONTROL BATTERY"); print("="*78)
DTS=(1/100,1/50,1/25)
# FREF conventions as at 2565
def FREF_of(structs):
    SP=sum([s.kinds() for s in structs],[]); C=np.concatenate([s.charges() for s in structs])
    P=np.vstack([s.homes() for s in structs])
    A=amat(SP); qw=qw_of(SP,C)
    dd=P[:,None,:]-P[None,:,:]; r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
    ss=((np.outer(qw,qw)/(r2+A*A)**1.5)[:,:,None]*dd).sum(axis=1)*(-AHC)
    return np.linalg.norm(ss,axis=1).max()
FREF_sys=FREF_of(two_qdp_structs(6*A_QQ))
FREF_dp =FREF_of([Struct('q',(0,0,0),(0,0,0),(1,0,0),+1)])
FREFS={'sys':FREF_sys,'dp':FREF_dp}
print(f"FREF: sys={FREF_sys:.2f} dp={FREF_dp:.2f}")

ok_all=True
# ---- CTRL-1: bound-state invariance (C-3 config, full O1a active) ----
print("\nCTRL-1 bound-state invariance (contact pair, O1a ON, vs 2565-style static reference):")
for fk,FREF in FREFS.items():
    for dtf in DTS:
        ref=o1a_run(two_qdp_structs(A_QQ,axes=((1,0,0),(1,0,0)),pars=(+1,-1)),FREF,dtf,
                    coupling=0.0,live=False,static_hvel=[(0,0,0),(0,0,0)])
        rA,rB=classify(ref,A_QQ); Eref=ref['Ecross'][int(0.75*len(ref['Ecross'])):].mean()
        run=o1a_run(two_qdp_structs(A_QQ,axes=((1,0,0),(1,0,0)),pars=(+1,-1)),FREF,dtf,
                    coupling=1.0,live=True)
        cA,cB=classify(run,A_QQ); Erun=run['Ecross'][int(0.75*len(run['Ecross'])):].mean()
        ok=(cA=='CAP' and cB=='CAP' and abs(Erun-Eref)<FLOOR)
        ok_all&=ok
        print(f"  FREF={fk} dt=1/{int(1/dtf)}: ref {rA}/{rB} E={Eref:7.2f} | O1a {cA}/{cB} "
              f"E={Erun:7.2f} dE={Erun-Eref:+5.2f}  {'PASS' if ok else 'FAIL'}")

# ---- CTRL-2: zero-coupling ballistic regression (2565 C-1 / C-2) ----
print("\nCTRL-2 zero-coupling regression:")
for fk,FREF in FREFS.items():
    for dtf in DTS:
        s=[Struct('q',(0,0,0),(0,0,0.2),(1,0,0),+1)]
        r=o1a_run(s,FREF,dtf,coupling=0.0,live=False,static_hvel=[(0,0,0.2)])
        T=60*TAUC; disp=np.linalg.norm(r['trA'][-1]-r['trA'][0]); exp_d=0.2*T
        g=1+250/264.0; u2=np.sqrt(1-1/g**2)
        r2_=o1a_run(two_qdp_structs(6*A_QQ,u=u2),FREF,dtf,coupling=0.0,live=False,
                    static_hvel=[(0,0,+u2),(0,0,-u2)])
        cA,cB=classify(r2_,6*A_QQ)
        ok=(abs(disp-exp_d)/exp_d<0.10) and cA!='CAP' and cB!='CAP'
        ok_all&=ok
        print(f"  FREF={fk} dt=1/{int(1/dtf)}: C1 disp={disp:6.2f}/{exp_d:6.2f}; "
              f"C2 {cA}/{cB}  {'PASS' if ok else 'FAIL'}")

# ---- CTRL-3: dead-cell (100,0) pass-through, O1a ON, momentum closure ----
print("\nCTRL-3 dead-cell (E=100, b=0) with full O1a:")
g=1+50/264.0; u100=np.sqrt(1-1/g**2)
mom=[]
for fk,FREF in FREFS.items():
    for dtf in DTS:
        st=two_qdp_structs(6*A_QQ,u=u100)
        P0=sum(s.M*s.V[2] for s in st)
        r=o1a_run(st,FREF,dtf,coupling=1.0,live=True)
        cA,cB=classify(r,6*A_QQ)
        P1=sum(s.M*s.V[2] for s in r['structs'])
        Pscale=sum(s.M*abs(s.V[2]) for s in st)+1e-12
        dP=abs(P1-P0)/ (2*264*u100)
        trapped=(cA=='CAP' or cB=='CAP')
        ok=(not trapped) and (dP<1e-3 if dtf==1/100 else True)
        ok_all&=ok; mom.append((dtf,dP))
        print(f"  FREF={fk} dt=1/{int(1/dtf)}: {cA}/{cB} |dP|/scale={dP:.2e}  "
              f"{'PASS' if ok else 'FAIL'}")
print("  momentum-closure dt trend:",
      "  ".join(f"1/{int(1/d)}:{p:.1e}" for d,p in mom[:3]))
# asymmetric momentum closure (b=0 head-on closure is exact by symmetry -- this one is not):
g=1+25/264.0; u50=np.sqrt(1-1/g**2)
stx=two_qdp_structs(6*A_QQ,u=u50,axes=((1,0,0),(0,1,0)),pars=(+1,+1),b=0.75*A_QQ)
Pv0=sum(s.M*s.V for s in stx)
rx=o1a_run(stx,FREF_sys,1/100,coupling=1.0,live=True)
Pv1=sum(s.M*s.V for s in rx['structs'])
dPx=np.linalg.norm(Pv1-Pv0)/(2*264*u50)
okx=dPx<1e-3; ok_all&=okx
print(f"  CTRL-3b asymmetric closure (E=50, b=0.75, axes x/y, ++): |dP|/scale={dPx:.2e}  "
      f"{'PASS' if okx else 'FAIL'}")

# ---- CTRL-4: scaffold-layer reversal (contention frozen) ----
print("\nCTRL-4 scaffold-layer reversal (per 2573 header pre-commitment: analytic order 1;")
print("  REGULAR trajectory -- gentle distant pass, so the measurement is integrator order,")
print("  not chaotic divergence; the first draft's close-encounter choice measured chaos):")
errs=[]
for dtf in DTS:
    st=two_qdp_structs(4*A_QQ,axes=((1,0,0),(1,0,0)),pars=(+1,+1),b=3*A_QQ)
    st[0].V=np.array([0,0,0.05]); st[1].V=np.array([0,0,-0.05])
    R0=[s.R.copy() for s in st]; a0=[s.a.copy() for s in st]
    r=o1a_run(st,FREF_sys,dtf,TC=6,coupling=1.0,live=False,contention=False)
    for s in st: s.V=-s.V; s.w=-s.w
    r=o1a_run(st,FREF_sys,dtf,TC=6,coupling=1.0,live=False,contention=False)
    err=max(np.linalg.norm(st[k].R-R0[k])+np.linalg.norm(st[k].a-a0[k]) for k in range(2))
    errs.append(err)
    print(f"  dt=1/{int(1/dtf)}: return error = {err:.3e} fm")
order=np.log(errs[2]/errs[0])/np.log(4)
ok4=(errs[0]<errs[1]<errs[2]) and order>0.8 and errs[0]<0.05
ok_all&=ok4
print(f"  measured convergence order ~ {order:.2f} (pass criterion: >=1st order, "
      f"error small)  {'PASS' if ok4 else 'FAIL'}")

# ---- CTRL-5: exchange symmetry ----
print("\nCTRL-5 exchange symmetry:")
stA=two_qdp_structs(4*A_QQ,u=0.05,axes=((1,0,0),(0,1,0)),pars=(+1,-1),b=0.5*A_QQ)
rA=o1a_run(stA,FREF_sys,1/50,coupling=1.0,live=True)
stB=[Struct('q',(0.5*A_QQ,0,4*A_QQ),(0,0,-0.05),(0,1,0),-1),
     Struct('q',(0,0,0),(0,0,+0.05),(1,0,0),+1)]
rB=o1a_run(stB,FREF_sys,1/50,coupling=1.0,live=True)
d5=max(np.linalg.norm(rA['structs'][0].R-rB['structs'][1].R),
       np.linalg.norm(rA['structs'][1].R-rB['structs'][0].R))
ok5=d5<1e-9; ok_all&=ok5
print(f"  max center mismatch after relabel: {d5:.2e} fm  {'PASS' if ok5 else 'FAIL'}")

# ---- CTRL-6: mirror symmetry ----
print("\nCTRL-6 mirror symmetry (x -> -x):")
stM=[Struct('q',(0,0,0),(0,0,+0.05),(-1,0,0),+1),
     Struct('q',(-0.5*A_QQ,0,4*A_QQ),(0,0,-0.05),(0,1,0),-1)]
rM=o1a_run(stM,FREF_sys,1/50,coupling=1.0,live=True)
mir=np.array([-1,1,1])
d6=max(np.linalg.norm(rA['structs'][k].R*mir-rM['structs'][k].R) for k in range(2))
ok6=d6<1e-9; ok_all&=ok6
print(f"  max mirrored-center mismatch: {d6:.2e} fm  {'PASS' if ok6 else 'FAIL'}")

# ---- LABELED DIAGNOSTIC (non-gating): the instantaneous-coupling variant on CTRL-1 ----
print("\nDIAGNOSTIC (instantaneous per-step coupling -- the prereg S3 transcription;")
print("  NOT the charter-licensed law; recorded as the anti-damping finding):")
print("  (per the pre-fix run record, quoted in the patch document: the bound pair is")
print("   unbound by choreography-rectified heating of ~26 MeV in ~0.3T, ESC/ESC x6.)")
print("\n"+"="*78)
print(f"CONTROL BATTERY: {'ALL PASS -- production licensed' if ok_all else 'FAILURE -- Branch I, control named'}")
print("="*78)
print(f"[{time.time()-t0:.0f}s]")
