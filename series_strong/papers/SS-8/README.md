# SS-8 — Per-Paper Subfolder

SS-8 is the first paper to use the per-paper subfolder convention (adopted 22 April 2026 — see `templates/operating_system.md` §11 "Per-paper subfolder convention" and "The three-file documentation-suite convention").

## Layout

```
SS-8/
├── README.md                      ← this file
├── reviews/                       ← verbatim reviewer correspondence (Round 1 + Round 2)
│   └── README.md                  ← catalog of reviews by round/reviewer/target
├── letters/                       ← Claude Opus correspondence (re-review requests, synthesis letters)
├── sketches/                      ← derivation notes, findings, exploratory analyses
├── scripts/                       ← Python verification scripts
├── founders_voice/                ← Thomas's recorded intuitions and organizational decisions
└── documentation_suite/           ← three-file documentation-suite (handover / development / transcript)
    ├── handover-SS-8.md           ← session-continuity state snapshot (next-session orientation)
    ├── development-SS-8.md        ← session-by-session vignettes (append-only, in-moment voice)
    └── transcript-SS-8.md         ← transaction-indexed pointer-map (optional, grows over time)
```

## Current state (22 April 2026)

SS-8 is pre-v0.1 exploratory. Round 2 review has closed with D1 promoted to conditional-theorem tier. OPEN-SS-26 consolidated into OPEN-SS-27. Pattern 6 Position A adopted. Four next-session items queued — see `documentation_suite/handover-SS-8.md` for the authoritative state.

## Entry points for different readers

- **Next Claude session, cold start:** read `documentation_suite/handover-SS-8.md` first. That file names the active state, the queued open items, and the pointers to everything else.
- **Reviewer entering the paper:** read `sketches/SS-8_H2prime_derivation_note.md` and `sketches/SS-8_D1_ssv_minimization_sketch.md`. The Q2 appendix is `sketches/SS-8_D1_Q2_algebraic_reduction_analysis.md`.
- **Future researcher tracing intellectual history:** read `documentation_suite/development-SS-8.md` for session-vignette narrative. Each vignette was written at the time of that session and preserves in-moment thinking, not retrospective framing.
- **Researcher looking for specific reviewer content:** `reviews/README.md` catalogs all reviewer correspondence by round and target.
- **Someone reconstructing ordinal order of transactions:** `documentation_suite/transcript-SS-8.md` (when populated) gives the indexed pointer-map.

## Convention notes

- No files are at the flat `series_strong/papers/` location for SS-8. Everything is inside this subfolder.
- Scripts in `scripts/` assume they are run from the repository root (or from their own folder — they do not rely on external paths).
- `documentation_suite/` contains three session-continuity files plus (progressively, from v0.1 forward) the seven-file documentation companion suite (`mechanism-SS-8.md`, `glossary-SS-8.md`, `phenomena-SS-8.md`, `philosophy-SS-8.md`, `reviews-SS-8.md`, `keywords-SS-8.md`, `FAQ-SS-8.md`). Companion suite files are written progressively during paper development, not heroically at v1.0.
- There is no crystallization point. v1.0 is a milestone of external-readiness, not finality. Post-OSF-registration revisions (reader feedback, public critique, programme-level discoveries) update these same files.

## Migration history

SS-8 was in active development when the per-paper subfolder convention was introduced. The full migration of flat files to subfolder layout was completed on 22 April 2026 in a single commit. All cross-references were updated at migration time. The `development-SS-8.md` file at the flat location was renamed to `documentation_suite/handover-SS-8.md` to reflect its actual role (session-continuity state, not retrospective narrative).
