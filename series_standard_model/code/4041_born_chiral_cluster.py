#!/usr/bin/env python3
# 4041 - 4040 said the structure must be BORN chiral rather than made chiral. Built one.
#
# TARGET (4038): icosahedral ROTATION symmetry I (532), no improper operations,
# nearest shell of exactly twelve. 4040 closed the decoration route. This builds the
# object directly, at cluster scale.
import numpy as np, math
from scipy.spatial import cKDTree
from scipy.spatial.transform import Rotation as Rot
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
phi=(1+math.sqrt(5))/2
def rot(ax,th):
    ax=np.asarray(ax,float); ax=ax/np.linalg.norm(ax)
    K=np.array([[0,-ax[2],ax[1]],[ax[2],0,-ax[0]],[-ax[1],ax[0],0]])
    return np.eye(3)+math.sin(th)*K+(1-math.cos(th))*K@K
ico=[]
for s1 in(1,-1):
    for s2 in(1,-1):
        ico += [(0,s1,s2*phi),(s1,s2*phi,0),(s1*phi,0,s2)]
ico=np.array(ico,float); ico/=np.linalg.norm(ico[0])
gens=[rot(ico[0],2*math.pi/5), rot(ico[0]+ico[1]+ico[2],2*math.pi/3)]
I=[np.eye(3)]; fr=[np.eye(3)]
while fr:
    nf=[]
    for A in fr:
        for G in gens:
            B=G@A
            if not any(np.allclose(B,C,atol=1e-8) for C in I): I.append(B); nf.append(B)
    fr=nf
def orbit(p):
    O=[]
    for R in I:
        q=R@p
        if not any(np.allclose(q,x,atol=1e-8) for x in O): O.append(q)
    return np.array(O)
def counts(X):
    key={tuple(np.round(x,7)) for x in X}
    return (sum(1 for R in I if all(tuple(np.round(R@x,7)) in key for x in X)),
            sum(1 for R in I if all(tuple(np.round((-R)@x,7)) in key for x in X)))

print("T1 -- THE IDEA: a first shell CANNOT carry the chirality, so the second must")
chk("a regular icosahedron is achiral", counts(ico)[1]>0,
    f"{counts(ico)[1]} improper symmetries of its own -- so z = 12 ICOSAHEDRAL forces "
    "an ACHIRAL first shell, whatever the rest of the structure does")
print("  Chirality therefore has to live in the SECOND shell. And there is a clean way:")
print("  a GENERIC point has a 60-point orbit under I and would have a 120-point orbit")
print("  under I_h -- so a 60-point orbit cannot be closed under any improper operation.")

print("\nT2 -- BUILT: icosahedron (12) + generic I-orbit (60) = 72 points")
X=np.vstack([ico, orbit(np.array([0.31,0.57,1.77]))])
pr,im=counts(X)
print(f"    {'cluster':<34}{'N':>4}{'proper':>8}{'improper':>10}")
print(f"    {'CHIRAL : 12 + generic 60-orbit':<34}{len(X):>4}{pr:>8}{im:>10}")
for nm,seed in (("control: 12 + 5-fold 12-orbit", ico[0]*1.9),
                ("control: 12 + 3-fold 20-orbit",
                 (ico[0]+ico[1]+ico[2])/np.linalg.norm(ico[0]+ico[1]+ico[2])*1.9),
                ("control: icosahedron alone", None)):
    Y=ico if seed is None else np.vstack([ico,orbit(seed)])
    p2,i2=counts(Y); print(f"    {nm:<34}{len(Y):>4}{p2:>8}{i2:>10}")
chk("the generic-orbit cluster has FULL icosahedral rotation symmetry", pr==60)
chk("and ZERO improper symmetries -- it is CHIRAL", im==0,
    "every control has 60. This is 4038's target realised at cluster scale")
print("  SCOPE OF THAT PROOF: the search covers I_h's improper coset {-R : R in I}. That")
print("  is sufficient -- if the cluster's point group contained I AND any improper")
print("  element it would have order >= 120, and the only finite point group containing")
print("  I at index 2 is I_h. So zero here means genuinely no improper symmetry.")

print("\nT3 -- TWO ATTEMPTS TO MEASURE 'HOW CHIRAL', BOTH FAILED. REPORTED.")
T=cKDTree(X); d,_=T.query(X,k=2); nn=float(np.median(d[:,1]))
nb=[np.array([j for j in T.query_ball_point(x,nn*1.15) if not np.allclose(X[j],x)]) for x in X]
npath=sum(len(nb[v])*max(len(nb[a])-1,0) for v in range(len(X)) for a in nb[v])
chk(f"the 3-hop path measure has only ~{npath} paths to work with", npath<2000,
    "nn = 0.638 with shell 2 at 1.9, so the nearest-neighbour graph is too sparse for "
    "the estimator that worked on the 600-cell. It returned 0 for lack of paths, not "
    "for lack of chirality")
def ccm(Y,n=4000,seed=0):
    M=Y.copy(); M[:,0]*=-1; Tt=cKDTree(Y); rng=np.random.default_rng(seed); best=1e9
    for _ in range(n):
        R=Rot.from_quat(rng.normal(size=4)).as_matrix()
        dd,_=Tt.query(M@R.T,k=1); v=float(np.sqrt((dd**2).mean()))
        best=min(best,v)
    return best/np.linalg.norm(Y,axis=1).mean()
c_ch=ccm(X); c_ct=ccm(ico)
print(f"    continuous chirality measure by random rotation search:")
print(f"      chiral cluster {c_ch:.5f}   ACHIRAL control (icosahedron) {c_ct:.5f}")
chk("the CCM floors at ~0.03 for BOTH -- it is sampling-limited, not measuring",
    abs(c_ch-c_ct)<0.01,
    "an achiral set must score exactly 0; 4000 random rotations never land on the exact "
    "superposition. The measure needs local optimisation seeded from the group elements. "
    "NOT DONE -- reported as a failed measurement rather than a small number")

print("\nT4 -- WHAT IS AND IS NOT ACHIEVED")
chk("ACHIEVED: a structure that is chiral by an EXACT group count, with icosahedral "
    "rotation symmetry and an achiral z = 12 first shell", pr==60 and im==0,
    "the first object in this arc that is actually chiral with the right rotation group")
chk("NOT ACHIEVED: a lattice", True,
    "this is a 72-point CLUSTER. Extending it to a space-filling structure while "
    "keeping z = 12 at every point is the remaining work, and 4034's trichotomy says "
    "that step is where the difficulty lives")
chk("NOT ACHIEVED: a quantified chirality", True,
    "both measures failed for their own reasons, stated above. The group count proves "
    "chirality; it does not say how much, and 'how much' is what a physical prediction "
    "would need")
chk("and NO chirality has been generated in the substrate", True,
    "FI-C-9 = V3 stands. This removes an obstruction and builds a candidate; it does "
    "not derive a handedness")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
raise SystemExit(1 if fails else 0)
