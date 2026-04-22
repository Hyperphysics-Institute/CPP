# SS-8 — Per-Paper Subfolder

SS-8 is the first paper to use the per-paper subfolder convention (adopted 22 April 2026 — see `templates/operating_system.md` §11 "Per-paper subfolder convention").

## Current layout

```
SS-8/
├── README.md              ← this file
├── reviews/               ← verbatim reviewer correspondence (Round 1 + Round 2)
├── letters/               ← Claude Opus correspondence (synthesis letters, re-review requests)
├── sketches/              ← derivation notes, findings docs, exploratory analyses
├── scripts/               ← Python verification scripts
└── founders_voice/        ← Thomas's recorded intuitions, organizational notes, decisions
```

Subfolders are created lazily — only when they have content.

## Transition notes

SS-8 was in active development when the subfolder convention was introduced. During the transition period, the canonical SS-8 artefacts (paper, H2′ note, development transcript, sketches, Round 2 request, synthesis letter, scripts) remain at the flat location `series_strong/papers/` and are referenced from bootup.md §8.5 at those locations.

The per-paper subfolder initially contains:

- **`reviews/`** — the 10-file verbatim reviewer archive (4 Round 1 + 6 Round 2), per the context-pressure preservation checklist's requirement that reviewer content be committed in full verbatim form.
- **`README.md`** — this file.

Over time, new SS-8 artefacts (letters, sketches, scripts, founder's voice entries) will land in the appropriate subfolder rather than in the flat `series_strong/papers/` directory. Older SS-8 artefacts may be migrated during a later cleanup pass; they are not migrated automatically because (a) the Round 2 review request letter already references them at their flat paths, and (b) `development-SS-8.md` is referenced from bootup.md §8.5 at the flat path.

## Related documents

- `../development-SS-8.md` — curated development transcript (canonical narrative record; at flat location pending migration)
- `../SS-8_H2prime_derivation_note.md` — H2′ derivation note
- `../SS-8_D1_ssv_minimization_sketch.md` — D1 SSV-minimization sketch
- `../SS-8_D1_Q2_algebraic_reduction_analysis.md` — Q2 algebraic reduction appendix
- `../SS-8_Round2_review_request.md` — Round 2 review request letter
- `../SS-8_Round2_synthesis_letter.md` — Round 2 synthesis letter
- `../SS-8_Phase1_extended_map_findings.md` — Phase 1b empirical substrate
