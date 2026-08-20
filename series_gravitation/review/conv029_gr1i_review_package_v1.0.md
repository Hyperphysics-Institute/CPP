You are one of five independent reviewers (ChatGPT, Grok, Copilot, Gemini,
DeepSeek) on the Conscious Point Physics (CPP) review panel.
IDENTITY (mandatory): in the §8 REVIEWER field put YOUR OWN actual
model/provider name; never echo another seat's name. (Both prior-round
identity/format defects were cured last round — please keep it that way.)
INDEPENDENCE (mandatory): your own analysis only.
Please review CONV-029 — the classical-tests companion **GR-1i** ("The
Classical Tests of Gravitation in Conscious Point Physics", V0). This is the
LAST unreviewed paper of the gravitational arc; on its adjudication,
OPEN-GR-TESTS-1 finally discharges and the series parent GR-1 proceeds to
V1.0 prep. Everything needed is inline; your steer is in §6; the paper's
verify script is in §7 (run it if you can; report SCRIPT-EXECUTED with
digits). Tier every claim (INSPECTED / INDEPENDENTLY RECOMPUTED /
SCRIPT-EXECUTED); answer in the §8 skeleton.

File (provenance; inline content authoritative):
  raw: https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_gravitation/review/conv029_gr1i_review_package_v1.0.md

---

# CONV-029 Review Package v1.0 — GR-1i: The Classical Tests

**Dispatched:** 20 Aug 2026, Session 150, Patch 3268. Founder-initiated.
**Responses land in:** `series_gravitation/review/reviews-CONV-029.md`.
**Settled, out of scope:** the T-1 field equation, the GR-1c corrigendum
(V2.2), R-CSTAR-MAP, T-2/T-3, GR-1j (CONV-027/028 + founder-ratified).

## §1 Context (cold-start, condensed)

CPP's gravitational sector, conditional on the PSR constitutive form
PSR_eff = l_P/(1 + k·Δ|SSV|) at W2 viability strength, produces EXACTLY the
Schwarzschild metric in isotropic coordinates (GR-1c Theorem 1): with
ϱ = GM/(2c²r) and the source relation k·Δ|SSV| = GM/rc²,
ds² = −((1−ϱ)/(1+ϱ))² c²dt² + (1+ϱ)⁴ (dr² + r²dΩ²). The exact coordinate
transformation r_std = r(1+ϱ)² takes this to the standard Schwarzschild
form (machine-verified identity, 3.3e-16). GR-1 (the series parent)
carries a results-only classical-tests table and defers ALL four
derivations, by founder ruling, to ONE companion: GR-1i, the paper under
review. Frozen claim discipline (stated in GR-1i's abstract and §1):
(i) conditional on the PSR form (W2, inherited, not upgraded); (ii) every
value is the GR value BY CONSTRUCTION (the metric is exactly
Schwarzschild); (iii) the tests discriminate CPP from NEWTON, not from GR;
(iv) Lense–Thirring is not redone (GR-1f/GR-1c territory); (v) zero new
zero-parameter predictions are minted (counting these values would
double-count GR-1c's exactness theorem) — the paper's stated contribution
is entry-criterion compliance in one citable place.

## §2 GR-1i claim chain

- **C-1 (coordinate route).** The four tests are coordinate-invariant
  observables; they are derived in standard Schwarzschild coordinates via
  the machine-verified exact transformation, and apply verbatim to the
  isotropic form. The isotropic frame returns in the mechanism section,
  where the graded-index reading is transparent (coordinate light speed
  c(r) ≈ c(1 − 2GM/c²r); n(r) ≈ 1 + 2GM/c²r).
- **C-2 (geodesics).** Conserved E and h from the static metric; Binet
  equations u″ + u = GM/h² + 3GMu²/c² (timelike) and u″ + u = 3GMu²/c²
  (null); Newtonian limits are the same equations without the 3GMu²/c²
  term.
- **C-3 (Test I, perihelion).** Perturbative resonant-term extraction from
  u₀ = A(1 + e·cosφ): δ = 3GM/(c²a(1−e²)); Δφ = 6πGM/(a(1−e²)c²) per
  orbit; Mercury (a = 5.7909×10¹⁰ m, e = 0.20563, GM_⊙ = 1.3275×10²⁰
  m³s⁻² — deliberately the verify script's own constant, provenance-
  matched): 5.019×10⁻⁷ rad/orbit × 415.2 orbits/century = 42.99″/cy vs
  observed 42.98 ± 0.04. Independent numeric RK4 Binet integration agrees
  with the closed form to four decimals (42.9917 vs 42.9917).
- **C-4 (Test II, deflection).** Photon Binet perturbation:
  u₁ = (3GM/2c²b²)(1 + ⅓cos2φ) ≡ (GM/c²b²)(1 + cos²φ) — the identity is
  EXACT; asymptote value 2GM/c²b²; total α = 4GM/(c²b) = 1.7516″ at the
  solar limb (numeric 1.7517″, 0.006%). The factor-of-two section: half
  from g_tt, half from g_ij; a scalar-broadcast-only CPP variant would
  bend light half as much — the deflection test separates the
  two-component LSP broadcast (GR-1b) from Newton AND from scalar-only
  CPP.
- **C-5 (Test III, Shapiro).** Leading-log round trip
  Δt = (4GM/c³)ln(4r_E r_V/b²) = 232.6 ≈ 233 μs (Earth–Venus, grazing).
  Sub-leading terms explicitly deferred to the γ-parametrized framing;
  Cassini bound quoted (γ−1 = (2.1±2.3)×10⁻⁵); CPP has γ = 1 identically.
- **C-6 (Test IV, redshift/GPS).** Static clock rates; Pound–Rebka
  gh/c² = 2.46×10⁻¹⁵ over 22.5 m; GPS: gravitational +45.7, special-
  relativistic −7.2 (credited to the SR-1 inheritance), net +38.5 μs/day.
- **C-7 (verification).** Everything machine-checked in the paper's own
  script (§7): the coordinate identity (3.3e-16); both dynamical tests by
  closed form AND independent numeric geodesic integration; the two
  numerical traps (φ-accumulation drift; crossing overshoot) found on the
  script's first run are documented IN THE PAPER BODY for reimplementers.
- **C-8 (PD-001 suite).** Keywords, Plain Language Summary, Mechanism
  section with CP/GP Signature, CPP-to-conventional mapping, Swarm-
  Validation (zero new predictions), Problem Status (OPEN-GR-TESTS-1
  discharged at V0, final at this review).

## §3 Triage — the hardest attacks (press these)

1. **The perturbation bookkeeping (C-3).** Is the resonant-term
   extraction clean — constant and cos2φ pieces correctly discarded as
   bounded, the secular term correctly identified? Recompute δ.
2. **The deflection identity (C-4).** Verify (3/2)(1 + ⅓cos2φ) ≡
   1 + cos²φ and the asymptote matching that yields α = 4GM/c²b; is the
   half-and-half g_tt/g_ij attribution stated correctly?
3. **Shapiro honesty (C-5).** Is the leading-log-only claim, with
   sub-leading terms deferred to γ, the right discipline — or does
   quoting "~233 μs" against a γ-parametrized modern bound blur the
   claim?
4. **Provenance of constants (C-3).** The paper quotes GM_⊙ = 1.3275×10²⁰
   (the script's G×M product), NOT the IAU 1.32712×10²⁰ — a deliberate
   provenance-matching choice. Right call, or should the paper carry the
   IAU value with a stated tolerance?
5. **Consistency with the now-ratified field equations.** GR-1i predates
   the FE-1 closure by a day: is its graded-index mechanism reading
   (C-1) consistent with the ratified log-lapse/lattice picture, or does
   any sentence now need harmonizing? (Note: the metric and all four
   values are untouched by FE-1 — this is a language-level check.)

## §4 — (reserved; no second package this round)

## §5 Frozen questions and vocabulary (answer ALL six)

- **Q1 (derivation chain):** SOUND / DEFECT-NAMED (step C-1…C-7 + defect;
  flag if verdict-flipping).
- **Q2 (claim discipline):** DISCIPLINED / OVERCLAIMS ("quote") /
  UNDERCLAIMS ("quote").
- **Q3 (numerical verification adequacy):** VERIFIED / DEFECT-NAMED.
- **Q4 (mechanism section + factor-of-two framing):** CORRECT-AND-HONEST /
  MISFRAMED (state the honest framing).
- **Q5 (completeness as the arc's tests companion):** READY /
  REVISE-NAMED (name it).
- **Q6 (status moves, vote both):**
  (a) OPEN-GR-TESTS-1: FINAL-DISCHARGE / BLOCK (verdict-flipper);
  (b) GR-1i: SHIP-PATH-CLEAR (V1.0 prep may begin) / RESTATE-REQUIRED
      (name it) / BLOCK.

**Binding:** majority per question; a sustained flipper on Q1 blocks both
Q6 moves; Q6(b) additionally requires a Q2 DISCIPLINED majority. Minority
specifications preserved verbatim. Panel attribution: "the AI review
panel."

## §6 Reviewer steers — read your own row

- **ChatGPT:** run the §7 script (SCRIPT-EXECUTED, digits). Then audit
  C-3's perturbation bookkeeping (triage 1): derive δ yourself from the
  resonant term and confirm the discarded pieces are non-secular.
- **Grok:** independently recompute C-4 end to end: the exact identity,
  the asymptote matching, the numeric 1.7517″, and the half/half
  g_tt-vs-g_ij attribution.
- **Gemini:** audit C-5 (triage 3): is the leading-log discipline against
  the Cassini γ-bound honestly framed? Also triage 4 (the constants-
  provenance call).
- **Copilot:** line-level audit of the abstract, claim-discipline §, Table
  1, and the Swarm-Validation zero-claim; check every Table-1 number
  against the §2 chain.
- **DeepSeek:** recompute C-6 (Pound–Rebka and all three GPS numbers) and
  run triage 5: the graded-index reading vs the ratified log-lapse
  picture — any sentence needing harmony?

## §7 Verify code — IN FULL (the paper's own script; 8/8 expected)

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

## §8 Response format (use exactly this skeleton)

```
REVIEWER: <your own actual model name>
TIER LEGEND USED: INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED

Q1: <SOUND | DEFECT-NAMED: <step + defect> [verdict-flipping? yes/no]>  [tier]
Q2: <DISCIPLINED | OVERCLAIMS: "<quote>" | UNDERCLAIMS: "<quote>">
Q3: <VERIFIED | DEFECT-NAMED: <what + how>>  [tier]
Q4: <CORRECT-AND-HONEST | MISFRAMED: <the honest framing>>  [tier]
Q5: <READY | REVISE-NAMED: <the revision>>
Q6a: <FINAL-DISCHARGE | BLOCK: <verdict-flipper>>
Q6b: <SHIP-PATH-CLEAR | RESTATE-REQUIRED: <the restate> | BLOCK>

SCRIPT OUTPUT (if executed): <paste the SUMMARY lines with digits>
STRONGEST OBJECTION (mandatory): <one paragraph>
NOVEL CONTRIBUTION (optional): <anything missed>
```

*End of CONV-029 package. One identical document per seat; your steer is
your §6 row.*
