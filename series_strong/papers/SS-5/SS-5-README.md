# SS-5 — Per-Paper Subfolder

SS-5 (Light-Nuclei Binding Energies from the Open-Vertex Cascade) was migrated to the per-paper subfolder convention on 25 April 2026 (patch 0019, OPEN-ORG-004 partial completion). Original location: flat at `series_strong/papers/`.

## Layout

```
SS-5/
├── SS-5-README.md                                          ← this file
├── SS-5_light_nuclei_open_vertex_cascade.tex               ← canonical .tex (v6)
├── SS-5_light_nuclei_open_vertex_cascade.pdf               ← compiled PDF
├── reviews/                                                ← verbatim reviewer correspondence (empty; reviews live in reviews-SS-5.md)
├── letters/                                                ← Claude Opus correspondence (empty for SS-5)
├── sketches/                                               ← derivation notes, exploratory analyses (empty)
├── scripts/                                                ← Python verification scripts (empty)
├── founders_voice/
│   └── SS-5_session_bootup_prompt.md                       ← Thomas's documented session-start intent for SS-5 drafting
└── documentation_suite/                                    ← 8 files (7 doc-suite + 1 lab-notebook trio member)
    ├── development-SS-5.md                                 ← lab-notebook narrative + doc-suite development history (single artifact, dual purpose)
    ├── glossary-SS-5.md
    ├── keywords-SS-5.md
    ├── mechanism-SS-5.md
    ├── phenomena-SS-5.md
    ├── philosophy-SS-5.md
    ├── reviews-SS-5.md
    └── transcript-SS-5.md                                  ← multi-session transcript (renamed from SS-5_development_transcript.md to match SS-8 convention)
```

Empty subfolders carry `.gitkeep` placeholders. The lab-notebook trio's `handover-SS-5.md` does not currently exist; per `templates/operating_system.md` §15 it would be created at the next substantive session-close on SS-5 if any future work is done. SS-5 is currently at v6 (publication-ready, 18 April 2026); no active work is in flight.

## Status

**Paper version:** v6 (polished) — 18 April 2026 header. Publication-ready, 19 pages, 15 bibliography entries all cited, clean compile, OSF pending (awaiting Grok numerical + Sonnet hostile review per `paper_catalog.md`).

**Doc-suite completeness:** 7 of 7 canonical doc-suite files present at v6 header currency. `reviews-SS-5.md` has its review-status table updated to v6, but body sections for v4 stress-test and Copilot review still pending per `paper_catalog.md` notes.

**Migration notes:** This subfolder migration moved 19 files. Eight of those were pre-§11-convention versioned drafts (`_v1`/`_v2`/`_v3`/`_v4`, .tex + .pdf each) which were archived to `archive/SS-5_versioned_drafts/` rather than being brought into the new structure, per the §11 "ONE file per paper, overwritten with each revision; git history preserves all versions" rule. The canonical .tex file at v6 is the one that lives here; earlier v1–v4 drafts are preserved in archive for historical audit.

## Migration cross-reference

| Original location (flat) | New location |
|---|---|
| `series_strong/papers/SS-5_light_nuclei_open_vertex_cascade.tex` | `series_strong/papers/SS-5/SS-5_light_nuclei_open_vertex_cascade.tex` |
| `series_strong/papers/SS-5_light_nuclei_open_vertex_cascade.pdf` | `series_strong/papers/SS-5/SS-5_light_nuclei_open_vertex_cascade.pdf` |
| `series_strong/papers/development-SS-5.md` | `series_strong/papers/SS-5/documentation_suite/development-SS-5.md` |
| `series_strong/papers/glossary-SS-5.md` | `series_strong/papers/SS-5/documentation_suite/glossary-SS-5.md` |
| `series_strong/papers/keywords-SS-5.md` | `series_strong/papers/SS-5/documentation_suite/keywords-SS-5.md` |
| `series_strong/papers/mechanism-SS-5.md` | `series_strong/papers/SS-5/documentation_suite/mechanism-SS-5.md` |
| `series_strong/papers/phenomena-SS-5.md` | `series_strong/papers/SS-5/documentation_suite/phenomena-SS-5.md` |
| `series_strong/papers/philosophy-SS-5.md` | `series_strong/papers/SS-5/documentation_suite/philosophy-SS-5.md` |
| `series_strong/papers/reviews-SS-5.md` | `series_strong/papers/SS-5/documentation_suite/reviews-SS-5.md` |
| `series_strong/papers/SS-5_development_transcript.md` | `series_strong/papers/SS-5/documentation_suite/transcript-SS-5.md` (renamed to match `[type]-[S]-[N].md` convention) |
| `series_strong/papers/SS-5_session_bootup_prompt.md` | `series_strong/papers/SS-5/founders_voice/SS-5_session_bootup_prompt.md` |
| `series_strong/papers/SS-5_light_nuclei_open_vertex_cascade_v1.tex/.pdf` | `archive/SS-5_versioned_drafts/SS-5_light_nuclei_open_vertex_cascade_v1.tex/.pdf` |
| `series_strong/papers/SS-5_light_nuclei_open_vertex_cascade_v2.tex/.pdf` | `archive/SS-5_versioned_drafts/SS-5_light_nuclei_open_vertex_cascade_v2.tex/.pdf` |
| `series_strong/papers/SS-5_light_nuclei_open_vertex_cascade_v3.tex/.pdf` | `archive/SS-5_versioned_drafts/SS-5_light_nuclei_open_vertex_cascade_v3.tex/.pdf` |
| `series_strong/papers/SS-5_light_nuclei_open_vertex_cascade_v4.tex/.pdf` | `archive/SS-5_versioned_drafts/SS-5_light_nuclei_open_vertex_cascade_v4.tex/.pdf` |

The canonical .tex uses an embedded `\begin{thebibliography}` block (no external `.bib` reference) — moving it did not require any path-update inside the .tex file. The v4 archived copy is the one exception in the version family: it uses `\bibliography{../../bibliography/cpp_references}`. After archive relocation the relative path changes (now `archive/SS-5_versioned_drafts/_v4.tex` is one level deep, so `../../` resolves differently), but archived .tex files are not expected to compile — they are historical artifacts. No fix attempted.

## Convention reference

This subfolder structure follows `templates/operating_system.md` §11 "Per-paper subfolder convention" and the `{scope}-README.md` convention codified in the same §11 location (patch 0017). The `documentation_suite/` folder uses the unified convention codified in `templates/documentation-suite.md` §"Folder Location" (patch 0015).
