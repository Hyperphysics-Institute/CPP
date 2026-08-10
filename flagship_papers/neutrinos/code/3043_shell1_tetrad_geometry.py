#!/usr/bin/env python3
"""3043_shell1_tetrad_geometry.py — RES-SF4-STRUCT-1 geometric backbone:
exact facts about tetrahedral 4-subsets of the 600-cell first shell.

FACT-G1: shell census from a vertex (reconfirm V = 12, 20, 12, 30 ...).
FACT-G2: enumerate all C(12,4) = 495 quartets of shell 1; classify by
  pairwise-distance multiset; report (a) whether an EXACTLY regular
  tetrahedron exists, (b) the most-uniform quartet class (distortion =
  max/min pairwise distance), its count, and (c) whether optimal
  quartets partition the 12 into 3 disjoint tetrads (a tetrad frame).
FACT-G3: the tetrahedral rotation subgroup T < I acting on the shell:
  orbit structure (simply transitive?).

Pure geometry; no physics minted. Seedless (exact enumeration).
"""
import numpy as np, itertools
PHI = (1+np.sqrt(5))/2

def verts_600():
    V=[]
    for i in range(4):
        for s in (1,-1):
            v=[0,0,0,0]; v[i]=s; V.append(v)
    for signs in itertools.product((0.5,-0.5),repeat=4):
        V.append(list(signs))
    from itertools import permutations
    base=[PHI/2,0.5,1/(2*PHI),0]
    evens=[p for p in permutations(range(4))
           if sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])%2==0]
    S=set()
    for p in evens:
        for s1 in (1,-1):
            for s2 in (1,-1):
                for s3 in (1,-1):
                    v=[0,0,0,0]; vals=[s1*base[0],s2*base[1],s3*base[2],0.0]
                    for k in range(4): v[p[k]]=vals[k]
                    S.add(tuple(round(x,10) for x in v))
    V=[tuple(round(x,10) for x in v) for v in V]+list(S)
    V=sorted(set(V))
    assert len(V)==120, len(V)
    return np.array(V)

V = verts_600()
apex = np.array([1.0,0,0,0])
d2 = np.round(np.sum((V-apex)**2,axis=1),8)
shells = {}
for x in d2:
    shells[x]=shells.get(x,0)+1
census = sorted(shells.items())
print("FACT-G1 shell census (d^2: count):",
      ", ".join(f"{a:g}:{b}" for a,b in census[:6]))
s1 = V[np.isclose(d2, np.min([x for x in d2 if x>1e-9]))]
print(f"  shell-1 count = {len(s1)} (want 12); d^2 = "
      f"{np.min([x for x in d2 if x>1e-9]):.6f} (1/phi^2 = {1/PHI**2:.6f})")

# FACT-G2: quartet classification
def pd(q):
    return sorted(np.round(np.linalg.norm(q[i]-q[j]),6)
                  for i in range(4) for j in range(i+1,4))
classes = {}
for idx in itertools.combinations(range(12),4):
    q = s1[list(idx)]
    key = tuple(pd(q))
    classes.setdefault(key, []).append(idx)
regular = [(k,v) for k,v in classes.items() if len(set(k))==1]
print(f"FACT-G2: {len(classes)} distance-multiset classes among 495 quartets")
print(f"  exactly-regular tetrahedra: "
      f"{sum(len(v) for _,v in regular) if regular else 0}")
best = min(classes.items(), key=lambda kv: kv[0][-1]/kv[0][0])
bk, bv = best
print(f"  most-uniform class: distances {sorted(set(bk))} "
      f"(distortion max/min = {bk[-1]/bk[0]:.4f}), count = {len(bv)}, "
      f"multiset = {bk}")
# partition check on the optimal class
opt = [frozenset(i) for i in bv]
part_found = False
for a in opt:
    for b in opt:
        if a & b: continue
        c = frozenset(range(12)) - a - b
        if c in opt:
            part_found = True
print(f"  optimal quartets partition 12 into 3 disjoint tetrads: "
      f"{part_found}")

# FACT-G3: T-orbit structure. Build the icosahedral rotation group of
# shell 1 (orthogonal maps of the 3-space x1 = phi/2 fixing the set),
# then find a tetrahedral (order-12) subgroup and its orbits.
P = s1[:,1:]  # 3D coordinates in the tangent space
key = {tuple(np.round(p,6)):i for i,p in enumerate(P)}
import itertools as it
# generate rotation group as permutations induced by orthogonal maps:
# search all signed permutation-free approach: use pairwise-distance-
# preserving vertex permutations generated from mapping candidates.
def perm_from_map(M):
    idx=[]
    for p in P:
        q=tuple(np.round(M@p,6))
        if q not in key: return None
        idx.append(key[q])
    return tuple(idx)
# candidate generators: rotations by 2pi/5 about a vertex axis and 2pi/3
# about a face axis — construct numerically via Rodrigues.
def rot(axis,ang):
    a=axis/np.linalg.norm(axis); K=np.array([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]])
    return np.eye(3)+np.sin(ang)*K+(1-np.cos(ang))*(K@K)
gens=[]
g1=perm_from_map(rot(P[0],2*np.pi/5))
face=(P[0]+P[1]+P[2])  # may not be a face; search a valid C3
g2=None
for tri in it.combinations(range(12),3):
    c=P[list(tri)].sum(0)
    if np.linalg.norm(c)<1e-6: continue
    cand=perm_from_map(rot(c,2*np.pi/3))
    if cand: g2=cand; break
assert g1 and g2
group={tuple(range(12))}
frontier=[g1,g2]
while frontier:
    g=frontier.pop()
    if g in group: continue
    group.add(g)
    for h in list(group):
        for comp in (tuple(g[h[i]] for i in range(12)),
                     tuple(h[g[i]] for i in range(12))):
            if comp not in group: frontier.append(comp)
print(f"FACT-G3: rotation group order = {len(group)} (want 60)")
# find order-12 subgroups containing no 5-cycles: elements of order 1,2,3
def order(g):
    x=g; n=1
    while x!=tuple(range(12)): x=tuple(g[x[i]] for i in range(12)); n+=1
    return n
t_elems=[g for g in group if order(g) in (1,2,3)]
print(f"  elements of order 1/2/3 (T-candidates): {len(t_elems)}")
# T = the unique-up-to-conjugacy order-12 subgroup; test transitivity of
# the subgroup generated by one C2 and one C3 that close at order 12
import random
found=None
c2s=[g for g in group if order(g)==2]; c3s=[g for g in group if order(g)==3]
for a in c2s:
    for b in c3s:
        sub={tuple(range(12))}; fr=[a,b]
        while fr and len(sub)<=12:
            g=fr.pop()
            if g in sub: continue
            sub.add(g)
            for h in list(sub):
                for comp in (tuple(g[h[i]] for i in range(12)),
                             tuple(h[g[i]] for i in range(12))):
                    if comp not in sub: fr.append(comp)
        if len(sub)==12:
            found=sub; break
    if found: break
orbs=[]
seen=set()
for i in range(12):
    if i in seen: continue
    orb={g[i] for g in found}
    orbs.append(len(orb)); seen|=orb
print(f"  a tetrahedral-order subgroup T (order 12) acts with orbits "
      f"{sorted(orbs)} on shell 1 -> "
      f"{'SIMPLY TRANSITIVE' if orbs==[12] else 'orbit-split'}")

# FACT-G4: optimal tetrads <-> icosahedron edges <-> the 30-vertex
# d^2 = 2 shell (icosidodecahedron = edge-midpoint directions).
s3 = V[np.isclose(d2, 2.0)]
P3 = s3[:,1:]
edges = [(i,j) for i in range(12) for j in range(i+1,12)
         if np.isclose(np.linalg.norm(P[i]-P[j]), 0.618034, atol=1e-5)]
print(f"FACT-G4: shell-1 icosahedron edge count = {len(edges)} (want 30);"
      f" d^2=2 shell count = {len(s3)} (want 30)")
match = 0
dirs3 = P3/np.linalg.norm(P3,axis=1,keepdims=True)
for (i,j) in edges:
    m = (P[i]+P[j]); m = m/np.linalg.norm(m)
    if np.max(dirs3 @ m) > 1-1e-9: match += 1
print(f"  edge-midpoint directions matching d^2=2 shell directions: "
      f"{match}/30 -> {'BIJECTION CONFIRMED' if match==30 else 'NO'}")
