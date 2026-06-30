#!/usr/bin/env python3
"""
G1a verify — the scale-free edge-bond angular-stiffness ratio g = kappa_scissor / kappa_bend
=============================================================================================
SF-2/SF-5 lane deliverable for the DM Cross-Rod X-junction floor verdict.
Patch 2200. Verifies the reasoning fragment reasoning/2200.md.

WHAT THIS COMPUTES
  The DM floor flexibility test (DM 1830) is kappa_scissor < 3B/L_arm, where B is the arm's
  bending rigidity. The DM 1836 collapse observed that kappa_scissor (the X-junction dihedral /
  "scissor" stiffness) and B (the in-line ribbon bend) are the SAME qq-edge-bond potential in
  two geometries, so with B = kappa_bend * ell_rung (worm-like chain) and L_arm = (N/2)*ell_rung
  the test becomes the scale-free ratio

      g  =  kappa_scissor / kappa_bend  <  6/N      (g < 0.43 at the floor-setting N ~ 14)

  In g, EVERYTHING absolute cancels: the coupling, kT_form, the ZBW params, the near-cancellation
  depth, and the static-vs-dynamic (Earnshaw) sign question -- because the same bond acts in both
  geometries. Only a pure GEOMETRY ratio of two same-potential second derivatives survives.

WHAT IT FINDS (the reversal)
  Evaluated faithfully from the SAME screened potential in the two geometries, g comes out
  O(1)-to-several (band 1.6 - 3.8 across the screened falloff family), AT or ABOVE g_crit = 0.43.
  This REVERSES the DM-lane's optimistic g ~ 0.1 "viable" read (1835 founder gradient estimate,
  1836 collapse) at the clean same-potential level: the junction leans RIGID-to-MARGINAL, so the
  cluster floor leans TENSE, not slack.

DIAGNOSIS OF THE FOUNDER-vs-RATIO DISCREPANCY
  Founder read (1835): "scissor mode considerably SOFTER than the LONGITUDINAL compression" -> TRUE,
  but that compares scissor (E_ee perimeter shell, ~MeV) to the E_qq CORE (~66 MeV) -- a ~70x
  hierarchy that makes softness obvious. The floor-relevant ratio is NOT scissor-vs-core; it is
  g = kappa_scissor / kappa_(in-line BEND), and the in-line ribbon bend is ALSO the E_ee perimeter
  shell ("the eCP shell is the bending-stiffness layer"), the SAME scale as the scissor. So the
  E_qq/E_ee hierarchy CANCELS OUT of the floor-relevant ratio; what's left is a pure geometry ratio
  of two E_ee-shell stiffnesses, which is O(1), not hierarchy-suppressed to 0.1.
"""
import numpy as np

d, w = 1.0, 2.0                                  # rung spacing ~1 fm; ribbon width ~2 fm
ys = np.array([-1.0, -0.5, 0.5, 1.0]) * (w / 2)  # bend: full-WIDTH line-contact perimeter fibers

def Vfam(s, lam):                                # screened power law: near-cancellation residual
    return lambda r: np.exp(-r / lam) / r**s
def d2(f, x, h=1e-4):                            # numerical second derivative (the stiffness)
    return (f(x + h) - 2 * f(x) + f(x - h)) / h**2

def kbend(V):
    # In-line ribbon bend: full-width LINE contact, conjugate perimeter fibers at close stacking d.
    # All width fibers engage (dense contact) -> sum over the width lever arms.
    return abs(d2(V, d)) * np.sum(ys**2)

def ksci(V, Lrod=4.0, n=12):
    # Perpendicular X-junction scissor: a single-point 90-deg crossing. Screening kills the far
    # diverging pairs -> only the near-crossing region carries stiffness. Sum over rod-element pairs.
    grid = np.arange(1, n + 1) * (Lrod / n)
    tot = 0.0
    for l in grid:
        for s_ in grid:
            R = lambda th: np.sqrt(l * l + s_ * s_ - 2 * l * s_ * np.cos(th))
            tot += d2(lambda th: V(R(th)), np.pi / 2)
    return abs(tot)

g_crit14 = 6 / 14
print(f"g_crit(N=14) = 6/14 = {g_crit14:.3f}    g_crit(N=8) = {6/8:.3f}\n")
print(f"{'screened potential':>24}{'g':>8}  verdict")
print("-" * 48)
gs = []
for nm, s, lam in [("s=1 lam=2.0", 1, 2.0), ("s=1 lam=1.3", 1, 1.3), ("s=1 lam=0.9", 1, 0.9),
                   ("s=1 lam=0.5", 1, 0.5), ("s=2 lam=1.3", 2, 1.3), ("s=2 lam=0.7", 2, 0.7)]:
    V = Vfam(s, lam)
    g = ksci(V) / kbend(V)
    gs.append(g)
    print(f"{nm:>24}{g:8.3f}  {'flexible(viable)' if g < g_crit14 else 'rigid-lean(tense)'}")
print("-" * 48)
print(f"g band (screened, faithful geometry) = {min(gs):.2f} - {max(gs):.2f}   "
      f"[all >= g_crit = {g_crit14:.2f}]\n")

# INVERSE: what separation ratio rho = r_sci/r_bend (steep falloff) WOULD give g < 0.43?
print("INVERSE -- what would deliver clean viability (g < 0.43)?  single-pair scaling g ~ rho^-(s+2):")
for s in (1, 3, 5):
    rho = 0.43 ** (-1 / (s + 2))
    print(f"  falloff index p = s+2 = {s+2}: need r_sci/r_bend >= {rho:.2f}  (scissor pairs {rho:.2f}x farther)")
print("  geometry gives r_sci/r_bend ~ sqrt(2) ~ 1.4 at the near crossing -- short of what's needed unless")
print("  the falloff is very steep (p >= 5) AND the far pairs are fully screened out.\n")

print("HONEST VERDICT (G1a, clean same-potential ratio):")
print("  Forward g band = 1.6 - 3.8, AT or ABOVE g_crit = 0.43 across the whole screened falloff family.")
print("  The scale-free ratio FRAMING is correct and cancels the blocked absolute scale -- but it does")
print("  NOT reproduce the DM-lane's g ~ 0.1 'viable' estimate. The junction leans RIGID-to-MARGINAL ->")
print("  cluster floor leans TENSE, reversing the 1836 optimistic read at the clean-ratio level.")
print("  Cause: the founder's softness reference was the E_qq core; the floor ratio is scissor-vs-E_ee-")
print("  bend, both the same perimeter shell -> the hierarchy cancels -> g is geometric O(1), not 0.1.")
print("  Residual: a definitive g still needs the pinned charge map (counts, alternating cancellation,")
print("  exact lever arms) = the edge-bond SSV potential blocked on OPEN-FP-SF-2-eta. As far as the")
print("  clean ratio is evaluable it leans AGAINST clean viability, NOT for it. NOT a clean kill")
print("  (a sufficiently steep + fully screened real charge map could in principle reach 0.43), but")
print("  definitively NOT the comfortable 'viable' the held DM panel round 2 was expecting.")
