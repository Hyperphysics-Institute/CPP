# Problem History: FALS-C-SM-2 — φ^(3(l-1)) Quark Mass Scaling Falsified

**Created:** Pre-2026 (original proposal)
**Status:** FALS (falsified)
**Falsified:** March 2026 (PS-1 session)
**Research_Frontier.md entry:** FALS-C-SM-2

---

## The Problem

The quark mass hierarchy spans five orders of magnitude (m_u ≈ 2 MeV to m_t ≈ 173 GeV). The original CPP proposal was that each additional cage shell multiplied the mass contribution by φ³ ≈ 4.236, the golden-ratio volume scaling factor. This was elegant and natural — the 600-cell is built from φ, and volume scales as the cube of length.

---

## The Journey

### Pre-2026 — The Conjecture

The formula proposed in SS-1 and the `cpp_benchmark` notebook (v12):

M_q(n) ≈ M_inner + Σ_{l=1}^{n} E_DP(l) · φ^{3(l-1)}

This gives mass ratios 1 : 4.2 : 17.9 : 76 : 322 across 4 cage layers. The actual observed ratios are 1 : 44 : 577 : 1900 : 78527. The formula was "too mild" — but the direction was right, and the qualitative ordering was correct, which kept it alive as a working hypothesis.

### March 2026 (PS-1 Session) — Exact Shell Computation

During the PS-1 session (600-cell distance shell analysis), Opus computed the exact 3D-projected Voronoi volumes of all 600-cell shells using the full set of 120 vertex coordinates.

**The result that killed the conjecture:** The actual shell volumes do NOT follow φ^{3(l-1)}. The volumes peak at the equatorial shell and then DECREASE — they follow a palindromic structure: N = 12, 20, 12, 30, 12, 20, 12, 1.

The φ^{3(l-1)} prediction gives factors of 3–8× error in the structural masses. For the top quark, the error is ~10×. The scaling is not just imprecise — it is structurally wrong.

### 30 March 2026 — SC-1 Computation Confirms Failure

Solution candidate SC-1 (Grok's exact-volume + PSR + interference mass ladder) attempted to rescue the approach by using exact shell volumes instead of φ³ scaling. The phase cancellation factors C_n were computed exactly:

C₁ = 0.7247, C₂ = 0.2374, C₃ = 0.3563, C₄ = 0.0750

**The structural impossibility:** C₄ = 0.075 means destructive inter-shell interference at shell 4 KILLS the top quark mass contribution rather than enhancing it. The 600-cell shell structure accumulates only 74 actual vertices across 4 shells. SM-2's effective N_k = 30,000 for the top quark (vs 30 actual vertices in shell 4) represents a factor of ~1000 that no combination of C_n and N_l can generate.

**Conclusion:** The φ^{3(l-1)} scaling and its exact-volume refinement are FALSIFIED for the quark mass hierarchy. The top quark mass cannot come from cumulative shell vertex counts × phase cancellation.

### 30 March 2026 — Two Surviving Discoveries

From the wreckage of the falsification, two empirical results survived:

1. **m_u/m_e = φ³** to 0.21% (PS-1). This connects the quark and lepton mass baselines through a single φ-algebraic ratio. Registered as CONJ-SM-4.

2. **K(c,b,t) = 2/3** to 0.42% (PS-1). The Koide ratio for the three heaviest quarks matches the K₃ spectral structure, suggesting heavy quarks are dominated by ZBW thermal energy (where K₃ spectral structure governs) rather than by cage geometry (where φ-volume scaling was supposed to govern). This redirected the search toward the thermal picture.

### April 2026 — The New Direction: SM-8

The falsification of φ^{3(l-1)} directly motivated SM-8's approach: instead of volume scaling, use the actual bonded distance shells (tetrahedron, icosahedron, dodecahedron, icosidodecahedron) with vertex count as the mass parameter. SM-8 Theorem 6.1 achieves 2.1% RMS with M_q = m_e(z/φ)V^(7/3) — a completely different formula that never uses φ³ volume scaling.

---

## Status Progression

| Date | Status | Event | Paper |
|------|--------|-------|-------|
| Pre-2026 | CONJ | φ^{3(l-1)} proposed as quark mass scaling | SS-1 |
| Mar 2026 | FALS | **Exact 600-cell shell volumes deviate by 3–8×; palindromic structure** | PS-1 |
| 30 Mar 2026 | FALS | SC-1 computation confirms: C₄ = 0.075 kills top quark mass | SC-1 |
| 30 Mar 2026 | — | m_u/m_e = φ³ and K(c,b,t) = 2/3 survive as independent results | PS-1 |
| Apr 2026 | — | SM-8 V^(7/3) replaces φ³ scaling; 2.1% RMS achieved | SM-8 |

---

## Lessons

1. **Elegant formulas can be wrong.** φ^{3(l-1)} was beautiful and natural for a φ-based theory. It was also wrong. The actual geometry of the 600-cell is more complex (and more interesting) than volume scaling.

2. **Negative results redirect productively.** The falsification forced the move from "volume scaling per shell" to "bonded distance shells with actual vertex counts," which produced SM-8's strongest results.

3. **Partial truths survive falsification.** m_u/m_e = φ³ and K(c,b,t) = 2/3 are real empirical patterns that survived the collapse of the formula that was supposed to explain them.

---

## Cross-References

- **Research_Frontier.md entry:** FALS-C-SM-2 (§6 Falsified)
- **Related problems:** OPEN-SS-1 (quark mass formula — still open), OPEN-SM-cage-1 (derive α = 2.38), CONJ-SM-4 (m_u/m_e = φ³)
- **Solution candidate:** SC-1 (falsified; C_n factors confirmed as lasting contribution)
- **Key development:** SM-8 development transcript, PS-1 session notes

---

*Problem history created 12 April 2026. Source material: OP-SS-1 problem file, solution_candidates.md (SC-1), PS-1 session results, SM-8 development transcript.*
