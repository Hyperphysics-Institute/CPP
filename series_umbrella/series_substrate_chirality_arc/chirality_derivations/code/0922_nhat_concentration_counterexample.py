import numpy as np, itertools
phi=(1+np.sqrt(5))/2
def even_perms(t):
    P=[p for p in itertools.permutations(range(4)) if sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])%2==0]
    return set(tuple(t[p[i]] for i in range(4)) for p in P)
def build_600cell():
    V=set()
    for i in range(4):
        for s in (1,-1): v=[0,0,0,0]; v[i]=s; V.add(tuple(v))
    for s in itertools.product([0.5,-0.5],repeat=4): V.add(s)
    for sg in itertools.product([1,-1],repeat=3):
        for w in even_perms([0,sg[0]*0.5,sg[1]*1/(2*phi),sg[2]*phi/2]): V.add(w)
    V=np.array(sorted(V)); N=len(V)
    D=np.sqrt(((V[:,None]-V[None])**2).sum(-1)); ed=D[D>1e-6].min(); A=np.abs(D-ed)<1e-6
    nbr=[list(map(int,np.where(A[v])[0])) for v in range(N)]
    return V,N,nbr

# 0922 — the n-hat-concentration counterexample that FALSIFIES 0827's "homogeneity => max=avg" step.
# Reproduces: homogeneous (same functional form) but n-hat-DEPENDENT concentration rules give
# avg row sum ~0.60 but MAX row sum = 1.0 and rho(M) = 1.0 at MEAN participation ~2.6 (NOT p=1),
# so max != avg. And: a POINTWISE floor (p(v)>=4 at every vertex) restores rho<1 (worst ~0.642).
V,N,nbr=build_600cell()
arc=lambda z:(2/np.pi)*np.arcsin(np.clip(z,-1,1))
def stats(cvec):
    M=np.zeros((N,N))
    for v in range(N):
        for k,w in enumerate(nbr[v]):
            kv=nbr[w].index(v); M[v,w]=arc(cvec[v][k]*cvec[w][kv])
    M=(M+M.T)/2; rs=np.abs(M).sum(1)
    return np.abs(np.linalg.eigvalsh(M)).max(), rs.max(), rs.mean()

print("Homogeneous n-hat-dependent rule c_e ~ |dir_e . n|^gamma (same form every vertex):")
print(f"{'n-hat':>14}{'gamma':>6}{'avg row':>9}{'MAX row':>9}{'rho':>8}")
for nm,nh in {'(1,1,1,1)':np.array([1.,1,1,1]),'(1,phi,phi2,phi3)':np.array([1,phi,phi**2,phi**3])}.items():
    nh=nh/np.linalg.norm(nh)
    for g in [0,12,200]:
        cvec=[]
        for v in range(N):
            al=np.array([abs((V[w]-V[v])@nh) for w in nbr[v]]); al/=al.max()+1e-12
            c=al**g+1e-9; c/=np.linalg.norm(c); cvec.append(c)
        rho,mx,av=stats(cvec); p=np.mean([1/np.sum(c**4) for c in cvec])
        print(f"{nm:>14}{g:6d}{av:9.4f}{mx:9.4f}{rho:8.4f}   (mean p={p:.2f})  {'<-- max!=avg, SUPER-CRIT' if mx>=0.999 else ''}")

print("\nPOINTWISE floor fix: mix uniform into the rule so every vertex has p>=4; rho collapses below 1:")
def make(nh,g,fm):
    nh=nh/np.linalg.norm(nh); cvec=[]
    for v in range(N):
        al=np.array([abs((V[w]-V[v])@nh) for w in nbr[v]]); al/=al.max()+1e-12
        c=al**g; c=c/(c.sum()+1e-12); c=(1-fm)*c+fm*(1/12); c=np.sqrt(c); c/=np.linalg.norm(c); cvec.append(c)
    return cvec
worst=0; rng=np.random.default_rng(5)
for _ in range(400):
    nh=rng.normal(size=4); g=rng.uniform(2,60); fm=rng.uniform(0,0.7)
    cvec=make(nh,g,fm); pmin=min(1/np.sum(c**4) for c in cvec)
    if pmin<4: continue
    rho,_,_=stats(cvec); worst=max(worst,rho)
print(f"   worst rho over 400 rules with pointwise min-participation >= 4:  {worst:.4f}  (margin {1-worst:.2f})")
print("=> 0827's max=avg is FALSE for n-hat-dependent eta; the correct floor is POINTWISE, not mean.")
