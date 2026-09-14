# 0963 — Piece 1, Route A first step: the corpus does pin the weights, and the floor argument already exists. It is closer to a day than a year.

**Patch:** 0963, 13 Sep 2026. **Lane:** chirality (09xx). **Type:** scoping report (search-and-read), the bounded session recommended at Patch 0961. **No claim registered, no verdict moved, piece 1 still formally open.**

**The question this session was to answer:** does the corpus already fix the dynamical η's weights, or is piece 1 a research programme?

**Answer: the corpus fixes them, and it also already contains the floor argument. Piece 1 is an assembly job, not a derivation.**

---

## 1. The weights are pinned, and they are unit magnitude

Every construction of η in the sub-corpus builds the per-edge weight as the **sign of a 4×4 orientation determinant**:

- **0819** (`klift_derivation`): `η_v = sign(g_v)`, `g_v` an orientation-weighted sum of local d.o.f.
- **0820** (`coarsegrain_effective_eta`): `osign(v,w) = sign det[d̂, n̂, r̂₁, r̂₂]` — commented in the source as *"a genuine pseudoscalar weight"*.
- **0821** (`residual1_eta_identity`, the correlator that produced K_lift): the same `sign(det(...))` weights.

**All three give `|w_e| = 1`.** The det-coset ℤ₂ is a statement about the *sign* of the determinant — that is what "det-coset" names — so a sign-valued weight is not a modelling convenience in these scripts, it is the construction.

**Consequence:** for unit-magnitude weights, **participation equals support**. `p(v) = 1/Σ(c_e)⁴` with all `|c_e|` equal over a support of size `m` gives `p(v) = m` exactly. Verified: unit weights on the full vertex figure give `p = 12.00`; on a minimal 4-edge reading, `p = 4.00`.

## 2. The floor argument already exists, in the F.1 sketches

`dynamical_substrate_law/sketches/lcapa_axis2_signcorr_closure.md` §5 states it:

> *"The only critical observable is `m=1`… carrying no intrinsic orientation. A genuine local enantiomorph indicator must resolve a handedness, i.e. an oriented frame; in 4-D an orientation is the sign of a 4×4 determinant, needing **≥ 4** independent directions. So the physical admissibility floor is…"*

This is the source of CHIR.md's phrase "the per-vertex **4-D orientation floor**." **The floor of 4 is not a chosen threshold — it is the dimensional requirement for an orientation to exist in 4-D.** An observable reading fewer than four independent directions cannot indicate handedness at all, so it is not a handedness observable and the theorem need not cover it.

## 3. The gap that remains — and it is narrow, and it is real

**The dimensional argument gives a SUPPORT floor, not a PARTICIPATION floor.** These are the same only for unit-magnitude weights. For general weights they come apart, and by a lot:

| observable | support | p(v) | clears p ≥ 4? |
|---|---|---|---|
| unit weights, full vertex figure | 12 | **12.00** | yes, 3× |
| unit weights, minimal reading | 4 | **4.00** | exactly at floor |
| general weights, full support, 70% on one edge | 12 | **3.79** | **no** |
| general weights, full support, 80% on one edge | 12 | **2.37** | **no** |

So an observable can have four or more independent directions in its support — satisfying the dimensional argument in full — and still fail the participation floor CAPACITY-1 requires. **The dimensional argument does not by itself deliver piece 1.**

**What closes the gap is §1:** the dynamical η's weights *are* unit magnitude, because the det-coset construction reads a sign per edge. With that, support = participation, and the dimensional floor becomes the participation floor.

## 4. What is actually owed — and it is short

Three statements, none of them new research, currently living in three different places and never joined:

1. **The dynamical η is the det-coset sign-reading, hence unit-weighted** (0819/0820/0821 all construct it this way; the det-coset ℤ₂ *is* a sign structure). **Needs stating as a claim rather than being implicit in three scripts.**
2. **For unit weights, `p(v) = ` support** (arithmetic, verified here).
3. **Support ≥ 4 by the 4-D orientation requirement** (lcapa §5, already written).

⇒ `p(v) ≥ 4` for the dynamical η. **Piece 1.**

**The one genuinely open sub-question**, and it should not be glossed: CAPACITY-1 quantifies over a class admitting *general* weights `w_e`, while the construction produces `±1`. Statement 1 is therefore a claim about the substrate, not a definition — **is the physically realised η necessarily unit-weighted, or could an effective/coarse-grained η acquire non-unit weights?** 0820 is the coarse-graining step and it preserves `osign`, i.e. unit magnitude. That is evidence, not proof, and it is the thing a reviewer will press on.

## 5. Recommendation

**One patch to assemble §4's three statements with a verify script, then a panel** — because making V3 unconditional on piece 1 is verdict-adjacent and under R-2 that is a fresh campaign, not a continuation of CONV-048.

**Before dispatching, R-1 applies** and I would run the hostile pass first: whether any coarse-graining or effective-η construction in the corpus produces non-unit weights; whether the minimal 4-edge reading is actually realisable on the 600-cell vertex figure or whether the construction always reads all 12; and whether the singleton-orbit shells found at 0961 admit a unit-weighted observable with support < 4.

**Revised estimate, against the 0961 question "a day or a year":** the derivation is a day. The assembly plus a hostile pass plus a panel is the real cost — call it two sessions and one dispatch, with the caveat that §4's open sub-question is exactly where a good reviewer will aim.

## 6. Disposition

- **Route A first step: COMPLETE.** The corpus pins the weights; the floor argument exists; piece 1 is assembly, not derivation.
- **Route C (CAPACITY-1B, banked at 0925) is no longer the likely play** — it was the fallback if piece 1 proved to be a programme, and it does not appear to be one.
- **Correction to 0961's framing:** that patch said the weights "must be derived from the dynamics." They were already derived; they were just never stated in one place as a claim about the dynamical η.
- **No claim registered. No verdict moved. CAPACITY-1 untouched. Piece 1 still open.**
