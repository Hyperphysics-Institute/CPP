# Reviews — F.1 Dynamical Substrate Law: Substrate-Locality of DI-Bit Currents at Vertex-Aligned Reading C in the 600-Cell

> **v1.0 SHIPPED STATUS NOTE (Patch 0572b, 24 May 2026, Session 143)**: This file is written at F.1 v1.0 SHIPPED state (Patch 0570, Session 142, 24 May 2026). The reviewer-engagement cycle is **definitively closed** with strongest-positive ChatGPT verdict at Round 6 + explicit Grok Round 1 v1.0 SHIP-acceptable + implicit Copilot Round 1 SHIP-acceptable with tier-ranked recommendations. Round 6 PDF-upload protocol identified and resolved the TikZ-rendering processing artifact that produced recurring-pattern recommendations at Rounds 3–5; the diagnostic resolution is now codified as a programme-level reviewer-engagement convention candidate (METH-PDF-UPLOAD-DEFAULT-REVIEWER). Full review-cycle details in `changelog-dynamical-substrate-law.md` v1.0 SHIPPED entry. This file is a historical record of the v0.9 → v1.0 SHIP-cycle reviewer engagement; future paper-version increments (v1.1 minor revisions, v2.0 substantive extensions) trigger new review cycles archived in additional Part 1 round sections below.

**Paper:** `flagship_papers/dynamical_substrate_law/dynamical_substrate_law.tex` (v1.0 SHIPPED 24 May 2026, Session 142 Patch 0570)
**Source letters:** `flagship_papers/dynamical_substrate_law/reviews/` (9 archived reviewer letters + 1 synthesis document)
**Last updated:** 24 May 2026 (Session 143 Patch 0572b)

---

## Review status

**Reviewer-engagement cycle:** v0.9 → v1.0 SHIP cycle, Session 142, Patches 0568 (Round 1 archival + synthesis) → 0569 (Round 1 multi-edit response) → 0569a (Round 2) → 0569b (Round 3) → 0569c (Round 4 diagnostic-framing) → 0569d (Round 5 recurring-pattern documentation) → 0569e (Round 6 diagnostic resolution).

**Reviewer panel composition:**

- **Round 1 (3 reviewers, parallel)**: Copilot v0.9 + Grok v0.9 + ChatGPT v0.9. Archived at Patch 0568 with synthesis classification (1 MUST-ADDRESS + 4 SHOULD-ADDRESS + 5 CAN-DEFER + 2 DECLINED).
- **Rounds 2–6 (ChatGPT-only)**: ChatGPT v0.9 v2 (R2) → v0.9 v3 (R3) → v0.9 v4 (R4) → v0.9 v4 round 5 (R5) → v0.9 v5 round 6 (R6). Copilot and Grok Round 1 SHIP-acceptable verdicts stood throughout subsequent ChatGPT rounds; no Round 2+ engagement with Copilot/Grok was required.

**Cross-reviewer convergent verdict at v1.0 SHIP:**

- **Grok Round 1:** EXPLICIT *"v1.0 SHIP-acceptable as the F.1 flagship paper (Dynamical Substrate Law)"*.
- **Copilot Round 1:** implicit SHIP-acceptable with tier-ranked recommendations (Tier 1: G1 + umbrella hardening; Tier 2: executive summary + δ² appendix; Tier 3: Layer 4 derivation + non-vertex-aligned Reading C).
- **ChatGPT R1 → R2 → R3 → R4 → R5 → R6:** monotonic verdict improvement from *"NOT yet publication-grade flagship overall"* at R1 to *"substantially more credible, rigorous, and publishable than all earlier versions; first version that feels architecturally stable, epistemically disciplined, mathematically centered, structurally self-aware"* at R6 (strongest-positive).

---

## Part 1 — Formal reviews

### Round 1: Copilot v0.9 (Session 142, Patch 0568 archival) — *Positive (implicit SHIP-acceptable with tier-ranked recommendations)*

**Source:** `copilot_v0.9_session_142.md`
**Verdict (overall):** SHIP-acceptable with Tier 1 / Tier 2 / Tier 3 ranked-recommendation framework. Mathematical verification of three calculations (host-to-first-shell projection $\hat{u}_i \cdot \hat{n} = -1/(2\phi)$; icosahedral sum $\sum_{i=1}^{12} \hat{u}_i = -6\hat{n}/\phi$; final current $\vec{J}_1 = 6\hat{n}/\phi^2$) all "Correct."

**Strengths cited:**

- Layer-distinction discipline (§8 + throughout): *"exceptionally clear"*.
- Hardened-trio integration (Patches 0550 + 0551 + 0552): *"integrated cleanly"* into §§5–6.
- Geometric primitives G1, G2: *"used with precision"*.
- Mechanism A formalization: *"formalized cleanly"* as framework axiom.
- Perturbation-locality engine: *"rigorous"*.

**Tier-ranked recommendations:**

- **Tier 1 (Most Impactful):** (1) Harden G1 [OPEN-FP-F1-3]; (2) Harden Theorem 7.1 umbrella.
- **Tier 2 (Substantial):** (3) Add executive summary to §1 introduction; (4) Add δ² appendix sketch.
- **Tier 3 (Long-Term):** (5) Outline Layer 4 derivation of Mechanism A; (6) Begin notes on non-vertex-aligned Reading C variants.

**Critiques accepted vs. declined at Patch 0569:**

- Accepted (SHOULD-ADDRESS at Patch 0569): Tier 2 #3 executive summary at §1.
- Deferred (CAN-DEFER, registered as Open Problems): Tier 1 #1 G1 hardening → OPEN-FP-F1-3 (RECOMMENDED first post-Phase-7 substantive physics Patch); Tier 1 #2 Theorem 7.1 umbrella hardening → §7.4 candidate follow-up Patch note (not formal Open Problem to preserve 5-OP commitment); Tier 2 #4 δ² appendix → OPEN-FP-F1-1; Tier 3 #5 Layer 4 derivation → OPEN-FP-F1-2; Tier 3 #6 non-vertex-aligned variants → OPEN-FP-F1-5.

**Integration outcomes:** all 6 Copilot recommendations integrated either via Patch 0569 (executive summary) or via Open-Problem registration (5 of 6) per synthesis classification §3.

### Round 1: Grok v0.9 (Session 142, Patch 0568 archival) — *Positive (explicit v1.0 SHIP-acceptable)*

**Source:** `grok_v0.9_session_142.md`
**Verdict (verbatim):** *"(A) v1.0 SHIP-acceptable as the F.1 flagship paper (Dynamical Substrate Law) — proceed to the reviewer-engagement cycle (Patches 0568–0569 + 0569a) followed by v1.0 SHIP closeout (Patch 0570)."* Most permissive of the three Round 1 reviewers. Decisive SHIP-acceptable verdict with critical assessment of zero structural gaps.

**Strengths cited (verbatim):**

- *"Layer discipline and anti-erasure (§8 + throughout): Every theorem carries its precise Layer label in parentheses... reviewer-honesty discipline operating at its best."*
- *"Integration of the hardened-trio artifacts: §§5–6 import the three `hardened_theorems/` artefacts (741 lines total) as direct, verbatim building blocks... The assembly is at sketch-document Layer 3, correctly not promoted."*
- *"Conditionality and scoping honesty: Mechanism A is explicitly a framework axiom... G1 remains at sketch-document Layer 3... The five Open Problems (§9) are independent, substantive, and correctly cross-referenced."*
- *"Structural payoff: The closed-form result $\vec{j}_{DI}^{\text{net}}(\vhost) = (6\delta/\phi^2)\hat{n} + \mathcal{O}(\delta^2)$ at $\mathcal{O}(\delta^1)$ is clean, parallel to Capotauro v2.0 §3 (shared structural constant $-1/(2\phi)$)."*

**Critical assessment (§7.1–§7.3 style):** *"Structural gaps: None in the load-bearing arc. Premature closures: None. Layer-confusion risks: None material."*

**Four minor polish items (optional, non-blocking):**

1. Bibliography BibTeX style switch (cosmetic).
2. Table 8.2 caption clarification.
3. Abstract names three theorems explicitly.
4. Date/version metadata update at SHIP.

**Critiques accepted vs. declined at Patch 0569:**

- Accepted (SHOULD-ADDRESS at Patch 0569): #2 Table 8.2 caption clarification; #3 Abstract three-theorem naming; #4 Date/version metadata (landed at Patch 0570 SHIP).
- Declined: #1 Bibliography BibTeX integration (already declined at Tier 4 §56.3 Patch 0567 deliberation; switching would require modifying body content with `\cite{}` commands disrupting 10-Patch editorial consistency).

**Integration outcomes:** 3 of 4 polish items integrated; 1 declined with explicit rationale.

### Round 1: ChatGPT v0.9 (Session 142, Patch 0568 archival) — *Mixed positive (strong pre-v1.0 internal flagship draft; not yet publication-grade flagship overall)*

**Source:** `chatgpt_v0.9_session_142.md`
**Verdict (verbatim):** *"strong pre-v1.0 internal flagship draft with credible theorem architecture and unusually disciplined conditionality handling, but still awaiting two decisive hardening steps: 1. G1 publication-grade hardening; 2. independent publication-grade hardening of Theorem 7.1."*

**Strengths cited:**

- *"The paper has a real architectural spine"* — coherent hierarchy from first-shell primitives to umbrella theorem.
- *"Scope qualifiers are unusually disciplined"* — Layer-distinction handling.
- *"The perturbation-locality theorem is the strongest section"* — §6 perturbation-theory propagation rule.
- *"Open-problem handling is excellent"* — 5 substantive, independent OPs.

**Four major concerns:**

1. *"The paper still depends critically on unproven geometric primitives"* (G1 + G2).
2. *"Theorem 7.1 is under-hardened relative to its centrality"* — umbrella at sketch-document Layer 3.
3. *"The physics interpretation remains underjustified"* — thermodynamic-arrow framing gap. *"Why should DI-bit propagation asymmetry induce thermodynamic arrow structure?"*
4. *"The symmetry arguments occasionally move too quickly"* — Step 3 of Theorem 7.1 proof.

**Four recommendations:**

1. Harden Theorem 7.1 independently.
2. Harden G1 before v1.0 if possible.
3. Separate "thermodynamic arrow" from "substrate directional current" (rename or rescope).
4. Reduce governance language by ~20–30% (repeated Patch references, Layer reminders).

**Critiques accepted vs. declined at Patch 0569:**

- Accepted (MUST-ADDRESS at Patch 0569 + SHOULD-ADDRESS): #3 Thermodynamic-arrow framing gap addressed via abstract + §1.1 + §10 triple-coverage at Patch 0569 (the single MUST-ADDRESS classification at synthesis §3.1); #4 Step 3 symmetry argument addressed via §7.3 representation-theoretic justification at Patch 0569.
- Deferred (CAN-DEFER, registered as Open Problems): #1 G1 dependency → OPEN-FP-F1-3; #2 Theorem 7.1 hardening → §7.4 candidate follow-up Patch note.
- Declined: #4 Reduce governance language ~20–30% — all three Round 1 reviewers praise the governance/Layer-distinction discipline as a paper strength; the discipline is operationalised at §8.3 (named "anti-erasure discipline"), Table 8.2 (Layer hierarchy), and throughout via theorem parenthetical labels — these are load-bearing, not redundant.

**Integration outcomes:** 2 of 4 substantive recommendations integrated at Patch 0569 (Concern #3 + Concern #4 Step 3); 2 deferred as Open Problems with explicit registration; recommendation #4 declined with cross-reviewer-convergent counter-rationale.

### Round 1 Synthesis (Session 142, Patch 0568) — Cross-reviewer cumulative position

**Source:** `synthesis_v0.9_to_v1.0_session_142.md`

**Classification summary (12 items):**

- **§3.1 MUST-ADDRESS at Patch 0569 (1 item)**: Thermodynamic-arrow framing gap (ChatGPT Concern #3) — scope-qualifier sharpening across abstract + §1.1 + §10 + executive summary.
- **§3.2 SHOULD-ADDRESS at Patch 0569 (4 items)**: §7.3 Step 3 representation-theoretic justification (ChatGPT Concern #4); Executive summary at §1 (Copilot Tier 2 #3); Table 8.2 caption clarification (Grok minor #2); Abstract names three theorems explicitly (Grok minor #3).
- **§3.3 CAN-DEFER (5 items)**: δ² appendix → OPEN-FP-F1-1; G1 hardening → OPEN-FP-F1-3; Theorem 7.1 hardening → §7.4 candidate follow-up; Layer 4 derivation → OPEN-FP-F1-2; Non-vertex-aligned Reading C → OPEN-FP-F1-5.
- **§3.4 DECLINED (2 items)**: Bibliography BibTeX integration (Grok minor #1) + Reduce governance language ~20–30% (ChatGPT Recommendation #4).

**Patch 0569 response plan:** 8 atomic LaTeX edits implementing 5 reviewer-cycle items (1 MUST-ADDRESS + 4 SHOULD-ADDRESS).

### Round 2: ChatGPT v0.9 v2 (Session 142, Patch 0569a archival) — *Positive (substantial improvement; reviewer-ready as disciplined pre-v1.0 framework paper)*

**Source:** `chatgpt_v0.9v2_session_142.md`
**Verdict (verbatim):** *"Proceed to reviewer engagement. Do not yet ship as final v1.0 unless v1.0 is explicitly scoped as: structurally-grounded sketch-document Layer 3 flagship preprint, with publication-grade hardened components but a non-publication-grade umbrella theorem. The manuscript is now much less overclaimed and much more structurally honest."*

**What improved most:** Explicit distinction between substrate-locality structure and full thermodynamic-arrow emergence (the main R1 overclaim). New §1 executive summary. Revised §7.3 Step 3 with representation-theoretic justification.

**Four remaining major concerns:**

1. Theorem 7.1 still not independently hardened.
2. G1 remains the exposed dependency.
3. "Scenario A closure" language still slightly too strong — soften to "Scenario A closure at the substrate-locality-support level" or "substrate-locality component required for Scenario A closure."
4. Connected-subgraph confinement proof (Lemma 6.3.1) is the least transparent mathematical step.

**Recommended changes before v1.0:** (1) Soften Scenario A closure language; (2) Add clarification sentence after Lemma 6.3.1; (3) Add note at §7.4 that umbrella hardening requires independent treatment; (4) Make G1 hardening the next patch if possible.

**Integration outcomes at Patch 0569a (4 atomic edits):**

- Accepted: #1 §1.2 "substrate-locality component required for Scenario A closure" clarification clause; #2 Lemma 6.3.1 unperturbed-step clarification added AFTER existing proof (calibration discipline preserved); #3 §7.4 "structural rather than editorial" hardening note.
- Also addressed at Patch 0569a: author email update to `drthomas@protonmail.com`.
- Deferred: G1 hardening as OPEN-FP-F1-3 (recommended first post-Phase-7 substantive physics Patch).

### Round 3: ChatGPT v0.9 v3 (Session 142, Patch 0569b archival) — *Positive (credible flagship framework theorem paper)*

**Source:** `chatgpt_v0.9v3_session_142.md`
**Verdict (verbatim):** *"a disciplined, internally coherent, structurally honest framework theorem paper with real geometric content and appropriately constrained claims... credible enough for: reviewer circulation, internal flagship positioning, serious technical discussion."* Verdict matrix YES for "reviewer-ready as flagship framework preprint."

**Strengths emphasized:** Scope discipline now much better; theorem stack architecturally clean; *"the anti-erasure discipline is excellent"*; abstract substantially stronger.

**Five remaining concerns:**

1. Umbrella theorem still weaker than supporting trio.
2. G1 still dominant vulnerability.
3. Thermodynamic-arrow language still occasionally overreaches.
4. Mechanism A remains physically underived.
5. Connection from DI-bit current to macroscopic arrow remains schematic.

**Four essential edits recommended:** (A) Replace any remaining "Scenario A closure" language; (B) Add explicit negative statement about what is NOT derived; (C) Add a dependency graph figure; (D) Separate "geometry theorem" from "physics interpretation."

**Integration outcomes at Patch 0569b (5 atomic edits):**

- Accepted: (A) Scenario A closure language extension to 3 anchors (abstract + §2.2 + §10); (B) §1 executive summary bold declarative ("This paper closes the F.1 sub-question at sketch-document Layer 3... The paper does NOT derive entropy production, coarse-graining, or macroscopic irreversibility"); (C) **Figure 8.1 TikZ dependency-graph in §8.2** (Layer hierarchy stack visualization).
- Partially accepted: (D) Mathematics-vs-interpretation separation — paper structure preserved (some interpretation appears in §1, §2, §10) per anti-erasure discipline; explicit separation deferred as long-term refactor consideration.

### Round 4: ChatGPT v0.9 v4 (Session 142, Patch 0569c archival) — *Positive (credible flagship framework theorem paper); recurring R3 recommendations*

**Source:** `chatgpt_v0.9v4_session_142.md`
**Verdict (verbatim):** *"v0.9 v4 is now a credible flagship framework theorem paper... genuinely stable in identity; credible flagship framework theorem paper."*

**Diagnostic-framing note added at Patch 0569c (per Capotauro v0.9_session_135_revised round-2 precedent):** Recommendations A + B + C + D recurring identically from R3 despite Patch 0569b having implemented all four. Candidate hypothesis: TikZ-rendering processing artifact (ChatGPT reading raw `.tex` source where `\begin{tikzpicture}...\end{tikzpicture}` code is unrendered text, so the Figure 8.1 dependency graph is invisible to the reviewer).

**Integration outcomes at Patch 0569c:** NO `.tex` content edits at this Patch. All 4 R4 recommendations already implemented at Patch 0569b. Patch 0569c is archival + diagnostic-framing only.

### Round 5: ChatGPT v0.9 v4 round 5 (Session 142, Patch 0569d archival) — *Positive (intellectually stable for long-term foundational programme); recurring-pattern documentation*

**Source:** `chatgpt_v0.9v4_session_142_round5.md`
**Verdict (verbatim):** *"first draft that reads like a disciplined mathematical framework paper rather than a speculative interpretive manifesto... intellectually stable enough to support a long-term foundational programme."*

**Recurring-pattern documentation at Patch 0569d:** Recommendations A + B + C + D recurring third time (R3 + R4 + R5). Two candidate hypotheses elevated: (a) TikZ-rendering processing artifact (carried forward from R4); (b) ChatGPT's verdict-stabilization trajectory plateauing without genuine new content engagement. R5 verdict is a verdict-improvement over R4 ("intellectually stable" stronger than "genuinely stable in identity"), supporting hypothesis (a) over hypothesis (b).

**Integration outcomes at Patch 0569d:** NO `.tex` content edits at this Patch. All 4 R5 recommendations already implemented at Patch 0569b. Patch 0569d is archival + recurring-pattern documentation + candidate-resolution-strategy framing for Round 6 (PDF upload protocol test).

### Round 6: ChatGPT v0.9 v5 round 6 (Session 142, Patch 0569e archival) — *Strongest-positive (substantially more credible, rigorous, and publishable than all earlier versions); diagnostic resolution confirmed*

**Source:** `chatgpt_v0.9v5_session_142_round6.md`
**Verdict (verbatim):** *"v5 is substantially more credible, rigorous, and publishable than all earlier versions... first version that feels: architecturally stable, epistemically disciplined, mathematically centered, structurally self-aware."* **The strongest-positive verdict in the F.1 paper's reviewer-engagement history.**

**Diagnostic resolution at Patch 0569e:** Round 6 was the first round where ChatGPT received the rendered PDF instead of `.tex` source. With the rendered PDF, ChatGPT now explicitly acknowledges all four previously-recurring recommendations (A, B, C, D) as implemented:

- **Rec A** implicitly accepted via "substrate-locality closure under a constrained framework" reframing in R6's Strongest Conceptual Success section.
- **Rec B** explicitly quoted verbatim: *"The present paper does not derive entropy production, coarse-graining, or macroscopic irreversibility..."* called *"absolutely necessary"*.
- **Rec C** explicitly praised: *"Figure 1 is especially important — the 'supported by, not derived from' dashed-arrow structure is exactly the right move"* (referring to the §8.2 Figure 8.1 dependency graph added at Patch 0569b).
- **Rec D** no longer flagged.

Candidate hypothesis (a) from Patch 0569c §61.3 — **TikZ-rendering processing artifact** — is **confirmed correct**. The recurring R3/R4/R5 recommendations were not substantive critique but the rendering artifact of `.tex`-source review where TikZ figures and bibliography environments did not visualize.

**Two genuinely new substantive suggestions (post-SHIP follow-up items):**

1. **Prose-density tightening** (registered as OPEN-FP-F1-6 at this Patch) — observation that cumulative scope-qualifier discipline has produced *"recursively self-referential"* framework-qualifier phrasings; *"the paper sometimes spends more words defending scope than advancing derivation."*
2. **Strategic suggestion: condensed "core theorem" version** focused on Theorem 6.1 (perturbation-locality) + Corollary 6.2 (shell-locality) + Theorem 7.1, with minimal CPP interpretation — *"a shorter geometry/locality paper could travel further academically"* than the manifesto-scale framing. Registered as F.1-condensed companion paper trajectory candidate (post-SHIP follow-up).

**Five remaining weaknesses cited at R6:** all five map exactly to the cross-reviewer Round 1 synthesis CAN-DEFER classification — G1 hardening + Theorem 7.1 hardening + Mechanism A derivation + prose density [new at R6] + thermodynamic emergence derivation [pre-existing OPEN-FP-F1-1 extension].

**Integration outcomes at Patch 0569e:** NO `.tex` content edits at this Patch. R6 verdict is SHIP-acceptable; reviewer-engagement cycle definitively closed. Two new follow-up items registered (OPEN-FP-F1-6 + F.1-condensed companion paper trajectory).

### Cross-reviewer convergence analysis (v0.9 → v1.0 SHIP cycle)

**Cumulative SHIP-state position:** Grok R1 EXPLICIT v1.0 SHIP-acceptable + Copilot R1 implicit SHIP-acceptable with tier-ranked recommendations + ChatGPT R6 strongest-positive verdict. All three reviewers converge on v1.0 SHIP-acceptable; ChatGPT's monotonic verdict-improvement trajectory (R1 → R6) supports the SHIP decision at maximum cross-reviewer-trajectory confidence.

**Diagnostic resolution as programme convention:** The Round 6 PDF-upload diagnostic resolution surfaces a programme-level reviewer-engagement convention candidate (`METH-PDF-UPLOAD-DEFAULT-REVIEWER`): going-forward protocol is to upload the freshly-compiled PDF (not `.tex` source) for ChatGPT reviewer engagement, especially for papers containing TikZ figures + bibliography environments + LaTeX content requiring compilation. Empirical motivation: Patch 0569e diagnostic resolution. Extends `relationship_protocol.md` reviewer-submission protocol with upload-format-aware guidance.

**Two new follow-up items registered at R6 (post-v1.0):**

1. **OPEN-FP-F1-6 prose-density tightening** — registered separately from the body §9 5-OP commitment (to preserve the v0.9 → v1.0 SHIP-cycle calibration-discipline rule "no Open Problems modified during reviewer cycle"). Patch candidate post-Phase-7.
2. **F.1-condensed companion paper trajectory** — geometric/locality-focused paper at Theorem 6.1 + Corollary 6.2 + Theorem 7.1 scope with minimal CPP interpretation. Registered as candidate follow-up Patch (long-term trajectory; depends on G1 hardening at OPEN-FP-F1-3 closure).

**Calibration discipline across the six-round cycle:** no theorem statements modified, no proofs modified (Patch 0569a Edit C added clarification AFTER existing Lemma 6.3.1 proof), no Open Problems modified during cycle, no `hardened_theorems/*.tex` source artifacts modified, no bibliography body modified. The 5-Open-Problem body §9 commitment preserved end-to-end across all six ChatGPT rounds. OPEN-FP-F1-6 registered separately at Patch 0569e from R6 follow-up (not as in-body §9 modification).

---

## Part 2 — FAQ

### Methodology

**Q: How does this paper relate to the rest of the CPP corpus?**
**A:** F.1 is the first paper in the F-line flagship series proper. It builds directly on Capotauro v2.0 (the precedent flagship trajectory, which closed OPEN-SD-CHIR-PRIMITIVE manifestations (i)–(iii) at the spatial-sector). F.1 closes manifestation (iv) of the same OPEN-SD-CHIR-PRIMITIVE umbrella at the temporal sector via substrate-locality of DI-bit currents. The two flagship papers share the structural constant $-1/(2\phi)$ as the first-shell host-to-first-shell projection. F.1 reuses the chirality continuum architecture and the Reading C foundational inputs (FI-C-RC-1 + FI-C-RC-2) established by Capotauro v2.0.

**Q: What is "anti-erasure discipline" and why is it named at §8.3?**
**A:** The anti-erasure discipline is a methodological framing element introduced at this paper that preserves three properties during paper polishing: (1) the Layer distinction (publication-grade L3 trio vs. sketch-document L3 umbrella); (2) the conditionality structure (Theorems 5.1 + 5.2 conditional on G1); (3) the explicit open higher-order questions (5 Open Problems in §9). The discipline emerged from ChatGPT R2–R6 reviewer pressure ("Do not erase the uncertainty structure during paper polishing. That would be a mistake."). Operationalised at three concrete points in §10: (a) §10 paragraph 1 restates the Layer status of Theorem 7.1; (b) §10 paragraph 3 explicitly disclaims thermodynamic emergence derivation; (c) §10 closing paragraph reaffirms 5-OP commitment as forward-trajectory anchor.

**Q: Why is Mechanism A taken as framework axiom rather than derived?**
**A:** Mechanism A (the propagation-rate asymmetry $r(\hat{e}) = r_0(1 + \delta\,\hat{e}\cdot\hat{n})$ plus the framework-local current construction at $\mathcal{O}(\delta^1)$) is the substrate-physics commitment from which substrate-locality is derived. Deriving Mechanism A itself from the eleven CPP primitive axioms A1–A11 is registered as OPEN-FP-F1-2 (Layer 4 axiomatic derivation, the long-term programme target). The framework-axiom strategy is methodologically standard for sketch-document Layer 3 papers: take the load-bearing physical mechanism as input at the chosen Layer, derive its consequences rigorously, and register the deeper derivation as future work.

### Scope

**Q: What is the paper's central result?**
**A:** Theorem 7.1 (substrate-locality of DI-bit currents at vertex-aligned Reading C): the net DI-bit current at any host vertex $\vhost$ at first order in the propagation-rate-asymmetry parameter $\delta$ is given in closed form by $\vec{j}_{DI}^{\text{net}}(\vhost) = (6\delta/\phi^2)\hat{n} + \mathcal{O}(\delta^2)$, depending only on first-shell content. The result is at sketch-document Layer 3 assembled from three publication-grade Layer 3 inputs (Theorems 5.1 + 5.2 + 6.1 + Corollary 6.2).

**Q: What does the paper NOT derive?**
**A:** Per §10 explicit disclaimer and the R6 strongest-positive verdict's central point: *"The present paper does not derive entropy production, coarse-graining, or macroscopic irreversibility; those derivations are future work beyond the present paper's framework qualifiers."* The substrate-locality structure supports a candidate thermodynamic-arrow mechanism (manifestation (iv) of the chirality continuum's substrate-direction primitive); the full emergence layer is registered as future work in §9 + §10.

**Q: Why is the umbrella theorem at sketch-document Layer 3 while its inputs are at publication-grade Layer 3?**
**A:** Theorem 7.1 assembles three publication-grade Layer 3 inputs (Theorems 5.1 + 5.2 + 6.1 + Corollary 6.2) but the assembly itself has not been independently hardened with explicit hypothesis tracking + five-class exclusion enumeration. The anti-erasure discipline preserves this Layer distinction transparently in the scope-framing subtitle and at §7.4 ("structural rather than editorial" hardening note). Independent hardening of Theorem 7.1 is a candidate follow-up Patch (registered at §7.4; not formal Open Problem to preserve 5-OP commitment).

### Falsifiability

**Q: What would falsify the substrate-locality theorem?**
**A:** Three falsifiability channels at the theorem level: (1) demonstrating that the host-to-first-shell projection $\hat{u}_i \cdot \hat{n}$ is NOT uniform at $-1/(2\phi)$ for some 600-cell first-shell vertex (would falsify Theorem 5.1); (2) demonstrating that some first-shell-to-first-shell edge has $\hat{e}_{ij} \cdot \hat{n} \neq 0$ (would falsify Theorem 5.2); (3) demonstrating a first-order-in-$\delta$ correction at any vertex beyond first-shell range (would falsify the perturbation-locality propagation rule Theorem 6.1 and Corollary 6.2). All three are testable by explicit calculation on the 600-cell using the regular polytope's vertex coordinates (Coxeter regular polytopes reference).

**Q: What would falsify Mechanism A as framework axiom?**
**A:** The framework-axiom strategy makes Mechanism A unfalsifiable at this paper's scope (it is input, not output). At Layer 4 (OPEN-FP-F1-2 closure), Mechanism A would become derivable from A1–A11 and therefore falsifiable by demonstration that no derivation can produce the propagation-rate asymmetry from primitive axioms. The Layer 4 derivability question is itself a research-direction question, not a derivation question.

### Relationship to Standard Model

**Q: How does this paper relate to the Standard Model?**
**A:** F.1 does not address Standard Model physics directly. The chirality continuum architecture (Capotauro v2.0 + F.1) does connect to electroweak physics via the substrate-direction primitive $\hat{n}$'s manifestations (i) parity violation, (ii) neutrino chirality structure, (iii) weak isospin assignment — but these are addressed in Capotauro v2.0 (the spatial sector) and SF-2 v2.0+ trajectory (the EFT continuum-limit closure), not in F.1. F.1's manifestation (iv) thermodynamic causal arrow is a foundational-physics question (arrow of time + irreversibility) traditionally not addressed within Standard Model phenomenology.

**Q: Does the result imply anything for cosmology or thermodynamics?**
**A:** The substrate-locality structure of Theorem 7.1 supports a candidate substrate mechanism for the thermodynamic causal arrow, but does NOT derive thermodynamic-arrow emergence in the conventional physics sense (entropy production, irreversible coarse-graining, statistical-mechanics emergence). Future work is the emergence-layer derivation. Sector-5 schema instantiation (OPEN-FP-F1-4) candidates include cosmological-arrow alignment.

### Future work

**Q: What is the recommended first post-v1.0 patch?**
**A:** G1 publication-grade hardening (OPEN-FP-F1-3) is the cross-reviewer-convergent "single highest-value next action" recommendation. ChatGPT R1–R6 + Copilot R1 Tier 1 #1 all converge on this priority. Closure produces `hardened_theorems/first_shell_inner_product_primitive.tex` parallel in structure to the three existing hardened artifacts (Patches 0550 + 0551 + 0552). Upgrades Theorems 5.1 + 5.2 from publication-grade Layer 3 conditional on G1 to publication-grade Layer 3 unconditional; consequently upgrades Theorem 7.1's conditionality clause. Estimated 1–2 sessions.

**Q: What are the long-term F.1 programme targets?**
**A:** Three programme targets: (1) Layer 4 axiomatic derivation of Mechanism A from A1–A11 (OPEN-FP-F1-2) — the deepest programme commitment; (2) Extension to $\mathcal{O}(\delta^2)$ and higher orders (OPEN-FP-F1-1) — closes the higher-order conditionality clause of Theorem 7.1; (3) Independent publication-grade hardening of Theorem 7.1 umbrella — closes the sketch-document Layer 3 vs publication-grade Layer 3 distinction at the umbrella level.

**Q: Is there a condensed version of the paper for academic submission?**
**A:** The F.1-condensed companion paper trajectory is registered at Patch 0569e from ChatGPT R6's strategic suggestion: a shorter geometry/locality paper focused on Theorem 6.1 (perturbation-locality) + Corollary 6.2 (shell-locality) + Theorem 7.1 with minimal CPP interpretation. The condensed version is registered as candidate follow-up Patch (long-term; depends on G1 hardening at OPEN-FP-F1-3 closure). R6 verbatim: *"a shorter geometry/locality paper could travel further academically"* than the manifesto-scale F.1 flagship framing.

---

## Summary

The v0.9 → v1.0 SHIP-cycle reviewer engagement at Session 142 (Patches 0568–0570) closed with cross-reviewer convergent SHIP-acceptable verdict: Grok R1 explicit + Copilot R1 implicit + ChatGPT R6 strongest-positive (*"substantially more credible, rigorous, and publishable than all earlier versions"*). Six-round ChatGPT trajectory showed monotonic verdict improvement from *"NOT yet publication-grade flagship overall"* at R1 to strongest-positive at R6; the trajectory was diagnostic-resolved at R6 via PDF-upload protocol (TikZ-rendering processing artifact resolved). Twelve reviewer items classified at synthesis (1 MUST-ADDRESS + 4 SHOULD-ADDRESS + 5 CAN-DEFER + 2 DECLINED); 5 integrated via Patch 0569 + 0569a + 0569b multi-edit responses; 5 deferred as Open Problems OPEN-FP-F1-1 through OPEN-FP-F1-6 (with OPEN-FP-F1-6 registered separately at Patch 0569e from R6 follow-up to preserve in-body 5-OP commitment); 2 declined with explicit rationale. Calibration discipline sustained across the entire six-round cycle: no theorem statements modified, no proofs modified, no Open Problems modified, no `hardened_theorems/*.tex` source artifacts modified, no bibliography body modified.

Three programme-level reviewer-engagement conventions surfaced at this cycle (candidates for Phase 7B methods catalogue audit): `METH-VARIANT-B-SCOPE-SUBTITLE` (the `\date{}` line scope-framing pattern adopted at Patch 0570 SHIP); `METH-PDF-UPLOAD-DEFAULT-REVIEWER` (the PDF-upload protocol for ChatGPT engagement validated by R6 diagnostic resolution); `METH-GITIGNORE-FLAGSHIP-PDF-EXCEPTION` (the `.gitignore` exception pattern for flagship paper SHIP PDFs added at Patch 0570 apply-fix). All three conventions extend `relationship_protocol.md` reviewer-engagement and SHIP-closeout protocol with concrete F-line flagship-trajectory-tested practice.

---

*Reviews file created Session 143 Patch 0572b (24 May 2026) as the third SHIP-time companion documentation file in Phase 7A. Per `templates/documentation-suite.md` §6 + checklist §A A6 (consolidated reviews + FAQ format; FAQ legacy-allowed but not required for papers adopted ≥ 22 April 2026, so consolidated here per checklist). Reference implementation: `flagship_papers/capotauro/documentation_suite/reviews-capotauro.md`. This file is a historical record of the v0.9 → v1.0 SHIP-cycle reviewer engagement; future paper-version increments trigger additional Part 1 round sections appended below the existing v0.9 → v1.0 SHIP-cycle content; Part 2 FAQ is updated continuously as new questions come in from any source.*
