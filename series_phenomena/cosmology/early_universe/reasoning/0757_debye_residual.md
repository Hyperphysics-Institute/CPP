# Reasoning capture — Patch 0757: the Debye √n̄ residual

*Session 154. Head-on analysis of whether a Debye-Hueckel mu_excess ~ -sqrt(n) survives charge
neutrality and sinks the tilt at cosmological occupation. Finding: `.../debye_residual_finding.md`.
Script: `.../scripts/0757_debye_residual.py`. NO THEO.*

## The threat
Neutrality cancels the LEADING mean-field (~n). The Debye correction is the NEXT order, mu_ex ~ -sqrt(n)
(kappa^2 ~ n q^2/kT), NOT removed by neutrality. At nbar~1e74: ln nbar~170, sqrt(nbar)~1e37, nbar^1/3~5e24.
Any power beats ln by >=35 orders -> a surviving sqrt(n) sinks the tilt. Worry is legitimate.

## Three-part resolution (computed)
A. Magnitude: confirmed any power residual at 1e74 dwarfs ln n -> tilt survives only if power residual
   ABSENT at cosmological occupation.
B. Debye validity: sqrt(n) is weak-coupling; N_D=(4pi/3)n lambda_D^3 ~ (kT/q^2)^{3/2} n^{-1/2} DECREASES
   with n. DH valid only n < n_* ~ (kT/q^2)^3. n_* reaches 1e74 only if kT/q^2 >~ 1e24.7 (q^2 ~25 orders
   below kT). For any appreciable coupling, n_* << 1e74 -> sqrt(n) cut off far below cosmological occ.
C. Point-stack: sqrt(n) needs 3D spatial charge correlations (screening clouds). A1: CP position IS the
   GP; co-located CPs share ONE position, no sub-GP space -> on-site/contact interaction -> NO screening
   substrate. Numeric: balanced on-site mu_excess over lambda{5..80} fits slope vs sqrt(n)=-0.002 (~0,
   no Debye) and vs n=-0.0001 (~0, mean-field cancelled). Only ideal ln n survives. Strong-coupling
   n^1/3 (Madelung) also needs a spatial charge lattice -> also absent for the point-stack.

## Verdict
sqrt(n) REAL in continuum charge-neutral plasma (neutrality NOT sufficient) but does NOT survive to 1e74
in CPP: Debye exit (n_* << 1e74 for any non-tiny coupling) + no sub-GP spatial substrate for the on-GP
stack. Only escape: long-range inter-GP SSV with absurdly weak coupling (n_* >~ 1e74) -- sharp falsifiable
knife-edge, not a generic killer. De-risked, not fully closed.

## Honesty calibration
- Confirmed the worry is real (continuum sqrt(n) survives neutrality) BEFORE showing why it doesn't reach
  cosmological occ -- did not wave it away.
- Two INDEPENDENT cutoff arguments (Debye-regime exit; point-stack no-spatial-substrate), strongest leg
  (point-stack) rests on A1.
- Dropped O(1) prefactors -- flagged; n_* is order-of-magnitude (fine vs 35-order gap, but real coupling
  must be plugged in).
- Did NOT simulate a real long-range lattice Coulomb -- argued inter-GP case via the crossover; flagged
  the inter-GP lattice-plasma calc + real SSV range as the remaining check. Explicitly 'de-risked, not
  fully closed'.
- Updated the conditional-prediction status with the third condition (c): SSV coupling not absurdly weak /
  effectively on-site for the stack. All three conditions falsifiable.

## Pointer
- Add to swarm request: the real SSV interaction range + inter-GP lattice-plasma mu(n) calc; does a sqrt(n)
  or n^1/3 survive for the actual SSV? Clear of chirality. PCD = Perceive/Compute/Displace.
