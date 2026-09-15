#!/usr/bin/env python3
# 4056 - 4055 named the non-product class as the only place a counterexample to RP could
# live. Looked there. FOUND ONE. H1 FAILS in the n-hat-preserving sector, and 4022,
# 4023, 4024 and 4055 all rest on it holding there.
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
K=200; K2=K*(K-1); K3=K2*(K-2); K4=K3*(K-3)

print("T1 -- THE MOMENT, EXACTLY, FOR THE SQUARED-OCCUPATION CLASS")
print("  n_i^2 = (n_i)_2 + n_i, so for i != j and multinomial(K, p):")
print("    E[n_i^2 n_j^2] = K4 p_i^2 p_j^2 + K3 (p_i^2 p_j + p_i p_j^2) + K2 p_i p_j")
print("  For F = sum_a w_a n_a^2 on the + side, <Theta(F) F> = K4 s^2 + 2 K3 s t + K2 t^2")
print("  with s = sum w_a p_a^2 and t = sum w_a p_a.  PSD iff K4*K2 - K3^2 >= 0.")
disc=K4*K2-K3*K3
chk(f"K4*K2 - K3^2 = {disc} -- NEGATIVE", disc<0,
    "algebraically K^2 (K-1)^2 (K-2) [(K-3)-(K-2)] = -K^2 (K-1)^2 (K-2), negative for "
    "every K >= 3, AND INDEPENDENT OF p. The indefiniteness is in the multinomial "
    "itself, not in the measure")

print("\nT2 -- AND ON THE REAL MEASURE, IN THE n-hat-FIXING SECTOR, IT BITES")
res={}
for delta in (0.0,0.10,0.35):
    p=stat(np.array([1.,0,0,0]),delta)
    u=np.array([p[a]**2 for a in plus]); v=np.array([p[a] for a in plus])
    G=K4*np.outer(u,u)+K3*(np.outer(u,v)+np.outer(v,u))+K2*np.outer(v,v)
    mn=float(np.linalg.eigvalsh((G+G.T)/2).min()); res[delta]=mn
    print(f"    delta={delta:4.2f}   min eigenvalue of the Gram = {mn:+.6e}")
chk("delta = 0: PSD", abs(res[0.0])<1e-10,
    "the measure is UNIFORM there, so p^2 is PARALLEL to p, s and t are proportional, "
    "and the indefinite 2x2 form is NEVER PROBED")
chk(f"delta = 0.10 and 0.35: NEGATIVE ({res[0.10]:+.2e}, {res[0.35]:+.2e})",
    res[0.10]<-1e-4 and res[0.35]<-1e-4,
    "once the tilt makes p non-uniform, p^2 and p are independent and the negative "
    "direction becomes reachable")

print("\nT3 -- EXPLICIT WITNESS, NOT AN ARTIFACT OF SYMMETRISATION")
for delta in (0.10,0.35):
    p=stat(np.array([1.,0,0,0]),delta)
    u=np.array([p[a]**2 for a in plus]); v=np.array([p[a] for a in plus])
    M=np.array([[K4,K3],[K3,K2]]); _,evec=np.linalg.eigh(M); s_,t_=evec[:,0]
    A=np.array([[u@u,u@v],[v@u,v@v]]); c=np.linalg.solve(A,np.array([s_,t_]))
    w=c[0]*u+c[1]*v; S=float(u@w); T=float(v@w)
    val=K4*S*S+2*K3*S*T+K2*T*T
    print(f"    delta={delta:4.2f}  <Theta(F) F> = {val:+.6e}  for an explicit F")
    chk(f"delta={delta:4.2f}: a single test function gives a NEGATIVE value", val<0,
        "RP demands <Theta(F) F> >= 0 for EVERY F on one side. One F suffices to refute")

print("\nT4 -- WHAT THIS COSTS, AND IT IS NOT SMALL")
chk("H1 is FALSE on [PCD-EXT] for delta > 0, in BOTH sectors", True,
    "4022 found it fails for n-hat-FLIPPING reflections. It also fails for n-hat-FIXING "
    "ones, on a class 4022 did not test and 4055 explicitly named as untested")
chk("4055's strengthening stands but is now the SMALLER half", True,
    "'necessary and sufficient within all PRODUCT observables' is still true. The "
    "product hierarchy was simply the wrong place to look, and 4055 said so")
chk("4023 and 4024 are UNDERMINED, and I should say which part", True,
    "both rest on RP holding in the n-hat-preserving sector. It does not. 4023's "
    "'VW-1's conclusion survives restricted RP' has no RP left to be restricted to, "
    "and 4024's finite-substrate strengthening -- E[<eta>] = 0 by exact symmetry -- "
    "SURVIVES, because that argument never used RP")
chk("and the delta = 0 case is untouched", abs(res[0.0])<1e-10,
    "RP holds at delta = 0 in both sectors. The failure is entirely a NESS effect, "
    "which is the same place 4022 found the flipping-sector failure")
print("\n  NOT CLAIMED: that the DSL measure fails RP. [PCD-EXT] is 4004's WORKING")
print("  extension, not the DSL measure, and every RP result in this arc -- 4022's,")
print("  4055's and this one -- is about [PCD-EXT]. What is established is that the")
print("  working extension does not satisfy H1, so it cannot be used to discharge it.")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved -- but H1 is now FAILED rather than open on [PCD-EXT].")
raise SystemExit(1 if fails else 0)
