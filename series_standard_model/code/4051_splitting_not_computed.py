#!/usr/bin/env python3
# 4051 - 4050 named the remaining step: compute the splitting of the two bracelet
# helicity states in a chiral environment. Attempted. NOT ACHIEVED. Two functionals,
# two failures, both caught by controls, and the likely reason connects to 4044.
import numpy as np, math, itertools as it
from itertools import permutations as P
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
V=build600(); N=len(V)
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
Th=np.diag([1.,1,1,-1])
sd=np.array([0.31,0.57,0.23,1.77]); sd/=np.linalg.norm(sd)
S=orbit4(sd*1.9); ACH=orbit4(np.array([1.,0,0,0])*1.9)
kS={tuple(np.round(v,7)) for v in S}; kA={tuple(np.round(v,7)) for v in ACH}

print("T1 -- A CHIRAL 4D SHELL, BUILT AND VERIFIED")
chk(f"left-icosian orbit of a generic 4D point: {len(S)} points", len(S)==120)
chk("Theta does NOT map it to itself -> CHIRAL",
    not all(tuple(np.round(Th@v,7)) in kS for v in S))
chk(f"and the special-position control ({len(ACH)} points) IS Theta-invariant",
    all(tuple(np.round(Th@v,7)) in kA for v in ACH),
    "so the two shells differ in exactly the property under test")

D=np.array([[np.linalg.norm(V[i]-V[j]) for j in range(N)] for i in range(N)])
Aj=(np.abs(D-e)<1e-9); nb=[set(np.flatnonzero(Aj[i]).tolist()) for i in range(N)]
cyc=[]
def walk(p):
    if len(p)==6:
        if p[0] in nb[p[-1]] and not any(b in nb[a] and abs(p.index(a)-p.index(b)) not in (1,5)
                                          for a,b in it.combinations(p,2)): cyc.append(tuple(p))
        return
    for x in nb[p[-1]]:
        if x in p or (len(p)>=2 and x<p[1]): continue
        walk(p+(x,))
for a in sorted(nb[0]): walk((0,a))
EPS=np.zeros((4,4,4,4))
for q in it.permutations(range(4)): EPS[q]=np.sign(np.linalg.det(np.eye(4)[list(q)]))
nhat=V[0]/np.linalg.norm(V[0])
def rd(idx):
    C=np.array([V[i] for i in idx]); c=C.mean(0); Cc=C-c
    L=np.zeros((4,4))
    for i in range(6):
        a,b=Cc[i],Cc[(i+1)%6]; L+=np.outer(a,b)-np.outer(b,a)
    return L,c
def hel(L,c): return float(np.einsum('ijkl,ij,k,l->',EPS,L,c,nhat))
def env(L,c,SH,lam=1.5):
    d=SH-c; w=np.exp(-np.linalg.norm(d,axis=1)/lam)
    return float(np.einsum('ijkl,ij,nk,l,n->',EPS,L,d,nhat,w))
H=np.array([hel(*rd(i)) for i in cyc]); m=np.abs(H)>1e-9

print("\nT2 -- FUNCTIONAL 1 FAILS, AND THE CONTROL IS WHAT CAUGHT IT")
e1=np.array([env(*rd(i),S) for i in cyc]); e0=np.array([env(*rd(i),ACH) for i in cyc])
c1=float(np.mean(np.sign(H[m])*e1[m])); c0=float(np.mean(np.sign(H[m])*e0[m]))
print(f"    <sign(h)*E>  chiral shell {c1:+.6e}   ACHIRAL control {c0:+.6e}")
chk("the achiral control gives the SAME value to five digits", abs(c1-c0)/abs(c1)<1e-4,
    "so the functional is not measuring the shell at all -- it is dominated by the "
    "ring's OWN helicity, since d = s - c carries a term proportional to -helicity")

print("\nT3 -- FUNCTIONAL 2 FAILS TOO, AND THE MIRROR IS WHAT CAUGHT IT")
Sm=S.copy(); Sm[:,3]*=-1
d1=np.array([env(*rd(i),S)-env(*rd(i),ACH) for i in cyc])
d2=np.array([env(*rd(i),Sm)-env(*rd(i),ACH) for i in cyc])
r1=float(np.mean(np.sign(H[m])*d1[m])); r2=float(np.mean(np.sign(H[m])*d2[m]))
print(f"    differenced:  chiral {r1:+.6e}   MIRRORED chiral {r2:+.6e}")
chk("the mirrored shell gives the SAME sign, not the opposite", r1*r2>0,
    "a residual that is the shell's CHIRALITY must flip under mirroring. This does not, "
    "so it is a P-EVEN difference between a generic-position and a special-position "
    "orbit -- not the quantity wanted")

print("\nT4 -- SO THE SPLITTING IS NOT COMPUTED, AND I SHOULD SAY SO PLAINLY")
chk("two functionals, two failures, both caught by controls rather than by inspection",
    True,
    "third and fourth time today a control has caught a result that looked clean. The "
    "controls are doing more work than the measurements")
print("  LIKELY REASON, offered as a hypothesis with its evidence:")
print("    Summing a P-odd quantity over a GROUP ORBIT gives a group invariant, and for")
print("    icosahedral symmetry the first ODD invariant is degree 15 (4044). So the")
print("    splitting may be suppressed for exactly the reason the parity-odd dispersion")
print("    was -- and if so, no low-order functional of this shape will ever see it.")
chk("that is a hypothesis, not a finding", True,
    "it is consistent with both failures and with 4044, and it is NOT tested. What IS "
    "established is that neither functional tried here measures the splitting")
chk("and this is where the lane's tools stop reaching", True,
    "two consecutive patches whose computation did not land. The mechanism sketch of "
    "4050 stands in FORM -- two P-odd binary states, exactly degenerate, degeneracy "
    "removable by a chiral substrate -- and its MAGNITUDE is not accessible by the "
    "means available here")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands. Nothing derived.")
raise SystemExit(1 if fails else 0)
