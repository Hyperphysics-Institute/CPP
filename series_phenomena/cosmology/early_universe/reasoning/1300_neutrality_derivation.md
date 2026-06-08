# Reasoning fragment — Patch 1300 (W3): leg-2 neutrality, topological derivation attempt

*Verbatim-grade reasoning capture bound to the patch-delivery contract. Window W3, Phase-0 parallel round.*

## The move

Leg 2 (0770) was *grounded* by asserting the DP-pair structure (glossary: DP = neutral ± pair) and reading off
n₊ = n₋. That assumes the structural fact. I looked for whether A1–A11 *force* it instead.

The unlock: leg 2 does not actually need *local* pairing — it needs **global** Q = 0 (the mean-field term is
∝ Q²; the local √n̄ piece is the separately-closed Debye thread). Global Q = 0 is exactly the quantity the
closed-manifold Gauss law fixes: **total charge on a compact boundaryless manifold is identically zero**, the
standard "a closed universe must be charge-neutral" result. CPP hands us the closed manifold for free — A2's
600-cell {3,3,5} *is* the regular tessellation of S³.

## Chain (A1+A2+A3+A6′)

1. A2 → substrate = S³ tessellation, compact, ∂ = ∅. f-vector check V−E+F−C = 0 = χ(S³).
2. A1 → CP polarity ± = charge ±q; Q = q(n₊−n₋).
3. A3+A6′ → U(1) edge field with local Gauss ∇·D = ρ, CP polarity the sole source. ← the one bridge (L1).
4. ∮_{∂S³} D·dA = 0 (no boundary) ⇒ ∫ρ = 0 ⇒ Q = 0 ⇒ n₊ = n₋, exact.
5. No boundary ⇒ ΔQ = 0 ⇒ neutrality holds at every occupation as n̄ ∝ e^{−3N} dilutes (pairwise removal).
6. b₂(S³) = 0 ⇒ no harmonic-2-form flux sector ⇒ no loophole (S³-specific; T³ would fail with b₂ = 3).

## Why it's better than 0770, honestly

- Derives the DP-pair *global* balance from topology; A10 attraction then gives local pairing → the DP Sea is a
  *consequence*, not a premise. Inverts the 0770 logic.
- Kills the 10⁻⁹ caveat for the charge channel: electric Q is *exactly* 0 by topology; the 10⁻⁹ is baryon/matter
  asymmetry, which does not source the Coulomb mean-field. This was the part I was most careful about — I had to
  separate "net charge" from "matter asymmetry," which 0770 had blurred.
- Independent of the glossary route ⇒ genuine second path to the same requirement (swarm-validation flavor).

## Where I held the line (escalation honesty)

It does NOT bottom out at a new axiom — so this is not the register-and-stop escalation outcome; it's a real
reduction to A1+A2+A3+A6′. But I did not overclaim "fully derived." Two bridges remain:
- **L1 (LEMMA-EU-NEUTRAL-GAUSS):** edge-sector U(1) Gauss law sourced solely by CP polarity. Maxwellian content
  of A6′ + A3; *implied*, not literally written. This is the load-bearing step and I flagged it as such rather
  than smuggling it.
- **R1:** A2's closed-S³ reading vs an infinite-flat reading. Closed → topological identity; flat → boundary
  condition D→0 at infinity. Both give Q = 0; I named the closed reading as primary (assumption-free, matches
  closed-FRW) and recorded the flat alternative honestly.
- R3 (loophole) is discharged by b₂(S³)=0, not left hanging.

So the claim I'm willing to defend: **leg-2 neutrality is derivable from A1–A11, conditional on L1**; promote
grounded→derived(conditional on L1); propose THEO-EU-NEUTRAL + LEMMA-EU-NEUTRAL-GAUSS for panel review. NO THEO
registered by me (registry freeze + no-THEO-for-conditional until the panel rules on L1).

## What I deliberately did NOT claim

- Did NOT claim this closes OPEN-EU-1 (homogeneity + ZRP-correction are untouched — those are the hard core).
- Did NOT change the PRED-C-96 count or its framework-conditional status (leg 1 + homogeneity still gate that).
- Did NOT touch neutrality_grounding.md, EU-1/, or any shared registry — handoff note only.

## Script

`scripts/1300_neutrality_topology.py` — ALL PASS (f-vector/χ; Betti/no-loophole; conservation at all occupations
+ open-system contrast). Structural checks only; no fit, no parameters.
