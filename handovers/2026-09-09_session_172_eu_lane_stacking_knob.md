# EU-lane Handover — Session 172 Close (9 Sep 2026) — the stacking knob: the budget constrains the total CP count, not the arrangement

**Patch 3826. Lane: EU, block 3800–3899. Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3824 at session start; 3825–3826 delivered as patch files. **Next free: 3827.** GR lane: next free 3715.
**Active paper(s):** EU-1 V1.5 (**Isak owes the recompile**; source verified clean in-container at Session 170). GR-2 V2.11 (**Isak owes the recompile**).
**Parallel windows:** none known.

## The single most important next action
**The VSL horizon computation** (OPEN-EU-EFOLD-BUDGET-1 route 1). Unchanged from Session 171 and still first: the 3823 audit assumed a fixed-c horizon integral while EU-1's background is FRW/VSL, and VSL is the only route that moves the *requirement* rather than the supply. Everything found this session sharpens the alternative route but does not displace this one.

**Second action, new this session:** OPEN-EU-EFOLD-BUDGET-1 **route 2 is now specific** — supply N_CP ≈ 5×10⁹⁷ from the DP-sea density rather than by calibration. The independent pin is **n_CP(today) ≈ 1.4×10¹⁷ m⁻³** (mean separation ~1.9 μm). Confront it with the DE-lane Λ/sea work and SF-6's ε₀/μ₀. If either lands on 10¹⁷ m⁻³, the budget closes without a fitted parameter.

## What was done this session
**3825 — the founder's stacking proposal assessed** (`founders_voice/founder_proposal_calibrate_stacking_2026-09-09.md`; `eu1_derivation/stacking_knob_assessment.md`, verify 6/6).
- **Generalisation owed to 3823 and made:** N = ln(l_P/s) + ⅓ln k + ⅓ln(4π/3). 3823's identity held the founder's k = 12 tacitly. Occupancy **is** a genuine second knob — the budget closes at k ≈ 5.8×10¹⁴ per GP at fixed lattice.
- **The finding:** both knobs enter only through the total count. Stacking → N_CP = 4.8×10⁹⁷; resolution → 5.0×10⁹⁷; an independent end-condition check (one CP per Planck sphere over a **6.0 mm** ball at N = 75) → 5.2×10⁹⁷. **The budget constrains how many CPs exist, not how they are arranged.** Master relation: N = ⅓ln N_CP − ln(R_init/l_P).
- **Cost (a):** k ≈ 5.8×10¹⁴ is the crowd-at-one-address the founder **retracted at 3814** — the retraction that opened the fork and produced the small-ball ruling. Flagged for his ruling; **not re-adopted by arithmetic**. Priced correctly: T-1 survives a k/12-per-icosahedral-vertex stack (the ℓ ≤ 5 result is about directions, not occupancies), and AP-5 permits saturation by depth, so the objection is to his own words and nothing else.
- **Cost (b):** calibration against the observed size is barred by charter bar (1) / PD-007. It would cost the e-fold total's zero-parameter status; it would **not** cost the tilt (n_s reads the adopted pivot 57).
- **The disciplined form:** N_CP was never independently pinned — EU-1's 10⁸⁰ and the founder's 10⁸⁴ are *matter* counts, while CPP holds most CPs sit in the DP sea. So the gap may be an output of sea density, not a free parameter. Targets registered as targets, not adopted.

## Forward queue
1. **VSL horizon computation** (EFOLD-BUDGET-1 route 1). Top item.
2. **Sea-density confrontation** (EFOLD-BUDGET-1 route 2): does an independent CPP determination give n_CP ≈ 1.4×10¹⁷ m⁻³?
3. **Founder picture question standing** (assessment §6): *is the twelve literal, or the pattern rather than the population?* Default if unanswered: twelve is literal; the budget is carried by route 1 or 2; **no calibration either way**.
4. **C-2's end-condition bridge**, then its spectrum argument. No δN computation before the bridge.
5. **T-2** — the O(α) ZRP coefficient. Unblocked and unaffected; the right fallback if 1–2 stall.
6. **EU-1 V1.x note owed** — resolution/occupancy dependence, budget tension, T-1 species qualification. Write once EFOLD-BUDGET-1 resolves so it lands with its outcome.
7. **CONV-046 package:** 3816 (+§2b correction) + S-HENGINE-HELD wording note + 3818 HALT + 3820 T-1 (+3822 amendment) + 3823 audit (+§4b) + 3825. Contains a win, a halt, and three self-corrections.

**Anti-priorities:** no calibration of k, s, or N_CP against an observable (PD-007); do not re-adopt the retracted stack by arithmetic; no computation on C-2 before its bridge; do not retire 3710; the ℓ = 6 residual is not an observable; never report the budget tension as a change to n_s.

## §15 Steps A–H
- **A** `session_logs/2026-09-09_session_172_log.md` (3826). **B** transcript row 3825. **C** development vignette (Session 172).
- **D** Tier 4: `reasoning/3825_stacking_knob.md`.
- **E** Registries: `research_frontier.md` (3825 prepend); `efold_budget_audit.md` §4b (generalisation); `id_block_registry.md` (next free 3827); `future_projects.md`. N/A: `predictions.md` (tilt untouched; targets are not predictions until derived), `axiom-registry.md`, `theorem-registry.md`, `master_glossary.md`.
- **F** none (no panel). **G** no PD minted; no founder ruling (a proposal, offered for evaluation). **H** this file.

## Governance notes
- Four of the worker's own claims corrected across 3820–3825 (E-2's quadrupole; the AP-4c target; 3816's resolution claim and wrong bound; 3823's tacit k = 12). Keep doing this in the worker's own words.
- The founder proposes knobs; the useful reply is to turn the knob quantitatively, say exactly how far it must turn, and name what that costs against his own prior rulings — not to invoke PD-007 as a conversation-stopper.
- Recompile in-container on every version change and report pages/errors — standing request from Session 170.
