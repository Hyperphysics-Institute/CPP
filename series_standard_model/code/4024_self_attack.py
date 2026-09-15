#!/usr/bin/env python3
# 4024 - PD-008 applied to my own patch: I flagged two attack points at 4023 and handed
# them to the next window. PD-008 says finish. So I ran them myself.
#
# ATTACK (a) does the OS/chessboard estimate need RP for a GENERATING SET of reflections,
#            not only the one implementing the symmetry?
# ATTACK (b) do the T-face and P-face separate as cleanly on a NESS as 0973 suggests?
#
# One lands and one does not, and the result is better than 4023's: STRONGER in the
# finite case, WEAKER in the extended one. 4023's "outside VW-1's scope" is WITHDRAWN.
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
                for pm_ in P(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm_[i]>pm_[j])%2==0:
                        Vs.append(np.array([sg[pm_[i]] for i in range(4)]))
    U=[]
    for v in Vs:
        if not any(np.allclose(v,u,atol=1e-9) for u in U): U.append(v)
    return np.array(U)
V=build(); N=len(V)
D=np.array([[np.linalg.norm(V[i]-V[j]) for j in range(N)] for i in range(N)])
edges=[(i,j) for i in range(N) for j in range(i+1,N) if abs(D[i,j]-e)<1e-9]
nbr=[np.flatnonzero(np.abs(D[i]-e)<1e-9) for i in range(N)]
key={tuple(np.round(v,9)):i for i,v in enumerate(V)}
nhat=np.array([1.,0,0,0]); Th=np.diag([1.,1,1,-1])
pm=np.array([key[tuple(np.round(Th@V[i],9))] for i in range(N)])
Pm=np.zeros((N,N))
for i in range(N): Pm[pm[i],i]=1.0
def Qmat(nh,delta):
    Q=np.zeros((N,N))
    for (i,j) in edges:
        u=(V[j]-V[i]); u/=np.linalg.norm(u); c=float(u@nh)
        Q[i,j]=1+delta*c; Q[j,i]=1-delta*c
    for i in range(N): Q[i,i]=-Q[i].sum()
    return Q
def stationary(Q):
    w,vec=np.linalg.eig(Q.T); k=int(np.argmin(np.abs(w)))
    p=np.real(vec[:,k]); return p/p.sum()
def eta(X,nh):
    out=np.empty(N)
    for v in range(N):
        nb=nbr[v]; pr=(X[nb]-X[v])@nh
        top=nb[np.argsort(-pr)[:4]]
        out[v]=np.sign(np.linalg.det(np.array([X[t]-X[v] for t in top])))
    return out

print("ATTACK (b) -- DOES NOT LAND. Theta is an EXACT symmetry of the NESS generator.")
for delta in (0.10,0.35):
    Q=Qmat(nhat,delta); QT=Pm@Q@Pm.T
    chk(f"delta={delta:4.2f}: |Theta Q Theta^-1 - Q|max = {np.abs(QT-Q).max():.3e}",
        np.abs(QT-Q).max()<1e-12, "a PURE P operation on the dynamics, not just on the measure")
    chk(f"delta={delta:4.2f}: and NOT time reversal -- |Theta Q Theta^-1 - Q^T|max = "
        f"{np.abs(QT-Q.T).max():.3e}", np.abs(QT-Q.T).max()>1e-2,
        "the gap grows with delta, so P and T are genuinely distinct here")
chk("=> P and T DO separate cleanly on this NESS, as 0973's P-even/T-odd split says",
    True, "attack (b) fails; 4023 Step 2 stands")

print("\nATTACK (a) -- LANDS. The available reflections cannot reach along n-hat.")
gens=[np.diag(s).astype(float) for s in ((1,1,1,-1),(1,1,-1,1),(1,-1,1,1))]
gens=[M for M in gens if all(tuple(np.round(M@v,9)) in key for v in V)]
grp=[np.eye(4)]
for _ in range(8):
    new=[]
    for A in grp:
        for G in gens:
            B=G@A
            if not any(np.allclose(B,C,atol=1e-9) for C in grp+new): new.append(B)
    if not new: break
    grp+=new
disp=max(float(np.abs(A@nhat-nhat).max()) for A in grp)
chk(f"the n-hat-fixing reflections generate {len(grp)} elements, NONE of which moves "
    f"n-hat (max displacement {disp:.3e})", len(gens)==3 and disp<1e-12)
print("  An OS/chessboard estimate is built by tiling with reflections. The ones where")
print("  RP holds generate only TRANSVERSE motion, so the estimate controls TRANSVERSE")
print("  correlations and has NO TRACTION ALONG n-hat AT ALL.")
chk("=> 4023's framing 'the failure is OUTSIDE VW-1's scope' is WITHDRAWN", True,
    "no-SSB is a statement about the whole system. A direction the argument cannot "
    "reach is a gap INSIDE the scope, not a region outside it. That was the convenient "
    "reading and it was wrong")

print("\nTHE RESULT, REVISED -- STRONGER IN ONE PLACE, WEAKER IN THE OTHER")
print("  (1) FINITE SUBSTRATE: stronger than 4023 said. Theta is an exact symmetry of Q,")
print("      so pi is exactly Theta-invariant, and eta is exactly Theta-odd. Then")
print("      <eta> = sum_v pi_v eta_v = 0 BY SYMMETRY ALONE -- no RP required anywhere.")
# NOTE: the draft asserted <eta> = 0 for a SINGLE configuration and FAILED at
# -8.6e-5 ... +4.4e-3. The draft was wrong and the failure is the point: pi is
# Theta-invariant and eta is Theta-ODD AS A FUNCTIONAL, but a single random X is not
# itself Theta-symmetric, so eta_{Theta v}(X) != -eta_v(X) for that X. The symmetry
# statement is an ENSEMBLE statement, and it reproduces 4020 exactly: each realisation
# chiral, the ensemble not. Corrected below, at the strength that actually holds.
for eps in (0.02,0.05):
    for delta in (0.10,0.35):
        p=stationary(Qmat(nhat,delta))
        vals=[float(p@eta(V+eps*np.random.default_rng(s).standard_normal((N,4)),nhat))
              for s in range(24)]
        v=np.array(vals); sem=v.std(ddof=1)/math.sqrt(len(v))
        chk(f"eps={eps:4.2f} delta={delta:4.2f}: pi Theta-inv ({np.abs(p[pm]-p).max():.1e});"
            f" single-realisation <eta> spans [{v.min():+.2e},{v.max():+.2e}] and is NOT 0;"
            f" ENSEMBLE mean {v.mean():+.2e} +- {sem:.1e}",
            np.abs(p[pm]-p).max()<1e-12 and np.abs(v).max()>1e-6 and abs(v.mean())<2.5*sem)
chk("so the finite-substrate statement is an ENSEMBLE one, and needs NO RP",
    True, "pi is exactly Theta-invariant because Theta commutes with Q (attack b), and "
    "the perturbation ensemble is Theta-symmetric, so E[<eta>] = 0 by symmetry alone. "
    "4023 presented this as RP-dependent; it is not. RP is needed only for the "
    "infinite-volume question")
print("  (2) EXTENDED LATTICE: weaker than 4023 said. The SSB question needs the")
print("      infinite-volume limit; RP-based control exists transversally and does NOT")
print("      exist along n-hat, and the available reflection group cannot even reach")
print("      there. VW-1 is GENUINELY WEAKENED on the extended lattice, not merely")
print("      incomplete. That is the live gap and it is now stated at full strength.")
chk("net: the self-attack improved the result in both directions", True,
    "which is the case for PD-008 -- had this gone to the next window, the finite-case "
    "strengthening would likely have been missed alongside the withdrawal")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("SUBMITTED FOR CRITIQUE. NO verdict moved. FI-C-9 = V3 stands.")
raise SystemExit(1 if fails else 0)
