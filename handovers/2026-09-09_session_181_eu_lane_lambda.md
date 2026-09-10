# EU-lane Handover — Session 181 Close (9 Sep 2026) — λ computed; the breaking step is idle; C-4 turns on one integer

**Patch 3844. Lane: EU, block 3800–3899. Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3842 at session start; 3843–3844 delivered as patch files. **Next free: 3845.** GR lane: next free 3715.
**Active paper(s):** EU-1 V1.5 (**Isak owes the recompile**). GR-2 V2.11 (**Isak owes the recompile**).
**Parallel windows:** none known.

## The single most important next action
**Compute the integer p** in λ ≈ λ_hard·x^p, where x = SSV_net/SSV_abs is the fractional departure from the exact dipole cancellation. **C-4 lives or dies on it: p = 2 gives m/H = 3.2 and the candidate fails; p ≥ 3 clears.**

What the computation is: track how a nonzero SSV_net feeds the displacement anisotropy back into the orientational sector. In the homogeneous state SSV_net = 0 exactly and the anisotropy is absent; the question is at what order in the departure it reappears. **Do not compute on the scaling ansatz itself** — λ ≈ λ_hard·x^p is a parameterisation that isolates the risk, not a derivation, and p must come from the protocol.

## What was done this session
**3843 — C-4's debt (1) worked.**
- **λ_hard = 0.052, computed exactly** from the covering function f(n̂) = maxᵢ(n̂·v̂ᵢ): covering radius 37.3°, range 0.795–1.000 (22%). Bonus: its multipoles **independently reproduce T-1** — ℓ = 1–5 at Monte-Carlo noise, leading anisotropy ℓ = 6 — from a function unrelated to the census T-1 was derived from.
- **As a potential, C-4 dies:** m/H = 7.1×10⁴, the register spring's wall (1.3×10⁵). This is the natural reading and 3841 §4 warned of exactly it.
- **It is not a potential.** (a) The twelve axes are icosahedrally equivalent and DP axes are quantised to them, so reorienting the mean director is a **repopulation** among equivalent states — Σpᵢε = ε, exactly flat in n̂. (b) The constraint acts on **displacement** (A1′/AP-3), a **mobility**; anisotropic damping does not gap a Goldstone, since the k → 0 uniform rotation still costs nothing. (c) **Decisive: the breaking step is idle.** Displacement is the *only* rotation-symmetry-breaking operation — the register computation is exactly covariant (SSV_abs sums magnitudes, SSV_net is a vector sum) — and in the homogeneous saturated era **SSV_net = 0 exactly** (S-HENGINE-HELD §2.2, resting on T-1's ℓ = 1 cancellation, verified as an identity at 3820). **The operation that would gap the Goldstone never fires during inflation.**
- **What remains is one integer** (table above). C-4 has moved from eleven orders from death to one integer from it, with the pessimistic branch a factor of three rather than 10⁵. **This is not a claim that C-4 clears.**
- **T-1 is now load-bearing in three independent places**: homogeneity/isotropy (3820), the mass suppression (3839 §5), and the idle-breaking argument (here). A result that keeps turning out load-bearing in unrelated places deserves scrutiny; its entailment status should go to the panel with CONV-046 on that basis.

## Forward queue
1. **Compute p** (above). Top; decides C-4 either way.
2. **AP-4's shell-clause derivation** — still owed, and load-bearing twice (the Moment-1 count; the amplitude's mass scale, 3841 §3).
3. **C-4 debts (2)–(4):** ε derived (PSR-EARLY-1's second half, which also fixes f via 3839 §4); the O(1) coefficient in δε ≈ ε δθ; an explicit adiabaticity check against Planck's isocurvature bound.
4. **OPEN-EU-EFOLD-BUDGET-1** — the VSL horizon computation. Still ~10.5 short; decoupled from the mass since 3841 §5.
5. **T-2** — the O(α) ZRP coefficient. Unblocked; the right fallback.
6. **CONV-046 package:** C-4's arc (3839, 3841, 3843) plus the 3837 conflict; and now T-1's triple role.

**Cross-lane, owed to the maintainer (NOT enacted — bar 4):** `cosmic_web_generation_constraints.md` owed-piece 1 (from 3833).

**Anti-priorities:** no calibration against an observable (PD-007); **λ and p are not minted**; **do not report C-4 as cleared** — p = 2 fails; do not treat λ ≈ λ_hard·x^p as derived; do not read "ℓ = 6" as the mass suppression (3841 §1); no cross-lane edits; do not retire 3710.

## §15 Steps A–H
- **A** `session_logs/2026-09-09_session_181_log.md` (3844). **B** transcript row 3843. **C** development vignette (Session 181).
- **D** Tier 4: `reasoning/3843_lambda_computation.md`.
- **E** Registries: `research_frontier.md` (3843 prepend, verified single); `id_block_registry.md` (next free 3845); `future_projects.md`. N/A: `predictions.md` (nothing moved — C-4 remains a derivation candidate and is not cleared), `axiom-registry.md`, `theorem-registry.md`, `master_glossary.md`.
- **F** none (no panel). **G** no PD minted; no founder ruling. **H** this file.

## Governance notes
- **Ask which physical slot a computed number occupies before drawing a verdict from it.** λ_hard is exact and would have killed C-4 read as a potential; the whole session turned on it being a mobility instead.
- State the pessimistic branch in the same breath as the optimistic one. p = 2 fails, and that belongs next to "one integer from resolution," not below it.
- T-1's third independent load-bearing role is worth a panel look. Results that keep proving structural in unrelated places are either deep or over-used, and the corpus should find out which.
