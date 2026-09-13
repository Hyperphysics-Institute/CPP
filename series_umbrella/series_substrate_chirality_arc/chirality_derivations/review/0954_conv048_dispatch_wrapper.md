# CONV-048 — dispatch wrapper (INTERNAL; not sent to reviewers)

**Patch:** 0954, 13 Sep 2026. **Lane:** chirality (09xx). **Reviewer-facing package:** `0954_conv048_reviewer_package.md` — **that file alone goes to the seats**, with the three `.py` scripts attached. **Returns receiver:** `reviews-CONV-048.md`.

**Supersedes for review:** CONV-047 (dispatched 0952, adjudicated 0953 as QUORUM-FAILED). CONV-047's package is retained as a record.

## Why this is a reformat, not just a re-dispatch

The founder reported on 13 Sep that the CONV-047 package was confusing to read, and that the reviewers appeared confused by it. That diagnosis is correct and it is traceable to a specific fault, not to reviewer quality alone.

**The 0952 package used internal shorthand without defining it.** It asked questions *about* `C1`, `C2`, `C3`, `piece 1`, `MA.1` and `L4-A` while never stating what any of them were. Two of the three rejected CONV-047 returns fail in exactly the shape that produces:

- DeepSeek invented a "C2 class" — a category of mechanism with `A = 0` — and built its entire Q3 answer on it. `C2` is one of three *arguments* discharging the theorem. The package never said so. That misreading was available because the document made it available.
- Copilot misnumbered every question, answering the dispatch's Q5 as its Q1. The questions were buried at the end of a document that opened with economy classification and registry bookkeeping, with no visual separation between reviewer-facing content and internal record-keeping.

This does not excuse the fabricated timings (Gemini, DeepSeek) or the invented evidence — those are return-side failures and the 0953 rejections stand. But a package that cannot be answered from cold invites exactly the failure mode where a reviewer pattern-matches to the format instead of engaging the content. **The fix is ours to make.**

## What changed

1. **Self-contained.** Every term used in a question is defined before the question. Explicit glossary table for `C1`/`C2`/`C3`, with a sentence saying what they are *not* ("not classes of particle, types of mechanism, or parameter regimes"), aimed squarely at the DeepSeek failure.
2. **Internal bookkeeping removed entirely.** No economy classification, no patch numbers in the question stems, no registry language, no "scope held" section. Those live here instead.
3. **Questions last, numbered, visually separated**, each with a self-contained stem that needs no cross-reference, and each carrying its own consequence note.
4. **Plain-language physical setting first** (§1.1–1.3), so a reviewer with no programme knowledge can reach the questions.
5. **The two repairs the CONV-047 valid seats earned are folded into the proposal rather than asked about**, per 0953 §5:
   - **C2 restated** as a magnitude bound at the physical bias, dropping the "order δ³" characterisation. This was Seat 1's preferred option (b) and Seat 2's amendment — the same repair from both. Q3 now tests *whether that repair is right*, rather than re-litigating a wording nobody defended.
   - **The admissible A-domain stated** (|A| ≤ 1.025, tested range 98% of its positive half) in place of an unqualified "not conditional on A = 0", per both seats' Q6.
6. **The C2 scaling effect and the κ modelling gap are disclosed in the body**, not left for a reviewer to discover. Q4 explicitly invites dissent on our own choice.
7. **Return instructions ask for honest substitution** where a script will not run, and say why — GPT's disclosed vectorised replay at CONV-047 was the most trustworthy execution evidence received, and the format should reward that rather than pressure a reviewer toward a fabricated number.

## What did not change, deliberately

The six questions map one-to-one onto CONV-047's, and the escalation logic is unchanged: Q1 unsound ⇒ proposal fails; Q2 unsound ⇒ the theorem's *existing* conditionality is in question and escalates; Q5 disagreement ⇒ escalates. The re-dispatch is not an attempt to get a different answer by asking differently — it is the same question asked answerably.

## Open governance item (founder's, not enacted)

0953 escalated seat sourcing: three of five CONV-047 returns were not reviews. This package improves what we send; it cannot fix who receives it. The recommendation from 0953 stands — **treat a missing or impossible COUNT-LINE as automatic seat rejection rather than a discounted vote** — and remains the founder's call.

## Scope held

Banks the reformatted package and wrapper only. **No verdict moved, no THEO registered, no CHIR.md verdict edit, no count change.** THEO-CHIR-CAPACITY-1's registered conditionality on Mechanism A stands unchanged until a quorate panel adjudicates.
