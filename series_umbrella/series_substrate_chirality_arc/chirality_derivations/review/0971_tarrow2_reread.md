# 0971 — TARROW-2 re-read against 0960: the conclusion survives and is strengthened; the order-counting does not. The PH's prediction is half right.

**Patch:** 0971, 13 Sep 2026. **Verify:** `code/0971_tarrow2_reread.py` (6/6). **No verdict moved, no claim registered** — this is the re-read filed at 0970, not an enactment.

**The prediction under test.** 1d-β's problem history: discharging Mechanism A *"would unconditionalize BOTH CAPACITY-1 (spatial) and TARROW-2 (temporal)."* TARROW-2's own header: *"once OPEN-FP-F1-2 discharges Mechanism A the W-move becomes unconditional."* Patch 0960 narrowed Mechanism A to its **derived** reversal-odd first harmonic, leaving `A` (the reversal-even midpoint term) and higher harmonics as named residuals. Nobody had checked what TARROW-2 does with that.

---

## 1. TARROW-2's argument, reproduced

It is a Kolmogorov cycle computation on the 1200 triangular faces of the 600-cell. Reproduced exactly at `A = 0`:

- **1200 faces**, and the per-face identity `a + b + c = 0` holds to 2×10⁻¹⁶ (T1).
- **Exactly 420 of 1200** faces carry nonzero `abc`, with `|abc| ∈ {1/8, 1/4}` (T2) — TARROW-2's headline numbers, independently obtained.
- **Order counting: slope 3.00** (T3), confirming claims (i) and (ii): the O(δ¹) sum vanishes per face, and the first violation is O(δ³).

## 2. The residual breaks the order-counting

With a constant reversal-even `A`, **the per-face O(δ¹) cancellation fails.** The reason is visible in the rate law: the cycle log-ratio per edge becomes

`log[(1 + A m_e + B c_e)/(1 + A m_e − B c_e)] ≈ 2 B c_e /(1 + A m_e)`,

so the effective tilt is **position-dependent** and the face sum is no longer proportional to `a + b + c = 0`. Measured: **slope drops from 3.00 to 0.99** at `A = 0.3` (T4).

**TARROW-2's claim (i) — "no O(δ²) term, first possible violation at O(δ³)" — therefore consumes `A = 0`.** That is exactly what Patch 0949 predicted for the NESS-based results, and TARROW-2 was named in that list. The prediction was right.

## 3. But the conclusion is robust — and strengthened

**The same 420 faces carry nonzero cycle affinity at every `A` tested** (0, ±0.3, 1.0) — T5. The residual changes the **order** at which detailed balance fails, not **whether** it fails. And it fails *earlier*: at O(δ¹) rather than O(δ³).

So TARROW-2's actual conclusion — **detailed balance is violated, the process is non-reversible, `C_T = Yes`, and the W3 → W1 upgrade is a live candidate** — survives the residual untouched, and the residual can only help it. At the physical bias the maximum cycle affinity is 6.9×10⁻³ at `A = 0` and 5.8×10⁻³ at `A = 0.3`: large in both cases, so none of this is a small-δ artefact (T6).

## 4. Verdict on the PH's prediction: half right, and the half that matters is right

| | prediction | finding |
|---|---|---|
| TARROW-2's **conclusion** (`C_T = Yes`, W3 → W1 candidate) | unconditionalized | **YES** — robust to the residual, and strengthened by it |
| TARROW-2's **order-counting** (claim (i), the δ³ statement) | unconditionalized | **NO** — consumes `A = 0`, as 0949 predicted |

**This is structurally identical to CONV-048's C2 finding**, and the parallel is worth naming: there too the conclusion survived at the physical bias while the asymptotic characterisation (`O(δ³)`) did not, and there too the fix was to restate the claim as a magnitude statement rather than an order statement. **The same repair applies here.**

## 5. What is owed, and what is not

**Owed — a wording correction to TARROW-2, not a re-derivation:** claim (i) should be scoped to the reversal-odd first harmonic, or restated as *"detailed balance is violated on 420 of 1200 faces, at O(δ³) when the rate law is the pure reversal-odd first harmonic and at lower order otherwise."* The 420-face result and `C_T = Yes` stand unchanged.

**Not owed — a panel.** This moves no verdict. TARROW-2's registered content is confirmed; one of its supporting claims gains a scope clause. **Under R-2 that is a wording correction to be bundled with the arc's other paste-ready corrigenda, not a fresh campaign.**

**Also not owed — an unconditionality claim.** W3 → W1 remains a *candidate* upgrade, exactly as TARROW-2 has it. This re-read removes the Mechanism-A conditionality from its conclusion; it does not perform the upgrade, and nothing here should be read as doing so.

## 6. Disposition

- **Re-read complete.** The 0970 item is closed.
- **Conclusion:** TARROW-2's verdict content is now conditional on the *derived* first harmonic only — the same status CAPACITY-1 reached at 0960. **Today's result does extend from the spatial verdict to the temporal one, which is what the PH predicted and what made this the recommended target.**
- **Owed:** the claim-(i) scope clause, filed with the corrigenda queue.
- **No verdict moved. No claim registered. No count change.**
