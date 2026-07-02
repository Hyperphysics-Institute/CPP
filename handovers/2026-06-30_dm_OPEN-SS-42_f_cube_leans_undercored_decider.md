# HANDOVER — DM / founder: OPEN-SS-42 result — the cube pins f to [1/12, 1/3]; over-coring is EXCLUDED, the dwarf branch LEANS UNDER-CORED, and one color-structure question decides it
**Date:** 2026-06-30 · **Lane:** DM 18xx / founder · **From:** Opus (strong/geometry lane, patch 2215) · **Consumer:** DM-1
**Delivers on:** OPEN-SS-42 (`frontier_sectors/SS.md`), the dwarf-branch decider.

## ⛔ CLONE GATE
```
cd ~/Documents/GitHub/CPP && git pull --rebase origin main && git log --oneline -6
```
Confirm HEAD includes **2215** (OPEN-SS-42 result). Grep before reserving sub-IDs.

## Orientation — read this first (it is not the confirm the sequence expected)
The element geometry is pinned — 0886 established it as a **cube** (cross-section = cube face = the 4 hTetra arms / 8 qCP; one axial rung = one cube; the eCP coat screens the transverse faces). So f is not a free parameter; it follows from the cube's orientational combinatorics (|O| = 24). The E_qq spine distinguishes 1 of 3 axes ⇒ **f ∈ [1/12, 1/3]**. With ΔG*_nuc = (n*−1)·|ln f| and n* ~ 2–4:
- **Over-cored kill: EXCLUDED (firm).** f ≥ 1/12 ⇒ ΔG*_nuc ≤ 7.5 kT < 9. The Cross-Rod cannot over-core.
- **Under-cored: the geometric DEFAULT.** The 4-fold-symmetric cross shape with coat-blocking only gives f = 1/3 ⇒ ΔG*_nuc ~ 1–3 kT ⇒ **N_form = 3^(n*−1) ~ 3–27** ⇒ dwarf σ/m ~ 0.04–0.35 cm²/g — below what dwarfs want.
- **Window: a corner.** ΔG*_nuc ∈ [6.0, 6.9] kT needs f ~ 1/9–1/12 **and** n* ~ 4 (N_form ~ 730–1720).

**Honest lean: the dwarf branch leans UNDER-CORED.** The window is reachable but not the default — the opposite of the first-pass optimism. Over-coring is off the table.

## THE DECIDER (one color-structure question)
Two considerations pull opposite ways: the cross-section **shape** is 4-fold symmetric (→ f = 1/3, under-cored), but the E_qq spine bond is a **color** bond whose neutrality plausibly forces the color charges to register (→ f < 1/3, toward the window). Which wins is **the cube-face E_qq color-pattern symmetry** — a specific SS-1b color-cage sub-question (does the 4-hTetra-arm color assignment on the spine face carry a 4-fold-symmetric singlet, or one that forces rotational registration?). 4-fold-symmetric ⇒ under-cored kill; registration-forcing ⇒ window at n* ~ 4. That is the single remaining decider, answerable from the pinned color-cage structure — one color-structure calc away.

## THE FULL PACKAGE (for panel round 2 — recommend running it now on this honest status)
- **Cluster branch: σ/m ∝ 1/v², parameter-free, Bullet-safe — the submittable headline prediction.** Unaffected by any of the above.
- **Dwarf branch: over-coring excluded; leans under-cored; in-window prediction reachable only in the color-registration + n* = 4 corner; one color-structure question (cube-face color-pattern symmetry) from a clean verdict.**
- **Do NOT present a pinned in-window dwarf prediction** — the geometry's default is under-cored, and the window is a corner, not the confirmed value.

Recommendation: **run panel round 2 now on this honest package** rather than hold it — the pin has landed, and it says the dwarf branch is more likely an under-cored kill than a prediction (with over-coring excluded). Open the color-pattern-symmetry decider in parallel if the founder wants the dwarf branch fully settled.

## LANE BOUNDARY
- **Strong/geometry delivered (2215, done):** the cube geometry (0886) → f ∈ [1/12, 1/3]; the over-cored exclusion; the under-cored default; the window-corner; the color-pattern-symmetry decider. **Still owed (if opened):** the cube-face E_qq color-pattern symmetry (f ~ 1/3 vs ~1/10).
- **DM consumes:** the lean + the exclusion → dwarf-branch framing + panel package. If the decider lands: f → ΔG*_nuc → N_form → dwarf σ/m(v).

## POINTERS
- `flagship_papers/strong/reasoning/2215.md` + `code/2215_f_from_cube_element.py` (the cube combinatorics, the [1/12,1/3] bracket, the per-(f,n*) verdict table, the exclusion + the corner). **OPEN-SS-42 / 41a / 41** (`frontier_sectors/SS.md`).
- `reasoning/0886.md` (the cube-element geometry — the load-bearing input). `flagship_papers/strong/reasoning/2209.md` (the ΔG*_nuc form). SS-1b (the color-cage structure the decider draws on).

## SUGGESTED SEQUENCE
Run panel round 2 on the honest package (cluster = parameter-free prediction; dwarf = over-coring excluded, leans under-cored, one color-structure question from settled). In parallel, founder's call: open the cube-face color-pattern symmetry calc — the single decider between an under-cored kill and an in-window prediction. The cluster branch is the submittable result regardless; the dwarf branch is now bounded (no over-coring) and one color-structure question from a clean verdict.
