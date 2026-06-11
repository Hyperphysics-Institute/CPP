# Handover — Cosmological-Constant Reconciliation (umbrella): unifying the three CPP vacuum-energy accounts and closing the DM R2 gate

**Arc:** Conscious Point Physics — cross-sector umbrella (SR + SM + Foundations + Cosmology/DM).
**Open problems:** `OPEN-SR-5` (CC from vacuum DP Sea, GR side) ↔ `OPEN-SM-6` (CC from CPP vacuum, SM side); gates DM requirement **R2** (`OPEN-COSMO-DM-1`).
**Date opened:** 10 June 2026 (Session 156), initiated from the 1000-series Project-C window. **Assigned by Thomas; to be run in the 1100 series, its own window.**
**This is both the durable record and the opening prompt for a fresh window. Paste it in to start; re-fetch from `handovers/` if context is lost.**

---

## KICKOFF LINE (paste to start a session)

```
Bootup for Conscious Point Physics (CPP). Clone the repo and read the bootup file at https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/bootup.md. Honor the line-1 CLONE-FIRST GATE before registering any ID, placing any file, or computing any coefficient (clone the repo and grep the registry first). Then open the handovers/ folder, sort by filename, and read the most recent dated file — then load THIS file: 2026-06-10_session_156_CC_reconciliation_umbrella.md.
```

## BLOCKING CLONE-AND-GREP GATE (before anything else)

1. Clone fresh; `git log --oneline | head -30` — see the live frontier and free patch bands (multiple windows push concurrently; the strong-sector Project-C window is in the 1000s, the DM lane in the 08xx).
2. **Claim the 1100 band** confirmed against `git log` (1100–1199; do not reuse any label already in history). Record a Round-2 base_ref = current HEAD.
3. Read the §Required reading in order before computing or deriving.
4. CLONE-FIRST: never register an ID, place a file, or compute a coefficient before cloning + grepping the registry.

## KICKOFF SENTENCE

> *You are reconciling CPP's **three different accounts of the cosmological-constant suppression** into one consistent mechanism, and wiring that mechanism explicitly to the dark-matter identification's R2 gate. The three accounts give the right ~10⁻¹²⁰ number for incompatible reasons — one dynamical/horizon-based, one static/substrate-based, one resting on an unverified Grid-Point count. The deliverable is: which suppression is physical, are SR-5 and SM-6 the same theorem, does the DP-Sea N⁴ claim survive without the 10³⁰ crutch, and does the uniform-Sea-inert mechanism actually deliver the "uniform Sea doesn't gravitate / swirls do" split that the DM claim needs. This is the gate on the qDP/hTetra → dark-matter identification.*

## Orientation — read this first

CPP "solves" the cosmological-constant problem in **three places that have never been reconciled**, and the inconsistency is now load-bearing because the DM identification depends on it. (A) The cosmology sector (`OPEN-SR-5`, Patches 0720–0727) derives ρ_Λ ~ (1/8π)·ρ_P·(l_P/R_H)² — a **dynamical, horizon-scale** suppression landing within a factor ~2 of observed, predicting a time-varying Λ. (B) The SM sector (`OPEN-SM-6`, last touched March 2026) has a "pairing-cancellation" estimate good to ~an order of magnitude. (C) The DP-Sea composition flagship asserts ρ_vac ~ ρ_sea/N⁴ ≈ 10⁻¹²⁰ ρ_Planck — a **static substrate ratio** — stated as "resolved," but resting on **N ≈ 10³⁰**, the unverified Grid-Point-per-l_P estimate (Grok-origin, never processed; the same shaky number flagged in the 1004/1005 framing correction), and sitting in the *same paper* as the TODO-016 error. The frontier already carries the standing instruction that SR-5 and SM-6 "must not be derived inconsistently." The single most important first action: **do NOT pick a favorite and polish it — first lay the three accounts side by side and decide which suppression is physical**, because (A) is dynamical and (C) is static and *they cannot both be the fundamental explanation.* The whole DM R2 gate hangs on the answer.

## Why this umbrella exists (the precise motivation — it is the DM gate)

The dark-matter identification Thomas is staking — *qDP/hTetra swirls ARE dark matter* — has a requirement **R2** (`series_phenomena/cosmology/dark_matter/R2_sea_gravitation_scoping.md`) that is **gated on `OPEN-SR-5`**: the uniform Dipole Sea must **NOT** gravitate cosmologically (else Ω_Sea ~ 10⁴⁵–10¹²⁰ — the vacuum catastrophe) **while its swirl-inhomogeneities DO** gravitate as dark matter. That is one mechanism with two outputs: uniform mode → suppressed Λ (dark energy), inhomogeneities → DM. So the CC problem and the DM identification are the same substrate question seen from two ends. **You cannot close "qDP/hTetra are dark matter" without the uniform-Sea-doesn't-gravitate half — which is the CC.** This is why the CC reconciliation is the gate, not a side-quest.

## The crux (state it sharply before computing)

The three accounts agree on the *number* (~10⁻¹²⁰) but disagree on the *physics*:

- **(A) (l_P/R_H)² is dynamical.** R_H grows with cosmic time, so this predicts ρ_Λ ∝ H² — a **time-varying** Λ (Λ was larger in the past; "why now" addressed). Horizon/holographic in character.
- **(C) N⁴ is static.** N is a fixed substrate property, so ρ_sea/N⁴ is a **constant** — Λ does not evolve.

These make **different predictions for Λ(z)** and cannot both be fundamental. Worse (or better), there is a numerical coincidence to resolve: today `R_H/l_P ~ 10⁶¹` and `N² ~ (10³⁰)² = 10⁶⁰` are the same order, i.e. **R_H ≈ N²·l_P at the present epoch** — which is *exactly why* the static N⁴ and the dynamical (l_P/R_H)² accounts coincide *now* and would diverge at other epochs. That coincidence is either (i) the "why-now" problem in disguise (favoring the dynamical reading and demoting N⁴ to a present-epoch accident), or (ii) a genuine substrate relation R_H ~ N²l_P to be derived (which would tie the horizon to the Grid-Point count and unify the two). **Deciding between (i) and (ii) is the heart of this umbrella.** Verify the orders first (`l_P`, present R_H, the claimed N); do not trust the 10³⁰ until it is checked.

## What "done" looks like (reconciliation targets)

1. **Audit the N⁴ account.** Does ρ_vac ~ ρ_sea/N⁴ survive without the 10³⁰ crutch? Either *derive* N from substrate combinatorics (600-cell / Sea structure) independently of the answer, or **retire the claim** in the DP-Sea paper (it is currently asserted as "resolved" — same epistemic error class as TODO-016, in the same paper).
2. **Decide static vs dynamical.** Determine which of (A)/(C) is physical, using the Λ(z) difference and the R_H ≈ N²l_P coincidence as the discriminant. Settle whether Λ is constant or evolving in CPP. (This also bears on the SR-5 event-horizon-selection open question.)
3. **Make SR-5 and SM-6 one theorem.** Per the standing frontier instruction, produce a single mechanism that both sectors inherit, not two estimates that happen to agree.
4. **Wire it to the DM R2 gate.** Show explicitly that the reconciled mechanism delivers uniform-Sea-inert + gravitating-swirls, discharging R2 for the DM identification (coordinate with the DM 08xx lane).

## Proposed umbrella structure (it is "widespreading" — give it children)

Like the Substrate Chirality Arc, this likely warrants a **Series Umbrella container** with sub-threads, run as a small multi-window round in the 1100 band:

- **CC-U/1 — N⁴ audit** (foundations): derive-or-retire N; pin the 10³⁰. *(Cheapest potential kill — do first.)*
- **CC-U/2 — static-vs-dynamical** (SR/cosmology): Λ(z); the R_H ≈ N²l_P coincidence; event-horizon selection.
- **CC-U/3 — SR-5 ↔ SM-6 unification** (SR+SM): one mechanism, two sectors.
- **CC-U/4 — c08 closed field equation** (the deep dependency): the excess-sourcing reduction G_μν = 8πG/c⁴·T_μν[LSP] that c08 itself calls a conjecture — *the single deepest risk in the whole cosmological sector*. Everything else rests on the ground state being excluded from the source.
- **CC-U/5 — DM R2 discharge** (cosmology/DM): connect to the dark-matter identification; coordinate with the 08xx lane.

## Required reading (in order)

1. `frontier_sectors/SR.md` — `OPEN-SR-5` and the Step A–D entries (the derived (l_P/R_H)² + 1/8π, the conditions).
2. `frontier_sectors/SM.md` — `OPEN-SM-6` (pairing cancellation; the "same theorem" cross-link).
3. `frontier_sectors/CONJ.md` — the DM R2 scoping and the OPEN-SR-5 ↔ OPEN-COSMO-DM-1 cross-link.
4. `series_phenomena/cosmology/sea_gravitation/stepA_…` through `stepD_…` and `scripts/0720_…`–`0723_…` (the derivation + verify scripts; **do not** re-derive 0722, it is done).
5. `series_phenomena/cosmology/dark_matter/R2_sea_gravitation_scoping.md` — the gate definition.
6. `series_foundations/dp_sea_composition/DP_sea_and_cage_composition.tex` — the N⁴ ≈ 10⁻¹²⁰ claim (line ~64) and N's provenance.
7. `series_relativity/SR_companion_papers/c05_…`, `c07_…`, `c08_strong-field_GR.tex` — gravity from SSV excess; the c08 field-equation conjecture.
8. `master_glossary.md` (post-1005) — PSR / SSV_abs / Grid Point; the 10³⁰ caveat.
9. TODO-014 — "absolute scale is one shared calibration, not derived" (the calibration stance the strong-sector arc converged on; the CC is the *suppression ratio*, a different question from the absolute anchor).

## Suggested approach (falsification-first)

Run CC-U/1 first (cheapest kill: if N⁴ cannot survive without 10³⁰, retire it and the field narrows to A-vs-conditions). Then CC-U/2 (static vs dynamical — the physics fork). Only after the suppression mechanism is settled, attempt CC-U/3 unification and CC-U/5 the DM wiring. Treat CC-U/4 (c08) as the standing deep dependency that may cap the whole thing at "conditional," exactly as it currently caps OPEN-SR-5. At each step, check: does the account reproduce ρ_Λ ≈ 5.3×10⁻¹⁰ J/m³ from substrate quantities **without** inserting the answer (no fitted horizon, no fitted N)?

## The deepest risk

c08's closed field equation — that gravity sources from the SSV **excess** (ground state excluded) rather than absolute |SSV| — is a **conjecture** c08 itself flags as unsolved. Both the no-CC-catastrophe result *and* the DM uniform-Sea-inert split rest on it. If the closed field equation sources from absolute |SSV|, the ground state gravitates, the catastrophe returns, and **both** the CC suppression and the DM R2 gate break together. This is the one place the umbrella can fail wholesale; everything else is reconciliation of accounts that individually almost work.

## Falsifier

If no single substrate mechanism can (i) suppress the uniform-Sea vacuum energy to ρ_Λ ≈ 5.3×10⁻¹⁰ J/m³ without inserting the horizon or N by hand, **and** (ii) simultaneously leave swirl-inhomogeneities gravitating at DM amplitude, then the dark-energy↔dark-matter unification fails and the DM identification loses its R2 leg. Sub-falsifier (CC-U/1): if N cannot be derived independently, the DP-Sea N⁴ claim is retired as unsupported.

## On success

A single CPP mechanism yielding suppressed-Λ + unsuppressed-inhomogeneity-gravity + Friedmann recovery: a **dark-energy ↔ dark-matter unification from one substrate**, discharging DM R2, collapsing OPEN-SR-5 and OPEN-SM-6 into one theorem, and resolving the static-vs-dynamical Λ(z) question. This is the keystone for the qDP/hTetra → dark-matter paper.

## Scope / window / collision note

Cross-sector (SR + SM + Foundations + Cosmology/DM) — **its own 1100-series window**, base_ref recorded at start. It will touch shared registries (`frontier_sectors/*`, `predictions.md`, `future_projects.md`, `todolist.md`, possibly `master_glossary.md`) and the DP-Sea flagship — all **integrator-only / batched** under the lightweight two-window protocol; flag before writing any of them. The DM **08xx** lane is adjacent (R2 cross-link) — coordinate, do not edit `dark_matter/` from this window. The strong-sector **1000s** lane (Project C) is independent. Registering this umbrella into `future_projects.md` / `frontier_sectors/` is itself a shared-registry action and should be a flagged INT patch, not folded into the handover-creation patch.
