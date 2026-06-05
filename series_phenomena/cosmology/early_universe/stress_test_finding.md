# Stress test + calibration (ChatGPT review of 0756/0757): partial, honest result

*Patch 0758, Session 154. Acts on ChatGPT's review of the 0756/0757 results: (1) a **language
calibration** (don't overclaim) and (2) a **stress test** — scan charge-balanced interactions *beyond*
the quadratic on-site toy (finite-range, screened-Coulomb-like) in 3D and fit the excess chemical
potential. Also records Grok's endorsement + independent convergence and Copilot's endorsement. Script:
`series_phenomena/cosmology/early_universe/scripts/0758_stress_test.py`. NO THEO.*

## 1. Language calibration (adopted)

ChatGPT is right that 0756 slightly overclaimed. The calibrated statements, adopted going forward:

- **Not:** "charge neutrality protects the log."
- **Instead:** "charge neutrality cancels the **leading mean-field** contamination (the ∝ n̄ term) in
  this quadratic toy interaction." Whether a sub-leading residual (√n̄ or other) survives is a separate
  question — addressed analytically in 0757 and probed (partially) here.
- The bath clause's requirement is sharpened to: a **fast neutral Gibbs bath with excess chemical-potential
  growth negligible against ln n̄ at the cosmological pivot** — not merely "thermalizes."

## 2. Stress test: scan balanced interactions beyond quadratic (3D)

Setup: 3D periodic lattice (L=8), balanced ± CPs, screened-Coulomb pair energy g·exp(−r/ξ)/r within a
cutoff, plus an unbalanced on-site control. Widom μ_excess measured over λ ∈ {4,8,16,32}; reported as raw
values + a robust single power p (|μ_excess| ∼ n^p). The 4-term A·n̄+B·√n̄+C·ln n̄+D fit is **ill-conditioned**
over this λ range (n̄, √n̄, ln n̄ near-collinear), so individual coefficients are not trustworthy — hence
the raw-values + single-power reporting.

| config | μ_excess(λ=4,8,16,32) | max\|μ\| | p | reading |
|---|---|---|---|---|
| UNBALANCED on-site control (K₀=0.1) | 0.19, 0.38, 0.78, 1.56 | 1.56 | 1.02 | ∝ n̄ — **positive control passes** |
| balanced short screened (ξ=0.7) | −0.005, −0.004, −0.013, −0.023 | 0.023 | — | **SMALL — clean** |
| balanced medium screened (ξ=1.5) | −0.011, −0.023, −0.062, −1.52 | 1.52 | 2.28 | blows up — toy breakdown |
| balanced long screened (ξ=4) | −0.029, −0.07, −1.35, −6.04 | 6.04 | 2.74 | blows up — toy breakdown |

## 3. Honest reading

- **Positive control works:** the unbalanced on-site interaction yields μ_excess ∝ n̄ (p ≈ 1.0). The probe
  correctly detects mean-field contamination (matches 0756 config B). So a null result elsewhere is
  meaningful, not a blind spot.
- **Balanced short-range/on-site is clean:** μ_excess stays tiny (max ≈ 0.02). Consistent with 0756
  (balanced quadratic) and 0757 (on-GP point-stack is on-site). This is the regime relevant to the CPs
  co-located on a single GP.
- **Balanced long-range is UNRESOLVED:** the medium/long-screened cases blow up super-linearly (p > 2) at
  high λ. This is the small-L toy **breaking down** — λ = 16–32 on 512 sites is an absurd density,
  strongly coupled and under-equilibrated at ~6 sweeps — **not** a clean √n̄ or linear law. The toy cannot
  resolve the long-range functional form; it just fails there.

## 4. Net status (honest, calibrated)

The stress test (a) validates the μ_excess probe, (b) **confirms** the balanced short-range/on-site case
is clean (the on-GP point-stack of 0757), but (c) does **not** clear the long-range inter-GP case — it
breaks down rather than resolving presence/absence of √n̄. So:

- **On-GP point-stack:** clean (0757 analytic [no sub-GP spatial substrate] + 0756/0758 numeric
  [balanced short-range μ_excess ≈ 0]). This is the load-bearing case for the stack chemical potential.
- **Long-range inter-GP residual:** genuinely **OPEN**. Neither 0757 (argued via the Debye crossover) nor
  this toy (breaks down) settles it. It needs a **proper large-L, well-equilibrated, dilute-regime MC**
  with long-range handling (Ewald/RPA) and ChatGPT's full A·n̄+B·√n̄+C·ln n̄+D fit over many λ — with the
  pass condition that any residual stays subdominant to ln n̄ ≈ 170 at n̄ ~ 10⁷⁴.

We do **not** claim the residual is absent in general. We claim it is absent on-site/short-range (the
point-stack) and **unresolved** for long-range inter-GP — the calibrated, non-overclaiming statement
ChatGPT asked for.

## 5. Panel status

- **Grok:** endorsed 0756 (clean, decisive, correctly interpreted); accepted the swarm request and reports
  an independent MC converging on the identical pass/fail; ready to run with the real SSV form.
- **Copilot:** endorsed the macro-CP mechanism as the bath justification (0756) and 0757 as the Debye
  "kill shot."
- **ChatGPT:** CONFIRMED-WITH-CALIBRATION; the calibration (§1) and stress test (§2) are now actioned, and
  the honest outcome is that the long-range case is explicitly open (not closed by the toy).

## Caveats

- Small L=8, cutoff rcut=2, ~6 sweeps, 4 λ points: adequate for the positive control and the short-range
  clean result, **inadequate** for the long-range form (the blowup is a toy artifact, not evidence of real
  cosmological contamination).
- The proper long-range test (Ewald/RPA, large L, dilute) is the recommended next independent task; added
  to the swarm request.

## Pointers

- Script: `.../scripts/0758_stress_test.py`. Builds on 0756 (neutrality), 0757 (Debye analytic).
- Swarm request updated with the long-range/Ewald stress-test task.
- Reasoning: `.../reasoning/0758_stress_test.md`.
