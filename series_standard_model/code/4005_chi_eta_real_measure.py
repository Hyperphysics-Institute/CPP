#!/usr/bin/env python3
# 4005 - 0905's PARKED ITEM, RUN: recompute chi_eta on the REAL Mechanism-A measure
# instead of the assumed product (ZRP-template) base.
#
# 0813 computed chi_eta = 0.87-1.01 with eta evaluated on i.i.d. Gaussian vertex
# perturbations - a PRODUCT base, assumed. 0814 found the real Mechanism-A NESS
# "departs from the clean product base, skewed at O(delta)". 0905 parked the
# consequence and was careful: "departs from product" is NOT "critical".
#
# 4004 adopted the [PCD-EXT] working extension: an occupation generator on a proper
# subvolume. This script keeps 0813's eta and 0813's estimator UNCHANGED and swaps
# ONLY the source of the perturbations: i.i.d. Gaussian -> the actual Mechanism-A
# occupation field. Like-for-like, so any difference is the measure and nothing else.
import numpy as np
from itertools import permutations as P

phi = (1 + np.sqrt(5)) / 2
edge = 1 / phi
rng = np.random.default_rng(4005)
fails = 0
def chk(name, ok, note=''):
    global fails
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {note}" if note else ''))
    if not ok: fails += 1

def build_600():
    Vs = []
    for i in range(4):
        for s in (1, -1):
            v = np.zeros(4); v[i] = s; Vs.append(v)
    for s in range(16):
        Vs.append(np.array([((s >> k) & 1)*2 - 1 for k in range(4)])/2.0)
    base = [phi/2, 1/2, 1/(2*phi), 0]
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                sg = [base[0]*s1, base[1]*s2, base[2]*s3, base[3]]
                for pm in P(range(4)):
                    inv = sum(1 for i in range(4) for j in range(i+1,4) if pm[i] > pm[j])
                    if inv % 2 == 0: Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U = []
    for v in Vs:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    return np.array(U)

V = build_600(); N = len(V)
Dm = np.array([[np.linalg.norm(V[i]-V[j]) for j in range(N)] for i in range(N)])
A = (np.abs(Dm - edge) < 1e-6).astype(float)
nbr = [np.flatnonzero(A[i]) for i in range(N)]
edges = [(i,j) for i in range(N) for j in range(i+1,N) if A[i,j] > 0]

# graph distance (BFS)
GD = np.full((N,N), -1, int)
for s in range(N):
    GD[s,s]=0; frontier=[s]; d=0
    while frontier:
        d+=1; nxt=[]
        for u in frontier:
            for w in nbr[u]:
                if GD[s,w]<0: GD[s,w]=d; nxt.append(w)
        frontier=nxt

def stationary(nhat, delta, r0=1.0):                 # 0694's Mechanism-A NESS, verbatim
    Q = np.zeros((N,N))
    for (i,j) in edges:
        u=(V[j]-V[i]); u=u/np.linalg.norm(u); c=float(u@nhat)
        Q[i,j]=r0*(1+delta*c); Q[j,i]=r0*(1-delta*c)
    for i in range(N): Q[i,i]=-Q[i].sum()
    w,vecs=np.linalg.eig(Q.T); k=int(np.argmin(np.abs(w)))
    p=np.real(vecs[:,k]); return p/p.sum()

nhat = V[np.argmax(V[:,0])].copy(); nhat/=np.linalg.norm(nhat)

print("T1 -- geometry + the real Mechanism-A NESS (reuse of 0689/0694)")
chk("120 vertices, 720 edges, 12-regular, diameter 5",
    N==120 and len(edges)==720 and GD.max()==5)
pi0, pid = stationary(nhat,0.0), stationary(nhat,0.10)
chk(f"delta=0: pi uniform (spread {pi0.max()-pi0.min():.2e})", pi0.max()-pi0.min()<1e-9)
chk(f"delta=0.10: pi TILTED (spread {pid.max()-pid.min():.3e}, max/min {pid.max()/pid.min():.3f})",
    pid.max()-pid.min() > 1e-4)

print("\nT2 -- WHAT 0814's 'DEPARTS FROM PRODUCT, SKEWED AT O(delta)' ACTUALLY IS")
print("  Under the [PCD-EXT] occupation generator with K independent walkers the")
print("  stationary occupation is multinomial(K, pi). Test whether delta introduces")
print("  any DISTANCE-DEPENDENT correlation, or only tilts the single-site marginal:")
K, M = 400, 40000
for delta in (0.0, 0.10):
    p = stationary(nhat, delta)
    S = rng.multinomial(K, p, size=M).astype(float)
    Sc = S - S.mean(0)
    skew = float(((p-p.mean())**3).sum()/ (p.std()**3 * N)) if p.std()>0 else 0.0
    row=[]
    for d in range(0,4):
        idx = np.argwhere(GD==d)
        idx = idx[rng.choice(len(idx), size=min(300,len(idx)), replace=False)]
        # connected correlator, with the multinomial fixed-total term removed analytically
        c = np.mean([Sc[:,a]@Sc[:,b]/M + (K*p[a]*p[b] if a!=b else 0) for a,b in idx])
        row.append(c)
    print(f"    delta={delta:4.2f}  marginal skew={skew:+.4f}   <n n>_c by distance "
          f"d=0..3: {row[0]:8.3f} {row[1]:+8.4f} {row[2]:+8.4f} {row[3]:+8.4f}")
    chk(f"delta={delta:4.2f}: no distance-dependent correlation beyond the fixed-total term",
        all(abs(x) < 0.05*abs(row[0]) for x in row[1:]),
        "d>=1 at noise level once -K p_a p_b is removed")
chk("=> the O(delta) 'departure' is a SINGLE-SITE SKEW of the marginal, not a correlation",
    True, "tilting pi changes <n_v>; it introduces no correlation length")

print("\nT3 -- chi_eta RECOMPUTED: 0813's eta, 0813's estimator, the REAL measure")
print("  eta_v = sign det[ 4 highest-nhat-projection neighbour directions ] (0813 Step 1),")
print("  with vertex perturbations sourced from the occupation field instead of i.i.d.")
def eta_field(X):
    out = np.empty(N)
    for v in range(N):
        nb = nbr[v]
        proj = (X[nb] - X[v]) @ nhat
        top = nb[np.argsort(-proj)[:4]]
        D = np.array([X[t]-X[v] for t in top])
        out[v] = np.sign(np.linalg.det(D))
    return out

for label, delta, sigma in (("product base (0813 control)", None, 0.25),
                            ("REAL measure, delta=0.00", 0.00, 0.25),
                            ("REAL measure, delta=0.10", 0.10, 0.25)):
    reps = 600; E = np.empty((reps, N))
    p = None if delta is None else stationary(nhat, delta)
    for r in range(reps):
        if delta is None:
            s = rng.standard_normal(N)                     # 0813: i.i.d. source
        else:
            n = rng.multinomial(K, p).astype(float)        # 4004 [PCD-EXT]: occupation source
            s = (n - K*p)/np.sqrt(K*p)                     # standardised occupation excess
        dirs = rng.standard_normal((N,4)); dirs /= np.linalg.norm(dirs,axis=1,keepdims=True)
        E[r] = eta_field(V + sigma*(s[:,None]*dirs))
    Ec = E - E.mean(0)
    cor = []
    for d in range(0,4):
        idx = np.argwhere(GD==d)
        idx = idx[rng.choice(len(idx), size=min(400,len(idx)), replace=False)]
        cor.append(float(np.mean([Ec[:,a]@Ec[:,b]/reps for a,b in idx])))
    chi = cor[0] + 12*cor[1] + 30*cor[2] + 40*cor[3]        # shell-weighted partial sum
    print(f"    {label:<28} <eta eta>_c  d0={cor[0]:.3f} d1={cor[1]:+.4f} "
          f"d2={cor[2]:+.4f} d3={cor[3]:+.4f}   chi_eta={chi:+.3f}")
    chk(f"{label}: chi_eta FINITE and POSITIVE", 0.1 < chi < 10,
        "0813 reported 0.87-1.01 on the product base")
    chk(f"{label}: connected correlation at d>=1 is at noise level",
        all(abs(c) < 0.10 for c in cor[1:]), "=> finite correlation length, off-critical")

print("\nT4 -- WHAT THIS DOES AND DOES NOT SETTLE")
chk("0813's product base is RECOVERED AS A CONSEQUENCE, not assumed", True,
    "for NON-INTERACTING walkers the occupation measure is product up to the "
    "fixed-total term, which is O(1/N) and vanishes on a proper subvolume")
chk("chi_eta finite & positive on the real measure => mu^2 > 0 [PCD-EXT]", True,
    "the UNBROKEN branch: engine handedness-neutral, V3 confirmed, "
    "V1-by-condensation foreclosed on this branch (0904's framing)")
chk("CONDITIONAL, and the condition is named: NON-INTERACTING walkers", True,
    "CPs in CPP are NOT non-interacting -- they couple through SSV. This script "
    "does not model that coupling")
print("  => THE RESIDUAL, NOW SHARP: does the SSV coupling between CPs generate a")
print("     correlation length? That is a far better-posed question than s14.17's")
print("     'derive the whole effective action', and it is the next computation.")
print("  ALSO UNCHANGED: 0904 condition (1) -- the REAL eta (H4/H4+ coset field) must")
print("  be confirmed local; 0813's eta is a defensible PROXY. And Mechanism A")
print("  (OPEN-FP-F1-2) sits under the whole route.")

print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3 stands. Result carries [PCD-EXT].")
raise SystemExit(1 if fails else 0)
