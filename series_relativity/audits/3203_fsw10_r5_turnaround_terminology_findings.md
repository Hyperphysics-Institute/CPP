# F-SW-10 · R-5 FINDINGS NOTE — "turnaround" terminology (Patch 3203)

**Charter:** `3140_fsw10_post_cc_subpsr_delta_audit_charter.md`, item R-5.
**Opened with:** the collision located by R-2.5 (Patch 3201 §5).
**Verdict: R-5 CLOSES CONSISTENT. Zero edits owed.** A naming convention is
registered to prevent future drift, and **the R-2.5 recommendation is reversed**
— see §3.

---

## §1 — Three senses, not two

Full-corpus grep (`turnaround`, `turn-around`, `turn around`, `.tex` and `.md`,
excluding handovers, audits, `founders_voice/`, and `development/`) returns
three distinct referents:

**Sense A — the ZBW mechanism.** The pair's stop-and-reverse at superposition.
R-ARC-CANCEL-TURNAROUND (3134); c04 §343–347; `scr3_eta_z_opening.md` FQ-3.2
and R-ZBW-DELAY; `subpsr_cascade_first_pass.md`; `subpsr_pass2_radial_resolution.md`;
DM reasoning fragments 2470, 2510. This is the load-bearing physics sense.

**Sense B — relativistic trajectory reversal.** The travel twin's mid-journey
course reversal. **Exactly one site:** `series_relativity/papers/phenomena-SR-1.md`
§45 — *"during acceleration phases (outbound, turnaround, return)."*

**Sense C — elapsed project time.** "24-hour turnaround," "reviewer turnaround,"
"same-day-class turnaround." `programme_orientation.md`, `founders_vision.md`,
`templates/operating_system.md`, `templates/reviewer_pause_template.md`,
`PH-OPEN-SS-22*.md`, the CONV-001 flash briefs, `SS-7_v1.2_revision_plan.md`.

## §2 — Sense C is excluded from the audit, deliberately

Sense C is the ordinary English idiom for elapsed time. It shares no context,
no register, and no subject matter with either physics sense, and no reader has
ever been at risk of reading "24-hour turnaround" as a ZBW mechanism. Sweeping
it would generate roughly a dozen edits of pure noise and would degrade the
audit's signal for whoever reads this note next.

**Excluded with prejudice.** Future sweeps should not re-raise it.

## §3 — The R-2.5 recommendation is REVERSED

R-2.5 (Patch 3201 §5) recommended reserving unqualified *turnaround* for the
ZBW mechanism and qualifying the relativistic sense as *trajectory reversal*,
reasoning that the ZBW usage is the one now load-bearing in a ruling.

**On examination that is backwards, and the recommendation is withdrawn.**

*Turnaround* is the standard, universal term for the twin-paradox course
reversal throughout the special-relativity literature. Renaming it inside CPP
papers would be a gratuitous deviation from established usage, would read as
an error to any physicist reviewer, and would buy nothing — the sole Sense B
site is unambiguous in context. A delta audit exists to keep the corpus
consistent with its rulings, not to impose CPP-internal vocabulary on terms
physics already owns.

The correct asymmetry runs the other way: the CPP-internal sense is the one
that should carry qualification, and **it already does everywhere it appears** —
as `R-ARC-CANCEL-TURNAROUND`, as "arc-cancel turnaround," or inside an explicit
ZBW/superposition sentence. No existing site is bare.

## §4 — CONV-023: the convention registered

**Sense B (relativistic).** Unqualified *turnaround* is correct and standard for
trajectory reversal in a relativistic context. **No edit owed; do not "fix" it.**

**Sense A (ZBW mechanism).** Must be qualified on first use in any paper section
— *ZBW turnaround*, *arc-cancel turnaround*, or an explicit
superposition/stop-and-reverse construction. Bare *turnaround* meaning the ZBW
mechanism is not permitted in shipped prose. All current sites already comply.

**Sense C (elapsed time).** Out of scope permanently.

Registered to `frontier_sectors/WORKFLOW.md` as **CONV-023**.

## §5 — R-5 close

Sense A sites: compliant. Sense B sites: 1, correct as written. Sense C: excluded.
**PROSE-LAYER: 0. SUBSTANTIVE: 0.** No fix pass, no panel round.

**Remaining in charter order:** R-1 (CAL-LABEL exposure), then R-3 (fanout /
~10% band citations).
