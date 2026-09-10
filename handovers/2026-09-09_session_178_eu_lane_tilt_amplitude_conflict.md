# EU-lane Handover — Session 178 Close (9 Sep 2026) — the escape closes; the tilt causes the amplitude problem; C-4 is candidate of record

**Patch 3838. Lane: EU, block 3800–3899. Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3836 at session start; 3837–3838 delivered as patch files. **Next free: 3839.** GR lane: next free 3715.
**Active paper(s):** EU-1 V1.5 (**Isak owes the recompile**). GR-2 V2.11 (**Isak owes the recompile**).
**Parallel windows:** none known.

## The single most important next action
**C-4's coupling to the end condition** — the one surviving route out of the 3835 no-go, now that PSR-EARLY-1 has closed.

The question is singular and specific: **is there a coupling by which the DP sea's orientation (the director / the AF order of 3827–3829) shifts *when* inflation ends?** Not how fast it runs — κ₀ and kT both do that and both die on the end condition (3818, 3835 §4). It must move the threshold itself.

Why this and nothing else: §5 of the finding shows the tilt's own form requires the count to be conserved, and a conserved count is blue (3835). So ζ cannot come from the count. It must come from a field that is **not** the count and that touches the **end condition** — structurally the modulated-reheating mechanism. C-4 is light by symmetry, Gaussian, freezes at horizon exit, and is not the count, so it cannot disturb the tilt. It owes exactly one thing, and that thing is the next session.

**Do not compute on C-4 before the coupling is named** (PD-007). If no coupling can be found, that is itself the result and should be registered.

## What was done this session
**3837 — OPEN-EU-PSR-EARLY-1 worked; the escape closes.**

*Two clearings, both of which could have voided the session:* (a) **CONV-045 does not block the perceived reading** — S-HENGINE-HELD settles held vs *acted-on* and its own text says the D1 cap is "silent on n̄"; the held-vs-perceived axis was never adjudicated, and nobody had checked this in the two prior patches that named this route. (b) **R-PSR-LAW-LOG's series 1 − ε + ε²/2 is e^{−ε}** — the law is the exponential its name implies.

*New result worth reusing:* with SSV_abs count-like, self-consistency gives **logarithmic saturation** — n̄_perc ≈ ln(n̄_ref)/(3λ) ≈ **N_rem/λ**. A point amid 10⁸⁴ CPs perceives a crowd of about **63**, and the perceived crowd tracks the remaining e-folds.

*Both branches fail, in opposite ways:*
- **B1 (the PSR responds):** breaks the no-go (n̄_perc depends on local state ⇒ non-conserved) and costs e-folds (N = ⅓ln n̄_ref − λ) — **but destroys the tilt.** n_s − 1 = −2/(N_rem ln(N_rem/λ)); matching n_s needs λ ≈ 21, at which N_total = 43.5 and the pivot 57 **falls outside its own window**; keeping the pivot inside caps λ ≤ 7.5, where the tilt is **4.2–7.0σ** off across the whole range. **EXCLUDED — by the corpus's own confirmed prediction.**
- **B2 (the PSR floors at the D1 cap):** ε → constant ⇒ n̄_perc ∝ ρ, **still conserved**; tilt survives, no-go stands verbatim. **Preserves the prediction by supplying no escape.**

*The structural core, independent of any ε model:* n_s − 1 = −2/N_rem requires **ln n̄ exactly linear in N_rem**, which requires n̄ ∝ ρ at constant volume — a conserved count — and 3835 shows conserved ⇒ blue. **PRED-C-96's tilt formula itself requires the conservation that forbids a viable amplitude. The tilt and the amplitude are not two problems; the first causes the second.** Conditional on the engine's form (0749) and on ζ = δN sourced by the count.

## Forward queue
1. **C-4's coupling to the end condition** (above). Top, and the only live route.
2. **OPEN-EU-EFOLD-BUDGET-1** — the VSL horizon computation. Still owed; now fully separate from the amplitude thread.
3. **T-2** — the O(α) ZRP coefficient. Unblocked and unaffected; the right fallback.
4. **EU-1 V1.x note owed** — should now record ε = 1/N_rem (3833), the no-go (3835), and this structural conflict (3837).
5. **CONV-046 package:** 3816 (+§2b) + S-HENGINE-HELD note + 3818 + 3820 (+3822) + 3822 (+§1b) + 3823 (+§4b) + 3825 + 3827 (+§5b) + 3829 + 3831 + 3833 + 3835 + 3837. **The structural conflict is the strongest single item in it** and is what the panel should be asked to grade.

**Cross-lane, owed to the maintainer (NOT enacted — bar 4):** `cosmic_web_generation_constraints.md` owed-piece 1 (from 3833).

**Anti-priorities:** no calibration against an observable (PD-007); **λ is not minted**; no computation on C-4 before its coupling is named; no cross-lane edits; do not retire 3710; **never report the structural conflict as a refutation of n_s** — PRED-C-96's tilt value is untouched, and the conflict is about what else the same form permits.

## §15 Steps A–H
- **A** `session_logs/2026-09-09_session_178_log.md` (3838). **B** transcript row 3837. **C** development vignette (Session 178).
- **D** Tier 4: `reasoning/3837_psr_early_dichotomy.md`.
- **E** Registries: `research_frontier.md` (3837 prepend); `id_block_registry.md` (next free 3839); `future_projects.md`. N/A: `predictions.md` (the tilt's value is unchanged; the amplitude tension is already carried as a registered item since 3818), `axiom-registry.md`, `theorem-registry.md` (the structural conflict rests on standard integral constraints plus the engine's assumed form — registering it as THEO would overstate its base), `master_glossary.md`.
- **F** none (no panel). **G** no PD minted; no founder ruling. **H** this file.

## Governance notes
- **Check whether a ratified statement actually covers the fork before treating it as a wall — and before treating it as clear.** This session's route survived only because CONV-045 turned out to be about a different axis; that check cost one grep and should have been done two patches earlier.
- When two branches fail in opposite ways, look for what they share. That is where 3837's real result came from, and it generalises past the model that produced it.
- A result this unwelcome should be stated at full strength and with its conditions named, not softened. It is registered as conditional on the engine's form, which is the honest boundary.
