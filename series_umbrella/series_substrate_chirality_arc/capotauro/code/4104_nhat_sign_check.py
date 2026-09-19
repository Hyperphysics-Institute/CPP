"""
TODO-4103-NHAT: does Capotauro v2.0's "sign of chi = sign of n-hat" survive
this lane's 4072 (-I4 is PROPER in R^4) and 4046 (Theta fixes n-hat)?

T1  Is n-hat -> -n-hat a chirality operation in R^4?      (4072)
T2  Is (600-cell, n-hat = v_host) achiral?                (4046)
T3  If both hold, the stated sign mechanism has no referent.
"""
import numpy as np, itertools
phi=(1+5**0.5)/2

def cell600():
    V=set()
    for i in range(4):
        for s in(1,-1):
            v=[0.]*4; v[i]=float(s); V.add(tuple(v))
    for s in itertools.product((.5,-.5),repeat=4): V.add(s)
    base=[0.,1/(2*phi),.5,phi/2]
    def par(p):
        return sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])%2
    for p in itertools.permutations(range(4)):
        if par(p)==0:
            vals=[base[p[i]] for i in range(4)]
            nz=[i for i in range(4) if abs(vals[i])>1e-12]
            for sg in itertools.product((1,-1),repeat=len(nz)):
                v=list(vals)
                for k,i in enumerate(nz): v[i]*=sg[k]
                V.add(tuple(v))
    A=np.array(sorted(V)); return A/np.linalg.norm(A,axis=1,keepdims=True)

V=cell600(); n=len(V)
print(f"600-cell built: {n} vertices")
assert n==120

def is_sym(M,tol=1e-9):
    P=(M@V.T).T
    return all(np.abs(V-p).max(1).min()<tol for p in P)

print("\nT1  is n-hat -> -n-hat a chirality operation in R^4?")
I4=-np.eye(4)
print(f"    det(-I4) = {np.linalg.det(I4):+.0f}   -> {'PROPER (a rotation)' if np.linalg.det(I4)>0 else 'improper'}")
print(f"    is -I4 a symmetry of the 600-cell? {is_sym(I4)}")
print("    => -I4 maps (600-cell, n) to (600-cell, -n) by a PROPER rotation:")
print("       the two configurations are CONGRUENT, not enantiomorphic.")
print("    T1: flipping the sign of n-hat selects NOTHING.  (confirms 4072)")

print("\nT2  is (600-cell, n-hat = v_host) achiral?")
print("    Need: an IMPROPER symmetry of the 600-cell that FIXES the chosen vertex.")
nhat=V[0]
# reflection in the hyperplane through the origin containing nhat, i.e. Householder
# in any direction r orthogonal to nhat: H_r fixes nhat and has det -1.
found=None
for r in V:
    if abs(r@nhat)>1e-9: continue                  # need r perpendicular to nhat
    H=np.eye(4)-2*np.outer(r,r)/(r@r)              # Householder reflection
    if abs(np.linalg.det(H)+1)<1e-9 and is_sym(H) and np.abs(H@nhat-nhat).max()<1e-9:
        found=(r,H); break
if found is not None:
    r,H=found
    print(f"    FOUND improper symmetry: Householder in r = {np.round(r,4)}")
    print(f"    det = {np.linalg.det(H):+.0f}   fixes n-hat? {np.abs(H@nhat-nhat).max()<1e-9}   600-cell symmetry? {is_sym(H)}")
    print("    => the pair (600-cell, n-hat) is mapped to itself by an IMPROPER operation")
    print("    T2: (600-cell, n-hat) is ACHIRAL.  (confirms 4046)")
else:
    print("    no improper symmetry fixing n-hat found -- 4046 would NOT be confirmed")

# how many such improper symmetries fix nhat?
cnt=0
for r in V:
    if abs(r@nhat)>1e-9: continue
    H=np.eye(4)-2*np.outer(r,r)/(r@r)
    if is_sym(H) and np.abs(H@nhat-nhat).max()<1e-9: cnt+=1
print(f"    improper symmetries of this shape fixing n-hat: {cnt}")

print("\nT3  consequence for Capotauro v2.0's stated sign mechanism")
print("    Claim under test: 'the sign of chi is fixed by which enantiomorph n-hat")
print("    selects (i.e., by the sign of n-hat itself)'.")
print("    T1: n-hat and -n-hat are related by a PROPER rotation -> same object.")
print("    T2: (600-cell, n-hat) admits an improper self-symmetry -> ACHIRAL, so")
print("        there are no two enantiomorphs for n-hat to select BETWEEN.")
print("    => the stated mechanism has no referent on this construction.")
print("\nNOTE: this does NOT touch |chi| = phi^-3 or |M| = chi/6, which are magnitudes.")

print("\n"+"="*62)
print("T4  FAIRNESS CHECK: does a GENERIC (non-vertex-aligned) n-hat escape T2?")
import numpy as np
# build full H4 symmetry group action test via all reflections in vertex directions
refl=[]
for r in V:
    H=np.eye(4)-2*np.outer(r,r)/(r@r)
    if is_sym(H): refl.append((r,H))
print(f"    improper (Householder) symmetries of the 600-cell available: {len(refl)}")
rng=np.random.default_rng(4104)
for lbl,nh in [("vertex-aligned n=v_host",V[0]),
               ("edge-midpoint direction",(V[0]+V[1])/np.linalg.norm(V[0]+V[1])),
               ("generic direction #1",None),("generic direction #2",None)]:
    if nh is None:
        nh=rng.normal(size=4); nh/=np.linalg.norm(nh)
    fix=sum(1 for r,H in refl if np.abs(H@nh-nh).max()<1e-9)
    print(f"    {lbl:26s} improper syms fixing n-hat: {fix:2d}  -> "
          f"{'ACHIRAL' if fix>0 else 'chiral (T2 escaped)'}")
print("""
    So T2 is specific to n-hat lying on a symmetry element (vertex, edge, face).
    A GENERIC n-hat does escape T2 -- consistent with 4063, which built a chiral
    4D structure from the 600-cell union a GENERIC H4+ orbit.

    But T1 is INDEPENDENT of that: -I4 is proper in R^4 for ANY n-hat, so
    'the sign of n-hat' never selects an enantiomorph, generic or not.
    T1 is the general refutation; T2 additionally kills the vertex-aligned
    reading FI-C-RC-2 that Capotauro actually cites.""")
