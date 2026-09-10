# EU-lane Handover — Session 180 Close (9 Sep 2026) — C-4's mass bound turns on AP-4's shell clause; the risk is now one number, λ

**Patch 3842. Lane: EU, block 3800–3899. Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3840 at session start; 3841–3842 delivered as patch files. **Next free: 3843.** GR lane: next free 3715.
**Active paper(s):** EU-1 V1.5 (**Isak owes the recompile**). GR-2 V2.11 (**Isak owes the recompile**).
**Parallel windows:** none known.

## The single most important next action
**Compute λ, the orientational anisotropy coefficient.** C-4 is light iff **λ ≤ 1.0×10⁻¹¹**, and everything else about the candidate now waits on that one number.

Where to look: **λ = 0 at leading order**, because the coupling found at 3839 is manifestly isotropic — SSV_abs sums *magnitudes*, and the arriving |E| depends on the scalar orientational correlation C, a rotational invariant, so rigidly rotating the sea costs nothing. The anisotropy enters only where **displacement is constrained to the twelve lattice directions** (A1′/AP-3: a CP displaces to a neighbouring GP, and there are only twelve). So the computation is: how strongly does that twelve-direction constraint feed back into the orientational energy, and is it suppressed by eleven orders?

**Do not treat "ℓ = 6" as the suppression.** The ℓ = 6 harmonic contributes curvature 6² = 36 — an *enhancement*. T-1 suppresses how many invariants survive, not how sharply the survivor curves. 3839 §5's wording permits the softer reading; it is corrected at 3841 §1 and should not be reintroduced.

## What was done this session
**3841 — C-4's debt (1) worked.**
- **Mapping:** f² ~ J/R, Λ⁴ ~ λJ/R³ ⇒ **m ≈ 6√λ/R**. The decay constant cancels; kT never enters; the mass is set by the **inverse interaction range** alone.
- **The whole question is R, and the answers differ by 10³²:** GP spacing (9.9×10⁻³³ l_P, fixed by the budget via N = ln(l_P/s)+1.31) ⇒ m/H = 3.1×10³⁷, λ ≤ 10⁻⁷⁵, dead on the spot; PSR shell (≈ l_P) ⇒ m/H = 3.1×10⁵, **λ ≤ 1.0×10⁻¹¹**.
- **AP-4 settles it:** imprint invariant in transit, **deposit once at the PSR shell**, near field by relay — the bits do not couple site-to-site at the grid spacing. **R = l_P.** C-4 survives on a ratified protocol clause rather than on anything introduced for the purpose.
- **Calibration, stated not glossed:** coherent O(1) anisotropy (λ ~ 0.15) gives m/H = 1.2×10⁵ — **the register spring's wall (1.3×10⁵)**. C-4 is not structurally safer than the candidate that died; it is eleven orders from an identical death.
- **Exponential tension averted:** had R = s, m/H would scale as e^N (64.5 → 3.2×10²³; 75 → 1.2×10²⁸; 85 → 2.6×10³²) — more e-folds meaning exponentially heavier modes, locking the budget shortfall and the amplitude in direct conflict with no move improving both. The shell clause decouples them. **Any future revision of the interaction range reinstates this silently.**
- **The bound is NOT cleared.** It is converted from a verdict awaiting a modelling choice into one computable number whose leading term is known to vanish.

## Forward queue
1. **Compute λ** (above). Top, and C-4's principal remaining risk.
2. **AP-4's shell-clause derivation** — now load-bearing **twice**: the Moment-1 count (3816 §6, 3820 §5) and the amplitude's mass scale. Its own derivation is owed, and that owed item is now more valuable than either problem resting on it.
3. **C-4 debts (2)–(4):** ε derived (PSR-EARLY-1's second half, which also fixes f through 3839 §4); the O(1) coefficient in δε ≈ ε δθ; an explicit adiabaticity check against Planck's isocurvature bound. All lower priority than λ.
4. **OPEN-EU-EFOLD-BUDGET-1** — the VSL horizon computation. Still ~10.5 short, and **now decoupled from the mass**, so it can be worked independently.
5. **T-2** — the O(α) ZRP coefficient. Unblocked; the right fallback.
6. **CONV-046 package:** C-4 remains its first positive item; the panel should see the 3837 conflict, the 3839 resolution and this bound together.

**Cross-lane, owed to the maintainer (NOT enacted — bar 4):** `cosmic_web_generation_constraints.md` owed-piece 1 (from 3833).

**Anti-priorities:** no calibration against an observable (PD-007); **λ is not minted**; do not read "ℓ = 6" as the mass suppression; **do not report C-4 as adopted or the mass bound as cleared**; no cross-lane edits; do not retire 3710; never report the budget tension as a change to n_s.

## §15 Steps A–H
- **A** `session_logs/2026-09-09_session_180_log.md` (3842). **B** transcript row 3841. **C** development vignette (Session 180).
- **D** Tier 4: `reasoning/3841_c4_mass_bound.md`.
- **E** Registries: `research_frontier.md` (3841 prepend, verified single); `id_block_registry.md` (next free 3843); `future_projects.md`. N/A: `predictions.md` (nothing moved — C-4 is a derivation candidate and the bound is not cleared), `axiom-registry.md`, `theorem-registry.md`, `master_glossary.md`.
- **F** none (no panel). **G** no PD minted; no founder ruling. **H** this file.

## Governance notes
- **Check `git log` and the id-block counter before starting work.** Sessions 179 and the 3816/3817 episode were both duplicated because this was skipped; it was done first this session and cost seconds.
- When a previous patch's wording permits a softer reading of its own result, correct it explicitly rather than working around it. 3839 §5's "ℓ = 6" phrasing was the case here.
- A surviving branch deserves its failure calibration stated in the same breath. C-4 survives, and it is eleven orders from the register spring's death; both facts belong together.
