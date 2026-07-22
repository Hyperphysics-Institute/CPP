# S4-X X5-FE RECORD (DRIVE-AUDIT-1, first act) — executed under the frozen 2746 prereg: **FORK F3 — all three ensembles agree at N = 64** (campaign driven path −1.412 ± 0.124; independent brute-force sampler −1.292 ± 0.136; exact Gibbs tilt −1.247 ± 0.092; pairwise 0.3–1.1σ) — **the campaign's driven code path is exonerated at this size by an implementation sharing no machinery with it**, and the B2 anomaly is therefore SCALE-DEPENDENT: the driven/tilt enhancement ratio is 1.70 at N = 432 (with the un-tilt check confirming that chain was NOT sampling Gibbs: un-tilted it predicts undriven ⟨A⟩ = −1.72 instead of 0, ESS_w = 632) versus 1.13 ± 0.12 at N = 64 — the frozen escalation stands, the N-scan is specified to locate the onset, and one discipline event is disclosed same-font: the independent sampler's k-space prefactor initially carried a spurious 0.5 relative to path A's convention, caught by inspection BEFORE any comparative result was read, fixed, and B restarted clean

**Patch 2747, 21 July 2026. Runs archived (data/x5fe/). Power caveat
recorded honestly: at N = 64 the frozen bands fired F3, but the size
of a hypothetical intermediate enhancement (≤ ~1.2×) is inside the
error bars — the fork verdict stands AS COMMITTED and the N-scan
makes the localization dispositive. Reasoning: `reasoning/2747.md`.
79.5% not in scope.**

## §1 — The three ensembles (N = 64, ε = 2.4, one mode)

A-UND: ⟨A⟩ = −0.099 ± 0.082, Var = 16.68, linear prediction −1.139;
exact tilt prediction **−1.247 ± 0.092** (the true Gibbs response at
this box: 1.09× linear — mild genuine nonlinearity, consistent with
the small box's larger relative fluctuations). A-DRV (campaign path):
**−1.412 ± 0.124** — 1.07σ from tilt. B-DRV (independent, total
energies rebuilt from nothing every move, no incremental S, no
shared state): **−1.292 ± 0.136** — 0.27σ from tilt, 0.65σ from
A-DRV. **F3 as frozen.**

## §2 — What F3 establishes

1. The campaign's driven code path — the exact lines that produced
   the N = 432/686 anomaly — is CORRECT at N = 64, certified by a
   from-scratch implementation and by the Gibbs tilt simultaneously.
   No line-level defect of the "wrong formula" kind exists.
2. The anomaly is a function of SCALE: driven/tilt = **1.70 at
   N = 432** (three chains) vs **1.13 ± 0.12 at N = 64**. The
   un-tilt symmetry check nails the large-N pathology independently:
   reweighting the X3-LONG driven chain back to ε = 0 predicts an
   undriven mean of −1.715 where the true value is 0 — that chain's
   stationary distribution was NOT exp(−β(H + εA)), full stop.
3. Remaining candidate mechanisms, all size-dependent, none enacted:
   (a) an N-dependent numerical pathology in the incremental path
   that N = 64 is too small to trigger (e.g., float accumulation in
   dEk across the larger k-vector sums interacting with the drive's
   symmetry breaking — disfavored by the 1e-12 drift audits but
   those audited S, not dEk round-off statistics); (b) a genuine
   finite-size-onset ergodicity failure of local-move Metropolis
   under a symmetry-breaking field (the driven mode's free-energy
   landscape at larger N developing structure the sampler
   equilibrates into incorrectly — this would be a REAL and
   publishable sampler phenomenon, not a bug); (c) an as-yet-unnamed
   mechanism. **The N-scan discriminates (a) vs (b) partially; the
   AUTOMATON — whose dynamics owe nothing to Metropolis — is the
   arbiter-of-record either way, per the standing elevation.**

## §3 — Next instruments (specs for the successor)

**N-SCAN:** A-path pairs (driven + undriven→tilt) at N ∈ {128, 216,
320}, same protocol, ~16k sweeps each (cheap on path A) —
the enhancement-ratio-vs-N curve locates the onset and its shape
(sharp threshold → (b)-like; smooth drift → (a)-like). **B-CHECK at
onset:** one B-sampler run at the smallest N showing enhancement
(cost permitting) — if B reproduces the enhancement there, the
"bug" reading dies entirely and (b) becomes the finding.
**AUTOMATON-1 execution prereg:** now the standing arbiter; may
charter in parallel on the founder-confirmed specification.

## §4 — Ledger

Discipline: the B-sampler prefactor correction (caught pre-result,
disclosed); the F3 power caveat (recorded, not hidden). Standing
physics untouched as throughout: the septuply-consistent spectrum,
the X6 shape finding, monotonic character, all caps and fences,
**79.5% untouched**. The anomaly remains confined to the driven-MEAN
instrument at N ≥ ~432 — which no standing claim consumes.
