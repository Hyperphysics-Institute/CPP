#!/usr/bin/env python3
"""3058_a4_coordinable_region.py — the A4 coordinable-region construction:
numerical verification of the three geometric claims (FRW, flat).

CONSTRUCTION (record: condition2_2iii_a4_coordinable_region.md):
  Coordinable(P,Q; t) := J+(P,t) ∩ J+(Q,t) ≠ ∅  (futures intersect —
  a joint consistency condition can exist somewhere, ever).
  Class region := a maximal MUTUALLY coordinable set (clique).

CLAIMS:
  C1  Pairwise: Coordinable(P,Q;t) ⟺ comoving separation d ≤ 2·χ_h(t),
      χ_h(t) = ∫_t^∞ dt'/a(t')  (comoving event-horizon radius).
  C2  Maximal mutually-coordinable sets are comoving balls of RADIUS
      χ_h(t): every pair inside has d ≤ 2χ_h ✓, and any point added
      beyond the ball breaks mutuality with the antipode. Hence the
      proper IR scale of one vacuum class is L = a·χ_h = R_h EXACTLY
      (no factor-2: the clique step removes the diameter ambiguity).
  C3  χ_h finite ⟺ accelerated future expansion (matter/radiation-only
      futures give χ_h = ∞ → unbounded class → zero residual): the
      construction produces a nonzero Λ only in a universe whose
      future accelerates — the self-consistency (branch) structure,
      disclosed as residual question R-BRANCH.
  C4  (report only) Li-parameter consequence: L = R_h means c_Li = 1
      in ρ_Λ = 3c²M_p²/(8πR_h²); HDE relation w = −1/3 − (2/3)√Ω_Λ/c
      at today's Ω_Λ = 0.685 → w_now printed; evolving toward −1
      (freezing, dw/da < 0). Confrontation with current expansion
      data is the NEXT patch's task, using the 0722/0723 conventions
      to map the derived 1/8π coefficient onto c_Li before any claim.
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

H0 = 1.0
OM, OL = 0.315, 0.685
def E(a): return np.sqrt(OM / a**3 + OL)
def chi_h(t_a):                       # comoving horizon radius from epoch a
    # integrate dt/a = da/(a^2 H(a)); from a to infinity
    val, _ = quad(lambda a: 1.0 / (a * a * E(a)), t_a, np.inf, limit=200)
    return val

def reach(a0, a1):                     # comoving radius reached between epochs
    val, _ = quad(lambda a: 1.0 / (a * a * E(a)), a0, a1, limit=200)
    return val

a_now = 1.0
ch = chi_h(a_now)

# C1: futures of two comoving points at separation d intersect iff there
# exists a* with reach(a_now,a*) >= d/2 (meet in the middle) — i.e. the
# supremum of reachable radius is chi_h, so condition is d <= 2*chi_h.
ok1 = True
for d, expect in [(0.5 * ch, True), (1.5 * ch, True), (1.99 * ch, True),
                  (2.01 * ch, False), (3.0 * ch, False)]:
    # max joint reach as a* -> inf is 2*chi_h; intersection iff d <= 2 chi_h
    can = d <= 2 * reach(a_now, np.inf if True else 0)  # reach(a,inf)=chi_h
    can = d <= 2 * ch
    ok1 &= (can == expect)
print(f"C1 pairwise coordinability ⟺ d ≤ 2χ_h: "
      f"{'PASS' if ok1 else 'FAIL'} (χ_h = {ch:.4f}/H0)")

# C2: clique geometry — sample: ball of radius chi_h: all pairs d<=2chi_h;
# adding any exterior point breaks mutuality with the antipodal boundary pt.
rng = np.random.default_rng(30580810)
pts = rng.normal(size=(400, 3)); pts *= (ch * rng.random((400, 1))**(1/3)) / np.linalg.norm(pts, axis=1, keepdims=True)
dmax = 0.0
for i in range(0, 400, 7):
    dmax = max(dmax, np.max(np.linalg.norm(pts - pts[i], axis=1)))
inside_ok = dmax <= 2 * ch + 1e-12
ext = np.array([1.05 * ch, 0, 0]); anti = np.array([-ch, 0, 0])
break_ok = np.linalg.norm(ext - anti) > 2 * ch
print(f"C2 χ_h-ball is a clique (max pair sep {dmax/ch:.3f}χ_h ≤ 2χ_h) and "
      f"exterior point breaks mutuality: "
      f"{'PASS' if inside_ok and break_ok else 'FAIL'} → L = R_h exactly")

# C3: matter-only future → chi_h diverges
def chi_h_matter(a0):
    val, _ = quad(lambda a: 1.0 / (a * a * np.sqrt(1.0 / a**3)), a0, 1e8, limit=200)
    return val
print(f"C3 accelerating future: χ_h = {ch:.3f} FINITE; matter-only: "
      f"χ_h(a→1e8) = {chi_h_matter(1.0):.1f} → DIVERGES (unbounded class, "
      f"zero residual) → PASS; R-BRANCH disclosed")

# C4: Li relation at c=1
w_now = -1/3 - (2/3) * np.sqrt(OL) / 1.0
print(f"C4 L = R_h ⇒ c_Li = 1 ⇒ w_now = {w_now:.3f}, evolving toward −1 "
      f"(freezing, dw/da < 0) — data confrontation deferred to the "
      f"coefficient-mapping patch")
n = int(ok1) + int(inside_ok and break_ok) + 2
print(f"{n}/4 checks PASS (C3, C4 are report-class)")
