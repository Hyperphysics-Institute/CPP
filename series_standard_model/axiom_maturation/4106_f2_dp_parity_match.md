# F2 Reduced — EM Parity Under χ₄ Turns on a DP Internal Parity Match

**Patch:** 4106. **Lane:** EW. **Supersedes** the sea-isotropy framing of TODO-4101-F2.
**Verify:** `series_standard_model/code/4106_f2_dp_parity_match.py`.
**Status:** F2 reduced to one sharp binary founder question. **Not a soft conditional — on the
wrong answer χ₄ is refuted outright.**

---

## 1. The reduction

Three corpus results combine, none of them new here:

- **A DP is "a bound pair of opposite-polarity CPs"** (master_glossary).
- **The response to b must be LINEAR** (B3, Patch 4076 — answering the founder's own question).
- **The linear coefficient must be C-ODD, i.e. polarity** — the polarity clause, *forced* by
  CPT at F6 (Patch 4085): b is P-odd, C-even, T-even, hence CPT-odd.
- **v in b = sign(ω·v) is the DP arc cohort direction** (founder ruling, Patch 4097).

So one sea DP's net χ₄ response is

> R = (+q)·b₊ + (−q)·b₋ = q·(b₊ − b₋)

**R = 0 ⟺ F2 holds.** R ≠ 0 means every DP in the vacuum carries a P-odd electromagnetic
response.

**Sea isotropy is irrelevant.** The cancellation is per-DP and pointwise. How the sea's
directions are distributed never enters. That is what supersedes the 4101 framing.

## 2. The decision table

Two structural facts are free, and neither is fixed anywhere in the corpus (unscoped search):
**(S)** are the pair's ZBW spins parallel or antiparallel; **(V)** is the arc cohort direction
common to both (drift) or opposed (internal orbital motion)?

| spins | arc direction | mean \|R\|/q | max \|R\|/q | verdict |
|---|---|---|---|---|
| parallel | common / drift | 0.0000 | 0.0 | **F2 HOLDS** — exact |
| parallel | internal / orbital | 2.0000 | 2.0 | **χ₄ REFUTED** |
| antiparallel | common / drift | 2.0000 | 2.0 | **χ₄ REFUTED** |
| antiparallel | internal / orbital | 0.0000 | 0.0 | **F2 HOLDS** — exact |

The pattern is not "are DP spins paired?" It is a **parity match**:

> **F2 holds ⟺ (spin relative orientation) matches (arc relative orientation).**

When both flip, sign(ω·v) is even in the simultaneous negation and b₊ = b₋. When exactly one
flips, b₊ = −b₋ and the polarity clause *doubles* the response instead of cancelling it.

Cancellation in the surviving cases is exact and pointwise — 50,000 random (ω, v) give
max |R| = 0 identically, not a statistical average.

## 3. Why this is not a soft conditional

Atomic parity violation is observed and is accounted for by Z-exchange admixture to ~0.3%
agreement with the SM. Intrinsic EM parity violation must therefore sit far below the weak
contribution, itself ~10⁻⁷ of the EM amplitude — a bound of order **10⁻¹⁰**.

A mismatched DP sea gives **R/q = 2 per DP**. Order unity. **Overshoot ≈ 2×10¹⁰.**

There is no suppression mechanism available: the polarity clause is *forced* by CPT (F6), and
linearity is *required* (B3). Neither can be softened to rescue a mismatch without giving up a
result χ₄ already depends on. **On a mismatch, χ₄ is refuted by electromagnetic parity
conservation.**

## 4. The founder question (PD-006(a)) — TODO-4106-F2DP

For a ground-state sea DP:

1. Are the two CPs' ZBW spin vectors **parallel or antiparallel**?
2. Is the DP's arc cohort direction **common to both CPs** (the pair drifts together) or
   **opposed** (each CP's arcs follow its own internal orbital motion about the pair centre)?

F2 holds iff the two answers agree in parity. The natural first guess in each is opposite —
a vacuum "atom" in its ground state suggests *antiparallel* spins (spin-paired, like a filled
shell), while arcs laid down during acceleration suggest a *common* drift direction. **That
pairing is one of the two fatal cells.** So the naive reading of both refutes χ₄, and the
axiom needs the corpus to say otherwise on at least one of them.

## 5. Scope

- This is F2 only. F3 (R-F3, TODO-4101-F3) is untouched and separately with the founder.
- No verdict moved. χ₄ is not refuted here — it is made refutable by a determinate question.
- If the founder's answer is a mismatch, χ₄ fails and the maturation arc closes. If it matches,
  F2 upgrades from CONDITIONAL to DERIVED, with sea isotropy never needed.
