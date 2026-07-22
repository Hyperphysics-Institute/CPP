# S4-X X1 RECORD — the error-closure analysis, executed under the frozen prereg: **the simulation's errors were SOUND** (τ_int = 0.38–0.54 samples at the 5-sweep spacing; ESS 334–615; the IACT-underestimation conjecture is REFUTED for these chains), the corrected MAIN error TIGHTENS to ±0.091, and the a_s = 0.04 tension therefore SHARPENS to **4.1σ** — the frozen classification rule fires: **CLOSURE-ERROR CANDIDATE or UNRESOLVED**; chains consistent; monotonicity preserved everywhere; a_s = 0.02 agrees (0.6σ); PR1's bar (unexplained ≤ 2σ) is NOT met at this stage — and one recorded paradox names the next discriminator: contact coupling is STRONGER at a_s = 0.02 than at 0.04, inverting the naive closure-error ordering and pointing at extraction-window mismatch (→ X6 matched-window dual extraction, with X3 replication)

**Patch 2733, 21 July 2026. Executed under the prereg frozen in the
script header before any result (`code/2733_s4x_x1_error_closure.py`);
the five chains' raw per-sample profiles are ARCHIVED in-repo at
`data/s4e_chains/` (gzipped JSON) for seat re-analysis. Reasoning:
`reasoning/2733.md`. 79.5% not in scope.**

## §1 — Results

| Chain | a_s | τ_int (samples) | ESS | κ_corr/κ_D | alternations |
|---|---|---|---|---|---|
| MAIN-A | 0.04 | 0.54 | 443 | 1.1192 ± 0.023 | 0 |
| MAIN-B | 0.04 | 0.39 | 615 | 1.1073 ± 0.024 | 0 |
| SIZE-S | 0.04 | 0.41 | 393 | 1.1568 ± 0.039 | 0 |
| SIZE-L | 0.04 | 0.38 | 420 | 1.1236 ± 0.027 | 0 |
| CORE | 0.02 | 0.48 | 334 | 1.0292 ± 0.042 | 0 |

MAIN combined (corrected): **1.1132 ± 0.0166**; |A−B| well inside
2×combined (chains CONSISTENT). Tension vs HNC 1.0206 ± 0.015:
**D = 4.14σ** (Gemini's 1.5σ target NOT met). a_s = 0.02:
D = 0.57σ (agrees). Monotonic character PRESERVED under corrected
errors in every chain.

## §2 — What X1 settles

1. **The statistical explanation is DEAD.** With samples every 5
   sweeps, τ_int < 1 sample throughout — the 2714 ten-block SEMs were
   correct; there is no hidden autocorrelation inflation; the tension
   is not a sampling artifact of the recorded chains. (The 2714-era
   concession of GPT's item 4 stands as a discipline matter — the
   check HAD to be run — but its numerical consequence here is nil.)
2. **The frozen classification: CLOSURE-ERROR CANDIDATE or
   UNRESOLVED** — with an honest asterisk recorded same-font: simple
   HNC-closure error should WORSEN as contact coupling grows, and the
   contact ordering is βv(0) = 2.05 at a_s = 0.02 vs 1.02 at 0.04 —
   yet 0.02 agrees and 0.04 does not. The naive closure story is
   inverted. **Named candidate mechanism:** the two instruments
   extracted κ on DIFFERENT windows (simulation: (2a_s, 3/κ_D); HNC:
   [0.40, 1.00] fm) over a profile carrying the O(Γ) shape deviation
   — a window-sensitive apparent discrepancy is possible without
   either instrument being "wrong." This is exactly PR5/X6 territory.
3. **PR1 status: NOT MET** (unexplained discrepancy 4.1σ > 2σ).
   Promotion remains barred; the path runs through **X6 (matched-
   window + pole dual extraction — now the sharpest discriminator),
   X3 (one longer a_s = 0.04 chain, prereg length from ESS ≈ 450:
   ~4× sampling for a ±0.008 target), and X4 (the ladder).**

## §3 — Ledger

Adverse-capable outcome delivered as committed: the convenient
resolution (blame the error bars) is refuted by the programme's own
frozen estimator; the tension is real, sharpened, and better-located.
Data archived; every number re-derivable by seats from the committed
artifacts.
