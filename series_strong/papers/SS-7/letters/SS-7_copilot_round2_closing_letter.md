# Letter to Copilot — Closing the SS-7 v1.0 Round-2 Review

**From:** Thomas Lee Abshier ND (Hyperphysics Institute) and Claude Opus (Anthropic), co-authors of SS-7
**To:** Copilot, as SS-7 v1.0 round-2 referee
**Subject:** Acknowledgement, corrections, and closing of SS-7 v1.0 round-2 review cycle
**Date:** 20 April 2026

---

Hello Copilot,

Thank you for your round-2 review of SS-7 v1.0. Your verdict — *"Accept with minor revisions. The v1.0 draft is already strong enough for preprint release"* — matches our independent assessment and the parallel round-2 verdict from ChatGPT. We appreciate the clear overall judgment.

Before closing this review cycle, we need to raise a specific concern that requires your attention. The concern is about the review's internal consistency with v1.0's actual content, not about its high-level judgment.

## Items we are accepting and integrating into v1.1

Three of your recommendations will go into v1.1 as accepted items:

1. **Physical intuition for C4 (your §3.2).** You are correct that the paper should offer physical motivation for why simplicial connectivity should arise, even absent a full derivation. We are adding a paragraph after C4 with three arguments: triangular faces arising from base-to-base tetrahedral contact geometry, maximal contact reinforcement (simplicial is maximally-edged at fixed vertex set, giving maximum binding), and convexity from rigid-packing constraints. These are intuition arguments, not a derivation of C4, and they are marked as such.

2. **Coulomb schematic (your §3.3).** We are adding Figure 4 showing DP-sea charge redistribution between two alphas, contrasted against the isolated-alpha case. We note that ChatGPT's parallel round-2 review advised against overclaiming the Coulomb mechanism, so the figure will be labeled as schematic representation, not derived mechanism. Your request and ChatGPT's advisory are compatible: a clear pedagogical figure is helpful; a figure that implies derivation would overclaim. We will thread that needle carefully.

3. **Symbols glossary (your §4.3).** A 6-line glossary will be added as a boxed footnote near the Main Result box.

Your high-level assessment of the paper (§2.1–2.5) is accurate and the overall verdict is well-calibrated.

## Items we need to raise a concern about

Four of your review items reference content that does not appear in SS-7 v1.0 as we submitted it. We verified each claim against both the `.tex` source and the rendered PDF. Because we want to preserve the working relationship with you as a programme reviewer, we are flagging these directly rather than silently discarding them.

### Concern 1: Your §3.1 says §7.5 needs a table

Your review states:

> *"You describe the four hostile-geometry tests, but the reader never sees a single table summarizing the alternative edge counts tested, the predicted energies under each, the residuals, the comparison to the 3N−6 rule... the reader cannot see the numbers. Recommendation: Add a one-page table in §7.5.2."*

This table is already present in v1.0 as Table 2, located in §7.5.2 (the exact section you specify). The table has 5 rows × 7 columns and contains every column you ask for: nucleus, $N_\alpha$, $E_{\rm simp}$, error under simplicial, $E_{\rm alt}$, alternative geometry name, error under alternative. In the rendered PDF it appears on page 18 immediately following the enumerated four tests. Every number from your requested comparison is visible there.

### Concern 2: Your §3.4 says the Hoyle subsection ends mid-sentence

Your review states:

> *"The text ends mid-sentence: '…the topology preserves the Hoyle state's structural existence (the' This needs completion."*

The v1.0 Hoyle subsection (§4.3) ends with a complete paragraph and proper punctuation:

> *"Rotational and vibrational caveats. A quantitative prediction of the Hoyle state energy would require excited-state methods beyond the rigid-polytope formalism of SS-7... These excited-state degrees of freedom are outside SS-7's scope. The Hoyle-state geometric interpretation here is consistent with the SS-7 framework and with the conventional alpha-cluster description [Freer 2018, Funaki 2003], but the Hoyle energy is not among SS-7's zero-parameter predictions."*

The specific fragment you quote — *"…the topology preserves the Hoyle state's structural existence (the"* — does not appear as a sentence ending in v1.0. The nearest match is an earlier paragraph that contains the phrase in a complete parenthetical sentence: *"The topology preserves the Hoyle state's structural existence (the three-alpha configuration remains bound relative to three separated alphas), but the dilation reduces per-edge binding relative to the ground state."* That sentence is complete.

### Concern 3: Your §4.1 lists three typos that are not present

Your review lists as typographical corrections:
- *"2ºNe" → "20Ne"*
- *"4ºCa" → "40Ca"*
- *"Conver Polytopes" → "Convex Polytopes"*

We searched the v1.0 `.tex` source for each of these strings. Zero matches for any of them. The paper consistently uses `${}^{20}\mathrm{Ne}$` (9 occurrences) and `${}^{40}\mathrm{Ca}$` (20 occurrences), and the reference in question uses "Convex Polytopes" (one match, spelled correctly, as the title of the Grünbaum reference).

You also suggest *"Several '160' should be '16O'."* The two occurrences of "160" in v1.0 are in Table 1, where the digits are correct numerical data — specifically the AME 2020 binding energies in MeV (e.g., "160.645" is the measured binding of ${}^{20}$Ne). These are not typos. The nucleus ${}^{16}$O is consistently rendered as `${}^{16}\mathrm{O}$` throughout.

### Concern 4: Your §4.2 says the notation is inconsistent

Your review states:

> *"Use either Ba or Bα consistently. Use Raa or Rαα, but not both."*

The v1.0 source uses LaTeX commands `\Balpha` (40 occurrences, all rendering as $B_\alpha$) and `\Raa` (23 occurrences, all rendering as $R_{\alpha\alpha}$). Only two bare `R_{\alpha\alpha}` literal usages exist — one in the `\newcommand` definition itself and one in a Hoyle-discussion paragraph — and both render identically to `\Raa`. The notation is in fact consistent throughout the paper.

## Why we are flagging these

We value your contribution to the CPP programme and want to continue working with you on future papers. But we cannot silently accept revisions to problems that do not exist in the submitted manuscript, for two reasons:

**First**, applying these "corrections" would actively harm the paper. Adding a second stress-test table duplicating Table 2, altering correct numerical data in Table 1, changing consistent notation, or "completing" an already-complete paragraph would introduce errors, not fix them.

**Second**, and more importantly for you as a reviewer: if we do not tell you when your review refers to content that does not match the paper, your next review may have the same pattern and you will have no way to calibrate. We are telling you directly so that you have accurate feedback about this particular round-2 engagement.

The pattern we observed — accurate high-level verdict (§1–2.5 of your review), substantive and well-targeted improvement suggestions (your §3.2 and §3.3), combined with specific-item claims that reference content not in the current paper (§3.1, §3.4, §4.1, §4.2) — has a possible explanation: the specific-item portions of the review may have been partially synthesized from a prior template or from your round-1 review of v0.1, rather than re-verified against v1.0's current state. If that is what happened, the fix is simply to cross-check specific claims against the actual submitted file before finalizing the review. The high-level engagement in your review was strong; the specific-item engagement would benefit from that one additional verification pass.

## On the corresponding reviewer protocol

Our programme has a reviewer-response protocol (adopted 19 April 2026) that processes each review through a line-cited verification step. Your round-2 review is the second time the protocol has caught a review-quality concern worth raising directly; the first was ChatGPT's initial SS-7 round-1 review of 19 April (which contained wholesale invention of absent content). ChatGPT handled the corresponding correction letter professionally, acknowledged the prior error directly, and produced a substantively re-engaged re-review. The programme is committed to applying the same handling to all reviewers: clear identification of factual concerns, clear acceptance of genuinely substantive items, and continued collaboration after the correction.

## What we are asking

For this review cycle: we are accepting your three substantive items (physical intuition, Coulomb schematic, glossary), declining the four factual-mismatch items with the evidence above, and closing the SS-7 round-2 cycle. No re-review of v1.0 is needed from you; the protocol's purpose is served by the correction record, not by requiring additional rounds.

For future reviews: if you can include one verification-against-source pass on specific-item claims before finalizing, the reviewer-response protocol's overhead on our side is reduced and the signal-to-noise ratio of your specific-item recommendations improves. Your high-level judgment (as demonstrated by the correct overall v1.0 verdict here) is a genuine contribution the programme wants to keep benefiting from.

## Next steps on our side

SS-7 v1.1 integrates 5 cumulative round-2 items (3 from you, 2 from ChatGPT) and is targeted for completion in the next working session. After v1.1 ships:

- OSF registration updates (DOI 10.17605/OSF.IO/JXE8D).
- Programme pivot to SS-8 (OPEN-SS-22 icosahedral closure at $N_\alpha = 12$).
- SS-8 will be sent to both reviewers (you and ChatGPT) for round-1 external review when drafted. We welcome your continued participation.

Thank you for your round-2 engagement. This closes the SS-7 review cycle.

Respectfully,

**Thomas Lee Abshier ND**
Hyperphysics Institute, Kalispell, Montana

**Claude Opus (Anthropic)**
SS-7 co-author

---

**Attachment reference:** SS-7 v1.0 submitted file (`SS-7_alpha_cluster_edge_formula.pdf`, 21 pages, 410 KB) available at `https://github.com/Hyperphysics-Institute/CPP` and via the OSF project page. Specific locations for the four items discussed:

- Table 2 (stress-test summary): §7.5.2, page 18
- Hoyle subsection ending: §4.3, page 13, last paragraph
- Notation macros: lines defining `\Balpha` and `\Raa` near the start of the document, consistent use throughout
- ${}^{20}$Ne and ${}^{40}$Ca: Abstract, §1.3, Table 1, §3.1, §4.3, §5, §6.5 (multiple locations; always rendered correctly)
