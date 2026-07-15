#!/usr/bin/env python3
"""
SR-1 verification: what the 600-cell geometry does and does not fix about k.
===========================================================================

Patch 2471. Replaces the non-functional stubs cited by SR-1 App. A.7
(series_relativity/notebooks/600cell_monte_carlo_voronoi_k_fit.py, whose vertex
list is empty; and 600-cell-monte-carlo-k-fit.py, whose Monte-Carlo loop is
`pass` and whose "results" are hard-coded comments).

Everything below is COMPUTED. No result is asserted.

Claims tested
-------------
 C1  The 600-cell vertex set, edge length a = 1/phi, and coordination z = 12
     are reproduced from the binary icosahedral group 2I.
 C2  V_0 = 600*sqrt(2)/(12*phi^3) is reproduced.
 C3  alpha_geom = 3*Abar/V_0 = 3(11+5sqrt5)sqrt(5+sqrt5)/320 ~ 0.5594
     is reproduced in unit-CIRCUMRADIUS coordinates.
 C4  *** alpha_geom is NOT dimensionless. *** Abar ~ L^2, V_0 ~ L^3, so
     3*Abar/V_0 ~ 1/L. Its numerical value tracks the length unit:
     0.5594 per circumradius, 0.2444 per insphere radius (= per l_P, the
     physical Planck normalisation). It is therefore not an "exact algebraic
     constant" simpliciter; it is exact only relative to a coordinate choice.
 C5  *** alpha cancels identically in k*dSSV. *** For ANY alpha,
     k = alpha*l_P^3/E_P together with dSSV = E_kin/(alpha*l_P^3) gives
     k*dSSV = E_kin/E_P = gamma-1. Hence k's numerical value is a
     NORMALISATION CONVENTION, not a prediction, and no choice of prefactor
     is more "derived" than any other.
 C6  Lorentz recovery is exact under every convention -- and is exact because
     the energy-momentum bridge (App. A.8.1) DEFINES dSSV = (gamma-1)mc^2/V,
     not because geometry delivers gamma. This is consistent with SR-1
     App. H.1 (Hyperspherical Cap Elimination Theorem), which proves no purely
     geometric displacement model yields the required v^2/c^2 scaling.

Verdict: geometry fixes the FUNCTIONAL FORM 1/(1+eps) and supplies the
elimination theorem. It does not fix k's number. The abstract's "first-
principles derivation of ... k ~ 2.16e-114 m^3/J from 600-cell packing
geometry" is not supportable under any prefactor choice.

Dependencies: NONE. Python 3 standard library only (math, itertools).
This is deliberate. A verification artifact that requires an uninstalled package
is a verification artifact that does not verify -- the same failure class this
patch retracts. Runs anywhere `python3` runs.

Author: Opus (Anthropic), for Thomas Lee Abshier / Hyperphysics Institute.
"""

import itertools
import math

PHI = (1.0 + math.sqrt(5.0)) / 2.0

# CODATA-2018 style Planck values (match SR-1's quoted figures)
HBAR = 1.054571817e-34
C_LIGHT = 2.99792458e8
G_NEWTON = 6.67430e-11
L_P = math.sqrt(HBAR * G_NEWTON / C_LIGHT**3)
E_P = math.sqrt(HBAR * C_LIGHT**5 / G_NEWTON)

OK, BAD = "PASS", "FAIL"
results = {}


def check(tag, got, want, tol=1e-9):
    good = abs(got - want) <= tol * max(1.0, abs(want))
    results[tag] = good
    print(f"  [{OK if good else BAD}] {tag:44s} got={got:.12g}  want={want:.12g}")
    return good


# --------------------------------------------------------------------------
# C1. The 120 vertices of the 600-cell = binary icosahedral group 2I
# --------------------------------------------------------------------------
def vertices_600cell():
    V = set()

    def add(v):
        V.add(tuple(round(x, 12) + 0.0 for x in v))

    # 8 : (+-1,0,0,0) and permutations
    for i in range(4):
        for s in (1.0, -1.0):
            v = [0.0] * 4
            v[i] = s
            add(v)

    # 16 : (+-1/2, +-1/2, +-1/2, +-1/2)
    for s in itertools.product((0.5, -0.5), repeat=4):
        add(s)

    # 96 : EVEN permutations of (+-phi/2, +-1/2, +-1/(2phi), 0)
    base = [PHI / 2.0, 0.5, 1.0 / (2.0 * PHI), 0.0]
    even = [p for p in itertools.permutations(range(4))
            if _parity(p) == 0]
    for p in even:
        vals = [base[p[0]], base[p[1]], base[p[2]], base[p[3]]]
        nz = [i for i in range(4) if abs(vals[i]) > 1e-15]
        for signs in itertools.product((1.0, -1.0), repeat=len(nz)):
            v = list(vals)
            for i, s in zip(nz, signs):
                v[i] = abs(v[i]) * s
            add(v)
    return sorted(V)


def _parity(p):
    p = list(p)
    par = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                par ^= 1
    return par


print("=" * 74)
print("C1  600-cell vertex set from the binary icosahedral group 2I")
print("=" * 74)
def _norm(v):
    return math.sqrt(sum(x * x for x in v))


def _dist(u, v):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))


P = vertices_600cell()
check("vertex count = 120", float(len(P)), 120.0, 0.0)
check("all unit quaternions (max |norm-1|)",
      max(abs(_norm(v) - 1.0) for v in P), 0.0, 1e-12)

# full pairwise distance table (120 x 120 = 7140 unique pairs; trivial in stdlib)
D = [[_dist(P[i], P[j]) if i != j else float("inf") for j in range(len(P))]
     for i in range(len(P))]
edge = min(min(row) for row in D)
check("edge length a = 1/phi", edge, 1.0 / PHI, 1e-10)
check("circumradius/edge = phi", 1.0 / edge, PHI, 1e-10)

coord = [sum(1 for d in row if abs(d - edge) < 1e-9) for row in D]
check("coordination z = 12", float(coord[0]), 12.0, 0.0)
print(f"        (coordination is uniform across all vertices: {set(coord) == {12}})")

# --------------------------------------------------------------------------
# C2. V_0
# --------------------------------------------------------------------------
print()
print("=" * 74)
print("C2  V_0 from H_4 cell-transitivity (600 congruent regular tetrahedra)")
print("=" * 74)
V0_formula = 600.0 * math.sqrt(2.0) / (12.0 * PHI**3)
V0_direct = 600.0 * (edge**3 * math.sqrt(2.0) / 12.0)
check("V_0 = 600*sqrt2/(12 phi^3)", V0_formula, 16.692527, 1e-6)
check("V_0 direct from measured edge", V0_direct, V0_formula, 1e-9)

# --------------------------------------------------------------------------
# C3 / C4. alpha_geom and its UNIT DEPENDENCE
# --------------------------------------------------------------------------
print()
print("=" * 74)
print("C3/C4  alpha_geom = 3*Abar/V_0  --  and why it is not a pure number")
print("=" * 74)

rho_face = PHI / math.sqrt(2.0)                       # 120-cell face circumradius (R=1)
Abar = (5.0 / 2.0) * rho_face**2 * math.sin(2.0 * math.pi / 5.0)
alpha_circ = 3.0 * Abar / V0_formula                  # sum_i <(n.r)^2> = 12*(1/4) = 3
alpha_closed = 3.0 * (11.0 + 5.0 * math.sqrt(5.0)) * math.sqrt(5.0 + math.sqrt(5.0)) / 320.0
check("alpha_geom (integral) == closed form", alpha_circ, alpha_closed, 1e-12)
check("alpha_geom ~ 0.5594 (per circumradius)", alpha_circ, 0.559359, 1e-5)

# Rescale to insphere units: r_in = a/sqrt2 = 1/(phi*sqrt2); set r_in = 1.
s = PHI * math.sqrt(2.0)                              # 1 / r_in
alpha_insphere = 3.0 * (Abar * s**2) / (V0_formula * s**3)
check("alpha rescales as 1/L  (=> NOT dimensionless)",
      alpha_insphere, alpha_circ / s, 1e-12)
print(f"        alpha  per circumradius R      = {alpha_circ:.6f}")
print(f"        alpha  per insphere r_in = l_P = {alpha_insphere:.6f}   <-- physical unit")
print(f"        ratio  = 1/(phi*sqrt2)         = {1.0/s:.6f}")
print("        => 'exact algebraic constant' holds ONLY in unit-circumradius coords.")

# --------------------------------------------------------------------------
# C5 / C6. The cancellation, and Lorentz recovery under every convention
# --------------------------------------------------------------------------
print()
print("=" * 74)
print("C5/C6  alpha cancels in k*dSSV  =>  k's value is a CONVENTION")
print("=" * 74)

conventions = {
    "paper      alpha = 1": 1.0,
    "March fix  alpha = 0.5594 (per R)": alpha_circ,
    "Planck-nrm alpha = 0.2444 (per l_P)": alpha_insphere,
}
print(f"  {'convention':38s} {'k [m^3/J]':>14s}   {'SSV_crit [J/m^3]':>18s}  k*SSV_crit")
for name, al in conventions.items():
    k = al * L_P**3 / E_P
    ssv_crit = E_P / (al * L_P**3)
    print(f"  {name:38s} {k:14.5e}   {ssv_crit:18.5e}  {k*ssv_crit:.10f}")
    check(f"k*SSV_crit == 1  [{name.split()[0]}]", k * ssv_crit, 1.0, 1e-12)

print()
print("  Lorentz recovery, each convention using ITS OWN matched dSSV:")
print(f"  {'v/c':>7s} {'gamma_SR':>11s}" + "".join(f"{n.split()[0]:>13s}" for n in conventions))
for v in (0.01, 0.1, 0.5, 0.9, 0.99, 0.999):
    g = 1.0 / math.sqrt(1.0 - v * v)
    row = f"  {v:7.3f} {g:11.6f}"
    for name, al in conventions.items():
        k = al * L_P**3 / E_P
        dssv = (g - 1.0) * E_P / (al * L_P**3)     # matched pair
        row += f"{1.0 + k*dssv:13.6f}"
        check(f"gamma exact v={v} [{name.split()[0]}]", 1.0 + k * dssv, g, 1e-12)
    print(row)
print("  => identical to machine precision. The prefactor is unobservable.")

print()
print("  MISMATCHED pair (k from one convention, dSSV from another) -- the live hazard:")
print(f"  {'v/c':>7s} {'gamma_SR':>11s} {'gamma_mixed':>13s} {'(g_mix-1)/(g_SR-1)':>20s}")
for v in (0.1, 0.5, 0.9):
    g = 1.0 / math.sqrt(1.0 - v * v)
    k_march = alpha_circ * L_P**3 / E_P            # March k ...
    dssv_paper = (g - 1.0) * E_P / L_P**3          # ... with paper's dSSV
    gm = 1.0 + k_march * dssv_paper
    print(f"  {v:7.3f} {g:11.6f} {gm:13.6f} {(gm-1.0)/(g-1.0):20.6f}")
print(f"  => ratio is exactly alpha ({alpha_circ:.4f}); a {100*(1-alpha_circ):.0f}% error in gamma-1.")
print("  => (k, dSSV) MUST be inherited as a matched pair. This is the SF-6/DM risk.")

# --------------------------------------------------------------------------
# Summary
# --------------------------------------------------------------------------
print()
print("=" * 74)
n_pass = sum(results.values())
print(f"SUMMARY: {n_pass}/{len(results)} checks passed")
print("=" * 74)
print("""
DERIVED by the 600-cell geometry (real, and CPP's own):
  * a = 1/phi, z = 12, V_0            -- reproduced above from 2I
  * the functional form 1/(1+eps)     -- Hooke + saturation, unique lowest
                                         -order rational approximant
  * App. H.1 elimination theorem      -- no purely geometric displacement
                                         model gives the v^2/c^2 scaling

NOT derived:
  * k's numerical value               -- a normalisation convention tied to
                                         the dSSV definition; alpha cancels
  * gamma                             -- supplied by the energy-momentum
                                         bridge (App. A.8.1) by identification

The paper's Step 3 ("dimensional analysis forces prefactor identically 1") is
invalid: dimensional analysis fixes dimensions, never a dimensionless
prefactor. But the March-2026 remedy (adopt alpha_geom = 0.5594) fails too, on
C4 -- that number is unit-dependent, and its own script printed the finding
("WAIT -- this means 3*Abar/V_0 is NOT dimensionless!") before proceeding
anyway. Neither prefactor is derivable, because by C5 the prefactor is not
physical at all.
""")

if n_pass != len(results):
    raise SystemExit(1)
