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

## 28. v1.4-DRAFT + short-cycle package (Patch 1889, 6 July 2026)

Brown notice drafted: CONV-004 supersession of the v1.3 governance sentence (debts → MEASUREMENTS;
**F3′ kill-branches retained undiminished and stated so in-notice**); SI-1/SI-2 folded (inferences, portrait
with prior-shaped flags, F7 corner, non-empty existence with pre-registered kill-condition); falsifiers
updated (F5 dual-form; DAMIC edge 40%; F6; group); governance revised (overdetermination discipline +
stability cycle + open derivation target). Compile clean. Package
`DM-1/review/DM-1_review_package_v1.4.md`: asks A–D; §5 invites the unfalsifiability attack on CONV-004
itself. Queue: panel → fold → ship → stability cycle → OSF.

## 29. v1.4 SHIPPED — panel 5/5; CONV-004 survives its own invited attack; the stability-cycle clock starts (Patch 1890, 6 July 2026)

Third five-member cycle: **5/5** (Grok "SHIP"); unanimous on the SI discipline and the falsifiers; **every
reviewer returned the invited unfalsifiability attack on CONV-004 in the programme's favor** — the
overdetermination rule + retained kill-branches judged sufficient ("falsifiability bookkeeping, not an
escape"). Folded: the provisional-empirical-anchors sentence with the anti-semantic-drift guard (measured ≠
established); the governance hard rules (no MEASURED→DERIVED promotion without an independent derivation
preserving the confrontation ledger; Layer-C promotion = one full no-supersession stability cycle +
independent-channel overdetermination — "so governance cannot keep moving the goalposts"). Queued: F5
D_st-prior sensitivity check (SI follow-up). No attribution anomaly this cycle. Returns:
`DM-1/review/reviews_v1.4_panel_returns.md`. **DM-1 is v1.4 SHIPPED. THE STABILITY-CYCLE CLOCK STARTS AT
THIS PATCH — OSF release on its completion. Open threads (none load-bearing): D_st sensitivity, DAMIC-floor
pin, rod–nucleus MC refinement, formation cap, F1/F5 data watch, the standing derivation target, DM-2/DM-3.**

## 30. Hardening — DAMIC adjudication fires as pre-registered; island trims to [0.012, 0.05]; D_st concern discharged; F5 sharpens (Patch 1891, 6 July 2026)

Bounding confrontation (MF17/MF18/1510.02126 pins; no digitization needed at ≥10³ margin): the unshielded
corner (S_c < 0.0124) carries σ_n = 2×10⁻³³–3×10⁻³¹ — inside DAMIC-shallow's excluded band. **Island trims
to S_c ∈ [0.012, 0.05]; ruling point untouched. NOT a correction — the v1.4 notice pre-registered exactly
this adjudication; paper untouched; stability cycle stands.** D_st-prior sensitivity (queued at v1.4):
discharged — trimmed-window F5 prior-robust across 1.5 orders: **8–50 events, median ~17, margin ×30**
(ruling-point form 46/×11 unchanged); refreshed figures to the OSF-deposit addendum. Verify
`code/1891_...py`; reasoning 1891. **Queue: OSF deposit package → reader's guide → cycle completion →
release.**

## 31. OSF deposit record prepared (Patch 1892, 6 July 2026)

`DM-1/documentation_suite/osf-deposit-DM-1.md` (house format): DOI versioning vs parent JXE8D + the 8 June
conjecture priority chain; honest-scope abstract (near-kill and PROVISIONAL ruling disclosed in-abstract);
full manifest (paper, campaign, SI-1, founder ruling, 49 scripts, 63 reasoning fragments, 3 review cycles
verbatim); **the stability-cycle completion criterion as an objective five-box checklist** (≥14 d or 2
sessions; zero load-bearing corrections, 1891-precedent carve-out for pre-registered adjudications; no
standing REFUTE; residual scan; founder sign-off); the 1891 addendum text (island [0.012, 0.05]; F5 8–50,
median ~17, ×30). Paper untouched; cycle intact. **Queue: reader's guide (item 3) → cycle completion →
deposit.**

## 32. Reader's guide written — the release plan's three items are complete (Patch 1893, 6 July 2026)

`DM-1/readers_guide.md`: the cold-reader companion — five-input table (ontology-independence stated), the
claim led by χ's prior provenance, both near-kills told straight (incl. both retractions), the
measured-coefficient turn with printed counting, the ordered kill list, a 30-minute audit path (1865 →
1871 → 1879 → 1888), and the objections we agree with. Deposit manifest updated (item 8 + wiki front page).
**Release plan complete: hardening ✓ (1891), deposit package ✓ (1892), reader's guide ✓ (1893). Remaining:
the stability-cycle clock → closing residual scan → founder sign-off → deposit.**

## 33. DM-2 opened (re-scoped for the rod era) — pointer (Patch 1894, 6 July 2026)

DM-2 campaign opened at `sea_gravitation/dm2_rod_era_rescoping.md`: June-era state mapped (A→D no-kill;
0722-derived Λ-suppression 0.46× observed; CC unification) and NOT re-opened; rod-era legs defined — L1 rod
equivalence (coat-budget vs inertial mass; CONFRONT-4 in spirit), L2 portrait-budget confrontation (Sea
budget = 10³⁹–10⁴²× ρ_Λ ⇒ zeroing must be exact; import verdict: ρ_Λ is consistency, not an SI target,
under the registered coefficient). Arc order L1 → L2 → Gate-1/D3 carry → paper → panel. DM-2 sessions run
this paper's stability clock. **[L1 PASS, Patch 1895: m_grav = m_inertial to 3×10⁻⁵ (coat ≤ 0.6 MeV
unledgered vs 25.3 GeV; margin ≥ 600) — every DM-1 gravitational anchor correctly normalized.]**

## 34. Q3c RE-AIM — the campaign re-scoped for the panel-verified ring family (Patch 2388, 9 July 2026)

**What changed since §33:** the population arc (OPEN-DM-DSPH-1, patches 2312–2387) killed the
dimer branch (2369, ratified with ε_th conditionality), derived a replacement population from
registered nucleation kinetics (2381–2383), and the derived family was **PANEL-VERIFIED**
(2384 round, 3× convergent, one re-executing seat; adjudicated 2387). The family is
**N = 6-dominant closed RINGS at ≈ 8.45 GeV** (companions 5, 7; kinetic placement
r = ℓ_p/ℓ_rung ≈ 8.5–12), floor-anchored in coupling — NOT the rod-era N ≈ 15–20 / 25.3 GeV
picture this campaign calibrated (§§6–32). This section re-aims the campaign's standing
targets at the verified family. Rod-era results are NOT retracted; each is tagged below as
carrying over or as rod-specific pending recompute.

### 34.1 The inherited demands (from 2383/2385/2387, all derived, none imposed)

| Demand | Value | Source |
|---|---|---|
| R_s | ∈ [20, 51] fm (anchor joint passes) | 2383_joint_couplings |
| S_c | floor-anchored: alive at 0.012, DEAD at 0.035 — fine wall S_c* owed | 2383 XQC |
| Sign | ARGUMENT-LEVEL attractive default (1858 E_qq); derivation owed here | 2383/F-A2 |
| Masses | 8.45 GeV dominant (N = 6); 7.04 / 9.86 companions | 2383 |
| Also carried in Q3c (not this campaign's channel) | N_stab = c·κ/(ℓ_rung·E_bond) ∈ ≈ [3.3, 7.3] + the F-A1 substrate-constancy theorem | 2382/2385 |

### 34.2 The reconciliation ledger — carries over vs rod-specific

**Carries over intact:** the channel decomposition (§17: gapped color-residual vs gapless
|SSV| — geometry-independent); the de-novo gap target m_s = χ·ħc/r_c = 7.76 MeV ⇒
R_s = 25.4 fm (Route B, N-flat — sits INSIDE the demanded [20, 51] band); the S(v)/soft-MC
methods (1869–1871); the CONFRONT method suite; the 1879 XQC pipeline (it graded the ring
family directly); CONV-004 measured-coefficient discipline.

**Rod-specific, pending recompute or superseded-in-part:** the N ≈ 15–20 selection chain
(floor ceiling + dwarf window + tail pruning) — superseded by the kinetic derivation's
N = 5–7 band; the dwarf-coring capture calibration at N = 15–20 (the dSph channel is now
carried by the 2371/2383 anchor machinery at the audited frames, which the ring family
passes); the group falsifier value 0.03–0.05 (rod floor at N = 18 — recompute for rings);
CONFRONT-1/3 numbers at 8N = 144–160 qCP (ring 8N = 40–56 — recompute); the D5-A′ ruling
point S_c = 0.035 (see C1).

### 34.3 The named collisions — where the derivation must land or the family dies

**C1 — the S_c gap (the sharpest number in Q3c).** The ring family is XQC-DEAD at the rod
era's natural scale S_c = R_N/R_s = 0.035 and ALIVE at the island floor 0.012 — a ×2.9 gap.
Either (i) ring topology supplies additional colour-singlet suppression beyond the rod's
first-power dipole (the closed cage's multipole structure — plausibly the same coherence
argument that carried D5-A′, taken one order further by closure), or (ii) the derived
coupling lands above S_c* and the family dies at the gate FULLY DERIVED — the third kill via
the D5 lineage. Note the island itself is [0.012, 0.05] (1891): the ring demand sits at its
bottom edge; DAMIC-floor behavior at the edge (J12′-a) becomes relevant again.

**C2 — Route C is now killable.** Source-coherence screening (R_s ≈ N·d_el) gives
R_s ≈ 6–12 fm at N = 6 — BELOW the demanded [20, 51] band at every anchor. The ring demand
selects the N-FLAT route (B, medium property): the de-novo gap derivation IS the R_s
deliverable, and its pre-registered kill stands — a √χ response order gives R_s ≈ 5 fm,
outside the band, weak-SIDM fallback per the v1.1 falsifier.

**C3 — CONFRONT-1 re-arms at ring composition.** Pairwise-additive E_NN ∝ 1/(8N)²: the ring
N = 6 gives ×(144/48)² ≈ ×9 the per-pair rod residual at N = 18. The np channel that
selected-then-released N must be recomputed at the ring point under the D5-A′
colour-suppressed coupling — cheap, and it can kill.

**C4 — the sign, decomposed by channel.** The registered structure ALREADY contains both
signs: the E_qq capture residual (attract-only, 1858 — the 2383 default) and the E_ee coat
channel (REPULSIVE, the measured floor, 1868–1871). The derivation owed is the effective
TRANSFER sign entering each graded channel for ring–ring and ring–nucleus scattering — i.e.,
which channel dominates σ_T at dwarf velocities and at XQC momentum transfer for the closed
ring (whose saturated bonds plausibly enhance the repulsive coat share). Deliverable: the
per-channel sign with the 2383 corridor re-graded on it (machinery standing). This
discharges F-A2's ARGUMENT-LEVEL tag in whichever direction it lands.

### 34.4 Stage plan (cheap-kill order; each stage carries its kill)

- **SS43-Q1 — the fine wall (1 session, existing machinery).** Pipeline S_c* bisection for
  the N6-dominant members (ε_th = 1 + floor-bracket robustness): turn "floor-anchored" into
  the quantitative landing window [0.012, S_c*]. Kill statement: the window IS the target
  C1's derivation must hit.
- **SS43-Q2 — ring multipole pass (1–2 sessions).** Does closure suppress the nucleon
  coupling beyond the rod's first power? Target ≥ ×2.9 at the ruling R_s. KILL: no extra
  suppression ⇒ S_c(ring) = 0.035 > S_c* ⇒ gate-death, fully derived.
- **SS43-Q3 — CONFRONT-1/3 recompute at ring composition (1 session).** np length + XQC +
  shielding ladder at N = 5–7, w from 2383, under Q2's coupling. KILL: np or ladder
  violation at every S_c in the Q1 window.
- **SS43-Q4 — the de-novo gap (the physics core; weeks-scale).** Derive m_s = χ·ħc/r_c:
  linear-in-χ response order in the colour-residual channel, |SSV| gapless (§17 target,
  standing since 1872). Delivers R_s = 25.4 fm into the [20, 51] demand. KILL: √χ order
  (R_s ≈ 5 fm) — pre-registered.
- **SS43-Q5 — sign synthesis + corridor re-grade (1 session on Q4/Q2 output).** Per-channel
  transfer sign for rings; re-run the 2383 corridor on the derived sign; F-A2 tag resolved.
- Held behind these: the group-falsifier recompute for rings; the F-A1 constancy theorem
  (OPEN-FP-SF-2-η side); registration of the family as successor branch (founder,
  post-rent).

### 34.5 Exits and rent

Clause 1(a) binds this leg directly: if the derivation excludes every suite-passing region,
the hypothesis takes the exit. The newly attested (d′) binds post-registration at 8.45 GeV.
Every stage above is a registered-primitives computation or derivation; no dark-sector
freedom is introduced at any stage (0865 held).

### 34.6 SS43-Q1 CONTRACT + WARM-LAUNCH REGISTRATION (Patch 2389, 9 July 2026)

**Warm-launch keyword: DM-WARM-2389.** Founder verbatim: "Initiate handover protocol for
SS43-Q1."

**Handover set (self-contained):** this file §34 (the re-aim, collisions, stage plan, and
this contract); `code/2383_results.json` (member weights + XQC ρ* rows) +
`code/2383_joint_couplings.json` (the six joint members); the committed
`code/2379_unit_cache.json` (360 keys); the bisection engine
`code/1879_xqc_recomputation.py`; arc-doc context = `sN_arc_2370_cost_estimate.md`
§Q3b-2c through §Patch-2388.

**SS43-Q1 pre-registered scope (the fine wall — the 2383 deferred debt):**
pipeline-level S_c* bisection for the six 2383 joint members (N6-dominant class) at
ε_th = 1, BOTH signs, ρ ∈ {0.2, 0.3}; floor-bracket ε_th robustness read from the cache
(already computed). Output: the quantitative landing window **[0.012, S_c*(member, sign,
ρ)]** — the numeric target collision C1's derivation (SS43-Q2) must hit. Bisection
tolerance 0.001 in S_c; every fresh pipeline point appended to the committed cache.

**Verify battery (binding):** V1 the 2381/2382/2383 batteries green underneath
(subprocess); V2 bisection bracket endpoints reproduce the cached grid verdicts
(alive at 0.012, dead at 0.035, per member/sign/ρ); V3 worst-ratio monotone
non-decreasing in S_c along each bisection path (the physical sanity that makes
bisection valid); V4 cache integrity after extension (schema + count).

**Scope guard:** no verdict moved; the wall is an input to Q2, not a grading. Expected
cost: one session (~170 pipeline calls ≈ 10 min compute + write-up). KILL statement
carried from §34.4: the window IS C1's target; if Q2's derived ring suppression lands
S_c above every member's S_c*, the family gate-dies fully derived.

**Next session opens with SS43-Q1 on the keyword; the founder's verbatim go completes
the launch.**

### 34.7 SS43-Q1 EXECUTED — the fine wall (Patch 2391, 9 July 2026)

**Launch:** DM-WARM-2389 keyword + founder's go ("Shall SS43-Q1 proceed there?").
Contract §34.6 executed as pre-registered: pipeline-level S_c* bisection, six 2383
joint members, ε_th = 1, both signs, ρ ∈ {0.2, 0.3}, tolerance 0.001; every fresh
point appended to the committed cache (360 → 475 keys; 115 fresh calls, under the
~170 budget). Script `code/2391_ss43_q1_fine_wall.py`; results
`code/2391_results.json`. **Battery 4/4 PASS** (V1 underneath 2381 6/6, 2382 7/7,
2383 5/5; V2 all 48 endpoint verdicts + stored ρ* rows reproduced at rel 0; V3
worst-ratio monotone in S_c on all 12 paths / 112 sampled points — bisection valid,
not merely convergent; V4 original 360 cache keys byte-identical, +115, round-trip).

**Pre-flight repair owned in-session (Patch 2390):** the 2381 V5 cache check pinned
an exact 336-key count, falsified by the cache's own registered growth (2383's
committed above-floor extension to 360; this task's contract appends more). Repaired
to the invariant form — floor bracket complete (320/320), 13-bin schema for every
key, count monotone ≥ 336 — machinery-catches-author, pre-commit, no verdict content
touched.

**The wall (S_c* = alive end of the 0.001 bracket; window = [0.012, S_c*]; required
C1 suppression = 0.035/S_c* from the rod-natural scale):**

| Member | Composition | attr ρ=0.2 | attr ρ=0.3 | rep ρ=0.2 | rep ρ=0.3 |
|---|---|---|---|---|---|
| A | {6: 1.0} | 0.0170 (×2.06) | 0.0142 (×2.47) | 0.0206 (×1.70) | 0.0163 (×2.15) |
| B | {5:.166, 6:.781, 7:.053} | 0.0163 (×2.15) | 0.0134 (×2.60) | 0.0192 (×1.82) | 0.0156 (×2.24) |
| C | {6:.658, 7:.326, 8:.016} | 0.0177 (×1.97) | 0.0149 (×2.35) | **0.0221 (×1.59)** | 0.0170 (×2.06) |
| D | {4:.012, 5:.276, 6:.543, 7:.157, 8:.012} | 0.0156 (×2.24) | 0.0127 (×2.75) | 0.0192 (×1.82) | 0.0149 (×2.35) |
| E | {4:.027, 5:.415, 6:.474, 7:.084} | 0.0149 (×2.35) | **0.0120 (×2.92)** | 0.0177 (×1.97) | 0.0142 (×2.47) |
| F | {4:.015, 5:.595, 6:.377, 7:.014} | 0.0142 (×2.47) | DEAD-AT-FLOOR | 0.0170 (×2.06) | 0.0134 (×2.60) |

**Reading (no verdict moved — the wall is C1's input):**
- **S_c* spans [0.0120, 0.0221].** The §34.3 "×2.9 gap" was the floor-referenced
  worst case; the fine wall grades it. Q2's derived ring suppression lands the WHOLE
  surviving table at ≥ ×2.92; it keeps at least one joint-(c) cell alive at ≥ ×1.59
  (member C, repulsive, ρ=0.2 — the loosest wall). Between those, the family narrows
  member-by-member instead of dying whole; the kill carried from §34.4 fires only if
  the derived S_c exceeds 0.0221.
- **Loosest walls by branch:** (c) repulsive ρ=0.3 → 0.0170 (×2.06); (d) attractive
  ρ=0.2 → 0.0177 (×1.97). The repulsive coat channel is uniformly the more forgiving
  target — consistent with its smaller per-unit XQC yield in the cache.
- **Two floor-edge facts, faithfully carried:** F(attr, ρ=0.3) has no window — its
  floor ρ* = 0.2969 < 0.3, i.e., F carried joint (d) at ρ ≥ 0.2 only in 2383; and
  E(attr, ρ=0.3)'s wall sits essentially AT the floor (S_c* = 0.0120, floor
  ρ* = 0.3244) — the J12′-a DAMIC-edge caution in §34.3 applies to that cell first.
- ε_th floor-bracket robustness (min ρ* over the 5-point bracket, read from the
  committed cache, not recomputed) is recorded per member/sign in
  `2391_results.json` (`floor_bracket_rho_star_min_over_eth`).

**Hand-off to SS43-Q2 (ring multipole pass):** the quantitative landing window is
now numeric per cell. Q2's deliverable is a DERIVED ring S_c; the grading against
this table is mechanical. Stage plan §34.4 unchanged; Q3 (CONFRONT recompute) and
Q4 (de-novo gap) queue behind Q2 as registered.

### 34.8 SS43-Q2 CONTRACT + WARM-LAUNCH REGISTRATION (Patch 2392, 9 July 2026)

**Warm-launch keyword: DM-WARM-2392.** Founder verbatim: "draft Q2 contract and initiate
handover protocol."

**Handover set (self-contained):** this file §34 (re-aim §34.1–34.5, Q1 contract §34.6,
the executed wall §34.7, this contract); §22 (the D5-A′ provisional ruling and its
standing derivation debt — the multipole-order question Q2 inherits one order further);
§17 (the channel decomposition, geometry-independent, carries over per §34.2);
`code/2391_results.json` (the wall + per-path traces); the committed
`code/2379_unit_cache.json` (475 keys); the grading engine
`code/1879_xqc_recomputation.py`; `code/2383_results.json` +
`code/2383_joint_couplings.json` (the six members and their weights); arc-doc context
`sN_arc_2370_cost_estimate.md` §Q3b-2c through §Patch-2388.

**SS43-Q2 pre-registered scope (the ring multipole pass — collision C1's derivation):**
derive, from registered primitives only (0865 held — no dark-sector freedom at any
step), the colour-singlet nucleon-coupling suppression of the CLOSED N-ring relative to
the rod's first-power dipole (the D5-A′ scale S_c = R_N/R_s = 0.035), at the ruling R_s,
for the ring compositions N = 4–8 where composition matters. The physical question, as
named at §34.3 C1: does closure — saturated bonds, no free ends, closed colour
circulation — take the D5-A′ coherence argument one order further? Deliverable: the
DERIVED ring S_c (or equivalently the derived suppression factor vs 0.035), with the
derivation chain written and every coefficient traced.

**Grading (mechanical, pre-registered against the §34.7 wall — no adjustment permitted
after the derived number exists):**
- derived S_c ≤ 0.0120 → the WHOLE surviving table lands (all 23 walled cells);
- 0.0120 < derived S_c ≤ 0.0221 → partial landing; cell-by-cell readout against the
  §34.7 table; the family narrows member-by-member, faithfully recorded;
- derived S_c > 0.0221 → **gate-death fully derived** (the kill carried from §34.4 —
  the third kill via the D5 lineage).
Adjacency, not obligation: if the same machinery resolves the ROD's multipole order in
its open-chain limit, record it against the 1880 D5-A′ derivation debt; discharging
that debt is NOT required for Q2 completion.

**Verify battery (binding):**
- **V1** the 2391 battery green underneath (subprocess; carries 2381/2382/2383
  transitively).
- **V2 rod-limit readout (MANDATORY, escalation-typed):** the multipole machinery's
  open-chain limit order is computed and REPORTED. Agreement with the D5-A′ first power
  = PASS. Disagreement is NOT a silent fail — it is a BLOCKING flag escalated to the
  founder, because it collides with the 1880 provisional ruling and its landscape
  (second power = the LZ dead zone, a registered kill). No grading proceeds past an
  unresolved V2 collision.
- **V3 grading reproduction:** the derived S_c's alive/dead verdicts via fresh pipeline
  calls match the §34.7 wall-table brackets (alive below each cell's S_c_alive, dead
  above its S_c_dead) on a pre-declared spot-check set spanning both signs and both ρ.
- **V4 no-freedom audit:** every coefficient in the derivation chain traced to a
  registered primitive, itemized in the reasoning fragment (0865 discipline; CONV-004
  measured-coefficient tags where a measured quantity enters).
- **V5 cache integrity** (schema + original keys byte-identical + append-only) if any
  fresh pipeline points are computed.

**Exits and rent:** Clause 1(a) binds this leg directly; the attested (d′) binds
post-registration at 8.45 GeV; every stage is registered-primitives derivation or
computation (0865 held). Scope guard: verdict moves ONLY by the mechanical grading
above or by founder adjudication of a V2 collision.

**Expected cost:** 1–2 sessions (§34.4 estimate stands: derivation-heavy; the pipeline
grading is cheap on the extended cache). KILL statement carried: no extra suppression
from closure ⇒ S_c(ring) = 0.035 > 0.0221 ⇒ the family gate-dies fully derived.

**Next session opens with SS43-Q2 on the keyword; the founder's verbatim go completes
the launch.**

### 34.9 SS43-Q2 EXECUTED — the ring multipole pass lands a DICHOTOMY, graded both ways (Patch 2393, 10 July 2026)

**Launch:** DM-WARM-2392 keyword + founder verbatim go ("Please proceed as per your
recommendation"). Contract §34.8 executed as pre-registered. Script
`code/2393_ss43_q2_ring_multipole.py`; results `code/2393_results.json`; reasoning
`reasoning/2393.md` (verbatim, at-patch — the full chain including a retracted
refutation and a rejected measured-coefficient route). **Battery 5/5 PASS** (V1
underneath 2391 4/4 transitive; **V2 rod-limit PASS — no escalation**; V3 12/12
spanning cells at fresh pipeline calls; V4 twelve coefficients traced, 0865 held;
V5 cache 475 byte-identical, +115 schema-pure flat appends, 20 ring-form calls
kept out of the cache by schema).

**The derived answer:** the registered primitives fix the machinery's boundary
conditions (the two D5-A′ data points: rod source side power-0; nucleon side
power-1) but **underdetermine the per-unit vertex class between exactly two
survivors** — both reproduce both data points:

- **Class S (scalar per-qCP additive — the registered 1879 line-fold's own
  composition law; 1858 unipolarity: magnitude cannot cancel by arrangement).**
  Closure supplies NO suppression: the ring is a single-shell fold at
  R_g = d/(2 sin(π/N)) (J8 pin d = 1.15 fm), and the XQC-equivalent flat
  **S_c = 0.0356 for every member and both signs** (form factor ≈ +0.6% on the
  ruling scale). **Grading: > 0.0221 → GATE-DEATH FULLY DERIVED** (the §34.4
  kill, landed by the registered model's own law).
- **Class V-t (chain-axis vector — the D5-A′ ruling's mechanism language
  "coherent cage"/"lacking cage coherence" made operational; the chain/rung axis
  is the rod's only registered coherence axis, 2381; no torsional lock registered
  → no transverse component admitted, 0865).** Two EXACT identities: closed-loop
  telescoping (Σ edge-differences = 0 identically; verified at machine precision)
  and orientation-average orthogonality (⟨t̂·∇Y⟩ ∝ t̂·x̂ = 0 exactly on the ring —
  tangent ⊥ radius) — under the registered fold convention the ring
  **decouples IDENTICALLY, near zone included**; the open-chain limit telescopes
  to END-SOURCED coupling: **the free ends ARE the coupling and closure removes
  them** — the contract's named question answered in mechanism. Conservative
  |V|-envelope bracket (ℓ_v fixed by deterministic rod-limit integral matching,
  one condition one parameter; rod consistency ×0.73–1.35 reported not fitted):
  **equivalent flat S_c ≤ 0.0014.** **Grading at both bracket ends: ≤ 0.0120 →
  WHOLE TABLE LANDS (all 23 walled cells).**

**V2 (escalation-typed): PASS.** Both classes give source-side power-0 in the
open-chain limit (Class V-t: end-sourced, saturating, log-log slope 0.106 — no
suppression power) → total = FIRST power = D5-A′. No 1880 collision. Adjacency
recorded against the 1880 debt (not discharged): under V-t the rod's power-0 is
END-sourced O(N⁰), not bulk-∝N — a substrate-level discriminant for the future
vertex derivation.

**Carried flags (no verdict moved — scope guard held):**
- **Below-floor flag (Class V-t):** the landing sits BELOW the island floor 0.012
  (1891 trim). Rod-era below-floor kills (DAMIC-unshielded, LZ dead zone) were
  derived for the flat long-range form; a collapsed/contact-range coupling is a
  different scattering object. **The LZ/shielding/DAMIC recompute at the derived
  coupling is Q3's registered job and is now LOAD-BEARING on this branch.**
  J12′-a attaches.
- **Anchor-channel consequence (for C4/Q5):** under V-t the ring–ring E_qq vertex
  collapses too — the dwarf anchors fall to the E_ee coat channel (repulsive,
  measured, 1868–1871), CONSISTENT with 2383's six repulsive joint points, §34.7's
  repulsive-walls-are-loosest finding, and C4's own anticipation.
- **1858 reconciliation (stated in full in the reasoning):** the telescoping is a
  coherence projection of the VERTEX, not sign-cancellation of the FORCE; E_qq
  remains attract-only between nonzero-vertex bodies; 1858 stands.
- **Rejected route recorded:** the 2383 per-species g² anneal pass-points span
  eight orders of magnitude — an existence witness, not a CONV-004 measurement;
  using them to pin the vertex would manufacture precision. Consistency brackets
  only; both branches sit inside the admitted region.

**FOUNDER'S DESK — the class adjudication (the campaign's sharpest open object):**
(a) adopt Class V-t (the ruling's own mechanism language): whole wall cleared
fully derived; survival shifts to Q3's below-floor recompute + Q5's coat-channel
sign synthesis; (b) adopt Class S (the pipeline's own composition law): gate-death
fully derived — the third kill via the D5 lineage; (c) hold the dichotomy open and
let Q3/Q4 discriminate — Q4's de-novo gap derivation is exactly the substrate
mechanics that would DERIVE the vertex class. No recommendation smuggled; the
derivation says the registered primitives genuinely do not decide, and says why.

### 34.10 CLASS ADJUDICATION RULED (c) + SS43-Q3 CONTRACT + WARM-LAUNCH REGISTRATION (Patch 2394, 10 July 2026)

**Founder ruling on the §34.9 dichotomy: option (c) — HOLD OPEN, let Q3/Q4 discriminate.**
Verbatim: "please proceed as recommended" (on the recommendation whose stated content was
(c) + Q3 next; recorded in `reasoning/2394.md`). No vertex class is adopted; neither
branch's grading is promoted; the dichotomy is the campaign's registered live fork.

**Warm-launch keyword: DM-WARM-2394.**

**Handover set (self-contained):** this file §34 (re-aim §34.1–34.5; the wall §34.7; the
Q2 result §34.9; this contract); §22 (D5-A′ + the 1880 landscape whose ladder this task
re-runs); `code/2393_results.json` + `code/2393_ss43_q2_ring_multipole.py` (the two
vertex classes, the ring-form potential machinery, the envelope); `code/1880_d5_sc_landscape.py`
(the full baryon ladder: XQC / rock-overburden shielding / LZ / np / CMB — the machinery
this task re-parameterizes); `code/2391_results.json` (the wall); the committed
`code/2379_unit_cache.json` (590 keys); `code/1879_xqc_recomputation.py` (engine);
`code/2383_joint_couplings.json` (the six members); arc-doc context §Q3b-2c → §Patch-2393.

**SS43-Q3 pre-registered scope (CONFRONT-1/3 recompute at ring composition — the
dichotomy's cheap discriminator):** re-run the FULL 1880 baryon ladder at the ring
family's registered parameters (masses N·1.408 GeV, N = 4–8; member weights from 2383;
ring geometry from 2393), PER CLASS:
- **(i) Class V-t branch (the decisive leg — the §34.9 below-floor flag made
  load-bearing):** the ladder at the COLLAPSED coupling, using the actual ring-form
  potential (2393 machinery: identity zero + envelope bracket), NOT the flat-S_c
  long-range form the rod-era dead-zone logic assumed. Channels: rock-overburden
  shielding collision count at ring masses; LZ σ_n at Xe-recoil momenta with the
  ring-form amplitude; DAMIC-shallow at ≈ 8.45 GeV (the J12′-a edge, now at LOW mass —
  the 25-GeV floor pin does not transfer; a fresh low-mass reach pin is a NAMED data
  action inside this task); np channel at ring composition (C3 re-arm: per-pair
  E_NN ∝ 1/(8N)², ×9 the rod per-pair at N = 6); CMB drag.
- **(ii) Class S branch (bookkeeping leg):** the branch is already XQC-gate-dead
  (§34.9); record the remaining ladder rows at S_c = 0.0356 for completeness of the
  kill's derivation chain — cheap, no bisection.

**Grading (mechanical, pre-registered — no adjustment after the numbers):**
- **(a)** V-t branch fails ANY ladder channel at both bracket ends (identity 0 AND
  envelope ≤ 0.0014) → the V-t branch is DEAD → with Class S gate-dead (§34.9), **the
  family is dead on BOTH classes, fully derived, adjudication moot** — the third kill
  via the D5 lineage lands regardless of the vertex question; Clause 1(a) exit engages
  on the founder's desk.
- **(b)** V-t branch clears EVERY channel at both bracket ends → the family is **alive
  on the V-t class only**; the class fork becomes the campaign's single live question;
  Q4 (the de-novo gap, which must also derive the vertex class from substrate
  mechanics) is the registered discriminator; Q5 (coat-channel sign synthesis) queues
  on the anchor side.
- **(c)** Split verdicts between the bracket ends (identity passes, envelope fails, or
  channel-conditional) → recorded faithfully channel-by-channel; the conditionality
  becomes a named pin/derivation demand; no smoothing.

**Verify battery (binding):**
- **V1** the 2393 battery green underneath (subprocess; carries 2391 → 2381/2382/2383
  transitively).
- **V2 rod-era ladder reproduction (PASS-GATE):** before any ring point is graded, the
  re-parameterized ladder machinery must REPRODUCE the registered 1880 landscape
  verdicts at the rod point (N = 18, 25.3 GeV, flat S_c grid incl. 0.035 ALIVE and
  1.3×10⁻³ dead-LZ). Failure = machinery not trusted; no grading proceeds; fix or
  escalate.
- **V3 grading reproduction:** ring-point verdicts reproduced by fresh calls on a
  pre-declared spot-check set spanning both classes and both V-t bracket ends.
- **V4 no-freedom audit:** every coefficient traced (0865 held; CONV-004 tags where
  measured quantities enter — the DAMIC low-mass pin will be one).
- **V5 cache integrity** (schema-pure appends only; ring-form calls stay out).

**Exits and rent:** Clause 1(a) binds — grading branch (a) puts the exit on the
founder's desk fully derived. The attested (d′) binds post-registration at 8.45 GeV.
Scope guard: verdict moves ONLY by the mechanical grading above; the class adjudication
itself stays HELD per the founder's (c) ruling — Q3 can moot it or sharpen it, not
decide it by preference.

**Expected cost:** 1–2 sessions (ladder machinery exists at 1880; ring-form machinery
exists at 2393; the DAMIC low-mass pin is the one data action). KILL statement carried:
grading branch (a) = the family dead on both classes, fully derived.

**Next session opens with SS43-Q3 on the keyword; the founder's verbatim go completes
the launch.**

### 34.11 SS43-Q3 EXECUTED — the ladder at ring composition: BRANCH (c), the fork sharpened and quantified (Patch 2395; DM-WARM-2394)

**Launch:** warm on DM-WARM-2394; founder verbatim go: **"Go. Please proceed as
recommended."** Contract §34.10 executed as written; grading branches stood
pre-registered; no renegotiation.

**Battery: ALL PASS** (`code/2395_ss43_q3_ring_ladder.py`, results
`code/2395_results.json`, Tier-4 record `reasoning/2395.md`).
- **V1** 2393 green underneath, run in a SCRATCH COPY (provenance guard — committed
  artifacts untouched by the warm re-run; the 2394 lesson made mechanical).
- **V2 PASS-GATE PASSED:** the generalized ladder reproduced a fresh 1880 subprocess
  verdict-for-verdict on all ten rod-grid rows (0.035 ALIVE; 1.3e-3 dead-LZ) before
  any ring point was graded. ell_v(N = 4–8) reproduced the committed 2393 values to
  < 1e-9.
- **V3** five pre-declared spot checks green; **V4** no new free parameters (trace
  table in-script); **V5** cache 590 byte-identical baseline + 15 schema-pure flat
  appends (→ 605); 22 non-schema calls (ring-form/envelope/DAMIC-differential) kept
  out.

**The DAMIC-shallow low-mass pin (CONV-004 THIS PATCH** — the contract's one named
data action; arXiv:1804.03073 §§2.2/6/B, lineage arXiv:1105.5191 + 1712.01170):
106.7 m NuMI-hall depth, crust ρ = 2.7 g/cm³ → 2.8809e4 g/cm² column (Si-proxy
collision convention as the registered 1880 rock channel); silicon, 107 g·days,
E_nr threshold 550 eV, 106 observed events, 90% CL expected-event bound N90 = 123.
Detection graded by the FULL DIFFERENTIAL spectrum above threshold (halo-folded) —
the forward-peaked light-mediator potential makes total-σ counting a
several-order overcount; shielding ceiling by total σ (1880 convention). The
25-GeV J12′-a pin confirmed non-transferable, as flagged.

**GRADING (mechanical, §34.10): BRANCH (c) — SPLIT VERDICTS.**
- **Identity end (registered fold convention): clears the ENTIRE ladder by exact
  identity** (A2a + A2b ⇒ every baryon channel exactly zero). Corollary computed,
  not assumed: branch (a) cannot trigger.
- **Envelope end (conservative |V| upper bracket): FAILS LZ(strict) and DAMIC at
  every species N = 4–8.** Unshielded (rock 2.4–6.8 collisions; DAMIC column
  0.16–0.46); σ_n = 3.1e-33–2.0e-32 vs the strict-point 9.2e-48 (15 orders); DAMIC
  expected events 3.4e7–1.5e8 vs 123 (5.4–6.1 orders). XQC passes everywhere
  (member-weighted ρ* = 76.6–109.3 ≥ 0.3); np passes (≤ 8.2e-5 fm vs 3e-3); CMB
  passes (≤ 3.9e-32 vs 1e-25).
- **Named pins (branch (c) clause), recorded at grading time:**
  1. **LZ low-mass edge:** N = 4, 5, 6 (5.63/7.04/8.45 GeV) sit at/below LZ's
     published 9-GeV lower edge — their LZ(strict) failures are EDGE-CONDITIONAL;
     N = 7, 8 (9.86/11.26 GeV) fail unconditionally in-coverage. The branch verdict
     rests on neither: DAMIC kills all five species inside its silicon coverage.
  2. **Residual-coupling demand (→ Q4):** rate ∝ amplitude² ⇒ survival of the V-t
     branch requires the TRUE post-closure residual amplitude below the |V| envelope
     by ×5.3e2–1.1e3 (DAMIC, per N) and ×1.8e7–4.6e7 (LZ strict). The envelope is a
     first-moment upper BOUND (a zero-mean vector potential scatters at second
     order), so these are a derivation demand, not a death sentence — but nothing
     registered currently derives the residual scale.
  3. The DAMIC pin itself (above), registered CONV-004.
- **Class S bookkeeping rows carried:** XQC gate-death stands at ring composition
  (nviol 2–11 at standard density); the species are additionally rock-shielded
  (5.7e3–1.55e4 collisions) AND DAMIC-shielded (380–1040) at S_c = 0.0356 — the
  §34.9 kill shown over-determined, per contract intent.

**Where this leaves the campaign:** the class fork did not resolve — it SHARPENED
into a quantified conditionality. The V-t branch survives the full ladder **iff**
the true residual coupling after closure sits ≲ envelope/2e7 (in-coverage LZ,
N = 7, 8; envelope/1e3 suffices for the DAMIC-only species) — with the identity end
(exact zero) trivially inside. **Q4's registered duty is now triple: R_s from
substrate mechanics + the vertex class + the residual coupling scale**, the last
being the fork-resolver. Class adjudication stays HELD per the founder's (c)
ruling; this record goes to the founder's desk; session-close handover follows the
reading, per operating_system.md §15. Q5 queues behind Q4; R2 release lane separate
and untouched.

### 34.12 SS43-Q4 CONTRACT + WARM-LAUNCH REGISTRATION — the de-novo substrate derivation, TRIPLE duty (Patch 2397, 10 July 2026)

**Founder direction:** verbatim: "Register the Q4 contract: Please proceed as per
recommendation." (on the Priority-1 recommendation of the 2026-07-10 Q3-close
handover; recorded in `reasoning/2397.md`). This section registers the contract;
per the standing anti-priority, NO derivation work begins until the next session's
warm launch completes on the founder's go.

**Warm-launch keyword: DM-WARM-2397.**

**Handover set (self-contained, all under `series_phenomena/cosmology/dark_matter/`
unless noted):** this file §34 in full (re-aim §34.1–34.5; wall §34.7; dichotomy
§34.9; Q3 contract §34.10; Q3 record §34.11; this contract); §17 (the de-novo
target: m_s = χ·ħc/r_c = 7.764 MeV, colour-residual channel gapped, |SSV| scalar
gapless — standing since 1872); §22 (D5-A′ + derivation debt); `reasoning/2395.md`
(the residual demand and its physics read); `code/2395_results.json`
(grading.residual_demand, grading.named_pins, Vt_envelope_end per-N);
`code/2393_ss43_q2_ring_multipole.py` + `code/2393_results.json` (the two vertex
classes, the exact identities, the envelope construction);
`code/2395_ss43_q3_ring_ladder.py` (the generalized ladder — Q4c's re-confrontation
instrument, V2-gated); `code/1880_d5_sc_landscape.py`; the committed
`code/2379_unit_cache.json` (605 keys at this registration); arc-doc context.

**SS43-Q4 pre-registered scope — the de-novo gap derivation (§34.4 stage 4),
carrying TRIPLE duty. From registered primitives only (0865 held; no dark-sector
freedom; CONV-004 tags wherever a measured quantity enters):**

- **(i) Q4a — R_s from substrate mechanics (the response-order question; the
  original §34.4 charter):** derive the colour-residual channel gap
  m_s = χ·(ħc/r_c) — i.e., establish that the response order in the colour-residual
  channel is LINEAR in χ, with the |SSV| scalar gapless (§17). Deliverable:
  R_s = ħc/m_s = 25.4 fm landing inside the inherited [20, 51] fm demand (§34.1).
  **Pre-registered kill (carried unchanged from §34.4): √χ response order ⇒
  R_s ≈ 5 fm ⇒ outside the demand ⇒ Clause 1(a) exit.**
- **(ii) Q4b — the vertex class DERIVED (S vs V-t), not read off D5-A′'s ruling
  language:** the same substrate mechanics that fixes the response order must fix
  what a per-unit qCP vertex sources — scalar per-qCP additive (Class S) or
  chain-axis vector (Class V-t). The registered discriminant is available and
  binding: under V-t the rod's D5-A′ power-0 sourcing is END-sourced O(N⁰), not
  bulk ∝ N (2393, V2 adjacency record against the 1880 debt) — the derivation must
  reproduce the rod's registered first-power dipole phenomenology under whichever
  class it lands. **Pre-registered kill: derived class = S ⇒ the family is dead
  fully derived (gate-death §34.9, over-determined §34.11) ⇒ Clause 1(a) exit,
  fork resolved toward death.** A derived V-t additionally discharges the
  registration debt on the two Q2 exact identities (theorem-registry entry
  unblocks — the §34.9/2394 deliberate deferral).
- **(iii) Q4c — the post-closure residual coupling scale (the fork-resolver;
  reached only on a Q4b V-t landing):** derive the order and scale of the TRUE
  residual amplitude a closed ring presents to a nucleon after the exact
  cancellations (A2a telescoping + A2b orientation orthogonality). The physical
  expectation named at 2395 is the second-order scattering of a zero-mean vector
  potential (the envelope being a first-moment bound); the derivation must produce
  the actual order, not assume it. **Grading window (quantified at 2395, CLOSED
  input):** V-t survival requires residual ≤ envelope/(1.8e7–4.6e7) at LZ
  in-coverage (N = 7, 8) and ≤ envelope/(5.3e2–1.1e3) at DAMIC (sufficient alone
  for N = 4–6); the registered-convention identity end (exact zero) is trivially
  inside. On a derived residual, the 2395 generalized ladder re-runs at the derived
  value (V2 pass-gate re-armed) — the re-confrontation is mechanical, not a new
  contract.

**Cheap-kill ordering (binding; the contract's own):** Q4a → Q4b → Q4c. Q4a is the
cheapest kill (response order; the pre-registered √χ kill moots everything
downstream). Q4b next (a Class-S landing kills the family with no residual work).
Q4c only on a V-t landing. No stage is skipped, none reordered, none begun before
its predecessor's grading is recorded in this file (§34.13+ execution records,
one per stage or session per §15 lane practice).

**Grading (mechanical, pre-registered — no adjustment after the derivation):**
- **(a) Any stage kill triggers** (Q4a √χ order; Q4b Class S; Q4c residual outside
  the window at any in-coverage channel with Class S already dead) → **the family
  is dead on both classes, fully derived** → Clause 1(a) exit on the founder's
  desk. The (d′) attestation at 8.45 GeV binds as registered.
- **(b) Full landing** (Q4a linear-in-χ ⇒ R_s = 25.4 fm in-demand; Q4b derives
  V-t; Q4c residual inside the window, ladder re-confrontation clean) → **the
  family is ALIVE fully derived**: the class fork is resolved by derivation, the
  Q2 identities register, Q5 (coat-channel sign synthesis + corridor re-grade)
  launches on the derived machinery, and successor-branch registration goes to the
  founder post-rent (§34.4 held list).
- **(c) Partial/conditional** (e.g., a derived response order carrying an unpinned
  O(1) coefficient that straddles a window edge; a class derivation conditional on
  an unregistered lock) → recorded faithfully stage-by-stage and channel-by-channel;
  named pins; NO smoothing; founder adjudication on the recorded residue before any
  downstream stage proceeds.

**Verify battery (binding, per-session across the weeks-scale arc):**
- **V1 chain green underneath:** the 2395 battery (transitively 2393 → 2391 →
  2381/2382/2383) run in a SCRATCH COPY at every session that touches the
  machinery (the provenance guard, now mechanical).
- **V2 known-limit reproduction (PASS-GATE, per stage):** every analytic stage
  must reproduce its registered limits before its result is graded — Q4a: the §17
  channel decomposition (gapped colour-residual vs gapless |SSV|) and the 1872
  numerical anchor; Q4b: the rod's D5-A′ first-power phenomenology under the
  derived class; Q4c: the 2393 identity zeros and envelope values, and (on
  re-confrontation) the 2395 V2 rod-grid reproduction. Failure = machinery/derivation
  not trusted; no grading proceeds; fix or escalate.
- **V3 spot-check reproduction** on pre-declared sets per stage.
- **V4 no-freedom audit:** every coefficient traced; 0865 held; CONV-004 tags on
  every measured entry. The LZ 9-GeV edge stays UNPINNED unless a Q4c
  re-confrontation makes it load-bearing — in which case pinning it is a named
  CONV-004 action registered by amendment to this contract (founder-gated), not a
  casual pin.
- **V5 cache integrity:** schema-pure appends only; derivation-stage calls stay
  out unless schema-compatible; committed-record runs get redirected output (the
  2395 §5 lesson).

**Exits and rent:** Clause 1(a) binds at every stage kill, fully derived. The
attested (d′) binds at 8.45 GeV. The §34.7 wall, §34.9 gradings, §34.11 grading,
and the 2395 residual-demand window are CLOSED inputs — cited, never re-derived,
never re-graded. The (c) HOLD on the vertex class stands until Q4b derives the
class or a kill moots it; no adoption in passing at any intermediate point.

**Out of scope (binding):** Q5 pre-work; theorem-registry entry for the Q2
identities before Q4b lands V-t; any DAMIC re-pin; the R2 release lane (DM-1
v1.5 / DM-3 v1.1 — separate, staged, founder-gated); glossary promotion of S/V-t
(stays §34.9-local until survival).

**Expected cost:** weeks-scale (§34.4). Q4a expected 1–2 sessions; Q4b 1–3
sessions; Q4c dependent on the Q4b landing (analytic core + one mechanical
re-confrontation session). Each session closes with the §15 handover; each stage's
grading lands in this file before the next stage opens.

**Next session opens with SS43-Q4a on the keyword; the founder's verbatim go
completes the launch.**

### 34.13 SS43-Q4a EXECUTED — the response order is LINEAR in χ, derived from the registered amplitude-level structure; R_s = 25.42 fm IN-DEMAND, the √χ kill not triggered (Patch 2399, 10 July 2026)

**Launch:** warm on **DM-WARM-2397**; chain-verify 2398 → 2397 → 2396 → 2395 → 2394
green. Founder launch go cited verbatim per the 2026-07-10 handover's mandate:
**"Go to complete SS43-Q4 launch."** (recorded at that handover; carried in
`reasoning/2399.md` §1 per the §10 block). Battery: **ALL PASS** — V1 2395 battery
green in a scratch copy (transitive 2393 → 2391 → 2381/2382/2383; 181 s, committed
artifacts untouched); **V2 PASS-GATE passed before any grading** (1872 anchor
recomputed fresh: χ = 0.03934466, m_s = 7.7638 MeV, R_s = 25.4164 fm, calibration
band 6.2–24.7 MeV; §17 decomposition reproduced: ξ/R_s = 6.3×10³⁹, gapped-channel
leak exponent −6.3×10³⁹ at r = R_H; the gapless side's geometric core reproduced as
a known limit — the first-shell icosahedron IS a spherical 5-design at machine
precision for ℓ = 1–5 and is NOT a 6-design, max ℓ=6 deviation 1.6×10⁻²); V3 3/3
(independent algebraic path χ = 1/(6(2φ+1)); m_s·R_s = ħc exact; ℓ=6 deviation
persists under an independent seed); V4 zero tunables (inputs: φ, d_Γ = 2,
V_cage = 12, r_c = 1 fm SF-5/J2, window §34.1, ħc — all registered; 0865 held);
V5 no cache opened, output only `code/2399_results.json`.

**THE DERIVED ANSWER (the contract's Q4a deliverable):**

- **L1 (registered — METH-CHIR-CONT-1, Capotauro v2.0):** the residual-channel
  vertex on a Sea qDP's first shell is a Wigner–Eckart **matrix element — an
  amplitude-level object**: g_res/g_color = |χ_sub|·d_Γ/V_cage = φ⁻³·(2/12) = χ.
  One power of χ **per vertex**; its square governs probabilities. Universal data
  (φ⁻³, 2, 12) registered and verified at the three Capotauro v2.0 sectors.
- **L2 (hermiticity):** perceive-side and source-side matrix elements of the same
  channel operator are equal in magnitude — every leg of a closed response loop in
  the residual channel carries χ once.
- **L3 (the registered J1/1864 linear-screening baseline):** the static gap is the
  channel-diagonal polarization, m_c² = Π_c(0) — a two-point function with exactly
  **two** vertex insertions (perceive + re-source per Sea response cycle).
- **THEOREM:** Π_res/Π_color = (g_res/g_color)² = χ² ⟹ **m_s = χ·√Π_color =
  χ·(ħc/r_c) = 7.764 MeV ⟹ R_s = r_c/χ = 25.42 fm — the gap is LINEAR in χ**, with
  the colour anchor √Π_color = ħc/r_c the SF-5 empirical confinement input (J2).
- **COROLLARY (√χ EXCLUDED, not merely disfavored):** m_s = √χ·ħc/r_c requires
  Π_res = χ·Π_color — one power of χ in the bubble — i.e. either a
  **probability-level** registration of χ (contradicts METH-CHIR-CONT-1) or
  **asymmetric legs** (contradicts L2 hermiticity). Not constructible from the
  registered primitives. Numerically the √χ point lands at R_s = 5.04 fm, outside
  [20, 51], reproducing the pre-registered kill value — the kill branch was armed
  and did not fire.
- **Channel decomposition exact:** the |SSV| scalar stays gapless because its
  restoring average vanishes at **symmetry level** (5-design, 1107–1108 CLOSED
  input — zero legs to suppress), while the colour-residual channel gaps at χ² in
  the bubble. Same mechanics, two channels; §17's target discharged as derived
  rather than pinned. **Route B's "numerological until derived" label (§3) is
  hereby lifted; Route C stays killed (§34.3 C2).**

**Named pins (recorded, not smoothed; none straddles — no (c)-trigger):**
**PIN-Q4a-1:** L3 inherits the registered J1/1864 linear-screening baseline (the
campaign's standing footing; the formal PCD → linear-response bridge remains the
FP-side debt, not new freedom introduced here). **PIN-Q4a-2:** the O(1)
channel-geometry coefficient c in R_s = c·r_c/χ is unpinned; window tolerance
c ∈ [0.787, 2.007] contains c = 1 with margin; a √χ rescue needs c ≥ 3.97 — not an
O(1); the two orders are cleanly separated by the window. **PIN-Q4a-3:** the r_c
spread 0.85–1.0 fm (J2, untagged) gives R_s ∈ [21.60, 25.42] fm — in-window end to
end.

**GRADING (mechanical, pre-registered §34.12): Q4a LANDS on the branch-(b) track —
linear order derived, R_s = 25.42 fm IN-DEMAND, kill not triggered.** Q4b (the
vertex class derived, S vs V-t) is now unblocked by this record and opens next
session per the contract's ordering; **the (c) HOLD on the vertex class stands**
until Q4b derives it or a kill moots it. Out-of-scope guard held this session: no
Q4b pre-work, no class adoption, no theorem registration, no DAMIC re-pin, R2 lane
untouched. Artifacts: `code/2399_ss43_q4a_response_order.py`,
`code/2399_results.json`; registry `frontier_sectors/SS.md` 2399 block;
`reasoning/2399.md` (verbatim, at-patch).

### 34.14 SS43-Q4b EXECUTED — the per-unit vertex class is CLASS V-t, DERIVED from the registered structure; the Class-S kill armed and not fired; the (c) HOLD discharged by derivation (Patch 2401, 10 July 2026)

**Launch:** warm on **DM-WARM-2400**; chain-verify 2400 → 2399 → 2398 → 2397 → 2396
green. Founder launch go this session (verbatim): **"Go on Q4b."** ("Please proceed
with Q4b." — recorded at `reasoning/2401.md` §1 per the §10 block; no go was on
record at the 2400 close; the launch completed on this verbatim per the 2397/2398
pattern). Battery: **ALL PASS** — V1 2395 battery green in a scratch copy
(181.4 s; transitive 2393 → 2391 → 2381/2382/2383; committed artifacts untouched);
**V2 PASS-GATE passed before any grading** — (a) the rod's registered D5-A′
phenomenology reproduced UNDER THE DERIVED CLASS: open-chain composite telescopes
EXACTLY to the end form (machine precision), source side power-0 (log-log slope
0.1055; 2393 record 0.106), total = FIRST power at the ruling scale
R_N/R_s = 0.0354; (b) the two Q2 exact identities reproduced as CONSEQUENCES of
the derived composition (closed-loop telescoping = 0 at machine precision, N = 4–8
× 12 random probes; orientation orthogonality 8.4×10⁻¹⁷; node-form crosschecks:
closed-ring node sum 8.0×10⁻¹², open-chain node-vs-edge 0.62% at midpoint rule);
V3 5/5 (global-flip sum → −sum exact; LOCAL single-unit flip physical, breaks
telescoping by O(per-edge); chain reversal flips the composite sign exactly — the
vector character checked; class verdict normalization-independent under arbitrary
c = 3.7; R_s = r_c/χ reproduces the 1879 engine RS to machine precision); V4 zero
tunables (φ; χ = φ⁻³/6; r_c = 1 fm SF-5/J2; R_s Q4a CLOSED; R_N = 0.9 fm 1880;
d = 1.15 fm J8; the D5-A′ data points enter as the GATE'S targets, not derivation
inputs; 0865 held — no torsional lock, no transverse component, no new transport
datum); V5 no cache opened, output only `code/2401_results.json`.

**THE DERIVED ANSWER (the contract's Q4b deliverable — the same substrate
mechanics as Q4a, asked its second question):**

- **L1 (the Q4a identification, §34.13 CLOSED input):** the per-unit
  residual-channel vertex is the METH-CHIR-CONT-1 Wigner–Eckart matrix element
  M = ±χ·(d_Γ/V_cage) — SIGNED, amplitude-level. The datum's ± is explicit: the
  magnitude is universal; the SIGN is relative to the unit's local ℤ₂ pairing
  convention (Ĉ in a ζ-ODD 1D irrep; M connects ζ-EVEN to ζ-ODD doublet
  components — relabeling flips M). In isolation only |M|² enters (the Q4a
  bubble); the sign is unphysical alone.
- **L2 (transport):** relative signs between units are physical iff a registered
  structure refers the conventions — the rung bond (2381 rung-bond primitives) IS
  that structure: bonding is a pairing relation between adjacent units' DPs and
  transports the ℤ₂ convention along the chain, the rod's ONLY registered
  coherence axis; no torsional lock registered ⟹ no second transport datum (0865).
- **L3 (chain-reversal parity fixes the tensor character):** the transported sign
  is defined relative to the bond ORDERING; chain reversal exchanges bond roles ⟹
  flips the convention-referred sign ⟹ the coherently sourced per-unit amplitude
  is ODD under t̂ → −t̂ — a chain-axis vector component v_k = M·t̂_k, coupling
  through the directional derivative t̂·∇ₓY, whose discrete form is the per-edge
  difference (the 2393 machinery, now derived rather than posited).
- **THEOREM (the class): Class V-t.** Composition = the rung-transported signed
  sum (discrete line integral). Closed loop: interior contributions telescope to
  zero identically. Open chain: telescopes to the ENDS — **the rod's D5-A′
  power-0 sourcing is END-sourced O(N⁰), the 2393 V2 adjacency record reproduced
  as a CONSEQUENCE, not an input.**
- **COROLLARY (Class S EXCLUDED by registration, not merely disfavored — the √χ
  exclusion's twin):** Class S needs the composite's per-unit source to be the
  UNSIGNED |M| (chain-reversal-EVEN), requiring either probability-level
  registration of the per-unit source (contradicts the amplitude-level L1,
  CLOSED) or a ζ-EVEN vertex operator (contradicts the ζ-ODD irrep placement in
  the registered datum). Not constructible. The incoherent composition
  (uncorrelated signs, RMS ~ √N — numerically resolved in the trichotomy) requires
  NO transport, contradicting the registered bonded structure itself; D5-A′'s
  "coherent cage" language is thereby given MECHANISM without being consumed as a
  premise.
- **1858 reconciliation carried:** telescoping is a coherence projection of the
  VERTEX; the force between nonzero-net-vertex bodies is second-order in the net
  amplitude — attractive always; unipolarity stands.

**Named pins (recorded, not smoothed; none straddles — no (c)-trigger; the
verdict is structural, coefficient-free, normalization-independent):**
**PIN-Q4b-1:** L2's transport stands on the 2381 rung-bond primitives as
registered; the PCD-level derivation of the transport rule is the standing
FP-side debt (same family as PIN-Q4a-1) — named conditionality, not new freedom.
**PIN-Q4b-2:** the derivation fixes the CLASS, not the post-closure TRUE residual
magnitude — Q4c's charter, untouched. **PIN-Q4b-3:** the per-edge normalization
inherits the PIN-Q4a-2 O(1) freedom; the class verdict is independent of it
(V3-iv).

**Instrument discipline note (recorded per no-smoothing):** two missteps in the
VERIFY INSTRUMENT (a check-design ~0/~0 division; a probe-vs-source gradient sign
in the node-form crosscheck) were caught by the V2 gate failing loudly, diagnosed,
and fixed; the derivation and identities moved zero. Full record
`reasoning/2401.md` §4.

**GRADING (mechanical, pre-registered §34.12): Q4b LANDS on the branch-(b)
track — derived class = V-t; the Class-S kill armed and NOT FIRED (Class S is
excluded by registration).** Consequences firing on this record: **the (c) HOLD
on the vertex class is DISCHARGED BY DERIVATION** (its stated terminus); **the
Q2-identity theorem registration UNBLOCKS** (the §34.9/2394 deliberate deferral
discharged — registration itself QUEUED as a named next-session action, not
executed in passing); **Q4c (the post-closure residual fork-resolver) unblocks**
and opens next session on the founder's verbatim go, graded at §34.15 against the
CLOSED 2395 window, the generalized-ladder re-confrontation V2-re-armed. Glossary
promotion of S/V-t stays gated on survival (not established until Q4c). Scope
guard held: no Q4c pre-work, no theorem registration executed, no DAMIC re-pin,
no LZ pin, R2 lane untouched. Artifacts: `code/2401_ss43_q4b_vertex_class.py`,
`code/2401_results.json`; registry `frontier_sectors/SS.md` 2401 block;
`reasoning/2401.md` (verbatim, at-patch).

### 34.15 SS43-Q4c EXECUTED — the residual coupling scale DERIVED: the discreteness defect, (N−1)-order multipole-protected; BRANCH (c) with ONE named residue — the LZ 9.86-GeV local-value pin, founder-gated (Patch 2403, 10 July 2026)

**Launch:** same-session continuation on the DM-WARM-2400 arc; founder go this
session (verbatim): **"Please proceed as per recommendation."** (on the stated
Q4c recommendation; `reasoning/2403.md` §1). Pass-gate honored: Patch 2401
verified at origin/main before Q4c opened (§34.12 grading-lands-first). Carried
triggers fired catalog-first at **Patch 2402**: METH-L1-013 (registration-level
response-order counting — the 2400 handover's named trigger), METH-L2-012
(strict-point gate) + METH-L2-013 (differential-vs-total σ) — all three reused
by this stage. Battery: **ALL PASS (27/27)** — V1 2395 scratch-copy green at
session open (181.4 s transitive); **V2 RE-ARMED and passed before grading**
per the Q4c contract clause: ℓ_v(4–8) byte-exact vs committed 2393; the
committed 2395 envelope LZ σ_n per N byte-exact; the committed 2395 DAMIC
envelope events reproduced (N = 6, rel 0.0); the rod-grid decisive rows fresh
(0.035 ALIVE; 1.3e-3 dead-LZ); the exact identities fresh. V3 5/5 (analytic
structure-factor FT vs numeric 3D FT exact; Born parameter 3.2×10⁻³; the
(N−1)-order law tracks the computed structure factor at ratio 0.90–1.09 for
every N; quadrature 5.5×10⁻¹³; uniform-tilt convention robustness). V4 zero
tunables (A_N = ℓ_v·ern1·SC_RULING/N the registered envelope convention; Si
28.09 the committed construction; bisector tangents per 2401 L2; 0865 held).
V5 no cache opened. Runtime 12.9 s.

**THE DERIVED ANSWER (the contract's Q4c deliverable — order NOT assumed):**

- **Three nested protections locate the residual exactly.** (P1-i) The
  fold-convention edge-difference zero is CONFIGURATION-INDEPENDENT (holds for
  arbitrarily deformed closed loops — verified 0.0) — an artifact of the edge
  convention, carrying no ring physics. (P1-ii) The continuum node form — the
  closed line integral of ∇Y — is zero for ANY closed loop by the gradient
  theorem: a TOPOLOGICAL protection that smooth deformations cannot break
  (refinement decays the node sum super-algebraically to the numerical floor).
  (P1-iii) **The physical residual is the DISCRETENESS DEFECT**: the ring is N
  point vertices (the 2401-derived v_k = M·t̂_k, bisector tangents), and the
  discrete node sum at generic orientation is nonzero — the 2401
  symmetric-probe zeros reproduced as the reflection-symmetric special case.
  Internal-excitation channels (phonons, ζ-flips) enter only as gap-suppressed
  second-order corrections to the static defect (PIN-Q4c-2) — never
  load-bearing.
- **The order (METH-L1-013 reused):** the structure factor
  D(q) = Σ_k(t̂_k·q̂)e^{iq·x_k} is exactly 2π/N-periodic in azimuth (C_N —
  forbidden harmonics at the absolute machine floor), with leading radial
  behavior **|D| ≈ (qR_g/2ħc)^{N−1}/(N−1)!·√N** — confirmed numerically within
  10% at every N. The residual is **(N−1)-order multipole-protected**:
  species-dependent, exponentially small in N at experimental momenta. The
  2395 "zero-mean second-order" expectation is upgraded to an exact
  selection-rule statement.
- **The scale, graded absolutely (Born exact; parameter 3.2×10⁻³):**
  **DAMIC — the envelope end's killer — passes at EVERY species by 3–15
  orders** (max 0.133 events vs N90 = 123; METH-L2-013 differential
  machinery, committed construction reproduced at the gate). **LZ strict:
  N = 8 (11.26 GeV) PASSES unconditionally, 32× inside** (2.85×10⁻⁴⁹ vs
  9.2×10⁻⁴⁸). **N = 7 (9.86 GeV) sits 12.6× over the 36-GeV strict point** —
  a STRICT-POINT-CONDITIONAL row (METH-L2-012): the local LZ value at
  9.86 GeV is unpinned and far weaker than the 36-GeV floor. N = 4–6 stay
  LZ-edge-conditional (2395 pins carry) and DAMIC-clean. Domination:
  XQC/rock/np/CMB pass (residual/envelope amplitude ≤ 3.7×10⁻³ across the
  band, on the envelope end's committed passes).

**GRADING (mechanical, pre-registered §34.12): BRANCH (c) — recorded
faithfully, channel-by-channel, NO smoothing.** No branch-(a) trigger fires
unconditionally anywhere. **N = 8 is fully derived-and-clear across the entire
ladder.** The single open residue: **PIN-Q4c-3 — the N = 7 verdict is
conditional on the LZ local value at 9.86 GeV, which this re-confrontation has
made LOAD-BEARING — exactly the fork §34.12 V4 pre-registered as a
founder-gated CONV-004 contract amendment, not a casual pin.** On the
founder's desk: (a) authorize the pin (named data action: the published LZ
limit at 9.86 GeV; if it exceeds 1.16×10⁻⁴⁶ cm², N = 7 clears); (b) decline
and carry N = 7 conditional (N = 8 alone gives the family an unconditionally
clear member); (c) direct otherwise. **Per branch (c): founder adjudication on
this recorded residue before Q5 proceeds.** Also on the desk (unchanged
queue): the Q2-identity theorem registration (unblocked at 2401, queued, not
executed in passing); Q5 and successor-branch registration post-adjudication;
R2 release lane separate.

**Pins:** PIN-Q4c-1 (bisector node-tangent convention; V3-v shows the C_N
selection robust under any UNIFORM convention — only site-dependent
conventions leak, excluded by uniform transport/0865); PIN-Q4c-2
(internal-excitation channels subleading for gaps ≳ keV — violation would
preclude the ring's registered survival as a cold species); PIN-Q4c-3 (the
LZ 9.86-GeV residue, above).

**Instrument discipline note (per no-smoothing; full record
`reasoning/2403.md` §4):** four instrument-side missteps caught by the gates
and fixed with the derivation unmoved — a guessed Si factor (V2c caught it;
the committed 2395 construction transplanted: the standing transplant-never-
reconstruct lesson), a harmonic-selection mis-statement (jN±1 → jN azimuthal
+ (N−1) radial), FFT aliasing + a relative-vs-absolute floor criterion, and
one stale variable.

Artifacts: `code/2403_ss43_q4c_residual_scale.py`, `code/2403_results.json`;
registry `frontier_sectors/SS.md` 2403 block; `reasoning/2403.md` (verbatim,
at-patch). Methods registrations: Patch 2402 (catalog-first).

### 34.16 CONV-004 CONTRACT AMENDMENT ADOPTED (PIN-Q4c-3 → option (a)) — the LZ 9.86-GeV local-value pin STRUCTURED; source identified; numeric assignment = a named founder data action; two adjacent data facts registered (Patch 2404, 10 July 2026)

**Founder ruling (verbatim, this session):** **"Please adopt the contract
amendments as recommended."** — adopting PIN-Q4c-3 option (a): the §34.12 V4
founder-gated CONV-004 amendment authorizing the pin of the published LZ local
value at 9.86 GeV. Recorded here; the gate is OPEN.

**The pin, structured (CONV-004; executed to the limit of in-session access):**
- **Primary source identified:** LZ WS2022+WS2024 combined analysis, *Phys.
  Rev. Lett.* **135**, 011802 (2025) = arXiv:2410.17036 (280.0 live days,
  4.2 t·y). The SI limit curve is Fig. 5; the digitized values are the HEPData
  record **ins2841863** (DOI 10.17182/hepdata.155182.v2), table **"SI cross
  section"** (record page hepdata.net/record/158592).
- **Published-in-text anchors (verified this session):** coverage: masses
  ≥ 9 GeV/c² (9.86 GeV IS in coverage); curve minimum 2.2×10⁻⁴⁸ cm² at
  40 GeV/c² (power-constrained; median sensitivity 5.1×10⁻⁴⁸); the combined
  limits "surpass previous best exclusions by a factor of four or more for
  WIMP masses > 9 GeV/c²."
- **Access record (no smoothing):** the HEPData table download endpoints
  (csv/yaml) were bot-blocked from this session; the 9.86-GeV numeric value is
  published only in Fig. 5 / the digitized table, and NO text source quotes
  it. Manufacturing the number from curve-shape expectations is forbidden by
  the same CONV-004 discipline this amendment exists to honor.
- **NAMED FOUNDER DATA ACTION (completes the pin — ~2 minutes):** read the
  "SI cross section" table at the HEPData record above on a local machine and
  report σ_LZ(9.86 GeV/c²) — at the tabulated mass nearest 9.86, or linearly
  log-interpolated. One number completes the amendment.
- **Pre-staged mechanical re-grade (fires on the number, no renegotiation):**
  **N = 7 CLEARS iff σ_LZ,combined(9.86 GeV) > 1.16×10⁻⁴⁶ cm²** (the Patch-2403
  derived value). On a clear: every ladder channel passes at N = 7 and N = 8;
  the family's in-coverage grading upgrades toward the branch-(b) full
  landing, gated only on the N = 4–6 item below. On a fail: N = 7 dies
  in-coverage fully derived; N = 8 stands alone unconditionally clear;
  family-level survival persists on N = 8 with member-weight consequences to
  the founder's desk.

**Adjacent data facts registered in the same CONV-004 search (both material,
neither smoothed):**

- **(i) The registered strict point is SUPERSEDED.** The registered
  LZ_STRICT = 9.2×10⁻⁴⁸ (SR1/WS2022, 36 GeV) is now dominated by the combined
  curve's 2.2×10⁻⁴⁸ at 40 GeV. **Q4c's grading is UNMOVED in kind:** N = 8's
  derived σ = 2.85×10⁻⁴⁹ clears even the superseded-updated strict point by
  **7.7×** (verified arithmetically this patch) — the N = 8 unconditional
  clear stands against the strongest published point of the strongest
  published curve. N = 7 remains strict-point-conditional exactly as graded.
  Carried note: the strict-point gate (METH-L2-012) re-arms on the 2.2×10⁻⁴⁸
  value at the next confrontation that consumes it.
- **(ii) A NEW LZ low-mass analysis exists (Dec 2025) that will dissolve the
  N = 4–6 edge pins.** LBL/SURF announcement, 8 Dec 2025: 417 live days
  (Mar 2023–Apr 2025), **first LZ search below 9 GeV, covering
  3–9 GeV/c², world-leading above 5 GeV/c²**; presented at SURF; arXiv/PRL
  release pending at announcement. All three edge-conditional species
  (N = 4: 5.63 GeV, N = 5: 7.04 GeV, N = 6: 8.45 GeV — the (d′) attestation
  mass) fall inside this new coverage. **Named follow-up data action
  (founder-gated, same CONV-004 family):** locate the published curve and
  grade the three species' derived residuals (1.37×10⁻³⁸, 2.46×10⁻⁴¹,
  5.07×10⁻⁴⁴ cm²) against it. No pre-grading here; recorded stake: these
  residuals are large on the xenon scale, so the new data plausibly
  discriminates WITHIN the family (killing lighter members while N = 7–8
  stand) — a member-weight / attestation-mass consequence that goes to the
  founder's desk with the numbers, not before.

**Standing consequences:** the (c)-branch founder-adjudication requirement of
§34.15 is now PARTIALLY DISCHARGED (the amendment adopted and structured; the
residue reduces to two named data numbers). Q5 remains gated on the completed
adjudication. The Q2-identity theorem registration remains unblocked-and-queued.
Scope guard held: no number manufactured, no pre-grading, no Q5 pre-work, R2
lane untouched. Artifacts: this section; `frontier_sectors/SS.md` 2404 block;
`reasoning/2404.md` (verbatim, at-patch; includes the full search/access
record).
