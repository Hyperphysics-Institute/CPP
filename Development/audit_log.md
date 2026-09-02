# Audit heartbeat log

The nightly extraction audit (`scripts/overnight_extraction_audit.sh`) appends
**exactly one dated line per run** below. This log is the anti-silent-rot rail:
**a missing line for the previous night is a LOUD, blocking flag at the next
bootup** — not a silent gap. The audit stopping unnoticed is the exact failure
that killed the old systems; this log is the guard against it.

## Heartbeat line format (the macro and the bootup-check both depend on this)

```
<YYYY-MM-DD> <HH:MM> <TZ> | run=<OK|DRY-RUN|FAIL> | transcripts=<n> | filed=reasoning:<n>,scripts:<n>,registry:<n> | founders=staged:<n>,review:<n>,promoted:<n> | notes=<free text>
```

- Line starts with the run **date**, so "did last night run?" is a trivial
  date-grep at bootup.
- `run=FAIL` lines are still written when the macro reaches its error handler —
  a written FAIL is recoverable; a *missing* line is the loud case.
- `founders=` counts the founder's-voice path: `staged` (diff staged for TLA),
  `review` (`[REVIEW]`-flagged, ambiguous), `promoted` (written — only once the
  path graduates from staged-first to auto, protocol §4).

## Bootup check (for all windows)

At bootup, confirm a heartbeat line exists for the previous calendar day. If it
is missing, surface it as a BLOCKING flag and investigate before proceeding —
the nightly audit may have failed to run.

---

## Runs

*SCAFFOLDED at Patch 2103 — no audit has run yet.* The first heartbeat line will
be appended when `scripts/overnight_extraction_audit.sh` first runs (built in
Step 4, Patch 2104+). Do not hand-write run lines here; only the macro appends.
2026-06-24 10:42 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-06-25 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-06-26 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-07-07 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-07-08 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-07-09 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-08-17 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-08-18 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-08-19 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-08-20 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-08-21 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-08-22 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-08-23 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-08-24 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-08-25 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-08-26 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-08-28 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-08-29 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-08-30 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-08-31 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-09-01 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
2026-09-02 03:00 MDT | run=OK | transcripts=0(malformed:0,orphan-deltas:0) | filed=reasoning:0,scripts:0,registry:0 | founders=staged:0,review:0,promoted:0 | temp_handles=seen:0,perm:0,alias:0,review:0 | open_review=0 | freeform_pending=0 | notes=v1-deterministic
