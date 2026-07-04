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

1. **ΔB density-integral refinement** (J5) — now gates the χ-revival claim. **DONE — Patch 1866 (§11 below).**
2. σ(v) shape at η = χ, N = 15–20: p(v) recompute + confrontation with dSph-regime fits and the group point.
3. CONFRONT-2: CC ξ-channel consistency with η = χ.
4. Formation-lane N (E_ee reversibility) — does formation kinetics land N ≈ 15–20 naturally?
5. Paper integration under CONV-003 tags; then the held CONV-001 panel.

## 11. ΔB refined — heavy-nucleus channel voided, constraint migrates to np scattering, χ corner survives (Patch 1866, 4 July 2026)

Queued item 1 executed (verify: `code/1866_db_density_integral.py`; verbatim record `reasoning/1866.md`).
Proper density integral (exact shell–shell Yukawa kernel; Coulomb sanity anchor passes to 5 decimals; uniform
sphere and Woods–Saxon agree within 2%) plus an SEMF-absorption test.

- **The crude 1864 estimate was ~1.6–1.8× high** (refined/crude ≈ 0.55–0.65 band-wide). At the χ point, raw
  refined ΔB = **0.29–0.80 MeV for N = 12–20 — under the ~1 MeV anchor with NO absorption credit.** N = 5
  stays in raw tension (1.5–3.2); N = 8 drops to safe-to-edge.
- **Absorption voids the heavy-nucleus channel:** ΔB(A) along the valley fits the SEMF basis to a residual of
  ~2×10⁻⁵ of raw; implied coefficient shifts are milli-MeV, far inside independent determinations. A smooth
  valley-wide shift of this shape is not detectable in mass fits. (Collinearity caveat on individual shifts
  tagged in the verify output.)
- **The constraint migrates to δa_np — unabsorbable, two-body:** at the χ point it EXCLUDES N = 12
  (3.7–4.6×10⁻³ fm > ~3×10⁻³), puts N = 15 at the edge (2.9×10⁻³), clears N = 20 (1.6–2.2×10⁻³). Anchor now
  pinned to the measured triplet length a_t = 5.4194(20) fm. **Surviving χ corner: N ≈ 15–20 — unchanged,
  carried by a cleaner channel, sharpest at N ≈ 18–20.**
- **Honest re-statement of the low-N leg:** the generic low-N low-target corner (N = 5–8 at σ_dwarf 1–2) is no
  longer robustly baryon-excluded once absorption is credited; conservative raw-refined reading still disfavors
  N = 5. The 1864 "baryon window pushes N to ≳ 12" claim is DOWNGRADED to a joint (N, target) bound for the
  generic band; it remains sharp specifically at the χ point via the np channel. Flagged for the panel.
- **Ledger:** J5 → J5′ (ΔB channel refined and retired-in-absorbed-reading; np channel promoted to the binding
  CONFRONT-1 observable). J6′ → J6″ (χ corner N ≈ 15–20 np-carried; generic band re-widens at low N).

**Queue after 1866:** (1) σ(v) shape at η = χ vs dSph-regime fits + group point **— DONE, Patch 1867 (§12);
opened the D4 fork**; (2) CONFRONT-2 (CC ξ-channel); (3) formation-lane N; (4) paper integration under
CONV-003; panel. **Items 2–4 HELD at the D4 fork (§12).**

## 12. The full-curve shape test — group point nailed, cluster floor collision, D4 fork opened (Patch 1867, 4 July 2026)

First assembly of the FULL σ(v) = floor + capture curve (1857 decomposition) at the χ point (verify:
`code/1867_sigma_v_shape_test.py`; verbatim record `reasoning/1867.md`). The elastic floor ε·0.11·N
(1856 MC ε ≈ 0.30, 1860 convention) = **0.49–0.66 cm²/g at N = 15–20, velocity-independent** — and every
prior cluster-safety number (1858/1865) was capture-only.

**Verdicts:** dwarf pin PASS (N = 18–20); LSB PASS (never calibrated to); **group PASS — the floor lands
directly on Sagunski's positive 0.5 ± 0.2 detection with zero adjustment** (ε from geometry MC, 0.11·N from
rod geometry, N from the np channel); Bullet PASS (marginal at N = 20); dSph regime LOW by ~25–50% (grazing
the window's edge — recorded as a miss within that window's systematics); **cluster FAIL — the floor violates
the full ladder ×1.4–1.9 (Sagunski < 0.35), ×2.6–3.5 (Eckert), ×3.8–5.1 (Andrade < 0.13).**

**The squeeze is in the data:** the group detection (≥ 0.3 at 1150) plus the cluster ladder (< 0.13–0.35 at
1500) demand σ falling ≳ 2.3× in that narrow window — for ANY model. The capture term is long gone by there;
only the flat floor remains. Natural CPP onset scales bracket but miss the window (whole-rod KE = E_ee at
~3500–4000 km/s; per-element at ~15,000); the needed barrier scale is ~0.06–0.13 MeV. Flat-floor fallback
(N ≲ 4) is np-dead at η = χ: **the χ corner stands or falls with a floor-suppression mechanism or a
bound-applicability argument.**

**PAPER EXPOSURE flagged (not edited):** DM-1 v1.1 §5's "cluster-safe, robust" is capture-only; the paper's
own σ_T convention implies a 0.5–0.7 cluster floor at the calibrated N. Same class as 1859, caught in-house
before the panel. Paper untouched pending the fork; **CONV-001 panel stays HELD.**

**D4 — founder decision points (campaign live fork; no route chosen in-patch):**
**D4-A** floor-suppression mechanism (~×2–5 between 1150 and 1500 km/s; barrier scale ~0.06–0.13 MeV — a
natural N-dependent CPP scale?); **D4-B** floor-normalization re-audit (linear ε·0.11·N vs MC ~N^0.7 with
independent anchor — worth ×1.5–2, enough for < 0.35, not < 0.13); **D4-C** bound-applicability audit
(cluster ladder calibrated on isotropic point-particle SIDM; anisotropic rod scattering may core less per unit
σ_T — must be argued quantitatively); **D4-D** accept and demote (χ dies; fallback N ≲ 4, small R_s).

**Ledger:** J7 registered — the hard-capsule velocity-independent floor is now the load-bearing judgment of
the campaign. Honest summary: **the floor is simultaneously the model's best unfit hit (group) and its
sharpest violation (clusters).** The 1150–1500 km/s window decides.

