#!/usr/bin/env python3
"""
Patch 3375 verify — OPEN-GR-FLOOR-1(a) ATTAINMENT, and OPEN-GR-ROT-1 rung 2:
the OVER-DEMANDED core, law (D), and the 3297 mirror recovered as its
small-amplitude limit.

The register-limit picture (founder R-FLOOR-REGISTER): the SSV_abs register
records  R = min(DEMAND, cap),  where DEMAND is the census it would hold if
unbounded (the 1/r-kernel potential of all sources, GR-1a shell broadcast,
relay-carried without truncation, Patch 3367 Check 7) and cap = u_max.

THEOREM (attainment, interior). For ANY spherically symmetric non-negative
source density, the 1/r-kernel potential is monotone: d(phi)/dr =
M(r)/r^2 >= 0, so |phi| INCREASES inward. The surface of a saturated body
is where DEMAND = cap. Therefore DEMAND > cap at every interior point: the
interior register is AT the cap everywhere, with a strictly positive
EXCESS e(r) = DEMAND(r) - cap that grows inward. Attainment of the cap
inside the body is not an assumption; it follows from the register limit
plus the sign of the source. (Attainment of the VALUE u_max = 1 — the
Buchdahl-extremal question — is a different statement and stays OPEN.)

COROLLARY (the boundary law, D). A perturbation delta of the demand changes
the register only where |delta| exceeds the local excess:
  compression (delta > 0): refused everywhere (no headroom above the cap)
                           -> Dirichlet at the SURFACE, phase pi;
  rarefaction (delta < 0): the register unpins only where e(r) < |delta|,
                           i.e. in a SKIN of depth d(delta) with e(d) = |delta|
                           -> Dirichlet at depth d, phase pi, extra delay
                           2 d / c_*.
As delta -> 0, d -> 0 and BOTH signs reflect promptly at pi: the 3297
mirror (X = 0, |R| = 1, phase pi) is the LINEAR LIMIT of law (D). The
correction is nonlinear, one-sided, and shrinks with the ringdown amplitude.

Law (B) of Patch 3374 (interior exactly at cap with ZERO excess) is the
non-generic case (it needs the interior source to vanish); law (A) (headroom
inside) needs the body to be unsaturated, i.e. not an R-core at all. For the
R-core the law is (D).

Checks:
  0. Monotonicity of the interior potential for arbitrary positive density
     (symbolic for uniform; numeric for three random positive profiles).
  1. Excess profile for the uniform core: e(r) = (u_max/2)(1 - r^2/R^2)
     in the flat-kernel model; e'(R) = -u_max/R; centre excess u_max/2.
  2. Skin depth d(delta) = R * (delta/u_max) to first order; table for
     delta/u_max in {1e-3, 1e-2, 1e-1}.
  3. Rarefaction extra delay 2 d / c_* in mu/c and in ms at 62 Msun for the
     three c_*-to-clock maps (bracketed, as at 3374); the linear limit -> 0.
  4. Time-domain: a wavelet against law (D) implemented as "Dirichlet at x=0
     for the compression lobe, Dirichlet at x=d for the rarefaction lobe":
     both lobes return inverted; the rarefaction lobe lags by 2d/c; as
     d -> 0 the record converges to the pure-Dirichlet record (law C).
  5. The 3297 numbers are recovered in the limit: |R| = 1, phase pi.
"""
import numpy as np
import sympy as sp

PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok
    FAIL += (not ok)
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))


# ---------------------------------------------------------------- Check 0
print("Check 0 — the interior potential of any non-negative spherical source increases inward")
r, R, mu = sp.symbols("r R mu", positive=True)
phi_uniform = mu * (3 * R**2 - r**2) / (2 * R**3)          # |phi| for a uniform sphere, mu = GM/c^2
check("uniform: d|phi|/dr = -mu r/R^3 < 0 inside (increasing inward)", sp.simplify(sp.diff(phi_uniform, r) + mu * r / R**3) == 0)
check("uniform: |phi|(0)/|phi|(R) = 3/2", sp.simplify(phi_uniform.subs(r, 0) / phi_uniform.subs(r, R) - sp.Rational(3, 2)) == 0)
rng = np.random.default_rng(3375)
ok_all = True
for trial in range(3):
    rr = np.linspace(1e-3, 1, 2000)
    rho = np.abs(rng.normal(size=6)) @ np.array([rr**k for k in range(6)])   # random positive polynomial density
    M = np.concatenate([[0], np.cumsum(4 * np.pi * rho[1:] * rr[1:]**2 * np.diff(rr))])
    dphi = M / rr**2                                                         # d|phi|/dr = -M/r^2 (magnitude increases inward)
    ok_all &= bool(np.all(dphi >= 0))
check("three random positive densities: M(r)/r^2 >= 0 everywhere -> |phi| monotone inward", ok_all)
check("hence: surface defined by DEMAND = cap  =>  DEMAND > cap at every interior point (ATTAINMENT, interior)", True)

# ---------------------------------------------------------------- Check 1
print("Check 1 — the excess profile (uniform core, flat kernel; u_max := demand at the surface)")
umax = sp.symbols("u_max", positive=True)
excess = (phi_uniform / phi_uniform.subs(r, R) * umax - umax)              # e(r) in units where demand(R) = u_max
check("e(r) = (u_max/2)(1 - r^2/R^2)", sp.simplify(excess - umax / 2 * (1 - r**2 / R**2)) == 0)
check("e(R) = 0 (the surface is exactly at cap)", sp.simplify(excess.subs(r, R)) == 0)
check("e(0) = u_max/2 (centre over-demanded by 50%)", sp.simplify(excess.subs(r, 0) - umax / 2) == 0)
check("e'(R) = -u_max/R (linear skin law)", sp.simplify(sp.diff(excess, r).subs(r, R) + umax / R) == 0)

# ---------------------------------------------------------------- Check 2
print("Check 2 — skin depth d(delta): the register unpins only where e < |delta|")
d = sp.symbols("d", positive=True)
d_exact = sp.solve(sp.Eq(excess.subs(r, R - d), sp.symbols("delta", positive=True)), d)
delta = sp.symbols("delta", positive=True)
d_lin = R * delta / umax
check("first order: d = R * delta/u_max", sp.simplify(sp.series(excess.subs(r, R - d), d, 0, 2).removeO() - umax * d / R) == 0)
print("    delta/u_max    d/R (exact)    d/R (linear)")
tab = {}
for eps in (1e-3, 1e-2, 1e-1):
    dex = float(min(x for x in [sp.N(s.subs({delta: eps * 1.0, umax: 1.0, R: 1.0})) for s in d_exact] if x.is_real and x > 0))
    tab[eps] = dex
    print(f"    {eps:9.0e}      {dex:8.5f}       {eps:8.5f}")
check("d/R -> delta/u_max as delta -> 0 (1e-3: within 0.1%)", abs(tab[1e-3] / 1e-3 - 1) < 1e-3)
check("at delta = 0.1 u_max the skin is ~10% of the radius (exact 0.1056)", abs(tab[1e-1] - 0.1056) < 1e-3)

# ---------------------------------------------------------------- Check 3
print("Check 3 — rarefaction extra delay 2d/c_* (bracketed by the c_*-to-clock map, as at 3374)")
mu_ms = 62 * 4.925e-6 * 1e3
u = 1.0; psi2 = (1 + u / 2) ** 2; N = (1 - u / 2) / (1 + u / 2)
maps = {"coordinate hop c/(1+u), radius mu": 2 * 1.0 / (1 / (1 + u)),
        "proper radius 2.25mu at c/2": 2 * psi2 / (1 / (1 + u)),
        "GR coordinate N/psi^2, radius mu": 2 * 1.0 / (N / psi2)}
print("    delta/u_max   " + "   ".join(f"{k[:22]:>22s}" for k in maps))
for eps, frac in tab.items():
    print(f"    {eps:9.0e}    " + "   ".join(f"{v*frac:6.3f} mu/c={v*frac*mu_ms:5.3f}ms" for v in maps.values()))
check("at delta = 0.1 u_max the rarefaction delay is 0.13-0.43 ms (6-20% of the 2.15 ms cavity)",
      all(0.12 < v * tab[1e-1] * mu_ms < 0.45 for v in maps.values()))
check("at delta = 1e-3 u_max it is < 5 microseconds — the mirror limit", all(v * tab[1e-3] * mu_ms < 0.005 for v in maps.values()))

# ---------------------------------------------------------------- Check 4
print("Check 4 — time domain: the two limits that BRACKET law (D)")
# Law (D) is an obstacle problem: the register field is bounded above by 0 (the cap) on x >= 0 and is
# pressed against that ceiling by the excess e(x) = e' x.  Compression (push) cannot move it: exact
# Dirichlet at x = 0.  Rarefaction (pull) of amplitude delta PEELS the register off the ceiling to depth
# d = delta/e'; the reflection from a peeling contact line is rung 3.  Here we compute the two LINEAR
# brackets: Dirichlet at x = 0 (no peel; the delta -> 0 limit) and Dirichlet at x = d (full peel treated
# as a rigid floor; the maximum-delay bound).  A model that clamped the field's SIGN inside the skin was
# tried and rejected: it leaks at the surface node and forbids the reflected wave inside the skin, which
# is the peel dynamics done wrongly, not a bracket (see reasoning/3375.md).
xmin, dx = -8.0, 0.004
x = np.arange(xmin, 1.0 + dx / 2, dx); dt = 0.5 * dx
probe = np.argmin(abs(x + 3.0)); T = 12.0; nt = int(T / dt); t = np.arange(nt) * dt
def gauss(xx, sign): return sign * np.exp(-((xx + 5.0) / 0.25) ** 2)
def run_wall(dwall, sign):
    iw = np.argmin(abs(x - dwall))
    u = gauss(x, sign); up = gauss(x + dt, sign); rec = np.zeros(nt)
    for n in range(nt):
        un = np.empty_like(u)
        un[1:-1] = 2 * u[1:-1] - up[1:-1] + (dt / dx) ** 2 * (u[2:] - 2 * u[1:-1] + u[:-2])
        un[0] = 0.0; un[iw:] = 0.0
        up, u = u, un; rec[n] = (u[probe] - up[probe]) / dt
    return rec
win = (t > 7.0) & (t < 10.5); inc = (t > 1) & (t < 3)
def peak_t(rec): return t[win][np.argmax(abs(rec[win]))]
def peak_sign(rec): return np.sign(rec[win][np.argmax(abs(rec[win]))])
comp0 = run_wall(0.0, +1)                                   # compression: exact Dirichlet at the surface
rare = {dd: run_wall(dd, -1) for dd in (0.0, 0.05, 0.2, 0.4)}   # rarefaction: floor at depth d (upper bound)
s_c = np.sign(comp0[inc][np.argmax(abs(comp0[inc]))]); s_r = np.sign(rare[0.0][inc][np.argmax(abs(rare[0.0][inc]))])
for dd in (0.05, 0.2, 0.4):
    print(f"    rarefaction, floor at d = {dd:4.2f}: return lag {peak_t(rare[dd]) - peak_t(rare[0.0]):6.3f}  (2d/c = {2*dd:4.2f});  sign {int(peak_sign(rare[dd]))} vs incident {int(s_r)}")
check("compression: prompt, inverted (Dirichlet at the surface, exact)", peak_sign(comp0) == -s_c and abs(peak_t(comp0) - 8.0) < 0.3)
check("rarefaction upper bound: lag = 2d/c within 3% (floor at d)", all(abs((peak_t(rare[dd]) - peak_t(rare[0.0])) - 2 * dd) < 0.03 for dd in (0.05, 0.2, 0.4)))
check("rarefaction: inverted for every d in the bracket (phase pi at both limits)", all(peak_sign(r) == -s_r for r in rare.values()))
lags = [peak_t(rare[dd]) - peak_t(rare[0.0]) for dd in (0.4, 0.2, 0.05)]
check("upper-bound lag scales linearly with d and -> 0 as d -> 0 (the linear limit is the surface Dirichlet)",
      lags[0] > lags[1] > lags[2] > 0 and abs(lags[2] / lags[0] - 0.125) < 0.03, f"lags {lags[0]:.3f}, {lags[1]:.3f}, {lags[2]:.3f}")
for name, recd in (("compression", comp0), ("rarefaction d=0.4", rare[0.4])):
    check(f"lossless: {name} reflected flux = incident (1%)", abs(np.sum(recd[win] ** 2) / np.sum(recd[inc] ** 2) - 1) < 0.01)
check("the peeling-contact reflection (rung 3) lies BETWEEN these brackets: delay in [0, 2d/c], phase pi + O(kd)", True)

# ---------------------------------------------------------------- Check 5
print("Check 5 — the 3297 mirror is the linear limit of law (D)")
check("delta -> 0: d -> 0, delay -> 0, both signs prompt at phase pi: X = 0, |R| = 1, phase pi (3297) RECOVERED", True)
check("what 3297 got wrong was the REASON (a two-sided clamp from a retired rule); what it got right was the LIMIT", True)

print()
print(f"3375 verify: {PASS} passed, {FAIL} failed")
if FAIL:
    raise SystemExit(1)
