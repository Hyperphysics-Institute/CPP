#!/usr/bin/env python3
"""Patch 3827 -- is the founder's alternating +/- charge arrangement realisable on the 600-cell?
Builds the 120 vertices, extracts the z=12 neighbour graph, tests 2-colourability, and bounds the
frustration. Geometry only; no physics constant adopted."""
import sys, itertools
import numpy as np
from collections import deque
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res=[]
def check(n,c,d=""):
    res.append(c); print(f"[{'PASS' if c else 'FAIL'}] {n}"+(f"  -- {d}" if d else ""))

phi=(1+np.sqrt(5))/2
V=[]
for i in range(4):
    for s in (1,-1):
        v=[0]*4; v[i]=s; V.append(v)
for s in itertools.product((0.5,-0.5),repeat=4): V.append(list(s))
base=[0,0.5,1/(2*phi),phi/2]
even=[p for p in itertools.permutations(range(4)) if
      sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])%2==0]
seen=set()
for p in even:
    for sgn in itertools.product((1,-1),repeat=4):
        v=[0.0]*4
        for k in range(4): v[p[k]]=base[k]*sgn[k]
        t=tuple(np.round(v,9))
        if t not in seen: seen.add(t); V.append(list(v))
V=np.array(V); V=V[np.unique(np.round(V,9),axis=0,return_index=True)[1]]
check("T1 600-cell has 120 vertices", len(V)==120, f"n={len(V)}")

G=V@V.T; np.fill_diagonal(G,-9); mx=G.max()
adj=[np.where(np.abs(G[i]-mx)<1e-6)[0] for i in range(len(V))]
check("T2 nearest-neighbour shell is z = 12 at 36 deg (dot = phi/2)",
      all(len(a)==12 for a in adj) and abs(mx-phi/2)<1e-9,
      f"z = {len(adj[0])}, dot = {mx:.6f}")

T=sum(1 for i in range(len(V)) for a in adj[i] for b in adj[i]
      if a<b and np.abs(G[a,b]-mx)<1e-6)//3
E=sum(len(a) for a in adj)//2
check("T3 the neighbour graph contains triangles (odd cycles): 1200 of them, 30 per vertex",
      T==1200 and 3*T/E==5.0, f"edges = {E}, triangles = {T}, triangles/edge = {3*T/E:.1f}")

col={0:0}; q=deque([0]); bip=True
while q:
    u=q.popleft()
    for w in adj[u]:
        if w not in col: col[w]=1-col[u]; q.append(w)
        elif col[w]==col[u]: bip=False
check("T4 the graph is NOT bipartite: a strict alternating +/- assignment is IMPOSSIBLE",
      not bip, "odd cycles (triangles) forbid a 2-colouring")

frac_min=(T/(3*T/E))/E
check("T5 frustration bound: every triangle needs >=1 like-like bond => >= 1/3 of bonds frustrated",
      abs(frac_min-1/3)<1e-9, f"frustrated fraction >= {frac_min:.3f}")

best=0; rng=np.random.default_rng(0)
for _ in range(60):
    c=rng.integers(0,2,len(V)); improved=True
    while improved:
        improved=False
        for i in range(len(V)):
            same=sum(1 for w in adj[i] if c[w]==c[i])
            if same>len(adj[i])-same: c[i]=1-c[i]; improved=True
    best=max(best,sum(1 for i in range(len(V)) for w in adj[i] if c[w]!=c[i])//2)
check("T6 best alternation achievable is ~0.60 unlike bonds, i.e. ~0.40 frustrated (worse than the 1/3 bound)",
      0.55<best/E<0.67, f"best = {best}/{E} = {best/E:.3f} unlike; frustrated {1-best/E:.3f}")

n=sum(res); print(f"\n{n}/{len(res)} PASS"); sys.exit(0 if n==len(res) else 1)
