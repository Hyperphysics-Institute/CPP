# Reasoning capture — Patch 2107: paper-production protocol — parallel-window registry discipline

**STATUS: verbatim (captured at-patch).** Window: 2100-band. Opus worker; integrator = TLA.

Modified the Paper Production Protocol so parallel windows can ship papers without colliding on shared registries.
Driven by TLA's observation that paper production is where the capture-and-audit protocol meets real collision
risk, and his decision to route the deliberate registry edits through the pending/overnight-merge path.

What I found (grounded in the actual protocol): the completion checklist already splits Phase 7 into **7A
(paper-level, in the paper's own subfolder)** and **7B (programme-level, repo-root shared files)**, and that
split IS the collision line. 7B (C1–C10, C12, D1) + the shared-file 7A items (C11 bibliography, D2 INDEX.md,
D3 series-README) edit shared repo-root registries every paper touches → two same-day ships collide. Everything
paper-local never collides. Notably the checklist already flags 7B as the **dropout**-prone set (4 flagship
SHIPs drifted); so the collision-prone set and the dropout-prone set are the same set — which is exactly why
routing it through the capture-and-audit overnight merge solves both at once with no new scope.

Edits (all DRAFT, pending Capture-and-Audit ratification; until then continue in-session edits):
- `operating_system.md` §4: new "Parallel-window registry discipline" subsection — the clean line (shared
  repo-root file → defer to `Registries_pending/<slug>.md`; paper's own subfolder → in-session unchanged), the
  precise-delta rule, the overnight merge, the read-render for same-day visibility + ID allocation, and the
  "what is unchanged" statement (the ~dozen shared edits defer; everything else identical).
- `operating_system.md` §4 Phase 5: pointer line to the new subsection.
- `paper_completion_checklist.md`: parallel-window collision-discipline note in the 7A/7B section.

Design decisions (TLA-ratified in-session):
- **Append-to-shared is NOT collision-free in a git/patch workflow** (two windows' patches both modifying one
  shared file = merge conflict, the 2B problem). The safe form is append to a **write-partitioned per-window**
  pending file — TLA's append idea + per-window partitioning.
- **Judgment stays in-session; only the write-to-canonical defers.** The window decides the precise delta while
  context is fresh and writes that exact instruction to its pending file — NOT reconstructed from prose by the
  macro. This is why the deliberate paper-production case justifies a scoped pending area where the general
  incidental-delta case did not.
- **ID-allocation hazard** (two windows grabbing the same THEO/PRED ID before the overnight merge) is closed by
  the read-render: read canonical AND glob `Registries_pending/*.md` before allocating. This is the read-only
  render the protocol §8 anticipated, now realized.

NO THEO. Owned this patch: edits to `templates/operating_system.md`, `templates/paper_completion_checklist.md`;
this fragment. No status move; no registry value changed; DRAFT until Capture-and-Audit ratified.
Next: 2108 — the Capture-and-Audit revision (panel change set + T3-middle + scope boundary + the
`Registries_pending/` mechanism this patch consumes).

Track: WORKFLOW
