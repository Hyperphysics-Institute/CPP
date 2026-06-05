# Reasoning capture — Patch 0750: specification of a CPP stack ensemble

*Session 154. A constructive specification (NOT a derivation) of what CPP would have to own for a CP
stack to carry μ ∝ ln(n/V) and thus derive n_s=0.9649. Writeup: `.../development/stack_ensemble_spec.md`.
NO THEO.*

## What this patch is and is not
- IS: a precise statement of the required ingredients (particles, volume, temperature, statistics, boost
  coupling) in CPP terms, each assessed for plausibility; an explicit, checkable commitment.
- IS NOT: a claim that CPP has such an ensemble. No prediction registered.

## Key points worked out
1. The tilt p=2 is ROBUST: independent of T's value, V's value, and the additive offset in μ=a+kT ln n
   (for large n the log term dominates d ln H/dN). So we need NOT derive T, V, or normalization -- only
   that the n-dependence is logarithmic and T~const over the ~7-8 e-fold window. This shrinks the
   derivational burden dramatically.
2. Volume V = the FIXED GP cell (not the PSR_base reach volume). Using the reach would be circular
   (PSR_base is what we compute) and would tangle the chemical potential with the answer. Over-occupation
   is a per-GP count (n where 1 belongs), so V = GP cell, concentration = n, μ ∝ ln n. Non-circular.
3. Temperature = ZBW jitter scale; value irrelevant to tilt, only ~constancy over the window matters
   (else d ln T/dN adds to the tilt). Plausible on the de Sitter plateau (local ZBW stationary).
4. Statistics MUST be Gibbs/indistinguishable (the 0749 lesson): ZBW phases as an exchangeable BATH, not
   permanent labels. Labels -> q^n -> constant μ -> cliff. Bath -> indistinguishable -> ln n -> 0.9649.
5. THE DEEP POINT: determinism is no barrier (classical stat-mech is deterministic + molecular chaos).
   The stack ensemble needs ZBW effective mixing/ergodicity -- which is the SAME assumption already used
   for the CLT/Gaussianity result (0738, 'CLT over ZBW phases'). So 'stack thermodynamics' is NOT a new
   bolt-on; it is the continuation of a commitment the sector already made. This materially lowers the
   cost and is the strongest honest point in the spec.
6. Bonus: μ ∝ ln n vanishes at n*=1, so H_eff -> 0 smoothly as n̄ -> 1: the graceful exit is automatic
   and is the SAME mechanism as the plateau (delivers the 0744 smooth-wind-down requirement for free).

## Honesty calibration
- Framed explicitly as specification, not derivation. NO THEO; no prediction registered.
- Separated robust (tilt p=2, given μ∝ln n + T~const) from assumed (ZBW-as-bath; boost∝μ) from
  falsifiers (ZBW-as-label -> cliff; fast-varying T -> extra tilt; field-driven boost -> 0746 stress
  branch -> excluded).
- Did NOT overstate the ZBW-Gaussianity link: it is the SAME CLASS of assumption (ZBW as effective
  stochastic bath), applied to a different observable -- not literally identical. Stated as such.
- The remaining decision is correctly posed as a single foundational question: does the ZBW layer make a
  CP stack a thermodynamic ensemble?

## Pointer
- If CPP can own (A) ZBW-as-bath -> Gibbs stack and (B) boost∝μ, write and register the chain
  ZBW-bath -> Gibbs stack -> μ∝ln(n/V) -> H_eff∝ln n -> n_s=0.9649 (coefficient-free, N_* from CP count).
  Clear of chirality. PCD = Perceive/Compute/Displace.
