# B-iii — the η-field susceptibility symmetric-part form, and the honest stop at (H-NESS)

**Patch 1100 (Phase-0 parallel round, worker window W1). Stage-2 structural pass on the sign(μ²) verdict-mover, built on the Patch-0694 NESS construction. Computes the FORM of the symmetric-part η-field susceptibility (reachable, geometric) and demonstrates concretely that the SIGN bottoms out at the named gap (H-NESS). NO η-field measure built, NO sign(μ²) asserted, NO reserved-ID consumed, NO verdict move (V3/W3 stand). Conditional on Mechanism A (axiom, OPEN-FP-F1-2).**

**Scope.** Patch 0694 constructed and validated the single-walker Mechanism-A NESS π and mapped the four-stage pipeline to sign(μ²): (1) build π [done, 0694]; (2) define the local η-field + the symmetric-part susceptibility *form* [reachable]; (3) the connected susceptibility's *sign* [load-bearing, (H-NESS)-gated]; (4) extract sign(μ²) [review-gated]. This patch executes the reachable content of stage 2 — the symmetric-part *form* — and then probes stage 3 to the point it bottoms out, naming exactly where and why. It computes a form; it fixes no sign; it moves no verdict.

---

## §0 Firewall + anti-priorities (continues 0668/0679/0683/0684/0688/0689/0694)

1. **NO η-field fluctuation measure built, NO connected susceptibility value computed, NO sign(μ²) asserted.** The symmetric-part *form* is computed; the field mass m² that carries the sign is not supplied here.
2. **NO verdict move.** FI-C-9 stays **V3**; sign(δ) stays **W3**.
3. **NO new theorem ID, NO reserved-ID consumed.** THEO-CHIR-CAPACITY-1 stays **reserved/untouched**. Per the Session-151 anti-priority and the Landau-scoping DG-3, crystallizing a structural lemma that reduces a question to an undetermined sign is borderline-bookkeeping until the DSL can at least *constrain* sign(μ²); that bar is not met here, so the ID is not consumed. NO header count change. NO new programme-level Open-Problem (this is stage-2 of B-iii-(i)/0668).
4. **NO closed theorem reopened** (TARROW-1/2, VW-1/2, STATUS-1/2, BRIDGE-1, CAP-1, MERGE-1/2, the THEO-DSL stack, CONT-1/2/3); **no F.1 / DSL / OPEN-SM-4 / Capotauro source edited** — all *consumed*. BRIDGE-1's kinematic/P2 cap rides every cross-sector statement.
5. **Conditional on Mechanism A** (F.1 Axioms MA.1/MA.2, OPEN-FP-F1-2). Every downstream statement carries that conditionality.
6. **No fabricated field measure, no proxy presented as the verdict.** Following the 0684 §5.2 anti-erasure ruling ("I will NOT fabricate a measure or present an (H-SUSC)-contingent proxy as sign(μ²)"): a number assembled from the single-walker π is explicitly *not* labeled sign(μ²) here. The gap is demonstrated, not papered over.

---

## §1 The two reachable structural facts (stage 2)

**(A) The symmetric-part susceptibility is zero-mode dominated, and reduces the sign to one number.**
In the equilibrium-like (Gaussian) approximation valid where detailed balance survives — through O(δ²), the regime the symmetric part of π lives in (0694 §4) — the symmetric η-field measure has action
  S_sym = ½ Σ_{v,w} η_v (L + m²I)_{vw} η_w,
with **L the 600-cell graph Laplacian** (the "kinetic channel" of 0684 §3; L = 12I − A on 120 vertices, degree 12) and m² the η²-curvature itself (the field mass). The integrated connected susceptibility is then
  **χ_sym = Σ_{v,w} [(L + m²I)⁻¹]_{vw} = 1ᵀ(L + m²I)⁻¹1.**
Because L's zero mode is the constant vector (L·1 = 0, verified: ‖L·1‖ = 0; λ₀ = 0, spectral gap λ₁ = 2.2918, λ_max = 15.708), the all-ones contraction projects onto the zero mode exactly:
  **χ_sym = N/m²  (verified to machine precision for m² ∈ {0.05, 0.1, 0.5, 1, 2}; χ·m²/N = 1.00000000).**
Hence χ_sym⁻¹ = m²/N and
  **sign(μ²) = sign(χ_η⁻¹) = sign(m²).**
This is a genuine reduction: the symmetric-part *form* is fully reachable, and it collapses the entire sign bit to **sign(m²)**, the field mass term — independent of the O(δ³) current correction (which can only *perturb* a sign the symmetric part fixes, per 0694 §4, unless the symmetric susceptibility is marginal/divergent — which N/m² is not, for m²>0).

**(B) The current-part contribution is subdominant by the established scaling.** The symmetric part is O(δ⁰–δ²); the current part is O(δ³) (0689/0694, current onset slope 3.000). So the current part is sign-*perturbing*, not sign-*setting*, wherever the symmetric m² is nonzero — consistent with the 0694 §4 expectation. The honest open question is therefore entirely **sign(m²)**.

---

## §2 Where it bottoms out, named precisely: (H-NESS)

The reduction in §1 makes the residual sharper than 0694 left it: the verdict bit is **sign(m²)**, the curvature of the η-FIELD effective potential. The constructed object π is the **single-walker** stationary measure — a probability distribution over *one* walker's vertex position, a 1-point marginal on 120 states. **It does not contain the η-field two-point function**, and therefore does not supply m².

This is demonstrated concretely (CHECK 4): the only off-diagonal connected correlator a single walker affords is the single-occupancy artifact
  ⟨n_v n_w⟩_c = ⟨n_v n_w⟩ − ⟨n_v⟩⟨n_w⟩ = 0 − π_vπ_w = −π_vπ_w  (v ≠ w),
which is **sign-definite negative by the one-walker-can't-be-in-two-places constraint and carries no m² at all**. A susceptibility assembled from π alone measures the occupancy constraint, not the chiral curvature. Presenting it as sign(μ²) would be exactly the proxy-as-verdict overclaim the firewall forbids.

> **(H-NESS) [carried from 0694 §5, now localized to m²]:** the η-curvature m² of the coarse-grained chiral order-parameter field's effective potential is recoverable from the single-walker Mechanism-A stationary measure π. Bridging π → m² requires **either (i)** an occupation/many-walker lift of Mechanism A — a *new* generator on η-field configurations, whose stationary measure is a measure over η-configurations (constructing it is introducing new machinery / a new mechanism) — **or (ii)** a justified single-site reduction asserting π's η-moments equal the field's (which is the H-NESS hypothesis itself, not a derivation). **Neither is available without inventing machinery.**

Per the round's escalation rule, I do not invent either. **STOP here.**

---

## §3 Inputs consumed
0694 (the NESS π construction + the four-stage pipeline + the (H-NESS) naming; `code/setup_ness_stationary_measure.py` reused for π); 0684 (the Landau identity sign(μ²)=sign(χ_η⁻¹); the kinetic-channel/graph-Laplacian framing; the anti-erasure ruling); 0689 (O(δ³) detailed-balance violation, current onset); TARROW-2 v1.1 (the NESS reframe, review-closed 3/3); STATUS-2 (η = ℤ₂-even det-coset label); B-iii/0668 (capacity ⟺ sign(μ²)); F.1 DSL (Mechanism A, OPEN-FP-F1-2).

---

## §4 Verdict + disposition
The symmetric-part susceptibility *form* is now in hand and clean — χ_sym = N/m², zero-mode dominated, reducing the verdict bit to **sign(m²)**. The residual (H-NESS) is correspondingly sharpened from "lift π to the η-field measure" to the still-unbridged "supply m² from π (or build the occupation-field lift)." **No invention was made; no sign was computed; no theorem was registered; the verdict stands — V3/W3.** This patch is a stage-2 structural advance plus an honest escalation stop, not a closure.

---

## §5 Honest caps + falsifiers
**Caps:** (a) the symmetric-part *form* is computed; m² and hence the sign are NOT; (b) the Gaussian/equilibrium-like action for S_sym is the natural symmetric-part model (the 0684 kinetic channel), not a derived field theory — a stronger derivation would itself require the field measure; (c) single-walker π carries no field two-point function (CHECK 4); (d) conditional on Mechanism A; (e) finite-600-cell caveat (block-spin/CONT-1 trend the honest continuum statement); (f) **NO verdict move — V3/W3 stand.**
**Falsifiers (route-map, not verdict):** (N1) if an occupation-field lift is built and its stationary measure yields a determinate m² — stage 3 sign becomes reachable (review-gated, major); (N2) if a single-site reduction is *justified* (H-NESS (ii) true) — likewise; (N3) if the symmetric action's m² is provably forced negative by some consumed result — would open V3→V1 (none does); (N4) if χ_sym were marginal/divergent rather than N/m² — would promote the O(δ³) current to sign-determining (it is not: χ_sym = N/m² is finite for m²>0).

---

## §6 Next (Thomas's choice)
1. **Attack (H-NESS) route (i):** build the occupation/many-walker lift of Mechanism A and seek its stationary η-configuration measure — the load-bearing bridge, the only route that supplies m² without an unjustified reduction. *(Flagged: constructing the many-body generator is itself new machinery and should be scoped as such, not slipped in.)*
2. **Attack (H-NESS) route (ii):** seek a *justified* single-site reduction (when/why π's η-moments equal the field's) — if found, sign(m²) becomes reachable directly.
3. **Discharge OPEN-FP-F1-2** (derive Mechanism A from A1–A11) — Priority 2 — making every NESS statement unconditional.

**No verdict move — V3/W3 stand until a reviewed sign(m²) is returned.**

---

## §7 REGISTRY HANDOFF NOTE (for the integrator to batch — this patch touches NO shared file)
*W1 does not edit `frontier_sectors/CHIR.md` or `theorem-registry.md`. The following are the exact updates this result implies; the integrator applies them.*

- **`frontier_sectors/CHIR.md`** — append a changelog-style *Last updated* line (sub-corpus precedent: changelog-style, **NO `theorem-registry.md` body-table row**), Patch 1100, recording: symmetric-part η-susceptibility *form* computed — χ_sym = N/m² (graph-Laplacian zero-mode dominated; λ₁ = 2.2918) ⇒ **sign(μ²) = sign(m²)**; the O(δ³) current is sign-perturbing not sign-setting; the residual (H-NESS) is sharpened to "supply m² from π / build the occupation-field lift"; **NO η-field measure, NO sign, NO theorem, NO verdict move — FI-C-9 = V3, sign(δ) = W3 STAND; THEO-CHIR-CAPACITY-1 stays reserved/untouched; header count UNCHANGED; conditional on Mechanism A (OPEN-FP-F1-2).**
- **`theorem-registry.md`** — **no change** (chirality sub-corpus registers changelog-style in CHIR.md; no body-table row; no theorem crystallized).
- **Reserved-ID ledger** — THEO-CHIR-CAPACITY-1 remains **reserved** (still below the "DSL constrains sign(μ²)" crystallization bar; the reduction to sign(m²) sharpens but does not meet it).
- **No `frontier_sectors/` other-sector file, no axiom-registry, no header count** touched or implied.
