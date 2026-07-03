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

## 5. Founder decision points (campaign blocked on these — substrate-mechanism selection is vision-driven)

- **D1 (primary): which screening mechanism is substrate-true?** A (saturation), B (channel-suppressed medium
  response), C (source coherence), a hybrid (e.g., C inside the rod length + B beyond), or an alternative from
  the founding picture. What does the Sea *do*, PCD-cycle by PCD-cycle, at the boundary of a color-balanced
  unipolar core?
- **D2: is the E_qq residual charge-additive along the rod** (E_c ∝ N) **or contact-local** (E_c flat)?
- **D3: does χ = φ⁻³/6 have standing in the Sea's screening response**, or is its appearance at 25.4 fm a
  coincidence to be resisted?

## 6. Queued next steps (post-selection)

1. Derive the selected route's (R_s(N), E_c(N)) from substrate mechanics (not fit).
2. Recompute p(v) and the full σ(v) shape under the derived V(r); update the falsifier form in DM-1 if changed.
3. Run the three-way intersection (§4); verdict: coring discriminant DERIVED / KILLED.
4. Feed the surviving N-band back to the formation lane (1855–1856 reversibility question, still open there).
5. Paper integration + panel, under CONV-003 provenance tags throughout.
