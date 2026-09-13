# SM-2 composition-level corrigendum — paste-ready (Patch 0942, CONV-038)

**Owed since:** Patch 3531 (12 Sep 2026, FORK-DM-COMPOSITION-1 resolved on the founder's ruling). **Prepared:** 13 Sep 2026, Patch 0942, from the chirality window under PD-006 — the SM lane holds no active ID block, so this artifact is filed in the 09xx block as a cross-lane deliverable (same precedent as 0936). **Verify:** `corrigenda/code/0942_down_charge_arithmetic.py` (5/5). **Target:** `series_standard_model/papers/SM-2_mass_generation_geometric_hierarchies.tex` — **shipped; not edited here.** Application is the founder's recompile.

**Founder ruling (3531, verbatim):** "the down quark is +qCP with a linearly oscillating -eCP, an orbital eDP, and a cloud of polarized CPs."

**Headline.** The corrigendum does not weaken SM-2 — it removes an internal inconsistency. SM-2's cage list, as written, **cannot reproduce SM-2's own charge section**: it gives the down −2/3, not −1/3. The founder's composition gives −1/3 exactly. Details in §2.

---

## 1. The three edits

### (a) Particle Cage Assignments — the down entry

Replace:

> \item Down: Central $-$qCP, $+$extra DP (2.5 eff.\ occupancy)

with:

> \item Down: Central $+$qCP, linearly oscillating $-$eCP extra, orbital eDP, polarised CP cloud ($N_k = 2.5$ eff.\ occupancy). \emph{(Composition corrected per FORK-DM-COMPOSITION-1, founder ruling 12 Sep 2026; the earlier entry's central $-$qCP with a neutral extra DP is inconsistent with the charge arithmetic of \S"Charge Quantisation" — see the corrigendum note.)}

### (b) §"Quark Charge Asymmetry and Capotauro" — the stabilisation sign

Replace:

> ...preferentially stabilises linear ZBW extras on negative ($-$qCP) centres.

with:

> ...preferentially stabilises linear ZBW extras on **positive** ($+$qCP) centres. \emph{(Sign corrected: the earlier statement is the anti-quark's, identified at Patch 3524. The bias operator is now derived rather than asserted — $\hat{C}^{qDP} = \chi\,(1/6)\,\hat{s}$, coupling to the sign of the central charge, Finding C-W46 as corrected at Patch 0937; the substrate's handedness supplies no preference among first-shell placements, only among centre signs.)*

### (c) §"Universal Refinements" — the species of the linear extra

Replace:

> \item Linear qDP/hDP ZBW extra for down-type quarks ($d=1$, $\sigma \approx 8.3 \times 10^{-3}$)

with:

> \item Linear $-$eCP ZBW extra for down-type quarks ($d=1$, $\sigma \approx 8.3 \times 10^{-3}$)

**The σ value and the d = 1 assignment are unaffected** — σ = 120⁻ᵈ counts unbound dimensions, not species, so the linear extra's dimensionality is what fixes it. Only the species label changes.

## 2. Why this strengthens the paper (the finding, verified 5/5)

SM-2's charge section fixes the screening exactly: the orbital ZBW inner pole screens the central qCP by δ = 1/3 (SM-1 Theorem 1; 1/φ² is an approximation to it). So an up-type centre reads +1 × (1 − 1/3) = **+2/3** (T1), and a down-type must land on **−1/3** — a gap of exactly **−1**, which the "linear ZBW extra" must supply.

- **A DP cannot supply it.** A DP is a bound CP/anti-CP pair and carries charge 0. SM-2's as-written down — central −qCP plus a neutral extra DP — therefore yields −1 × (1 − 1/3) + 0 = **−2/3**, not −1/3 (T2). The cage list contradicts the charge section.
- **The founder's composition supplies it exactly.** +qCP centre screened to +2/3, plus a linear −eCP at −1, gives **−1/3** (T3).
- **Scope of what the arithmetic proves.** Exactly two register species carry −1: −qCP and −eCP. Every neutral DP species fails (T4). So the charge arithmetic narrows the linear extra to a *charged* CP but does **not** by itself select which; the 3531 ruling selects −eCP. Stated this way because the first draft of the test asserted −eCP was the unique closer and the test refused it.

## 3. The mass fit — label-level, with one question

The down row of the Mass Contribution Breakdown (2.4 / 0.8 / 0.0 / 0.24 / 0.96 / 0.4 → 4.8 MeV) is driven by the effective occupancy N_k = 2.5, which the paper states is a structural assignment on geometric grounds. **The composition correction does not move N_k and therefore does not move any published number** — the corrigendum is label-level for the table as it stands.

**Open question (physics; founder's, not mine).** Whether the linear −eCP contributes a rest-mass term of its own that the current breakdown folds into the N_k = 2.5 assignment, or whether it is already accounted there. If it is a separate contribution, the down fit moves and the N_k calibration needs revisiting. I have not assumed either way.

## 4. Escalation — the question this corrigendum cannot settle

The cage list also assigns **Strange: Central −qCP** and **Bottom: Central −qCP**. These are down-type quarks carrying the same −1/3, and T5 confirms the −1 gap is identical for d, s and b and independent of cage occupancy. So the same charged linear extra is required for all three, and the same centre-sign question arises for all three.

**The 3531 ruling names only the down quark.** Whether it extends to strange and bottom — i.e. whether all down-type centres are +qCP with a linear −eCP, or whether the down is special — is a question in a physical picture and is escalated to the founder under PD-006(a). **It is not derived here and the s/b entries are left untouched.** If the answer is "all down-type", edits (a)–(c) generalise and two further cage entries change; if the down is special, the charge arithmetic for s and b needs its own account, since as written they inherit the same −2/3 problem as T2.

## 5. Sequencing

The Capotauro corrigendum from Patch 0937 (`capotauro.tex` §20.1/§20.2/§20.5/§20.6 + theorem step (iv)) should land **with or before** this one, so that SM-2's Capotauro section and Finding C-W46 quote the same operator. Both are paste-ready; both are founder recompiles. `chirality_continuum.tex` carries the same A₂u label at four places and bundles with them.

**No verdict moves. No number in SM-2 changes. No CPP paper is edited by this patch.**
