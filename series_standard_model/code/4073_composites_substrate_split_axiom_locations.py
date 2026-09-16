"""4073 (EW lane) -- axiom maturation step 2, after the founder's answers:
  Q3: antiparticle = same CP with opposite polarity (CONFIRMED; F9 resolved).
  Q1/Q2: a CP has no second plane or second parameter to rotate in; a spin direction/pole or second plane
         would be an AXIOMATIC ADDITION.
But SPIN-1 derives spin from a captured DP ORBITING the CP in a plane -- composites DO rotate. So before
declaring an axiom unavoidable: can COMPOSITE rotations supply handedness with no new variable?

S1  THE 3-SPACE THEOREM. B^B is a 4-form: it needs all four dimensions. So ANY rotation, or ANY SUM of
    rotations (any number of orbits, planes, composites), confined to a 3-dimensional subspace has
    B^B = 0 identically. If CPP's physical rotations (ZBW transverse plane, SPIN-1 orbits, qDP colour
    planes) all live in the 3-space orthogonal to n_hat, NO composite can ever be handed.
S2  WHAT HANDEDNESS NEEDS. Write B = n_hat ^ e + b, with e orthogonal to n_hat and b a bivector in the
    3-space orthogonal to n_hat, omega = its 3D axial dual. Then B^B = 2 n_hat^e^b is proportional to
    e . omega. Handedness requires a rotation in a plane CONTAINING n_hat, aligned with the 3D spin axis.
    The pseudoscalar is HELICITY-SHAPED: a projection of the spin axis onto the 4th-direction partner.
S3  THE SUBSTRATE'S OWN L/R SPLIT. The 600-cell's vertices are the 120 unit quaternions of the binary
    icosahedral group 2I. Left multiplication x -> q x and right multiplication x -> x q both preserve
    the 600-cell, are isoclinic, and carry OPPOSITE duality. A reflection exchanges them. So the
    left/right structure is ALREADY in H4+ = (2I x 2I)/Z2 -- in the substrate's symmetry, though in
    no CP variable.
S4  CONTROL: detector nonzero with correct signs where handedness exists (S2, S3).
"""
import numpy as np, itertools
rng = np.random.default_rng(4073)
phi = (1 + 5**.5) / 2

def pf(B): return 2.0 * (B[0,1]*B[2,3] - B[0,2]*B[1,3] + B[0,3]*B[1,2])
def wedge(a, b): return np.outer(a, b) - np.outer(b, a)

print("S1  rotations confined to the 3-space orthogonal to n_hat -- can any sum of them be handed?")
nhat = np.array([1.0, 0, 0, 0])
worst = 0.0
for _ in range(20000):
    B = np.zeros((4,4))
    for _ in range(rng.integers(1, 6)):                 # up to five composite rotations / orbits
        a = rng.normal(size=4); a[0] = 0
        b = rng.normal(size=4); b[0] = 0
        B += rng.normal() * wedge(a, b)
    worst = max(worst, abs(pf(B)))
print(f"    up to 5 superposed rotations, all orthogonal to n_hat: max |B^B| = {worst:.3e}")
print(f"    => IDENTICALLY ZERO. No composite confined to 3-space can carry handedness, however many planes.")
assert worst < 1e-10

print("\nS2  what handedness needs: B = n_hat^e + b  =>  B^B proportional to e . omega")
worst = 0.0
for _ in range(20000):
    e = rng.normal(size=4); e[0] = 0
    b3 = rng.normal(size=3)                               # 3D axial vector omega
    b = np.zeros((4,4))
    b[2,3], b[3,1], b[1,2] = b3[0], b3[1], b3[2]
    b = b - b.T
    B = wedge(nhat, e) + b
    pred = 2.0 * float(e[1:] @ b3)
    worst = max(worst, abs(pf(B) - pred))
print(f"    max |B^B - 2 e.omega| over 20000 draws = {worst:.3e}")
print(f"    => the pseudoscalar is exactly the ALIGNMENT of the 3D spin axis omega with the partner direction e")
print(f"       of a rotation in a plane containing n_hat. Helicity-shaped. Requires a rotation INTO the 4th axis.")
assert worst < 1e-10

print("\nS3  the substrate's own left/right split (600-cell vertices = unit quaternions of 2I)")
def build600():
    Vs = []
    for i in range(4):
        for s in (1, -1):
            v = np.zeros(4); v[i] = s; Vs.append(v)
    for s in range(16): Vs.append(np.array([((s >> k) & 1) * 2 - 1 for k in range(4)]) / 2.0)
    bb = [phi/2, 1/2, 1/(2*phi), 0]
    for s1 in (1,-1):
        for s2 in (1,-1):
            for s3 in (1,-1):
                sg = [bb[0]*s1, bb[1]*s2, bb[2]*s3, bb[3]]
                for pm in itertools.permutations(range(4)):
                    if sum(1 for i in range(4) for j in range(i+1,4) if pm[i]>pm[j]) % 2 == 0:
                        Vs.append(np.array([sg[pm[i]] for i in range(4)]))
    U = []
    for v in Vs:
        if not any(np.allclose(v, u, atol=1e-9) for u in U): U.append(v)
    return np.array(U)
V = build600(); keys = {tuple(np.round(v, 8)) for v in V}

def qmul(p, q):
    a1,b1,c1,d1 = p; a2,b2,c2,d2 = q
    return np.array([a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2,
                     a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2])
closed = all(tuple(np.round(qmul(p, q), 8)) in keys for p in V[:30] for q in V[:30])
print(f"    600-cell vertices closed under quaternion multiplication (spot 900 products): {closed}")
assert closed

def Lmat(q): return np.column_stack([qmul(q, np.eye(4)[k]) for k in range(4)])
def Rmat(q): return np.column_stack([qmul(np.eye(4)[k], q) for k in range(4)])

# pick a vertex that is a small rotation: q = cos(t) + sin(t) u
q = min((v for v in V if v[0] < 0.999), key=lambda v: -v[0])
L, R = Lmat(q), Rmat(q)
pres_L = all(tuple(np.round(L @ v, 8)) in keys for v in V)
pres_R = all(tuple(np.round(R @ v, 8)) in keys for v in V)
print(f"    q = {np.round(q,4)}:  left-mult preserves 600-cell {pres_L};  right-mult preserves {pres_R}")
from scipy.linalg import logm
BL = np.real(logm(L)); BR = np.real(logm(R))
print(f"    generator of LEFT  multiplication: B^B = {pf(BL):+.6f}")
print(f"    generator of RIGHT multiplication: B^B = {pf(BR):+.6f}")
print(f"    opposite duality: {np.sign(pf(BL)) == -np.sign(pf(BR)) and abs(pf(BL)) > 1e-6}")
assert pres_L and pres_R and np.sign(pf(BL)) == -np.sign(pf(BR))
Refl = np.diag([1., -1, -1, -1])              # quaternion conjugation: an improper map (det -1)
swap = np.allclose(Refl @ L @ Refl, Rmat(qmul(np.array([1,0,0,0.]), np.array([q[0],-q[1],-q[2],-q[3]]))), atol=1e-9) \
       or np.allclose(Refl @ L @ Refl, Rmat(np.array([q[0],-q[1],-q[2],-q[3]])), atol=1e-9)
print(f"    det(conjugation) = {np.linalg.det(Refl):+.0f};  conjugation turns left-mult into right-mult: {swap}")
assert swap
print("    => H4+ already contains BOTH hands as separate factors, and a mirror exchanges them.")
print("       The substrate's symmetry group is handed-SPLIT; nothing in the axioms prefers one factor.")

print("\nCONCLUSION")
print("  (1) Founder's answers stand and are sharpened: not only does a CP lack a second plane -- NO composite")
print("      confined to physical 3-space can be handed either, however many orbits it has (S1).")
print("  (2) Handedness needs a rotation into the 4th axis, aligned with a 3D spin axis (S2): a helicity.")
print("  (3) The 600-cell's own symmetry already splits into left and right isoclinic factors (S3).")
print("  => An axiom is required, and it has three distinct possible LOCATIONS: a new CP variable, a new")
print("     rotation into the 4th axis, or a rule selecting one of the substrate's two existing factors.")
