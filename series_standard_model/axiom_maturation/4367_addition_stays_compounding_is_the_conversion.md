# The Addition Stays Addition; the Compounding Lives in the One Conversion the Corpus Never Specified, and a Grid Point Can Do It with One Multiplication per Unit of Stress

**Patch:** 4367. **Lane:** foundations, with GR. **Session:** 242.
**Founder:** `founders_voice/4367_same_amount_per_dibit_how_to_compute_compounding.md`.
**Verify:** `series_standard_model/code/4367_compounding_by_one_multiply_per_unit.py` (sympy).

## 1. Correction to how 4366 put the question

4366 §3 asked whether stress raises SSV_abs by the same amount or by the same percentage, as though "same amount"
must fail. That framing was mine and it was too narrow. The founder's answer, *every DI-bit carries the same amount, and
the addition is unaffected by SSV_abs*, is fully compatible with the working rule. Two separate steps were run
together:

1. **The addition.** The GP sums its arrivals into its stress census. Each DI-bit adds the same amount. This is GR-1j's
   census linearity, it is what makes the statics exactly Laplace, and **it does not change**.
2. **The conversion.** The GP turns that sum into a PSR (equivalently, a GP count for its Planck sphere). The corpus has
   never specified this step (founder 4365), and the curve's *shape* is the whole question:
   - **inverse proportion** (count ∝ 1/sum) fails: Mercury's second order comes out 2, and α drifts;
   - **compounding** (each unit of the sum removes the same *fraction* of the count) works: Mercury's ½, and the
     background scales out.

So "compound interest" is not a change to the addition. It is the shape of the conversion curve. 4365's form (B) is
exactly this: n = n_∞·e^{−3kΔ} with Δ the plain sum. 4366's "compounding SSV_abs" was the same physics written with the
compounding moved into the register; with the founder's additive picture, the 4365 bookkeeping is the one to keep.

## 2. How a GP could compute it (the founder's question)

| method | what the GP does each Moment | cost |
|---|---|---|
| step by step | start from the deep-space count and, for each unit of arrived stress, keep the fraction (1 − f) | one multiplication per arriving unit |
| table | read the count from one table T[Δ] shared by every GP | one lookup |
| formula | n = n_∞·e^{−3kΔ} | one exponential |

All three give the same number. **For an integer census the step-by-step rule is an exact exponential:**
(1 − f)^Δ = e^{−3kΔ} with 3k = −ln(1 − f). The script checks this symbolically, and numerically to machine precision at
Δ = 1…1000. So the compounding needs no logarithm and no table. It is a fixed small fraction removed per unit of stress,
the same at every GP. The rejected inverse proportion would be one division by the sum; it is equally simple and simply
the wrong curve. **Simplicity does not choose between the two shapes; Mercury and the clocks do.**

Which of the three the substrate "uses" is not observable: they agree exactly. The step-by-step form is the one that
reads most naturally as a per-arrival act, which suits an automaton whose Perceive phase already handles arrivals one at
a time.

## 3. The DI-bit and the LSP

The founder asks whether a DI-bit should compute its message (the LSP) from SSV_abs. In the registered automaton the
**GPs compute and the DI-bits only carry** (GR-1j inputs; payload {origin address, E, S}). The 4364 source rule needs
no extra computation by anyone. The GP holding a CP already computes its Planck-sphere count n to set its own PSR, and
the rule is that the CP's part of that GP's LSP is stamped with a strength proportional to that same n. **One number,
computed once per Moment by the origin GP, sets its PSR and the strength of its resident CP's message.** The DI-bit
carries it unchanged. (Wording note: in the founder's question "the CP would execute" reads as "the GP would execute";
the CPs move, the GPs compute.)

## 4. What "works across all phenomena" covers today

Checked:
- Mercury's ½ (now a consequence of the curve's shape, given the 4364 source rule);
- local G and α the same in every background (lunar-ranging and clock tests of that kind);
- EIH's static cross term;
- single-body classical tests unchanged.

Not yet checked, on file:
- the strong field: no horizon, a shadow 4.6% larger than GR's, and the conflict with GR-1c's exact-Schwarzschild claim
  (TODO-4365-THIRDORDER);
- the relay kernel across PSR gradients (TODO-4364-KERNEL);
- self-gravitating bodies against lunar ranging (TODO-4364-SELFGRAV);
- moving sources and preferred-frame bounds (TODO-4364-PREFFRAME).

"All phenomena" is not established. The rule is the only one found so far that passes the tests it has met.

## 5. PD-008

- **Not claimed:** that the founder has ratified the compounding curve. His answer settles the addition (same amount
  per DI-bit) and leaves the curve's shape conditional on it working across phenomena. Recorded as open (TODO-4365-THIRDORDER).
- **Corrected:** 4366 §3's framing, as above. 4366's algebra stands.
