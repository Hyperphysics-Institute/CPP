# PRE-REGISTRATION — THE TURNOVER TEST: DIRECT DIFFERENTIAL LEGS AT β = 0.25 AND β = 0.30

**Patch 2923. Committed and presented BEFORE any leg runs. Purpose:
sign-level discrimination between the hybrid drive shape (turnover at
β ≈ 0.15, drag by β = 0.30) and the direct-trend extrapolation
(sustained forward drive), per Patch 2922 §§3–4.**

## §1 — METHOD (inherited from the sign round, unchanged)

Direct paired mobile/frozen differential legs, 2907-class engine and
procedure, mirror-symmetrised seeded Sea, gated kernel, T_eq = 40.
Δ = D_mob − D_fro per (class, seed, β).

## §2 — DESIGN LITERALS (feasibility multiplied out; 2916 discipline)

| β | T_meas | total Moments | transit | half-transit | edge buffer |
|---|---|---|---|---|---|
| 0.25 | 50 | 90 | 22.5 | ±11.25 | 3.75 |
| 0.30 | 33 | 73 | 21.9 | ±10.95 | 4.05 |

Both buffers meet or exceed the round-1 β = 0.2 precedent (4.7 is not
met at 0.25's 3.75; the smallest here, 3.75, exceeds the 2905 failure
margin and is accepted with disclosure). Windows are 2 (resp. 4)
round multiples of the grid period 2.5/β. Seeds {4, 5, 6} × classes
{A, B} per β = **12 legs total.** No other β. No hybrid machinery
anywhere in this test.

## §3 — FROZEN PREDICTIONS AND BANDS

Pooled per β across 6 legs, M = mean(Δ), SE = std/√6:

- **TURNOVER CONFIRMED:** M(0.30) < 0 with M/SE ≤ −2.0, OR
  {M(0.30) < M(0.25) < M(0.20)=2.75e-3·(carried) with both
  M/SE ≥ 2.0 declines individually resolved}.
- **TURNOVER REFUTED (sustained drive):** M(0.25) ≥ +2.0e-3 AND
  M(0.30) ≥ +2.0e-3, each with M/SE ≥ +2.0.
- **INCONCLUSIVE:** neither pattern at the stated significances.

The hybrid's point predictions, recorded for scoring but NOT bands:
D(0.25) ≈ +0.4e-3, D(0.30) ≈ −1.6e-3. The direct-trend prediction:
both ≥ +3e-3.

## §4 — GUARDS

Every leg checkpoints (2907 driver); any leg failing its own symmetry
gate is rerun at the next seed in {7, 8, 9} with disclosure, never
silently pooled. The frozen analysis refuses incomplete ensembles.
If the two β disagree in a pattern outside §3 (e.g. non-monotone),
the verdict is INCONCLUSIVE and the follow-up must add β = 0.22 and
0.27 before any claim.

## §5 — STANDING

Ledger untouched: 1B OPEN; PR7 PARTIAL; six of seven; B7 holds
DM-1/2/3; Candidate (B) 79.5%. G1, P-A2-1, statics suspension, 7 July
ruling stand.
