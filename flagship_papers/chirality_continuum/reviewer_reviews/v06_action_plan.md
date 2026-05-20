# v0.6 Reviewer Cycle — Round 1 Action Plan

**Cycle**: v0.6 reviewer cycle, Session 1 — ChatGPT round-1 review captured at Patch 0504
**Companion document**: `chatgpt_round1.md` (ChatGPT review captured verbatim)
**Action plan status**: Patch 0504 captures and categorizes; Patch 0505+ executes integration

---

## Top-line verdict on ChatGPT round-1 review

Substantively positive review. ChatGPT identifies the programme's trajectory of explanatory-scope-control, emergent-vs-primitive chirality framing, cleaner orientation hierarchy, and improved open-problem identification as strong v5 advances. The reviewer's central concerns (dynamical-substrate-law gate, mathematical inevitability, EFT mapping precision, retrospective-closure danger, mechanism figure) substantially align with our own §8 Open Theorem-Level Work + §9 Discussion scope-limitation framing — meaning the review's critical content is mostly what we have already acknowledged as future-window work.

The single most concrete actionable item is the **master mechanism figure** (Figure 1 at §1 Introduction).

---

## Categorization of feedback

### A. Strengths acknowledged (no action needed; record for posterity)

ChatGPT identifies six strongest features of v5:
1. Chirality treated as emergent constraint rather than primitive ontology
2. Orientation-closure hierarchy is cleaner
3. Weak-sector routing is more plausible
4. Framework controls ontological inflation
5. Closure logic is the real core
6. Better at identifying open problems

All six are consistent with our own framing. No paper changes required; record in PH for trajectory tracking.

### B. Actionable for v0.6 integration (Patch 0505+)

| Priority | Item | Scope | Estimated patches |
|---|---|---|---|
| 1 | **Master mechanism figure (Figure 1) at §1 Introduction** | Canonical cognitive map showing substrate primitive $\hat{n}$ + $\|\chi\| = \varphi^{-3}$ → three substrate objects (K3-doublet + W-bracelet + qDP/eDP) → bridge theorem $\chi/6 \to \chi/6$ at Layer 4 → sector-specific operators (V--A current vs $\Delta F^{qDP}$) → observable scale (leptogenesis CP-asymmetry) + theorem dependencies + falsifiers + dynamical-substrate-law gate (future-window). | 1 patch (Patch 0505) |
| 2 | **Sharper chirality-as-emergent-constraint framing at §1** | Make the philosophical shift more explicit at §1.1 or §1.2: substrate primitive is $\hat{n}$ (the 4D direction); chirality magnitude $\|\chi\| = \varphi^{-3}$ is derived from $\hat{n}$ + 600-cell polytope edge-length ratios; chirality structure emerges from substrate orientation + closure inheritance rather than being assumed as primitive. | 1 patch (Patch 0506) |
| 3 | **Elevate dynamical-substrate-law gate framing at §8** | Reorganize §8 to put the dynamical-substrate-law gate as §8.1 (primary subsection rather than one bullet item among many). Make it the section's organizing principle: "the defining next gate identified by reviewers + the most load-bearing open theorem-level item." | 1 patch (Patch 0506) |

### C. Deferred to future-window (aligned with §8 Open Theorem-Level Work)

ChatGPT's deepest concerns are already acknowledged as future-window work in our paper:

| Concern | Our existing acknowledgment | Future-window registration |
|---|---|---|
| **Genuine dynamical law / action principle / substrate evolution equation** | §8.1 + §9.3 explicitly identify the dynamical-substrate-law gate as the defining next gate for the Capotauro programme | Q1$'$+Q1$'$.A Layer 3 promotion programme; THEO-SD-CHIR-3/-4 candidates at substrate level |
| **Mathematical inevitability / uniqueness** | §6.4 zero-parameters framing + §8.1 FI-CHIR-CONT-2 first-principles closure as future-window | Layer 1 substrate-dynamics derivation of $\hat{n}$ from CPP primitive axioms |
| **EFT mapping precision: gauge emergence + chirality protection mechanisms** | §8.3 Picture A alternative continuum-EFT framework + §3.7 topological-projection argument with leading-order claim | Picture A as complementary closure to Picture B Wigner-Eckart framework |
| **EFT mapping precision: mass-sector projection** | Partly addressed at §4.3 Michel parameter derivation + §5.4 BAU back-derivation; deeper mass-spectrum derivation not in scope | SF-line follow-up work (SF-2 v2.0+ mass-sector closures + SF-6 electromagnetism unified) |
| **Retrospective closure danger** | §7.2 six falsifiers articulate quantitative experimental thresholds at $> 3\sigma$ significance | Could be strengthened by §9.4 "On the retrospective-closure danger and our falsifiability commitments" subsection at Patch 0506; light-touch addition |

### D. Cosmetic/framing improvements (light-touch v0.6 polish)

| Item | Scope | Estimated patches |
|---|---|---|
| Tighten §3.7 topological-projection argument exposition | Small clarifications around RG-flow correspondence (ChatGPT calls this "renormalization correspondence" interpretive gap) | Part of Patch 0506 |
| Possible §9.4 "Failure modes and falsifiability commitments" subsection | Explicit framing addressing retrospective-closure danger; structures the existing six falsifiers + future-collider precision targets as "what would convince us we're wrong" | Part of Patch 0506 (or skip if §7.2 + §8.5 framing is judged sufficient) |

---

## Integration sequence

| Patch | Scope | Title-block | Lines added (est.) |
|---|---|---|---|
| **0504** (this patch) | ChatGPT round-1 review capture + action plan | unchanged: v0.5 (SHIPPED) | 0 to .tex |
| **0505** | Figure 1 master mechanism diagram at §1 introduction | bump to v0.6 (DRAFT) | ~50-100 to .tex (TikZ figure + caption + cross-references) |
| **0506** | §1 chirality-as-emergent framing sharpening + §8 dynamical-substrate-law gate elevation + light-touch polish items | bump to v0.6 (SHIPPED) | ~30-50 to .tex |
| **0507+** | CoPilot round-1 review submission + integration | v0.7 cycle | TBD |
| **0508+** | Grok round-1 review submission + integration | v0.8 cycle | TBD |
| **0509+** | Final reviewer-cycle iterations + v1.0 SHIP | v0.9 → v1.0 SHIPPED | TBD |

---

## Anti-priorities at v0.6 integration

- Do NOT attempt to close the dynamical-substrate-law gate at v0.6. This is genuine future-window work (Q1$'$+Q1$'$.A Layer 3 promotion programme) and cannot be done as part of paper polish; trying would either fail or inflate the paper's scope beyond what its Layer 4 closure can support.
- Do NOT add new theorems or predictions at v0.6 integration. Theorem-level content is frozen at v0.5 SHIP.
- Do NOT modify §3 substantive proof content during EFT-mapping clarifications. Clarifications stay at exposition level; proof structure is frozen at v0.5 SHIP.
- Do NOT attempt to address every reviewer concern. Some concerns are deep future-window items that paper polish cannot resolve; addressing them would be performative rather than substantive.
- Do NOT modify Capotauro v2.0 / SF-2 v1.0 / SM-2 v1.0 .tex sources during integration.
- Do NOT promote paper to v0.7 SHIPPED at Patch 0506. v0.6 SHIPPED is the end-state of ChatGPT round-1 integration; v0.7 cycle begins with CoPilot or Grok round-1 submission.

---

## Programme-level observation on ChatGPT round-1 review

The review confirms the joint paper's substantive maturation trajectory. The most important programme-level signal is ChatGPT's framing:

> "The framework is now organized enough that the absence of a dynamical substrate law becomes the dominant visible gap. Ironically, that is evidence of progress."

This matches the programme's own internal characterization of the dynamical-substrate-law gate as the defining next gate (registered at §8.1 + §9.3 of the joint paper; tied to the Q1$'$+Q1$'$.A Layer 3 promotion programme). External reviewer confirmation that this is the right next gate is valuable programme-state information independent of the v0.6 paper integration.

---

## End of v0.6 round-1 action plan
