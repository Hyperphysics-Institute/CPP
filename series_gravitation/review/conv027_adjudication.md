# CONV-027 ADJUDICATION + THE A-5 CLOSURE ANNEX

**Patch 3261 (20 Aug 2026, Session 150). All five seats returned
same-session; returns registered verbatim in `reviews-CONV-027.md`.
Annex verify: `code/3261_a5_closure_annex_verify.py`, 6/6 PASS.**

## §1 — Seat and defect ledger

Seat attribution is by the founder's paste order. Two protocol defects,
recorded, votes counted:

- **Gemini seat:** IDENTITY DEFECT — the return self-labels
  "REVIEWER: ChatGPT" despite the identity mandate (second occurrence of
  an identity/echo defect across rounds; CONV-026 had a duplicate-return
  incident). Content is substantive and distinct from the ChatGPT seat's
  return; counted as the Gemini seat.
- **Copilot seat:** FORMAT DEVIATION — §8 skeleton not used, REVIEWER
  field absent; all six questions answered; counted.
- DeepSeek's return includes its own reasoning preamble; preserved (in
  condensed, marked form) in the receiver.
- SCRIPT-EXECUTED runs: ChatGPT seat (both scripts, digits pasted,
  10/10 + 8/8) and Gemini seat (claims 10/10 + 8/8). Copilot's
  script-run condition is therefore satisfied by the panel itself.

## §2 — Tally (majority binding per question)

| Q | Verdicts | Outcome |
|---|---|---|
| Q1 (A chain) | SOUND ×4 (Grok, Gemini, Copilot, DeepSeek); DEFECT-NAMED ×1 (ChatGPT: A-5 uniqueness, flagged verdict-flipping) | **SOUND** — the flipper is NOT majority-sustained (1/5), so Q6b is not blocked |
| Q2 (√3/F-1) | NORMALISATION-AT-K-STANDING ×4; MISPREDICTION ×1 (ChatGPT) | **NORMALISATION-AT-K-STANDING** |
| Q3 (B math) | VERIFIED ×5 | **VERIFIED** (unanimous) |
| Q4 (diagnosis+corrigendum) | CORRECT-AND-SUFFICIENT ×5 | **CORRECT-AND-SUFFICIENT** (unanimous) |
| Q5 (discipline) | DISCIPLINED ×4; OVERCLAIMS ×1 (ChatGPT, two quoted passages) | **DISCIPLINED** |
| Q6a (corrigendum) | APPROVE-EITHER ×5 | **APPROVED (unanimous)** — enactment awaits the founder's ratification |
| Q6b (T-1) | ACCEPT ×3 (Grok, Gemini, DeepSeek); ACCEPT-CONDITIONAL ×1 (Copilot); BLOCK ×1 (ChatGPT) | **ACCEPTED (4–1)** — Copilot's conditions discharged at this patch (§4); ChatGPT's minority position preserved (§3) and substantively answered by the annex (§5) |

## §3 — Minority positions (preserved verbatim; binding rule honored)

**ChatGPT Q2/Q6b (the sharpest objection of the round):** "even
accepting the proposed recurrence, its homogeneous speed is
ℓ_P/(√3 t_P), whereas the package asks reviewers to compare against
c = ℓ_P/t_P. The PSR normalisation k multiplies Δ|SSV| and therefore
cannot alter R = ℓ_P when that departure vanishes. A separate,
independently grounded temporal/spatial normalisation could conceivably
repair this, but it is not supplied here." — CORRECT AS STATED, and the
adjudication treats it as such: the k convention indeed cannot absorb
the √3. The repair is the explicit registered mapping of §6 below,
which is exactly the "independently registered kinematic mapping" the
BLOCK vote named as its own discharge condition.

**ChatGPT Q5 quotes:** (i) "force the unique linear conservative
time-symmetric closure"; (ii) "forced, not tuned" (F-1). Both passages
are AMENDED in `T1_derivation.md` at this patch (§7): "unique" is
withdrawn in favor of the annex's forced-FORM + closure-robustness
statement; the F-1 passage now points to the registered mapping.

## §4 — Copilot's ACCEPT-CONDITIONAL: conditions and discharge

1. *Independent SCRIPT-EXECUTED runs* — DISCHARGED by the panel itself
   (ChatGPT seat, digits pasted; Gemini seat concurring).
2. *A-5 resolution: proof of impossibility OR bounded-error/robustness
   analysis* — DISCHARGED by the annex (§5): robustness over the full
   admissible class is PROVED; uniqueness is withdrawn as unnecessary.
3. *Ordering-of-limits appendix* — DISCHARGED (§5.4).

## §5 — THE A-5 CLOSURE ANNEX (machine-checked, 6/6)

The panel's shared objection (ChatGPT, Copilot, Grok, DeepSeek all
raised it): the two-level closure was claimed UNIQUE; the premises don't
prove uniqueness. The annex replaces the uniqueness claim with three
lemmas — each strictly stronger for the T-1 conclusion:

**L1 (the two-level FORM is forced).** For a linear one-register
recurrence u(t+τ) = 𝒜u(t) + ℬu(t−τ), invariance under running the same
law backwards forces ℬ = −1 (symbolic: the only solutions are ℬ = −1
with 𝒜 free, or the trivial swap 𝒜 = 0, ℬ = +1); the companion map then
has det = +1 (volume-preserving). The GP's single SSV register (AP-3)
grounds the one-register state space; time-reversal invariance is the
full-Moment symmetry (founder Q3) applied to the automaton. So the FORM
u(t+τ) + u(t−τ) = 𝒜u(t) is forced; only 𝒜's content was at issue.

**L2 (the admissible class).** One-hop locality (one Moment = one PSR;
AP-4c) restricts 𝒜 to the operators available to a GP in one Moment:
its own register (identity) and this Moment's arrivals (M_R). So
𝒜 = 2[α·M_R + (1−α)·I], α ∈ (0,1] — dispersion
cos(ωτ) = α·sinc(kR) + (1−α), UNITARY for the whole class (checked on a
dense k-grid). ChatGPT's counterexample family u_{n+1}+u_{n−1} =
2P(M_R)u_n with P(1)=1 is exactly this class at polynomial degree one;
higher polynomial degrees in M_R would require multi-hop reach within
one Moment, excluded by AP-4c.

**L3 (closure-robustness of the continuum operator).** For EVERY
admissible α, long-wave phase and group speed are
c_*(α) = √α·R/(√3·τ) — the continuum limit is the SAME variable-speed
wave operator; only the speed coefficient changes, and that coefficient
is degenerate with the c-identification (§6). **The T-1 continuum
equation is therefore closure-independent** — Grok's requested note,
now a theorem. The picture-preferred value is α = 1 (AP-3's per-Moment
refresh: the Compute stage rebuilds the register from arrivals; α < 1
would retain stale register content alongside arrivals), reproducing
the 3258 dispersion exactly (L4) — but nothing in T-1 depends on it.

**L4 (honest falsifier weakening).** The discrete-dispersion residue is
correspondingly the one-parameter FAMILY cos(ωτ) = α·sinc(kR) + (1−α),
not the single α = 1 curve. The family is non-vacuous (members are
numerically distinguishable at kR ~ 1; max separation 0.82 rad between
α = 0.25 and α = 1). Still UNMINTED as a prediction; registered as the
falsifier-shaped residue.

**§5.4 Ordering of limits (Copilot condition 3).** The continuum claim
is taken in the order: (1) N_V → ∞ (the Voronoi sampling of the shell
becomes the continuum shell mean; N_V cancels from all means before the
limit, so this is regularity, not tuning); (2) λ/R → ∞ (long-wave
expansion of the dispersion; corrections O((kR)²) from the sinc
expansion); (3) slow PSR variation: |∇R|·λ ≪ R (adiabatic condition;
the variable-radius mean-value property makes the STATIC sector exact
at every order in this expansion — the ordering only constrains the
dynamical sector). Violations of (3) arise only where PSR varies on
wavelength scale, i.e. strong-field/Planck-adjacent regimes — exactly
where DeepSeek's noted c_*(x) → ~0.29c near the exclusion radius lives.

## §6 — The registered kinematic mapping (implements the Q2 majority; discharges the ChatGPT minority's named condition)

**R-CSTAR-MAP (registered at this patch; founder ratification requested
alongside the corrigendum):** The observed vacuum light speed is
identified as c ≡ √α·R_vac/(√3·t_P) with the picture-preferred α = 1,
i.e. c = R_vac/(√3·t_P). The corpus shorthand "c = l_P/t_P" is hereby
read, at T-1 level and below, as this mapping — equivalently, the
vacuum hop radius is R_vac = √3·c·t_P (which constant absorbs the √3 is
a units convention: R_vac and t_P are not separately observable at long
wavelength; only their ratio through the dispersion is). Standing:
identical to k (GR-1 §7) — a registered normalisation with NO long-wave
observable content; the observable residue is the §5 L4 dispersion
family. This is precisely the "independently registered
temporal/spatial normalisation" the ChatGPT seat's BLOCK vote named as
what was missing.

## §7 — Actions executed at this patch

1. Returns registered verbatim (`reviews-CONV-027.md`).
2. This adjudication + annex registered; annex verify 6/6.
3. `T1_derivation.md` amended per the Q5 minority quotes: A-5's
   "unique" claim replaced by the L1–L3 statement; F-1 re-pointed to
   R-CSTAR-MAP. (Worker working-document; not a shipped paper; no HALT
   issue.)
4. DeepSeek's novel contribution registered as
   **NOTE-GR-CSTAR-STRONGFIELD** (GR.md): the position-dependent
   c_*(x) = PSR_eff(x)/(√3 t_P) → ~0.29·c near the exclusion radius —
   flagged for GR-1d/GR-1e (echo/remnant) cross-check as possible
   testable strong-field departure; unminted.
5. GR-1c corrigendum: **panel-approved 5–0 (APPROVE-EITHER)** — text
   ready (FTERM_reconciliation.md §6, Form A primary with the
   equivalence note, Form B displayed; Copilot's verdict-note honored:
   the corrigendum patch will attach the SCRIPT-EXECUTED artifact and
   the sympy-verification pointer). **NOT enacted at this patch:
   founder ratification is the final gate.**
6. T-1 status: **ACCEPTED-AS-CHARTER-T-1 (panel 4–1, conditions
   discharged)** — pending the founder's confirmation, at which point
   W-3 (Birkhoff) and W-4 (T-3 source tensor) run.

## §8 — What the founder decides next

(i) Ratify the GR-1c corrigendum (panel 5–0) → the corrigendum patch is
enacted next turn. (ii) Confirm T-1 acceptance (panel 4–1, conditions
discharged, minority answered) → W-3/W-4 run. (iii) Ratify R-CSTAR-MAP
(§6) — bundled with (i)/(ii); it is the formal repair the strongest
minority objection asked for.
