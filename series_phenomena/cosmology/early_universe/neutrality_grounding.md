# Neutrality grounding: leg 2 reduces to the DP-pair structure of the vacuum

*Patch 0770, Session 154. With leg 1 (bath reality) grounded (0769, panel-confirmed) and the √n̄ corner
closed (0768), the last live leg of n_s = 0.9649 is leg 2 — the charge-neutral effective equation of state
that 0756 found the tilt requires. This finding grounds it in the DP-pair structure of the CPP vacuum.
Script: `scripts/0770_neutrality_dp_pairs.py`. NO THEO (grounded; n_s stays conditional).*

## What leg 2 needs (from 0756)

The interacting MC (0756) showed: a balanced ± plasma (K = K_att) → μ_excess flat (ideal, no tilt
contamination); an unbalanced plasma → a spurious slope that contaminates the tilt. So the tilt requires
the early CP plasma to be **charge-neutral (± balanced)**. 0756 left this as a falsifiable requirement; this
finding supplies it from first principles.

## The grounding: the vacuum is built from bound ± pairs

From `master_glossary.md`:
- **DP (Dipole Pair) = "a bound pair of opposite-polarity CPs (+ and −)"; "a DP is electrically and
  colour-neutral."**
- **DP Sea = "all lattice sites occupied by DPs in their ground state"** — the CPP vacuum.

So the substrate / early CP plasma is composed **entirely of bound ± pairs**. The occupation that drives the
tilt is therefore a stack of DPs — equivalently, of CPs in exact ± balance.

> **Occupation variable (ChatGPT calibration, made explicit):** the grounding holds *provided the inflating
> occupation stack is a DP / DP-Sea occupation stack, not an arbitrary unpaired-CP plasma.* The two readings
> coincide: if the occupation variable n counts **DPs**, neutrality is automatic (each unit is a neutral
> pair); if it counts **individual CPs**, then n is even and the CPs enter in ± pairs (n₊ = n₋). Either way
> the stack is ±-balanced by construction. The tilt's log (indistinguishable occupation counting, A1) is
> unaffected — it counts occupation units; neutrality constrains their ± composition, which the DP-pair
> structure fixes.

Consequently:
- n₊ = n₋ **exactly** at every occupation n (each added unit is a neutral ± pair),
- net charge Q(n) = 0 **identically**,
- the mean-field Coulomb term (∝ Q²) **vanishes at every n** — which is precisely the 0756 "balanced ±,
  K = K_att" ideal case, for which μ_excess is flat and the tilt is uncontaminated.

| n (CPs) | n₊ | n₋ | net Q | mean-field (∝Q²) |
|---|---|---|---|---|
| 10 | 5 | 5 | 0 | 0 |
| 10³ | 500 | 500 | 0 | 0 |
| 10⁵ | 50000 | 50000 | 0 | 0 |

**Neutrality is not an assumption tailored to the n_s result** — it is the ± pair structure of the DP Sea
vacuum, the same structure that makes the CPP vacuum electrically neutral everywhere. The DP-pair
construction is load-bearing across the corpus (eDP/qDP/hDP species, the vacuum energy density, all of QFT-
analog physics), so leg 2 is the n_s instance of a standing commitment — exactly as leg 1 turned out to be.

## The √n̄ leg is not reopened

The only n-dependent residual after the mean-field cancels is the **local Poisson charge fluctuation**
~ √n̄ per Grid Point — the long-range Debye term. That is the √n̄ residual **already closed PASS** (0764–
0768): bounded by c·Γ^{3/2} with Γ ~ α at the substrate bath. So grounding leg 2 does not reopen the closed
√n̄ corner; the two are consistent — global balance (leg 2) kills the mean-field, and the local fluctuation
(the √n̄ thread) is separately bounded.

## Honest scope

- This **grounds** leg 2 — global ± balance follows from the DP-pair construction (glossary), which is a
  framework-level commitment, not a theorem derived from A1–A11. Same epistemic status as leg 1's grounding.
- **Caveat (owned, sharpened per ChatGPT):** a tiny global charge/matter asymmetry (~10⁻⁹, the baryon-
  asymmetry scale; cf. Capotauro leptogenesis) breaks exact balance at the 10⁻⁹ level. This is physically
  expected to be harmless, but the honest statement is: **any cosmological charge asymmetry is subleading
  and must be checked not to reintroduce an O(n) chemical-potential slope.** The 0756 cancellation needs
  only |imbalance| ≪ 1, not exactly 0, and a 10⁻⁹ fractional imbalance is far below any tilt-relevant
  threshold — but this is a check to record, not to wave away. Not a blocker.
- With this, **both legs of n_s = 0.9649 are grounded in standing CPP commitments:** (1) ZBW-ergodicity +
  A1 [leg 1, 0769] and (2) DP-pair neutrality [leg 2, here]. Neither is a bespoke assumption. The result is
  now at the level ChatGPT named as registerable — **a conditional/grounded zero-new-axiom prediction**,
  not a fully-derived one. Registration is the next step, pending the panel's sign-off on leg 2.

## Pointers

- Requirement: 0756 (interacting MC — balanced → flat; unbalanced → contaminated).
- Grounding: `master_glossary.md` (DP = bound ± pair, neutral; DP Sea = vacuum).
- √n̄ consistency: 0764–0768 (local Poisson residual bounded, closed PASS).
- Numerics: `scripts/0770_neutrality_dp_pairs.py`.
- Reasoning: `reasoning/0770_neutrality_grounding.md`.
