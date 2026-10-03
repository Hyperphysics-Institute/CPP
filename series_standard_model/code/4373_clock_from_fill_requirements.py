#!/usr/bin/env python3
"""Patch 4373 - the founder's clock-from-fill idea (3 Oct 2026): as a GP's Planck sphere fills deeper with
its origin's DI-bits, the space inside is informed in fewer re-radiations; this may slow the local
(apparent) clock without altering the PSR.  What shape must that clock effect have?

Notation: ruler = PSR ratio q_r; clock = lapse N; extra clock factor X = N / q_r (4372: N sqrt(A) = X).
Fill relative to ordinary space: g = f / f_0 = q_r^-3 (f = 1/(8 q_r^3), R-DIBIT-COUNT-AT-FLOOR).
Self-consistency (GR-1c): r^2 sqrt(A) N' = m, census rho = m/(2r) flat-harmonic.

  1. Einstein's black hole as a clock-from-fill law: X_E(g).
  2. Fill at the photon sphere and where the sphere becomes full, in Einstein's geometry.
  3. Light deflection (Cassini): a FIRST-order term X = 1 - a (g - 1) shifts gamma; bound on a.
  4. The quadratic coefficient Einstein needs, and the fraction the ringdown box needs (4372: lam >= 0.47).
  5. Mercury: any purely quadratic X keeps beta = 1 (4372); a clock effect with the PSR curve held fixed
     instead (no self-consistency) shifts beta.
"""
import sympy as sp
print(__doc__)

rho, g, a, c, eps, lam = sp.symbols('rho g a c epsilon lam', positive=True)

# 1. Einstein: q_r = 1/(1+rho)^2, N = (1-rho)/(1+rho), X = 1 - rho^2;  g = q_r^-3 = (1+rho)^6
XE = 1 - (g ** sp.Rational(1, 6) - 1) ** 2
print("1. Einstein's clock factor as a function of fill (g = fill / ordinary fill):  X_E(g) =", XE)
print("   check against 1 - rho^2 with g = (1+rho)^6:", sp.simplify(XE.subs(g, (1 + rho) ** 6) - (1 - rho ** 2)) == 0)
dg = sp.Symbol('dg')
print("   expansion about ordinary space (dg = g - 1):  X_E =", sp.series(XE.subs(g, 1 + dg), dg, 0, 4))
print("   -> no first-order term; X_E starts as -(dg)^2/36: the clock effect must grow as the SQUARE of the fill increase")

# 2. fill in Einstein's geometry
rho_ph = 1 / (2 * (1 + sp.sqrt(3) / 2))          # isotropic photon sphere r = m(1 + sqrt3/2)
for name, rv in (("photon sphere", rho_ph), ("sphere full (g = 8: ruler = 1/2)", sp.sqrt(2) - 1),
                 ("AP-5 cap (clock = 1/2)", sp.Rational(1, 3))):
    gv = (1 + rv) ** 6
    print(f"2. {name:34s} rho = {float(rv):.4f}  fill f = {float(gv)/8:.3f}  ruler q_r = {float((1+rv)**-2):.4f}"
          f"  clock N = {float((1-rv)/(1+rv)):.4f}  X = {float(1-rv**2):.4f}")
print("   In Einstein's geometry the sphere is ~52% full at the photon sphere (4371's 0.65 assumed one PSR).")
print("   The sphere becomes full (ruler 1/2) where the clock is 0.414, not 1/2: with clock != ruler, the AP-5")
print("   cap (clock 1/2, v = 2/3) and the black-hole floor (PSR = l_P/2, R-DIBIT-COUNT-AT-FLOOR) separate.")

# 3. first-order term -> gamma
# first order: N = 1 - 2 rho (normalisation fixes m); sqrt(A) = X / N; g - 1 = 3(1 - q_r) ~ 6 rho
Xlin = 1 - a * 6 * rho
sqrtA1 = sp.series(Xlin / (1 - 2 * rho), rho, 0, 2).removeO()
gam = sp.simplify(sqrtA1.coeff(rho) / 2)          # sqrt(A) = 1 + gamma * U, U = 2 rho
print(f"\n3. X = 1 - a (g-1): gamma = {gam}; Cassini |gamma - 1| < 2.3e-5  ->  |a| < {2.3e-5/3:.1e}")

# 4. quadratic coefficient
cE = sp.Rational(1, 36)
print(f"4. X = 1 - c (g-1)^2: Einstein c = 1/36 = {float(cE):.4f}; ringdown box (lam >= 0.47, eikonal) needs c >~ {0.47*float(cE):.4f}")
print("   (near ordinary space (g-1)^2 = 36 rho^2, so c (g-1)^2 = lam rho^2 with lam = 36 c)")

# 5. Mercury
N_self = 1 - eps + eps ** 2 / 2                     # self-consistent family: clock keeps Mercury's 1/2 (4372)
N_fixedPSR = sp.expand(sp.series(sp.exp(-eps) * (1 - lam * (eps / 2) ** 2), eps, 0, 3).removeO())
print("\n5. Self-consistent (GR-1c): clock N = 1 - eps + eps^2/2 for every lam (4372) -> beta = 1; the PSR's own")
print("   second order becomes 1/2 + lam/4 (rulers; unmeasured in the solar system).")
print("   PSR held at e^-eps and the clock multiplied by X instead: N =", N_fixedPSR,
      "-> beta = 1 - lam/4; Mercury |beta-1| < ~1e-4 -> lam < ~4e-4, far too small for the ringdown.")
print("   So the clock effect works only together with the self-consistency: the ratified 1/2 is the CLOCK's (Mercury),")
print("   and the PSR's own curve follows from it.")
