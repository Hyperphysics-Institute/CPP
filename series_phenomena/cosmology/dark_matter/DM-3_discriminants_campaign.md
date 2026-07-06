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
