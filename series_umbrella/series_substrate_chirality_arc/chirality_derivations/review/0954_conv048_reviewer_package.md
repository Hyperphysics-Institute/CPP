# Review request: should a theorem's stated assumption be narrowed?

You are one of five independent reviewers. You do not need any prior knowledge of this research programme — everything needed is below. Please read Parts 1 and 2, then answer the six questions in Part 3.

**What we are asking you to judge:** a theorem currently says it depends on assumption X. We believe we have *proved* the part of X that the theorem actually uses, and that the unproved remainder of X is never used. If we are right, the theorem's stated assumption should be narrowed. We want to know whether we are right, and we especially want to know if we are fooling ourselves.

**Time required:** roughly an hour, including running three short Python scripts (attached separately). One of them takes about 45 seconds; the other two are under 2 seconds.

---

# Part 1 — Background

## 1.1 The physical setting, in plain terms

The programme models spacetime as a discrete lattice — specifically the **600-cell**, a 4-dimensional polytope with 120 vertices, each joined to 12 nearest neighbours by 720 edges. Signals hop from vertex to vertex along those edges.

The lattice has one built-in preferred direction, a unit 4-vector written **n̂**. Because of it, hopping is slightly anisotropic: a hop is marginally faster or slower depending on how the edge is oriented relative to n̂.

## 1.2 The rate law

The framework assumes hops occur at this rate:

> **`r(ê) = r₀ (1 + δ (ê · n̂))`**
>
> where **ê** is the unit vector along the edge being traversed, **r₀** is a baseline rate, and **δ** is a small number measuring the anisotropy. Its physical value is **δ = φ⁻³ ≈ 0.236**, where φ is the golden ratio.

This assumption is named **MA.1**. Together with a companion assumption about how hop rates combine into a net flow, the pair is called **Mechanism A**. Mechanism A has always been *assumed*, not derived — it is a stated input to the framework.

## 1.3 The theorem under review

**THEO-CHIR-CAPACITY-1** ("the theorem") says, informally:

> The lattice does not spontaneously develop a net handedness. A certain order parameter — a local left/right observable written **η**, defined at each vertex — does not "condense" (does not spontaneously align across the lattice) in any mode.

Why it matters: the lattice *is* observed to have a handedness. If that handedness cannot arise spontaneously, it must be built in from the start. So the theorem is the basis for treating handedness as fundamental rather than emergent.

**The theorem is registered as conditional on Mechanism A.** That is the assumption we are asking about.

## 1.4 The theorem's three supporting conditions — please read this carefully

The theorem was established by discharging three conditions. **These are not classes of particle, types of mechanism, or parameter regimes — they are three separate arguments, labelled for convenience.** A previous review round produced confusion here, so they are spelled out:

| label | what it is |
|---|---|
| **C1** | A spectral bound showing that the coupling between η at neighbouring vertices is too weak to produce alignment. It has two parts: (i) a *locality* step establishing that the coupling reaches only nearest neighbours; (ii) a *bound* step showing the resulting matrix has spectral radius ρ < 1. |
| **C2** | An argument that a certain persistent circulating flow in the lattice (a "steady current") is too small to shift the alignment threshold or drive alignment itself. |
| **C3** | A numerical check that η is comfortably below its critical coupling in every mode. The key number is **K_lift ≈ 0.053**, compared against thresholds of 0.095 and 0.27. |

There is also a **fourth, separate assumption** the theorem carries, which we call **piece 1**:

> **piece 1:** the η field is "pointwise non-degenerate" — at every vertex, η genuinely reads several incident edges rather than collapsing onto one.

**Piece 1 is not part of this review.** It is older, it is still assumed, and nothing in the work below touches it. We ask you to confirm that in Q5, because if we have accidentally implied otherwise, that is a serious error we want caught.

## 1.5 What is new: the rate law has two terms, not one

Recent work asked what symmetry alone forces the rate law to look like. The method: hop rates are functions on the lattice's 1,440 *directed* edges; the lattice's symmetry group must leave the physics unchanged; so expand in powers of n̂ and count how many independent symmetric forms exist at each order. Standard representation theory (Frobenius reciprocity) reduces this to counting invariants of the subgroup that fixes one directed edge.

**Three findings:**

**(a) At zeroth order, the rate is a single constant.** The symmetry group acts transitively on all 1,440 directed edges, so there is exactly one orbit and nothing can vary. *This part of MA.1 is now derived.*

**(b) At first order there are TWO independent terms, not one.** The subgroup fixing a directed edge has order 10 and leaves a 2-dimensional subspace fixed. So the general first-order rate perturbation is:

> **`A (m̂ · n̂) + B (ê · n̂)`**
>
> where **ê** is the edge direction (as in MA.1) and **m̂** is the edge's *midpoint*.

The two terms behave differently under reversing an edge (swapping its endpoints): the midpoint is unchanged, so the **A-term is reversal-even**; the direction flips, so the **B-term is reversal-odd**.

**(c) The reversal-odd part is unique.** Within the 2-dimensional space, the reversal-odd part is 1-dimensional — spanned by `B (ê · n̂)`, which is exactly MA.1's form. *So MA.1's form is derived, up to scale, as the unique reversal-odd first-order term, with δ ≡ B.*

**What is NOT derived:** that `A = 0`. Nothing in the symmetry forbids the reversal-even midpoint term. Nor is it derived that the rate law stops at first order — second-order terms are symmetry-permitted too.

**We call `A ≠ 0` and higher-order terms "the residual."** The question this review exists to settle is whether the theorem depends on the residual.

## 1.6 What we found when we tested the residual

We switched `A` on and re-ran each of the theorem's three conditions.

**C1 — unaffected.** Two reasons. First, both residual terms are functions of a *single edge* (the midpoint belongs to that edge), so they change per-edge numbers but never introduce a coupling between *different* edges — which is what C1's locality step needs. Second, C1's spectral bound is computed from the η observable's weights, not from the rate law at all; the rate law does not appear in it. Re-verified against 120 deliberately adversarial weightings: 0 violations, max ρ = 0.49.

**C2 — one real effect, which we have accounted for.** With `A = 0`, the steady current grows as δ³. With a constant `A`, it grows as roughly `A²δ` — a two-order change in how it scales at small δ. **This is genuine and we are not hiding it.** However, C2's claim is about the current's *size at the physical value* δ = φ⁻³, not about its scaling exponent. At that value the current stays between 1.7×10⁻⁵ and 3.4×10⁻⁵ across the whole range of `A` we tested — a factor of 2 — and the quantity that actually enters the argument, its square, stays below 1.2×10⁻⁹. The current also remains divergence-free and time-reversal-odd, which is what C2's symmetry step requires.

**Because of this, we are also proposing to amend C2's own wording** — it should be stated as a magnitude bound at the physical value, not as an "order δ³" claim, since the latter is false once `A ≠ 0` is admitted. This amendment is part of the proposal, not a separate question.

**C3 — unaffected.** K_lift moves from 0.0532 to 0.0526 across the tested range: margins of 36% and 80% against the two thresholds. The reason it barely moves is worth stating: **η is a sign.** A sign is unchanged if you scale its argument up or down, and a reversal-even term acts as a scale. So this kind of perturbation is close to the least effective way to move a sign-valued observable.

**A modelling choice we want scrutinised.** To test C3 we had to decide how `A` enters the statistical model underlying K_lift. Since `A` is reversal-even it cannot shift a reversal-odd mean, so we modelled it as a *scale* on each edge's fluctuation: `x_e = δ·bias_e + (1 + κ A m̂_e·n̂)·noise`. The constant **κ** relating rate modulation to fluctuation scale **is not derived anywhere.** We scanned it over κ ∈ {±0.5, ±1, ±2} and report the worst case. We do not claim this is a derivation, and Q4 asks you to judge it.

## 1.7 How large can A be?

A rate must be positive on every edge: `1 + A(m̂·n̂) ± B(ê·n̂) > 0`. At the physical δ this gives **|A| ≤ 1.025**. We tested `A ∈ [0, 1]`, which is **98% of the positive half of what is physically admissible.** So "we tested a range" is nearly "we tested everything the rate law allows" — but it is not literally everything, and the proposal below is worded accordingly.

---

# Part 2 — The proposal

We propose changing the theorem's stated conditionality from this:

> *THEO-CHIR-CAPACITY-1 is conditional on **Mechanism A**, together with per-edge independence of its measure and pointwise non-degeneracy of the dynamical η.*

to this:

> *THEO-CHIR-CAPACITY-1 is conditional on **MA.1's reversal-odd first harmonic** — `r(ê) = r₀(1 + δ ê·n̂)` with `δ ≡ B` — together with per-edge independence of the measure and pointwise non-degeneracy of the dynamical η (**piece 1, unchanged and still assumed**).*
>
> *It is **not** conditional on `A = 0`, nor on the rate law terminating at first order, for `|A|` within the physically admissible range `|A| ≤ 1.025` (of which `A ∈ [0,1]` has been tested).*
>
> *Accordingly, condition **C2** is restated as a magnitude bound at the physical bias δ = φ⁻³ — the steady current and its square are too small to affect the threshold — and no longer as a claim that the current is of order δ³, which does not hold when `A ≠ 0`.*
>
> *The reversal-odd first harmonic is **derived**, not assumed.*

**What this would and would not mean.** It would mean the theorem's rate-law input is proved rather than assumed. It would **not** mean Mechanism A as a whole is derived, and it would **not** make the theorem unconditional — piece 1 remains assumed, and that is a separate and older question.

---

# Part 3 — The six questions

Please answer each. Say **which tier** your answer rests on: **T1** = you computed or algebraically verified it yourself; **T2** = you audited the reasoning chain for consistency; **T3** = it requires a physical judgment call beyond the material provided.

---

**Q1. Is the uniqueness claim in §1.5 correct?**

That is: one orbit on the directed edges (so a single constant at zeroth order); an edge-fixing subgroup of order 10 with a 2-dimensional fixed subspace (so two first-order terms); and a 1-dimensional reversal-odd part (so MA.1's form is unique up to scale). Is there a missed invariant, a miscounted orbit, or an error in the reduction?

*If a majority finds this unsound, the whole proposal fails and we go back to the drawing board.*

---

**Q2. Does C1 genuinely survive `A ≠ 0`?**

Our argument is that both residual terms are functions of a single edge, so they change per-edge values without ever coupling *different* edges — and that C1's bound is built from the observable's weights rather than from the rate law. Is that sufficient, or does C1's locality step need something stronger that the residual breaks?

*If a majority finds this unsound, that is worse than rejecting our proposal — it would call into question the theorem's existing registered assumption. Please flag it clearly if so.*

---

**Q3. Is our handling of C2 honest and adequate?**

We found a real effect — the current's scaling changes from δ³ to ~A²δ — and rather than defend the old wording we are proposing to amend C2 itself, to a magnitude bound at the physical value. Two sub-questions: **(a)** is amending C2 the right response, or does the scaling change defeat C2's role in the theorem altogether? **(b)** is resting C2 on the magnitude at one physical value, rather than on an asymptotic statement, legitimate here?

*A previous round split on this. Both prior reviewers rejected the old "order δ³" wording; they differed on whether to amend C2 or to attach an exception instead. We have taken the amendment route and want it tested.*

---

**Q4. Is the C3 modelling choice defensible? (Dissent actively wanted.)**

We modelled the reversal-even residual as a per-edge *scale* on fluctuations rather than a shift in their mean, on parity grounds, and we scanned the unknown constant κ rather than deriving it. Is the scale-not-mean identification right? And is scanning κ an acceptable substitute for deriving it — or does it merely show the result is insensitive within the box we happened to choose?

---

**Q5. Have we correctly left piece 1 alone?**

We claim that none of this work addresses, weakens, or discharges the assumption that η is pointwise non-degenerate, and that it remains a live condition of the theorem. Is that accurate — or does anything in Part 1 quietly depend on it?

*If you disagree, say so explicitly; this one is escalated to the principal investigator rather than settled by vote.*

---

**Q6. What have we missed?**

Anything: an error, an unstated assumption, a better way to test the claim, a place where we have overclaimed. Items raised here are adopted regardless of how the other questions come out.

---

# Part 4 — How to return

**Please include all of the following.** A return missing the execution evidence cannot be counted.

1. **Who you are** — model and version.
2. **Execution evidence.** Run the three attached scripts and report, for each, the pass count printed on the last line and your wall-clock time:
   - `0949_l4a_rate_law_form.py` → expect `8/8`, ~1 s
   - `0950_capacity1_residual_consumption.py` → expect `7/7`, ~2 s
   - `0951_c3_klift_recompute.py` → expect `5/5`, ~45 s
   If a script will not run in your environment, **say so plainly and say what you did instead.** An honest substitution is worth far more to us than a reported number you did not produce; a previous round included returns whose timings were not physically possible, and they were rejected.
3. **Your six answers**, each with its tier label.
4. **Your overall verdict:** enact / enact with amendments / do not enact / do not enact and escalate.

Please disagree where you disagree. We are asking five independent reviewers precisely because we may be fooling ourselves, and a return that agrees with everything is of little use to us.
