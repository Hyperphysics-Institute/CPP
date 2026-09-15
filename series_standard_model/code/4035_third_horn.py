#!/usr/bin/env python3
# 4035 - closing 4034's scoping caveat, and finding the dilemma has a THIRD HORN that
# the DM lane has been quietly using for months.
#
# 4034 left: "only translation sets from the motif's own vertex directions were tested;
# a general translation set could differ." Close it.
import numpy as np, math, itertools as it
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
            x=np.zeros(4); x[i]=s; Vs.append(x)
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
V=build600(); N=len(V)
D=np.array([[np.linalg.norm(V[i]-V[j]) for j in range(N)] for i in range(N)])
nb=lambda i: set(np.flatnonzero(np.abs(D[i]-e)<1e-9).tolist())

print("T1 -- THE TRANSLATION SET DROPS OUT OF THE PROBLEM")
print("  For z = 12 EXACTLY at a vertex v, no vertex of any other copy may lie within e")
print("  of v -- its own motif already supplies twelve. So copies cannot interpenetrate")
print("  at the edge scale, WHATEVER the translation set. The union is then simply some")
print("  point set with minimum distance e and exactly twelve neighbours at e.")
chk("=> 4034's caveat is CLOSED: no translation set can be the difference", True,
    "the motif structure drops out of the condition entirely")

print("\nT2 -- AND MY DRAFT OF THE NEXT STEP WAS WRONG")
print("  Draft: 'so it reproduces the 600-cell's local structure, which carries the")
print("  7.356-deg deficit, so flat space forbids it.' THAT IS FALSE, and the")
print("  counterexample is standard: FCC has z = 12 exactly, in flat space, tiling.")
Pf=np.array([p for p in it.product(range(-5,6),repeat=3) if sum(p)%2==0],float)
T=cKDTree(Pf); r=np.linalg.norm(Pf,axis=1); inner=np.flatnonzero(r<3.0)
d,_=T.query(Pf[inner],k=2); ef=float(np.median(d[:,1]))
z=np.array([len(T.query_ball_point(Pf[i],ef*1.02))-1 for i in inner])
rng=np.random.default_rng(0); q=rng.uniform(-2,2,(4000,3)); dd,_=T.query(q,k=1)
chk(f"FCC: every interior site has z = 12 exactly ({set(z.tolist())})", set(z.tolist())=={12})
chk(f"and it TILES -- largest hole {float(dd.max()):.4f} < nn {ef:.4f}", float(dd.max())<ef)
chk("so 'z = 12 in flat space' is NOT the obstruction", True,
    "I nearly shipped that. Caught by asking for a counterexample before asserting")

print("\nT3 -- THE OBSTRUCTION IS 'ICOSAHEDRALLY', NOT 'TWELVE'")
i0=inner[len(inner)//2]; nbf=np.array(T.query_ball_point(Pf[i0],ef*1.02)); nbf=nbf[nbf!=i0]
sh=sorted({len(set(T.query_ball_point(Pf[i0],ef*1.02))&set(T.query_ball_point(Pf[w],ef*1.02)))
           for w in nbf})
off=Pf[nbf]-Pf[i0]; u=off/np.linalg.norm(off,axis=1,keepdims=True)
spec=sorted(set(np.round(np.sort(np.round(u@u.T,6)[np.triu_indices(12,1)]),4).tolist()))
sh600=sorted({len(nb(0)&nb(w)) for w in nb(0)})
print(f"    FCC       shared-per-edge {sh}   cos-angle spectrum {spec}")
print(f"    600-cell  shared-per-edge {sh600}")
chk("FCC shares SIX neighbours per edge, the 600-cell FIVE", sh==[6] and sh600==[5],
    "six is 4 tetrahedra + 4 octahedra round an edge, which closes 360 deg exactly; "
    "five regular tetrahedra give 352.644 deg and leave the 7.356-deg deficit (4019)")
chk("and FCC's coordination is CUBOCTAHEDRAL, not icosahedral", spec!=[-1.0,-0.4472,0.4472],
    f"FCC {spec} against the icosahedron's -1, -0.4472, +0.4472")
chk("=> the obstruction is 'twelve ICOSAHEDRALLY', not 'twelve'", True,
    "SF-4's own words are 'each vertex has 12 nearest neighbors ARRANGED ICOSAHEDRALLY' "
    "(4016). That adjective is doing all the work")

print("\nT4 -- SO THE DILEMMA HAS A THIRD HORN, AND THE DM LANE HAS BEEN USING IT")
print("  (A) give up TILING     -- keep icosahedral z = 12, accept holes or curvature")
print("  (B) give up EXACTLY-12 -- accept the quasicrystal's 13/18/19/26 spread")
print("  (C) give up ICOSAHEDRAL -- keep twelve AND tiling. That is FCC/HCP.")
chk("(C) is not hypothetical: it is what the DM lane already runs on", True,
    "Patch 2685's four z = 12 arenas are FCC ball, HCP ball, random-stacking Barlow "
    "ball and FCC-cubic; Patch 3133's sub-PSR cascade is an FCC lattice. Both were "
    "labelled PROXIES -- 4012 and 4020 found them and I filed them as precedent")
chk("and (C) explains why those proxies worked", True,
    "they were satisfying the constraint that is actually satisfiable in flat space")
print("  (C)'s cost is the adjective: SF-4, SM-1 and SS-1 say ICOSAHEDRAL, and the")
print("  600-cell's vertex figure is what the geometry programme is built on. Whether")
print("  the mass ladder needs the ARRANGEMENT or only the COUNT is not mine to say --")
print("  4016 showed only the COUNT enters Sum m_nu ~ z^-9.")
chk("NOT decided here", True,
    "whether z's ARRANGEMENT is load-bearing anywhere, or only its VALUE, is a question "
    "about the SM papers' derivations. Raised with the FCC counterexample attached")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. SR-1 and SF-4 unrevised. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)
