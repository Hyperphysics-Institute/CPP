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
sharpest violation (clusters).** The 1150–1500 km/s window decides. **[D4 RESOLVED by §§13–14 below.]**

## 13. J7 audited — the "wall" is the coat radius, and the convention already knew it (Patch 1868, 4 July 2026)

D4 executed under founder-delegated judgment: audit the hard-capsule idealization before inventing mechanisms
or demoting. The rod's elastic size is b_eff(v) solving V_coat(b) = KE, from the REGISTERED coat scales only
(E_ee = 0.9 MeV, r_scr = 1.0 fm, r_c = 1 fm). **Self-consistency hit:** the 1860 convention's normalization
implies r_impl = 9.46 fm; the coat gives b_eff(50 km/s, segment) = 9.21 fm — **3% agreement, zero tuning**.
The 0.11·N "geometric" size IS the low-velocity coat radius. The 1856 MC froze it; the physical floor inherits
b_eff(v). Variant grid k ∈ {1, 2} × μ ∈ {seg, rod}: cluster spans 0.028–0.245; stress test with the MC's own
f(A) assembly gives k_eff ≈ 0.4 (still violating) — spread decidable only by treating the softness exactly →
Patch 1869. All variants convert the 1867 group "hit" into an undershoot (it was borrowed from frozen b_eff).
Verify `code/1868_coat_radius_floor.py`; reasoning 1868. J7 → J7′; J8 (element spacing unpinned) registered.

## 14. The exact classical S(v) — D4 resolved, cluster ladder passes, χ stands, group becomes the falsifier (Patch 1869, 4 July 2026)

Orbit-integral deflection angle for the repulsive coat channel (sanity: low-v σ_T = π·b_eff² × 1.06–1.09) →
derived shape **S(v): 1.00 (50) → 0.44 (200) → 0.082 (1150) → 0.056 (1500) → 0.012 (3500)**; effective
exponent ≈ 1.85, ruling out the k_eff ≈ 0.4 hard-interior reading. Full curve at χ, N = 15–20: dwarf pin PASS,
LSB PASS, **cluster 0.034–0.037 — the ENTIRE ladder passes with ×3.5 margin on Andrade**, Bullet PASS, dSph-lo
grazing (~20–25% low, unchanged), **group 0.053–0.056 → 2.2σ below Sagunski's mild 0.5 ± 0.2.** Data-trumps
arithmetic: three independent 95% cluster limits outweigh one 2.5σ mild preference. **χ = φ⁻³/6 at N ≈ 15–20
STANDS** (np channel untouched). **New crisp falsifier: predicted group-scale σ/m ≈ 0.05–0.25, not 0.5 —
near-term group analyses discriminate.** PRED-candidate at paper integration. Verify
`code/1869_coat_channel_deflection_integral.py`; reasoning 1869. J7′ → J7″ (floor = ε·0.11·N·S(v), derived
shape, single v_ref anchor); J9 closed by computation.

**Queue after 1869 (paper path REOPENED):** (1) soft-potential rigid-body MC confirming S(v) [gold-standard
check, founder may deem non-blocking]; (2) CONFRONT-2 (CC ξ-channel at η = χ); (3) formation-lane N;
(4) DM-1 §5 integration under CONV-003 (capture channel + derived-shape coat channel + the group falsifier +
the 1867 exposure correction) → CONV-001 panel. Founder may reorder.


## 15. LOOP-BACK CORRECTION — the soft MC supersedes the 1869 shape; cluster verdict is normalization-limited and marginal (Patch 1870, 4 July 2026)

The gold-standard check was run (`code/1870_soft_rod_mc.py`; reasoning 1870): full rigid-body rod–rod MC with
the screened coat force law, registered scales only, robustness seeds + dt/2 probe. **It does NOT confirm
§14's shape: S_MC(1150) = 0.40 ± 0.06, S_MC(1500) = 0.37 ± 0.05 (dt/2 probe 0.30) — ~4–7× softer than the
deflection integral at cluster velocities.** The central-potential reduction missed multi-segment contact
accumulation and the torque channel; it was a lower bound on transport. **§14's "cluster ladder passes with
×3.5 margin" is RETRACTED** (this section corrects; §14 retained for the audit trail per house discipline).

Where it stands now: cluster total = 0.25 ± 0.04 (convention normalization) to ≈ 0.11–0.14 (MC-absolute
normalization, 0.54× convention, known-biased low by sampling truncation) — **×1.0–1.9 of the tightest
isotropy-calibrated bounds; a live marginal tension.** Group prediction updates to ≈ 0.1–0.3 (1.3–1.9σ below
Sagunski's mild 0.5 ± 0.2) — still the near-term discriminant. Dwarf pin, LSB, Bullet, np channel: all
unchanged, all pass. **χ at N ≈ 15–20: alive, not clean.**

Resolution now concentrates in: (a) MC refinement (sampling-disk truncation, J8 element-spacing pin, tumbling
temperature, dt convergence) → settle the normalization band [0.32, 0.59]; (b) **D4-C bound-applicability,
now operative** — the < 0.13–0.19 cluster limits assume isotropic point-particle scattering; rod DM's
anisotropic, rotational-channel transport must be mapped onto core-formation efficiency quantitatively.
J10 (MC systematics) registered. Queue: MC refinement → D4-C → CONFRONT-2 → formation-lane N → paper
integration (carrying the corrected floor story and the marginal tension honestly) → panel.

## 16. J8 pinned — the normalization was the artifact; cluster ladder passes by direct measurement; χ unobstructed (Patch 1871, 4 July 2026)

Registry pin (1812/0835): element pitch = corpus rung spacing **d ≈ 1.0–1.3 fm**; 1868's 4.7 fm conflated coat
radius with structural pitch. MC rerun at physical geometry (L(N=18) ≈ 20 fm; verify
`code/1871_soft_rod_mc_pinned_geometry.py`): **σ_T/m measured directly = 0.094–0.154 (50 km/s) → 0.027–0.044
(1500) cm²/g.** Cluster total ≈ 0.03–0.05 → **entire ladder passes, ×2.7–4.5 margin on Andrade — by
measurement, not composition.** The ε·0.11·N convention (1860) is superseded (it was the coat-fattened
side-projection at dwarf v — the true origin of 1868's 3% hit — overestimating transport ~4–6×): **paper
exposure registered for §5 integration.** Dwarf coring unaffected (capture-carried). Group ≈ 0.037–0.05 —
2.3σ below Sagunski, an undershoot that survived every floor treatment: **robust falsifier, final form:
group-scale σ/m ≈ 0.03–0.05.** D4-C stands down (σ_V/σ_T ≈ 0.9–1.2; rotational uptake 3–9%). **χ at
N ≈ 15–20: alive and unobstructed** — the capture channel was never touched by the floor arc. Correction
chain 1867→1869→1870→1871 closed and recorded. J8 closed; J10′ (MC bands: tumbling ×1.4, dt ×1.2) carried.
**Queue: CONFRONT-2 → formation-lane N → paper integration (capture + measured floor + falsifier + audit
trail) → panel.**

## 17. CONFRONT-2: consistent — gapped color-residual channel vs gapless |SSV| mode; de-novo target pinned at m_s = χ·(ħc/r_c) = 7.8 MeV (Patch 1872, 4 July 2026)

No conflict between R_s ≈ 25 fm (DM) and ξ ~ R_h (CC): channel decomposition — the screening is a GAPPED
response channel (m_s = ħc/R_s = χ·ħc/r_c = 7.764 MeV at η = χ), the CC coherence is the GAPLESS |SSV| scalar
(1107–1108); e^{−m_s r} cannot leak to cosmological r; D-FRAG spot check clean (rods = localized excesses,
baryon footing). **The de-novo derivation target is now sharp: a χ·(ħc/r_c) gap in the color-residual channel,
|SSV| scalar gapless — the gap in rung units IS χ.** Verify `code/1872_confront2_cc_xi_channel.py`; reasoning 1872.

## 18. Formation-lane scoping: kT_form ≈ 16.5 keV lands on the 0860 ≤19 keV hook — log-robust — but the N-cap must be kinetic; coincidence registered, not claimed (Patch 1873, 4 July 2026)

Isodesmic equilibrium inversion (all inputs pinned): ⟨N⟩ = 15–20 ⟺ kT_form = 16.2–16.6 keV, insensitive to
the occupancy judgment. Kinetic check: rate/H ≈ 10⁵ there — equilibrium tracks, so the cap is kinetic or
collisional (candidates: re-equilibration shutoff, virialization tail-pruning, or smaller E_b within the 0860
window — the last inverts into an E_b selection worth a dedicated arc). Verify
`code/1873_formation_lane_scoping.py`; reasoning 1873. **Queue: paper integration (founder-gated: §5 rewrite
carrying capture + measured floor + group falsifier + correction-chain audit) → CONV-001 panel.**

## 19. DM-1 v1.2 SHIPPED — panel 5/5, five changes folded; the de-novo gap is the standing gate (Patch 1876, 5 July 2026)

CONV-001 cycle complete on the v1.2-DRAFT (package Patch 1875): **five-member panel this round (ChatGPT, Grok,
Gemini, Copilot, DeepSeek) — 5/5 ratification** (3× RATIFY incl. Grok "SHIP" and DeepSeek "full ratification";
2× RATIFY-WITH-CHANGES), no RESTATE, no REFUTE. Per-claim: B (η = χ characterization), D (measured floor),
E (correction-chain disclosure) unanimous; A, C, F carry minor wording changes. All five requested changes
folded in Patch 1876: (1) `\smt` transport-observable macro (archival `\smm` body untouched); (2) J3′ labeled
a working synthesis; (3) J4 + density-integral conditionality stated in-claim; (4) process-why sentence;
(5) F1 phrased as a pre-registered disqualifier. **Attribution anomaly RESOLVED** (founder confirms 5 Jul: the slot-3 return was Gemini, which consistently misidentifies itself; the 5/5 stands unqualified). Returns:
`DM-1/review/reviews_v1.2_panel_returns.md`. **DM-1 is v1.2 SHIPPED.** OPEN-SS-43's remaining work is the
sharpened de-novo target (§17): derive the χ·(ħc/r_c) = 7.76 MeV gap in the colour-residual channel with the
|SSV| scalar gapless — the promotion gate beyond Layer-C. Secondary open threads: formation-cap mechanism
(§18), soft-MC refinements (J10′), F1 group-scale data watch.

## 20. CONFRONT-3 OPENED — the baryon sector (founder green-light; Patch 1878, 5 July 2026)

The campaign used the rod–nucleon coupling (np channel, 1866) and now confronts everything it implies
(verify: `code/1878_confront3_baryon_sector_scoping.py`; reasoning 1878; sources pinned in-header).
Scoping verdicts at the χ corner (a₀ = 0.17–0.23 fm; σ_n(0) = 3.6–6.4×10⁻²⁷ cm²): **CMB drag +
dwarf-gas heating PASS ×20** (≲10⁻²⁵, 2112.00707); **underground detectors INAPPLICABLE** — ~1200
atmospheric collisions at ~45% loss each thermalize the rods high in the atmosphere (the SIMP shielding
structure of 2209.04387; internally forced by the same coupling the np channel required); **XQC LIVE
TENSION** — XQC-effective σ_n(q = 2–11 MeV) = 0.4–3.7×10⁻²⁷ sits at the reported reach of the excluded
band at tens of GeV (Erickcek 2007; Mahdawi–Farrar 2017/18), but every published boundary is a
contact-interaction mapping and ours is a 7.76 MeV-mediator, 20 fm composite. **Arc task 1 (decisive):
recompute the XQC boundary for the light-mediator composite. Task 1 now outranks the de-novo gap in
priority — a live kill risk before a promotion gate.** Tasks 2–5: rod form factor; Earth-thermalized
population (Dewar-class); computed CMB drag; verdict + paper hook (DM-1 v1.3 / DM-3).

## 21. CONFRONT-3 task 1 — XQC EXCLUDES the registered coupling ×20–30; fork D5 opened: XQC survival and the np-selection claim are mutually exclusive (Patch 1879, 5 July 2026)

The published XQC exclusion is a contact mapping inapplicable to a light-mediator composite (Born diverges on
heavy nuclei), so the actual scattering was solved: partial-wave Numerov for V = ±A·E_rN·(r_c/r)e^{−r/R_s},
rod-extension-folded, Helm form factor, solver validated to 0.1% against the exact finite-k Born formula, full
pinned XQC exposure model (Erickcek 2007: 34-pixel layer stack, swept-volume normalization, Table-I bins,
per-bin sensitivities, >4 keV rate). Verify `code/1879_xqc_recomputation.py`; reasoning 1879.

**Verdict: 10,261–14,998 predicted in-band events vs 527 observed; 1,404–3,542 vs 60 above 4 keV — every bin
violated ≫5σ, both signs, both rod models. At the registered J4-additive nucleon coupling the χ-corner rod is
EXCLUDED as more than ~3.5% of local DM.** No numerical or astrophysical band approaches the factor 20–30.

**The fork (D5, founder-gated):** the saturated σ makes the escape logarithm-assisted — S_c ≲ 0.1 on the
nucleon coupling clears XQC — but the 1866 np-selection of N ≈ 15–20 (DM-1 v1.2 item (ii)) required S_c ≈ 1.
**Mutually exclusive.** D5-A: color-neutrality/dipole suppression of the nucleon coupling (natural estimate
(R_N/R_s)² ≈ 1.3×10⁻³; XQC clears ×10³; δa_np → invisible; DM-1 v1.3 must retract the np-selection argument —
N ≈ 15–20 then rests on floor ceiling + dwarf window + tail pruning). D5-B: additive coupling upheld —
candidate falsified as the DM at the χ corner. The mechanism question (does unipolar residual sourcing require
the rod's cage coherence, which color-neutral nucleons lack?) is the founder's to rule. **J11 (S_c) registered
as the baryon sector's load-bearing unknown. External release (OSF) HELD pending D5. CONFRONT-3 tasks 2–4
downstream of D5. Queue: D5 ruling → v1.3 under the chosen horn → CONFRONT-3 remainder → de-novo gap → panel.**

## 22. D5 resolved by landscape: one non-sterile survival island, and S_c = R_N/R_s lands dead-center — ruling D5-A′ adopted provisionally with derivation debt (Patch 1880, 5 July 2026)

Founder directive ("choose the choice that saves the candidate") executed as model selection by computation,
with the motivation recorded as survival-conditional (verify `code/1880_d5_sc_landscape.py`; reasoning 1880;
LZ pin 9.2×10⁻⁴⁸ @ 36 GeV, arXiv:2207.03764). The full-ladder S_c landscape: S_c ≳ 0.1 dead (XQC);
**S_c ∈ [~0.005, 0.05] ALIVE (Island I: XQC 46 events vs 527, rock-shielded from LZ, np invisible)**;
S_c ∈ (10⁻⁹, 0.003) dead (LZ — un-shielded; **the naive second-power dipole 1.3×10⁻³ lands here**);
S_c ≲ 10⁻⁹ alive-but-sterile (Island II). **Ruling D5-A′: first-power color-dipole, S_c = R_N/R_s = 0.035 —
the unique natural scale inside the unique non-sterile island.** Debts: derive the multipole order (must be
first power — maximally falsifiable from inside the theory); DM-1 v1.3 retracting the np-selection claim
(N ≈ 15–20 reverts to floor ceiling + dwarf window + tail pruning); panel re-consult. Signature space:
near-threshold XQC-class events ×11 below current data; thermalized atmospheric/crustal rod population.
J11 resolved-provisionally; **J12 registered (island-I residual pins: CRESST-surface/DAMIC-shallow/Dewar at
25 GeV — unpinned, island could shrink). Queue: J12 pins → v1.3 → panel → derivation debts. OSF HELD.**

## 23. J12 pinned — Island I survives the surface/Dewar ladder at the ruling point (Patch 1881, 5 July 2026)

Full-text pins (2112.00707/NFM18/NBN19/CRESST-s): Dewar-class channels NOT constraining at 25.3 GeV
(source-stated 0.5–10 GeV reach; barometric collapse of surface density, H ~ 9 km); CRESST-surface low-mass
scope; DAMIC-shallow SHIELDED at S_c = 0.035 (81 collisions), operative only at the island bottom edge
(S_c ≲ 0.01) where its 25-GeV floor is unpinned (J12′-a); Earth heating 0.16 GW vs 44 TW; XQC ε_th caveat
top-edge only. **Ruling point clears every pinned channel.** DM-3 signature registered: deep-Earth
thermalized rod population (n̄ ~ 2×10¹³ cm⁻³, center-concentrated). Verify `code/1881_...py`; reasoning 1881.

## 24. DM-1 v1.3 SHIPPED — panel 5/5; the retraction ratified unanimously; the epistemics ratified with a restatement, folded (Patch 1884, 5 July 2026)

Second five-member cycle: **5/5 ratification, no REFUTE** — unanimous on A (the retraction), E (J12
accounting), F (falsifiers). Ask D (judging the survival-conditional ruling's disclosure): Grok/Gemini/
DeepSeek-slot found it sufficient-to-exemplary ("transforms a fine-tuning vulnerability into a sharp,
maximally falsifiable target"); ChatGPT RESTATE + Copilot RWC folded — the teal notice now states the ruling
is PROVISIONAL, non-upgradable until the multipole order is derived, and overturnable by that derivation.
Also folded: tempered exclusion wording (reproduction invited); shielding-criterion coarseness +
island-existence-vs-edges + dipole-squared clarification; governance (promotion = both debts cleared + a
stability cycle with no load-bearing corrections; review-lessons record = this file). **Anomaly RESOLVED** (founder, 6 Jul: slot-5 was DeepSeek self-misidentifying, matching Gemini's v1.2 failure mode; 5/5 unqualified). Returns: `DM-1/review/reviews_v1.3_panel_returns.md`.
**DM-1 is v1.3 SHIPPED. Standing gates: m_s gap; multipole order; stability cycle. OSF decision returned to
the founder. Open threads: derivation debts (the campaign's remaining physics), DAMIC-floor pin (island
bottom edge), rod–nucleus MC refinement (Gemini, low-priority), F1/F5 data watch, formation cap, DM-2/DM-3.**

## 25. CONV-004 adopted — the debts become measurements; the SUBSTRATE INVERSION ARC opens (Patch 1886, 6 July 2026)

Founder methodological ruling (verbatim in `founders_voice/founder_ruling_measured_coefficients_2026-07-06.md`;
registered as CONV-004 in `todolist.md`): where substrate physics is unresolved, claim the structure and let
data fix the coefficients — Galileo before Newton — with MEASURED/DERIVED/CONJECTURED tags, an
overdetermination requirement, scope limited to derivation-premature sectors, and the derivation layer
retained as the standing goal ("the coefficient-free layer will fall faster, with the coefficients in place
and the unified theory confirming them by overdetermination"). **Under CONV-004 the campaign's two debts are
re-read as its first two substrate MEASUREMENTS: m_s = 7.76 MeV [MEASURED: halo ladder → gap; = χ·ħc/r_c] and
S_c ∈ [0.005, 0.05] ∼ R_N/R_s [MEASURED: XQC/LZ/shielding ladder → colour-singlet suppression].**

**SUBSTRATE INVERSION ARC (opened):** invert the full measured set {m_s, S_c, E_ee, ε, m_el, d, η = χ} into
the deep unknowns the founder named (DP density, lattice occupancy, ZBW amplitude, cancellation/superposition
factors). Deliverables: (1) the **existence region** — do substrate parameters exist producing ALL measured
values simultaneously? (non-empty and natural = the existence proof the founder's bet needs; EMPTY = a
structural falsification that legitimately kills the candidate); (2) the explicit **measured-vs-unknown
count**, kept visible per CONV-004; (3) **no-refit predictions** for F5, F6, the DAMIC-floor pin, and the
group point from the inverted substrate. Paper hook: "What the dark-matter data reveal about the DP Sea."
**Obligation carried: a v1.4 wording cycle** — the panel-ratified "derivation debt / non-upgradable-until-
derived" governance sentence must be revised to the measured-parameter framing and re-ratified (short cycle).
OSF: after the inversion existence proof + v1.4 + a stability cycle.

## 26. SI-1 shipped — ledgers, forward maps, three pre-scan inferences, NON-EMPTY existence preview (Patch 1887, 6 July 2026)

Task 1 of the inversion arc complete (`SI-1_unknowns_and_forward_maps.md`; verify `code/1887_...py`;
reasoning 1887). 8-unknown ledger vs 9-target ledger (CONV-004 tags); 7 forward maps from registered
structure (J-SI-1…5); honest counting: 6 hard / 8 unknowns, under-determined by 2 — pinned COMBINATIONS
stated. **Pre-scan inferences: α_e/α_q ≈ 6×10⁻³; C_r ≈ 2.5×10⁻⁴ (the Sea's colour-channel cancellation is
now a measured number); D_st = O(1) (singlets present a static leading moment).** Existence preview
(200k MC): **NON-EMPTY** — sensible region (α_q median 0.75; occupancy f_occ ~ 0.1, a sparse Sea; C_r
independently confined to the 10⁻⁴ decade). Kill-condition did not fire. **Queue: SI task 2 (tightened scan +
substrate table + no-refit predictions) → DM-1 v1.4 wording cycle → stability cycle → OSF.**

## 27. SI-2 — the portrait, the F7 corner, the predictions (Patch 1888, 6 July 2026)

Tightened scan (2M numpy samples, SI-1 criteria): **913 accepted — existence confirmed ×10 statistics.**
Portrait (16/50/84, prior-shaped entries flagged): α_q = 0.89 (0.35–2.3); α_e = 5.5×10⁻³;
**C_r = 2.4×10⁻⁴ (0.6–8.7×10⁻⁴)**; D_st = 0.34 (0.15–0.67; window-softened from the center-point ≈1);
**f_occ = 0.10 (sparse Sea)**; X1 = n·S_p/Ez pinned to a decade. **F7-conditional corner EXISTS** (E_z ≈ 16
keV ⇒ f_occ ~ 4×10⁻³, n ~ 3×10⁻³ fm⁻³, S_p ~ 0.04 — very sparse, weakly coherent). **No-refit predictions:**
F5 XQC-reflight 46 events at the ruling point (×11) / 2–28 region-weighted (median ×98); F6 n̄ ~ 2×10¹³ cm⁻³;
**DAMIC edge: 40% of the region unshielded — the future pin adjudicates it**; group 0.037–0.05 standing.
Verify `code/1888_...py` + XQC grid json; reasoning 1888. **Queue: DM-1 v1.4 wording cycle → stability
cycle → OSF.**
