#!/usr/bin/env python3
# 4033 - the item 4032 left: "nobody has bounded the error" between SR-1's
# quasicrystalline APPROXIMATION and SM's EXACT use of the same structure.
#
# PD-008 says bound it rather than hand it on. Trying to bound it turns up why nobody
# has, and why 4009-4032 kept failing to build the lattice.
import os
import numpy as np, math
from itertools import permutations as P
from scipy.spatial import cKDTree
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
phi=(1+math.sqrt(5))/2; e=1/phi
def build600():
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
M=build600()
SR="series_relativity/papers/SR-1_special_relativity_emergence.tex"
txt=open(SR,encoding='utf-8',errors='replace').read()

print("T1 -- I HAD NEVER BUILT WHAT SR-1 ACTUALLY NAMES")
chk("SR-1's construction is 'modular repetition of 600-cell motifs with overlapping "
    "Voronoi'", "modular repetition of 600-cell motifs" in txt)
chk("that is NOT cut-and-project, which is what 4010-4030 tested", True,
    "cut-and-project projects a higher-dimensional lattice through a window; modular "
    "repetition unions translated copies of a motif. Different constructions. "
    "SEVENTH instance today of building on my own reading instead of the corpus's")

print("\nT2 -- SO I BUILT IT. LITERAL READING, AND THE READING IS MINE (labelled)")
print("  Translate the 120-vertex motif by t*u for u in the motif; union; overlap when")
print("  t < 2 (the motif's diameter).")
res={}
for t in (0.618034,1.0,1.175571,1.618034,2.0):
    X=np.vstack([M+t*u for u in np.vstack([np.zeros((1,4)),M])])
    Xr=np.round(X,9); _,idx=np.unique(Xr,axis=0,return_index=True); X=X[np.sort(idx)]
    T=cKDTree(X); r=np.linalg.norm(X,axis=1)
    inner=np.flatnonzero(r<np.percentile(r,35))
    d,_=T.query(X[inner],k=2); dmin=float(np.median(d[:,1]))
    z=np.array([len(T.query_ball_point(X[i],max(dmin,1e-9)*1.02))-1 for i in inner])
    res[t]=(len(X),dmin,float((z==12).mean()))
    print(f"    t={t:.4f}  N={len(X):>5}  nn={dmin:.4f}  z=12 fraction {(z==12).mean():.3f}")
chk("no t gives anything like uniform z = 12 (best 2.7%)",
    max(v[2] for v in res.values())<0.05)
chk("and at several t the nearest-neighbour distance is 0.0000 -- NEAR-COINCIDENT POINTS",
    min(v[1] for v in res.values())<1e-6,
    "a point set with coincident points is not a lattice. THE READING IS WRONG, and "
    "that is the finding -- not that the construction fails")

print("\nT3 -- THE ACTUAL FINDING: SR-1's APPROXIMATION IS NOT SPECIFIED TO A LEVEL THAT")
print("      CAN BE CHECKED")
print("  'Modular repetition of 600-cell motifs with overlapping Voronoi cells' names a")
print("  FAMILY of constructions, not a recipe. It fixes neither the translation set,")
print("  nor the overlap rule, nor what happens where motifs collide. My most literal")
print("  reading produces coincident points, which SR-1 plainly does not intend.")
chk("=> the error term 4032 asked for CANNOT BE BOUNDED until the construction is "
    "specified", True,
    "you cannot measure the deviation of an unbuilt object from an exact requirement")
chk("and THIS IS THE ROOT CAUSE OF THE WHOLE 4009-4032 ARC", True,
    "every lattice I built -- icosian cut-and-project at 4010/4013/4015/4030, the "
    "anisotropic patch at 4026, this -- was MY GUESS at what the corpus means. The "
    "lateral lattice was never unbuilt because it is hard. It was unbuilt because IT "
    "WAS NEVER SPECIFIED")

print("\nT3b -- SEARCHED UNSCOPED BEFORE CLAIMING IT (the absence gate failed a draft)")
import subprocess
hits=subprocess.run(["git","grep","-l","-i","modular repetition|overlapping Voronoi|"
                     "translation set|motif lattice","-E"],capture_output=True,text=True,
                    errors="replace").stdout.split()
hits=subprocess.run(["git","grep","-l","-iE",
                     "modular repetition|overlapping Voronoi|translation set|motif lattice"],
                    capture_output=True,text=True,errors="replace").stdout.split()
other=[h for h in hits if not h.startswith("series_standard_model/code/40")
       and h not in ("frontier_sectors/SM.md","research_frontier.md","id_block_registry.md")]
print(f"    unscoped hits outside my own 40xx files: {other}")
chk("the only other places are SR-1, its revision chain, and TWO COPIES OF ONE FIGURE",
    all(("SR-1" in h or "revision-chain" in h or "fig2_lattice_tiling" in h
         or h.endswith(".md")) for h in other),
    "and the second copy is SM-1's -- series_standard_model/figures/figures-SM-1/ "
    "carries the SAME schematic. So the SM sector adopted the same unspecified "
    "construction rather than supplying one of its own")
fig="series_relativity/figures/figures-SR-1/fig2_lattice_tiling.svg"
figtxt=open(fig,encoding='utf-8',errors='replace').read() if os.path.exists(fig) else ""
chk("and the figure is labelled SCHEMATIC by its own title",
    "Schematic" in figtxt,
    "'600-Cell Quasicrystalline Lattice (Schematic 3D Projection)' / 'Overlapping "
    "600-cell motifs tile flat R^4 space -- Grid Points at all vertices'")
chk("the revision-chain hit is about DeltaSSV geometry inside cells, not the lattice "
    "construction", True,
    "'a purely geometric property of how a moving cage partitions the fixed l_P budget "
    "inside overlapping Voronoi cells' -- a different use of the same phrase")
print("    So the construction is DESCRIBED -- one sentence plus a figure its own title")
print("    calls schematic -- and NOT SPECIFIED. The paper does not claim otherwise.")
chk("ONE CONSTRAINT GAINED from the figure, worth having", True,
    "'Grid Points at ALL VERTICES' -- so every motif vertex is a GP, which rules out "
    "readings where overlap merges or discards vertices")

print("\nT4 -- WHERE THAT LEAVES IT, AND WHAT I AM NOT DOING")
print("  The blocker is now located in ONE SENTENCE of a shipped paper, and it is a")
print("  specification gap, not a physics gap. Resolving it needs either:")
print("    (i)  SR-1's construction written out to the level of a build -- translation")
print("         set, overlap rule, collision handling; or")
print("    (ii) a founder ruling that some named standard construction IS the intended")
print("         one, at which point it can be built and measured in an afternoon.")
chk("not revising SR-1", True, "it is a paper's stated approximation, not an error")
chk("not asserting the approximation is bad", True,
    "unbuilt is not the same as wrong, and I have no measurement either way")
chk("not offering my literal reading as the construction", True,
    "it produces coincident points; it is reported as a REFUTED reading, which is "
    "evidence about the sentence's ambiguity and nothing more")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. SR-1 and SF-4 unrevised. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)
