# SR-1 reconciliation brick #4: Branch-V construction adopted; the primordial spectrum is the gate

*Patch 0738, Session 154. Fourth brick of the SR-1 rederivation pass. Records the cosmology-sector
decision out of the Q2 fork (Brick #3, `q2_metric_variability_fork.md`, 0737), specifies the
construction, and reports the toy-model result that gates it. The toy
(`series_phenomena/cosmology/early_universe/scripts/0738_brick4_spectrum_gate.py`) PASSES at the
capability/coherence level; this is NOT yet a parameter-free prediction. NO THEO (program decision +
numerical evidence, conditional).*

---

## 1. The decision

**Branch V is adopted**, in the specific form Thomas specified (Session 153/154 dialogue):

- **Fixed UNIT, variable REACH.** `l_P_base` is a true constant (global, time- and space-independent
  geometric scale). What varies is `PSR_base`, a value *computed at each GP* from (a) its H-boost
  history and (b) the local absolute SSV; the actual per-Moment displacement is `l_P_eff` = PSR_eff,
  with `l_P_eff = l_P_base` only in the unboosted, baseline-SSV case. So `c_eff = l_P_eff/t_P` is
  state- and epoch-dependent.

- **Labelling correction (important, and consistent with Thomas's own framing).** Fixing the *unit*
  `l_P_base` does NOT make this Branch F. Branch F's free dissolution of the first-Moment infinity
  required the *operative reach ceiling* to be the fixed finite length. Once the H-engine can boost
  PSR_base, the operative reach (and `c_eff`) is state-dependent — that is Branch V cosmologically.
  What the fixed unit genuinely buys is **clean present-epoch anchoring**: when the boost is off and
  SSV is baseline, `l_P_eff = l_P_base` = standard Planck length, so `k = l_P_base³/E_P` and the five
  SR predictions + muon bound are exactly preserved (Brick #2 invariants hold). The fixed unit is
  worth keeping for that reason; it is not an escape from Branch V's costs.

## 2. Division of labour (each ingredient does ONE job; they are non-substitutable)

| Job | Ingredient | Note |
|---|---|---|
| First-Moment regulator + seed texture | **Finite initial patch** (~13 GPs: a GP + 12 neighbours) | Removes the infinite-PSR pathology WITHOUT an axiom (every GP sees a mix of occupied/empty neighbours ⇒ finite, textured SSV from Moment 1). Surface/volume imbalance seeds anisotropy. Spreading is ballistic (≤ c_eff), NOT exponential — so the patch is regulator+seed, not the engine. |
| Expansion ENGINE | **H-axiom** (always-on, local) | When a GP hosts superposed CPs for > 1 t_P, PSR_base ×(1+H) per tick; factor = 1 (no boost) in any tick with no superposition (graceful, self-terminating exit). Persists for all time as an anti-collapse regulator (limits CP *stacking* per GP; candidate footing for degeneracy pressure). |
| Primordial STATISTICS | **CLT over ZBW phases** | Additive sum of ~10³⁰ independent ZBW kicks ⇒ Gaussian (Test A). Replaces the multiplicative qCP cascade (0730), which is heavy-tailed. |
| Web/halo MORPHOLOGY | **qCP-qCP chaining + qDP aggregation** | Seeds filaments/voids; DM backbone; adiabatic baryon/lepton response. (Already strong, CPP-native — DM arc.) |
| HORIZON problem | **early high c_eff** (VSL) | Global causal contact directly; does not require e-folds. |
| SPECTRUM (scale-invariance) | **interlock**: stationary CLT injection + constant-H freezing | The gate. See §4. |

**Reframing of "is inflation needed?":** for the *horizon* problem, no — early high `c_eff` does it.
For the *spectrum*, yes — a constant-H stretching phase is needed, not to connect the universe
causally but to FREEZE fluctuations into scale-invariance. Inflation in CPP is repurposed as the
**spectrum generator**; the H-axiom is its engine.

## 3. Axiom ledger (what is POSITED, not derived)

1. `l_P_base` — constant baseline reach unit (fixes present-epoch anchoring).
2. `H` — constant fractional PSR_base boost per superposed tick (the engine; constant by axiom, NOT
   tied to late-time Friedmann H — avoid double-counting).
3. `α_SSV` — coupling in PSR_eff = PSR_base/(1 + α_SSV·ΔSSV) (modulates SSV→reach).
4. **Finite-patch initial condition** — ~13 GPs at t≈0 (an IC, not an axiom; removes the infinity).

This is one rule + ~3 constants + an IC, against a full inflaton potential V(φ). Parameter count is
not the objection. (The H-axiom's status changes here from *evaluated-not-adopted* (0732) to
*adopted as the working early-universe engine, gate passed at toy level* — see
`axiom_h_inflation_engine_evaluation.md`.)

## 4. The gate: toy-model result (Patch 0738)

Run `0738_brick4_spectrum_gate.py`. Three tests, all PASS:

- **A — CLT Gaussianity.** Additive ZBW sum → excess kurtosis **−0.012** at N=512 (Gaussian);
  multiplicative qCP cascade → excess kurtosis **~1.6×10⁵** (heavy-tailed). Additive decisively
  beats multiplicative — confirms the CLT choice over the 0730 cascade.

- **B — spectrum interlock (the make-or-break).** Stationary injection under constant H → **n_s =
  1.000** (flat / scale-invariant), with small skewness (~0.036). The analytic relation
  **n_s − 1 = d ln σ²/dN** is confirmed (impose β=−0.035 → predicted 0.965, measured 0.965). A modest
  roll-off of the injected variance (superposition thinning near the end) lands **n_s ≈ 0.965** in
  the Planck band with small non-Gaussianity. The interlock works: CLT supplies a *stationary
  Gaussian* source, constant-H freezing converts temporal stationarity into spatial
  scale-invariance, and the slow end-of-inflation roll-off tilts it slightly red (correct direction).

- **C — e-fold budget.** The H-engine self-terminates at ~1 CP/GP, so the TOTAL e-folds is set by the
  initial stacking depth, not by H: N_efold ≈ (1/3)·ln(N_CP/N_GP). The observable-universe CP count
  (~10⁸⁰) gives **N_efold ≈ 60** — the right ballpark, from the right CP count, with no tuning of H.
  H sets the *rate*; depth sets the *total*. (Suggestive, order-of-magnitude — not a precision claim.)

**What PASS means and does NOT mean.** It means the construction is internally coherent and *capable*
of the targets — there is no contradiction in the F-vs-V knot once the pieces are assigned as in §2.
It does NOT mean CPP predicts n_s = 0.965 from first principles: the tilt roll-off is a free function
and the amplitude A_s is one tuning (exactly as standard inflation tunes its potential). The honest
status is **"viable, gate cleared at toy level; first-principles content still owed."**

## 5. Debts ledger (kept visible)

- **First-principles roll-off.** The red tilt currently comes from a *posited* end-of-inflation
  decline in injected variance. Deriving that decline from the superposition-thinning law (how the
  superposed fraction falls as dilution proceeds) is the next real piece — it would turn n_s from a
  tuning into a prediction. HIGH priority.
- **Amplitude A_s ≈ 2×10⁻⁹.** Set by σ_ZBW (the ZBW kick scale). One tuning; deriving it from the
  ZBW frequency/scale is owed.
- **Δc bound (cheap filter).** Density-dependent c_eff predicts present-day spatial Δc between
  galactic and intergalactic space (different qDP density). Must be ≲ varying-constants bounds
  (quasar-α ~10⁻⁵–10⁻⁶, Oklo, atomic clocks, BBN, CMB). Cheap to estimate once α_SSV is scaled;
  could be a feature or a falsifier. Run before investing further.
- **Flatness.** Not addressed by horizon-via-high-c_eff; needs its own mechanism (does not come free).
- **Reheating / energy accounting.** Exponential reach-growth is work; where it comes from and how it
  dumps into the hot Big Bang is owed (later debt).
- **Degeneracy pressure — HIGH RISK, not a free bonus.** Fermi degeneracy pressure is precisely
  measured (Chandrasekhar 1.4 M_⊙; WD/NS mass–radius). If H-anti-collapse *replaces* it, it must
  reproduce those numbers; if it *adds*, beware double-counting / over-pressure. **And distinguish it
  cleanly from Patch 0731:** "H limits CP *stacking* on a single GP" must not be conflated with
  "occupancy fraction f → 1 across GPs" (0731's near-100% black-hole-interior picture) — two
  different quantities, or the stories collide.

## 6. Recommended next move

Two parallel, both cheap:
1. **The Δc filter** (§5) — could kill the density-dependent-c_eff picture outright; run it first.
2. **The superposition-thinning roll-off law** — the one piece that upgrades n_s from tuning to
   prediction; the highest-value first-principles target.

If both survive, the construction graduates from "toy gate cleared" toward a defensible early-universe
sector, at which point the SR-1 rederivation can fold the semantics in and dispatch to the review
panel.

## 7. Pointers

- Decision out of: `q2_metric_variability_fork.md` (Brick #3, 0737). Builds on Bricks #1–#2 (0734,
  0736).
- Toy + verify: `series_phenomena/cosmology/early_universe/scripts/0738_brick4_spectrum_gate.py`.
- H-axiom status: `series_phenomena/cosmology/early_universe/axiom_h_inflation_engine_evaluation.md`
  (evaluated-not-adopted → adopted-as-working-engine, gate passed at toy level).
- Reasoning: `series_relativity/development/reasoning/0738_brick4_branch_v_gate.md`.
- Handover task item 3 (first-moment story) is addressed here; items 4 (spectrum thread) and the
  Δc filter are the live continuations.
