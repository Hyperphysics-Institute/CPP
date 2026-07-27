# PR3-R EXTERNAL-FIELD SUSCEPTIBILITY — RE-PREREGISTRATION (FROZEN)

**Patch 2821. Frozen 2026-07-26 BEFORE any PR3-R measurement.
Authority: FOUNDER ("Please accept preregistration and re-run",
2026-07-26), lifting the worker's self-imposed bar on choosing a
successor route after seeing PR3's data. The defect being repaired is
D-PR3-1 (frozen 5% guard and frozen chain length jointly guaranteed
sub-unity signal-to-noise). PR3's frozen parent text is UNCHANGED and
governs; only the worker-stratum protocol is replaced.**

## §1 — Three repairs, adopted together

1. **SYMMETRIC AMPLITUDE LADDER + SLOPE FIT (replaces single-point
   ratios).** Drive at A ∈ {−2A₁, −A₁, +A₁, +2A₁}, A₁ = 0.66 (the
   2A₀ of the failed leg), and fit ⟨Re ρ_k⟩ = S·A through the origin
   by weighted least squares. The slope uses all four points, so its
   error is ≈ 2.1× smaller than any single-point estimate, and any
   constant offset (a known bias risk in the raw-mean estimator)
   cancels by antisymmetry.
2. **LINEARITY MEASURED, NOT ASSUMED (replaces the incompatible 5%
   guard).** The frozen guard is REPLACED by two explicit checks:
   (i) **odd-symmetry**: |⟨Re ρ⟩(+A) + ⟨Re ρ⟩(−A)| ≤ 2σ at each |A|;
   (ii) **slope stability**: the slope from |A| = A₁ alone agrees with
   the four-point slope within combined error. Failure of either ⇒
   NONLINEAR-REGIME, no verdict.
3. **SIMULTANEOUS MULTI-MODE DRIVING (efficiency, and a new
   control).** All three committed wave numbers (n² = 1, 2, 3) are
   driven in the SAME chain, H_ext = Σ_j A·Re[ρ_{−k_j}]; in linear
   response the modes do not cross-talk, so each ⟨Re ρ_{k_j}⟩ reports
   its own susceptibility. **CROSS-TALK CONTROL: shell n² = 4 is
   driven with ZERO amplitude in every run; its measured response must
   be consistent with zero.** A nonzero n² = 4 response invalidates
   the multi-mode assumption and voids the leg.

## §2 — Frozen protocol

Committed 2790 Ewald/Metropolis machinery verbatim; N = 432,
a_s = 0.02; eq 200 + production 1000 sweeps, sample every 2 (500
samples per leg; sized from a pre-freeze timing run, see §4); four legs at A ∈ {−1.32, −0.66, +0.66, +1.32};
unperturbed reference of record: ⟨|ρ_k|²⟩₀ per shell (n² = 1 value
112.5083 ± 9.6789 already committed at 2820; n² = 2, 3, 4 measured in
the same run family). Seeds 20260831–20260834. Errors: 24-block ×
2000-resample bootstrap on every leg mean; slope error propagated
from the weighted fit.

**Statistic (unchanged from PR3):** Λ(k) = S(k) / [−β N S_zz(k)/2].

## §3 — Frozen verdict classes (unchanged in substance from PR3)

- **PR3-PASS:** Λ(k) consistent with 1 within combined uncertainty at
  **≥ 2 of the 3** driven shells, AND both linearity checks pass, AND
  the cross-talk control is consistent with zero, AND no shell deviates
  from 1 by more than 3σ.
- **PR3-FAIL:** ≥ 2 shells deviate from 1 by more than 3σ, or a
  linearity check fails, or cross-talk is significant.
- **PR3-UNRESOLVED:** otherwise — **including combined slope error
  > 0.35 on Λ, which is hereby declared insufficient discrimination
  and must be reported as UNRESOLVED, never as a pass.** (This
  threshold is frozen NOW, before data, precisely because the failure
  of 2820 was an error bar admitting factor-of-two failures.)

**Power statement, computed at freeze:** with per-leg error ≈ 0.9–1.0
on ⟨Re ρ⟩ and the four-point ladder (Σ A² = 2(0.66² + 1.32²) = 4.36),
the expected slope error is ≈ 0.48 and Λ error ≈ 0.30 — inside the
0.35 bar but NOT comfortably. **If the achieved error exceeds 0.35 the
leg reports UNRESOLVED regardless of where Λ lands.** This is stated
plainly because the design is power-marginal by construction: the
compute budget, not the physics, sets it.

## §4 — Pre-freeze disclosure

Sizing this protocol required a timing run, which exposed one
result-adjacent number: a 400-sweep, 100-equilibration, 50-sample
fragment at A = +0.66 returned mean Re ρ(n²=1) = +3.198. That
fragment is unequilibrated and noise-dominated (the predicted
response at that amplitude is −1.06 with per-leg error ≈ 1), and it
is NOT part of the committed dataset — no committed leg uses seed
20260833 at those lengths. It is disclosed because it was observed
before this document was frozen, per the 2784 §0 precedent. The
committed legs below are blind.

---

## EXECUTION RECORD (Patch 2822) — **PR3-R VOIDED BY ITS OWN CONTROLS**

**Executed 2026-07-26 under the frozen protocol. Four legs
(A = −1.32, −0.66, +0.66, +1.32; seeds 20260831–34), acceptance 0.94
throughout, origin-constrained weighted slope fit.**

**Results:**

| shell | slope S | Λ | |Λ−1|/err |
|---|---|---|---|
| n²=1 (driven) | −3.417 ± 0.499 | **2.135 ± 0.312** | 3.64σ |
| n²=2 (driven) | −1.416 ± 0.585 | not computable (see D-PR3R-3) | — |
| n²=3 (driven) | −2.466 ± 0.713 | not computable (see D-PR3R-3) | — |
| **n²=4 CONTROL (undriven)** | **−1.452 ± 0.696** | must be 0 | **2.08σ from zero** |

**VERDICT: VOIDED — no PR3 verdict is drawn.** Three independent
grounds, all frozen in advance, all disclosed:

- **D-PR3R-1 — CROSS-TALK CONTROL FAILED.** The undriven n² = 4 shell
  responded at −1.452 ± 0.696 (2.08σ from zero), a magnitude
  comparable to the driven shells n² = 2 (−1.416) and n² = 3
  (−2.466). The frozen text: "A nonzero n² = 4 response invalidates
  the multi-mode assumption and voids the leg." **It does.** The
  control responding at driven-shell magnitude means the measured
  "responses" are not demonstrably mode-specific; a common systematic
  is present. **Most probable cause (diagnosis, not excuse): 200
  equilibration sweeps is insufficient, leaving a drifting initial
  transient common to all modes** — the frozen chain length was set
  by compute budget, as the prereg itself warned.
- **D-PR3R-2 — LINEARITY CHECK FAILED at one point** (n² = 2,
  |A| = 1.32: odd-symmetry residual 2.02σ against a ≤ 2σ bar). **And
  the prereg is internally inconsistent about the consequence:** §1
  says a linearity failure ⇒ "NONLINEAR-REGIME, no verdict"; §3 lists
  it under PR3-FAIL. **This is the third jointly-inconsistent freeze
  in this campaign** (after 2784 D1 and 2820 D-PR3-1) and is recorded
  as such. The protective reading is applied — no verdict — because a
  nonlinear regime means the linear-response identity under test does
  not apply, so failure of the identity cannot be concluded.
- **D-PR3R-3 — PROTOCOL GAP: the unperturbed S_zz references for
  n² = 2 and n² = 3 were never measured.** The prereg asserted they
  would be "measured in the same run family"; no such run was
  specified or executed. Λ is therefore computable for only ONE of
  three driven shells — which alone fails PR3's parent requirement of
  ≥ 3 wave numbers, independent of everything above.

**THE NUMBER I AM NOT CLAIMING.** The n² = 1 result, Λ = 2.135 ±
0.312, is 3.64σ from unity — read naively it is a *factor-of-two
violation of the fluctuation-response bridge*, which would be a major
finding directly relevant to PR3, PR6, PR7, and to every screening
result that assumes the bridge. **It is not claimed, not reported as
a finding, and must not be cited.** A shell whose companion control
is simultaneously showing a spurious response of comparable size
cannot support a claim of this magnitude; the most likely reading is
that both are the same under-equilibration artifact. Extracting the
exciting number from a run whose controls failed is precisely the
error the controls exist to prevent.

**Successor requirements (for a fresh prereg; NOT chosen here):**
equilibration long enough that the cross-talk control is consistent
with zero at ≤ 1σ **before** any driven measurement is read; explicit
unperturbed S_zz measurement for every driven shell; and a single
internally-consistent statement of the linearity-failure consequence.
PR3 remains **PARTIAL**; PR6's external-field leg remains **OPEN**.
