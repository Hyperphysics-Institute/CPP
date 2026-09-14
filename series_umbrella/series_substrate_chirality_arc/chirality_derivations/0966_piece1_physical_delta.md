# 0966 — The owed physical-bias test, and three fixes the pre-dispatch panel demanded. Grok's objection was decisive and is answered by a bound, not a defence.

**Patch:** 0966, 13 Sep 2026. **Lane:** chirality (09xx). **Verify:** `chirality_derivations/code/0966_piece1_physical_delta.py` (6/6). **Status:** still DRAFT, still not registered — but the blocking items are now cleared.

Five pre-dispatch returns on the 0965 draft (GPT-5.6 Sol, Grok 4.6, Gemini, Copilot, DeepSeek). **Unanimous: HOLD.** All five demanded the physical-δ test; two independently demanded the headline sentence be withdrawn; two independently attacked link (c). All of it was right.

---

## 1. Grok's objection, which came first because it could have voided everything

> *"C_nn is a proxy for participation. The claim is about p(v). Measure p(v) against δ directly. If C_nn is insensitive to a drop from p=12 toward p=4, a 3×10⁻⁴ shift is not evidence."*

If `C_nn` doesn't respond to participation, 0965's T4 measured nothing. **Tested first.**

On the Gaussian base `C_nn = (2/π) arcsin(1/p)`, so `C_nn(p=12) = 0.0531` against `C_nn(p=4) = 0.1609` — **a factor of 3.03 across exactly the range in dispute** (T1). The proxy is strongly sensitive to the quantity the claim is about.

**And that turns the null result into a bound, which is the right answer rather than a defence of the proxy.** Inverting the relation: a measured `|ΔC_nn| ≤ 3×10⁻⁴` **excludes any participation below `p ≈ 11.93`** (T2). 0965's measurement does not merely fail to detect concentration — it bounds concentration to `p ≥ 11.9` against a floor of 4.

## 2. The owed test, done properly

Not two endpoints at a convenience value. Six δ values through the physical bias, six independent Monte-Carlo replicates each, standard errors, and **`p_eff` reported directly** as Grok and Copilot required:

| δ | C_nn | s.e. | p_eff |
|---|---|---|---|
| 0.0000 | −0.0528 | 0.00029 | 12.06 |
| 0.0500 | −0.0528 | 0.00035 | 12.07 |
| 0.1000 | −0.0527 | 0.00036 | 12.10 |
| 0.1600 | −0.0525 | 0.00034 | 12.15 |
| **0.2361 = φ⁻³** | **−0.0521** | **0.00030** | **12.24** |
| 0.3000 | −0.0517 | 0.00031 | 12.34 |

**At the physical bias, `p_eff = 12.24` against a floor of 4.** The shift from δ = 0 is 0.0008, within a few standard errors.

**The trend runs the helpful way.** `p_eff` increases with δ at `+0.92` per unit δ — the bias very slightly *de*-concentrates the reading. There is no systematic concentration anywhere on the interval, and the worst point in the scan sits three times above the floor.

## 3. Link (c) rescoped — the universal form is withdrawn

Two reviewers attacked it independently, and the sharper version is GPT's:

> *"Four vectors required to define chirality ⇏ four nonzero coefficients required to read an already-defined chirality variable."*

**That is correct and it defeats (c) as 0965 wrote it.** Only **one** of `{d̂, n̂, r̂₁, r̂₂}` is an edge direction; the other three are the fixed frame. So "an orientation needs four independent directions" says nothing about how many *edges* the reading must touch. Grok added that 0965's T2 was too weak to carry the prose: `rank{d̂, n̂} = 2` is trivial and shows nothing about 2- or 3-edge readings once the frame is present.

**What actually carries (c) is scope, not dimension.** A single-edge determinant is **frame-dependent** — its sign flips under **98 of 200** random admissible frames (T6). A frame-dependent quantity is not an invariant handedness reading. The canonical observable is the whole-vertex-figure orientation (0820 §(1)), whose frame-dependence cancels across the twelve edges.

**So (c) holds within the det-coset vertex-figure scope, and the universal version — "any sub-4-support functional is not a handedness observable" — assumed the conclusion and is withdrawn.** CAPACITY-1's η must be explicitly scoped to the vertex-figure reading, as Grok required.

## 4. The headline sentence, withdrawn

0965 said: *"CAPACITY-1's piece-1 conditionality discharges and V3 becomes unconditional on anything but the axioms."* GPT and Grok independently ruled it must not ship. Grok: *"That contradicts the next page."* GPT: it *"prevents the last assumption from disappearing by renaming it rather than deriving it."*

**Corrected, and adopted essentially as GPT drafted it:**

> *If sustained, the independent quantitative piece-1 assumption `p(v) ≥ 4` is discharged and **replaced** by the structural identification that the dynamical η remains the undeformed det-coset sign-reading. CAPACITY-1 then carries no independent numerical participation-floor assumption; the structural identification remains explicit unless separately derived from the axioms. V3 would rest on the axioms, the derived MA.1 reversal-odd first harmonic, **and that structural reading**.*

0965 has been amended in place.

## 5. What (a2) still is

Unchanged and unchangeable by this patch: **evidence, not proof.** The scan bounds concentration tightly across the physical range for this observable to this precision. It does not derive weight-uniformity from A1–A11. Every reviewer said so and the draft agrees.

## 6. Dispatch structure — adopting GPT's split

GPT recommended sending the panel two sharply separated questions rather than "is piece 1 proved":

- **(A)** Does the corpus definition plus dynamical evidence justify carrying *"the dynamical η is the undeformed det-coset sign-reading"* as an explicit structural premise?
- **(B)** Given that premise, does the definition of that *reading* — rather than merely the geometry defining its sign — force support ≥ 4?

**Adopted.** If both pass, `p ≥ 4` follows cleanly, and what still does not follow is axiom-only unconditionality.

## 7. Disposition

- **Blocking items cleared:** physical-δ test done with a scan and error bars; `p_eff` reported directly; (c) rescoped; headline withdrawn and corrected.
- **Still DRAFT.** No claim registered, no verdict moved, CAPACITY-1 untouched, piece 1 formally open.
- **Ready for R-2 dispatch**, with the effort bound written *at* dispatch — clause 3(i), and not repeating the CONV-047/048 miss, as Grok explicitly reminded us.
- **Standing credit:** all four substantive corrections in this patch came from the pre-dispatch panel. The R-1 discipline of reviewing before dispatching is what made them cheap.
