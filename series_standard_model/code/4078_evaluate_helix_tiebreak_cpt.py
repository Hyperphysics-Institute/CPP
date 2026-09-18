"""4078 (EW lane) -- evaluating K2 (helical packing), K3 (tie-break), K4 (CPT) against CPP's own constraints.

Founder: "The simplest option, as usual, is probably the best. The helical organization of space sounds
intriguing, since it lets the 4D structure fit without stretching the space. I like that a lot better than
the variable-position GPs that I agreed to."  (The variable-position GPs = founder ruling at 4020, allowing
slightly distorted cages to absorb 4019's 7.356 deg angular deficit.)

THE CLAIM UNDER TEST: does helical packing let the structure fit WITHOUT stretching?

D1  THE DEFICIT, recomputed from scratch: regular tetrahedra around a shared edge.
D2  WHAT THE HELIX BUYS: the Boerdijk-Coxeter helix stacks PERFECTLY REGULAR tetrahedra face-to-face --
    zero distortion, no stretching. Verified: every tetrahedron regular to machine precision.
D3  WHAT IT COSTS: the twist per tetrahedron is arccos(-2/3) = 131.81 deg, an IRRATIONAL multiple of 2 pi.
    So the helix NEVER CLOSES and NEVER REPEATS. No periodic lattice, no translational symmetry, and no
    repeating GP address grid along the helix axis. This is the real trade: exact tetrahedra for
    aperiodicity. Tested by searching for any closure out to 10,000 tetrahedra.
D4  z = 12?  Count nearest neighbours along a single BC helix. The corpus needs z = 12 (4020/4034).
D5  CHIRALITY: confirm the helix is chiral and that BOTH hands are geometrically available (so, as with
    every earlier route, the STRUCTURE supplies a hand but not a CHOICE of hand).
"""
import numpy as np
phi = (1 + 5**.5)/2

print("D1  the deficit, from scratch")
dih = np.degrees(np.arccos(1/3.0))
print(f"    regular tetrahedron dihedral angle       = {dih:.4f} deg")
print(f"    five around a shared edge                = {5*dih:.4f} deg")
print(f"    deficit vs 360                           = {360 - 5*dih:.4f} deg   (4019's 7.356 deg)")
assert abs((360 - 5*dih) - 7.3561) < 1e-3

def bc_helix(n):
    pts = [np.array([0,0,0.]), np.array([1,0,0.]), np.array([.5,np.sqrt(3)/2,0]),
           np.array([.5,np.sqrt(3)/6,np.sqrt(6)/3])]
    out = [p.copy() for p in pts]
    for _ in range(n):
        a, b, c, d = out[-4], out[-3], out[-2], out[-1]
        cen = (b+c+d)/3.0; nrm = np.cross(c-b, d-b); nrm = nrm/np.linalg.norm(nrm)
        out.append(a + 2*float((cen-a)@nrm)*nrm)
    return np.array(out)

H = bc_helix(400)
print("\nD2  what the helix buys: are the tetrahedra REGULAR (no stretching)?")
worst = 0.0
for i in range(len(H)-3):
    T = H[i:i+4]
    ds = [np.linalg.norm(T[a]-T[b]) for a in range(4) for b in range(a+1,4)]
    worst = max(worst, max(ds)-min(ds))
print(f"    max edge-length spread over 400 stacked tetrahedra = {worst:.2e}")
print(f"    => PERFECTLY REGULAR. The founder is right: helical stacking needs NO distortion of the cells.")
assert worst < 1e-9

print("\nD3  what it costs: does the helix ever close or repeat?")
# twist per step: angle between successive vertex positions projected perpendicular to the helix axis
axis = np.linalg.svd(H - H.mean(0))[2][0]
axis = axis/np.linalg.norm(axis)
proj = (H - H.mean(0)) - np.outer((H - H.mean(0)) @ axis, axis)
angs = []
for i in range(len(proj)-1):
    u, v = proj[i], proj[i+1]
    if np.linalg.norm(u) < 1e-9 or np.linalg.norm(v) < 1e-9: continue
    cosang = float(u@v)/(np.linalg.norm(u)*np.linalg.norm(v))
    angs.append(np.degrees(np.arccos(np.clip(cosang, -1, 1))))
tw = float(np.median(angs))
print(f"    median twist per tetrahedron = {tw:.4f} deg;  arccos(-2/3) = {np.degrees(np.arccos(-2/3)):.4f} deg")
Hlong = bc_helix(10000)
closures = 0
for i in range(4, len(Hlong)):
    if np.linalg.norm(Hlong[i] - Hlong[0]) < 1e-6: closures += 1
print(f"    exact closures found out to 10,000 tetrahedra: {closures}")
print(f"    => the twist is an irrational multiple of 2pi: the helix NEVER closes and NEVER repeats.")
print(f"       THE TRADE: exact regular cells, but NO periodic lattice and no repeating address grid.")
assert closures == 0

print("\nD4  coordination number along a single helix")
d0 = np.linalg.norm(H[1]-H[0])
zs = []
for i in range(20, 120):
    d = np.linalg.norm(H - H[i], axis=1); d[i] = np.inf
    zs.append(int(np.sum(np.abs(d - d0) < 1e-6)))
print(f"    nearest-neighbour count along one BC helix: min {min(zs)}, max {max(zs)}  (corpus needs z = 12)")
print(f"    => a single helix is a 1D column, not a space-filling lattice. Bundling helices to reach z = 12")
print(f"       and fill 3-space is an OPEN construction, not something the helix gives for free.")

print("\nD5  chirality: available, but is it CHOSEN?")
def torsion(Q):
    return sum(float(np.linalg.det(np.array([Q[i+1]-Q[i], Q[i+2]-Q[i+1], Q[i+3]-Q[i+2]])))
               for i in range(len(Q)-3))
Hm = H @ np.diag([1.,1,-1])
print(f"    torsion(helix) = {torsion(H):+.4f};  torsion(mirror) = {torsion(Hm):+.4f}")
print(f"    both hands are geometrically valid stackings of regular tetrahedra.")
print(f"    => as with EVERY earlier route: the structure supplies a HAND, not a CHOICE of hand.")
print(f"       A rule is still needed to say which helix the substrate builds.")
assert abs(torsion(H) + torsion(Hm)) < 1e-9
