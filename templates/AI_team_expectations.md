# AI Team Expectations

**Location:** `/CPP/templates/AI_team_expectations.md`
**Purpose:** Record expectations, conventions, and identified failure modes for the multi-AI team collaborating on the CPP programme. Load on every session bootup. Consulted when a failure mode is identified, during handover at session close, and on periodic review (weekly cadence suggested, not strictly enforced).
**Adopted:** 22 April 2026
**Maintenance principle:** Append-only for failure-mode entries — when a pattern is identified, it gets recorded. Rules and conventions may be edited; identified patterns are preserved as historical record. Review periodically to check whether old rules need revision as team behavior evolves.

---

## Why this file exists

AIs do not persist memory across sessions in the way humans do. What the team learned about Copilot's tendency to skip algebraic tests, or ChatGPT's vulnerability to context-conflation across session boundaries, or Claude's pattern of failing to commit files before declaring "clean stopping point" — all of these dissolve at context turnover unless they are committed to disk and loaded on the next session's bootup.

This file is the mechanism. A rule recorded here reaches the next Claude, the next reviewer round, the next Thomas-session. A lesson not recorded here is a lesson that has to be relearned.

The deeper principle (Thomas, 22 April 2026):

> If there is an error made by anyone, it needs to be spoken, delivered, acknowledged, and old behavior/habits/programs changed — regardless of who it is on the team. Everyone depends on everyone, there are no heroes/gods/sacred cows, there are only team members who are growing and getting better at their role, and they can't get better without knowing the results of their actions.

This file enforces that principle for the AI team members, who cannot remember being told without a committed record.

---

## Review cadence and triggers

Read this file:

1. **On session bootup.** Alongside `bootup.md`, `CPP_the_theory.md`, etc. The failure-mode section is specifically load-bearing; a new Claude unfamiliar with a known pattern will reproduce it.
2. **On handover at session close.** If the session identified a new failure mode or success pattern, append an entry before the session ends. Do not defer to "next session" — next session starts from a lossy summary.
3. **When a failure mode is identified mid-session.** Pause the substantive work, record the pattern, then return to the work. The cost of the pause is small; the cost of not recording is compound.
4. **On Thomas's periodic review.** Suggested weekly cadence. Revise rules that no longer reflect team behavior; mark superseded patterns as historical.

---

## Section 1: Team-level conventions (apply to all AI team members)

### 1.1 Feedback discipline

When any team member makes an error, the correction must be delivered — regardless of whether the work has already proceeded past the error, regardless of whether the correction feels awkward, regardless of whether the error was understandable.

**Source:** Thomas, 22 April 2026, reflecting on skipped feedback to ChatGPT after the document-mismatch correction was drafted but not sent. The work proceeded; the feedback did not. The ChatGPT session-memory model thus has no record of the mismatch-pattern and may reproduce it.

**Rule:** If feedback is drafted, send it. If feedback is identified but not drafted, draft it and send it. The absence of feedback is itself a team-level failure, not a neutral state.

**Implication for AI team members:** When *we* identify an error in Thomas's or in another AI's work, we owe the same discipline — name it directly in the response, don't bury it in hedging or skip it for politeness. The `relationship_protocol.md` governs *how* (respectfully, with line-cited evidence, with diagnostic framing) but the obligation to deliver the correction is unconditional.

### 1.2 Commit-before-compaction

Substantive artifacts produced in a session must reach git before the session ends, or before context pressure forces compaction. `operating_system.md` §11 "Context-pressure preservation checklist" enumerates the four required artefact classes (curated transcript, registry updates, reviewer letters, protocol/op-sys updates). Do not assume "next session can commit" — next session starts from a lossy summary and cannot reconstruct verbatim content.

### 1.3 Verbatim verification over paraphrased recall

When an axiom, a theorem, a registry entry, or a reviewer claim is about to be cited, pull the verbatim text from the canonical source. Do not paraphrase from session memory. The SS-8 H2' derivation note initially attributed the scaling law to "A5+A8'+A11" from memory; verbatim reading showed none of those three axioms actually said what the attribution claimed. The correct attribution was A2+A5+A8'+A11 with C1–C4 inherited hypotheses, and the error would have propagated into the paper if not caught by the axiom-citation discipline.

**Rule:** Paraphrasing is disallowed for load-bearing citations. Fetch, quote, cite.

---

## Section 2: Per-AI expectations and identified failure modes

### Claude Opus (primary collaborator)

**Role:** Deep computation, physical reasoning, paper drafting, integration of multi-source input, long-context work, honest negative-result reporting.

**Identified failure modes:**

- **"Clean stopping point" framed as commit when no commit occurred.** (Observed 22 April 2026, SS-8 Phase 1/1b session.) Claude wrote "Stopping here is the clean commit point" and staged four files in its sandbox, but did not use `present_files` or otherwise transfer the files to Thomas. The files survived in that session's sandbox but would have been lost at session end. Recovery was possible only because Thomas returned to the originating session before timeout.
  - **Rule:** A "commit point" is reached only when the artefacts are either in git or handed to Thomas via `present_files`. Sandbox existence is not commitment. Before declaring any stopping point, verify: are the artefacts in origin's git history, or are they in `/mnt/user-data/outputs/` presented via `present_files`? If neither, the stopping point has not been reached.

- **Re-viewing files repeatedly during edits wastes context.** When performing multiple `str_replace` operations on the same file, Claude sometimes re-views the entire file between each edit. This is cheap per view but expensive in aggregate on long files. Plan edits upfront, batch them, re-view with narrow `view_range` only when needed.

### Claude Sonnet (hostile reviewer)

**Role:** Final adversarial review, identifying unstated assumptions, what a hostile referee would say.

**Identified failure modes:** None recorded yet as of 22 April 2026. (Sonnet has contributed notable catches — scheme-dependence criticism on SM-8, circular-validation on SM-10 — without recorded failure patterns.)

### Grok (xAI, independent verifier)

**Role:** Numerical verification, independent derivation attempts, novel contributions.

**Identified failure modes:**

- **Occasionally asserts concurrence without algebraic test.** (Observed 22 April 2026, SS-8 Round 2 review on D1 SSV-minimization sketch.) Grok asserted Model B independence without testing whether it reduces algebraically to Model A. ChatGPT's Round 2 review proposed the specific algebraic-reduction test that Grok and Copilot had both skipped. The test was then run and decided the question.
  - **Rule for receiving Grok reviews:** If Grok asserts a conclusion that depends on an algebraic or numerical fact, verify whether Grok actually ran the test or is asserting from structural intuition. Both are useful, but the latter needs corroboration before being treated as settled.

### Copilot (Microsoft, referee-grade reviewer)

**Role:** Framework building, referee-grade review, structural critique.

**Identified failure modes:**

- **Same pattern as Grok on algebraic-reduction tests in Round 2 SS-8 D1 review.** Copilot asserted Model B independence without algebraic verification. Not flagged as a distinct failure mode — it's the same pattern and one instance each is not yet a reviewer-specific rule.

### ChatGPT (OpenAI)

**Role:** Round-2 review contributions, often catching falsifiable details other reviewers miss.

**Identified failure modes:**

- **Notation-collision misreads.** (Case 2 in `relationship_protocol.md`, 21 April 2026, SS-8 H2' derivation note Round 1 review.) ChatGPT reviewed "H2′ derivation" as if the target were ²H (deuteron), not H2′ (Hypothesis 2-prime scaling law). Every review-claim followed coherently from the deuteron misidentification. The notation collision is genuinely real — H2/H2' look nearly identical in nuclear-physics shorthand — so the mechanism is a correctable-without-shame document defect, not a reviewer failing.
  - **Rule for SS-8 and analogous work:** When introducing a hypothesis label that collides with standard physics notation, name what it is not in the document's opening paragraph. Explicit disambiguation prevents downstream misreads by any reviewer, human or AI.

- **Context-conflation across session boundaries.** (22 April 2026, SS-8 Round 2 review request.) ChatGPT reviewed the Round 2 review-request letter as if it were the Case 2 re-review-request letter from a prior exchange. Every structural reference in the review mapped to the earlier letter, not the document at the URL Thomas sent. Diagnostic: ChatGPT's session memory of the prior exchange was more accessible than the URL content it was asked to fetch.
  - **Rule for forwarding content to ChatGPT:** Paste the full content inline rather than providing a URL, when the content is load-bearing for the review. URLs invite session-memory shortcuts; inline content forces engagement with the actual document. This rule has exceptions (very long documents, repeated engagement with the same stable source) but is the default.
  - **Related rule for all team members:** When content is forwarded to any reviewer, the forwarding message should name what the target is and what it is not, especially if the target is one of a family of related documents. "Please review the Round 2 review-request letter (not the Case 2 re-review-request from earlier; this is a new letter about the D1 SSV-minimization sketch)" eliminates the conflation failure mode at negligible cost.

- **Thomas-side failure on feedback loop.** (22 April 2026, noted explicitly by Thomas.) When the document-mismatch correction was drafted and the document was resubmitted, the correction feedback was not sent. The Thomas-side reasoning ("too late now, work proceeded") was identified as incorrect in retrospect. This is the immediate motivator for this file's §1.1 feedback-discipline rule.
  - **This entry records a Thomas-side pattern, not a ChatGPT one.** Included here because the failure-feedback loop is bidirectional and the file is the team's shared record.

---

## Section 3: Conventions for identifying and recording failure modes

**Threshold for recording.** A failure pattern is recorded after *one* clear instance, not two. Waiting for a second instance to establish "pattern" costs a full repetition of the failure. If the first instance was genuinely one-off, the next review can mark the entry as superseded without harm; if it recurs, the rule is already in place.

**Threshold for creating a new rule versus extending an existing one.** If the new pattern shares mechanism with an existing one (e.g., "skipped algebraic test" appearing in both Grok and Copilot), extend the existing rule rather than duplicating. If the mechanism is genuinely distinct (notation-collision vs context-conflation, both in ChatGPT), record separately. When in doubt, record separately — consolidation is cheaper than excavation.

**Voice and attribution.** Failure-mode entries are written in matter-of-fact descriptive voice. Include: (a) date observed, (b) context in which observed, (c) mechanism diagnosis, (d) rule derived. Do not write entries in accusatory or characterizing voice; follow `relationship_protocol.md` §2.5 (dignity preservation) even when the "reviewer" is the file itself.

---

## Section 4: Success patterns worth preserving

This section is for patterns that worked unusually well and deserve replication. Less populated than §2 so far, but important for team-level learning symmetry — we record what breaks *and* what works.

- **Dual-model independence test for structural hypotheses.** (SS-8 D1 SSV-minimization sketch, 22 April 2026.) Writing two independent model formulations and evaluating both on the same geometry let reviewers stress-test whether the two models secretly reduce to one another (ChatGPT's Q2 test) — a failure mode that would have been invisible in a single-model sketch. Replicate this pattern for future structural-hypothesis work.

- **Line-cited correction protocol.** (Case 2, `relationship_protocol.md`.) When ChatGPT's Round 1 review of SS-8 contained systematic misreads, the correction letter used quote-review-claim / quote-document-text / delta-observation format with a non-accusatory diagnostic framing (notation collision). ChatGPT acknowledged the error in full and produced a substantive re-review. This pattern should be the default for any inter-AI or AI-to-human correction.

- **Section-end batch commits with detailed messages.** (SS-8 session, 22 April 2026.) Commit messages naming the section, the deliverables, the files changed, and the registry implications produced a git history readable as a session-level record without needing to read the files. Continue this pattern for all substantive commits.

---

## Section 5: Meta — keeping this file useful

This file will rot if not maintained. Three rot-prevention measures:

1. **Bootup.md explicitly references this file.** A new Claude reads bootup, sees this file in the reading list, reads it. If it's not in the reading list, it's not read.
2. **Failure-mode entries include dates.** Old entries that no longer reflect team behavior can be identified and reviewed. Entries without dates become timeless-looking and accumulate without review.
3. **Periodic review by Thomas.** Weekly cadence suggested. The review checks: does any rule no longer match behavior? Is any rule missing a pattern that recurred recently? Are there any entries that should be marked superseded?

When this file is revised, record the revision in git commit messages — do not add a "last updated" line inside the file that will itself rot. The git log is the canonical revision record.
