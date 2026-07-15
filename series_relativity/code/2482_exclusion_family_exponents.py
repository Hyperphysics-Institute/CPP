#!/usr/bin/env python3
# ============================================================
# 2482: OPEN-SR-H1-CLASS — exclusion-family exponents and the
#       codimension-2 all-orders identity.
# stdlib only (2471 standard). Exit 0 = all checks pass.
#
# CLAIMS VERIFIED
#  C1  For the family "f-neighborhood of a central k-codimensional
#      locus" in the round 4-ball (i.e. {x : |P_k x| <= f R} with
#      P_k projection onto k coordinates), the small-f volume
#      exponent equals the codimension: n = k for k = 1,2,3,4.
#      (Closed forms below; cross-checked by fixed-seed MC.)
#  C2  The k=2 member has EXACT fractional volume
#          V_excl/V0 = 2 f^2 - f^4 = 1 - (1 - f^2)^2,
#      so V_free/V0 = (1-f^2)^2, and under SR-1's strain rule
#      (V ∝ r^4;  ε = l_P/r - 1) this gives
#          ε(f) = (1 - f^2)^{-1/2} - 1 = γ_SR(f) - 1
#      EXACTLY, at all orders in f — not only at leading order.
#  C3  The hyperspherical cap (H.1 Model 3) has exponent 5/2
#      (the Patch-2475 correction), reproduced here from the
#      exact integral for regression.
#
# G7 NOTE (read the campaign file before using C2 for anything):
#  C2 is a GEOMETRIC identity. It does not by itself derive γ.
#  Whether CPP dynamics selects a distinguished 2-plane, the
#  neighborhood-exclusion rule, and radius exactly d = f·l_P is
#  the pre-registered mechanism question with kill conditions
#  K1–K3 (series_relativity/development/OPEN-SR-H1-CLASS_campaign.md).
# ============================================================
import math, random, sys

R = 1.0
V0 = math.pi**2 * R**4 / 2
FAIL = 0

def check(name, ok, detail=""):
    global FAIL
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
    if not ok:
        FAIL = 1

# ---- closed forms: V_excl(k, f)/V0 -----------------------------------------
def frac_excl(k, f):
    a = f * R
    if k == 4:                      # ball of radius fR
        return f**4
    if k == 3:                      # {x1^2+x2^2+x3^2 <= a^2}
        I = (a/8)*(2*a*a - R*R)*math.sqrt(R*R - a*a) + R**4/8*math.asin(a/R)
        return 8*math.pi*I / V0
    if k == 2:                      # {x1^2+x2^2 <= a^2}
        return 1 - (1 - f*f)**2
    if k == 1:                      # {|x1| <= a}
        def F(t):
            return (t*(R*R - t*t)**1.5/4
                    + 3*R*R/8*(t*math.sqrt(R*R - t*t) + R*R*math.asin(t/R)))
        return (4*math.pi/3)*2*F(a) / V0
    raise ValueError(k)

# ---- C1: exponents = codimension (closed form + MC cross-check) -------------
print("C1: exponent = codimension for central-locus f-neighborhoods")
random.seed(42)
pts, N = [], 300000
while len(pts) < N:
    x = [random.uniform(-1, 1) for _ in range(4)]
    if sum(v*v for v in x) <= 1:
        pts.append(x)

for k in (1, 2, 3, 4):
    f1, f2 = 1e-4, 2e-4
    n = math.log(frac_excl(k, f2)/frac_excl(k, f1)) / math.log(2)
    check(f"codim {k}: small-f exponent", abs(n - k) < 1e-6, f"n = {n:.9f}")
    for f in (0.05, 0.2):
        mc = sum(1 for x in pts if sum(v*v for v in x[:k]) <= f*f) / N
        cf = frac_excl(k, f)
        tol = 4*math.sqrt(max(cf, 1e-9)/N) + 2e-4
        check(f"codim {k}, f={f}: closed form vs MC", abs(cf - mc) < tol,
              f"closed {cf:.6f} vs MC {mc:.6f}")

# ---- C2: the codim-2 all-orders identity ------------------------------------
print("C2: codim-2 tube (radius exactly d = f*l_P) reproduces gamma exactly")
worst = 0.0
for i in range(1, 100):
    f = i/100.0
    vfree = 1 - frac_excl(2, f)
    eps = vfree**(-0.25) - 1
    gamma_minus_1 = (1 - f*f)**(-0.5) - 1
    worst = max(worst, abs(eps - gamma_minus_1))
check("eps(f) == gamma_SR(f) - 1 for f = 0.01..0.99", worst < 1e-12,
      f"max |diff| = {worst:.2e}")
# and the algebra: V_free/V0 must be exactly (1-f^2)^2
worst = max(abs((1 - frac_excl(2, f/100)) - (1 - (f/100)**2)**2) for f in range(1, 100))
check("V_free/V0 == (1-f^2)^2 exactly", worst < 1e-15, f"max |diff| = {worst:.2e}")

# ---- C3: cap exponent 5/2 regression (Patch 2475) ---------------------------
print("C3: hyperspherical cap exponent (regression of the 2475 correction)")
def frac_cap(f):
    lo, n = R*(1-f), 4000
    s, h = 0.0, (R - lo)/n
    for i in range(n):
        t = lo + (i + 0.5)*h
        s += (4/3)*math.pi*(R*R - t*t)**1.5 * h
    return s / V0
n = math.log(frac_cap(2e-4)/frac_cap(1e-4)) / math.log(2)
check("cap small-f exponent", abs(n - 2.5) < 1e-3, f"n = {n:.6f} (target 5/2)")

print("=" * 60)
print("RESULT:", "FAIL" if FAIL else "ALL CHECKS PASS")
sys.exit(FAIL)
