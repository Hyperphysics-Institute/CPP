# 0949 — L4-A of OPEN-FP-F1-2: what the primitives force about MA.1's form, what they permit, and what remains framework input

**Lane:** chirality (09xx). **Patch:** 0949, 13 Sep 2026. **Layer:** 3 (representation-theoretic derivation from A11 + H₄-covariance + the single primitive n̂; publication-grade candidate, single pass, no panel). **Verify:** `code/0949_l4a_rate_law_form.py` (8/8 — the vertex stabiliser, the directed-edge stabiliser, its fixed subspaces in R⁴ and Sym²(R⁴), the current, and the detailed-balance ratio are all constructed from the lattice). **Reasoning fragment:** `documentation_suite/reasoning-0949.md`.

**Target.** L4-A: derive MA.1's rate-law *form* — `r(ê; v) = r₀(1 + δ ê·n̂)` — from the primitives by representation-theoretic uniqueness. MA.1 makes three commitments: **(i)** linear in ê·n̂, "exact at the framework level"; **(ii)** a single scalar δ; **(iii)** no O(δ⁰) tangent term.

**Result in one line.** Representation theory forces (iii), forces the *reversal-odd* part of (i)+(ii) uniquely, and does **not** force the rest. The part it forces is exactly the part everything at O(δ¹) consumes. The part it does not force is consumed only by the NESS-based results at O(δ³). So Mechanism A's conditionality does not lift; it **narrows** to a residual that can now be named in one sentence.

---

## 1. Method

A rate law is a function on the **directed edges** (v, ê) of the 600-cell that depends on the primitive n̂, and H₄-covariance means `r(gv, gê; gn̂) = r(v, ê; n̂)`. Expand in harmonics of n̂: the O(n̂⁰) part is an H₄-invariant function on directed edges; the O(n̂¹) part is `c(v,ê)·n̂` with c an H₄-*equivariant* vector field; the O(n̂²) part is `n̂ᵀT(v,ê)n̂` with T an equivariant symmetric-tensor field. On a transitive action, Frobenius reciprocity makes each of these spaces as large as the number of **invariants of the directed-edge stabiliser S** in the corresponding representation. So the whole question reduces to computing S and its fixed subspaces.

## 2. What is forced

**O(δ⁰) — commitment (iii) is derived.** The vertex stabiliser is transitive on the twelve first-shell directions, and the substrate is vertex-transitive (0940 T2), so H₄ is **arc-transitive**: one orbit on all 1,440 directed edges (T1). An H₄-invariant function on one orbit is a constant. The unperturbed rate is a single r₀ with no tangent structure whatsoever. There was never room for an O(δ⁰) tangent term.

**O(δ¹) — the reversal-odd form is unique.** The directed-edge stabiliser S has order 10 = 14400/1440, element orders {1, 2, 5} — C₅v — and its fixed subspace in R⁴ is **exactly span{v, w}**, dimension 2 (T2). So the most general first-harmonic rate perturbation is a **two-parameter** family,

  r₁(v, ê) = A (m·n̂) + B (ê·n̂),  m = (v+w)/2 the edge midpoint, ê the edge direction,

and under edge reversal (v,ê) → (w,−ê) the m-term is **even** and the ê-term is **odd** (T3). The reversal-odd part is one-dimensional: **B ê·n̂, unique up to scale.** That is MA.1's form. It is the unique reversal-odd first-harmonic H₄-covariant on directed edges.

**And the reversal-odd part is all that O(δ¹) physics sees.** The reversal-even term A m·n̂ cancels *identically* in MA.2's antisymmetric current construction, at every one of the 120 vertices, for arbitrary A — reverse traversal has the same midpoint (T4). Theorem 7.1's α₁ = 6/φ² comes out unchanged with A = 0.5 in place (T4b). So the O(δ¹) current, the substrate-locality theorem, L4-C, and every downstream consumer at first order depend on B alone. **For that content, MA.1's "single scalar δ" is a theorem: δ ≡ B.**

## 3. What is permitted but not forced

Two things in MA.1 are framework input, and representation theory can say precisely which physics consumes them.

- **A = 0.** Nothing in the primitives kills the reversal-even midpoint term. It is invisible at O(δ¹), but it does **not** cancel in the detailed-balance ratio: `r(v→w)/r(w→v) = (r₀ + A m·n̂ + B ê·n̂)/(r₀ + A m·n̂ − B ê·n̂)`, whose effective tilt `B/(r₀ + A m·n̂)` is position-dependent and enters the stationary measure at O(AB) = O(δ²) (T5). So the NESS results — the π-construction of 0694, the μ²-sign form of 1100, the O(δ³) steady current, the TARROW-2 cross-check — **consume A = 0**.
- **Linearity "exact at the framework level."** The S-invariant subspace of Sym²(R⁴) has dimension 4 — three independent quadratic invariants beyond |n̂|² = 1 (T6). Quadratic (and higher) harmonics are representation-theoretically available. MA.1's exact linearity is a **truncation to the first harmonic**, and again it is consumed only beyond O(δ¹).

Neither residual is a defect in MA.1. Both are the kind of simplification a framework axiom is entitled to make; L4-A's job was to find out whether they were *forced*, and they are not.

## 4. A structural lead for L4-E (not its closure)

Reading C's edge-length perturbation `ℓ(ê) = ℓ₀(1 + ε ê·n̂)` is the **same** reversal-odd first-harmonic covariant. Under constant-speed traversal — one Displace per Absolute Moment at c (A6′) — rate = c/length, and the two forms map onto each other with **δ = −ε + O(ε²)** (T7). F.1 §"600-cell substrate at Reading C" states the δ–ε relation is "not pinned" and takes both as independent inputs. The representation theory says they cannot be independent *in form*; whether δ = −ε *in value* is L4-E's question and depends on whether the propagation speed is genuinely constant across perturbed edges. Filed as the lead.

## 5. Consequence for the arc's conditionality — narrowed, not lifted

Both arc verdicts are "conditional on Mechanism A" (CHIR.md; THEO-CHIR-CAPACITY-1 at 0927; the determination closure at 0903). After L4-B (0940), L4-C (0941) and this patch, that conditionality reads precisely:

> **conditional on MA.1 beyond its reversal-odd first harmonic** — i.e. on A = 0 (no reversal-even midpoint term) and on the absence of higher harmonics.

- Everything the arc consumes at **O(δ¹)** is derived: r₀ isotropy, the unique form B ê·n̂, vertex-uniformity of r₀ and B (0940), the antisymmetric current (0941), α₁ = 6/φ², the substrate-locality theorem.
- **W3** — the T-arrow as `sign(δ)` at STATUS level — is `sign(B)`, an O(δ¹) object. Its status is unaffected by the residual; its W1 *upgrade* runs through the NESS (0694/1100) and does consume it.
- **V3** — THEO-CHIR-CAPACITY-1 — is stated as conditional on "Mechanism A incl. per-edge independence + pointwise non-degeneracy." Per-edge independence holds for the full two-parameter family (m and ê are both properties of the edge). Whether CAPACITY-1's argument consumes the residual at all, or only per-edge independence and O(δ¹), is **not determined here** and should be re-read against the named residual by whoever holds 0927. If it consumes only the derived content, V3's Mechanism-A conditionality lifts. **Filed; not claimed.**

## 6. Disposition

- **L4-A discharged to the extent the primitives allow**, with the residual named: A = 0 and first-harmonic truncation, consumed only by NESS/O(δ³) results. Not a full discharge; a precise one.
- **OPEN-FP-F1-2 status:** all three F.2-free sub-targets (A, B, C) now have Layer-3 artifacts; the parent stays **OPEN** on the named residual and on L4-E. Mechanism A's four framework commitments: vertex-uniformity **derived** (0940), current construction **derived** (0941), O(δ⁰) isotropy **derived** (this patch), rate-law form **derived at first harmonic, residual named** (this patch).
- **Theorem candidacy.** "The reversal-odd first-harmonic H₄-covariant on directed edges of the 600-cell is one-dimensional, spanned by ê·n̂; the reversal-even part is spanned by m·n̂ and cancels in the antisymmetric current" is theorem-grade and is the natural registry unit for L4-A+B+C jointly. **Not registered here** — single pass, no panel; owed to a window that can run one (todolist).
- **Owed to F.1:** §4.3 should replace the "Layer 3 faith" framing of MA.1's form with the split above; the δ–ε "not pinned" sentence should note the forms are the same covariant. Bundles with the 0940/0941 wording items.
- **No verdict moves.** V3/W3 stand; CAPACITY-1 untouched; THEO-CHIR-MERGE-2 untouched. No THEO/ID/prediction registered.
