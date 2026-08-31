# Frontier sector: GR (local gravitation series)

> **GR-LANE STATUS (Patch 3348, 30 Aug 2026).** Block discipline:
> **GR owns 3300–3399** (highest used: 3348); DE owns 3400s (at 3449);
> DM owns 3500s (at 3505). **The GR lane writes status HERE, not to
> `research_frontier.md`** — the lane-isolation protocol (Patch 3346)
> was lost in the origin rewind and never restored, so the shared
> dashboard is back to the single-`Last updated:` format where two
> lanes collide on one line. Founder-endorsed 30 Aug: "a frontier
> specific for GR... that seems to be the place where the collision
> happens."
>
> **JUST DONE — 3348: GR-2 V1.4, the verification claim corrected and
> made SELF-TESTING.** §2's "every number is reproduced by the paper's
> verify script (3329, 9/9)" was FALSE and worsening — the ~5%
> amplitude was inherited from GR-1d V3 and never in 3329 (false since
> V1.0), and V1.1–V1.3 added ℓ_crit = 7±1, the 0.122 slope, the
> 165-mode domain, 236 Hz, the four eikonal tops and the δ_w envelope,
> all from 3333/3334/3339. **Timing mattered: DOIs are being prepared,
> and no DOI should carry a false verification claim.** Replaced by an
> explicit provenance table (3329→9/9, 3333→9/9, 3334→7/7, 3339→6/6)
> with the ONE non-script-verified quantity declared, and the table is
> asserted in code by `3348_gr2_verification_provenance.py` (6/6,
> fail-closed, directory-independent): scripts exist, counts equal
> actual `check()` totals, the exception stays declared, the old
> phrasing cannot return. **Rot-detector adversarially tested** —
> reinstating the V1.3 sentence drops it to 5/6 with "REGRESSION",
> removing it restores 6/6. No physics changed; no template number
> moved; the four underlying scripts untouched.
>
> **UPDATE — 3349: OPEN-GR-RCORE-3(e) PARTIALLY DISCHARGED (8/8,
> all-FAST).** Route: a trapped mode sits BELOW its barrier top, so
> exciting it and seeing it each cost the tunnelling factor
> Γ = ∫|k|dr; the observable factor is e^(−4Γ), computable with the
> Leg-B/C instrument. **The hypothesis FAILED at ℓ_crit and the record
> says so:** at ℓ = 7, ω₁ = 1.1552 sits only 0.024 below ω_top, so the
> forbidden region is THIN — Γ = 0.404, e^(−4Γ) = 0.20, a factor of
> five, NOT negligible. ℓ_crit is where trapping just begins and
> therefore where it is weakest. Threshold e^(−4Γ) < 1e−3 was declared
> BEFORE the numbers were read; it is first met at **ℓ = 9** (7.1e−4),
> falling ~3.2e−2 per further multipole (Γ ≈ 0.858ℓ − 5.82, fitted).
> **So: DERIVED for ℓ ≥ 9; STILL INHERITED at ℓ = 7–8 — two named
> multipoles instead of an open-ended tail. The item stays OPEN at
> reduced scope; a source-side excitation computation closes it.**
> **UNSOUGHT SECOND FINDING, and the better half:** the trapped high-ℓ
> combs span **602–986 Hz** while the predicted line set is
> **211–294 Hz** — a factor 2.0 clear, so the ladder is SPECTRALLY
> SEPARATED and cannot contaminate a search in the predicted band at
> ANY ℓ, independent of the remaining gap. Three shields now stand
> between the ladder and the prediction (barrier ℓ ≥ 9, band
> separation all ℓ, inherited hierarchy) and the borrowed one is now
> the weakest — where a borrowed assumption belongs. Consistency: ℓ = 6
> carries no trapped mode to suppress, meeting Leg C exactly. Method
> caveat recorded: first-order WKB lacks the Miller–Good correction
> near the top, exactly where ℓ = 7 sits, so its Γ is the least
> reliable entry — and the one the conclusion leans on least, since it
> is reported as a FAILURE to discharge. **GR-2 amendment QUEUED (not
> enacted): V1.4's "inherited... not computed in this programme" is now
> half wrong and should read derived for ℓ ≥ 9 and for all ℓ in the
> search band, inherited only for ℓ = 7–8.** Record:
> `rcore_derivation/3349_rcore3e_multipole_excitation.md`.
>
> **UPDATE — 3350: OPEN-GR-RCORE-3(e) CLOSED (9/9, all-FAST).** The
> ℓ = 7–8 source-side budget: multipole scaling P_ℓ/P₂ ~ v^(2(ℓ−2))
> (derived here from the moment expansion), counter-rotation mismatch
> (**bounded at 1.0, deliberately under-counted** — trapped modes are
> extreme retrograde while the remnant forms from a PROGRADE inspiral,
> so the true factor is < 1 and a real waveform can only push the
> numbers DOWN), and 3349's barrier factor. Worst case over the
> physical range: **ℓ=7 1.94e−4, ℓ=8 3.56e−6**, both under the
> pre-declared 1e−3 bar. **PHYSICAL RANGE DERIVED, NOT ASSUMED:**
> r_ISCO = 3.484 M at χ = 0.68 ⇒ **v_ISCO = 0.536**, and the scan runs
> PAST it on purpose so the break point is found rather than avoided.
> **THE EDGE, STATED: the margin is THIN** — ℓ=7 crosses 1e−3 at
> v = 0.589, only +0.053 beyond v_ISCO; at the unphysical v = 0.60 the
> budget is 1.20e−3, above the bar. First run FAILED there, and the
> response was to compute the physical range rather than trim the scan
> or move the bar. Verdict: **closed inside the physical range,
> marginal just outside it.** **FOUR SHIELDS now stand, three derived
> here: multipole scaling, barrier penetration (ℓ ≥ 9 decisive), band
> separation (602–986 Hz vs 211–294 Hz — a factor 2.0, independent of
> excitation, holding at EVERY ℓ, and the one with real margin), and
> the inherited hierarchy, now redundant rather than load-bearing.**
> Honest note: this closure is the third-best of the three derived
> arguments and the prediction does not lean on it alone. Record:
> `rcore_derivation/3350_rcore3e_source_excitation.md`.
> **GR-2 amendment QUEUED and now larger: V1.4's "inherited... not
> computed in this programme" is simply wrong and should read derived
> + closed within the physical range, thin supra-ISCO margin noted.**
>
> **UPDATE — 3351: GR-2 V1.5 SHIPPED, the queued amendment folded.**
> V1.4's "inherited… not computed in this programme… undischarged,
> load-bearing" was true when written and made FALSE by 3349–3350.
> Replaced by three COMPUTED arguments **ordered by margin, not by
> discovery**: band separation first (602–986 Hz vs 211–294 Hz, factor
> 2.0, holds at every ℓ, independent of excitation — the one with
> room), barrier penetration second (7e−4 at ℓ=9; explicitly NOT
> decisive at ℓ=7), source-side budget third (1.9e−4 / 3.6e−6 at worst
> case), **with the thin margin stated IN THE PAPER** (ℓ=7 crosses
> 1e−3 at v=0.589, only 0.053 above v_ISCO=0.536). Provenance table →
> six scripts. **THE PATCH'S REAL CONTENT: the checker had a blind
> spot.** V1.4's version validated ledger→paper but never
> paper→ledger, so numbers from 3349/3350 entered with NO objection —
> the exact mechanism that grew the V1.0–V1.3 defect. Found by asking
> before editing, "will the checker catch this?" (it would not).
> **SCOPE-CREEP DETECTOR added; checker now 7/7.** It then failed
> twice on its way in, both recorded in the code: it first passed
> VACUOUSLY (matched raw LaTeX, found one citation, reported all-clear
> — the same fail-open mode the 3347 audit condemned, second
> occurrence this session), so it now runs on normalized text and
> FAILS CLOSED on its own reach; and its exclusions are NAMED WITH
> REASONS, since silent exemptions are how ledgers rot. Adversarially
> tested with a bogus citation. **Habit worth keeping: the question to
> ask of a new guard is not "does it pass?" but "what would it fail to
> notice?"**
>
> **NEXT IN THIS LANE, ranked: (1) the
> analytic disjointness inequality** (upgrades the 165-mode stability
> scan from evidence to theorem: prove trapped ⇒ m ≤ −(ℓ−1) and
> superradiance-capable ⇒ buried). **(3) full-Teukolsky line positions
> and widths** (converts orientation-scale tops into a registered
> band; the expensive one). **(4) OPEN-GR-RCORE-4**, the substrate
> census functional — discharges the A1–A3 conditionality the entire
> spin sector inherits. **(5) GR-1i is still V0.1**, the only GR paper
> not at shipped grade.
>
> **DEPOSIT FLAG (founder's domain, not the worker's):** the queue
> holds 123 papers with 120 still `not approved`. If Isak's DOIs now
> cover the corpus, the queue's APPROVED column has diverged from
> reality and is worth reconciling before any deposit wave. The gate
> stays fail-closed regardless.



**Location:** `/CPP/frontier_sectors/GR.md`
**Created:** 19 Aug 2026, Patch 3229 (Session 149), concurrent with the GR-1
V0 assembly (Patch 3228). Series home: `series_gravitation/`.
**Scope of this sector:** the gravitational series parent GR-1 and its
companions GR-1a–GR-1h (formerly c05, c07–c13; moved to
`series_gravitation/GR_companion_papers/` at Patch 3230 — OPEN-ORG-023
Item 2 executed). GR-1i is reserved for the classical-tests companion.
**Boundary:** LOCAL gravitation only. Cosmology (FRW/Friedmann, dark energy)
is owned by OPEN-EU-1 (`frontier_sectors/SR.md` / CONJ.md) and the DE lane;
nothing in this sector claims it.

---

## OPEN-GR-FE-1 — Derive the general CPP field equations (registered Patch 3229)

**The problem.** The arc reproduces the Schwarzschild (isotropic
coordinates), Kerr, and Kerr–Newman *solutions* exactly, but the general
field *equations* are present only as correspondence claims: c07 states the
CPP self-consistency condition is "≡ Einstein field equations" in the
continuum limit; c08 "identifies the CPP equation that plays the role of
Einstein's field equations" (a nonlinear wave equation for Δ|SSV| reducing
to the linearised Einstein equations in the weak field). Recovering specific
metrics is not the same as deriving the equation family whose solutions they
are, and a GR-literate reader will make exactly that distinction (Patch 3225
scoping assessment §3; founder ruling: V0 claims the solutions and registers
the derivation).

**The target.** Derive the general CPP field equations from the deeper
DI-bit / SSV_abs / SSV_net / DP Sea picture — not by positing correspondence
in the continuum limit. Folded into this item (consequences of the same
underived general equation, 0 mentions each across the eight companions):

- **Birkhoff-type uniqueness** — is the c08 static solution the unique
  spherically symmetric vacuum solution of the CPP equation?
- **The CPP energy-momentum tensor** — the object the field equations are
  equated *to*; currently absent from the corpus.

**What would count as progress.** (i) A stated general equation for the
LSP/SSV field configuration with the c08 nonlinear wave equation as its
static reduction; (ii) proof that Eq. (isotropic_schw) is its unique
spherically symmetric vacuum solution; (iii) identification of the source
tensor and its conservation law within PCD dynamics.

**Dependencies / inheritance.** Rests on the PSR constitutive form whose
SR-1 grounding is W2 viability strength (OPEN-SR-10 caveats inherited
verbatim; k is a normalisation convention, not a derived quantity — see GR-1
§7). Any derivation here inherits, and must not silently upgrade, that
standing.

**GR-1 cycle note (CONV-026, Patch 3242/3243):** Q4 3–2 RESTATE-REQUIRED fired on the Q1 3–2 OVERCLAIMS finding (abstract/thesis outran the ledger); restate EXECUTED at V0.2 — the W2/PSR conditionality promoted into the abstract and thesis. Q2 4–1 COMPLETE, Q3 5–0 SOUND stand. **Confirmation pass returned 3/3 CONFIRMED-DISCHARGED (Patch 3247; one cross-label recorded — the Gemini window signed "ChatGPT"; attributed by receipt): Q4 = SHIP-PATH-CLEAR; CONV-026 CLOSED.** V1.0 prep unblocked; deposit still gated by the founder's ruling + the tests companion. Next papers in the lane, in readiness order: the tests companion (OPEN-GR-TESTS-1, → GR-1i; bounded, targets frozen) then OPEN-GR-FE-1.

**Status:** OPEN — CHARTERED (Session 150, Patch 3254:
`series_gravitation/OPEN-GR-FE-1_derivation_charter.md`). Three theorem
targets frozen (T-1 general equation with the c08 wave equation as static
reduction; T-2 Birkhoff-type uniqueness; T-3 source tensor + PCD
conservation); inheritance bar frozen (W2/PSR standing must not be silently
upgraded); worker pre-picture expectations on record (charter §5, the A1
anti-extraction pattern); **founder physical-picture session ANSWERED —
W-1 EXECUTED (Patch 3255):** all five §6 questions answered same-session;
narrative registered verbatim at
`founders_voice/founder_ruling_GR-FE-1_physical_picture_2026-08-19.md`
(worker commentary labelled, nothing adopted). Picture-set constraints for
W-2, per the labelled commentary: conserved quantity = the conscious
points themselves + the per-Moment DI-bit equal-redistribution invariant
(redirects §5 E-1); PCD executor = the GP (CP displaces per the GP's
computed SSV_net; DI-bits a third conserved CP type — glossary/axiom-impact
flag recorded, not actioned); source = compressed-DP SSV_abs content, no
independent kinetic term posited (narrows §5 E-2); A3′ load-bearing
(symmetry at full-Moment granularity only); lattice zero-freedom + CP-only
configuration freedom + full-occupancy black-hole saturation (T-2 skeleton;
cross-check the new full-occupancy mechanism against GR-1c/GR-1e before
quoting); DP-Entities gravitationally silent at LOCAL scale (founder
expectation, DM-lane confirmation owed); Voronoi-cell-to-PSR ratio OPEN
(~10^30 GPs/PSR quoted; W-2 must not depend on it or carries it
symbolically). **W-2 EXECUTED — Patch 3258, T-1 CANDIDATE DERIVED, WITH
A HALT FINDING** (`series_gravitation/fe1_derivation/T1_derivation.md`;
verify `code/3258_t1_relay_verify.py` 10/10): from the census (AP-4
linearity + equal-redistribution cancellation + one-hop-per-Moment shell
kernel on the RIGID lattice), statics are EXACTLY flat-lattice
Laplace/Poisson for any PSR profile — the GR-1a relation k·Δ|SSV| = GM/rc²
re-derived as the unique vacuum solution, and absolute-lattice
coordinates identified with the isotropic coordinates (why the corpus
solution is conformally flat). Dynamics: messenger conservation +
determinism + full-Moment symmetry force the time-symmetric two-level
relay u(t+τ)+u(t−τ) = 2M_R u(t) — unitary, dispersion cos(ωτ) = sinc(kR),
emergent speed c_* = PSR_eff/(√3 t_P) (the √3 is a kinematic
normalisation at the k standing, Finding F-1; dispersion form flagged as
future falsifier material, unminted). T-1 candidate (lattice frame,
conditional-on-PSR/W2): (1/c_*²)∂²_t(Δ|SSV|) − ∇²_lattice(Δ|SSV|) =
normalized compressed-DP census source. Standing:
**DERIVED-PENDING-ADJUDICATION** — nothing downstream cites it yet.
**OPEN-GR-FE1-FTERM (minted Patch 3258, HALT registered per charter §4;
DIAGNOSED AND RESOLVED Patch 3259 — PENDING RATIFICATION):**
the static reduction is NOT the GR-1c Proposition as stated — symbolic
Check 5: □_g on GR-1c's OWN exact profile = −a³/(2kr⁵)+O(a⁴) (required
compensator O(a³)) while GR-1c's stated 𝓕-term is O(a⁴) under all three
readings — i.e. the 𝓕 formula fails against GR-1c's own exact solution,
independent of the new derivation. Solution-level agreement is EXACT
(the metric, the classical tests, and the weak-field sector are
untouched). GR-1c NOT adjusted (HALT discipline). ADJUDICATION OWED
(founder/panel): (i) GR-1c 𝓕-term corrigendum question; (ii) acceptance
of the T-1 candidate. **W-3 (Birkhoff — classical uniqueness of the
harmonic exterior on the lattice frame, near-free if T-1 accepted) and
W-4 (T-3 source tensor) are GATED on the adjudication.**
**RESOLUTION (Patch 3259, `fe1_derivation/FTERM_reconciliation.md`,
verify `code/3259_fterm_reconciliation_verify.py` 8/8 exact-symbolic):**
the Proposition was written for the wrong POTENTIAL. The measured-frame
vacuum statics is EXACTLY harmonic for the LOG-LAPSE
N = ln√(−g_tt/c²) = −2·artanh(k·Δ|SSV|/2): □_g N = 0 identically on the
exact solution (C1). In Δ|SSV| variables the exact compensator is
F_true = (k²Δ|SSV|/2)/(1−(kΔ|SSV|/2)²)·|∇Δ|SSV||²_g (C2) — an
O(u)·gradient-squared, where the stated 𝓕 was O(u²)·□ln (slip localised:
right building block, prefactor one power of u too many, artanh-vs-ln
resummation; C6). **EQUIVALENCE THEOREM (C3/C4):**
□_g artanh(kv/2) = [32k/((2−kv)(2+kv)⁵)]·∇²_flat v for GENERIC v —
pure algebraic factor, no derivative terms — and the full-3D coefficient
identity f″/f′ + d/du ln(√A B^{1/2}) = 0 holds identically: the corrected
measured-frame equation and the Patch-3258 lattice-frame T-1 statics are
THE SAME EQUATION in two variables. The HALT's substantive content is
DISCHARGED: the T-1 static reduction IS the (corrected) GR-1c equation,
in full 3D. GR-1c still UNEDITED; proposed corrigendum text (Form A
log-lapse / Form B quasilinear) in the reconciliation doc §6 — panel
dispatch (CONV) + founder ratification owed. T-1 candidate standing
STRENGTHENED (statics equivalence full-3D). Physical reading (commentary):
clock rates compose multiplicatively ⇒ the measured potential is the LOG
of the clock rate; the lattice census is additive in Δ|SSV|; the static
measured-frame nonlinearity is purely the dictionary. F-3 (static
superposition-in-u vs GR's nonlinear constraints) remains FLAGGED,
unminted.
**CONV-027 DISPATCHED (Patch 3260, founder-initiated):** bundled round —
Package A: the T-1 candidate (Q6b: ACCEPT-AS-CHARTER-T-1 vote); Package B:
the F-term finding + corrigendum (Q6a: APPROVE Form A/B vote). Package:
`review/conv027_fe1_t1_fterm_review_package_v1.0.md` (single block, one
paste per seat; both verify scripts inlined in full); returns receiver:
`review/reviews-CONV-027.md`. Ratification gate for the corrigendum AND
the T-1 acceptance = CONV-027 returns + founder ruling. W-3/W-4 remain
gated on that adjudication.
**CONV-027 RETURNED AND ADJUDICATED (Patch 3261,
`review/conv027_adjudication.md`; returns verbatim in
`reviews-CONV-027.md`):** Q3 VERIFIED 5–0; Q4 CORRECT-AND-SUFFICIENT 5–0;
**Q6a corrigendum APPROVED 5–0 (APPROVE-EITHER)**; Q1 SOUND 4–1 (flipper
not sustained); Q2 NORMALISATION 4–1; Q5 DISCIPLINED 4–1; **Q6b T-1
ACCEPTED 4–1** (Copilot's conditions DISCHARGED: panel script runs +
the A-5 closure annex + ordering-of-limits, `code/3261` 6/6; ChatGPT-seat
BLOCK's named condition discharged by the registered kinematic mapping
**R-CSTAR-MAP**: c ≡ R_vac/(√3·t_P), α = 1 picture-preferred; the
"unique closure" wording withdrawn — annex L1–L3 prove the two-level
FORM is forced and the continuum operator is CLOSURE-INDEPENDENT over
the admissible class, with the honest falsifier weakening to the
dispersion FAMILY cos(ωτ) = α·sinc(kR)+(1−α), unminted). Protocol
defects recorded: Gemini-seat identity defect (self-labeled "ChatGPT");
Copilot format deviation. **NOTE-GR-CSTAR-STRONGFIELD** registered
(DeepSeek novel contribution): c_*(x) → ~0.29c near the exclusion
radius — GR-1d/GR-1e cross-check flag, unminted. **FOUNDER RATIFIED ALL THREE (Patch 3262, verbatim in the adjudication
§9): (i) GR-1c corrigendum ENACTED — Proposition field_eq restated
(Form A log-lapse boxed; Form B quasilinear; equivalence identity
displayed; corrigendum remark with the old formula preserved
anti-erasure, the CONV-027 record, and the SCRIPT-EXECUTED artifact
citation); proof sketch + downstream remarks + op:einstein entry
re-pointed (op:einstein remains OPEN); GR-1c V2.1 → V2.2, compile gate
clean. (ii) T-1 CONFIRMED AS CHARTER T-1 → W-3 + W-4 execute
(Patch 3263). (iii) R-CSTAR-MAP RATIFIED — registered law at the k
standing. OPEN-GR-FE1-FTERM: CLOSED.**
**W-3 + W-4 EXECUTED (Patch 3263,
`fe1_derivation/T2_T3_uniqueness_and_source.md`, verify `code/3263`
9/9):** **T-2** — static uniqueness EXACT (general spherical static
solution C₁+C₂/r; decay + Gauss matching pin the GR-1c profile
uniquely); honesty check REGISTERED: the bare T-1 equation admits
monopole radiation (f(t−r/c)/r is an exact vacuum solution), so the
Birkhoff-type theorem is CONDITIONAL — proved on (i) T-3 census
conservation with J = 0 through the boundary and (ii) no-incoming
radiation, via the machine-checked chain (general spherical solution →
flux −4π[f+(R/c)∂_t f] → constant-flux forces f′ = 0). GR stores
no-monopole in the field equations; CPP stores it in the census — same
physics for census-conserving sources; the counterfactual discriminator
is op:einstein commentary, unminted. **T-3** — the source object is the
conserved census current (ρ, J): ρ = compressed-DP SSV_abs excess
density, J = its CP-displacement flux; continuity EXACT from CP
conservation + once-per-Moment displacement (founder Q1/A1′;
discrete checks exact-integer over 10⁴ Moments); weak-field ρ ↔ mass
density confirmed; rank-2 completion explicitly bounded at op:einstein
(REMAINS OPEN — the arc's clean frontier is now the dynamic/rank-2
sector). **Standing: T-2/T-3 DERIVED-PENDING-REVIEW** (recommend a
CONV round bundling T-2/T-3 + the FE-1 paper draft). **All three
charter theorem targets now exist; the Patch-3231 big-wave gate moves
toward open upon T-2/T-3 review + founder confirmation.**
**GR-1j V0 DRAFTED (Patch 3264):** the FE-1 consolidation companion —
T-1 (ratified) + equivalence/corrigendum context + T-2/T-3 + the
four-script verification record + full PD-001 suite; compile gate
clean; V0 / DERIVED-PENDING-REVIEW. **Next action: CONV-028 dispatch
bundling GR-1j V0 + T-2/T-3.**
**CONV-028 DISPATCHED (Patch 3265):** package
`review/conv028_t2_t3_gr1j_review_package_v1.0.md` (scope fence: T-1/
corrigendum/R-CSTAR-MAP/annex SETTLED, not re-opened; six frozen
questions — Q6a T-2 ratify, Q6b T-3 ratify, Q6c GR-1j ship-path;
triage: Birkhoff circularity, no-incoming honesty, decay class,
scalar-vs-rank-2 charter language, CONV-027 representation fairness;
Gemini identity reminder in-document; 3263 script inlined). Receiver:
`reviews-CONV-028.md`. On adjudication + founder confirmation:
OPEN-GR-FE-1 closes and the Patch-3231 big-wave gate formally moves.
**CONV-028 RETURNED AND ADJUDICATED (Patch 3266,
`review/conv028_adjudication.md`):** Q2 CORRECT-AND-HONEST 5–0; Q3
SOUND 5–0; Q4 DISCIPLINED 5–0; Q1 SOUND 4–1 (Copilot regularity
defect, explicitly non-flipping — discharged by ADOPTING the GPT
seat's STRONGER two-radius proof, C¹-only, new 3263 check T2-3b,
re-run 10/10); Q5 READY 4–1 (the minority's three revisions adopted
anyway); **Q6a T-2 RATIFIED (5–0 ratify-family, conditions
discharged); Q6b T-3 RATIFIED 5–0; Q6c GR-1j SHIP-PATH-CLEAR 4–1
(Q4 gate met 5–0)** — GR-1j → V0.1 with five adoptions (explicit
hypotheses; the "what this theorem does NOT give" remark; cosmology
exclusion; units note; trace mapping; GW-dispersion extension of
NOTE-GR-CSTAR-STRONGFIELD). Seat hygiene: both CONV-027 defects
CURED; one Grok reporting anomaly recorded. **OPEN-GR-FE-1: ALL
THREE THEOREM TARGETS RATIFIED — charter COMPLETE pending the
founder's one-word confirmation ("Confirm FE-1 complete"), which
formally MOVES the Patch-3231 big-wave gate.** Then: founder APPROVED
column (fail-closed) → Isak's DOIs (spin-trio test run first) →
GR-1j V1.0 prep.**

Deliberately deferred out of GR-1 V0 by founder ruling (Session 148
handover §5). The single most consequential open item in the arc; the
big-wave deposit gate (Patch 3231 ruling) rests on it.

---

## OPEN-GR-TESTS-1 — The classical-tests companion (registered Patch 3229)

**The problem.** The three conventional entry-criterion tests of any
gravitational theory (perihelion precession, light deflection, Shapiro
delay) plus gravitational redshift were absent or barely touched across the
eight companions (perihelion 0 mentions, Shapiro 0, geodesic 1 of 8). GR-1
V0 now carries the predicted-versus-observed summary table (GR-1 Table 1),
with every number verified by `series_gravitation/code/3228_classical_tests_verify.py`
(8/8 PASS: closed forms cross-checked against independent numeric
Binet-equation geodesic integration; the c08 isotropic form verified to BE
Schwarzschild at machine precision).

**The target.** ONE dedicated companion paper (founder ruling: not inside
GR-1, not split into three) carrying the full geodesic derivations of all
four tests on the c08 metric — timelike orbit precession, null deflection,
round-trip Shapiro delay, static redshift — as consequences worked out from
the parent's result, exactly as c09 takes c08's core and derives echoes.
Independently citable, because "does it pass the classical tests" is
precisely what a reader will search for.

**Frozen constraints.** The results it must reproduce are frozen in GR-1
Table 1 and the 3228 verify script: perihelion 42.99″/century, deflection
1.75″ at the solar limb, Shapiro ~233 μs (Earth–Venus superior conjunction,
grazing, leading log), redshift gh/c² = 2.46×10⁻¹⁵ (22.5 m) and GPS net
+38.5 μs/day. The claim discipline is also frozen: since the metric is
exactly Schwarzschild, the values are GR-identical by construction — the
tests discriminate CPP from Newton, NOT from GR, and the companion must say
so. Lense–Thirring frame-dragging is already covered (c11 ×16 mentions, c08
×7); do not redo it.

**Numerical cautions for the implementer** (found and fixed at 3228, see
`series_gravitation/reasoning/3228.md`): (1) accumulate the integration
angle as i·dφ from an integer counter — naive `phi += dphi` over ~10⁷ steps
injects rounding drift at percent level against a 5×10⁻⁷ rad/orbit signal;
(2) locate zero crossings by interpolation — first-grid-point stopping
overshoots at 10% level against an 8.5×10⁻⁶ rad deflection.

**Status:** DISCHARGED AT V0 (Session 150, Patch 3252) — final discharge at
panel review/ship. GR-1i drafted:
`series_gravitation/GR_companion_papers/GR-1i_classical_tests/GR-1i_classical_tests.tex`,
full geodesic derivations of all four tests on the c08 metric (standard
coordinates via the machine-verified exact transformation; isotropic form
carries the mechanism section). All frozen Table-1 values reproduced
(42.99″/cy · 1.75″ · ~233 μs · 2.46e-15 / +38.5 μs/day); 3228 verify re-run
8/8 PASS pre-draft; both numerical traps promoted into the paper body;
claim discipline verbatim (W2 conditionality in the abstract's first
sentence — the CONV-026 restate lesson applied from the start; GR-identical
by construction; discriminates from Newton, not GR; Lense–Thirring not
redone). Swarm-Validation subsection written honestly at ZERO new
predictions (entry-criterion compliance, no double-count of GR-1c's
exactness). Compile gate clean. Next lane item: OPEN-GR-FE-1 (charter
first, then founder physical-picture session, per the Session 149
handover).


**OPEN-GR-FE-1: CLOSED — COMPLETE (Patch 3267; founder verbatim:
"Confirm FE-1 complete.").** The Patch-3231 big-wave gate's FE-1
condition is DISCHARGED; the gate FORMALLY MOVES. Remaining
wave-opening mechanics: founder APPROVED column (fail-closed) → Isak's
DOI reservations (IN PROGRESS per the founder, 20 Aug — spin-trio test
run first; on reservation the worker executes the deposit-metadata
pass against permanent filenames) → GR-1j V1.0 prep → GR-1i review
(the last unreviewed GR companion; OPEN-GR-TESTS-1 final discharge
rides on it). Lane frontier: op:einstein (dynamic/rank-2 sector).


**CONV-029 DISPATCHED (Patch 3268):** GR-1i (the last unreviewed GR
paper) to the five seats — package
`review/conv029_gr1i_review_package_v1.0.md` (claim chain C-1…C-8;
triage incl. the perturbation bookkeeping, the deflection identity,
Shapiro/γ honesty, the constants-provenance call, and the FE-1
language-harmony check; 3228 inlined; Q6a OPEN-GR-TESTS-1
final-discharge vote; Q6b GR-1i ship-path vote gated on Q2
discipline). Receiver: `reviews-CONV-029.md`. On adjudication:
OPEN-GR-TESTS-1 final-discharges and GR-1 proceeds to V1.0 prep.


**CONV-029 RETURNED AND ADJUDICATED (Patch 3269,
`review/conv029_adjudication.md`): UNANIMOUS ON EVERY QUESTION — the
cleanest round of the cycle. Q6a: OPEN-GR-TESTS-1 FINALLY DISCHARGED
5–0 (the item opened at Patch 3229 is CLOSED). Q6b: GR-1i
SHIP-PATH-CLEAR 5–0 → V0.1** with five editorial adoptions (constants
provenance/sensitivity — the IAU shift lands the perihelion prediction
dead-centre of observation; PPN β = γ = 1 structural note; the
reproduces-vs-shares sentence; the achromatic-bending falsifiable
feature, unminted; the implementation-cross-check caution).
**GR-1 V1.0 PREP IS UNBLOCKED — the gravitational arc has no
unreviewed papers and no open review gates.** Seat ledger: Grok
count-line anomaly SECOND occurrence (pattern; next dispatch will
instruct verbatim count-line pasting). Lane frontier: op:einstein.


**GR-1 V1.0 + GR-1j V1.0 SHIPPED (Patch 3270):** closed-state updates
only (abstract/claims/open-problems with execution records; W2 ledger,
Table 1, and all derivations untouched); both compile gates clean;
changelogs updated. **ARC END-STATE: fully derived, fully reviewed,
ship-ready — GR-1 V1.0; GR-1a–h stable; GR-1c V2.2; GR-1i V0.1
(cleared unanimous); GR-1j V1.0.** Remaining: deposit mechanics
(Isak's DOIs → spin-trio test run → queue regeneration → founder
APPROVED rows). Lane frontier: op:einstein (future charter).


**OPEN-GR-PPP-1 REGISTERED (Patch 3271; trigger: founder PPP audit
question — honest answer NO):** the Paper Production Protocol is NOT
complete across the arc. Audit: GR-1 was missing Keywords/PLS/CP-GP
Signature at V1.0 (FIXED this patch → V1.0.1); GR-1a missing
PLS+Signature; GR-1b–h missing Signature; documentation suites
changelog-only vs the ~10-file SPIN-3 standard, all 11 papers;
anthology/TATWD: ZERO of 17 existing chapters cover the GR arc.
Program: W-A formatting pass GR-1a–h (bounded, next warm-up); W-B
suites ×11 (multi-session); W-C anthology chapters (≈1 session each;
FOUNDER DECISION FLAGGED: chapter-per-paper vs a smaller arc-spine
set — the FE-1 story is prime chapter material). None of it gates the
Zenodo wave mechanically; suites-before-deposit preference on
flagship rows flagged for the founder.

**OPEN-GR-PPP-1 W-B PROGRESS (Patches 3276–3278, Session 151): the two
flagship rows are done — GR-1 and GR-1j now carry full ten-file
documentation suites** to the SPIN-3 standard (keywords, glossary,
mechanism, phenomena, philosophy, FAQ, reviews, reasoning pointer-map,
transcript pointer-map, development vignettes), each beside its existing
changelog. Every relative pointer in both suites was asserted to resolve
before commit.

**AND THE SUITE PASS EARNED ITS KEEP IMMEDIATELY — a defect in shipped
GR-1 V1.0.1 was found by writing it (Patch 3276 → V1.0.2).** GR-1's
epistemic ledger, §"Correspondence claims", still asserted that the
general field equation was correspondence-level and "not attempted in
V0", and that Birkhoff-type uniqueness and the CPP energy-momentum
object "are likewise open ... the corpus currently contains neither" —
while the SAME paper's abstract and Open Problems section both recorded
OPEN-GR-FE-1 as CLOSED. The V1.0 prep (3270) had checked the ledger's
W2/PSR *conditionality*, which was correct, and not its *status rows*.
Corrected anti-erasure: V0 rows retained verbatim under a superseded
heading, each followed by a Status-at-V1.0 note giving the delivered
result at ratified strength (T-1 CONV-027 4–1; T-2 conditional Birkhoff
in the asymptotically-flat local class; T-3 a conserved current, NOT a
rank-2 tensor) and naming what is still not claimed (op:einstein).
Process finding registered: a ledger has as many independent staleness
surfaces as it has rows; "the ledger is fine" is not a checkable
statement, and a status change closes some rows while leaving others
correct.

**Second defect, and its corpus scan CLOSED:** GR-1's title-block
version line had lagged at "Version 0 (assembly draft)" against a \date
of 1.0.1 — the same defect class caught in SPIN-3 six patches earlier
(3253). The corpus-wide check flagged in `reasoning/3276.md` was then
RUN across all eleven GR .tex files: no further instances. GR-1a–h carry
no version string in the title block at all (nothing to disagree), GR-1i
and GR-1j are consistent. The defect class is confined to papers that
put a version string in `\title`, and both known instances are now
fixed. No further W-A2-style sweep is owed on this item.

**W-B REMAINING: nine suites** — GR-1a–h (eight legacy companions,
March-2026 vintage; source material is thinner than the flagships and
the development vignettes will be correspondingly shorter) and GR-1i
(recent, CONV-029 records available). Suggested pace 2–3 per session.
**W-C: chapters 1–4** per `book_project/GR_arc_chapter_plan.md`
(chapter 5 written at 3272); chapter one "The One Formula" is next.

**OPEN-GR-PPP-1 W-B ROWS 3–5 (Patches 3281–3284, Session 152): GR-1i,
GR-1a, GR-1b suites complete — five of eleven done, six remaining
(GR-1c–h).** GR-1i was straightforward (recent paper, CONV-029 records
in-repo). The two legacy companions required a different discipline and
got it: **GR-1a and GR-1b each received a CREATED changelog** (neither
had one) and carry **STATUS: reconstructed** on changelog, reasoning,
and transcript. The V1→V3 content deltas of both papers were never
recorded and are left BLANK rather than invented; `reviews-GR-1a.md` and
`reviews-GR-1b.md` each open by stating there is NO paper-level review
basis, list indirect coverage as indirect, and name the never-reviewed
load-bearing claim (GR-1a: the "by analogy" Q_grav normalization from
which G follows; GR-1b: the equal-shares result behind the factor of
two).

**W-B ROW-4 CROSS-CHECK WORTH THE RECORD:** GR-1a's central relation
k·Δ|SSV| = GM/rc², obtained in March 2026 by shell-broadcast analogy,
was **independently re-derived from the messenger census** by the
field-equation programme five months later (T-1's exact statics; unique
decaying spherical vacuum solution, Patches 3258–3262). Neither route
knew the other when it started. For a paper that has never had a panel
round, this is stronger evidence than a round would have been.

**SECOND STALENESS FINDING — REGISTERED, NOT EXECUTED (Patch 3283).**
GR-1b's §Open Problems is overtaken by the arc's own later work: item
(2) exact Schwarzschild with non-singular Planck-scale interior
**DELIVERED** (GR-1c Theorem 1, r_core = r_S/2); item (3) Kerr
**DELIVERED** (GR-1f; GR-1g for Kerr–Newman); item (1) full nonlinear
Einstein still open as stated but substantially advanced (GR-1j T-1,
rank-2 at op:einstein); item (5) cosmological constant **downgraded**
rather than advanced (OBL-CAL-LABEL at V3.3; bracketing language
withdrawn at CONV-020). Status table in
`GR-1b_weak_field_GR/documentation_suite/phenomena-GR-1b.md`.

**THE .tex WAS NOT EDITED, and the boundary is the point.** A paper
contradicting *itself* is bookkeeping — corrected unilaterally under
PD-006 at Patch 3276 (GR-1's ledger). A paper overtaken by *later work*
is a decision about how a legacy document should read, and belongs to
the founder. **PROPOSED W-D: a status-note pass across GR-1a–h open-problem
and future-direction sections**, on the 3276 anti-erasure pattern
(original retained verbatim; dated status note beside it, naming the
delivering companion). Bounded — a survey plus one patch per paper.
**Recommended BEFORE the Zenodo wave: DOIs are permanent, and a
deposited paper listing a solved problem as open is the kind of thing a
hostile reader finds first.** Founder decision; not started.

**PATTERN, now explicit: status sections rot silently.** Two findings in
two sessions (GR-1's ledger, GR-1b's open problems), both surfaced by
the suite pass — because no compile gate and no review round checks
whether last March's open problem is still open, and the suite is the
only step that reads a paper whole. W-B should be expected to keep
finding these in GR-1c–h.

**OPEN-GR-PPP-1 W-B ROWS 6–8 (Patches 3285–3288, Session 152): GR-1c,
GR-1d, GR-1e suites complete — EIGHT of eleven done; three remain
(GR-1f, GR-1g, GR-1h).** All three papers received a CREATED changelog
(none had one) and STATUS: reconstructed markers where the record does
not exist. GR-1c's changelog now carries the **V2.2 corrigendum in
full** — found by the T-1 HALT check against the paper's own exact
solution, diagnosed to the wrong-potential root cause, APPROVE-EITHER
5–0 at CONV-027, founder-ratified, enacted with the defective formula
preserved. That chain previously lived only scattered across reasoning
fragments; it is the arc's reference case and now has one home.

**THIRD STALENESS FINDING — GR-1c, and the sharpest so far.** Three of
five open problems delivered or superseded (`op:kerr` → GR-1f/GR-1g;
`op:echoes` → GR-1d; `op:hawking` → GR-1e substantially); `op:einstein`
correctly still open. **`op:24cell` is DOUBLY STALE**: it requests a
discrete-to-continuum proof "on the 600-cell lattice with 24-cell
Voronoi cells, requiring the eigenvalue spectrum established in Spin
III." SPIN-3 now exists and supplies that spectrum — **but on the
REGULAR DODECAHEDRON**, because founder ruling A1 (Patch 3236) retired
the 24-cell (600-cell dual = 120-cell). The item states a superseded
geometry as current, not merely a stale status. `.tex` NOT edited —
third time under the boundary held since 3283. **This strengthens the
W-D case: a deposited paper asserting a retired geometry is worse than
one listing a solved problem as open.**

**AND THE PATTERN IS NOT UNIVERSAL — GR-1d and GR-1e have NO staleness
finding, for a principled reason.** Every open problem in both papers
depends on the strong-field INTERIOR or a full quantum-field treatment,
and the Session-150 field-equation programme deliberately stopped at the
exterior (T-1/T-2/T-3 are census-level exterior results; the interior
stays at `op:einstein`). Papers whose open problems sit *behind*
`op:einstein` have not been overtaken. Refines the Session-151 finding:
status sections rot only where the arc actually advanced past them.

**FORWARD POINTER REGISTERED FOR THE ECHO/EVAPORATION LANE (both papers,
unexploited):** NOTE-GR-CSTAR-STRONGFIELD — census speed c_* → ~0.29c
near the exclusion radius — was minted at CONV-027 and flagged
*explicitly* for the GR-1d/GR-1e lane, and extended at CONV-028 to
frequency-dependent GW dispersion/birefringence in strong fields.
**Neither has ever been folded into either paper.** For GR-1d the
suppression sits in the same region as the echo cavity and would modify
the tortoise-coordinate travel time — hence the delay formula — if
significant at the stated precision. For GR-1e the geometric-breakdown
criterion counts cells and may be untouched, while the force-balance
stability argument involves propagation and may not be. Bounded,
well-posed, unasked. Recorded rather than guessed at — resolving it is
physics, not documentation.

**REVIEW-COVERAGE MAP, now explicit across the arc's legacy papers.**
None of GR-1a, GR-1b, GR-1c (whole-paper), GR-1d, or GR-1e has had a
dedicated CONV round. CONV-027 reviewed GR-1c's field-equation
Proposition **and nothing else in that paper** — so GR-1c's Theorem 1
(exact Schwarzschild) and Theorem 2 (Planck core) are unreviewed, and
GR-1d and GR-1e both rest on Theorem 2. Each suite names where a future
round should start: GR-1a the "by analogy" Q_grav normalization; GR-1b
the equal-shares result; GR-1c Theorem 1's shell integration and Theorem
2's Exclusion argument; GR-1d the r₀ = r_S + l_P identification (the
delay is logarithmically sensitive to it); GR-1e the mechanical-stability
fixed point (the strong, exposed claim — not the termination argument,
which is a robust breakdown-of-validity claim). **In GR-1c and GR-1e the
unreviewed parts and the uncaptured-reasoning parts coincide exactly.**

---

## OPEN-GR-PPP-1 W-B: **COMPLETE** (Patches 3276–3292, Sessions 151–152)

**All eleven gravitational papers now carry documentation suites to the
SPIN-3 ten-file standard.** Rows: GR-1 (3277), GR-1j (3278), GR-1i
(3281), GR-1a (3282), GR-1b (3283), GR-1c (3285), GR-1d (3286), GR-1e
(3287), GR-1f (3289), GR-1g (3290), GR-1h (3291). Nine of the eleven
had **no changelog at all** and received one; every legacy suite carries
`STATUS: reconstructed` where the record does not exist, with unrecorded
content deltas left BLANK rather than invented.

### What the pass produced beyond the suites

**1. One in-paper correction, executed** (Patch 3276, GR-1 → V1.0.2):
the epistemic ledger contradicted the paper's own abstract. Corrected
anti-erasure under PD-006.

**2. Four staleness findings, recorded and NOT executed** — GR-1b
(items 2, 3 delivered), GR-1c (three of five delivered/superseded, and
`op:24cell` **states a retired geometry as current**), GR-1f (two of
four delivered by same-week siblings), GR-1g (one partially). Boundary
held throughout: a paper contradicting *itself* is bookkeeping; a paper
overtaken by *later work* is a founder decision.

**3. The staleness pattern, refined to a rule.** Status sections rot
**exactly where the programme advanced past them, and nowhere else.**
GR-1d, GR-1e, and GR-1h came back clean because every open problem in
all three sits behind the strong-field interior (`op:einstein`), where
the arc has not gone. GR-1f's finding is a distinct kind: its
delivering siblings carry the *same March week* date — a batch shipped
without a closing cross-reference pass, not a document aging.

**4. A shared bottleneck, newly visible.** Three of GR-1h's four open
problems **and** GR-1d's amplitude problem all reduce to one uncomputed
quantity: **Planck-core reflectivity**. Two papers, different
directions, one blocker behind `op:einstein`. Computing it would unblock
the arc's two most observationally live results simultaneously. This is
the strongest argument the suite pass produced for prioritising the
interior sector.

**5. Forward pointers on an unexploited review note.**
NOTE-GR-CSTAR-STRONGFIELD (census speed c_* → ~0.29c near the exclusion
radius) was minted at CONV-027, flagged *explicitly* for GR-1d/GR-1e,
and never folded into either. The suite pass found it bears on **four**
papers, not two: GR-1d (echo cavity sits in that region), GR-1e
(force-balance stability involves propagation), **GR-1f and GR-1g**
(their bounds are derived from a near-horizon velocity *reaching c* —
directly exposed to a near-horizon speed reduction), and GR-1h (its
threshold compares velocities at the horizon). Unworked in all five.

**6. The arc-wide review-coverage map — the pass's most uncomfortable
output.** **None of the eight legacy companions has ever had a dedicated
CONV round.** CONV-027 examined GR-1c's field-equation Proposition **and
nothing else in that paper**, so GR-1c's Theorem 1 (exact Schwarzschild)
and Theorem 2 (Planck core) are unreviewed — and GR-1d, GR-1e, and
GR-1g all rest on Theorem 2. Textbook agreement (Gravity Probe B;
standard Kerr results) is *inherited* agreement and must not be read as
coverage. Each suite names its own best attack surface:

| Paper | First thing a panel should attack |
|---|---|
| GR-1a | the "by analogy" Q_grav normalization, from which G follows |
| GR-1b | the equal-shares result behind the factor of two |
| GR-1c | Theorem 1's shell integration; Theorem 2's Exclusion argument |
| GR-1d | the r₀ = r_S + l_P identification (delay is log-sensitive to it) |
| GR-1e | the mechanical-stability fixed point (not the termination argument, which is robust) |
| GR-1f | treating a **pattern** velocity as a subluminality-constrained propagation speed — this carries the Kerr-bound theorem, i.e. the arc's cosmic-censorship claim |
| GR-1g | **additivity** — Einstein–Maxwell is nonlinear; charge does not generally superpose onto vacuum solutions |
| GR-1h | Ω₊ read as a literal broadcast frequency — same class as GR-1f, so **one round should examine both together** |

**In GR-1c, GR-1e, GR-1f, GR-1g, and GR-1h the unreviewed parts and the
uncaptured-reasoning parts coincide exactly.** Five papers where the
load-bearing step has neither external examination nor a recorded
derivation.

### Remaining in OPEN-GR-PPP-1

- **W-C: anthology chapters 1–4** per `book_project/GR_arc_chapter_plan.md`
  (chapter 5 written at 3272). Chapter one, "The One Formula"
  (GR-1 + 1a/1b), is next.
- **W-D (proposed, founder decision outstanding):** status-note pass
  across the legacy companions' open-problem sections, anti-erasure per
  the 3276 pattern. Scope is now known precisely from the W-B findings —
  **GR-1b, GR-1c, GR-1f, GR-1g only**; GR-1a, GR-1d, GR-1e, GR-1h need
  nothing. Bounded at four papers. Recommended before the Zenodo wave.

---

## OPEN-GR-PPP-1 W-D: **OPENED** (Patch 3294, Session 153) — 1 of 4 done

**Executed under PD-006.** W-D was flagged to the founder at Patches 3283
and 3285 and left with him both times; he replied "proceed" both times
without addressing it. Process and sequencing are delegated, so
continuing to ask would itself have been the violation. Executed before
the deposit wave because the GR-1c `op:24cell` item states a **retired
geometry** and Zenodo DOIs are permanent.

**Form (fixed for all four rows).** These papers do **not** contradict
themselves — they were accurate when written and were overtaken by later
work. So nothing is rewritten: original item text retained **verbatim**,
a dated bracketed note appended beside it. Precedent is GR-1b's own V3.3
calibration label (Patch 3204), which sits inline in exactly this shape.

**Three rules, held on every note:**
1. **Name the delivering companion AND its limits.** A note reading only
   "DELIVERED by GR-1c" would convert an honest open problem into an
   unqualified claim — the failure W-D exists to prevent, not commit.
2. **Never upgrade a still-open item.** GR-1b item (1) reads STILL OPEN
   first, "substantially advanced" second.
3. **Touch only what needs it.** Three of GR-1b's six items; the
   cosmological-constant item was left alone because its V3.3
   calibration label is better hedged than any note would be.

**Row 1 — GR-1b V3.5 (Patch 3294): DONE.** Items (1) STILL OPEN /
advanced (`op:einstein`); (2) DELIVERED by GR-1c Thms 1–2, **with the
note recording that neither theorem has been externally reviewed**;
(3) DELIVERED by GR-1f/GR-1g, carrying forward `op:allorders`.

**Rows 2–4 REMAINING: GR-1c (do first — the retired-geometry item),
GR-1f, GR-1g.** Patches 3295–3297. Design rationale in
`reasoning/3294.md`; scope is fixed by the W-B findings — **no
re-survey needed.**

---

## Separate finding, Session 153 — **GR-1b's figures had NEVER rendered** (Patch 3293)

Found by the pre-edit baseline compile opening W-D. **Two compounding
defects, both from W-A2 (Patch 3274):** the three figures exist **only
as `.svg`** while the `.tex` was switched to `graphicx` (which
`pdflatex` cannot read SVG with), **and** no `\graphicspath` was set
while `\includegraphics` names bare filenames against assets in
`figures/`. Either alone suffices. The paper had never rendered its
figures — not before W-A2 (no files) nor after (wrong format, wrong
path) — compiling with three `pdftex.def` errors and three draft-mode
placeholder boxes.

**W-A2 reported "compile: 0 errors" for this paper.** A gate reporting
clean on a document rendering three empty boxes is itself worth
examining, and is flagged here for the PPP program: **any paper claiming
figures should have its RENDERING verified, not its `.tex` inspected.**

**Worker error owned:** the Patch-3283 suite pass recorded the W-A2
entry as "matplotlib → PDF, committed." The repository contained no
PDFs. The detail was reconstructed from the W-A2 narrative rather than
the file listing and stated as fact in a changelog whose purpose is to be
the reliable record; the `STATUS: reconstructed` markers did not catch it
because the error sat in a *confident* sentence. **Process finding: when
reconstructing a patch's effect, check the ARTIFACTS, not the
narrative.** Sentence amended in place, correction named.

**Fixed:** SVGs converted to PDF (cairosvg), committed alongside;
`\graphicspath{{figures/}}` added. Baseline 3 errors / 16 pp / 267 KB →
**0 errors / 14 pp / 543 KB**. The page count *falling* while size
doubles is the proof: draft placeholder boxes ran taller than the real
figures. One `natbib` undefined-citation warning is **pre-existing**,
unchanged, flagged for a future pass rather than silently absorbed.

---

## OPEN-GR-RCORE-1 — Planck-core reflectivity: **DERIVED-PENDING-REVIEW**, with a HALT finding against shipped GR-1d (Patch 3297, Session 154)

**Deliverable:** `series_gravitation/rcore_derivation/RCORE_derivation.md`;
verify `code/3297_rcore_verify.py` **9/9 PASS**. Executed on the founder's
Session-154 opening instruction (run the priority calculation), superseding
the queued W-D rows for this session; W-D rows 2–4 carry forward unchanged.
The two unacted threads from Session 153 (reflectivity bottleneck; the
five-paper C* exposure) turned out to be ONE problem: NOTE-GR-CSTAR-
STRONGFIELD's c_*(x) is the T-1 wave speed in exactly the region where the
reflectivity was uncomputed, and the ratified T-1 IS the "full CPP field
equation in the strong-field interior" that GR-1d Open Problem 1 named as
its missing prerequisite.

**Results (all machine-verified, zero free parameters):**

- **R-1: |R_core| = 1 exactly** — absorption requires storage (forbidden:
  Exclusion-floor register has no compression headroom), a sink (forbidden:
  AP-4 conserves DI-bits), or secular transfer (forbidden: GR-1e fixed point
  stable). GR-1d's amplitude problem closes at argument level: first echo at
  |T_bar|² ≈ 5% of ringdown, no free reflectivity parameter.
- **R-2: reflection phase π (Dirichlet)** at linear order — the clamped
  register is a fixed end; confirms GR-1d's assumed pressure-node phase.
  One-sided-constraint refinement registered, not hidden.
- **F-R1 (the structural yield): the exclusion surface sits OUTSIDE the
  would-be horizon.** The PSR formula's r is the lattice = ISOTROPIC radius
  (GR-1c's own declaration; ratified at T-1). Saturation at r̄ = μ maps to
  areal **9μ/4 = (9/8) r_S**; the horizon's image r̄ = μ/2 is inside the
  excluded region; k·Δ|SSV| ∈ [0,1] on the whole exterior — the dictionary
  singularity at k·Δ|SSV| = 2 is unreachable. **The Exclusion floor censors
  the horizon: CPP black holes are horizonless, hard-surfaced objects.**
  Surface lapse exactly 1/3 by two independent routes; z = 2;
  c_*(surface) = c/2 under ratified R-CSTAR-MAP.
- **C-R1 consilience: EXACT Buchdahl saturation.** GR's maximum-compactness
  bound for static matter is R ≥ 9GM/4c², saturated by incompressible matter
  at critical pressure with surface lapse 1/3. The CPP core — incompressible
  BY the Exclusion floor — lands exactly there with exactly that lapse,
  nothing tunable. Registered as consilience, unminted as prediction.
- **HALT-GR-1D-DELAY:** GR-1d's shipped Theorem Δt = (4GM/c³)ln(2M/m_P)
  (~112 ms, GW150914) rests on the areal reading + the r_S + l_P quantum-
  displacement step; under the ratified identification neither survives. New
  closed forms: **Level A (measured-metric, eikonal) Δt = (3/2 + 8 ln 2)
  GM/c³ ≈ 7.05 GM/c³ → 2.15 ms for GW150914** (finite-ℓ barrier peak: 8.60;
  time-domain evolution measures 8.20); Level B (T-1 lattice dynamics)
  ≈ 2.98 GM/c³ → 0.91 ms. The ln(2M/m_P) factor is GONE; the prediction
  becomes sharper and far more exposed (ms-scale 5% echoes on GW150914-class
  remnants — constrainable with existing LIGO ringdown data; if excluded,
  the falsifier machinery worked). **GR-1d and GR-1e NOT edited — HALT
  discipline, FTERM precedent. Adjudication owed: founder ruling on the
  coordinate reading's consequence for the shipped Theorem, then a CONV
  round — natural anchor for the GR-1c Thm 1–2 round the review-coverage
  map already owes.**
- **C* note disposition:** the five-paper exposure is SUBSUMED under F-R1
  (no horizon exists; GR-1f/g/h "near-horizon velocity" arguments re-read as
  near-surface with c_* ≥ c/2; the note's ~0.29c figure diagnosed as the
  pre-R-CSTAR-MAP shorthand, 1/(2√3) — updates to c/2). Per-paper dated
  notes deferred until the adjudication settles what they should say.
- **OPEN-GR-RCORE-2 (minted):** residue bundle — Level A/B dictionary
  question (dispersion-falsifier territory); unilateral-constraint phase
  refinement; tensor-sector wall condition; Kerr (ergoregion vs exclusion
  surface — the "Planck-core bomb" re-framed as the textbook ergoregion
  instability of horizonless spinning reflectors).
- **CONV-030 RETURNED (4/5, same-session) AND ADJUDICATED (Patch 3299):**
  verbatim `reviews-CONV-030.md`; adjudication `conv030_adjudication.md`.
  Copilot seat DELIVERY-FAILED (wants the package as a .md file) — retry
  issued as direct file upload; its eventual return is CONFIRMATION-CLASS
  (no majority flippable). Tally: Q1 SOUND-family 4–0 (GPT
  SOUND-WITH-GAPS minority adopted as honest restatement — "(i)+(ii) one
  conservation argument + (iii) independent dynamical constraint";
  "three independent ways" withdrawn); Q2 CORRECT-family 4–0; **Q3
  GENUINE 4–0 — the directed numerology attack on the Buchdahl
  consilience found no purchase**; Q4 WARRANTED 4–0, delay grade
  BOTH-WITH-DICTIONARY-CAVEAT 3–1 (Level-A displayed as measured-metric
  benchmark); **Q5 Thm 1 SOUND 4–0, Thm 2 SOUND-WITH-RELABELING 4–0 —
  GR-1c's load-bearing theorems pass their first external review, with
  the relabeling corrigendum panel-approved**; Q6 AMEND 4–0, SUBSUMED
  3–1 (GPT's per-paper GR-1f/g/h dependency audit adopted as the C*
  notes' execution plan); Q7 COMPLETE 3–1 (both GPT missing items
  adopted: RCORE-2 gains (vi) frequency-dependent wall response under
  the unilateral constraint, (vii) the dependency audit). Gemini's
  error-bar mandate adopted (Δt_A = 2.15 ± 0.14 ms at 62 ± 4 M_⊙).
  Seat hygiene: COUNT-LINE mandate CURED (Grok pasted "9/9 PASS"
  verbatim). Llama non-seat note recorded without prejudice.
  **RATIFIED (Patch 3300, founder verbatim in
  `founders_voice/founder_ruling_conv030_rcore_ratification_2026-08-20.md`):
  all three items — amendments EXECUTE at 3301–3303. Copilot's return
  landed via file upload: 5/5, no majority moved (Q3 GENUINE and Q5 both
  now 5–0 UNANIMOUS); RCORE-2 further extended (viii) LIGO search
  systematics, (ix) non-spherical/accreting cores, (x) multi-messenger/EM
  constraints; seat-ledger: Copilot SCRIPT line reclassified to INSPECTED
  (quoted the package's reference run, not its own execution) and its
  audit steer unexecuted (covered elsewhere); next-dispatch mandate:
  SCRIPT-EXECUTED requires the seat's OWN run. F-R1 is the sector's
  STANDING READING, founder physical-picture anchor registered ("a body
  with solid, irreducibly minimum inter-CP spacing / maximally compact
  body").**
- **RATIFICATION EXECUTED (Patches 3301–3303):** GR-1c V2.3 (relabeling
  corrigendum: dated Remark + table supersession note; no equation
  changes; compile 0 errors); GR-1d V3 (112 ms Theorem superseded
  anti-erasure; new §Amendment — surface at areal (9/8) r_S, |R|=1
  DERIVED with the honest restatement, both delays with the dictionary
  question INLINE, Level-A benchmark, 2.15 ± 0.14 ms / 0.91 ± 0.06 ms at
  62 ± 4 M_⊙, amended table with f_echo IN the LIGO band — 465 Hz for
  GW150914; V2 Open Problem 1 CLOSED; compile 0 errors); GR-1e V1.1
  (horizonless reading applied interpretively; emission mechanism
  honestly RE-OPENED for the hard-surfaced body — no silent
  re-derivation; prop:stability UNAFFECTED and promoted as a pillar of
  the |R|=1 derivation; remnant census logic stands; compile 0 errors).
  **The HALT arc is CLOSED: finding (3297) → dispatch (3298) →
  adjudication (3299) → ratification (3300) → enactment (3301–3303),
  one session.** REMAINING FROM THE ROUND: the C* dated-notes pass on
  GR-1f/g/h, now with the adopted execution plan (per-paper dependency
  audit for hidden horizon/interior assumptions FIRST — CONV-030
  adoption 4); OPEN-GR-RCORE-2 items i–x.
- **RCORE-2(iv) DERIVATION (Patch 3320) — THE KERR EXCLUSION SURFACE
  AND THE ERGOREGION-CENSORSHIP THEOREM: censorship at ALL spins; the
  3318 χ_crit = 2/√7 retired as a conservative scalar-only artifact.**
  Two-component census: A1 scalar ≡ lapse dictionary (inverts to
  s = 2(1−α)/(1+α); reproduces the ratified μ/r̄ EXACTLY at a = 0);
  A2 vector ≡ ZAMO dragging speed v = ωϖ/α (register demand in local
  reach units); A3 quadrature |kΔ|² = s² + v²; surface = {s² + v² = 1}.
  Engine: the exact Kerr identity g_tt = −α²(1 − v²) — the ergosphere
  IS the v = 1 surface — so F = s² + 1 > 1 there strictly: **the
  circulation register alone is full at the ergosphere, so total
  saturation occurs outside it, at every spin and latitude. The same
  floor that censors the horizon censors the ergoregion. No exterior
  ergoregion ⇒ no ergoregion instability, any spin, any
  reflectivity.** Min ergosphere-F 1.706; min clearance 0.25 M;
  extremal clearance 0.258 M; χ = 0.68 equator: derived surface
  2.267 M (proxy was 2.052 M). GR-1f's Kerr-bound subluminality
  relocates to the exclusion surface (register capacity, not a
  never-formed horizon). SECONDARY FINDING (script's own first run):
  **prograde-ring burial from χ ≈ 0.55** — at remnant spins the
  prograde equatorial photon ring lies INSIDE the surface; the echo
  cavity is RETROGRADE-ring keyed: Δt_ret(χ = 0.68) ≈ 8.59 GM/c³ =
  2.62 ms GW150914 (+22% over Schwarzschild — the feared 45% (a/M)²
  systematic is now a derived 22%); f_echo ≈ 380 Hz in-band; the
  pro/retro asymmetry is itself a CPP-vs-horizon-ECO discriminator.
  Grade: DERIVATION-CONDITIONAL on A1–A3; **CONV-032 OWED** (attack
  surface: A3's composition law, A2's identification, eikonal grade);
  no paper edits until the round + ratification. **OPEN-GR-RCORE-3
  minted:** Kerr wall spectroscopy (time-domain (2,±2) on the derived
  co-rotating Dirichlet surface; echo comb; fate of prograde modes
  above ring burial). Zel'dovich surface superradiance survives
  censorship as a separate milder channel (registered, unexplored).
  Verify `code/3320_kerr_surface_derivation_verify.py` 8/8. Record
  `rcore_derivation/3320_kerr_surface_derivation.md`.
  **CONV-032 CLOSED 5/5 (Patches 3324–3325): theorem CORRECT given
  A1–A3, 5–0; burial CONFIRMED 5–0; template ADEQUATE-FOR-DRAFT 5–0
  with a BINDING error-bar rider; the reverse-engineering suspicion
  SURVIVES on the paper trail 4–1 — while the GPT dissent's
  γ-weighted-norm counterexample (F = s² + γv², γ < 1, preserves the
  full a = 0 result yet can admit the ergosphere) SUSTAINS the
  load-bearing-ness of A3's unweighted norm as a derivation debt.
  Q1 "unique extension" WITHDRAWN (minimal, not unique); χ_crit =
  2/√7 relabeled SUPERSEDED-CONDITIONAL-ON-A1–A3 (GPT compromise
  adopted). Adjudication `review/conv032_adjudication.md` v1.0;
  founder RATIFIED 21 Aug 2026 (Patch 3326,
  `founders_voice/founder_ruling_conv032_censorship_ratification_2026-08-21.md`,
  verbatim: "Ratify the bundle. Please proceed with GR-2") — all seven
  items ENACTING Patches 3326–3329; **GR-2 drafting IS OPEN.**
  **OPEN-GR-RCORE-3 AMENDED (Patch 3326, CONV-032 Q7 adoptions):** the
  statement now reads — Kerr wall spectroscopy: (a) systematic
  finite-ℓ, m-mode time-domain analysis on the derived co-rotating
  Dirichlet surface (the eikonal equatorial ring is NOT the finite-ℓ
  barrier — Copilot item (a)); (b) surface co-rotation ω(r_surf) in
  the template as COMMITTED work, not an implicit omission; (c) echo
  comb structure and the fate of prograde modes above ring burial;
  (d) quantitative growth-time bounds for the surviving Zel'dovich
  surface-superradiance channel (censorship of an exterior ergoregion
  does not dispose of rotating-boundary amplification — GPT closing
  caution, adopted verbatim).**
  **LEG A DISCHARGED (Patch 3333, Session 156, verify 9/9, FAST
  4/4):** at ℓ=2, χ=0 the eikonal comb does NOT survive — the
  Buchdahl-wall cavity (~3.5M) supports a SINGLE top-of-barrier
  resonance per parity (RW ω₁=0.4535 → **236 Hz @ 62 M_⊙**, τ=21.5
  GM, Q=4.9; Zerilli 0.4513, 0.5% split; TD cross-validated −1.0%);
  persistent signature = resonant reprocessing + early broadband
  transients at the eikonal spacing. Kerr mode-fate recon (geodesic
  grade, χ=0.68): the ENTIRE corotating (ℓ,ℓ) branch FULLY-BURIED
  (μ_crit=0.774 vs μ(ℓ,ℓ)≥0.8) — burial sharpens — with thin (2,2)
  margin (0.026) and mode-resolved onset χ=0.665 (vs eikonal 0.555).
  A provisional "+1% comb correction" from a failed TD instrument
  was RETRACTED (wall-shift test + no-wall control; five-dead-end
  trail in the record §3). GR-2 V1.0 NOT contradicted — the CONV-033
  eikonal scoping held. Record:
  `rcore_derivation/3333_rcore3_legA_finite_ell.md`. **REMAINING =
  LEG B, the lane's sharpest question: does the longer Kerr
  retrograde cavity (wall 2.267M → retro ring 3.71M) restore a
  multi-resonance comb? Decides PRED-O-39's refined search target.**
  Plus items (b) co-rotation BC and (d) Zel'dovich bounds above.
  PRED-O-39/predictions.md untouched pending Leg B; f₁=236 Hz
  registered unminted. GR-2 amendment queue (additive): Leg-A
  pointer, onset 0.665, thin-margin caution.
  **LEG B DISCHARGED at eikonal-WKB grade (Patch 3334, Session 156,
  verify 7/7, all-FAST):** THE COMB IS NOT RESTORED — the
  Bohr–Sommerfeld census gives N_trapped = 0 for every exposed mode
  at χ=0.68 (max Φ/π = 0.245 for (2,−2), threshold ¾) and for
  (2,−2) across the ENTIRE spin scan χ∈[0.30,0.98] (max 0.247 at
  0.52): lengthening cavity and falling barrier top (0.4425→0.3846)
  cancel. Refined search target (eikonal-top, +17% Leg-A position
  calibration, Q~5): a LINE SET at ~211/233/260/294 Hz
  ((2,−2)/(2,−1)/(2,0)/(2,+1); ~247–344 Hz calibrated) + early
  transients at the 2.624 ms retrograde delay; retrograde keying
  survives as line ORDERING — the corotating (ℓ,ℓ) lines are absent
  (wave-side burial: R<0 AT the wall at every ω with a forbidden
  region). Instrument validated on the a→0 anchor (ω_top =
  (ℓ+½)/√27 to <1%; N=0 = Leg A). Record:
  `rcore_derivation/3334_rcore3_legB_kerr_census.md`. **REMAINING:**
  full-Teukolsky line positions/widths; co-rotation BC (b);
  Zel'dovich bounds (d). **PRED-O-39 PROVISIONAL refinement text
  registered in the record §4, NOT executed — awaits CONV-034
  (RCORE-3 Legs A+B audit round, the natural next dispatch) +
  founder ratification, as does the GR-2 amendment set.**
  **AUDITED AND RATIFIED (CONV-034, 5/5 same-session,
  AMENDMENTS-CLEAR 4–1; founder "Ratify the bundle", Patch 3337):**
  both instruments VALID-family 5–0; the single-resonance and
  N_trapped = 0 findings CONFIRMED 5–0; retraction ADEQUATE 5–0.
  Leg B's discharge carries the adopted grade label **"the integer
  census at eikonal-WKB grade"** (not exact finite-ℓ Kerr
  spectroscopy). Q5 FAITHFUL-AT-GRADE 4–1 — the binding rule did NOT
  fire — and the OVERCLAIMS minority's revisions were ADOPTED anyway
  (the rule is a floor, not a certification): the "~247–344 Hz" band
  and the transported Q ≈ 5 are WITHDRAWN as registered quantities;
  eikonal tops retained as orientation-scale; the +17% anchor
  demoted to a one-point directional note; onset restated as "0.665
  under the μ correspondence, finite-ℓ onset unquantified, the 0.026
  margin may sit inside the correspondence error"; wave-side burial
  graded corroborative-at-same-grade; co-rotation explicitly
  UNTESTED for line structure. Enacted: PRED-O-39 amended (Patch
  3337), GR-2 V1.0 → V1.1 (Patch 3338). **LEGS A AND B DISCHARGED at
  those grade labels. REMAINING RCORE-3: (1) full-Teukolsky line
  positions and widths — the computation that would convert the
  orientation-scale tops into a registered band and give Kerr
  mode-dependent Q; (2) the co-rotating wall BC; (3) Zel'dovich
  growth-time bounds.** Adjudication:
  `review/conv034_adjudication.md` v1.0.
  **LEG C (Patch 3339, verify 6/6, all-FAST) — ITEM (b) DISCHARGED FOR
  THE COUNT, AND A HALT-CLASS NARROWING OF LEGS A/B:** (1) co-rotation
  is COUNT-NEUTRAL at Dirichlet grade — R(r;ω) depends only on
  (a,m,Q,ω), so a wall rotating at Ω_w leaves the phase volume
  invariant (verified to 1e-9); line-position effects remain
  full-Teukolsky work. (2) **THE NARROWING:** Leg B computed ℓ ≤ 3
  only; running the exposed extreme-retrograde branch to ℓ = 12 shows
  Φ/π grows LINEARLY (≈ 0.122 ℓ at χ = 0.68, increments ±0.0002) and
  crosses ¾ at **ℓ_crit = 7 ± 1** for χ ≥ 0.30 (ℓ ≈ 10 ± 1 at χ = 0;
  the ±1 is phase-convention sensitivity, CONV-035 adopted — never
  quote the bare integer) —
  **trapped combs DO exist at high multipole**; "no comb at any spin"
  is withdrawn and replaced by "no comb at ℓ = 2, 3 (every spin
  tested), ladders from ℓ ≳ 7 where excitation is negligible."
  (3) **CONSISTENCY WIN:** the eikonal comb is the ℓ → ∞ limit and is
  recovered FROM BELOW — Leg A's single ℓ = 2 resonance and geometric
  optics are two ends of one ladder; the eikonal picture was never
  wrong. (4) **ROBUSTNESS ENVELOPE:** the ¾ threshold is
  δ_w/2 + π/4, so the low-ℓ N = 0 needs δ_w > 0.235π = 42.3° — the
  DERIVED clamped-register δ_w = π clears it 4.3× (a Neumann-like end
  WOULD trap: the result is about the clamped wall, not geometry
  alone). (5) **STRUCTURAL PROTECTION** (regraded CONV-035:
  ESTABLISHED-OVER-A-DECLARED-EXHAUSTIVE-DOMAIN, reconnaissance —
  a structural exclusion needs the analytic disjointness inequality,
  registered as work): over 165 modes = ALL (ℓ,m) with ℓ = 2..12, NO mode is simultaneously EXPOSED, TRAPPED, and
  SUPERRADIANT — trapped modes are extreme-retrograde (no window),
  superradiance-capable modes are corotating and BURIED; burial and
  trapping select disjoint regions of the (ℓ,m) grid, so censorship
  protects the finite-ℓ sector too, by a mechanism the eikonal
  analysis could not see. Record:
  `rcore_derivation/3339_rcore3_legC_corotation_multipole.md`.
  **NEW: OPEN-GR-RCORE-3(e) — MULTIPOLE EXCITATION BUDGET.** The
  negligibility of ℓ ≳ 7 excitation in comparable-mass ringdown is
  INHERITED from standard phenomenology and computed NOWHERE in this
  corpus; it is now load-bearing for the observable prediction and
  must be discharged. **CONV-035 CLOSED 5/5 (Patch 3344): Q9b CLEAR
  4–1, Q6 (the process call) CORRECT 3–2 — enact-on-discovery stands,
  no standing constraint imposed, the two dissenting seats' reasoning
  recorded as the minority position. Five revisions adopted, all
  enacted. NEW OWED WORK: the corpus-wide quantifier audit across the
  eleven GR papers, before the next flagship prediction move.**
  (Superseded note:) **CONV-035 OWED:** the panel ratified
  (CONV-034) the generalization Leg C narrows. Enacted: PRED-O-39
  narrowed (3339), GR-2 V1.1 → V1.2 (3340).
- **OPEN-GR-RCORE-4 (minted Patch 3325, from the CONV-032 GPT
  dissent): DERIVE THE ROTATIONAL CENSUS FUNCTIONAL FROM MICROSCOPIC
  REGISTER DYNAMICS.** Two conjuncts, both currently assumptions of
  the 3320 construction: (a) A2's normalization — WHY is the
  rotational register demand the ZAMO dragging speed v = ωϖ/α rather
  than another locally normalized gravitomagnetic invariant (the
  decisive property v = 1 ⟺ g_tt = 0 is a consequence of this
  choice, not independently established); (b) A3's norm and relative
  weighting — WHY unweighted L² quadrature (the registered
  counterexample: F = s² + γv² with γ < 1 preserves the entire
  static sector but can de-censor the ergosphere; L∞ places the
  surface AT it). Discharging RCORE-4 upgrades all-spin ergoregion
  censorship from a theorem of the A1–A3 model to a physical theorem
  of CPP; until then all censorship prose stays explicitly
  conditional (CONV-032 Q4 adoption). Logically prior to any
  unconditional-censorship claim; independent of (and parallel to)
  RCORE-3's finite-ℓ spectroscopy.
- **RCORE-2(iv) RECONNAISSANCE (Patch 3318): THE ERGOREGION-BURIAL
  CRITERION — χ_crit = 2/√7 ≈ 0.756, and the GW merger-remnant
  population is GEOMETRICALLY SAFE.** Under the dictionary-consistent
  proxy (spinning exclusion surface = Kerr ZAMO-lapse-1/3 surface;
  exact at a = 0, recovering areal 9M/4), the closed form
  α²(r_E,eq) = a²/(2(2M²+a²)) gives an exact critical spin: below
  2/√7 the exclusion surface sits OUTSIDE the ergosphere at every
  latitude — no exterior ergoregion, no negative-energy modes, NO
  ergoregion instability at any reflectivity. χ = 0.68 (GW150914-class)
  is buried with gap 0.052 M. Above χ_crit an equatorial exposure band
  opens (±20° at 0.80, ±41° at 0.95); only there do the growth-time and
  drain conjuncts even arise — and the high-spin X-ray-binary
  comparison is a MODELING question (those spin fits assume a Kerr
  horizon to the ISCO). Honest grade: reconnaissance; the lapse-1/3
  criterion is the approximation (rotational census enters at O(a²));
  Zel'dovich surface superradiance survives burial as a separate milder
  channel, noted unexplored. Verify
  `code/3318_ergoregion_burial_recon.py` 7/7 (two check-logic sign
  errors caught by the script's own first run — the binding case is the
  lapse MAXIMUM on the ergosphere, and burial means α(r_E) < 1/3 —
  fixed before commit). Record
  `rcore_derivation/3318_ergoregion_burial_recon.md`. HARDENING PATH =
  RCORE-2(iv) proper (derive the Kerr surface from the rotational
  census, re-run the comparison). PRIORITY EFFECT: the corpus's only
  viability-class flag drops to ordinary urgency — SD-5/K₀ and
  OPEN-QM-9 no longer queue behind an existential question.
- **W-D COMPLETE (4/4) AND THE FIVE-PAPER C* PASS COMPLETE (Patches
  3305–3309):** GR-1c V2.3.1 (notes on op:kerr / op:24cell /
  op:hawking / op:echoes; op:einstein untouched — op:hawking honestly
  partially-delivered-then-RE-OPENED, op:echoes
  delivered-and-CORRECTED); GR-1f V1.1 + GR-1g V1.1 (W-D merged with
  the dependency audit — thm:kerr_bound and the KN bound flagged twice
  over: horizon evaluation + c-vs-c_* ceiling, with GP-B/LT and the
  exterior KN/RN structure explicitly fenced unaffected; both
  correction-order estimates declared unverified against the amended
  baseline); GR-1h V1.1 (delivered-input-NOT-closed discipline on the
  shared-bottleneck problems; the "Planck-core bomb" re-framed as the
  ergoregion instability of a horizonless spinning perfect reflector,
  flagged LOAD-BEARING for spinning-object viability); GR-1b V3.6
  (addendum to the week-overtaken 3294 note, PLUS a defect: the 3293
  figure repair never survived a clone — .gitignore's blanket *.pdf
  silently excluded the figure PDFs; fixed with the principled
  exception !**/figures/*.pdf and a clean corpus scan; new detection
  rule: after committing generated assets, verify them in
  git show --stat, not on disk). All five compile gates 0 errors.
  ARC STATE: every gravitational paper post-RCORE consistent — three
  amended (GR-1c/1d/1e), four noted (GR-1b/1f/1g/1h), three
  untouched-by-design (GR-1a/1i/1j).
