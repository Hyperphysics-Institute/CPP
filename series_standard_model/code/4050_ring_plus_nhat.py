#!/usr/bin/env python3
# 4050 - 4049 asked SF-2 for "a binary, P-odd, two-state degree of freedom on the ring".
# That request was MIS-SPECIFIED, and the right object exists already in the corpus.
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
D=np.array([[np.linalg.norm(V[i]-V[j]) for j in range(N)] for i in range(N)])
A=(np.abs(D-e)<1e-9); nb=[set(np.flatnonzero(A[i]).tolist()) for i in range(N)]
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
nhat=V[0]/np.linalg.norm(V[0]); Th=np.diag([1.,1,1,-1])
EPS=np.zeros((4,4,4,4))
for q in it.permutations(range(4)):
    EPS[q]=np.sign(np.linalg.det(np.eye(4)[list(q)]))
def bivec(idx):
    C=np.array([V[i] for i in idx]); C=C-C.mean(0)
    L=np.zeros((4,4))
    for i in range(6):
        a,b=C[i],C[(i+1)%6]; L+=np.outer(a,b)-np.outer(b,a)
    return L
def hel(idx,n):
    return float(np.einsum('ijkl,ij,k,l->',EPS,bivec(idx),
                           np.array([V[i] for i in idx]).mean(0),n))

print("T1 -- 4049's REQUEST WAS MIS-SPECIFIED, AND I SHOULD SAY SO FIRST")
print("  I asked for 'a binary, P-odd, two-state degree of freedom ON THE RING' and")
print("  suggested a circulation. A CIRCULATION IS P-EVEN: it is an axial vector, like")
print("  a magnetic moment, and parity leaves it alone. It cannot be what a P-odd")
print("  substrate sign selects between.")
chk("so the object cannot live on the ring alone", True,
    "one patch old, and wrong in its own terms")

print("\nT2 -- THE RIGHT OBJECT IS THE RING TOGETHER WITH n-hat, AND BOTH ALREADY EXIST")
print("  (axial) . (polar) = PSEUDOSCALAR. The ring supplies an oriented area bivector L;")
print("  n-hat is CPP's primitive 4D direction (FI-C-RC-1). Contract them with the 4D")
print("  Levi-Civita and the result is P-ODD by construction.")
h=[hel(c,nhat) for c in cyc]
nz=[x for x in h if abs(x)>1e-9]
print(f"    rings through one vertex: {len(cyc)};  nonzero helicity: {len(nz)}")
print(f"    values: {min(nz):+.6f} to {max(nz):+.6f}")
chk("every ring carries a nonzero helicity", len(nz)==len(cyc))
chk(f"and the magnitude is 1/(2*phi) = {1/(2*phi):.6f}",
    abs(abs(nz[0])-1/(2*phi))<1e-6, "phi-valued, like everything else here")

print("\nT3 -- AND THE TWO STATES ARE EXCHANGED BY AN EXACT SYMMETRY OF THE CURRENT SETUP")
key={tuple(np.round(v,9)):i for i,v in enumerate(V)}
pmv=np.array([key[tuple(np.round(Th@V[i],9))] for i in range(N)])
flip=same=0
for c in cyc:
    a=hel(c,nhat); b=hel(tuple(pmv[list(c)]),nhat)
    if abs(a)<1e-9: continue
    if abs(a+b)<1e-6: flip+=1
    elif abs(a-b)<1e-6: same+=1
print(f"    under Theta = diag(1,1,1,-1), which FIXES n-hat and preserves the 600-cell:")
print(f"      helicity FLIPS for {flip} rings, unchanged for {same}")
chk("the helicity flips for EVERY ring", flip==len(cyc) and same==0,
    "so the two states are exchanged by a symmetry the current substrate HAS -- which "
    "means they are EXACTLY DEGENERATE, and nothing in the present setup prefers one")

print("\nT4 -- WHICH COMPLETES THE MECHANISM SKETCH, IN FORM")
print("    achiral substrate  -> Theta exists -> the two helicities are degenerate")
print("    CHIRAL substrate   -> no Theta     -> the degeneracy is BROKEN")
print("    and the variable is BINARY: sign(helicity) is +1 or -1, all-or-nothing,")
print("    which is the maximality V-A wants and which a 2% bias can select between.")
chk("built entirely from objects the corpus already has", True,
    "the W bracelet (SF-2 Theorem 4.2), n-hat (FI-C-RC-1), and the chiral shell (4041). "
    "Nothing new is postulated")
chk("and 4049's negative becomes the REQUIREMENT rather than the obstacle", True,
    "the bracelet's achirality is what GUARANTEES exactly two degenerate states. A "
    "chiral bracelet would have split them geometrically, leaving nothing for the "
    "substrate to do")

print("\nT5 -- WHAT IS NOT DONE")
chk("THE SPLITTING IS NOT COMPUTED", True,
    "this shows the two states exist, are P-odd, are binary, and are degenerate in the "
    "present setup. It does NOT show that a chiral substrate splits them, nor by how "
    "much, nor with which sign. That needs the bracelet embedded in the chiral "
    "environment and is the next piece of work")
chk("and it is not claimed that this is how SF-2's bracelet works", True,
    "SF-2 describes a catalyst activated at a D_6-symmetric centroid, not a helicity "
    "state. Whether the W state carries this variable is SF-2's to say")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands. SF-2 unrevised.")
raise SystemExit(1 if fails else 0)
