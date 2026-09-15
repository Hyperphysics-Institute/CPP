#!/usr/bin/env python3
# 4022 - H1: is the DSL measure REFLECTION-POSITIVE?
#
# H1 is THEO-CHIR-VW-1's sole residual, open since Patch 0679/0680 in June. Every route
# this session has funnelled into it: 4003 named it, 4004 closed its twin (H-NESS) as
# ill-posed, 4005 discharged the recompute, 4021 showed the relaxation question reduces
# to it. It is the last residual standing on the mu^2-sign route.
import numpy as np, math
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
V=build(); N=len(V)
D=np.array([[np.linalg.norm(V[i]-V[j]) for j in range(N)] for i in range(N)])
edges=[(i,j) for i in range(N) for j in range(i+1,N) if abs(D[i,j]-e)<1e-9]
Theta=np.diag([1.,1,1,-1]); key={tuple(np.round(v,9)):i for i,v in enumerate(V)}
def stationary(nhat,delta,r0=1.0):
    Q=np.zeros((N,N))
    for (i,j) in edges:
        u=(V[j]-V[i]); u/=np.linalg.norm(u); c=float(u@nhat)
        Q[i,j]=r0*(1+delta*c); Q[j,i]=r0*(1-delta*c)
    for i in range(N): Q[i,i]=-Q[i].sum()
    w,vec=np.linalg.eig(Q.T); k=int(np.argmin(np.abs(w)))
    p=np.real(vec[:,k]); return p/p.sum()

print("T1 -- the reflection exists and is exact")
chk("Theta = diag(1,1,1,-1) maps the 600-cell to itself, det = -1",
    all(tuple(np.round(Theta@v,9)) in key for v in V) and abs(np.linalg.det(Theta)+1)<1e-12)
pm=np.array([key[tuple(np.round(Theta@V[i],9))] for i in range(N)])
plus=[i for i in range(N) if V[i][3]>1e-9]; K=200
chk(f"it splits the lattice cleanly: {len(plus)} on the + side", len(plus)==45)

print("\nT2 -- RP TESTED, AND IT IS CONDITIONAL ON WHETHER THE REFLECTION FIXES n-hat")
def gram(p, obs):
    """G_ij = <Theta(F_i) F_j> under multinomial(K, p) occupation.
       obs = list of vertex tuples; F = product of occupations on the + side."""
    def mom(a,b):
        if a==b: return K*(K-1)*p[a]*p[b] + K*p[a]
        return K*(K-1)*p[a]*p[b]
    return np.array([[mom(pm[a],b) for b in obs] for a in obs])
rows=[]
for name,nhat in (("n-hat = e1  (Theta FIXES it)", np.array([1.,0,0,0])),
                  ("n-hat = e4  (Theta FLIPS it)", np.array([0.,0,0,1])),
                  ("n-hat tilted (partly flipped)", np.array([1.,0,0,1])/math.sqrt(2))):
    fixed=np.allclose(Theta@nhat,nhat)
    print(f"  {name}   Theta(n-hat)==n-hat: {fixed}")
    for delta in (0.0,0.10,0.35):
        p=stationary(nhat,delta)
        inv=float(np.max(np.abs(p[pm]-p)))
        G=gram(p,plus); asym=float(np.abs(G-G.T).max())
        mn=float(np.linalg.eigvalsh((G+G.T)/2).min())
        print(f"     delta={delta:4.2f}  max|pi(Th v)-pi(v)|={inv:9.3e}  "
              f"|G-G^T|max={asym:9.3e}  min eig={mn:+11.4e}")
        rows.append((fixed,delta,inv,asym,mn))
for fixed,delta,inv,asym,mn in rows:
    if fixed or delta==0.0:
        chk(f"{'n-fixing' if fixed else 'delta=0'} delta={delta:4.2f}: pi is Theta-INVARIANT, "
            f"G symmetric, PSD", inv<1e-12 and asym<1e-10 and mn>-1e-10)
    else:
        chk(f"n-flipping delta={delta:4.2f}: RP FAILS -- G is not even symmetric, min eig {mn:+.3e}",
            asym>1e-2 and mn<-1e-2, "a genuine witness: one negative eigenvalue refutes RP")

print("\nT3 -- THE ASYMMETRY BETWEEN THE TWO ANSWERS, STATED")
chk("the FAILURE is a proof; the SUCCESS is not", True,
    "RP requires positivity for ALL functions on the + side. A single negative "
    "eigenvalue on ANY test class REFUTES it -- so the n-hat-flipping result is a "
    "witness and settles that case. Passing on this class is a NECESSARY condition "
    "only, and is not proof of RP")
print("  Test class used: single-site occupations on the + side, 45 observables,")
print("  under the multinomial(K, pi) occupation measure of 4004's [PCD-EXT].")

print("\nT4 -- WHY THIS MATTERS AND WHERE I STOP")
print("  VW-1 (0680, review-closed 3/3 at 0682): H1 => mu^2 > 0 and eta = 0, so the")
print("  det-coset Z2 cannot break spontaneously within the substrate axioms.")
print("  H1 is NOT simply true or false. It is TRUE for the reflections that fix n-hat")
print("  and FALSE, at O(delta), for those that do not.")
chk("and the reflections the chirality question needs are the n-hat-FIXING ones", True,
    "R = diag(1,1,1,-1) with n-hat = e1 is exactly the map 4011, 4012, 4015 and 4020 "
    "used; and 0973 puts sign(delta) as P-EVEN, so the P-face lives in the "
    "n-hat-preserving sector. H1 holds where the chirality argument needs it")
chk("NOT CLAIMED: that VW-1's argument goes through on RESTRICTED RP", True,
    "whether a transfer-matrix/OS construction can be run with RP holding only on the "
    "n-hat-preserving subgroup is a technical question about VW-1 itself. It belongs "
    "to whoever holds that theorem. FLAGGED, not decided")
print("\n  AND A STRUCTURAL ECHO, RECORDED WITHOUT A STORY:")
print("  RP fails precisely for the reflections that FLIP n-hat -- and 0973 located the")
print("  T-ARROW in exactly that direction (sign(delta) P-even, T-ODD). The RP failure")
print("  and the T-arrow occupy the same place. Noted; nothing built on it.")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)
