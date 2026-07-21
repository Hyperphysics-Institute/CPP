#!/usr/bin/env python3
"""FA-SG-R1 leg L2 (Patch 2687): registered-arena restriction/prediction test.

Frozen [ADJ] (charter SS2 R1-L2): the I1 field (both distance metrics, as
committed at 2671) shown quantitatively consistent with the extended-
instrument solution governed by l, with statistic and tolerance chosen and
committed BEFORE the comparison runs. The commitments below were fixed
before any I1-vs-envelope residual was computed:

  P1/S1 (structural class prediction). Screening locality (l = 0.090 fm <<
  arena size) predicts that ANY compact arena of I1's proportions shows a
  sign-oscillating field with no clean decay regime. Classifier: arena is
  "sign-oscillating / no-clean-regime" iff neg-site fraction >= 0.25 AND
  there is no constant-sign, monotone-|shell-mean f*r| shell run spanning
  >= 0.3 fm. Prediction: I1 (chord metric), I1 (geodesic metric), and the
  two compact-FCC restriction arenas (diameter-matched to I1's max chord
  1.178 fm; count-matched to I1's 120 sites) ALL classify as
  sign-oscillating/no-clean-regime. PASS iff all four match.

  P2/S2 (envelope consistency). Per metric: I1 shell means f_s, I6-
  normalized at the shell nearest d_reg = 1.15 fm; extended envelope from
  FCC R=9 shell means (window 0.45-1.8 fm), same normalization. Residual
  D_s = ln|f_s r_s| - ln(env(r_s) r_s). Tolerance T = 1.25 x the extended
  instrument's own max shell modulation about its fitted envelope over
  r in [0.36, 1.2] fm (log units; computed BEFORE I1 residuals below).
  PASS iff >= 6 of 8 shells have |D| <= T and none exceeds 1.6 T.

  S3 (screening-locality diagnostic, reported, no pass/fail): compact-FCC
  solves vs the full-arena field restricted to the same sites.

Stronger-form clause: a construction permitting a DIRECT l readout on I1
supersedes if found; the determination is reported in the leg record.
"""
import itertools, math, numpy as np

PHI=(1+math.sqrt(5))/2; L_UNIT=0.589; L_EDGE=L_UNIT/PHI; D_REG=1.15
alpha=L_EDGE/(math.pi*math.sqrt(2))

# ---------- extended instrument (FCC R=9) : envelope + own modulation ----------
def fcc_ball(R):
    pts=[]
    for i in range(-2*R,2*R+1):
        for j in range(-2*R,2*R+1):
            for k in range(-2*R,2*R+1):
                if (i+j+k)%2==0:
                    x=np.array([i,j,k])/math.sqrt(2.0)
                    if np.linalg.norm(x)<=R: pts.append(x)
    return np.array(pts)
P=fcc_ball(9)*L_EDGE
src=int(np.argmin(np.linalg.norm(P,axis=1)))
mask=np.ones(len(P),bool); mask[src]=False
Q=P[mask]; r0=np.linalg.norm(Q,axis=1)
Dm=np.linalg.norm(Q[:,None,:]-Q[None,:,:],axis=2); np.fill_diagonal(Dm,np.inf)
phiX=np.linalg.solve(np.eye(len(Q))+alpha/Dm, 1.0/r0)
shells=np.unique(np.round(r0,6)); rs,fs=[],[]
for s in shells[shells<=2.2]:
    m=np.abs(r0-s)<1e-6; rs.append(s); fs.append(phiX[m].mean())
rs,fs=np.array(rs),np.array(fs)
w=(rs>=0.45)&(rs<=1.8)
c=np.polyfit(rs[w],np.log(np.abs(fs[w])*rs[w]),1)
l_ext=-1.0/c[0]
mod=np.log(np.abs(fs)*rs)-np.polyval(c,rs)
mm=(rs>=0.36)&(rs<=1.2)
T=1.25*np.max(np.abs(mod[mm]))
print(f"extended instrument: l_ext={l_ext:.4f} fm ; max own modulation over "
      f"[0.36,1.2] fm = {np.max(np.abs(mod[mm])):.3f} log units ; T = {T:.3f}")

def classify(rlist,flist,neg_frac):
    r_,f_=np.array(rlist),np.array(flist)
    order=np.argsort(r_); r_,f_=r_[order],f_[order]
    g=np.abs(f_)*r_
    best=0.0; i=0
    while i<len(r_):
        j=i
        while j+1<len(r_) and np.sign(f_[j+1])==np.sign(f_[i]) and g[j+1]<=g[j]:
            j+=1
        best=max(best,r_[j]-r_[i]); i=j+1
    osc=(neg_frac>=0.25) and (best<0.3)
    return osc,best

# ---------- I1 (both metrics) ----------
verts=[]
for signs in itertools.product([0.5,-0.5],repeat=4): verts.append(signs)
for i in range(4):
    for s in (1.0,-1.0):
        v=[0.0]*4; v[i]=s; verts.append(tuple(v))
even_perms=[(0,1,2,3),(0,2,3,1),(0,3,1,2),(1,0,3,2),(1,2,0,3),(1,3,2,0),
            (2,0,1,3),(2,1,3,0),(2,3,0,1),(3,0,2,1),(3,1,0,2),(3,2,1,0)]
base=(PHI/2,0.5,1/(2*PHI),0.0); seen=set()
for perm in even_perms:
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                v=[0.0]*4
                vals=(s1*base[0],s2*base[1],s3*base[2],0.0)
                for k in range(4): v[perm[k]]=vals[k]
                t=tuple(round(x,9) for x in v)
                if t not in seen: seen.add(t); verts.append(t)
V=np.array(verts); assert len(V)==120
D4=np.linalg.norm(V[:,None,:]-V[None,:,:],axis=2)*L_UNIT
dmin=D4[D4>1e-9].min()
Ad=(np.abs(D4-dmin)<1e-6).astype(float)
Dg=np.where(Ad>0,1.0,1e9); np.fill_diagonal(Dg,0.0)
for k in range(120): Dg=np.minimum(Dg,Dg[:,k][:,None]+Dg[k,:][None,:])
Dg*=L_EDGE

def i1_solve(D,label):
    resp=np.arange(1,120); r0=D[0,resp]
    G=np.zeros((119,119))
    for a in range(119):
        for b in range(119):
            if a!=b: G[a,b]=1.0/D[resp[a],resp[b]]
    f=np.linalg.solve(np.eye(119)+alpha*G,1.0/r0)
    sh=sorted(set(np.round(r0,6))); rl,fl=[],[]
    for s in sh:
        m=np.abs(r0-s)<1e-6; rl.append(s); fl.append(f[m].mean())
    neg=(f<0).mean()
    osc,best=classify(rl,fl,neg)
    print(f"\nI1 [{label}]: shells={len(rl)}  neg-frac={neg:.3f}  "
          f"longest clean run={best:.3f} fm  class={'OSC/NO-REGIME' if osc else 'CLEAN-REGIME'}")
    # S2 residuals
    rl,fl=np.array(rl),np.array(fl)
    inorm=int(np.argmin(np.abs(rl-D_REG)))
    lhs=np.log(np.abs(fl)*rl)-np.log(np.abs(fl[inorm])*rl[inorm])
    rhs=-(rl-rl[inorm])/l_ext
    Dres=lhs-rhs
    npass=int(np.sum(np.abs(Dres)<=T)); worst=np.max(np.abs(Dres))
    print(f"  S2: norm shell r={rl[inorm]:.3f} fm ; per-shell |D| = "
        +np.array2string(np.abs(Dres),precision=2)
        +f"\n  S2: {npass}/{len(rl)} within T={T:.2f} ; worst={worst:.2f} "
          f"(1.6T={1.6*T:.2f}) -> {'PASS' if npass>=len(rl)-2 and worst<=1.6*T else 'FAIL'}")
    return osc

osc_c=i1_solve(D4,"4D chord metric")
osc_g=i1_solve(Dg,"graph-geodesic metric")

# ---------- compact-FCC restriction arenas ----------
def compact(radius_fm,label):
    sel=np.linalg.norm(P-P[src],axis=1)<=radius_fm+1e-9
    Ps=P[sel]
    s2=int(np.argmin(np.linalg.norm(Ps-P[src],axis=1)))
    m2=np.ones(len(Ps),bool); m2[s2]=False
    Qs=Ps[m2]; rr=np.linalg.norm(Qs-Ps[s2],axis=1)
    Ds=np.linalg.norm(Qs[:,None,:]-Qs[None,:,:],axis=2); np.fill_diagonal(Ds,np.inf)
    f=np.linalg.solve(np.eye(len(Qs))+alpha/Ds,1.0/rr)
    sh=sorted(set(np.round(rr,6))); rl,fl=[],[]
    for s in sh:
        m=np.abs(rr-s)<1e-6; rl.append(s); fl.append(f[m].mean())
    neg=(f<0).mean(); osc,best=classify(rl,fl,neg)
    print(f"\ncompact-FCC [{label}]: N={len(Ps)} sites, max pair dist "
          f"{np.max(np.linalg.norm(Qs-Ps[s2],axis=1)):.3f} fm ; neg-frac={neg:.3f} ; "
          f"longest clean run={best:.3f} fm ; class={'OSC/NO-REGIME' if osc else 'CLEAN-REGIME'}")
    # S3 diagnostic: vs full-arena field on same sites
    idx_full=np.where(mask)[0]; posQ={tuple(np.round(q,9)):i for i,q in enumerate(Q)}
    dev=[]
    for qi,qq in enumerate(Qs):
        key=tuple(np.round(qq,9))
        if key in posQ: dev.append(abs(f[qi]-phiX[posQ[key]])/max(abs(phiX[posQ[key]]),1e-30))
    dev=np.array(dev)
    print(f"  S3 diagnostic: median rel deviation vs full-arena field = {np.median(dev):.3f} "
          f"(90th pct {np.percentile(dev,90):.2f})")
    return osc

osc_d=compact(0.60,"diameter-matched, r<=0.60 fm")
osc_n=compact(1.00,"count-matched, r<=1.00 fm")

print(f"\nS1 verdict: predictions all OSC/NO-REGIME -> observed "
      f"I1chord={osc_c} I1geo={osc_g} compactD={osc_d} compactN={osc_n} "
      f"-> {'PASS' if all([osc_c,osc_g,osc_d,osc_n]) else 'FAIL'}")
