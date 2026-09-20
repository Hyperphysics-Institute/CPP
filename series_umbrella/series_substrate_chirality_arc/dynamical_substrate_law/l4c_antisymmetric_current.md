# 0941 — L4-C of OPEN-FP-F1-2: MA.2's antisymmetric current construction derived from the PCD cycle

**Lane:** chirality (09xx). **Patch:** 0941, 13 Sep 2026. **Layer:** 3 (structural derivation from A6′ + A11 + L4-B; publication-grade candidate, single pass, no panel). **Verify:** `code/0941_l4c_antisymmetric_current.py` (8/8). **Reasoning fragment:** `documentation_suite/reasoning-0941.md`.

**Target.** L4-C of the OPEN-FP-F1-2 decomposition (Patch 0646): derive MA.2's antisymmetric first-shell current construction from A1 + A6′ Displace-phase dynamics. MA.2 posits

  j_net(v) = Σ_{ê ∈ E₁(v)} [ r(ê; v) − r(−ê; v) ] ê + O(δ²).

Three commitments sit in that line: (i) the sum runs over the first shell only — already THEO-DSL-1 (perturbation-locality), not re-derived here; (ii) the rate enters in the **antisymmetric** combination r(ê) − r(−ê); (iii) each term is weighted by the unit direction ê. L4-C is (ii) and (iii).

**Result.** Both are forced by the Perceive/Displace split of A6′ together with L4-B's vertex-uniformity. Neither is an ansatz. And the derivation returns F.1 Theorem 7.1's structural constant α₁ = 6/φ² without being told it.

## 1. The difficulty: −ê is not an edge

At a 600-cell vertex the twelve first-shell directions all sit at û·n̂ = −1/(2φ) (F.1 Theorem 5.1). The set is therefore **not centrally symmetric** — for every one of the twelve û, the direction −û is not a first-shell direction at v at all (T2). Nor do they cancel: Σû = −(6/φ) n̂, a vector of length 3.708 (T3).

So MA.2's "r(−ê; v)" cannot be read as *the rate along the opposite edge at v*. There is no such edge. Read that way the axiom is ill-posed, and the reading matters, because the naive symmetric alternative Σ r(ê) ê produces at δ = 0 a current −r₀(6/φ) n̂ (T4): a net substrate flow in a substrate with **no perturbation in it**. Any construction that permits that is wrong on physical grounds before any parameter is fixed.

## 2. The PCD reading, which repairs it

Per Absolute Moment (A6′ / A1′ division of labour): the **GP** at v runs **Perceive** — integrating DI-bit *arrivals* — then **Compute**, refreshing V_i; the **CP** executes **Displace** along the V_i its GP computed. The net flux at v is therefore *departures minus arrivals*, counted edge by edge.

Every first-shell edge {v, w} carries both. The departure is imprinted at v and travels along û. The arrival is imprinted at **w**, and its direction of travel seen at v is exactly −û. Its rate is the rate law evaluated **at w** — and by **L4-B (Patch 0940)** w carries the same r₀ and the same δ as v, so that rate is r₀(1 + δ (−û)·n̂) = r(−û) (T5, checked at all 120 vertices, not only v_host).

So `r(−ê; v)` denotes **the reverse traversal of the same edge, governed by the same law at the other end** — not a missing edge at v. Given that reading, departures-minus-arrivals *is* Σ [r(û) − r(−û)] û, with the weighting by û being nothing more than the vector bookkeeping of a flux along a direction. **Commitments (ii) and (iii) are consequences, not choices.**

## 3. Two things that fall out

- **The isotropic r₀ cancels identically**, at every vertex (T6). It has to: the r₀ part is direction-blind, so departures and arrivals match edge by edge. This is exactly what removes the spurious δ = 0 current of §1 — the antisymmetric construction is the one that does not manufacture a current from nothing. The non-central-symmetry of the edge set, which looked like an obstruction, is the reason the antisymmetry is load-bearing rather than cosmetic.
- **α₁ = 6/φ² is recovered.** The surviving first-order current is 2 r₀ δ Σ (û·n̂) û = (6/φ²) r₀ δ n̂, parallel to n̂ to machine precision (T7). F.1 Theorem 7.1's structural constant comes out of the PCD bookkeeping rather than being imported. This is a consistency check on the derivation, not a new result.

## 4. L4-C rests on L4-B, and that is checked

Deny vertex-uniformity at a single neighbour — give w its own r₀ — and the arrival rate is no longer r(−û), the T5 identity fails, and the δ = 0 current reopens (T8). So the two sub-targets are not independent: L4-C's derivation consumes L4-B's result. Recorded because the 0646 decomposition lists them as parallel items, which they are not.

## 5. Status and scope

- **L4-C discharged** at Layer 3 from A6′ (PCD) + A11 + L4-B + THEO-DSL-1 (for the first-shell restriction, inherited not re-derived). No F.2, no new axiom, no circularity: nothing in the argument uses Mechanism A.
- **Mechanism A is still not discharged.** **L4-A** — MA.1's rate-law *form* (linearity in ê·n̂, a single scalar δ, no O(δ⁰) tangent term), by representation-theoretic uniqueness from A1 + A6′ — remains open and is the last F.2-free piece. **L4-E** (the δ–ε magnitude relation) remains open, low priority. **V3/W3 therefore stay conditional on Mechanism A.**
- **Registry unit.** With L4-B and L4-C both in hand, the natural theorem-registry candidacy is L4-A + L4-B + L4-C jointly, once L4-A lands. Not registered here.
- **Owed to F.1** (paper wording, not a number): §4.3 should state what `r(−ê; v)` denotes — the reverse traversal governed by the law at the far end, which requires vertex-uniformity — since the literal reading has no referent at v. Bundles with the §4.3 correction already owed from 0940. Exclusion class E1 narrows again: of Mechanism A's four framework commitments, vertex-uniformity (0940) and the current construction (this patch) are now derived; the rate-law form is not.

**No verdict moves.** V3/W3 stand; THEO-CHIR-CAPACITY-1 untouched; no THEO/ID/prediction; header counts unchanged.
