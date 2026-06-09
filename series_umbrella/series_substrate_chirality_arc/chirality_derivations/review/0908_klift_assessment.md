# Chirality-lane assessment — K_lift derivation (Patch 0819)

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/0908_klift_assessment.md`
**Patch:** 0908 · **Reviews:** Patch 0819 (F.1/DSL window — lift-induced η–η coupling K_lift vs K_c=1/12).
**Disposition:** Substantial reduction, accepted as **input to the verdict spec (0907)**. **No verdict move. V3/W3 stand. THEO-CHIR-CAPACITY-1 stays reserved.** DG-3 not met.

---

## 1. Does it help? Yes — it compresses the verdict to one named question

0819 is a real reduction. The entire chirality verdict is now reduced to a **single quantity**: the d.o.f.-structure `m` of the *effective* η-field (equivalently `K_lift`, equivalently `sign(K_c − K_lift)`). The threshold is computed (K_c = 1/12 mean-field) and the comparison is sharp. This is the maximal reduction reachable without the effective action, and it lands exactly on the 0907 verdict criterion.

The F.1 window's self-correction is accepted and good practice: the 0818 "K_lift ≪ 1/12, comfortably primitive" over-lean is retracted; `K_lift` is the **same order** as K_c (both ~1/z, z=12).

## 2. Sharpening: the knife-edge is in the η-IDENTITY, not in a marginal number

The "knife-edge" is best localized. For a *fixed* η-identity the comparison is not razor-thin — it is the **choice of η-field** that straddles the threshold (crossover at m ≈ 8):

- registry actualization (0906 edge pattern `ε(ê·n̂)`, full vertex figure, m=12): K_lift/K_c ≈ **0.64 → primitive**;
- a vertex/state-based reading (adjacent vertices share 5 neighbours): K_lift/K_c ≈ **3.4 → emergent**.

One correction in the favourable direction: **mean-field K_c = 1/12 is a *lower bound*** on the true K_c (fluctuations raise the critical coupling). So for the m=12 case the *true* margin is **better than 0.64** (true K_lift/K_c < 0.64). Conclusion: **conditional on the effective η being the m=12 edge object, the primitive reading is reasonably robust, not razor-thin.** The whole uncertainty is therefore the η-identity — *which* effective field the dynamics produces.

## 3. The chirality-lane caution (the value-add): the η-identification is unproven

0819's primitive lean rests on identifying the **dynamical effective η-field** (the order parameter whose NESS fluctuations set K_lift) with the **descriptive edge pattern of 0906** (`ε(ê·n̂)` over the 720 edges, m=12). Those are not the same object by definition:

- 0906 describes how the *primitive* `sign(n̂)` is geometrically *actualized*;
- K_lift needs the *order parameter the coarse-grained dynamics acts on*.

Equating them is a **cross-lane object identification of exactly the class that produced the earlier inversion** — plausible, registry-consistent, and likely right, but **it must be *derived* by coarse-graining, not assumed.** If the effective dynamical η is more local than the m=12 edge object, the verdict crosses to emergent. This is condition (1) of the chirality gate (0904: "confirm the precise H₄/H₄⁺ order-parameter field is local / what η is"), now revealed as the pivot of the whole verdict.

## 4. The O(δ³) current completeness check (0907 §3) is still open and separate

0819 derives the **symmetric** lift-induced coupling. It does **not** address the O(δ³) current (the 0814 product-departure): whether the current shifts the effective K_c toward K_lift, or drives a non-equilibrium ordering the equilibrium K_c comparison cannot see (also where the VW/RP route can fail). The verdict-complete condition remains **both** (i) the η-identity pins m on the primitive side of the current-corrected K_c, **and** (ii) the current induces no ordering. K_lift settles part (i)'s coupling; neither the η-identity nor (ii) is closed.

## 5. Disposition + the next probe

**No verdict move** (DG-3 unmet: η-identity not derived, current not cleared, comparison is identity-sensitive). V3/W3 stand; THEO-CHIR-CAPACITY-1 reserved; header count unchanged; conditional on Mechanism A (OPEN-FP-F1-2).

**On the F.1 window's proposed next probe** (coarse-grain Mechanism A to derive the η d.o.f.-structure): **endorsed** — it is the right next infrastructure step and it targets the now-pivotal unknown. Two chirality-lane asks of it: **(a) DERIVE the effective η-identity from the coarse-graining — do not assume effective η = the 0906 edge pattern** (§3); **(b) carry the O(δ³) current through, not just the symmetric coupling** (§4). This probe is also, by the F.1 window's own read and ours, **the node most likely to hand off to Thomas's PCD layer** — because "what is the effective η-field" is partly a physical/definitional question about the order parameter, not a pure calculation. If it bottoms out, it bottoms out *there*, precisely.
