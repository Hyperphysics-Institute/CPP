# Documentation-suite / paper-production-protocol — consolidation map  [PROPOSAL — for TLA direction]

**Not a rewrite.** This is a planning map produced overnight from a read of the existing protocol docs +
tonight's capture audit. Canonical protocol docs are untouched. It exists so you can point me at the right
piece in the morning rather than my guessing scope.

## A. What already exists (the protocol suite — canonical, do not duplicate)

| Doc | Role |
|---|---|
| `templates/capture_and_audit_protocol.md` | The verbatim-capture + nightly-extraction inversion. **CANONICAL but NOT OPERATIONAL** — see B. |
| `templates/reasoning_capture_protocol.md` | The per-patch capture contract (.tex + reasoning fragment + verify script + founder block). Live. |
| `templates/review_dispatch_protocol.md` | CONV-001 panel dispatch (the single-block form we used all session). |
| `templates/project_tracking_protocol.md` | The per-patch development ledger. |
| `templates/new_window_protocol.md` / `anticollision_protocol.md` | Multi-window bootup + collision avoidance. |
| `templates/collaborator_protocol.md` / `relationship_protocol.md` | Contribution mode + working relationship. |
| `templates/paper_completion_checklist.md` | The atomic task list a paper clears to ship. |
| `operating_system.md`, `frontier_sectors/WORKFLOW.md` | The governing OS + the workflow registry. |

These cover the **paper-production protocol** well. The consolidation need is not new protocol text — it is
(1) closing the one operational gap, (2) a single index that ties the pieces together, and (3) finishing the
per-paper suites the protocol calls for.

## B. The operational gap (the load-bearing one)

`capture_and_audit_protocol.md` is ratified but **not operational**: its §3.1 always-on automatic-capture
mechanism and its Step-4 nightly macro (`scripts/overnight_extraction_audit.sh`) are **not built**. Until they
are, the protocol's guarantee is aspirational and the root cause reappears one layer down — which is exactly
what tonight's audit found: under load, the founder's *words* dropped even though the per-patch block caught
the *fact* of the contribution (3 GAP / 3 PARAPHRASE across the Cross-Rod campaign). **This is the highest-
leverage item; it is also a build task that likely wants Isak** (technical director), not a prose patch.

## C. The per-paper suite gap (bounded; I can do this)

The protocol calls for a per-paper `documentation_suite/`. A mature one (SF-3) has ~10 files
(changelog, development, glossary, keywords, mechanism, phenomena, philosophy, reasoning, reviews, transcript).
**DM-1 v1.0 just shipped with only `changelog-DM-1.md`.** Also: the `reviews-DM-1.md` I wrote at ship (Patch
0889) landed in `dark_matter/documentation_suite/` but the DM-1 header points at `DM-1/documentation_suite/` —
**one path to reconcile.**

## D. Proposed work, prioritized (your call on order/scope)

1. **[TLA] Promote the staged founder backfill** — review `founders/dm_cross_rod_founders_backfill.md`
   (9 verbatim entries), apply the approved ones to `founders_vision.md`, push. Closes the audit's open loop.
2. **[Opus, bounded] Complete the DM-1 v1.0 documentation_suite** — draft the ~9 missing suite files from the
   campaign material I already hold (reasoning fragments 0860–0889, the paper, the reviews, the memo), and
   reconcile the `reviews-DM-1.md` path. This is the cleanest next thing I can do well unattended.
3. **[Opus, bounded] A paper-production-protocol INDEX** — one short doc that ties A's pieces into a single
   read-order ("at patch-time do X; at panel-time do Y; at ship do Z; nightly the audit does W"), pointing to
   each canonical doc rather than restating it. Removes the "which protocol governs this step?" friction.
4. **[Isak/build] The capture-and-audit macro (B)** — the §3.1 capture hook + `overnight_extraction_audit.sh`.
   The operational gap. Out of my lane (a scheduled local build), but I can write the spec/acceptance tests.
5. **[Opus, until 4 lands] Export-based capture audit at each campaign close** — repeat tonight's manual audit
   whenever a campaign wraps, while the export still holds the window. Cheap insurance until the macro exists.

**My recommendation if you just say "go":** #2 then #3 — finish DM-1's suite while the campaign is fresh, then
write the index — and leave #1 (yours) and #4 (Isak's) for when you're at the keyboard.
