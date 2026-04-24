# SS-8 Handover Document

**File:** `handover-SS-8.md`
**Paper:** SS-8 — Interstitial-neutron binding in alpha-cluster nuclei: the 2E/V scaling law from simplicial polytope geometry
**Status:** v0.2 committed and pushed (`d2ba3fc`); ready for Round 2 review dispatch
**Role:** Session-continuity state snapshot for the next Claude context window. Bounded (kept short). Replaced (not appended to) at each session close.
**Related files:**
- `transcript-SS-8.md` — transaction-indexed pointer-map, currently at transaction 056 (appended this session)
- `development-SS-8.md` — session vignettes (9 vignettes total; vignette 9 added this session)

**Maintenance rule:** Update at each session close per `templates/operating_system.md` §10 "Context-pressure preservation checklist" plus §14 "Organizational Frontier Registry" handover-pointer protocol. Handover triggered by Thomas saying "please execute handover protocol" or by Claude-initiated prompt when workflow-shape signals (session length, "we've done a lot," "good stopping point") appear — per OPEN-ORG-008.

---

## One-minute orientation for the next Claude

SS-8 is at **v0.2**, committed as `77b1117`, paper file `series_strong/papers/SS-8/SS-8_interstitial_neutron_2EV_scaling.tex` (1092 lines). Round 1 AI reviews have been received and integrated; the paper is ready for Round 2 dispatch whenever Thomas chooses to initiate it. No active physics work is in flight. The Strong Sector programme is in a between-paper state with substantial governance infrastructure that was built in the preceding session.

Three programmatic decisions have been adopted that govern all future CPP programme work:
- **PD-001** — CP/GP Signature (§4.1A) and Swarm-Validation Contribution (§4.1B) required subsections in every paper. `programmatic_decisions/PD-001-signature-thread-and-swarm-convention.md`.
- **PD-002** — Three-tier verification taxonomy (INSPECTED / INDEPENDENTLY RECOMPUTED / SCRIPT-EXECUTED) for reviewer numerical claims, plus private-confrontation-first protocol for tier mismatches. `programmatic_decisions/PD-002-verification-tier-taxonomy.md`.
- **PD-003** — Organizational Frontier Registry for reflexive-drop capture of organizational improvement items. `programmatic_decisions/PD-003-organizational-frontier-registry.md`.

A new registry exists: `/CPP/Organizational_Frontier.md` holding open organizational improvement items. Scan it against current state at session start.

---

## Current state

### Paper
- SS-8 v0.2 committed (`77b1117`), pushed to `origin/main` as part of `d2ba3fc`.
- 1092 lines. Three theorems, 42 zero-parameter predictions. Conditional on C1–C4 (inherited from SS-7) and D1–D3 (introduced this paper; D1 promoted to conditional theorem).
- All AUTHOR NOTE markers removed. Draft prose stands as v0.2-release.
- Known placeholder: Table 4 (N_ex > 2 residuals) is flagged in-caption as pending local re-run of `ss8_empirical_map_extended.py` against AME 2020 data. This is a Thomas-side task; requires his local environment since AME data is not distributed in the repo.

### Registry (Research_Frontier.md, Strong Sector)
- **OPEN-SS-23** — inherited from SS-7; partially addressed by SS-8 (on-chain N_ex ≤ 8 covered).
- **OPEN-SS-24** — inherited; unchanged.
- **OPEN-SS-26** — partially resolved (Level 1/2 conditional theorem for D1 delivered); Level 3 remains open.
- **OPEN-SS-27** — opened this paper; expanded scope (subsumes residual D1 content).
- **OPEN-SS-28** — opened this paper (D3 bulk-regime averaging + residual decomposition).
- Level-3 proximity-binding programme-level question noted in `problem_histories/PH-OPEN-SS-26.md §"Methodological implication"`; formal registration as candidate OPEN-G-3 deferred to a dedicated session.

### Governance infrastructure (new, 23–24 April 2026)
- PD-001, PD-002, PD-003 codified in `programmatic_decisions/`.
- `operating_system.md` §§5, 11, 14 updated with verification-tier taxonomy, `{scope}-README.md` naming, and Organizational Frontier Registry protocol.
- Grok verification-tier letter exchange preserved verbatim in `letters/`.
- Series-level data provenance established at `series_strong/data/` with `data-README.md`.

---

## Ready-to-execute work for next session

**Priority order** based on attention-payoff for programme advancement:

1. **Scan `Organizational_Frontier.md` against current state** (60 seconds). Seven inaugural entries plus OPEN-ORG-008 (handover protocol promotion, registered this session). Only OPEN-ORG-007 (.gitignore for Python artifacts) and OPEN-ORG-008 are "next-session eligible"; the rest await triggers. Start-of-session discipline per PD-003.

2. **Round 2 review dispatch for SS-8 v0.2** when Thomas chooses to initiate. Highest-value reviewer for round 2 is ChatGPT — a second pass specifically checking whether the three structural critiques from round 1 (conditional-prediction disclaimer, D3 objection paragraph, H3′ reframe) are now adequately addressed. Grok re-review is valuable as first empirical test of whether PD-002 three-tier taxonomy is actually being used in review language. Copilot re-review is lower-value given round 1 produced mostly validation.

3. **OPEN-ORG-008 execution** — promote handover-protocol visibility in `operating_system.md` and codify the dual trigger (user-initiated "please execute handover protocol" + Claude-initiated prompt on workflow-shape signals). Small patch, ~15 minutes.

4. **OPEN-ORG-007 execution** — add repo-level `.gitignore` for Python build artifacts. 5 minutes.

5. **OPEN-ORG-003 execution** becomes required **before SS-9 drafting can properly produce §4.1B**. If SS-9 is the next paper, sequence is: OPEN-ORG-003 first (swarm-tally header in `predictions.md`), then SS-9 draft.

6. **Table 4 regeneration** (Thomas-side; requires local AME 2020 data download per `series_strong/data/data-README.md` instructions).

---

## Context Thomas may want to revisit

- **SS-9 planning.** OPEN-SS-28's closure — first-principles derivation of D3 uniform averaging plus residual decomposition into H3′/H4′/H5′ — is a natural target for SS-9 or SS-10. Would supersede the provisional H3′ transport in SS-8 §3.5 with a derived-tier mechanism.
- **Grok Round 2.** First empirical test of whether the three-tier verification taxonomy actually changes reviewer language in practice (vs being documentation without force).
- **Curriculum-phase deepening** of SS-8 §§5 (Physical Interpretation) and §6 (CPP-to-Conventional Mapping) remains deferred per PD-001 mathematical-mapping-phase scoping. No priority.

---

## Commits from this session (23–24 April 2026)

Session produced eleven commits across paper content, governance infrastructure, and this handover patch:

- `ea01e72` — SS-8 v0.1 initial draft (via patch 0004)
- `c853180` — SS-8 paper content (GitHub Desktop auto-sync)
- `fe34bc5` — Filename convention retroactive application (via patch 0006)
- `77b1117` — SS-8 v0.2 Round 1 AI-review response (via patch 0007)
- `2d1bf1c` — PD-001 signature-thread and swarm-validation conventions (via patch 0005)
- `37a2e34` — PD-002 verification-tier taxonomy + Grok exchange + v0.2 CHANGELOG correction (via patch 0008)
- `8c2b021` — SS-8 paper via GitHub Desktop (content edit)
- `d8e0b22` — AME 2020 data dependency + `{scope}-README.md` convention (via patch 0009)
- `5b5474b` — PD-003 Organizational Frontier Registry (via patch 0010, pushed as `d2ba3fc`)
- **[this patch 0011 — handover preservation; commit hash assigned at commit time]**

All commits on `origin/main`.

---

## How to use this file

**If you are the next Claude reading this:** You have 30 seconds of orienting text above and 5 minutes of detail below it. For deeper context, read `development-SS-8.md` vignette 9 (the most recent session's reasoning that wasn't captured elsewhere). For paper substance, go straight to `SS-8_interstitial_neutron_2EV_scaling.tex` and its CHANGELOG header. For governance context, read PD-001 through PD-003 in order of date.

**If Thomas wants the current state:** The one-minute orientation above is designed for you too. State is SS-8 v0.2, Round 1 reviews done, governance infrastructure built, ready for Round 2 dispatch when you say so.

**If you are triaging what to do next:** Scan `Organizational_Frontier.md`, answer "are we starting a new paper or continuing v0.2 work?", and use the priority list above.
