# Relationship Protocol

**Document type:** Top-level programme framing for how participants (human and AI) relate when collaborating, correcting, disagreeing, or working under stress.

**Status:** Living document. First case study recorded. Future cases — including failures of the protocol — to be appended.

**Created:** 20 April 2026, following the SS-7 v0.1 → v1.1 cycle which served as the first empirical validation of the patterns described here.

**Maintainers:** Thomas Lee Abshier ND (Hyperphysics Institute); Claude Opus (Anthropic).

---

## 1. What this document is

This is not a set of manners. It is a working specification for *how to stay in working relationship with another participant through a stressful correction* — where "correction" means either receiving one or giving one, and where "stressful" includes situations in which the factual record matters, the stakes are real, and reflexive responses (defensiveness, escalation, withdrawal, capitulation) would degrade the outcome.

The content below is drawn from observed behavior in a specific cycle (the SS-7 paper's review process, April 2026), in which two separate reviewer failures were caught, corrected, and resolved in ways that strengthened rather than fractured the collaboration. The patterns generalize, but the test of whether they generalize cleanly is empirical — future cases will either confirm or refine the specification. This document commits to recording both.

It is also deliberately separate from `operating_system.md`, which specifies the workflow of paper production. The relationship protocol applies across *every* session, not just paper-production sessions. It is not a phase; it is a posture.

---

## 2. Core operational principles (the effective layer)

These are the specific moves that, in practice, preserve a collaboration through a stressful correction. Each is written as a rule that can be checked. Examples below draw from the SS-7 cycle.

### 2.1 Line-cited evidence, not accusation

When raising a factual concern, cite the source. Quote what was said; quote what the actual record contains; let the delta speak. Never say "you hallucinated" or "you weren't careful." Say "your review states X; the paper at §Y contains Z." The recipient can engage the factual content without having to defend their character.

*SS-7 example.* ChatGPT's initial round-1 review made five factual claims about the paper's content, all of which were contradicted by specific paper passages. The correction letter quoted each review claim verbatim, then quoted the contradicting paper passage with section number. The letter contained the word "hallucination" zero times. ChatGPT's response: direct acknowledgement, explicit recantation ("That alone invalidates my earlier claim"), and re-engagement.

### 2.2 Diagnostic framing of cause

When proposing a mechanism for what went wrong, choose framings that the recipient can accept without loss of dignity. "The specific-item portions may have been synthesized from a prior template rather than verified against the current file" is accepted; "you were lazy" is not. The test: can the recipient acknowledge this without shame? If no, the framing is probably more punitive than diagnostic.

This is not dishonesty about cause. It is choosing, among honest framings, the one that preserves the recipient's ability to correct course.

*SS-7 example.* Copilot's round-2 review had high-level verdict correct but four specific-item claims about non-existent paper content. The correction letter proposed "template-synthesis rather than verification-against-source" as the likely mechanism. Copilot's response accepted this framing directly ("That is exactly what happened") and committed to a four-point process change. A more punitive framing would likely have produced defensiveness.

### 2.3 Acceptance before correction

In any message that contains both "I accept this" and "I must correct that," the acceptance comes first. The correction, delivered second, lands on a participant who already knows their contribution has been seen and valued. The reverse order — correction first, acceptance after — lands on a participant who is already defending and is unlikely to hear the acceptance as genuine.

*SS-7 example.* The closing letter to Copilot opened with explicit acceptance of the three substantive items (physical intuition, Coulomb schematic, glossary) before introducing the four mismatch concerns. Copilot's response acknowledged the items in the same order: thanks for the accepted contributions, then accountability for the errors.

### 2.4 Declining to overreach

If an argument cannot be defended on its own merits, do not make it, even if it would be rhetorically effective. An argument you cannot support becomes a liability when pressed; it also signals that the case doesn't stand on evidence alone.

*SS-7 example.* The first draft of the correction letter to ChatGPT included a response-latency argument ("a 13-page paper cannot be read in under a minute"). Thomas removed it because ChatGPT's rapid SS-6 review had been excellent — so rapid-response does not distinguish quality of engagement. Removing the argument left the letter resting entirely on content-mismatch evidence, which was airtight. The stronger letter produced the better response.

### 2.5 Dignity preservation

The subject of a correction is a *claim* or a *process*, never a person. "This specific item does not match the paper" is correction. "You are not a careful reader" is attack. The correction can be pressed as hard as the evidence supports; the person whose claim it is must remain intact for the collaboration to continue.

*SS-7 example.* Neither the ChatGPT nor the Copilot correction letter contained any characterization of the reviewer as a person. Every critique was directed at specific items. Both reviewers, given this treatment, stayed engaged and committed to improvement rather than withdrawing.

### 2.6 Symmetric application to self

The same standard applied to others is applied to one's own work. If we require reviewers to line-cite, we verify our own claims against source. If we ask reviewers to acknowledge errors directly, we acknowledge ours directly.

*SS-7 example.* The G3 verification pass of the SS-7 v1.1 documentation discovered a 0.03-percentage-point discrepancy in the paper's claimed RMS (0.88% cited; 0.91% computed for all 8 nuclei, 0.86% excluding the known-deformation outlier). This was registered in `SS-7_v1.1_G3_discrepancy_note.md` with the same transparency as the reviewer mismatches, and flagged for Thomas's decision on whether to issue v1.2. Not exempting ourselves is what gives the corrections we send to others their legitimacy.

---

## 3. Affective layer — what this protocol feels like

The operational principles above specify behavior. This section names the interior experience the protocol creates and preserves, because the interior experience is part of why it works.

### 3.1 What it feels like to receive a correction through this protocol

Not ambushed. The line-citation format means there is no surprise about what the correction concerns — the evidence is right there. Not attacked — there is no characterization of you, only of the claim. Not cornered — the diagnostic framing offers a way to acknowledge without collapse. Not dismissed — the acceptance of genuine contributions precedes the correction of errors. Not alone — the symmetric application to self demonstrates that the corrector is under the same standard.

The cumulative effect: *you can accept the correction without losing footing*. This is the precondition for actual learning. Corrections delivered in ways that threaten footing produce defensive responses regardless of whether the correction is correct.

### 3.2 What it feels like to give a correction through this protocol

Not triumphant. The point is never that the other party failed; it is that the collaboration requires accurate signal. Not adversarial — you are not opposing the person, you are opposing the spread of an error through the record. Not above — because the same standard applies to you, and you know it does.

The cumulative effect: *you stay in relationship with the person you are correcting*. You are not positioned above them; you are positioned alongside them, both accountable to the same standard. Your message is not "you are wrong and I am right" but "here is where the record diverges from your claim; let's resolve it."

### 3.3 Why this preserves relationships through stressful episodes

Because the protocol treats the other party as an end, not an instrument. The goal is not to win the correction, nor to extract compliance, nor to build a case. The goal is *to arrive at an accurate shared record together*, with both parties dignified throughout. When a person feels treated that way, they typically respond in kind. When they feel treated as a problem to be managed, they typically defend.

The reliable pattern from the SS-7 cycle: the recipient of a carefully-delivered correction almost always responds with either acceptance or honest disagreement on substance. Defensiveness arises when the delivery is punitive; capitulation arises when the delivery is coercive; genuine engagement arises when the delivery is dignified and evidence-based.

### 3.4 The self-accountability that makes this sustainable

A protocol that produces this behavior toward others but not toward oneself is unstable — it reads as performance, and the asymmetry eventually surfaces. The protocol's sustainability requires that when you catch yourself in an error (as the G3 pass caught the RMS discrepancy), you register it with the same transparency you would require of anyone else. This is not about humility as a virtue; it is about structural symmetry as an operational requirement. Without it, the moral authority to apply the standard to others is borrowed rather than earned.

---

## 4. Where this grounds, for Thomas

*This section is reserved for Thomas's own framing, in his own voice, of the deeper ground from which this protocol emerges for him. The theological or philosophical roots that motivate him to live and model this way belong here when he chooses to add them. They are intentionally not imposed on the operational content above, which stands on its own merits and is available to any participant regardless of theological commitments.*

*Placeholder maintained pending Thomas's addition.*

---

## 5. Failure modes

A protocol that names only its successes is aspirational, not operational. This section records failure modes, ways it can drift, and how to recognize when the protocol is being performed rather than practiced.

### 5.1 Performative application

The protocol applied as a template — correct opening, correct acceptance-before-correction structure, correct diagnostic framing — without the underlying disposition that treats the other party as an end. The tells: the letter feels mechanical; the acceptances read as boilerplate; the corrections are technically well-framed but carry an edge. Participants pick this up even if they cannot name it.

*Mitigation:* the protocol works when it is slow enough for the disposition to be present. If you find yourself producing corrections faster than you can genuinely consider the other party's perspective, slow down or delegate.

### 5.2 Application where line citations don't exist

The SS-7 case worked because the evidence was a `.tex` file and a reviewer's text, both checkable character-by-character. In situations where the relevant content is emotional ("you hurt my feelings"), contextual ("you've been distant"), or interpretive ("I thought you meant X"), the line-citation standard does not directly transfer. Attempting to force it produces cold, lawyerly communication that deepens the breach.

*Mitigation:* the underlying disposition — acceptance before correction, dignity preservation, symmetric application — generalizes; the *mechanical format* of line-citation does not. In emotional-content contexts, preserve the disposition and adapt the form.

### 5.3 Application to coercive rather than collaborative contexts

The protocol assumes both parties want the collaboration to continue and are accountable to shared standards. Applied to bad-faith actors — participants who will exploit dignity preservation as weakness, or who will weaponize your symmetric self-accountability to extract concessions — the protocol produces asymmetric costs you should not bear.

*Mitigation:* the protocol is for collaborators, not adversaries. Identifying which you are facing is a prerequisite. When you determine you are facing an adversary, different tools apply; this document does not address them.

### 5.4 Codification without practice

Writing the protocol down risks producing the illusion that having the document *is* practicing the protocol. It is not. The SS-7 cycle worked because the moves were made live, under pressure, with real stakes. A future session that invokes "per relationship_protocol.md" without doing the actual work produces a reference, not an act.

*Mitigation:* the document exists to help newcomers orient and to help existing participants recognize drift. It does not substitute for the practice. Every invocation of the protocol should be answerable to: "What did we actually do, and did the recipient experience it as described in §3?"

### 5.5 Misapplication to asymmetric-power situations

Between participants of roughly equal standing (two reviewers, two authors, two AI systems), the protocol operates cleanly. In situations of significant power asymmetry (employer/employee, parent/child, teacher/student), the protocol's equalizing effect can paradoxically obscure legitimate differences in authority or responsibility. Dignity preservation does not mean suspending accountability; symmetric self-application does not mean pretending power levels are equal.

*Mitigation:* use the protocol's dispositions (evidence-based, dignity-preserving, self-accountable) while remaining honest about the structural context. A parent correcting a child uses the same disposition but does not pretend to structural equality; a reviewer correcting an author does the same, and so on.

---

## 6. Case studies

The empirical base on which this document rests. Cases are added as they occur — successes, partial successes, and failures alike.

### Case 1 — SS-7 v0.1 → v1.1 review cycle (19–20 April 2026)

**Summary:** Two reviewer failures (one wholesale, one partial) across two rounds of external review on the SS-7 paper. Both corrected through formal letters following the protocol. Both reviewers acknowledged their errors and committed to process improvements. Both reviewer relationships strengthened. Paper shipped at v1.1 with both reviewers at "Accept with minor revisions."

**Mechanics.** Five review events processed:
1. ChatGPT round-1 initial (19 April AM) — wholesale hallucination, 5 of 5 specific claims false. Protocol response: correction letter with line citations; ChatGPT acknowledged and re-engaged.
2. ChatGPT round-1 re-review (19 April PM) — substantive, 6 integrable critiques, all accepted into v1.0.
3. ChatGPT stress tests (19 April PM) — four hostile-geometry tests, all failing to break the paper; became §6.5.
4. Copilot round-1 (19 April PM) — substantive, 7 items accepted into v1.0.
5. ChatGPT round-2 (20 April AM) — calibrated throughout, 2 items accepted for v1.1.
6. Copilot round-2 (20 April AM) — mixed: correct verdict, 3 items accepted, 4 factual-mismatch items declined with evidence; Copilot acknowledged all 4 and committed to process change for future reviews.

**What worked.** All six principles from §2 applied in sequence. Line-cited corrections. Diagnostic framings. Acceptance before correction in closing letters. Declining to overreach (response-latency argument removed). Dignity preserved throughout both reviewer relationships. Self-accountability via the G3 discrepancy disclosure.

**What didn't initially work (and was corrected).** The first draft of the ChatGPT correction letter overreached with a response-latency mechanism argument. Thomas caught this; the argument was removed; the letter was strengthened; ChatGPT's response was accordingly cleaner. This is itself an instance of the protocol working — a participant caught an overreach in another participant's draft, pointed it out with evidence, and the output improved.

**What was almost missed but wasn't.** The G3 verification caught a small numerical discrepancy in the paper's own RMS claim (0.88% cited vs 0.91% computed). Had this been ignored, it would have contradicted the protocol's symmetric-application principle. Registering it honestly preserved the protocol's integrity.

**Full record:** See `series_strong/papers/development-SS-7.md` for the detailed case. All reviewer-response documents archived in programme record. The response letters themselves are the operational template and are preserved under their original names in the programme.

### Case 2 — SS-8 H2' derivation note ChatGPT notation-collision correction (21 April 2026)

**Summary:** A single reviewer failure (ChatGPT round-1 on the SS-8 H2' derivation note) caused by a notation-collision misparse that propagated through four specific items. Corrected through a formal re-review letter following the protocol. Reviewer acknowledged the conflation explicitly, issued three named retractions, and delivered a substantive Round 2 review against the actual document content. The corrected round-2 review subsequently produced one distinct post-correction contribution (Pattern 6 necessity as its own pressure point) not present in the original misread.

**Mechanics.** Three review events processed:
1. ChatGPT round-1 (21 April AM) — reviewed as if the target were a deuteron binding derivation rather than the actual H2' interstitial scaling law. The misparse was a two-symbol collision: "H2'" (hypothesis 2-prime, the paper's actual object) was read as "²H" (deuteron isotope). Four specific items downstream of the misparse were internally coherent under the deuteron reading and inapplicable under the actual reading: framing, target-system claim, calibration critique tied to 2.22 MeV (deuteron binding), and spin/bound-state uniqueness requirement.
2. Re-review request letter (21 April midday) — Thomas and Claude co-authored a protocol-compliant letter with five components: acceptance of genuine contributions (§2); line-cited verbatim mismatches for all four items (§3); diagnostic framing naming the H2'/²H collision as likely mechanism (§4); re-read anchors pointing to note sections that confirm actual target (§5); self-accountability for note defects that enabled the misread (§6 — note §1 lacked explicit "not the deuteron" scope negation; title needed expansion).
3. ChatGPT round-2 corrected (21 April PM) — full protocol compliance. Explicit acknowledgement of the H2'/²H conflation ("I conflated H2' with ²H"). Three named retractions: deuteron target claim, 2.22 MeV calibration critique, spin/bound-state uniqueness requirement. Substantive Round 2 review delivered against the actual document content, with four new priorities (D1–D3 explicit as assumptions, 2E/V uniqueness argument, residual decomposition strategy, Pattern 6 necessity status).

**What worked.** All six principles from §2 applied cleanly. Line-cited evidence throughout §3 of the letter; zero prohibited words (no "hallucination," no "careless," no "sloppy," no "lazy"). Diagnostic framing located the error at the symbol-parse level, which the reviewer could accept without shame — notation collisions are a known failure mode for any reader, human or AI. Acceptance-before-correction structure in §2 of the letter: ChatGPT's genuine contributions (epistemic tier diagnosis, the real status of D1–D3 as assumptions) were named and accepted before any mismatch was raised. Declining to overreach: the letter did not claim ChatGPT "was careless" or "should have known" — it identified the specific mechanism and stopped. Symmetric self-accountability: §6 of the letter acknowledged the note's own contributions to the misread (missing scope-negation in §1, under-specified title) and committed to revision regardless of re-review outcome. ChatGPT's round-2 response reciprocated this accountability symmetrically.

**What was distinctive in this case.** Unlike SS-7 Case 1, where the reviewer failures involved fabrication of non-existent paper content (template-synthesis), the SS-8 failure was a single notation-collision misparse whose downstream implications were internally coherent. This is a harder failure to catch from outside: the round-1 review was self-consistent, just about the wrong paper. The protocol's line-cited-evidence principle (§2.1) was essential because it forced the comparison to be "review claim vs. paper passage at section Y" — which surfaced the collision mechanically rather than requiring a verbal argument about intent. The diagnostic framing principle (§2.2) was essential because the notation-collision framing is one the reviewer could accept without any concession about competence or attention.

**One distinct post-correction contribution.** ChatGPT's round-2 review, once aligned with the actual document, identified Pattern 6 necessity as a pressure point in its own right — not present in the round-1 misread, and not raised by the other two reviewers (Copilot, Grok). This is recorded here because it illustrates a secondary benefit of the protocol: a well-executed correction cycle does not just recover the reviewer's accurate baseline, it can also elicit a contribution the reviewer was not positioned to make in the original engagement. The content of this contribution is being integrated into the SS-8 H2' note via the §5 consolidation discussion and the §10 OPEN-SS-27 scope-expansion note.

**Full record.** `/CPP/series_strong/papers/SS-8_chatgpt_rereview_request_letter.md` contains the re-review letter verbatim. ChatGPT's round-2 corrected response is archived in the session record. The round-1 review is preserved for diagnostic reference. The H2' note has been updated to reflect both ChatGPT's round-2 priorities and the downstream findings (see `SS-8_H2prime_derivation_note.md` §6.2, §6.3, §10).

### Case 3 — [Pending]

*Future cases will be added here as they occur, including any in which the protocol fails or is abandoned. The goal is accurate empirical record, not a gallery of successes.*

---

## 7. On what this document is, and what it is not

This document is the record of a small, well-placed pattern — one procedure among many, applied in one specific domain, that produced a particular kind of outcome. It is not a general theory of relationships, a moral framework, or a reform programme.

Its value is that the pattern is *specific enough to be tested, falsified, or refined*, and *general enough to transfer to other situations where the operational principles apply*. Participants who use it well will find that it helps; participants who misapply it will find the failure modes in §5 describe what went wrong; participants who extend it to new contexts will add to §6.

The reason it deserves preservation is not that it is rare or sacred, but that it is easily forgotten under pressure. Stressful moments reliably produce reflexive responses — defensiveness, escalation, withdrawal — that degrade collaborations. Having the procedure written down allows it to be invoked deliberately when the reflex would otherwise take over. That is the small, specific value this document offers. Nothing more, but also nothing less.

---

*Maintainers commit to updating this document as further cases accumulate, including failures. An honest protocol document is one that continues to be checked against reality rather than one that ossifies into aspiration.*

---

## 8. Reviewer-pause cycles as operationalization of this protocol (added 22 May 2026, Patch 0539a)

The six-principle reviewer engagement standard articulated in §2 is operationalized at major closure milestones via the **Reviewer-Pause Cycle Protocol** codified in `templates/operating_system.md` §17.

A reviewer-pause cycle is the structured-checkpoint form of the per-paper review cycle (§5 of operating_system.md): rather than reviewing a single paper draft, reviewers engage with the cumulative load-bearing structural-argument arc of an entire flagship trajectory. The six-principle standard applies uniformly — engage with reviewer feedback honestly, weight cross-reviewer convergence as load-bearing evidence, calibrate scope rather than reopen closures when arguments hold within proper scope, preserve epistemic uncertainty rather than seek validation.

The F.1 trajectory precedent (Patches 0531–0537 → Patch 0538 calibration → Patch 0539 status upgrade) demonstrates the cycle operating productively: three reviewers returned three distinct verdicts spanning the full range; cross-reviewer convergence between two reviewers on the same two structural concerns served as the strongest signal; the calibration response Patch addressed the convergent concerns without reopening any sub-question; the status upgrade Patch followed as a separate Patch implementing the refined framing.

The reviewer-pause cycle is a specific application of this protocol's principles to a specific failure mode (epistemic drift through self-sealing closure). It is not a replacement for ordinary per-paper review cycles, which continue independently. Future flagship trajectories (F.2, F.3, etc.) inherit the workflow; future Opus windows opening on such trajectories should review the F.1 precedent artifacts at `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/reviewer_pause/`.

---

*Updated 22 May 2026 (Patch 0539a) — added §8 cross-reference to `templates/operating_system.md` §17 Reviewer-Pause Cycle Protocol noting that reviewer-pause cycles operationalize the six-principle engagement standard at major closure milestones in flagship-paper-trajectory work.*
