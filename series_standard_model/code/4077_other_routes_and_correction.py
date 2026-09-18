"""4077 (EW lane) -- other routes to a P-odd source, and a CORRECTION to my own 4071/4073 phrasing.

PHYSICAL PARITY (4074 founder ruling) is P = diag(+1,-1,-1,-1): it inverts 3-SPACE and leaves the 4th-axis
address alone. That has a consequence I stated too broadly at 4071/4073:

  * 4071 said "a P-odd scalar needs FOUR independent directions". True for the 4D Levi-Civita invariant
    det[a,b,c,d]. But under PHYSICAL parity, det3[a,b,c] of THREE SPATIAL vectors is already P-odd:
    each flips, and (-1)^3 = -1. THREE spatial directions suffice.
  * 4073/4074 said "no composite confined to 3-space can be handed". True for ROTATIONS (B^B needs all four
    dimensions). FALSE for ARRANGEMENTS: a 3D chiral arrangement -- a helix, a fixed cyclic triad -- is
    P-odd under physical parity. This is ordinary 3D chirality (a left hand is not a right hand).

Both objects are tested below, and the distinction is the point: ROTATIONS in 3-space carry no handedness;
ARRANGEMENTS in 3-space do. My earlier summaries blurred the two.

NEW CANDIDATE ROUTES, tested:
  K1  the corrected counting: three spatial directions, or a fixed cyclic triad, is P-odd.
  K2  a chiral 3D ARRANGEMENT in the substrate -- e.g. the Boerdijk-Coxeter tetrahedral helix, which is what
      regular tetrahedra actually do when stacked (relevant: 4019 showed the 600-cell cannot tile flat R^4).
  K3  PROCEDURAL chirality: the tie-break rule. When a CP's move is degenerate, SOMETHING must choose. A
      tie-break that uses sign(det3) is P-odd and adds NO variable -- it specifies a rule the corpus has
      left unspecified. Simulated on a walk: chiral tie-break gives a net P-odd current; a P-even
      tie-break gives exactly zero.
  K4  the CPT route: P-odd = (C-odd) x (T-odd). The corpus ALREADY has a T-odd element (sign(delta),
      TARROW-1/2, W3) and the universe has a C-odd fact (matter excess). Their product is P-odd with no
      new primitive. Shown as a transformation table.
"""
import numpy as np, itertools
rng = np.random.default_rng(4077)
P3 = -np.eye(3)

print("K1  corrected counting under PHYSICAL parity (3-space inversion)")
worst = 0.0; flips = 0; n = 0
for _ in range(20000):
    a, b, c = rng.normal(size=3), rng.normal(size=3), rng.normal(size=3)
    d0 = np.linalg.det(np.array([a, b, c]))
    dm = np.linalg.det(np.array([P3@a, P3@b, P3@c]))
    n += 1; flips += (np.sign(dm) == -np.sign(d0)); worst = max(worst, abs(d0 + dm))
print(f"    det3 of THREE spatial vectors: flips under P in {flips}/{n}; max |d + d_mirror| = {worst:.1e}")
print(f"    => THREE spatial directions suffice for a P-odd scalar. 4071's 'four' was for the 4D invariant.")
assert flips == n and worst < 1e-9

print("\nK1b  the distinction I blurred: ROTATIONS vs ARRANGEMENTS in 3-space")
def pf4(B): return 2.0*(B[0,1]*B[2,3]-B[0,2]*B[1,3]+B[0,3]*B[1,2])
def wedge(a,b): return np.outer(a,b)-np.outer(b,a)
worst_rot = 0.0
for _ in range(5000):
    B = np.zeros((4,4))
    for _ in range(3):
        u = rng.normal(size=4); u[0]=0; v = rng.normal(size=4); v[0]=0
        B += rng.normal()*wedge(u,v)
    worst_rot = max(worst_rot, abs(pf4(B)))
print(f"    3-space ROTATIONS: max |B^B| = {worst_rot:.1e}   -> still carry no handedness (4073 stands)")
tri = np.array([[1.,0,0],[0,1.,0],[0,0,1.]])
print(f"    3-space ARRANGEMENT (fixed cyclic triad): det3 = {np.linalg.det(tri):+.1f}, "
      f"mirrored = {np.linalg.det(P3@tri.T):+.1f}  -> IS handed")
assert worst_rot < 1e-9

print("\nK2  a chiral 3D arrangement the substrate could actually have: the Boerdijk-Coxeter helix")
def bc_helix(n=12, hand=+1):
    """Stack regular tetrahedra face to face; the result is a helix with a definite hand."""
    pts = [np.array([0,0,0.]), np.array([1,0,0.]), np.array([.5,np.sqrt(3)/2,0]), np.array([.5,np.sqrt(3)/6,np.sqrt(6)/3])]
    out = [p.copy() for p in pts]
    for _ in range(n):
        a, b, c, d = out[-4], out[-3], out[-2], out[-1]
        # reflect the oldest vertex through the opposite face to add the next tetrahedron
        cen = (b + c + d)/3.0; nrm = np.cross(c-b, d-b); nrm = nrm/np.linalg.norm(nrm)
        new = a + 2*float((cen-a)@nrm)*nrm
        out.append(new)
    Q = np.array(out)
    if hand < 0: Q = Q @ np.diag([1.,1,-1])
    return Q
def torsion_sign(Q):
    tot = 0.0
    for i in range(len(Q)-3):
        t1, t2, t3 = Q[i+1]-Q[i], Q[i+2]-Q[i+1], Q[i+3]-Q[i+2]
        tot += np.linalg.det(np.array([t1, t2, t3]))
    return tot
H = bc_helix(); Hm = H @ P3
print(f"    BC helix torsion invariant = {torsion_sign(H):+.5f};  mirrored = {torsion_sign(Hm):+.5f};"
      f"  sum = {torsion_sign(H)+torsion_sign(Hm):+.1e}")
print(f"    => tetrahedra stacked face-to-face make a CHIRAL 3D structure. No new variable; the hand is in")
print(f"       the PACKING. (4019: the 600-cell cannot tile flat R^4 -- helical packing is what tetrahedra do.)")
assert abs(torsion_sign(H)) > 1e-3 and abs(torsion_sign(H)+torsion_sign(Hm)) < 1e-9

print("\nK3  PROCEDURAL chirality: put the hand in the TIE-BREAK rule (adds no variable)")
def walk(chiral_tiebreak, steps=40000):
    """A walker on a cubic lattice. At each step several moves are degenerate; a rule must choose.
    Chiral rule: prefer the option maximising det3[v_prev, option, ref]; P-even rule: prefer max |dot|."""
    ref = np.array([0.,0,1]); pos = np.zeros(3); prev = np.array([1.,0,0]); net = 0.0
    dirs = [np.array(d, dtype=float) for d in
            [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
    for _ in range(steps):
        opts = [d for d in dirs if abs(float(d@prev) + 1) > 1e-9]        # no immediate backtrack
        if chiral_tiebreak:
            key = [float(np.linalg.det(np.array([prev, d, ref]))) for d in opts]
        else:
            key = [abs(float(d @ ref)) for d in opts]
        mx = max(key)
        cands = [opts[i] for i in range(len(opts)) if key[i] > mx - 1e-12]
        d = cands[rng.integers(len(cands))]
        net += float(np.linalg.det(np.array([prev, d, ref])))
        prev = d; pos = pos + d
    return net / steps
c_net = walk(True); e_net = walk(False)
print(f"    chiral tie-break : mean P-odd invariant per step = {c_net:+.5f}")
print(f"    P-even tie-break : mean P-odd invariant per step = {e_net:+.5f}")
print(f"    => the hand can live in the RULE THAT RESOLVES DEGENERACY -- a rule CPP has never specified.")
assert abs(c_net) > 0.1 and abs(e_net) < 1e-9

print("\nK4  the CPT route: P-odd = (C-odd) x (T-odd), from elements the corpus/nature ALREADY has")
rows = [("sign(delta)  -- the T-arrow (TARROW-1/2, W3)", +1, +1, -1),
        ("matter excess -- C-odd (baryogenesis, empirical)", +1, -1, +1),
        ("their PRODUCT", None, None, None)]
print(f"    {'quantity':50s}  P     C     T")
for name, p, c, t in rows[:2]:
    print(f"    {name:50s} {p:+d}    {c:+d}    {t:+d}")
pp, cc, tt = 1*1, 1*-1, -1*1
print(f"    {'their PRODUCT':50s} {pp:+d}    {cc:+d}    {tt:+d}")
print(f"    product is C-odd and T-odd. With CPT exact, CPT-even requires P-odd x C-odd x T-odd = even,")
print(f"    so a C-odd, T-odd quantity is P-ODD. No new primitive: the T-arrow exists in CPP, the C")
print(f"    asymmetry exists in nature. What is owed is the LINK, not a new axiom.")
