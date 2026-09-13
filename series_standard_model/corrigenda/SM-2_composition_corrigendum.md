# SM-2 composition-level corrigendum — paste-ready (Patches 0942 + 0943, CONV-038)

**Owed since:** Patch 3531 (12 Sep 2026, FORK-DM-COMPOSITION-1 resolved on the founder's ruling). **Prepared:** 13 Sep 2026, Patch 0942, from the chirality window under PD-006 — the SM lane holds no active ID block, so this artifact is filed in the 09xx block as a cross-lane deliverable (same precedent as 0936). **Extended 13 Sep 2026, Patch 0943,** on the founder's instruction to fix the other SM particles carrying the wrong charge. **Verify:** `corrigenda/code/0942_down_charge_arithmetic.py` (5/5) and `corrigenda/code/0943_sm2_charge_audit.py` (6/6 — a full audit of every cage entry against SM-2's own charge rules). **Target:** `series_standard_model/papers/SM-2_mass_generation_geometric_hierarchies.tex` — **shipped; not edited here.** Application is the founder's recompile.

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

## 4. Extension to strange and bottom (founder ruling, 13 Sep 2026)

The founder has ruled that the fix extends. The full audit (`0943_sm2_charge_audit.py`, 6/6) confirms the defect is exactly the down-type family and nothing else among the fermions: **down, strange and bottom are each written with a central −qCP, which screens to −2/3 against a required −1/3**, and no neutral DP species rescues any of them (T3). The required gap is −1 for all three despite cage occupancies of N_k = 2.5, 30 and 3000 — **cage-independent, so the repair generalises exactly** (T4). Up-type (u, c, t) at +2/3, the charged leptons at −1 as unscreened eCP centres, and the neutrals (ν's, Z, Higgs) are all correct as written and owe no correction (T1, T2).

### (d) Particle Cage Assignments — strange

Replace:

> \item Strange: Central $-$qCP, tetrahedral cage ($N_k = 30$ eff.)

with:

> \item Strange: Central $+$qCP, linearly oscillating $-$eCP extra, orbital eDP, polarised CP cloud, tetrahedral cage ($N_k = 30$ eff.)

### (e) Particle Cage Assignments — bottom

Replace:

> \item Bottom: Central $-$qCP, tetrahedral+icosahedral+dodecahedral ($N_k = 3000$ eff.)

with:

> \item Bottom: Central $+$qCP, linearly oscillating $-$eCP extra, orbital eDP, polarised CP cloud, tetrahedral+icosahedral+dodecahedral ($N_k = 3000$ eff.)

Edits (b) and (c) of §1 already read "down-type" and therefore cover s and b without further change. Add to the corrigendum note: *"The central-charge and linear-extra assignments for all three down-type quarks are corrected together; the −1/3 charge is cage-independent, so no cage-size argument distinguishes them (Patch 0943)."*

**Mass fits for s and b are label-level exactly as for the down** — N_k = 30 and N_k = 3000 are unmoved, so no published number changes. The same open question carries across all three: whether the linear −eCP contributes a rest-mass term of its own or is already folded into N_k.

## 4b. A third defect, found by the audit: the W boson

Not previously flagged, and **not covered by the founder's down-type ruling.**

The cage list assigns **"W: Linear hDP chain"**, and the mass table row reads "Linear 6-hDP chain". An hDP chain is a chain of *bound neutral pairs* and therefore carries charge **0** — so the assignment describes a neutral object, while W^± carries ±1 (T5). The Z (icosahedral cage) and the Higgs (dodecahedral cage) are genuinely neutral and are unaffected: **the defect is specific to the charged member of the weak triplet.** After the d/s/b repair, W is the **single residual entry** in SM-2 that cannot reproduce its own charge (T6).

**This one is not closable by arithmetic.** The audit says the chain needs a net ±1 from somewhere — a charged constituent, or an asymmetric termination of the chain — but which is a composition question, and the founder has ruled only on the down quark. **No edit is proposed here and the W entries are left untouched.**

*Pointer, offered for the founder's consideration and explicitly not a derivation:* CPP already carries a structure of exactly this shape elsewhere — the "odd man out" / partnerless third of Patch 3513 (a bare qCP attached to a DP entity), which is the W/W′ channel the DM lane's E3 count uses (3531). A linear hDP chain carrying a partnerless bare CP would supply the ±1 and would reuse an existing mechanism rather than introduce one. Whether that is the right picture for the W is the founder's call.

## 5. Sequencing

The Capotauro corrigendum from Patch 0937 (`capotauro.tex` §20.1/§20.2/§20.5/§20.6 + theorem step (iv)) should land **with or before** this one, so that SM-2's Capotauro section and Finding C-W46 quote the same operator. Both are paste-ready; both are founder recompiles. `chirality_continuum.tex` carries the same A₂u label at four places and bundles with them.

**No verdict moves. No number in SM-2 changes. No CPP paper is edited by these patches.** Residual after application: the W entry only (§4b), pending a founder composition ruling.
