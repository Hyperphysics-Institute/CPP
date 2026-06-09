# What `sign(n̂)` Is, Where It Enters the Axioms, and How FI-C-9 Carries It — a Geometric Description

**Patch:** 0816 (Session 156, 8 June 2026) · **Type:** descriptive consolidation · **For:** the chirality lane (hand-off)
**Lane:** F.1 / `dynamical_substrate_law/` (geometry + axiom-map home; DSL-3 lives here).
**Verify:** `code/0816_signn_geometry.py` (shell structure + pseudoscalar character).
**Discipline:** **Descriptive only.** No verdict moved, no derivation, no FI-C-9 *re*definition — this consolidates existing established objects (STATUS-2, MERGE-2, CHI-1, CAP-1, DSL-3) into one geometric statement. The deep derivation question stays parked at §14.17; this does not touch it.

---

## Purpose

The chirality-lane review (0904) named the productive in-bounds task: *describe the existing primitive cleanly — what `sign(n̂)` is and exactly where it enters the axioms.* This is a first pass from the geometry side. It answers three things: **what** `sign(n̂)` is, **where** it enters the dynamical law, and **how** FI-C-9 carries it through the corpus.

## 1. What n̂ is (the direction) vs what `sign(n̂)` is (the orientation bit)

**n̂ — the substrate's primitive direction.** A unit 4-vector. In the vertex-aligned Reading C, n̂ points along a 600-cell vertex. Choosing it breaks the full symmetry group **H₄** (order 14400, *contains reflections*) down to the icosahedral stabilizer **H₃ = I_h** at the host vertex. The local neighbourhood of that breaking is the **two nearest shells**: the 12-vertex icosahedron (the vertex figure, at distance φ⁻¹) and the 20-vertex dodecahedron (its dual, at distance 1). This is the locus where CHI-1's magnitude χ = φ⁻³ arises, as the bias ratio of those two shells (0638). *n̂ as a direction is P-even and T-even.*

**`sign(n̂)` — the orientation pseudoscalar (= FI-C-9).** Fixing n̂ leaves a residual ℤ₂: the **H₄/H₄⁺ coset** (H₄⁺ = the rotation subgroup, order 7200; the coset is proper-vs-improper, i.e. the two enantiomorphs). `sign(n̂)` is the label of which coset element — concretely a **det-sign**: the orientation of the local frame at the n̂-vertex. It is **one ℤ₂ bit**, and it is **P-odd** (flips under a global reflection) and **T-even**. The verify script exhibits exactly this: a fixed local 4-frame gives `sign = +1`, and under a global reflection it flips to `−1`.

> The clean one-line distinction: **n̂ the arrow is P-even; its handedness bit `sign(n̂)` is the P-odd pseudoscalar — and *that bit* is FI-C-9.** (STATUS-2: order parameter of the H₄→H₄⁺ chain = `sign(n̂)`.)

## 2. Where it enters the axioms / the dynamical law

n̂ enters at the substrate-dynamics level, in three linked places:

| place | statement | role of n̂ / `sign(n̂)` | source |
|---|---|---|---|
| PCD angular velocity | `ω_PCD = σ · n̂` | σ is the orientation sign; n̂ the cycle axis | DSL-3 |
| Mechanism-A rate bias | `r(v→w) = r₀(1 + δ ê_vw·n̂)` | n̂ the bias direction; δ the magnitude | MA.1 |
| net DI current (arrow) | `j_DI = (6δ/φ²) n̂ + O(δ²)` | direction n̂; sign = `sign(δ)·sign(n̂)` | DSL-3 |

So the **direction** n̂ enters the Mechanism-A rate law and the PCD cycle axis; the **orientation bit** `sign(n̂)` is what σ carries in `ω_PCD = σ·n̂`. The arrow current's sign factorizes as **`sign(δ) · sign(n̂)` = (temporal arrow) × (spatial handedness)**.

**One honest subtlety in the actualization of the sign** (descriptive, *not* the §14.17 question): DSL-3 states that at Layer-3 rigor σ in `ω_PCD = σ·n̂` is *a framework convention* — the two sign choices are time-reversal-symmetric framings, physical only once coupled to the F.2 Wigner–Eckart datum. So the bridge "the cycle orientation σ *equals* the geometric `sign(n̂)`" is **M3-undetermined** (MERGE-β, 0644), gated on (i) the F.2 coupling that makes σ physical and (ii) the Layer-4 Mechanism-A derivation that ties `sign(δ)`. This is a description of where the *physical* sign is pinned, distinct from the V3→V1 derivation gate.

## 3. How FI-C-9 carries it through the corpus

FI-C-9 = `sign(n̂)` is the **single spatial chirality primitive** everything reduces to, and it is **consumed (used as input), not derived**, by:

- **MERGE-2** — reduces *all* chirality to FI-C-9 + the time-arrow `sign(δ)`. FI-C-9 is the spatial half.
- **CHI-1** — supplies the **magnitude** χ = φ⁻³ (the two-nearest-shell bias ratio). FI-C-9 is the **sign**; CHI-1 is the modulus; together they are the chiral bias `δ ê·n̂`. (Sign ⊗ magnitude split.)
- **CAP-1** — **capture handedness = involution × FI-C-9**: the DP spin-capture handedness is FI-C-9 times a fixed involution, i.e. FI-C-9 propagates into the capture sector.

Parity/time bookkeeping (consolidated, for the lane's convenience):

| object | P | T | what it is |
|---|---|---|---|
| n̂ (direction) | even | even | the primitive axis |
| **`sign(n̂)` = FI-C-9** | **odd** | even | the spatial handedness bit (pseudoscalar) |
| δ (bias magnitude / arrow param) | even | odd | the time-arrow parameter |
| j_DI (arrow current) | — | odd | sign = `sign(δ)·sign(n̂)` |

## 4. Where `sign(n̂)` is actualized (the question behind the question)

`sign(n̂)` is **a boundary condition, not a dynamical output.** The substrate's primitive direction n̂ — and with it the orientation bit — is **selected from the degenerate orientation manifold at some cosmological epoch** (the n̂-fixing closure question, manifestation (v) of the substrate-chirality inventory). The recent Steps 1–2 result is consistent with exactly this reading: μ² > 0 means the engine is handedness-*neutral* (it does not condense a net η), so the handedness is **not** manufactured by the dynamics — it has to live in the primitive, and FI-C-9 is where it lives. From there it is broadcast into the physics through `ω_PCD = σ·n̂`, the Mechanism-A bias, capture handedness (CAP-1), and the chiral magnitude (CHI-1).

So the honest picture: the world *is* handed at the level of FI-C-9 = `sign(n̂)`, a single P-odd ℤ₂ bit fixed as a cosmological boundary condition; the engine carries that bit rather than creating it; and "deriving chirality" (V3→V1) would mean showing the engine *creates* it instead — the parked §14.17 question, untouched here.

## Scope held

Descriptive consolidation only. No verdict moved (V3/W3 stand). No THEO, no ID, no `sign(n̂)`/FI-C-9 redefinition — every object cited is pre-existing (STATUS-2 0654, MERGE-2 0647, CHI-1 0638, CAP-1 0640, DSL-3, MERGE-β 0644). No CHIR.md / chirality verdict-registry edits. Handed to the chirality lane for use/integration. The M3-undetermined sign-bridge and §14.17 derivation both remain open exactly as before.
