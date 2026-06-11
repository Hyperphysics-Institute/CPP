#!/usr/bin/env python3
"""
1120_step7_tensor_meson_test.py -- spin-2 construction, Step 7 (the tensor-meson test).

QUESTION (from the kickoff handover, the candidate SECOND motivation): can CPP's strong sector
build a spin-2 hadron -- f_2(1270), the light 3P2 nonet member (a_2(1320), f_2(1270),
f_2'(1525), K_2*(1430)) -- as an EMERGENT orbital state (no new bit), or does it hit the same
per-point representational wall as the gravitational wave (1116)? If the wall recurs, that is
an independent phenomenon demanding the same Q_ij axiom (mono- -> multi-motivation). If not,
the axiom stays mono-motivated but the granularity diagnosis is sharpened from the matter side.

CORPUS ANCHORS (audited before this run):
  - SS-1e (hadron spectrum) already lists chi_c2(1P) as "L=1, J=2" -- a standard orbital
    excitation in the charmonium table. Same 3P2 construction as f_2(1270).
  - SS-6 (deuteron observables): the observed quadrupole Q_d = +0.286 fm^2 is ORBITAL-dominated
    (the rigid bipyramid core gives only -0.022 fm^2); CPP already attributes a measured l=2
    observable to the extended orbital wavefunction.
  - c8/c9 (Spin I/II): constituent spin-1/2 is emergent ZBW orbital angular momentum (a vector).

RESULT (three parts):
  P1. COMPOSITION: two emergent vectors -- the quark-antiquark ZBW spin triplet S=1
      (1/2 x 1/2 = 0 + 1) and one unit of relative orbital angular momentum L=1 -- compose to
      J=2: the 9-dim L=1 x S=1 configuration space contains the 5-dim J=2 multiplet (3P2 = f_2).
      Numerically: eigenvalues of J^2 on the product space = {0, 1, 2} with degeneracies
      {1, 3, 5}. Spin-2 matter requires NO new bit.
  P2. CONFIGURATION SPACE CARRIES ALL l: the two-body relative coordinate ranges over lattice
      shells; the 5 real l=2 harmonics evaluated on lattice relative positions have full rank 5.
      The resource the GW lacked (per-point field data: 4-dim, l <= 1) is unbounded here (a
      FUNCTION SPACE over relative positions: every l).
  P3. ICOSAHEDRAL PROTECTION (bonus): branching D^(l) under the icosahedral rotation group I:
      l=2 -> H (5-dim, IRREDUCIBLE -- the multiplet survives intact); first splitting at l=3
      (T2+G). Contrast the cubic group O: l=2 -> E + T2 (splits 2+3). The 600-cell's symmetry
      uniquely protects the 5-fold spin-2 multiplet -- and the protecting irrep H(_g) is exactly
      the empty GW slot identified in 1112.

VERDICT: f_2(1270) does NOT hit the wall -- spin-2 hadrons are emergent orbital states (the
candidate second motivation DISSOLVES; the spin-bit axiom remains mono-motivated by GW
empirics). The parallax gained: the wall is precisely PER-POINT. Matter configurations
represent l=2 effortlessly; the per-point broadcast cannot. The axiom activates a
geometrically protected, pre-slotted representation -- it does not import alien structure.
NO VERDICT MOVED (no THEO/PRED/count change; foundational scoping).
"""
import numpy as np

# ---------------------------------------------------------------- P1: composition to J=2
print("=== P1. COMPOSITION: two emergent vectors reach J=2 at configuration level ===")
# spin-1 generators (S=1 from the ZBW 1/2 x 1/2 triplet; L=1 relative orbital)
Sx = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]]) / np.sqrt(2)
Sy = np.array([[0, -1j, 0], [1j, 0, -1j], [0, 1j, 0]]) / np.sqrt(2)
Sz = np.diag([1.0, 0.0, -1.0])
I3 = np.eye(3)
J = [np.kron(Sa, I3) + np.kron(I3, Sa) for Sa in (Sx, Sy, Sz)]   # J = L + S on 3x3 = 9-dim
J2 = sum(Ja @ Ja for Ja in J)
ev = np.sort(np.linalg.eigvalsh(J2).real)
js = np.round((-1 + np.sqrt(1 + 4 * ev)) / 2, 10)   # j from j(j+1)
vals, counts = np.unique(js, return_counts=True)
print("  L=1 (x) S=1 (9-dim) -> J multiplets:", {float(v): int(c) for v, c in zip(vals, counts)})
print("  => the 5-dim J=2 multiplet (3P2 = f_2(1270) / a_2 / f_2' / K_2* ; chi_c2 in SS-1e)")
print("     is built from VECTORS ONLY -- emergent ZBW spins + orbital L. No rank-2 bit needed.")
print("  (And the constituent S=1 itself: 1/2 x 1/2 = 0 + 1 -- dims", end=" ")
h = np.eye(2); print(f"{2*2} = 1 + 3, standard.)")

# ---------------------------------------------------------------- P2: configuration space
print("\n=== P2. THE CONFIGURATION SPACE CARRIES THE FULL l=2 MULTIPLET ===")
phi = (1 + np.sqrt(5)) / 2
raw = []
for a, b in [(1, phi), (1, -phi), (-1, phi), (-1, -phi)]:
    raw += [(0, a, b), (a, b, 0), (b, 0, a)]
shell1 = np.array(raw, float)
# relative-position sample: first shell + a second shell (sums of non-antipodal neighbors)
rel = [v for v in shell1]
for i in range(12):
    for j in range(i + 1, 12):
        s = shell1[i] + shell1[j]
        if np.linalg.norm(s) > 1e-9:
            rel.append(s)
rel = np.array(rel)
u = rel / np.linalg.norm(rel, axis=1, keepdims=True)
Y2 = np.column_stack([u[:, 0] * u[:, 1], u[:, 1] * u[:, 2], u[:, 0] * u[:, 2],
                      u[:, 0]**2 - u[:, 1]**2, 3 * u[:, 2]**2 - 1])   # 5 real l=2 harmonics
print(f"  {len(rel)} lattice relative-position vectors (shells 1-2); rank of the 5 l=2")
print(f"  harmonics evaluated on them = {np.linalg.matrix_rank(Y2)} / 5  (full -- every l=2")
print("  component of a two-body relative wavefunction psi(r) is supported).")
print("  THE CONTRAST: per-point field data = 4 components (l <= 1, fixed); two-body")
print("  configuration = a FUNCTION SPACE over relative positions (every l available).")

# ---------------------------------------------------------------- P3: icosahedral protection
print("\n=== P3. ICOSAHEDRAL PROTECTION OF THE SPIN-2 MULTIPLET (vs cubic) ===")
def chi_l(l, th):
    if abs(th) < 1e-12: return 2 * l + 1
    return np.sin((l + 0.5) * th) / np.sin(th / 2)

# Icosahedral rotation group I (order 60): classes E, 12C5, 12C5^2, 20C3, 15C2
I_classes = [(1, 0.0), (12, 2*np.pi/5), (12, 4*np.pi/5), (20, 2*np.pi/3), (15, np.pi)]
I_irreps = {  # characters on (E, C5, C5^2, C3, C2)
    'A':  [1, 1, 1, 1, 1],
    'T1': [3, phi, 1 - phi, 0, -1],
    'T2': [3, 1 - phi, phi, 0, -1],
    'G':  [4, -1, -1, 1, 0],
    'H':  [5, 0, 0, -1, 1],
}
# Octahedral rotation group O (order 24): classes E, 8C3, 6C2', 6C4, 3C2
O_classes = [(1, 0.0), (8, 2*np.pi/3), (6, np.pi), (6, np.pi/2), (3, np.pi)]
O_irreps = {
    'A1': [1, 1, 1, 1, 1], 'A2': [1, 1, -1, -1, 1], 'E': [2, -1, 0, 0, 2],
    'T1': [3, 0, -1, 1, -1], 'T2': [3, 0, 1, -1, -1],
}
def branch(l, classes, irreps, order):
    out = {}
    for name, ch in irreps.items():
        m = sum(n * ch[i] * chi_l(l, th) for i, (n, th) in enumerate(classes)) / order
        m = int(round(m))
        if m: out[name] = m
    return out

print("  branching of D^(l) under the ICOSAHEDRAL group I:")
for l in range(5):
    b = branch(l, I_classes, I_irreps, 60)
    note = "  <-- IRREDUCIBLE: the 5-fold spin-2 multiplet survives INTACT (= the H_g GW slot, 1112)" if l == 2 else (
           "  <-- first splitting" if l == 3 else "")
    print(f"    l={l} ({2*l+1}-dim): {b}{note}")
print("  branching under the CUBIC group O (for contrast):")
b2 = branch(2, O_classes, O_irreps, 24)
print(f"    l=2 (5-dim): {b2}  <-- SPLITS 2+3: a cubic lattice would fine-split every")
print("    spin-2 multiplet (tensor mesons AND the future Q_ij / GW polarizations).")
print("  => The 600-cell's icosahedral symmetry is the UNIQUE crystallographic-class choice")
print("     that protects spin-2 exactly; l=2 is the HIGHEST l so protected (l>=3 split).")

# ---------------------------------------------------------------- the distinction, stated
print("\n=== WHY THIS DOES NOT CONTRADICT 1115/1116 (the wall is per-point) ===")
print("  A hadron's spin-2 is the transformation property of an extended STATIONARY")
print("  multi-constituent configuration -- it lives in the function space over relative")
print("  coordinates (P2: every l), composed from vectors (P1). No amplitude-order or")
print("  frequency-doubling bookkeeping applies to a bound state's quantum numbers.")
print("  A gravitational wave needs a LINEAR, MASSLESS, PROPAGATING field mode of helicity")
print("  +/-2 arriving at the source frequency -- carried point-by-point in the per-GP")
print("  broadcast data, which is 4-dimensional (l <= 1; 1116/1119). Matter CAN be spin-2;")
print("  the radiating field CANNOT (without the axiom). This is 1114's finding -- 'source")
print("  quadrupoles exist, the radiating tensor field does not' -- now DEMONSTRATED.")

print("\n================== VERDICT (Step 7, the tensor-meson test) ==================")
print("f_2(1270) does NOT hit the wall: spin-2 hadrons are emergent orbital states (3P2 from")
print("emergent vectors), consistent with SS-1e's chi_c2 and SS-6's orbital-dominated Q_d.")
print("The candidate SECOND motivation DISSOLVES -- the spin-bit axiom remains mono-motivated")
print("by GW empirics, and that must be stated honestly in the axiom writeup. The parallax")
print("gained: the wall is precisely PER-POINT granularity (the architect's diagnosis, matter-")
print("side); and the lattice PROTECTS the 5-fold spin-2 multiplet (H_g irreducible) that a")
print("cubic lattice would split -- the geometry pre-slots AND protects the seat the axiom")
print("will fill. NO VERDICT MOVED.")
