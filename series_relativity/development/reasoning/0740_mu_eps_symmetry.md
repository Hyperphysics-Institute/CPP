# Reasoning capture — Patch 0740: DP-Sea μ↔ε symmetry (α-variation = impedance-variation)

*SR-1 rederivation pass, Session 154. Resolves the 0739 Δc-filter residual. Writeup:
`series_relativity/development/dp_sea_mu_eps_symmetry.md`. Demonstrator:
`.../early_universe/scripts/0740_mu_eps_impedance_symmetry.py`. NO THEO.*

## The reduction that did the work

The 0739 filter left "is the DP-Sea SSV response μ↔ε symmetric (A≈0)?" as the open piece. The clean
move: c=1/√(μ₀ε₀) and Z₀=√(μ₀/ε₀) give μ₀=Z₀/c, ε₀=1/(Z₀c), so under an SSV step
  Δc/c = dc (product),  Δα/α = dZ (ratio),  A = −dZ/dc.
**Δα/α = Δ ln Z₀ exactly.** The entire danger collapses to one number: does the impedance move under
SSV? This is the cleaner form of the d_μ/d_ε framing from 0739 (A independent of ΔSSV magnitude — it's
a structural property of the response, not a perturbation size).

## I read the corpus before asserting (did NOT invent physics)

Grounding facts found:
- c06: photon magnetic component = "curl of the propagating SSV pattern" ⇒ B locked to E by curl over
  the GP network, NOT an independent susceptibility ⇒ μ,ε are two views of one ZDC propagation.
- c06: "all four DP types participate equally" ⇒ no species-selective (composition) channel to split
  E vs B response — directly addresses the qDP-density channel 0739 flagged.
- c06: Z₀=√(μ₀/ε₀) is explicitly "to be derived in lattice units" / "express μ₀,ε₀ in terms of the
  600-cell stiffness C and broadcast speed c" — i.e. the symmetry reduces to an ALREADY-REGISTERED
  CPP task. CPP currently fixes the PRODUCT (=1/c²) but not the RATIO (Z₀).
- Brick #2 / SR-1: GPs fixed/eternal ⇒ the curl/broadcast geometry setting Z₀ is fixed-lattice; SSV
  moves stiffness C and reach c, not the geometric ratio. THIS is what makes Z₀ geometric — and it
  ties the cosmology result straight back to Brick #2.

## Honesty boundary

I did NOT claim the symmetry is proven. I claimed: it reduces exactly to "is Z₀ geometric?", the three
corpus facts all indicate yes, and the explicit Z₀(C,c) derivation (already on c06's books) is the
remaining step — with a sharp pass/fail: Z₀ must come out C-independent (pure 600-cell geometry). Pass
⇒ A=0, Δc residual CLOSED, c_eff variation purely gravitational. Fail (Z₀∝C) ⇒ k_α~1, dead by ~6
orders vs the clock bound. The script confirms the algebra (identities) and tabulates the two outcomes;
it does not (cannot yet) compute Z₀ from C — that's the owed derivation.

## Bonus: not make-work

The Z₀(C,c) derivation is independently needed by c06 for the photon emission envelope / natural
linewidth (Δν∝ν³, Einstein-A). Same computation, two payoffs (closes cosmology Δc residual + advances
EM substrate). I added a cross-ref note in c06's future-work to record the second motivation.

## Conventions
- NO THEO (structural reduction + conditional argument). No new prediction/term/axiom registered (the
  falsifiable Z₀-geometric statement is conditional on the owed derivation). Verify script bundled.
  Clear of chirality. PCD = Perceive/Compute/Displace (SSV per master_glossary: SSV_abs determines
  local time rate and PSR).

## Pointer
- Next first-principles targets: (1) the c06 Z₀(C,c) derivation (proves/refutes this symmetry — hands
  off to the EM sector); (2) the superposition-thinning roll-off law (0738, upgrades n_s tuning→
  prediction). When both resolve, fold semantics into SR-1 and dispatch to the review panel.
