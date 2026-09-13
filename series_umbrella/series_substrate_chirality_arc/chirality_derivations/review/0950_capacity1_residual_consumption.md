# 0950 — Does V3 consume L4-A's residual? C1 and C2 survive it; C3 needs one quantitative re-check

**Lane:** chirality (09xx). **Patch:** 0950, 13 Sep 2026, Opus. **Layer:** 2/3 bookkeeping (re-running an existing theorem's conditions against a newly named residual). **Verify:** `chirality_derivations/code/0950_capacity1_residual_consumption.py` (7/7), reusing the 0694 NESS construction. **Answers:** the item 0949 filed and explicitly declined to claim.

**Question.** Patch 0949 discharged MA.1's form to its reversal-odd first harmonic and named what is *not* forced: the reversal-even midpoint term **A (m·n̂)**, and higher harmonics. Does THEO-CHIR-CAPACITY-1 — the V3 verdict — actually consume that residual, or only per-edge independence and O(δ¹) content?

**Answer.** **C1 is robust. C2 is robust where it makes its claim. C3 is the only condition that needs re-evaluating, and its margins are wide.** V3's Mechanism-A conditionality is therefore much closer to lifting than 0949 left it — but I am not lifting it, because C3's |K_lift| is computed from the measure and the measure moves.

---

## C1 — robust (this is the condition CAPACITY-1 names)

0925 §"Scope and conditionalities" states the dependence as *"conditional on Mechanism A and per-edge independence of its measure (proof part 1)."* Two findings:

- **Per-edge independence survives A ≠ 0.** The residual terms are *per-edge functions*: `A (m·n̂)` depends only on the undirected edge through its midpoint, and a quadratic `n̂ᵀT(v,ê)n̂` only on the directed edge (T1). Neither introduces coupling between **distinct** edges. So the factorization structure of the measure over edges is untouched; only per-edge parameter *values* change, the effective tilt becoming `B/(r₀ + A m·n̂)` — still a function of that edge alone (T2).
- **C1's spectral bound never references the rate law.** The 0828 refined-chord bound `ρ(M) ≤ κ(z*) < 1` is built from the *observable's* weights `c^v_e` under the pointwise participation floor `p(v) ≥ 4`. Rates enter only through the shared-edge-only step, which T1/T2 preserve. Re-verified here as at 0828: 0 violations over 120 adversarial non-homogeneous weightings, max ρ = 0.491 (T3).

Moreover the bound was *specifically repaired* at 0828 to hold with **no homogeneity and no vertex-transitivity** — "this holds for n̂-dependent (non-uniform) rules." A non-zero A produces exactly such a non-uniform rule. The residual lands inside the family 0828 was hardened against.

## C2 — the scaling changes, the claim does not

Tested rather than argued, by rebuilding the 0694 NESS with A switched on.

- **A = 0 reproduces 0694**: steady-current onset slope 3.00, the δ³ result.
- **Constant A promotes it by two orders**: slope 0.99, with `J ~ A² δ` (T4). This is a real effect and worth recording.
- **But C2 is stated "at the physical bias, not all-orders."** At δ = φ⁻³ the current is 1.7×10⁻⁵ to 3.4×10⁻⁵ across A ∈ [0, 1] — a spread of a factor of 2 around the A = 0 value of 2.9×10⁻⁵ — with O(J²) ≤ 1.1×10⁻⁹ throughout (T6). The scaling change is a small-δ phenomenon that **does not reach the physical bias**.
- **C2's symmetry argument is untouched.** The current stays divergence-free (max |div J| = 1.0×10⁻¹⁵) and T-odd, so T-odd current against T-even η-ordering still couples only at O(J²) (T5).

**A correction I have to record.** My first version of T4 tied A to δ, which makes `A²δ = δ³` and reproduced the A = 0 slope exactly — masking the effect completely and inviting the conclusion "the residual changes nothing." The test refused the claim I had written, and the claim was corrected rather than the test. Had I tied the parameters that way and moved on, this patch would have reported a false robustness for C2.

## C3 — the one that needs re-checking

C3 clears η off-critical with |K_lift| ≈ 0.053 against thresholds 0.095 (uniform) and 0.27 (staggered) — margins of roughly 44% and 80%. K_lift is computed **from the measure**, and the measure does move: at the physical bias, `max|π_A − π_0|` is **10.9%** of the A = 0 tilt itself (T7).

That is a modest shift against wide margins, and the likely outcome is that C3 clears comfortably. **But "likely" is not a re-check**, and recomputing K_lift is 0927's holder's job, not something to assert from outside it. This is the single item standing between V3 and an unconditional-on-Mechanism-A reading.

## Disposition

- **V3's Mechanism-A conditionality NARROWS again but does not lift.** The condition CAPACITY-1 actually names — per-edge independence — is **robust to the residual**, as is the spectral bound and C2 at the physical bias. What remains is one quantitative re-evaluation of C3's K_lift at a 10.9% measure shift.
- **W3 unaffected**, as at 0949: `sign(δ) = sign(B)` is O(δ¹).
- **Owed, filed:** recompute C3's K_lift with A ≠ 0 (0927's holder); if it clears, CAPACITY-1's Mechanism-A conditionality can be restated as "conditional on MA.1's reversal-odd first harmonic" — i.e. on derived content only — and V3 becomes unconditional on the residual. That restatement is a verdict-adjacent move and needs the panel CONV-001 requires; it is **not** done here.
- **Also worth a note to the NESS holders:** the `J ~ A²δ` promotion (T4) is a genuine sensitivity of the small-δ scaling to a term the framework assumes away. It does not affect results quoted at φ⁻³, but any future argument that leans on the δ³ *exponent* rather than on the magnitude at the physical bias should carry A = 0 explicitly.

**No verdict moves. No THEO registered. CAPACITY-1 untouched. Single pass, no panel.**
