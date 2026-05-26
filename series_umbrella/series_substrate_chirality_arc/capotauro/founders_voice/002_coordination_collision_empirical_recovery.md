# 002 — Coordination-Collision Empirical Recovery

**Date:** 16 May 2026 (Session 123)
**Speaker:** Thomas Lee Abshier ND
**Context:** During the parallel-window workflow of Session 123 (see `001_parallel_window_workflow_design.md`), a near-simultaneous-publication collision occurred. The documentation window was about to push Patch 0416G and the parallel physics window had also reached a publication-ready state at approximately the same time. Thomas asked the methodologically appropriate question rather than assuming or guessing.

---

## Thomas's articulation (verbatim)

> "Your instructions were to commit and push the first-arriving file, and that there would be no conflict with the new physics context window session. The new physics window and documentation window both finished at approximately the same time, and I don't know which one published first. What should I do?"

A follow-up message after running the `git pull --rebase` showed the rebase landing cleanly on origin/main, which displayed the prior patch in `git log`:

> "This is the message in response to your first command.
> It ends with a colon: what do I do?"

(The colon was the `less` pager prompt; pressing `q` exits, revealing the rebase had landed cleanly because the docs window's Patch 0416G touched a disjoint file set from the physics window's Patch 0417.)

---

## The structural insight, distilled

The Thomas question reframes a coordination problem as an empirically-answerable one. Three parts:

**(1) Methodology should not depend on temporal precedence claims.** The naive resolution to a collision would be "whoever pushed first wins; the other rebases." But Thomas did not know which window had pushed first, and the timestamps in the chat record do not reflect git push timestamps. The question is methodologically: do not assume; check. The answer is in `git log origin/main --oneline` — whichever commit is at HEAD on origin is the one that landed last; the rest of the rebase chain reflects what happened before. The temporal-precedence claim is recoverable from the git history; it does not need to be remembered.

**(2) The right response is to attempt the apply and handle conflicts at the conflict line.** The push-pull discipline (see 001) assumed disjoint file sets between docs and physics arcs. In the actual Patch 0416G + Patch 0417 collision, that assumption held — the files touched were disjoint and the rebase landed cleanly. The mechanical procedure for the receiving window:
  1. `git fetch origin && git log origin/main --oneline -8` — see what's on origin
  2. `git pull --rebase origin main` — attempt clean rebase
  3. `git am ~/Downloads/0NNNX-*.patch` — attempt apply
  4. If conflict, open the conflicting file (typically `changelog-X.md` if anything), find the `<<<<<<<` markers, keep both rows, save, `git add && git am --continue`
  5. If no conflict, just push.
  
The conflict resolution is local-and-fixable; the alternative ("redo the entire patch") is only necessary if the conflict is substantial enough that the patch's content has changed meaning under the new HEAD state. For Capotauro doc-suite patches and Reading C physics-arc patches, the file sets are disjoint enough that this has never happened.

**(3) Knowing what page in `less` you're on is not failure.** The follow-up message ("It ends with a colon: what do I do?") was the `less` pager prompt waiting for input after `git log` ran. The correct response is "press q to quit the pager." More broadly: tool-output ambiguity is normal; the right response is to ask, not guess. Setting `git config --global core.pager cat` or using `--no-pager` removes the friction for future invocations. The friction was minor and procedural; not asking would have been silent failure.

## What this teaches about parallel-window workflow

The Session 123 coordination collision is the first empirically-resolved test of the parallel-window workflow. It produced two refinements to the discipline (see 001):

- **Pre-apply inspection becomes a step.** The receiving window should run `git log origin/main --oneline -8` before assuming its handover state is current. The docs window did this; the physics window did not (and its Patch 0417 commit message reflected the stale handover). The right discipline going forward: every patch-apply chain starts with the git-log inspection.

- **Pager friction is a real cost.** The `less` pager defaults caused a momentary stall in the apply chain. Removing pager defaults globally (`git config --global core.pager cat`) or always invoking with `--no-pager` is a small change that prevents the friction class.

The coordination glitch (physics window's commit message claiming drift items still pending when they had been fixed) is structurally informative: it shows that handover state can become stale during a window's lifetime. The mitigation is `git log` inspection at apply time, not handover document refresh.

---

*This file is a Tier-1 founders_voice artifact per `templates/operating_system.md` §4 Four-Tier Documentation Discipline. The verbatim quotation is from the current Session 123 docs-arc context window (third compaction window of this session, not yet archived as a transcript file at the time of this writing). Source-text exact reproduction relies on the active context window's recall.*
