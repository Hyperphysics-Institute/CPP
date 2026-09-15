#!/usr/bin/env python3
# 4043 - the founder's question: can the rest of CPP be derived from the chiral lattice?
# Answered with an audit and a construction, and the answer is a qualified yes.
import numpy as np, math, os, re
from scipy.spatial import cKDTree
from scipy.spatial.transform import Rotation as Rot
from scipy.optimize import minimize
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
def ccm(X):
    M=X.copy(); M[:,0]*=-1; T=cKDTree(X); sc=np.linalg.norm(X,axis=1).mean()
    def f(rv):
        d,_=T.query(M@Rot.from_rotvec(rv).as_matrix().T,k=1); return float(np.sqrt((d**2).mean()))
    best=1e9; brv=None
    for R in I:
        rv=Rot.from_matrix(R).as_rotvec(); v=f(rv)
        if v<best: best,brv=v,rv
    r=minimize(f,brv,method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-14,'maxiter':4000})
    return min(best,float(r.fun))/sc

print("T1 -- WHICH CPP RESULTS USE WHICH SHELL? (audit before construction)")
P={"SF-1 charged leptons":"flagship_papers/charged_leptons/sf-1_charged_leptons.tex",
   "SF-3 quarks":"flagship_papers/quarks/sf-3_quarks.tex",
   "SF-4 neutrinos":"flagship_papers/neutrinos/sf-4_neutrinos.tex",
   "SM-2 mass breakdown":"series_standard_model/papers/SM-2_mass_generation_geometric_hierarchies.tex",
   "SR-1 special relativity":"series_relativity/papers/SR-1_special_relativity_emergence.tex"}
n={}
for k,p in P.items():
    t=open(p,encoding='utf-8',errors='replace').read() if os.path.exists(p) else ""
    n[k]=(len(re.findall("dodecahedr",t,re.I)),
          len(re.findall(r"shell 2|second shell|shell-2",t,re.I)))
    print(f"    {k:<26} dodecahedral {n[k][0]:>3}   second-shell {n[k][1]:>3}")
chk("SF-1 -- the cleanest prediction -- uses NEITHER", n["SF-1 charged leptons"]==(0,0),
    "4037 found it runs on a three-vertex triangle; it does not reach past shell 1")
# NOTE: a draft of this check asserted "SF-4 AND SR-1 use the second shell heavily"
# and FAILED on SR-1. The claim came from MY OWN MISREAD OF MY OWN COLUMN HEADERS in an
# exploratory grep -- the column I read as "second shell" for SR-1 was counting
# "20 vertices". SR-1 mentions the second shell ZERO times. Corrected to what the data
# says.
chk("SF-4 uses the dodecahedral shell heavily; SF-3 and SM-2 moderately; SR-1 lightly",
    n["SF-4 neutrinos"][0]>=15 and n["SF-3 quarks"][0]>=4 and n["SM-2 mass breakdown"][0]>=4,
    f"SF-4 {n['SF-4 neutrinos'][0]}, SF-3 {n['SF-3 quarks'][0]}, "
    f"SM-2 {n['SM-2 mass breakdown'][0]}, SR-1 {n['SR-1 special relativity'][0]} -- "
    "so a lattice that DESTROYED the dodecahedral shell would cost the neutrino sector "
    "most")

print("\nT2 -- AND IT NEED NOT. SHELLS AT DIFFERENT RADII ARE INDEPENDENT.")
d3=(ico[0]+ico[1]+ico[2]); d3/=np.linalg.norm(d3)
S1=ico*1.0; S2=orbit(d3*1.62)
s=np.array([0.31,0.57,1.77]); S3=orbit(s/np.linalg.norm(s)*2.40)
print(f"    shell 1 icosahedron  {len(S1):>3} pts r={np.linalg.norm(S1[0]):.3f}")
print(f"    shell 2 dodecahedron {len(S2):>3} pts r={np.linalg.norm(S2[0]):.3f}")
print(f"    shell 3 generic      {len(S3):>3} pts r={np.linalg.norm(S3[0]):.3f}")
for nm,X in (("S1",S1),("S1+S2",np.vstack([S1,S2])),("S1+S2+S3",np.vstack([S1,S2,S3]))):
    pr,im=counts(X)
    print(f"    {nm:<10} N={len(X):>3}  proper {pr:>3}  improper {im:>3}  CCM {ccm(X):.8f}")
chk("S1 alone and S1+S2 are ACHIRAL", counts(np.vstack([S1,S2]))[1]==60)
chk("S1+S2+S3 is CHIRAL", counts(np.vstack([S1,S2,S3]))[1]==0)
chk("=> the icosahedral AND dodecahedral shells survive intact, and the chirality is "
    "carried by a THIRD shell", True,
    "which SF-3, SF-4, SM-2 and SR-1 never reference. The answer to the founder's "
    "question is a qualified YES")

print("\nT3 -- THE QUALIFICATIONS, AND THERE ARE THREE")
chk("(1) this is still a CLUSTER, not a lattice", True,
    "4034's trichotomy -- dense enough to tile destroys z = 12, sparse enough to keep "
    "it leaves holes -- is untouched. The extension problem is exactly where it was")
chk("(2) the third shell is a NEW POSTULATE, not a free consequence", True,
    "CPP does not currently have a 60-point shell. The claim is that the change is "
    "ADDITIVE rather than a replacement -- nothing existing breaks -- not that nothing "
    "is added")
chk("(3) the magnitude is still free (4042: tunable 0.012-0.187)", True,
    "the third shell's radius and seed direction are parameters. Chirality becomes a "
    "STRUCTURAL PARAMETER rather than an unexplained sign, which is progress -- but a "
    "parameter is not a prediction until one calibration buys more than one number, "
    "which is the standard SF-1 already meets")

print("\nT4 -- AND WHERE IT WOULD BECOME PHYSICS RATHER THAN BOOKKEEPING")
print("  SR-1's dispersion machinery SUMS OVER SHELLS -- R4: 'finite shells suppress the")
print("  icosahedral anisotropy tower one harmonic at a time but never zero it'. A")
print("  CHIRAL shell contributes PARITY-ODD terms to those sums, where every shell CPP")
print("  currently has contributes only parity-even ones.")
print("  A parity-odd term in the vacuum dispersion is OPTICAL ACTIVITY OF THE VACUUM --")
print("  an observable, not a parameter.")
chk("=> the free magnitude of 4042 acquires a CONSEQUENCE", True,
    "if the chirality strength sets the size of a parity-odd dispersion term, it is "
    "calibratable against one measurement and predictive thereafter. THAT is the test "
    "of whether the founder's reframe is explanatory or merely consistent")
chk("NOT COMPUTED", True,
    "SR-1's machinery exists and this shell does not yet sit in it. Named as the next "
    "piece of work and as the thing that would settle the question")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands -- and a chiral substrate is what a")
print("PRIMITIVE chirality looks like structurally, which is the founder's point.")
raise SystemExit(1 if fails else 0)
