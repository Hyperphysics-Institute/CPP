# SS-5 Versioned Drafts Archive

Historical SS-5 paper drafts (v1 through v4) preserved here per the `templates/operating_system.md` §11 rule: "ONE file per paper, overwritten with each revision; Git history preserves all versions." Until 22 April 2026, SS-5 had been kept as multiple side-by-side `_v1`/`_v2`/`_v3`/`_v4` files alongside the canonical (v5/v6) file in `series_strong/papers/`. The §11 convention adopted 22 April 2026 normalized the rule going forward; SS-5's pre-existing versioned copies were archived here on 25 April 2026 (patch 0019) when SS-5 was migrated to its per-paper subfolder.

## Contents

| File | Header version | Date | Notes |
|---|---|---|---|
| `SS-5_light_nuclei_open_vertex_cascade_v1.tex/.pdf` | (early) | pre-17 Apr 2026 | First-pass draft |
| `SS-5_light_nuclei_open_vertex_cascade_v2.tex/.pdf` | (intermediate) | mid-development | |
| `SS-5_light_nuclei_open_vertex_cascade_v3.tex/.pdf` | (intermediate) | mid-development | |
| `SS-5_light_nuclei_open_vertex_cascade_v4.tex/.pdf` | "Version 1.0" — 17 April 2026 | 17 Apr 2026 | Uses external `\bibliography{../../bibliography/cpp_references}` reference; remaining copies use embedded `\begin{thebibliography}`. After the archive move the relative path no longer resolves, but archived files are not expected to compile. |

The canonical SS-5 paper (v6, 18 April 2026) lives at `series_strong/papers/SS-5/SS-5_light_nuclei_open_vertex_cascade.tex` and is the publication-ready version. These archived versions are preserved for historical audit only.

## Reference

- `series_strong/papers/SS-5/SS-5-README.md` — current SS-5 paper folder
- `templates/operating_system.md` §11 — single-file-per-paper convention
- `series_strong/papers/SS-5/documentation_suite/development-SS-5.md` — narrative of the v1→v6 development arc
- `series_strong/papers/SS-5/documentation_suite/transcript-SS-5.md` — multi-session transcript covering "v0.1 → v1 → v2 → v3/v0.2 → v4 → v5 → v6 (current)"
