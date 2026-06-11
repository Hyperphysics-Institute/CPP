# Reasoning capture — Patch 1104 (CC-U/1: DP-Sea "CC resolved by N⁴" reframe)

**Protocol:** `templates/reasoning_capture_protocol.md`. Records the enacted DP-Sea flagship reframe.
**Target:** `series_foundations/dp_sea_composition/DP_sea_and_cage_composition.tex`.
**Sign-off:** Thomas, 11 June 2026 — abstract **Option A**; comparison-table CC cell →
`Dynamical $10^{-120}$ (cond.)`; "Complete" cell + general rhetoric (lines 478/564) left for a
later pass (out of CC-U/1 scope). Built on HEAD `bd34ba92`; file had only its creation commit
(TODO-016's DP-spectrum fix still owed on the same file — separate task).

## Why this edit
The paper asserted, as a headline result in seven places, that CPP "resolves the cosmological
constant problem naturally" via `ρ_sea/N⁴ ≈ 10⁻¹²⁰` (incl. "holographic bit recycling"). The CC
umbrella verdict (Patch 1101/1103) demotes that: the suppression is **dynamical** and lives in the
GR companion (OPEN-SR-5, `ρ_Λ=(1/8π)ρ_P(l_P/R_H)²`, excess-sourcing, factor ~2, time-varying,
conditional on the c08 closed field equation); the static `1/N⁴` equals `(l_P/R_H)²` only because
`R_H ≈ N²l_P` *today* — a present-epoch coincidence (`1101_cc_coincidence_check.py`) — and per Patch
0736 the lattice resolution `N` enters no CPP prediction, so it cannot be Λ's fundamental origin.
Same epistemic-honesty class as TODO-016, same paper.

## What the reframe does (consistently, all 7 spots)
1. Keeps the `10⁻¹²⁰` number everywhere.
2. Attributes the actual suppression to the GR companion's dynamical, excess-sourced mechanism.
3. Marks `ρ_sea/N⁴` as a present-epoch coincidence, not the mechanism.
4. States the c08 conditionality.
5. Removes the unsupported "holographic bit recycling" phrase (line 507) and the "without
   fine-tuning"/"naturally resolves" over-claims; softens the comparison-table CC cell.

Locations: abstract (37, Option A), contributions (49), body origin ¶ (64), Vacuum-Catastrophe item
(181), comparison table CC cell (243), CC-subsection lead-in + CPP bullet (501, 507).

## Left unchanged (deliberately, per sign-off)
Comparison-table "Complete" unification cell; general "resolves naturally" rhetoric (478, 564);
keyword (41); all energies/ratios and the DP spectrum (the spectrum scale is TODO-016's fix).

## Status
NO VERDICT MOVED — no THEO, no PRED, no count change. CC-U/1 disposition (demote, reframe) now
enacted in the flagship. Recompile (ClearPC) is Thomas's step. Remaining CC arc work: CC-U/3 SR-5≡SM-6
writeup (frontier note already in 1103); CC-U/5 R2 reframe (DM lane); CC-U/4 c08 (the standing cap).

## Confidence
- Solid: the demotion (three independent reasons, one verified numerically) and the honest
  attribution to SR-5.
- Conditional: everything rests on the c08 closed field equation (stated as such throughout the
  reframe — not hidden).
