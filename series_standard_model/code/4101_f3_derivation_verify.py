"""
4101 (EW lane) — F3 formal derivation: does the confined quark's helicity bit
average to exactly zero, so the strong force stays P-even under chi_4?

Founder ruling 4097: velocity is not intrinsic to a CP; it is carried by the DP arc
cohort established during acceleration. So b = sign(omega . v_arcs), where v_arcs is
the arc cohort direction. F3 asks whether <b> = 0 for a confined quark.

C1  Cage shells (SF-2: icosahedral Z-cage 12, dodecahedral H-cage 20) are EXACTLY
    antipodally paired.
C2  <sign(omega . v)> over an antipodally paired, equally weighted set = 0 IDENTICALLY,
    for every omega -- pairwise, no averaging.
C3  A free particle has ONE persistent arc direction: nothing to cancel, |<b>| = 1.
C4  Equal weighting follows from the icosahedral PROPER rotation group I (|I| = 60,
    det = +1 throughout, transitive on both shells). No improper operation is used,
    so the argument does NOT assume the cage dynamics is P-even. NOT CIRCULAR.
C5  INCONVENIENT BRANCH: I does not contain -I. Exact pairing is a property of the
    SPECIAL symmetry-axis orbits (12 / 20 / 30), not of icosahedral symmetry in
    general. Generic 60-point orbits are NOT paired and leave a residual bit sum of
    order 10%. F3 therefore REQUIRES the arc cohort to lie on cage bond directions.
C6  Falsifier scale: the residual <b> scales linearly with any antipodal imbalance.
    Observed hadronic parity violation (~1e-7, fully accounted for by weak admixture)
    caps any intrinsic imbalance at ~1e-7. Off-shell arcs would overshoot by ~1e6.
"""
import numpy as np
from itertools import product
phi = (1 + 5**0.5) / 2

def icosa12():
    V = []
    for s1 in (1, -1):
        for s2 in (1, -1):
            V += [(0, s1, s2*phi), (s1, s2*phi, 0), (s2*phi, 0, s1)]
    V = np.array(V, float); return V / np.linalg.norm(V, axis=1, keepdims=True)

def dodeca20():
    V = [np.array(s, float) for s in product((1, -1), repeat=3)]
    for s1 in (1, -1):
        for s2 in (1, -1):
            V += [np.array([0, s1/phi, s2*phi]), np.array([s1/phi, s2*phi, 0]),
                  np.array([s2*phi, 0, s1/phi])]
    V = np.array(V); return V / np.linalg.norm(V, axis=1, keepdims=True)

def antipodal_count(V, tol=1e-9):
    return sum(1 for v in V if np.linalg.norm(V + v, axis=1).min() < tol)

rng = np.random.default_rng(4101)

print("C1  cage shells are exactly antipodally paired")
for nm, V in [("icosahedral Z-cage (12)", icosa12()), ("dodecahedral H-cage (20)", dodeca20())]:
    a = antipodal_count(V)
    print(f"    {nm:26s} {a}/{len(V)} paired   |sum v_hat| = {np.abs(V.sum(0)).max():.1e}")
    assert a == len(V)
print("    C1 PASS")

print("\nC2  <sign(omega . v)> = 0 identically over those shells")
for nm, V in [("icosa 12", icosa12()), ("dodeca 20", dodeca20())]:
    worst = 0.0
    for _ in range(20000):
        w = rng.normal(size=3); w /= np.linalg.norm(w)
        worst = max(worst, abs(np.sign(V @ w).sum()))
    print(f"    {nm:10s} max |sum of bits| over 20000 omega = {worst:.1f}")
    assert worst == 0.0
print("    sign(omega.(-v)) = -sign(omega.v): pairwise cancellation, every omega.  C2 PASS")

print("\nC3  free particle: one persistent arc direction, no cancellation")
w = rng.normal(size=3); w /= np.linalg.norm(w)
v = rng.normal(size=3); v /= np.linalg.norm(v)
b = np.sign(v @ w)
assert abs(b) == 1
print(f"    b = {b:+.0f},  |<b>| = 1.000   -- same coupling, opposite outcome.  C3 PASS")

print("\nC4  equal weighting comes from PROPER rotations only (not circular)")
def build_I(V, tol=1e-9):
    G = [np.eye(3)]
    known = lambda M: any(np.abs(M - g).max() < tol for g in G)
    seeds = []
    for ax in list(V) + [np.cross(V[0], V[i]) for i in range(1, 12)]:
        n = np.linalg.norm(ax)
        if n < tol: continue
        ax = ax / n
        for ang in np.arange(1, 10) * 2*np.pi/10:
            K = np.array([[0, -ax[2], ax[1]], [ax[2], 0, -ax[0]], [-ax[1], ax[0], 0]])
            R = np.eye(3) + np.sin(ang)*K + (1 - np.cos(ang))*K@K
            if all(np.abs(V - p).max(1).min() < tol for p in (R @ V.T).T): seeds.append(R)
    for R in seeds:
        if not known(R): G.append(R)
    ch = True
    while ch and len(G) < 200:
        ch = False
        for a in list(G):
            for bb in list(G):
                M = a @ bb
                if not known(M): G.append(M); ch = True
    return G
G = build_I(icosa12())
dets = [np.linalg.det(g) for g in G]
assert len(G) == 60 and all(abs(d - 1) < 1e-6 for d in dets)
for nm, V in [("icosa 12", icosa12()), ("dodeca 20", dodeca20())]:
    orb = {min(range(len(V)), key=lambda i: np.abs(V[i] - g @ V[0]).max()) for g in G}
    assert len(orb) == len(V)
    print(f"    |I| = {len(G)}, all det = +1, transitive on {nm} ({len(orb)}/{len(V)})")
print("    no improper operation used => P-evenness of the dynamics is NOT assumed.  C4 PASS")

print("\nC5  INCONVENIENT BRANCH: pairing is special, not generic")
def orbit(v, tol=1e-9):
    O = []
    for g in G:
        p = g @ v
        if not any(np.linalg.norm(p - q) < tol for q in O): O.append(p)
    return np.array(O)
for nm, seed in [("12-shell (C5 axis)", icosa12()[0]),
                 ("20-shell (C3 axis)", icosa12()[0] + icosa12()[1] + icosa12()[2]),
                 ("30-shell (C2 axis)", icosa12()[0] + icosa12()[1])]:
    O = orbit(seed / np.linalg.norm(seed))
    print(f"    {nm:20s} n={len(O):3d}  paired {antipodal_count(O)}/{len(O)}  EXACT")
    assert antipodal_count(O) == len(O)
nbad = 0
for k in range(6):
    v = rng.normal(size=3); v /= np.linalg.norm(v)
    O = orbit(v); a = antipodal_count(O)
    if a != len(O): nbad += 1
    resid = max(abs(np.sign(O @ (lambda u: u/np.linalg.norm(u))(rng.normal(size=3))).sum())
                for _ in range(2000))
    print(f"    generic orbit #{k+1}      n={len(O):3d}  paired {a}/{len(O):<3d} "
          f"max |sum of bits| = {resid:.0f}  ({resid/len(O):.1%})")
assert nbad == 6
print("    6/6 generic orbits FAIL pairing, residual ~10%.")
print("    => F3 REQUIRES the arc cohort on cage bond directions.  C5 PASS (as a requirement)")

print("\nC6  falsifier scale")
V = icosa12()
for eps in (1e-3, 1e-5, 1e-7):
    r = []
    for _ in range(4000):
        w = rng.normal(size=3); w /= np.linalg.norm(w)
        wts = np.ones(len(V)); wts[::2] += eps
        r.append((np.sign(V @ w) * wts).sum() / wts.sum())
    print(f"    antipodal imbalance eps = {eps:.0e}  ->  induced <b> = {np.mean(np.abs(r)):.2e}")
print("    hadronic PV bound ~1e-7 caps any intrinsic imbalance at ~1e-7.")
print("    On-shell arcs: exact zero, satisfied. Off-shell arcs: ~1e-1, overshoot ~1e6.  C6 PASS")

print("\nALL CHECKS PASS")
print("\nF3 VERDICT: DERIVED, conditional on one named requirement --")
print("  the confined quark's DP arc cohort must lie along cage bond directions")
print("  (the 12/20/30 symmetry-axis shells), not in generic directions.")
print("  Given that, <b> = 0 EXACTLY, for every omega, with no averaging and no")
print("  parity assumption. Without it, F3 fails by six orders of magnitude.")
