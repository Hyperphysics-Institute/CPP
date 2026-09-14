# Review request: can a theorem's last numerical assumption be replaced by a structural one?

You are one of five independent reviewers. **No prior knowledge of this research programme is assumed** — everything you need is below. Read Parts 1–3, then answer the two questions in Part 4.

**Time:** roughly an hour, including running two Python scripts (attached). One takes about 4 seconds, the other about 30.

**What makes this review unusual:** we are *not* asking you whether something has been proved. We know it has not. We are asking whether a specific unproved thing is acceptable to carry as an **explicit named premise**, and whether a second thing follows from it. Those are different judgments and they are asked separately on purpose.

---

# Part 1 — The setting

## 1.1 The lattice

The programme models spacetime as a discrete lattice — the **600-cell**, a 4-dimensional polytope with 120 vertices, each joined to 12 nearest neighbours by 720 edges. The lattice has one built-in preferred direction, a unit 4-vector **n̂**, which makes signal-hopping slightly anisotropic. The size of that anisotropy is a number **δ**, whose physical value is **δ = φ⁻³ ≈ 0.236** (φ = golden ratio).

## 1.2 The handedness detector, η

At each vertex there is a local left/right indicator called **η**. It works by reading the twelve edges at that vertex and combining them into a single ± verdict:

> **`η_v = sign( Σ_e w_e x_e )`**, the sum running over the edges at vertex `v`.

`x_e` is the state variable on edge `e`; `w_e` is the weight η gives that edge. In this programme's construction, the weight is the **sign of a 4×4 orientation determinant**, `w_e = sign det[d̂_e, n̂, r̂₁, r̂₂]`, where `d̂_e` is the edge's direction and `(r̂₁, r̂₂)` is a reference frame. **Because it is a sign, every weight has magnitude 1.**

## 1.3 The theorem, and the assumption under review

**THEO-CHIR-CAPACITY-1** says, informally: *the lattice does not spontaneously develop a net handedness — η does not align across the lattice.* This matters because the lattice *is* observed to be handed, so if handedness cannot arise spontaneously it must be built in.

The theorem currently carries an assumption we call **piece 1**:

> **piece 1:** at every vertex, η is *pointwise non-degenerate* — it genuinely reads several edges rather than collapsing onto one. Formally `p(v) = 1/Σ_e (c^v_e)⁴ ≥ 4`, where `c^v_e` are the normalised weights and `p(v)` is the **participation** — the effective number of edges η reads.

**Piece 1 is currently just assumed.** It is the theorem's last remaining numerical assumption. This review is about whether to replace it.

---

# Part 2 — The proposal

**We are not proposing to prove piece 1.** We are proposing to replace it with a different, structural premise, from which it follows.

The chain has four links:

| link | content | status |
|---|---|---|
| **(a1)** | The construction in §1.2 *is* a sign structure, so weights have unit magnitude. | **definitional** |
| **(a2)** | **The substrate's dynamics does not deform those weights.** | **EVIDENCED, NOT PROVED — this is the whole question** |
| **(b)** | For unit-magnitude weights, participation = support exactly (`p` = number of edges actually read). | **proved** (arithmetic) |
| **(c)** | The canonical η is the *whole-vertex-figure* reading, and its support is ≥ 4. | **proved within that scope** |

**(a1) + (a2) + (b) + (c) ⇒ p(v) ≥ 4.**

**What would change if you sustain this.** The independent numerical assumption `p(v) ≥ 4` is discharged and **replaced** by the structural identification in (a2), which remains explicit. The theorem would then rest on the axioms, a separately-derived rate-law result, **and that structural reading**. It would **not** become assumption-free. We say this plainly because an earlier draft of this proposal claimed otherwise and two reviewers rejected the claim; their point was that this must not become *an assumption disappearing by being renamed rather than derived*.

---

# Part 3 — The evidence, and its exact limits

## 3.1 Why the evidence for (a2) is not merely a null result

The test measures a quantity `C_nn` — the correlation between η at neighbouring vertices — at different values of the anisotropy δ. **If the anisotropy were concentrating η's reading onto fewer edges, `C_nn` would change.**

A reviewer of an earlier draft objected, correctly, that this is worthless unless `C_nn` actually responds to participation. **So we calibrated it first.** On the Gaussian base, `C_nn = (2/π) arcsin(1/p)`:

| p | 12 | 8 | 6 | 4 |
|---|---|---|---|---|
| C_nn | 0.0531 | 0.0798 | 0.1066 | 0.1609 |

A collapse from `p = 12` to the floor of 4 would **triple** `|C_nn|`. So the measurement is sensitive across exactly the range in dispute, and a null result becomes a **bound**: a measured `|ΔC_nn| ≤ 3×10⁻⁴` **excludes any participation below `p ≈ 11.9`.**

## 3.2 The measurement at the physical anisotropy

Six values of δ through the physical value, six independent Monte-Carlo replicates each:

| δ | C_nn | s.e. | p_eff |
|---|---|---|---|
| 0.0000 | −0.0528 | 0.00029 | 12.06 |
| 0.1000 | −0.0527 | 0.00036 | 12.10 |
| **0.2361 = φ⁻³** | **−0.0521** | **0.00030** | **12.24** |
| 0.3000 | −0.0517 | 0.00031 | 12.34 |

**At the physical value, `p_eff = 12.24` against a floor of 4.** There is no concentration trend; if anything participation rises slightly with δ.

Independently, direct computation of the construction's support gives a minimum of **11 of 12** over 150 random frames, and **7 of 12** under adversarial frames chosen to force degeneracies.

## 3.3 Three limits on that evidence, stated by us rather than left for you

These were identified by pre-dispatch reviewers and we are carrying them verbatim:

1. **`p_eff` is an inversion of `C_nn` under a Gaussian relation — not a direct census of the weights.** It is only as universal as that relation.
2. **The Monte Carlo freezes the weights and moves only the edge means.** So the test shows that *polarising a fixed unit-sign reading does not mimic concentration*. **It does not show that the substrate is incapable of deforming the weights.** That is precisely the gap (a2) names.
3. **(c) is scope, not dimension.** An earlier draft argued that resolving handedness in 4-D requires four independent directions, therefore four edges. **That argument was wrong and is withdrawn** — only one of the four vectors in the determinant is an edge direction. What replaces it: a single-edge determinant is *frame-dependent* (its sign flips under 98 of 200 admissible frames), so it cannot be the invariant observable; the canonical reading is the whole vertex figure.

---

# Part 4 — The two questions

Answer both. They are separate judgments and a panel that merges them will produce a muddled verdict.

---

**Question A — epistemic.**

**Is the corpus construction, together with the evidence in Part 3, sufficient to carry *"the dynamical η is the undeformed det-coset sign-reading"* as an explicit, named structural premise of the theorem?**

Note what is *not* being asked: whether it is derived (it is not), or whether it may be struck (we are not proposing that). Only whether carrying it as a named premise is acceptable, in place of the bare numerical assumption `p(v) ≥ 4`.

---

**Question B — mathematical/definitional.**

**Conditional on A: does the definition of the whole-vertex-figure reading actually force support ≥ 4 — and hence `p ≥ 4`?**

One reviewer asked us to put a precise joint to you rather than answer it ourselves, so here it is in his words: *does the corpus definition of the whole-vertex-figure reading actually require nonzero unit-magnitude contributions from at least four edges?* **"Whole vertex figure" should not merely be a label from which support is inferred.** If the definition genuinely requires it, `p ≥ 4` follows immediately under (a2). If it does not, say so — that is the answer we most need.

---

**Optional: anything we have missed.** Adopted regardless of your verdict on A and B.

---

# Part 5 — How to return, and when this stops

**Include:** who you are; the pass count and wall-clock time for each script (`0965_piece1_assembly.py`, expect 6/6 ~4 s; `0966_piece1_physical_delta.py`, expect 6/6 ~30 s); your answers to A and B; and your overall disposition.

If a script will not run in your environment, **say so plainly and say what you did instead.** An honest substitution is worth more to us than a number you did not produce.

## The effort bound — committed before your returns, not after

A previous campaign in this programme ran to nine rounds because each round produced a correction that triggered the next. Our governance requires a stopping rule written *before* the work; we failed to write one then. **This is it, written now.**

- **This is dispatch 1 of at most 2 on this claim.**
- **Majority YES on both A and B** ⇒ we enact: the numerical piece-1 assumption is discharged and replaced by the named structural premise.
- **Majority NO on A** ⇒ we abandon the replacement and piece 1 stays as it is. No further dispatch.
- **Majority NO on B** ⇒ the scope question returns to us for one revision and at most one further dispatch. If still unresolved, we abandon.
- **Notes and optional findings are recorded as named residuals. They do not trigger another round.** If you think something should *block*, say NO on A or B — do not rely on a note to force a further cycle.

We are telling you the rule so you can calibrate your answer to it.
