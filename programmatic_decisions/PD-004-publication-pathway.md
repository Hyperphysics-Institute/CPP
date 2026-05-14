# PD-004: Publication Pathway and Layered Rollout Strategy

**Date:** 14 May 2026
**Session:** SF-2 v0.7 + Companion v1.3 review cycle (post ChatGPT v1.3 pair review)
**Status:** Adopted as programme-wide publication-sequencing guidance for external rollout.
**Scope:** Programme-wide — governs the sequencing and framing of CPP papers when presented to external audiences (arXiv, peer-reviewed venues, conference proceedings, anthology).
**Origin:** ChatGPT external review of SF-2 main paper v0.7 + Companion v1.3 (14 May 2026), specifically the "Best publication path" recommendation.
**Companion artifacts:**
- `Research_Frontier.md` (programme-wide problem registry)
- `paper_catalog.md` (per-paper version + status tracking)
- `flagship_papers/*/README.md` (per-flagship status headers)

---

## Context

During the multi-reviewer cycle on SF-2 v1.3 pair (ChatGPT, Copilot, Grok), ChatGPT delivered a strategic recommendation distinct from the textual / rigor critiques: a recommended publication pathway for how CPP papers should be rolled out externally to maximize professional reception.

The recommendation arose specifically because ChatGPT identified that SF-2 + Companion, while substantively strong, sits at the *intersection* of multiple research postures (mathematical geometry, symmetry classification, discrete-substrate phenomenology, exploratory pre-continuum unification). Presenting it as a single "completed theory of electroweak unification" would invite immediate rejection on the unresolved continuum-EFT bridge alone. Presenting it as one node in a layered research programme makes each layer separately defensible.

This PD captures that recommendation as durable programme strategy.

## The recommended publication pathway

ChatGPT's "Best publication path" identifies five strategic layers, ordered by how externally defensible each is:

### Layer 1: Mathematical-combinatorial geometry papers

These papers present 600-cell, $H_4$, binary icosahedral, and related polytope/group structure results as **standalone mathematical contributions** — independent of any physics interpretation. They are defensible to a discrete-mathematics audience on pure mathematical content.

**Current programme exemplars:**
- SS-1: Binary icosahedral group $\Gamma$ structure
- SS-4: String tension from polytope geometry
- SS-9: Polyhedron's conditions (Steinitz / FvdW classification bridge)
- Foundational shell-classification theorems in SF-2 §3 + §4 (W bracelet, Z icosahedron, H dodecahedron, mass-gap)

**Strategic value:** These contributions are externally legitimate as discrete-mathematics work *regardless* of the physics interpretation. A reviewer who is skeptical of CPP-as-physics can still validate the polytope-theoretic content.

### Layer 2: Symmetry / orbit classification papers

These papers present orbit classification results (e.g., the W bracelet's 1200-orbit under $H_4$ action, the unique-orbit-of-maximum-stabilizer arguments) as **symmetry-mathematical results**. They build on Layer 1 but add representation-theoretic content.

**Current programme exemplars:**
- SM-1: Standard Model particle taxonomy from 600-cell cage stability
- SM-3: K3 spectral theorem
- SF-2 §4 cage-shape theorems (the W bracelet orbit argument is the cleanest example)

**Strategic value:** Symmetry-classification work is the layer most readily defensible to mathematical physicists familiar with finite-group methods. ChatGPT identified the W bracelet orbit argument specifically as a "real conceptual upgrade" from "we chose a hexagon" to "the symmetry structure forces a distinguished orbit class."

### Layer 3: Discrete substrate phenomenology

These papers present **physical predictions** from the discrete substrate, with the rigor explicitly bounded at "discrete-substrate phenomenology" rather than "completed quantum field theory." This is where most of the empirical content lives.

**Current programme exemplars:**
- SS-7: Eight nuclei in a row (alpha-conjugate B/A predictions)
- SS-8: Octahedron in magnesium (³⁶Ar / ⁴⁰Ca cluster predictions)
- SM-8: Symmetry Degeneracy Theorem + quark mass spectrum
- SM-9: Top quark mass at 0.02% from cage cooperative SSV reinforcement
- SF-4: Neutrino sector (7 of 8 zero-parameter predictions)
- SF-2 mass-formula content (§10): calibrated mass values

**Strategic value:** Phenomenological match is empirically falsifiable. ChatGPT explicitly identified pattern-strength at integer counts and substrate primitives as the load-bearing signal across the corpus (SS-7's twelve nuclei to 1.5%, SM-9's top quark to 0.02%, SF-4's $\sigma_\nu = z^{-10}$ to 2%).

### Layer 4: Separate continuum-limit development papers

These papers develop the **continuum-EFT bridge** as a dedicated mathematical-physics problem, independent of any specific phenomenology. The challenge: showing that the discrete substrate, local update dynamics, and stabilizer structures can produce Lorentz invariance, renormalizable gauge structure, locality, causal propagation, and correct quantum amplitudes in a mathematically controlled limit.

**Current programme state:** This work does *not yet exist* as a dedicated paper. The proof-outline content in SF-2 §8.3 (Theorem 8.3, Yang-Mills EFT emergence) is the current best statement, but the full continuum derivation is registered as future work.

**Strategic value:** This is the single biggest reality constraint on CPP-as-physics. Without continuum-limit work, the framework remains "geometric phenomenology, not a completed physical theory" (ChatGPT). With it, the bridge between Layer 3 phenomenology and standard QFT is established. Dedicated papers are required — this cannot be folded into flagship phenomenology papers.

### Layer 5: Eventual EFT bridge work

These papers complete the chain: continuum-limit derivation (Layer 4) connects to Standard Model EFT structure with explicit Lagrangian matching, propagator structure, renormalization scheme matching, and one-loop verification. This is where the framework either becomes externally validated as a derivation of Standard Model structure or fails the bridge.

**Current programme state:** None yet. Sequence: Layer 4 must establish before Layer 5 becomes tractable.

**Strategic value:** Successful Layer 5 work would be the strongest possible external validation. Failed Layer 5 work would be a clean falsification of the framework. Both outcomes are scientifically valuable.

## Programme-strategic implications

### What this guidance does NOT recommend

The pathway is *layered*, not *sequential-in-time*. Programme work continues across all five layers in parallel; the recommendation governs **how each paper is framed and presented externally**, not the order of internal development.

Specifically, the recommendation is *not*:
- "Stop work on flagship papers until Layer 1 is published" — Layer 1 mathematical results are already embedded in SF-2 §3 + §4, SS-9, etc.
- "Do not publish phenomenology before continuum bridge" — phenomenology stands on its own as Layer 3
- "Hold SF-2 until SF-line is complete" — SF-2 + Companion at v1.3 are SHIP-ready as Layer 3 work

### What this guidance DOES recommend

Each paper's framing language and abstract positioning should reflect *which layer the paper occupies*. SF-2 should be framed as Layer 2 + Layer 3 work (symmetry classification + discrete substrate phenomenology), not as Layer 5 (completed EFT derivation). The Companion v1.3 sensitivity-scan content explicitly identifies Layer 4 work (continuum-EFT derivation) as future work — this is the appropriate Layer positioning.

### Implications for SF-2 + Companion v1.0 SHIP

Per this PD, SF-2 v0.8 (post-Patch 0367 polish) + Companion v1.4 should explicitly position themselves as:

> "A discrete-substrate research program for the electroweak sector, providing symmetry-orbit cage-shape theorems for the four cage bosons, a $W^0$ catalyst framework for the activated $W^{\pm}$, a Weinberg-angle numerical correspondence emerging from spectral trace structure, and a calibrated mass-formula partial closure. The framework provides a discrete-structure modeling architecture for the electroweak sector at Layer 2 (symmetry classification) and Layer 3 (substrate phenomenology); the continuum-EFT bridge (Layer 4) is registered as proof-outline future work."

This framing is defensible across all three reviewer audiences (ChatGPT, Copilot, Grok have all converged on this positioning).

### Implications for future flagship papers

Each future SF-line flagship (SF-3 quarks, SF-5 strong unification, SF-6 EM unification, SF-7 grand unification) should similarly identify its Layer occupation in the §1 positioning paragraph. Mixed-Layer papers (typical) should make the Layer mix explicit.

### Implications for the eventual continuum-EFT paper

Per ChatGPT v1.3 review: continuum-EFT derivation is registered as proof-outline in SF-2 §8.3 with Theorem 8.3. Full derivation should be a **dedicated paper** (likely named SF-2-CL or similar; alternatively a standalone paper in a new SL series for "Substrate Limits"). This paper should *only* contain Layer 4 content, with the bridge to Layer 5 (Standard Model EFT matching) deferred to a later paper.

This sequencing makes each paper individually evaluable, reduces the cognitive load per paper for external reviewers, and prevents "single monolithic theory of everything" framing that ChatGPT explicitly flagged as a rejection trigger.

## Reflexive observation

ChatGPT's recommendation matches the programme's existing corpus structure essentially perfectly: SS-line for strong-sector mathematics (Layer 1-2), SM-line for taxonomy and predictions (Layer 2-3), SF-line for flagship phenomenological synthesis (Layer 3, occasionally crossing into Layer 2). The recommendation is therefore not "restructure the programme" but "make the layering explicit in framing language and abstract positioning."

This PD codifies that observation: the programme's de facto layering is now explicit programme strategy, with externally-facing framing aligned accordingly.

## Status tracking

When a new paper is drafted, the author identifies which Layer(s) it occupies in the v0.1 §1.4 positioning paragraph. This information feeds into:

- `paper_catalog.md` row (new "Layer" column proposed for next paper_catalog refresh)
- `flagship_papers/*/README.md` status headers
- v1.0 SHIP abstract language

## Future revision

This PD captures ChatGPT's recommendation as of 14 May 2026 in the context of SF-2 v1.3 pair review. Future external reviewers (peer-review, arXiv comments, conference reception) may refine or extend the layering. This PD is durable strategic guidance, not a one-time decision; subsequent external feedback that suggests refinement should be folded in as PD-004 revisions.

---

**Maintainer:** Thomas Lee Abshier ND, Hyperphysics Institute
**Adopted by:** Patch 0367 (14 May 2026)
**Origin:** ChatGPT v1.3 review of SF-2 main paper v0.7 + Companion v1.3, "Best publication path" recommendation.
