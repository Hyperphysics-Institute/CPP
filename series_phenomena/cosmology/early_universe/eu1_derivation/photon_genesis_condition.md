# C-5's adiabaticity condition, restated correctly — and the founder's photon-genesis picture as the candidate that meets it

**Patch 3934, Session 226, 11 Sep 2026. Lane: EU.** Supersedes the *wording* of the condition in `adiabaticity.md` (3908) and the FP-lane question in `../review/eu_outbound_questions.md` §1 (3928). Reasoning `../reasoning/3934_photon_genesis.md`. Founder source `../founders_voice/3934_photon_genesis_picture.md`. Bookkeeping + registration patch; no computation; no verify script. **C-5 remains a conditional pass. Nothing is reported as working. PRED-C-96, T-1, T-2, the count law: untouched.**

## 1. Why the 3908/3928 condition could not be answered as written

3908 conditioned C-5 on "the sea's q:e composition carries no net conserved quantum number — if it shifts baryon or lepton number, C-5 dies," and 3928 routed that to the FP lane. Corpus search before acting (D-1, D-3, D-7) found:

| what 3908/3928 assumed | what the corpus says | where |
|---|---|---|
| B and L are conserved quantum numbers the composition might carry | **B and L are not fundamental in CPP.** Only electric charge and energy-momentum are conserved; lepton number, baryon number and generation number are emergent cage-stability quasi-conservation | SF-2 v1.0 §(reorganization), shipped, three-reviewer |
| "qDP is an opposite-charge pair ⇒ no baryon content" is an EU-lane inference without standing | **It is a founder ruling.** Baryons are *unpaired* +qCPs, n_b = U_q/3; paired qDP/hDP/hTetra feedstock goes to DM | S3-M1, Patch 2520 (founder provenance) |
| the FP lane "owns η_B via leptogenesis at zero free parameters" | **η_B is the empirical anchor** back-derived to Δp_LR ≈ 0.04; CPP predicts χ/6, and η_B is "downstream ... beyond Capotauro's direct scope" | `predictions.md` PRED-O-25 |
| the composition variation is "vacuum structure that thermalises away" | **The pairing state thermalises; the species ratio does not.** qCP and eCP counts in a comoving patch are each conserved (the same conserved count the tilt relies on) and there is no q↔e conversion. A qCP-rich patch stays qCP-rich to baryon freeze-out | A1′; 3908's own premise |
| the FP lane could answer whether the unpaired inventory tracks local qCP abundance | **It cannot:** S3a Route α (pairing freeze-out kinetics) is BLOCKED; U_q was obtained by back-solving from η_B (Route β) | `relic1_s3a_uq_from_registered_anchors.md` |

So the question as routed was ill-posed (no B or L to carry) and, once posed correctly, unanswerable by either lane from the corpus. **The FP routing item in TODO-3930-EU is closed as reframed, not as answered.**

## 2. The condition, stated correctly

Photon number is not conserved; after thermalisation n_γ ∝ T³ is fixed by the energy released into a region, not by a count of emission events. Baryons are the unpaired +qCP residue. The isocurvature test is therefore on δ ln(n_B/s) across patches that differ in q:e composition by δ ln(n_q/n_e) ≈ 1.4×10⁻⁴ (3908, Hubble-coarse-grained), against ζ = 4.5×10⁻⁵ and a Planck bound on uncorrelated baryon isocurvature of a few percent of ζ:

> **C-5 passes adiabaticity iff the energy a region releases into the radiation bath and the number of baryons it retains scale identically with its local q:e composition.** Quantitatively, with n_B ∝ n_q and released energy ∝ n_q^a n_e^b, the residual composition-dependence |1 − a + b| must be ≲ 0.07 (for n_q ~ n_e). Baryon and DM yields must also co-vary (both are q-side per S3-M1, so this half is on file).

This replaces "carries no net conserved quantum number." **It is a statement about photon genesis at reheating, which the corpus has not specified. That is OPEN-EU-PHOTON-GENESIS-1** (registered in `research_frontier.md` at this patch; non-blocking; search mode per the founder's calibration stance).

## 3. The founder's picture, and where it lands

The founder's 11 Sep picture (founders_voice/3934) puts photon energy release on the **q side**: qDP-entity collisions and binding, more numerous and more energetic in qCP-rich volumes because the species are heavier and larger; eDP-side collisions contribute less. Under that picture radiation, baryons and DM all grow together with local qCP content — **the branch on which the ratio can be uniform, i.e. composition feeds the adiabatic mode.** On its face this is the surviving branch for C-5. It is *not* secured: collision rates go as density squared with mass-dependent cross-sections while baryon yield goes as the count, so the ≲7% proportionality of §2 is a calculable constraint to be met, not a given. Recorded as the **candidate mechanism** for OPEN-EU-PHOTON-GENESIS-1, not its closure.

**Consequence to carry (not computed here):** if composition drives energy release in proportion, composition is a *second* adiabatic source of ζ, of the same order as the unstacking source (3908: both coarse-grain to ~1.4×10⁻⁴). C-5's amplitude accounting must include it or risk double-counting. Flagged only.

**Two elements of the founder's text are not carried into the registrable core**, because they conflict with what the CMB is and would not survive review: (i) the CMB is not light transmitted from emitting volumes — its photons were made early, fully thermalised, and last-scattered at recombination ~380 kyr later from a plasma that retains only the *energy* per region, not the photon count or the source; (ii) "brighter CMB where there is more matter" is not observed — galaxies form ~10⁸ yr after last scattering, and on the largest scales overdense regions are slightly *colder* (Sachs–Wolfe). What the mechanism must deliver is a density/temperature ripple that the standard plasma physics then processes. Neither point damages the mechanism; both constrain how it is stated.

## 4. Standing after this patch

- C-5: **conditional pass, condition restated as §2**; condition owned by OPEN-EU-PHOTON-GENESIS-1; candidate mechanism registered.
- TODO-3930-EU "route the FP question": **closed — reframed**, no FP-lane action required. `eu_outbound_questions.md` §1 annotated, not rewritten (anti-erasure).
- 3928 §1.1 wording "owns η_B ... at zero free parameters": **corrected** by annotation.
- Wording rules: all nine of the master handover honoured; no number retracted here; 3920 not cited; "83 orders" absent.

**Worked at Patch 3936:** see `photon_genesis_passband.md` — the condition reduces to a pass-band in the inventory exponent p at the corpus-anchored release ratio ε = 2.70; both naive endpoints fail by 3–5×, not 30×; p not computed (NB-S3a-1).
