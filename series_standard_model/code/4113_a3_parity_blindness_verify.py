import numpy as np, itertools
phi=(1+5**0.5)/2
def ico():
    V=[]
    for s1 in(1,-1):
        for s2 in(1,-1): V+=[(0,s1,s2*phi),(s1,s2*phi,0),(s2*phi,0,s1)]
    V=np.array(V,float); return V/np.linalg.norm(V,axis=1,keepdims=True)
V=ico(); n=len(V)
# pick a linearly independent reference triple
ref=None
for t in itertools.combinations(range(n),3):
    B=V[list(t)].T
    if abs(np.linalg.det(B))>1e-6: ref=t; B0=B; break
G0=np.linalg.inv(B0)
gram0=V[list(ref)]@V[list(ref)].T
Ih=[]
for t in itertools.permutations(range(n),3):
    W=V[list(t)]
    if np.abs(W@W.T-gram0).max()>1e-9: continue      # same mutual geometry
    M=W.T@G0
    if np.abs(M@M.T-np.eye(3)).max()>1e-9: continue  # orthogonal
    if any(np.abs(V-p).max(1).min()>1e-9 for p in (M@V.T).T): continue  # symmetry
    if not any(np.abs(M-S).max()<1e-9 for S in Ih): Ih.append(M)
I=[M for M in Ih if np.linalg.det(M)>0]
print(f"|I| (proper) = {len(I)},  |I_h| (full) = {len(Ih)}")
assert len(I)==60 and len(Ih)==120

chi_p=np.array([np.trace(M) for M in Ih])
chi_a=np.array([np.linalg.det(M)*np.trace(M) for M in Ih])
ip=lambda x,y: float(np.dot(x,y))/len(Ih)
print(f"\nOn the FULL group I_h:")
print(f"  <chi_polar,chi_polar> = {ip(chi_p,chi_p):.4f}   (1 => irreducible)")
print(f"  <chi_axial,chi_axial> = {ip(chi_a,chi_a):.4f}   (1 => irreducible)")
print(f"  <chi_polar,chi_axial> = {ip(chi_p,chi_a):.4f}   (0 => INEQUIVALENT irreps)")
assert abs(ip(chi_p,chi_p)-1)<1e-9 and abs(ip(chi_a,chi_a)-1)<1e-9 and abs(ip(chi_p,chi_a))<1e-9

cp=np.array([np.trace(M) for M in I]); ca=np.array([np.linalg.det(M)*np.trace(M) for M in I])
print(f"\nOn the PROPER group I only:")
print(f"  max |chi_polar - chi_axial| = {np.abs(cp-ca).max():.1e}  => IDENTICAL characters")
print("  A rotation-only enumeration CANNOT distinguish polar from axial.")
print(f"\n  I_h improper elements: {sum(1 for M in Ih if np.linalg.det(M)<0)}")
