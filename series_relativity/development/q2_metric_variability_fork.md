# SR-1 reconciliation brick #3: the Q2 metric-variability fork (fixed-metric vs variable-metric/VSL)

*Patch 0737, Session 154. Third brick of the SR-1 rederivation pass. Builds on Brick #1
(`lp_psr_grid_reconciliation.md`, Patch 0734) and Brick #2 (Q1 grid resolution settled = nested
600-cell hierarchy, Patch 0736). This note POSES the Q2 fork cleanly and makes it testable; it does
NOT pick a branch. The choice — and the first-moment story that follows from it — is Brick #4.*

---

## 0. Why Q2 is the question that decides native inflation

Brick #1 §3 established the load-bearing fact: PSR_eff ≤ l_P holds under **either** Q1 reading, so the
maximum recession rate is c = l_P/t_P and expansion *at the ceiling* is **linear at c, not
exponential**. De Sitter inflation is super-luminal recession of comoving points (recession ∝
distance, unbounded), which requires **l_P itself to change** — a varying physical metric. So whether
CPP can inflate turns entirely on Q2, not on Q1 (which Brick #2 just closed). Patch 0731 closed only
*graph growth* (adding/stretching GPs); a variable physical metric on a *fixed* graph is a different
mechanism that 0731 did not touch. Inflation in CPP is therefore genuinely open via the
variable-metric route, and this note frames the decision.

## 1. A disambiguation the fork forces (must be carried into Brick #4)

`l_P` plays two roles in the corpus that the fixed/variable question pulls apart:

- **(a) Timelike advance per Moment** — c01: every CP advances the fixed amount per universal tick;
  the Absolute Moment postulate. This is a property of the *graph operation* (one tick = one
  broadcast/compute/displace cycle, PCD), stress-invariant.
- **(b) Spatial reach ceiling** — the baseline PSR, the maximum spatial displacement per Moment,
  c = l_P/t_P.

"Variable metric" must be stated as a claim about which of these varies. The cleanest reading (to be
made precise in Brick #4): the **graph operation** (one tick) is invariant — what varies is the
**physical distance one tick's reach represents**, set by the medium (DP-Sea μ, ε) on the fixed
graph. The Moment is still "one tick"; its physical scale is epoch-dependent. Under fixed-metric that
physical scale is a constant geometric length. This disambiguation is necessary because otherwise
"variable c" and "fixed Absolute Moment" appear to contradict (c01) — they do not, once (a) is graph
and (b) is medium-set.

---

## 2. Branch F — fixed-metric

**Definition.** `l_P` is a fixed geometric length set by the lattice; c = l_P/t_P is constant for all
epochs. k = l_P³/E_P with the standard Planck `l_P` (the value already used for the five predictions).

**First-moment / Big Bang.** With no DP Sea, ΔSSV = 0 ⇒ PSR_eff = l_P (the finite geometric ceiling
set by the bare 600-cell). **No infinity arises, and the H-axiom's `l_P_base` is unnecessary, not ad
hoc.** The "c = 1/√(με) → ∞ with no medium" intuition double-counts: it treats the bare lattice as
zero-impedance, but the lattice geometry itself sets a finite reach ceiling. This dissolves the
infinite-displacement problem at the first Moment without any new primitive.

**Inflation.** Expansion at the ceiling is linear at c; saturation-dilution caps e-folds far below
the required ~60 (the 0732 result, correctly read). De Sitter requires l_P to change, which Branch F
forbids. **⇒ No native inflation.** CPP would then need either an alternative early-universe story
(e.g. a bounce, or a non-inflationary resolution of horizon/flatness) or to accept that the
inflationary observables (near-scale-invariant spectrum, horizon, flatness) are inputs rather than
outputs.

**Cost.** Owes a non-inflationary account of the standard inflationary successes — or a principled
statement that CPP does not claim them.

## 3. Branch V — variable-metric (VSL)

**Definition.** `l_P` is the *physical* distance a one-Moment reach represents, set by the medium
(DP-Sea μ, ε) on the fixed graph; it can differ by epoch. c = l_P/t_P then varies with epoch.
Crucially, because l_P enters the Planck units, **the Planck-unit framework itself becomes
epoch-dependent**: k = l_P³/E_P and E_P = √(ℏc⁵/G) shift with c, so "k constant" holds only
per-epoch. (Present-epoch k is fixed; see §5.)

**Not closed by 0731.** 0731 closed graph growth. A variable physical metric on the *fixed,
eternal* GP graph (same GPs, different physical distance per step, medium-set) is a distinct
mechanism. So this branch is live.

**First-moment / Big Bang.** With no medium, l_P (the physical reach) is large/undefined ⇒ the
infinite-displacement problem **returns** and needs a regulator: either a derivable floor (a minimum
physical reach even at zero medium) or a new axiom (the H-axiom's `l_P_base` reinstated as the
regulator). Whether that floor is derivable from the bare-600-cell geometry or must be posited is the
open question Brick #4 must answer for this branch.

**Inflation.** A varying l_P admits super-luminal recession of comoving points ⇒ the de Sitter route
opens. Native inflation becomes possible. Two genuine sub-problems remain before it is established:
- **(i) Constant-H sustainability.** Does a variable metric admit a *sustained* constant-H phase
  long enough for ~60 e-folds? 0729's "no constant-H source" was computed at fixed c and **must be
  redone in a variable-c framework** before it can be read as a no-go here.
- **(ii) The spectrum.** Gaussianity + scale-invariance is separately owed under any choice.
  Candidate Gaussianity route: CLT over additive ZBW phases (distinct from the failed multiplicative
  qCP cascade, 0730). Scale-invariance needs the freezing/constant-H mechanism, i.e. (i).

**Cost.** Owes the regulator, the constant-H proof, the spectrum, and consistency with the
observational bounds on varying constants (§4).

---

## 4. The fork is TESTABLE (the empirical discriminant)

This is not a purely conceptual choice. The two branches make opposite empirical claims about whether
fundamental constants vary with epoch:

- **Branch F:** c (and the derived constants) are epoch-independent. Predicts **null** variation.
- **Branch V:** c is epoch-dependent. Predicts a (possibly tiny, late-time-suppressed) variation of
  c and of the constants that depend on it, which must (a) vanish to present-epoch precision and
  (b) remain within established bounds at all intermediate epochs.

The discriminating observational programs (standard, present-day bounds — CPP must be consistent with
them, not derive them): time-variation of the fine-structure constant α from quasar absorption
spectra and the Oklo natural reactor; laboratory atomic-clock frequency comparisons; BBN light-element
abundances; and CMB constraints on early-universe varying-c/varying-α models. **Branch V is viable
only if its predicted variation is below all of these; Branch F is falsified by any robust detection
of variation.** This gives the rederivation a genuine external check rather than an internal
preference.

---

## 5. Decision table

| Axis | Branch F (fixed) | Branch V (variable / VSL) |
|---|---|---|
| c = l_P/t_P | constant | epoch-dependent |
| Planck units / k | fixed all epochs | epoch-dependent; present-epoch k fixed |
| First-moment infinity | dissolved (finite ceiling) | returns → needs regulator (floor or H-axiom) |
| H-axiom `l_P_base` | unnecessary | the regulator (or a derived floor) |
| Native inflation | NO (linear at c) | route OPEN (needs constant-H + spectrum) |
| 0729 no-go | stands (fixed c) | must be redone at variable c |
| Present-epoch SR/SM tests | untouched | untouched (anchored at present l_P) |
| Empirical discriminant | predicts null Δc | predicts bounded Δc (varying-constants bounds) |
| New-primitive cost | none | regulator + constant-H proof + spectrum |

**The sharp fork (anti-correlation):** the same choice that dissolves the first-moment infinity
(fixed) also forecloses VSL inflation, and the same choice that opens inflation (variable) reinstates
the infinity. They cannot both be had. Brick #4 must pick and pay the corresponding cost.

## 6. What is invariant under either branch (present-epoch anchors — untouched)

- GPs fixed/eternal; the graph does not change (SR-1 line 1168).
- k = l_P³/E_P with the standard Planck l_P anchors the five SR predictions + the muon-storage-ring
  bound **at the present epoch** (present DP-Sea density). Any early-epoch VSL leaves them intact.
- PSR_eff ≤ l_P (ΔSSV ≥ 0): the speed-of-light ceiling at any given epoch.
- Brick #2's nested 600-cell hierarchy (Q1) holds in both branches (resolution is orthogonal to
  metric variability).

## 7. Resolution criteria (what Brick #4 must deliver for whichever branch is chosen)

- **If Branch F:** show explicitly that l_P is the finite geometric reach ceiling of the bare
  600-cell, dissolving the infinite-displacement story without the H axiom; and state plainly that
  CPP forgoes native inflation, with whatever alternative early-universe account Thomas wants.
- **If Branch V:** (1) specify the regulator/floor and whether it is derivable from bare-600-cell
  geometry or a new axiom; (2) redo the constant-H analysis (the 0729 no-go) in a variable-c
  framework to test sustained inflation; (3) advance the spectrum thread (CLT-over-ZBW Gaussianity +
  freezing for scale-invariance); (4) verify the predicted Δc is within the §4 bounds.

**Recommended sequencing (not a decision):** the empirical discriminant (§4) is the cheapest filter —
if a CPP-VSL law would predict Δc above current bounds, Branch V is dead and Branch F is forced
regardless of its inflation cost. So the first Brick-#4 sub-task under V is the magnitude estimate of
Δc. This is offered as sequencing only; Thomas picks the branch.

## 8. Pointers

- Builds on: `lp_psr_grid_reconciliation.md` (Brick #1, 0734); SR-1 §"Grid Resolution"
  (`sec:grid_resolution`, Brick #2, 0736).
- Supersedes nothing; sharpens the open question left by 0732/0733/0734.
- Related cosmology artifacts: `series_phenomena/cosmology/early_universe/`
  (`axiom_h_inflation_engine_evaluation.md`, `step1_scaling_phase_kill.md`,
  `lattice_growth_escape_closure.md`; reasoning 0729–0733).
- Next: Brick #4 — first-moment Big-Bang story under the chosen branch. See handover
  `handovers/2026-06-02_session_153_SR1_rederivation_scope.md` task list item 3.
