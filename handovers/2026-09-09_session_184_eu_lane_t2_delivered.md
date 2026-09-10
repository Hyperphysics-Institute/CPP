# EU-lane Handover — Session 184 Close (9 Sep 2026) — T-2 delivered; all three charter targets discharged; the headline number moves

**Patch 3851. Lane: EU, block 3800–3899. Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3849 at session start; 3850–3851 delivered as patch files. **Next free: 3852.** GR lane: next free 3715.
**Active paper(s):** EU-1 V1.5 (**Isak owes the recompile**; and V1.6 is now owed — see below). GR-2 V2.11 (**Isak owes the recompile**).
**Parallel windows:** none known.

## The single most important next action
**EU-1 V1.6 — and it is a substantive version, not a note.** Two things land together:

1. **The headline number moves.** T-2 shows the O(α) correction is a **one-sided systematic shift**, not a symmetric uncertainty: **n_s = 0.9649 ± 5×10⁻⁴ → n_s = 0.9654** (0.12σ from Planck central; agreement survives comfortably). **Do not fold this in silently** — the paper currently prints a different claim from the one its own derivation supports.
2. **The amplitude closure** (3847): the paper's asserted spectator prescription has no mechanism; all seven candidates are dead; three exits remain, none a candidate search.

Also owed into V1.6, lower priority: ε = 1/N_rem (the engine is quasi-de Sitter, 3833); the e-fold budget tension (3823); T-1's species qualification (3822).

## What was done this session
**3850 — T-2 delivered**, fully EU-local, by putting two year-old results together that nobody had joined.
- **The closure:** 0774 gives g(n) = n(1+λ(n−1)) with λ ~ Γ; **0766 derives Γ = α/κ *exactly*** (κ ≡ kT_bath/E_Pl), because a = l_P makes Γ = q²/(a kT) = q²/(ℏc) = **α** at kT = E_Pl. So **λ = α/κ**. The 0.1α–10α bracket **is κ ∈ [0.1, 10]** — one parameter, and it is the bath temperature.
- **Self-correction:** 3848 §4 warned that α here is *not* the fine-structure constant. It is, exactly. Corrected in place.
- **One-sided bound:** the bath is the ZBW/substrate bath at the substrate clock, so kT ≤ E_Pl ⇒ **κ ≤ 1 ⇒ λ ≥ α**. **The bracket's lower half is excluded.** (E-3 predicted a two-sided narrowing: right in magnitude, wrong in shape.)
- **Value and sign:** at κ = 1, **λ = α exactly**, η = 1.43×10⁻², **Δn_s = +5.0×10⁻⁴**, and η > 0 — hence the headline shift above.
- **New empirical result:** Planck 1σ requires λ ≲ 9.7α ⇒ **kT_bath ≳ 0.1 E_Pl**. Not a fit — an observation *bounding* a substrate parameter the theory independently claims is of order E_Pl. The corpus did not have this bound.
- **Structural:** T-2's uncertainty **is κ**, already a named conditionality leg of PRED-C-96 (bath clause; OPEN-EU-BATH-DEPTH-1). **T-2 adds no theory error; it re-expresses one already counted.** The three framework legs stay three.
- **Not delivered: κ itself** — correctly, that is OPEN-EU-BATH-DEPTH-1's business.

## Charter status — the arc has a natural end
> **T-1 delivered (3820). T-2 delivered (3850). T-3 closed negative (3847).**
> **All three of OPEN-EU-1's frozen targets are discharged** — two positively, one as a characterised gap.

This is a stopping point, not an exhaustion. The remaining EU work (below) is separate from the charter.

## Forward queue
1. **EU-1 V1.6** (above). Top.
2. **CONV-046 dispatch — maintainer's call, and now a stronger package:** the 3835 no-go + the 3837 conflict + the 3847 closure (the negative), *and* T-1 and T-2 (the positives). A panel seeing only the negative would get a skewed picture of the arc.
3. **OPEN-EU-EFOLD-BUDGET-1** — the VSL horizon computation; ~10.5 e-folds short (3823), untouched and independent.
4. **AP-4's shell-clause derivation** — still owed, load-bearing for the Moment-1 count.
5. **OPEN-EU-BATH-DEPTH-1** — now more valuable than before: κ is what T-2's residual reduces to, and this item owns κ.

**Cross-lane: one item outstanding** — `cosmic_web_generation_constraints.md` owed-piece 1 (3833).

**Anti-priorities:** no calibration against an observable (PD-007 — §4's bound is an observation constraining a parameter, not a fit); **do not fold the headline change into EU-1 silently**; do not open an eighth amplitude candidate (3835 forbids the reflex); no cross-lane edits without sanction; do not retire 3710.

## §15 Steps A–H
- **A** `session_logs/2026-09-09_session_184_log.md` (3851). **B** transcript row 3850. **C** development vignette (Session 184).
- **D** Tier 4: `reasoning/3850_t2_coefficient.md`.
- **E** Registries: `research_frontier.md` (3850 prepend, verified single); `id_block_registry.md` (next free 3852); `future_projects.md`; `T2_specification.md` §4 corrected in place. **N/A but flagged:** `predictions.md` — PRED-C-96's row is **not** edited here, because the headline change belongs to EU-1 V1.6 and the registry should follow the paper, not lead it. **The next worker must not forget that predictions.md still carries 0.9649 ± 5×10⁻⁴.**
- **F** none (no panel). **G** no PD minted; no founder ruling. **H** this file.

## Governance notes
- **Two results a year old, in the same lane, never joined.** T-2 needed no new physics — only someone to read 0774 and 0766 together. Worth a periodic pass over the lane's own back-catalogue before opening new work.
- **A derived shift is not an error bar.** The distinction changed the paper's headline and would have been easy to miss by carrying the same number forward.
- **When a result changes a printed number, say so loudly and twice** — here in the finding, the handover, and the §15 E note about `predictions.md`.
