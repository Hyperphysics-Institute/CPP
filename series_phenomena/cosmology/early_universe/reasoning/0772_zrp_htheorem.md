# Reasoning capture — Patch 0772: bath-clause H-theorem (LEMMA-NS-HTHEOREM)

*Session 154. Hardening of leg 1 (Thomas chose this over leg-2 A1-A11 derivation). Upgrades leg 1(a)
relaxation + 1(c) indistinguishable-Gibbs stationary state from GROUNDED (0769) to DERIVED, given the ZRP
model. Finding: `bath_htheorem.md`. Script: `scripts/0772_zrp_htheorem.py`. Finding-level lemma, NO THEO.*

## Model
Minimal-PCD / ZBW occupation dynamics = symmetric constant-rate ZERO-RANGE PROCESS:
- state = occupation numbers (A1: indistinguishable CPs -> occupation-number objects);
- each CP hops independently at the ZBW rate (=1) to a uniform neighbour: rate g(n_i)*p(i,j), g(n)=n,
  p(i,j)=1/deg(i) symmetric.

## H-theorem (theorem, given the model)
1. Reversibility: detailed balance w.r.t. product-Poisson (multinomial at fixed N). Verified machine-prec
   (~1e-17) on exact L=3,N=6 generator (28 states).
2. KL Lyapunov: H(t)=KL(P(t)||pi) monotone non-increasing (any Markov gen w/ stationary pi), strict until
   P=pi. Verified: H(0)=6.59 -> 2.3e-10 monotonically (exact matrix exponential). => leg 1(a) relaxation.
3. Stationary = indistinguishable Gibbs: pi = product-Poisson; n_i! = Gibbs indistinguishability divisor
   (0749) -> mu = kT ln rho -> mu prop ln nbar (tilt's log). Marginal Binomial(N,1/L) -> Poisson(N/L) as
   N->inf (exact at nbar~1e74). Distinguishable/labelled state (n_s=1 cliff) is NOT stationary. => leg 1(c).
4. tau_eq from spectral gap = O(1) in ZBW units, non-vanishing w/ system size (gap=1.5 on test system) ->
   R = tau_eq H_inf << 1 (0769). Precise prefactor != 0753 toy's N_mix (system/normalization); the H-theorem
   secures a FINITE gap, which is what 'fast enough' needs.

## Upgrade
leg 1(a)+(c): grounded (0769) -> DERIVED given ZRP model. Distinguishable cliff EXCLUDED as stationary
measure, not just disfavoured.

## Honest scope
- Math standard (ZRP reversibility + KL monotonicity); CPP content = IDENTIFICATION minimal-PCD/ZBW =
  symmetric constant-rate ZRP. That's the new, more minimal, checkable premise (independent hops, rate-
  homogeneous, symmetric lattice).
- n_s stays conditional/grounded (premise is a model, not A1-A11); NOT promoted to Section 1 / counted swarm.
  Conditionality now concentrated in ONE minimal modelling statement.
- Deeper target: A1-A11 derivation that PCD update IS a symmetric constant-rate ZRP. Registered next step.
- LEMMA-NS-HTHEOREM finding-level, NO THEO (standard math + residual model premise).

## Honesty notes
- Did NOT overclaim: explicitly 'derived GIVEN the ZRP model', residual named, n_s still conditional.
- Owned the spectral-gap/N_mix number mismatch with 0753 (system/normalization-dependent; the robust claim
  is finite gap, not the exact prefactor).
- Binomial->Poisson only a limit at finite N (N=6 not close); noted exact at cosmological nbar.

## Pointer
- Next options: (i) A1-A11 derivation of the ZRP identification [completes leg 1 -> derived]; (ii) A1-A11
  derivation of DP-pair neutrality [leg 2]. Either upgrades n_s toward Section-1/counted. PCD =
  Perceive/Compute/Displace.
