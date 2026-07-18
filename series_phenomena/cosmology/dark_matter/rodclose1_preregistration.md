# OPEN-DM-RODCLOSE-1 pre-registration: the rod bend-and-close window — definitions, closed input list, the blindness protocol, structural geometry computed now, routes, and readings, committed before any derivation

**Patch 2541, 18 July 2026. Status: OPEN-DM-RODCLOSE-1 REGISTERED and OPENED at pre-registration; NO
derivation performed.** Grep collision check clean (no prior RODCLOSE ID). **Verify:
`code/2541_rodclose_prereg.py`. Lineage: successor to the HELD 2537 prereg under the §6g model shift
(2538–2540); inherits the 2529/2537 discipline apparatus in full. This document's frozen §§5–6 govern
the compute patch(es).**

## 0. What this campaign resolves, and the prize

Under §6g (as clarified in its two Addenda), T_form(DM) is set by the rod→ring bend-and-close window,
and the composition dial re-scopes to the plane-resident-vs-free fraction at that window. This
campaign attacks the WINDOW: for a rod of L stacked planes, at what thermal collision scale does the
bend-displacement–inertia–end-bond-and-close sequence fire, and what L-band does it select?

**The prize, and its blindness requirement (frozen NOW):** OPEN-SS-43 produced N = 8 elements (16
planes) from the stability side as sole survivor. A closure window selecting L ≈ 16 planes from the
formation side would be a second, independent route to the same number. The empirical 16 is currently
CONSUMED, not derived, on the formation side (founder disclosure, 2539 correction rider). Therefore:
**the compute patch treats L symbolically throughout; the window function W(L; T) and its selected
L-band are FROZEN in the compute patch before any comparison to 16 is written down.** A derivation
whose L-band is adjusted after meeting 16 = Branch T (output-justified step). The comparison procedure
is fixed here: freeze the band, then one sentence — is 16 inside it, and where.

**Scope limit (honest, frozen):** this campaign supplies T_form and the L-window. The plane-resident
fraction at that window (the re-scoped NB-F-1 dial proper) is a SEPARATE limb — not resolved here; the
2529/2530 reopening apparatus consumes it whenever it is supplied. No reading in this campaign is a
composition reading.

## 1. Definitions fixed

- **The rod:** L planes stacked at pitch D = 1.15 fm, alternating parity, each plane = 4 qCP core +
  4 eCP coat (the registered Candidate-B element-plane; §6g plane unit).
- **Closure geometry:** ring closure distributes total bend 2π over L inter-plane junctions:
  per-junction angle θ_L = 2π/L; ring radius R(L) = L·D/(2π).
- **E_bend(L):** the elastic energy to take the straight rod to the closed-ring configuration, at
  harmonic order in the per-junction bend, from the registered pure-bend stiffness lineage (input 2).
- **E_endbond:** the depth of the closure bond = the inter-plane stacking bond (founder identity, §6g
  Second Addendum): 4qCP-core-to-core preferential channel, 90°-offset/alternating-parity
  configuration.
- **ΔE_close(L) ≡ E_bend(L) − E_endbond.** ΔE_close < 0: closure downhill once bent (barrier = the
  bending itself); ΔE_close > 0: closure disfavored even bonded.
- **The window W(L; T):** the L-band in which (a) the thermal collision impulse scale at temperature T
  can supply the bend (short-rod stiffness cutoff), and (b) the rod's end inertia does not exceed what
  the impulse can displace through the closure sequence (long-rod inertia cutoff) — the founder's
  two-sided structure (Q5). The kinetic content of (a)/(b) is handled per §5's route split.
- **Proofreading clause (registered mechanism, rate-free):** accidental E_ee-type end closures anneal
  under ambient collisions where the qCP-core closure survives; the operative E_endbond is the strong
  channel. Comparative statement only; no absolute rate may be built on it.

## 2. Closed input list (nothing else may enter)

1. **Geometry:** plane = 4 qCP (square, edge a_q = 1.15 fm) + 4 eCP (diagonals, R_e = 1.301 fm,
   sequence eCP–qCP–qCP–eCP); pitch D = 1.15 fm; alternating parity; l_unit = 0.589 fm.
2. **Bend stiffness lineage:** the corrected pure-bend stiffness (+291, Patch 2450 — validated by
   independent builder, L-scaling, direction symmetry, 0.91-ratio decomposition). **Normalization
   task, frozen as a lineage-walk not a new input:** the compute patch must extract the units and
   per-junction normalization from the 2450 artifacts (script + reasoning) before use; if the
   normalization is not recoverable from the registered artifacts, that is Branch I on the stiffness
   (named blocker: bend-stiffness normalization), NOT license to re-derive a stiffness in-campaign.
3. **End-bond depth lineage:** the axial stacking wells — E_qq-branch map [40, 170] MeV; the 102 MeV
   contact-depth consistency lock (α_s·ℏc/a_qq, 2455); the founder end-bond identity and preferential
   4qCP-core channel (§6g Second Addendum). Band-strength, carried as a band.
4. **Inertias:** m_qCP = 132, m_eCP = 44 MeV/c² (2496 blind pin; 2452 in-situ convergent). Plane mass
   = 4·132 + 4·44 = 704 MeV; element (2 planes) = 1408 MeV.
5. **Thermal scale:** kT_form ≈ 16.5 keV carried as the registered corpus value with its
   consistency-gate status UNADJUDICATED (2529 input 6 lineage); the compute patch may test the window
   AT this value and report consistency, but may not adjust it.
6. **Standing pre-commitments:** 2521 (in-campaign rate construction = Branch T); the 2529 §6 Branch-T
   triggers verbatim; the 2529 trap clause + 2537 near-threshold extension (no composition reading in
   this campaign, §0 scope limit); the OBS-RELIC-1 √5 fence (any √5 in the window derivation →
   maximum-scrutiny provenance procedure).
7. **EXCLUDED, named:** any buffeting frequency, collision rate, or KE-spectrum sampling distribution
   (kinetics — Branch-I limbs per §5); the vision-tier ℏ-per-bond statement; any stiffness or depth
   not in inputs 2–3; N = 16 as an input in any form (blindness protocol, §0).

## 3. The impulse-scale convention (fixed now, before computation)

The window comparison needs a thermal impulse scale without building rates. Convention frozen: the
admissible statics-side comparator is the ambient per-collision energy scale ~ kT (input 5) and its
geometric leverage on the rod (moment arm ~ rod half-length L·D/2 acting against the bend stiffness;
end-mass inertia from input 4). Any refinement requiring a collision spectrum, flux, or duration
distribution is kinetics → the corresponding limb goes Branch I with NB-S3a-1 named. Choosing between
statics-admissible comparator forms by which one lands a preferred band = Branch T; if more than one
defensible form exists, ALL are computed and the band is reported as their union with the spread
disclosed.

## 4. Structural geometry computed NOW (2529-ceiling class; script-verified)

- θ_L = 2π/L; at L = 16 (stated for later comparison only, not consumed): θ = 22.5°, R = 16·1.15/(2π)
  ≈ 2.93 fm.
- Harmonic scaling shape: E_bend(L) = L·½·κ_θ·θ_L² = 2π²·κ_θ/L — **monotonically DECREASING in L** at
  fixed κ_θ. Frozen consequence: the short-rod cutoff (bending cost) and the long-rod cutoff (inertia)
  are AUTOMATICALLY two-sided under the founder's Q5 picture — the harmonic form guarantees bending
  gets cheaper with length while the inertia term grows, so a window (rather than a threshold) is the
  structurally expected shape. This is a consistency entailment of the founder's picture, banked
  before computation.
- Plane/element masses (input 4): 704 / 1408 MeV; ring at L = 16: 11.264 GeV (consistency echo of the
  registered candidate mass; consumed, not derived).

## 5. Routes (order LOCKED; post-hoc selection by output = Branch T)

- **R-A — statics window (first).** Walk the 2450 normalization (input 2); compute E_bend(L)
  symbolically; compare against E_endbond band (input 3) → ΔE_close(L) band; apply the §3 comparator
  at kT_form → the statics-admissible L-band, with the input-3 band and any comparator spread
  propagated as a band, never collapsed. Freeze W(L)-statics. THEN the one-sentence comparison to 16.
- **R-B — inertia cutoff refinement (only after R-A frozen).** The long-rod limb using input-4
  inertias and the §3 comparator. Statics-admissible portion only; anything needing collision duration
  or frequency → Branch I limb, NB-S3a-1 named.
- **R-C — full kinetic window (named, expected blocked).** The founder's complete multivariable
  problem (species mixture + KE spectrum + buffeting sequence) = NB-S3a-1 territory ⇒ Branch I by
  2521. Named so its absence is a recorded limb, not a silent gap.

## 6. Readings (frozen; committed now)

- **W(L)-statics frozen and 16 ∈ band** → formation-side convergence with OPEN-SS-43's stability-side
  N = 8 elements: **win-class result**; queues with the standing disclosure package for the next
  dispatch per the §6f governance ruling; conditionality ledger (band widths, comparator spread,
  kinetic limbs Branch I) travels in full.
- **W(L)-statics frozen and 16 ∉ band** → **adverse-direction recorded** as-is (no band re-derivation,
  no comparator swap, no input revisiting — any of those after the comparison = Branch T); the
  discrepancy becomes the named next problem.
- **Normalization unrecoverable (input 2) or comparator underdetermined (§3)** → Branch I with the
  named blocker; partial structure (the §4 entailments; ΔE_close band if reachable) banks.
- **Any √5 in the derivation** → fence procedure before any reading.
- **No composition reading under any outcome** (§0 scope limit; the trap clause governs).
- **T_form consistency note:** R-A reports whether the window at kT_form ≈ 16.5 keV is self-consistent
  (input 5); an inconsistency is RECORDED, not repaired in-campaign.

## 7. Campaign bookkeeping

79.5% PROVISIONAL-FAVORABLE untouched (pre-registration only; OPEN-DM-RELIC-1 remains CLOSED at D3;
this campaign feeds its reopening contract's T_form/window requirements but takes no composition
reading). Queued measurements (δ_E energy-weighted duty; MW-MODES TC-extension) remain ranked behind
this campaign per the standing handover ordering. The formal NB-F-1 re-scope annotation (dial =
plane-resident-vs-free fraction) rides with this registration; the fraction itself is the remaining
separate limb. Next patch: R-A, under this document only, beginning with the 2450 normalization walk.
