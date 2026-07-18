# OPEN-DM-RELIC-1 S3 — pre-registration: the founder's unpaired-monomer mechanism (S3-M1), its readings, dependencies, and hazards — committed BEFORE any computation

**Patch 2520, 16 July 2026. Status: S3 OPENED at pre-registration level; NO branching computation performed.**
**Founder input (16 Jul, second note):** the two DM assembly paths (Path #1 ribbon condensation — qDP chains →
eDP coat → 4-wide ribbon → rod → ring, matching the registered G1 cross morphology 0870; Path #2 hTetra
condensation — 4-hTetra elements with the 4th-addition activation step, matching 1855–1856), the baryon channel's
complexity (multi-step UUD assembly on an hTetra backbone), and the central proposal: **the branching is set by
the scarcity of UNPAIRED +qCPs** — quarks are bare +qCPs, in competition with qDP/hDP-A/hTetra pairing, while
both DM paths consume abundant PAIRED feedstock nearly barrier-free. **Verify:** `code/2520_s3_prereg_checks.py`.

## 1. The mechanism, stated sharply (S3-M1, founder provenance)

Baryon number is inventory-limited: **n_b = U_q / 3**, where U_q is the unpaired +qCP population surviving
pairing freeze-out into the condensation epoch (each baryon consumes exactly 3 bare +qCPs as its quarks; the
scaffold hTetra is paired-sourced). Ring number is yield-limited: n_ring is set by the paired-channel
condensation (Paths #1/#2) independently of U_q. The target T1 = n_ring/n_b = 0.4468 therefore **decomposes**:

> n_ring/n_b = 3 · n_ring / U_q — one scarce-inventory factor (U_q) and one aggregation-yield factor (n_ring
> from the paired Sea), each requiring its own registered-physics derivation.

## 2. The retro-prediction check (computed at pre-registration; it PASSES)

A mechanism adopted at S3 must be consistent with the 2519 closure theorem. S3-M1's skeleton — per-species
sign-symmetric unpaired inventories (U_q per qCP sign, U_e per eCP sign); matter-only consumption (3 unpaired
+q and 2 unpaired −e per baryon: the two down-quark captures... [one per down; a proton has one down] — one
captured −eCP in the down quark plus one orbital electron per H-equivalent, = 2 per baryon net, per S1);
baryogenesis running to exhaustion of unpaired +q — **forces the mirror populations to distribute as: 2n_b of
the unpaired −q bind the 2n_b unpaired +e into hDP-B (the Sea's type-B excess = 2n_b ✓) and the remaining n_b
unpaired −q have no partner and no antibaryon channel (the clouds = n_b ✓).** The mechanism reproduces BOTH
closure-forced sinks at exact magnitude — a non-trivial retro-prediction — and adds two pins closure alone
could not give: **U_q(consumed) = 3n_b and U_e(consumed) = 2n_b**, i.e., the founder's claim "unpaired qCP
availability limits baryons" is not only consistent with the ledger, it is the ledger's mechanistic completion.
The matter-only tilt itself remains the chirality-arc input (registered strength), as before.

## 3. Pre-registered readings (mapped to the frozen charter branches; committed now)

The S3 computation, when run, produces n_ring/n_b = 3·n_ring/U_q with a propagated uncertainty band (E_qq
window 40–170 MeV and any other registered-window inputs propagate; charter v1.1 D-strong requires the BAND to
overlap [0.436, 0.458], not the central value). Readings:
- **Band overlaps [0.436, 0.458]** → Branch D-strong (panel adjudicates verdict movement; FI-RELIC-1
  conditionality attached).
- **Central value in [0.30, 0.67], band not D-strong** → Branch D-directional (favorable-directional ONLY).
- **Forced outside [0.30, 0.67] with all inputs registered** → K1 (route killed; ratio stays calibrated;
  candidate untouched).
- **Any tuned rate coefficient, discrete mechanism shopping between Paths #1/#2 after seeing outputs,
  unregistered cutoff, or dropped failed channel** → Branch T (broadened, v1.1).
- **U_q or the ring yield bottoms out in unregistered pairing-freeze-out thermodynamics** → Branch I (park,
  named blocker).
Sub-computations, each its own patch with readings committed before running: **S3a** — U_q from pairing
freeze-out (what fraction of +qCPs escapes qDP/hDP-A/hTetra pairing; kT_form ≈ 16.5 keV *[retired as T_form(DM), Patch 2543 — see 2542]*; failed channels
carried). **S3b** — ring yield of the paired channel (Paths #1/#2 jointly; the 4th-hTetra activation step
1855–1856; eDP-displacement energetics per the founder's note). **S3c** — the combination and branch reading.

## 4. Hazards, registered before they can bite

- **H1 — exponential overshoot (the serious one):** any reading where the branching rides a Boltzmann factor
  exp(−E/kT_form) with registered E ~ 0.5–170 MeV against kT ≈ 16.5 keV produces suppressions of e^(−30) to
  e^(−10⁴) — nothing like 6.5%. S3-M1 survives this hazard ONLY in its kinetic form: the inventories (U_q, and
  the paired feedstock) are FROZEN relics of the initial condensation, and the branching is a ratio of frozen
  inventories and near-barrier-free aggregation yields — not a thermal equilibrium ratio. Any S3a/S3b result
  that reintroduces an equilibrium exponential into the branching must be read as K1-direction, not massaged.
- **H2 — the E_qq window:** E_qq is registered as a 40–170 MeV estimator-spanned window (registry condition 3,
  statics-parked). Using E_qq in FORMATION energetics is distinct from the parked E_bond statics fork
  (condition 4) — recorded here so the distinction is explicit and no statics-route claim occurs by drift. The
  window propagates into the S3 band; if the band is window-dominated, that is reported, not narrowed.
- **H3 — order-one-factor products:** the condensation network has many rates; under broadened T, rates enter
  only as RATIOS grounded in registered energetics/geometry, and every introduced factor is enumerated in the
  S3a/S3b records with its registration pointer or the computation stops.

## 5. Founder-note items recorded non-silently

Path #1 vs Path #2 are treated as one paired-channel class at S3 level (both consume paired feedstock; internal
DM-path competition is a sub-question of S3b, not a branching selector — choosing between them after seeing
outputs would trip broadened T). The founder's "Let there be light / 13 GPs" cosmogonic sequence is provenance
narrative, carried verbatim in `reasoning/2520.md`, not formalized here. The E_ee down-quark vertex remarks and
the weakened same-charge E_qq observation are noted for S3b's energetics ledger.
