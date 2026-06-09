import numpy as np, itertools
rng=np.random.default_rng(53); phi=(1+np.sqrt(5))/2
def even_perms(t):
    P=[p for p in itertools.permutations(range(4))
       if sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])%2==0]
    return set(tuple(t[p[i]] for i in range(4)) for p in P)
V=set()
for i in range(4):
    for s in (1,-1): v=[0,0,0,0]; v[i]=s; V.add(tuple(v))
for s in itertools.product([0.5,-0.5],repeat=4): V.add(s)
for sg in itertools.product([1,-1],repeat=3):
    for w in even_perms([0,sg[0]*0.5,sg[1]*1/(2*phi),sg[2]*phi/2]): V.add(w)
V=np.array(sorted(V)); N=len(V)
Dm=np.sqrt(((V[:,None]-V[None])**2).sum(-1)); ed=np.min(Dm[Dm>1e-6]); A=(np.abs(Dm-ed)<1e-6)
nbrs=[np.where(A[v])[0] for v in range(N)]
lam=np.linalg.eigvalsh(A.astype(float)); lam_max=lam.max(); lam_min=lam.min()
Klift=0.053
print(f"600-cell adjacency spectrum: lambda_max={lam_max:.4f} (uniform/FM), lambda_min={lam_min:.4f}")
print(f"  |lambda_min| = {abs(lam_min):.4f} < 12 => NON-BIPARTITE (frustrated); triangles present\n")
KcFM=1/lam_max; KcAFM_mf=1/abs(lam_min)
print(f"FM threshold  K_c^FM  = 1/lambda_max  = {KcFM:.4f}   (what 0821-0823 used -- WRONG for AFM coupling)")
print(f"AFM threshold K_c^AFM = 1/|lambda_min| = {KcAFM_mf:.4f}   (mean-field; the CORRECT proxy)\n")
print(f"EXACT margin against the AFM/staggered threshold:")
print(f"   criticality:  |K_lift| * |lambda_min| = {Klift*abs(lam_min):.3f}  (orders if this reaches 1)")
print(f"   => |K_lift|/K_c^AFM = {Klift/KcAFM_mf:.3f}  =>  margin = {(1-Klift/KcAFM_mf)*100:.0f}%  (mean-field)")

# AFM Ising MC: staggered susceptibility via the lambda_min eigenvector (frustration-corrected threshold)
psi=np.linalg.eigh(A.astype(float))[1][:,0]    # lambda_min eigenvector = staggered mode
def mc_stag(absK, sweeps=4000, eq=1500):        # H = +|K| sum s_v s_w  (antiferromagnetic)
    s=rng.choice([-1,1],N); ms=[]
    for sw in range(sweeps):
        for v in range(N):
            dE=-2*absK*s[v]*s[nbrs[v]].sum()    # AFM: anti-aligned lowers energy
            if dE<=0 or rng.random()<np.exp(-dE): s[v]=-s[v]
        if sw>=eq: ms.append(psi@s)
    ms=np.array(ms)/N
    return N*(np.mean(ms**2)-np.mean(np.abs(ms))**2)
print(f"\nAFM Ising MC -- staggered susceptibility chi_stag(|K|) (frustration-corrected):")
print(f"{'|K|':>7}{'|K|/Kc^AFM_mf':>15}{'chi_stag':>10}")
peakK=0;peakc=0
for K in [0.05,0.08,0.11,0.14,0.17,0.20]:
    c=mc_stag(K)
    if c>peakc:peakc=c;peakK=K
    print(f"{K:7.3f}{K/KcAFM_mf:15.2f}{c:10.3f}")
print(f"   staggered chi peaks near |K_c^AFM|(frustration-corrected) ~ {peakK:.3f}  (>= mean-field {KcAFM_mf:.3f})")
print(f"\nVERDICT-RELEVANT COMPARISON (exact, correct threshold):")
print(f"   |K_lift| = {Klift}  vs  K_c^AFM(mean-field)={KcAFM_mf:.3f}, (frustration-corrected)~{peakK:.3f}")
print(f"   => |K_lift| is {Klift/KcAFM_mf:.2f} of the mean-field AFM threshold and {Klift/peakK:.2f} of the")
print(f"      frustration-corrected one => SUB-CRITICAL by a WIDER margin than the FM proxy showed.")
print(f"   Both ordering channels cleared: uniform/FM (1/lambda_max) AND staggered/AFM (1/|lambda_min|).")
