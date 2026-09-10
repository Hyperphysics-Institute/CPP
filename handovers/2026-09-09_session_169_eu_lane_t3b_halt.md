# EU-lane Handover — Session 169 Close (9 Sep 2026) — the occupancy re-grounded; T-3b HALT; amplitude gap named

**Patch 3819. Lane: EU, block 3800–3899. Written under PD-006.**

## Orientation
**Repository state:** origin/main at Patch 3818 after push. **Lane:** EU, **next free: 3820** (run `python code/next_id.py eu` against a fresh clone before claiming). GR lane: highest used 3714 (cross-lane, Session 168), next free 3715.
**Active paper(s):** EU-1 at V1.5 (3817; **Isak owes the recompile**). GR-2 at V2.11 (3714; **Isak owes the recompile**).
**Parallel windows:** none known active.

## The single most important next action
**A new T-3a founder picture: what wavers slowly in the crowd?**

The charter's Q1 (§6) remains open. C-1 (the bath-energy mode δkT) was tested at 3818 and gives ζ = 0 — it is not a ζ source under the geometric end condition. The tilt stands. The amplitude gap is now precisely characterised: the δN bridge needs an end that depends on the fluctuating variable, and neither the count (conserved) nor the pairing pattern (frozen) nor the bath temperature (sets H but not N_*) fills that role under the simplest formulation. The next action is not a computation — it is a picture question to the founder:

**Q1 (charter §6, still open): In the crowd, is there anything that changes slowly — slower than the spreading itself — and changes more when the crowd is denser?** The count thins but doesn't waver; the spring settles every Moment (too heavy); the pairing was finished at the start; δkT wavers H but not the end. What is left that could differ from one large region to the next — the pace of the spreading, something in how the addresses hand the crowd along, something in how the bath couples to the end condition?

Default if unanswered: T-3a stays open, no computation on a guessed variable (PD-007), proceed to T-1 (homogeneity, nearly free, AP-4c check load-bearing).

## What was done this session

**3816 (prior context):** FORK-EU-OCCUPANCY-1 resolved → Branch P, small-ball reading, by founder ruling R-IGNITION-BALL-IN-ONE-PSR. The "large early PSR" phrase withdrawn: the ball is one Planck sphere, the reach is ordinary, everyone perceives everyone at Moment 1 because every register is empty (derived from AP-3/AP-4). Occupancy re-grounded: n̄ ≡ CPs within one rest-frame Planck sphere; N_* = ⅓ ln N_CP − ln(R_init/l_P) = 64.5 (10⁸⁴, l_P); pivot 57 survives; hierarchy consistency ≳ 3×10²⁷ GPs per l_P linearly (consistency, not input). OPEN-EU-PSR-EARLY-1 registered (PSR floor under saturated load; held vs perceived count; pass line = pivot survives). Files: `founders_voice/founder_ruling_ignition_ball_one_psr_2026-09-09.md`; `eu1_derivation/occupancy_regrounding.md`; verify 6/6; reasoning/3816. S-HENGINE-HELD wording note filed beside ratified text.

**3817 (prior context):** EU-1 → V1.5: honesty note (occupancy re-grounding; thirteen-GP seed superseded; large-early-PSR sentence re-grounded; OPEN-EU-PSR-EARLY-1 named). No equation changed. Isak owes recompile.

**3818 (this context):** T-3b first computation. δkT → ζ = 0, S = 0 under the geometric end condition (N_* = ⅓ ln N_CP; kT enters H_eff but not N_*; end condition n̄_end = 1 is kT-free). **HALT** (charter §4): S < 220 under C-1 (founder-supported). Tension registered against PRED-C-96's amplitude companion (A_s); tilt (n_s = 1 − 2/N_*) unaffected — kT-free. **OPEN-EU-AMPLITUDE-1** registered: two escape routes named but uncomputed (PSR-EARLY-1-mediated end condition; kT-dependent threshold from first principles). Files: `eu1_derivation/t3b_delta_kT_computation.md`; verify 4/4; reasoning/3818.

## Forward queue
1. **New T-3a founder picture** (Q1, above). HALT stops T-3b until a mode candidate gives ζ ≠ 0.
2. **T-1 homogeneity** (charter §2): twelve-per-GP (momenta cancel; bath born uniform) means T-1 is nearly free; deliverable is the statement plus the twelve-axis residual plus the AP-4c near-field check (§6 of `occupancy_regrounding.md`) — the near-field relay clause must deliver the full count to interior GPs; this is load-bearing for T-1 and should not be assumed silently.
3. **OPEN-EU-PSR-EARLY-1**: the PSR floor under saturated load; held vs perceived n̄; correction to N_*; pass line = the pivot survives. Not a founder question — a derivation, but OPEN for now.
4. **T-2** (charter §2): the ZRP correction coefficient (order-one times α; one or two sessions).
5. **CONV-046 candidate package**: re-grounding (3816) + S-HENGINE-HELD wording note + HALT (3818). **Panel only when T-3b clears or a CONV-046-grade picture result exists** (review economy §2).

**Anti-priorities:** no panel until T-3b clears; no minting κ₀ or any force law (PD-007); do not compute S on a guessed variable; do not retire 3710.

## §15 Steps A–H — completion record
- **A** Session log: `session_logs/2026-09-09_session_169_log.md` (3819).
- **B** Transcript pointer-map: `…/EU-1/documentation_suite/transcript-EU-1.md`, arc rows 3816–3818.
- **C** Development vignette: `…/documentation_suite/development-EU-1.md`, Session-169 entry (three paragraphs).
- **D** Tier 4: per-patch verbatim fragments — `…/early_universe/reasoning/3816_occupancy_regrounding.md` (prior context); `3818_t3b_delta_kT.md` (this context). 3817 was a bookkeeping patch; reasoning rider N/A (per Patch 3817 commit message).
- **E** Registries: `research_frontier.md` (3818 header prepend); `eu1_derivation/OPEN-EU-1_derivation_charter.md` §7 (3818 ledger entry); `id_block_registry.md` EU row (3819 → next free 3820); `future_projects.md` EU-lane status (3818 close). N/A: `predictions.md` (PRED-C-96 tilt unaffected; OPEN-EU-AMPLITUDE-1 is a registered tension, not a changed prediction row); `axiom-registry.md`; `theorem-registry.md`; `master_glossary.md` (OPEN-EU-AMPLITUDE-1 is a registered open item, not a glossary term); `paper_regeneration_ledger.md` (EU-1 ledger was updated at 3817; no further change).
- **F** Reviewer artifacts: none. No panel this session (HALT; review economy §2).
- **G** Protocol: no PD minted. Founder ruling R-IGNITION-BALL-IN-ONE-PSR registered (3816, prior context). One HALT registered against PRED-C-96's amplitude companion (3818).
- **H** This file.

## Pointer index (assets this session)
- Ruling: `founders_voice/founder_ruling_ignition_ball_one_psr_2026-09-09.md` (3816)
- Re-grounding: `eu1_derivation/occupancy_regrounding.md` (3816); verify `scripts/3816_occupancy_regrounding_checks.py` (6/6)
- T-3b finding: `eu1_derivation/t3b_delta_kT_computation.md` (3818); verify `scripts/3818_t3b_delta_kT_checks.py` (4/4)
- Charter: `eu1_derivation/OPEN-EU-1_derivation_charter.md` (§7 updated through 3818)
- Paper: EU-1 V1.5 (`EU-1/EU-1_primordial_spectral_index.tex`)

## Governance notes for the next worker
- The HALT is a gap in the derivation, not a falsification. PRED-C-96's tilt stands. The amplitude question is more precisely located now than it was before this session.
- Charter Q1 is the natural picture question. The founder answers picture questions with pictures, promptly. Ask one question per turn; state the default; never ask him to adopt a computed constant (PD-007).
- T-1 is likely fast under twelve-per-GP (momenta cancel by symmetry; bath born uniform). The one non-trivial item is the AP-4c near-field relay check: for a ball smaller than the reach, the interior must receive through the relay clause. Do not assume it silently.
- Isak: recompile EU-1 (V1.5) and GR-2 (V2.11).
