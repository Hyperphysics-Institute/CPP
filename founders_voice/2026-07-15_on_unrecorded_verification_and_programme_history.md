# Founder statement — on unrecorded verification and the programme's early history

**Date:** 15 July 2026 · **Context:** delivered after the Patch 2477–2480 integrity-audit
arc, correcting the characterization of the SR-1-era Monte-Carlo citations.
**Capture class:** founders_voice (verbatim; per the founder-capture protocol).
**Consequence patches:** 2481 (terminology correction: "fabricated" → "unrecorded,
Sonnet-era, pre-protocol"; reconstruction track opened).

---

Verbatim:

> Note: none of the MC paper and results were fabricated in the "without basis" sense;
> they were unrecorded. SR-1 was the first paper in the series, done with Sonnet, after
> retiring a previous AI model upon realizing Sonnet seemed reliable. Sonnet assured me
> that an earlier model of Opus was unnecessary, that he could handle it, so we used
> Opus as the Reviewer. We did not have a protocol; no one told us what to record or
> where to record it. Little by little, I had ideas about what we should do to have a
> complete record of what we were doing (how we got there, rather than just the
> theorems). Prior to that time, we did not use Git macros to apply patches; I applied
> them manually in Git Desktop. Initially, we had commands in the operating system to
> record .py code, reasoning, or founders' voice. Several times we embedded rules in
> the operating system to record reasoning and scripts, and then as changes were made,
> those OS prescriptions were forgotten/overlooked. All this is to say that papers
> based on results reporting the use of .py code actually ran code. It was merely
> unrecorded after it was used and results generated. The entirety of SR-1, all the
> conclusions that ran MC tests, were done by Claude in one version or another. The
> deficiencies were those of an immature researcher and an early-stage AI model, not
> fabrication. The question is only whether the code, MC runs, papers, and results can
> be reconstructed. The effort to simply identify them as unreliable or fabricated is
> hygienic but does not capture the spirit and possibility of reconstruction. Just
> some background. These were the results of creating something from nothing, guided
> only by AI and my sense of what good research should be, having never done research.
> I think we are in a much better place now, but it has taken us months of iterative
> protocol development to create a system that is reasonably reliable. Looking back, I
> should have had Opus redo Sonnet's work entirely, but since Opus had reviewed it, I
> thought it was reliable. We now have 5 reviewers, all from independent models, and we
> all realize how fallible the human and silicon brains are, and we do our best.

---

**Methodological significance (AI annotation, not founder voice):** This statement
establishes the correct failure taxonomy for the pre-protocol era. The audit's
artifact-level findings stand unchanged — a stub committed where a script is cited is
irreproducible-as-committed regardless of history — but the intent-laden word
"fabricated" is withdrawn from the programme's characterization of them. The correct
term is **unrecorded verification**: the runs occurred in-session (Sonnet-era), the
capture protocols that would have preserved them did not yet exist, and the committed
placeholders are scars of that gap, not inventions. The remedy taxonomy differs
accordingly: fabrication is terminal; unrecorded verification is **reconstructible**,
and each unrecorded item becomes a reconstruction candidate with a defined target. It
also documents why the capture discipline (reasoning fragments + verify scripts bundled
per-patch, CLONE-FIRST, the 2477 integrity gate) exists: the OS-prescription era showed
that rules not enforced by tooling get forgotten under change.
