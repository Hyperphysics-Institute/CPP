# NB-F-1-T pre-registration: ΔE_b as a signed three-term sum, E_act, and the freeze-out composition — definitions, closed input list, the bond-identity adjudication, structural consequences computed now, routes, and readings, committed before any derivation

**Patch 2537, 18 July 2026. Status: NB-F-1-T OPENED at pre-registration; NO derivation performed.**
**Governing lineage: 2529 (prereg discipline) → 2530 (D3/NB-F-1) → 2531–2534 (§6f arc) → 2536 (input
audit). Verify: `code/2537_nbf1t_prereg.py`. This document's frozen §§5–6 govern the compute patch(es);
every reading there will be an application of this file.**

## 0. What NB-F-1-T resolves, and what it does not

NB-F-1-T is the derivation route for the NB-F-1 blocker (relic-epoch Sea composition dial). Per the §6f
epoch anchor T_form(DM) ≈ T_form(hTetra), the dial reduces to the reaction eDP + qDP ⇌ hTetra evaluated
at its own window. Three targets, in dependency order:

1. **ΔE_b** — the thermodynamic differential, defined §1, as the signed three-term second-order sum on
   top of the theorem-grade leading order.
2. **E_act** — the kinetic barrier along the minimum-barrier assembly path.
3. **The freeze-out composition** — the rate-vs-ambient step. **Pre-registered honestly NOW: this step
   sits at the NB-S3a-1 boundary; constructing rates in-campaign = Branch T (2521). Even a fully
   computed ΔE_b + E_act may leave this step Branch I.** Reopening OPEN-DM-RELIC-1 requires all three;
   partial results bank without reopening.

**The trap clause, carried forward verbatim (2529 §4):** *"The zero-skew baseline f_hTe = 1/2 lies
INSIDE the pass window, and (script-verified) reproduces T1 exactly at c_pack ≈ 1.32 ∈ [1, √2]. So a
lazy derivation that merely assumes equal proportions lands in-window. Committed now: that is NOT a
pass. A pass requires the skew magnitude at the composition-setting epoch to be derived (small or zero)
from the closed input list — e.g., a registered mechanism that suppresses or caps the skew. Defaulting
to x = 1/2 because no registered input discriminates = Branch I dressed as a pass — read as Branch I
(named blocker), not as a landing. The distinction is auditable: a derivation must exhibit the
registered content that fixes x; 'absence of a registered skew value' fixes nothing."* Extension
committed for THIS campaign: **"ΔE_b is near-threshold" does NOT license x = 1/2 or f_hTe = 1/2.** A
near-threshold ΔE_b feeds a composition claim only through the freeze-out step; skipping that step and
reading equal proportions off "≈ 0" is the same trap in thermodynamic dress.

## 1. Definitions fixed

- **ΔE_b ≡ B(eDP) + B(qDP) − B(hTetra)** (binding energies positive). ΔE_b < 0: tetra thermodynamically
  favored; ΔE_b > 0: metastable (barrier-protected only); |ΔE_b| ≲ second-order scale: near-threshold.
- **Decomposition, per 2532/2534 (theorem-grade structure):** ΔE_b = 0 (leading electric order, exact
  at the symmetric point for any edge lengths under the two-axis geometry) + **T_dist** (elastic
  distortion, sign +, positive-definite at harmonic order) + **T_color** (color-in-tetra SSV_abs
  deepening of the q–q channel, sign −, founder-registered direction) + **T_store** (ZBW-storage vs
  compression-storage asymmetry, sign ?). Signs are pre-stated here and may not be re-assigned by the
  compute patch; a computed term violating its pre-stated sign = HALT and diagnose (theorem or
  registration error), no reading taken.
- **E_act:** the maximum of the total interaction energy along the minimum-barrier assembly path from
  separated eDP + qDP at rest to the finished tetra, measured from the initial state. Channel energies
  only — per-edge energies are not separately defined (non-separability principle, §6f Second Addendum,
  adopted 2533).
- **Composition step:** the frozen 2526/2527/2529 apparatus consumes x at the window; f_hTe = 1 − x;
  m/k = f_hTe·[0.678, 0.959]; charter bands unchanged. Zero new decisions on reopening (2530 §6).

## 2. Closed input list (nothing else may enter)

1. **The 2532 neutrality-cancellation theorem** + 2533 irregular-tetra robustness + **2534
   amended-ledger convergence** (leading-order ≈ 0; repulsive-edge refund; compression-storage
   mechanism). Theorem-grade + founder-ruling grade.
2. **Registered DP scales at 0880/2452 depth:** E_eDP = 88, E_qDP = 264 = 3·E_eDP, E_hDP = 152 =
   √(E_eDP·E_qDP) MeV; element identity 4·264 + 4·88 = 1408 MeV. The 0834 absolute-scale caveat
   (r_min reconciliation) rides along; ratio structure is the load-bearing part.
3. **The super-additive inequality** (registered assumption, 0672a): B(hTetra) > 2·B(hDP).
4. **E_ee band** [0.8 keV, 2 MeV] (0865; aggregate-edge lane) and **E_qq window** [40, 170] MeV
   (map-strength; DM lane) — admissible ONLY after the §3 bond-identity adjudication assigns them a
   role; ordering E_qq > E_ee sign-certain.
5. **Pinned inertias** m_qCP = 132, m_eCP = 44 MeV/c² (2496 blind pin; 2452 in-situ convergent).
6. **Lengths:** l_unit = 0.589 fm (derivation-strength); a_q = 1.15 fm; R_e = 1.301 fm; qDP bond
   1.0–1.3 fm (0835).
7. **§6f arc registrations:** epoch anchor T_form(DM) ≈ T_form(hTetra); kT_form ≈ 16.5 keV consistency
   gate carried UNADJUDICATED; equal-CP-inventory affirmation; canonical hDP labels.
8. **Standing pre-commitments:** 2521 (in-campaign rate construction = Branch T); 2529 §6 Branch-T
   triggers verbatim (any fraction chosen to land; any step justified only by its output; vision-tier
   qualitatives promoted to numbers; unregistered epoch selection); the trap clause (§0 above).
9. **EXCLUDED, named:** Part I §3's "probably an ℏ unit" ZBW statement (vision-tier, self-qualified —
   using it as a number is input-8's named Branch T); any SSV_abs→energy formula (none registered,
   audit (ii)); any bond stiffness (none registered, audit (i-5)); zone enrichment or unregistered
   conversion routes (2529 §1 scope commitments carried).

## 3. The bond-identity adjudication (mandatory first act of the compute patch)

The corpus registers two e-scale energies (audit (i-1)/(i-2)): DP-internal (E_eDP = 88 MeV) and
aggregate inter-element edge (E_ee ∈ [0.8 keV, 2 MeV]). **The compute patch must adjudicate, by
structural identity and registration depth ONLY (not by output), which scale prices the tetra's e–e and
q–q channels — before any number is used.** The adjudication criteria are fixed now:

- The tetra's e–e channel is the bond between the two eCPs that constitute, on dissociation, a free
  eDP. If the corpus's structural identifications make that bond the eDP internal bond, the DP-internal
  scale (input 2) governs. If the corpus registers the tetra edge as an aggregate-lane screened
  residual, the band (input 4) governs.
- Choosing a scale because it lands a preferred reading = Branch T. If registration depth cannot
  discriminate, that is **Branch I with the bond-identity question as the named blocker** — recorded,
  not improvised around.

## 4. Structural consequences computed NOW (2529-ceiling class; script-verified)

- **The super-additive inequality is ENTAILED at leading order.** With B(hTetra) = B(eDP) + B(qDP) =
  4·E_eDP (leading-order theorem structure, input 1) and B(hDP) = √3·E_eDP (input 2 ratios):
  4·E_eDP > 2√3·E_eDP identically. The 0672a registered *assumption* (input 3) is a *consequence* of
  later theorem-grade structure — banked as a retroactive hardening of the RELIC-1 input list.
- **The leading-order sink margin:** B(hTetra) − 2·B(hDP) = (4 − 2√3)·E_eDP ≈ 0.536·E_eDP ≈ 47.2 MeV
  (at the DP-internal scale). This is the erosion budget: the hTetra-sink picture survives second-order
  corrections unless |T_dist + T_color + T_store| in the hDP-comparison channel exceeds ~47 MeV.
  Computed as structure, NOT as a reading on ΔE_b (which compares against eDP + qDP, where the leading
  order is ≈ 0 and the three terms decide alone).
- **Fence note (OBS-RELIC-1):** the ratio structure introduces √3 (E_hDP = √3·E_eDP), not √5. No √5
  enters any quantity defined in this file; any √5 appearing in the compute patch's ΔE_b or E_act
  derivation triggers maximum scrutiny with step-by-step provenance, per the standing fence.

## 5. Routes (order LOCKED; post-hoc selection by output = Branch T)

- **R-A — leading-order channel comparison + signed-term bounding (first).** Execute the §3
  adjudication; state ΔE_b's leading order (theorem, ≈ 0); then attempt each second-order term FROM THE
  CLOSED LIST ONLY: T_dist needs equilibrium lengths + stiffnesses (audit: unregistered → expected
  Branch-I limb, sign + banked); T_color needs an SSV_abs formalization (audit: none → expected
  Branch-I limb, sign − banked, blocker identity = the E_bond-pin shared root); T_store (audit: nothing
  → expected Branch-I limb). **An honest R-A outcome may be: "ΔE_b = 0 + (three signed, individually
  Branch-I terms)" — near-threshold at theorem strength, magnitude unresolved.** That is a bankable
  partial, not a failure and not a pass.
- **R-B — E_act path (only after R-A's terms are dispositioned).** Requires stiffnesses and path
  dynamics; inertias (input 5) cover half. Expected Branch I on the same stiffness gap; if a
  stiffness-free bound on E_act exists from the closed list, it may be recorded as a bound only.
- **R-C — freeze-out composition (only on computed ΔE_b AND E_act).** Sits at the NB-S3a-1 boundary;
  any rate construction = Branch T (input 8). Named, expected blocked; the honest terminus is Branch I
  with NB-S3a-1 as the named blocker unless a rate-free registered argument exists (none known at
  prereg).

## 6. Readings (frozen; committed now)

- **All three targets computed from the closed list** → x at the window → f_hTe = 1 − x → the 2529 §6
  frozen readings verbatim (D-strong / D-directional / K1-direction bands unchanged; conditionality
  ledger carried in full). Campaign REOPENS per the 2530 contract.
- **ΔE_b resolved but composition step Branch I** → record ΔE_b at its earned strength (theorem /
  derived / bounded); campaign REMAINS CLOSED at D3; NB-F-1 narrows to the freeze-out step; blocker
  ledger updated.
- **ΔE_b itself Branch I on all three terms** → record the theorem-grade near-threshold structure + the
  §4 entailment as banked partials; NB-F-1-T closes Branch I with the named blockers (stiffness/length
  registrations; SSV_abs formalization = E_bond-pin root; storage model); founder registration of ZBW
  bond statics through the standing channel is the named route (ii)-class reopening key.
- **Any computed term violating its §1 pre-stated sign** → HALT and diagnose; no reading.
- **Any √5 in the derivation** → fence procedure (§4), maximum scrutiny before any reading.
- **Branch T restated:** scale chosen by output (§3); rates in-campaign; vision-tier ℏ promoted;
  near-threshold read as f_hTe = 1/2 (§0 extension); any step justified only by its output.

## 7. Campaign bookkeeping

79.5% PROVISIONAL-FAVORABLE untouched (pre-registration only; RELIC-1 remains CLOSED at D3 pending
§6's first reading). Dispatch posture per the §6f governance ruling: no panel dispatch on Branch-I
outcomes; a computed-ΔE_b positive result queues with the standing disclosure package for the next
win-class dispatch. Queued measurements (δ_E energy-weighted duty; MW-MODES TC-extension) remain ranked
behind NB-F-1-T. Founder physical input on ZBW bond statics (stiffness/length of the e–e and q–q bonds)
remains welcome through the standing channel and would directly convert R-A's T_dist limb from Branch I
to computable. Next patch: the R-A compute, under this document only.

---

*[STATUS RIDER, Patch 2538 — founder capture §6g (18 July 2026): this pre-registration is **HELD**.
The §6g model shift registers that the hTetra does not form as a Sea species (fold-blocked by the two
repulsive cross relationships; hTetra formation occurs only at the baryogenesis final step, folded by
up/down-quark attraction). The reaction target eDP + qDP ⇌ hTetra is therefore superseded IN ROLE as
the Sea's composition-setting reaction, before any compute patch executed under this document — no
reading was ever taken here. What carries forward intact into the re-scoped campaign: the trap clause
and its near-threshold extension (§0); the bond-identity adjudication criteria (§3); the closed-list
method and Branch semantics (§§2, 5–6); and the §4 structural consequences (the super-additive
entailment survives as a statement about tetra binding wherever the tetra occurs — now the baryon
interior — and the 47 MeV margin retains that meaning). The successor targets are the §6g plane-unit
energetics (flat eDP–qDP binding) and the rod→ring bending window (T_form(DM) from the registered
pure-bend stiffness, Patch 2450 lineage); a successor pre-registration will be written against those
targets after the §6g clarification questions (Q1–Q5) resolve. Per anti-erasure this document is
annotated, not deleted; it remains the reference implementation of the prereg discipline for the
successor.]*
