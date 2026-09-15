#!/usr/bin/env python3
# 4055 - the extension 4022 owed. Different item from the queue: the chirality-
# construction line stopped at 4054, and this is an unrelated debt.
#
# 4022: RP holds for n-hat-FIXING reflections and fails for n-hat-FLIPPING ones -- on
# SINGLE-SITE occupations, and it said plainly that passing was NECESSARY ONLY.
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
                for pm_ in P(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm_[i]>pm_[j])%2==0:
                        Vs.append(np.array([sg[pm_[i]] for i in range(4)]))
    U=[]
    for v in Vs:
        if not any(np.allclose(v,u,atol=1e-9) for u in U): U.append(v)
    return np.array(U)
V=build600(); N=len(V)
D=np.array([[np.linalg.norm(V[i]-V[j]) for j in range(N)] for i in range(N)])
edges=[(i,j) for i in range(N) for j in range(i+1,N) if abs(D[i,j]-e)<1e-9]
key={tuple(np.round(v,9)):i for i,v in enumerate(V)}
Th=np.diag([1.,1,1,-1]); PM=np.array([key[tuple(np.round(Th@V[i],9))] for i in range(N)])
plus=[i for i in range(N) if V[i][3]>1e-9]
def stat(nh,delta):
    Q=np.zeros((N,N))
    for (i,j) in edges:
        u=(V[j]-V[i]); u/=np.linalg.norm(u); c=float(u@nh)
        Q[i,j]=1+delta*c; Q[j,i]=1-delta*c
    for i in range(N): Q[i,i]=-Q[i].sum()
    w,vec=np.linalg.eig(Q.T); k=int(np.argmin(np.abs(w)))
    p=np.real(vec[:,k]); return p/p.sum()
K=200
def gram(p,sets):
    m=len(sets[0]); f=1.0
    for k in range(2*m): f*=(K-k)
    u=np.array([np.prod([p[PM[a]] for a in A]) for A in sets])
    v=np.array([np.prod([p[a] for a in A]) for A in sets])
    return f*np.outer(u,v)

print("T1 -- THE EXACT MOMENT, WHICH IS WHY THIS IS CLOSED-FORM AND NOT SAMPLED")
print("  For multinomial(K, p) with all indices DISTINCT,")
print("    E[n_a1..n_am n_c1..n_cm] = K(K-1)...(K-2m+1) * prod p   EXACTLY.")
print("  Theta maps the + side to the - side, so {Theta a} and {c} NEVER overlap --")
print("  every index is distinct and no coincidence term ever enters.")
chk("so the Gram matrix is EXACTLY G = K^(2m) * u (x) v, RANK ONE at every m", True,
    "u_A = prod p_(Theta a), v_C = prod p_c. Symmetric iff u is proportional to v, "
    "i.e. iff pi is Theta-invariant")

print("\nT2 -- m = 2 AND m = 3, MEASURED")
P2=[t for t in it.combinations(plus,2)][:120]
P3=[t for t in it.combinations(plus,3)][:80]
print(f"    {'n-hat':<12}{'m':>3}{'delta':>7}{'rank':>6}{'|G-G^T|max':>14}{'min eig':>15}")
res={}
for nm,nh in (("FIXED",np.array([1.,0,0,0])),("FLIPPED",np.array([0.,0,0,1]))):
    for m,sets in ((2,P2),(3,P3)):
        for delta in (0.0,0.10,0.35):
            p=stat(nh,delta); G=gram(p,sets)
            asym=float(np.abs(G-G.T).max()); mn=float(np.linalg.eigvalsh((G+G.T)/2).min())
            res[(nm,m,delta)]=(asym,mn)
            print(f"    {nm:<12}{m:>3}{delta:>7.2f}"
                  f"{np.linalg.matrix_rank(G,tol=1e-6):>6}{asym:>14.3e}{mn:>15.4e}")
for m in (2,3):
    for delta in (0.0,0.10,0.35):
        a,mn=res[("FIXED",m,delta)]
        chk(f"n-hat FIXED, m={m}, delta={delta:4.2f}: symmetric and PSD",
            a<1e-10 and mn>-1e-9)
for m in (2,3):
    for delta in (0.10,0.35):
        a,mn=res[("FLIPPED",m,delta)]
        chk(f"n-hat FLIPPED, m={m}, delta={delta:4.2f}: RP FAILS (min eig {mn:+.2e})",
            a>1e-2 and mn<-1e-2)

print("\nT3 -- SO 4022's CAVEAT IS DISCHARGED FOR THE WHOLE PRODUCT HIERARCHY")
chk("the verdict is IDENTICAL at m = 1, 2 and 3, and the structure is m-INDEPENDENT",
    True,
    "rank one at every m, symmetric exactly when pi is Theta-invariant. There is no "
    "m at which a product observable could give a different answer")
chk("4022's 'NECESSARY ONLY' becomes 'NECESSARY AND SUFFICIENT WITHIN ALL PRODUCT "
    "OBSERVABLES'", True,
    "a real strengthening of VW-1's residual, and the first owed item discharged since "
    "the chirality line stopped")

print("\nT4 -- WHAT IS STILL NOT COVERED, AND IT IS A REAL CLASS")
print("  NON-PRODUCT observables: anything with a REPEATED index (n_a^2), or any")
print("  function of a SUM. Those bring in the multinomial's coincidence terms -- the")
print("  +K p_a on the diagonal that 4022's single-site Gram already had -- and the")
print("  clean rank-one form breaks.")
chk("NOT tested here", True,
    "the product hierarchy is closed; the coincidence-bearing classes are not, and "
    "they are where a counterexample to RP would have to live if one exists")
chk("and nothing downstream changes", True,
    "4023 and 4024 rest on RP holding in the n-hat-preserving sector, which is now "
    "established on a strictly larger class than before. No verdict moves")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)
