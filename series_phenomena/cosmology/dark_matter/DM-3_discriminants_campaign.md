# DM-3 campaign — the discriminating-predictions paper (opened Patch 2301, 6 July 2026; DM lane 23xx band)

**Charter:** founder green-light ("let's see how the model holds up under DM-3"). Falsification-first: the
arc's cheapest-kill computation ran at open (§2). **Scope reconciliation:** the June-era DM-3 definition
(derive ρ(r); Tully–Fisher; core sizes) targeted the pre-rod candidate and leans on the structure-formation
sector; the rod-era DM-3 is the HARVEST paper — the discriminating observational content the 1878–2300 arcs
generated. The June targets are noted as a possible DM-4-class follow-on, not silently absorbed.

## 1. The paper's spine (three pillars)

**P1 — the assembled falsifier suite as observational protocols.** F1 (group-scale σ/m = 0.037–0.05, 2.3σ
below the current mild detection); F5 (XQC-class reflight: 46 events at the ruling point / 8–50
region-weighted, ×11–×30 below existing sensitivity); F6 (deep-Earth thermalized population, n̄ ~ 2×10¹³
cm⁻³, center-concentrated, H_c ~ 1100 km); F-DM2-1 (the R_h form's evolving w(z), DESI-era live); F2 (np
precision); F3′ (the multipole kill-branches). Each stated as: instrument class, observable, kill/confirm
bands.

**P2 — the bound-state / anomalous-isotope discriminant (COMPUTED at open, §2).**

**P3 — the σ(v)-shape discriminant (to compute):** the capture+measured-floor curve's specific velocity
dependence vs generic velocity-dependent SIDM parametrizations — the joint {dSph grazing-low, dwarf pass,
group undershoot, cluster floor} shape as a single testable signature.

## 2. P2 RESULT — the bound-state threshold: a null-at-ruling-point discriminant with an element-threshold sweep (Patch 2301)

Verify `code/2301_dm3_bound_states_isotope_channel.py`. The attractive rod–nucleus Yukawa
(V = −A·E_rN·S_c·(r_c/r)e^{−r/R_s}) supports an s-wave bound state iff the screening coupling
s = 2μ g² R_s/(ħc)² ≥ 1.680. Because both g² and μ grow with A, binding has a sharp mass-number threshold:

| S_c | A_thresh | Terrestrial consequence |
|---|---|---|
| 0.012 (island bottom) | > 400 | nothing binds |
| **0.035 (ruling point)** | **257** | **nothing binds — even Pb (s = 1.32) is below critical** |
| 0.05 (island top) | 186 | only trans-tungsten elements (W marginal; Pt/Au/Pb/Th/U bind) |

**Kill-risk verdict: ELIMINATED at the ruling point.** No bound states ⇒ no anomalously heavy isotopes ⇒
the stringent light-element searches (≲10⁻²⁸) and all heavier searches are trivially satisfied — not by
threshold-dodging (my opening heuristic) but by across-the-board sub-criticality. **Signature verdict:
RESTRUCTURED into a sharper discriminant:** (a) at most of the island the prediction is a clean NULL — no
anomalous isotopes anywhere — itself discriminating against generic strongly-interacting composite DM
(which typically binds); (b) near the island's top edge, a heavy-element-only anomalous-isotope population
switches on with a sharp elemental threshold; (c) therefore a future S_c refinement (notably the F3′
multipole derivation) converts this channel into a yes/no laboratory test with a named element list.
J-DM3-1 (heavy-element search limits) needed only for branch (b); J-DM3-2 (capture kinetics) moot at the
ruling point. **Process note (recorded per discipline):** the opening heuristic (well depth vs zero-point)
predicted Fe binds; the proper critical-screening computation overturned it before any claim was made —
the compute-before-claim rule catching its author, again.

## 3. Arc order

P3 computation → P1 assembly → paper (v1.0-DRAFT) → CONV-001 panel. DM-3 sessions run DM-1's stability
clock (fourth DM-lane session banked at this patch).

## 4. P3 RESULT — S1 (the plateau) DELIVERED implementation-independent; S2/S3 provisional pending capture-model reconciliation (Patch 2302, 6 July 2026)

Verify `code/2302_dm3_sigma_v_shape_discriminant.py` (the script states its own tension when run).

**S1 — THE PLATEAU (the paper's sharpest discriminant; STANDS):** CPP's high-velocity behaviour is the
1871 MEASURED geometric floor (0.05 → 0.035 → 0.02 across 1150–3500 km/s), while the standard SIDM
phenomenological form σ₀/(1+(v/w)⁴), FITTED to the same dwarf+LSB anchors (σ₀ = 4.69, w = 135 km/s), has
crashed to 10⁻³–10⁻⁵ there: **divergence ×56 (group), ×135 (cluster), ×2000 (Bullet)** — pure shape, zero
normalization freedom. **F1 → F1′, a three-way decision channel:** group-scale detection at 0.03–0.05
selects CPP over single-mediator SIDM; a firm 0.5 kills CPP; a firm null below ~0.02 kills CPP's measured
floor and favors SIDM. Every branch is decisive; Sagunski-class analyses at 0.03–0.1 sensitivity are the
instrument.

**S2 (low-v saturation) and S3 (mid-band curvature): PROVISIONAL — J-DM3-3-OPEN.** The at-patch classical
capture implementation disagrees with the panel-ratified v1.2 anchors in the mid/low band (gives 0.34 at
LSB vs registered 0.74–0.85; 50 at dSph vs registered grazing-low). The registered anchors are
authoritative; the implementation's capture SHAPE is wrong between ~15–300 km/s. **Required before paper
assembly: pull the corpus's registered capture computation and recompute S2/S3 from it.** Caught at-patch
by the anchor cross-check — the compute-before-claim rule firing within its own patch.

**Arc queue updated: J-DM3-3 reconciliation → S2/S3 recompute → P1 assembly → paper → panel.**

## 5. J-DM3-3 CLOSED — S2′/S3′ recomputed from the registered model; a new analytic result: the running-slope law (Patch 2303, 6 July 2026)

Verify `code/2303_dm3_shape_reconciled.py` (anchor validation gates the claims: dwarf 4.38 ✓, LSB 0.74 ✓,
dSph@10 = 14.6 grazing ✓).

**Diagnosis:** the registered pipeline (1864/1865) is the **dissipative-reach criterion** — V(b_max) = KE,
σ = πb² — which is the correct capture physics: conservative dynamics cannot capture at all (energy
conservation), and the 2302 barrier implementation was therefore wrong in principle, not merely in shape.
The Sea-response channel supplies the dissipation; the reach criterion is its standard approximation.

**S2′ — logarithmic saturation:** the reach grows as b ~ R_s·ln(1/v²), so σ_cap ∝ ln²(1/v) — slower than
any power law, faster than a plateau. The dSph grazing is now a SHAPE PREDICTION: σ(10 km/s) ≈ 15,
20–25% under the heterogeneous window's low edge — analyses firming that edge above ~17 kill CPP;
landings at 12–18 select CPP over both flat-plateau and steep-power SIDM.

**S3′ — THE RUNNING-SLOPE LAW (new analytic result):** differentiating the reach condition gives the
local capture exponent in closed form, **p(v) = 4R_s/(b_max(v) + R_s)**, verified numerically
(0.60 → 0.98 → 1.80 → 3.0 across 10 → 600 km/s; the 3500 km/s numeric slope is floor-dominated, capture
negligible there). Neither a constant-p power law nor the SIDM (v/w)⁴ knee runs this way — and the law
INVERTS: two slope measurements at known velocities determine R_s directly. **Halo shape data alone
measure the screening length — an in-situ χ determination independent of normalization and of every
laboratory channel. Registered F-DM3-2.**

**S1 unchanged** (implementation-independent; ×51/×121/×2000 in the reconciled table — F1′ three-way).
**P3 is COMPLETE. Queue: P1 assembly → paper (v1.0-DRAFT) → CONV-001 panel.**

## 6. P1 COMPLETE — the protocol table assembled; J-DM3-1 CLOSED in the model's favor (Patch 2304, 6 July 2026)

`DM-3/falsifier_protocols.md`: nine protocols (F1′, F5, F6, F-DM2-1, F2, F3′, F-DM3-1, F-DM3-2, F-DM3-3),
each with instrument class, observable, decision bands, status, provenance. **J-DM3-1 pinned:** Javorsek
et al. PRD 64 012005 (AMS, anomalous Au/Fe, 200–350 amu — rod-bound Au ≈ 224 amu in-window; limits
X/Au ~ 10⁻¹¹–10⁻⁸) vs our top-edge ceiling ~10⁻¹⁵ → **safe by ≥4 orders across the island**; channel
graduates to future-instrument discriminant. Suite properties: three LIVE channels; F1′ and F-DM3-2
two-sided; F-DM3-2 = the first proposal to measure χ from galactic dynamics. **All three pillars done.
Queue: paper (v1.0-DRAFT) → panel.**

## 7. DM-3 v1.0-DRAFT ASSEMBLED (Patch 2305, 6 July 2026)

`DM-3/DM-3_discriminating_predictions.tex` — compiled clean. Structure: abstract organized around the
three results (the plateau ×56–×2000 with F1′ three-way; the running-slope law with the χ-from-the-sky
inversion; the bound-state threshold with the Javorsek pin); §1 the series role incl. the five in-house
catches stated as pedigree; §2 P3 with the reconciled table and the 2302→2303 reconciliation on record;
§3 P2 with the overturned-heuristic note; §4–5 lab/space/cosmological channels; §6 the protocol table
declared NORMATIVE (the paper is its narrative); §7 the inheritance ledger (D5-A′ PROVISIONAL; Gate-1/B1
+ EP sub-item; D3(b)) with kill-propagation stated; §8 grade with the two-channel positive-identification
statement. CONV-004 tags in-text. NOT SHIPPED — CONV-001 panel pending founder go.

## 8. DM-3 v1.0 SHIPPED — first-cycle 5/5; the counter-comparator challenge failed; THE SERIES' FIRST ARC IS COMPLETE (Patch 2307, 6 July 2026)

Five returns (ChatGPT/Grok/Gemini/Copilot/DeepSeek; no anomaly): **5/5** — Grok clean RATIFY; four RWC,
all disclosure-level ("disclosure refinements, not physics repairs"). **§5(ii): no reviewer could
construct a plateau-mimicking single-mediator comparator** ("we cannot construct one — the divergence
is robust"); **§5(vii): prematurity unanimously rejected** (the kill-propagation ledger "is exactly what
allows a harvest paper to exist"). Unanimous on C/E/F. Folded (six edits, no numbers moved): comparator
"representative" + community challenge; slope-inversion systematics caveat (4× convergent); χ-scoping
("within the CPP interaction model"); unit-capture-efficiency note; two-channel statement conditional/
programme-level; floor-extrapolation flag. Returns: `DM-3/review/reviews_v1.0_panel_returns.md`.
**Series state: DM-1 v1.4 (stability cycle; calendar ≥ 20 July binding), DM-2 v1.0, DM-3 v1.0 — three
papers, five panel cycles, every one ratified. Standing opens unchanged and named.**

## 9. DM-4 registered as prospectus (Patch 2308) — pointer

`DM-4/DM-4_prospectus.md`: the complete outline/strategy/methods for the structure-formation arc,
written at arc-close while fresh. Work NOT started; sequencing OSF → Gate-1/B1 → DM-4; the
capture-aftermath ruling identified as the true gate; K1 (dissipative collapse timescale) pre-identified
as the opening cheap kill; seeds and relic abundance named and fenced OUT of scope.
