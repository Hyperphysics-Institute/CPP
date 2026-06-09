# Path A closure spec — discharging DG-3 Q1 by eigenmode completeness + a worst-case-observable bound

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/0916_pathA_capacity1_closure_spec.md`
**Patch:** 0916 · **Type:** verdict-side closure specification (chirality lane). Hands the F.1 window the single lemma (**L-CAP-A**) that converts C1 from a *sampled* mode-scan into an *exhaustive* bound, discharging the convergent DG-3 Q1 falsifier (0914/0915). **No verdict moved**; CAPACITY-1 reserved; conditional on Mechanism A. Re-fire happens only after L-CAP-A returns.

---

## The Q1 gap (what must be closed)

C1 presented a **scan** of candidate η-observables (`m∈{4,6,8,12}` × 3 frames), all sub-critical (`|K_lift|/K_c ∈ [0.50, 0.64]`). ChatGPT + Copilot (2/3) RESTATEd on the same point: a scan is a **sample**, not a proof that **every** admissible local η is sub-critical; a more-local / untested η could in principle condense. (Grok's CONFIRM asserted "no admissible η survives" but did not establish exhaustiveness — Path A is the proof of exactly that assertion.)

The closure must be exhaustive on **two axes**: (1) which **mode** orders, for a fixed η-observable; (2) which **η-observable** is the dynamical one (the "more-local η" concern).

## The closure

**Setup.** η lives on the 120 vertices of the 600-cell. Review-closed **CHI-1 locality** (+ the 0821 nn-only correlator: d=1 −0.053, d=2 ≈+0.0004, d≥3 ≈0) confines the effective η-coupling operator `M_eff` to the nearest neighborhood; icosahedral symmetry of the vertex figure (I_h fixes the host; the 12 NN are equivalent) makes the NN coupling uniform. `M_eff` is real-symmetric.

**Axis 1 — eigenmode completeness (which mode).** A real-symmetric `M_eff` has a **complete** orthonormal eigenbasis of the 120-dim η-space: *any* η-configuration is a combination of its eigenmodes. Mean-field ordering of eigenmode `v` (eigenvalue `a_v`) occurs at `|K_lift|·|a_v| = 1`; the **largest** `|a_v|` gives the **smallest** threshold and binds first. Hence the single inequality

> **`|K_lift| · a_max(M_eff) < 1`**   (where `a_max` = spectral radius, in ordering-normalized units `= |K_lift|/K_c`)

clears **every** eigenmode at once, for either coupling sign (the worst case is the largest-`|a|` mode). This is exhaustive over Axis 1 — it replaces the per-mode scan with one spectral-radius bound. Numerically `|K_lift|·a_max = 0.053·(1/K_c)` ; with `K_c^uniform = 1/12` (mean-field) this is `0.64 < 1` (the package's 0.64), and the true `K_c` (0823) only raises the threshold → margin widens to ≈44%.

**Axis 2 — worst-case observable (the "more-local η" concern).** Different η-observables (different support `m`) give different `M_eff(m)`, hence different `a_max(M_eff(m))`. But the spectral radius is bounded by the **max row sum** (Gershgorin/Perron): with the per-neighbour coupling entries bounded (Cauchy–Schwarz on normalized η: `|M_ij| ≤ 1`), `a_max ≤ (number of engaged neighbours)`. The **full 12-neighbour vertex figure (`m=12`) engages the most neighbours at full weight → it maximizes the row sum → it is the worst-case observable.** Any **more-local** observable (`m<12`) engages fewer / partially-weighted neighbours → strictly **smaller** `a_max` → **more** sub-critical. (This is exactly why 0821 found `m=4 → 0.50 < m=12 → 0.64`, and it overturns 0819's abstract-model "more-local → emergent" once and for all: more-local lowers the spectral radius, it does not raise it.)

**Together:** the `m=12` vertex figure is the worst case over all admissible CHI-1-confined observables, and its spectral radius gives `|K_lift|·a_max = 0.64 < 1`. Therefore **no admissible η-observable, in any mode, condenses** — exhaustive on both axes. Q1's "sample" becomes a complete-eigenbasis + worst-case-observable bound. The ≈44% conservative margin **is** that bound.

## L-CAP-A — the lemma the F.1 window must establish (the one load-bearing computation)

> **L-CAP-A.** For the full effective η-coupling operator `M_eff` of the `m=12` vertex-figure observable (the complete 120×120 correlator matrix from 0821, **all shells included**):
> (i) its **spectral radius** `a_max(M_eff)` (largest `|eigenvalue|`, in ordering-normalized units) satisfies **`|K_lift|·a_max(M_eff) < 1`** — i.e. the package's 0.64 is the *complete-spectrum* largest eigenvalue, not a single-mode estimate; and
> (ii) `m=12` is the **worst-case** admissible observable: `a_max(M_eff(m')) ≤ a_max(M_eff(12))` for every more-local / alternative CHI-1-confined η-observable `m'` (Gershgorin row-sum + monotonicity in engaged-neighbour weight; confirm numerically across the `m∈{4,6,8}` operators already built in 0821, and state the row-sum argument for the general bound).

**Computation (F.1 window, reuses 0821/0824 machinery):** assemble `M_eff` from the measured correlator (the 0821 object), diagonalize the full operator, report `a_max(M_eff)` and `|K_lift|·a_max`; confirm `< 1`. Check the 2nd-shell (dodecahedral ×20) contribution does not lift the row sum enough to matter (0821: d=2 ≈ +0.0004, ~100× below NN → expected negligible, but **compute, don't assume** — this is the one place the bound could in principle fail).

**Falsifier for L-CAP-A:** `a_max(M_eff) ≥ 1/|K_lift| ≈ 18.9` in ordering-normalized units (equivalently the full-spectrum largest eigenvalue ≥ 1), or a more-local observable with a larger spectral radius than `m=12`. Either would mean a mode can condense and Path A fails → fall back to Path B (narrow the claim to the local-η regime).

## On confirmation → reframe C1, fix Q2/Q3/Q4, re-fire

If L-CAP-A holds, the chirality lane rebuilds the DG-3 package:
- **C1 reframed** from "sampled scan, not a proof" to the **L-CAP-A exhaustive bound** (complete eigenbasis + worst-case `m=12` observable; `|K_lift|·a_max < 1`). This answers Q1 directly.
- **Q3 fix:** add 0824 + 0825 to the source links; annotate 0823's superseded "staggered not V1."
- **Q4 fix:** chain reworded to "**every eigenmode** off-critical (`|K_lift|·a_max<1`) ⇒ no det-coset breaking ⇒ μ²>0 ⇒ V3 confirmed / V1 excluded."
- **Q2:** carry "at the physical bias δ=φ⁻³" as an explicit scope limit.
…then re-fire to the swarm. Pass remains **3/3 CONFIRM**.

## Residual honesty (carried into the re-fire)

- L-CAP-A is a **mean-field spectral-radius** bound; true `K_c ≥` mean-field (0823) only helps (the 0823 MC already shows disorder at `K_lift`). Beyond-mean-field would only widen the margin.
- The closure is conditional on **CHI-1 locality** (review-closed) confining `M_eff`. A genuinely **non-local** η outside CHI-1 is excluded *by CHI-1* + the 0821 nn-only correlator; if a reviewer disputes CHI-1's completeness, that reopens CHI-1, not this closure.
- Conditional on **Mechanism A** (OPEN-FP-F1-2), as throughout.

## Scope held

Verdict-side closure spec; hands L-CAP-A to the F.1 window. **No verdict moved, no THEO, no ID, no CHIR.md edit, no re-fire** (awaits L-CAP-A). V3/W3 stand; CAPACITY-1 reserved; OPEN-CHIR-1d-β OPEN; conditional on Mechanism A.
