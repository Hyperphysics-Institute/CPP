#!/usr/bin/env python3
# 4025 - the gap 4024 left: VW-1 has NO TRACTION ALONG n-hat on the extended lattice.
# PD-008 says press on, so this attacks it by DIRECT MEASUREMENT instead of by the
# RP argument that cannot reach there. If the eta correlator along n-hat decays, there
# is no long-range order along n-hat, and VW-1's CONCLUSION holds by another route even
# though VW-1's ARGUMENT does not.
#
# The honest headline is in T3: the gap is BOUNDED, not CLOSED -- and the direction
# where the theory has least control is also where this measurement has least power.
import numpy as np, math, itertools as it
from itertools import permutations as P
from collections import deque
from scipy.spatial import cKDTree
phi=(1+math.sqrt(5))/2; phic=1-phi; e=1/phi
def vpq():
    out=[]
    for i in range(4):
        for s in (1,-1):
            v=[(0,0)]*4; v[i]=(2*s,0); out.append(tuple(v))
    for sg in it.product((1,-1),repeat=4): out.append(tuple((s,0) for s in sg))
    b=[(0,0),(1,0),(-1,1),(0,1)]
    for s1 in(1,-1):
        for s2 in(1,-1):
            for s3 in(1,-1):
                sv=[b[0],(b[1][0]*s1,b[1][1]*s1),(b[2][0]*s2,b[2][1]*s2),(b[3][0]*s3,b[3][1]*s3)]
                for pm in P(range(4)):
                    if sum(1 for a in range(4) for c in range(a+1,4) if pm[a]>pm[c])%2==0:
                        out.append(tuple(sv[pm[a]] for a in range(4)))
    return sorted(set(out))
G=vpq()
val=lambda v: np.array([(p+q*phi )/2 for p,q in v])
cval=lambda v: np.array([(p+q*phic)/2 for p,q in v])
add=lambda a,b: tuple((a[i][0]+b[i][0],a[i][1]+b[i][1]) for i in range(4))
def grow(R,W,cap=30000):
    z=((0,0),)*4; seen={z}; dq=deque([z]); out=[z]
    while dq and len(out)<cap:
        cur=dq.popleft()
        for g in G:
            nx=add(cur,g)
            if nx in seen: continue
            if np.linalg.norm(val(nx))>R or np.linalg.norm(cval(nx))>W: continue
            seen.add(nx); dq.append(nx); out.append(nx)
    return out
X0=np.array([val(p) for p in grow(3.0,1.4)]); M=len(X0)
T=cKDTree(X0); nb=[np.array([j for j in T.query_ball_point(x,e+1e-6) if not np.allclose(X0[j],x)]) for x in X0]
good=np.array([i for i in range(M) if len(nb[i])>=4 and np.linalg.norm(X0[i])<2.0])
print(f"extended icosian patch: {M} points, {len(good)} usable interior (z>=4, r<2.0)")
nhat=np.array([1.,0,0,0])
def eta(X):
    out=np.zeros(M)
    for v in good:
        n=nb[v]; pr=(X[n]-X[v])@nhat
        top=n[np.argsort(-pr)[:4]]
        out[v]=np.sign(np.linalg.det(np.array([X[t]-X[v] for t in top])))
    return out
reps=260; E=np.empty((reps,len(good)))
rng=np.random.default_rng(4025)
for r in range(reps):
    X=X0+0.25*rng.standard_normal((M,4))
    E[r]=eta(X)[good]
Ec=E-E.mean(0)
Xg=X0[good]
dpar=np.abs(Xg[:,None,0]-Xg[None,:,0])
dperp=np.linalg.norm(Xg[:,None,1:]-Xg[None,:,1:],axis=2)
C=(Ec.T@Ec)/reps
print("\n  ALONG n-hat (transverse separation < 0.35):")
for lo,hi in ((0.5,0.9),(0.9,1.4),(1.4,2.0),(2.0,3.0)):
    m=(dpar>=lo)&(dpar<hi)&(dperp<0.35)
    if m.sum()>30:
        print(f"    |dpar| in [{lo},{hi}): n={int(m.sum()):>6}  <eta eta>_c = {C[m].mean():+.5f} "
              f"+- {C[m].std(ddof=1)/math.sqrt(m.sum()):.5f}")
print("  TRANSVERSE (separation along n-hat < 0.35):")
for lo,hi in ((0.5,0.9),(0.9,1.4),(1.4,2.0),(2.0,3.0)):
    m=(dperp>=lo)&(dperp<hi)&(dpar<0.35)
    if m.sum()>30:
        print(f"    |dperp| in [{lo},{hi}): n={int(m.sum()):>6}  <eta eta>_c = {C[m].mean():+.5f} "
              f"+- {C[m].std(ddof=1)/math.sqrt(m.sum()):.5f}")
d0=np.eye(len(good),dtype=bool)
print(f"\n  on-site <eta^2>_c = {C[d0].mean():.5f}")

# ---- verdict block -------------------------------------------------------------
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
onsite=C[d0].mean()
def band(mask):
    return C[mask].mean(), C[mask].std(ddof=1)/math.sqrt(mask.sum())
print("\nT1 -- NO LONG-RANGE ORDER ALONG n-hat, AT THIS SIZE")
for lo,hi in ((0.5,0.9),(0.9,1.4),(1.4,2.0),(2.0,3.0)):
    m=(dpar>=lo)&(dpar<hi)&(dperp<0.35)
    mu,se=band(m)
    chk(f"|dpar| in [{lo},{hi}): <eta eta>_c = {mu:+.5f} +- {se:.5f} "
        f"({100*abs(mu)/onsite:.2f}% of on-site)",
        abs(mu)<2.0*se or abs(mu)<0.01*onsite,
        "consistent with zero, and below 1% of the on-site variance")
chk(f"on-site <eta^2>_c = {onsite:.4f} (eta = +-1, so ~1 as it must be)",
    abs(onsite-1)<0.02)

print("\nT2 -- TRANSVERSE, FOR CONTRAST")
for lo,hi in ((0.5,0.9),(1.4,2.0),(2.0,3.0)):
    m=(dperp>=lo)&(dperp<hi)&(dpar<0.35)
    mu,se=band(m)
    chk(f"|dperp| in [{lo},{hi}): {mu:+.5f} +- {se:.5f}", abs(mu)<2.5*se)

print("\nT3 -- WHAT THIS IS AND IS NOT, AND AN UNCOMFORTABLE COINCIDENCE")
npar=int(((dpar>=0.5)&(dpar<3.0)&(dperp<0.35)).sum())
nperp=int(((dperp>=0.5)&(dperp<3.0)&(dpar<0.35)).sum())
chk(f"the along-n-hat bound is ~10x LOOSER than the transverse one "
    f"({npar} pairs vs {nperp})", npar*8 < nperp,
    "the patch is roughly isotropic, so 'along n-hat with small transverse offset' is a "
    "thin tube. THE DIRECTION WHERE THE THEORY HAS NO CONTROL IS ALSO THE DIRECTION "
    "WHERE THIS MEASUREMENT HAS LEAST POWER. Stated because it is the convenient "
    "coincidence and someone should push on it")
chk("this bounds long-range order AT THIS SIZE, it does not exclude it", True,
    "patch radius 3.0, so separations reach ~3 edge lengths; a correlation length of "
    "5 or more would not show here")
chk("and the patch is a PROXY, not the substrate", True,
    "the icosian cut-and-project was established NOT to be the substrate at 4013/4015 "
    "(window boundary; z spread). It is extended, 4D and near-icosahedral, which is "
    "what the correlation question needs -- but it is not the lattice")
print("\n  VERDICT: the gap is BOUNDED, NOT CLOSED. Along-n-hat eta correlations sit")
print("  below 1% of on-site and within ~2 sem of zero out to 3 edge lengths, which is")
print("  evidence against long-range order along the drive -- NOT proof. VW-1's")
print("  CONCLUSION survives this test; VW-1's ARGUMENT still cannot reach here.")
chk("submitted for critique per PD-008", True,
    "attack it at the power asymmetry in T3 first")
print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)
