# `flagship_papers/neutrinos/sketches/` — SF-4 Staging Documents

**Purpose:** Working documents that develop subsidiary derivations for SF-4 (Neutrino Sector Unification flagship paper) before they are integrated into the main `.tex` source. This folder follows the SS-9 sketches → development → paper-text staging discipline, imported for the flagship-paper line.

## Why staging exists

A flagship-paper-class derivation is not produced in one pass. Substantive sub-derivations — the neutrino sector mechanism selection, the K3-eigenstructure preservation argument, the suppression-factor first-principles closure, individual section drafts — benefit from working out in standalone documents first, then being integrated when mature. This protects the main paper from absorbing partially-formed material; it also produces a richer artifact trail that an external evaluator can follow if they want to see how the conclusions were reached.

Per Thomas's working framing: the sketches are open-source and effectively part of the paper. They are not drafts of the paper text; they are the substance behind it. A reader who wants to verify the conclusions can read the .tex; a reader who wants to see the development path can read the sketches.

## Convention

Sketches in this SF-4 folder are named `SF-4_{topic}.md`. The original Q1-numbered audit document migrated from the prior `flagship_papers/hierarchy_problem/sketches/` location at patch 0295; "Q1" was the open-question number from the original Track-1 hierarchy paper outline, which dissolved into SF-4 under the Option-3 architecture.

Once a sketch's content lands in the main paper text, the sketch stays in this folder as a development artifact. It is not deleted. It may be marked at the top with an "INTEGRATED into §N of paper at v0.x" header.

## Status table

| File | Status | Integration target | Sessions |
|------|--------|--------------------|----------|
| `SF-4_neutrino_sector_audit.md` | COMPLETE — audit phase | Foundation document for SF-4; mechanism-selection input | Session 37 (audit) |
| `SF-4_mechanism_selected.md` | TBD | Records mechanism choice for §3-§5 of SF-4 paper | Session 39 (selection) |
| `SF-4_*.md` (subsequent) | Per derivation campaign needs | §-specific derivation work | Sessions 40+ |

## Same discipline applies in any flagship-paper sketches folder

The discipline is generic — sketches → development → paper-text staging applies to any `flagship_papers/SF-N/sketches/` folder when SF-1, SF-2, SF-3, SF-5 begin substantive work. Each will have its own `sketches/README.md` reflecting the specific paper's content.

---

*Subfolder migrated from `flagship_papers/hierarchy_problem/sketches/` to `flagship_papers/neutrinos/sketches/` at Session 38 (patch 0295) per Option-3 architecture adoption. Discipline imported from SS-9 working pattern (`series_strong/papers/SS-9/sketches/`).*
