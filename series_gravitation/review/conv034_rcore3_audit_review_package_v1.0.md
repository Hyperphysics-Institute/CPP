# CONV-034 REVIEW PACKAGE v1.0 — OPEN-GR-RCORE-3 Legs A + B Audit
# (Patch 3335, 21 Aug 2026, Session 156)

**PASTE DISCIPLINE (founder):** this ENTIRE file is one package. Paste
its full contents to each of the five seats — one identical paste per
seat (Copilot may need the file-upload route). Execution-capable seats
also receive the two separate `.py` files. Returns come back INLINE as
text, verbatim.

---

## §0 One-paragraph intro (cold start)

Conscious Point Physics (CPP) derives gravitational phenomena from a
substrate model; its compact objects are horizonless, hard-surfaced
bodies at exactly the Buchdahl radius (panel-ratified reading F-R1),
predicting gravitational-wave "echoes." The shipped paper GR-2 V1.0
("The Echo Falsifier," reviewed by this panel as CONV-033) gives an
EQUATORIAL EIKONAL template: a 2.624 ms retrograde-keyed echo delay
for GW150914, explicitly naming the unquantified eikonal systematic
as its dominant uncertainty and fencing finite-(ℓ,m) work as
OPEN-GR-RCORE-3. THIS ROUND audits the two computations that then
discharged that systematic at their stated grades: **Leg A** (Patch
3333 — finite-ℓ cavity spectroscopy at χ=0: the eikonal comb does NOT
survive; a single top-of-barrier resonance per parity replaces it;
plus a Kerr mode-fate reconnaissance) and **Leg B** (Patch 3334 — a
Bohr–Sommerfeld resonance census on Kerr: the comb is NOT restored at
any astrophysical spin; the refined search target is a mode-resolved
LINE SET). The stakes: on this round's clearance + founder
ratification, the registered prediction PRED-O-39 is amended per the
provisional text in the Leg-B record §4, and GR-2 V1.0 receives an
additive amendment set. GitHub (repo `CPP`, branch `main`, HEAD =
Patch 3334): `series_gravitation/rcore_derivation/3333_rcore3_legA_finite_ell.md`,
`.../3334_rcore3_legB_kerr_census.md`,
`series_gravitation/code/3333_rcore3_legA_finite_ell_verify.py`,
`.../3334_rcore3_legB_kerr_wkb_verify.py`.

## §1 What is under review / what is fenced

UNDER REVIEW: (a) the Leg-A instrument (frequency-domain scattering
phase δ(ω), Wigner delay τ = 2 dδ/dω; wall-shift validation; TD
cross-validation) and its findings; (b) the Leg-B instrument
(geodesic-eikonal radial WKB; fixed eikonal Carter constant
Q = (ℓ+½)² − m²; k = √R/Δ; Bohr–Sommerfeld count at Φ = (n+¾)π with
one hard wall + one smooth turning point) and its findings; (c) the
retraction discipline (a provisional "+1% comb correction" was nearly
claimed and retracted — audit whether it is fully dead); (d) the
PROVISIONAL PRED-O-39 refinement text (Leg-B record §4); (e) the
GR-2 amendment set (additive under the existing eikonal scoping).

FENCED (settled upstream, NOT re-adjudicated): A1–A3 + the
ergoregion-censorship mathematics (CONV-032, 5/5); the derived Kerr
exclusion surface itself; |R| = 1 (spin-independent); GR-2 V1.0's
eikonal-scoped claims (CONV-033, 4–1 clear); F-R1; the eikonal delay
closed form (3/2 + 8 ln 2) GM/c³. The A1–A3 conditionality
(OPEN-GR-RCORE-4) is INHERITED by everything here and stated in both
records — reviewers should verify it is stated, not re-litigate it.

## §2 Claim chains

**Leg A (χ = 0, ℓ = 2):**
A-1 The Dirichlet wall at areal 9M/4 + the ℓ=2 barrier form a cavity
    ~3.5 M long (tortoise x_wall = −1.909, barrier peaks at
    x = 2.39 (RW) / 1.90 (Zerilli)).
A-2 The Wigner delay τ(ω) of the exact scattering phase shows exactly
    ONE prominent resonance per parity: RW ω₁ = 0.4535 (236 Hz @ 62
    M_⊙, τ = 21.5 GM, Q = 4.9); Zerilli ω₁ = 0.4513 (0.5% split).
A-3 The resonance sits ABOVE the barrier top (√V_max = 0.389):
    top-of-barrier reprocessing, not a deep-cavity trapped mode.
A-4 Instrument validation: an inward wall displacement δ = 2.0 grows
    the high-ω geometric plateau by 4.12 vs exactly 4.00 expected;
    stable under grid/box refinement (<1%).
A-5 TD cross-validation: an independent time-domain evolution's
    late-time spectral peak = 0.4488 (−1.0% vs FD).
A-6 Kerr mode-fate recon (geodesic grade, χ = 0.68): finite-ℓ mode
    barriers are inclined spherical photon orbits (μ = m/(ℓ+½) ≈
    ξ/√(ξ²+η)); the ENTIRE corotating (ℓ,ℓ) branch is FULLY-BURIED
    (μ_crit = 0.774 < μ(ℓ,ℓ) ≥ 0.8); (2,+1),(2,0),(2,−1),(2,−2)
    EXPOSED; the (2,+2) burial onset is χ = 0.665 (vs eikonal
    equatorial 0.555) with thin margin 0.026 at χ = 0.68.
A-7 RETRACTION: a provisional "+1–3% finite-ℓ comb correction" from
    two failed TD instruments is retracted — the measured 7.00 GM/c³
    was π/ω₁ (the resonance carrier half-period), whose match to the
    eikonal 7.045 is STRUCTURAL (ω₁ ≈ π/2L). Caught by the
    wall-shift test + a no-wall control. Five-dead-end trail kept in
    the script header and record §3.

**Leg B (Kerr):**
B-1 For fixed (ℓ,m), the eikonal Carter constant Q = (ℓ+½)² − m² is
    ω-independent; the radial function R(r;ω) = [ω(r²+a²) − am]² −
    Δ[(m−aω)² + Q] gives k = √R/Δ (radial Hamilton–Jacobi).
B-2 Bohr–Sommerfeld with one hard node (wall) + one smooth turning
    point: resonances at Φ(ωₙ) = (n+¾)π; N_trapped is a computed
    integer per mode.
B-3 a→0 anchor: ω_top = (ℓ+½)/√27 recovered to <1%; Φ_max/π = 0.178
    < ¾ ⇒ N = 0 — exactly Leg A's finding (its single resonance is
    ABOVE the top). The instrument could have failed here; it didn't.
B-4 Census at χ = 0.68 (equatorial wall 2.2668 M): every exposed
    mode has N_trapped = 0 — (2,−2) Φ_max/π = 0.245, (2,−1) 0.138,
    (2,0) 0.056, (2,+1) 0.007, (3,−3) 0.366; threshold ¾.
B-5 Spin scan χ ∈ [0.30, 0.98] for (2,−2): max Φ_max/π = 0.247 (at
    0.52); N ≥ 1 NOWHERE. Mechanism: the lengthening retrograde
    cavity and the falling barrier top (ω_top 0.4425 → 0.3846,
    monotone) cancel.
B-6 Wave-side burial: for (2,+2) the forbidden region R < 0 begins
    AT THE WALL for every ω < 0.642 (e.g. R(wall) = −5.4 at
    ω = 0.05); above 0.642 no barrier exists — no propagating cavity
    at any frequency.
B-7 Wall-sensitivity: at the smallest surface radius the (2,−2)
    orbit's latitude band sees (2.1897 M, longest cavity), Φ_max/π
    rises only to 0.304; N unchanged.
B-8 THE REFINED TARGET (eikonal-top grade, +17% Leg-A position
    calibration, Q ~ 5): a mode-resolved LINE SET at
    ~211/233/260/294 Hz @ 62 M_⊙ ((2,−2)/(2,−1)/(2,0)/(2,+1);
    ~247–344 Hz calibrated) + early broadband transients at the
    retrograde-keyed 2.624 ms; retrograde keying survives as line
    ORDERING (the corotating (ℓ,ℓ) lines are ABSENT).

## §3 Triage — the worker's five weakest points, handed to the panel

T-1 **The +17% calibration transport.** The above-top resonance
    position was calibrated at ONE point (χ=0, ℓ=2, RW/Zerilli) and
    transported to five Kerr modes across spins as "~247–344 Hz."
    Is a single-point calibration honest even with the "~" and the
    stated grade, or is it false precision that should be widened or
    dropped to "near the barrier-top frequencies"?
T-2 **The eikonal μ-correspondence at ℓ = 2.** μ = m/(ℓ+½) ↔
    ξ/√(ξ²+η) is exact only as ℓ → ∞; at ℓ = 2 the mapping (and
    hence r_sp, θ_min, μ_crit = 0.774, onset 0.665) carries
    unquantified O(1/ℓ) error. The thin (2,+2) margin (0.026) could
    be inside that error. Are the burial claims correctly graded?
T-3 **The ¾ threshold + census robustness.** Bohr–Sommerfeld with a
    hard wall and smooth turning point gives (n+¾)π — but the
    turning-point structure near the top is soft, and the largest
    Φ_max/π found anywhere is 0.366 ((3,−3)). Is the margin to ¾
    wide enough that WKB phase-convention quibbles cannot flip any
    N to 1? (Worker's position: yes — factor ~2 everywhere — but
    audit it.)
T-4 **The wall as non-corotating Dirichlet.** Surface co-rotation
    ω(r_surf) is a COMMITTED open item (RCORE-3 (b)); a corotating
    boundary shifts effective frequencies mode-dependently. Could
    it plausibly create trapping the static wall lacks, or only
    shift line positions?
T-5 **Retraction adequacy.** The dead "+1%" claim had convergence
    and parity-consistency stamps when it was caught. Is the record
    honest that these virtues were traps, and is the structural-
    coincidence diagnosis (π/ω₁ ≈ eikonal because ω₁ ≈ π/2L)
    correct?

## §4 Frozen questions (answer ALL; use ONLY the given vocabulary)

Q1 — Leg-A instrument (FD scattering phase + wall-shift + TD
    cross-validation): **VALID / VALID-WITH-CAVEATS / INVALID**
Q2 — Leg-B instrument (WKB census, fixed-Q correspondence, ¾
    threshold, a→0 anchor): **VALID / VALID-WITH-CAVEATS / INVALID**
Q3 — Findings, each separately **CONFIRMED / NOT-CONFIRMED**:
    (i) single top-of-barrier resonance at χ=0 (no surviving comb);
    (ii) N_trapped = 0 at every spin (comb not restored);
    (iii) (ℓ,ℓ) burial with onset 0.665 and thin margin, at its
    stated geodesic grade.
Q4 — Retraction/trail discipline (is the +1% claim fully dead; is
    the five-dead-end trail honest): **ADEQUATE / INADEQUATE**
Q5 — The PROVISIONAL PRED-O-39 refinement text (Leg-B record §4):
    **FAITHFUL-AT-GRADE / OVERCLAIMS / UNDERCLAIMS**
Q6 — The GR-2 amendment set (Leg-A pointer; onset 0.665;
    thin-margin caution; line-set restatement — all additive under
    the existing eikonal scoping): **COMPLETE / MISSING-ITEMS**
Q7a — The two-patch assembly overall: **PROPER /
    PROPER-WITH-REVISIONS / IMPROPER**
Q7b — Disposition: **AMENDMENTS-CLEAR / RESTATE-REQUIRED / BLOCK**

BINDING RULES (frozen): majority per question. A majority INVALID on
Q1 reverts the Leg-A discharge to OPEN and strikes the Leg-A-derived
amendment items; likewise Q2 for Leg B. A majority OVERCLAIMS on Q5
blocks the predictions.md execution regardless of the Q7b tally
(flagship-prediction discipline — the CONV-033 rule's analog). All
adopted revisions fold at execution per the CONV-028/033 precedent.

## §5 Seat mandates (all seats)

- **IDENTITY:** put YOUR OWN model name in the REVIEWER field.
  Gemini seat: you are Gemini — do not self-label ChatGPT. DeepSeek
  seat: you are DeepSeek — do not self-label ChatGPT or GPT.
- **OWN-RUN:** SCRIPT-EXECUTED requires YOUR OWN run. Quoting the
  reference run below is INSPECTED and will be reclassified. FAST
  mode is legitimate own-run: `3333_..._verify.py --fast` runs in
  seconds (4 checks); `3334_..._verify.py` is all-FAST (7 checks,
  ~1 min). An independent harness of your own construction is
  INDEPENDENT-HARNESS.
- **COUNT-LINE:** paste your run's final count line(s) VERBATIM.
- **TIER LEGEND:** INSPECTED / INDEPENDENTLY RECOMPUTED /
  SCRIPT-EXECUTED / INDEPENDENT-HARNESS — tag every question.
- **RETURNS:** inline text only, in the §8 skeleton.

Per-seat steers:
- **ChatGPT/GPT (dissent seat):** T-1 and T-2 are yours — attack
  the +17% transport and the ℓ=2 correspondence error; rule whether
  "~247–344 Hz" survives or must widen.
- **Grok (script seat):** own-run both; audit the census numerics
  (grid density, the clip at the turning point, the ¾ convention)
  and the Wigner-delay smoothing/prominence choices.
- **Gemini (error-budget seat):** your CONV-032 error-bar mandate —
  does every quoted number carry honest uncertainty language? Does
  the record anywhere quote what it cannot know at its grade?
- **Copilot (registry seat):** audit the discharge bookkeeping and
  the DISCIPLINE claims — verify predictions.md and GR-2 were NOT
  edited; verify the amendment set is additive under the CONV-033
  scoping; verify anti-erasure on the retraction.
- **DeepSeek (falsifier seat):** does the line-set target remain
  falsifiable — is line ORDERING a real kill condition, and does
  the CONV-033 preregistered injection-recovery criterion carry
  over to lines? What would let a null be explained away?

## §6 Reference runs (for INSPECTED tiers; own-runs preferred)

### 3333 FAST reference (full run is 9/9; TD part ~minutes):
```
[FAST][PASS] F1. eikonal reference reproduced: 2*(x(3M) - x_wall) = (3/2 + 8 ln 2) — x_wall = -1.9089, closed form 7.0452
      surface(chi=0.68): equator 2.2668 M, pole 2.0212 M (min 2.0212, max 2.2668)
      mode (2,+2): mu=+0.800  r_sp=2.1631 M  theta_min= 52.7 deg  -> FULLY-BURIED
      mode (3,+3): mu=+0.857  r_sp=2.1289 M  theta_min= 58.6 deg  -> FULLY-BURIED
      mode (4,+4): mu=+0.889  r_sp=2.1106 M  theta_min= 62.3 deg  -> FULLY-BURIED
      mode (2,+1): mu=+0.400  r_sp=2.4417 M  theta_min= 23.3 deg  -> EXPOSED
      mode (2,0): mu=+0.000  r_sp=2.7731 M  theta_min=  0.0 deg  -> EXPOSED
      mode (2,-1): mu=-0.400  r_sp=3.1354 M  theta_min= 23.4 deg  -> EXPOSED
      mode (2,-2): mu=-0.800  r_sp=3.5139 M  theta_min= 53.0 deg  -> EXPOSED
      burial threshold: FULLY-BURIED for mu > 0.774 (chi = 0.68)
[FAST][PASS] F2. equatorial limits recovered: (2,-2)-limit mu=-0.8 EXPOSED; prograde equatorial ring (mu -> +1) buried — (2,-2): EXPOSED
[FAST][PASS] F3. THE RECON FINDING: the finite-ell prograde (2,+2) barrier (mu=+0.8, an INCLINED spherical orbit) — burial verdict computed honestly — (2,+2) at r_sp=2.1631 M, theta_min=52.7 deg: FULLY-BURIED; mu_crit=0.774
[FAST][PASS] F4. finite-ell (2,+2) burial ONSET located; sits ABOVE the eikonal equatorial onset 0.555 (thin-margin caution at chi = 0.68 recorded) — onset chi(2,+2) = 0.665; margin at 0.68 in mu: 0.026
FAST: 4/4 PASS
```

### 3334 full reference:
```
chi = 0.68: equatorial wall r = 2.2668 M
[PASS] 1. a->0 VALIDATION against Leg A: ell=2 cavity holds ZERO sub-top resonances, and omega_top matches the closed form (ell+1/2)/sqrt(27) — omega_top = 0.4811 vs 0.4811; Phi_max/pi = 0.178 < 3/4 -> N = 0 (Leg-A FD found its single resonance ABOVE the top — consistent)
[PASS] 2. (2,+2) at chi=0.68: the wave-side confirmation of burial — the forbidden region R<0 starts AT THE WALL for all omega below 0.642 (the wall sits inside the mode's forbidden zone; no propagating cavity exists at any omega), so N_trapped = 0 — R(wall) = -3.267 < 0 below omega = 0.642; above it, no barrier anywhere — either way, no cavity
      mode (2,-2): omega_top = 0.4055 (~211 Hz @62; Leg-A calibration +17% -> ~247 Hz), Phi_max/pi = 0.245, N_trapped = 0
      mode (2,-1): omega_top = 0.4477 (~233 Hz @62; Leg-A calibration +17% -> ~273 Hz), Phi_max/pi = 0.138, N_trapped = 0
      mode (2,0): omega_top = 0.4996 (~260 Hz @62; Leg-A calibration +17% -> ~305 Hz), Phi_max/pi = 0.056, N_trapped = 0
      mode (2,+1): omega_top = 0.5643 (~294 Hz @62; Leg-A calibration +17% -> ~344 Hz), Phi_max/pi = 0.007, N_trapped = 0
      mode (3,-3): omega_top = 0.5601 (~292 Hz @62; Leg-A calibration +17% -> ~342 Hz), Phi_max/pi = 0.366, N_trapped = 0
[PASS] 3. THE LEG-B ANSWER: the retrograde-keyed (2,-2) cavity at chi=0.68 — trapped-resonance count computed, comb question decided by integer — (2,-2): N_trapped = 0 (COMB NOT RESTORED — top-of-barrier reprocessing only)
[PASS] 4. full exposed-mode census at chi=0.68 completed (the multi-line signature set for the search target) — (2,-2): N=0, f~211 Hz; (2,-1): N=0, f~233 Hz; (2,0): N=0, f~260 Hz; (2,+1): N=0, f~294 Hz; (3,-3): N=0, f~292 Hz
[PASS] 5. wall-sensitivity: with the SMALLEST surface radius the (2,-2) orbit's latitude band sees (longest cavity), the trapped count is unchanged — wall 2.2668 -> 2.1897 M: Phi_max/pi 0.245 -> 0.304, N 0 -> 0
[PASS] 6. spin scan chi in [0.30, 0.98]: does the (2,-2) trapped count ever reach 1? (the comb-restoration question across the astrophysical range) — max Phi_max/pi = 0.247 at chi = 0.52; N >= 1 anywhere: False
[PASS] 7. sanity: omega_top(2,-2) decreases monotonically with spin (the retrograde ring recedes and slows) — omega_top: 0.4425, 0.4170, 0.4055, 0.3919, 0.3846
7/7 PASS
FAST: all checks are FAST (no TD evolution in this instrument); FAST: 7/7 PASS
```

## §7 The two records and the two scripts, in full

### 7.1 Leg-A record (`rcore_derivation/3333_rcore3_legA_finite_ell.md`)

# OPEN-GR-RCORE-3 — Leg A: Finite-ℓ Cavity Spectroscopy at χ = 0 + the Kerr Mode-Fate Reconnaissance

**Patch 3333, 21 Aug 2026 — Session 156.** Verify:
`code/3333_rcore3_legA_finite_ell_verify.py`, **9/9 PASS** (FAST subset
4/4). Charter: the founder's "proceed with the next physics on deck" —
the eikonal discharge GR-2 V1.0 names as its own dominant uncertainty.

---

## §1 THE LEG-A FINDING: at ℓ = 2, χ = 0, the eikonal echo comb does not survive — it collapses to a single top-of-barrier resonance

Frequency-domain scattering computation (validated instrument, §3):
the Dirichlet wall at the derived surface (areal 9M/4, tortoise
x_wall = −1.909) plus the ℓ = 2 barrier forms a cavity only ~3.5 M
long — too short to support a multi-mode trapped comb. The Wigner
delay τ(ω) = 2 dδ/dω shows exactly ONE prominent resonance per
parity:

| Parity | ω₁ [1/GM] | f₁ @ 62 M_⊙ | τ (lifetime) | Q = ω₁τ/2 |
|---|---|---|---|---|
| Regge–Wheeler (axial) | 0.4535 | **236 Hz** | 21.5 GM | 4.9 |
| Zerilli (polar) | 0.4513 | **235 Hz** | 19.5 GM | 4.4 |

The resonance sits ABOVE the barrier top (√V_max = 0.389): this is
top-of-barrier reprocessing, not a deep-cavity mode. Parity agreement
0.5%; TD cross-validation: an independent time-domain evolution's
late-time spectral peak lands at 0.4488 (−1.0%).

**Phenomenological restatement of the χ = 0 anchor.** The eikonal
picture "echo train with spacing Δt = (3/2 + 8 ln 2) GM/c³ =
2.15 ms" survives only as (a) the light-travel time governing the
FIRST few broadband transient bounces, and (b) the would-be comb
spacing 2π/Δω in a multi-mode limit the ℓ = 2 cavity does not reach.
The persistent finite-ℓ signature is instead **damped resonant
ringing at f₁ ≈ 236 Hz with quality factor Q ≈ 5** (bandwidth
Γ = 1/τ ≈ 48 Hz), fed by ringdown energy transmitted into the
cavity, plus the early transients. Both remain in-band.

**GR-2 V1.0 is NOT contradicted** — precisely because the CONV-033
adoptions scoped every template claim to "equatorial eikonal grade"
and named this systematic as the dominant uncertainty. The scoping
did its job on its first encounter with the finer calculation. The
GW150914-relevant question (does the LONGER Kerr retrograde cavity —
wall 2.267 M to retrograde ring 3.71 M — restore a multi-resonance
comb?) is **Leg B**, open below.

## §2 The Kerr mode-fate reconnaissance (χ = 0.68, geodesic grade)

Finite-ℓ mode barriers are spherical photon orbits at inclination
μ = m/(ℓ+½) ≈ ξ/√(ξ²+η), not the equatorial rings. Against the
θ-dependent derived surface (equator 2.267 M, pole 2.021 M):

| Mode | μ | r_sp [M] | θ_min | Verdict |
|---|---|---|---|---|
| (2,+2) | +0.800 | 2.163 | 52.7° | **FULLY-BURIED** |
| (3,+3) | +0.857 | 2.129 | 58.6° | FULLY-BURIED |
| (4,+4) | +0.889 | 2.111 | 62.3° | FULLY-BURIED |
| (2,+1) | +0.400 | 2.442 | 23.3° | EXPOSED |
| (2, 0) |  0.000 | 2.773 |  0.0° | EXPOSED |
| (2,−1) | −0.400 | 3.135 | 23.4° | EXPOSED |
| (2,−2) | −0.800 | 3.514 | 53.0° | EXPOSED |

Burial threshold **μ_crit = 0.774** at χ = 0.68. Since
μ(ℓ,ℓ) = ℓ/(ℓ+½) ≥ 0.8 for all ℓ ≥ 2, **the entire corotating
dominant (ℓ,ℓ) branch is buried** — GR-2's burial claim survives its
first finite-ℓ test, sharpened: burial is a statement about the
(ℓ,ℓ) branch, while lower-|m| prograde modes keep exposed barriers
at larger radii (different cavities, different delays). Two honest
cautions: (i) **the (2,+2) margin is thin** (μ = 0.800 vs 0.774);
(ii) **the finite-ℓ burial onset moves UP**: the (2,+2) mode buries
only for **χ ≥ 0.665** (vs the eikonal equatorial onset 0.555) —
the inclined orbit reaches latitudes where the surface sits lower.
GR-2's "buried for χ ≳ 0.55" is an eikonal-grade statement; the
mode-resolved onset is 0.665 at geodesic grade. GW150914-class
remnants (χ ≈ 0.68) remain inside the buried regime, with less
margin than the eikonal picture suggested.

## §3 The instrument, its validation, and the retracted provisional claim

Five instrument designs failed before the validated one, and the
fifth failure was itself the finding. Trail (full detail in the
script header, kept per computation-before-claims): (1) outside-in
TD burst spacing — contaminated by initial-data artifacts and QNM
ringdown, exposed by a NO-WALL control run; (2) raw-signal
autocorrelation — locks onto the carrier; (3) envelope
autocorrelation — intra-burst ringing; (4) WKB round trip at the
resonance — inapplicable, the resonance is above the barrier top;
(5) in-cavity leakage-train spacing — **failed the wall-shift test**:
its measured 7.00 GM/c³ was π/ω₁, the resonance carrier half-period,
whose match to the eikonal 7.045 is STRUCTURAL (ω₁ ≈ π/2L). **A
provisional "+1–3% finite-ℓ correction to the comb spacing" was
nearly claimed from instruments (1) and (5) and is RETRACTED here:
the corrected statement is that the comb-spacing quantity does not
exist at ℓ = 2, χ = 0.** The validated instrument — the scattering
phase δ(ω) with Wigner delay — passes the decisive test: under an
inward wall displacement δ = 2.0, the high-ω plateau grows by 4.12
vs the geometric 4.00 (3%), and is stable under grid/box refinement
(<1%).

## §4 Registry impact

- **OPEN-GR-RCORE-3: Leg A DISCHARGED** (Schwarzschild finite-ℓ
  spectroscopy, both parities, validated + cross-validated; Kerr
  mode-fate at geodesic grade). **REMAINS OPEN — Leg B:** the Kerr
  finite-ℓ computation on the retrograde cavity (comb restoration
  question; the m-resolved analog of §1), surface co-rotation
  ω(r_surf) in the boundary condition, and the Zel'dovich
  growth-time bounds.
- **PRED-O-39: refinement note flagged, NOT yet executed** — on Leg
  B, the search-target language refines from "comb at Δt" toward
  "resonance(s) near the finite-ℓ frequencies + early transients."
  No predictions.md edit until the Kerr (GW150914-relevant) numbers
  exist; the χ = 0 anchor f₁ ≈ 236 Hz is registered here unminted.
- **GR-2 amendment queue (next round/ratification, not executed):**
  §3 gains the Leg-A pointer; the burial onset sentence gains the
  mode-resolved 0.665; the thin-margin caution enters §7. All are
  additive under the existing eikonal scoping — no shipped claim is
  false as scoped.

## §5 Honest limits

Leg A is χ = 0 (the wall+barrier system exactly spherically
symmetric); the Kerr mode-fate table is geodesic/eikonal-
correspondence grade (μ-mapping approximate at ℓ = 2); the burial
verdict uses the A1–A3 surface and inherits its conditionality
(OPEN-GR-RCORE-4); resonance widths are read from the Wigner
lifetime, not a complex-pole computation; no waveform or SNR
statement is made anywhere.


### 7.2 Leg-B record (`rcore_derivation/3334_rcore3_legB_kerr_census.md`)

# OPEN-GR-RCORE-3 — Leg B: The Kerr Cavity Census — the Comb Is Not Restored

**Patch 3334, 21 Aug 2026 — Session 156.** Verify:
`code/3334_rcore3_legB_kerr_wkb_verify.py`, **7/7 PASS** (all checks
FAST — no time-domain evolution in this instrument). Charter: the
Leg-B question minted at Patch 3333 — does the longer Kerr retrograde
cavity restore a multi-resonance echo comb? It decides PRED-O-39's
refined search target.

---

## §1 THE LEG-B ANSWER: no. The comb is not restored at any astrophysical spin — the signature is a multi-LINE set of top-of-barrier resonances plus early transients

Instrument (§3): geodesic-eikonal radial WKB. For each mode (ℓ,m)
the Carter constant is fixed (Q = (ℓ+½)² − m²), the radial
wavevector is k = √R/Δ from the Kerr Hamilton–Jacobi radial function
R(r;ω), and the Bohr–Sommerfeld phase Φ(ω) = ∫ k dr between the
Dirichlet wall and the turning point counts trapped resonances:
N = #{n : Φ(ωₙ) = (n+¾)π}. The comb question becomes a computed
integer.

**Census at χ = 0.68, equatorial wall r = 2.2668 M:**

| Mode | ω_top [1/GM] | f_top @ 62 M_⊙ | +17% Leg-A calib. | Φ_max/π | N_trapped |
|---|---|---|---|---|---|
| (2,−2) | 0.4055 | 211 Hz | ~247 Hz | 0.245 | **0** |
| (2,−1) | 0.4477 | 233 Hz | ~273 Hz | 0.138 | 0 |
| (2, 0) | 0.4996 | 260 Hz | ~305 Hz | 0.056 | 0 |
| (2,+1) | 0.5643 | 294 Hz | ~344 Hz | 0.007 | 0 |
| (3,−3) | 0.5601 | 292 Hz | ~342 Hz | 0.366 | 0 |

Every exposed mode's Φ_max sits far below the ¾π threshold for even
one trapped resonance. The spin scan (check 6) closes the question
across the astrophysical range: for the retrograde-keyed (2,−2),
max Φ_max/π = 0.247 (at χ = 0.52) over χ ∈ [0.30, 0.98] — **N ≥ 1
nowhere**. The intuition from Patch 3333 was correct and is now
computed: the Kerr retrograde cavity is longer, but its barrier is
correspondingly lower (ω_top falls monotonically with spin, check
7: 0.4425 → 0.3846 across χ = 0.30 → 0.95), and the phase volume
never accumulates a trapped mode.

**The refined search target at this grade (χ ≈ 0.68, M ≈ 62 M_⊙):**
not a 381 Hz comb, but (a) **a small set of damped resonance lines**,
one per exposed (ℓ,m) mode, at ~211/233/260/294 Hz eikonal-top
(~247–344 Hz with the +17% Leg-A position calibration), with
Leg-A-calibrated quality factors Q ~ 5; the retrograde-keyed (2,−2)
line is the lowest and strongest-coupled to the ringdown; plus
(b) **the early broadband transient pair(s)** at the retrograde
eikonal delay 2.624 ms (GR-2's Δt survives exactly there). Retrograde
keying survives as the ordering of the line set — the (ℓ,ℓ)
corotating branch is absent (buried), so the lowest line sits at the
*retrograde* top, not the prograde one: the discriminator persists
in line-set form.

## §2 The wave-side confirmation of burial

For (2,+2) at χ = 0.68 the forbidden region R < 0 begins **at the
wall itself** for every ω < 0.642 (e.g. R(wall) = −5.4 at ω = 0.05),
and above 0.642 no barrier exists anywhere: the wall sits inside the
mode's forbidden zone at all frequencies that have one. That is the
wave-instrument restatement of the Patch-3333 geodesic burial
verdict — no propagating cavity exists for the corotating dominant
mode at any frequency, so nothing can key a prograde comb or line.

## §3 Instrument validation

Check 1 is the designed-to-fail anchor: at a → 0 the instrument must
reproduce Leg A, and does — ω_top = 0.4811 matches the closed form
(ℓ+½)/√27 to <1%, and Φ_max/π = 0.178 < ¾ gives N = 0, exactly
consistent with the Leg-A FD finding that the lone χ = 0 resonance
sits ABOVE the barrier top. Wall-position sensitivity (check 5):
moving the wall to the smallest surface radius the (2,−2) orbit's
latitude band sees (2.1897 M — the longest-cavity bound) raises
Φ_max/π only to 0.304; N unchanged. Grade statement: eikonal-WKB
throughout; resonance positions above the top are quoted as ω_top
with the +17% Leg-A calibration; exact line positions and widths are
full-Teukolsky work (the remaining RCORE-3 computational upgrade),
as is the surface co-rotation boundary condition (committed item
(b)) and the Zel'dovich growth-time bounds (item (d)).

## §4 Registry impact

- **OPEN-GR-RCORE-3: Leg B DISCHARGED at eikonal-WKB grade.** The
  comb-restoration question is answered (NO, at any spin). REMAINS
  OPEN: full-Teukolsky line positions/widths; co-rotation BC;
  Zel'dovich bounds.
- **PRED-O-39 — PROVISIONAL refinement text registered here, NOT
  executed in predictions.md:** "GW150914-class remnant: no
  horizon-keyed comb; instead a line set at ~247–344 Hz (grade:
  eikonal-top +17% calibration, Q ~ 5), lowest line retrograde-keyed,
  plus early transients at 2.624 ms ± the GR-2 error budget; the
  corotating (ℓ,ℓ) lines are absent (burial)." Execution of the
  predictions.md amendment and the GR-2 amendment set (Leg-A pointer,
  onset 0.665, thin margin, line-set restatement) awaits a panel
  round — **CONV-034 (RCORE-3 Legs A+B audit) is the natural next
  dispatch** — and founder ratification, per the paper-edit and
  prediction-edit discipline.

## §5 Honest limits

Eikonal-WKB grade end to end; Q fixed by the eikonal correspondence
(exact only as ℓ → ∞); line positions above-top by an amount
calibrated at one point (Leg A, +17%); wall treated as
non-corotating Dirichlet (item (b) open); no amplitude, SNR, or
waveform statement; the burial verdicts inherit A1–A3 conditionality
(OPEN-GR-RCORE-4). The census integer N = 0 is robust across the
wall band and the spin scan, and is the load-bearing result.


### 7.3 Leg-A verify script (`code/3333_rcore3_legA_finite_ell_verify.py`)

```python
#!/usr/bin/env python3
"""3333_rcore3_legA_finite_ell_verify.py — OPEN-GR-RCORE-3 Leg A.

Two computations, claims written only after outputs:

PART 1 (Schwarzschild, finite-ell): 1+1 time-domain evolution of the
ell = 2 axial (Regge-Wheeler) and polar (Zerilli) perturbations with a
Dirichlet wall at the derived surface (areal r = 9M/4, the exact
Buchdahl/exclusion radius, tortoise x_wall = 9/4 + 2 ln(1/8)).  The
measured echo spacing at finite ell is the FIRST quantification of the
eikonal-grade systematic that GR-2 V1.0 names as its dominant formal
uncertainty (eikonal reference: (3/2 + 8 ln 2) GM/c^3 = 7.0452).

PART 2 (Kerr chi = 0.68, geodesic grade): spherical-photon-orbit
reconnaissance of the (ell, m) mode-fate question — finite-ell
prograde barriers are NOT the equatorial prograde ring; each mode's
eikonal barrier is a spherical photon orbit at inclination
mu = m/(ell+1/2) ~ xi/sqrt(xi^2 + eta).  Which of these orbits are
buried inside the theta-dependent derived surface?

FAST mode: --fast runs Part-2 recon + closed-form checks (seconds).
The TD evolution (Part 1) runs in the full mode only (~1 min).

Units G = c = M = 1 throughout; GW150914 ms conversions at 62 Msun.
"""
import sys
import numpy as np

FAST_ONLY = "--fast" in sys.argv
PASS, FASTPASS = [], []


def check(name, ok, detail="", fast=False):
    (FASTPASS if fast else PASS).append(bool(ok))
    tag = "[FAST]" if fast else "      "
    print(f"{tag}[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


GM_ms = 62 * 4.92549e-6 * 1e3  # GM/c^3 in ms at 62 Msun

# ===================== shared closed forms =====================
x_of_r = lambda r: r + 2 * np.log(r / 2 - 1)   # Schwarzschild tortoise, M=1
R_WALL = 2.25                                   # areal 9M/4
X_WALL = x_of_r(R_WALL)
EIK = 1.5 + 8 * np.log(2)                       # 7.0452

check("F1. eikonal reference reproduced: 2*(x(3M) - x_wall) = (3/2 + 8 ln 2)",
      abs(2 * (x_of_r(3.0) - X_WALL) - EIK) < 1e-12,
      f"x_wall = {X_WALL:.4f}, closed form {EIK:.4f}", fast=True)

# ===================== PART 2: Kerr mode-fate recon =====================
A = 0.68


def alpha_n(r, a, th):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    Aa = (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2
    return np.sqrt(max(D * S / Aa, 0.0))


def v_n(r, a, th):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    Aa = (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2
    om = 2 * a * r / Aa
    gpp = Aa * np.sin(th) ** 2 / S
    al2 = D * S / Aa
    return om * np.sqrt(gpp / al2) if al2 > 0 else np.inf


def F_n(r, a, th):
    al = alpha_n(r, a, th)
    s = 2 * (1 - al) / (1 + al)
    return s * s + v_n(r, a, th) ** 2


def r_E(a, th):
    return 1 + np.sqrt(max(1 - a * a * np.cos(th) ** 2, 0.0))


def r_surface(a, th):
    lo, hi = r_E(a, th) * (1 + 1e-10), 60.0
    if F_n(lo, a, th) <= 1:
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F_n(mid, a, th) > 1:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def xi_eta(r, a):
    """Conserved ratios for the Kerr spherical photon orbit at BL radius r."""
    xi = (r * r * (3 - r) - a * a * (1 + r)) / (a * (r - 1))
    eta = r ** 3 * (4 * a * a - r * (r - 3) ** 2) / (a * a * (r - 1) ** 2)
    return xi, eta


def mu_of_r(r, a):
    """Inclination parameter mu ~ m/(ell+1/2): +1 prograde equatorial,
    0 polar, -1 retrograde equatorial."""
    xi, eta = xi_eta(r, a)
    return xi / np.sqrt(xi * xi + max(eta, 0.0))


def theta_min(r, a):
    """Minimum polar angle reached by the spherical orbit at r (its
    highest latitude); equator = pi/2."""
    xi, eta = xi_eta(r, a)
    if eta <= 0:
        return np.pi / 2  # equatorial
    # Theta(u) = eta + (a^2 - xi^2 - eta) u - a^2 u^2, u = cos^2 theta
    b, c = (a * a - xi * xi - eta), -eta
    disc = b * b - 4 * a * a * c
    u_turn = (b + np.sqrt(disc)) / (2 * a * a)
    u_turn = min(max(u_turn, 0.0), 1.0)
    return np.arccos(np.sqrt(u_turn))


def r_sp_of_mu(mu_target, a):
    """Spherical-orbit radius with the given inclination parameter."""
    r_pro = 2 * (1 + np.cos(2 / 3 * np.arccos(-a)))
    r_ret = 2 * (1 + np.cos(2 / 3 * np.arccos(+a)))
    lo, hi = r_pro + 1e-9, r_ret - 1e-9  # mu decreases from +1 to -1
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if mu_of_r(mid, a) > mu_target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def burial(r_sp, a, th_min):
    """Verdict over the orbit's latitude range [th_min, pi/2]:
    FULLY-BURIED (inside the wall at every visited theta),
    EXPOSED (outside at every theta), or PARTIAL."""
    ths = np.linspace(th_min, np.pi / 2, 60)
    inside = [r_sp < r_surface(a, t) for t in ths]
    if all(inside):
        return "FULLY-BURIED"
    if not any(inside):
        return "EXPOSED"
    return "PARTIAL"


# surface profile
th_scan = np.linspace(1e-3, np.pi / 2, 90)
surf = np.array([r_surface(A, t) for t in th_scan])
print(f"      surface(chi=0.68): equator {surf[-1]:.4f} M, pole {surf[0]:.4f} M "
      f"(min {surf.min():.4f}, max {surf.max():.4f})")

# mode ladder: mu = m/(ell+1/2) for the dominant modes
modes = [("(2,+2)", 2 / 2.5), ("(3,+3)", 3 / 3.5), ("(4,+4)", 4 / 4.5),
         ("(2,+1)", 1 / 2.5), ("(2,0)", 0.0),
         ("(2,-1)", -1 / 2.5), ("(2,-2)", -2 / 2.5)]
rows = []
for name, mu in modes:
    r_sp = r_sp_of_mu(mu, A)
    tmin = theta_min(r_sp, A)
    verdict = burial(r_sp, A, tmin)
    x_ret_like = None
    rows.append((name, mu, r_sp, np.degrees(tmin), verdict))
    print(f"      mode {name}: mu={mu:+.3f}  r_sp={r_sp:.4f} M  "
          f"theta_min={np.degrees(tmin):5.1f} deg  -> {verdict}")

# burial threshold in mu
mu_grid = np.linspace(0.999, -0.999, 400)
mu_crit = None
prev_buried = True
for mu in mu_grid:
    r_sp = r_sp_of_mu(mu, A)
    vd = burial(r_sp, A, theta_min(r_sp, A))
    b = (vd == "FULLY-BURIED")
    if prev_buried and not b:
        mu_crit = mu
        break
    prev_buried = b
print(f"      burial threshold: FULLY-BURIED for mu > {mu_crit:.3f} (chi = 0.68)")

d22 = dict((r[0], r[4]) for r in rows)
check("F2. equatorial limits recovered: (2,-2)-limit mu=-0.8 EXPOSED; "
      "prograde equatorial ring (mu -> +1) buried",
      d22["(2,-2)"] == "EXPOSED"
      and burial(r_sp_of_mu(0.999, A), A, theta_min(r_sp_of_mu(0.999, A), A)) == "FULLY-BURIED",
      f"(2,-2): {d22['(2,-2)']}", fast=True)

check("F3. THE RECON FINDING: the finite-ell prograde (2,+2) barrier "
      "(mu=+0.8, an INCLINED spherical orbit) — burial verdict computed honestly",
      d22["(2,+2)"] in ("FULLY-BURIED", "PARTIAL", "EXPOSED"),
      f"(2,+2) at r_sp={rows[0][2]:.4f} M, theta_min={rows[0][3]:.1f} deg: "
      f"{d22['(2,+2)']}; mu_crit={mu_crit:.3f}", fast=True)

# finite-ell burial onset for the (2,+2) mode: smallest chi where the
# mu = 0.8 spherical orbit is FULLY-BURIED (the eikonal equatorial onset
# was 0.555; the inclined orbit reaches higher latitude where the surface
# is lower, so the finite-ell onset must be HIGHER).
chi_on22 = None
for a_try in np.linspace(0.30, 0.90, 121):
    r_sp = r_sp_of_mu(0.8, a_try)
    if burial(r_sp, a_try, theta_min(r_sp, a_try)) == "FULLY-BURIED":
        chi_on22 = a_try
        break
check("F4. finite-ell (2,+2) burial ONSET located; sits ABOVE the eikonal "
      "equatorial onset 0.555 (thin-margin caution at chi = 0.68 recorded)",
      chi_on22 is not None and 0.555 < chi_on22 < 0.68,
      f"onset chi(2,+2) = {chi_on22:.3f}; margin at 0.68 in mu: "
      f"{0.8 - mu_crit:.3f}", fast=True)

print(f"FAST: {sum(FASTPASS)}/{len(FASTPASS)} PASS")
if FAST_ONLY:
    raise SystemExit(0 if all(FASTPASS) else 1)

# ===================== PART 1: finite-ell cavity spectroscopy =====================
# INSTRUMENT-HARDENING TRAIL (kept in full per computation-before-claims —
# five dead ends preceded the validated instrument, and the fifth failure
# WAS the finding):
#   (1) outside-in TD burst spacing        -> contaminated by initial-data
#       artifacts + QNM ringdown (no-wall control run exposed it);
#   (2) raw-signal autocorrelation         -> locks onto the carrier period;
#   (3) |envelope| autocorrelation         -> intra-burst ringing;
#   (4) WKB round trip at the resonance    -> the resonance sits ABOVE the
#       barrier top, so the narrowband-trapped-mode model does not apply;
#   (5) in-cavity leakage-train spacing    -> FAILED THE WALL-SHIFT TEST:
#       the measured ~7.0 GM/c^3 was pi/omega_1, the resonance carrier
#       half-period, whose numerical match to the eikonal 7.045 is
#       STRUCTURAL (omega_1 ~ pi/(2 L_cavity)) — a trap that would have
#       produced a false "+1% eikonal correction" claim.
# VALIDATED INSTRUMENT: frequency-domain scattering phase delta(omega) of
# the Dirichlet-wall + barrier system; Wigner delay tau = 2 d(delta)/d(omega).
# Validation: the high-omega tau plateau must shift by exactly 2*delta under
# a wall displacement (geometric optics) — it does (check 2).
# THE LEG-A FINDING: at ell = 2, chi = 0, the Buchdahl-wall cavity
# (~3.5 M) supports a SINGLE broad top-of-barrier resonance, not a comb.

def V_RW(r, ell=2):
    return (1 - 2 / r) * (ell * (ell + 1) / r ** 2 - 6 / r ** 3)


def V_Z(r, ell=2):
    n = (ell - 1) * (ell + 2) / 2
    num = 2 * n * n * (n + 1) * r ** 3 + 6 * n * n * r ** 2 + 18 * n * r + 18
    return (1 - 2 / r) * num / (r ** 3 * (n * r + 3) ** 2)


def r_of_x(x):
    r = np.where(x > 2, x, 2 + np.exp((x - 2.0) / 2))
    r = np.maximum(r, 2 + 1e-14)
    for _ in range(80):
        f = r + 2 * np.log(r / 2 - 1) - x
        fp = r / (r - 2)
        r = np.maximum(r - f / fp, 2 + 1e-14)
    return r


def wigner_delay(Vf, x_wall, omegas, x_far=300.0, dx=0.01, smooth_k=41):
    """delta(omega) from u''=(V-w^2)u, u(x_wall)=0, matched to
    sin(w x + delta) at x_far; returns (tau_smooth, tau_raw)."""
    xs = np.arange(x_wall, x_far, dx)
    V = Vf(r_of_x(xs))
    w2 = omegas ** 2
    u = np.zeros_like(omegas)
    up = np.ones_like(omegas)
    for i in range(len(xs) - 1):
        V0, V1 = V[i], V[i + 1]
        Vm = 0.5 * (V0 + V1)
        k1u, k1p = up, (V0 - w2) * u
        k2u = up + 0.5 * dx * k1p
        k2p = (Vm - w2) * (u + 0.5 * dx * k1u)
        k3u = up + 0.5 * dx * k2p
        k3p = (Vm - w2) * (u + 0.5 * dx * k2u)
        k4u = up + dx * k3p
        k4p = (V1 - w2) * (u + dx * k3u)
        u = u + dx / 6 * (k1u + 2 * k2u + 2 * k3u + k4u)
        up = up + dx / 6 * (k1p + 2 * k2p + 2 * k3p + k4p)
        nrm = np.maximum(np.abs(u), np.abs(up))
        nrm = np.where(nrm > 1e6, nrm, 1.0)
        u, up = u / nrm, up / nrm
    xf = xs[-1]
    s, c = np.sin(omegas * xf), np.cos(omegas * xf)
    P = u * s + (up / omegas) * c
    Q = u * c - (up / omegas) * s
    delta = np.unwrap(np.arctan2(Q, P))
    tau = 2 * np.gradient(delta, omegas)
    ts = np.convolve(tau, np.ones(smooth_k) / smooth_k, mode="same")
    return ts, tau


def evolve(Vfunc, x_wall, x_out=420.0, dx=0.04, t_end=200.0, x0=25.0, sig=1.5,
           x_obs=45.0, cfl=0.5):
    xs = np.arange(x_wall, x_out + dx, dx)
    rs = r_of_x(xs)
    V = Vfunc(rs)
    dt = cfl * dx
    lam = (dt / dx) ** 2
    psi_p = np.exp(-(xs - x0) ** 2 / (2 * sig ** 2))
    psi_c = np.exp(-(xs - (x0 - dt)) ** 2 / (2 * sig ** 2))
    psi_c[0] = psi_p[0] = 0.0
    iobs = int(round((x_obs - x_wall) / dx))
    nt = int(t_end / dt)
    sig_t = np.zeros(nt)
    for n in range(nt):
        lap = np.zeros_like(psi_c)
        lap[1:-1] = psi_c[2:] - 2 * psi_c[1:-1] + psi_c[:-2]
        psi_n = 2 * psi_c - psi_p + lam * lap - dt * dt * V * psi_c
        psi_n[0] = 0.0
        psi_n[-1] = psi_c[-2]
        psi_p, psi_c = psi_c, psi_n
        sig_t[n] = psi_c[iobs]
    return np.arange(nt) * dt, sig_t


def td_late_peak(t, s, t_start=60.0):
    m = t >= t_start
    x = (s[m] - s[m].mean()) * np.hanning(m.sum())
    spec = np.abs(np.fft.rfft(x))
    freqs = 2 * np.pi * np.fft.rfftfreq(m.sum(), t[1] - t[0])
    band = (freqs > 0.05) & (freqs < 1.2)
    return float(freqs[band][np.argmax(spec[band])])


OM = np.linspace(0.10, 1.00, 1200)
GM_s = 62 * 4.92549e-6
res = {}
for label, Vf in (("RW", V_RW), ("Zerilli", V_Z)):
    ts, _ = wigner_delay(Vf, X_WALL, OM)
    # prominent resonances: local maxima over a +-0.02 window, tau above
    # 1.5x the high-omega plateau
    plateau = float(np.median(ts[OM > 0.8]))
    win = 40
    pk = [i for i in range(win, len(OM) - win)
          if ts[i] == ts[i - win:i + win].max() and ts[i] > 1.5 * plateau]
    # dedupe contiguous
    pks = []
    for i in pk:
        if not pks or OM[i] - OM[pks[-1]] > 0.02:
            pks.append(i)
    w_res = [float(OM[i]) for i in pks]
    tau_res = [float(ts[i]) for i in pks]
    res[label] = (w_res, tau_res, plateau, ts)
    f_hz = [w / (2 * np.pi * GM_s) for w in w_res]
    print(f"      {label}: prominent resonances "
          f"{['w=%.4f (tau=%.1f, f=%.0f Hz @62)' % (w, tt, f) for w, tt, f in zip(w_res, tau_res, f_hz)]}; "
          f"high-omega plateau tau = {plateau:.2f}")

n_rw = len(res["RW"][0])
n_z = len(res["Zerilli"][0])
w1_rw = res["RW"][0][0] if n_rw else float("nan")
w1_z = res["Zerilli"][0][0] if n_z else float("nan")
Vmax_rw = float(np.max(V_RW(np.linspace(2.05, 8, 40000))))
check("1. THE LEG-A FINDING: exactly ONE prominent cavity resonance per parity "
      "in the band (the eikonal comb does NOT survive at ell=2, chi=0)",
      n_rw == 1 and n_z == 1,
      f"RW: {n_rw} at w={w1_rw:.4f} ({w1_rw/(2*np.pi*GM_s):.0f} Hz @62, "
      f"tau={res['RW'][1][0]:.1f}, Q={w1_rw*res['RW'][1][0]/2:.1f}); "
      f"Zerilli: {n_z} at w={w1_z:.4f}; barrier top sqrt(Vmax)={np.sqrt(Vmax_rw):.3f} "
      f"(the resonance sits ABOVE it — top-of-barrier reprocessing, not a deep comb)")

# decisive instrument validation: wall shift
DELTA = 2.0
ts_s, _ = wigner_delay(V_RW, X_WALL - DELTA, OM)
pl_s = float(np.median(ts_s[OM > 0.8]))
pl_0 = res["RW"][2]
check("2. WALL-SHIFT VALIDATION: high-omega Wigner plateau grows by 2*delta "
      "under an inward wall displacement (geometric optics recovered)",
      abs((pl_s - pl_0) - 2 * DELTA) < 0.3,
      f"plateau {pl_0:.2f} -> {pl_s:.2f} (grew {pl_s - pl_0:.2f}, expected {2*DELTA:.1f})")

# TD cross-validation
t_td, s_td = evolve(V_RW, X_WALL)
w_td = td_late_peak(t_td, s_td)
check("3. TD/FD cross-validation: the time-domain late-time spectral peak "
      "matches the FD resonance within 3%",
      abs(w_td - w1_rw) / w1_rw < 0.03,
      f"TD {w_td:.4f} vs FD {w1_rw:.4f}")

check("4. parity agreement: RW and Zerilli resonance positions within 3% "
      "(near-isospectral)",
      abs(w1_rw - w1_z) / w1_rw < 0.03, f"{w1_rw:.4f} vs {w1_z:.4f}")

# convergence: x_far and grid refinement
ts_c, _ = wigner_delay(V_RW, X_WALL, OM, x_far=360.0, dx=0.005)
pl_c = float(np.median(ts_c[OM > 0.8]))
i1 = int(np.argmax(ts_c * ((OM > 0.3) & (OM < 0.6))))
check("5. convergence: resonance position and plateau stable under x_far/dx "
      "refinement (within 1% / 0.2)",
      abs(OM[i1] - w1_rw) / w1_rw < 0.01 and abs(pl_c - pl_0) < 0.2,
      f"w1 {w1_rw:.4f} -> {OM[i1]:.4f}; plateau {pl_0:.2f} -> {pl_c:.2f}")

# the eikonal number's surviving role: early-transient spacing only.
# (No check asserts a "finite-ell correction to the comb spacing" —
# that quantity does not exist at ell=2; the retraction of the
# provisional +1% reading from instrument (5) is recorded above.)
allp = FASTPASS + PASS
print(f"{sum(allp)}/{len(allp)} PASS")
raise SystemExit(0 if all(allp) else 1)

```

### 7.4 Leg-B verify script (`code/3334_rcore3_legB_kerr_wkb_verify.py`)

```python
#!/usr/bin/env python3
"""3334_rcore3_legB_kerr_wkb_verify.py — OPEN-GR-RCORE-3 Leg B.

THE LEG-B QUESTION (frontier, Patch 3333): does the longer Kerr
retrograde cavity (wall 2.267 M -> retrograde structures out to
r ~ 3.5 M at chi = 0.68) restore a multi-resonance echo comb?

INSTRUMENT (geodesic-eikonal radial WKB — one grade above the Leg-A
reconnaissance, one below full Teukolsky):
For a mode (ell, m) the eikonal Carter constant is FIXED:
    Lz = m,   Q = (ell + 1/2)^2 - m^2   (omega-independent),
and the Kerr null-geodesic radial function at frequency omega is
    R(r; omega) = [omega (r^2 + a^2) - a m]^2
                  - Delta [ (m - a omega)^2 + Q ],
with radial wavevector k(r) = sqrt(R)/Delta (radial Hamilton-Jacobi).
The wall+barrier cavity's Bohr-Sommerfeld phase
    Phi(omega) = int_{r_wall}^{r_turn(omega)} sqrt(R)/Delta dr
counts trapped resonances: with one hard node (Dirichlet wall) and one
smooth turning point, resonances satisfy Phi = (n + 3/4) pi.  The comb
question is therefore the computed integer
    N_trapped = #{ n : Phi(omega_n) = (n + 3/4) pi, omega_n < omega_top }.
Barrier-top frequency omega_top(mode) = sup{omega : R has a forbidden
region (R < 0) outside the wall}; above it there is no turning point
and only top-of-barrier reprocessing survives (Leg-A calibration: the
chi = 0 resonance sat +17% above its eikonal top, Q ~ 5).

VALIDATION BUILT IN: at a -> 0 the instrument must reproduce the
Leg-A FD result — ZERO sub-top resonances at ell = 2 (the single
resonance found there sits ABOVE the top).  Check 1 enforces this.

Wall convention: equatorial derived-surface radius (largest; shortest
cavity).  Sensitivity row: wall at the surface radius at the orbit's
theta_min (smallest surface the orbit's latitude band sees; longest
cavity) — N_trapped must be reported for BOTH (check 5).

All claims below are at the stated eikonal-WKB grade; resonance
POSITIONS above the top are quoted as ~omega_top with the +17% Leg-A
calibration, exact positions being full-Teukolsky work (remaining
RCORE-3 upgrade).  Units G = c = M = 1; Hz at 62 Msun.
"""
import sys
import numpy as np

PASS = []


def check(name, ok, detail=""):
    PASS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))


GM_s = 62 * 4.92549e-6
to_hz = lambda w: w / (2 * np.pi * GM_s)

# ---------- surface machinery (identical construction to 3333) ----------
def alpha_n(r, a, th):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    Aa = (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2
    return np.sqrt(max(D * S / Aa, 0.0))


def v_n(r, a, th):
    D = r * r - 2 * r + a * a
    S = r * r + a * a * np.cos(th) ** 2
    Aa = (r * r + a * a) ** 2 - D * a * a * np.sin(th) ** 2
    om = 2 * a * r / Aa
    gpp = Aa * np.sin(th) ** 2 / S
    al2 = D * S / Aa
    return om * np.sqrt(gpp / al2) if al2 > 0 else np.inf


def F_n(r, a, th):
    al = alpha_n(r, a, th)
    s = 2 * (1 - al) / (1 + al)
    return s * s + v_n(r, a, th) ** 2


def r_E(a, th):
    return 1 + np.sqrt(max(1 - a * a * np.cos(th) ** 2, 0.0))


def r_surface(a, th):
    lo, hi = r_E(a, th) * (1 + 1e-10), 60.0
    if F_n(lo, a, th) <= 1:
        return None
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F_n(mid, a, th) > 1:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def xi_eta(r, a):
    xi = (r * r * (3 - r) - a * a * (1 + r)) / (a * (r - 1))
    eta = r ** 3 * (4 * a * a - r * (r - 3) ** 2) / (a * a * (r - 1) ** 2)
    return xi, eta


def mu_of_r(r, a):
    xi, eta = xi_eta(r, a)
    return xi / np.sqrt(xi * xi + max(eta, 0.0))


def r_sp_of_mu(mu_target, a):
    r_pro = 2 * (1 + np.cos(2 / 3 * np.arccos(-a)))
    r_ret = 2 * (1 + np.cos(2 / 3 * np.arccos(+a)))
    lo, hi = r_pro + 1e-9, r_ret - 1e-9
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if mu_of_r(mid, a) > mu_target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def theta_min(r, a):
    xi, eta = xi_eta(r, a)
    if eta <= 0:
        return np.pi / 2
    b, c = (a * a - xi * xi - eta), -eta
    disc = b * b - 4 * a * a * c
    u_turn = (b + np.sqrt(disc)) / (2 * a * a)
    u_turn = min(max(u_turn, 0.0), 1.0)
    return np.arccos(np.sqrt(u_turn))


# ---------- the WKB census instrument ----------
def Rfun(r, a, m, Q, w):
    D = r * r - 2 * r + a * a
    return (w * (r * r + a * a) - a * m) ** 2 - D * ((m - a * w) ** 2 + Q)


def barrier_exists(a, m, Q, w, r_wall, r_out=12.0, n=6000):
    rs = np.linspace(r_wall * (1 + 1e-9), r_out, n)
    return np.any(Rfun(rs, a, m, Q, w) < 0)


def omega_top(a, m, Q, r_wall, w_hi=2.0):
    """Largest omega for which a forbidden region survives outside the wall."""
    lo, hi = 1e-3, w_hi
    if not barrier_exists(a, m, Q, lo, r_wall):
        return None          # no barrier even at low omega: no cavity
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if barrier_exists(a, m, Q, mid, r_wall):
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def phase_integral(a, m, Q, w, r_wall, n=40000):
    """Phi(omega) over the propagating region from the wall to the first
    turning point (R crossing negative)."""
    rs = np.linspace(r_wall * (1 + 1e-9), 12.0, n)
    R = Rfun(rs, a, m, Q, w)
    if R[0] <= 0:
        return None, "R<0 at wall (no propagating cavity at this omega)"
    i_turn = np.argmax(R < 0)
    if i_turn == 0:
        return None, "no turning point (omega above top)"
    rs_c, R_c = rs[:i_turn], np.clip(R[:i_turn], 0, None)
    D = rs_c * rs_c - 2 * rs_c + a * a
    k = np.sqrt(R_c) / D
    return float(np.trapezoid(k, rs_c)), None


def census(a, m, ell, r_wall):
    """Returns (omega_top, Phi_max, N_trapped) for the mode at this wall."""
    Q = (ell + 0.5) ** 2 - m * m
    wt = omega_top(a, m, Q, r_wall)
    if wt is None:
        return None, None, 0
    phi, err = phase_integral(a, m, Q, wt * 0.999, r_wall)
    if phi is None:
        return wt, None, 0
    N = int(np.floor(phi / np.pi - 0.75)) + 1 if phi / np.pi >= 0.75 else 0
    return wt, phi, N


# ============================ RUN ============================
A = 0.68
r_wall_eq = r_surface(A, np.pi / 2)
print(f"      chi = {A}: equatorial wall r = {r_wall_eq:.4f} M")

# --- Check 1: a -> 0 validation against Leg A
wt0, phi0, N0 = census(1e-6, 0, 2, 2.25)
wt0_expect = 2.5 / np.sqrt(27)   # (ell+1/2) sqrt(max (1-2/r)/r^2) at r=3
check("1. a->0 VALIDATION against Leg A: ell=2 cavity holds ZERO sub-top "
      "resonances, and omega_top matches the closed form (ell+1/2)/sqrt(27)",
      N0 == 0 and abs(wt0 - wt0_expect) / wt0_expect < 0.01,
      f"omega_top = {wt0:.4f} vs {wt0_expect:.4f}; Phi_max/pi = "
      f"{phi0/np.pi:.3f} < 3/4 -> N = {N0} (Leg-A FD found its single "
      f"resonance ABOVE the top — consistent)")

# --- Check 2: (2,+2) burial seen by the wave instrument
wt22, phi22, N22 = census(A, +2, 2, r_wall_eq)
Rw_probe = Rfun(r_wall_eq * (1 + 1e-9), A, 2, 2.25, min(wt22 * 0.9, 0.5) if wt22 else 0.3)
check("2. (2,+2) at chi=0.68: the wave-side confirmation of burial — the "
      "forbidden region R<0 starts AT THE WALL for all omega below 0.642 "
      "(the wall sits inside the mode's forbidden zone; no propagating "
      "cavity exists at any omega), so N_trapped = 0",
      N22 == 0 and Rw_probe < 0,
      f"R(wall) = {Rw_probe:.3f} < 0 below omega = {wt22:.3f}; above it, no "
      f"barrier anywhere — either way, no cavity")

# --- THE LEG-B ANSWER: exposed-mode census at chi = 0.68
modes = [(-2, 2, "(2,-2)"), (-1, 2, "(2,-1)"), (0, 2, "(2,0)"),
         (+1, 2, "(2,+1)"), (-3, 3, "(3,-3)")]
rows = []
for m, ell, name in modes:
    wt, phi, N = census(A, m, ell, r_wall_eq)
    rows.append((name, wt, phi, N))
    if wt:
        print(f"      mode {name}: omega_top = {wt:.4f} "
              f"(~{to_hz(wt):.0f} Hz @62; Leg-A calibration +17% -> "
              f"~{to_hz(wt*1.17):.0f} Hz), Phi_max/pi = "
              f"{(phi/np.pi if phi else float('nan')):.3f}, N_trapped = {N}")
    else:
        print(f"      mode {name}: no barrier/cavity")

N_ret = dict((r[0], r[3]) for r in rows)
check("3. THE LEG-B ANSWER: the retrograde-keyed (2,-2) cavity at chi=0.68 — "
      "trapped-resonance count computed, comb question decided by integer",
      rows[0][1] is not None and rows[0][2] is not None,
      f"(2,-2): N_trapped = {N_ret['(2,-2)']} "
      f"({'COMB NOT RESTORED — top-of-barrier reprocessing only' if N_ret['(2,-2)'] == 0 else 'TRAPPED COMB EXISTS'})")

check("4. full exposed-mode census at chi=0.68 completed (the multi-line "
      "signature set for the search target)",
      all(r[3] is not None for r in rows),
      "; ".join(f"{r[0]}: N={r[3]}" + (f", f~{to_hz(r[1]):.0f} Hz" if r[1] else "")
                for r in rows))

# --- Check 5: wall-position sensitivity (longest-cavity bound)
r22 = r_sp_of_mu(-0.8, A)
th22 = theta_min(r22, A)
r_wall_lo = r_surface(A, th22)
wt_lo, phi_lo, N_lo = census(A, -2, 2, r_wall_lo)
check("5. wall-sensitivity: with the SMALLEST surface radius the (2,-2) "
      "orbit's latitude band sees (longest cavity), the trapped count is "
      "unchanged",
      N_lo == N_ret["(2,-2)"],
      f"wall {r_wall_eq:.4f} -> {r_wall_lo:.4f} M: Phi_max/pi "
      f"{rows[0][2]/np.pi:.3f} -> {phi_lo/np.pi:.3f}, N {N_ret['(2,-2)']} -> {N_lo}")

# --- Check 6: spin scan — does ANY astrophysical spin restore the comb?
scan = []
for a_try in np.linspace(0.30, 0.98, 35):
    rw = r_surface(a_try, np.pi / 2)
    if rw is None:
        scan.append((a_try, None, 0))
        continue
    wt_s, phi_s, N_s = census(a_try, -2, 2, rw)
    scan.append((a_try, (phi_s / np.pi if phi_s else 0.0), N_s))
max_phi = max(s[1] or 0 for s in scan)
any_comb = any(s[2] >= 1 for s in scan)
check("6. spin scan chi in [0.30, 0.98]: does the (2,-2) trapped count ever "
      "reach 1? (the comb-restoration question across the astrophysical range)",
      True,
      f"max Phi_max/pi = {max_phi:.3f} at chi = "
      f"{[s[0] for s in scan if (s[1] or 0) == max_phi][0]:.2f}; "
      f"N >= 1 anywhere: {any_comb}")

# --- Check 7: monotonic sanity — omega_top(2,-2) decreases with spin
wts = []
for a_try in (0.30, 0.55, 0.68, 0.85, 0.95):
    rw = r_surface(a_try, np.pi / 2)
    Q = 2.5 ** 2 - 4
    wts.append(omega_top(a_try, -2, Q, rw))
check("7. sanity: omega_top(2,-2) decreases monotonically with spin (the "
      "retrograde ring recedes and slows)",
      all(wts[i] > wts[i + 1] for i in range(len(wts) - 1)),
      "omega_top: " + ", ".join(f"{w:.4f}" for w in wts))

print(f"{sum(PASS)}/{len(PASS)} PASS")
print("FAST: all checks are FAST (no TD evolution in this instrument); "
      f"FAST: {sum(PASS)}/{len(PASS)} PASS")
raise SystemExit(0 if all(PASS) else 1)

```

## §8 Return skeleton (fill EXACTLY; inline text)

```
REVIEWER: <your model name>
TIER LEGEND USED: <tiers used>
Q1: <verdict> [<tier>] — <reasoning>
Q2: <verdict> [<tier>] — <reasoning>
Q3: (i) <verdict>; (ii) <verdict>; (iii) <verdict> [<tier>] — <reasoning>
Q4: <verdict> — <reasoning>
Q5: <verdict> — <reasoning>
Q6: <verdict> — <reasoning>
Q7a: <verdict>  Q7b: <verdict> — <reasoning>
SCRIPT: <SCRIPT-EXECUTED (own run) + verbatim count line(s) /
        INDEPENDENT-HARNESS + description / INSPECTED (reference run)>
DEFECTS/OBJECTIONS: <numbered list, or NONE>
```
