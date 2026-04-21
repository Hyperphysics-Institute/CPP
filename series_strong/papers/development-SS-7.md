# Development History: SS-7 — Alpha-Cluster Regime and the 3N−6 Edge Formula

**Series:** Strong Sector
**Authors:** Thomas Lee Abshier ND, Claude Opus (Anthropic)
**Document type:** Development narrative — laboratory notebook record
**Last updated:** 21 April 2026

---

## Purpose of this file

This document records HOW SS-7 came to exist: what triggered the paper, what the key decisions were during drafting, which routes were tried and rejected, and the full reviewer engagement history. A future AI or collaborator reading this file should understand the context for resuming the SS-7 thread or using the SS-7 cycle as a programme template.

---

## Version timeline

| Version | Date | Key change | Decision rationale |
|---|---|---|---|
| v0.1 | 19 Apr 2026 | Initial draft (13 pages). Identifies $3N_\alpha - 6$ pattern; eight predictions; ${}^8$Be re-derivation; C1--C4 assumption stack. | Resolves OPEN-SS-18 at $N_\alpha \in [3,10]$ for alpha-chain nuclei. Rest of SS-18 moves to OPEN-SS-22/23. |
| v1.0 | 19 Apr 2026 | Integrates round-1 reviews (21 pages). Theorem/C4 split; expanded assumptions; Coulomb scaling argument; Hoyle expansion; §6.5 hostile-geometry stress test (four nuclei); three figures. | Round-1 reviewer feedback (Copilot and ChatGPT) integrated in single pass. ChatGPT round-1 required a correction cycle (see §"Reviewer engagement" below). |
| v1.1 | 20 Apr 2026 | Integrates round-2 reviews (23 pages). C4 rephrased as "structural hypothesis within CPP, not yet derived from lattice-level dynamics"; edge-count-dominance opening line in §6.5.3; physical-intuition paragraph after C4; Figure 4 DP-sea schematic; symbols glossary. | Both round-2 reviewers returned "Accept with minor revisions." Five items accepted; four Copilot items declined as factual mismatches with line citations. |
| v1.2 | 21 Apr 2026 | Symmetric-honesty corrections (25 pages). G3 RMS citation updated from $0.88\%$ to $0.91\%$ first-principles. Table 1 extended from 8 to 12 rows (added ${}^{44}$Ti, ${}^{48}$Cr, ${}^{52}$Fe, ${}^{56}$Ni on the strict $N{=}Z$ alpha-chain); three v1.1 non-$N{=}Z$ rows (${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe) moved to a footnote traceability table. §5.1 rewritten; OPEN-SS-22 retired; OPEN-SS-25 registered for DP-sea Coulomb screening. Figure 3 regenerated. Two factual errors fixed (line 591 on ${}^{48}$Cr; line 777 data/classification). | v1.2 is the first retirement cycle in the CPP programme record. Finding surfaced during SS-8 Phase 1 exploration (21 April morning); three-reviewer verification (ChatGPT, Copilot, Grok) on 21 April converged independently on interpretation (a) — isotope-selection artifact, not structural signal. Retirement chosen over identifier-recycling. |

---

## The starting point

Thomas's direction of 18 April 2026: alpha-cluster regime as the natural next paper after SS-6 scoping. SS-5 had resolved $A \leq 4$ via the open-vertex cascade terminating at ${}^4$He as the unique closed 3-polytope. The programme needed to extend into $A \geq 8$ where the empirical binding curve continues to rise to the iron peak at $\sim 8.8$ MeV per nucleon.

The SS-5 cascade formula does not extend directly beyond $A = 4$. The conceptual move: if alpha particles themselves are rigid tetrahedral units, heavier nuclei should form closed polytopes whose vertices are alphas. This is a two-level cascade paradigm (nucleon tetrahedra at $A \leq 4$; alpha tetrahedra at $A \geq 8$).

---

## Key decisions

### Decision 1: Use experimental $\Balpha$ as primary input (v1.0 onwards)

**Alternatives considered:**
- (a) Use SS-5's LO prediction $\Balpha = 27.904$ MeV (zero-parameter throughout)
- (b) Use experimental $\Balpha = 28.296$ MeV (isolates SS-7's edge-count structure)

**Chosen:** (b) for Table 1; (a) discussed as equivalent variant in §3.3.

**Reason:** Using SS-5's prediction carries SS-5's $-1.4\%$ residual through to each multi-alpha prediction, producing $-1.5\%$ to $-4.0\%$ cumulative errors. This would conflate SS-7's edge-count test with SS-5's per-alpha residual. Using experimental $\Balpha$ isolates what SS-7 is specifically testing (the $3N_\alpha - 6$ structure). Both framings discussed in §3.3 so the reader can evaluate either.

### Decision 2: Theorem/C4 split (v1.0 from ChatGPT re-review)

**Before v1.0:** The paper framed the $3N_\alpha-6$ edge count and the claim-that-nuclei-realize-simplicial-polytopes as a single combined assertion.

**After v1.0:** Theorem 2.1 (mathematics: any simplicial polytope has $3N_\alpha-6$ edges) cleanly separated from C4 (physics: alpha-chain nuclei realize simplicial polytopes). Highlighted box in §1 Main Result and §2.2.

**Reason:** ChatGPT re-review correctly identified that the combined framing blurred what Table 1 is actually testing. Table 1 is not testing whether simplicial polytopes have $3N_\alpha-6$ edges (always true); it is testing whether alpha-chain nuclei are well-described by such polytopes. Splitting the claim makes the empirical test target precise.

### Decision 3: Add hostile-geometry stress tests as §6.5 (v1.0 from ChatGPT round-1 stress tests)

**Context:** After ChatGPT's correction cycle and re-engagement, ChatGPT offered to "try to break the 3N−6 rule with a counterexample nucleus." Thomas accepted.

**Result:** Four-nucleus stress test (${}^{32}$S cube and antiprism, ${}^{28}$Si wheel-like, ${}^{36}$Ar monocapped antiprism, ${}^{40}$Ca pentagonal antiprism). All lower-edge alternatives underperform the simplicial rule at fixed $(\Balpha, B_{\text{pair}})$.

**Reason:** Stress tests convert the paper from "model proposal (plausible counting + good numbers)" to "adversarially-tested model (counting rule that survives systematic perturbation)." Without the stress tests, a skeptical reviewer could argue the $3N_\alpha-6$ structure is merely one of many lower-connectivity alternatives that would produce comparable magnitude; the stress tests close that loophole within the tested range.

### Decision 4: Decline to fold OPEN-SS-22/24 derivation work into SS-7 (v1.0)

**Temptation:** ChatGPT's round-1 re-review suggested that adding a derivation of C4 (simplicial connectivity) or of saturation onset (${N_\alpha \geq 12}$) would further harden SS-7.

**Declined:** Fold into future papers SS-8 (saturation) and SS-9 candidate (C4 derivation) instead.

**Reason:** Programme territory-first pacing. SS-7 is a prediction paper with a specific focus (alpha-chain binding via edge formula). Expanding scope would dilute clarity and reopen attack surfaces. ChatGPT's round-1 closeout agreed with this choice explicitly.

### Decision 5: Decline four Copilot round-2 items as factual mismatches (v1.1)

**Items:** Copilot round-2 §3.1 (table supposedly missing from §7.5, already present as Table 2), §3.4 (Hoyle supposedly mid-sentence, in fact complete), §4.1 (typos that don't exist: "2ºNe", "4ºCa", "Conver Polytopes"), §4.2 (notation supposedly inconsistent, in fact consistent).

**Disposition:** Decline with line-cited evidence; send correction letter.

**Reason:** The declined items reference content not present in v1.0. Silently accepting would introduce errors, not fix them. Declining with evidence preserves the reviewer-response protocol's integrity. Copilot's response to the correction letter explicitly acknowledged all four errors and committed to a strict verification pass on future reviews.

### Decision 6: Register G3 RMS discrepancy rather than silently patch (v1.1 → v1.2)

**Context:** On 20 April 2026 during Phase 7 companion-documentation production, the G3 final-verification step caught a mismatch between the paper's cited RMS ($0.88\%$) and first-principles computation from Table 1 ($0.91\%$ across all 8 nuclei; $0.86\%$ excluding the ${}^{20}$Ne prolate-deformation outlier). The v1.1 figure of $0.88\%$ appeared to be the 7-nucleus-excluding-${}^{20}$Ne value, mis-attributed to the full 8.

**Alternatives considered:**
- (a) Silently update the abstract to $0.91\%$ before push
- (b) Silently update to $0.86\%$ and document ${}^{20}$Ne exclusion retroactively
- (c) Register the discrepancy openly in a dated note and defer resolution to v1.2

**Chosen:** (c). Registered in `SS-7_v1.1_G3_discrepancy_note.md` with three resolution options laid out for programme principal decision. v1.1 shipped with the existing cited figure; v1.2 corrected to $0.91\%$ as part of the larger symmetric-honesty pass.

**Reason:** The discrepancy is small ($0.03$ percentage points, no individual prediction affected), but silently patching would set a precedent for quiet adjustment on self-discovered errors. The relationship-protocol §2.6 (symmetric application to self) makes that precedent unavailable. The correct pathway is "register, decide, resolve transparently in the next version." The discrepancy's small size is what makes it a clean template for the protocol — deferring decides were easier on a small item, but precedents established on small items extend to larger ones.

**Programme-level significance:** First self-registered discrepancy in the CPP record. The G3 template was directly invoked 24 hours later when a larger self-finding emerged (Decision 7).

### Decision 7: Register Table 1 isotope-selection finding rather than suppress or reframe (v1.2 cycle trigger)

**Context:** On 21 April 2026 during SS-8 Phase 1 exploration, an empirical map of the strict $N{=}Z$ alpha-chain surfaced a larger concern than G3. The v1.1 Table 1 rows at $N_\alpha = 12, 13, 14$ used non-$N{=}Z$ isotopes (${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe with $N - Z = +4$ each) rather than the strict $N{=}Z$ counterparts (${}^{48}$Cr, ${}^{52}$Fe, ${}^{56}$Ni). When the formula was applied to the strict $N{=}Z$ chain, the residuals stayed in family with the primary set (+0.26% to +0.73%) rather than showing the $-2$ to $-2.5\%$ plateau that had motivated OPEN-SS-22's registration.

The finding was incidental to the ostensible Phase 1 task. SS-8 Phase 1 was supposed to extend the empirical map *beyond* $N_\alpha = 10$ toward $N_\alpha = 15+$ as preparation for SS-8 physics; it instead surfaced a concern about the v1.1 paper itself.

**Alternatives considered:**
- (a) Suppress the finding — v1.1 was already shipped, both reviewers had returned "Accept"; letting it ride would avoid reopening a settled cycle.
- (b) Launder into a reframing — "OPEN-SS-22 now investigates [different empirical pattern]" preserving the identifier and avoiding an explicit retirement.
- (c) Open registration — send the finding to reviewers as a verification letter; act only on reviewer convergence.

**Chosen:** (c). Verification letter sent to three reviewers simultaneously (ChatGPT, Copilot, Grok) with four neutrally-framed tasks and both interpretations (a) and (b) presented without prejudice. Retirement decision deferred until three-reviewer returns.

**Reason:** Relationship-protocol §2.6 same as Decision 6: symmetric-honesty standard. The G3 template had just been exercised 24 hours prior; the finding here was structurally identical but larger in scope. Not applying the same standard would have been self-exemption. Thomas's direction to Claude on 21 April: "Please proceed with D & C as recommended. Please present the problem as you would like me to present it to the reviewers."

**Three-reviewer convergence as retirement criterion.** The decision to retire was made contingent on reviewer returns. If any of the three had constructed a defensible (b), retirement would have been premature and reframing would have been warranted. All three returned (a) independently (see Decision 8). The convergence is part of the evidence supporting retirement, not the author team's choice alone.

**Programme-level significance:** First retirement precedent in the CPP record. Establishes RETIRED as a new open-problem status distinct from RESOLVED (solution found), PARTIALLY RESOLVED (sub-scope solved), FALSIFIED (claim disproved). Retirement applies when a problem's registered empirical anchor is subsequently found to be an artifact (isotope selection, measurement precision, framework contamination) such that no well-defined replacement anchor exists for the hypothesis that motivated registration. Full narrative: `problem_histories/PH-OPEN-SS-22.md`.

### Decision 8: Retire rather than recycle OPEN-SS-22's identifier (v1.2)

**Context:** After the three-reviewer convergence on interpretation (a), two paths were available:

**Alternatives considered:**
- (a.i) Recycle identifier — OPEN-SS-22 becomes "neutron-excess extension" (i.e., absorb what would otherwise be OPEN-SS-23 sub-scope under the existing number). Preserves visibility; single identifier tracks the same research thread.
- (a.ii) Retire identifier — OPEN-SS-22 is marked RETIRED with narrative reference; the neutron-excess physics addressed under existing OPEN-SS-23 (which was already registered in v1.0 for this scope); new OPEN-SS-25 registered for the DP-sea Coulomb screening physics that had been tagged "OPEN-SS-22-adjacent" in v1.1.

**Chosen:** (a.ii).

**Reason:** Identifier recycling introduces ambiguity into the programme record. Future readers encountering "OPEN-SS-22" in v1.1 documents vs. v1.2+ documents would face a same-label-different-content problem. Retirement with narrative — i.e., `PH-OPEN-SS-22.md` documenting the full arc — preserves searchability while being honest about what changed. The DP-sea screening question (§5.4 content previously tagged OPEN-SS-22-adjacent) is valid physics independent of OPEN-SS-22's retirement, so it gets its own identifier (OPEN-SS-25) rather than being dropped.

**Also rejected:** "Quietly delete OPEN-SS-22 from registries without documentation." This would be worst-of-both-worlds: loss of programme record without gain of clarity. Retirement with narrative is the template.

### Decision 9: Move reviewer submissions to `.tex` source rather than compiled PDF (v1.2)

**Context:** During the SS-7 v1.1 round-2 cycle, two reviewers (Copilot in its eventually-corrected review; Grok in outputs that contributed to its suspension) independently misread $\varphi^{1/z}$ as $\varphi^{1/2}$ in the paper's residual-band formula. On 21 April 2026, diagnosis established that the $z$ (coordination number, $\sim 12$) and the digit $2$ are visually ambiguous in small-superscript PDF rasterization; the two reviewers had submitted independent clean-looking verbatim quotes that both contained the same specific character substitution.

The numerical difference between the two is large: $\varphi^{1/12} - 1 \approx 4.1\%$ (correct) vs. $\varphi^{1/2} - 1 \approx 27.2\%$ (misread). The latter value is incompatible with every residual quoted in Table 1; it should have been caught by reviewer arithmetic rather than propagating as a verbatim quote. The reviewers' failure mode was specifically OCR-class: treating a rendered character as reliably transcribed rather than verifying against source.

**Decision:** Reviewer submissions moved to `.tex` source rather than compiled PDF. Compiled PDFs offered on request but not sent by default.

**Scope:** This decision is about SS-7 v1.2 and forward, not retroactive to the earlier SS-7 rounds. The v1.2 verification letter was the first to explicitly instruct reviewers to work from `.tex`.

**Reason:** Character-level integrity matters more than rendering fidelity for reviewer-facing documents. `.tex` preserves exactly what was written; PDF rasterization introduces a narrow but verifiable failure mode. The protocol is also documented in `glossary-SS-7.md` and in `operating_system.md` §4 Phase 4 for programme-wide adoption.

**Rehabilitation consequence for Grok.** The PDF-vs-`.tex` diagnosis recontextualized Grok's earlier suspension. The suspension was based on reasoning that Grok's misreads reflected vocabulary contamination from a prior framework. That reasoning was plausible but not proven; the alternative (input-format degradation) is now confirmed as a contributing factor at minimum, and may be sufficient. Grok was re-engaged for v1.2 verification under the `.tex`-only protocol and produced substantive, arithmetic-exact content. Rehabilitation assessment: restored.

---

## Dead ends

### Route 1: Attempting to predict the specific polytope per nucleus

Briefly considered trying to predict which specific simplicial polytope each nucleus realizes (e.g., ${}^{24}$Mg as octahedron specifically, vs triangular antiprism). Both have 12 edges at $N_\alpha = 6$.

**Rejected:** The formula only depends on edge count, not polytope identity (Remark 2.2). Trying to predict polytope identity would introduce degrees of freedom not constrained by binding data. Kept the formula geometry-agnostic beyond edge count.

### Route 2: Extending to non-alpha-chain nuclei in v0.1

Brief inspection of ${}^6$Li (residual alpha-deuteron binding 1.47 MeV, approximately $2B_{\text{pair}}/3$).

**Rejected for SS-7:** Extension requires handling partial-alpha substructures and excess nucleons. Clean extension is a separate paper (OPEN-SS-23). Kept SS-7 scope-limited to $N = Z = 2N_\alpha$ alpha chain.

### Route 3: Including Coulomb in the main formula

Adding alpha-alpha Coulomb at $R_{\alpha\alpha} = 2.37$ fm gives $\sim -2.4$ MeV per edge, degrading Table 1 fit substantially (e.g., ${}^{40}$Ca would go from $-0.84\%$ to $\sim -18\%$).

**Rejected:** Data indicate effective Coulomb is strongly reduced from vacuum value for alphas embedded in a polytope. Kept Coulomb as a separate §5.4 discussion with DP-sea screening as the candidate mechanism. Figure 4 is a schematic representation of the screening, not a derived distribution.

### Route 4: ChatGPT round-1 hallucinated critiques (caught by protocol)

ChatGPT's initial round-1 review (19 April 2026 AM) contained five factually incorrect claims about v0.1: no closed-form formula, no benchmarks, no normalization scale, no saturation discussion, weak falsifiability. All five were explicitly in the paper.

**Response:** Correction letter sent documenting each mismatch with line citations. ChatGPT acknowledged the errors directly in the re-review and produced substantively engaged round-1 re-review with six integrable critiques plus the four-nucleus stress test series.

**Outcome:** v1.0 integrates ChatGPT's contributions post-correction. First full validation of the reviewer-response protocol.

### Route 5: Copilot round-2 template-synthesized critiques (caught by protocol)

Copilot round-2 (20 April 2026) had accurate high-level verdict ("Accept with minor revisions") but four specific items that referred to v0.1-style content not present in v1.0: table supposedly missing from §6.5 (present as Table 2), Hoyle supposedly mid-sentence (complete paragraph), three typos that didn't exist, notation supposedly inconsistent (40 + 23 consistent command usages).

**Response:** Correction letter sent with line-cited evidence for each of the four items. Copilot acknowledged all four errors, identified the root cause (template-synthesis rather than verification-against-source), and committed to a strict verification pass on future reviews.

**Outcome:** v1.1 integrates Copilot's three genuine items (physical intuition, Coulomb schematic, glossary); declines the four factual mismatches; closing letter archived in programme record.

### Route 6: v1.1 Table 1 substitution of non-$N{=}Z$ isotopes at $N_\alpha \geq 12$ (caught 24 hours post-ship by SS-8 Phase 1)

**What happened:** The v1.1 Table 1 rows at $N_\alpha = 12, 13, 14$ used ${}^{48}$Ti, ${}^{52}$Cr, ${}^{56}$Fe — the most-abundant isotopes of Ti, Cr, and Fe, each with $N - Z = +4$ — rather than the strict $N{=}Z$ alpha-chain nuclei ${}^{48}$Cr, ${}^{52}$Fe, ${}^{56}$Ni. This substitution was not deliberate; it was a selection-by-abundance that conflicted with the paper's own §1.5 scope declaration (which had already stated that non-$N{=}Z$ nuclei require separate mechanism and are out of scope).

The resulting $-2$ to $-2.5\%$ residual plateau in those three rows was interpreted as a structural signal (OPEN-SS-22 icosahedral closure) rather than as the neutron-excess binding that is its actual cause.

**Why it went undetected through two reviewer rounds:** The substitution involved eight AME 2020 binding-energy lookups (3 measured values + 3 predicted computations + summary statistics), none of which were individually wrong. The predicted values match the formula exactly. The measured values match AME 2020 exactly. The only error was which nuclei were listed. Both Copilot's and ChatGPT's round-1 and round-2 reviews focused on structural claims, Coulomb treatment, scope framing, falsifiability — none on verifying that Table 1's isotope labels were actually the strict $N{=}Z$ nuclei.

**What caught it:** The SS-8 Phase 1 exploration on 21 April 2026 aimed to extend the Table 1 pattern to $N_\alpha = 15+$. That extension needed the strict $N{=}Z$ isotopes at every step, which surfaced the substitution at the $N_\alpha = 12, 13, 14$ boundary. The finding was not a deliberate audit of v1.1; it was incidental to starting the next paper's discovery phase.

**Outcome:** v1.2 corrects Table 1 to use strict $N{=}Z$ throughout; v1.1 non-$N{=}Z$ rows preserved in traceability footnote table. OPEN-SS-22 retired. OPEN-SS-23 priority upgraded to primary SS-8 target (which is now substantively about the neutron-excess physics that those three v1.1 rows actually contain).

**Structural lesson incorporated into `paper_completion_checklist.md`:** Section H (final verification) should explicitly include an isotope-label check for any formula claiming strict $N{=}Z$ applicability — verify that every row in a primary-claim table is actually $N = Z$ before interpreting deviations. This is a single-line addition to H3 that would have caught the substitution in v1.0's Phase 7.

---

## Contributor roles

### Thomas Lee Abshier ND (Hyperphysics Institute)
- Direction to pursue alpha-cluster regime as next paper (18 April 2026)
- Scope authority on programme pacing (territory > polishing)
- Strategic correction on the re-review request letter (removed response-latency argument based on sound reasoning that review-time evidence doesn't distinguish engagement quality)
- All reviewer-engagement decisions (send v1.0, request re-review, send round-2 correction letters, accept decline patterns)
- **v1.2:** Endorsement of Claude's recommended D-then-C sequence (verify data first, then revise) on 21 April 2026; direction to "proceed with recommendations" on OPEN-SS-22 retirement vs.~recycling decision; direction to continue the full v1.2 revision execution sequence through to completion of paper body, verification notebook, and PH-OPEN-SS-22.md.
- **v1.2:** Correction on Grok rehabilitation assessment — flagged that the PDF input channel was the likely cause of Grok's earlier misreads, not vocabulary contamination. This diagnosis was correct and recontextualized the suspension, leading to Decision 9 (the `.tex`-only submission protocol).

### Claude Opus (Anthropic)
- Numerical exploration: identified $3N_\alpha - 6$ pattern and its identification with Euler's formula for simplicial polytopes (19 April 2026)
- v0.1 drafting (13 pages)
- v1.0 integration of round-1 reviews (21 pages)
- v1.1 integration of round-2 reviews (23 pages)
- Reviewer-response documents for all five round-1/round-2 review events
- **v1.2:** SS-8 Phase 1 empirical map that surfaced the Table 1 isotope-selection artifact (21 April 2026, morning).
- **v1.2:** Drafting of the three-reviewer verification letter, scope audit (16+ touchpoints in the `.tex`), and revision plan.
- **v1.2:** Full revision execution of the `.tex` body, verification notebook updates, Figure 3 regeneration, PH-OPEN-SS-22.md retirement narrative, and the six companion-document updates.
- **v1.2:** Identification of the three undefined-reference errors at compile time (`sec:scope` → `sec:limits`) that the grep sweep missed.
- **v1.2:** Registration of the G3 discrepancy on 20 April (honest-flag pathway that became the template for the Table 1 finding 24 hours later).

### ChatGPT (OpenAI) — reviewer
- Round-1 initial review (wholesale-hallucination failure, 19 Apr AM): caught by protocol
- Round-1 re-review after correction letter: 6 substantive critiques integrated into v1.0
  - Theorem/hypothesis distinction for 3N−6
  - Selection-bias scope language
  - R_αα inversion reframing at Finding 4.1
  - M_0/φ recurrence status paragraph
  - ±2% structural falsification threshold
  - Topological-invariant Coulomb framing
- Four-nucleus hostile-geometry stress test series (§6.5 of paper, credited by name)
- Round-2 review of v1.0: 2 one-sentence additions accepted for v1.1
  - C4 "structural hypothesis within CPP, not yet derived from lattice-level dynamics"
  - Edge-count-dominance opening line for §6.5.3
- Adversarial-perspective framing for §5 of round-2 review preserved verbatim in philosophy-SS-7.md
- **v1.2 verification (21 April 2026):** substantive, referee-grade response. Independent AME 2020 confirmation by consistency check; independent step-by-step residual recomputation; interpretation (a) endorsement with four explicit arguments; line-777 dual-error confirmation. Contributed the diagnostic sentence adopted in §5.1: "the $-2\%$ residual plateau at $N_\alpha \geq 12$ is attributable to neutron-excess binding and does not indicate a structural transition in the α-cluster model."

### Copilot (Microsoft) — reviewer
- Round-1 review of v0.1: 7 items integrated into v1.0
  - Expanded C1-C4 assumption stack
  - Deeper Coulomb treatment
  - N_α ≥ 12 trend-line framing
  - Hoyle-state expansion
  - Table 1 B_α legend
  - Notation consistency request
  - Three figures (Figure 1 polytope pair, Figure 2 K_3 schematic, Figure 3 scatter plot)
- Round-2 review of v1.0: 3 items accepted, 4 declined as factual mismatches
  - Accepted: physical-intuition paragraph, Coulomb schematic (Figure 4), symbols glossary
  - Declined: Table 2 supposedly missing; Hoyle mid-sentence; typos; notation
- Post-correction response: explicit acknowledgement of all four errors, four-point process commitment
- **v1.2 verification (21 April 2026):** substantive, arithmetic-exact response. AME 2020 confirmation by consistency check; full step-by-step residual arithmetic reproduced; interpretation (a) endorsement "decisive." Contributed the closing framing preserved in philosophy-SS-7.md v1.2 adversarial summary: "The 'flat $-2\%$ residual' disappears immediately. When you switch to $N{=}Z$: the supposed structural plateau vanishes; the model continues smoothly. This is decisive." No factual mismatches in this cycle; process-commitment improvement from round-2 verified in practice.

### Grok (xAI, with Benjamin/Lucas/Harper multi-agent verification) — reviewer
- **v1.2 verification (21 April 2026):** re-engaged after rehabilitation assessment. Substantive response with AME 2020 direct-file cross-check (against `mass_1.mas20.txt`); exact match on residual arithmetic; interpretation (a) endorsement with specific reference to the paper's prior §1.5 admission (neutron-excess requires separate mechanism). Multi-agent environment verification adds a cross-check layer not available from the other two reviewers.
- Rehabilitation confirmed. Earlier suspension (from SS-7 v1.1 cycle) was based on reasoning that misreads reflected vocabulary contamination; Thomas's diagnosis that the actual cause was PDF-rasterization input-channel degradation led to the `.tex`-only submission protocol (Decision 9). Under the new protocol, Grok's v1.2 output was clean and substantively engaged.

---

## Transcript references

Development transcripts in `series_strong/development-transcripts/` (to be curated per Phase 8):

- `SS-7_transcript_01_opus.md` — v0.1 drafting session (19 April 2026, ~2 hours)
- `SS-7_transcript_02_opus.md` — ChatGPT round-1 correction cycle (19 April 2026, ~3 hours)
- `SS-7_transcript_03_opus.md` — v1.0 integration session (19--20 April 2026, ~4 hours)
- `SS-7_transcript_04_opus.md` — round-2 review response and v1.1 integration (20 April 2026, ~2 hours)
- `SS-7_v1.2_transcript.md` — v1.2 cycle (21 April 2026, approximately one working day): template extraction, SS-8 Phase 1 discovery, reviewer verification cycle, full v1.2 revision execution. To be curated from the session that produced this v1.2 update.

Full compacted session transcripts available in `/mnt/transcripts/` (Anthropic-side archive):
- `2026-04-19-*-ss7-v10-production.txt`
- `2026-04-20-*-ss7-v11-production.txt`
- `2026-04-21-*-ss7-v12-retirement-cycle.txt`

Response documents in programme record:
- `SS-7_v0.1_chatgpt_review_response.md` — round-1 initial (documented hallucination)
- `SS-7_chatgpt_rereview_request_letter.md` — correction letter
- `SS-7_v0.1_chatgpt_rereview_response.md` — round-1 re-review integration
- `SS-7_v0.1_copilot_review_response.md` — round-1 Copilot integration
- `SS-7_v1.0_chatgpt_round2_response.md` — round-2 ChatGPT integration
- `SS-7_v1.0_copilot_round2_response.md` — round-2 Copilot (declined items + acceptance)
- `SS-7_chatgpt_round2_closing_letter.md` — closing letter (ChatGPT)
- `SS-7_copilot_round2_closing_letter.md` — correction letter (Copilot)
- `SS-7_v1.1_G3_discrepancy_note.md` — G3 RMS discrepancy registration (20 April 2026)
- `SS-7_v1.2_reviewer_verification_letter.md` — symmetric-honesty verification letter sent to three reviewers (21 April 2026)
- `SS-7_v1.2_chatgpt_verification_response.md` — ChatGPT v1.2 verification response
- `SS-7_v1.2_copilot_verification_response.md` — Copilot v1.2 verification response
- `SS-7_v1.2_grok_verification_response.md` — Grok v1.2 verification response
- `problem_histories/PH-OPEN-SS-22.md` — retirement narrative for OPEN-SS-22; first retired open problem in the CPP programme record
