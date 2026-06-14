# C1 mass-ordering provenance audit — does SF-4/SM-5 force normal ordering, or is the package "TBD" correct?

**Patch:** 1207 (SF-2 external-validation campaign, 1200-block). **Cycle:** gating reconcile from the Patch 1206 forward queue (Priority 1). **Type:** corpus provenance audit — reconciles the C1 mismatch ChatGPT flagged at PSQ1 of the Patch 1204 portfolio consultation. **Not** a verdict-moving review; **not** new physics. Self-contained.

**Convening mismatch (ChatGPT, Patch 1204 PSQ1):** the portfolio package (`sf2_portfolio_scoping_review_package_v1.0.md` §2) marks candidate **C1 (neutrino mass ordering)** as "**TBD by panel**," while SF-4 repository summaries list hierarchy ordering among the *derived* neutrino outputs. ChatGPT correctly judged that a pre-registration campaign cannot carry that ambiguity, and made resolution the gating step before C1 can be ranked.

---

## Verdict

**The package's "TBD by panel" mark on C1 is STALE / INCORRECT. Normal mass ordering is FORCED-DERIVED in SF-4 and registered as a shipped zero-parameter prediction (PRED-C-16). The mismatch resolves in favor of the corpus, not the package.** C1 reclassifies from *TBD* to **FORCED-DERIVED, with moderate-but-diluted pre-registration value** (three caveats below). This is a genuine upgrade over the package's parking — but the dilution is why C1 should not auto-displace the C5/C7 tracks adjudicated at Patch 1206.

---

## What the corpus actually says (evidence)

| Source | Statement | Attribution / mechanism cited |
|--------|-----------|-------------------------------|
| `flagship_papers/neutrinos/sf-4_neutrinos.tex` §abstract + §cageassignment | "Normal mass hierarchy is forced by the cage-shell assignment (ν₁→V=4, ν₂→V=12, ν₃→V=30)." Listed as **FORCED CONSEQUENCE** in the deliverables table; one of the **7/8 zero-parameter predictions** ("normal hierarchy (1 prediction)"). | Cage-shell **V² monotonicity**: V₁=4 < V₂=12 < V₃=30 ⟹ m₁<m₂<m₃, with {4,12,30} forced by 600-cell topology + SM-1 four-cage taxonomy. |
| `sf-4_neutrinos.tex` §falsifier_juno | "The framework **cannot accommodate inverted hierarchy** — no permutation of the cage-shell assignment is consistent with V ∈ {4,12,30} … while reproducing the observed splittings." Clean named falsifier: JUNO inverted-hierarchy confirmation kills the cage-shell assignment. | Topological non-accommodation of IO. |
| `predictions.md` PRED-C-16 | "Neutrinos have normal mass ordering · ν₁ < ν₂ < ν₃ · **Normal ordering favoured (current data)** · Consistent." | "**σ suppression**," sourced to "**SM-1 §8**." |
| `predictions.md` swarm map (SM-1 row) | PRED-C-7 ("mass ordering") and PRED-C-16 ("neutrino ordering") both grouped under SM-1. | SM-1. |
| `theory-overview.md` §summary + SF-4 row | "normal hierarchy forced." | SF-4. |
| `README.md` | SF-4 "… normal hierarchy forced." | SF-4. |
| `paper_catalog.md` SF-4 v1.0 row | "normal hierarchy forced" among the 7/8 zero-parameter predictions. | SF-4. |

The *claim* — normal ordering is forced — is **internally consistent across every summary and the flagship `.tex`.** It is not TBD anywhere in the corpus except the (stale) portfolio-package §2 mark. ChatGPT's flagged "repo says derived" reading is correct.

---

## Why the package said TBD (root cause)

The portfolio package was drafted as a *forward-looking scoping inventory* and carried several candidates at "TBD by panel" as placeholders pending exactly this kind of audit (C1, C2, C6 all so marked). For C1 specifically, the TBD reflects the *package author's* deferral, not the corpus state — SF-4 had already shipped the forced-ordering prediction at v1.0 (Session 54) and preserved it through v4.4. The TBD is a provenance-staleness artifact, not a real open question. **The package is not retroactively edited** (it is the shipped Patch 1204 consultation artifact reviewers already responded to); this audit supersedes its C1 mark on the record.

---

## Three caveats qualifying how C1 should re-enter the portfolio

### Caveat 1 — Attribution is split across the corpus (touches an at-risk shared file)

The *claim* is consistent, but the *cited mechanism and source are not*:

- **SF-4 `.tex`** attributes the forcing to the **cage-shell V² monotonicity** (V₁<V₂<V₃ from the topologically-forced {4,12,30} assignment).
- **`predictions.md` PRED-C-16** attributes it to "**σ suppression**" and sources it to "**SM-1 §8**" (not SF-4).

These are plausibly two readings of the same underlying structure (the σ-suppression and the V²-scaling both ride the same cage-shell assignment), but for a *pre-registration-grade* derivation chain the attribution must be single and clean. **Recommended unification:** make SF-4's cage-shell V² assignment the canonical derivation of record, and update PRED-C-16's mechanism/source field to cross-reference SF-4 (retaining the SM-1 §8 lineage as the upstream cage-taxonomy input). **This edit lands on `predictions.md`, which is on the multi-window at-risk shared set — it is NOT made in this patch.** It is registered here as a recommended follow-up; land it only with a stop-and-warn + re-sync before push.

### Caveat 2 — The forcing is structurally robust

The ordering depends only on the **monotonicity** V₁<V₂<V₃ given the {4,12,30} assignment, which is forced by 600-cell topology + SM-1 cage taxonomy. It does **not** depend on the absolute σ_ν magnitude or the K3-coupling fine structure (the OPEN-FP-SF-4-1/-2 work, itself largely closed at v2.0–v4.0). The ordering is therefore the **most theorem-stable single output of SF-4** — stronger footing than the absolute-mass-scale claims. For pre-registration purposes this is the good news: the forcing survives even if the suppression-magnitude residuals were reopened.

### Caveat 3 — Pre-registration novelty is diluted

Normal ordering is **already the experimentally favored option.** SF-4 §falsifier_juno itself notes the NuFIT 6.0 global fit shows a mild preference for normal ordering; `predictions.md` PRED-C-16 records the status as "Normal ordering favoured (current data)." JUNO's *decisive* ~3σ determination is a multi-year program (~6 years of full operation → roughly 2028–2031). So as a pre-registration target C1 is:

- ✓ forced, falsifiable, named, and already shipped (strong);
- ✓ not-yet-*decisively*-confirmed — a real future JUNO confirmation event exists;
- ✗ but the field already leans normal, so confirmation is a *leaning confirmation*, not a coin-flip resolution. The novelty is real but partial.

This is the decisive nuance neither the package (TBD) nor a naive "derived, ship it" reading captures: C1 is a legitimate Category-A candidate, **not** an automatic primary.

---

## Portfolio implication (recommendation, not a verdict move)

**Reclassify C1 in the next portfolio iteration:** `TBD by panel` → **`FORCED-DERIVED (PRED-C-16; SF-4 cage-shell V² assignment); pre-registration value MODERATE-but-diluted (experimental prior favors NO; decisive JUNO ~3σ pending ~2028–2031); attribution-unification recommended (predictions.md, at-risk)`**.

Consequence for the Patch 1206 adjudication: this *strengthens* C1 relative to the package's parking but does **not** overturn the DEFERRED verdict or displace the two-track C5/C7 plan. C1's diluted novelty is precisely why the portfolio should lead with a less-diluted track (C5 reframe / C7 closure) while C1 stands as an already-shipped clean falsifier that JUNO will adjudicate on its own timeline regardless of campaign framing. C1 is best positioned as a **standing Category-A falsifier in the portfolio**, available for promotion to primary in a *follow-on* consultation if a sharper not-yet-hinted angle (e.g., a quantitative ordering-plus-splitting joint prediction) is developed.

---

## Registry-touch ledger (what this audit recommends, and where)

| Recommended edit | Target file | At-risk? | Status |
|------------------|-------------|----------|--------|
| Unify PRED-C-16 attribution (σ-suppression/SM-1 §8 → cross-ref SF-4 cage-shell V²) | `predictions.md` | **YES (shared registry)** | **NOT made in 1207; warn-and-resync before landing** |
| Reclassify C1 in portfolio inventory (TBD → FORCED-DERIVED + dilution annotation) | next portfolio-consultation package (lane-private) | No | deferred to next portfolio iteration |
| Cross-reference this audit from SM.md OPEN-SM-4 / CHIR.md OPEN-CHIR-1d | `frontier_sectors/SM.md`, `frontier_sectors/CHIR.md` | **YES (shared registry)** | optional housekeeping; warn-and-resync before landing |

No edit on the at-risk set is made in this patch. No verdict moves; no theorem/prediction registrations; header/theorem count UNCHANGED. All chirality-arc verdicts (V3/W3; W3→W1 candidate conditional on Mechanism A; CAPACITY-1 reserved) stand unchanged.

---

*Audit produced Patch 1207 (Session 159, 13 June 2026) on Thomas's authorization, as the gating Priority-1 reconcile from the Patch 1206 cycle-close forward queue. Finding: C1 normal ordering is FORCED-DERIVED (PRED-C-16; SF-4), not TBD — the portfolio package's mark is stale; the corpus summaries are correct. Pre-registration value moderate-but-diluted (experimental prior favors NO; JUNO decisive ~3σ ~2028–2031). One recommended downstream attribution-unification lands on `predictions.md` (at-risk) and is deliberately deferred to a warn-and-resync patch. Band-discipline: 1200-block SF-2 portfolio lane; 09xx H1 sprint continues in its own lane.*
