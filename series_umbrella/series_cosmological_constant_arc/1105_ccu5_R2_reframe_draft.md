# CC-U/5 — R2 reframe (DRAFT for the DM 08xx lane to apply)

**Patch:** 1105 (CC umbrella). **This is a handoff artifact, not an edit.** The target file lives in the
DM lane's owned subtree (`series_phenomena/cosmology/dark_matter/R2_sea_gravitation_scoping.md`),
so per the anti-collision protocol the CC window does **not** edit it. Thomas hands this to the DM
window, which applies it as its own patch in the 08xx band.

## Why R2 needs updating
`R2_sea_gravitation_scoping.md` is a **Patch-0705** deliverable (31 May 2026), written **before** the
SR-5 Step A–D arc (Patches 0720–0723). Its §3 ("what is NOT derived"), §4 ("what OPEN-SR-5 must
deliver"), and §5 ("do not write up yet; OPEN-SR-5 is a hard prerequisite") describe a state that the
A–D arc has since substantially superseded. The CC umbrella (Patches 1101–1104) banked the
reconciliation; R2 should be brought current so the DM identification reads off the right status.

## What changed since 0705 (the substance the DM lane should fold in)
- **§3.1 "horizon sensitivity / coincidence-restatement, not a derivation"** → **superseded.** Step C
  (0722) replaced the inserted (l_P/R_H)² with a *derived* substrate mechanism: `ρ_Λ = c²H²/8πG =
  (1/8π)ρ_P(l_P/R_H)²`, scaling **and** 1/8π derived; Step D3 **resolved the horizon ambiguity** by
  selecting the future event horizon (Li 2004; w_Λ(now) ≈ −1.02). It is no longer a coincidence-
  restatement.
- **§3.2 "time-dependence / why-now"** → now a **feature**, not a debt: the dynamical ρ_Λ ∝ H² is what
  *addresses* why-now (Λ larger in the past), per the CC umbrella's static-vs-dynamical verdict
  (dynamical; Patch 1101/1103). The static N⁴ reading is demoted to a present-epoch coincidence
  (1/N⁴ ≈ (l_P/R_H)² because R_H ≈ N²l_P today).
- **§4(i) derived suppression** → **DELIVERED** (Step C).
- **§4(iii) Friedmann recovery** → **DELIVERED** (Step D1; q crosses zero at z ≈ 0.63).
- **§4(ii) inhomogeneities gravitate as DM** → handled by the same excess-sourcing (c05); amplitude
  is the DM lane's own work (DM-1 manuscript 0844).
- **§5 "do not write up yet / hard prerequisite"** → the **uniform-Sea-inert half is essentially in
  hand** (DM-1 0844 records exactly this), conditional on the **c08 closed field equation**
  (op:einstein) — the one standing condition (see CC-U/4 scoping, `1105_ccu4_c08_scoping.md`).

## Proposed edit (the DM lane's call on exact wording)

**(A) Prepend a status banner** under the existing `**Status:**` line:

> **[UPDATE — superseded by SR-5 Steps A–D (Patches 0720–0723) and the CC umbrella (1101–1104).**
> The §3 "not derived / coincidence-restatement" framing and the §5 "do not write up yet" posture are
> stale. Step C **derived** the suppression `ρ_Λ = (1/8π)ρ_P(l_P/R_H)²` (scaling + coefficient); Step
> D3 **resolved** the horizon ambiguity (future event horizon, w_Λ ≈ −1.02); Step D1 **recovered**
> Friedmann (q→0 at z ≈ 0.63). The dynamical ρ_Λ ∝ H² is now the *resolution* of why-now, not a debt;
> the static N⁴ reading is demoted to a present-epoch coincidence (CC umbrella). **R2's uniform-Sea-
> inert half is in hand, conditional on the c08 closed field equation (op:einstein)** — the single
> standing cap, shared with the dark-matter split (see `series_umbrella/series_cosmological_constant_arc/`,
> Patches 1101–1104, and CC-U/4 scoping). Treat §3–§5 below as the historical 0705 snapshot.]**

**(B) Optional inline flips** (lighter touch, if the DM lane prefers not to prepend a banner): mark
§3 items as "SUPERSEDED (Step C/D3)", §4(i)/(iii) as "DELIVERED", and replace §5's "do not write up
yet" recommendation with "uniform-Sea-inert half in hand; conditional on c08; coordinate with the CC
umbrella."

## What this does NOT claim
R2's *gravitating-swirls-at-DM-amplitude* half (§4 ii) and the full DM identification remain the DM
lane's open work; this reframe only updates the *uniform-Sea-inert / dark-energy* leg to its true
(post-A–D) status. And it does **not** revive structure formation — CONJ-COSMO-1's structure-
formation role is a separate standing conditional-false verdict (Patch 0729). Everything remains
conditional on c08.
