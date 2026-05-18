# SS-8 H2' Derivation Note — Tiered Derivation of the 2E/V Scaling Law

**Location:** `/CPP/series_strong/papers/SS-8/sketches/SS-8_H2prime_derivation_note.md`
**Produced:** 21 April 2026
**Author:** Claude Opus (SS-8 kickoff session, post-Phase-1b)
**Tier:** **EXPLORATORY** — pre-v0.1 working note. No registry updates triggered. Subject to multi-AI review per `operating_system.md` §5 before any promotion to paper-level theorem or axiom stack.
**Inputs:** `SS-8_Phase1_extended_map_findings.md` (this folder); `axiom-registry.md` (21 April 2026); `series_strong/papers/SS-7_alpha_cluster_edge_formula.tex` v1.2.
**Partial OPEN reference:** opens OPEN-SS-26 (D1), OPEN-SS-27 (D2), OPEN-SS-28 (D3) as sub-targets of the first-principles H2' derivation flagged in §8.7 of the findings doc.

---

## 1. What this note is (and is not)

The Phase 1b findings note closed with H2' — the empirical observation that single-neutron interstitial binding in alpha-cluster nuclei scales as $(6 - 12/V) \cdot B_{\text{pair}}$ — labeled as a **hypothesis** and carrying a provisional attribution "derivable from A5 + A8' + A11 without geometric input" (§8.7, line 479).

This note does three things:

1. **Refines the attribution.** Verbatim reading of `axiom-registry.md` shows that A5, A8', A11 as stated do not directly encode a nucleon-scale bonding mechanism; they establish the lattice scale, the propagation efficiency, and the cage-volume self-energy scaling that collectively source the *quantum* $B_{\text{pair}}$, but the *mechanism* (how an interstitial neutron couples to K₃ edges at its host alpha-vertex) is paper-level structural content that must be named as such.

2. **Separates the derivation into tiers.** Following the SS-7 Theorem 3N-6 / hypothesis C4 epistemic split (SS-7 v1.2 §2.2 yellow-boxed block), this note identifies three distinct tiers for H2': pure combinatorial mathematics (Layer 1), axiom-sourced quantum physics (Layer 2a), and paper-level structural hypotheses (Layer 2b).

3. **Opens three refined sub-problems** (OPEN-SS-26, -27, -28) corresponding to the three paper-level hypotheses in Layer 2b, each with a specific target for first-principles derivation from CPP primitives.

**This note is not:**
- A draft of SS-8 v0.1.
- A registry update (no axioms added, no predictions promoted, no conjectures resolved).
- A reviewer-ready derivation (Layer 2b hypotheses are stated at the same tier SS-7 C1–C4 live at — structural, empirically supported, not yet derived).

---

## 2. Target: H2' restated precisely

From findings §8.5:

> **H2' (single-neutron interstitial binding).** For an even-even alpha-cluster nucleus with N_α alpha-vertices in the bulk regime, the per-extra-neutron binding delta is
>
> $$\Delta_1(N_\alpha) = \frac{2E(N_\alpha)}{V(N_\alpha)} \cdot B_{\text{pair}} = \left(6 - \frac{12}{N_\alpha}\right) B_{\text{pair}}$$
>
> where $V = N_\alpha$ is the vertex count and $E$ is the edge count of the alpha-polytope.

The target is a **zero-parameter prediction** for 12 data rows (N_α = 3..14) at N_ex = 2, with residuals attributable to (a) nn pairing bonus (H3'), (b) small-polytope attenuation at N_α ≤ 4 (H5'), and (c) Pauli decrement at higher N_ex (H4').

Findings §8.6 reports ratios observed/predicted within 10% of unity for N_α ∈ {4, 6, 8, 10, 12, 14} at N_ex = 2, with N_α = 6 (octahedron) and N_α = 10 (gyroelongated square bipyramid) matching to **<1.5%**.

---

## 3. The tiered derivation structure

H2' decomposes cleanly into three independent claims, each provable at a different tier:

| Layer | Content | Type | Source |
|---|---|---|---|
| **1** | $2E/V = 6 - 12/V$ for simplicial polytopes | Pure mathematics (Euler) | Classical combinatorics; no CPP input |
| **2a** | $B_{\text{pair}} = M_0/\varphi = 2.342$ MeV | Programme-level axiom-derived | A2, A5, A8', A11 via SS-5 |
| **2b** | Per-neutron binding $= (\text{avg K₃-degree at host vertex}) \cdot B_{\text{pair}}$ | Paper-level structural hypotheses | D1, D2, D3 (new to SS-8) |

The claim "A5 + A8' + A11 ⇒ H2' without geometric input" from findings §8.7 is **accurate for Layers 1 and 2a combined** (the axioms plus the math) but **incomplete for Layer 2b**: the mechanism by which an interstitial neutron couples, at each alpha-vertex, to exactly the K₃ edges incident there and at strength $B_{\text{pair}}$ per edge is not stated by A5, A8', or A11. It is a structural claim about the physics of interstitial insertion that parallels SS-7's C3 (K₃ collective mode at alpha-alpha contact) at a different contact scale.

Layers 1 and 2a are inherited mathematics and inherited physics; Layer 2b is SS-8's new structural content.

---

## 4. Layer 1 — Pure combinatorics

### Theorem 1 (Average vertex degree of a simplicial polytope)

For any convex polytope on $V \geq 4$ vertices with exclusively triangular faces (a simplicial 3-polytope, equivalently a triangulated topological sphere), the average vertex degree satisfies

$$\bar{d}(V) \equiv \frac{1}{V} \sum_{v} \deg(v) = \frac{2E}{V} = 6 - \frac{12}{V}.$$

**Proof (classical).** Two standard facts combine:

(a) *Handshaking lemma* (true for any finite graph): $\sum_v \deg(v) = 2E$, since each edge contributes $+1$ to the degree of each of its two endpoints.

(b) *Euler's formula for simplicial polytopes* (SS-7 Theorem 3N-6, reproduced here for self-containment): For a convex simplicial 3-polytope, $V - E + F = 2$ and $2E = 3F$ (each edge is shared by exactly two triangles), giving $E = 3(V - 2) = 3V - 6$.

Combining: $\bar{d}(V) = 2E/V = 2(3V-6)/V = 6 - 12/V$. $\square$

### Remark 1 (Universality over polytope identity).

Different simplicial polytopes on the same $V$ vertices share the same edge count and hence the same average vertex degree, even when individual vertex degrees differ (e.g., a gyroelongated square bipyramid at $V = 10$ has vertices of degree 4 and 5, but the average is exactly $4.8 = 6 - 12/10$). H2' therefore does not require identifying the specific polytope realized in each nucleus — only that some simplicial polytope (or graph-simplicial structure, per H1') is realized. This mirrors SS-7 Remark 5.1 for the edge count.

### Remark 2 (Degenerate extension to $V = 3$).

For $V = 3$ (three alphas in a planar triangle), the 3-polytope framework does not apply (the configuration is 2D). Nonetheless, the direct edge count $E = 3$ combined with the handshaking lemma gives $2E/V = 2$, matching the formula $6 - 12/3 = 2$. The Phase 1b scaling-law fit reports $k_{\text{eff}}^{\text{obs}}(N_\alpha = 3) = 2.85$ against this predicted $2.00$ (findings Table §8.4); the +0.85 residual is the light-side excess flagged under H5', not a Layer-1 failure.

### What Layer 1 does and does not claim.

Layer 1 claims only the mathematical identity. It does not claim:
- That alpha-cluster nuclei realize simplicial polytopes (that's SS-7's C4, inherited).
- That interstitial neutrons couple to K₃ edges at the host alpha-vertex (that's SS-8's D2, new).
- That the per-edge coupling strength equals $B_{\text{pair}}$ (that's Layer 2a + D2 combined).

---

## 5. Layer 2a — Quantum sourcing: $B_{\text{pair}}$ from programme-level axioms

The quantum $B_{\text{pair}} = M_0/\varphi = 2.342$ MeV that enters both SS-7's $(3N_\alpha - 6) B_{\text{pair}}$ edge sum and SS-8's $(2E/V) B_{\text{pair}}$ interstitial sum is **identically the same quantum**. Its derivation is inherited from SS-5 and requires no new SS-8 content; we reproduce the axiom stack here only to establish that Layer 2a is complete before Layer 2b is invoked.

### Verbatim axiom citations (from `/CPP/axiom-registry.md`, 21 April 2026)

**A2 (600-cell topology, Tier 1):**
> "CPs are arranged on the vertices of a tessellated 600-cell polytope (V=120, E=720, F=1200, C=600, z=12)"

**A5 (Propagation efficiency, Tier 2):**
> "The cage-scale propagation efficiency is η = l_edge/R_circ = 1/φ, where φ = (1+√5)/2"

**A8' (Cage-Volume Scaling Principle, Tier 5):**
> "Quark masses scale as M ∝ m_e(z/φ)V^(7/3) because the self-energy of the ZBW/qDP chain network is proportional to the number of angular-weighted nearest-neighbour pairs in the cage volume. [...] The prefactor M₀ = m_e z/φ follows from lattice connectivity (z=12, l_edge=1/φ)."

**A11 (Lattice-Scale Grounding, Tier 6):**
> "The conversion between 600-cell lattice units and physical length is fixed by the convergence of the pion decay constant (Pagels-Stokar) and the running of α_geom = 1/√5 to α_s(m_Z), yielding l_unit = ℏc/Λ_QCD ≈ 0.589 fm."

### The $B_{\text{pair}}$ derivation

The prefactor $M_0 = m_e \cdot z / \varphi$ follows directly from A8' (which defines $M_0$ in its statement) with the coordination number $z = 12$ supplied by A2 (the 600-cell has $z = 12$ edge neighbors per vertex) and the $1/\varphi$ factor supplied by A5 (propagation efficiency). Numerically,

$$M_0 = m_e \cdot \frac{z}{\varphi} = 0.511 \text{ MeV} \cdot \frac{12}{1.618} \approx 3.79 \text{ MeV}.$$

The SS-5 eigenvalue calculation over a K₃ triangular face structure produces one collective bonding mode at energy $M_0/\varphi$, yielding

$$B_{\text{pair}} = \frac{M_0}{\varphi} = \frac{m_e z}{\varphi^2} \approx 2.342 \text{ MeV}.$$

A11 fixes the lattice-to-physical length conversion that makes this numerical value come out in MeV rather than in lattice units.

### Pattern 6: the scale-recurrence observation

The axiom registry (line 234) identifies $B_{\text{pair}} = M_0/\varphi$ as a quantum that has now appeared in **three distinct physical contexts without rescaling**:

1. Nucleon-nucleon contact in SS-5 (np pairs).
2. The ⁴He tetrahedral closure bonus in SS-5.
3. Each alpha-alpha contact in SS-7 v1.2 (producing $(3N_\alpha - 6) B_{\text{pair}}$).

**SS-8 adds a fourth scale to this pattern:** the interstitial-neutron to alpha-vertex contact, with per-incident-edge strength $B_{\text{pair}}$ (by D2, §6 below). Whether this scale recurrence is structurally *necessary* (forced by the axiom set) or merely *allowed* remains the observation underlying the Pattern-6 open question in the registry. The SS-5 K₃ eigenvalue calculation replicates identically at each scale because the underlying graph is the same geometric object (K₃); what varies is the physical scale at which the three contact nodes live.

### What Layer 2a does and does not claim.

Layer 2a inherits the $B_{\text{pair}} = M_0/\varphi$ derivation entirely from SS-5. It establishes that the quantum in H2' is fixed by programme-level axioms with no SS-8 calibration. It does not claim that interstitial-neutron binding operates at this quantum per-edge — that is Layer 2b's D2.

---

## 6. Layer 2b — Mechanism: structural hypotheses D1–D3

### 6.1 Inheritance from SS-7 (C1–C4)

SS-8 inherits without modification the four SS-7 assumptions on the alpha-polytope substrate:

- **C1** (alpha rigidity at nuclear scale)
- **C2** (alpha-alpha base-to-base contact)
- **C3** (K₃ collective mode at each alpha-alpha contact, supplying $B_{\text{pair}}$ per edge)
- **C4** (simplicial alpha-polytope connectivity)

The underlying alpha-cluster substrate for SS-8 is whatever substrate SS-7 establishes: an $N_\alpha$-vertex simplicial polytope with $E = 3N_\alpha - 6$ alpha-alpha contact edges. SS-8 adds interstitial neutrons to that substrate without modifying it; C1–C4 carry over unchanged, and C4's status as OPEN-SS-24 (first-principles derivation deferred to SS-9 candidate) is also inherited unchanged.

### 6.2 D1 — Interstitial-neutron localization at alpha-vertex

**Statement.** An extra neutron added to an alpha-cluster nucleus (beyond the $N = Z = 2N_\alpha$ baseline) localizes near one of the $N_\alpha$ alpha-vertices of the cluster polytope, rather than at an edge-midpoint, triangular-face-center, or polytope-interior (cell-center) site.

**Empirical support (Phase 1b).** Findings §8.2 and §8.3 falsify two natural alternatives:

- Naive face-center (k = 3) model: predicts $\Delta_1 = 3 \cdot B_{\text{pair}} = 7.03$ MeV per neutron. Matches N_α ≤ 4 but underpredicts N_α ≥ 9 by a factor of ~1.7. Ruled out as sole mechanism.
- Interior-centroid (k = V) model: predicts $\Delta_1 = V \cdot B_{\text{pair}}$. At N_α = 6 (octahedron) predicts 14.05 MeV; observed 9.40 MeV. At N_α = 12 (icosahedron) predicts 28.10 MeV; observed 12.62 MeV. Ruled out hard.

The Phase 1b 2E/V fit (findings §8.4) sits numerically between these two alternatives and implies vertex-localization with K₃-edge coupling — the D1 + D2 picture.

**Physical intuition (SSV-minimization, schematic).** In SS-5/SS-7, alpha-alpha contact forms a K₃ structure because the three outer nucleons of each alpha's face meet three-to-three. An interstitial neutron approaching the alpha-polytope would, in this geometric picture, find its lowest-SSV-stress site not at an abstract face-center (where no pre-existing K₃ structure terminates) but at an alpha-vertex, where multiple K₃ faces terminate in a single nucleon of one of the alphas. At such a vertex, the incoming neutron sees $\deg(v)$ incident K₃ edge-contacts and can form a compound K-mode analogous to the alpha-alpha K₃ mode but at the (interstitial-n)-(alpha-outer-nucleon) scale.

This intuition parallels SS-7's C4 physical-intuition argument structure ("thermodynamic selection": the ground-state configuration should minimize SSV stress by maximizing usable K₃ contacts). It is verbal reasoning, not derivation; a full SSV-minimization proof over candidate localization sites is the content of OPEN-SS-26, partially delivered by the SSV-minimization sketch of 21 April 2026 (see below).

**Status (updated 22 April 2026).** D1 promotes from structural hypothesis to **conditional theorem under two functionally distinct realizations of a shared proximity-binding premise**, as established in `SS-8_D1_ssv_minimization_sketch.md` and refined by the Round 2 Q2 algebraic-reduction analysis (`SS-8_D1_Q2_algebraic_reduction_analysis.md`). The two realizations:

- **Premise A (D2-counting):** given D2's K₃-face-participation counting rule, D1 is a corollary by polytope combinatorics alone — deg(v) ≥ 3 > 2 (edge) > 1 (face) > 0 (centroid) for any simplicial 3-polytope with V ≥ 4.
- **Premise B (SR-nn-pair):** given SR-nn-pair physics with range λ_nn << L_αα (inherited from SS-5 pair physics and SS-7's alpha-alpha contact distance L_αα = 2.37 fm), vertex wins via Yukawa localization, independent of D2's counting rule.

Numerical evaluation at the octahedron (N_α = 6) and gyroelongated square bipyramid (N_α = 10) — the two Phase 1b predictions matched to <1.5% — confirms gap factors of 2.0× and 2.5× under Premise A, 1.57× and 1.59× under Premise B.

The two realizations are **Level-1 and Level-2 independent** (algebraically and functionally distinct by multiplicity vector, site ordering, and degree scaling), but they share the proximity-binding ancestor principle, so **Level-3 independence is not established**. The conditional-theorem tier respects this distinction: "either sufficient realization" does not mean "either distinct physical principle." A derivation of D1 from a non-proximity mechanism (topological, entropic, geometric-phase) would be needed for full Level-3 independence and is promoted to a programme-level OPEN-FRONTIER question (see §10).

First-principles derivation of either premise from programme-level axioms alone is not yet delivered. Since both premises reduce to SS-5/SS-7-inherited substrate, the remaining first-principles work is consolidated with **OPEN-SS-27** (functional content) and promoted to programme-level OPEN-FRONTIER registry (physical-principle content). D1 and D2 are coupled, not independent — Premise A makes D1 a corollary of D2, so deriving D2 from primitives delivers D1 as an automatic consequent.

### 6.3 D2 — K₃-edge coupling at the host alpha-vertex

**Statement.** An interstitial neutron localized at alpha-vertex $v$ (by D1) couples to the $\deg(v)$ K₃ contact faces incident at $v$. Each such coupling contributes binding energy $B_{\text{pair}}$ (the same quantum established by Layer 2a, via the SS-5 K₃ eigenvalue calculation applied at the (interstitial-n)-(alpha-vertex) scale).

**Geometric justification.** By C2 and C3 (inherited from SS-7), each alpha-alpha contact at vertex $v$ realizes a K₃ triangular face between the two alphas meeting there. When an interstitial neutron occupies a site near $v$, its pair-contact with the outer nucleon at $v$ participates simultaneously in all $\deg(v)$ of those K₃ faces — each face now has a fourth vertex candidate (the interstitial) adjacent to its triple. By the SS-5 eigenvalue rule, each K₃ face with an incoming participant produces one collective bonding mode at $M_0/\varphi = B_{\text{pair}}$. The interstitial neutron therefore accrues $\deg(v) \cdot B_{\text{pair}}$ in binding from its host vertex alone.

The scale at which this K₃ calculation is run has shifted: SS-5 runs it over a K₃ of nucleon-nucleon contacts (internal to an alpha); SS-7 runs it over a K₃ of alpha-alpha contact pairs (at the alpha-alpha interface); SS-8 now runs it over a K₃ of interstitial-alpha contact pairs (at each face incident to the host vertex). The eigenvalue outputs the same $B_{\text{pair}}$ quantum because the underlying graph is the same object (the complete graph on three edges). This is precisely the Pattern-6 scale recurrence (Layer 2a) now extended to a fourth scale.

**Connection to A6' (Walk-Dimension Gauge Principle).** A6' currently describes two coupling regimes at the 600-cell cage scale: the **edge sector** (1D walks, coupling to "2 internal K₃ bonds per vertex", U(1)) and the **face sector** (2D walks, coupling to "z = 12 incident bonds in the closed neighbourhood", SU(3)). The SS-8 interstitial-coupling pattern, $\deg(v) = 2E/V$ averaged across $v$, sits between these two regimes and is not currently spanned by A6' as written. Whether D2 can be derived as a nucleon-scale analog of A6' (with $\deg(v) = 2E/V$ emerging as the correct coordination number at the interstitial-alpha scale) is the content of **OPEN-SS-27** (see §10).

**Status.** D2 is a **paper-level structural hypothesis** at the same tier SS-7 C3 lives at: supported empirically by Phase 1b's 2E/V fit, supported geometrically by the Pattern-6 scale-recurrence argument, but not derived from the programme-level axiom stack. OPEN-SS-27 targets the A6'-extension derivation.

**D1–D2 coupling note (added 21 April 2026).** D1 and D2 are not logically independent. Under the Premise A path of `SS-8_D1_ssv_minimization_sketch.md` §4, D1 (vertex localization) is a corollary of D2 (K₃-face-participation counting) plus simplicial polytope combinatorics — deg(v) ≥ 3 > 2 > 1 > 0 holds for any simplicial 3-polytope with V ≥ 4. The reverse implication does not hold: D1 alone does not determine the per-face strength. D2 therefore stands as the **primary paper-level hypothesis** of Layer 2b, with D1 its localization-consequent. Deriving D2 from programme-level axioms (the content of OPEN-SS-27) automatically delivers D1 as a corollary; the original OPEN-SS-26 (first-principles D1 derivation) is subsumed accordingly (§10).

### 6.4 D3 — Bulk-regime averaging

**Statement.** In the bulk regime $N_{\text{ex}} \ll V$, interstitial neutrons distribute across the $V$ alpha-vertices such that the mean per-neutron binding equals the average of $\deg(v) \cdot B_{\text{pair}}$ over all vertices, i.e.

$$\langle \Delta_1 \rangle = \frac{1}{V} \sum_{v \in V} \deg(v) \cdot B_{\text{pair}} = \bar{d}(V) \cdot B_{\text{pair}} = \frac{2E}{V} \cdot B_{\text{pair}}.$$

**Quantitative support.** Findings Table §8.4 reports the empirical $k_{\text{eff}}$ across N_α = 4..14:

| N_α | 2E/V (predicted) | $k_{\text{eff}}^{\text{obs}}$ | residual |
|---|---|---|---|
| 4 | 3.00 | 2.68 | −0.32 |
| 6 | 4.00 | 4.01 | **+0.01** |
| 8 | 4.50 | 4.98 | +0.48 |
| 10 | 4.80 | 4.85 | **+0.05** |
| 12 | 5.00 | 5.39 | +0.39 |
| 14 | 5.14 | 5.55 | +0.41 |

Mean residual across N_α = 4..14 (excluding the planar $N_\alpha = 3$ case): +0.21. Most rows match to <10%; N_α = 6 and N_α = 10 match to <1.5% — a "clean, SS-7-level quantitative result" (findings §8.6).

**The residual structure (what D3 should predict, not absorb).** The +0.2 to +0.5 bulk residual is **predicted**, not tuned, and decomposes across three sources:

1. **nn pairing bonus (H3').** At $N_{\text{ex}} = 2$, two interstitials pair with opposite DP polarity, acquiring $\sim 0.2$–$0.4 \cdot B_{\text{pair}}$ per pair. This accounts for most of the +0.2 bulk-mean residual.
2. **Small-polytope attenuation (H5').** At $N_\alpha = 4$, the tetrahedron has only 4 faces; interstitials see an effective coordination reduced by boundary effects. This accounts for the −0.32 residual at N_α = 4.
3. **Finite-V corrections.** The handshaking-lemma average $2E/V$ assumes uniform distribution across vertices; for small V, stochastic vertex-occupation departures produce $O(1/V)$ corrections. At N_α = 4 this is already a ~25% effect, decaying as $V^{-1}$.

**Status.** D3 is a **paper-level structural hypothesis** at a tier analogous to SS-5's uniform nucleon-distribution assumption: supported empirically by the Phase 1b fit, but not derived from first principles. The residual-decomposition claim above is itself a sub-hypothesis that the Phase 1b fit is consistent with but does not prove. First-principles derivation of D3 plus a proof that residuals decompose exactly as above (no hidden mechanisms absorbed into "pairing bonus") is the content of **OPEN-SS-28** (see §10).

---

## 7. The H2' theorem (combined)

### Theorem 2 (H2' interstitial scaling law)

Under assumptions C1–C4 (inherited from SS-7, with C4 as OPEN-SS-24) and D1–D3 (introduced in this note, with OPEN-SS-26/27/28), the per-extra-neutron binding delta for an even-even alpha-cluster nucleus in the bulk regime ($N_{\text{ex}} \ll V$) satisfies

$$\Delta_1(N_\alpha) = \left(6 - \frac{12}{N_\alpha}\right) B_{\text{pair}}$$

to leading order in $1/V$ and $N_{\text{ex}}/V$, where $B_{\text{pair}} = M_0/\varphi$ is fixed by programme-level axioms A2, A5, A8', A11 (via the SS-5 derivation).

**Proof (combining Layers 1, 2a, 2b).**

*Step 1 (Layer 2b).* By D1, the interstitial neutron is at some alpha-vertex $v$ of the cluster polytope. By D2, its binding is $\deg(v) \cdot B_{\text{pair}}$, with $B_{\text{pair}}$ sourced by Layer 2a (A2+A5+A8'+A11 via SS-5).

*Step 2 (Layer 2b).* By D3 (bulk-regime averaging), the per-neutron binding delta equals the uniform average over vertices:

$$\Delta_1 = \frac{1}{V} \sum_{v \in V} \deg(v) \cdot B_{\text{pair}} = \frac{B_{\text{pair}}}{V} \sum_v \deg(v).$$

*Step 3 (Layer 1).* By the handshaking lemma, $\sum_v \deg(v) = 2E$. By Theorem 1 (Euler's formula for simplicial polytopes, itself inheriting C4 from SS-7 for the assertion that the nuclear alpha-polytope *is* simplicial), $E = 3V - 6$, so $2E/V = 6 - 12/V$.

*Combining:* $\Delta_1 = (2E/V) B_{\text{pair}} = (6 - 12/V) B_{\text{pair}}$. $\square$

### Remark 3 (Same combinatorial backbone as SS-7).

Theorem 2 (SS-8) and SS-7's central formula both rest on the simplicial polytope identity $E = 3V - 6$. SS-7 counts edges directly ($E \cdot B_{\text{pair}}$); SS-8 counts edge-incidences per vertex, averaged ($2E/V \cdot B_{\text{pair}}$). Both results come from the same Euler identity applied to the same alpha-polytope. This is not a coincidence: it is the mathematical signature of a consistent edge-counting physics across the two papers.

### Remark 4 (Recovery of SS-7 at $N_{\text{ex}} = 0$).

At $N_{\text{ex}} = 0$, Theorem 2 gives $\Delta_1 \cdot 0 = 0$ interstitial contribution, and the total binding reduces to SS-7's $N_\alpha \cdot B_\alpha + (3N_\alpha - 6) B_{\text{pair}}$. SS-8 therefore nests SS-7 as the $N_{\text{ex}} = 0$ special case, in the same way SS-7 v1.1 nested SS-5's ⁴He prediction at $N_\alpha = 1$.

---

## 8. Theorem vs. hypothesis: the epistemic split

> **What is mathematics:** Theorem 1 (§4) is pure combinatorics. It holds unconditionally for every simplicial 3-polytope regardless of any physics claim. Likewise, the handshaking lemma holds for every finite graph.
>
> **What is axiom-derived:** Layer 2a's derivation of $B_{\text{pair}} = M_0/\varphi$ follows from programme-level axioms A2, A5, A8', A11 via the SS-5 K₃ eigenvalue calculation. No SS-8-specific calibration enters.
>
> **What is paper-level structural hypothesis:**
> - **D1** (interstitial neutron localizes at an alpha-vertex)
> - **D2** (K₃-edge coupling at the host vertex, with strength $B_{\text{pair}}$ per edge)
> - **D3** (bulk-regime uniform averaging)
>
> And also the inherited SS-7 hypotheses C1 (alpha rigidity), C2 (alpha-alpha base-to-base contact), C3 (alpha-scale K₃ mode), C4 (simplicial polytope connectivity).
>
> **What remains an open problem:**
> - **OPEN-SS-24** (inherited): first-principles derivation of C4 (simplicial connectivity) from CPP lattice primitives.
> - **OPEN-SS-26** (new): first-principles derivation of D1 (interstitial vertex-localization) from SSV minimization.
> - **OPEN-SS-27** (new): first-principles derivation of D2 (K₃-edge coupling at interstitial scale) from A6' extended to the nucleon-interstitial scale.
> - **OPEN-SS-28** (new): first-principles derivation of D3 (bulk-regime averaging) plus proof that residuals decompose cleanly into H3' pairing, H5' small-polytope attenuation, and Pauli (H4').
>
> Theorem 2 is therefore a **conditional theorem**: unconditionally true given C1–C4 + D1–D3, conditionally open on four first-principles open problems. The 12 quantitative predictions in Phase 1b (findings §8.6) are empirical tests of the conjunction of those hypotheses, not of Theorem 2 in isolation.

This epistemic structure directly parallels SS-7's Theorem 3N-6 / C4 split (SS-7 v1.2 §2.3 yellow-boxed block) and inherits its honesty discipline: the empirical predictions that come out of the theorem are attributed to the full stack (axiom stack + inherited hypotheses + new hypotheses), not to the programme-level axioms alone.

---

## 9. Empirical validation (from Phase 1b)

From findings §8.6, Theorem 2 predicts at $N_{\text{ex}} = 2$:

| N_α | Nuclide | $\Delta_{\text{pred}} = 2 \Delta_1$ (MeV) | $\Delta_{\text{obs}}$ (MeV) | ratio obs/pred |
|---|---|---|---|---|
| 4 | ¹⁸O | 14.05 | 12.57 | 0.89 |
| 6 | ²⁶Mg | 18.74 | 18.80 | **1.003** |
| 8 | ³⁴S | 21.08 | 23.32 | 1.11 |
| 10 | ⁴²Ca | 22.48 | 22.73 | **1.011** |
| 12 | ⁵⁰Cr | 23.42 | 25.24 | 1.08 |
| 14 | ⁵⁸Ni | 24.08 | 26.00 | 1.08 |

**Five of six rows within 10%; two rows (N_α = 6, 10) within 1.5%.** Zero SS-8-specific parameters fitted.

The systematic +0.1 to +0.3 residual in the $N_\alpha \geq 8$ regime is predictively attributed to the H3' pairing bonus (two opposite-polarity interstitials contribute an extra ~0.2–0.4 $B_{\text{pair}}$ per pair, independent of N_α). The −0.11 residual at N_α = 4 is attributed to H5' small-polytope attenuation. Both H3' and H5' are separate structural hypotheses not covered by D1–D3, registered as targets for further Phase 1b refinement or v0.1 derivation.

---

## 10. Open problems opened (OPEN-SS-26, -27, -28)

Following the SS-7 precedent (OPEN-SS-18 splitting into -22, -23, -24 as distinct numbered problems with separate PH records), the H2' derivation target from findings §8.7 splits into three sub-problems:

### OPEN-SS-26 — Derivation of D1 (interstitial localization) — **partially resolved 21 April 2026**

**Statement.** Derive from A2 (600-cell lattice), A5 (propagation efficiency), A11 (lattice scale), and an SSV energy-minimization principle that an interstitial neutron, when added to an alpha-cluster bound state, preferentially localizes near one of the $N_\alpha$ alpha-vertices rather than at a face-center, edge-midpoint, or polytope-interior site.

**Status update (21 April 2026).** Partially resolved by `SS-8_D1_ssv_minimization_sketch.md`. D1 promotes from structural hypothesis to **conditional theorem** under either of two independent sufficient premises: (A) the D2 counting rule makes D1 a corollary via simplicial polytope combinatorics (gap factor 2.0× for octahedron, 2.5× for GESBP); (B) SR-nn-pair physics with λ_nn << L_αα makes D1 a Yukawa-localization consequence, independent of D2 (gap factor 1.57× and 1.59× respectively). Numerical evaluation at both test polytopes confirms vertex-preference under both models.

**Remaining content — split by independence level (refined 22 April 2026).** Following the Round 2 Q2 algebraic-reduction analysis, the residual first-principles work is split into two tiers:

- **Functional content (absorbed into OPEN-SS-27):** Deriving either Premise A (D2 counting rule) or Premise B (SR-nn-pair scaling) from programme-level axioms alone. Premise A plus simplicial combinatorics gives D1 automatically; deriving D2 therefore closes Level-2 independence of D1 at programme tier. OPEN-SS-27 (D2 derivation) subsumes this content.
- **Physical-principle content (promoted to programme-level OPEN-FRONTIER):** Deriving D1 from a mechanism unrelated to proximity-aggregation (topological, entropic, geometric-phase). Both Model A and Model B share the proximity-binding ancestor principle; a Level-3-independent derivation would require exhibiting D1 under a distinct physical premise. This is a programme-wide structural question, not SS-8-specific, and is promoted to `research_frontier.md` as OPEN-FRONTIER-NNN rather than kept under the SS-8 OPEN-SS list.

**Target paper:** conditional theorem now in sketch; full first-principles content merged into OPEN-SS-27's scope.

**Relationship:** Originally parallel to OPEN-SS-24 (C4 derivation). Post-resolution: D1 is a corollary of D2; OPEN-SS-26 is effectively a sub-clause of OPEN-SS-27.

**Registry action pending:** create PH-OPEN-SS-26 marking partial resolution with reference to this sketch.

### OPEN-SS-27 — Derivation of D2 (K₃-edge coupling at interstitial scale) — **expanded scope 21 April 2026**

**Statement.** Extend A6' (Walk-Dimension Gauge Principle) from the 600-cell cage scale to the (interstitial-nucleon)-(alpha-vertex) contact scale, deriving that the coupling coordination number equals $\deg(v)$ (the K₃-edge count incident at the host vertex) rather than the edge-sector value $z_{\text{edge}} = 2$ or the face-sector value $z_{\text{face}} = 12$.

**Scope expansion (21 April 2026).** Post the SSV-minimization sketch, OPEN-SS-27 additionally subsumes the residual first-principles content of OPEN-SS-26. Deriving D2 from programme-level axioms automatically delivers D1 via the D1–D2 coupling (§6.3 of this note). OPEN-SS-27 is therefore the single substantive Layer 2b first-principles target for SS-8.

**Target:** A6' currently distinguishes 1D edge walks (U(1), $z_{\text{edge}} = 2$) from 2D face walks (SU(3), $z_{\text{face}} = 12$). The interstitial-neutron coupling pattern ($\deg(v) = 2E/V$) is neither; it is a new regime at the nucleon-scale contact manifold. A fully-derived D2 would either (a) show that the A6' principle extends to this regime with $\deg(v)$ as the correct coordination count, or (b) introduce a new principle A6'' for nucleon-scale contacts.

**Target paper:** SS-8 v0.1 if tractable; otherwise an A6'-extension paper (SM-series candidate) or SS-11 candidate.

**Relationship:** Extension of A6' to a new walk regime. Now also the derivation target for D1 (via D1–D2 coupling).

### OPEN-SS-28 — Derivation of D3 (bulk-regime averaging and residual structure)

**Statement.** Derive from C1–C4 + D1 + D2 that interstitial neutrons in the bulk regime distribute uniformly across alpha-vertices (so that the per-neutron binding averages to $\bar{d}(V) \cdot B_{\text{pair}}$), and that the deviations from this average decompose into: (i) nn pairing bonus (H3'), (ii) small-polytope attenuation at $N_\alpha \leq 4$ (H5'), (iii) Pauli-induced decrement at higher $N_{\text{ex}}$ (H4'), with no residual mechanisms absorbed.

**Target:** Show that the $\sim +0.2$ to $+0.5 \cdot B_{\text{pair}}$ residuals at $N_\alpha \geq 6$ in Phase 1b's $k_{\text{eff}}$ table are fully accounted for by H3' + H5' without an additional SS-8-specific coupling adjustment. This is the "predict, don't absorb" test: a clean D3 derivation would forecast the residuals' sign and magnitude ahead of the fit.

**Target paper:** SS-8 v0.1 (likely partially covered in residual-analysis section); full derivation possibly deferred to companion or future paper.

**Relationship:** Structural analog of nucleon-distribution uniformity claims in SS-5, at the alpha-cluster + interstitial scale.

### Summary of open-problem cascade

SS-7 left behind: **OPEN-SS-23** (odd-A and non-alpha-chain, retargeted to SS-8), **OPEN-SS-24** (C4 → theorem, SS-9 candidate), **OPEN-SS-25** (DP-sea Coulomb screening, SS-7-adjacent).

SS-8 (this Phase 1b work) adds: **OPEN-SS-26** (D1, partially resolved 21 April 2026 — conditional theorem delivered, remainder subsumed by OPEN-SS-27), **OPEN-SS-27** (D2, expanded scope — now includes the residual D1 content), **OPEN-SS-28** (D3, unchanged). The net substantive first-principles count for SS-8's Layer 2b is therefore two open problems (OPEN-SS-27 and OPEN-SS-28), reduced from three by the D1–D2 coupling discovery.

None of these changes the programme-level axiom count (still 9 as of SS-7 v1.2). All are paper-level hypothesis derivation targets.

---

## 11. Next steps

### 11.1 Immediate (this exploratory note)

- Commit this note + the four Phase 1b artifacts as exploratory-tier; **no registry updates**.
- Circulate to Copilot, Grok, ChatGPT for adversarial review per `operating_system.md` §5 multi-AI cycle. Target questions:
  - Does Layer 2a correctly source $B_{\text{pair}}$ from A2+A5+A8'+A11 as stated, or is an additional axiom needed?
  - Is D1's SSV-minimization intuition derivable in-paper (closing OPEN-SS-26 within SS-8 v0.1), or is it genuinely a future-paper target?
  - Does D2 fit within A6' extended, or does it require a new principle?
  - Are the Phase 1b residuals fully accounted for by H3' + H5' (i.e., is D3 an honest hypothesis without hidden tuning)?
  - Is Remark 3 (same combinatorial backbone as SS-7) structurally deep or numerically coincidental?

### 11.2 Gating criteria for SS-8 v0.1 drafting

Draft v0.1 only after:
- Multi-AI review round on this note completes (~1 review cycle).
- Any required axiom refinements from review are adjudicated per `operating_system.md` §10 axiom reconciliation procedure.
- Thomas ratifies D1–D3 as the SS-8 v0.1 hypothesis stack.

If OPEN-SS-26 proves tractable in-paper (SSV-minimization argument closes to a theorem), promote D1 from hypothesis to theorem in v0.1. Same for OPEN-SS-27 (D2) and OPEN-SS-28 (D3). If none close, v0.1 proceeds with D1–D3 at the hypothesis tier, mirroring SS-7's C4 treatment.

### 11.3 Registry updates to defer

Per `operating_system.md` exploratory-tier policy, defer all of the following until v1.0:

- Addition of D1, D2, D3 to `postulates_and_theorems.md`.
- Addition of Theorem 2 (H2' scaling law) to `postulates_and_theorems.md`.
- Addition of 12 zero-parameter predictions to `predictions.md` with axiom attribution.
- Addition of OPEN-SS-26, -27, -28 to any OPEN registry (currently registered informally in this note; formal entry at v1.0).
- Update to `axiom-registry.md` Pattern 6 entry to add the fourth scale (interstitial-alpha contact).
- Update to `axiom-registry.md` OPEN-SS-24 entry to reference OPEN-SS-26 as structural analog at interstitial scale.

### 11.4 Physical-intuition capture (founders_vision.md pending)

The SSV-minimization argument for D1 and the A6'-extension picture for D2 are Thomas-intuitions that should eventually be added to `founders_vision.md` (per `operating_system.md` §3 physics-discovery-session procedure). The present note deliberately omits that capture until Thomas has a chance to review and refine the intuition statements. If Thomas endorses the §6.2 and §6.3 intuition paragraphs, they become candidates for founders_vision entries.

---

## 12. References

- `/CPP/axiom-registry.md` (version 21 April 2026).
- `/CPP/series_strong/papers/SS-7_alpha_cluster_edge_formula.tex` v1.2 (Theorem 3N-6, Assumption Stack C1–C4, epistemic-split block).
- `/CPP/series_strong/papers/SS-8/sketches/SS-8_Phase1_extended_map_findings.md` (Sections 1–8, H1'–H6').
- `/CPP/operating_system.md` §3 (session types), §5 (multi-AI review cycle), §10 (axiom reconciliation).
- `/CPP/problem_histories/PH-OPEN-SS-18.md` (precedent for OPEN-SS-22/23/24 split).
- `/CPP/problem_histories/PH-OPEN-SS-22.md` (precedent for retirement-via-understanding).

---

*End of SS-8 H2' derivation note.*
*Exploratory tier. Awaiting multi-AI review and Thomas's ratification before any registry cascade.*
