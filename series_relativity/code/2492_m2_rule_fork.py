#!/usr/bin/env python3
"""
Patch 2492 -- SR-MECH-2485 Step 4 -- M2: the exclusion rule.

FORK-PINNING script (2486-style: demonstrates, does not resolve). The
postulate-available single-CP kinematics (c01 displacement-response +
A3'/M4 reach + M1's distinguished plane) admit several inequivalent
candidate rules for how the obligatory drift interacts with the
per-Moment capacity set. This script:

  (W1) applies the one available FORWARD filter -- continuity of the
       capacity fraction in the rest limit v -> 0+ (grounded in c01's
       displacement-response equation being continuous in net SSV: an
       infinitesimally moving aggregate is an infinitesimally perturbed
       Sea state) -- which KILLS two candidates forward;
  (W2) computes the exact capacity fraction V_free/V0 and its leading
       small-f behaviour for each surviving candidate (closed forms
       cross-checked by fixed-seed Monte Carlo in the round 4-ball);
  (W3) computes the strain output eps(f) = (V_free/V0)^(-1/4) - 1 under
       SR-1's constitutive rule for each survivor, demonstrating the
       survivors are pairwise inequivalent at leading order -- the fork
       is REAL, the selection is consequential, and the postulates (as
       of Patch 2491 + the unpinned SF-6 inertia mechanism, handover
       2026-07-14 / Patch 2470) do not discriminate among them.

Candidate rules (f = d/l_P = v/c; arena = unit 4-ball, coords
(x_tau, x_1, x_2, x_3), Pi = (x_tau, x_1) per M1):

  R1  TRANSLATION / relabeling. The drift is bookkeeping inside the one
      computed displacement; the admissible target set is unchanged.
      V_free/V0 = 1 identically; eps = 0.
  R2  VECTOR REACH CONSUMPTION (lens). The drift consumes reach
      vectorially and the discretionary part carries its own full-reach
      bound: capacity = Ball CAP (Ball + f e_1).
  R3h COMPONENT FLOOR, half-space. The e_motion component cannot fall
      below the drift: free iff x_1 >= f.  [KILLED by W1]
  R3s COMPONENT SLICE (c01 exact-advance template transferred to the
      drift): x_1 = f exactly. Free set has measure zero.  [KILLED by W1]
  R3y SYMMETRIZED COMPONENT SLAB (codim-1, E_1 of the 2482 family):
      forbidden iff |x_1| <= f.
  R4  IN-PLANE MAGNITUDE FLOOR (codim-2 tube, E_2 of the 2482 family):
      forbidden iff sqrt(x_tau^2 + x_1^2) <= f.

stdlib only (F3/numpy ruling owed). Seed 2492.
"""

import math
import random

random.seed(2492)

V0 = math.pi ** 2 / 2.0            # volume of unit 4-ball


def a3(x):
    """3-volume of the spatial cross-section of the unit 4-ball at x."""
    if abs(x) >= 1.0:
        return 0.0
    return (4.0 * math.pi / 3.0) * (1.0 - x * x) ** 1.5


def integrate(fn, a, b, n=4000):
    """Simpson quadrature."""
    if b <= a:
        return 0.0
    if n % 2:
        n += 1
    h = (b - a) / n
    s = fn(a) + fn(b)
    for i in range(1, n):
        s += fn(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3.0


# ---------------------------------------------------------------- exact
def frac_R1(f):
    return 1.0


def frac_R2(f):
    """Ball CAP (Ball + f e_1): two caps of height 1 - f/2."""
    cap = integrate(a3, f / 2.0, 1.0)
    return 2.0 * cap / V0


def frac_R3h(f):
    return integrate(a3, f, 1.0) / V0


def frac_R3y(f):
    return 1.0 - integrate(a3, -f, f) / V0


def frac_R4(f):
    return (1.0 - f * f) ** 2


# ------------------------------------------------------------ MC checks
def mc_fracs(f, n=200_000):
    """Monte Carlo capacity fractions for R2, R3h, R3y, R4 in one pass."""
    cnt = {"R2": 0, "R3h": 0, "R3y": 0, "R4": 0}
    tot = 0
    while tot < n:
        x = [random.uniform(-1, 1) for _ in range(4)]
        r2 = sum(a * a for a in x)
        if r2 > 1.0:
            continue
        tot += 1
        xt, x1 = x[0], x[1]
        d2 = (x1 - f) ** 2 + xt * xt + x[2] ** 2 + x[3] ** 2
        if d2 <= 1.0:
            cnt["R2"] += 1
        if x1 >= f:
            cnt["R3h"] += 1
        if abs(x1) > f:
            cnt["R3y"] += 1
        if xt * xt + x1 * x1 > f * f:
            cnt["R4"] += 1
    return {k: v / tot for k, v in cnt.items()}


def eps(frac):
    return frac ** (-0.25) - 1.0 if frac > 0 else float("inf")


results = {}

# W1 -- rest-limit filter -------------------------------------------------
f_small = 1e-6
lims = {
    "R1": frac_R1(f_small),
    "R2": frac_R2(f_small),
    "R3h": frac_R3h(f_small),
    "R3y": frac_R3y(f_small),
    "R4": frac_R4(f_small),
}
survivors_ok = all(abs(lims[k] - 1.0) < 1e-4 for k in ("R1", "R2", "R3y", "R4"))
killed_ok = abs(lims["R3h"] - 0.5) < 1e-4       # discontinuous -> killed
# R3s: free set has measure zero for every f > 0 -> frac = 0, eps = inf: killed.
results["W1 rest-limit: R1/R2/R3y/R4 -> 1 continuously; R3h -> 1/2 KILLED; "
        "R3s -> 0 KILLED"] = survivors_ok and killed_ok

# W2 -- exact fractions vs closed leading forms vs MC ---------------------
w2_ok = True
lead = {
    "R2": lambda f: 1.0 - (8.0 / (3.0 * math.pi)) * f,
    "R3y": lambda f: 1.0 - (16.0 / (3.0 * math.pi)) * f,
    "R4": lambda f: 1.0 - 2.0 * f * f + f ** 4,
}
for f in (0.05, 0.1, 0.2):
    ex = {"R2": frac_R2(f), "R3h": frac_R3h(f), "R3y": frac_R3y(f),
          "R4": frac_R4(f)}
    mc = mc_fracs(f)
    for k in ex:
        if abs(ex[k] - mc[k]) > 0.005:          # ~4 sigma at N = 2e5
            w2_ok = False
    # leading-order agreement at small f
for f in (0.01, 0.02):
    if abs(frac_R2(f) - lead["R2"](f)) > 5e-4:
        w2_ok = False
    if abs(frac_R3y(f) - lead["R3y"](f)) > 5e-4:
        w2_ok = False
    if abs(frac_R4(f) - lead["R4"](f)) > 1e-12:  # exact
        w2_ok = False
results["W2 exact fractions match closed leading forms and MC "
        "(R2: 1-8f/3pi; R3y: 1-16f/3pi; R4: (1-f^2)^2 exact)"] = w2_ok

# W3 -- survivors pairwise inequivalent at leading order ------------------
f = 0.001                          # small enough that O(f^2) is negligible
e1, e2, e3, e4 = (eps(frac_R1(f)), eps(frac_R2(f)), eps(frac_R3y(f)),
                  eps(frac_R4(f)))
# R1: 0. R2, R3y: O(f) with distinct coefficients. R4: O(f^2).
c2 = e2 / f
c3 = e3 / f
c4 = e4 / (f * f)
w3_ok = (e1 == 0.0
         and abs(c2 - 2.0 / (3.0 * math.pi)) < 1e-3      # (1/4)*8/(3pi)
         and abs(c3 - 4.0 / (3.0 * math.pi)) < 1e-3      # (1/4)*16/(3pi)
         and abs(c4 - 0.5) < 1e-3                        # (1/4)*2
         and abs(c2 - c3) > 1e-3)
results["W3 survivors pairwise inequivalent: eps = {0, ~0.212f, ~0.424f, "
        "~f^2/2} -- the fork is REAL and consequential"] = w3_ok

# -------------------------------------------------------------------------
print("Patch 2492 -- M2 exclusion-rule fork pin -- verify")
print("=" * 70)
print(f"{'rule':6s} {'frac(f=0.1)':>12s} {'eps(f=0.1)':>12s}   leading eps")
table = [
    ("R1", frac_R1(0.1), "0 (no strain from motion)"),
    ("R2", frac_R2(0.1), "(2/3pi) f      ~ 0.2122 f   [n=1]"),
    ("R3y", frac_R3y(0.1), "(4/3pi) f      ~ 0.4244 f   [n=1]"),
    ("R4", frac_R4(0.1), "f^2/2 = gamma(f)-1 all orders [n=2]"),
]
for name, fr, note in table:
    print(f"{name:6s} {fr:12.6f} {eps(fr):12.6f}   {note}")
print("R3h/R3s: KILLED forward by the rest-limit filter (W1)")
print("=" * 70)
all_ok = True
for name, ok in results.items():
    print(("PASS  " if ok else "FAIL  ") + name)
    all_ok = all_ok and ok
print("=" * 70)
print("ALL PASS" if all_ok else "FAILURES PRESENT")
print()
print("FINDING (stated after computation, K3-safe): among the four")
print("survivors only R4 reproduces gamma; the postulates as currently")
print("developed do not discriminate among R1/R2/R3y/R4 -- the")
print("discriminating input is the per-Moment single-CP content of the")
print("motion state, i.e. the SF-6 inertia mechanism (UNPINNED; isolated")
print("investigation opened 14 Jul 2026, Patch 2470). Selecting R4 today")
print("would be selection by target (K3').")
raise SystemExit(0 if all_ok else 1)
