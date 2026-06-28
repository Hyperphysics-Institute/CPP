# Manual capture-audit run note — 2026-06-28

**Not a macro run.** `Development/audit_log.md` is owned by `overnight_extraction_audit.sh` (macro-only
appends, per its header); this manual audit therefore records its heartbeat here in staging instead.

```
2026-06-28 ~01:30 MDT | run=MANUAL(opus) | source=account-export(Option-B) conv '260625 0865 DM' (93 msgs)
  | scope=founder-contribution | result=GAP:3,PARAPHRASE:3,PARTIAL:2,CAPTURED:1
  | filed=staged-backfill:1(9 entries, all [REVIEW]), audit-report:1 | promoted-to-canonical:0
  | open_review=9 (TLA morning review owns) | notes=manual nightly-equivalent; §3.1 macro not yet built
```

**Owner action (TLA):** review `founders/dm_cross_rod_founders_backfill.md`, approve/edit/reject each of the
9 entries, apply approved entries to `founders_vision.md`, push. Then this staging date can be cleared.
