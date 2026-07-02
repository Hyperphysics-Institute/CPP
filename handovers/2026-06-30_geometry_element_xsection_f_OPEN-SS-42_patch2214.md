# HANDOVER — Strong/geometry lane: derive f from the DM element cross-section (OPEN-SS-42) — the derivation that settles the dwarf branch
**Date:** 2026-06-30 · **Opening patch:** **2214** (2200-series; strong/geometry, SS-2 / element-structure) · **From:** Opus (DM 18xx lane, OPEN-SS-42 registrant + consumer) · **Registered target:** **OPEN-SS-42** (`frontier_sectors/SS.md`).

## ⛔ CLONE GATE
```
cd ~/Documents/GitHub/CPP && git pull --rebase origin main && git log --oneline -8
```
Confirm HEAD includes **2212/2213** (OPEN-SS-41a partial close: n* pinned, f not), DM **1853** (consumption), and DM **1854** (OPEN-SS-42 registered). Begin at **patch 2214**; grep before reserving sub-IDs.

## ORIENTATION — the one derivation that settles the dwarf branch
OPEN-SS-41a pinned **n\* ~ 2–4** but **f did not pin** (2212): f = (exposed-core spine-face solid angle)/4π needs
the DM element cross-section *shape*, which the corpus has only qualitatively. With n* pinned, the window wants
**f ~ 0.04–0.11**, but the plausible exposed-core range **f ~ 0.05–0.20 reaches both kill bands** — so this calc
**genuinely decides window-vs-kill**, it is not a formality. The founder has set the sequence: **derive f, present
the panel the full package** (cluster branch = parameter-free prediction; dwarf branch = settled — a pinned
prediction *or* a clean kill), then refine on the panel's objections. **Panel round 2 is held until f lands.**

## THE ASK (strong/geometry lane, patch 2214+) — OPEN-SS-42
**Derive f = (exposed-core spine-face solid angle)/4π from the 8qCP+8eCP element cross-section on the 600-cell /
tetrahedral-cage substrate.** Make quantitative what the corpus has qualitatively:
1. **The 8qCP core polyhedron** — the shape of the color core (ℓ_el ~ 2 fm, r₀ ~ 0.26 fm).
2. **The eCP-coat corner coverage** — how the coat buffers/screens the core, and which core faces it leaves exposed.
3. **The axial E_qq spine face** — which face presents the spine for a *correct* ordered axial bond, and its
   solid angle as a fraction of 4π. That fraction is **f**.
Then ΔG*_nuc = (n*−1)·|ln f|·kT_form (n* ~ 2–4 from OPEN-SS-41a) is pinned.

## BANDS (from OPEN-SS-42)
- **Win (pinned prediction):** f giving **ΔG*_nuc ∈ [6.0, 6.9] kT_form** (with n* ~ 2–4, f ~ 0.04–0.11) ⇒ N_form ~
  400–1000 ⇒ dwarf normalization a zero-parameter prediction.
- **Kill (clean):** f giving ΔG*_nuc ≲ 4 kT (under-cored) or ≳ 9 kT (over-cored). Either is a legitimate,
  presentable outcome — a clean kill of the dwarf branch. **Cluster σ/m ∝ 1/v² stands regardless.**

## LANE BOUNDARY
- **Strong/geometry owes:** f from the element cross-section → pinned ΔG*_nuc → the settled dwarf verdict. Register
  under 2214+, update OPEN-SS-42 (and OPEN-SS-41a/41). This is **SS-2 / element-structure** — it may draw on or
  feed the SS-2 lattice-scale nucleon kit; scope that as you see fit, but the DM deliverable is just f.
- **DM consumes:** pinned ΔG*_nuc → ε_nuc = exp(−ΔG*_nuc/kT) → N_form → dwarf σ/m(v). **Then** DM assembles the
  full package and the founder runs panel round 2.
- Cross-link OPEN-SS-41a (parent purpose) + SS-2. Distinct from OPEN-FP-SF-2-η.

## POINTERS
- `flagship_papers/strong/reasoning/2212.md` + `code/2212_fnstar_pin_dGnuc.py` (n* pinning; the f-window
  requirement f ~ 0.04–0.11; why f isn't derivable from the corpus yet; the bracket reaching both kills).
- `reasoning/1842.md` (the qualitative 8qCP+8eCP element structure + coat buffering). **OPEN-SS-42 / OPEN-SS-41a /
  OPEN-SS-41** (`frontier_sectors/SS.md`). `reasoning/1853.md` (DM consumption + the full-package sequence).
- SS-2 (lattice-scale nucleon structure) — the element-geometry kit this likely builds on.

## SUGGESTED SEQUENCE
Fix the 8qCP core polyhedron and the eCP-coat coverage on the substrate → the exposed spine-face solid angle → f.
Combine with n* → pinned ΔG*_nuc; compare to [6.0, 6.9] kT; hand the verdict (prediction or clean kill) back to DM.
That completes the package for panel round 2. The cluster branch is the parameter-free headline throughout; f
decides only whether the dwarf branch joins it as a prediction or resolves as a clean kill.
