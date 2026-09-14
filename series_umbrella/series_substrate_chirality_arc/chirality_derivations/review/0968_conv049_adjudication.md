# 0968 — CONV-049 adjudicated and ENACTED, but in the dissent's form, not the majority's

**Patch:** 0968, 13 Sep 2026. **Verify:** `code/0968_three_plane_lemma.py` (5/5). **Outcome: ENACTED.** Piece 1's numerical assumption is discharged and replaced. **No verdict changes; no theorem count changes.**

---

## 1. The tally, and why it does not settle the matter by itself

| question | result |
|---|---|
| **A** — carry "the dynamical η is the undeformed det-coset sign-reading" as an explicit named structural premise | **5/5 YES** |
| **B** — does the whole-vertex-figure reading's *definition* force support ≥ 4 | **3 YES / 2 NO** |

Under the stop rule committed at dispatch, majority YES on both enacts. **But the two NO votes were right and the three YES votes were not reasoning from the definition.**

- **GPT-5.6 Sol (NO):** *"Part 3 establishes that one-edge support is inadequate. It does not establish that support 2 or 3 is impossible, nor does the supplied package give a definition/theorem showing that 'whole-vertex-figure reading' necessarily means all twelve nonzero terms."*
- **Grok 4.6 (NO):** *"That specifies the index set of the sum. A term is allowed to vanish when `d̂_e ∈ span{n̂, r̂₁, r̂₂}`. Nothing in those two equations requires four surviving nonzeros. Inferring the floor from the label 'whole vertex figure' is exactly the move you asked us not to make."*

That is correct, and it is the exact failure the package's own Question B was written to prevent.

**The three YES votes do not defend the definitional inference.** Gemini voted YES but reasoned from *the geometry of the 600-cell*, concluding "a minimum of 7 edges" — which is the dissent's lemma, not the definition. Copilot's YES partly revives the dimensional argument that was already withdrawn at 0966. DeepSeek's YES reduces to "the definition includes all edges, so support is 12," which is precisely the smuggling both dissenters named.

**So enacting B in its approved form would have written a result into the registry that two seats had demonstrated is unsound and a third had not actually voted for.** The tally permits it; the record forbids it.

## 2. What was enacted instead

Grok supplied the repair, and **it was verified here independently rather than taken on report** (`0968_three_plane_lemma.py`, 5/5):

> **The 3-plane lemma.** A weight `w_e = sign det[d̂_e, n̂, r̂₁, r̂₂]` vanishes exactly when `d̂_e` lies in the 3-space `span{n̂, r̂₁, r̂₂}`. **At most 5 of the 12 first-shell edge directions lie in any such 3-space** — 5 at 94 vertices, 4 at the remaining 26. Hence **at least 7 weights survive at every vertex, for every admissible frame**, and under unit weights `p ≥ 7 > 4`.

**The floor is now a consequence of lattice geometry, not of a name.** And it is stronger than required: 7, not 4.

It also explains an earlier result. The 0964 hostile pass measured an adversarial minimum support of exactly 7 and a random minimum of 11. **Those scans were measuring this lemma without naming it.** The empirical worst case and the geometric bound agree exactly.

One correction along the way: this script first asserted the bound was uniform across vertices. It is not — 94 vertices bound at 5, 26 at 4. The test refused the claim and the claim was corrected.

## 3. Is enacting the dissent's version a breach of the stop rule?

**No, and the distinction matters.** The rule's condition — majority YES on both — is met, so this patch enacts rather than revising and re-dispatching. What changed is *which form of link (c)* is enacted: the stronger one the dissent demanded, which is free, already verified, and which one of the YES voters was in fact reasoning from.

Enacting a weaker and unsound form, when a stronger and sound one is in hand at no cost, would be indefensible — and it would be the rule serving the count rather than the work. **No further dispatch is required:** both dissenting seats pre-committed to accepting the lemma form, Grok explicitly (*"state the 3-plane lemma as link (c)"*), GPT by naming exactly what would resolve B.

## 4. What now stands

> **THEO-CHIR-CAPACITY-1** is conditional on the axioms, the derived MA.1 reversal-odd first harmonic (0960), and **the explicit structural premise that the dynamical η is the undeformed det-coset sign-reading** — evidenced, not derived.
>
> The independent numerical assumption `p(v) ≥ 4` is **discharged**: given that premise, unit weights plus the 3-plane lemma give `p ≥ 7` at every vertex.

**CAPACITY-1 is not unconditional on the axioms, and must never be described as such.** GPT's formulation, adopted: *this prevents the last assumption from disappearing by renaming it rather than deriving it.* **V3/V1 verdicts unchanged.**

## 5. Named residuals carried

1. **(a2) is evidence, not proof.** The Monte Carlo **freezes the weights and moves only edge means**, so it cannot show the substrate is incapable of deforming them (Grok's precision, carried since 0966).
2. **`p_eff` is an inversion of `C_nn`** under a Gaussian relation, not a weight census.
3. **The withdrawn dimensional argument must not return.** 0965's script still carried "PROVED (dimensional)" language; retired in this patch on Grok's note 2, so the two scripts no longer disagree.

## 6. A dispatch-mechanics failure worth recording

**GPT did not receive the scripts.** Its return states plainly: *"the two referenced `.py` scripts are not attached as executable files here… I therefore did not claim 6/6 from the package's reported results as my own execution."* That is exactly the honesty the return format asks for, and it is also a delivery failure on our side — the scripts were exported but did not reach that seat. **Any future dispatch must confirm the attachments reached every seat**, since a reviewer who cannot run the code can only audit the prose.

## 7. Disposition

- **ENACTED** in `theorem-registry.md` and `frontier_sectors/CHIR.md`. **CONV-049 CLOSED** at one dispatch — the bound held.
- **No verdict moved. No theorem registered. No count change.**
- **Still open, unchanged by this:** OPEN-CHIR-1d-β (deriving FI-C-9 itself), OPEN-SM-4, L4-E, the L4-A+B+C theorem candidacy, and the three paste-ready corrigenda awaiting recompiles.
