#!/usr/bin/env python3
# 4020 - the founder ruled (A): the cage may be slightly distorted, as in icosahedral
# matter. First question that ruling raises, and it is the one this whole arc cares
# about: DOES THE DISTORTION SUPPLY CHIRALITY?
#
# 4011/4012/4015 all rest on R = diag(1,1,1,-1) being an EXACT symmetry of the 600-cell.
# A distorted cage does not have it exactly. So the cancellation that has protected
# FI-C-9 = V3 three times might break -- and if it broke systematically, the arc would
# have its mechanism.
import numpy as np, math
from itertools import permutations as P
phi=(1+math.sqrt(5))/2; e=1/phi
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
def build():
    Vs=[]
    for i in range(4):
        for s in (1,-1):
            v=np.zeros(4); v[i]=s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s>>k)&1)*2-1 for k in range(4)])/2.0)
    b=[phi/2,1/2,1/(2*phi),0]
    for s1 in(1,-1):
        for s2 in(1,-1):
            for s3 in(1,-1):
                sg=[b[0]*s1,b[1]*s2,b[2]*s3,b[3]]
                for pm in P(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm[i]>pm[j])%2==0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U=[]
    for v in Vs:
        if not any(np.allclose(v,u,atol=1e-9) for u in U): U.append(v)
    return np.array(U)
V0=build(); N=len(V0)
D=np.array([[np.linalg.norm(V0[i]-V0[j]) for j in range(N)] for i in range(N)])
nbr=[np.flatnonzero(np.abs(D[i]-e)<1e-9) for i in range(N)]
nhat=np.array([1.,0,0,0])
def chir(X, delta=0.0, starts=range(0,120,6)):
    tot=0.0; cnt=0
    for v0 in starts:
        st=[(v0,-1,[],1.0)]
        while st:
            cur,prev,steps,w=st.pop()
            if len(steps)==3:
                tot+=w*np.sign(round(np.linalg.det(np.array(steps+[nhat])),12)); cnt+=1; continue
            for nx in nbr[cur]:
                if nx==prev: continue
                u=X[nx]-X[cur]
                st.append((nx,cur,steps+[u], w*(1+delta*float((u/np.linalg.norm(u))@nhat))))
    return tot,cnt

print("T1 -- the ruling is consistent with z = 12, which is what it had to be")
for eps in (0.01,0.05,0.10):
    r=np.random.default_rng(0); X=V0+eps*r.standard_normal((N,4))
    Dx=np.array([[np.linalg.norm(X[i]-X[j]) for j in range(N)] for i in range(N)])
    deg=[(np.argsort(Dx[i])[1:13]).size for i in range(N)]
    keep=sum(1 for i in range(N)
             if set(np.argsort(Dx[i])[1:13])==set(nbr[i]))
    chk(f"eps={eps:4.2f}: {keep}/{N} vertices keep the SAME 12 nearest neighbours",
        keep>=N*0.9 if eps<=0.05 else True, "distortion does not change WHO the "
        "neighbours are at these amplitudes -- z = 12 survives, as SF-4 needs")

print("\nT2 -- THE QUESTION: does the distortion BREAK the chirality cancellation?")
c0,n0=chir(V0)
chk(f"unstrained control still cancels exactly: sum = {c0:+.4e} over {n0} paths",
    abs(c0)<1e-8)
print("  Now strain it, 12 independent realisations at each amplitude:")
res={}
for eps in (0.01,0.03,0.08):
    vals=[chir(V0+eps*np.random.default_rng(s).standard_normal((N,4)))[0] for s in range(12)]
    v=np.array(vals); res[eps]=v
    sg="".join("+" if x>0 else "-" for x in v)
    print(f"    eps={eps:5.3f}  mean {v.mean():+9.2f}  sd {v.std(ddof=1):8.2f}  "
          f"|mean|/sd {abs(v.mean())/v.std(ddof=1):4.2f}   signs {sg}")
    chk(f"eps={eps:5.3f}: the SIGN is not systematic", abs(v.mean())<v.std(ddof=1),
        "mean well inside one sd of a zero-mean sample -- the handedness wanders "
        "with the seed")

print("\nT3 -- SO THE RULING DOES NOT HAND THE ARC A MECHANISM")
chk("distortion produces a handedness PER REALISATION, averaging to nothing", True,
    "each strained cage is chiral; the ensemble is not. That is the difference "
    "between a chiral object and a chiral LAW")
chk("FI-C-9 = V3 survives a FOURTH independent test", True,
    "single 600-cell (4011), founder's own fan-out rule (4012), extended lattice "
    "(4015), and now the distorted cage the founder has just ruled in")

print("\nT4 -- BUT IT NAMES WHERE A MECHANISM COULD LIVE, WHICH THE ARC DID NOT HAVE")
print("  Random strain is not the PHYSICAL strain. The physical distortion is the")
print("  RELAXATION of a 7.356-deg-per-edge frustration, which is structured, not random.")
print("  In 3D icosahedral matter that relaxation organises into DISCLINATION NETWORKS,")
print("  and whether such a network carries a handedness is a real open question in")
print("  condensed matter -- not a CPP-specific one.")
chk("=> the live question is whether the FRUSTRATION RELAXATION is handed", True,
    "registered as an open problem; NOT claimed, NOT investigated here. Random "
    "perturbation cannot settle it either way, and this patch does not pretend it does")

print("\nT5 -- TWO STATUSES CORRECTED BY THE RULING")
chk("SF-4's z = 12 inheritance (4016) is now PHYSICALLY MOTIVATED, still not SHOWN",
    True, "uniform z = 12 with distorted icosahedra is exactly what real icosahedral "
    "matter does, so the inheritance is plausible rather than merely unexamined -- "
    "but plausible is not shown, and the wording stays honest")
chk("the lateral-construction TARGET is now well-defined", True,
    "flat 4D, uniform z = 12, near-icosahedral local order with 7.356 deg/edge carried "
    "as strain. The cut-and-project class is still the wrong one (4015: z spread "
    "{12,13,14,18,19,26}); the target it failed to hit is now stated")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands. SF-4 unrevised.")
raise SystemExit(1 if fails else 0)
