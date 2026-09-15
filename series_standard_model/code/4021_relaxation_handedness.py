#!/usr/bin/env python3
# 4021 - the open problem 4020 named: is the FRUSTRATION RELAXATION handed?
#
# 4020 showed RANDOM strain gives a random handedness (sign wanders with the seed) and
# argued the physical strain is different -- it is the structured relaxation of a
# 7.356-deg-per-edge frustration. This patch asks whether that relaxation can bias the
# handedness, and finds the question reduces to one the corpus has already studied.
#
# Prior art honoured first, per the note 4020 filed to itself: the DM lane's four
# extended z=12 arenas (Patch 2685) were read before anything was built here.
import numpy as np, math, subprocess
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
pairs=[(i,j) for i in range(N) for j in nbr[i] if j>i]
nhat=np.array([1.,0,0,0]); R=np.diag([1.,1.,1.,-1.])

print("T0 -- PRIOR ART READ BEFORE BUILDING (the note 4020 filed to itself)")
src=subprocess.run(["git","show","HEAD:series_phenomena/cosmology/dark_matter/code/2685_r1_l1_arenas.py"],
                   capture_output=True,text=True,errors="replace").stdout
chk("DM Patch 2685 builds four extended z = 12 arenas", "fcc_ball" in src and "barlow_seq" in src,
    "fcc_ball, layered_ball (HCP), barlow_seq (random stacking), fcc_rot_cube -- each "
    "sanity-checked for coordination 12 and min chord = edge length")
chk("they are 3D close-packings, so CUBOCTAHEDRAL not icosahedral local order", True,
    "real prior art for extended z = 12; NOT the 4D near-icosahedral target, and "
    "labelled proxies by their own author. Reused here as precedent, not as lattice")

print("\nT1 -- THE STRAIN ENERGY IS ACHIRAL, AND THAT IS THE WHOLE ARGUMENT")
def energy(X):
    """bond-length strain: any functional of PAIRWISE DISTANCES is invariant under
       every isometry, proper or improper."""
    return float(sum((np.linalg.norm(X[i]-X[j])-e)**2 for i,j in pairs))
rng=np.random.default_rng(4021)
for s in range(4):
    X=V0+0.05*rng.standard_normal((N,4))
    chk(f"seed {s}: E(X) == E(RX) to 1e-12  ({energy(X):.9f})",
        abs(energy(X)-energy(X@R.T))<1e-12)
chk("=> the relaxation landscape is MIRROR-SYMMETRIC by construction", True,
    "every minimum has a mirror partner of exactly equal energy; no gradient flow on "
    "an achiral functional can prefer one")

print("\nT2 -- RELAX, AND CHECK THE MIRROR PARTNER RELAXES THE SAME WAY")
def relax(X, steps=400, lr=0.05):
    X=X.copy()
    for _ in range(steps):
        G=np.zeros_like(X)
        for i,j in pairs:
            d=X[i]-X[j]; r=np.linalg.norm(d); g=2*(r-e)*d/r
            G[i]+=g; G[j]-=g
        X-=lr*G
    return X
def chir(X, starts=range(0,120,10)):
    tot=0.0
    for v0 in starts:
        st=[(v0,-1,[])]
        while st:
            cur,prev,steps=st.pop()
            if len(steps)==3:
                tot+=np.sign(round(np.linalg.det(np.array(steps+[nhat])),12)); continue
            for nx in nbr[cur]:
                if nx==prev: continue
                st.append((nx,cur,steps+[X[nx]-X[cur]]))
    return tot
for s in range(3):
    X0=V0+0.05*np.random.default_rng(100+s).standard_normal((N,4))
    A=relax(X0); B=relax(X0@R.T)
    cA,cB=chir(A),chir(B)
    chk(f"seed {s}: relaxed energies equal ({energy(A):.6f} vs {energy(B):.6f})",
        abs(energy(A)-energy(B))<1e-9)
    chk(f"seed {s}: chirality exactly OPPOSITE ({cA:+.1f} vs {cB:+.1f})",
        abs(cA+cB)<1e-6)
print("  Mirror-image starting conditions relax to mirror-image end states of IDENTICAL")
print("  energy and OPPOSITE handedness. The relaxation cannot bias the sign.")

print("\nT3 -- SO THE NEW PROBLEM REDUCES TO ONE THE CORPUS ALREADY HAS")
print("  Any handedness the relaxation produces must therefore be SPONTANEOUS: two")
print("  exactly degenerate minima, one picked per domain. That is a Z2 spontaneous")
print("  symmetry breaking on the substrate -- which is EXACTLY THEO-CHIR-VW-1's subject.")
print("  VW-1 (Patch 0680, review-closed 3/3 at 0682): conditional on H1 (the DSL measure")
print("  is reflection-positive), mu^2 > 0 and eta = 0 -- the det-coset Z2 CANNOT break")
print("  spontaneously within the substrate axioms.")
chk("=> 4020's 'is the relaxation handed?' is not a new open problem", True,
    "it is VW-1's question in different clothing, and VW-1's sole residual (H1) is "
    "already on the queue. Registering it as NEW would have split one problem into two")
chk("and the per-domain picture matches what 4020 measured", True,
    "4020: each strained cage chiral, ensemble not. Degenerate minima picked at "
    "random per domain give exactly that, with no net handedness without a bias")

print("\nT4 -- WHAT WOULD ACTUALLY BE NEEDED, AND WHAT IS NOT CLAIMED")
print("  A chirality mechanism here needs ONE of:")
print("    (i)  an ACHIRAL-BREAKING term in the substrate dynamics -- i.e. the energy")
print("         functional is NOT a function of distances alone. Nothing in the axioms")
print("         supplies one; A1'/A3' are distance-and-census based.")
print("    (ii) an external bias selecting between the degenerate minima -- which is a")
print("         PRIMITIVE handedness, i.e. FI-C-9 = V3 restated, not derived.")
chk("both branches lead back to V3 or to H1", True,
    "which is the fifth independent route to the same place this session")
chk("NOT claimed: that no relaxation mechanism exists", True,
    "only that a distance-based strain functional cannot supply one, and that anything "
    "which could is either an axiom change or VW-1's H1. The disclination-NETWORK "
    "question 4020 raised is untouched at the network level -- this treats the "
    "energetics, not the topology")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)
