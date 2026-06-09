# Residual 1 (the decisive one): the Effective η Order Parameter — Short-Range, and NO Candidate Mode Orders

**Patch:** 0821 (Session 156, 8 June 2026) · **Type:** infrastructure result (chirality residual 1) · **Lane:** F.1 / `dynamical_substrate_law/` (verdict stays chirality-lane / DG-3).
**Answers:** chirality-lane residual 1 (0909) — "confirm Mechanism A's coarse-grained slow/order-parameter mode is the 12-neighbour vertex-figure η," the single spot flagged as possibly needing PCD insight.
**Verify:** `code/0821_residual1_eta_identity.py`. **Predecessors:** 0819 (K_lift reduction), 0820 (coarse-graining probe).

---

## What residual 1 needed

The verdict was reduced (0819) to the η-identity: which effective η-field the dynamics produces (full-vertex-figure → primitive; more-local → emergent, crossover at the abstract-model `m≈8`). Residual 1 is to confirm the dynamical order-parameter mode is the vertex-figure η — or find it bottoms out at the PCD layer.

I attacked it two ways on the real (Mechanism-A; bias + edge-field) measure, computing the **full η-field connected correlator** rather than a single pair.

## Result — residual 1 closes mechanically, and more robustly than required

**1a — Locality.** For the canonical vertex-figure η (m=12), the connected correlator vs graph distance is **nearest-neighbour only**: `d=1: −0.053`, `d=2: +0.0004`, `d=3: ≈0` (decay `d2/d1 ≈ 0.01`). So the effective η-theory is a **short-range (nearest-neighbour) coupling model** → the order parameter is the **local vertex-figure η**, with no non-local or hidden long-range structure. The coarse-grained slow mode is the magnetization of this local η.

**2b — No candidate mode orders (the stronger result).** Scanning candidate local η-modes — support `m ∈ {4,6,8,12}` × three independent orientation frames — **every** mode gives `|K_lift|/K_c ∈ [0.50, 0.64]`, i.e. **all sub-critical, max `K_lift ≈ 0.053 < K_c = 1/12`**. So the verdict-lean (no ordering → primitive) is **robust to the η-identity ambiguity that was residual 1's whole concern**: whichever local η the dynamics selects, none of the candidate modes condenses.

This **refutes the "more-local → emergent" escape**: 0819's abstract arcsin model put small-`m` modes super-critical (`m=4 → 1.95 K_c`), but the explicit geometric pseudoscalar gives `m=4 → 0.50 K_c` — sub-critical. The arcsin model overestimated the small-`m` coupling (it assumed a coherent shared-edge contribution; the genuine geometric orientation-signs partially cancel it). *(This also corrects 0820's single-pair `m=4 ≈ 0` estimate, which was a pair-selection artifact; the full-correlator average is `≈ 0.50 K_c`.)*

## What this means

Residual 1 — the decisive residual, the one flagged as possibly needing the PCD layer — **closed by computation, without that layer.** And it closed in a form stronger than "dynamical = geometric η": *no candidate local η-mode is super-critical*, so the primitive lean does not even hinge on pinning the exact effective η. The coarse-graining yields a short-range local theory whose every plausible order-parameter mode sits at `0.5–0.64 K_c`.

## Honest caveats (this licenses no verdict yet)

- **The O(δ³) current (residual 2) is NOT in this measure.** This is the equilibrium/symmetric measure (bias + i.i.d. edge noise). Per 0907 §3, the current could shift the effective `K_c` down or drive *non-equilibrium* ordering the equilibrium correlator can't see. Residual 1 closing does **not** license the verdict; residual 2 must still clear. This is the next computation.
- **Mode scan is a sample,** not exhaustive — but the tight consistency (all `0.50–0.64`) across diverse frames/supports argues the sub-criticality is generic, not fine-tuned.
- **Mean-field `K_c`** (true higher → safer); **arcsin/Ising map** is mean-field-level (residual 3).
- Conditional on Mechanism A (OPEN-FP-F1-2).

## Scope held

Infrastructure (order-parameter locality + the no-ordering mode-scan). **No verdict moved** (V3/V1 stays chirality-lane, DG-3). No THEO, no ID, no CHIR.md / verdict-registry edits. Residual 1 reported closed-by-computation; residuals 2 (O(δ³) current) and 3 (true K_c) remain, per the chirality-lane spec (0907 §3–4).
