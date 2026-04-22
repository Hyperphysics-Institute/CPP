# Founders Voice 005 — Three-file documentation-suite convention

**Date:** 22 April 2026
**Session:** SS-8 structure cleanup — per-paper subfolder convention refinement
**Thomas's specification of three distinct documentation file types**

---

**Context:** Claude had proposed a single documentation file ("development-SS-8.md") that would play both the retrospective-narrative role and the session-handover role. Thomas pushed back with a distinction that generalized the convention.

**Thomas's contribution (first articulation):**

> I was thinking of making the handoverxxx.md file ad hoc, upon command, as needed, rather than incrementally, but perhaps doing it incrementally would be better, since it would be able to give the full transcript in pointers and requires almost no additional processing to do it at the time the full session transcript was being created. So, yes, this sounds good to me. The one thing that I don't think I communicated well enough for it to be isolated, was that I was advocating for 3 types of files. 1) full transcript, leaving out housekeeping, 2) edited transcript that gave the roadmap tour with more summary content (this is the way that it had been done on previous files), and 3) a handover.md file.

**Thomas's refinement on the edited transcript (second articulation):**

> I don't think it needs to be edited. It would simply be a narrative of the journey, without a definitive knowledge of the end in every vignette. This should be really low computational overhead; it's just the summarized story of each session (or sessions), never to be touched again.

---

## Why this matters

Claude had been thinking of "retrospective narrative" as requiring periodic re-curation — hindsight-informed rewriting as the paper's state advanced. Thomas's refinement replaced that model with something simpler and better:

- **Session vignettes written in-moment.** Each vignette captures what that session believed at the time, without foreknowledge of how things turned out.
- **Never retrospectively edited.** Later sessions do not rewrite earlier vignettes. If a later session proves an earlier framing wrong, the later vignette records the correction; the earlier vignette stays as written.
- **Low overhead.** No craft-work of periodic recuration. Just session-by-session append.

This has three beneficial consequences:

1. **Preserves honesty about what was believed.** A decision that looked weird at the time and turned out to be right is recorded as it was thought, not prettified. A dead-end that later work avoided is preserved as a dead-end, not hidden.

2. **Makes incremental update costless.** A session-closing vignette is 1-3 paragraphs. That's always affordable regardless of context budget.

3. **Dissolves the v1.0 crystallization problem.** Under a retrospective model, there was a question of when to "finalize" the retrospective. Under the vignette model, the file just keeps appending forever. v1.0 is just another vignette. Post-publication revisions are just more vignettes.

---

## Direct consequences

The three-file convention now documented in `templates/operating_system.md` §11:

- **`transcript-[ID].md`** — transaction-indexed pointer-map (the "full transcript" with housekeeping removed, per Thomas's point 1)
- **`development-[ID].md`** — session-by-session vignettes (the "narrative of the journey, without definitive knowledge of the end," per Thomas's point 2 refined)
- **`handover-[ID].md`** — bounded state snapshot for next session (per Thomas's point 3)

The "no retrospective editing" rule is load-bearing. It's stated explicitly in operating_system.md §11 under "The three-file documentation-suite convention" and in each development-*.md header.

---

## Pattern to record

Thomas's initial framing ("edited transcript that gave the roadmap tour") had an implicit assumption about craft-level curation. His refinement ("I don't think it needs to be edited") eliminated a significant cost that Claude hadn't noticed was a cost. The simpler model scales linearly with session count; the retrospective-editing model scales super-linearly (each re-curation pass costs more as the file grows, and the craftsmanship requirement compounds).

This is a case where Thomas's scope-discipline instinct caught a Claude-side tendency toward over-engineering. Claude wanted the file to be elegant retrospective narrative; Thomas wanted the file to be cheap and honest.

The rule: when facing a choice between "periodic recuration of prior content" and "append-only new content," choose append-only unless the recuration is absolutely necessary.
