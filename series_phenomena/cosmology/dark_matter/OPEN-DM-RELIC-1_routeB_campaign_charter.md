# OPEN-DM-RELIC-1 — the Ω_DM route-B relic-abundance campaign (asymmetric DM via a shared Sea asymmetry), scoped for candidate (B)

**Registered:** Patch 2515, 16 July 2026. **Status:** OPEN — campaign charter; no derivation attempted at open.
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

- **S1 — Baryon-side net-CP bookkeeping.** Extract from the registered SS/SF-3 corpus the net conserved-CP content
  of the nucleon (net qCP count A_p; net eCP if the conserved charge involves it). If the corpus does not register
  a net-CP bookkeeping for the baryon, that is a NAMED BLOCKER (→ Branch I) — record it; do not improvise one.
- **S2 — The conserved shared charge.** Enumerate candidates: (a) net qCP number; (b) the substrate
  chirality/polarity asymmetry (the chirality-arc primitive FI-C-9 — flagged at 0843 as the native candidate,
  DIRECTION not result); (c) composite charges (color-singlet units, electric-neutral units). For each: what the
  asymmetry conserves, what a baryon costs, what a ring costs.
- **S3 — The branching/counting mechanism.** Derive, from registered formation physics only (cascade 2382/2421–2423;
  kT_form ≈ 16.5 keV; the N≥8-dominance corridor), the fraction of the shared asymmetry that lands ring-bound vs
  baryon-bound. Zero free parameters. This is where the ×2.24 / ×3.57 factor must come from or the route dies.
- **S4 — Consistency gates (run on any S3 candidate that lands):** (i) the cascade's N≥8 population dominance must
  be preserved under the asymmetric production history; (ii) falsifier (iv) carries over — N_eff = 2.99 ± 0.17 and
  BBN light-element abundances; (iii) no double-counting of baryon-bound CP content (the 0704 ~19% effect,
  cleanly avoidable there, must stay avoided here).

## 3. Pre-registered branches and kill conditions (fixed at open, before any computation)

- **Branch D-strong:** a zero-knob mechanism yields n_ring/n_b inside the observational ±2σ window
  **[0.436, 0.458]**. → Route B DERIVES the ratio; panel adjudicates whether/how this moves candidate (B)'s
  verdict (it is favorable evidence, but promotion semantics are the panel's, not the worker's).
- **Branch D-weak:** the mechanism lands within ×1.5 either side, **[0.30, 0.67]**, but not D-strong. → Recorded
  as FAVORABLE-DIRECTIONAL only; the ratio remains NOT derived; no verdict movement claimed.
- **Branch T (tunable-only → route KILLED as a derivation claim):** the only way to land in-window is a continuous
  free parameter with no independent pin. G7 applies in full: no re-parametrizing toward the window. The ratio
  then stays CALIBRATED (on par with ΛCDM, per 0704/0843) — this kills the route-B derivation claim for
  candidate (B), NOT the candidate.
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
