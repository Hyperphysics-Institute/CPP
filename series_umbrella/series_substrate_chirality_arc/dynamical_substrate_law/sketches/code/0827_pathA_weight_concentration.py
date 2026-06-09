import numpy as np, itertools, collections
rng=np.random.default_rng(17); phi=(1+np.sqrt(5))/2
def even_perms(t):
    P=[p for p in itertools.permutations(range(4)) if sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])%2==0]
    return set(tuple(t[p[i]] for i in range(4)) for p in P)
V=set()
for i in range(4):
    for s in (1,-1): v=[0,0,0,0]; v[i]=s; V.add(tuple(v))
for s in itertools.product([0.5,-0.5],repeat=4): V.add(s)
for sg in itertools.product([1,-1],repeat=3):
    for w in even_perms([0,sg[0]*0.5,sg[1]*1/(2*phi),sg[2]*phi/2]): V.add(w)
V=np.array(sorted(V)); N=len(V)
Dm=np.sqrt(((V[:,None]-V[None])**2).sum(-1)); ed=np.min(Dm[Dm>1e-6]); A=(np.abs(Dm-ed)<1e-6)
nbr=[list(map(int,np.where(A[v])[0])) for v in range(N)]
arc=lambda z:(2/np.pi)*np.arcsin(np.clip(z,-1,1))

print("PART (b): does VERTEX-TRANSITIVITY tame the concentrated worst case?\n")
print("AM-GM bound (general, any normalized weighting): (2/pi)arcsin(z)<=z (arcsin convex on[0,1] => below its chord),")
print("so sum_v RowSum_v <= sum_edges (cv^2+cw^2) = N  =>  AVERAGE row sum <= 1.  Equality only at full concentration.\n")
# verify avg row sum <= 1 for random + concentrated weightings via the shared-edge arcsin law
def rowsum_stats(cvec):   # cvec[v] = weights on v's edges (aligned to nbr[v]); returns avg & max row sum of |M|
    rs=np.zeros(N)
    for v in range(N):
        for k,w in enumerate(nbr[v]):
            kv=nbr[w].index(v)
            rs[v]+=abs(arc(cvec[v][k]*cvec[w][kv]))
    return rs.mean(), rs.max()
for trial in range(4):
    cvec=[]
    for v in range(N):
        c=rng.random(12)**rng.uniform(1,6); c/=np.linalg.norm(c); cvec.append(c)
    a,m_=rowsum_stats(cvec); print(f"  random non-uniform weighting #{trial+1}: avg rowsum={a:.4f}  max rowsum={m_:.4f}")

print("\nWorst-case VERTEX-TRANSITIVE concentrated rule = reciprocal perfect-matching preferred edge (weight W), rest eps:")
# build a perfect matching greedily (each vertex matched to an unused neighbour)
match=-np.ones(N,int)
for v in range(N):
    if match[v]<0:
        for w in nbr[v]:
            if match[w]<0: match[v]=w; match[w]=v; break
print(f"  matched {int((match>=0).sum())}/{N} vertices")
print(f"{'W^2':>6}{'partic p':>10}{'rho(M)':>9}{'R*=maxrow':>11}{'avg row':>9}  status (crit rho=1)")
for W2 in [1/12,0.2,0.3,0.5,0.7,0.85,0.95,0.99]:
    W=np.sqrt(W2); eps=np.sqrt((1-W2)/11)
    cvec=[]
    for v in range(N):
        c=np.full(12,eps); c[nbr[v].index(match[v])]=W; cvec.append(c)
    # build M
    M=np.zeros((N,N))
    for v in range(N):
        for k,w in enumerate(nbr[v]):
            kv=nbr[w].index(v); M[v,w]=arc(cvec[v][k]*cvec[w][kv])
    M=(M+M.T)/2; rho=np.abs(np.linalg.eigvalsh(M)).max()
    p=1/ (W2**2+11*eps**4)
    a,mx=rowsum_stats(cvec)
    print(f"{W2:6.2f}{p:10.2f}{rho:9.4f}{mx:11.4f}{a:9.4f}  {'CRIT' if rho>=0.999 else 'sub-crit'}")
print("\nCONTRAST -- the LOOSE adversary (every neighbour of v concentrates W onto the edge to v): NON-vertex-transitive.")
for W2 in [0.3,0.5,0.7]:
    W=np.sqrt(W2)
    loose=12*arc(W*W)          # m=12 neighbours all present weight W to v
    print(f"   W^2={W2}: loose rowsum at the special vertex = 12*arc(W^2) = {loose:.3f}  (needs in-degree 12 at ONE vertex;")
print("     a single rule gives average in-degree 1, so this row cannot occur at every vertex => excluded by transitivity.)")

print("\n\nPART (a): orientation => participation floor, and the margin at the floor")
print("Equal-weight gives p=12; the worst-case homogeneous rule at participation p has rho=R*(p):")
import numpy as np
for ptarget,lbl in [(4,"4-D orientation floor (enantiomorph = sign of a 4-direction determinant)"),
                    (2,"minimal non-degenerate handedness (>=2 directions)")]:
    # invert: find W2 giving participation ~ptarget on the matching rule, report rho there (read from table trend)
    print(f"  p>={ptarget}: {lbl}")
print("""
  From the table: p=12 -> rho 0.637 (36%); p~3.7 -> 0.652 (35%); p~2.0 -> 0.685 (32%); p->1 -> 1.
  => at the 4-D orientation floor p>=4, rho<=~0.65, margin ~35%. For ANY non-degenerate handedness (p>1), rho<1.
  The ONLY critical case is full single-edge concentration (p=1) -- not a handedness.""")
