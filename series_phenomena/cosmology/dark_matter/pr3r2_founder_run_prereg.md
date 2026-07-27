# PR3-R2 — FOUNDER-EXECUTED RUN, PREREGISTRATION (FROZEN)

**Patch 2823. Frozen 2026-07-26 BEFORE any PR3-R2 measurement.
Execution venue: the FOUNDER's local machine (GPU-capable); the
worker writes, freezes, and analyses but does not execute. Repairs
D-PR3R-1/2/3 from Patch 2822. PR3's frozen parent text is UNCHANGED.**

## §0 — CLAUSE-CONSISTENCY PASS (new standing practice, per the 2822 failure mode)

Before freezing, every conditional in this document was checked
against every other. Result: **each failure condition appears exactly
once and maps to exactly one outcome.** The 2822 defect (linearity
failure mapped to both "no verdict" and "FAIL" in different sections)
cannot recur here because §3 is the ONLY section that assigns
outcomes, and §2 states conditions without assigning them.

## §1 — The three repairs

1. **EQUILIBRATION SIZED BY THE CONTROL, NOT BY THE CLOCK
   (repairs D-PR3R-1).** The undriven control shell must be
   consistent with zero BEFORE any driven measurement is read.
   Procedure: equilibrate; then run a control-only diagnostic block;
   if |⟨Re ρ_control⟩| > 1σ, discard and equilibrate again for the
   same length; repeat up to 5 times. **The production block does not
   begin until the control passes at ≤ 1σ.** The number of
   equilibration blocks used is REPORTED.
2. **UNPERTURBED REFERENCE FOR EVERY DRIVEN SHELL (repairs
   D-PR3R-3).** A dedicated A = 0 chain measures ⟨|ρ_k|²⟩₀ for
   n² = 1, 2, 3, 4 at the same length and error model as the driven
   legs. Λ is then computable for all three driven shells, satisfying
   PR3's ≥ 3 wave-number parent requirement.
3. **SINGLE OUTCOME TABLE (repairs D-PR3R-2).** See §3; conditions
   are stated in §2 and assigned outcomes ONLY in §3.

## §2 — Protocol (conditions only; no outcomes assigned here)

Machinery: committed 2790 Ewald/Metropolis lineage, N = 432,
a_s = 0.02, identical constants. Driven shells n² = 1, 2, 3
simultaneously; n² = 4 undriven as control. Amplitude ladder
A ∈ {−1.32, −0.66, +0.66, +1.32} plus one A = 0 reference chain (5
chains total). **Equilibration ≥ 2000 sweeps per chain, extended by
the §1.1 control gate; production 6000 sweeps, sample every 2 (3000
samples/chain)** — ~10× the 2822 statistics, which the founder's
hardware makes affordable. Seeds 20260841–20260845. Errors: 24-block
× 2000-resample bootstrap. Statistic unchanged:
**Λ(k) = S(k) / [−β N S_zz(k)/2]**, S from the origin-constrained
weighted slope fit over the four driven amplitudes.

Conditions evaluated (no outcome attached in this section):
- **C-CTRL:** |slope(n²=4)| / σ ≤ 2.
- **C-LIN:** for every driven shell and both |A|,
  |y(+A) + y(−A)| ≤ 2σ.
- **C-POWER:** combined Λ error ≤ 0.35 at each driven shell.
- **C-AGREE:** |Λ − 1| ≤ 2σ at a given shell.
- **C-DEVIATE:** |Λ − 1| > 3σ at a given shell.

## §3 — OUTCOME TABLE (the ONLY section assigning outcomes; evaluated top to bottom, first match wins)

| # | If | Then |
|---|---|---|
| 1 | C-CTRL fails | **VOID — cross-talk**; no PR3 verdict |
| 2 | C-LIN fails at any driven shell | **VOID — nonlinear regime**; no PR3 verdict (the linear-response identity under test does not apply, so its failure cannot be concluded) |
| 3 | C-POWER fails at ≥ 2 driven shells | **PR3-UNRESOLVED** |
| 4 | C-DEVIATE holds at ≥ 2 driven shells | **PR3-FAIL** (bridge violated) |
| 5 | C-AGREE holds at ≥ 2 driven shells and C-DEVIATE holds nowhere | **PR3-PASS** |
| 6 | otherwise | **PR3-UNRESOLVED** |

Directional/anisotropy values are REPORTED per shell (R8-relevant,
report-only, no outcome weight).

**Freeze declaration:** every amplitude, length, seed, condition, and
outcome above was fixed before any PR3-R2 number existed. The worker
will not execute this run and will analyse only what the founder
returns. A discovered defect voids the affected leg and requires a
fresh prereg, same-font.

---

## AMENDMENT (Patch 2825) — the §1.1 control GATE is withdrawn as defective; C-CTRL is unchanged and moves to analysis

**Founder's partial run of 2026-07-27 (v1 script, cancelled at chain 4)
exposed a defect in the gate, NOT in the protocol.** Observed control
block means: chain A=−0.66 → {−2.249, −0.942, +6.327, −1.314, +1.014};
chain A=+0.66 → {+4.298, +4.317, +1.676, −3.815, −1.740}, each quoting
an internal error of ±0.5–1.0. **A quantity whose 200-sweep block means
span ±6 while reporting ±0.7 errors is a SLOW MODE**: its
autocorrelation time greatly exceeds the probe length, so the naive
std/√n error understates the true uncertainty by ≈ 4× (implied τ ≈ 16
sweeps). The gate therefore did not test equilibration — it passed
whenever the wandering control happened to drift near zero, and chain 4
never passed in five blocks purely by luck of phase.

**This also retroactively reinterprets D-PR3R-1** (Patch 2822): the
2.08σ "cross-talk" was most probably the same slow fluctuation
evaluated with a naive error, not mode contamination. That leg's VOID
stands as recorded; its *diagnosis* is corrected here.

**Amendment (worker-stratum only; the frozen §3 outcome table and every
condition in §2 are UNCHANGED):** the §1.1 iterative control gate is
WITHDRAWN. Equilibration is a fixed 2000 sweeps per chain. **C-CTRL is
evaluated exactly as frozen — on the production data, with the same
24-block × 2000-resample bootstrap used for every other quantity**,
which is autocorrelation-aware by construction. No condition, bar, or
outcome changes; only the point of evaluation moves from a defective
pre-production probe to the committed estimator.

**Power restatement with the measured τ:** at τ ≈ 16 and 6000
production sweeps, effective samples ≈ 375, per-leg error ≈ 0.39,
four-point slope error ≈ 0.19, **Λ error ≈ 0.12** — comfortably inside
the frozen 0.35 bar. The protocol was adequate all along.
