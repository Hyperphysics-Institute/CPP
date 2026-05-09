# SF-Line Switch Log and Protocol

**Location:** `/CPP/flagship_papers/SF-line_switch_log.md`
**Established:** 9 May 2026 (Session 38, patch 0296)
**Strategic source:** [`/CPP/research_priorities.md`](../research_priorities.md), [`README.md`](README.md)

---

## §1. Purpose

The SF-line work proceeds **serially**, with one Claude conversation window active at a time. Default primary work is the active heavy-lift paper (currently **SF-4 neutrinos**); other family papers (SF-1, SF-2, SF-3) and the synthesis paper (SF-5) are advanced as derivation logic dictates, not by fixed shipping priority.

A **family switch** is the deliberate redirection of session work from the currently active SF-paper to a different SF-paper, on the recognition that the next-step derivation in the active paper will be most cleanly closed by first developing a specific result in another family. This document records every such switch — the trigger, the target, the planned return condition, the actual outcome — so the SF-line's development path is readable both to future external reviewers and to future Claude context windows.

The protocol exists because CPP's harder derivations (SS-9 conditional-theorem closure, SM-9 $V^{7/3}$ exponent, the angular-pair-model resolution of the Shell-3 gap) historically did not yield to working straight through a single paper. They yielded to sustained engagement with one problem until it surfaced an adjacent piece that needed development; that adjacent piece was developed; the original problem was returned to with the new tool. Strict-C SF-line work — particularly the SF-4 neutrino derivation campaign — almost certainly has the same texture. The switch log is the discipline that lets that texture be productive instead of chaotic.

## §2. When to switch — trigger discipline

A family switch is justified when **all four** of the following are true:

1. **The trigger is a specific identified derivation gap in the current paper's work**, not a generalized sense that the work is stuck. "I cannot see how to derive the unbound-mode suppression factor" is not a switch trigger. "The unbound-mode suppression factor requires the EW Higgs-analog VEV mechanism that SF-2 has not yet derived; SF-2 §X work would close this" is.

2. **The target work is specific in scope.** Specific target paper, specific target section, specific derivation result. Not "let's go work on SF-2 for a while."

3. **The expected return condition is specific.** The original gap closes when a specific, statable result has been derived in the target family. Not "we'll know when to come back."

4. **Both Thomas and Claude agree on the switch.** Documented in the switch log entry. Not a unilateral redirection.

If any of the four fails, the switch is not justified. Press on the active paper, register the gap as an `OPEN-FP-N-*` problem under the active paper's conditional-theorem inheritance, and continue rather than redirect.

## §3. When NOT to switch — anti-patterns

The following do not justify a switch and represent failures of the protocol:

- **Procrastination disguised as redirection.** "This is hard, let me work on SF-1 reframing for a while." If the switch is motivated by the difficulty of the active work rather than by a specific identified derivation gap, the switch is procrastination. The fix is to register the gap as `OPEN-FP-N-*` and press on, or to take a session break, not to switch.

- **Vague triggers.** "The suppression factor seems to need more thought" is not a derivation gap. "I'm uncertain about the K3 eigenstructure argument" is not a derivation gap. A derivation gap is a specific result that, once obtained, would close a specific step in the active paper's derivation.

- **Speculative cross-pollination.** "Maybe SF-2 work would yield something useful for SF-4" is not a switch trigger; it is speculation. Speculative cross-pollination is the hope of insight from elsewhere; valid switches are the *recognition* that a specific elsewhere result is needed.

- **Switching to route around strategic-decision queue.** Some decisions require Thomas's input — calibration architecture, $\delta_{CP}$ posture, conditional-theorem inheritance scope, headline number framing. If the active paper is queued on Thomas, the appropriate response is to wait for Thomas, not to switch families to keep moving. Sessions can close cleanly waiting on a strategic decision; switches should not be used to manufacture motion.

- **Switching during heavy-context derivation work.** When the active paper is mid-derivation in a session — substantial context loaded, working through specific calculations — switches mid-session lose the loaded context and produce churn. Switches should happen at session boundaries, not within a session, except in rare cases where the in-session work has produced an unambiguous "I need result X from family Y to proceed" finding.

## §4. Switch entry format

Each switch is recorded as a numbered entry below. Entry format:

```
### SW-NNN: [one-line summary]

**Date / Session:** YYYY-MM-DD / Session NN
**Patch:** ####
**Source family:** SF-N (paper title)
**Source-specific issue:** [the specific derivation gap that triggered the switch]
**Target family:** SF-M (paper title)
**Target-specific work:** [the specific derivation needed in the target family]
**Planned return condition:** [the statable result whose obtaining marks the source gap as closeable]
**Expected duration:** [sessions]
**Thomas + Claude agreement:** [date / session of agreement]

#### Outcome (filled in on return)

**Actual duration:** [sessions]
**Result obtained:** [what was actually derived]
**Original gap closed?** [Yes / No / Partially — with explanation]
**Lessons:** [what the switch taught about SF-line texture or this protocol]
```

Failed switches — switches that did not close the original gap — are particularly valuable to record honestly. They reveal where the SF-line texture is more entangled than anticipated and where the protocol may need adjustment.

## §5. Switch log

*No switches recorded yet. First entry will be appended below as switches occur.*

---

## §6. Protocol revision history

This protocol is itself adjustable. Experience with actual switches will surface format inadequacies, missing discipline categories, or trigger criteria that prove too strict or too loose. Revisions are recorded here.

| Revision | Date | Patch | Change | Rationale |
|----------|------|-------|--------|-----------|
| v1.0 | 9 May 2026 | 0296 | Initial protocol established | Session 38 conversation between Thomas and Claude on SF-line coordination after Option-3 architecture adoption (patch 0295). Codify discipline before the first switch rather than after, with the explicit acceptance that revisions will follow real experience. |

---

*This protocol applies to inter-paper switches within the SF-line (SF-1 through SF-5). It does not govern within-paper section ordering, within-section iteration, or programme-level priority shifts (which are recorded in `research_priorities.md`).*

*See [`README.md`](README.md) for the SF-line architecture overview.*
