# OPEN-DM-RELIC-1 — the Ω_DM route-B relic-abundance campaign (asymmetric DM via a shared Sea asymmetry), scoped for candidate (B)

**Registered:** Patch 2515, 16 July 2026. **Status:** OPEN — v1.1 **FROZEN** (Patch 2517: panel-amended per
dispatch-1 Q1 returns, then frozen per the dispatch's own terms; see
`conv001_2026-07_relic1_dispatch1_adjudication.md`). No derivation attempted at open.
**Lane:** DM campaign (`series_phenomena/cosmology/dark_matter/`). **Warm lineage:** DM-WARM-2514 → this campaign.
**Provenance:** Route survey Patch 0843 (`qdp_relic_abundance_scoping.md`, routes A/B/C; route B judged the
structurally promising one); OPEN-COSMO-DM-1 Step-2 bookkeeping (Patch 0704: ratio NOT derived, relocated to the
free amplitude); registry condition 5 of `DM-CANDIDATE-B_N8_cdm_like_registration.md` (Patch 2511: "Ω_DM/Ω_b ≈ 5.36
NOT derived; the promotion UNPARKS the relic-abundance line (route B, asymmetric DM scoping)").
**Verify at open:** `code/2515_relic_targets.py`. **Reasoning:** `reasoning/2515.md`.

---

## 1. What changed since the 0843 survey — the DM unit is now pinned

The 0843 verdict ("not derivable as a first-pass; every route bottoms out in an undeveloped sub-sector") was issued
when the DM unit's mass and composition were themselves open. That is no longer true. Candidate (B) pins:

| Quantity | Value | Provenance |
|---|---|---|
| Ring mass m_ring | 11.26 GeV (= 8 × 1.408 GeV) | 2383 (DD-ladder-selected, 2410/2411) |
| Element mass | 1.408 GeV = 8·m_qCP + 8·m_eCP = 8×(132+44) MeV | 2452 in-situ inertia identity; κ pinned 2496, never fit |
| Element composition | 2 planes × 2 crosses × (eCP–qCP–qCP–eCP) = 8 qCP + 8 eCP | founder geometry, 2433/2443 (geometry #3) |
| Ring composition | 64 qCP + 64 eCP (128 CPs) | 8 elements, N_planes=16 |

Route B's bookkeeping identity Ω_DM/Ω_b = (m_DM/m_p)·(n_DM/n_b) therefore has ONE of its two unknowns removed.
With Planck Ω_c h²/Ω_b h² = 5.364 ± 0.065 and m_ring pinned, the observational target is a pure number:

> **T1 (the campaign target): n_ring/n_b = 0.4468 ± 0.0054** (equivalently n_element/n_b = 3.574;
> per-qCP: n_qCP(DM-bound)/n_b = 28.6).

Both naive one-to-one ADM readings FAIL out of the box, and the charter states this adversely upfront:
n_ring = n_b predicts Ω_DM/Ω_b = 12.0 (×2.24 OVER); n_element = n_b predicts 1.50 (×3.57 UNDER). Route B for
candidate (B) survives only if a **derived, zero-knob counting mechanism** supplies the factor between the shared
asymmetry and the ring number density. That factor is the campaign's entire subject.

## 2. Scoping steps (in order; each a separate pre-registered patch)

- **S1 — Baryon-side net-CP bookkeeping.** *[STATUS ANNOTATION, Patch 2518 — not a semantics amendment:
  S1 COMPLETE; registered, Branch I does not fire; proton (+3 qCP, −1 eCP), neutron (+3, −2), neutral bulk
  (+3, −2)/baryon invariant; ring (0, 0) per 2435 → S2 candidate (a) CLOSED-NEGATIVE. See
  `relic1_s1_baryon_cp_bookkeeping.md`.]* Extract from the registered SS/SF-3 corpus the net conserved-CP content
  of the nucleon (net qCP count A_p; net eCP if the conserved charge involves it). If the corpus does not register
  a net-CP bookkeeping for the baryon, that is a NAMED BLOCKER (→ Branch I) — record it; do not improvise one.
- **S2 — The conserved shared charge.** *[STATUS ANNOTATION, Patch 2519 — not a semantics amendment:
  S2 COMPLETE on founder physical-picture input (16 Jul). (a) closed-negative (2518); (b) retained as asymmetry
  SOURCE at registered strength; (c) sharpened to the common-precursor mechanism c-hT: baryons (1 hTetra each)
  and rings (32 each) drain one precursor species. Closure theorem: the founder's two sinks are FORCED at
  hDP-B excess = 2n_b, free −qCP = n_b; n_r drops out (rings asymmetry-blind, ledger level). S3 target:
  ring:baryon hTetra branching = 14.30 ± 0.17 (93.46%/6.54%). New scenario gate SG-1 (charged-cloud relics)
  UNRESOLVED. FI-RELIC-1 (initial sign symmetry) conditionality rides on all downstream results. See
  `relic1_s2_closure_theorem_and_common_precursor.md`.]* Enumerate candidates: (a) net qCP number; (b) the substrate
  chirality/polarity asymmetry (the chirality-arc primitive FI-C-9 — flagged at 0843 as the native candidate,
  DIRECTION not result); (c) composite charges (color-singlet units, electric-neutral units). For each: what the
  asymmetry conserves, what a baryon costs, what a ring costs.
- **S3 — The branching/counting mechanism.** *[STATUS ANNOTATION, Patch 2520 — not a semantics amendment:
  S3 OPENED at pre-registration on founder mechanism S3-M1 (unpaired-monomer-limited baryogenesis vs
  barrier-free paired aggregation; n_b = U_q/3; decomposition n_ring/n_b = 3·n_ring/U_q, one ring per 6.71
  unpaired +qCPs at target). Retro-prediction check PASSED (skeleton forces the 2519 sinks at exact magnitude
  + pins U_q = 3n_b, U_e = 2n_b). Hazard H1 quantified: equilibrium Boltzmann readings give e^(−30)–e^(−10⁴),
  so only the frozen-inventory kinetic form is viable. Sub-computations S3a (U_q from pairing freeze-out),
  S3b (ring yield, Paths #1/#2 jointly), S3c (combination + branch reading) — each pre-registered before
  running. See `relic1_s3_preregistration.md`.]*
  *[S3a STATUS, Patch 2521: COMPLETE at Reading B. Route α (pairing kinetics) BLOCKED — NB-S3a-1, no
  registered rate framework. Route β: U_q/n_γ = 3η_B = (1.836±0.012)×10⁻⁹ via the registered PRED-O-25 anchor
  (n_b anchored-not-derived; NB-S3a-2 = forward leptogenesis pin). Transposed S3b target: n_ring/n_γ =
  (2.734±0.038)×10⁻¹⁰. Direction S3b-D1 (asymmetry-seeded nucleation, founder provenance) registered NOT
  adopted; S3b pre-registration must weigh it against a non-seeded alternative. See
  `relic1_s3a_uq_from_registered_anchors.md`.]*
  *[S3b STATUS, Patch 2522: pre-registration COMMITTED — three-way contest D1 (seeded; seed criterion locked:
  clouds primary, per-qCP reading, B-excess considered-and-rejected; target m = 0.4468±0.0054 rings/seed) vs
  D2 (homogeneous; computable kill-test defined, run FIRST) vs D3 (calibrated incumbent, named fallback).
  Anti-readings locked (no seed switching, no post-hoc clustering-k, no target-justified derivations).
  OBS-RELIC-1 recorded and FENCED (T1 at 0.077σ from 1/√5; NON-EVIDENTIAL; reverse-engineering = Branch T).
  See `relic1_s3b_preregistration.md`.]*
  *[S3b R1 EXECUTED, Patch 2523: D2 KILLED — ungated bound n_ring/n_γ ≤ 9.3×10³⁴ vs target 2.734×10⁻¹⁰,
  overshoot 44.5 orders on the CONSERVATIVE density basis (Ω cross-check 12× below the R2 band low end =
  the understating direction; kill a fortiori). Ring formation MUST be gated; D1 LICENSED under the locked
  seed criterion. Next: the m derivation (founder nucleation-geometry input → pre-registered computation).
  See `relic1_s3b_d2_kill_test.md`.]* Derive, from registered formation physics only (cascade 2382/2421–2423;
  kT_form ≈ 16.5 keV; the N≥8-dominance corridor), the fraction of the shared asymmetry that lands ring-bound vs
  baryon-bound. Zero free parameters. This is where the ×2.24 / ×3.57 factor must come from or the route dies.
- **S4 — Consistency gates (run on any S3 candidate that lands):** (i) the cascade's N≥8 population dominance must
  be preserved under the asymmetric production history; (ii) falsifier (iv) carries over — N_eff = 2.99 ± 0.17 and
  BBN light-element abundances; (iii) no double-counting of baryon-bound CP content (the 0704 ~19% effect,
  cleanly avoidable there, must stay avoided here); **panel-added gates (2517):** (iv) symmetric-component
  depletion — the symmetric ring/anti-ring or precursor population must be shown annihilated or otherwise
  removed; (v) conserved-charge closure — baryons + DM + every residual carrier must reproduce the assumed
  total shared asymmetry; (vi) entropy/dilution-history survival — the predicted number ratio must survive
  reheating, annihilation, phase transitions, and any late entropy injection; (vii) perturbation
  compatibility — no forbidden baryon–DM isocurvature mode, no disruption of the observed matter power
  spectrum; (viii) formation-temperature/density consistency with the registered thermal history (EU-1 +
  BBN/CMB; the corpus value is kT_form ≈ 16.5 keV — the gate is consistency, not a scale assertion).
  Violation of any gate = K2, even in-window.

## 3. Pre-registered branches and kill conditions (fixed at open, before any computation)

- **Branch D-strong:** a zero-knob mechanism yields a predicted n_ring/n_b whose distribution, WITH propagated
  registered uncertainties, overlaps the observational ±2σ window **[0.436, 0.458]** (a bare central value
  inside the window is insufficient — panel amendment, 2517). → Route B DERIVES the ratio; panel adjudicates
  whether/how this moves candidate (B)'s verdict (favorable evidence, but promotion semantics are the
  panel's, not the worker's).
- **Branch D-directional** (renamed from D-weak, panel amendment 2517): the mechanism lands within ×1.5 either
  side, **[0.30, 0.67]**, but not D-strong. → Recorded as FAVORABLE-DIRECTIONAL only; the ratio remains NOT
  derived; no verdict movement claimed; this label may NEVER be described as partial derivation.
- **Branch T (tunable-only → route KILLED as a derivation claim):** the only way to land in-window is a continuous
  free parameter with no independent pin. **Broadened (panel amendment, 2517): T also fires for discrete model
  selection among unpinned mechanisms; post-result selection of the conserved charge; unregistered cutoffs,
  freeze-out epochs, or stopping rules; products of individually unpinned order-one factors; survivorship
  conditioning (counting only surviving formation channels); and any parameter — continuous or discrete —
  beyond the registered corpus, even if the output lands in-window.** G7 applies in full: no re-parametrizing
  toward the window. The ratio then stays CALIBRATED (on par with ΛCDM, per 0704/0843) — this kills the
  route-B derivation claim for candidate (B), NOT the candidate.
- **Branch I (indeterminate → campaign PARKS):** S1–S3 bottom out in an undeveloped sub-sector (net-CP bookkeeping
  unregistered; CPP baryogenesis mechanism undeveloped; chirality-arc asymmetry uncomputed — the FI-C-9 primitive
  is registered as not-yet-derived). Park with the named blocker; ratio stays calibrated; candidate (B) untouched.
- **K1 (structural kill):** the shared-charge bookkeeping, with all counting factors registered and no derivable
  branching remaining, FORCES n_ring/n_b outside [0.30, 0.67]. → Route B killed for candidate (B) (ratio stays
  calibrated; candidate survives on its existing basis).
- **K2 (consistency kill):** any mechanism that lands T1 but violates an S4 gate (cascade dominance, N_eff/BBN,
  double-counting) is killed even if in-window. In-window does not buy a broken gate.

**Verdict semantics, pre-registered:** no outcome of this campaign except a panel-adjudicated Branch D-strong moves
candidate (B)'s 79.5% PROVISIONAL-FAVORABLE. K1/K2/T firing does NOT falsify candidate (B) — it returns the ratio
to calibrated status, which is where it already stands. This is fixed now so no later reading can be motivated
in either direction.

## 4. Anti-priorities (verbatim-in-force)

- No numerology on 0.4468 / 3.574 / 28.6 — a counting factor counts only if it is DERIVED from registered
  structure, not matched post hoc.
- No re-fit of κ (pinned 132/44, G7), no re-fit of the ring mass or composition, no post-hoc composition switches.
- No statics-route claims — the E_bond CONV-001 fork and the R5 transverse tensor reactivate the moment one is
  made (registry condition 4). The relic campaign is bookkeeping + formation-history work; it has no statics need.
- The chirality-arc connection (S2 candidate b) enters as a DIRECTION with its registered not-yet-derived status
  attached; it may not be silently promoted to a mechanism.

## 5. First panel dispatch

The campaign's first dispatch (drafted Patch 2516, UNDISPATCHED) presents this charter for pre-registration review
BEFORE any S1–S3 computation, and carries the two queued disclosures riding from the prior session: the 2513
C7-stands/estimator-diagnosis record and the 2514 Branch-L emergent-duty record with its apposition-scale /
energy-weighting convention question. Dispatch runs under the Patch-2512 Copilot probation protocol: five seats
receive; four-seat binding (ChatGPT, Grok, Gemini, DeepSeek); Copilot's return passes the pre-registered fidelity
screen; a five-seat sensitivity line is reported alongside every binding read.
