# Handover — THEO-CHIR-CAPACITY-1: Path A, Axis 1 done / Axis 2 open at the η-identity

**Arc:** Conscious Point Physics — Substrate Chirality Arc, chirality LANE (owns the spatial VERDICT + the DG-3 swarm review). A separate F.1/DSL window owns the computation/infrastructure.
**Date opened:** 9 June 2026 (Session 157).
**Predecessor context:** determination arc CLOSED (0903); CAPACITY-1 season (0907–0913); DG-3 swarm review returned **RESTATE** (0914/0915); Path A chosen (0916); spec-reviewed and refined (0917); F.1 computation assessed (0918).
**This document is both the durable record and the opening prompt for the fresh window. Paste it in to start; it tells the window to re-fetch itself from `handovers/` if context is lost.**

---

## LINE 1 — BLOCKING CLONE-AND-GREP GATE (do this before anything else)

Before you register an ID, place a file, compute a coefficient, or write a line of prose:

1. Clone the repo fresh.
2. `git log --oneline | head -30` — see the live frontier and which patch numbers are in use. **A second window (F.1/DSL + DM-2) pushes concurrently** in the 08xx and 1100–1400 bands. The chirality lane runs in the **09xx** band; you are at **0918**, so claim **0919+** after confirming free in `git log`. Collisions are real.
3. Read the §Required-reading files **in order** — do not re-open what is settled.
4. After every patch: `git pull` → `git am` → `git push` → **`git log --oneline -2` to confirm it landed on origin before switching context.** Push-misses have happened repeatedly this arc.

## KICKOFF SENTENCE (start here)

> *You are opening a fresh window on the Conscious Point Physics chirality lane; your sole target is to close (or honestly localize) **THEO-CHIR-CAPACITY-1** — the status theorem that substrate chirality FI-C-9 is a genuine irreducible **primitive** (spatial **V3 confirmed / V1 excluded**), conditional on Mechanism A. The verdict and the DG-3 swarm review are YOURS; the F.1/DSL window does the computation. The one open node is **Axis 2 of the Path-A closure = the η-identity**: prove that no admissible more-local η-observable is more strongly per-link correlated than the m=12 vertex figure.*

---

## Orientation — read this first

CAPACITY-1 went to the three-AI swarm and came back **1 CONFIRM / 2 RESTATE** (0914/0915) — **not a pass**; the verdict is **NOT enacted**. The convergent falsifier was **Q1**: C1 was a *sampled* mode-scan, not a proof that *every* admissible η is sub-critical. We chose **Path A** (0916): convert the scan into an exhaustive bound on two axes. **Axis 1 (which mode condenses, for a fixed observable) is ESTABLISHED** by the F.1 diagonalization (a_max ≈ 0.644 < 1, vertex-transitive ⇒ the row-sum bound is tight; 0918). **Axis 2 (which η-observable is dynamical — the "more-local η" worry) is OPEN.** The F.1 window's Axis-2 argument re-ran the *original* Gershgorin row-sum step, which ChatGPT correctly refuted (0917) and which I replaced with an observable-**monotonicity theorem** (L-CAP-A(ii)′); the F.1 window had not seen 0917 when it computed. **Your job: get L-CAP-A(ii)′ proven via the Perron route (below), or determine that it bottoms out at the η-identity.** Nothing re-fires and no verdict moves until Axis 2 closes. The framing guard is non-negotiable: **μ²>0 / off-critical ⇒ chirality PRIMITIVE, not emergent.**

## Where the arc stands (read this; do not re-open it)

- **Determination arc: CLOSED** (0903) — chirality reduces to one primitive FI-C-9 (spatial V3) + T-arrow sign(δ) (W3); V2/W2 excluded at axiom level; sole reopener = CPT-unified **OPEN-SM-4**.
- **CAPACITY-1 = the status-to-theorem move on the spatial axis.** Claim: the uniform det-coset order parameter ⟨η⟩ does not condense ⇒ FI-C-9 not dynamically generated ⇒ primitive ⇒ V3 confirmed / V1 excluded. Conditional on **Mechanism A** (OPEN-FP-F1-2).
- **Three discharged conditions (as fired to the swarm, 0912/0913):** C1 (η short-range + no candidate mode orders), C2 (O(δ³) current T-parity-suppressed at physical bias), C3 (both channels cleared: |K_lift|≈0.053 below uniform K_c≈0.095 *and* staggered K_c≈0.27=1/|λ_min|, λ_min=−3.708; conservative margin ≈44%).
- **DG-3 result (0914/0915): RESTATE, NOT a pass.** ChatGPT + Copilot RESTATE on Q1; Grok CONFIRM but did not engage the sample-vs-exhaustive gap. Q5 confirmed by all; framing guard drew no inversion flag. **Q3 fix already validated** (linking 0824/0825 resolved ChatGPT's earlier staggered-channel falsifier). **Q4** (reword chain to "every eigenmode / both modes") and **Q2** (carry "at the physical bias" as an explicit scope limit) are still **queued for the re-fire.**
- **Path A (0916 → refined 0917 → assessed 0918):**
  - **Axis 1 — DONE.** Real-symmetric M_eff has a complete eigenbasis; |K_lift|·a_max < 1 clears every mode. F.1 diagonalized the full operator: row sum ≈ 0.644 (NN 12×0.053 + d=2 20×0.0004), uniform mode saturates ⇒ a_max ≈ 0.644 < 1, far from the falsifier (18.9). 2nd shell computed, negligible.
  - **Axis 2 — OPEN.** The Gershgorin row-sum argument is **invalid for ordering different observables** (it bounds each operator by its *own* row-sum upper bound; m=12's row sum does not bound a more-local m′'s actual spectral radius). It tacitly assumes |C(m′)|≤0.053 and uniformity — which *is* the theorem.

## YOUR JOB: prove L-CAP-A(ii)′ by the Perron route, or localize the η-identity

The rigorous route (replaces Gershgorin; stated in 0918 §3): for real-symmetric M, ρ(M) ≤ ρ(|M|); and for non-negative matrices entrywise domination ⇒ spectral-radius domination. Therefore:

> **If `|C(m′)_ij| ≤ |C(12)_ij| = 0.053` entrywise for every admissible CHI-1-confined η-observable m′**, then ρ(M(m′)) ≤ ρ(|M(12)|) ≈ 0.644 < 1, and **Axis 2 closes**.

So the entire observable axis reduces to **one structural fact**: no admissible more-local η is more strongly per-link correlated than the full vertex figure. **That fact is the η-identity** — the node flagged all season as the one spot that might need Thomas's PCD-layer insight. It has now surfaced three times (C1 → DG-3 Q1 → Path-A Axis 2). Hand the Perron route to the F.1/DSL window (with 0917 + 0918 — it is missing both) and have it attempt the entrywise domination from the structure of the admissible observables.

## The decision gate (sharp, three outcomes — all useful)

1. **F.1 proves the entrywise domination** (|C(m′)| ≤ 0.053 ∀ admissible m′, structurally) → Axis 2 closes → **Path A closes** → reframe C1 to the exhaustive bound, fold the Q2/Q4 fixes (Q3 already done), and **re-fire the DG-3 package** (0912/0913) to the swarm. Pass = 3/3 CONFIRM.
2. **Proving it reduces to pinning the dynamical observable** → the η-identity is the **located irreducible residual**: CAPACITY-1 is provable *except* at this one fact. That is where Thomas's PCD-layer insight is genuinely called — answered sharply ("yes, here, and only here"), not vaguely.
3. **Fallback — Path B:** narrow CAPACITY-1 to "V1 excluded over the admissible local-η class with |C| ≤ 0.053, at the physical bias" — airtight now, weaker headline.

## Load-bearing facts (carry verbatim; flag if you challenge one)

- **Framing guard:** μ²>0 / off-critical = UNBROKEN branch = chirality **PRIMITIVE (V3)**, NOT emergent. Emergent (V1) is μ²<0 / condensed. Any "off-critical ⇒ emergent" wording is an inversion — reject it.
- **Numbers:** |K_lift| ≈ 0.053 (magnitude robust; **sign convention-dependent**, 0820). Uniform K_c≈0.095 (true; MF 0.083 / Bethe 0.091 / MC 0.100). Staggered K_c≈0.27=1/|λ_min|, λ_min=−3.708, λ_max=12. a_max(M_eff(12))≈0.644 (= |K_lift|/K_c). Conservative margin ≈44% (uniform = smallest threshold = worst-case sign); staggered cleared ≈80% (reinforcing, non-load-bearing).
- **V1 = breaking the global det-coset ℤ₂.** BOTH uniform (⟨η⟩≠0) and staggered (chirality-density-wave, ⟨η⟩=0 but the domains swap under the global flip) order break it → **both channels cleared** (NOT "staggered orthogonal" — that was 0912's soft spot, corrected in 0913 per 0825).
- Conditional on **Mechanism A** (OPEN-FP-F1-2); BRIDGE-1 kinematic/P2 cap inherited; sole reopener **OPEN-SM-4** (CPT-unified). CHI-1 (0638, review-closed 3/3) confines M_eff to the nearest neighbourhood — the closure rests on it.

## Scope guards (the DON'Ts)

- **Do not enact CAPACITY-1, move CHIR.md, register a THEO/ID, or change the prediction count** until a re-fired DG-3 returns **3/3 CONFIRM with no unresolved falsifier.** V3/W3 stand; OPEN-CHIR-1d-β stays OPEN meanwhile.
- **Do not accept the Gershgorin row-sum argument for Axis 2** — it is refuted (0917/0918). Axis 2 needs the Perron entrywise-domination proof.
- **Do not let momentum override the gap.** This arc has repeatedly seen one reviewer / the F.1 window assert a closure the dissenting (more rigorous) review had already broken. A 1-CONFIRM/2-RESTATE split is not a pass; a re-asserted refuted argument is not a proof.
- Lane discipline: chirality lane owns the VERDICT + DG-3; the F.1/DSL window does the computation. Don't do the F.1 window's diagonalization yourself; spec it and hand it off.

## Patch numbering

Chirality lane = **09xx**; you are at 0918 → claim **0919+** (confirm free in `git log` first). The F.1/DSL + DM windows use 08xx and 1100–1400 — leave those alone. Per the patch-delivery contract: after every `present_files` on a `.patch`, immediately output the apply-and-push block (one clause per line, `&& \` continuation, `cd ~/Documents/GitHub/CPP`, patch from `~/Downloads`), then have Thomas confirm `git log` shows it on origin.

## Required reading (in order, mapped to the work)

1. `bootup.md` (programme orientation + CLONE-FIRST GATE).
2. This handover (you are here).
3. `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/0918_LCAPA_computation_assessment.md` — current state + the **Perron route** for Axis 2.
4. `…/review/0917_pathA_specreview_refined_LCAPA.md` — the Axis-2 RESTATE + refined L-CAP-A(ii)′.
5. `…/review/0916_pathA_capacity1_closure_spec.md` — the Path A spec (note: its Axis-2 Gershgorin step is superseded by 0917/0918).
6. `…/review/0914_dg3_review_results_RESTATE.md` (+ 0915 Grok) — the DG-3 result + the Q2/Q3/Q4 fix list.
7. `…/review/dg3_capacity1_swarm_presentation.md` (0912/0913) — the live DG-3 package to re-fire (already has the Q3 "both channels cleared" fix).
8. `…/chirality_derivations/chirality_determination_closure.md` (0903) — the closed determination arc this builds on.
9. F.1-side source objects: `…/dynamical_substrate_law/sketches/residual1_dynamical_eta_identity.md` (0821, the M_eff/correlator), `residual3_afm_correction.md` (0824, λ spectrum), `residual3_true_Kc.md` (0823, true K_c).
10. `…/chirality_derivations/INDEX.md` — the arc patch index (0635 → 09xx).

## Honest expectation-setting

Axis 1 is genuinely closed; the whole verdict now hinges on **one structural fact about the admissible η-observables** (Axis 2 = the η-identity). Best case: the F.1 window proves the entrywise domination and a re-fire passes 3/3 — the first full status-to-theorem move on the spatial chirality axis. Realistic case: the domination proof reduces to pinning the dynamical observable, and you will have *precisely located* the one place CAPACITY-1 needs the PCD layer — which is itself the season's central question answered. Either way, the next decision is the F.1 window's L-CAP-A(ii)′ attempt; pending also the 3rd spec-review read (Copilot) if Thomas wants it before the re-fire.

## Pending threads (don't drop)

- **L-CAP-A(ii)′** handed to F.1 (Perron route, 0917+0918) — the decisive next computation.
- **Q2 + Q4 fixes** queued for the re-fire (Q3 done). 
- **3rd spec-review (Copilot)** of 0916 — optional before re-fire.
- On any re-fire PASS: enact in a separate patch (register CAPACITY-1; CHIR.md V3 confirmed / V1 excluded; resolve OPEN-CHIR-1d-β as "V1 excluded — confirmed primitive"; count unchanged; conditional on Mechanism A; reopenable only via OPEN-SM-4).
