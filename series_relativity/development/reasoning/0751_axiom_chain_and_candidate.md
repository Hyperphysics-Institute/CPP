# Reasoning capture — Patch 0751: candidate axiom CAND-AX-EU-1 + derivation chain

*Session 154. Drafts a CANDIDATE axiom (ZBW thermalizes a CP stack) + the conditional chain to
n_s=0.9649, for the swarm to accept/reject. Writeup: `.../development/stack_ensemble_axiom_and_chain.md`.
Verify: `.../scripts/0751_axiom_chain_verify.py`. NO THEO; nothing registered.*

## Status discipline
- Explicitly CANDIDATE. Did NOT edit axiom-registry.md / theorem-registry.md / predictions.md -- editing
  any would assert an acceptance the swarm has not given. The whole point is to present a clean
  accept/reject object, with the cost (axiom count 9->10) stated honestly.
- Provisional labels CAND-AX-EU-1 / CAND-THEO-EU-1 chosen after grepping registry: no existing AX-EU /
  THEO-EU / CAND IDs, no collision. The 9-axiom set is labeled A1-A11 (consolidations); H-engine is held
  as adopted-working in the early_universe folder, not in the 9.

## The axiom, minimally stated
Two assertions only: (i) n identical CPs on a GP are INDISTINGUISHABLE (1/n! Gibbs factor); (ii) the ZBW
layer mixes fast enough that a stack has a free energy F(n,T) and chemical potential mu=dF/dn. The
prediction flows entirely from (i); (ii) makes mu legitimate. Does NOT posit T, V_GP, or kappa.

## The chain (each step standard)
1. axiom -> Z_n = z1^n/n!.
2. F=-kT ln Z_n -> mu(n)=kT ln(n/z1)=kT ln n + const. The ln n IS the -ln(n!) term.
3. nbar(N)=nbar_init e^{-3N}; ln nbar = 3 N_rem (reach volume ~ e^{3N}).
4. boost ~ mu rel. to equilibrium n*=1: H_eff=kappa(mu(nbar)-mu(1))=kappa kT ln nbar ~ N_rem [0746].
5. P~H_eff^2 (spectator/dN) -> n_s-1=2 d ln H_eff/dN = -2/N_rem.
6. N_*=(1/3)ln(N_CP/N_GP)~60.5, pivot ~57 -> n_s=1-2/57=0.9649; alpha_s=-2/N_rem^2~-0.0006.

## What the verify script proved (computed, not asserted)
- COEFFICIENT-FREE: varied kappa (1e-2..1e3), kT (1e-4..50), ln z1, offset (-15..20). n_s=0.9649 EVERY
  time -- all coefficients drop out of d ln H_eff/dN. Only N_* (from CP count) survives.
- AXIOM-NECESSITY: replacing Gibbs (Z=z^n/n!) with distinguishable labels (Z=z^n) collapses mu to const
  -> n_s=1.0000 (cliff). So the 1/n! indistinguishability IS the load-bearing ingredient.

## Honesty calibration (where a skeptic should push)
- (A) the axiom is STRONGER than CLT-Gaussianity (0738): CLT needs independence+finite variance; a Gibbs
  mu needs full configurational equilibrium. Stated this as the legitimate weak point -- a skeptic can
  accept ZBW-Gaussianity yet decline a full stack chemical potential. Did NOT paper over this.
- (B) boost~mu is the 0746 count-driven branch; if field/stress-driven -> excluded. Commitment, not
  theorem.
- (C) T~const over window; if d ln T/dN ~ 1/N_rem it adds tilt. Plausible on plateau, flagged to check.
- (modelling) spectator P~H^2 vs single-field 1/eps form (would add eps-running). Flagged.
- Robust GIVEN A,B,C: 0.9649 coefficient-free; graceful exit automatic (mu->0 at n*=1).
- Offered an honest middle path (accept provisionally as working axiom, like the H-engine, with the
  asterisk visible) rather than forcing a binary.

## Pointer
- IF accepted: register axiom (9->10), THEO-EU-1, PRED entries; update early-universe sector. NOT done
  -- pending swarm. Clear of chirality. PCD = Perceive/Compute/Displace.
