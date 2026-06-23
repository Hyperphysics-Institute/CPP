# VTD-1 RESOLVED — the bulk⊥internal quadrature is FORCED, by reduction to SR-1's f_eff

**Patch:** 2037 (22 June 2026) · **Window:** 2000-band · **Status: substantive — VTD-1 PASS, conditional
on the one SR-1 input that Appendix H already names (not on a new assumption).**
**Verify:** `scripts/2037_vtd1_quadrature_feff_bridge.py` (quadrature == 1−f_eff == energy-bridge == 1/γ, exact).

---

## 0. The question (from VTD-1_handover.md)

VTD-1 asks whether the displacement-budget quadrature — bulk consumes v·t_P along the motion, internal gets
the **orthogonal** remainder √(l_P²−(v t_P)²) = l_P/γ — is **(A) forced** by the substrate mechanism or
**(B) an assumption** that merely reproduces γ. The named worry: "in the standard light-clock the
orthogonality is automatic only for a *transverse* internal process; a general internal displacement need
not be ⊥ v." If (B), the exact-γ — and the velocity leg that forced c_photon ∝ C and thence R2 — rests on an
unjustified orthogonality.

## 1. The resolution — quadrature ≡ f_eff ≡ energy-bridge (one object, three faces)

The decisive fact is already in SR-1, in the very appendix that looked like it would *block* a geometric
quadrature. **Appendix H (Geometric Insufficiency Theorem)** proves that no purely geometric displacement
model recovers exact γ on its own, and in doing so it **characterises the unique effective consumed
displacement fraction**:

    f_eff = 1 − 1/γ_SR        (SR-1 Appendix H; reviews-SR-1.md, v15 resolution)

The remaining (internal) budget is therefore 1 − f_eff = 1/γ. Now compare the three candidate budget splits:

| split | consumed | internal remainder | internal clock rate | exact γ? |
|---|---|---|---|---|
| LINEAR (collinear) | v/c | 1 − v/c | 1 − v/c | **no** |
| QUADRATURE (orthogonal) | 1 − √(1−v²/c²) | √(1−v²/c²) | √(1−v²/c²) = 1/γ | **yes** |
| SR-1 f_eff (App. H) | 1 − 1/γ | 1/γ | 1/γ | yes (by construction) |
| energy-bridge (Step 11) | — | 1/(1+kΔSSV) | 1/(1+kΔSSV) = 1/γ | yes (kΔSSV = γ−1) |

The quadrature remainder √(1−v²/c²), SR-1's f_eff remainder 1/γ, and the energy-bridge internal rate
1/(1+kΔSSV) are the **same number at every v** (verified to 1e-12 across v/c ∈ [0.01, 0.999]). They are not
three competing derivations; they are three descriptions of one object:

    QUADRATURE  ⟺  (1 − f_eff) = 1/γ  ⟺  1/(1+kΔSSV),   kΔSSV = γ − 1.

Algebraically the equivalence is forced: 1 − f_eff = √(1−v²/c²) ⟹ f_eff = 1 − 1/γ, which is exactly the
Appendix-H fraction. **The geometric quadrature IS the geometric face of f_eff = 1 − 1/γ.**

## 2. Why this answers (A) vs (B) honestly

- It is **not naked geometry**, so Appendix H is respected. Pure lattice geometry does not *by itself* tell
  you the consumption is quadrature rather than linear; that is precisely the content of the Geometric
  Insufficiency Theorem. We do **not** claim the orthogonality follows from geometry alone.
- It is **not a new assumption** either, so it is not a naked (B). The orthogonality is the geometric
  statement of f_eff = 1 − 1/γ — and f_eff is the SR-1 physical input that the A− external review already
  accepted as the *unique* consumed fraction rendering the framework internally consistent. The quadrature
  introduces **no premise beyond what SR-1 already commits to**.

So VTD-1 is **(A) forced — by reduction**: forced by the same energy-momentum-bridge / fixed-magnitude
4-displacement input that SR-1 already invokes and Appendix H already proves is necessary and sufficient.
The "missing machinery" the 2024 patch flagged ("why orthogonal?") is supplied: orthogonality = f_eff.

## 3. The handover's specific worry, dissolved

"A general internal displacement need not be ⊥ v." Correct — and it does not need to be. What is required is
that the **effective consumed fraction** equal f_eff = 1 − 1/γ, not that every internal motion be transverse.
Appendix H establishes that f_eff (not the linear v/c) is the unique fraction consistent with the framework;
the quadrature is simply the magnitude statement of that fraction. Equivalently, in the fixed-magnitude
4-displacement reading (the CPP analogue of the invariant 4-velocity U·U = c²), the bulk velocity rotates a
fixed-magnitude-l_P 4-displacement from timelike toward spatial, and the orthogonal-complement **magnitude**
left for the internal/timelike advance is l_P√(1−v²/c²) **regardless of where in the complement the internal
process points**. Orientation-independence of the remainder magnitude is the geometric content; f_eff is its
already-accepted physical license.

## 4. Honest standing — what VTD-1 PASS does and does not buy

- **VTD-1: PASS (conditional).** The quadrature is forced as the geometric encoding of SR-1's f_eff = 1−1/γ.
  It adds **no new gap**: it inherits exactly the status of SR-1's energy-momentum bridge — a *physical
  identification*, panel-accepted (A− review), not a geometric theorem. That the bridge is an identification
  and not a geometric consequence is a known, documented feature of SR-1 (Appendix H exists *to say so*), not
  a fresh VTD-1 weakness.
- **What it does NOT buy:** it does not upgrade the bridge to a from-geometry derivation. If one demands that
  f_eff itself be *derived* rather than *identified*, that demand falls on SR-1 Appendix A.8.1/H, not on VTD-1
  — and it is the same demand for rest-frame SR-1, already adjudicated. VTD-1 does not reopen it.
- **Consequence for R2:** the velocity leg (moving frame = exact Lorentz boost ⇒ c_photon ∝ C via the
  unified budget) rests on **the same footing as published SR-1 — no weaker.** VTD-1 therefore clears its R2
  gate at the strength SR-1 already carries. (R2's *own* residual remains OPEN-SR-9, the EM-emergence /
  ΔSSV↔C construction — untouched by VTD-1, which is upstream of it.)

## 5. The one founder-adjudication hook (for TLA, mechanism-level)

The reduction routes VTD-1 through f_eff = 1 − 1/γ, i.e. through the reading that **bulk velocity's budget
cost is the quadrature fraction** (the 4-displacement magnitude is the invariant; velocity rotates it,
timelike→spatial), the CPP analogue of invariant 4-velocity. SR-1 Appendix H already commits to this f_eff,
so this should be a **confirm**, not new physics — but it is a mechanism statement about the PCD /
Absolute-Moment partition, and TLA owns that. Precise question for the founder:

> Is the bulk-velocity budget cost the **quadrature** fraction f_eff = 1 − 1/γ (fixed-magnitude
> 4-displacement, velocity rotates timelike→spatial), consistent with SR-1 Appendix H — and **not** a
> separate linear/collinear consumption? Confirm, and VTD-1 PASS stands at SR-1 strength.

## 6. Definition-of-done check (against VTD-1_handover §7)

Outcome (A) was reached **without forcing it**: not "geometry proves orthogonality" (that would violate
Appendix H and would be the dishonest force), but "orthogonality = f_eff, an input SR-1 already owns." The
FAIL branch (B) was genuinely available and is **not** what the mechanism gives: the linear split is
falsified (it is not 1/γ), and the orthogonal split is licensed by an existing, panel-accepted fraction
rather than by fiat. NO THEO — no new axiom, term, or counted prediction; all claims conditional; owned
greenfield path.

---

### Proposed for integrator (do NOT let a window edit these — batched registry/cross-file)

1. `mu_eps_closure/R2-STATUS.md` (or `MISSING-MACHINERY-FOUND.md` gate line): VTD-1 conditional-PASS →
   **PASS by reduction to SR-1 f_eff**; residual hook = founder confirm of the quadrature reading (§5), not a
   new derivation. R2's live residual stays OPEN-SR-9 (EM-emergence), unchanged.
2. `frontier_sectors/SR.md` / `CONJ.md`: note VTD-1 closed at SR-1 strength; it does not weaken or strengthen
   R2 beyond SR-1's existing footing.
3. No `theorem-registry.md` / `predictions.md` edit (NO THEO; conditional finding, frontier-tracked).
