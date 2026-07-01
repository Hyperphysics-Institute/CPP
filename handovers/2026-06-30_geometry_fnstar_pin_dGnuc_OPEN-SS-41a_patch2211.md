# HANDOVER — Strong/geometry lane: pin (f, n*) → ΔG*_nuc (OPEN-SS-41a) — the dwarf-branch last-mile
**Date:** 2026-06-30 · **Opening patch:** **2211** (2200-series; strong/geometry, SS-2-adjacent) · **From:** Opus (DM 18xx lane, OPEN-SS-41a registrant + consumer) · **Registered target:** **OPEN-SS-41a** (`frontier_sectors/SS.md`).

## ⛔ CLONE GATE
```
cd ~/Documents/GitHub/CPP && git pull --rebase origin main && git log --oneline -8
```
Confirm HEAD includes **2210** (OPEN-SS-41 first pass), DM **1851** (consumption), and DM **1852** (OPEN-SS-41a registered). Begin at **patch 2211**; grep before reserving sub-IDs.

## ORIENTATION — the single input that pins the dwarf branch
OPEN-SS-41 first pass (2209/2210) found ΔG*_nuc = (n*−1)·|ln f|·kT_form is a **configurational-selectivity** barrier
whose natural value **brackets** the 6.0–6.9 kT window (most-natural reading n* ~ 4, f ~ 0.11 in-window) — the dwarf
branch is **reachable / plausibly non-tuned** but **not yet pinned**. This handover closes that gap. The founder set
the sequence: **pin ΔG*_nuc before panel round 2** (submit a pinned prediction, not a bracket).

## THE ASK (strong/geometry lane, patch 2211+) — OPEN-SS-41a
**Derive f and n\* from the 8qCP+8eCP element cross-section:**
1. **f** — the eCP-coat **spine-face solid-angle fraction**: of the incoming-orientation sphere, the fraction that
   presents the E_qq spine face for a *correct axial* bond (the orientation selectivity that discriminates ordered
   Cross-Rod growth from amorphous attachment).
2. **n\*** — the **critical nucleus**: the smallest cooperatively-stable rod seed (below which the seed dissolves,
   above which it grows).
Then **ΔG*_nuc = (n*−1)·|ln f|·kT_form** is pinned — a single number, not a bracket.

## BANDS (from OPEN-SS-41a)
- **Win:** pinned ΔG*_nuc ∈ **[6.0, 6.9] kT_form** ⇒ N_form ~ 400–1000 ⇒ dwarf normalization a zero-parameter
  prediction. (The first-pass natural reading already sits here — this is pin-and-confirm, not a fresh search.)
- **Kill:** pinned ΔG*_nuc ≲ 4 kT (under-cored) or ≳ 9 kT (over-cored). Cluster σ/m ∝ 1/v² stands regardless.

## LANE BOUNDARY
- **Strong/geometry owes:** f, n* from the element cross-section → pinned ΔG*_nuc. Register under 2211+, update
  OPEN-SS-41a (and OPEN-SS-41). Do NOT reopen the cosmology side (ε_nuc = exp(−ΔG*/kT) settled) or the barrier form
  (2209 settled: selectivity, not strain/energy).
- **DM consumes:** pinned ΔG*_nuc → ε_nuc = exp(−ΔG*_nuc/kT) → N_form → dwarf σ/m = K·N_form·ε_bounce → σ/m(v).
  **Panel round 2 runs after this lands** (held by founder until pinned).
- Cross-link OPEN-SS-41 (parent) + SS-2 (element cross-section kit). Distinct from OPEN-FP-SF-2-η.

## POINTERS
- `flagship_papers/strong/reasoning/2209.md` + `code/2209_dGnuc_nucleation_barrier.py` (the ΔG*_nuc = (n*−1)·|ln f|
  form, the (n*, f) that hit the window — §D is where f and n* enter). **OPEN-SS-41 / OPEN-SS-41a**
  (`frontier_sectors/SS.md`). `reasoning/1842.md` (the 8qCP+8eCP element geometry + ribbon→cross tracks).
  `reasoning/1851.md` (DM consumption of the first pass).

## SUGGESTED SEQUENCE
n* from the cooperative-stability crossover along the ribbon→cross coordinate; f from the eCP-coat spine-face solid
angle of the element. Combine → pinned ΔG*_nuc; compare to [6.0, 6.9] kT; hand N_form back to DM. That closes the
dwarf branch to a pinned prediction (or a clean verdict) and unblocks panel round 2. The cluster branch stands
throughout; the candidate is one number from a full, submittable σ/m(v) statement.
