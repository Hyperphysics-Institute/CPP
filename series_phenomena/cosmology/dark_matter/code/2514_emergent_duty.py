#!/usr/bin/env python3
"""Emergent same-charge apposition duty (Patch 2514) -- in-run measurement of registry
condition 2 on DM-CANDIDATE-B. dance_v8 dynamics VERBATIM at pinned kappa (kscale=1.0,
G7); instrumentation is read-only pair counting per post-burn step -- the trajectory is
bit-identical to 2510/2513. Pre-registration: reasoning/2514.md SS1-3, fixed before run.

Primary: duty_qq at r < a_qq (qq contact scale), ring, dt=tauC/{100,50,25}; verdict vs
3/7 over all three dt. Secondary: radius x{0.5,2}, ee/qe duties, rod at dt=1/50,
occupancy. Thin-statistics guard: total qq apposed-pair count >= 1000 per dt.
Deterministic; no RNG."""
import numpy as np, time, os
_PD=os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(_PD,"2461_ssv_kinematics.py")).read().split("if __name__")[0])
_src=open(os.path.join(_PD,"2510_hardened_dance_inertia.py")).read().split("Pr,Cr,SPr=ring_scaffold()")[0]
exec("\n".join(l for l in _src.splitlines() if not l.startswith("exec(") and not l.startswith("import ")))

DELTA_STATIC=3.0/7.0

def dance_v8_duty(H,C,SP,FREF,dtfrac,kscale=1.0,TC=60,burn=0.15,radii=(0.5,1.0,2.0)):
    """dance_v8 verbatim + read-only apposition counters. Returns duty tables + checksum."""
    A=amat(SP); qw=qw_of(SP,C); NS=len(H)
    QW=np.outer(qw,qw); A2=A*A
    reach=build_reach(H,C,SP)
    oppr=[np.array([j for j in reach[i] if C[j]*C[i]<0],dtype=int) for i in range(NS)]
    for i in range(NS):
        if len(oppr[i])==0: oppr[i]=np.where(C*C[i]<0)[0]
    isE=np.array([s=='e' for s in SP]); isQ=~isE
    kap=np.where(isE, KE_PIN, KQ_PIN)*kscale
    mu=1.0/FREF
    dt=TAUC*dtfrac; nst=int(TC*TAUC/dt)
    eA=np.exp(-dt/(kap*mu)) if kscale>0 else np.zeros(NS)
    P=H.copy()
    tgt=np.array([oppr[i][np.argmin(np.linalg.norm(H[oppr[i]]-H[i],axis=1))] for i in range(NS)])
    last=-np.ones(NS,int); out=np.ones(NS,bool)
    v=np.zeros(NS)
    Es=[]
    # counters: [radius][pairclass qq/ee/qe][same/opp]
    cnt={rm:{pc:[0,0] for pc in ('qq','ee','qe')} for rm in radii}
    iu=np.triu_indices(NS,k=1)
    pq=isQ[iu[0]]&isQ[iu[1]]; pe=isE[iu[0]]&isE[iu[1]]; pm=~pq&~pe
    same=(C[iu[0]]*C[iu[1]])>0
    Aij=A[iu]
    for st in range(nst):
        dd=P[:,None,:]-P[None,:,:]
        r2=(dd*dd).sum(axis=2); np.fill_diagonal(r2,np.inf)
        r=np.sqrt(r2)
        F=(((QW/(r2+A2)**1.5))[:,:,None]*dd).sum(axis=1)*(-AHC)
        Fm=np.linalg.norm(F,axis=1)
        v=v*eA+np.minimum(mu*Fm,1.0)*(1-eA); v=np.minimum(v,1.0)
        idx=np.arange(NS)
        o=idx[out]
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
        dest=np.where(out[:,None],P[tgt],H)
        u=dest-P; un=np.maximum(np.linalg.norm(u,axis=1),1e-9)
        P=P+(v/un)[:,None]*u*dt
        if st>=int(burn*nst):
            Es.append(0.5*np.sum(QW/np.sqrt(r2+A2))*AHC)   # checksum vs 2510/2513
            rp=r[iu]
            for rm in radii:
                ap=rp<rm*A_QQ                        # NOTE: apposition threshold in units of a_qq
                for pc,msk in (('qq',pq),('ee',pe),('qe',pm)):
                    s=ap&msk
                    cnt[rm][pc][0]+=int((s&same).sum()); cnt[rm][pc][1]+=int((s&~same).sum())
    return cnt, np.array(Es), nst

if __name__=='__main__':
    t0=time.time()
    Pr,Cr,SPr=ring_scaffold(); Ps,Cs,SPs=straight_scaffold()
    Fr=ssv_vectors(Pr,Cr,SPr); Fs=ssv_vectors(Ps,Cs,SPs)
    FREF=max(np.linalg.norm(Fr,axis=1).max(),np.linalg.norm(Fs,axis=1).max())
    # home-scaffold sanity: no qq pair within a_qq at home (pre-registered premise)
    dd=Pr[:,None,:]-Pr[None,:,:]; r=np.sqrt((dd*dd).sum(axis=2)); np.fill_diagonal(r,np.inf)
    iq=[i for i,s in enumerate(SPr) if s=='q']
    print(f"home ring min qq distance = {r[np.ix_(iq,iq)].min():.3f} fm vs a_qq={A_QQ:.3f} (must exceed)")
    print(f"static combinatorial delta = 3/7 = {DELTA_STATIC:.4f}\n")
    verdicts=[]
    for dtf in (1/100,1/50,1/25):
        cnt,Es,nst=dance_v8_duty(Pr,Cr,SPr,FREF,dtf)
        line=f"RING dt=tauC/{int(1/dtf):>3}: <Ep>={Es.mean():+8.1f} (checksum)"
        for rm in (1.0,0.5,2.0):
            s,o=cnt[rm]['qq']; tot=s+o
            duty=s/tot if tot else float('nan')
            tag=' PRIMARY' if rm==1.0 else ''
            line+=f" | r<{rm}a_qq: duty_qq={duty:.4f} (n={tot}){tag}"
            if rm==1.0:
                nb=int((1-0.15)*nst)
                occ=tot/nb
                sE,oE=cnt[rm]['ee']; sM,oM=cnt[rm]['qe']
                sec=(f"    ee duty={sE/(sE+oE) if sE+oE else float('nan'):.4f} (n={sE+oE}); "
                     f"qe duty={sM/(sM+oM) if sM+oM else float('nan'):.4f} (n={sM+oM}); "
                     f"qq occupancy={occ:.2f} pairs/step")
                verdicts.append((duty,tot))
        print(line); print(sec); print(f"  ({time.time()-t0:.0f}s)")
    cnt,Es,_=dance_v8_duty(Ps,Cs,SPs,FREF,1/50)
    s,o=cnt[1.0]['qq']
    print(f"\nROD  dt=tauC/50 (secondary): duty_qq={s/(s+o) if s+o else float('nan'):.4f} (n={s+o}) <Ep>={Es.mean():+8.1f}")
    print("\n== pre-registered branch reading (reasoning/2514 SS3):")
    guard=[i for i,(d,n) in enumerate(verdicts) if n<1000]
    if guard: print(f"   thin-statistics guard fired at dt index {guard} -> BRANCH X: condition 2 NOT discharged")
    else:
        ge=[d>=DELTA_STATIC for d,_ in verdicts]
        if all(ge): print(f"   duty_qq >= 3/7 at all three dt -> BRANCH Y: condition 2 DISCHARGED (expected direction)")
        elif not any(ge): print(f"   duty_qq < 3/7 at all three dt -> BRANCH L: resolved-adverse-direction; disclosure queued")
        else: print(f"   dt-inconsistent -> BRANCH X: condition 2 NOT discharged")
    print(f"total {time.time()-t0:.0f}s")
