#!/usr/bin/env python3
"""
2951_xi2_relay_moments.py — verify script for the xi_2 relay computation
(Patch 2951, executes xi2_derivation_prereg.md §7).

stdlib only. Checks:
 1. Icosahedral stencil: 12 unit vectors, antipodal pairing (inversion).
 2. Second moments exactly isotropic: sum mu^2 = 4 for all directions.
 3. Fourth moments exactly isotropic: sum mu^4 = 12/5 (spherical 5-design).
 4. Fifth moments vanish (odd order, inversion + 5-design).
 5. Sixth moments ANISOTROPIC (first icosahedral invariant at degree 6):
    direction-dependence strictly nonzero; random-direction mean near 12/7.
 6. Continuous-time completion: fitted (kd)^2 coefficient of omega/ck - 1
    equals -1/40 exactly-within-fit-tolerance, direction-independent
    -> signed coefficient -1/20 half -> xi2 = 1/20, SUBLUMINAL sign.
 7. Leapfrog-class completion at sigma = 0.5: fitted coefficient equals
    (sigma^2/12 - 1/20)/2; zero crossing of the (kd)^2 coefficient at
    sigma^2 = 3/5 confirmed numerically.
 8. CFL bound of the leapfrog completion on the uniform edge stencil:
    numeric sigma_max = 2*sqrt(2)/sqrt(max_k Sigma) < 1, so the
    'one edge per Absolute Moment' ratio sigma = 1 is EXCLUDED for this
    completion class (evidence for underdetermination, not a relay claim).

NOTE (band discipline, prereg 2950 §4 CASE-DEP): the numbers 1/20,
(sigma^2/12 - 1/20), 1/30-at-sigma-1 etc. are properties of CANDIDATE
temporal completions exhibited to PROVE that registered data D
underdetermines xi_2 in both magnitude and sign. NO value of xi_2 is
minted by this script or its patch.
"""
import math
import random

random.seed(20260802)
PHI = (1 + 5 ** 0.5) / 2
TOL_EXACT = 1e-12
TOL_FIT = 5e-6

# ---- stencil -------------------------------------------------------------
def icosa_vertices():
    raw = []
    for s1 in (+1, -1):
        for s2 in (+1, -1):
            raw.append((0.0, s1 * 1.0, s2 * PHI))
            raw.append((s1 * 1.0, s2 * PHI, 0.0))
            raw.append((s2 * PHI, 0.0, s1 * 1.0))
    n = math.sqrt(1 + PHI * PHI)
    return [tuple(c / n for c in v) for v in raw]

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def rand_unit():
    while True:
        v = (random.gauss(0, 1), random.gauss(0, 1), random.gauss(0, 1))
        r = math.sqrt(dot(v, v))
        if r > 1e-9:
            return tuple(c / r for c in v)

E = icosa_vertices()
checks = []

def check(name, ok, detail=""):
    checks.append((name, ok, detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}")

# ---- 1: unit norm + antipodal pairing ------------------------------------
ok = len(E) == 12 and all(abs(dot(v, v) - 1) < TOL_EXACT for v in E)
paired = all(any(all(abs(v[i] + w[i]) < TOL_EXACT for i in range(3)) for w in E) for v in E)
check("1 stencil: 12 unit vectors, inversion-symmetric", ok and paired)

# ---- 2-5: moments --------------------------------------------------------
DIRS = [rand_unit() for _ in range(400)]
m2 = [sum(dot(k, e) ** 2 for e in E) for k in DIRS]
m4 = [sum(dot(k, e) ** 4 for e in E) for k in DIRS]
m5 = [sum(dot(k, e) ** 5 for e in E) for k in DIRS]
m6 = [sum(dot(k, e) ** 6 for e in E) for k in DIRS]

check("2 second moments = 4 (isotropic, all dirs)",
      max(abs(x - 4.0) for x in m2) < 1e-10, f"max dev {max(abs(x-4.0) for x in m2):.2e}")
check("3 fourth moments = 12/5 (5-design, all dirs)",
      max(abs(x - 12.0 / 5.0) for x in m4) < 1e-10, f"max dev {max(abs(x-2.4) for x in m4):.2e}")
check("4 fifth moments = 0 (all dirs)",
      max(abs(x) for x in m5) < 1e-10, f"max |m5| {max(abs(x) for x in m5):.2e}")
spread6 = max(m6) - min(m6)
mean6 = sum(m6) / len(m6)
check("5 sixth moments anisotropic; mean near 12/7",
      spread6 > 1e-3 and abs(mean6 - 12.0 / 7.0) < 0.02,
      f"spread {spread6:.4f}, mean {mean6:.4f} (12/7={12/7:.4f})")

# ---- dispersion machinery ------------------------------------------------
def Sigma(kd, khat):
    return sum(1.0 - math.cos(kd * dot(khat, e)) for e in E)

def omega_ct(kd, khat):
    # continuous-time: omega^2 = (c^2/2 d^2) * Sigma  (c=d=1)
    return math.sqrt(0.5 * Sigma(kd, khat))

def omega_lf(kd, khat, sigma):
    # leapfrog: sin^2(omega tau/2) = (tau^2/4) * Omega^2, tau = sigma (c=d=1)
    arg = (sigma / 2.0) * math.sqrt(0.5 * Sigma(kd, khat))
    if arg > 1.0:
        raise ValueError("outside dispersion branch")
    return (2.0 / sigma) * math.asin(arg)

def fit_quad_coeff(omega_fn):
    # fit a in omega/(c k) = 1 + a (kd)^2 over small kd, several directions
    coeffs = []
    for khat in DIRS[:25]:
        xs, ys = [], []
        for kd in (0.02, 0.03, 0.04, 0.05, 0.06):
            xs.append(kd * kd)
            ys.append(omega_fn(kd, khat) / kd - 1.0)
        n = len(xs)
        sx = sum(xs); sy = sum(ys)
        sxx = sum(x * x for x in xs); sxy = sum(x * y for x, y in zip(xs, ys))
        a = (n * sxy - sx * sy) / (n * sxx - sx * sx)
        coeffs.append(a)
    return sum(coeffs) / len(coeffs), max(coeffs) - min(coeffs)

# ---- 6: continuous-time completion ---------------------------------------
a_ct, spread_ct = fit_quad_coeff(omega_ct)
target_ct = -1.0 / 40.0
check("6 continuous-time: coeff = -1/40, dir-independent",
      abs(a_ct - target_ct) < TOL_FIT and spread_ct < TOL_FIT,
      f"fit {a_ct:.8f} vs {target_ct:.8f}, dir spread {spread_ct:.2e} (residual = degree-6 leakage at O(kd^4))")

# ---- 7: leapfrog completion ----------------------------------------------
sig = 0.5
a_lf, spread_lf = fit_quad_coeff(lambda kd, kh: omega_lf(kd, kh, sig))
target_lf = (sig * sig / 12.0 - 1.0 / 20.0) / 2.0
sig0 = math.sqrt(3.0 / 5.0)
a_z, _ = fit_quad_coeff(lambda kd, kh: omega_lf(kd, kh, sig0))
check("7 leapfrog sigma=0.5 coeff matches (sig^2/12-1/20)/2; zero at sig^2=3/5",
      abs(a_lf - target_lf) < TOL_FIT and abs(a_z) < TOL_FIT,
      f"fit {a_lf:.8f} vs {target_lf:.8f}; at crossing {a_z:.2e}")

# ---- 8: CFL of leapfrog completion ---------------------------------------
smax_sigma = 0.0
for _ in range(4000):
    khat = rand_unit()
    kd = random.uniform(0.0, 4.0 * math.pi)
    smax_sigma = max(smax_sigma, Sigma(kd, khat))
sigma_max = 2.0 * math.sqrt(2.0) / math.sqrt(smax_sigma)
check("8 leapfrog CFL: sigma_max < 1 (sigma=1 excluded for this class)",
      sigma_max < 1.0, f"max Sigma {smax_sigma:.4f} -> sigma_max {sigma_max:.4f}")

# ---- summary -------------------------------------------------------------
n_pass = sum(1 for _, ok, _ in checks if ok)
print(f"\n{n_pass}/{len(checks)} checks PASS")
if n_pass != len(checks):
    raise SystemExit(1)
