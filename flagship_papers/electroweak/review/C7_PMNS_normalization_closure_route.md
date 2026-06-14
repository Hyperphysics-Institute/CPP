# C7 PMNS normalization-closure route map — and why the high-upside swing does not connect

**Patch:** 1209 (SF-2 external-validation campaign, 1200-block). **Cycle:** Priority-3 deliverable from the Patch 1206 cycle-close forward queue — the high-payoff parallel track whose success would upgrade the portfolio to PORTFOLIO-READY with C7 primary. **Type:** closure route map + empirical-viability assessment for candidate **C7** (JUNO solar PMNS angle), resolving the consultation's central disagreement (PSQ7). **Not** new physics; **not** a verdict-moving review of the chirality arc. Self-contained; verification script bundled (`C7_PMNS_normalization_closure_route_verify.py`).

---

## Verdict

**Do NOT elevate C7 to primary. The high-upside swing does not connect — C7 is high-RISK, not high-payoff.** Copilot's "bounded, closure-feasible → excellent primary" rests on a premise that does not survive an empirical check: the candidate value **sin²θ₁₂ = 12/40 = 0.300 is on a falsification trajectory against JUNO**, the very experiment C7 is named for. The portfolio stays **PORTFOLIO-DEFERRED with C5 as the backbone** (Patch 1206 verdict unchanged). The route map below documents what closure would require, but it is gated behind an empirical-viability question that currently points the wrong way.

This refines Copilot's PSQ7 the way the Patch-1207 audit refined ChatGPT's PSQ1: on the merits, not by head-count.

---

## 1. What C7 actually is (OPEN-SM-5)

C7 traces to **OPEN-SM-5** (`frontier_sectors/SM.md`, "PMNS Mixing Angles — Analytic Derivation," last updated 23 March 2026):

- **Goal:** derive the PMNS angles analytically from 600-cell subgroup overlaps.
- **Solution shape:** exact overlap fractions |G_i ∩ G_j|/|G_i| for all pairs, **with normalization *derived* (not fitted)**, matching NuFIT to 3–4 digits.
- **Current best lead:** Monte-Carlo overlap analysis matches NuFIT to 3–4 digits, **but the normalization is currently fitted**; the headline rationals are sin²θ₁₂ = 12/40 = 0.300 and sin²θ₂₃ = 12/21 ≈ 0.571.

The fitted normalization is exactly the gap C7 closure must fill. Copilot judged that gap a bounded representation-theory task; the assessment below is less optimistic on two independent grounds.

## 2. Scope correction — C7-as-"JUNO" is sin²θ₁₂ only

The candidate is titled "JUNO solar oscillation parameter tightening," but only **sin²θ₁₂** is a JUNO observable. **sin²θ₂₃ = 12/21 is an *atmospheric* angle**, measured by accelerator long-baseline experiments (DUNE, T2HK, NOνA), not by JUNO's reactor-antineutrino program. So the JUNO-facing content of C7 reduces to the single prediction **sin²θ₁₂ = 12/40 = 0.300**. (θ₂₃ belongs to a different experiment and a different window; folding it into a "JUNO" candidate over-counts the campaign value.)

## 3. Empirical viability — the gating finding (points the wrong way)

JUNO's first physics result (Nov 2025, 59.1-day exposure) already measures the solar angle at percent level:

$$\sin^2\theta_{12}^{\rm JUNO\,2025} = 0.3092 \pm 0.0087,\qquad \Delta m^2_{21} = (7.50\pm0.12)\times10^{-5}\,{\rm eV}^2.$$

JUNO's projected **ultimate precision is σ ≈ 0.003** on sin²θ₁₂ (decisive-test level). Against the CPP value 0.300:

| Comparison | Tension |
|------------|---------|
| vs JUNO 2025 (σ = 0.0087) | **1.06σ** (low, acceptable now) |
| at JUNO ultimate (σ ≈ 0.003) | **3.07σ** |
| at σ ≈ 0.0015 (full-run optimistic) | **6.1σ** |

The trajectory is unambiguous: **0.300 is ~1σ low today and heads toward ~3σ tension as JUNO sharpens**, *assuming the JUNO central holds near 0.309*. This is not idle worry — JUNO is presently in the business of killing discrete-flavor-symmetry θ₁₂ rationals: of the five (four) A₄/S₄/A₅ cases allowed by global data at 3σ for NO (IO), only three (two) survive after the first JUNO measurement. The CPP rational 0.300 sits in exactly that class, on the low side, ~3σ from where JUNO is pointing.

**Consequence:** a *derived* 0.300 that JUNO falsifies at 3σ is the worst possible outcome for an external-validation campaign — a clean, pre-registered, wrong prediction. C7 closure does not de-risk the campaign; it *adds* a falsification exposure on the campaign's named experiment.

## 4. Structural diagnosis — where the "fitted normalization" enters

The headline form is an overlap fraction |G_i ∩ G_j|/|G_i| with G_i, G_j subgroups of the 600-cell symmetry group H₄ (|H₄| = 14400). By Lagrange, any genuine subgroup order must divide 14400. Checking the stated denominators:

| Denominator | 14400 / d | Subgroup-order-admissible? |
|-------------|-----------|----------------------------|
| 12 (numerator) | 1200 | yes |
| 40 (θ₁₂) | 360 | yes |
| **21 (θ₂₃)** | **685.7…** | **NO — 21 ∤ 14400** |

**The 12/21 form cannot be a clean subgroup-overlap fraction**: 21 is not the order of any subgroup of H₄. This is the structural fingerprint of the fitted normalization — the denominators are normalization constants chosen (via the MC fit) to land near NuFIT, not group orders read off the lattice. (40 *could* be a subgroup order, so θ₁₂ is less obviously broken than θ₂₃, but SM.md states the normalization is fitted for both, and 40 is not established as derived.)

So the closure faces a structural problem deeper than "tighten a loose constant": at least one of the current best-lead rationals (12/21) is **not of overlap-fraction form at all**, which means the MC "match to 3–4 digits" is doing work a derived construction may not reproduce.

## 5. What closure would require (the route, gated behind §3)

If C7 were pursued despite §3, the derivation chain is:

1. **Identify the stabilizer subgroups.** Fix G_i = the little group (stabilizer in H₄, or in the relevant icosahedral/A₅ sub-action on the K3 cage) of each neutrino mass eigenstate ν₁, ν₂, ν₃. These must be honest subgroups (orders dividing 14400), specified from the cage geometry, not chosen.
2. **Compute the overlap fractions from group orders.** |G_i ∩ G_j|/|G_i| for the (1,2) pair → sin²θ₁₂. No free constant: the denominator *is* |G_i|, the numerator *is* |G_i ∩ G_j|.
3. **Reproduce (or correct) 12/40 without a fitted normalization.** Either the stabilizer orders yield 12/40 = 0.300 intrinsically (→ falsification risk per §3), or they yield a different rational closer to 0.309 (→ viable). **This is the lock-to-0.300 question and it is the cheap gate that should run *before* any group-theoretic work.**
4. **Theoremize at Layer 3.** Promote the overlap-fraction construction to a theorem with the stabilizer assignment as the load-bearing input; register a prediction entry with an honest theory band.
5. **Falsifier statement.** State the JUNO acceptance/falsification band explicitly (e.g., predicted sin²θ₁₂ vs JUNO σ ≈ 0.003).

## 6. Feasibility verdict (vs Copilot's "bounded 2–3 patch task")

C7 closure is **not** the bounded, low-risk swing Copilot described. It carries **two independent failure modes**:

- **Structural:** the current best-lead rationals are partly non-overlap-form (12/21 violates Lagrange), so a *derived* normalization may not reproduce the MC fit at all — the "3–4 digit match" may be fit artifact, not structure.
- **Empirical:** even if the construction cleanly derives 0.300, that value is on a ~3σ JUNO falsification trajectory. A derived-and-falsified prediction is negative campaign value.

Either failure mode alone is disqualifying for a *primary*. Together they make C7 a poor bet for the high-payoff slot.

## 7. Recommendation

1. **Do not elevate C7 to primary; do not schedule the group-theoretic closure patches yet.** The Patch-1206 verdict stands: **PORTFOLIO-DEFERRED, C5 backbone.** The two-track plan resolves with C5 (now-shippable, Patch 1208) as the campaign's pre-registration, C7 *not* upgrading the portfolio to READY.
2. **If C7 is pursued at all, run the cheap gate first (§5 step 3):** a single targeted check of whether the stabilizer-overlap construction is *locked* to 0.300 or can flex toward the JUNO central ~0.309. Only if it can flex toward 0.309 — and only then — is the full group-theoretic closure worth funding. Estimated cost of the gate: 1 patch. Estimated cost of full closure if the gate passes: 3–5 patches (more than Copilot's 2–3, given the Lagrange complication).
3. **Reclassify C7 in the portfolio inventory:** `Category B; depends on normalization closure` → `Category B, HIGH-RISK; JUNO falsification trajectory (0.300 vs JUNO 0.3092±0.0087 → ~3σ at ultimate precision); θ₂₃ leg is a DUNE/T2HK target not JUNO; closure gated on lock-to-0.300 question`.
4. **Net effect on the campaign:** the two-track gamble does not pay out on C7. C5 is the backbone and the de-facto pre-registration; C1 (Patch 1207) is a standing forced-derived falsifier on JUNO's mass-ordering timeline; C7 recedes to a gated, high-risk longer-shot. The honest campaign primary is **C5's joint (n_s-tightening, α_s) pre-registration** from Patch 1208.

## 8. Verification

Bundled script `C7_PMNS_normalization_closure_route_verify.py` checks: the Lagrange divisibility of {12, 40, 21} against |H₄| = 14400 (21 fails); the rational values 12/40, 12/21; and the JUNO tension of 0.300 at σ ∈ {0.0087, 0.003, 0.0015}. All checks reproduce the table values (1.06σ now → 3.07σ at ultimate → 6.1σ optimistic).

## Registry-touch ledger

| Recommended edit | Target | At-risk? | Status |
|------------------|--------|----------|--------|
| Update OPEN-SM-5 "current best lead" with the JUNO-2025 tension + Lagrange-21 diagnostic + lock-to-0.300 gate | `frontier_sectors/SM.md` | **YES (shared registry)** | **NOT made; warn-and-resync if desired** |
| Reclassify C7 in portfolio inventory (Category B → Category B HIGH-RISK) | next portfolio-consultation package (lane-private) | No | deferred to next portfolio iteration |

No at-risk shared file is touched in this patch. No verdict moves; no theorem/prediction registrations; header/theorem count UNCHANGED. All chirality-arc verdicts (V3/W3; W3→W1 candidate conditional on Mechanism A; CAPACITY-1 reserved) stand unchanged.

---

*Route map produced Patch 1209 (Session 159, 13 June 2026) on Thomas's authorization, as Priority-3 of the Patch 1206 forward queue (the high-payoff C7 track). Finding: the swing does not connect — C7's sin²θ₁₂ = 12/40 = 0.300 is on a ~3σ JUNO falsification trajectory (JUNO 2025: 0.3092 ± 0.0087; ultimate σ ≈ 0.003), the θ₂₃ leg (12/21) is a DUNE/T2HK target not a JUNO one and violates Lagrange (21 ∤ 14400), and the normalization is genuinely fitted. C7 is HIGH-RISK not high-payoff; do NOT elevate to primary. Portfolio stays PORTFOLIO-DEFERRED with C5 backbone (Patch 1206 unchanged); the campaign's de-facto pre-registration is C5's joint (n_s, α_s) from Patch 1208. If C7 is pursued, run the cheap lock-to-0.300 gate before any group-theoretic closure. Band-discipline: 1200-block SF-2 lane; lane-private files, no at-risk shared file touched; 09xx H1 sprint continues in its own lane.*
