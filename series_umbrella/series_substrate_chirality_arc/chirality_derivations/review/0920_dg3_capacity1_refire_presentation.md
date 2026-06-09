# DG-3 Swarm Presentation — THEO-CHIR-CAPACITY-1 (RE-FIRE; Q1 closed by the row-sum invariant)

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/0920_dg3_capacity1_refire_presentation.md`
**Patch:** 0920 · **Type:** CONV-001 swarm-review package (RE-FIRE of the 0912/0913 package after the 1 CONFIRM / 2 RESTATE result, 0914/0915).
**Supersedes for review purposes:** `dg3_capacity1_swarm_presentation.md` (0912/0913) — that file is retained as the record of the first fire. Send the block below to each reviewer (ChatGPT, Grok, Copilot). On **3/3 CONFIRM with no unresolved falsifier**, the chirality lane enacts THEO-CHIR-CAPACITY-1 in a separate patch. **No verdict is moved by this patch** — V3/W3 stand and CAPACITY-1 stays reserved until the review returns.

---

## What changed since the first fire (read before sending)

The first DG-3 fire returned **1 CONFIRM (Grok) / 2 RESTATE (ChatGPT, Copilot)**; the two RESTATEs converged on the **same Q1 falsifier**: the C1 evidence was a `{m=4,6,8,12}` mode-**scan** (a sample), while the conclusion was phrased universally ("η disordered in *every* mode"). The split was therefore **not a pass**. This re-fire closes that gap and folds the documentation fixes:

- **Q1 (the convergent falsifier) — CLOSED by a closed-form proof, not a larger sample.** C1 is replaced by the **sign-correlation row-sum invariant** (Patch 0826, Perron route): the connected η-coupling is shared-edge-only, the per-link correlation is the Gaussian sign law `(2/π)arcsin(1/m)`, and Perron gives `ρ(M(m)) ≤ R(m) = m·(2/π)arcsin(1/m) < 1` for **every** admissible observable with support `m ≥ 2`. This is a bound over the **whole** admissible class, not a scan.
- **Honest correction carried (0826).** The originally-proposed Axis-2 sufficient condition (entrywise domination `|C(m′)| ≤ 0.053`) is **false** — a more-local observable is *more* per-link correlated, not less (`m=4 → 0.16 > m=12 → 0.053`); the scan's apparent "more-local → weaker" was a dilution artefact of the averaged mean. The correct invariant is the **row sum** `R(m)`, where fewer-but-stronger links trade off exactly. We disclose this rather than bury it.
- **Q3 documentation gap fixed.** The both-channels sources `0824` (AFM correction) and `0825` (threshold reconciliation) are now linked, and `0823` is forward-annotated (its "staggered ≠ V1" framing was corrected by 0825).
- **Q2 scope limit made explicit:** the current argument is carried "at the physical bias δ = φ⁻³," stated, not buried.
- **Q4 chain reworded** to the all-eigenmodes / both-channels form.

---

## ⬇️ Paste the following to each reviewer (one 4-backtick block per reviewer)

````
# Multi-AI Review Request (RE-FIRE) — THEO-CHIR-CAPACITY-1 (Conscious Point Physics)

This is a re-review. A prior round returned 2 RESTATE / 1 CONFIRM, converging on one falsifier (Q1): the universality of the no-condensation result rested on a finite mode-scan (a sample), not a proof. That gap is now closed by a closed-form spectral bound (below). Please adjudicate afresh and adversarially — we want falsifiers, not agreement.

**Source files (GitHub, Hyperphysics-Institute/CPP, branch main):**
- C1 closure — sign-correlation row-sum invariant (the Q1 proof; replaces the mode-scan):
  blob: https://github.com/Hyperphysics-Institute/CPP/blob/main/series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/lcapa_axis2_signcorr_closure.md
  raw:  https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/lcapa_axis2_signcorr_closure.md
  verify script: https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/code/0826_lcapa_signcorr_rowsum.py
- η construction (the per-edge measure C1 is derived on):
  raw:  https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/residual1_dynamical_eta_identity.md
- C2 — O(δ³) non-equilibrium current completeness:
  raw:  https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/residual2_current_check.md
- C3 — thresholds + both-channels (read all three; 0823 carries a forward-correction note):
  raw:  https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/residual3_true_Kc.md
  raw:  https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/residual3_afm_correction.md
  raw:  https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/threshold_reconciliation.md
- Determination-arc context (the closed 3/3 theorems this builds on):
  raw:  https://raw.githubusercontent.com/Hyperphysics-Institute/CPP/main/series_umbrella/series_substrate_chirality_arc/chirality_derivations/chirality_determination_closure.md

**The ask.** Adjudicate the proposed theorem THEO-CHIR-CAPACITY-1 below against Q1–Q5. For each, answer CONFIRM or FALSIFY with a one-line reason; then give an overall verdict (CONFIRM / FALSIFY / RESTATE). The verdict-moving claim is **spatial V3 confirmed / V1 excluded, conditional on Mechanism A**. A CONFIRM should mean "I tried to break this and could not."

---

**THEO-CHIR-CAPACITY-1 (proposed).** The CPP substrate does **not** spontaneously develop a net global handedness: the det-coset order parameter η (the sign(n̂) / H₄→H₄⁺ enantiomorph condensate) does not condense — in **any** admissible mode of **any** admissible local observable. Therefore the observed substrate chirality FI-C-9 is **not dynamically generated** — it is a **genuine irreducible primitive (Foundational Input)**. **Verdict: spatial V3 confirmed, V1 (emergence-by-condensation) excluded.**

*Framing (please check, do not assume):* μ²>0 / off-critical / ρ(coupling) < 1 is the UNBROKEN branch ⇒ chirality **primitive**, NOT emergent. The emergent outcome (V1) would be the opposite branch (μ²<0 / ρ ≥ 1 / condensed). "Off-critical ⇒ emergent" would be an inversion.

*Scope:* V1 = spontaneous breaking of the **global** det-coset ℤ₂ (the η→−η enantiomorph flip), via **either** a **uniform** order (⟨η⟩≠0, net global handedness) **or** a **staggered** order (chirality-density-wave: ⟨η⟩=0, but the two staggered domains swap under the global flip, so ℤ₂ is still broken). Both are genuine ordering channels and **both** are cleared — and the spectral-radius bound below clears both at once (it bounds |λ| for the most-positive/uniform and most-negative/staggered eigenmodes together). This is a *status* theorem (chirality is a primitive input), NOT a derivation of chirality.

**The evidence (three discharged conditions):**

- **C1 — no admissible η-observable condenses, proved over the whole class (Patch 0826; replaces the 0821 mode-scan).** Each candidate order parameter is η_v = sign(Σ_{e∈R_v} w_e x_e) over a read set of m edges, on the Mechanism-A measure with **per-edge-independent** fluctuations. Two consequences, both verified on the real measure:
  (i) **The connected coupling is shared-edge-only.** Neighbours v,w share exactly one fluctuating input — the common edge variable x_{vw} (common *neighbours* contribute different, independent edge variables). So the connected correlator is nearest-neighbour only; measured d≥2 correlation ≈ 0.005 ≈ 0. The coupling matrix M is therefore nn-only. (NB: the *response* matrix (1−M)⁻¹−1 is dense and has spectral radius > 1 even when M does not — the criticality object is M, not the measured full correlation.)
  (ii) **Per-link correlation is the Gaussian sign law** C(m) = (2/π)·arcsin(1/m) (shared-edge correlation ρ=1/m; verified m=2→0.333, m=4→0.161, m=12→0.053 against the measure). Each vertex reads m edges ⇒ at most m reciprocal links ⇒ by Perron–Frobenius, **ρ(M(m)) ≤ ρ(|M(m)|) ≤ max row sum ≤ R(m) := m·(2/π)arcsin(1/m).** R(m) is monotonically decreasing with R(1)=1, R(2)=2/3, R(∞)=2/π≈0.637 — so **R(m) < 1 for every m ≥ 2** (critical only at the degenerate single edge m=1). The fewer-but-stronger trade-off is exact: more-local = fewer links × proportionally stronger links = invariant row sum ≈ 2/π. Numerically ρ(M(m)) = 0.59–0.64 for m=2…12 (matching R(m) and reproducing the m=12 Axis-1 value 0.644), ρ→1 only at m=1.
  *This is a closed-form bound over the entire admissible observable class, not a sample.* **Correction we are explicit about:** the route one might first try — entrywise domination |C(m′)| ≤ 0.053 — is **false** (more-local links are *stronger* per link); the correct sufficient condition is the row-sum invariant R(m)<1. The only critical observable is m=1 (a single oriented edge), which carries no handedness; a 4-D enantiomorph indicator needs ≥4 independent directions, so the physical admissibility floor is m≥4 (R(4)=0.643, margin 36%) — non-load-bearing, since the closure already holds for all m≥2. *Load-bearing input (Q1/Q5):* the shared-edge-only structure, hence the whole bound, rests on **per-edge independence** of the Mechanism-A measure; long-range fluctuation correlations in that measure would revive d≥2 coupling and require R(m) to be re-derived. This is a sub-case of the standing Mechanism-A conditionality and is stated as the load-bearing assumption.

- **C2 — the O(δ³) non-equilibrium current neither shifts the threshold nor drives ordering, at the physical bias (Patch 0822).** The Mechanism-A NESS current scales as δ^3.09 (O(δ³)), is tiny at the physical bias δ=φ⁻³ (J≈3×10⁻⁵), and is divergence-free. The current is T-odd while η-ordering is T-even, so it couples to ordering only at even powers, O(J²)=O(δ⁶)≈0.0002 — far below the margin. *Explicit scope (Q2):* this is a parametric/symmetry argument **at the physical bias δ=φ⁻³**, not an all-orders NESS proof.

- **C3 — η is off-critical in every mode; both ordering channels cleared (Patches 0823–0825, now fully linked).** The effective coupling magnitude is robust, |K_lift| ≈ 0.053; its sign is convention-dependent. η=0 (the symmetric primitive state) is stable iff the coupling is below the binding threshold of whichever mode binds: **uniform/FM** K_c ≈ 0.095 (mean-field 0.083 / Bethe–Peierls 0.091 / finite-N MC ≈0.100); **staggered/AFM** K_c ≈ 0.27 (= 1/|λ_min|, λ_min=−3.708; AFM MC: staggered susceptibility flat to |K|≈0.20). |K_lift|≈0.053 is below **both** ⇒ disordered in every mode regardless of sign ⇒ no det-coset breaking, uniform *or* staggered. **Conservative headline margin ≈ 44%** (against the uniform threshold, the smallest, so it binds for the worst-case sign; this is the honest number). **Reinforcing ≈ 80%** against the staggered threshold. Equivalently, the C1 spectral bound makes this one statement: ρ(M)≤R(m)<1 bounds |λ| for *both* the most-positive (uniform) and most-negative (staggered) eigenmodes — so both channels are cleared by a single invariant. *Caveat:* thermodynamic K_c can only exceed these finite-N estimates, so the margins only widen.

**Standing conditionalities:** conditional on **Mechanism A** (the substrate rate law, OPEN-FP-F1-2) — and specifically on per-edge independence of its measure (C1, §load-bearing); bridge-side statements inherit a prior kinematic/premise cap (BRIDGE-1); the only route that could later reopen the sign is the cross-sector SM CP/T phase (OPEN-SM-4), untouched here.

**Questions:**
- **Q1 (universality — the prior falsifier).** Is C1 now sufficient as a **proof over the whole admissible class**? Specifically: does the row-sum invariant ρ(M(m)) ≤ R(m) = m·(2/π)arcsin(1/m) < 1 (m≥2), resting on shared-edge-only coupling + the Gaussian sign law, exclude condensation for **every** admissible local η — including more-local and non-uniform observables — rather than a sample? Is the entrywise-domination correction sound, and is the per-edge-independence caveat the right (and only) load-bearing residual?
- **Q2 (the current).** Does C2 rule out a threshold shift and current-induced (e.g. staggered) ordering **at the physical bias**, or does the parametric/symmetry argument leave a gap that matters for a Mechanism-A-conditional status theorem?
- **Q3 (the comparison).** Is C3 sound — is |K_lift|≈0.053 below **both** the uniform (≈0.095) and staggered (≈0.27) thresholds, and does the spectral-radius bound ρ(M)≤R(m)<1 correctly subsume both channels at once? Is the **conservative ≈44%** (uniform, worst-case sign) the right binding margin to headline?
- **Q4 (logic + framing).** Is the chain "**every eigenmode of every admissible observable off-critical (ρ(M)<1, both channels)** ⇒ no det-coset breaking ⇒ μ²>0 ⇒ V3 confirmed / V1 excluded" valid, and is the **primitive (not emergent)** reading correct (no inversion)?
- **Q5 (scope/honesty).** Is the Mechanism-A conditionality (including the per-edge-independence sub-condition) correctly carried; does the claim avoid overclaiming (confirms primitive, does not derive chirality); are the temporal axis and OPEN-SM-4 correctly left untouched?

Please be specific about any falsifier.
````

---

## After the three responses come back

Record each reviewer's Q1–Q5 answers + overall verdict in a results note (`092x_dg3_refire_results.md`). **PASS = 3/3 CONFIRM, no unresolved falsifier.** On PASS, the chirality lane enacts (separate patch): register THEO-CHIR-CAPACITY-1; set CHIR.md spatial verdict **V3 confirmed / V1 excluded**; resolve **OPEN-CHIR-1d-β** as *V1 excluded — chirality is a confirmed primitive*; state conditional on Mechanism A (incl. per-edge independence), reopenable only via OPEN-SM-4; header count unchanged (status theorem). On any FALSIFY/RESTATE, address it before enacting; V3/W3 stand meanwhile.

## Scope held

This patch banks the RE-FIRE review package only. **No verdict moved, no THEO registered, no ID consumed, no CHIR.md verdict edit, no count change.** The Q1 closure (C1) is the F.1-lane result 0826, assessed and adopted here by the chirality lane for review; conditional on Mechanism A (OPEN-FP-F1-2).
