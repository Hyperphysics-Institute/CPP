# 0965 — Piece 1 assembled: the dynamical η is pointwise non-degenerate. Two links proved, one evidenced — and the evidenced one is named.

**Patch:** 0965, 13 Sep 2026. **Lane:** chirality (09xx). **Type:** proposed result, assembled for panel. **Verify:** `chirality_derivations/code/0965_piece1_assembly.py` (6/6). **Status: DRAFT — not registered, not enacted, no verdict moved.** CAPACITY-1's conditionality on piece 1 stands until a panel closes it.

---

## The claim

> **`p(v) = 1/Σ_e (c^v_e)⁴ ≥ 4` at every vertex, for the dynamical η.**

If it holds, CAPACITY-1's piece-1 conditionality discharges and **V3 becomes unconditional on anything but the axioms** — the last standing assumption under the spatial chirality verdict.

## The chain, with its weakest link named first

Three links. **Two are proved. One is not.** Stating that up front because the panel's attention belongs on the third, and because the natural way to write this document would bury it.

| link | content | status |
|---|---|---|
| **(a1)** | The det-coset ℤ₂ order parameter **is** a sign structure: the canonical local enantiomorph is the orientation of the whole vertex figure, read as `sign det[d̂, n̂, r̂₁, r̂₂]` on each incident edge. All three corpus constructions (0819, 0820, 0821) build it this way. **Weights are unit magnitude by construction.** | **definitional** |
| **(a2)** | **The substrate's dynamics does not deform those weights.** | **EVIDENCED, NOT PROVED — the load-bearing link** |
| **(b)** | For unit-magnitude weights, participation = support, exactly. | **proved** (arithmetic, T1) |
| **(c)** | A handedness observable in 4-D must resolve an orientation — the sign of a 4×4 determinant — needing ≥ 4 independent directions. So support ≥ 4. | **proved** (dimensional, T2; `lcapa_axis2_signcorr_closure.md` §5) |

**(a1) + (a2) + (b) + (c) ⇒ p(v) ≥ 4.**

## On (a2) — what is actually established

The corpus statement is 0820 §(3): *"The Mechanism-A bias shifts edge MEANS… but leaves the reading WEIGHTS uniform ⇒ m_eff stays 12 for small delta… **So the bias polarises but does NOT concentrate the reading.**"*

**A tempting non-argument, rejected.** One could write a weight function taking no `δ` argument, observe that it does not depend on `δ`, and call that a test. It is not: it records what the construction is, not what the substrate does. T3 is labelled a *structural observation* precisely so it cannot be read as evidence.

**The real test (T4)** reproduces 0820's Monte Carlo from scratch: if the bias concentrated the reading, the connected nearest-neighbour correlator `C_nn` — which depends on the effective participation — would move with `δ`. Measured: `C_nn = −0.0545` at `δ = 0` and `−0.0542` at `δ = 0.10`, a difference of `0.0003`. **It does not move.**

**That is evidence, not proof.** It shows the bias does not concentrate the reading *at the tested δ, for this observable, to this statistical precision*. It does not derive weight-uniformity from the axioms. **Piece 1, if closed this way, replaces a quantitative assumption (`p ≥ 4`) with a structural one (the dynamical η is the undeformed det-coset sign-reading).** That is a real improvement — the structural claim is what the corpus already builds, it is definitional to "det-coset," and it is checkable — but it is a replacement, not an elimination, and the panel should be told so in those words.

## The assembled result (T5)

Over 150 random frames × 120 vertices, the **minimum `p(v)` is 11.00** against a floor of 4 — seven to spare in the worst case. The R-1 hostile pass at 0964 pushed harder: adversarial frames aligned to lattice directions give a minimum of 7, still clearing.

## Reconciliation of 0820 §(2) — stated up front, not buried

**0820 §(2) says: *"A 4-edge det reads only 4 (⇒ emergent)."*** Read cold, our own corpus appears to contradict our own floor.

It does not. That verdict came from **0819's mean-field `K_lift` crossover at `m_read ≈ 8`**, a mode scan that **0828 replaced** with a refined-chord bound proved over the whole class. Under the live bound: `p ≥ 4 ⇒ c_max ≤ (1/4)^{1/4} = 0.7071 ⇒ z* ≤ 0.5 ⇒ ρ(M) ≤ κ(0.5) = 2/3 < 1`. Both numbers are computed in T6. **The live bound clears `p = 4`; the superseded estimate did not; CAPACITY-1 rests on the live one.**

This is raised here because a panel will read 0820 — it is where the uniform-weight claim lives — and meet §(2) two paragraphs later. The R-1 pass at 0964 identified it as the most likely falsifier vote if left unaddressed.

## What a panel should press on

Named so the dispatch does not have to discover them:

1. **(a2) is evidence, not proof.** Is "the dynamical η is the undeformed det-coset sign-reading" acceptable as a *structural* conditionality replacing the quantitative one — the same class of judgment as CONV-048's Q5 on per-edge independence?
2. **Is (c)'s definitional move legitimate?** It excludes sub-4-support observables by declaring them not handedness observables. Sound, or does it assume the conclusion?
3. **`δ = 0.10` is not the physical bias.** T4 tests at 0.10; the physical value is `φ⁻³ ≈ 0.236`. The test should be repeated there before dispatch — **noted as owed, not done here.**

## Disposition

- **DRAFT.** No claim registered, no verdict moved, CAPACITY-1 untouched, piece 1 still formally open.
- **Owed before dispatch:** T4 repeated at `δ = φ⁻³`; then a panel under R-2 as a fresh campaign with its effort bound written at dispatch.
- **If the panel sustains:** piece 1 discharges, CAPACITY-1 loses its last named conditionality, and V3 rests on the axioms plus the derived Mechanism-A first harmonic alone.
