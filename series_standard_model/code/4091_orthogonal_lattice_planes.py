"""4091 (EW lane) -- does the 600-cell supply two ORTHOGONAL orbital planes (the missing second leg)?

4090 left this: SPIN-1's two orbits are coplanar, so they cannot form a double rotation; the w-leg is doing
all the unexplained work. SPIN-1 conjectures that colour "may emerge from the three possible orbital planes
of the qDP in the 600-cell geometry". If two of those planes were ORTHOGONAL, the double rotation would come
from existing geometry and the w-leg would be unnecessary.

T1  A DIMENSIONAL FACT FIRST: in R^4 two orthogonal 2-planes already span the space, so THREE mutually
    orthogonal 2-planes cannot exist. SPIN-1's three colour planes therefore cannot be mutually orthogonal
    -- whatever they are. The question is only whether some PAIR is orthogonal.
T2  Enumerate the lattice 2-planes at a 600-cell vertex: planes spanned by pairs of the 12 neighbour
    directions. For each, test whether its orthogonal complement is ALSO a lattice plane (spanned by
    lattice directions). Orthogonal lattice pairs are what a double rotation needs.
T3  If such pairs exist, count them and check whether they come in threes (which colour would need).
T4  CONTROL: the count must be invariant under relabelling the vertex -- checked on a second vertex.
"""
import numpy as np, itertools
phi=(1+5**.5)/2

def build600():
    Vs=[]
    for i in range(4):
        for s in (1,-1):
            v=np.zeros(4); v[i]=s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s>>k)&1)*2-1 for k in range(4)])/2.0)
    b=[phi/2,1/2,1/(2*phi),0]
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                sg=[b[0]*s1,b[1]*s2,b[2]*s3,b[3]]
                for pm in itertools.permutations(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm[i]>pm[j])%2==0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U=[]
    for v in Vs:
        if not any(np.allclose(v,u,atol=1e-9) for u in U): U.append(v)
    return np.array(U)

V=build600(); N=len(V); em=1/phi
D=np.linalg.norm(V[:,None]-V[None],axis=2)

print("T1  dimensional fact")
print("    two orthogonal 2-planes span R^4 (2+2 = 4), so THREE mutually orthogonal 2-planes cannot exist.")
print("    => SPIN-1's three colour planes CANNOT be mutually orthogonal, whatever else they are.")
print("       Only a PAIR can be, and a pair is all a double rotation needs.")

def lattice_dirs(vi, neighbours_only=False):
    """WIDENED (in-patch): the orthogonal complement of a neighbour-spanned plane may be spanned by
    directions to NON-neighbour vertices, so the honest test uses ALL 119 vertex-difference directions,
    not just the 12 nearest neighbours."""
    if neighbours_only:
        nb = np.flatnonzero(np.abs(D[vi]-em)<1e-9)
        return np.array([V[j]-V[vi] for j in nb])
    return np.array([V[j]-V[vi] for j in range(len(V)) if j != vi])

def plane_basis(u, w):
    A = np.stack([u, w]); q, _ = np.linalg.qr(A.T)
    return q[:, :2]

def is_lattice_plane(Q, dirs, tol=1e-7):
    """does the plane spanned by Q contain at least two independent lattice directions?"""
    inside = [d for d in dirs if np.linalg.norm(d - Q@(Q.T@d)) < tol*max(1,np.linalg.norm(d))]
    if len(inside) < 2: return False
    M = np.array(inside)
    return np.linalg.matrix_rank(M, tol=1e-7) >= 2

def count_orthogonal_pairs(vi, verbose=False):
    nbdirs = lattice_dirs(vi, neighbours_only=True)
    dirs = lattice_dirs(vi)                       # all 119 directions, for the complement test
    planes = []
    for a, b in itertools.combinations(range(len(nbdirs)), 2):
        Q = plane_basis(nbdirs[a], nbdirs[b])
        if not any(np.allclose(abs(Q.T@P), np.eye(2), atol=1e-7) for P in planes):
            planes.append(Q)
    hits = 0
    for Q in planes:
        # orthogonal complement basis
        M = np.eye(4) - Q@Q.T
        w_, vecs = np.linalg.eigh(M)
        C = vecs[:, w_ > 0.5]
        if is_lattice_plane(C, dirs): hits += 1
    return len(planes), hits

np_, hits = count_orthogonal_pairs(0)
print(f"\nT2  at vertex 0: distinct lattice 2-planes spanned by neighbour pairs = {np_}")
print(f"    of these, how many have an orthogonal complement spanned by lattice directions\n    (tested against ALL 119 vertex-difference directions, not just the 12 neighbours): {hits}")

np2, hits2 = count_orthogonal_pairs(7)
print(f"\nT4  CONTROL at a different vertex: planes = {np2}, orthogonal-complement lattice planes = {hits2}")
print(f"    counts match: {np_==np2 and hits==hits2}")

# T5: can an orthogonal pair avoid the 4th axis (i.e. both planes inside physical 3-space)?
print("\nT5  can such a pair live entirely in physical 3-space?")
nhat = V[0]/np.linalg.norm(V[0])
dirs0 = lattice_dirs(0); nb0 = lattice_dirs(0, neighbours_only=True)
worst_out = 1e9; checked = 0
for a,b in itertools.combinations(range(len(nb0)), 2):
    Q = plane_basis(nb0[a], nb0[b])
    M = np.eye(4) - Q@Q.T
    wv, vecs = np.linalg.eigh(M); C = vecs[:, wv > 0.5]
    if not is_lattice_plane(C, dirs0): continue
    checked += 1
    # how much of the PAIR lies outside the 3-space orthogonal to n_hat?
    out = max(np.linalg.norm(Q.T@nhat), np.linalg.norm(C.T@nhat))
    worst_out = min(worst_out, out)
print(f"    over {checked} orthogonal pairs, the SMALLEST out-of-3-space component of either plane = {worst_out:.4f}")
print("    => never zero. Dimensionally forced: two orthogonal 2-planes span R^4, while physical 3-space is")
print("       only 3-dimensional, so at least one plane must have a component along the 4th axis.")
print("    => the 4th-axis motion is NOT avoided by using lattice planes -- it is REQUIRED BY THE GEOMETRY.")
print("       The founder's oscillation is what orbiting in such a plane MEANS, rather than an extra postulate.")

print("\nT3  verdict")
if hits == 0:
    print("    NO lattice plane at a vertex has a lattice plane as its orthogonal complement.")
    print("    => the 600-cell's neighbour geometry does NOT supply two orthogonal orbital planes.")
    print("       Colour-as-three-planes cannot furnish the double rotation, and the w-leg is NOT")
    print("       replaceable by existing 600-cell geometry. The founder's oscillation remains required.")
else:
    print(f"    {hits} of {np_} neighbour-spanned planes have a lattice orthogonal complement.")
    print("    => the 600-cell DOES supply orthogonal plane pairs: the double rotation can be built from")
    print("       EXISTING lattice geometry, with no new oscillation postulated.")
    print("    => but (T5) any such pair necessarily leaves physical 3-space, so the 4th-axis motion is")
    print("       REQUIRED rather than avoided. The founder's oscillation is GROUNDED, not eliminated.")
    print("    => and, as at every previous step, BOTH hands are available: geometry still supplies no SIGN.")
