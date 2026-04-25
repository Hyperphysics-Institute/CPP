# SS-6 — Per-Paper Subfolder

SS-6 (Deuteron Observables Beyond Binding: Scope and Limits of the Base-to-Base Picture) was migrated to the per-paper subfolder convention on 25 April 2026 (patch 0018, OPEN-ORG-004 partial completion). Original location: flat at `series_strong/papers/`.

## Layout

```
SS-6/
├── SS-6-README.md                                       ← this file
├── SS-6_deuteron_observables_beyond_binding.tex         ← canonical .tex (v0.2)
├── SS-6_deuteron_observables_beyond_binding.pdf         ← compiled PDF
├── reviews/                                             ← verbatim reviewer correspondence (empty pre-v1.0)
├── letters/                                             ← Claude Opus correspondence
│   └── SS-6_v02_copilot_review_response.md              ← response to Copilot Round 1 review of v0.2
├── sketches/                                            ← derivation notes, exploratory analyses (empty)
├── scripts/                                             ← Python verification scripts (empty)
├── founders_voice/                                      ← Thomas's recorded intuitions (empty)
└── documentation_suite/                                 ← 7-file doc-suite + lab-notebook trio (created at v1.0)
```

Empty subfolders carry `.gitkeep` placeholders. The `documentation_suite/` directory will be populated when SS-6 reaches v1.0 (currently at v0.2 scoping draft).

## Status

**Paper version:** v0.2 (19 April 2026 header). Scoping draft. Round 1 Copilot review received and response drafted (in `letters/`); Round 1 ChatGPT review response is referenced in the Copilot response but the file does not appear to exist in the repository (gap to address at v1.0 production).

**Next steps:** v0.3 polishing per Copilot Round 1 dispositions, then v1.0 with full documentation suite.

## Migration notes

This subfolder migration moved 3 files from flat `series_strong/papers/` into this structure:

| Original location | New location |
|---|---|
| `series_strong/papers/SS-6_deuteron_observables_beyond_binding.tex` | `series_strong/papers/SS-6/SS-6_deuteron_observables_beyond_binding.tex` |
| `series_strong/papers/SS-6_deuteron_observables_beyond_binding.pdf` | `series_strong/papers/SS-6/SS-6_deuteron_observables_beyond_binding.pdf` |
| `series_strong/papers/SS-6_v02_copilot_review_response.md` | `series_strong/papers/SS-6/letters/SS-6_v02_copilot_review_response.md` |

Cross-references in `INDEX.md`, `paper_catalog.md`, and any other root-level documentation were updated as part of this patch. No internal `\input` or `\includegraphics` references existed in the .tex file (paper is self-contained), so the migration did not require any LaTeX-internal path updates.

## Convention reference

This subfolder structure follows `templates/operating_system.md` §11 "Per-paper subfolder convention" (adopted 22 April 2026, codified in §11 by patch 0009/0017). The README filename uses the `{scope}-README.md` convention codified in the same §11 location.
