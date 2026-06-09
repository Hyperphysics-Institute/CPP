# DG-3 Swarm Presentation — THEO-CHIR-CAPACITY-1 (RE-FIRE #2; C1 = pointwise refined-chord bound, piece-1 conditionality surfaced)

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/0924_dg3_capacity1_refire2_presentation.md`
**Patch:** 0924 · **Type:** CONV-001 swarm-review package (third fire). **Supersedes for review:** 0920 (re-fire #1) and 0912/0913 (first fire) — retained as records.
**Bar:** PASS = 3/3 CONFIRM with no unresolved falsifier. On PASS the chirality lane enacts CAPACITY-1 in a separate patch. **No verdict moved by this patch** — V3/W3 stand, CAPACITY-1 reserved.

---

## What changed since re-fire #1 (read before sending)

Re-fire #1 (0920) returned **2 CONFIRM / 1 RESTATE** (0921). All three accepted the old Q1 (sample→proof) as discharged, and confirmed Q2–Q5. ChatGPT's lone RESTATE landed a **real** falsifier: the row-sum bound `R(m)` assumed *equal-weight* reads; a weighted observable can concentrate on one shared edge and approach the critical single-edge case. The chirality lane verified it and the C1 closure was then rebuilt:

- **0826** equal-weight closure (`ρ ≤ R(m) < 1`) — sound but equal-weight only.
- **0827** first weighted-class attempt — claimed "homogeneity ⇒ max row sum = avg ≤ 1." The chirality lane (0922) **falsified this** with an explicit n̂-dependent counterexample (avg row sum ≈ 0.60 but max = 1.0, ρ = 1.0 at *mean* participation ≈ 2.6): an n̂-dependent rule is the same form everywhere but is **not** H₄-invariant, so its row sums are not equal.
- **0828** the repair, **adopted** (0923): a **refined-chord quadratic-form bound**, `ρ(M) ≤ κ(z*) = (2/π)arcsin(z*)/z* < 1`, with **no homogeneity assumption**, under a **pointwise** participation floor. Independently verified (analytic + 120 adversarial non-homogeneous weightings, 0 violations).

So C1 is now the pointwise κ-bound, and the only open item is a **single, explicitly named physical conditionality** (piece 1 below), not a hidden math gap. That is what this fire adjudicates.

---

## ⬇️ Paste the block below to each reviewer (one 4-backtick fence; full content in §"presentation block")

The CONV-001 single-paste block is delivered separately. Reviewers should adjudicate the proposed theorem against Q1–Q5; the live question is **Q1 (is the pointwise κ-closure sound and exhaustive, with no 0827-style hidden gap?)** and **Q5 (is "the dynamical η is pointwise non-degenerate" acceptable as a Mechanism-A sub-conditionality?)**.

---

**THEO-CHIR-CAPACITY-1 (proposed, re-fire #2).** The CPP substrate does not spontaneously develop a net global handedness: the det-coset order parameter η does not condense — in any mode of any admissible **pointwise non-degenerate** local observable. Therefore the observed substrate chirality FI-C-9 is **not dynamically generated** — it is a genuine irreducible primitive (Foundational Input). **Verdict: spatial V3 confirmed, V1 (emergence-by-condensation) excluded — conditional on Mechanism A, including pointwise non-degeneracy of the dynamical η.**

*Framing (check, do not assume):* off-critical / `ρ(M) < 1` is the UNBROKEN branch ⇒ chirality **primitive**, NOT emergent. The emergent outcome (V1) is the opposite branch (condensed). "Off-critical ⇒ emergent" is an inversion.

*Scope:* V1 = breaking of the global det-coset ℤ₂ (η→−η), via a **uniform** order (⟨η⟩≠0) or a **staggered** order (⟨η⟩=0 but domains swap under the global flip). Both channels are covered — `ρ(M)` bounds `|λ|` for the most-positive and most-negative eigenmodes together. Status theorem (chirality is a primitive input), not a derivation of chirality.

**The evidence (three discharged conditions):**

- **C1 — no admissible pointwise-non-degenerate η condenses (closed-form, no homogeneity; Patches 0826 + 0828).**
  - *Shared-edge-only coupling (0826):* on the per-edge-independent Mechanism-A measure, the connected η-coupling is nearest-neighbour only; the per-link entry is `M_vw = (2/π)arcsin(c^v_{(v,w)}·c^w_{(v,w)})` with per-vertex normalization `Σ_{w~v}(c^v_{(v,w)})² = 1`.
  - *Refined-chord spectral bound (0828):* `g(z) := (2/π)arcsin(z)/z` is increasing on `(0,1]`, so for `z ≤ z*`, `(2/π)arcsin(z) ≤ κ·z` with `κ := g(z*) < 1`. Then for any unit `x`,
    `|xᵀMx| ≤ 2κ Σ_edges c^v c^w |x_v||x_w| ≤ κ Σ_edges[(c^v)²x_v² + (c^w)²x_w²] = κ Σ_v x_v² = κ`.
    Hence **`ρ(M) ≤ κ(z*)`**, where `z*` = max single-edge weight-product `≤ c_max²`. **No homogeneity, no vertex-transitivity** — this holds for n̂-dependent (non-uniform) rules, the family that defeated the earlier `R(m)`/`max=avg` arguments.
  - *Pointwise floor:* admissibility = **pointwise non-degenerate**, `p(v) ≥ 4` at every vertex (`Σ_e (c^v_e)⁴ ≤ 1/4 ⇒ c_max(v) ≤ (1/4)^{1/4} = 0.707 ⇒ z* ≤ 0.5`). Then **`ρ(M) ≤ κ(0.5) = 2/3 < 1`, margin 33%.** Verified: 120 adversarial non-homogeneous weightings respect `ρ ≤ κ(z*)` (0 violations); tight construction `ρ = 0.616 ≤ 2/3`.
  - *History, stated for adversarial review:* the equal-weight `R(m)` bound (0826) and the "homogeneity ⇒ max=avg" argument (0827) were **both** insufficient/false for the weighted class; 0827 was falsified by an explicit counterexample. The present bound is the repair and assumes neither equal weights nor homogeneity — only the pointwise cap.

- **C2 — the O(δ³) non-equilibrium current neither shifts the threshold nor drives ordering, at the physical bias (Patch 0822).** NESS current `~δ^{3.09}`, tiny at `δ=φ⁻³` (`J≈3×10⁻⁵`), divergence-free; T-odd vs T-even η-ordering ⇒ couples only at `O(J²)=O(δ⁶)≈2×10⁻⁴`. Parametric/symmetry argument **at the physical bias**, not all-orders. *(CONFIRMed by all three reviewers in re-fire #1.)*

- **C3 — η off-critical in every mode; both ordering channels cleared (Patches 0823–0825).** `|K_lift|≈0.053` below both uniform (`K_c≈0.095`) and staggered (`K_c≈0.27`) thresholds; the single `ρ(M) ≤ κ < 1` bound clears both channels at once. Conservative headline margin ≈ 44% (uniform). *(CONFIRMed by all three in re-fire #1.)*

**Standing conditionalities:** conditional on **Mechanism A** (OPEN-FP-F1-2), specifically on (i) per-edge independence of its measure (C1 shared-edge step) and (ii) **pointwise non-degeneracy of the dynamical η** (the piece-1 input, see Q5); bridge-side statements inherit BRIDGE-1's prior cap; the only sign-reopener is the cross-sector SM CP/T phase OPEN-SM-4, untouched.

**The two honest pieces (stated up front):**
- **Piece 2 — the bound: proven.** Pointwise `c_max ≤ c* < 1 ⇒ ρ(M) ≤ κ(c*²) < 1`. Closed form, homogeneity-free, verified.
- **Piece 1 — the residual: that the *dynamical* η is pointwise non-degenerate.** That a genuine local handedness is non-degenerate at every vertex is *definitional* for "handedness field"; whether the substrate's dynamics *guarantees* the dynamical η is pointwise non-degenerate (rather than degenerating at n̂-extremal vertices) is the η-identity in its narrowest form. We carry it as a Mechanism-A sub-conditionality; **Q5 asks whether you accept that.**

**Questions:**
- **Q1 (the math — is C1's closure sound and exhaustive?).** Is the refined-chord bound `ρ(M) ≤ κ(z*) = (2/π)arcsin(z*)/z*` correct, and does pointwise `p(v) ≥ 4` ⇒ `ρ ≤ 2/3 < 1` exclude condensation for **every** admissible pointwise-non-degenerate local η — uniform or n̂-dependent/non-uniform — with **no** residual gap of the kind that broke the earlier `max=avg` argument (0827)? Is the homogeneity-free quadratic-form step valid?
- **Q2 (the current).** Does C2 rule out a threshold shift / current-driven ordering at the physical bias for a Mechanism-A-conditional status theorem?
- **Q3 (the comparison).** Is C3 sound — `|K_lift|≈0.053` below both thresholds, `ρ(M)≤κ<1` subsuming both channels, ≈44% the right conservative headline?
- **Q4 (logic + framing).** Is the chain "every mode of every pointwise-non-degenerate observable off-critical (`ρ(M)<1`, both channels) ⇒ no det-coset breaking ⇒ V3 confirmed / V1 excluded" valid, with the **primitive (not emergent)** reading correct (no inversion)?
- **Q5 (the conditionality — the live scope judgment).** Is **"the dynamical η is pointwise non-degenerate (`p(v) ≥ 4` everywhere)"** acceptable as a sub-condition of Mechanism A — on the same footing as per-edge independence? I.e. is pointwise non-degeneracy **definitional** for a genuine local handedness field (so the theorem is effectively universal over handedness fields), or must it be **derived** from the substrate dynamics (leaving the residual live)? And does the theorem otherwise avoid over-claiming (confirms primitive, does not derive chirality; temporal axis and OPEN-SM-4 untouched)?

Please be specific about any falsifier, and distinguish a *falsifier* (a broken step) from a *scope/conditionality judgment* (Q5).

---

## After the three responses

Record Q1–Q5 + overall verdicts in `092x_dg3_refire2_results.md`. **PASS = 3/3 CONFIRM, no unresolved falsifier.** On PASS: enact CAPACITY-1 (separate patch) — register THEO-CHIR-CAPACITY-1; CHIR.md spatial **V3 confirmed / V1 excluded**; resolve **OPEN-CHIR-1d-β**; conditional on Mechanism A (incl. per-edge independence + pointwise non-degeneracy), reopenable only via OPEN-SM-4; count unchanged (status theorem). If a reviewer rejects the Q5 conditionality but finds no Q1 falsifier, fall back to the **Path B** narrowed theorem (0925) — V1 excluded over the explicitly non-degenerate class, unconditional on piece 1.

## Scope held

Banks the third-fire review package only. **No verdict moved, no THEO registered, no ID consumed, no CHIR.md edit, no count change.** C1 closure = 0826 + 0828 (adopted 0923); conditional on Mechanism A.
