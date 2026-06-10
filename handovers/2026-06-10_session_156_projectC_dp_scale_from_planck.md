# Handover — Project C: the DP/QCD binding scale from the Planck scale (SS-1 `op:lambda_psr`)

**Arc:** Conscious Point Physics — strong sector / foundations. **Project:** `future_projects.md` Project 2b.
**Date opened:** 10 June 2026 (Session 156), Patch 0839. **Assigned by Thomas as the next project** (Option C of TODO-016).
**This is both the durable record and the opening prompt for a fresh window. Paste it in to start; re-fetch from `handovers/` if context is lost.**

---

## BLOCKING CLONE-AND-GREP GATE (before anything else)

1. Clone fresh; `git log --oneline | head -30` — see the live frontier and free patch bands (multiple windows push concurrently).
2. Read the §Required reading in order before computing or deriving.
3. Claim a free patch band confirmed against `git log`.
4. CLONE-FIRST: never register an ID, place a file, or compute a coefficient before cloning + grepping the registry.

## KICKOFF SENTENCE

> *You are deriving the QCD confinement scale Λ_QCD ≈ 0.218 GeV — and with it the CPP Dipole-Pair binding spectrum (eDP 88, qDP 264, hDP 152 MeV) — from the Planck length l_P and sea_strength = 0.185 via the PSR-saturation mechanism (PSR_eff → l_P/2), **without** using any PDG value as input. This is SS-1 open problem `op:lambda_psr`. Success makes the DP/QCD scale a first-principles result; it currently is calibrated.*

## Why this project exists (the precise motivation)

The DP-Sea flagship's appendix presents the DP binding spectrum as `E_eDP = αℏc/(φl_p) ≈ 88 MeV`. **That formula is false by ~17 orders** — with l_P the gravitational Planck length (as the paper uses it consistently: `E_p = ℏc/l_p ≈ 10¹⁹ GeV`), `αℏc/(φl_p) = α·E_p/φ ≈ 4.5×10¹⁶ GeV`, not 88 MeV. The 88 MeV is the physically-correct value (the QCD/constituent scale) but its **stated Planck derivation is wrong**; SS-1 honestly marks the same scale **calibrated, derivation open** (`op:sigma`, `op:lambda_psr`). The appendix is being brought into line with SS-1's honest stance separately (TODO-016 Track 1). **This project is Track 2: actually doing the derivation SS-1 leaves open.** Closing it upgrades **both** the DP-Sea appendix and SS-1 from "calibrated" to "derived," and firms the *absolute* scale on which the whole DP spectrum (and downstream the DM-2 Era-2 constituent mass) rests — today only the **ratios** (color factor 3; geometric mean) are clean.

## The target, precisely

Derive, from l_P and sea_strength = 0.185, with **no PDG input**:
- Λ_QCD ≈ 0.218 GeV (the SS-1 `op:lambda_psr` target), and
- the DP binding scale E_eDP ≈ 88 MeV (with E_qDP = 3·E_eDP, E_hDP = √(E_eDP·E_qDP) following from the already-clean ratios).

The physical hierarchy to bridge is Planck (~10¹⁹ GeV) → QCD/DP scale (~10⁻¹ GeV) — ~20 orders. **Do not** expect a fixed multiplicative suppression; scale hierarchies of this kind are logarithmic/exponential (dimensional-transmutation / RG-running). The CPP candidate mechanism is **PSR saturation** (the PSR_eff → l_P/2 threshold), not a Coulomb-at-Planck-length evaluation.

## Candidate mechanism and partial work already on file

- **PSR saturation** (SS-1 Remark `rem:psr`): relates Λ_QCD to the Planck-scale threshold PSR_eff → l_P/2. This is the stated route.
- **C14 self-consistent relation:** `r_conf = √(α_s ℏc/σ)` and `σ = α_s ℏc/r_conf²`, self-consistent at r_conf ≈ 0.161 fm, σ = 0.900 GeV/fm. So σ and r_conf are **not independent** — deriving either from sea_strength closes both.
- **Numerical work:** `series_strong/notebooks/chain_fraying_dynamics.ipynb` (Jan 2026) — the established self-consistent relation + bow-rigidity confinement mechanism (the four partial results listed under SS-1 `op:sigma`).
- **Consistency target (SS-1 `op:sigma`):** derive σ from sea_strength = 0.185 **consistently with the EW boson-mass calibration** (same sea_strength, same φ⁻³ factor) — this would unify the quark-mass and boson-mass calibrations and close the strong-sector parameter space.

## Required reading (in order)

1. `series_strong/papers/SS-1_strong_sector_from_600cell_lattice.tex` — open problems `op:sigma` (~line 987) and `op:lambda_psr` (~line 1086), Remark `rem:psr`, the α_s running block (~line 587), and the C14 relation.
2. `series_strong/notebooks/chain_fraying_dynamics.ipynb` — partial numerical results.
3. The c14 companion (color charge / confinement) and SM-7 (α_s lattice value 5/(8φ) ≈ 0.386, Project 2 connects its running).
4. `series_foundations/dp_sea_composition/DP_sea_and_cage_composition.tex` lines 312–340 — the appendix whose scale this derivation would justify.
5. `handovers/2026-06-10_session_156_todo016_dpsea_mass_scale.md` — the two-track framing and the appendix correction (Track 1).

## Suggested approach

1. Pin sea_strength = 0.185 and its role; confirm the φ⁻³ EW-mass calibration uses the same sea_strength (the `op:sigma` consistency demand).
2. Work the PSR-saturation threshold (PSR_eff → l_P/2) into a relation for r_conf (or σ) in terms of l_P and sea_strength; use the C14 self-consistency to convert between σ, r_conf, Λ_QCD.
3. Likely the running of the CPP coupling (β₀ = 7, SS-1; Project 2) carries the Planck→QCD hierarchy via dimensional transmutation — connect the lattice coupling 5/(8φ) at the Planck/lattice scale to the scale where confinement sets in.
4. Falsification-first: at each step, check whether the construction can reproduce Λ_QCD ≈ 0.2 GeV from l_P + sea_strength alone, or whether it secretly requires a PDG-anchored input.

## Falsifier

If no l_P → QCD-scale relation reproduces Λ_QCD ≈ 0.2 GeV (and the DP spectrum) from l_P + sea_strength within tolerance and without PDG input, abandon the "DP scale is Planck-derived" claim in favour of permanent calibration — in which case TODO-016 Track 1's honest "calibrated" stance is the terminal answer and the DP-Sea appendix stays as corrected there.

## On success

Register the derivation (THEO/PRED per the registry rules + panel sign-off); upgrade SS-1 `op:lambda_psr`/`op:sigma` and the DP-Sea appendix from "calibrated" to "derived"; close TODO-016 fully (Track 2). This would make the entire DP binding spectrum a first-principles consequence of l_P + sea_strength + the 600-cell geometry.

**Status at handover:** registered as Project 2b; assigned as the next project; not started. DM-2 Era-2 arc (Patches 0830–0836) is independent of the outcome (uses only the clean color-factor-3 ratio).
