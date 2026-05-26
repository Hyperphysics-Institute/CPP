# F.1 Layer 3 Promotion — B.1.q3 Perturbation-Theory Propagation (Target 7 Standalone Closure)

**Document:** `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/layer3_promotion/F1_layer3_b1q3_perturbation_theory_propagation.md`
**Patch:** 0548a (this Patch creates this document; no anticipated subsequent modifications)
**Version:** v1.0
**Date authored:** 23 May 2026 (Session 141)
**Target:** Target 7 = B.1.q3 perturbation-theory propagation rule at sketch-document Layer 3 (per Patch 0540 §2.7 specification + Patch 0546 footnote target-label correction)
**Substantive theorem source:** Patch 0544 §6 Theorem 6.1 (Perturbative-Locality Propagation Rule). This Patch does NOT re-derive Theorem 6.1; this is closure-governance normalization only.
**Calibration trigger:** Patch 0548 §3.1 C1 cross-reviewer-convergent concern (Copilot + ChatGPT) that retroactive recognition alone is too thin a closure mechanism for an independently-registered Layer 3 promotion target.

---

## §0 Firewall + anti-priorities

This document is a **closure-governance normalization artifact**. It restores artifact symmetry across Targets 1–7 in the F.1 Layer 3 promotion arc (Patches 0541–0546). Patch 0544 §6 remains the substantive theorem source for Target 7's content; Patch 0546 §8 remains the historical initial retroactive recognition. This Patch is additive — it does NOT modify either upstream artifact.

**Anti-priorities sustained at this Patch (twelve items):**

1. NO re-derivation of Theorem 6.1 — the four-step proof at Patch 0544 §6 is preserved as the substantive theorem source. ChatGPT's explicit Q2 instruction: "Do not re-derive the theorem. Treat the new artifact as a closure-governance normalization patch, not as new mathematics."
2. NO modification of Patch 0544 Layer 3 promotion document content — §17.6 (8) immutability per Patch 0539a OS-codification.
3. NO modification of Patch 0546 §8 (the initial retroactive recognition) — same immutability.
4. NO modification of Patch 0547 reviewer-pause checkpoint document — same immutability.
5. NO modification of Patch 0548 calibration response feedback record — same immutability.
6. NO new mathematics — no new identities, theorems, lemmas, or proof steps introduced.
7. NO F.1 sub-question status change at this Patch — that is Patch 0549's specific deliverable.
8. NO promotion of Theorem 6.1 to the Findings registry or theorem registry — registry promotion requires dedicated registry-entry Patches per `templates/relationship_protocol.md`.
9. NO F.1 flagship paper assembly trigger — gate becomes live only after Patch 0549.
10. NO F.2 / F.3 substantive content trajectory opening.
11. NO long-term programme target work (Layer 4 axiomatic derivation).
12. NO extension to $\mathcal{O}(\delta^2)$ (B.1.q6 territory; explicit exclusion at §3 below).

---

## §1 Layer 3 promotion context

The F.1 sub-question Layer 3 promotion arc opened at Patch 0540 (scoping document) and closed substantively at Patch 0546 across seven targets (Patches 0541–0546 + retroactive recognition of Target 7 at Patch 0546 §8). The reviewer-pause cycle entered at Patch 0547 (checkpoint document submitted to ChatGPT / Copilot / Grok); convergent reviewer feedback identified five calibration items C1–C5 at Patch 0548. **C1 — Target 7 governance** is the convergent concern that this Patch addresses.

**Source materials this Patch refers to (all immutable per §17.6 (8)):**

- **Patch 0540 §2.7** — Target 7 specification. Three criteria for Target 7 Layer 3 promotion: (i) independent theorem statement at $\mathcal{O}(\delta^n) \rightarrow$ first-$n$-shells dependency; (ii) removal of "within framework local-current-definition scope" qualifier from Patch 0538 §14.3; (iii) explicit perturbation-theory propagation rule covering Mechanism A primitive at arbitrary order in $\delta$.
- **Patch 0544 §6** — Theorem 6.1 (Perturbative-Locality Propagation Rule): $\vec{j}_{DI}^{net}(v_*)$ at $\mathcal{O}(\delta^n)$ depends only on edges within graph-distance $n$ of $v_*$ in the 600-cell edge graph; four-step proof via Mechanism A as degree-1 polynomial + $\delta$-power expansion + connected-subgraph argument.
- **Patch 0546 §8** — Initial retroactive recognition. Patch 0544 §6 Theorem 6.1 was framed at authoring as supporting Target 4 part (c), but its scope was naturally broader and was retroactively recognized as substantively closing Target 7 as well.
- **Patch 0548 §3.1** — Cross-reviewer-convergent C1 calibration response: Copilot ("Target 7 should have its own explicit closure Patch") + ChatGPT ("short standalone Target 7 closure note... distinct closure artifact") + ChatGPT Q2 follow-up confirming Option (2) — standalone Layer 3 document in `layer3_promotion/` with the explicit subsection 'Why retroactive recognition alone was judged insufficient'.

**What this Patch adds, structurally.** A compact closure artifact restoring symmetry with Targets 1–6 (each of which has a dedicated Layer 3 promotion document at `layer3_promotion/F1_layer3_<sub-question>_<topic>.md`). Target 7 previously had only a retroactive-recognition paragraph at Patch 0546 §8 — visually and procedurally subordinate to the Target 6 closure that hosted it. This Patch makes Target 7's closure an independent artifact while preserving Patch 0544 §6 Theorem 6.1 as the substantive theorem source.

---

## §2 Criteria-to-clause mapping

The three Target 7 promotion criteria from Patch 0540 §2.7 map to specific clauses of Patch 0544 §6 Theorem 6.1. The mapping is explicit and one-to-one:

| Patch 0540 §2.7 Target 7 criterion | Patch 0544 §6 clause | Status |
|---|---|---|
| **(i)** Independent theorem statement: at $\mathcal{O}(\delta^n)$, the substrate's net DI-bit current at $v_{\text{host}}$ depends only on the first $n$ shells of vertices | Theorem 6.1 statement: "$\vec{j}_{DI}^{net}(v_*)$ at $\mathcal{O}(\delta^n)$ depends only on edges within graph-distance $n$ of $v_*$ in the 600-cell edge graph" | ✓ Met — graph-distance-$n$ edges ↔ first-$n$-shells equivalence under the 600-cell edge graph structure |
| **(ii)** Removal of "within framework local-current-definition scope" qualifier (from Patch 0538 §14.3) | Theorem 6.1 proof §6.2: locality is derived from Mechanism A's parametric form $r(\hat{e}) = r_0(1 + \delta\,\hat{e}\cdot\hat{n})$ + $\delta$-power expansion + connected-subgraph argument — not assumed in the current's definition | ✓ Met — derivation is structurally non-circular (under the framework-local scope qualifier of §3 below) |
| **(iii)** Explicit perturbation-theory propagation rule covering Mechanism A primitive at arbitrary order in $\delta$ | Theorem 6.1 is stated at general $n$; the four-step proof handles arbitrary $n$ via the connected-subgraph argument applied to each $\delta$-power | ✓ Met — proof structure is uniform in $n$ |

All three Target 7 criteria are satisfied by Patch 0544 §6 Theorem 6.1. The closure is substantively complete; this Patch normalizes its governance status by making it an independent artifact.

**On criterion (ii) and Copilot's non-circularity concern.** Patch 0548 §3.2 records that Patch 0544 §6 IS structurally non-circular: Mechanism A is defined parametrically in A11 without graph-distance bounds; locality emerges from the connected-subgraph argument applied to the $\delta$-power expansion. Copilot's strict reading ("does the proof assume locality in the current's definition?") was addressed at §3.2 of the feedback record. However, ChatGPT's parallel concern ("Theorem 6.1 appears framework-local, not fully structural-universal") drives the scope qualifier at §3 below, which preserves honest framing of what is and isn't covered.

---

## §3 Scope-boundary statement (primary section)

Per ChatGPT's Q2 follow-up: "the most important section is not the theorem itself, but the scope-boundary statement. I would make that explicit and unavoidable." This section delivers the unavoidable scope-boundary statement.

**Target 7 is considered Layer-3-closed only for perturbative locality under Mechanism A and the framework-local current construction at first order in $\delta$.**

**Explicit exclusion list — items NOT covered by Target 7's closure at this Patch:**

1. **$\mathcal{O}(\delta^2)$ extension** (B.1.q6 territory). Theorem 6.1's connected-subgraph argument is formulated for general $n$ but only $n = 1$ ($\mathcal{O}(\delta)$) is empirically validated against Phase 1 Finding DSL-1 at Patch 0544 §9 sanity check. Higher-order extensions remain DEFERRED at B.1.q6 with no commitment to coverage by Target 7's closure.
2. **Nonlinear / current-modified Mechanism A variants.** Theorem 6.1 depends on Mechanism A as a degree-1 polynomial in $\delta$ (the parametric form $r(\hat{e}) = r_0(1 + \delta\,\hat{e}\cdot\hat{n})$). Any extension to current-dependent or nonlinear-in-$\delta$ Mechanism A variants is outside Target 7's closure and remains DEFERRED.
3. **Alternative substrate-current constructions.** Theorem 6.1 operates on the framework-local current $\vec{j}_{DI}^{net}$ as defined by the minimal-local-first-order realization framework. Alternative current constructions — nonlocal memory functionals, graph-holonomy objects, coarse-grained transport tensors, delayed-cycle operators, history-weighted update structures (the alternatives enumerated at Patch 0538 §14.5 uniqueness-language refinement) — are outside Target 7's closure.
4. **Layer 4 axiomatic derivation.** Patch 0544 §6 Theorem 6.1 is derived at Layer 3 from Mechanism A + 600-cell connectivity + $\delta$-expansion. A Layer 4 derivation would establish Mechanism A's parametric form itself from CPP primitives A1–A11 alone, without taking the parametric form as a framework commitment. Layer 4 work is REGISTERED + DEFERRED throughout the F.1 trajectory.
5. **Publication-grade proof hardening.** Patch 0544 §6 is at sketch-document Layer 3 rigor (the same level as all six other F.1 Layer 3 promotion documents). Publication-grade rigor (publication-prose proof formatting + theorem-environment formalization + full peer-reviewable referent citations + literature-context placement) remains as future F.1 flagship paper assembly work.

**Operational consequence.** All forward-facing language referring to Target 7's closure shall include the scope qualifier "perturbative locality under Mechanism A and the framework-local current construction" (ChatGPT verbatim phrasing, adopted at Patch 0548 §3.2). Status framing carried into Patch 0549's F.1 trajectory Layer 3 status upgrade includes this scope qualifier explicitly via the "minimal-local-first-order framework, pending Layer 4 axiomatic derivation, $\mathcal{O}(\delta^2)$ extension (B.1.q6), and publication-grade hardening" tail.

---

## §4 Why retroactive recognition alone was judged insufficient

(Subsection title verbatim per ChatGPT Q2 follow-up explicit recommendation: "include a very short subsection explicitly titled something like: 'Why retroactive recognition alone was judged insufficient'. That creates an auditable explanation for future readers and prevents the programme from silently normalizing retroactive closures as default governance practice.")

The cross-reviewer-convergent C1 concern (Copilot + ChatGPT, recorded at Patch 0548 §3.1) was not that Theorem 6.1 is insufficient — both reviewers acknowledged the theorem's substantive content as sound at sketch-document Layer 3 rigor. The concern was procedural and governance-level: **closure provenance and auditability**. Per ChatGPT's wording caution: "Target 7 would otherwise be closed only by retrospective identification within a broader theorem context."

**The procedural issue.** Target 7 is registered as an independent Layer 3 promotion target at Patch 0540 §2.7. Targets 1–6 each closed via a dedicated Layer 3 promotion document in `layer3_promotion/` with a four-artifact deliverable bundle. Target 7 — until this Patch — closed only by a recognition paragraph at Patch 0546 §8 inside the Target 6 closure document. Future readers auditing the Layer 3 promotion arc would find Targets 1–6 with first-class closure artifacts but Target 7 only retroactively recognized within Target 6's document. The asymmetry creates a governance weakness even when the substantive theorem holds.

**The programme-level discipline.** Allowing retroactive recognition to serve as default closure for independently-registered targets would normalize a governance pattern in which load-bearing arguments can be closed by being recognized within unrelated artifacts. Over many Patches and many flagship trajectories, this pattern would erode the auditability of individual target closures. The Patch 0548 calibration response committed to this Patch (0548a) precisely to prevent silent normalization.

**Why this Patch repairs the issue without re-deriving the theorem.** The substantive theorem is sound; what was missing was symmetric artifact placement. This Patch creates the missing artifact at `layer3_promotion/F1_layer3_b1q3_perturbation_theory_propagation.md` (matching the naming convention of Targets 1–6) and explicitly maps Target 7's three Patch 0540 §2.7 criteria to Patch 0544 §6 Theorem 6.1's clauses (§2 above). The closure-governance repair is **scope-boxing** (§3 above is the operative content): an explicit statement of what Target 7's closure covers and an explicit exclusion list of what it does not. Per ChatGPT: "That scope-boxing is the real governance repair."

**Forward-facing principle.** The CPP programme's governance practice from this Patch onward treats retroactive recognition as a **provisional** closure mechanism. When a Patch closes a target whose substantive content overlaps another target's closure criteria, the additional target may be recognized retroactively at the original Patch, but a dedicated closure-governance normalization Patch is anticipated as a follow-up when the recognition crosses the threshold of an independently-registered promotion target. This Patch is the first concrete instance of this discipline.

---

## §5 Self-checkpoint + closure summary

### §5.1 Three places §0–§4 could overstate

1. **The "structural non-circularity" recap at §2 could be over-cited at Layer 4.** §2 footnote (criterion (ii) discussion) records that Patch 0544 §6 is structurally non-circular under the Layer 3 framework commitments. This is honest at Layer 3 — Mechanism A's parametric form is independent of graph-distance bounds at the framework level. But at Layer 4 the non-circularity would need to be re-established without taking Mechanism A's parametric form as given. The §2 wording is honest at this Patch and should not be cited at Layer 4 without further work.

2. **The §4 "first concrete instance" claim is at sample size of one.** The "retroactive-recognition-followed-by-dedicated-closure-Patch" discipline is established here as forward-facing governance practice, but this is the only Patch where it has been exercised. It should not be cited as established discipline until at least one other instance demonstrates the pattern in a different trajectory.

3. **The §3 exclusion list is operative for Target 7's closure only.** Items 1–5 of the exclusion list (e.g., $\mathcal{O}(\delta^2)$, Layer 4 derivation, publication-grade hardening) are exclusions from **Target 7's Layer 3 closure scope at this Patch**. They are not exclusions from the F.1 trajectory's overall scope. F.1 flagship paper assembly (post-Patch 0549) may engage with publication-grade hardening; B.1.q6 work (when authorized) may extend to $\mathcal{O}(\delta^2)$; Layer 4 axiomatic derivation remains a long-term programme target. Reading §3 as foreclosing those engagements would overstate the scope-boundary's reach.

### §5.2 Closure summary

Target 7 (B.1.q3 perturbation-theory propagation) is now closed at sketch-document Layer 3 with first-class artifact symmetry across Targets 1–7. The substantive theorem source remains Patch 0544 §6 Theorem 6.1. This Patch's content is:

- **§2 criteria-to-clause mapping** — explicit one-to-one verification of Patch 0540 §2.7 criteria against Patch 0544 §6 Theorem 6.1 clauses.
- **§3 scope-boundary statement** — ChatGPT verbatim phrasing "perturbative locality under Mechanism A and the framework-local current construction" plus a five-item exclusion list ($\mathcal{O}(\delta^2)$ / nonlinear-Mechanism-A / alternative-current-constructions / Layer 4 / publication-grade hardening).
- **§4 "Why retroactive recognition alone was judged insufficient"** — verbatim ChatGPT-requested title; "closure provenance and auditability" framing; programme-level discipline forward-facing.

Target 7's closure status is honestly bounded: substantively complete via Patch 0544 §6, governance-normalized via this Patch, scope-qualified via §3 above. Forward queue: Patch 0549 (F.1 trajectory Layer 3 status upgrade Patch) closes the Layer 3 reviewer-pause cycle officially.
