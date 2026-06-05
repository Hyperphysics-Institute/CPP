# Bath-clause grounding: leg 1 reduces to standing CPP commitments

*Patch 0769, Session 154. With the long-range √n̄ corner closed (0768), the load-bearing condition for
n_s = 0.9649 is the bath clause itself (leg 1: the CP occupations reach the ZBW/substrate Gibbs state fast
enough). This finding grounds leg 1 in commitments the framework already holds, rather than treating it as a
free-floating assumption. Script: `scripts/0769_bath_timescale.py`. NO THEO (leg 1 is grounded, not proven
from A1–A11; n_s stays conditional).*

## Leg 1 decomposes into three pieces — each already in the corpus

**(a) Mixing exists.** The bath clause needs the CP occupations to be ergodically mixed. The mixing
mechanism is **ZBW switching**: a CP switches between DP partners at a rate that is "deterministic but
appears random due to the complexity of the local SSV field… the CPP origin of quantum randomness — not
ontological indeterminacy but practical unpredictability" (`master_glossary.md`). This is **not a new
assumption** — it is the *same* effective-randomness mechanism CPP already uses for:
- quantum randomness (the glossary statement above), and
- the Gaussianity of the primordial spectrum (CLT over ZBW phases, Patch 0738).
The bath clause is a **third application** of one standing commitment. The ZBW switching that randomizes
quantum outcomes and Gaussianizes the fluctuations is the same switching that ergodically mixes the
occupation states.

**(b) Fast enough (R ≪ 1).** Equilibration time τ_eq ~ N_mix · t_P (N_mix ZBW re-mixings at the substrate
clock t_P = ℓ_P/c); e-fold time t_efold ~ 1/H_inf (macroscopic). So

  R = τ_eq / t_efold = N_mix · t_P · H_inf = **N_mix · (H_inf / E_Pl).**

| inflation Hubble scale | H/E_Pl | R (N_mix=30) |
|---|---|---|
| Planckian H ~ E_Pl | 1 | 30 (fails — excluded) |
| near-Planck 10¹⁷ GeV | 8×10⁻³ | 0.25 |
| high-scale 10¹⁶ GeV | 8×10⁻⁴ | 0.025 |
| typical 10¹⁴ GeV | 8×10⁻⁶ | 2.5×10⁻⁴ |
| low-scale 10¹³ GeV | 8×10⁻⁷ | 2.5×10⁻⁵ |

For **any sub-Planckian inflation scale**, the occupations are re-thermalized 10⁴–10⁶ times per e-fold —
R ≪ 1 by many orders. The only way R ~ 1 is Planckian inflation (H_inf ~ E_Pl), which is **doubly
excluded**: by the observational tensor bound (H_inf ≲ 10¹⁴ GeV) and by CPP's own H-axiom (the lattice-
growth ceiling forbids sustained near-Planck recession — `axiom_h_inflation_engine_evaluation.md`). N_mix =
O(10–30) is the only input, and it was already measured by the 0753 minimal-PCD MC toy. This is the **same
substrate-vs-macroscopic separation** that makes kT ~ E_Pl the relevant bath (LEMMA-NS-BATH, 0767): the
substrate is fast and hot at its own scale; everything cosmological is slow and comparatively cold.

**(c) The stationary state is the *indistinguishable* Gibbs state.** Fast mixing to *a* stationary state is
not enough; it must be the indistinguishable-occupation Gibbs state (the one that gives μ ∝ ln n̄ and the
0.9649 tilt), not a labelled/distinguishable state (which gives the n_s = 1 cliff, 0749). This is fixed by
**A1**: a CP is polarity + type + position and nothing else — no identity — so CP configurations *are*
occupation-number objects and the only stationary state available is the indistinguishable one. Secured at
0749/0752; the ZBW dynamics act on the A1 state space by construction, so they cannot manufacture spurious
labels.

## Net: leg 1 is a corollary of standing commitments

Leg 1 (bath reality) = **(a) the standing ZBW effective-randomness commitment** (shared with quantum
randomness + CLT-Gaussianity) **+ (b) the substrate-vs-macroscopic timescale separation** (R ≪ 1 for sub-
Planckian inflation, the only input N_mix = O(10–30) toy-measured) **+ (c) A1** (indistinguishable
stationary state). None of the three is a new free parameter or a new assumption; all three are already
load-bearing elsewhere in CPP.

## Honest scope

- This **grounds** leg 1 — it does not **prove** it from A1–A11. The ZBW ergodicity is a framework-level
  commitment (the same epistemic status it has for quantum randomness), and N_mix = O(10–30) is toy-
  measured, not derived. What changes is that leg 1 is no longer a *separate* assumption tailored to the
  n_s result; it is the n_s instance of a commitment CPP already makes three other ways.
- The n_s = 0.9649 prediction remains **conditional**, but its conditionality is now cleanly stated: it
  rests on (1) the standing ZBW-ergodicity commitment + A1 [leg 1, here grounded] and (2) a charge-neutral
  effective equation of state [leg 2, 0756 toy-supported]. There is no longer a bath-clause assumption that
  stands apart from the rest of the framework.
- A natural hardening (future): a detailed-balance / H-theorem argument that the minimal-PCD occupation
  dynamics provably relax to the A1 Gibbs state would upgrade (a)+(c) from "grounded" to "derived." The
  0753 toy is the numerical stand-in for now.

## Pointers

- Mechanism: `master_glossary.md` (ZBW switching = effective randomness); 0738 (CLT-Gaussianity, same
  mechanism); 0749/0752 (A1 → indistinguishable Gibbs state); 0753 (minimal-PCD MC toy, N_mix); 0767
  (LEMMA-NS-BATH, same timescale separation).
- Numerics: `scripts/0769_bath_timescale.py` (R = N_mix·H_inf/E_Pl across inflation scales).
- Reasoning: `reasoning/0769_bath_clause_grounding.md`.
