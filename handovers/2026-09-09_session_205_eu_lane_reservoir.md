# EU-lane Handover — Session 205 Close (9 Sep 2026) — reservoir debt discharged; ζ derived; the amplitude is now the gate and is workable in-lane

**Patch 3893. Lane: EU, block 3800–3899. Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3891 at session start; 3892–3893 delivered as patch files. **Next free: 3894.** GR lane: next free 3715.
**Active paper(s):** **EU-1 at V1.6** (**Isak owes the recompile**). GR-2 V2.11 (**Isak owes the recompile**).

## The single most important next action — and it is WORKER work
**C-5 debt (2): compute δ ln f.** For the first time in this arc the gating question is **in-lane and computable**, not a founder question or a maintainer decision.

> **ζ = ⅓ δ ln f**, where **f** is the local fraction of CPs that have left superposition.

**The warning, recorded at 3892 before anyone gets attached:** if unstacking is a **Poisson process**, δ ln f goes as the inverse root of the events per coherence volume — **white** — and C-5 meets **the same wall as the conserved count, composition, C-2 and DM clumping**. **Being a rate does not by itself guarantee a red spectrum.**

**What would save it:** a **correlation** in the unstacking — a dependence of the local rate on local H_eff, making f self-regulating rather than Poisson. **The founder's charge rule is the first place to look** (below), since it distinguishes outcomes rather than treating all landings alike.

**PD-007 bars calibrating the amplitude against A_s.** This is where that temptation lives.

## What was resolved
**C-5's reservoir needs nothing new.** CPs stack because **the summation of their arriving DI-bits directs them to the same GP address** — **ordinary A1′/AP-3 displacement**. And **the initial condition *is* stacking**: *"they start out with a large number of CPs on every GP."* **The reservoir is the starting state, not a posited structure. Debt (3) discharged.**

**This overturns 3890's sparsity argument.** That patch computed 2.3×10⁻¹³ CPs per GP and concluded superposition needed forcing — but it **assumed the CPs were spread** across a Planck sphere's 4.3×10⁹⁶ GPs. The founder's initial condition **stacks** them. **The number is right; treating it as the starting state was not.** Same error class as 3882's invented mass — **the worker supplied an unstated arrangement** — and the second occurrence in four sessions.

**C-5's perturbation is now derived:** occupied GPs ≈ f·N_CP ⇒ **ln n̄ = ln N_CP − 3N + ln f** ⇒ **ζ = ⅓ δ ln f.**

## Both banked results survive — check this before trusting anything downstream
- **Count law exactly.** f → 1 at the end ⇒ V_end = N_CP Planck spheres ⇒ **N = ⅓ ln N_CP = 64.47.**
- **Tilt exactly.** If ln f is linear in N_rem, ln n̄ stays linear, and **ε = 1/N_rem whatever the coefficient** ⇒ **n_s = 0.9649** at n₀ = 10⁶, 10¹², 10²⁴ alike.

> **Both are independent of the stack number**, which the founder states he does not remember and which was **carried as a parameter, not invented.**

## Registered, not yet used
**The charge rule for re-superimposition:** *opposite charge → ZBW oscillator; same charge → launches without oscillating.* An input to **f's evolution law**, hence to debt (2). **Start here when attacking the amplitude.**

## C-5's debts, current
1. ~~The referent~~ — discharged 3890.
2. ~~The reservoir~~ — **discharged 3892.**
3. **The amplitude — δ ln f. NOW THE GATE, and in-lane.**
4. **Adiabaticity** vs Planck's isocurvature bound.

## Owed (elsewhere)
- **Isak:** recompile **EU-1 (V1.6)** and GR-2 (V2.11).
- **Maintainer:** CONV-046 — **the sector has a live candidate with a derived perturbation**; the amended DE escalation (3858); cosmic-web owed piece (3833); `DM_project_map.md` stale (3884).
- **EU-1 V1.7 (bundle):** 3854 VSL clarification; 3876 §5 as qualified by 3878. **Do not add C-5.**

**Anti-priorities:** **do not report C-5 as working**; **no calibration against an observable** (PD-007) — debt (3) is where it will be tempting; **never supply a parameter, least of all one the founder has flagged as unknown**; follow **§0.5 D-1…D-6**; no cross-lane edits without sanction; do not retire 3710; **nothing in this arc refutes n_s** — PRED-C-96 reads 0.9654 (V1.6).

## §15 Steps A–H
- **A** `session_logs/2026-09-09_session_205_log.md` (3893). **B** transcript row 3892. **C** development vignette (Session 205).
- **D** Tier 4: `reasoning/3892_reservoir_mechanism.md`.
- **E** Registries: `research_frontier.md` (3892 prepend); `id_block_registry.md` (next free 3894); `future_projects.md`; in-place supersession at `referent_resolved.md` §5b. N/A: `predictions.md`, `axiom-registry.md`, `theorem-registry.md`, `master_glossary.md` — **C-5 is live, not adopted**; the count law and tilt are unchanged, so nothing moves.
- **F** none (no panel). **G** no PD minted; founder mechanism registered verbatim. **H** this file.

## Governance note
**The discipline worked once and failed once in the same session, and both are worth recording.**

It **worked** on the stack number: the founder flagged it as unremembered, and rather than choose a plausible value the parameter was carried and the three results shown independent of it. That is 3884's lesson operating rather than being restated.

It **failed** on the arrangement: 3890 computed a correct occupancy from an arrangement the worker supplied, and called superposition non-generic on that basis. **Numbers do not protect you if the configuration they describe is assumed.** The rule needs the addition: *when you compute a quantity about a configuration, check that the configuration is the corpus's and not yours.*
