# `flagship_papers/hierarchy_problem/sketches/` — Staging Documents

**Purpose:** Working documents that develop subsidiary derivations for the Track 1 hierarchy paper before they are integrated into the main `.tex` source. This folder follows the SS-9 sketches → development → paper-text staging discipline.

## Why staging exists

A flagship-paper-class derivation is not produced in one pass. Substantive sub-derivations — the neutrino sector mechanism, the Q3 calibration honesty story, individual section drafts — benefit from working out in standalone documents first, then being integrated when mature. This protects the main paper from absorbing partially-formed material; it also produces a richer artifact trail that an external evaluator can follow if they want to see how the conclusions were reached.

Per Thomas's working framing: the sketches are open-source and effectively part of the paper. They are not drafts of the paper text; they are the substance behind it. A reader who wants to verify the conclusions can read the .tex; a reader who wants to see the development path can read the sketches.

## Convention

Sketches are named `SS-Q{N}_{topic}.md` where Q{N} corresponds to the open-question number from `../hierarchy_paper_outline.md` (Q1 = neutrino mechanism, Q2 = conditional-theorem inheritance, Q3 = $M_0$/$m_e$ calibration honesty, Q4 = headline number). Sub-derivations not tied to a specific open question are named `SS-{topic}.md`.

Once a sketch's content lands in the main paper text, the sketch stays in this folder as a development artifact. It is not deleted. It may be marked at the top with a "INTEGRATED into §N of paper at v0.x" header.

## Status table

| File | Status | Integration target | Sessions |
|------|--------|--------------------|----------|
| `SS-Q1_neutrino_sector_audit.md` | ACTIVE — audit phase | §8 (neutrino sector) of hierarchy paper, OR companion neutrino flagship paper depending on architectural decision | Session 37 (audit) → 38 (mechanism selection) → 39+ (derivation) |

---

*Subfolder established at Session 37 (patch 0294) per audit-session output. Discipline imported from SS-9 working pattern (`series_strong/papers/SS-9/sketches/`).*
