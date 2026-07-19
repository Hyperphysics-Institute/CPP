#!/usr/bin/env python3
"""
PATCH 2574 -- REACH-AUDIT-2 R-A under the 2567 S3 registration (audit-class; no physics
adjudication; founder-input-free per the 19 Jul session directive).

FROZEN READINGS (committed here, before any run):
 A) DEPENDENCY LEDGER: every DM-lane file defining/consuming a reach builder is listed
    with classifier version (old global-dz vs reach-S) and registry load it bears.
 B) TRUNCATION CENSUS (hunt item 6): the 'q' reach list is truncated as
    sorted(set(inpl+axl))[:5] -- sorted() on integer indices = INDEX order, not distance
    order. If |inpl+axl| <= 5 for every qCP on the load-bearing geometries (ring L=16,
    straight rod; both classifiers), the truncation NEVER BINDS -> invariant, item
    resolved. If it binds anywhere -> DEFECT flagged (arbitrary index-order selection),
    affected results listed, re-run obligation registered. The census also runs on the
    FORM-L geometries L in {8,12,20,22} (the wall's own scan range).
 C) DUTY RE-RUN (2514 primary, registry condition 2): dance_v8_duty re-invoked with
    build_reach overridden to reach-S (2557 verbatim); ring, dt = tauC/{100,50,25},
    primary duty_qq at r < a_qq. INVARIANCE VERDICT = the 2514 pre-registered BRANCH
    reading (Y/L/X) unchanged under reach-S across all three dt; numeric shifts
    disclosed at any size. Branch flip -> supersession rider queued per the 2557
    precedent + founder disclosure line. (2513 modes, 2549 ENDBOND-2, 2510 contention/
    pile statistics: enumerated in the ledger, queued to R-B -- runtime class exceeds
    this patch's box.)
"""
import numpy as np, time, os, sys
_D=os.path.dirname(os.path.abspath(__file__))
t0=time.time()
print("="*78); print("PATCH 2574 -- REACH-AUDIT-2 R-A"); print("="*78)

# ---- load the 2514 chain (2461 kinematics + 2510 engine + 2514 duty instrument) ----
sys.argv=[sys.argv[0]]
_g=dict(globals()); _g['__file__']=os.path.join(_D,"2514_emergent_duty.py")
head=open(_g["__file__"]).read().split("\nif __name__")[0]
exec(head, _g)                       # run the chain in a namespace with correct __file__
for _k in ("build_reach","ring_scaffold","straight_scaffold","ssv_vectors",
           "dance_v8_duty","DELTA_STATIC","A_QQ","D","A_Q","R_E"):
    globals()[_k]=_g[_k]
build_reach_OLD=build_reach

# ---- reach-S verbatim from 2557 ----
s57=open(os.path.join(_D,"2557_reregistration_reach_s.py")).read()
import re as _re
m=_re.search(r"def build_reach_S.*?return reach", s57, _re.S)
exec(compile(m.group(0),"reachS","exec"))

# ---- B) TRUNCATION CENSUS ----
print("\n[B] '[:5]' truncation census (does index-order truncation ever bind?):")
def census(P,C,SP,label):
    NS=len(P); worst=0; binds=[]
    for i in range(NS):
        if SP[i]!='q': continue
        dd=P-P[i]; r=np.sqrt((dd*dd).sum(axis=1)); r[i]=np.inf
        ki=i//8
        inpl=[j for j in range(NS) if SP[j]=='q' and j//8==ki and r[j]<1.8]
        axl=[j for j in range(NS) if SP[j]=='q' and j//8!=ki and r[j]<1.3]
        n=len(set(inpl+axl)); worst=max(worst,n)
        if n>5: binds.append((i,n))
    print(f"  {label:28s}: max |inpl+axl| = {worst}  "
          f"{'TRUNCATION BINDS at '+str(len(binds))+' qCPs -- DEFECT' if binds else 'never binds -- invariant'}")
    return binds
def census_old(P,C,SP,label):
    NS=len(P); worst=0; binds=[]
    for i in range(NS):
        if SP[i]!='q': continue
        dd=P-P[i]; r=np.sqrt((dd*dd).sum(axis=1)); r[i]=np.inf
        inpl=[j for j in range(NS) if SP[j]=='q' and abs(P[j][2]-P[i][2])<0.5*D and r[j]<1.8]
        axl=[j for j in range(NS) if SP[j]=='q' and not(abs(P[j][2]-P[i][2])<0.5*D) and r[j]<1.3]
        n=len(set(inpl+axl)); worst=max(worst,n)
        if n>5: binds.append((i,n))
    print(f"  {label:28s}: max = {worst}  {'BINDS -- DEFECT' if binds else 'never binds -- invariant'}")
    return binds
Pr,Cr,SPr=ring_scaffold(); Ps,Cs,SPs=straight_scaffold()
b1=census(Pr,Cr,SPr,"ring L=16 (reach-S rule)")
b2=census(Ps,Cs,SPs,"straight   (reach-S rule)")
b3=census_old(Pr,Cr,SPr,"ring L=16 (old dz rule)")
b4=census_old(Ps,Cs,SPs,"straight   (old dz rule)")
# FORM-L geometries: scaffold_L from the 2557 chain if present, else 2559's loader
mL=_re.search(r"def scaffold_L.*?\n(?=def |\S)", s57, _re.S)
exec(compile(mL.group(0),"scafL","exec"))
for L in (8,12,20,22):
    kap_ring=2*np.pi/(L*D)          # closed ring at pitch D (the FORM-L geometry)
    out=scaffold_L(L,kap_ring); PL,CL,SL=out[0],out[1],out[2]
    census(PL,CL,SL,f"ring L={L} (reach-S rule)")

# ---- C) DUTY RE-RUN under reach-S ----
print("\n[C] 2514 primary duty re-run, build_reach := reach-S (2557 verbatim):")
_g['build_reach']=build_reach_S      # override IN THE CHAIN NAMESPACE (dance_v8_duty and
build_reach=build_reach_S            # the 2510 engine resolve build_reach in _g, not here;
# first-draft override set only module globals -> bit-identical rerun of the OLD
# classifier, which exactly reproduced the registered 2514 record (banked as a
# reproduction check) and exposed the override failure -- disclosed in-patch.
Fr=ssv_vectors(Pr,Cr,SPr); Fs=ssv_vectors(Ps,Cs,SPs)
FREF=max(np.linalg.norm(Fr,axis=1).max(),np.linalg.norm(Fs,axis=1).max())
duties=[]
for dtf in (1/100,1/50,1/25):
    cnt,Es,nst=dance_v8_duty(Pr,Cr,SPr,FREF,dtf)
    s_,o_=cnt[1.0]['qq']; tot=s_+o_
    duty=s_/tot if tot else float('nan')
    duties.append((duty,tot))
    print(f"  RING dt=tauC/{int(1/dtf):>3}: duty_qq(reach-S)={duty:.4f} (n={tot})   [{time.time()-t0:.0f}s]")
print(f"  2514 registered values (old classifier), from the 2514 record, are quoted in")
print(f"  the audit document for the side-by-side; BRANCH reading re-applied below.")
guard=[i for i,(d,n) in enumerate(duties) if n<1000]
if guard:
    print(f"  thin-statistics guard fired -> BRANCH X under reach-S")
else:
    ge=[d>=DELTA_STATIC for d,_ in duties]
    if all(ge):   print(f"  duty_qq >= 3/7 at all dt -> BRANCH Y under reach-S")
    elif not any(ge): print(f"  duty_qq < 3/7 at all dt -> BRANCH L under reach-S")
    else:         print(f"  dt-inconsistent -> BRANCH X under reach-S")
print(f"\n[{time.time()-t0:.0f}s total]")
