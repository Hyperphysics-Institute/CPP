# Handover — TODO-016: DP-Sea binding-energy scale is presented as Planck-derived but is off by ~17 orders

**Task:** reconcile the DP-Sea flagship's binding-energy appendix (`series_foundations/dp_sea_composition/DP_sea_and_cage_composition.tex`).
**Date opened:** 10 June 2026 (Session 156), Patch 0837. **Origin:** surfaced during the DM-2 Era-2 required-inputs derivation (Patch 0833); registered as `todolist.md` TODO-016.
**Why a handover and not an inline fix:** the correction is a **foundational physics decision about the theory's own energy scale**, on a **flagship paper** — not a typo. It is Thomas's call (and his flagship edit/publish workflow). This document is the durable record and the opening prompt; a fresh window should paste it in and re-fetch from `handovers/` if context is lost.

---

## BLOCKING CLONE-AND-GREP GATE (before anything else)

1. Clone fresh; `git log --oneline | head -30` to see the live frontier and free patch bands (multiple windows push concurrently).
2. Read the §Required reading in order before editing.
3. This task edits a **flagship**; do not push a `.tex` content change to it without Thomas's sign-off on the physics decision below.

## KICKOFF SENTENCE

> *You are reconciling a single numerical inconsistency in the DP-Sea flagship: the DP binding-energy spectrum (eDP 88, qDP 264, hDP 152 MeV) is presented as derived from the golden-ratio-scaled **Planck** length, but that formula actually evaluates to ~10¹⁶ GeV — off by ~17 orders. The physically-correct values (88/264/152 MeV) must be retained; what must change is the **claimed origin** of the scale. Choosing the origin is a physics decision (options A/B/C below) — make it with Thomas, then prepare the corrected appendix text for his approval.*

## The inconsistency, precisely

In `DP_sea_and_cage_composition.tex` (Appendix "DP Binding Energy Calculation", lines ~316–327; also the body, lines ~76, 80):

- Stated: `E_bind = αℏc/r_min`, with `r_min = φ·l_p = 1.618 × 1.616×10⁻³⁵ m ≈ 2.61×10⁻³⁵ m`, "the golden-ratio-scaled Planck length."
- Claimed: `E_eDP = αℏc/(φl_p) ≈ 88 MeV`, `E_qDP = 3αℏc/(φl_p) ≈ 264 MeV` (color factor 3), `E_hDP = √(E_eDP·E_qDP) ≈ 152 MeV`.
- **Actual evaluation:** the paper itself (line 80) correctly states `E_p = ℏc/l_p ≈ 10¹⁹ GeV` (the Planck energy). Therefore `αℏc/(φl_p) = α·E_p/φ ≈ (1/137)(10¹⁹ GeV)/1.618 ≈ 4.5×10¹⁶ GeV ≈ 4.5×10¹⁹ MeV` — **not 88 MeV. The discrepancy is a factor of ~5×10¹⁷ (~17–18 orders of magnitude).**
- The quoted 88 MeV instead requires `r_min = αℏc/88 MeV ≈ 0.0164 fm = 1.64×10⁻¹⁷ m` — ~18 orders **larger** than the Planck length, and ~`10⁴⁸` larger than the CPP grid spacing (line 64: 10³⁰ gradations per Planck length). So `r_min ≈ 0.016 fm` corresponds to an energy scale `ℏc/r_min ≈ 12 GeV`, with the α prefactor bringing it to 88 MeV.

`l_p` is used **consistently as the gravitational Planck length** elsewhere in the paper (line 80 Planck energy 10¹⁹ GeV; line 69 Planck breaking; line 64 grid scale), and correctly so. The error is localized: applying the Planck-scale Coulomb energy to the DP binding. The 88 MeV is the right physical value (it is the constituent/QCD/Λ_QCD scale) — only its stated derivation is wrong.

## What is affected / not affected

**Affected:** the *claimed derivation* of the DP binding spectrum (eDP 88, qDP 264, hDP 152), and any text asserting "DP energies follow from the golden-ratio Planck length." The eDP = 88 MeV scale propagates through the whole DP/cage spectrum and the boson-mass averaging in this paper.

**NOT affected (do not re-open these):**
- The **ratios** are clean and untouched: `E_qDP/E_eDP = 3` (color factor) and `E_hDP = √(E_eDP·E_qDP)`. The entire DM-2 **Era-2 arc (Patches 0830–0836)** uses only the *ratio* (m_qDP ≈ 264 MeV = 3×88) and the color factor — so the Era-2 chain (glueball-avoidance, collisionless, diffuse, f ≈ 0.2) needs **no rework** regardless of how this is resolved. This is stated in the 0833 patch.
- The SM/SS-sector matching uses the *values* (88/264/152), not the Planck-derivation, so it is unaffected by a reframing of the origin.

## The fix is a physics decision — three options (do NOT pick unilaterally)

**Option A — calibrated scale (minimal-consistency).** State that 88 MeV is the empirically-anchored DP binding scale (≈ the QCD/constituent/Λ_QCD scale of CPP's strong sector), drop the false `αℏc/(φl_p)` Planck derivation and the "2.61×10⁻³⁵ m" value. Lowest risk; honest; but concedes the DP scale is an input/anchor rather than a Planck-level derivation.

**Option B — a genuine sub-quantum CPP length.** Identify a real CPP length `r_min ≈ 0.016 fm` (≈12 GeV⁻¹) — NOT the Planck length — that sets the minimum stable CP separation (e.g. a ZBW-collapse radius at the DP scale, a screening/confinement length, or a defined lattice-coarse scale), and derive 88 MeV from `αℏc/r_min`. Preserves a derivation, but the 0.016 fm scale must be **independently justified** — the corpus does **not** currently provide it (searched: the only `l_p` is the gravitational Planck length; the grid spacing is `l_p/10³⁰`, far smaller).

**Option C — Planck scale plus a derived suppression.** Keep the Planck-scale bare Coulomb (~10¹⁶ GeV) and derive the ~10¹⁷ suppression down to 88 MeV (a renormalization/screening cascade from the Planck scale to the DP scale). Most ambitious; would be a genuine result if a real suppression mechanism exists, but is a research task, not an edit.

Whichever is chosen: **retain the energies (88/264/152 MeV)** — they are physically correct and downstream-load-bearing — and **change the origin language** (lines ~76, 321) and the **"2.61×10⁻³⁵ m" value** (lines ~76, 321). The color-factor-3 and geometric-mean ratios stay.

## Required reading (in order)

1. `series_foundations/dp_sea_composition/DP_sea_and_cage_composition.tex` lines 60–96 (body scale statements) and 312–340 (the appendix block).
2. `series_phenomena/cosmology/dark_matter/qdp_required_inputs_derivation.md` (Patch 0833 — where this was surfaced; confirms the ratio is clean and the DM arc is unaffected).
3. `todolist.md` TODO-016.

## Suggested execution path for the fresh window

1. Run the clone-and-grep gate; confirm a free patch number.
2. Put the physics-decision options (A/B/C) to Thomas and get his choice — this is the gating step; do not edit the flagship before it.
3. For the chosen option, draft the corrected appendix text (energies retained, origin corrected) and present it to Thomas for approval; let him perform the flagship `.tex` edit + recompile + (if applicable) publish per his workflow.
4. On completion, move TODO-016 to the cleared-items section of `todolist.md` with the date and patch number.

**Status at handover:** diagnosed and scoped; **awaiting the physics decision (A/B/C) from Thomas**; no flagship edit made; DM-2 Era-2 arc confirmed independent of the resolution.
