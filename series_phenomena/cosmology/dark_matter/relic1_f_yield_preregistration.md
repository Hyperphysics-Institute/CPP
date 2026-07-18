# OPEN-DM-RELIC-1 — NB-T2-1 pre-registration: the hTetra-formable yield fraction f — definition, closed input list, the structural ceiling, the null-baseline trap, routes, and readings, committed before any derivation

**Patch 2529, 17 July 2026. Status: NB-T2-1 OPENED at pre-registration; NO dial derivation performed.**
**This is the decisive computation of the campaign (2527/2528). Verify: `code/2529_f_prereg.py`.**

## 0. Symbol disambiguation (gate catch, recorded per anti-erasure)

The repo already carries an **f**: Patches 0834/0835 (`qdp_residual_fraction_f_derivation.md`,
`qdp_f_as_a_number.md`, DM-2 lane) define f = (residual qDP–qDP well depth)/E_qDP ≈ 0.2. **That is a
different quantity.** The NB-T2-1 quantity — written **f_hTe** in this file and in the compute patch — is a
*composition yield fraction*. The 2527 pre-stated pass window (0.466–0.659) refers to f_hTe. The grep
collision was caught at the gate and is recorded here so no future session conflates the two (the 0757↔1858
precedent).

## 1. Definition fixed

> **f_hTe = (Sea CPs resident in hybrid species — hDP-A, hDP-B, hTetra — within one screened horizon) /
> (total Sea CPs within that horizon)**, converted at the registered stoichiometry 1 hTetra = 1 hDP-A +
> 1 hDP-B = 4 CPs (Patch 2519).

Two scope commitments, fixed now:

- **Zone composition = ambient composition.** Entailed by the 2527 reframing: the capture zone IS the
  pre-existing screened ambient horizon; no pre-sorting or species-selective transport mechanism is
  registered. If the compute patch wants zone enrichment, that is an unregistered mechanism → Branch I.
- **No unregistered conversion routes.** hTetra-formable content = the hybrid-resident CPs. A
  shell-catalyzed partner swap eDP + qDP → hDP-A + hDP-B would enlarge f_hTe toward 1, but 0672a registers
  the *opposite* direction as favored (the qCP–qCP channel is the skew driver; the forward swap costs the
  color binding). Importing a forward-swap mechanism = unregistered → Branch I, not improvised.

## 2. Registered inputs (CLOSED list — nothing else may enter)

1. **The 0672a conservation lock** (`founders_vision.md` Part V §6c, Opus scope note): equal initial
   inventories N of {+eCP, −eCP, +qCP, −qCP} ⇒ n(eDP) = n(qDP) ≡ n_q exactly, n(hDP-A) = n(hDP-B) = N − n_q,
   independent of binding energies. One dial: x ≡ n_q/N.
2. **The registered skew direction + driver**: qDP is the one doubly-bound species (electric + qCP–qCP/color);
   color screening pushes n(qDP) *up* from the equal-probability split. Direction registered; magnitude NOT.
3. **The hTetra sink + freeze-out ordering + super-additive inequality** (hTetra binding > 2× hDP): under
   Thomas's registered lean (scarce free hDPs, available hTetras), hybrid-resident CPs sit predominantly in
   hTetras — the hybrid fraction is hTetra-formable in full.
4. **The registered regime caution** (0672a, verbatim class): the 1:1 lock is a hot/thermal-equilibrium
   statement; the sink and on-demand pictures are kinetic freeze-out statements. The two must not be conflated.
5. **The 2519 stoichiometry** (4 CPs/hTe; hTetra = hDP-A + hDP-B).
6. **kT_form ≈ 16.5 keV** (registered corpus value; charter §"consistency, not scale assertion"). *[RETIRED as T_form(DM) at founder ratification, Patch 2543; superseded by the derived bend-close epoch kT_form(L=16) ∈ [10.2, 17.0] MeV (2542). Historical input of the D3-closed campaign; annotation per anti-erasure.]*
7. **Standing pre-commitment (2521)**: constructing pairing/condensation rates in-campaign = Branch T.
   NB-S3a-1 (the CPP kinetic framework) remains a missing PROJECT.

## 3. The structural ceiling — computed NOW from the lock alone, before any dial derivation

The lock parametrizes all four populations by x ∈ [1/2, 1] (floor = the equal-probability split; the
registered driver only pushes x up). The hybrid-resident CP fraction is:

> **f_hTe = 1 − x ≤ 1/2 exactly, with equality iff zero skew.**

Frozen consequences (sympy-verified in the script):

- **The reachable part of the 2527 pass window is [0.466, 0.500].** The window itself is untouched — the
  lock simply makes its upper portion (0.500–0.659) unreachable. Any derivation producing f_hTe > 1/2
  violates the lock ⇒ algebra error or smuggled conversion route ⇒ HALT and diagnose, no reading taken.
- **The route's survival condition is now razor-thin:** pass requires x ∈ [0.500, 0.534] — the relic-epoch
  qDP excess over the unskewed floor must be ≤ 3.4 percentage points (≤ 7% relative). The registered
  color-screening driver, if strong at the composition-setting epoch, drives x → 1 and f_hTe → 0 ⇒
  K1-direction. The derivation is therefore a genuine two-sided jeopardy: too much skew kills it; and
  recovering no skew has its own trap (§4).

## 4. The null-baseline trap (pre-committed before knowing which way the derivation goes)

The zero-skew baseline f_hTe = 1/2 lies INSIDE the pass window, and (script-verified) reproduces T1 exactly
at c_pack ≈ 1.32 ∈ [1, √2]. So a lazy derivation that merely *assumes* equal proportions lands in-window.
**Committed now: that is NOT a pass.**

- A pass requires the skew magnitude at the composition-setting epoch to be **derived** (small or zero) from
  the closed input list — e.g., a registered mechanism that suppresses or caps the skew.
- Defaulting to x = 1/2 because no registered input discriminates = **Branch I dressed as a pass** — read as
  Branch I (named blocker), not as a landing.
- The distinction is auditable: a derivation must exhibit the registered content that *fixes* x; "absence of
  a registered skew value" fixes nothing.

## 5. Routes (order LOCKED; post-hoc selection by output = Branch T)

- **R-A — registered composition statement (first).** Does the corpus register the Sea's species proportions
  at the relevant epoch at declarative strength (Part I §3 "Mixed DP/hTetra Sea"; 0672a; glossary)? If yes,
  read off; registration depth checked (vision-tier qualitative statements — "reasonably available",
  "need not be common" — do NOT fix a number; treating them as numeric = Branch T).
- **R-B — equilibrium statistics (only on R-A miss).** Valid only if a *registered* composition-setting epoch
  plus *registered* binding energies fix x with zero new rates. Tension recorded openly, in advance: at
  kT_form = 16.5 keV any MeV-scale binding differential saturates the skew (x → 1, f_hTe → 0 ⇒
  K1-direction); whether equilibrium even applies at kT_form is exactly what the registered regime caution
  (input 4) governs — the composition may instead be frozen from an earlier, hotter epoch. If the epoch
  selection is itself unregistered, R-B is Branch I, not a choice.
- **R-C — frozen-inventory kinetics (only on R-B miss).** Requires the pairing/condensation kinetic
  framework = NB-S3a-1 ⇒ **Branch I by the standing 2521 pre-commitment.** Named, expected blocked.

## 6. Readings (frozen-band mapping, committed now)

With B ≡ (π/96)·c_pack·φ³·(r_c/l_unit)³ ∈ [0.678, 0.959] the 2527 maximal form (c_pack spread carried, its
4D→3D inference flagged), the prediction is m/k = f_hTe·B:

- **f_hTe derived ∈ [0.466, 0.500]** → propagate the full band f_hTe·[0.678, 0.959] against the charter v1.1
  frozen branches: **D-strong** if the band overlaps [0.436, 0.458] (band overlap, distribution not central
  value); **D-directional** if within [0.30, 0.67]; conditionality ledger carried in full (§8).
- **f_hTe derived < 0.466** → K1-direction → **D3** (ratio stays calibrated; record clean).
- **f_hTe > 0.500** from any derivation → lock violation → HALT/diagnose; no reading.
- **Dial underivable from the closed list** (R-A miss, R-B Branch I, R-C blocked) → **Branch I**, named
  blocker **NB-F-1: the relic-epoch Sea composition dial is unregistered** → campaign closes at **D3** with
  the STRUCTURAL-PARTIAL record standing (44 orders → ×2 → one named unregistered dial).
- **Branch T triggers restated:** any fraction chosen to land; any step whose only justification is its
  output; any in-campaign rate construction; vision-tier qualitatives promoted to numbers; unregistered
  epoch selection.

## 7. OBS-RELIC-1 fence, restated at this step

f_hTe multiplies a form that already carries √5 (φ³ = 2 + √5; provenance documented independent of the
fenced observation at 2527). f_hTe itself is rational algebra on populations; **any appearance of √5 in
f_hTe's own derivation triggers maximum scrutiny with step-by-step provenance documentation.** Noted for the
record (script-verified): 1/√5 ≈ 0.4472 lies BELOW the pass window — an f_hTe landing exactly there is
K1-direction, not a pass; the fenced coincidence cannot be gamed into a success at this step.

## 8. Campaign bookkeeping

79.5% PROVISIONAL-FAVORABLE untouched (this patch is pre-registration only). Conditionality ledger on any
D-branch: FI-RELIC-1 + NB-S3a-2 + FI-RELIC-3(a) + the T-2 c_pack 4D→3D inference + whatever route R-A/R-B
imports. Dispatch-2 disclosure package completes with the f reading (whichever branch) and fires per
WORKFLOW-REVIEW-ECONOMY. Next patch (2530): the computation, under this document only.
