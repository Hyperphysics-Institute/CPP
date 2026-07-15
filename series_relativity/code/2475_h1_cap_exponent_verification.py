#!/usr/bin/env python3
"""
SR-1 Appendix H.1: verification of the hyperspherical-cap exponent.
===================================================================

Patch 2475. Dependencies: NONE (Python 3 stdlib only).

H.1 as published states:

  Theorem (Geometric Insufficiency). ... eps_geom = O(f^n) with n <= 1 at small f.
  Since gamma_SR - 1 = O(f^2), no such model recovers the Lorentz factor.

  "The proof follows directly from the integral Eq. (cap_integral): any simply
   connected excluded region of height h = fR in a 4D hypersphere has volume
   [scaling as f^{1/2}]."

  Elimination table: Hyperspherical cap -> r_free = l_P(1 - sqrt(2f)/3pi),
                     eps ~ sqrt(2f)/3pi, "No (f^{1/2})".

THIS IS WRONG. Verified below:

 V1  The exact cap fraction scales as f^{5/2}, not f^{1/2}.
     A cap of height h on a d-ball has volume ~ h^{(d+1)/2}; for d = 4 that is
     h^{5/2}. The closed form is V_cap/V_4 = 8(2f)^{5/2}/(15*pi) + O(f^{7/2}).
 V2  Hence eps_cap ~ 0.2401 * f^{5/2}, NOT sqrt(2f)/(3pi).
 V3  *** The theorem's claim n <= 1 is FALSE, refuted by its own cap model
     (n = 5/2 > 1). The stated proof is void: its premise is the erroneous
     f^{1/2} scaling. ***
 V4  The CONCLUSION survives for the three models examined -- n in {1, 1, 5/2},
     none equal 2, so none recovers gamma. But it survives as three worked
     examples, NOT as the class theorem the paper asserts.
 V5  *** The corrected exponents BRACKET the target: 1 < 2 < 5/2. The paper's
     only class-coverage argument was "all n <= 1 < 2", which is false. Nothing
     now excludes an intermediate exclusion geometry with V_excl ~ f^2, which
     would yield eps ~ f^2 exactly as required. The published (erroneous)
     theorem CLOSED a route that may in fact be OPEN. ***

Author: Opus (Anthropic), for Thomas Lee Abshier / Hyperphysics Institute.
"""

import math

results = {}


def check(tag, got, want, tol=1e-6):
    ok = abs(got - want) <= tol * max(1.0, abs(want))
    results[tag] = ok
    print(f"  [{'PASS' if ok else 'FAIL'}] {tag:46s} got={got:.10g}  want={want:.10g}")
    return ok


# --- exact cap fraction, by Simpson on the paper's own integral -------------
def cap_fraction(f, n=200001):
    """V_cap/V_4 for a 4-ball, cap height h = f*R.  Paper's Eq. (cap_integral):
       V_cap = (4 pi R^4/3) * Int_{arcsin(1-f)}^{pi/2} cos^4(th) dth ;  V_4 = pi^2 R^4/2."""
    a, b = math.asin(1.0 - f), math.pi / 2.0
    if n % 2 == 0:
        n += 1
    h = (b - a) / (n - 1)
    s = 0.0
    for i in range(n):
        w = 1 if i in (0, n - 1) else (4 if i % 2 else 2)
        s += w * math.cos(a + i * h) ** 4
    I = s * h / 3.0
    return (4.0 * math.pi / 3.0) * I / (math.pi ** 2 / 2.0)


print("=" * 76)
print("V1  The exact cap fraction scales as f^(5/2), not f^(1/2)")
print("=" * 76)
print(f"  {'f':>10} {'exact':>16} {'paper 4sqrt(2f)/3pi':>22} {'8(2f)^2.5/(15pi)':>20}")
for f in (1e-2, 1e-3, 1e-4, 1e-5):
    ex = cap_fraction(f)
    paper = 4.0 * math.sqrt(2 * f) / (3 * math.pi)
    mine = 8.0 * (2 * f) ** 2.5 / (15 * math.pi)
    print(f"  {f:>10.0e} {ex:>16.6e} {paper:>22.6e} {mine:>20.6e}")

e1, e2 = cap_fraction(1e-3), cap_fraction(1e-4)
n_measured = math.log(e1 / e2) / math.log(1e-3 / 1e-4)
check("cap exponent n = 5/2 (paper implies 1/2)", n_measured, 2.5, 2e-3)
check("closed form 8(2f)^2.5/(15pi) matches exact",
      8.0 * (2e-4) ** 2.5 / (15 * math.pi) / cap_fraction(1e-4), 1.0, 1e-3)
check("paper's formula is WRONG at f=1e-4 (ratio != 1)",
      1.0 if abs(4 * math.sqrt(2e-4) / (3 * math.pi) / cap_fraction(1e-4) - 1.0) > 1e3 else 0.0, 1.0, 0)
print(f"        paper's formula overstates the cap by a factor "
      f"{4*math.sqrt(2e-4)/(3*math.pi)/cap_fraction(1e-4):.3e} at f = 1e-4")

# --- V2: the strain ---------------------------------------------------------
print()
print("=" * 76)
print("V2  eps_cap from V ~ r^4 volume conservation")
print("=" * 76)
# r_free = l_P (1 - V_cap/V_4)^{1/4};  eps = (l_P - r_free)/r_free
def eps_cap(f):
    s = (1.0 - cap_fraction(f)) ** 0.25
    return (1.0 - s) / s
pred = 2.0 * (2.0 ** 2.5) / (15 * math.pi)          # eps ~ pred * f^{5/2}
check("eps_cap coefficient = 2*2^2.5/(15pi) ~ 0.2401", pred, 0.240084, 1e-4)
check("eps_cap(1e-3) matches pred*f^2.5", eps_cap(1e-3) / (pred * (1e-3) ** 2.5), 1.0, 1e-2)
print(f"        eps_cap ~= {pred:.6f} * f^(5/2)   [paper: sqrt(2f)/(3pi) ~ f^(1/2)]")

# --- V3/V4/V5: the theorem --------------------------------------------------
print()
print("=" * 76)
print("V3/V4/V5  What this does to the Geometric Insufficiency Theorem")
print("=" * 76)
models = [("Model 1  linear subtraction", 1.0),
          ("Model 2  corridor exclusion", 1.0),
          ("Model 3  hyperspherical cap", 2.5)]
print(f"  {'model':32s} {'exponent n':>11}  {'n <= 1 (theorem)':>17}  {'n == 2 (needed)':>16}")
for nm, n in models:
    print(f"  {nm:32s} {n:>11.1f}  {'YES' if n <= 1 else '*** NO ***':>17}  {'yes' if abs(n-2) < 1e-9 else 'no':>16}")
check("theorem's claim (all n <= 1) is FALSE", 1.0 if max(n for _, n in models) > 1 else 0.0, 1.0, 0)
check("conclusion holds for the 3 models (no n == 2)",
      0.0 if any(abs(n - 2) < 1e-9 for _, n in models) else 1.0, 1.0, 0)
check("corrected exponents BRACKET the target n=2",
      1.0 if min(n for _, n in models) < 2 < max(n for _, n in models) else 0.0, 1.0, 0)

print()
n_ok = sum(results.values())
print("=" * 76)
print(f"SUMMARY: {n_ok}/{len(results)} checks passed")
print("=" * 76)
print("""
VERDICT
  * H.1's cap expansion is wrong: f^(1/2) published, f^(5/2) correct.
  * The THEOREM AS STATED ("n <= 1 for all models") is FALSE -- refuted by its
    own Model 3 (n = 5/2). The stated proof is void; its premise is the error.
  * The CONCLUSION ("none of the three recovers gamma") SURVIVES: n in {1,1,5/2},
    none equal 2.  But as three worked examples, not a theorem about the class.
  * The class-coverage claim is now UNSUPPORTED and the question is OPEN: the
    natural models bracket the target (1 < 2 < 5/2), so an exclusion geometry
    with V_excl ~ f^2 would give eps ~ f^2 exactly as required. The published
    theorem closed a route that may be open.

  Note the direction of the error: Model 3 fails by giving too LITTLE strain
  (f^2.5 < f^2 at small f), not too much as the paper asserts. The three models
  no longer sit on one side of the target -- they straddle it.
""")
raise SystemExit(0 if n_ok == len(results) else 1)
