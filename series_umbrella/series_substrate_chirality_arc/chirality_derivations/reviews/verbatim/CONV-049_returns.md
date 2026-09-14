# CONV-049 — verbatim returns (5 seats)

**Dispatched:** Patch 0967. **Adjudicated:** 0968 — **ENACTED, in the dissent's form.**
**Tally: A = 5/5 YES · B = 3 YES / 2 NO.**

The B split is the reason this file matters. A tally records three-against-two; the text records that the two were right, that one of the three reasoned from the dissent's own geometry, and that a third's YES revived an argument already withdrawn.

---

## GPT-5.6 Sol — **A YES · B NO**

Execution, and a delivery failure on the lane's side:

> "**SCRIPT STATUS:** I cannot honestly supply the required own-run counts/timings from this dispatch. The review package is attached, but the two referenced `.py` scripts are not attached as executable files here. I therefore did **not** claim `6/6` from the package's reported results as my own execution."

A:

> "**YES: it is acceptable to carry 'the dynamical η is the undeformed det-coset sign-reading' as an explicit, named structural premise.** This is importantly **not** a vote that (a2) has been derived… So A passes as an **explicit structural premise**, not as a theorem."

B — the sentence that killed the lane's link (c):

> "Part 1.2 gives the observable as η_v=sign(Σ w_e x_e), w_e=sign det[d̂_e,n̂,r̂₁,r̂₂] … **If that twelve-edge formula is itself the binding definition of the canonical dynamical η, then the result is actually stronger than B asks for:** under undeformed unit weights its support is 12, hence p=12, not merely p≥4. But Part 3 introduces a different issue… That establishes that **one-edge support is inadequate**. It does not establish that support 2 or 3 is impossible, nor does the supplied package give a definition/theorem showing that 'whole-vertex-figure reading' necessarily means all twelve nonzero terms rather than some invariant combination of a proper subset."

Its stated resolution condition — met by the enacted lemma, and recorded as met at 0969:

> "**Does canonical η, by definition or invariance, require the twelve unit-sign edge contributions appearing in §1.2—or, failing that, can every invariant proper-subset realization be shown to require at least four nonzero edges?**"

## Grok 4.6 — **A YES · B NO**, and supplies the repair

Own-run: `0965` 6/6 3.75 s · `0966` 6/6 26.94 s.

B:

> "Part 1.2 defines … sum over the twelve incident edges. That specifies the *index set* of the sum. A term is allowed to vanish when d̂_e ∈ span{n̂,r̂₁,r̂₂}. Nothing in those two equations requires four surviving nonzeros. **Inferring the floor from the label 'whole vertex figure' is exactly the move you asked us not to make.**"

The lemma, verified independently at 0968 and enacted as link (c):

> "The twelve edge directions at a 600-cell vertex span ℝ⁴. A weight vanishes iff that direction lies in a 3-plane. Checking every 3-space spanned by three of those directions: **at most five of the twelve lie in any such 3-space**, hence **support ≥7** when vanishing is aligned to the figure. Random frames in the same check gave support 12 in 2000/2000 trials."

And his pre-commitment, which is why no further dispatch was owed:

> "If you want p≥4 as a consequence rather than a label, the next (and, by your rule, last) revision should state the 3-plane lemma as link (c), with the frame scans as its check, and retire 'whole vertex figure ⇒ support ≥4'."

## Gemini — **A YES · B YES**, reasoning from the dissent's geometry

Its B answer does not defend the definitional inference; it reproduces Grok's lemma:

> "The 12 edge directions of a vertex figure in the 600-cell form a regular icosahedron in the 3D subspace orthogonal to the radial vector… **the geometry of the 600-cell guarantees a minimum of 7 edges with non-zero determinants.** Therefore, the definition of summing over the *whole* vertex figure, combined with the fixed geometry of the 600-cell, strictly requires non-zero unit-magnitude contributions from at least 7 edges. Since 7 ≥ 4, the support is structurally guaranteed."

**This is the dissent's argument arriving under a YES label** — recorded at 0968 as the reason the tally could not be read at face value.

## Copilot — **A YES · B YES**

Own-run: `0965` 6/6 3.9 s · `0966` 6/6 31.2 s. Its B partly revives the dimensional argument withdrawn at 0966:

> "by construction that set contains at least four independent directions in the sense required to form the orientation determinant. The arithmetic in (b) and the dimensional argument in (c) together imply that the support … is ≥ 4."

With a caveat that concedes the dissent's point:

> "If a reader objects that 'whole-vertex-figure' could be interpreted more weakly (e.g., allowing degenerate frame choices that zero some edges by construction), then the implication would fail."

## DeepSeek — **A YES · B YES**

Own-run: `0965` 6/6 ~4 s · `0966` 6/6 ~30 s. Its visible reasoning wobbles onto and off the dissent's point before landing on YES:

> "But the issue is that the dynamical η might deform the weights away from unit magnitude. Under (a2), we assume it does not, so the weights remain unit magnitude. Then indeed, every edge contributes with equal magnitude, so support = 12… So the definition of the whole-vertex-figure reading, if taken literally, requires all edges to be included."

Its final B reasoning is "the definition includes all edges" — **the smuggling both dissenters named.**
