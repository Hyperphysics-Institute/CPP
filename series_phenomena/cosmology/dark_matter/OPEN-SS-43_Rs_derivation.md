# OPEN-SS-43 — De-novo derivation of the DM-core sea-screening length R_s(N)

**Campaign opened:** Patch 1863, 3 July 2026 (Opus; founder-ratified same session as the DM-1 v1.1
re-ratification). **Status: OPEN — routes formalized, mechanism NOT selected.** Verify:
`code/1863_rs_routes_and_velocity_power.py`. Pipeline grounding: `code/1858_eqq_screened_residual_capture.py`
(re-read in full before this file was written).

## 0. Problem statement and why it is the make-or-break

DM-1 v1.1's dwarf-core magnitude is conditional on this derivation. The capture force is the screened unipolar
E_qq residual: V(r) = (E_c·r_c/r)·exp(−r/R_s), r_c = 1 fm (1858). The Sea screens single-hadron color at ~1 fm
(SF-5 confinement scale). The question: **what is the screening length R_s of an N-element, color-balanced qCP
rod core, from substrate physics — and what is the residual well depth E_c from the same mechanism?** If the
answer is pion-like (~1 fm), DM-1 falls back to weak-SIDM (pre-registered falsifier, v1.1 §Falsifiability).

**Pinned inputs (CONV-003 provenance):** m_el = 1408 MeV [0886]; σ_el/m_el = 0.11 cm²/g geometric convention
[0859/0886] ⇒ σ_el = 27.6 fm²; E_ee = 0.9 MeV [1813]; floor ceiling N ≲ 18–21 [1860]; formation-kinetics
short-N result [1855–1856]; χ = φ⁻³/6 ≈ 0.0394 [Capotauro]; 1858 scan anchors (E_c ~ 0.3 MeV, R_s ~ 15–30 fm
"targets", N = 15 fixed).

## 1. Element-scale anchors (needed by every route; honesty flag attached)

From σ_el = 27.6 fm²: interaction radius r_int ≈ 2.96 fm; square-face scale d_sq ≈ 5.26 fm. Structural bond
scale d_bond ~ 2ℏc/264 MeV ≈ 1.49 fm. **Flag:** the 0.11 convention is polarizability-enhanced (London-additive
lineage), so r_int is an *interaction* radius, not a hard structural size; every route below is tabulated at
both anchors rather than silently choosing the favorable one.

## 2. Deliverable 3 resolved first (the velocity power — computable now, and it was)

The v1.1 panel pinned a discrepancy: corpus ∝1/v² (capture-focusing) vs Copilot's ∝1/v⁴ (Rutherford transfer).
Computing p(v) = d ln(σ/m)/d ln v directly on the 1858 model (script §B): **the power is not a single
exponent.** At R_s = 15–30 fm, N = 15: p ≈ −0.8 to −1.3 at dwarf velocities (30–100 km/s, deep screening tail),
steepening through −2 to −3.6 in the 200–1500 km/s Coulomb window (Copilot's −4 gloss is this regime's limit),
then p → 0 above ~2500 km/s (contact floor, b_max = r_c). The corpus "1/v²" is the dwarf↔cluster *average*.
**Consequences:** (i) both panel glosses were regime-local truths of one formula — the pin is resolved without
either being wrong; (ii) the live falsifier's shape is the full b_max(v) curve, not a power law — the
observable signature is a *gentle* dwarf-side rise (p ~ −1), a steep mid-range fall, and a hard floor; (iii)
this is a property of the 1858 model and inherits its conditionality — a selected mechanism could modify V(r)'s
form and must recompute p(v).

## 3. Candidate mechanisms for R_s(N) — formalized, not selected

**Route A — Sea saturation (charge loading).** The Sea's qq-channel response saturates near the core; screening
completes when integrated response matches source strength Q ∝ 8N: R_s ≈ (8N)^{1/3}·r₀. At r₀ = 1 fm (color
scale): needs N > 400 — **excluded by the floor ceiling.** At r₀ = r_int: N = 17–21 clips the window bottom —
marginal sliver only. *Physical content required: is the near-core Sea response actually saturated, and what
sets r₀?*

**Route B — channel-suppressed Debye (medium property, N-flat).** R_s is set by the Sea alone: the
color-balanced rod couples to the Sea only through the residual (magnitude-only) channel, suppressed relative
to bare color by an efficiency χ_res. If the suppression enters the response linearly, R_s ≈ 1 fm/χ_res; with
χ_res = χ_Capotauro = φ⁻³/6: **R_s ≈ 25.4 fm — in the window, N-independent.** If it enters as √χ (standard
Debye ∝ 1/√(n g²)): R_s ≈ 5.0 fm — below. *Honest label: the 1/χ landing is numerological until the response
order is derived; the Capotauro matrix element's relevance to Sea screening (vs its native chirality
cross-sector role) is itself a founder question.* Signature: no N-dependence in R_s.

**Route C — source coherence (geometric).** The Sea cannot complete cancellation inside the source's own
extent: an extended unipolar rod of length L = N·d_el polarizes the Sea coherently over ~L, so R_s ≈ N·d_el.
(Reinforced by rod field structure: within r ≲ L the residual is line-like ~1/r 2-D, transitioning to 1/r²
beyond L — the screened point form only applies outside the rod's own length.) Window landings: d_bond → N =
11–20 (upper allowed band); r_int → N = 6–10; d_sq → N = 3–5. **Compatible with the ceiling at every anchor**;
selects different N sub-bands. Signature: R_s ∝ N.

## 4. The over-determination structure (sharpened by the §D map — an honest tightening)

The 1858 "targets" (E_c ~ 0.3, R_s ~ 15–30) were quoted at N = 15. The §D map shows the dwarf magnitude is
~R_s²-sensitive and only ~log-E_c-sensitive — **R_s is the lever** — and at E_c = 0.3, R_s = 30 fm gives
σ/m(dwarf) ≈ 7, over-coring; the viable band at N = 15 is nearer **R_s ≈ 10–17 fm at E_c ~ 0.3** (widening to
~25 fm at E_c ~ 0.1). Moreover the N-trend table shows small-N rods core *harder* (σ/m ∝ b²_max/N with KE ∝ N),
so viability is genuinely a **surface in (N, R_s, E_c)**, not a rectangle.

**Kill-criterion (three-way over-determination):** the selected mechanism outputs a *curve* (R_s(N), E_c(N))
with no dark-sector freedom. It must (1) intersect the dwarf-viability surface, (2) at an N below the floor
ceiling [1860], (3) at the N that formation kinetics [1855–1856, hTetra 4th-addition / ribbon pathways]
actually produces. Three independent constraints on one curve — if no N satisfies all three, the mechanism
dies; if none of A/B/C (or a founder alternative) survives, the coring discriminant falls to weak-SIDM exactly
as the v1.1 falsifier pre-registers. E_c must come from the SAME mechanism (residual strength at contact),
including its N-scaling (charge-additive E_c ∝ N vs flat — §D shows the two give measurably different coring
N-trends).

## 5. Campaign restructure (founder-directed inversion — TLA, 3 July 2026, Patch 1864)

The mechanism-selection decision points (D1–D3, §5 of the 1863 layer) are **superseded by founder direction**:
do not guess the subquantum structure; **invert** — assume the DM model, calibrate the invisible Sea parameter
from the coring requirement, then test whether the calibrated value keeps every other pillar standing. Data
trumps theory; loop back on counterfactuals. (Verbatim capture: `reasoning/1864.md`, two FOUNDER CONTRIBUTION
blocks.) Registry note: the master glossary defines the Sea as all-sites-occupied at the Planck-scale lattice,
so the calibrated quantity is not raw DP density but the **residual-channel response amplitude relative to the
color channel**: η ≡ r_color/R_s under linear screening, anchored to SF-5's empirical ~1 fm confinement length.
The ontology alternative (sparse occupancy; η reinterpreted as occupancy-weighted response) is FLAGGED, not
adopted — it would touch the glossary and A-tier.

## 6. Phase-1 calibration result (Patch 1864; `code/1864_eta_calibration_and_confront1.py`)

Calibrating R_s so σ/m(50 km/s) ∈ [1, 2] cm²/g (corpus v1.1 central band; **empirical re-pin queued as the
first data-trumps action**), across N = 5–20 and both D2 E_c-scalings:

- **R_s ≈ 3.5–17 fm, η ≈ 0.29–0.058**, monotone falling with N. The calibrated range sits *below* the old
  "15–30 fm" quote at nearly every N — the 1863 tightening, confirmed by inversion.
- **Cluster safety survives calibration everywhere** (σ/m ≈ 0.001–0.02 at the calibrated R_s): post-calibration
  this is a genuine prediction, and it passes across the whole band.
- **D3 answered by measurement, conditionally:** η = χ = φ⁻³/6 (R_s = 25.4 fm) over-cores at every N ≤ 20 under
  the [1, 2] target. Closest approach η(N=20, σ=2) ≈ 0.058 ≈ 1.5χ. χ revives only if the empirical dwarf target
  is ~4–5 cm²/g — which some SIDM fits allow. **The Capotauro question is now hostage to the empirical dwarf
  cross-section, i.e. to data — exactly where the founder wants it.**

## 7. CONFRONT-1: the baryon-residual bound (first cross-sector confrontation — and it bites)

If the residual coupling is pairwise-additive in qCP count (rod core 8N, nucleon 3), the calibrated rod residual
implies an NN long-range tail: E_NN = 9·E_c/(8N)², same screening length. Born-level observables:

- **np scattering length: PASSES with 3–10× margin** across the whole band (δa ≈ 3×10⁻⁴–1×10⁻³ fm vs ~3×10⁻³ fm
  sensitivity).
- **Heavy-nucleus coherent binding: CONSTRAINS.** ΔB(A=200) ≈ 2.7–3.9 MeV at N = 5 (flat E_c) — in tension with
  ~1 MeV mass-fit systematics; ≈ 0.4–1.0 MeV at N ≳ 12 — safe-to-marginal. **The baryon window disfavors small-N
  calibrations (N ≲ 8) and pushes toward N ≈ 10–20** — converging with the floor ceiling (N ≲ 20) and tail
  pruning (N ≲ 40) on a narrow surviving band: **N ≈ 10–20, R_s ≈ 7–17 fm, η ≈ 0.06–0.14.**
- Caveats attached (judgment ledger): the ΔB estimate is pairs × ⟨V⟩ at 4 fm typical separation (crude; density
  integral queued); the semi-empirical mass formula could partially absorb a smooth ΔB; and if the rod residual
  is *collective/geometric* rather than pairwise-decomposable (a live mechanism alternative), the nucleon
  residual could vanish and CONFRONT-1 is moot — in which case its constraint evaporates rather than kills.

## 8. Judgment ledger (auditable; founder may veto any entry and we loop back)

J1 linear N-flat screening baseline (source-extent correction deferred, testable). J2 r_color = 1.0 fm
(0.85–1.0 fm spread untagged in corpus). J3 dwarf target [1, 2] cm²/g at v = 50 (corpus; **empirical literature
pin is the queued data action and moves both η and the χ verdict**). J4 pairwise-additive qCP coupling for
CONFRONT-1 (collective alternative noted, voids CONFRONT-1). J5 sensitivity anchors order-of-magnitude
(a_np ± 0.003 fm; mass fits ~1 MeV). J6 calibration band N ∈ {5…20} from the floor ceiling + formation kinetics.

## 9. Queued next steps (data first, per mandate) — SUPERSEDED by §10's reordered queue (Patch 1865)

1. **Pin the empirical dwarf coring σ/m** from published SIDM analyses (moves J3, decides the χ question).
   **DONE — Patch 1865 (§10 below).**
2. Refine ΔB with a proper nuclear density integral; check whether mass-formula absorption hides it.
3. Formation-lane N (1855–1856 E_ee reversibility) — now load-bearing for where in the band nature sits.
4. CONFRONT-2: CC correlation-length ξ channel consistency with the calibrated Sea response.
5. Recompute p(v)/falsifier shape at the calibrated (N, R_s, E_c); paper integration under CONV-003 tags; panel.

## 10. The empirical dwarf pin — and χ revives (Patch 1865, 4 July 2026)

Queued action 1 executed (verify: `code/1865_empirical_dwarf_pin_recalibration.py`; verbatim record
`reasoning/1865.md`; source provenance in the verify-script header per CONV-003).

**The pin (J3 → J3′).** The published dwarf-scale landscape is a broad band, not [1, 2]: rotation-curve fits
prefer ~2–3 cm²/g at v ~ 50–100 km/s (Kaplinghat–Tulin–Yu 2016; Ren et al. 2019); core-formation viability at
V_max ≈ 40 km/s spans 0.5–50 cm²/g with the LARGEST cores at 5–10 (Elbert et al. 2015); MW dSphs at
v ~ 10–40 km/s want 20–100 (Correa 2021; Roberts et al. 2024). High-v bounds: groups 0.5 ± 0.2 (Sagunski
2021); clusters < 0.13 tightest (Andrade 2022). **Adopted: σ/m(50 km/s) ∈ [1, 5] central, [0.5, 10] extended.
The old corpus [1, 2] was the low edge of the empirical window.**

**Verdicts at the pin (1864 pipeline unchanged, targets moved):**

- **χ REVIVES.** η = χ = φ⁻³/6 (R_s = 25.4 fm) delivers σ_dwarf = 3.6–4.2 cm²/g at N = 20 (IN-central),
  5.6–7.0 at N = 12–15 (in-extended), both E_c models. The 1864 contingency ("χ revives only if the dwarf
  target is ~4–5") is cashed by data. Cluster at η = χ: 0.0016–0.0036.
- **Surviving band tightens.** CONFRONT-1 at the widened calibration excludes N = 5 everywhere and N = 8 at
  nearly every corner: survivors **N ≈ 12–20, R_s ≈ 8–32 fm, η ≈ 0.12–0.03** — and the χ point (N = 15–20)
  sits inside it, ΔB ≈ 0.5–0.8 MeV.
- **Cluster safety passes the tightest published bound post-calibration:** max σ/m(1500) over the whole pinned
  band = 0.058 < 0.13.

**Consilience read (founder's criterion):** floor ceiling (N ≲ 20) + tail pruning (N ≲ 40) + baryon residual
(N ≳ 12–15) + empirical dwarf window under η = χ (N ≈ 15–20) converge on **N ≈ 15–20, η = χ** — a
zero-parameter candidate (Capotauro heritage) where §6 had only a calibration. Candidate coherence, NOT a
closure: it must survive the ΔB density-integral refinement (now load-bearing) and CONFRONT-2.

**Honest flags:** J3′ band-drawing is still a judgment (heterogeneous analyses mapped to one number at
50 km/s; sources pinned so the panel can re-draw it). χ IN-central holds exactly at N = 20; N = 15 gives 5.6,
just past the central edge. All results remain conditional on the 1858 V(r) form (J1) and pairwise additivity
(J4). The dSph-regime fits (20–100 at v ~ 10–40) are an unrun SHAPE test on σ(v) at η = χ.

**Reordered queue (by load-bearing-ness):**

1. **ΔB density-integral refinement** (J5) — now gates the χ-revival claim.
2. σ(v) shape at η = χ, N = 15–20: p(v) recompute + confrontation with dSph-regime fits and the group point.
3. CONFRONT-2: CC ξ-channel consistency with η = χ.
4. Formation-lane N (E_ee reversibility) — does formation kinetics land N ≈ 15–20 naturally?
5. Paper integration under CONV-003 tags; then the held CONV-001 panel.

