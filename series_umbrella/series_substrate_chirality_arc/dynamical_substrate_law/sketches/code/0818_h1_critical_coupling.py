import numpy as np, itertools
phi=(1+np.sqrt(5))/2
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
Dm=np.sqrt(((V[:,None]-V[None])**2).sum(-1)); edge=np.min(Dm[Dm>1e-6]); A=(np.abs(Dm-edge)<1e-6).astype(float)

# The H1 question, made concrete: model the lifted eta-field measure as an Ising-type
# measure on the 600-cell -- eta_v in {+-1} (local enantiomorph), symmetric/achiral base,
# coupling K induced by the lift. Off-critical (K<K_c) => finite chi => mu^2>0 => PRIMITIVE (V3).
# Ordered (K>K_c) => spontaneous eta condensation => mu^2<0 => EMERGENT (V3->V1).
# So the verdict reduces to a SINGLE comparison: is the lift-induced K below the lattice K_c?
lam=np.linalg.eigvalsh(A); lam_max=lam.max()
Kc_mf=1.0/lam_max
print(f"600-cell adjacency: N={N}, regular degree={int(A.sum(1)[0])}, lambda_max={lam_max:.4f}")
print(f"mean-field/RPA critical coupling  K_c = 1/lambda_max = {Kc_mf:.5f}  (= 1/12)")
print("  (true K_c is HIGHER: fluctuations raise it above mean-field => off-critical window is")
print("   AT LEAST K_lift < 1/12, and in reality wider.)\n")

# RPA susceptibility chi(K) = (1/N) sum_i 1/(1 - K lambda_i): finite below K_c, diverges at K_c
print("RPA susceptibility chi(K) (the off-criticality diagnostic):")
for K in [0.0,0.02,0.04,0.06,0.08,0.0825,0.0833]:
    if K*lam_max<1: chi=(1.0/N)*np.sum(1.0/(1-K*lam)); print(f"  K={K:.4f} (K/K_c={K/Kc_mf:5.2f}):  chi={chi:8.3f}")
    else: print(f"  K={K:.4f} (K/K_c={K/Kc_mf:5.2f}):  chi -> DIVERGES (critical/ordered)")
print("\nREFRAME: the verdict = sign(K_c - K_lift). K_c is computed above (mechanical, done).")
print("K_lift = the lift-induced eta-eta coupling, to be DERIVED from the Mechanism-A NESS.")
print("That derivation is a CALCULATION (given Mechanism A), NOT a PCD-mechanism invention --")
print("deriving Mechanism A itself (OPEN-FP-F1-2) is the separate, upstream PCD task.")
print(f"\nHeuristic lean (NOT a verdict): 0813's achiral base has <eta>~0 (no bare alignment) and")
print(f"the bias is O(delta) weak => K_lift is plausibly << 1/12 => off-critical => primitive (V3).")
print(f"Consistent with 0813's favorable finite-chi. The season's job is to DERIVE K_lift and confirm.")
