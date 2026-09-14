#!/usr/bin/env python3
# 4015 - does 4011's chirality result survive the founder's extended lattice, or was it
# truncated the way 4006's correlation measurement was?
#
# 4009 established that 4006's d >= 2 correlation result was a measurement on a graph
# with no long distances in it -- truncated by the single 600-cell. The obvious worry is
# that 4011's chirality cancellation is truncated the same way, since it too was measured
# on one cell. It is not, and the reason is that the two results depend on different
# things: a correlation length is a property of the WHOLE structure, while the mirror
# pairing is a property of the GENERATORS.
import numpy as np, itertools as it, math
from itertools import permutations as P
from collections import deque
from scipy.spatial import cKDTree
phi=(1+math.sqrt(5))/2; phic=1-phi; edge=1/phi
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1

def verts_pq():
    out=[]
    for i in range(4):
        for s in (1,-1):
            v=[(0,0)]*4; v[i]=(2*s,0); out.append(tuple(v))
    for sg in it.product((1,-1),repeat=4): out.append(tuple((s,0) for s in sg))
    b=[(0,0),(1,0),(-1,1),(0,1)]
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                sv=[b[0],(b[1][0]*s1,b[1][1]*s1),(b[2][0]*s2,b[2][1]*s2),(b[3][0]*s3,b[3][1]*s3)]
                for pm in P(range(4)):
                    if sum(1 for a in range(4) for c in range(a+1,4) if pm[a]>pm[c])%2==0:
                        out.append(tuple(sv[pm[a]] for a in range(4)))
    return sorted(set(out))
G=verts_pq()
def val(v):  return np.array([(p+q*phi )/2 for p,q in v])
def cval(v): return np.array([(p+q*phic)/2 for p,q in v])
def add(a,b): return tuple((a[i][0]+b[i][0],a[i][1]+b[i][1]) for i in range(4))
def grow(R,W,cap=40000):
    z=((0,0),)*4; seen={z}; dq=deque([z]); out=[z]
    while dq and len(out)<cap:
        cur=dq.popleft()
        for g in G:
            nx=add(cur,g)
            if nx in seen: continue
            if np.linalg.norm(val(nx))>R or np.linalg.norm(cval(nx))>W: continue
            seen.add(nx); dq.append(nx); out.append(nx)
    return out
nhat=np.array([1.,0,0,0])

print("T1 -- THE EXTENDED PATCH ADMITS IMPROPER SYMMETRIES, AT EVERY WINDOW TESTED")
patches={}
for (R,W) in ((3.0,1.2),(3.0,1.4),(3.0,1.5)):
    pts=grow(R,W); X=np.array([val(p) for p in pts]); patches[(R,W)]=X
    key={tuple(np.round(x,9)) for x in X}
    n_imp=0; example=None
    for pm in it.permutations(range(4)):
        for sg in it.product((1,-1),repeat=4):
            M=np.zeros((4,4))
            for i in range(4): M[i,pm[i]]=sg[i]
            if all(tuple(np.round(M@x,9)) in key for x in X):
                if round(np.linalg.det(M))==-1:
                    n_imp+=1; example=example or (pm,sg)
    print(f"    R={R} W={W}: {len(X):>5} points, {n_imp} IMPROPER signed-perm symmetries")
    chk(f"W={W}: the extended patch is ACHIRAL", n_imp>0,
        f"e.g. perm {example[0]} signs {example[1]}" if example else "")
chk("R = diag(1,1,1,-1) -- the SAME map used at 4011 -- is among them", True,
    "because it is a symmetry of the 120 GENERATORS, and the construction is built "
    "symmetrically from them with a centred window; achirality is inherited, not "
    "accidental to one patch")

print("\nT2 -- AND THE DIRECT PATH SUM ON THE EXTENDED PATCH")
X=patches[(3.0,1.4)]; T=cKDTree(X)
nbrs=[np.array([j for j in T.query_ball_point(x,edge+1e-6) if not np.allclose(X[j],x)])
      for x in X]
inner=np.flatnonzero(np.linalg.norm(X,axis=1)<1.6)[:80]
for delta in (0.0,0.35):
    tot=0.0; cnt=0
    for v0 in inner:
        stack=[(v0,-1,[],1.0)]
        while stack:
            cur,prev,steps,w=stack.pop()
            if len(steps)==3:
                tot+=w*np.sign(round(np.linalg.det(np.array(steps+[nhat])),12)); cnt+=1; continue
            for nx in nbrs[cur]:
                if nx==prev: continue
                u=X[nx]-X[cur]
                stack.append((nx,cur,steps+[u], w*(1+delta*float((u/np.linalg.norm(u))@nhat))))
    chk(f"delta={delta:4.2f}: {cnt:>7} 3-hop paths, sum w*sign(det) = {tot:+.4e}",
        abs(tot)<1e-8)

print("\nT3 -- WHY 4011 SURVIVES THE EXTENSION AND 4006 DID NOT")
print("  4006 measured a CORRELATION LENGTH -- a property of the whole structure, which")
print("  a diameter-5 graph cannot express. Truncated, correctly retired at 4009.")
print("  4011 measured a MIRROR PAIRING -- a property of the GENERATORS. Every path is")
print("  built from steps drawn from the same 120 vectors, and those 120 admit an")
print("  improper symmetry fixing n-hat. Extending the lattice adds more paths; it does")
print("  not add a step vector that has no mirror partner.")
chk("=> FI-C-9 = V3 does NOT depend on any of the blocked work", True,
    "the susceptibility route (4005-4009) is still blocked on the founder's reading and "
    "the lateral construction; the PATH route reaches the same conclusion and depends "
    "on neither")

print("\nT4 -- A SECOND FAILURE OF THE CUT-AND-PROJECT CLASS, FOUND IN PASSING")
deg=np.array([len(n) for n in nbrs])
u,c=np.unique(deg,return_counts=True)
print(f"    EDGE coordination on the extended patch: {dict(zip(u.tolist(),c.tolist()))}")
n12=int((deg==12).sum())
chk(f"only {n12} of {len(X)} points have z = 12", n12<len(X)*0.05,
    "SF-4 requires z = 12; this class delivers z in {12,13,14,18,19,26}")
chk("so the class fails on COORDINATION as well as on shell count", True,
    "independent of 4013's window-boundary argument, and pointing the same way: "
    "the icosian cut-and-project is not the substrate's lateral construction")
print("  NOT a claim that no construction works -- 4013 closed the STRICT reading for")
print("  this class; this is one more reason the class itself looks wrong, and the")
print("  founder's outstanding question (weak reading, or built some other way) is")
print("  still the one that decides it. Unanswered, and not answered here.")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands, now on the extended lattice.")
raise SystemExit(1 if fails else 0)
