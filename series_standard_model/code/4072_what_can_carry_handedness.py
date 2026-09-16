"""4072 (EW lane) -- AXIOM MATURATION, step 1: what KIND of object can carry handedness in CPP, and is the
currently registered primitive (FI-C-9 = "which of {n_hat, -n_hat} is physical") one of them?

Founder direction (16 Sep): explore the axiom deeply and be fully convinced of its specifics and nature
BEFORE any panel. This script tests the two structural facts that decide the axiom's form.

M1  IS sign(n_hat) A CHIRALITY?  In R^4 the point inversion -I has det(-I) = (-1)^4 = +1: it is a PROPER
    rotation (by pi in two orthogonal planes). The 600-cell is centrally symmetric, so -I is in H4+.
    Then (600-cell, n_hat) and (600-cell, -n_hat) are related by a PROPER symmetry -- they are the SAME
    configuration turned around, NOT mirror images. "Which of {n_hat, -n_hat}" is not a handedness choice.
    Contrast R^3, where det(-I) = -1 and point inversion IS parity. The intuition imported from 3D fails.

M2  4071 REFINED -- the bivector route. 4071 proved a P-odd scalar from VECTORS needs four of them. But a
    single 4D ROTATION is a bivector B (6 components), and a bivector has its own quadratic pseudoscalar
        B ^ B = 2 (B01 B23 - B02 B13 + B03 B12)     (the Pfaffian).
    * a SIMPLE bivector (rotation in ONE plane -- the 3D-like spin) has B ^ B = 0 identically: no handedness.
    * a DOUBLE rotation (two orthogonal planes, both nonzero) has B ^ B != 0.
    * SELF-DUAL (left-isoclinic) gives B^B > 0; ANTI-SELF-DUAL (right-isoclinic) gives B^B < 0.
    * B^B is invariant under every PROPER rotation and FLIPS under every reflection.
    So ONE internal rotation suffices -- if and only if it is a DOUBLE rotation. This is the object 4071
    missed, and it is native to CPP: the ZBW is already a rotation.

M3  THE C / CP STRUCTURE the Standard Model demands (P and C each maximally violated, CP ~conserved).
    Rule under test: "the ZBW of a +CP is self-dual; of a -CP anti-self-dual" (duality = polarity x kappa).
    Check the truth table under P (mirror geometry), C (swap polarity), CP (both).

M4  CONTROL: the pseudoscalar detector is not blind -- it returns zero on simple rotations and nonzero,
    sign-flipping values on double rotations.
"""
import numpy as np, itertools
rng = np.random.default_rng(4072)
phi = (1 + 5**.5) / 2

def build600():
    Vs = []
    for i in range(4):
        for s in (1, -1):
            v = np.zeros(4); v[i] = s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s >> k) & 1) * 2 - 1 for k in range(4)]) / 2.0)
    b = [phi/2, 1/2, 1/(2*phi), 0]
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                sg = [b[0]*s1, b[1]*s2, b[2]*s3, b[3]]
                for pm in itertools.permutations(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm[i]>pm[j]) % 2 == 0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U = []
    for v in Vs:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    return np.array(U)

V = build600(); assert len(V) == 120
keys = {tuple(np.round(v, 9)) for v in V}

print("M1  is sign(n_hat) a chirality in 4D?")
mI = -np.eye(4)
print(f"    det(-I_4) = {np.linalg.det(mI):+.0f}   (R^3 would give -1)")
pres = all(tuple(np.round(mI @ v, 9)) in keys for v in V)
print(f"    -I_4 preserves the 600-cell: {pres}   => -I_4 is a PROPER symmetry in H4+")
nhat = V[0] / np.linalg.norm(V[0])
print(f"    -I_4 maps n_hat to -n_hat: {np.allclose(mI @ nhat, -nhat)}")
print(f"    => (600-cell, n_hat) and (600-cell, -n_hat) are CONGRUENT BY A ROTATION, not mirror images.")
print(f"       'Which of {{n_hat, -n_hat}} is physical' is NOT a handedness choice in R^4.")
assert pres and abs(np.linalg.det(mI) - 1) < 1e-12

def B_from_planes(a, b, c, d, w1, w2):
    """Bivector of a rotation with angular speed w1 in plane (a,b) and w2 in plane (c,d)."""
    B = w1 * (np.outer(a, b) - np.outer(b, a)) + w2 * (np.outer(c, d) - np.outer(d, c))
    return B

def pf(B):
    return 2.0 * (B[0,1]*B[2,3] - B[0,2]*B[1,3] + B[0,3]*B[1,2])

def ortho4():
    Q, _ = np.linalg.qr(rng.normal(size=(4,4)))
    if np.linalg.det(Q) < 0: Q[:, 0] *= -1
    return Q

print("\nM2  the bivector route: does ONE internal rotation carry a pseudoscalar?")
worst_simple = 0.0
for _ in range(20000):
    Q = ortho4()
    B = B_from_planes(Q[:,0], Q[:,1], Q[:,2], Q[:,3], rng.normal(), 0.0)   # single-plane
    worst_simple = max(worst_simple, abs(pf(B)))
print(f"    SIMPLE rotation (one plane, the 3D-like spin): max |B^B| = {worst_simple:.3e}  -> NO handedness")
assert worst_simple < 1e-9

vals = []
for _ in range(20000):
    Q = ortho4(); w1, w2 = rng.normal(), rng.normal()
    vals.append(pf(B_from_planes(Q[:,0], Q[:,1], Q[:,2], Q[:,3], w1, w2)))
vals = np.array(vals)
print(f"    DOUBLE rotation (two planes): min |B^B| = {np.abs(vals).min():.3e}, typical {np.median(np.abs(vals)):.3f}"
      f"  -> handedness EXISTS")

Q = ortho4()
SD  = B_from_planes(Q[:,0], Q[:,1], Q[:,2], Q[:,3], 1.0, +1.0)
ASD = B_from_planes(Q[:,0], Q[:,1], Q[:,2], Q[:,3], 1.0, -1.0)
print(f"    equal-speed double rotation, one sense  (isoclinic): B^B = {pf(SD):+.4f}")
print(f"    equal-speed double rotation, other sense(isoclinic): B^B = {pf(ASD):+.4f}   -> the two hands")

worst_rot = 0.0; worst_ref = 0.0
R = np.diag([1., 1, 1, -1])
for _ in range(5000):
    Q = ortho4(); w1, w2 = rng.normal(), rng.normal()
    B = B_from_planes(Q[:,0], Q[:,1], Q[:,2], Q[:,3], w1, w2)
    G = ortho4()
    worst_rot = max(worst_rot, abs(pf(G @ B @ G.T) - pf(B)))
    worst_ref = max(worst_ref, abs(pf(R @ B @ R.T) + pf(B)))
print(f"    under any PROPER rotation: max |change in B^B| = {worst_rot:.2e}  (invariant)")
print(f"    under a REFLECTION       : max |B^B + B^B'|    = {worst_ref:.2e}  (flips exactly)")
assert worst_rot < 1e-9 and worst_ref < 1e-9
print("    => a single DOUBLE rotation is a genuine P-odd object. 4071's 'four directions' threshold applies")
print("       to VECTOR attributes; a BIVECTOR attribute gets there with one object.")

print("\nM3  the C / CP pattern -- rule: +CP ZBW self-dual, -CP ZBW anti-self-dual")
def obeys(polarity, duality): return polarity == duality     # +1 <-> SD(+1), -1 <-> ASD(-1)
base = (+1, +1)                                              # a +CP with SD rotation: obeys the rule
ops = {"P  (mirror geometry)": lambda p, d: (p, -d),
       "C  (swap polarity)  ": lambda p, d: (-p, d),
       "CP (both)           ": lambda p, d: (-p, -d)}
print(f"    start: polarity {base[0]:+d}, duality {base[1]:+d}  obeys rule: {obeys(*base)}")
res = {}
for name, op in ops.items():
    q = op(*base); res[name.strip()[:2].strip()] = obeys(*q)
    print(f"    after {name}: polarity {q[0]:+d}, duality {q[1]:+d}  obeys rule: {obeys(*q)}"
          f"   => {'CONSERVED' if obeys(*q) else 'VIOLATED'}")
assert res["P"] is False and res["C"] is False and res["CP"] is True
print("    => P violated, C violated, CP conserved -- the Standard Model's weak-sector pattern, as a")
print("       LOGICAL CONSEQUENCE of tying duality to polarity, not as a fitted input.")

print("\nM4  CONTROL: detector returns 0 on simple rotations (M2) and flips sign on double ones -- not blind.")
