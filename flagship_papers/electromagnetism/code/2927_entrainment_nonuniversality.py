"""PATCH 2927 — THE ENTRAINMENT CANCELLATION POINT IS NOT UNIVERSAL, AND
THE ENTRAINED DRIVE IS CLOSED-FORM THROUGH O(eps^2).

Follow-on to Patch 2926. The 2900 entrainment result (one dial eps* =
0.0589 kills the beta^2 curvature) was measured at ONE configuration
(m=2, r=[1,12]); the eps=0 robustness grid was never run at eps > 0.
The 2926 factorization predicts each eps order adds radial weight r^-3,
so eps* should track radial-integral ratios, not be universal.

RESULTS (all pre-registered in session chat before execution):

TEST A (universality): eps* spans 0.00735 .. 0.44620 across the six
  2900-robustness configurations — a factor of 61. UNIVERSALITY DEAD.
  At fixed m = 2 the ratio R_m/R_{m+3} predicts the variation to 5%.

ANALYTIC THEORY: with Phi(b) = sum 8 b^{2n+1}/[(2n-1)(2n+1)(2n+3)]
  (Patch 2926) the entrained drive expands, all closed form:
    D(b; eps) = 2 pi [ R_m Phi(b) + eps R_{m+3} Psi(b;m)
                       + eps^2 R_{m+6} X(b;m) + O(eps^3) ],
  R_p = int r^-p dr, odd in b, with exact series coefficients
  (derived via gradient/Hessian contraction of G(y) = y_x/|y|^{m+1}
  against the exact retarded unit vector; the m-dependence enters only
  through prefactors, so five m-free angular integrals determine all):
    psi1(m) = -8(2m+1)/3        psi3(m) = -8(4m+1)/3
    chi1(m) = -4(m+1)(3m+2)/3   chi3(m) = -4(m+1)(113m+22)/15
  Hence dc/deps|_0 = -(2/5)(11m+3) R_{m+3}/R_m  (= -10 R'/R at m=2),
  and the cancellation point is the smallest positive root of
    R_m phi3 + eps R_{m+3} psi3(m) + eps^2 R_{m+6} chi3(m) = 0,
  phi3 = 8/15. eps* is a JOINT property of the kinematics and of WHERE
  the Sea's response lives (the R_p). The 2900 "physically modest ~6%
  dial" is r-range-contingent. Effective expansion parameter
  eps |chi3 R_{m+6} / (psi3 R_{m+3})| ~ eps/rmin^3 — which is why
  eps* = 0.446 at rmin = 2 is MORE perturbative than 0.171 at rmin = 1.

CHECK LEDGER (split verdicts disclosed, not smoothed):
  (a)  FD first derivative dD/deps at eps = 0 vs 2 pi R_5 Psi:
       deviation equals the discrete R_5 radial-sum offset. PASS.
  (a2) FD second derivative vs 2 pi R_8 X at m = 2: deviation equals
       the discrete R_8 offset. PASS (validates order eps^2
       independently of the symbolic route).
  (b)  O(eps^2)-truncated eps* vs measured: FAILED the pre-registered
       5% band on three configs (6-10% low). Pre-registered attribution
       tests: (i) with DISCRETE radial sums the gap closes to 1.5-3.2%
       on five configs (m = 1 remains 9.7%); (ii) measured eps* rises
       monotonically under grid refinement toward the continuum root;
       (iii) residuals ORDER by the next-term parameter
       eps*|chi3 R_{m+6}/(psi3 R_{m+3})|: 0.46 -> 9.7%, ~0.28 -> ~3%,
       0.21 -> 1.5% (ordering enforced where parameters are separated
       by > 10%; the three ~0.28 configs are statistical ties).
       Attributed: discrete radial sums + O(eps^3), right sign, right
       ordering, right inversion.
  (c)  k(eps) drift: analytic k(0) x discrete-R_2 factor = -15.554
       (2900: -15.554); k(eps*) to O(eps^2) = -16.9 (2900: -16.96,
       0.3%). PASS.

Run: python3 2927_entrainment_nonuniversality.py   (sympy + numpy)
"""
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss

FAIL = []


def check(name, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        FAIL.append(name)


phi3 = 8.0 / 15
psi1 = lambda m: -8 * (2 * m + 1) / 3
psi3 = lambda m: -8 * (4 * m + 1) / 3
chi1 = lambda m: -4 * (m + 1) * (3 * m + 2) / 3
chi3 = lambda m: -4 * (m + 1) * (113 * m + 22) / 15


def Rint(p, a, bnd):
    return np.log(bnd / a) if p == 1 else (a ** (1 - p) - bnd ** (1 - p)) / (p - 1)


def Rdisc(p, a, bnd, nr):
    rg = np.linspace(a, bnd, nr)
    return float(np.sum(rg ** (-float(p))) * (rg[1] - rg[0]))


# ----------------------------------------------------------------------
# PART A — symbolic: exact series coefficients, symbolic m throughout.
# Gradient/Hessian contraction of G(y) = y_x/|y|^{m+1} against the exact
# retarded unit vector u (Patch 2926 closed forms):
#   u_x = -[mu(1+b^2)+2b]/g,   (u.y)/r = -(1 - 2 b^2 (1-mu^2)/g),
#   g = 1 + 2 b mu + b^2,  |u| = 1.
# Order eps^1 (r-stripped): (1-b^2)^4 g^-4 [u_x - (m+1) mu U]
# Order eps^2 (r-stripped): (1/2)(1-b^2)^6 g^-6 (m+1)
#                               [-(2 u_x U + mu) + (m+3) mu U^2]
# m enters only via prefactors -> five m-free angular integrals suffice.
# ----------------------------------------------------------------------
print("PART A — symbolic derivation (exact, symbolic m)")
b, mu = sp.symbols('beta mu', positive=True)
M = sp.symbols('m')
g = 1 + 2 * b * mu + b ** 2
uxh = -(mu * (1 + b ** 2) + 2 * b) / g
U = -(1 - 2 * b ** 2 * (1 - mu ** 2) / g)


def ang(expr):
    J = sp.integrate(sp.expand(sp.cancel(expr)), (mu, -1, 1))
    ser = sp.expand(sp.series(J, b, 0, 5).removeO())
    return sp.nsimplify(ser.coeff(b, 1)), sp.nsimplify(ser.coeff(b, 3))


D1, D3 = ang((1 - b ** 2) ** 4 * uxh / g ** 4)
E1, E3 = ang((1 - b ** 2) ** 4 * mu * U / g ** 4)
A1, A3 = ang((1 - b ** 2) ** 6 * uxh * U / g ** 6)
B1, B3 = ang((1 - b ** 2) ** 6 * mu / g ** 6)
C1, C3 = ang((1 - b ** 2) ** 6 * mu * U ** 2 / g ** 6)

psi1_sym = sp.factor(D1 - (M + 1) * E1)
psi3_sym = sp.factor(D3 - (M + 1) * E3)
chi1_sym = sp.factor(sp.Rational(1, 2) * (M + 1) * (-2 * A1 - B1 + (M + 3) * C1))
chi3_sym = sp.factor(sp.Rational(1, 2) * (M + 1) * (-2 * A3 - B3 + (M + 3) * C3))
print(f"  psi1(m) = {psi1_sym}    psi3(m) = {psi3_sym}")
print(f"  chi1(m) = {chi1_sym}    chi3(m) = {chi3_sym}")
check("psi1 = -8(2m+1)/3 and psi3 = -8(4m+1)/3 (exact symbolic)",
      sp.simplify(psi1_sym + sp.Rational(8, 3) * (2 * M + 1)) == 0
      and sp.simplify(psi3_sym + sp.Rational(8, 3) * (4 * M + 1)) == 0)
check("chi1 = -4(m+1)(3m+2)/3 and chi3 = -4(m+1)(113m+22)/15 (exact symbolic)",
      sp.simplify(chi1_sym + sp.Rational(4, 3) * (M + 1) * (3 * M + 2)) == 0
      and sp.simplify(chi3_sym + sp.Rational(4, 15) * (M + 1) * (113 * M + 22)) == 0)

# full angular functions for check (a)/(a2), via Gauss-Legendre
xg, wg = leggauss(400)


def Psi_full(bv, m):
    gg = 1 + 2 * bv * xg + bv ** 2
    ux_ = -(xg * (1 + bv ** 2) + 2 * bv) / gg
    Uv = -(1 - 2 * bv ** 2 * (1 - xg ** 2) / gg)
    return (1 - bv ** 2) ** 4 * float(np.sum(wg * (ux_ - (m + 1) * xg * Uv)
                                             / gg ** 4))


def X_full(bv, m):
    gg = 1 + 2 * bv * xg + bv ** 2
    ux_ = -(xg * (1 + bv ** 2) + 2 * bv) / gg
    Uv = -(1 - 2 * bv ** 2 * (1 - xg ** 2) / gg)
    return 0.5 * (1 - bv ** 2) ** 6 * (m + 1) * float(
        np.sum(wg * (-(2 * ux_ * Uv + xg) + (m + 3) * xg * Uv ** 2) / gg ** 6))


# ----------------------------------------------------------------------
# PART B — numeric machinery (verbatim 2900 entrained drive)
# ----------------------------------------------------------------------
def geometry(v, rmin, rmax, nr, nth, c=1.0):
    rg = np.linspace(rmin, rmax, nr)
    th = np.linspace(0, np.pi, nth)
    R, TH = np.meshgrid(rg, th, indexing='ij')
    yx, yp = R * np.cos(TH), R * np.sin(TH)
    w = (R ** 2) * np.sin(TH) * (rg[1] - rg[0]) * (th[1] - th[0]) * 2 * np.pi
    y = np.hypot(yx, yp)
    t2 = -y / c
    A = yx - v * t2
    disc = A * A * v * v + (c * c - v * v) * (A * A + yp * yp)
    ss = (A * v + np.sqrt(disc)) / (c * c - v * v)
    t1 = t2 - ss
    return yx, yp, w, c * ss, v * t1


def drive(v, eps, m, rmin, rmax, nr=480, nth=720):
    yx, yp, w, d_out, cx = geometry(v, rmin, rmax, nr, nth)
    amp_ = 1.0 / d_out ** 2
    ux_, up_ = (cx - yx) / d_out, (0.0 - yp) / d_out
    ypx_, ypp_ = yx + eps * amp_ * ux_, yp + eps * amp_ * up_
    yn = np.hypot(ypx_, ypp_)
    return float(np.sum((amp_ / yn ** m) * (ypx_ / yn) * w))


BETAS = np.array([0.01, 0.02, 0.03, 0.05, 0.08, 0.10, 0.15, 0.20])
XD = np.column_stack([np.ones_like(BETAS), BETAS ** 2, BETAS ** 4])


def cfit(eps, m, a, bnd, nr=480, nth=720):
    y = np.array([drive(bb, eps, m, a, bnd, nr, nth) for bb in BETAS]) / BETAS
    coef, *_ = np.linalg.lstsq(XD, y, rcond=None)
    return -coef[1] / coef[0]


def bisect(m, a, bnd, lo, hi, nr=480, nth=720, iters=16):
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        lo, hi = (mid, hi) if cfit(mid, m, a, bnd, nr, nth) > 0 else (lo, mid)
    return 0.5 * (lo + hi)


# ----------------------------------------------------------------------
# PART C — TEST A: non-universality of eps*
# ----------------------------------------------------------------------
print("\nPART C — TEST A: universality of eps*")
CONFIGS = [(2, 1, 12), (2, 1, 20), (2, 2, 12), (2, 0.5, 12),
           (1, 1, 12), (3, 1, 12)]
meas = {}
for (m, a, bnd) in CONFIGS:
    guess = (0.0589 * (Rint(m, a, bnd) / Rint(m + 3, a, bnd))
             / (Rint(2, 1, 12) / Rint(5, 1, 12)))
    meas[(m, a, bnd)] = bisect(m, a, bnd, guess * 0.2, guess * 5.0)
    print(f"  ({m},[{a},{bnd}])  eps* = {meas[(m, a, bnd)]:.5f}")
vals = np.array(list(meas.values()))
check(f"NON-UNIVERSAL: eps* span factor {vals.max() / vals.min():.0f} > 10",
      vals.max() / vals.min() > 10)
check("fixed-m radial scaling R_m/R_{m+3} tracks eps* to 5%",
      all(abs(meas[c] / meas[(2, 1, 12)]
              / ((Rint(2, c[1], c[2]) / Rint(5, c[1], c[2]))
                 / (Rint(2, 1, 12) / Rint(5, 1, 12))) - 1) < 0.05
          for c in CONFIGS if c[0] == 2))

# ----------------------------------------------------------------------
# PART D — CHECKS (a) and (a2): FD derivatives vs analytic terms
# ----------------------------------------------------------------------
print("\nPART D — CHECKS (a), (a2)")
BT = np.array([0.02, 0.05, 0.10, 0.15, 0.20])
h = 1e-4
fd1 = np.array([(drive(t, h, 2, 1, 12) - drive(t, -h, 2, 1, 12)) / (2 * h)
                for t in BT])
an1 = 2 * np.pi * Rint(5, 1, 12) * np.array([Psi_full(t, 2) for t in BT])
off5 = Rdisc(5, 1, 12, 480) / Rint(5, 1, 12) - 1
check("(a) FD dD/deps offset equals discrete R_5 offset (<2e-4 abs)",
      bool(np.all(np.abs(fd1 / an1 - 1 - off5) < 2e-4)))

h2 = 0.01
fd2 = np.array([(drive(t, h2, 2, 1, 12) - 2 * drive(t, 0, 2, 1, 12)
                 + drive(t, -h2, 2, 1, 12)) / h2 ** 2 / 2 for t in BT])
an2 = 2 * np.pi * Rint(8, 1, 12) * np.array([X_full(t, 2) for t in BT])
off8 = Rdisc(8, 1, 12, 480) / Rint(8, 1, 12) - 1
check("(a2) FD (1/2) d2D/deps2 offset equals discrete R_8 offset (<1e-2 abs)",
      bool(np.all(np.abs(fd2 / an2 - 1 - off8) < 1e-2)))

# ----------------------------------------------------------------------
# PART E — CHECK (b): eps* prediction and attribution
# ----------------------------------------------------------------------
print("\nPART E — CHECK (b): eps* prediction and attribution")


def eps_quad(m, a, bnd, R):
    A0, A1_, A2_ = R(m) * phi3, R(m + 3) * psi3(m), R(m + 6) * chi3(m)
    roots = [rr.real for rr in np.roots([A2_, A1_, A0])
             if abs(rr.imag) < 1e-12 and rr.real > 0]
    return min(roots)


print(f"  {'config':>14} | {'quad(cont)':>10} | {'quad(disc)':>10} | "
      f"{'measured':>8} | next-term param")
rows = []
for (m, a, bnd) in CONFIGS:
    ec = eps_quad(m, a, bnd, lambda p: Rint(p, a, bnd))
    ed = eps_quad(m, a, bnd, lambda p: Rdisc(p, a, bnd, 480))
    mv = meas[(m, a, bnd)]
    par = mv * abs(chi3(m) * Rint(m + 6, a, bnd)
                   / (psi3(m) * Rint(m + 3, a, bnd)))
    rows.append((abs(mv / ed - 1), par))
    print(f"  ({m},[{a:>4},{bnd:>2}]) | {ec:10.5f} | {ed:10.5f} | "
          f"{mv:8.5f} | {par:.2f}")
check("discrete-R prediction within 3.5% wherever next-term param < 0.3",
      all(res < 0.035 for res, par in rows if par < 0.3))
check("residuals ordered by next-term parameter (pairs separated > 10%)",
      all((p1 - p2) * (r1 - r2) > 0
          for i, (r1, p1) in enumerate(rows) for (r2, p2) in rows[i + 1:]
          if abs(p1 / p2 - 1) > 0.10))
e0 = meas[(2, 1, 12)]
e1 = bisect(2, 1, 12, 0.03, 0.12, 960, 1440, iters=14)
e2 = bisect(2, 1, 12, 0.03, 0.12, 1920, 2880, iters=12)
cont = eps_quad(2, 1, 12, lambda p: Rint(p, 1, 12))
print(f"  refinement: eps*(480) = {e0:.5f}  (960) = {e1:.5f}  "
      f"(1920) = {e2:.5f}  [continuum quad root {cont:.5f}]")
check("measured eps* rises monotonically toward the continuum root",
      e0 < e1 < e2 < cont)

# ----------------------------------------------------------------------
# PART F — CHECK (c): k(eps) drift
# ----------------------------------------------------------------------
print("\nPART F — CHECK (c): k drift")
off2 = Rdisc(2, 1, 12, 480) / Rint(2, 1, 12) - 1
k0 = 2 * np.pi * Rint(2, 1, 12) * (-8 / 3)
check("k(0) x discrete-R_2 factor = -15.554 (2900) to 0.1%",
      abs(k0 * (1 + off2) / -15.554 - 1) < 1e-3)
k_star = 2 * np.pi * (Rint(2, 1, 12) * (-8 / 3)
                      + e0 * Rint(5, 1, 12) * psi1(2)
                      + e0 ** 2 * Rint(8, 1, 12) * chi1(2))
check("k(eps*) to O(eps^2) matches 2900's -16.96 to 1%",
      abs(k_star * (1 + off2) / -16.96 - 1) < 0.01)

print("\n" + ("ALL CHECKS PASS" if not FAIL else f"FAILURES: {FAIL}"))
raise SystemExit(1 if FAIL else 0)
