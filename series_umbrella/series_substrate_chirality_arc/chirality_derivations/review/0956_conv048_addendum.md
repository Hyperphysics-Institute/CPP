# Addendum to the review package — two tests run after the package was written

**Read this after Part 2 of the main package and before answering the questions.** It is short.

Three reviewers have already returned on the original package. Two of them raised the same gap; a third raised a different one. Both gaps were real and both were computable, so we ran them rather than filing them. **One result changed the proposal.** This addendum reports both, and it is the reason the proposal in Part 2 now reads differently from the version those three reviewers saw.

---

## A1. The negative half of the A-range — tested, and it is not a mirror

**What was raised.** The package stated that a rate law must stay positive on every edge, giving an admissible range `|A| ≤ 1.025`, and then reported tests over `A ∈ [0, 1]` only. Two reviewers noted that the negative half had never been run. One added that symmetry would suggest it behaves similarly.

**What we found.** It does not behave similarly. Across `A ∈ [−1, 1]` the steady current at the physical bias varies by a factor of **94**, and peaks at **1.0 × 10⁻⁴ at A = −1.00** — about **3.5× its value at A = 0**. The reason is visible in the rate law: near the negative edge of the admissible domain, `1 + A(m̂·n̂)` approaches zero on some edges, those edges become slow, and the relative circulation grows.

**Does it change the conclusion?** No. The quantity that enters the argument is the current's square, and its maximum over the whole domain is `1.0 × 10⁻⁸` — far below the threshold. The other condition, C3, is untouched: K_lift stays at or below 0.0526 over negative A, against thresholds of 0.083 and 0.27.

**But the reasoning offered for skipping the test was wrong**, and we would have inherited a false statement had we accepted it. We record that as the reviewers' result, not ours.

## A2. Second-order terms — and a reversal-odd channel nobody had identified

**What was raised.** The package conceded that second-order terms are permitted by symmetry and never bounded them. A reviewer asked for a justification for truncating at first order.

**What we found — this is the part that matters.** At second order the symmetry-permitted forms are:

| form | behaviour under reversing an edge |
|---|---|
| `(ê·n̂)²` | **even** |
| `(m̂·n̂)²` | **even** |
| `(ê·n̂)(m̂·n̂)` | **ODD** |

**This breaks the argument the first-order case relied on.** At first order, the unforced term `A(m̂·n̂)` was safe *precisely because it is reversal-even*: it cancels identically in the antisymmetric current and cannot shift a reversal-odd mean. That protection is a parity accident of first order. **At second order there is an odd channel, and it shifts the tilt directly.**

Tested at the coefficient scale the framework would naturally give a second harmonic (φ⁻³):

- **C1 (the locality and spectral argument): untouched.** A second-order term is still a function of a single directed edge, so it changes per-edge values without coupling different edges — which is all C1's locality step needs, for either parity.
- **C2 (the steady current): a real effect.** The odd quadratic **raises the current 3.3×** over its absence — a larger effect than the even first-order term ever produced. It still clears: the squared current stays at `9.3 × 10⁻⁹`.
- **C3 (the alignment margin): clears.** K_lift 0.0528 against a baseline of 0.0526.

**The honest limit.** We pushed the odd coefficient to 1, 3 and 10. K_lift went to 0.0513, 0.0405, 0.0111 — it never crosses the threshold and in fact *decreases*. So we have no evidence of danger. But we also have no *argument* covering large coefficients, and unlike the first-order case we cannot appeal to parity to get one. **We are treating this as a named open residual, not as closed.**

**This is why the proposal changed.** It previously said the theorem is not conditional on the rate law terminating at first order — full stop. That claimed more than we can support. It now says so only at the framework's own scale, and flags the odd channel as unbounded in general.

---

## What we are asking you to do with this

- **Answer Q1, Q2 and Q5 as usual** — none of the above bears on them.
- **Q3 (our handling of C2)** now has more to weigh: C2 must survive both a 3.5× current increase from negative `A` and a 3.3× increase from the odd quadratic. Both still clear by five or more orders of magnitude on the squared current. Is that still an adequate basis for C2, or does the accumulation of separate effects each "still clearing" concern you?
- **Q6** — is our treatment of the odd second-order channel right? Specifically: is "harmless at the framework's scale, named as open beyond it" the correct disposition, or should the proposal decline to mention second order at all until the channel is bounded?

**If you have already returned on the earlier package**, you need only tell us whether A1 or A2 changes any answer you gave. Nothing else needs repeating.
