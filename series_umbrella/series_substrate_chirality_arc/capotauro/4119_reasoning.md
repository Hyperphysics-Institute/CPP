# 4119 — Capotauro v2.1 first tranche (Tier 4 reasoning, filed late at 4131)

**Lane:** CHIR/EW. **Filed late:** the §15 Step D check at Patch 4131 found 4119 had no Tier-4
document — the only record was its commit message. A patch that **edits a shipped paper** needs
one. Recorded here rather than silently.

## The decision that shaped the patch

The founder's approval was conditional: *"If everything Capotauro-related has been retired as a
useful/necessary mechanism, and properly replaced with a more fundamental mechanism, then I
fully approve."* **That antecedent was not met**, in two ways, so it was not taken at face value:

1. **Not everything should be retired.** The magnitude — sub-claim (c), THEO-CAP-1, |M| = χ/6 —
   is not replaced by χ₄, which produces no magnitude anywhere. It carries PRED-O-25, validated
   within 2%. It stays.
2. **The replacement was not in place.** χ₄ was a candidate awaiting the A3G suite, three of
   whose tests were falsifiers. "Properly replaced" was not yet true.

## What was executed, and on what grounds

Sub-claim (a) was retired on grounds **independent of χ₄ and robust to its failure**: Patch 4104
established n̂ selects no enantiomorph (−I₄ is proper in ℝ⁴; 30 improper symmetries fix n̂ under
the vertex-aligned reading). **A sub-claim whose stated mechanism cannot perform its stated
function does no work and is retired whatever succeeds it.** χ₄ was named as candidate
successor, explicitly not adopted.

That framing has since proved its worth: χ₄'s case narrowed considerably (4121, 4128, 4129), and
the retirement is unaffected because it never rested on χ₄.

- **E2** |χ| renamed to *primitive anisotropy amplitude* + scope remark + 12 occurrences swept
- **E3** sub-claim (a) → superseded and withdrawn, **retained not deleted** (a published-then-
  withdrawn claim stays visible with its reason)
- **E5** δ_CP/η_B referral withdrawn; *no candidate mechanism exists* recorded

LaTeX verified: whole-file brace balance unchanged from HEAD; environments paired.
