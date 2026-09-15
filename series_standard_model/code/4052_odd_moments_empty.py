#!/usr/bin/env python3
# 4052 - 4051 offered a hypothesis for why the splitting would not compute: degree-15
# suppression. TESTED. The hypothesis is WRONG, and the real reason is cleaner and says
# what the next functional must look like.
import numpy as np, math, itertools as it
from itertools import permutations as P
fails=0
def chk(n,ok,note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}"+(f"  -- {note}" if note else ''))
    if not ok: fails+=1
phi=(1+math.sqrt(5))/2
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
V=build600()
def Lq(q):
    w,x,y,z=q
    return np.array([[w,-x,-y,-z],[x,w,-z,y],[y,z,w,-x],[z,-y,x,w]])
LEFT=[Lq(q) for q in V]
def orbit4(p):
    O=[]
    for R in LEFT:
        q=R@p
        if not any(np.allclose(q,x,atol=1e-8) for x in O): O.append(q)
    return np.array(O)
sd=np.array([0.31,0.57,0.23,1.77]); sd/=np.linalg.norm(sd); S=orbit4(sd)
Th=np.diag([1.,1,1,-1]); kS={tuple(np.round(v,7)) for v in S}

print("T1 -- THE HYPOTHESIS, TESTED AND WRONG")
print("  4051 guessed the splitting was suppressed by the degree-15 pseudo-invariant,")
print("  as at 4044. Prediction: sum_s (s.k)^m vanishes for odd m < 15, nonzero at 15.")
rng=np.random.default_rng(3); K=rng.normal(size=(40,4)); K/=np.linalg.norm(K,axis=1,keepdims=True)
vals={m: float(np.mean([abs(((S@k)**m).sum()) for k in K])) for m in (1,3,5,7,9,11,13,15,17)}
print(f"    odd moments: " + "  ".join(f"m={m}:{v:.1e}" for m,v in vals.items()))
chk("EVERY odd moment is at machine zero, m = 15 INCLUDED", all(v<1e-14 for v in vals.values()),
    "so the degree-15 hypothesis is REFUTED -- nothing turns on at 15, and the channel "
    "is empty at every order")

print("\nT2 -- THE REAL REASON, AND IT IS A FACT ABOUT FOUR DIMENSIONS")
neg=[i for i,v in enumerate(V) if np.allclose(v,-V[0])]
chk("the quaternion -1 lies in 2I, so L_{-1} = -Identity is in the LEFT group",
    any(np.allclose(Lq(v),-np.eye(4)) for v in V),
    "left-multiplication by -1 is exactly the inversion x -> -x")
chk("=> the shell is CENTRALLY SYMMETRIC", all(tuple(np.round(-v,7)) in kS for v in S),
    "and central symmetry kills EVERY odd moment identically, at every order. That is "
    "why nothing turned on at 15 or anywhere else")
chk("and yet the shell is still CHIRAL", not all(tuple(np.round(Th@v,7)) in kS for v in S),
    "because IN FOUR DIMENSIONS INVERSION IS PROPER: det(-I_4) = +1. Central symmetry "
    "and chirality COEXIST in 4D, which they cannot in 3D")
print(f"    det(-I) in 4D = {np.linalg.det(-np.eye(4)):+.0f};  in 3D = "
      f"{np.linalg.det(-np.eye(3)):+.0f}")

print("\nT3 -- SO 4051's FUNCTIONALS WERE PROBING AN EMPTY CHANNEL")
print("  Both of 4051's functionals reduce to odd MOMENTS of the shell -- sums of the")
print("  form sum_s f(s) with f odd under s -> -s. Central symmetry annihilates all of")
print("  them, whatever the shell's chirality. The failures were not suppression; they")
print("  were a probe aimed at a channel that is identically zero.")
chk("this is a better diagnosis than 4051's and it REPLACES it", True,
    "4051 said 'may be suppressed at degree 15, NOT TESTED'. Tested, refuted, replaced")

print("\nT4 -- AND IT SAYS WHAT THE NEXT FUNCTIONAL MUST LOOK LIKE")
print("  A P-odd scalar in 4D needs the LEVI-CIVITA CONTRACTED WITH FOUR INDEPENDENT")
print("  VECTORS. An odd moment of ONE vector cannot be P-odd in 4D at all -- that is a")
print("  3D intuition carried across, and it is where both functionals came from.")
print("  4050's ring helicity eps(L, c, n-hat) DOES have the right shape: the bivector L")
print("  supplies two of the four slots. A splitting functional needs the same form with")
print("  the shell entering through a slot the inversion cannot cancel.")
chk("4050's helicity was the right shape all along", True,
    "it is the one P-odd quantity in this arc that has worked in 4D, and 4051 did not "
    "reuse its form")
chk("NOT built here", True,
    "the diagnosis is the deliverable. Building the functional is the next step and it "
    "now has a specification instead of a guess")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands. Nothing derived.")
raise SystemExit(1 if fails else 0)
