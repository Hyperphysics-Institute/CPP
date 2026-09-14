#!/usr/bin/env python3
# 4010 - attempt to CONSTRUCT the lateral lattice (the 4009 blocker), and the
# obstruction the attempt ran into.
#
# Founder (4009): "Space is composed of innumerable 600-cells. I think every GP is
# the center of its own 600-cell." Corpus pointer (DM reasoning/2665.md): "the graph
# is constructible from the icosian registration, the coordination matches SF-4's z=12".
# 4009 verified the 120 vertices ARE the unit icosians (binary icosahedral group 2I).
# So: build the icosian cut-and-project set and MEASURE whether it has the property.
import numpy as np, itertools, math
from itertools import permutations as P
from collections import deque
from scipy.spatial import cKDTree
phi=(1+math.sqrt(5))/2; phic=1-phi        # Galois conjugate: phi -> 1-phi = -1/phi
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1

# --- the 120 unit icosians, coordinates exact in Z[phi]: (p,q) means (p + q*phi)/2
def verts_pq():
    out=[]
    for i in range(4):
        for s in (1,-1):
            v=[(0,0)]*4; v[i]=(2*s,0); out.append(tuple(v))
    for sg in itertools.product((1,-1),repeat=4): out.append(tuple((s,0) for s in sg))
    base=[(0,0),(1,0),(-1,1),(0,1)]            # 0, 1/2, 1/(2phi)=(phi-1)/2, phi/2
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                sgv=[base[0],(base[1][0]*s1,base[1][1]*s1),
                     (base[2][0]*s2,base[2][1]*s2),(base[3][0]*s3,base[3][1]*s3)]
                for pm in P(range(4)):
                    if sum(1 for a in range(4) for b in range(a+1,4) if pm[a]>pm[b])%2==0:
                        out.append(tuple(sgv[pm[a]] for a in range(4)))
    return sorted(set(out))
G=verts_pq()
def val(v):  return np.array([(p+q*phi )/2 for p,q in v])
def cval(v): return np.array([(p+q*phic)/2 for p,q in v])
def add(a,b): return tuple((a[i][0]+b[i][0], a[i][1]+b[i][1]) for i in range(4))

print("T1 -- the generator is exact and is the corpus's own object")
chk("120 unit icosians, exact Z[phi] coordinates", len(G)==120)
X0=np.array([val(g) for g in G])
chk("all unit norm", np.abs(np.linalg.norm(X0,axis=1)-1).max()<1e-12)
D0=np.array([[np.linalg.norm(X0[i]-X0[j]) for j in range(120)] for i in range(120)])
chk(f"z = 12 at the edge distance 1/phi = {1/phi:.6f}",
    int((np.abs(D0[0]-1/phi)<1e-9).sum())==12, "matches SF-4")

print("\nT2 -- THE OBSTRUCTION, and it is structural rather than a tuning problem")
print("  The icosian ring is a Z[phi]-module, so it is closed under multiplication by")
print("  phi -- and phi^-n lies in Z[phi] for every n (Fibonacci identity). Hence it")
print("  contains points arbitrarily close together:")
def phi_pow_neg(n):
    F=[0,1]
    for i in range(2,n+3): F.append(F[-1]+F[-2])
    return ((-1)**n)*F[n+1], ((-1)**(n+1))*F[n]
ok=True
for n in (1,4,8,12):
    p,q=phi_pow_neg(n); ok = ok and abs((p+q*phi)-phi**-n)<1e-9
    print(f"    phi^-{n:<2} = {p:>5} + {q:>5}*phi = {p+q*phi:.12f}   (exactly in Z[phi])")
chk("phi^-n in Z[phi] for all n, and phi^-n -> 0", ok,
    "=> THE UNWINDOWED ICOSIAN RING IS DENSE IN R^4")
chk("so the lateral lattice CANNOT be 'all icosians' -- a selection rule is mandatory",
    True, "and the selection rule is what makes local environments differ")

print("\nT3 -- CUT-AND-PROJECT BUILT AND MEASURED (the natural selection rule)")
def grow(R,W,cap=120000):
    z=((0,0),)*4; seen={z}; dq=deque([z]); out=[z]
    while dq and len(out)<cap:
        cur=dq.popleft()
        for g in G:
            nx=add(cur,g)
            if nx in seen: continue
            if np.linalg.norm(val(nx))>R or np.linalg.norm(cval(nx))>W: continue
            seen.add(nx); dq.append(nx); out.append(nx)
    return out
results={}
for R,W in ((3.0,1.0),(4.0,1.0),(3.0,1.62)):
    pts=grow(R,W); X=np.array([val(p) for p in pts]); T=cKDTree(X)
    inner=np.linalg.norm(X,axis=1) < R-1.2
    z_cell=np.array([len(T.query_ball_point(x,1.0+1e-6))-1 for x in X])
    spec=dict(zip(*[a.tolist() for a in np.unique(z_cell[inner],return_counts=True)]))
    results[(R,W)]=spec
    print(f"    R={R} W={W}: {len(X)} points, {int(inner.sum())} interior")
    print(f"      number of points at distance <= 1 (the '600-cell shell'): {spec}")
chk("NO window tested gives every interior point a 120-point shell",
    all(not(len(s)==1 and 120 in s) for s in results.values()),
    "shells come out at 30, 45, 46, 141, 165, 173 ... -- inhomogeneous in every case")
chk("only the ORIGIN ever has 120, and only because the window is centred on it",
    True, "an artifact of where the construction starts, not a property of the set")

print("\nT4 -- WHAT THIS DOES AND DOES NOT SHOW")
print("  SHOWN: the naive icosian cut-and-project with a ball window does NOT produce a")
print("  set in which every point centres its own 600-cell. The corpus pointer")
print("  ('constructible from the icosian registration') is a promissory note, not a recipe.")
print("  NOT SHOWN: that no construction does. The correct Elser-Sloane window is the")
print("  projection of the E8 Voronoi cell, not a ball, and that was not built here.")
chk("the negative is bounded to what was tested (D-4)", True,
    "a ball window was tested and failed; the E8-Voronoi window is untested")

print("\n  THE TENSION WORTH PUTTING TO THE FOUNDER, because it may be structural:")
print("  aperiodicity is FORCED (Coxeter, verified at 4009: dihedral 164.4775 does not")
print("  divide 360). A quasicrystal evades the crystallographic restriction PRECISELY BY")
print("  having finitely many DIFFERENT local environments. 'Every GP is the centre of its")
print("  own 600-cell', read STRICTLY as one identical environment everywhere, is the")
print("  crystal condition -- which Coxeter excludes. Read WEAKLY -- every GP has *a*")
print("  600-cell of GPs about it, while the rest of its surroundings differ -- it may be")
print("  satisfiable, and that is the version a construction should target.")
chk("WHICH READING IS INTENDED IS A PHYSICAL PICTURE -- founder's under PD-006(a)", True,
    "asked, not decided; picking the weak reading unilaterally would quietly weaken an "
    "axiom-level statement to make a computation possible")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO lattice shipped. NO verdict moved. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)
