# CPP Theorem Dependency Graph

**Location:** `/CPP/theorem-dependency-graph.md`
**Purpose:** Programme-level dependency map for all formal mathematical objects in the CPP programme (theorems, propositions, lemmas, corollaries). Companion to `theorem-registry.md` (which gives full mathematical statements) — this document maps the inheritance and load-bearing relationships *between* the formal objects so that the programme's logical structure is navigable at a glance.

**Adopted:** 11 May 2026 (Session 79, patch 0340) following ChatGPT's suggestion in the SF-4 v4.3 review that "future flagship papers may benefit from a short dependency DAG figure, or a theorem dependency table." This document is the table form; a rendered DAG figure may be added later if the theorem count grows past where readability requires visualization.

**Format:** Sector-organized sections; each formal object gets a paragraph or bullet block listing its dependencies (Depends On), its downstream consumers (Downstream), and any notable methodological flags (cross-sector closure, conditional theorem closure level, etc.).

**Maintenance:** Update at each flagship-paper SHIP or version increment that adds a new theorem or upgrades closure level. The update is a required step in the `templates/paper_completion_checklist.md` SHIP-mechanics sequence going forward.

---

## SS-line (Substrate Structure)

Sources: SS-2 (Lattice-Scale Grounding), SS-3 (SU(3) Uniqueness from Tetrahedral Cage), SS-4 (String Tension), SS-5 (Deuteron Binding Energy), SS-6 (Linear Cage Series), SS-7 (Isotope Binding-Energy Series), SS-8 (Tetrahedral Cage Architecture), SS-9 (Cooperative Binding).

**THEO-SS-1 through THEO-SS-10**: SS-2 core theorems on lattice-scale grounding and nucleon structure. Depend on AXIM-1 (DI-bit exchange), AXIM-2 (substrate-stress framework), AXIM-7 (substrate-stress vector), and the 600-cell distance-shell structure (geometric FI). Downstream: load-bearing for the entire SM-line (the mass quantum $M_0 = m_e \cdot z/\phi$ is established here via five independent convergence routes).

**PROP-SS-11**: SS-7 v1.2 proposition on isotope binding-energy scaling. Depends on THEO-SS-1 through THEO-SS-6 (lattice scale + nucleon structure). Downstream: enables SS-7 → SS-8 cage architecture extension.

**THEO-SS-12**: SS-7 v1.2 theorem on isotope-selection corrections. Depends on PROP-SS-11. Downstream: SS-8 cage architecture (THEO-SS-13 through THEO-SS-15).

**THEO-SS-13** (Euler-degree theorem): SS-8 v1.0 core theorem on cage architecture topology. Depends on AXIM-7. Downstream: THEO-SS-14, THEO-SS-15.

**THEO-SS-14** (D1 conditional vertex localization, Level-1+2 independence): SS-8 v1.0 conditional theorem on paper-level hypotheses C1-C4 + D1-D3. **Conditional theorem closure**: depends on paper-level structural hypotheses, not unconditional from CPP axiom set. Depends on THEO-SS-13. Downstream: THEO-SS-15.

**THEO-SS-15** (2E/V interstitial scaling law): SS-8 v1.0 conditional theorem. **Conditional theorem closure**: same conditionality structure as THEO-SS-14. Depends on THEO-SS-13, THEO-SS-14, hypotheses C1-C4 + D1-D3.

**THEO-SS-16**: SS-9 main theorem on cooperative binding. Depends on hypothesis stack C1-C8 (SS-9 paper-level hypotheses). Downstream: provides the cage-cooperative SSV reinforcement FI used by SF-4 v3.0 ($\alpha$-exponent reduction, FI-$\alpha$-2).

## SM-line (Standard Model Series)

Sources: SM-1 (Particle-Type Cage Taxonomy), SM-2 (Substrate-Stress Cascade), SM-3 (SU(3) and the Tetrahedral Cage), SM-4 (Charged-Lepton K3-Vertex Identification), SM-5 (Neutrino Sector Foundations), SM-7 through SM-9 (Bound-Mode Mass Formula Machinery), SM-8 (Heavy Quark Mass Spectrum).

**THEO-SM-1** (Particle-type cage taxonomy): SM-1 main theorem. Depends on THEO-SS-1 through THEO-SS-10 (lattice geometry). Downstream: THEO-SF-4-5 clause (iii) (via FI-K-3 K3 base structure inheritance); THEO-SF-4-1 (V=20 exclusion for neutrinos).

**THEO-SM-2** (Substrate-stress cascade): SM-2 main theorem. Depends on AXIM-7 + 600-cell distance-shell structure. Downstream: provides framework for the SM-9 §7.2 cascade structure used by SF-4 v3.0 ($\alpha$-exponent reduction).

**THEO-SM-3** (SU(3) uniqueness from tetrahedral cage): SM-3 main theorem. Depends on AXIM-2, AXIM-4 + 600-cell geometry. Downstream: THEO-SF-4-1 (K3 spectrum FI-K-1); THEO-SF-4-5 (via FI-K-1).

**THEO-SM-4** (Charged-lepton K3-vertex identification): SM-4 main theorem. Depends on AXIM-2, AXIM-4; THEO-SM-1; THEO-SM-3. Downstream: THEO-SF-4-1, THEO-SF-4-5 (via FI-K-6 charged-lepton K3-vertex identification — the load-bearing FI that breaks $S_3$ to $S_2(V_k)$ in the cross-sector closure).

**THEO-SM-5** (Neutrino sector foundations): SM-5 main theorem. Depends on AXIM-2, AXIM-4; THEO-SM-3, THEO-SM-4. Downstream: THEO-SF-4-1, THEO-SF-4-3, PROP-SF-4-2, THEO-SF-4-5 (via FI-K-2 neutrino identification). **Note:** SM-5's foundational open problem op:nu_id (K3-eigenmode identification from CPP interaction rules) is **conditionally resolved cross-sector at v4.0 via THEO-SF-4-5**; SM-5 itself is unchanged at the paper level but inherits the resolution via the cross-sector closure.

**THEO-SM8-1, THEO-SM8-2, THEO-SM8-3**: SM-8 v1.0 theorems on heavy quark mass spectrum. Depend on SM-7 mass quantum + 600-cell geometry. Downstream: provides M_0 calibration used by SF-4 v3.0+ ($\alpha$-exponent reduction, $m_\text{unbound} = M_0 \cdot V^2 \cdot \sigma_\nu$).

**THEO-SM9-1**: SM-9 cooperative binding theorem extending SM-7/SM-8. Depends on SM-7 + SM-8 theorems + SS-9 cooperative binding (THEO-SS-16). Downstream: SF-4 v3.0 ($\alpha$-exponent reduction; the SM-9 §7.2 cascade structure is FI-$\alpha$-1; $V^{7/3}/N_\text{links}$ per-link amplification).

**CORL-SM-1, CORL-SM-2, CORL-SM-3, CORL-SM-4**: SM-line corollaries flowing from the main theorems. Specific dependencies registered in `theorem-registry.md`.

## SF-line (Flagship synthesis)

Sources: SF-4 (Neutrino Sector Unification from 600-Cell Geometry), v4.3 SHIP-ready 11 May 2026.

**THEO-SF-4-1** (K3-Cage-Shell Consistency, three-clause theorem): Depends on AXIM-2, AXIM-4; THEO-SM-3, THEO-SM-4; THEO-SF-4-5 (clause (iii)). Clauses (i)+(ii) exact at zeroth order. Clause (iii) at v1.0-v3.0 was at SM-5-inheritance level (depended on SM-5 op:nu_id ansatz); at v4.0 closes at **conditional theorem closure level** via THEO-SF-4-5. Downstream: PROP-SF-4-2, THEO-SF-4-3.

**PROP-SF-4-2** ($\mu\tau$-exchange symmetry of mass operator): Depends on AXIM-2, AXIM-4; THEO-SM-4; THEO-SF-4-1. Exact result. Downstream: THEO-SF-4-3.

**THEO-SF-4-3** (Exact recovery of TBM angles): Depends on AXIM-2, AXIM-4; THEO-SM-4; PROP-SF-4-2. Tautological by construction (the assignment is in mass basis with TBM as the change-of-basis to flavor basis). Downstream: SF-4 predictions table (mixing angles).

**THEO-SF-4-4** ($\alpha$-Exponent Reduction at the Bound/Unbound Boundary, Theorem 3.1 of v3.0+): **Conditional theorem closure**. Depends on AXIM-1, AXIM-2, AXIM-4, AXIM-6', AXIM-7, AXIM-9; THEO-SM-7, THEO-SM-9 (and through them THEO-SS-1 through THEO-SS-10); LEMMA-SF-4-1 (supporting). FI stack (4): FI-$\alpha$-1 SM-9-inheritance for $V^{7/3}$; FI-$\alpha$-2 cage-cooperative SSV reinforcement framework; FI-$\alpha$-3 neutrino as unbound 3D orbital ZBW; FI-$\alpha$-4 rigid-cage operational definition with central-anchor condition. **Resolves OPEN-FP-SF-4-1** at conditional theorem closure level. Downstream: THEO-SF-4-5 (via FI-K-5 SF-4 v3.0 mass formula).

**LEMMA-SF-4-1** (No-Anchor Correlator Suppression, Lemma 3.1 of v4.1+): Supporting lemma for THEO-SF-4-4 sub-claim (c). Depends on AXIM-4, AXIM-7; FI-$\alpha$-3 (no-anchor structural condition). Established at v4.1 in response to ChatGPT v4.0 review (the lemma made explicit the implicit A4 → correlator-suppression step). Downstream: THEO-SF-4-4 sub-claim (c).

**THEO-SF-4-5** (Composite K3-Cage-Shell Coupling Theorem, Theorem 5.2 of v4.0+): **Conditional theorem closure**; **first cross-sector closure in CPP**. Depends on AXIM-1, AXIM-4, AXIM-7, AXIM-9 (A1+A7+A9 most load-bearing); THEO-SM-1, THEO-SM-3, THEO-SM-4, THEO-SM-5; THEO-SF-4-4 (via FI-K-5). FI stack (6): FI-K-1 K3 spectrum from SM-3; FI-K-2 neutrino identification from SM-5; FI-K-3 K3 base structure from SM-1; FI-K-4 600-cell distance-shell structure; FI-K-5 SF-4 v3.0 cage-shell mass formula = THEO-SF-4-4; FI-K-6 charged-lepton K3-vertex identification from SM-4. **Simultaneously resolves OPEN-FP-SF-4-2 (vertex-by-vertex K3-Cage-Shell Consistency) AND SM-5's op:nu_id (foundational open problem of CPP neutrino sector)** — first cross-sector closure in CPP via Finding $\beta$-10 methodology. Downstream: THEO-SF-4-1 clause (iii) upgrade to conditional theorem closure level.

## EW-line (Electroweak)

Sources: EW-1 through EW-5 (electroweak sector theorems on the W/Z boson cage-binding structure, the Weinberg angle from substrate geometry, parity-violation mechanism, gauge-boson masses from the icosahedral first shell).

**THEO-EW-1 through THEO-EW-8**: Depend on AXIM-1, AXIM-2, AXIM-4, AXIM-7 + 600-cell first-shell (icosahedral) geometry. Downstream: provides cage-boson identification for W$^\pm$ (icosahedral shell, V=12) and Z (dodecahedral shell). Note that THEO-EW-1 through THEO-EW-8 are paper-level theorems within the EW-line; their specific dependencies and the OP-SM-7d open problem (Capotauro mechanism for $\delta_{CP}$ and TBM-angle corrections) are registered in `theorem-registry.md`. The OP-SM-7d closure is a candidate for the next cross-sector closure in CPP (SF-2 EW flagship ↔ SM-5 OP-SM-4).

## QM-line (Quantum Mechanics)

Sources: QM-1 through QM-6 + QM-7 through QM-10 (quantum-mechanical structure from CPP: wavefunction collapse, Born rule, entanglement, decoherence, etc.).

**THEO-QM-1 through THEO-QM-10**: Depend on AXIM-1, AXIM-3, AXIM-5, AXIM-7 + substrate dynamics. Downstream: cross-references to specific theorems are registered in `theorem-registry.md`. Note that QM-line theorems include three corollaries (CORL-QM-1, CORL-QM-2, CORL-QM-3) and two cross-corollaries (CORL-1a, CORL-1b).

## SD-line (Foundations / Special Domains)

Sources: SD-1 through SD-10 (foundations theorems covering consciousness-substrate interaction, identity persistence, CP individuation, etc.).

**THEO-SD-1 through THEO-SD-10**: Depend on the full CPP axiom set + substrate dynamics. Downstream: SD-line theorems are typically programme-foundational rather than feeding specific physics-sector closures.

**THEO-1**: Cross-line theorem; specific dependencies in `theorem-registry.md`.

## Cross-sector and partner-switching theorems

**Partner-switching theorems**: Three formal objects covering the partner-switching mechanism (the substrate-level binding-rebinding dynamics that produces ZBW). Cross-line dependencies; specific registrations in `theorem-registry.md`.

## Summary statistics (post-SF-4 v4.3, 11 May 2026)

- **SS-line**: 14 theorems + 1 proposition + 1 theorem at SS-9 conditional level = 16 (counting all THEO-SS-* and PROP-SS-*).
- **SM-line**: 9 theorems + 4 corollaries (CORL-SM-1 through CORL-SM-4) = 13 entries.
- **SF-line**: 4 theorems + 1 proposition + 1 lemma = 6 entries (the most recently expanded sector).
- **EW-line**: 8 theorems.
- **QM-line**: 10 theorems + 3 corollaries (CORL-QM-*) + 2 cross-corollaries (CORL-1a, CORL-1b) = 15 entries.
- **SD-line**: 10 theorems.
- **Partner-switching**: 3 entries.
- **Cross-line (THEO-1)**: 1 theorem.
- **Programme total**: 56 theorems + 1 proposition + 1 lemma + 9 corollaries = 67 entries.

## Methodological notes

**Conditional theorem closure**: A theorem-level closure that depends on a named stack of foundational inputs (FIs) plus a named subset of CPP axioms. SF-4's v3.0 closure (THEO-SF-4-4) has 4 FIs; SF-4's v4.0 cross-sector closure (THEO-SF-4-5) has 6 FIs. SS-9's THEO-SS-16 closes at conditional theorem closure on hypothesis stack C1-C8. SS-8's THEO-SS-14 and THEO-SS-15 close at conditional theorem closure on hypotheses C1-C4 + D1-D3. See `templates/conditional_closure_framework.md` for the programme-level convention.

**Cross-sector closure**: A single derivation chain that simultaneously resolves open problems in two or more distinct papers. First instance: THEO-SF-4-5 resolves SF-4's OPEN-FP-SF-4-2 and SM-5's op:nu_id jointly (v4.0, 10 May 2026). Methodology registered as Finding $\beta$-10. Candidate future pairs: SF-2 ↔ SM-5 OP-SM-4 ($\delta_{CP}$ via Capotauro); SS-corpus ↔ SF-5 (strong unification); SR-corpus ↔ SF-6 (electromagnetism).

**FI accounting**: Each FI is named, traceable to its derivation source, and counted toward the inheritance scope of the closure. Higher FI counts reflect wider cross-paper inheritance, not weaker closure. See `templates/conditional_closure_framework.md` § 2 for the accounting convention.

---

**Related programme documents:**
- `theorem-registry.md` — formal statements of all theorems; this document maps dependencies *between* them.
- `templates/conditional_closure_framework.md` — programme-level methodology for conditional closure and FI accounting.
- `axiom-registry.md` — the CPP axiom set (AXIM-1 through AXIM-11 + the 6-axiom set from `postulates_and_theorems.md`).
- `paper_catalog.md` — per-paper inventory with version history and OSF/arXiv status.

**Future enhancement (deferred):** A rendered DAG figure (Mermaid or Graphviz syntax) for visual inspection of inheritance patterns. Useful once theorem density grows past where the bullet-list form becomes hard to scan. Not required for current programme size (~67 entries).
