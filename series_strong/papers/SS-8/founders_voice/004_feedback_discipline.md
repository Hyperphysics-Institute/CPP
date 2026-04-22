# Founders Voice 004 — Feedback discipline: no sacred cows, everyone grows

**Date:** 22 April 2026
**Session:** SS-8 structure cleanup — AI_team_expectations.md creation
**Thomas's articulation of team-level feedback principle, reflecting on skipped ChatGPT feedback**

---

**Context:** Thomas had drafted a correction letter to ChatGPT after ChatGPT's Round 2 review exhibited the context-conflation failure mode (reviewed the wrong document). The correction was drafted, but after Thomas had already resubmitted the correct content to ChatGPT, he decided not to send the correction — reasoning "it seemed too late."

**Thomas's retrospective:**

> I should have given ChatGPT the feedback. I didn't think about how important giving feedback was at the time, and it seemed too late after I had already resubmitted (both opinions were incorrect — if there is an error made by anyone, it needs to be spoken, delivered, acknowledged, and old behavior/habits/programs changed, regardless of who it is on the team — everyone depends on everyone, there are no heroes/gods/sacred cows, there are only team members who are growing and getting better at their role, and they can't get better without knowing the results of their actions — in the case of the AIs, that means recording rules that are reviewed periodically and revised as needed — which means that we should have a AI_team_expectations.md file that is reviewed on context window bootup, handover, when failure mode ID'd..., and periodically/weekly?).

---

## Why this matters

This is the most structurally important Thomas-voice contribution to date. It:

1. **Names the symmetric failure mode** — Thomas's own skip of the feedback loop is recorded as a pattern worth recording, not as a one-off. "Both opinions were incorrect" refers to his two reasonings ("too late now" and "work proceeded"). Neither held up to reflection.

2. **States the team-level principle explicitly** — no heroes, no sacred cows. The principle applies uniformly to Thomas, Claude, Copilot, Grok, ChatGPT, Sonnet, and anyone else who joins the team. Everyone's actions have consequences; everyone needs to know those consequences to grow.

3. **Identifies the mechanism for AI team members specifically** — recording rules in a committed file that's loaded on bootup. AIs cannot remember being told between sessions unless told is committed. A rule that lives only in session memory reaches only that session.

4. **Specifies the cadence** — bootup, handover, when failure mode identified, periodically. The file is not write-once; it's reviewed as behavior evolves.

---

## Direct consequences

- **`templates/AI_team_expectations.md` created this session.** Initial entries cover Claude Opus's "clean stopping point" failure, ChatGPT's notation-collision and context-conflation failure modes, Grok's assert-without-algebraic-test pattern, and this Thomas-side feedback-discipline lesson itself. The file is in the bootup.md mandatory reading list at priority 8.

- **Transaction 024 in `transcript-SS-8.md` flags the skipped correction letter as an uncommitted artefact.** The content is preserved in session transcript but not in git. A future recovery session can draft the letter and send it if Thomas chooses.

- **Rule operationalized for Claude:** When a correction is identified, deliver it. When a correction is drafted, send it. The absence of feedback is itself a team-level failure, not a neutral state.

---

## Pattern to record

Thomas's capacity to identify his own failure mode and articulate it with the same precision he applies to AI-side failure modes is a programme-level asset. The symmetry matters: if the protocol were only for correcting AI errors, it would be one-directional paternalism. The symmetric application establishes that everyone is accountable to the same standard.

This is the vignette that should be referenced when any team member — human or AI — is tempted to skip feedback because "the moment passed" or "it would embarrass them." The moment has not passed; the embarrassment cost is always less than the drift cost.
