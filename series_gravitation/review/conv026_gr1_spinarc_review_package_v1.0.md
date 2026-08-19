You are one of five independent reviewers (ChatGPT, Grok, Copilot, Gemini,
DeepSeek) on the Conscious Point Physics (CPP) review panel. CPP is a
theoretical-physics programme deriving Standard-Model structure from a
600-cell lattice substrate.
IDENTITY (mandatory): in the §8 REVIEWER field put YOUR OWN actual model name;
do NOT adopt or echo another reviewer's name. If unsure, name your
provider/family.
INDEPENDENCE (mandatory; a prior round produced a verbatim-duplicate return):
produce YOUR OWN independent analysis; do not reproduce, summarize, or vote
with any other reviewer's return.
Please review CONV-026 — a bundled round on two packages: (A) GR-1 V0, the
new series parent for the CPP gravitational arc, and (B) the completed
three-paper spin sub-arc, centered on Spin III V0.2 (lattice selection +
protection). Everything you need is inline below (context, claim chains,
triage, all four verify scripts in full, frozen questions, response format).
Find YOUR reviewer-specific steer in §6 ("read your own row"). If you can run
the §7 code, please do and report SCRIPT-EXECUTED with pasted output digits.
Label every claim with its verification tier — INSPECTED / INDEPENDENTLY
RECOMPUTED / SCRIPT-EXECUTED (PD-002) — and respond in the §8 format.

File (provenance only — likely unreachable for external reviewers; the inline
content below is authoritative):
  blob: https://github.com/Hyperphysics-Institute/CPP/blob/main/series_gravitation/review/conv026_gr1_spinarc_review_package_v1.0.md
  raw:  https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_gravitation/review/conv026_gr1_spinarc_review_package_v1.0.md

---

# CONV-026 Review Package v1.0 — GR-1 V0 + the Spin Arc (bundled round)

**Dispatched:** 19 Aug 2026, Session 149, Patch 3240. Founder-initiated
("Please send both papers; initiate the review protocol").
**Bundling rationale (review-economy protocol):** two WIN-class packages, one
block, one paste per seat.
**Responses land in:** `series_gravitation/review/reviews-CONV-026.md`.

## §0 What this round adjudicates

Two packages, eight frozen questions (§5), frozen vocabulary, majority
binding per question. Q4 and Q8 govern status moves; a verdict-flipping
defect sustained by majority on Q1 or Q5 blocks the corresponding status
move until a restate. A "verdict-flipper" is a named defect that, if
sustained, changes a package's central claim — not a wording preference.

- **Package A:** GR-1 V0 (Patch 3228, bumped V0.1 at 3230) —
  `series_gravitation/papers/GR-1_local_gravitation_from_SSV_shell_broadcast.tex`.
- **Package B:** the spin sub-arc — Spin I, Spin II (March 2026, shipped),
  and Spin III V0.2 (Patches 3234/3236/3238) —
  `series_quantum_mechanics/spin_papers/`.

## §1 Context (cold-start)

CPP models physical space as a lattice of Grid Points with 600-cell geometry
(each vertex has 12 icosahedrally-arranged nearest neighbors — the vertex
figure is an icosahedron). Matter and fields are patterns of Dipole
Particles (DPs) in a "Dipole Sea"; stress is carried by the Space Stress
Vector (SSV); the substrate's constitutive response is the Planck Sphere
Radius formula PSR_eff = l_P/(1 + k·Δ|SSV|). Electrons exhibit
Zitterbewegung (ZBW): a polarization cloud with a thermal boundary at
r_th = ħ/(2 m_e c).

**Package A history:** eight gravitational companion papers (~5,600 lines)
sat filed beneath the special-relativity paper SR-1 with no parent. A
scoping assessment (Patch 3225) found the arc ~75% synthesis. Founder
rulings fixed the writing discipline; GR-1 V0 was assembled at Patch 3228;
the companions were moved and re-identified GR-1a–GR-1h at Patch 3230.

**Package B history:** the spin arc was planned as three papers. Spin I and
Spin II shipped in March 2026. Spin III was never written (full-history
finding): only its materials existed. It was drafted at Patch 3234, its
lattice measurement executed at 3236 (after a founder domain ruling), and
its symmetry theorems added at 3238.

## §2 Package A — GR-1 V0: claims

**Thesis (made once, at series level):** one nonlinear substrate response —
the PSR formula — generates Coulomb's law, Newtonian gravity, weak-field GR,
and the exact Schwarzschild metric as successive regimes (Taylor
truncations of one response), extended by the companions to Kerr,
Kerr–Newman, GW echoes, modified Hawking evaporation, and superradiance.

**Claim discipline (founder-ruled, the round's Q1):** GR-1 claims exact
reproduction of the named SOLUTIONS — Schwarzschild *in isotropic
coordinates*, Kerr, Kerr–Newman — and explicitly does NOT claim derivation
of the general field equations. c07/c08's "≡ Einstein field equations in
the continuum limit" and "plays the role of" are recorded in the paper as
correspondence claims; the general derivation (with Birkhoff uniqueness and
the CPP energy-momentum tensor folded in) is registered as OPEN-GR-FE-1.

**The exact static solution (established in companion GR-1c, formerly c08;
restated in GR-1 as a Claim, not re-proved):** with ϱ = GM/(2c²r_iso), the
shell-broadcast source relation k·Δ|SSV| = GM/rc² and the PSR response
yield

    ds² = −[(1−ϱ)/(1+ϱ)]² c²dt² + (1+ϱ)⁴ (dr_iso² + r_iso² dΩ²)

— exactly the isotropic Schwarzschild metric, no free parameters; standard
form under r = r_iso(1+ϱ)². The CP Exclusion Rule (PSR_eff ≥ l_P/2)
replaces the point singularity with a Planck-density core at r_S/2.

**Classical tests (results-only Table 1; derivations deferred to ONE tests
companion, OPEN-GR-TESTS-1, per founder ruling):** since the metric is
exactly Schwarzschild, predictions are GR-identical BY CONSTRUCTION — the
paper states affirmatively that the tests discriminate CPP from Newton, not
from GR. Table values (all verified in the §7.1 script): Mercury perihelion
42.99″/cy (obs 42.98±0.04); solar-limb deflection 1.75″; Shapiro ~233 μs
(Earth–Venus grazing, leading log); redshift gh/c² = 2.46e-15 (22.5 m) and
GPS net +38.5 μs/day. Verify highlights: the isotropic form transforms to
standard Schwarzschild g_tt at 3.3e-16 max relative mismatch; perihelion and
deflection computed BOTH in closed form and by independent numeric
Binet-equation geodesic integration (agreement 4 decimals / 0.006%).

**Epistemic ledger + SR-1 inheritance (the round's Q2):** the paper
aggregates exact / correspondence / conditional claims and states in full
what it inherits from SR-1 — the PSR constitutive form as a minimal ansatz
within the rational class (NOT unique to the 600-cell); k as a
normalization convention, not a derived quantity; the strain–kinematics
grounding at W2 viability strength with OPEN-SR-10 caveats verbatim — and
what SR-1 withdrew: the v19 prediction set (Patch 2474) and the
class-coverage theorem (Patch 2475: f^{1/2} published, f^{5/2} correct,
refuted by its own Model 3). Net statement in the paper: "the gravitational
arc's exactness claims are conditional on the PSR constitutive form, whose
SR-1 grounding is at W2 viability strength."

**Scope boundary:** LOCAL gravitation only; zero FRW content; cosmology
owned by OPEN-EU-1 and the dark-energy lane, declared in the abstract.

## §3 Package B — the spin arc: claims

**Spin I (shipped):** an unpaired −eCP moving through the Dipole Sea
captures a DP: inner +CP at r_in, outer −CP at r_out = 2r_in. Coulomb
force balance gives ω_in/ω_out = 2√2 exactly; total orbital angular
momentum L = m_e ω_out r_in² (2√2+4) = ħ/2 exactly when
r_in = a₀/[4(1+√2)²].

**Spin II (shipped):** derives r_out = 2r_in. The ZBW cloud is an
open–closed radial resonator on u = r·ψ: node at r = 0 (CP Exclusion),
free end u′ = 0 at r_th. Modes k_n = (2n−1)π/2r_th. Mode 2's interior
antinode is at r_th/3, interior node at 2r_th/3 — ratio exactly 2,
independent of every physical constant. Mode 2 is the minimum-energy mode
with both anchoring features.

**Spin III V0.2 (this round's centerpiece):**

*(a) Consolidation:* FD verification of the spectrum by TWO independent
discretization routes (<0.05%; the March CSV regenerated bit-identically);
the scale bridge UPGRADED from numerical observation to exact identity:
r_in(Spin I)/r_in(Spin II) = 6/[4α(1+√2)²] = 35.2675 given a₀ = r_C/α,
r_th = r_C/2 (verified 1e-12); discreteness bound (l_P/r_th)² ≈ 7e-45 ⇒
the lattice owes mode SELECTION, not corrections.

*(b) Honest diagnosis of the March instrument:* the committed 24-cell
graph-Laplacian computation solved the CLOSED (Neumann) problem — the
CP-Exclusion node was never encoded — so its low spectrum is the four 4D
dipole modes and its own Mode-2 diagnostic found nothing (made reproducible
as a verify check). A SECOND semantic trap was found in designing the fix:
ψ-Neumann is NOT Spin II's u-Neumann (on a sphere it gives tan(kR)=kR,
k₁R≈4.493, not (2n−1)π/2). The corrected instrument discretizes the
u-equation directly: −u″ − r⁻²Δ_S u = k²u.

*(c) The measurement (Patch 3236; founder ruling A1: the 24-cell carried no
physical-picture weight; the true Voronoi cell of the 600-cell lattice is
the regular dodecahedron — 600-cell dual = 120-cell):* sphere control EXACT
(k₁R = 1.57079 vs π/2 = 1.57080; Mode-2 zero 0.66667; antinode 0.3333).
True cell at two densities (162×80, 642×120): three radial candidates
(isotropy scores 0.999–1.000); Mode-2 k⟨R⟩ = 4.6976 (−0.31% from sphere);
node 0.6670 vs exact 2/3; antinode 0.3333; Mode-3 double zero (0.402,
0.801). FROZEN VERDICT (declared at Patch 3234, BEFORE the domain ruling
existed): **MODE2-RECOVERED** at both densities, node drift 0.0000 vs the
0.02 gate. Declared instrument approximations (anisotropy² class):
shell-averaged angular metric weight; ray-coordinate cross-terms neglected.

*(d) The theorems (Patch 3238):*
- **LEMMA (exact character arithmetic):** the trivial-irrep multiplicity of
  the icosahedral rotation group I in spin-l is m_l = 0 for l = 1..5;
  m_6 = m_10 = m_12 = 1 (m_15 = 1 for I, parity-excluded in I_h). Realized
  in the actual cell: support-function projection gives ε_6 = 0.0510,
  ε_10 = 0.0113, ε_12 = 0.0120, forbidden channels ≤ 5e-6 (quadrature
  floor).
- **SELECTION THEOREM:** within the trivial irrep (the ZBW cloud's scalar
  breathing sector — an identification inherited from Spin II, whose
  equation was radial from the start; the round's Q7), the first
  anisotropy-carrying channel is l = 6 with lowest eigenvalue
  k(6,1)R = 8.211 > 3π/2 = 4.712 (74% margin) ⇒ the second invariant mode
  of the true cell IS the anchoring mode. Interloper accounting: globally,
  exactly l=1 (k = 2.744, 3 states) + l=2 (k = 3.870, 5 states) = 8
  non-invariant modes sit between the radial modes — precisely why the
  3236 run found its radial modes at global indices 1 and 10. Symmetry
  removes the interlopers from the SECTOR, not the spectrum.
- **PROTECTION THEOREM:** for a radial mode, the first-order Hadamard
  boundary shift integrates an angularly constant density against δR ⇒
  only the l=0 mean (pure scale) couples; the first-order eigenfunction
  correction is pure l≥6 and angular-averages to zero ⇒ fractional
  node/antinode positions shift only at O(ε₆²). Predicted ε₆² = 0.0026;
  measured (3236) mean-normalized eigenvalue residual 0.0031 (20%
  agreement), node shift 0.0005. STATED AS CONSISTENCY, NOT DECOMPOSITION
  (the instrument's own declared approximation enters at the same order).
  Neither leg knew the other's number when its own was fixed.

**Status claimed:** OPEN-QM-8 SUBSTANTIALLY RESOLVED; registered residual
(rigor upgrade only): a fully non-perturbative-in-ε₆ bound. Not claimed:
symmetry choosing the boundary conditions (inherited premises: CP Exclusion
node; thermal free end from the ZBW Mass companion).

## §4 Triage — the hardest questions (press these)

A-1. GR-1's abstract says "exact ... with no free parameters" while its own
§7 says the exactness is conditional on a constitutive form at W2 viability
strength. Is the conditioning stated prominently enough, or does the
abstract outrun the ledger?
A-2. The classical-tests table exists in GR-1 while the derivations
companion (OPEN-GR-TESTS-1) does not yet exist. Is a results-only table
backed by a verify script (closed forms + independent geodesic integration)
adequate for a V0, or does it presuppose the companion?
A-3. The GR-1c keystone claim (exact isotropic Schwarzschild) is restated
as a Claim, not re-proved, in GR-1. Is the parent's reliance on the
companion's Theorem appropriately labeled?
B-1. Is "the ZBW cloud's scalar breathing sector = the trivial irrep of
I_h" (Q7) an inherited identification or a new physical assumption smuggled
into the Selection Theorem?
B-2. The Protection Theorem's quantitative closure: is 0.0026-vs-0.0031 at
20% honest "consistency," or does the same-order instrument approximation
make the comparison uninformative?
B-3. The Selection Theorem's gap uses the SPHERICAL l=6 eigenvalue as the
invariant-channel reference on a non-spherical cell. Does the 74% margin +
the non-perturbative 3236 measurement adequately cover the gap between
"perturbative theorem" and "the lattice must choose Mode 2"?
B-4. "SUBSTANTIALLY RESOLVED" for OPEN-QM-8 with a registered
non-perturbative residual: right status, premature, or underclaimed?

## §5 Frozen questions and vocabulary (answer ALL eight)

- **Q1 (A, claim discipline):** DISCIPLINED / OVERCLAIMS(quote the passage)
  / UNDERCLAIMS(quote the passage).
- **Q2 (A, inheritance + ledger):** COMPLETE / GAP-NAMED(state the missing
  item verbatim).
- **Q3 (A, classical tests + §7.1 verify):** SOUND / DEFECT-NAMED.
- **Q4 (A, verdict):** SHIP-PATH-CLEAR(list required calibrations, if any)
  / RESTATE-REQUIRED(name the verdict-flipper) / STRUCTURAL-REWORK.
- **Q5 (B, Lemma + Selection Theorem):** VALID / DEFECT-NAMED. Recompute
  the character table and the l=6 gap if you can; label the tier.
- **Q6 (B, Protection + 20% closure):** CALIBRATED / OVERREAD / UNDERREAD.
- **Q7 (B, trivial-irrep identification):** JUSTIFIED-AS-INHERITED /
  NEEDS-INDEPENDENT-GROUNDING(name what would ground it).
- **Q8 (B, OPEN-QM-8 status):** RATIFY(SUBSTANTIALLY-RESOLVED stands) /
  DEMOTE(name the status) / UPGRADE(name the status).

**Binding rules:** majority per question; Q4 governs Package A's status
move, Q8 governs Package B's; a majority-sustained verdict-flipper on Q1
blocks Q4's move, and on Q5 blocks Q8's, until a restate round. Minority
specifications are preserved verbatim in the adjudication. Convergence
counts are taken from abstracts per founder ruling; panel attribution is to
"the AI review panel."

## §6 Reviewer steers — read your own row

- **ChatGPT:** hostile pass on the triage items A-1, B-1, B-2; press
  overclaim/deflation on both abstracts; verdict-honesty on Q4/Q8.
  *Disambiguation rider:* this is the CPP gravitation + spin bundled round
  CONV-026; it is NOT a nuclear-physics OPEN-SS audit, NOT a dark-matter
  Route-C item, NOT a request to reconstruct from memory — engage the
  inline content directly.
- **Grok:** independent recompute. Run §7.3 and §7.4 (SCRIPT-EXECUTED;
  paste output digits); recompute the character table m_l by hand from the
  five-class formula; recompute 6/[4α(1+√2)²]; check the l=6 gap by any
  independent route; check the GR-1 isotropic↔standard transformation
  algebraically.
- **Copilot:** structural consistency per question; referee-grade framing;
  the load-bearing chain GR-1c → GR-1 Table 1, and Spin II → Selection
  Theorem premise flow; check §5's binding rules are decidable as written.
- **Gemini:** breadth/confirmatory pass across both packages; note — per
  standing panel practice, your SCRIPT-EXECUTED claims are treated as
  RESTATE-tier unless you paste actual run output.
- **DeepSeek:** strictest-statistics seat. Press B-2 (is 20% agreement at
  one point a "closure"?), the 3236 two-density stability gate, and whether
  any Q5/Q6 claim exceeds its evidence tier; propose stricter wording where
  warranted (your CONV-021 stricter-test precedent is why you have this
  seat).

## §7 Verify code — IN FULL (run any; report SCRIPT-EXECUTED with digits)

All four scripts are self-contained (numpy/scipy/matplotlib only). Key
fingerprint values are printed at precisions not quoted in the prose
(OPEN-ORG-022 discipline).


### §7.1 Package A — classical tests (Patch 3228)
```python
#!/usr/bin/env python3
"""Patch 3228 verify script — GR-1 V0 classical-tests summary table.

Purpose. c08 (strong-field companion) claims the CPP shell-broadcast PSR
mechanism yields EXACTLY the Schwarzschild metric in isotropic coordinates.
GR-1 V0 therefore claims the four classical tests at exactly the GR values:
the tests discriminate CPP from Newtonian gravity, not from GR. This script
(1) verifies the isotropic form used in c08 is the Schwarzschild metric
    (coordinate-transformation identity, machine precision),
(2) computes the classical-test numbers that populate GR-1 Table 1, the two
    dynamical ones by numeric geodesic integration cross-checked against the
    closed form, so every number in the table traces to this script.

No free parameters; no CPP-specific inputs beyond "the metric is exactly
Schwarzschild" — which is precisely the claim being surfaced.

Numerical notes (learned on first run, kept for the record):
- phi is accumulated as i*dphi (integer step count), not phi += dphi; naive
  accumulation over ~10^7 steps injects ~1e-6 rad of rounding drift, which is
  percent-level against a per-orbit advance of 5e-7 rad.
- Zero crossings (perihelion passages, outgoing photon asymptote) are located
  by linear interpolation; taking the first post-crossing grid point overshoots
  by up to dphi, which is 10%-level against a deflection of 8.5e-6 rad.

Run: python3 3228_classical_tests_verify.py
"""

import math

# ---------------------------------------------------------------- constants
G       = 6.67430e-11        # m^3 kg^-1 s^-2 (CODATA 2018)
c       = 2.99792458e8       # m/s (exact)
M_sun   = 1.98892e30         # kg
R_sun   = 6.957e8            # m (IAU nominal solar radius)
AU      = 1.495978707e11     # m (exact)
g_earth = 9.80665            # m/s^2 (standard)

GM = G * M_sun
rs = 2 * GM / c**2           # Schwarzschild radius of the Sun

ARCSEC = math.pi / (180 * 3600)
JULIAN_CENTURY_DAYS = 36525.0

passes = []
def check(name, ok, detail=""):
    passes.append((name, ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")

# ---------------------------------------------------- 0. metric identity
print("== 0. Isotropic form (c08 Eq. isotropic_schw) IS Schwarzschild ==")
# c08: with varrho = GM/(2 c^2 r_iso),
#   g_tt = -[(1-varrho)/(1+varrho)]^2 ; standard r = r_iso (1+varrho)^2,
#   g_tt = -(1 - rs/r).
worst = 0.0
for r_iso in [1e9, 1e10, 1e11, AU, 10 * AU]:
    vr = GM / (2 * c**2 * r_iso)
    gtt_iso = -((1 - vr) / (1 + vr))**2
    r_std = r_iso * (1 + vr)**2
    gtt_std = -(1 - rs / r_std)
    worst = max(worst, abs(gtt_iso - gtt_std) / abs(gtt_std))
print(f"  max relative g_tt mismatch over 5 radii: {worst:.3e}")
check("isotropic == standard Schwarzschild g_tt (machine precision)",
      worst < 1e-14, f"max rel {worst:.1e}")

# ------------------------------------------- 1. Mercury perihelion advance
print("\n== 1. Perihelion precession of Mercury ==")
a_merc = 5.7909050e10        # m
e_merc = 0.205630
P_merc_days = 87.9691

dphi_cf = 6 * math.pi * GM / (a_merc * (1 - e_merc**2) * c**2)  # per orbit

# Independent route: relativistic Binet equation
#   u'' + u = GM/h^2 + (3GM/c^2) u^2
L = a_merc * (1 - e_merc**2)
h2 = GM * L
u = (1 + e_merc) / L         # start at perihelion (u max, u'=0)
up = 0.0
dphi = 2e-5
n_orbits = 30
n_steps = int(2 * math.pi * (n_orbits + 0.5) / dphi)

def deriv_m(u_, up_):
    return up_, GM / h2 - u_ + (3 * GM / c**2) * u_ * u_

crossings = []               # up sign change - -> + (interpolated)
last_up = up
for i in range(1, n_steps + 1):
    k1u, k1p = deriv_m(u, up)
    k2u, k2p = deriv_m(u + 0.5 * dphi * k1u, up + 0.5 * dphi * k1p)
    k3u, k3p = deriv_m(u + 0.5 * dphi * k2u, up + 0.5 * dphi * k2p)
    k4u, k4p = deriv_m(u + dphi * k3u, up + dphi * k3p)
    u  += dphi / 6 * (k1u + 2 * k2u + 2 * k3u + k4u)
    up += dphi / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
    if last_up < 0.0 and up >= 0.0:
        frac = last_up / (last_up - up)      # in [0,1]
        crossings.append((i - 1 + frac) * dphi)
    last_up = up

# Telescoping estimator: interior interpolation errors cancel.
N = len(crossings) - 1
dphi_num = (crossings[-1] - crossings[0]) / N - 2 * math.pi

orbits_per_century = JULIAN_CENTURY_DAYS / P_merc_days
adv_cf  = dphi_cf  / ARCSEC * orbits_per_century
adv_num = dphi_num / ARCSEC * orbits_per_century
print(f"  closed form : {adv_cf:.4f} arcsec/century")
print(f"  numeric     : {adv_num:.4f} arcsec/century ({N} orbit intervals)")
check("perihelion numeric vs closed form (0.1%)",
      abs(adv_num - adv_cf) <= 1e-3 * adv_cf,
      f"{adv_num:.4f} vs {adv_cf:.4f}")
check("perihelion vs observed 42.98 +/- 0.04 \"/cy",
      abs(adv_cf - 42.98) <= 0.04, f"{adv_cf:.4f}")

# ------------------------------------------------- 2. Light deflection
print("\n== 2. Light deflection at the solar limb ==")
b = R_sun
defl_cf = 4 * GM / (c**2 * b)

# Photon Binet: u'' + u = (3GM/c^2) u^2, ICs u(0)=0, u'(0)=1/b
u, up = 0.0, 1.0 / b
dphi = 1e-6
u_prev = u
i = 0
def deriv_p(u_, up_):
    return up_, -u_ + (3 * GM / c**2) * u_ * u_
while True:
    i += 1
    k1u, k1p = deriv_p(u, up)
    k2u, k2p = deriv_p(u + 0.5 * dphi * k1u, up + 0.5 * dphi * k1p)
    k3u, k3p = deriv_p(u + 0.5 * dphi * k2u, up + 0.5 * dphi * k2p)
    k4u, k4p = deriv_p(u + dphi * k3u, up + dphi * k3p)
    u_prev = u
    u  += dphi / 6 * (k1u + 2 * k2u + 2 * k3u + k4u)
    up += dphi / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
    if i > 10 and u <= 0.0:
        frac = u_prev / (u_prev - u)
        phi_end = (i - 1 + frac) * dphi
        break
defl_num = phi_end - math.pi
print(f"  closed form : {defl_cf / ARCSEC:.4f} arcsec")
print(f"  numeric     : {defl_num / ARCSEC:.4f} arcsec")
check("deflection numeric vs closed form (0.2%)",
      abs(defl_num - defl_cf) <= 2e-3 * defl_cf,
      f"{defl_num/ARCSEC:.4f} vs {defl_cf/ARCSEC:.4f}")
check("deflection vs 1.75 arcsec (0.5%)",
      abs(defl_cf / ARCSEC - 1.75) <= 0.005 * 1.75,
      f"{defl_cf/ARCSEC:.4f}")

# ------------------------------------------------- 3. Shapiro delay
print("\n== 3. Shapiro delay (Earth-Venus superior conjunction, grazing) ==")
r_venus = 1.0821e11
delay = (4 * GM / c**3) * math.log(4 * AU * r_venus / R_sun**2)
print(f"  round-trip excess delay: {delay * 1e6:.1f} microseconds")
check("Shapiro delay in the ~200 us class (leading log)",
      200e-6 <= delay <= 260e-6, f"{delay*1e6:.1f} us")

# ------------------------------------------------- 4. Gravitational redshift
print("\n== 4. Gravitational redshift ==")
h_tower = 22.5               # m, Pound-Rebka-Snider
z_pr = g_earth * h_tower / c**2
print(f"  Pound-Rebka 22.5 m tower: dnu/nu = {z_pr:.3e}")
check("Pound-Rebka dnu/nu ~ 2.46e-15", abs(z_pr - 2.46e-15) <= 0.02 * 2.46e-15,
      f"{z_pr:.3e}")
R_e = 6.371e6
GM_e = 3.986004418e14
r_gps = R_e + 2.0200e7
grav = (GM_e / c**2) * (1 / R_e - 1 / r_gps) * 86400 * 1e6    # us/day
v_gps = math.sqrt(GM_e / r_gps)
sr = -0.5 * (v_gps / c)**2 * 86400 * 1e6                       # us/day
print(f"  GPS: grav +{grav:.1f} us/day, SR {sr:.1f} us/day, net {grav+sr:.1f} us/day")
check("GPS net offset ~ 38.5 us/day (3%)",
      abs((grav + sr) - 38.5) <= 0.03 * 38.5, f"{grav+sr:.1f}")

# ---------------------------------------------------------------- verdict
print("\n== SUMMARY ==")
n_ok = sum(1 for _, ok in passes if ok)
for name, ok in passes:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"{n_ok}/{len(passes)} checks pass")
raise SystemExit(0 if n_ok == len(passes) else 1)
```

### §7.2 Package B — Spin III V0 consolidation + March-instrument diagnosis (Patch 3234)
```python
#!/usr/bin/env python3
"""Patch 3234 verify script — Spin III V0.

Four checks, each independent of the committed cpp_spin3_eigenvalues.py
implementation where that is possible:

  1. ANALYTIC + FD REPRODUCTION. Rebuild the open-closed radial FD problem
     from scratch (own matrix construction) and compare eigenvalues against
     the COMMITTED data/spin3_eigenvalues.csv. The committed CSV was also
     regenerated bit-identically from the committed script this session
     (recorded in reasoning/3234.md); this check adds an independent
     construction route.
  2. MODE-2 GEOMETRY. From the independently computed Mode-2 eigenvector:
     interior antinode at R/3, interior node at 2R/3, ratio 2 — the exact
     result the arc rests on.
  3. THE SCALE-BRIDGE IDENTITY. r_in(Spin I)/r_in(Spin II)
     = 6/[4*alpha*(1+sqrt(2))^2] EXACTLY, given a0 = r_C/alpha and
     r_th = r_C/2. Verified as an algebraic identity numerically to 1e-12,
     and against the value 35.267491 quoted in the committed script.
  4. THE PART-3 DIAGNOSIS, MADE REPRODUCIBLE. Rebuild the committed
     24-cell kNN graph Laplacian (same construction, same seed, reduced
     n for runtime) and assert the finding reported in Spin III V0 §5:
     (a) the lowest nontrivial modes form a 4-fold near-degenerate group
         (4D dipole modes of the closed/Neumann-like problem), and
     (b) NO mode among the lowest ten has exactly one interior radial
         sign change under the committed script's own diagnostic —
     i.e. the committed instrument does not (and, solving the closed
     problem, cannot) exhibit the open-closed Mode 2.

Run: python3 3234_verify_spin3_v0.py            (checks 1-3, fast)
     python3 3234_verify_spin3_v0.py --with-p3  (adds check 4, ~1 min)
"""

import argparse
import math
import os
import sys

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "..", "data", "spin3_eigenvalues.csv")

# constants (CODATA, as in the committed script)
HBAR = 1.054571817e-34
C_LT = 2.99792458e8
M_E = 9.1093837015e-31
ALPHA = 7.2973525693e-3
L_P = 1.616255e-35
R_C = HBAR / (M_E * C_LT)
R_TH = R_C / 2.0

passes = []
def check(name, ok, detail=""):
    passes.append((name, ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


# ---------------------------------------------------------------- check 1+2
print("== 1+2. Independent FD reconstruction vs committed CSV; Mode-2 geometry ==")
# Independent construction: the SYMMETRIC lumped-mass Neumann formulation
# (generalized problem M u = k^2 B u with half mass at the Neumann node),
# second-order accurate — a genuinely different route from the committed
# script's plain forward-difference ghost, so agreement is a two-route check.
N = 6000
R = 1.0
h = R / N
main = np.full(N, 2.0) / h**2
off = np.full(N - 1, -1.0) / h**2
main[-1] = 1.0 / h**2                      # stiffness at the free end
M = sp.diags([off, main, off], [-1, 0, 1], format="csr")
bdiag = np.ones(N); bdiag[-1] = 0.5        # lumped half mass at r = R
B = sp.diags(bdiag, format="csr")
vals, vecs = spla.eigsh(M, k=12, M=B, which="SM", tol=1e-14)
order = np.argsort(vals)
k_fd = np.sqrt(np.abs(vals[order]))[:8]
vecs = vecs[:, order]

rows = []
with open(CSV) as f:
    next(f)
    for line in f:
        m, kt, kc, e = line.strip().split(",")
        rows.append((int(m), float(kt), float(kc), float(e)))
k_theory = np.array([r[1] for r in rows])
k_committed = np.array([r[2] for r in rows])

worst_theory = float(np.max(np.abs(k_fd - k_theory) / k_theory))
worst_committed = float(np.max(np.abs(k_fd - k_committed) / k_committed))
check("independent FD vs analytic k_n (<0.02%)", worst_theory < 2e-4,
      f"max rel {worst_theory:.2e}")
check("independent FD vs committed CSV (<0.05%)", worst_committed < 5e-4,
      f"max rel {worst_committed:.2e} (two FD routes, different Neumann ghosts)")

r = np.arange(1, N + 1) * h
psi2 = vecs[:, 1]
# antinode: max |psi| in interior; node: sign change
i_anti = int(np.argmax(np.abs(psi2[: int(0.6 * N)])))
sc = np.where(np.diff(np.sign(psi2)))[0]
r_node = None
for i in sc:
    rr = r[i] + h * abs(psi2[i]) / (abs(psi2[i]) + abs(psi2[i + 1]))
    if 0.1 < rr < 0.95:
        r_node = rr
        break
r_anti = r[i_anti]
check("Mode-2 antinode at R/3", abs(r_anti - 1 / 3) < 2e-3, f"{r_anti:.5f}")
check("Mode-2 node at 2R/3", r_node is not None and abs(r_node - 2 / 3) < 2e-3,
      f"{r_node:.5f}")
ratio = r_node / r_anti
check("r_out/r_in = 2 (exact target)", abs(ratio - 2.0) < 5e-3, f"{ratio:.6f}")

# ---------------------------------------------------------------- check 3
print("\n== 3. Scale-bridge identity ==")
A_BOHR = R_C / ALPHA                      # a0 = r_C / alpha (exact relation)
r_in_I = A_BOHR / (4 * (1 + math.sqrt(2)) ** 2)
r_in_II = R_TH / 3.0
lhs = r_in_I / r_in_II
rhs = 6.0 / (ALPHA * 4 * (1 + math.sqrt(2)) ** 2)
check("r_in(I)/r_in(II) == 6/[4 alpha (1+sqrt2)^2] (1e-12)",
      abs(lhs - rhs) / rhs < 1e-12, f"{lhs:.9f} vs {rhs:.9f}")
check("value matches committed 35.267491", abs(lhs - 35.267491) < 5e-6,
      f"{lhs:.6f}")
corr = (L_P / R_TH) ** 2
check("discreteness bound (l_P/r_th)^2 ~ 7e-45", 6e-45 < corr < 8e-45,
      f"{corr:.3e}")

# ---------------------------------------------------------------- check 4
ap = argparse.ArgumentParser()
ap.add_argument("--with-p3", action="store_true")
args = ap.parse_args()
if args.with_p3:
    print("\n== 4. Part-3 diagnosis (committed instrument, reduced n, same seed) ==")
    # Reproduce the committed construction verbatim in miniature.
    verts = set()
    for i in range(4):
        for j in range(i + 1, 4):
            for si in (1, -1):
                for sj in (1, -1):
                    v = [0, 0, 0, 0]; v[i] = si; v[j] = sj
                    verts.add(tuple(v))
    V = np.array(sorted(verts), dtype=float)
    V /= np.linalg.norm(V[0])
    rng = np.random.default_rng(42)
    n_pts = 6000
    pts = []
    while sum(len(p) for p in pts) < n_pts:
        cands = rng.uniform(-1, 1, size=(n_pts * 8, 4))
        mask = np.max(np.abs(cands @ V.T), axis=1) <= 1.0 + 1e-9
        pts.append(cands[mask])
    pts = np.vstack([np.zeros((1, 4)), np.vstack(pts)[:n_pts]])

    from scipy.spatial import cKDTree
    tree = cKDTree(pts)
    dists, nbrs = tree.query(pts, k=21)
    sigma = np.mean(dists[:, 1]) * 1.5
    n = len(pts)
    rowsI, colsI, w = [], [], []
    for i in range(n):
        for ki in range(1, 21):
            j = nbrs[i, ki]
            rowsI.append(i); colsI.append(j)
            w.append(math.exp(-dists[i, ki] ** 2 / (2 * sigma ** 2)))
    W = sp.csr_matrix((w, (rowsI, colsI)), shape=(n, n))
    W = (W + W.T).multiply(0.5)
    deg = np.array(W.sum(axis=1)).flatten()
    dinv = sp.diags(1.0 / np.sqrt(np.where(deg > 0, deg, 1.0)))
    L = sp.eye(n, format="csr") - dinv @ W @ dinv
    ev, Q = spla.eigsh(L, k=14, which="SM", tol=1e-10)
    m = ev > 1e-8
    ev, Q = np.sort(ev[m])[:10], Q[:, m][:, :10]

    grp = ev[:4]
    spread = (grp.max() - grp.min()) / grp.mean()
    gap = ev[4] / grp.mean()
    check("lowest nontrivial modes: 4-fold near-degenerate dipole group",
          spread < 0.15 and gap > 1.5,
          f"group spread {spread:.2%}, gap ratio {gap:.2f}")

    def radial_profile_zeros(vec):
        rr = np.linalg.norm(pts, axis=1)
        edges = np.linspace(0, rr.max(), 81)
        prof = np.zeros(80); cnt = np.zeros(80)
        bi = np.clip(np.searchsorted(edges, rr) - 1, 0, 79)
        np.add.at(prof, bi, vec); np.add.at(cnt, bi, 1)
        prof[cnt > 0] /= cnt[cnt > 0]
        p = prof[np.abs(prof) > 0.02 * np.max(np.abs(prof))]
        return int(np.sum(np.abs(np.diff(np.sign(p))) > 0))

    zero_counts = [radial_profile_zeros(Q[:, i]) for i in range(10)]
    check("NO mode among lowest 10 with exactly one radial zero "
          "(committed diagnostic)", 1 not in zero_counts,
          f"zero counts {zero_counts}")
else:
    print("\n(check 4 skipped; run with --with-p3)")

# ---------------------------------------------------------------- verdict
print("\n== SUMMARY ==")
n_ok = sum(1 for _, ok in passes if ok)
for name, ok in passes:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"{n_ok}/{len(passes)} checks pass")
sys.exit(0 if n_ok == len(passes) else 1)
```

### §7.3 Package B — the corrected lattice measurement (Patch 3236)
```python
#!/usr/bin/env python3
"""Patch 3236 — OPEN-QM-8 corrected measurement (A1 ruled: true Voronoi cell).

THE PROBLEM SOLVED (the one Spin II actually published):
    The ZBW resonator is stated on the u-field, u = r*psi:
        -u'' - (1/r^2) Delta_S u = k^2 u
    with u = 0 at the center (CP Exclusion) and the FREE end u' = 0 at the
    cell boundary along each ray (Spin II: "antinode at the thermal
    boundary"). On a sphere this is exactly the 1D open-closed string per
    ray: k_n = (2n-1)pi/2R, Mode-2 antinode at R/3, node at 2R/3.

WHY THIS FORMULATION (recorded so the choice is auditable):
    The committed March instrument solved the CLOSED psi-Neumann problem
    (diagnosed in Spin III V0 par.5). But there is a second, subtler
    semantic trap this instrument avoids: a free (Neumann) condition on
    PSI is NOT the same as Spin II's free condition on U — on a sphere,
    psi'(R)=0 gives the tan(kR)=kR spectrum (k1 R = 4.493...), not
    (2n-1)pi/2. The paper's resonator is defined on u, so the instrument
    discretizes the u-equation directly.

DOMAIN (founder ruling A1, 19 Aug 2026): the true Voronoi cell of the
    600-cell-based lattice = the regular dodecahedron (dual-120-cell cell;
    12 pentagonal faces, normals at the 12 icosahedral neighbor
    directions). Sphere control validates the instrument. The 24-cell leg
    is deferred with reason (wrong dimension for the published 3D radial
    problem); see the ruling registration.

DISCRETIZATION:
    Angular: icosphere triangulation of S^2 (subdivided icosahedron),
    cotangent Laplacian L_cot with Voronoi-area lumped mass m_a.
    Radial: per-ray coordinate s in [0,1], r = s*R(omega); 1D FEM
    stiffness with Dirichlet at s=0, natural (free) at s=1.
    Boundary radius: sphere R(omega)=1; dodecahedron
    R(omega) = rho_in / max_f(omega . n_f), n_f = 12 icosahedron vertex
    directions, rho_in = 1 (readings are per-ray fractional, scale-free).
    DECLARED APPROXIMATION (anisotropy^2 class, ~1% positions): the
    angular coupling uses the shell-averaged metric weight
    w_j = <L_a>/rbar_j^2 (exact in the sphere limit); ray-coordinate
    cross-terms neglected. Dodeca anisotropy: R in [1, 1.258].

READINGS (frozen in OPEN-QM-8 / Spin III V0 par.6, applied verbatim):
    Radial candidates: eigenmodes whose isotropy score (mass-weighted
    fraction of variance explained by the angular-mean profile) >= 0.5.
    MODE2-RECOVERED: a radial candidate with exactly one interior zero of
      the mean u-profile, node s in [0.60, 0.73], antinode s in
      [0.28, 0.40], stable across the two mesh densities.
    MODE2-ABSENT: no such candidate among the lowest 20 radial candidates
      at the highest density.
    INDETERMINATE: anything else.
    Worker expectation, declared pre-run: MODE2-RECOVERED.

Run: python3 3236_qm8_true_cell_run.py
"""

import math
import sys

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

PHI = (1 + math.sqrt(5)) / 2


# ---------------------------------------------------------------- icosphere
def icosahedron():
    v = []
    for s1 in (1, -1):
        for s2 in (1, -1):
            v += [(0, s1, s2 * PHI), (s1, s2 * PHI, 0), (s2 * PHI, 0, s1)]
    V = np.unique(np.array(v, float).round(12), axis=0)
    V /= np.linalg.norm(V, axis=1)[:, None]
    # faces via convex hull
    from scipy.spatial import ConvexHull
    F = ConvexHull(V).simplices
    # orient outward
    for i, f in enumerate(F):
        n = np.cross(V[f[1]] - V[f[0]], V[f[2]] - V[f[0]])
        if np.dot(n, V[f].mean(0)) < 0:
            F[i] = f[[0, 2, 1]]
    return V, F


def subdivide(V, F, levels):
    V = list(map(tuple, V))
    index = {v: i for i, v in enumerate(V)}
    F = [tuple(f) for f in F]
    for _ in range(levels):
        newF = []
        cache = {}
        def mid(a, b):
            key = (min(a, b), max(a, b))
            if key in cache:
                return cache[key]
            p = np.array(V[a]) + np.array(V[b])
            p /= np.linalg.norm(p)
            t = tuple(p)
            if t not in index:
                index[t] = len(V); V.append(t)
            cache[key] = index[t]
            return index[t]
        for (a, b, c) in F:
            ab, bc, ca = mid(a, b), mid(b, c), mid(c, a)
            newF += [(a, ab, ca), (ab, b, bc), (ca, bc, c), (ab, bc, ca)]
        F = newF
    return np.array(V), np.array(F)


def cot_laplacian(V, F):
    """Cotangent stiffness (PSD) and lumped Voronoi-area mass on the mesh."""
    n = len(V)
    I, J, W = [], [], []
    mass = np.zeros(n)
    for (a, b, c) in F:
        p, q, r = V[a], V[b], V[c]
        area = 0.5 * np.linalg.norm(np.cross(q - p, r - p))
        for (i, j, k) in ((a, b, c), (b, c, a), (c, a, b)):
            u_, v_ = V[j] - V[k], V[i] - V[k]
            cot = np.dot(u_, v_) / (np.linalg.norm(np.cross(u_, v_)) + 1e-300)
            w = 0.5 * cot
            I += [i, j, i, j]; J += [j, i, i, j]; W += [-w, -w, w, w]
        for vv in (a, b, c):
            mass[vv] += area / 3.0
    K = sp.csr_matrix((W, (I, J)), shape=(n, n))
    K = (K + K.T) * 0.5
    return K, mass


# ------------------------------------------------------------ boundary radii
ICO_V, _ = icosahedron()   # 12 unit vertices = dodeca face normals

def R_sphere(dirs):
    return np.ones(len(dirs))

def R_dodeca(dirs):
    # support-function radius of the dodecahedron with unit inradius
    return 1.0 / np.max(dirs @ ICO_V.T, axis=1)


# ------------------------------------------------------------ assembly
def assemble(V, F, R_of, Nr):
    """K u = k^2 M u for the u-equation on rays s in [0,1], r = s R(omega)."""
    Kang, m_a = cot_laplacian(V, F)
    n_ang = len(V)
    R = R_of(V)                     # per-ray boundary radius
    h = 1.0 / Nr
    s = (np.arange(1, Nr + 1)) * h  # s_1..s_Nr ; Dirichlet at s=0 eliminated

    # 1D FEM stiffness (Dirichlet at 0, natural at 1) and lumped mass on s-grid
    d = np.full(Nr, 2.0); d[-1] = 1.0
    o = np.full(Nr - 1, -1.0)
    K1 = sp.diags([o, d, o], [-1, 0, 1]) / h
    m1 = np.full(Nr, h); m1[-1] = h / 2.0

    # global index: a * Nr + j
    # radial part: sum_a (m_a / R_a) * K1  on ray a   [ (1/R^2) u'' with mass R ]
    Krad = sp.kron(sp.diags(m_a / R), K1, format="csr")
    # mass: M = diag(m_a * R_a) x diag(m1)
    M = sp.kron(sp.diags(m_a * R), sp.diags(m1), format="csr")
    # angular part: shell-averaged weight  w_j = <R> / rbar_j^2 ,
    # rbar_j = s_j * <R>   =>  w_j = 1 / (<R> s_j^2)
    Rmean = float(np.mean(R))
    w = m1 / (Rmean * s ** 2)
    Kang_glob = sp.kron(Kang, sp.diags(w), format="csr")
    K = (Krad + Kang_glob).tocsr()
    K = (K + K.T) * 0.5
    return K, M, m_a, R, s


def radial_family(K, M, m_a, R, s, n_eigs=90, iso_thresh=0.5):
    vals, vecs = spla.eigsh(K, k=n_eigs, M=M, sigma=0, which="LM")
    order = np.argsort(vals)
    vals, vecs = vals[order], vecs[:, order]
    n_ang, Nr = len(m_a), len(s)
    wa = (m_a * R) / np.sum(m_a * R)
    fam = []
    for i in range(n_eigs):
        U = vecs[:, i].reshape(n_ang, Nr)
        prof = wa @ U                       # mass-weighted angular mean u(s)
        num = np.sum(prof ** 2 * (s == s))  # profile energy per shell
        # isotropy score in the M-inner-product:
        e_iso = np.sum((prof ** 2))
        e_tot = np.sum(wa @ (U ** 2))
        score = e_iso / e_tot if e_tot > 0 else 0.0
        if score >= iso_thresh:
            fam.append((i, vals[i], score, prof))
    return vals, fam


def mode_geometry(prof, s):
    p = prof / np.max(np.abs(prof))
    sc = np.where(np.diff(np.sign(p)))[0]
    zeros = []
    for i in sc:
        zeros.append(s[i] + (s[i + 1] - s[i]) * abs(p[i]) / (abs(p[i]) + abs(p[i + 1])))
    zeros = [z for z in zeros if 0.05 < z < 0.97]
    i_anti = int(np.argmax(np.abs(p[: int(0.6 * len(s))])))
    return zeros, s[i_anti]


def run_domain(name, R_of, level, Nr):
    print(f"\n== {name}  (icosphere level {level}, Nr={Nr}) ==")
    V0, F0 = icosahedron()
    V, F = subdivide(V0, F0, level)
    K, M, m_a, R, s = assemble(V, F, R_of, Nr)
    print(f"  angular nodes {len(V)}, DOF {K.shape[0]}, "
          f"R range [{R.min():.4f}, {R.max():.4f}]")
    vals, fam = radial_family(K, M, m_a, R, s)
    print(f"  radial candidates (isotropy>=0.5) among lowest 90: {len(fam)}")
    out = []
    for rank, (i, lam, score, prof) in enumerate(fam[:4], 1):
        zeros, anti = mode_geometry(prof, s)
        k_eff = math.sqrt(lam) * np.mean(R)   # report in mean-radius units
        print(f"  radial mode {rank}: idx {i+1}, k*<R> = {k_eff:.5f}, "
              f"iso {score:.3f}, zeros {['%.4f' % z for z in zeros]}, "
              f"antinode s = {anti:.4f}")
        out.append(dict(rank=rank, k=k_eff, score=score, zeros=zeros, anti=anti))
    return out


def main():
    passes = []
    def check(name, ok, detail=""):
        passes.append((name, ok))
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}"
              f"{(' — ' + detail) if detail else ''}")

    # ---- SPHERE CONTROL: the instrument must reproduce Spin II exactly ----
    ctrl = run_domain("SPHERE CONTROL", R_sphere, level=3, Nr=120)
    k1t, k2t = math.pi / 2, 3 * math.pi / 2
    check("control k1 = pi/2 (0.5%)", abs(ctrl[0]["k"] - k1t) < 5e-3 * k1t,
          f"{ctrl[0]['k']:.5f} vs {k1t:.5f}")
    check("control k2 = 3pi/2 (0.5%)", abs(ctrl[1]["k"] - k2t) < 5e-3 * k2t,
          f"{ctrl[1]['k']:.5f} vs {k2t:.5f}")
    z2 = ctrl[1]["zeros"]
    check("control Mode-2: one interior zero at 2/3 (1%)",
          len(z2) == 1 and abs(z2[0] - 2 / 3) < 0.01, f"{z2}")
    check("control Mode-2 antinode at 1/3 (2%)",
          abs(ctrl[1]["anti"] - 1 / 3) < 0.02, f"{ctrl[1]['anti']:.4f}")

    # ---- TRUE VORONOI CELL (dodecahedron), two densities ----
    lo = run_domain("DODECAHEDRON (true Voronoi cell) — density 1",
                    R_dodeca, level=2, Nr=80)
    hi = run_domain("DODECAHEDRON (true Voronoi cell) — density 2",
                    R_dodeca, level=3, Nr=120)

    def reading(res):
        if len(res) < 2:
            return "INDETERMINATE", None
        m2 = res[1]
        ok = (len(m2["zeros"]) == 1
              and 0.60 <= m2["zeros"][0] <= 0.73
              and 0.28 <= m2["anti"] <= 0.40)
        return ("MODE2-RECOVERED" if ok else "INDETERMINATE"), m2

    r_lo, m2_lo = reading(lo)
    r_hi, m2_hi = reading(hi)
    stable = (r_lo == r_hi == "MODE2-RECOVERED"
              and abs(m2_lo["zeros"][0] - m2_hi["zeros"][0]) < 0.02)
    verdict = "MODE2-RECOVERED" if stable else (
        "MODE2-ABSENT" if (r_hi != "MODE2-RECOVERED" and len(hi) >= 20)
        else "INDETERMINATE")
    print(f"\n  density-1 reading: {r_lo}; density-2 reading: {r_hi}")
    check("frozen verdict MODE2-RECOVERED (both densities, node drift <0.02)",
          verdict == "MODE2-RECOVERED", f"verdict {verdict}")

    if m2_hi:
        drift_k = abs(m2_hi["k"] - k2t) / k2t
        print(f"\n  dodeca Mode-2: k*<R> = {m2_hi['k']:.5f} "
              f"(sphere {k2t:.5f}; shift {100*drift_k:.2f}%), "
              f"node {m2_hi['zeros'][0]:.4f} (2/3 = 0.6667), "
              f"antinode {m2_hi['anti']:.4f} (1/3 = 0.3333)")

    print("\n== SUMMARY ==")
    n_ok = sum(1 for _, ok in passes if ok)
    for name, ok in passes:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    print(f"{n_ok}/{len(passes)} checks pass; FROZEN VERDICT: {verdict}")
    sys.exit(0 if n_ok == len(passes) else 1)


if __name__ == "__main__":
    main()
```

### §7.4 Package B — the analytic leg (Patch 3238)
```python
#!/usr/bin/env python3
"""Patch 3238 verify script — OPEN-QM-8 ANALYTIC LEG (icosahedral selection).

Turns every arithmetic claim of the Spin III analytic-leg theorems into a
checked computation:

  1. CHARACTER COUNTS (Lemma: invariant content of I). The multiplicity of
     the trivial irrep of the icosahedral rotation group I in the spin-l
     representation of SO(3), by the exact character formula
         m_l = (1/60) * sum_classes |C| * sin((l+1/2)theta_C)/sin(theta_C/2),
     over the classes {E(1), C5(12, 72deg), C5^2(12, 144deg), C3(20, 120deg),
     C2(15, 180deg)}. Claim: m_l = 0 for l = 1..5; m_6 = 1; m_10 = 1;
     m_12 = 1. (Parity/inversion in I_h then kills odd l for the even
     boundary function; m_15 = 1 for I is computed and noted as
     parity-excluded.)

  2. HARMONIC CONTENT OF THE TRUE CELL. Project the dodecahedron support
     function R(omega) = 1/max_f(omega . n_f) onto real spherical harmonics
     on a Gauss-Legendre x uniform-phi product grid. Claim: relative
     amplitudes eps_l = sqrt(sum_m a_lm^2)/(sqrt(4 pi) Rbar) vanish (to
     quadrature error) for l = 1..5 and every odd l, and the first
     nonzero channel is l = 6; report eps_6, eps_10, eps_12.

  3. THE l=6 GAP (selection). Lowest eigenvalue of the l=6 radial u-problem
         -u'' + (42/r^2) u = k^2 u,  u(0)=0, u'(R)=0,
     by FD. Claim: k_{6,1} R > 3 pi / 2, so within the trivial irrep the
     second mode of the true cell is the deformed radial Mode 2 — the
     anchoring mode — for the actual cell's anisotropy. Also computes the
     l=1 and l=2 lowest eigenvalues and checks the INTERLOPER ACCOUNTING:
     exactly l=1 (3 states) + l=2 (5 states) = 8 non-invariant modes sit
     between radial Modes 1 and 2, matching the 3236 run's global indices
     (radial modes at 1 and 10).

  4. PROTECTION ORDER (consistency with the 3236 measurement). The
     perturbative claim is that fractional positions shift at O(eps_6^2)
     and the (mean-normalized) eigenvalue at O(eps_6^2). Reports
     eps_6^2 against the measured residuals (|dk|/k = 0.31%, node shift
     0.05%) — an order-of-magnitude consistency check, stated as such
     (the 3236 instrument's own declared approximation enters at the same
     order, so this is consistency, not decomposition).

Run: python3 3238_verify_2I_selection.py
"""

import math
import sys

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.special import lpmv

PHI = (1 + math.sqrt(5)) / 2

passes = []
def check(name, ok, detail=""):
    passes.append((name, ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}{(' — ' + detail) if detail else ''}")


# ------------------------------------------------------------- 1. characters
print("== 1. Trivial-irrep multiplicities of I in spin-l (exact characters) ==")
classes = [  # (size, rotation angle in radians)
    (1, 0.0),
    (12, 2 * math.pi / 5),
    (12, 4 * math.pi / 5),
    (20, 2 * math.pi / 3),
    (15, math.pi),
]
def chi_l(l, theta):
    if abs(theta) < 1e-12:
        return 2 * l + 1
    return math.sin((l + 0.5) * theta) / math.sin(theta / 2)

def mult_trivial(l):
    s = sum(size * chi_l(l, th) for size, th in classes)
    m = s / 60.0
    return m

expect = {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0, 8: 0, 9: 0,
          10: 1, 11: 0, 12: 1, 15: 1}
all_ok = True
for l in sorted(expect):
    m = mult_trivial(l)
    ok = abs(m - expect[l]) < 1e-9
    all_ok &= ok
    print(f"    l={l:>2}: m = {m:+.6f}  (expected {expect[l]})")
check("m_l = 0 for l=1..5; first invariant channel l=6 (exact)", all_ok)
print("    (m_15 = 1 for the rotation group I; excluded for the even boundary")
print("     function by the inversion in I_h — odd l carries odd parity.)")


# --------------------------------------------------- 2. cell harmonic content
print("\n== 2. Harmonic content of the true Voronoi cell's support function ==")
def icosa_vertices():
    v = []
    for s1 in (1, -1):
        for s2 in (1, -1):
            v += [(0, s1, s2 * PHI), (s1, s2 * PHI, 0), (s2 * PHI, 0, s1)]
    V = np.unique(np.array(v, float).round(12), axis=0)
    return V / np.linalg.norm(V, axis=1)[:, None]

ICO = icosa_vertices()

n_t, n_p = 240, 480
x_gl, w_gl = np.polynomial.legendre.leggauss(n_t)   # x = cos(theta)
phi = (np.arange(n_p) + 0.5) * 2 * math.pi / n_p
w_p = 2 * math.pi / n_p
ct = x_gl[:, None] * np.ones(n_p)[None, :]
st = np.sqrt(1 - ct ** 2)
X = st * np.cos(phi)[None, :]
Y = st * np.sin(phi)[None, :]
Z = ct
dirs = np.stack([X, Y, Z], axis=-1)                  # (n_t, n_p, 3)
R = 1.0 / np.max(dirs @ ICO.T, axis=-1)              # support radius, rho_in=1
W = w_gl[:, None] * w_p * np.ones(n_p)[None, :]      # quadrature weights

Rbar = float(np.sum(R * W) / (4 * math.pi))

def real_Ylm(l, m, ct2, phi1):
    # orthonormal real spherical harmonics
    mm = abs(m)
    norm = math.sqrt((2 * l + 1) / (4 * math.pi)
                     * math.factorial(l - mm) / math.factorial(l + mm))
    P = lpmv(mm, l, ct2)
    if m > 0:
        return math.sqrt(2) * norm * P * np.cos(mm * phi1)[None, :]
    if m < 0:
        return math.sqrt(2) * norm * P * np.sin(mm * phi1)[None, :]
    return norm * P * np.ones_like(phi1)[None, :]

eps = {}
for l in range(0, 13):
    p2 = 0.0
    for m in range(-l, l + 1):
        Y_ = real_Ylm(l, m, x_gl[:, None], phi)
        a = float(np.sum(R * Y_ * W))
        p2 += a * a
    eps[l] = math.sqrt(p2) / (math.sqrt(4 * math.pi) * Rbar)

print(f"    mean radius <R> = {Rbar:.6f} (inradius units)")
for l in range(0, 13):
    tag = "  <-- first anisotropy channel" if l == 6 else ""
    print(f"    eps_{l:<2} = {eps[l]:.3e}{tag}")

quad_floor = 5e-4   # support function has edge kinks; quadrature is algebraic
forbidden = max(eps[l] for l in (1, 2, 3, 4, 5, 7, 8, 9, 11))
check("eps_l at the quadrature floor for l=1..5,7,8,9,11",
      forbidden < quad_floor, f"max forbidden {forbidden:.1e}")
check("l=6 is the leading anisotropy channel",
      eps[6] > 10 * forbidden and eps[6] > eps[10] > 0,
      f"eps_6 = {eps[6]:.3e}, eps_10 = {eps[10]:.3e}, eps_12 = {eps[12]:.3e}")


# ------------------------------------------------------------- 3. the l=6 gap
print("\n== 3. The l=6 gap and the interloper accounting ==")
def lowest_k(l, N=20000, R1=1.0):
    h = R1 / N
    r = (np.arange(1, N + 1)) * h
    d = np.full(N, 2.0) / h**2 + l * (l + 1) / r**2
    d[-1] = 1.0 / h**2 + l * (l + 1) / r[-1] ** 2
    o = np.full(N - 1, -1.0) / h**2
    K = sp.diags([o, d, o], [-1, 0, 1], format="csr")
    b = np.ones(N); b[-1] = 0.5
    B = sp.diags(b, format="csr") * 1.0
    v = spla.eigsh(K, k=1, M=B, sigma=0, which="LM",
                   return_eigenvectors=False)
    return math.sqrt(float(v[0]))

k2 = 3 * math.pi / 2
k6 = lowest_k(6)
k1l = lowest_k(1)
k2l = lowest_k(2)
k3l = lowest_k(3)
print(f"    k(l=1,n=1) = {k1l:.4f}, k(l=2,n=1) = {k2l:.4f}, "
      f"k(l=3,n=1) = {k3l:.4f}")
print(f"    k(l=6,n=1) = {k6:.4f}   vs   radial Mode 2: 3pi/2 = {k2:.4f}")
check("l=6 gap: k(6,1) > 3pi/2 (selection within the trivial irrep)",
      k6 > k2, f"{k6:.4f} > {k2:.4f}")
between = [("l=1", k1l, 3), ("l=2", k2l, 5), ("l=3", k3l, 7)]
count = sum(mult for _, kv, mult in between if math.pi / 2 < kv < k2)
names = [nm for nm, kv, _ in between if math.pi / 2 < kv < k2]
check("interloper accounting: exactly 8 non-invariant modes between radial "
      "Modes 1 and 2 (l=1 + l=2)", count == 8 and names == ["l=1", "l=2"],
      f"{names} -> {count} states (3236 run: radial modes at global "
      f"indices 1 and 10)")


# ------------------------------------------------- 4. protection consistency
print("\n== 4. Protection order vs the 3236 measured residuals ==")
e6sq = eps[6] ** 2
meas_dk = 0.0031     # |k shift| / k, mean-radius-normalized (3236 record)
meas_node = 0.0005   # node position shift (0.6670 vs 0.6667)
print(f"    eps_6 = {eps[6]:.4f}  =>  eps_6^2 = {e6sq:.5f}")
print(f"    measured: |dk|/k = {meas_dk:.4f}, node shift = {meas_node:.4f}")
check("measured residuals are O(eps_6^2)-sized (order consistency: "
      "0.1x-3x window)", 0.1 * e6sq < meas_dk < 3 * e6sq,
      f"eps_6^2 = {e6sq:.4f} vs |dk|/k = {meas_dk:.4f}")
check("node shift <= eps_6^2 class", meas_node < 3 * e6sq,
      f"{meas_node:.4f} <= {3*e6sq:.4f}")

print("\n== SUMMARY ==")
n_ok = sum(1 for _, ok in passes if ok)
for name, ok in passes:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
print(f"{n_ok}/{len(passes)} checks pass")
sys.exit(0 if n_ok == len(passes) else 1)
```

## §8 Response format (use exactly this skeleton)

```
REVIEWER: <your own actual model name>
TIER LEGEND USED: INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED

Q1: <DISCIPLINED | OVERCLAIMS: "<quoted passage>" | UNDERCLAIMS: "<quoted passage>">  [tier]
Q2: <COMPLETE | GAP-NAMED: <item>>  [tier]
Q3: <SOUND | DEFECT-NAMED: <defect>>  [tier]
Q4: <SHIP-PATH-CLEAR: <calibrations, if any> | RESTATE-REQUIRED: <verdict-flipper> | STRUCTURAL-REWORK>
Q5: <VALID | DEFECT-NAMED: <defect>>  [tier]
Q6: <CALIBRATED | OVERREAD | UNDERREAD>  [tier]
Q7: <JUSTIFIED-AS-INHERITED | NEEDS-INDEPENDENT-GROUNDING: <what>>
Q8: <RATIFY | DEMOTE: <status> | UPGRADE: <status>>

SCRIPT OUTPUT (if executed): <paste the SUMMARY blocks with digits>
STRONGEST OBJECTION (mandatory, even if all verdicts positive): <one paragraph>
NOVEL CONTRIBUTION (optional): <anything the packages missed>
```

*End of CONV-026 package. Thank you — one identical document is pasted to
every seat; your steer is your §6 row.*
