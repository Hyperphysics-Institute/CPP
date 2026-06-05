# Reasoning capture — Patch 0767: bath-temperature lemma (LEMMA-NS-BATH)

*Session 154. Acts on ChatGPT's review of 0766: asked for one lemma — mu in the H_eff ∝ mu tilt chain is
evaluated w.r.t. the ZBW/substrate bath, NOT the macroscopic de Sitter temperature; "if accepted, the
long-range corner is effectively closed PASS." Finding: `bath_temperature_lemma.md`. NO THEO.*

## The lemma
LEMMA-NS-BATH: mu(nbar) in the tilt chain (H_eff ∝ mu; mu = kT ln nbar + const; n_s-1 = -2/N_*), and any
mu_excess in it, is evaluated w.r.t. the ZBW/substrate bath (kT ~ hbar c/l_P = E_Pl), NOT the macroscopic
de Sitter temperature.

## Why it follows from the bath clause (not new)
Bath clause (0750-0752) = the CP occupations are thermalized by ZBW substrate dynamics (ZBW = exchangeable
bath -> Gibbs ln nbar). A chemical potential is defined relative to the bath the ensemble equilibrates
with. The occupation ensemble equilibrates with the ZBW (bath clause) -> mu and mu_excess are substrate-
level at the ZBW temperature. De Sitter T = macroscopic/horizon descriptor, not the substrate occupation
bath. Gaussian amplitude also ZBW-sourced (CLT, 0738). So LEMMA-NS-BATH is a COROLLARY of the bath clause:
the bath that sets the log is the bath that sets mu_excess, and it's the ZBW/substrate one.

## Consequence
kT_bath = kT_ZBW ~ E_Pl -> kappa ~ 1 -> Gamma = alpha/kappa ~ alpha ~ 7.3e-3 -> |mu_ex|/kT ~ c alpha^{3/2}
~ 3.6e-4 << ln nbar ~ 170. Minimal PASS requirement kappa >~ 1e-4 (kT >~ 2e15 GeV); ZBW bath clears by
~4 orders. Long-range corner CLOSED PASS, conditional only on the bath clause (Reading A).

## Conditionality update
n_s=0.9649 was conditional on (a) bath, (b) neutrality, (c) no surviving long-range sqrt(n). Leg (c)
DISCHARGED by chain: kernel=Coulomb (0764) -> residual coupling-bounded c Gamma^{3/2} (0764) -> Gamma=
alpha/kappa grounded (0766) -> kappa~1 by LEMMA-NS-BATH (0767). Remaining conditionality = always-present
legs (a) bath clause + (b) neutrality. No separate sqrt(n) leg.

## Honesty discipline
- LEMMA-NS-BATH is a conceptual COROLLARY of the bath clause, not a hardened theorem; finding-level, NOT in
  theorem-registry. Strength = bath clause's strength.
- Closes the sqrt(n) corner GIVEN the bath clause; does NOT make n_s unconditional (still rests on bath
  clause + neutrality).
- Steelmanned Reading B (de Sitter bath): rejected as the consistent reading because the occupations
  equilibrate with the ZBW (bath clause), not the horizon radiation; de Sitter T doesn't set substrate
  occupation statistics. Not cherry-picking -- the consistent reading given the established mechanism.
- Offered to panel for final check (ChatGPT named this the one statement to pin).
- NO THEO (conditional result).

## Pointer
- If panel accepts LEMMA-NS-BATH, the long-range corner is settled; arc's open items reduce to the bath
  clause's own confirmation (Ewald Stage A/B, MC bath toy 0753) + neutrality. Then, if those hold, register
  n_s=0.9649 + alpha_s~-0.0006. PCD = Perceive/Compute/Displace.
