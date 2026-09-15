#!/usr/bin/env python3
# 4062 - PD-008 critique of 4056/4057 (the H1 refutation), the conclusion the 4000-4061 window
# most wanted. Finding: the refutation is an O(1/K) artifact of treating ONE closed 600-cell
# as an isolated system with a fixed total. The corpus's conservation law is a CONTINUITY
# equation with flux (constancy only for an isolated system), A2's substrate is tessellated,
# and VW-1 itself places reflection positivity in the continuum limit (CONT-1), which "a
# finite polytope does not literally possess". In that limit the violation is exactly zero.
# THIS IS THE CONVENIENT BRANCH FOR THE PROGRAMME. It is marked as such and submitted.
import numpy as np, math, os
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
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
def ff(K,r):
    o=1.0
    for i in range(r): o*=(K-i)
    return o
def gram(p,K,sites,thmap,orders=(1,2),const=True,poisson=False):
    # basis on the + side: 1, and (n_a)_r / (K p_a)^r for r in orders.  Rescaling a basis is a
    # congruence, so the INERTIA (sign of the minimum eigenvalue) is unchanged by it.
    # Multinomial(K,p), i != j:  E[(n_i)_r (n_j)_s] = K^(r+s falling) p_i^r p_j^s
    # Poisson(K p) independent:  E[(n_i)_r (n_j)_s] = (K p_i)^r (K p_j)^s
    idx=([('c',0)] if const else [])+[(a,r) for a in sites for r in orders]
    G=np.zeros((len(idx),len(idx)))
    for x,(a,r) in enumerate(idx):
        for y,(b,s) in enumerate(idx):
            rr=0 if a=='c' else r; ss=0 if b=='c' else s
            if a=='c' and b=='c': G[x,y]=1; continue
            pa=None if a=='c' else p[thmap[a]]; pb=None if b=='c' else p[b]
            num=(ff(K,rr+ss)*(pa**rr if rr else 1)*(pb**ss if ss else 1)) if not poisson else \
                ((K*pa)**rr if rr else 1)*((K*pb)**ss if ss else 1)
            den=((K*p[a])**rr if rr else 1)*((K*p[b])**ss if ss else 1)
            G[x,y]=num/den
    return G
def lmin(G): return float(np.linalg.eigvalsh((G+G.T)/2).min())

print("T1 -- 4056's delta = 0 'PSD' IS AN ARTIFACT OF A CLASS WITHOUT CONSTANTS")
print("  RP is <Theta(F) F> >= 0 for EVERY F in the + side algebra, and that algebra is UNITAL.")
print("  Take F = n_a/(K p_a) - 1.  <Theta(F) F> = (K-1)/K - 1 = -1/K, at ANY p, ANY delta.")
K=200
for delta in (0.0,0.10,0.35):
    p=stat(np.array([1.,0,0,0]),delta); a=plus[0]
    val=ff(K,2)*p[PM[a]]*p[a]/(K*p[a])**2 - 2*(K*p[PM[a]])/(K*p[PM[a]]) + 1
    chk(f"delta={delta:4.2f}: explicit F gives {val:+.6e} = -1/K = {-1/K:+.6e}",
        abs(val+1/K)<1e-12, "the same number at delta = 0 -- so it is NOT a NESS effect")
print("  => 4056's 'delta = 0 is untouched; the failure is entirely a NESS effect' is WRONG.")
print("     It holds only on the tied, constant-free class 4056 tested.")

print("\nT2 -- THE WHOLE VIOLATION IS ONE 3x3 MATRIX THAT DEPENDS ON K ALONE")
print("  In the rescaled basis every multinomial entry is K^(r+s falling)/K^(r+s): p drops out.")
print("  So the Gram's nonzero inertia is that of H_rs = K^(r+s)/K^(r+s), r,s in {0,1,2}.")
def H(K): return np.array([[ff(K,r+s)/K**(r+s) for s in range(3)] for r in range(3)])
for delta in (0.0,0.35):
    p=stat(np.array([1.,0,0,0]),delta)
    chk(f"delta={delta:4.2f}: Theta-invariant measure in the n-hat-FIXING sector",
        np.allclose(p[PM],p,atol=1e-12))
    G=gram(p,K,plus,PM)
    chk(f"delta={delta:4.2f}: full 600-cell Gram min eig {lmin(G):+.3e} (sign of H's {lmin(H(K)):+.3e})",
        (lmin(G)<0)==(lmin(H(K))<0))
rows=[]
for Kt in (200,2000,20000,200000,2000000):
    rows.append((Kt,lmin(H(Kt)))); print(f"    K={Kt:>8}   lambda_min(H) = {rows[-1][1]:+.4e}   K*lambda_min = {Kt*rows[-1][1]:+.4f}")
chk("lambda_min(H) = O(1/K) -> 0", all(abs(Kt*l-rows[-1][0]*rows[-1][1])<0.05 for Kt,l in rows[1:]),
    "K*lambda_min converges; the violation is a finite-total correction with nothing left at K = infinity")
chk("K = infinity: H is the all-ones matrix, rank one, PSD", abs(lmin(np.ones((3,3))))<1e-12,
    "which is exactly the independent-Poisson Gram -- 4057's grand-canonical measure is the LIMIT, not a rival")

print("\nT3 -- EMBED THE 600-CELL IN A LARGER CONSERVED SYSTEM: K is the TOTAL, not the window count")
print("  A window of the substrate holding mean occupancy 200 inside a closed system of total K_tot")
print("  has E[(n_i)_r (n_j)_s] = K_tot^(r+s falling) P_i^r P_j^s -- the SAME H, now with K = K_tot.")
for Kt in (200,200*10,200*1000):
    p=stat(np.array([1.,0,0,0]),0.35); q=200/Kt  # window mass fraction, mean window count 200
    G=gram(q*p,Kt,plus,PM)
    print(f"    K_tot={Kt:>7}  window mean 200   min eig = {lmin(G):+.4e}")
chk("the window's violation is set by K_tot and vanishes as the window is embedded", abs(lmin(gram((200/200000)*stat(np.array([1.,0,0,0]),0.35),200000,plus,PM)))<2e-4,
    "a fixed total on ONE 600-cell is the special case K_tot = window count, i.e. an ISOLATED 600-cell")

print("\nT4 -- D-7: RESOLVE 'CPs ARE CONSERVED' AGAINST THE LANE THAT WROTE IT")
t=open(os.path.join(ROOT,"series_gravitation/fe1_derivation/T2_T3_uniqueness_and_source.md"),encoding='utf-8').read()
chk("GR-FE-1's conservation law is CONTINUITY with a flux J", "\u2202_t \u03c1 + \u2207\u00b7J = 0" in t,
    "local conservation; census is constant only 'for an isolated system, J = 0 on the boundary'")
chk("and the fixed-census statement is scoped to an ISOLATED system", "isolated system" in t)
v=open(os.path.join(ROOT,"series_umbrella/series_substrate_chirality_arc/chirality_derivations/theo_chir_vw_1.tex"),encoding='utf-8').read()
chk("VW-1 places RP in the CONT-1 continuum limit", "a finite\npolytope does not literally possess" in v or "polytope does not literally possess" in v,
    "the theorem whose hypothesis H1 is says RP is not a property of a finite polytope at all")
ax=open(os.path.join(ROOT,"axiom-registry.md"),encoding='utf-8').read()
chk("A2's substrate is TESSELLATED (4007: one 600-cell is a first shell, not the substrate)", "tessellat" in ax.lower())
print("  => 4057's step 'the fixed total is PHYSICAL' resolved 'conserved' as 'fixed on this window'.")
print("     The corpus meaning is continuity. On a non-isolated window the total is not fixed,")
print("     and in the limit VW-1 names, the canonical measure converges to the product measure.")

print("\nT5 -- WHAT SURVIVES OF 4056/4057, AND IT IS REAL")
p=stat(np.array([0.,0,0,1]),0.35)
chk("n-hat-FLIPPING sector: the measure is NOT Theta-invariant", not np.allclose(p[PM],p,atol=1e-6))
mu=np.array([K*p[a] for a in plus]); muT=np.array([K*p[PM[a]] for a in plus])
Gp=np.outer(np.r_[1,muT],np.r_[1,mu]); 
chk(f"and it fails RP in the Poisson limit too (min eig {lmin(Gp):+.3e})", lmin(Gp)<-1e-6,
    "intrinsic, as 4022 and 4057 found; VW-1's use is the fixing sector (4022/4023)")
print("  RULING: 4057's diagnosis 'the fixing-sector failure is CAUSED BY the fixed total' STANDS  --",
    "T2 sharpens it: the failure is NOTHING BUT the fixed total, at every delta")

print("\nT6 -- THE STATUS THIS LEAVES, AND THE TWO CONDITIONS IT NOW RESTS ON")
print("  In the limit, independent walkers with a Theta-invariant intensity give a product measure,")
print("  and a Theta-invariant product measure is RP trivially: <Theta(F)F> = <F>^2 >= 0.")
print("  H1 (n-hat-fixing sector) is therefore NOT refuted. It is OPEN, and rests on:")
print("   (a) NON-INTERACTING walkers -- the condition 4005 already named; CPs couple through SSV,")
print("       and the refutation carried the SAME condition, so nothing new is assumed here;")
print("   (b) Theta being a symmetry of the TESSELLATED substrate's generator -- exact on one")
print("       600-cell (T2), UNESTABLISHED on the aperiodic tessellation (4009).")
print("  RULING: "+"4057 'H1 is FALSE on the physical measure' -- WITHDRAWN")
print("  RULING: "+"4056's refutation downgraded to: RP fails on an ISOLATED 600-cell, by O(1/K)")
print("  RULING: "+"4023 returns to its pre-4056 conditional standing, now conditional on (a) and (b)")
print("  RULING: "+"4059's 'both delta_CP contingencies are refuted' -- WITHDRAWN; they are OPEN")
print("\nT7 -- INDEPENDENT EXACT CHECK (rational arithmetic, no floats, no 600-cell code reused)")
from fractions import Fraction as Fr
def ffr(K,r):
    o=1
    for i in range(r): o*=(K-i)
    return o
for Kx in (3,10,1000):
    # F = n_a/(K p_a) - 1, Theta(F) = n_b/(K p_b) - 1, a != b, multinomial: E[n_a n_b] = K(K-1) p_a p_b
    val=Fr(ffr(Kx,2),Kx*Kx)-1-1+1
    chk(f"K={Kx}: <Theta(F)F> = {val} = -1/K exactly, p-free", val==Fr(-1,Kx))
    d=ffr(Kx,4)*ffr(Kx,2)-ffr(Kx,3)**2
    chk(f"K={Kx}: 4056's determinant K4*K2-K3^2 = {d} = -K^2(K-1)^2(K-2)", d==-(Kx**2)*(Kx-1)**2*(Kx-2))
    chk(f"K={Kx}: and in rescaled units it is O(1/K): d/K^6 = {float(Fr(d,Kx**6)):+.3e}", abs(Fr(d,Kx**6))<=Fr(1,Kx))
print("  QUANTIFIER (stated so the convenient branch is not overstated):")
print("   for ANY finite closed total K_tot the explicit F violates RP by exactly -1/K_tot.")
print("   H1 is restored ONLY as a property of the limit state, which is where VW-1 locates RP (CONT-1).")
print("   'H1 holds on every finite window' is NOT claimed and is false.")
print("  NOT RE-EXAMINED HERE: whether 4022's static spatial-reflection reading of H1 is VW-1's OS sense.")

print("\n  CONVENIENT BRANCH: this is it. It restores a hypothesis 40 live files lean on. It is")
print("  submitted, not adopted: the next window should attack T4 first (is H1 really a")
print("  thermodynamic-limit property for the substrate?) and (b).")
print(f"\n{'ALL CHECKS PASS' if fails==0 else str(fails)+' FAILURES'}")
print("NO verdict moved. FI-C-9 = V3; V1 EXCLUDED; H1 status: REFUTED -> OPEN (conditional).")
raise SystemExit(1 if fails else 0)
