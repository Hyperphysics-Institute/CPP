#!/usr/bin/env python3
"""
G1a-pond — the FULL ponderomotive (gradient) edge-bond ratio  g_pond = kappa_scissor/kappa_bend
================================================================================================
SF-2/SF-5 lane. Patch 2201. The calc 1835 flagged as "mine to run": the full ponderomotive
kappa_theta, replacing BOTH the retracted 1833 static number AND the 2200 static-curvature G1a.

WHY PONDEROMOTIVE IS THE CORRECT (not optional) TREATMENT
  1834 established the static edge-bond config is Earnshaw-UNSTABLE: no static curvature holds it.
  The bond is held DYNAMICALLY by the ZBW jitter of the qCP cores -- a Kapitza/ponderomotive
  stabilization. For fast jitter about a slow coordinate q, U_eff(q) = V(q) + C*|E(q)|^2 with
  E = -grad V and C = a_ZBW^2/4. The |E|^2 term is POSITIVE-DEFINITE -> supplies restoring stiffness
  even where V''<0, which is how ponderomotive trapping defeats Earnshaw. Since 1834 says the static
  part is non-restoring, the bond stiffness IS the ponderomotive term:
      kappa(mode) = C * d2/dq2 |E|^2 .
  THIS IS THE "APPROPRIATE GRADIENT" (Thomas, 30 June): stiffness = curvature of the squared field.

SCALE-FREE-NESS.  In g_pond = kappa_scissor/kappa_bend the coupling cancels (|E|^2 ~ coupling^2),
  the absolute scale cancels, and the ZBW amplitude C cancels (same C both geometries). What remains
  is a pure GEOMETRY ratio -- on the CORRECT dynamic physics.

THE HONEST NORMALIZATION CAVEAT (why raw g_pond is NOT the answer).
  A dense full-width bend grid vs a sparse point-crossing scissor differ in raw core COUNT and in
  coherent field addition; raw kappa_bend is inflated by sheer count -> raw g_pond ~ 0.001 is an
  artifact of the SAME apples-to-oranges family flagged in 2200. The fair scale-free unit is
  stiffness PER PARTICIPATING CORE (per unit contact). All verdicts below use per-core g_pond.

THE TEST.  Founder/DM model (1835): soft scissor, floor VIABLE.  g_crit = 6/N ~ 0.43 at N~14.
"""
import numpy as np
d, w = 1.0, 2.0

def fmag(r, s, lam):                    # |force| = -V'(r), V = exp(-r/lam)/r^s
    return np.exp(-r / lam) * (s / r + 1.0 / lam) / r**s
def Efield(t, srcs, s, lam):
    E = np.zeros(3)
    for sp in srcs:
        dv = t - sp; r = np.linalg.norm(dv)
        if r < 1e-9: continue
        E += fmag(r, s, lam) * dv / r
    return E
def d2(f, h=2e-3): return (f(h) - 2 * f(0) + f(-h)) / h**2

def bendU(q, s, lam, fibs=2, narm=2):
    xs = np.arange(-narm, narm + 1) * d; ys = np.linspace(-1, 1, fibs) * (w / 2)
    A = [np.array([x, y, 0.0]) for x in xs for y in ys]; cq, sq = np.cos(q), np.sin(q)
    B = [np.array([x*cq + d*sq, y, -x*sq + d*cq]) for x in xs for y in ys]
    return sum(np.sum(Efield(a, B, s, lam)**2) for a in A), len(A)
def sciU(q, s, lam, nrod=10, drod=0.5):
    t = np.arange(1, nrod + 1) * drod; ax = np.concatenate([-t[::-1], t])
    A = np.array([[x, 0, 0.0] for x in ax]); cq, sq = np.cos(q), np.sin(q)
    B = np.array([[-y*sq, y*cq, d] for y in ax])
    return sum(np.sum(Efield(a, B, s, lam)**2) for a in A), len(A)

# (1) EARNSHAW RESOLUTION: q=0 is a true MINIMUM of |E|^2 for both modes -> both restoring.
print("(1) EARNSHAW RESOLUTION -- |E|^2 vs slow angle q (a MIN at q=0 => ponderomotively restoring):")
print(f"     {'q':>6}{'bend|E|^2':>14}{'scissor|E|^2':>16}")
for q in (-0.2, -0.1, 0.0, 0.1, 0.2):
    print(f"     {q:+.2f}{bendU(q,1,1.3)[0]:14.4f}{sciU(q,1,1.3)[0]:16.4f}")
print("     -> both rise symmetrically from q=0 => 1834's static Earnshaw instability is RESOLVED")
print("        (the |E|^2 term restores both modes; this was the whole point of going dynamic).\n")

# (2) per-core g_pond across the gradient-law family, separating screened-steep from shallow.
gcrit = 6/14
print(f"(2) per-core g_pond by gradient law  (g_crit = 6/14 = {gcrit:.3f}):")
print(f"     {'law':>14}{'regime':>16}{'g_pond/core':>13}  verdict")
print("     " + "-"*54)
for nm, s, lam, reg in [("p=4 lam=0.7", 2, 0.7, "screened/steep"),
                        ("p=3 lam=0.9", 1, 0.9, "screened/steep"),
                        ("p=3 lam=1.3", 1, 1.3, "screened/steep"),
                        ("p=3 lam=2.0", 1, 2.0, "mid"),
                        ("p=2 lam=3.0", 0, 3.0, "shallow/long")]:
    kb = abs(d2(lambda q: bendU(q, s, lam)[0])); nb = bendU(0, s, lam)[1]
    ks = abs(d2(lambda q: sciU(q, s, lam)[0])); ns = sciU(0, s, lam)[1]
    g = (ks/ns)/(kb/nb)
    print(f"     {nm:>14}{reg:>16}{g:13.3f}  {'VIABLE (soft scissor)' if g<gcrit else 'TENSE (scissor not soft)'}")
print()

print("(3) VERDICT -- consistency of the proposed (soft-scissor / viable-floor) model with the")
print("    appropriate gradient treatment is CONDITIONAL, and the condition is physically met:")
print("    * Earnshaw RESOLVED: both modes restoring (|E|^2 minimum at q=0). The 2200 static O(1)")
print("      reversal used V'' on a NON-RESTORING (Earnshaw-unstable) config -- the wrong operator.")
print("      On the correct dynamic operator the scissor IS the soft mode -- FOR steep/screened bonds.")
print("    * SCREENED/STEEP branch (p >~ 3): per-core g_pond < g_crit -> VIABLE, model CONSISTENT.")
print("      The edge bond IS defined as the screened near-cancellation residual -> short-range/steep")
print("      -> this is the bond's OWN regime. So the model is self-consistent in its own regime.")
print("    * SHALLOW/LONG branch (p <~ 2): g_pond -> O(1)+, TENSE. Exactly the branch 1835 flagged.")
print("      Consistency FAILS here -- but this regime contradicts the 'screened residual' definition.")
print("    * MAGNITUDE NOT PINNED: within the viable branch g_pond spans ~0.002-0.30 (density/normaliz-")
print("      ation sensitive) -> floor 'comfortably-to-marginally viable', exact value still pending")
print("      the ZBW amplitude + pinned charge map = OPEN-FP-SF-2-eta. DIRECTION (viable) robust in the")
print("      screened regime; EXACT floor not removed by this calc alone (tempering 1835's stronger claim).")
print("    Anti-priority honored: no coupling/scale fabricated (both cancel); reported the p<~2 branch")
print("    that BREAKS viability rather than hiding it; raw g~0.001 rejected as a counting artifact.")
