# Transcript Pointer-Map — SF-3: The Quark Sector from 600-Cell Geometry

**Tier 2.** Transaction-level index of SF-3's development. Each row: patch ID +
date + one-liner + pointer to the artifact. This is the canonical sequence of
events and the navigation index for the Tier-3 development file, the Tier-4
reasoning file, and the changelog. SF-3 window = 1500-patch band, Session 161.

| Patch | Date | Transaction | Pointer |
|-------|------|-------------|---------|
| 1303 | 2026-06 | SF-3 outline drafted (window bootstrap) | `sf-3_outline.md` |
| 1308 | 2026-06 | Structural-core sketch | `sketches/SF-3_structural_core.md` |
| 1500 | 2026-06-14 | v0.1 `.tex` assembly (initially mislabeled v1.0) | `sf-3_quarks.tex` |
| 1501 | 2026-06-14 | Relabel v1.0 → v0.1 (pre-review drafts are v0.x) | `sf-3_quarks.tex` title block |
| 1502 | 2026-06-14 | v0.1 → v0.2: round-1 review incorporation | `review/sf-3_v0.1_review_*.md`; `changelog-sf-3.md` |
| 1503 | 2026-06-14 | v0.2 → v0.3: round-2 review incorporation | `review/sf-3_v0.2_review_*.md`; `changelog-sf-3.md` |
| 1504 | 2026-06-14 | v0.3 → v0.4: round-3 over-claim tightening | `review/sf-3_v0.3_review_*.md`; `changelog-sf-3.md` |
| 1505 | 2026-06-14 | **v0.4 → v1.0 SHIP**: round-4 final items + version bump | `sf-3_quarks.tex`; `review/sf-3_v0.4_review_*.md`; `changelog-sf-3.md`; `reasoning-SF-3.md` |
| 1506 | 2026-06-14 | Ship-time registry integration (OPEN-FP-3-CKM, predictions, catalog, README, INDEX, bib) | `frontier_sectors/FP.md`; `predictions.md`; `paper_catalog.md`; `README.md`; `INDEX.md`; `bibliography/cpp_references.bib` |
| 1507 | 2026-06-14 | Phase 7A documentation suite (7 companion files + this map) | `documentation_suite/*` |

## Verification transactions

| Artifact | Purpose | Status |
|----------|---------|--------|
| `code/1500_verify_sf3_core.py` | Reproduces the four masses, `M_0`, `α_s`, complementarity, Koide phase | ALL CHECKS PASS |

## Review-round index

| Round | Version | Files |
|-------|---------|-------|
| 1 | v0.1 | `review/sf-3_v0.1_review_chatgpt.md`, `_grok.md`, `_copilot.md` |
| 2 | v0.2 | `review/sf-3_v0.2_review_chatgpt.md`, `_grok.md`, `_copilot.md` |
| 3 | v0.3 | `review/sf-3_v0.3_review_chatgpt.md`, `_grok.md`, `_copilot.md` |
| 4 | v0.4 | `review/sf-3_v0.4_review_grok.md`, `_adversarial.md` |

## Key decision pointers (for the dramatic arc / anthology chapter)

- **Route adjudication** (Route A canonical, `m_c` demoted) — `sf-3_quarks.tex` §7;
  `development-SF-3.md` Decision 1; `reasoning-SF-3.md`.
- **Proposition 5.1** (phase–mass bookkeeping separation) — `sf-3_quarks.tex` §5;
  `mechanism-SF-3.md` Mechanism 4; `philosophy-SF-3.md` Honest Assessment.
- **OPEN-FP-3-CKM registration** — `sf-3_quarks.tex` §8; `frontier_sectors/FP.md`.
- **The v0.4 α_s-structural catch** — `reviews-SF-3.md` Critical Review;
  `reasoning-SF-3.md` Patch 1505 entry.
