# DM-2 — Step 0: Audit of OPEN-SR-5 and the c08 Dependency

**Patch:** 0802 (Session 156, 8 June 2026) · **Work item:** DM-2 / R2 / OPEN-SR-5 · **Type:** audit (not a derivation)
**Predecessor:** the DM-2 kickoff handover (Patch 0798); the Sea-gravitation arc A→D (Patches 0720–0723).
**Verify:** none (audit is a read-and-reconcile deliverable; no computation).

---

## Purpose

Step 0 of the DM-2 falsification-first sequence: read OPEN-SR-5a/b/c/d, `R2_sea_gravitation_scoping.md`, `step2_bookkeeping.md`, and `c08_strong-field_GR.tex` in full; state precisely what SURVIVES vs what is PARTIAL/CONDITIONAL; and pin the exact c08 dependency. This is an inventory before any new physics, so the arc does not re-derive what is already settled.

## Headline

R2 / OPEN-SR-5 is **not a wall and not closed.** The falsification-first sequence A→D was already traversed once (0720–0723) with **no kill**, Friedmann recovered, and — contrary to the DM-2 kickoff handover's framing — the (l_P/R_H)² coincidence-restatement was **already replaced** by a substrate derivation at Patch 0722. The genuinely remaining open work is narrower and sharper than "make the Λ-suppression real."

## Stale-framing reconciliation (handover vs on-disk)

The DM-2 kickoff handover (0798) described 5b as *still* resting on the (l_P/R_H)² coincidence-restatement and posed the job as "make it a real derivation — or show it cannot be done." That framing predates the on-disk A→D state. `stepC_lambda_suppression.md` and the SR.md OPEN-SR-5b entry show the restatement was **replaced** at 0722 (scaling and 1/8π coefficient derived). The handover also omits Steps B and D entirely. The handover has been corrected at Patch 0804 to point here. **Work from the A→D state.**

## Per-item status (OPEN-SR-5, actual on-disk)

| Sub-item | Step | Status | What it establishes |
|---|---|---|---|
| 5a | A | **SURVIVES** (0720) | Friedmann reconciliation via the Milne–McCrea shell theorem. "Uniform Sea locally inert" and "uniform matter drives expansion" are the same fact two ways; no BBN/CMB conflict. |
| 5c | B | **DELIVERED, structural** (0721) | Sea-vs-matter distinction: CPP gravity couples to the **excess** ΔSSV above the local ground state, not to absolute energy. Uniform Sea → zero source; matter/swirls/Λ all gravitate as excesses. *This is the handover's "cheapest kill" (uniform vs inhomogeneous) — and it survives structurally.* |
| 5b | C | **PARTIAL, upgraded** (0722) | Coincidence-restatement **replaced**. ρ_Λ ~ c⁴/(8πG R_H²) = (1/8π)·ρ_P·(l_P/R_H)²; scaling **and** 1/8π coefficient **derived**; ρ_Λ within factor ~2 of observed; dynamical Λ ∝ H² ("why now"). Open: exact coefficient, IR-scale choice, w(z). |
| 5d | D | **CONDITIONAL CAPSTONE** (0723) | D1 Friedmann recovery **PASS** (q crosses zero, decel→accel, at z≈0.63 vs observed ~0.6–0.7). D2 ground-state exclusion **CONDITIONAL** (rests on c08 field-equation reduction). D3 horizon/w(z) **RESOLVED** to the future event horizon (holographic; w_Λ≈−1.02), but *why* the event horizon is underived. |

The handover's "cheapest kill first" — does the mechanism that suppresses the uniform Sea also suppress the inhomogeneities? — is structurally answered by Step B's excess-sourcing: a uniform Sea sources zero gravity (constant g_tt → zero curvature) while matter, swirls, and Λ all gravitate as excesses by the same mechanism, differing only in what the gradient is. It survives, **conditional on c08**.

## The pinned c08 dependency (the key deliverable)

The c08 field equation (Proposition "field_eq") is

    ∇_λ∇^λ(Δ|SSV|) + 𝓕[PSR_eff, Δ|SSV|] = (8πG/c⁴) T,   T = ρ_mass c²,

with the nonlinear feedback term

    𝓕 = [2k(Δ|SSV|)² / (1 + kΔ|SSV|)²] · ∇_λ∇^λ ln(1 + kΔ|SSV|).

Two facts about c08 *as written* pull apart in a way the current audit trail conflates:

1. **The gravitating source is the excess.** The LHS operator acts on Δ|SSV|; the rigorous exact-Schwarzschild source is k·Δ|SSV| = GM/rc²; absolute |SSV| enters **only** the metric-value mapping (|SSV|_abs → g_tt), where a uniform Sea gives a *constant* g_tt → zero curvature → non-gravitating. A grep confirms: **nowhere does c08 source gravity from absolute |SSV|.** So falsifier D2-1 ("closed field equation sources from absolute |SSV| → ground state gravitates → break") is **not realized in c08's current written form** — it is built the right way by construction and confirmed by the exact Schwarzschild theorem.

2. **What c08 actually leaves open** (its stated central unsolved problem, Open Problem 1) is whether the *full nonlinear* 𝓕 term reproduces the exact Einstein G_μν in the **strong-field** regime. That is a **separate and stronger** question than D2's excess-sourcing requirement.

**Audit finding.** Both the handover and the SR.md D2 entry tie D2's CONDITIONAL status to c08's "central challenge not yet solved" — but that central challenge is *strong-field nonlinear Einstein equivalence*, which D2 does **not** need. D2 needs excess-sourcing / ground-state exclusion, and the relevant cosmological background is **weak-field/linear-order** (Friedmann), the regime where c08's reduction to linearised Einstein is already *proved* (companion 7). So D2's true dependency on c08 is **narrower** than the trail states. The genuinely under-controlled piece is not the qualitative ground-state exclusion — it is the **Λ-magnitude at the IR/horizon scale**: the 5b coefficient (factor ~2) and the D3 event-horizon selection, which sit at the IR edge where the weak-field expansion is least controlled.

## Go/no-go read (feeding the R2 feasibility question)

**Go, but the remaining risk has moved.** It is not "derive the Λ-suppression" (largely done, factor ~2) and not "ground-state exclusion" (structurally in hand, conditional only on a *weak-field* c08 property already proved). The two real, named derivation targets are:

- **(i) separability of D2 from c08 Open Problem 1** — can ground-state exclusion be established from c08's *established* results alone (excess-sourcing form + exact Schwarzschild + proved weak-field reduction), without the unproven strong-field nonlinear closure? If yes, the c08 dependency de-risks to the weak-field regime. If no, D2 is gated on c08's hardest open problem — the wall signal.
- **(ii) event-horizon selection (D3)** — why the CPP Sea IR coherence scale is the future event horizon; this also fixes the 5b coefficient and w(z).

The separability test (i) is the cheapest decisive next move (the real **Step 1**) and runs at Patch 0805.

## Side-flags raised by this audit (both actioned)

- **c08 PCD drift — FIXED at Patch 0803.** c08 expanded PCD as "Polarize–Capture–Depolarize" (the Session-146 drift); corrected to the canonical "Perceive–Compute–Displace." Legitimate terms ("ZBW polarization cloud", the cited "Captured Dipole Particle" paper title) left untouched.
- **Handover 5b framing stale — FIXED at Patch 0804.** See reconciliation above.

## Deferred (registry freeze)

The SR.md OPEN-SR-5 entry warrants a status note reflecting the Step-0/Step-1 findings (narrowed c08 dependency). Per the multi-window registry-freeze discipline (chirality window active at 0902), **all `frontier_sectors/` edits are deferred to a single batched registry patch** once the Step-1 result is in hand.

## Scope held

This audit does not move any verdict: CONJ-COSMO-1 remains NOT-confirmed; LEMMA-DM-CONSIST-1 remains consistency-grade; no THEO, no swarm-count change, no `theorem-registry.md`/`predictions.md` edits. The bank-and-release strategy and the 0797 priority date stand unchanged.
