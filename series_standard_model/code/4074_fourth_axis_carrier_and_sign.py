"""4074 (EW lane) -- axiom maturation step 3: the founder's proposal -- use the 4th dimension.

Founder (16 Sep): the 4th dimension is an address on a 4th orthogonal axis, not visualizable, but existent
at the level of perception and interaction between CPs, processed by proximity; not yet used in CPP.

Coordinates (w, x, y, z): w = the 4th-axis address, (x, y, z) = physical 3-space.
Physical parity P = diag(+1, -1, -1, -1): inverts 3-space, leaves the 4th-axis address alone. det P = -1.

T1  WHAT IS P-ODD NOW. Under P: the w-address (P-even), displacement along w (P-even), a 3D spin
    b in (x,y,z) (P-even, axial), a rotation MIXING w with a spatial direction e (P-ODD), and the
    pseudoscalar  e . omega  (P-ODD). So once 3-space and the 4th axis are distinguished, the object
    that can carry handedness is exactly a w-mixing rotation aligned with a 3D spin.
T2  CARRIER YES, SIGN NO. A process whose rules are P-even produces the two signs of e . omega equally.
    The 4th axis supplies WHERE handedness can live without a new variable; it does not by itself choose
    the hand. Tested on the substrate's own rotations: the w-mixing rotations of H4+ come in exact
    left/right pairs.
T3  THE MERGE. Left-isoclinic rotation <=> e . omega > 0;  right-isoclinic <=> e . omega < 0.
    So L3 ("one of H4+'s two factors governs") and the founder's 4th-axis idea are the SAME rule seen from
    two sides: the rule is the SIGN of the alignment between 4th-axis mixing and 3D circulation.
T4  CONTROL: pure-3D rotations give exactly zero (S1 of 4073, now unconditional under the founder's
    identification of 3-space).
"""
import numpy as np, itertools
rng = np.random.default_rng(4074)
phi = (1 + 5**.5) / 2
P = np.diag([1., -1, -1, -1])

def pf(B): return 2.0 * (B[0,1]*B[2,3] - B[0,2]*B[1,3] + B[0,3]*B[1,2])
def wedge(a, b): return np.outer(a, b) - np.outer(b, a)
W = np.array([1., 0, 0, 0])

print("T1  parity behaviour once 3-space and the 4th-axis address are distinguished  (P = diag(+1,-1,-1,-1))")
print(f"    det P = {np.linalg.det(P):+.0f}")
pos = rng.normal(size=4)
print(f"    4th-axis address w of a CP:        {pos[0]:+.4f} -> {(P@pos)[0]:+.4f}    P-EVEN")
dw = np.array([0.7, 0, 0, 0])
print(f"    displacement along the 4th axis:   {dw[0]:+.4f} -> {(P@dw)[0]:+.4f}    P-EVEN")
b = wedge(np.array([0,1.,0,0]), np.array([0,0,1.,0]))            # 3D spin in the (x,y) plane
bP = P @ b @ P.T
print(f"    3D spin (x,y) component:           {b[1,2]:+.4f} -> {bP[1,2]:+.4f}    P-EVEN (axial)")
m = wedge(W, np.array([0,0,0,1.]))                               # rotation mixing w with z
mP = P @ m @ P.T
print(f"    4th-axis mixing rotation (w,z):    {m[0,3]:+.4f} -> {mP[0,3]:+.4f}    P-ODD")
worst = 0.0
for _ in range(20000):
    e = rng.normal(size=4); e[0] = 0
    om = rng.normal(size=3)
    bb = np.zeros((4,4)); bb[2,3], bb[3,1], bb[1,2] = om; bb = bb - bb.T
    B = wedge(W, e) + bb
    worst = max(worst, abs(pf(P @ B @ P.T) + pf(B)))
print(f"    pseudoscalar e.omega (= B^B/2):    flips exactly under P, max residual {worst:.1e}    P-ODD")
assert worst < 1e-10

print("\nT2  carrier yes, sign no: do the substrate's own 4th-axis-mixing rotations prefer a hand?")
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
V = build600()
def qmul(p, q):
    a1,b1,c1,d1 = p; a2,b2,c2,d2 = q
    return np.array([a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2,
                     a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2])
def Lmat(q): return np.column_stack([qmul(q, np.eye(4)[k]) for k in range(4)])
def Rmat(q): return np.column_stack([qmul(np.eye(4)[k], q) for k in range(4)])
from scipy.linalg import logm
pos_n = neg_n = 0; tot = 0.0
for q in V:
    if abs(abs(q[0]) - 1) < 1e-9 or abs(q[0] + 1) < 1e-9: continue      # identity / -identity
    for M in (Lmat(q), Rmat(q)):
        B = np.real(logm(M))
        s = pf(B)
        if abs(s) < 1e-9: continue
        tot += s; pos_n += s > 0; neg_n += s < 0
print(f"    left+right multiplications by all 118 non-trivial vertices: {pos_n} positive, {neg_n} negative")
print(f"    net handedness summed over the substrate's rotations = {tot:+.3e}")
print(f"    => the 4th axis gives handedness a PLACE to live; the substrate's P-even structure gives both")
print(f"       signs equally. A rule is still needed to choose the sign.")
assert pos_n == neg_n and abs(tot) < 1e-9

print("\nT3  the merge: is 'left-isoclinic' the same thing as 'e.omega > 0'?")
agree = 0; n = 0
for q in V:
    if abs(abs(q[0]) - 1) < 1e-9: continue
    for M, hand in ((Lmat(q), "L"), (Rmat(q), "R")):
        B = np.real(logm(M))
        e = B[0, :].copy(); e[0] = 0                   # the w-mixing partner direction
        om = np.array([B[2,3], B[3,1], B[1,2]])        # 3D spin axis of the purely spatial part
        eo = float(e[1:] @ om)
        if abs(eo) < 1e-9: continue
        n += 1
        agree += ((hand == "L") == (eo < 0)) or ((hand == "R") == (eo > 0))
consistent = agree in (0, n)
print(f"    over {n} substrate rotations: sign(e.omega) separates left from right in {max(agree, n-agree)}/{n} cases")
print(f"    => one-to-one: {consistent}. The left/right factor IS the sign of the 4th-axis/3D-spin alignment.")
assert consistent and n > 0

print("\nT4  CONTROL: rotations confined to 3-space (the founder's physical space) are never handed")
worst = 0.0
for _ in range(20000):
    B = np.zeros((4,4))
    for _ in range(rng.integers(1, 6)):
        a = rng.normal(size=4); a[0] = 0; c = rng.normal(size=4); c[0] = 0
        B += rng.normal() * wedge(a, c)
    worst = max(worst, abs(pf(B)))
print(f"    max |B^B| = {worst:.1e}  -- S1 of 4073 is now UNCONDITIONAL under the founder's identification")
assert worst < 1e-10

print("\nCONCLUSION")
print("  The founder's 4th axis is the right CARRIER, and it needs no new variable. It does not by itself")
print("  choose the SIGN. The one rule that does is: 'when CP interaction mixes the 4th axis with 3-space,")
print("  the mixing and the 3D circulation are aligned in one sense' -- which is exactly L3. L2 and L3 merge.")
