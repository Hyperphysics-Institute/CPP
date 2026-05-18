# PH-OPEN-SS-28 — Problem History

**Problem:** OPEN-SS-28 — D3 (bulk-regime averaging) derivation + residual decomposition without hidden mechanisms
**Status at time of this file:** OPEN (registered as paper-level conditional theorem in SS-8 v1.0; structural derivation + residual-decomposition target deferred to a future paper)
**Sector:** SS (nuclear physics)
**Location in registry:** `research_frontier.md` §1, Strong Sector (SS)
**File created:** 26 April 2026
**Purpose:** Record the extended narrative of OPEN-SS-28's registration during the SS-8 development cycle, the empirical signature of D3's degradation as $N_\text{ex}/V$ grows, and the candidate scope for a derivation that delivers explicit error bounds and a residual decomposition without hidden mechanisms absorbed into "pairing bonus" terminology.

---

## Why this file exists

OPEN-SS-28 was opened during the SS-8 H2′ derivation note work (21 April 2026) as the third of three structural sub-problems needed to promote H2′ (the 2E/V alpha-vertex scaling law) from a layered hypothesis structure to a derived result. Of the three sub-problems, OPEN-SS-28 is the one most exposed to the empirical degradation of SS-8's predictions: D1 and D2 are categorical (vertex vs. non-vertex; edge-incident vs. not-edge-incident) and either hold or fail, but D3 is a quantitative approximation that degrades smoothly as $N_\text{ex}/V$ grows.

The acknowledged 8–15% precision band on the secondary 30-cell extension at $N_\text{ex} \in [3, 8]$ is exactly D3's degradation regime — it is not a parameter-fitting band but a structural-approximation band tied to the bulk-regime assumption $N_\text{ex}/V \ll 1$ being violated. Closing OPEN-SS-28 means deriving D3 from CPP primitives with explicit error bounds, and decomposing the observed residual into a small set of identifiable physical mechanisms rather than absorbing it into a generic "pairing bonus" coefficient.

This file records the registration narrative and the candidate scope.

---

## Timeline

| Date | Event | Artefact |
|------|-------|----------|
| 21 April 2026 | OPEN-SS-28 opened in H2′ derivation note §10 alongside OPEN-SS-26 and OPEN-SS-28 | `series_strong/papers/SS-8/sketches/SS-8_H2prime_derivation_note.md` |
| 22 April 2026 | Round 2 review of D1 sketch flags D3 as the load-bearing quantitative approximation. Copilot's review specifically requests an explicit treatment of where D3 breaks down (adopted into v0.2's primary/secondary split). | `series_strong/papers/SS-8/reviews/round2_copilot_on_review_request.md` |
| 22 April 2026 | Phase 1b empirical map (`ss8_empirical_map_extended.py` output) catalogues residuals across $N_\alpha \in \{6, 8, 10, 12, 14\}$ × $N_\text{ex} \in \{3, \ldots, 8\}$ — 26 of 30 cells with current data, 4 cells data-pending. Residuals 8–15%, systematically negative. | `series_strong/papers/SS-8/sketches/SS-8_Phase1_extended_map_findings.md` |
| 23 April 2026 | Formal `research_frontier.md` entry created for OPEN-SS-28 with priority MEDIUM. Three identified residual mechanisms registered: H3′ opposite-polarity pair bonus, H4′ Pauli decrement at higher $N_\text{ex}$, H5′ small-polytope attenuation. | `research_frontier.md` |
| 24 April 2026 | SS-8 v1.0 §5 secondary content explicitly bounds the 8–15% precision band as OPEN-SS-28-attributable degradation. The §5 result stands independently of any §4 outcome. | `series_strong/papers/SS-8/SS-8_interstitial_neutron_2EV_scaling.tex` |
| 26 April 2026 | OPEN-SS-28 paper reference cleaned to "Target paper: SS-9 candidate or later" per Session 1 high-priority registry update (patch 0027) | `research_frontier.md` |

---

## What we know now

**The empirical signature of D3 degradation is clean and structurally identified.** SS-8 v1.0 §5 catalogues the secondary 30-cell residual map with three explicit degradation sources:

1. **Leading-order-only H4′ form.** The H4′ Pauli-decrement model is first-order in $(N_\text{ex} - 2)/V$. Higher-order corrections would tighten the $N_\text{ex} \in \{5, 6, 7, 8\}$ rows but require a full derivation that captures how additional interstitial neutrons see the depleted vertex distribution left by their predecessors. This is the largest single source of degradation and the most tractable to attack: a clean derivation of D3 produces the higher-order correction directly.

2. **Bulk-regime assumption broken at $N_\text{ex}/V \sim 0.5$.** At $N_\text{ex} = 8$, $V = 14$, the ratio $N_\text{ex}/V = 0.57$ is not "$\ll 1$" — the uniform-vertex-distribution averaging assumption is approximate. This is a quantitative-approximation breakdown, not a categorical failure: a derived form of D3 with explicit error bounds would predict the residual size at any given $N_\text{ex}/V$ rather than treating it as an empirical band.

3. **Polytope-identity fine structure at non-unique $N_\alpha$.** For $N_\alpha$ values admitting multiple simplicial deltahedra (notably $N_\alpha = 6, 12$), the specific realized polytope could introduce up to ±2% variation from the $2E/V$ average. First-principles polytope identification is content of OPEN-SS-24 — methodologically related but distinct from OPEN-SS-28's bulk-regime work.

**The residual decomposition discipline is "no hidden mechanisms."** SS-8 v1.0 explicitly chose not to absorb the residuals into a generic "pairing bonus" coefficient that would parameterize the deviation. Instead, the H3′/H4′/H5′ provisional residual model identifies *named structural mechanisms* (opposite-polarity pair bonus inherited from SS-5's K₃ pair mechanism; Pauli decrement at higher $N_\text{ex}$ inherited from SS-5's same-polarity ratio; small-polytope attenuation from D3 breakdown at $N_\alpha \leq 4$) and applies them with no fitted parameters. The discipline is honest: the named mechanisms either work or they don't, and the residual decomposition succeeds or fails on the basis of named structural inheritance rather than on parametric tuning.

The cost of the discipline is that the residual band is wider than it would be under tuning. The benefit is that the falsification routes are sharp: if H3′'s inherited $1/\varphi^2$ attenuation gives the wrong magnitude or sign, the decomposition fails directly rather than being rescued by a tuned coefficient. SS-8 v1.0 documents that H3′ matches the +0.98 MeV per pair implied by the bulk-regime residual to within 10%, supporting the inheritance interpretation; this is a successful falsification test of H3′.

**The empirical residual is consistent in sign across all 26 mapped cells.** The systematic negative residual (in $k_\text{eff}^\text{obs} - k_\text{eff}^\text{pred-H4'}$) at $N_\text{ex} \in [3, 8]$ suggests the H4′ Pauli coefficient $c_\text{Pauli} \approx 1/\varphi \approx 0.618$ is too small. If a higher-order H4′ derivation gives $c_\text{Pauli}^\text{true}$ closer to 0.7–0.8 from first principles (rather than fitting), the residual band would tighten substantially without parameter adjustment.

---

## Candidate scope for closure

A paper attacking OPEN-SS-28 would need to deliver three things:

1. **A derivation of D3 with explicit error bounds.** State the bulk-regime averaging assumption formally, identify the small parameter ($N_\text{ex}/V$ or similar), and derive the leading-order plus next-to-leading-order corrections. Verify that the $\mathrm{O}(N_\text{ex}^2/V^2)$ correction has the right size to account for the observed secondary-regime residual.

2. **A first-principles derivation of the H4′ Pauli decrement to higher order.** SS-5's same-polarity ratio gives $c_\text{Pauli} = 1/\varphi$ at leading order; the SS-8 secondary regime residual suggests the next-order term is comparable in magnitude. Deriving that next-order term would tighten the secondary 30-cell residual band from 8–15% to under 5%.

3. **A residual decomposition with no hidden mechanisms.** The decomposition should be parameter-free (each mechanism inherits its coefficient from prior CPP work, not fitted in this paper) and should account for the observed residual sign and magnitude across all 26 mapped secondary cells. Cells that the decomposition cannot explain would be registered as residual problems with explicit physical interpretation, not absorbed into a numerical correction.

A paper closing OPEN-SS-28 would convert SS-8's THEO-SS-15 (2E/V scaling law) from "conditional on D3" to a more refined statement with explicit error bounds. This would not promote the conditional theorem to unconditional on its own — that requires OPEN-SS-26 and OPEN-SS-27 closure as well — but it would substantially tighten the empirical band on SS-8's secondary 30-cell predictions and provide a falsifiable derived form of D3.

---

## Methodological observations

**OPEN-SS-28 is the most empirically exposed of the three SS-8 sub-problems.** D1 and D2 are categorical and either hold or fail — no graceful degradation. D3 is quantitative and degrades smoothly with $N_\text{ex}/V$. The 8–15% precision band on SS-8's secondary 30-cell regime is exactly D3's empirical signature, which means a derivation of D3 has a sharp falsification target: it either reproduces the observed residual band size and sign as a function of $N_\text{ex}/V$, or it doesn't.

**The "no hidden mechanisms" discipline is portable.** SS-8 v1.0's choice to decompose the residual into named inheritance mechanisms rather than tuning a coefficient is a programme-level methodological standard that applies beyond SS-8. SS-7's RMS 0.80% residual on the strict-$N{=}Z$ alpha-chain is a smaller residual, but the same discipline applies: future SS-7 refinements should identify named mechanisms rather than tune coefficients. The OPEN-SS-28 closure work would establish this discipline empirically by showing it can succeed at higher precision.

**OPEN-SS-28 is methodologically distinct from OPEN-SS-26 (Level-3) and OPEN-SS-27 (D2 structural derivation).** Closing OPEN-SS-26 Level-3 requires constructing a new model that delivers D1 without proximity-binding. Closing OPEN-SS-27 requires extending A6′ to the per-edge polytope setting. Closing OPEN-SS-28 requires deriving a quantitative approximation with explicit error bounds and a parameter-free residual decomposition. The three problems share the SS-8 lineage but require different mathematical machinery.

**OPEN-SS-28 closure has the smallest leverage on the swarm-count promotion.** Closing OPEN-SS-26 + OPEN-SS-27 jointly converts 54 of the 55 conditional D-N entries to unconditional (the entire SS-7 + SS-8 conditional stack, excluding only PRED-C-31 string tension). Closing OPEN-SS-28 alone does not unconditionalize any entry — it tightens the precision band on SS-8's secondary 30-cell extension but does not remove the conditional dependency on D1 + D2. This makes OPEN-SS-28 a lower-leverage SS-9 candidate than OPEN-SS-26 or OPEN-SS-27.

---

## What's needed to close OPEN-SS-28

A paper would need to:

1. State the bulk-regime averaging assumption formally with a small parameter and derive the leading-order plus next-to-leading-order forms.
2. Derive the H4′ Pauli decrement to higher order from SS-5's same-polarity ratio framework. Verify $c_\text{Pauli}^\text{true}$ closer to 0.7–0.8 emerges from the derivation, not from fitting.
3. Decompose the observed secondary-regime residual using H3′/H4′/H5′ with no fitted parameters; account for sign and magnitude across all 26 mapped cells.
4. Re-state THEO-SS-15 (the 2E/V scaling law) with explicit error bounds replacing the current "conditional on D3" form.
5. Update SS-8's secondary 30-cell precision band from 8–15% (current) to under 5% (post-closure target).

---

## Cross-references

- `research_frontier.md` § OPEN-SS-28 — the formal registry entry
- `axiom-registry.md` — Pattern 6 scale recurrence observation; SS-5 same-polarity ratio source
- `theorem-registry.md` — THEO-SS-15 (2E/V scaling) — current statement is "conditional on D3"
- `series_strong/papers/SS-8/SS-8_interstitial_neutron_2EV_scaling.tex` v1.0 §5 — secondary 30-cell extension and OPEN-SS-28 attribution
- `series_strong/papers/SS-8/sketches/SS-8_Phase1_extended_map_findings.md` — empirical map data
- `series_strong/papers/SS-5/` — SS-5's same-polarity ratio derivation (source of H4′ leading-order $c_\text{Pauli}$)
- `problem_histories/PH-OPEN-SS-26.md` and `problem_histories/PH-OPEN-SS-27.md` — sibling problem histories
- `future_projects.md` Project 0f — OPEN-SS-28 as SS-9 candidate (rank 5 of 7 by leverage)

---

*Problem history file maintained per `templates/research_frontier_architecture.md` problem-history format. Append new dated entries to the timeline as the problem evolves; do not retroactively edit prior entries.*
