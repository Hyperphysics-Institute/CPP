# SS-9 — Per-Paper Subfolder

SS-9 (working title: *Conditional Derivation of Simplicial Alpha-Polytope Connectivity from CPP Lattice Geometry*) is the SS-9 candidate paper targeted by OPEN-SS-24 (first-principles derivation of simplicial contact structure for alpha-cluster nuclei). The subfolder was created on 26 April 2026 Session 3 to provide stable housing for the substantive artifacts accumulating across the development arc. As of subfolder creation, no .tex/.pdf paper file exists yet — SS-9 is at exploratory/scaffold stage.

**Important pre-paper note.** The subfolder was created early (pre-v1.0) because Sessions 1–3 produced enough substantive content (working draft, multi-faceted-rigidity refinement, registry entries, residual-fingerprint analysis) that housing it in `session_logs/` alone was no longer adequate. The four-tier documentation discipline (reasoning → development → transcript pointer-map → pre-paper artifacts) is in place ahead of the paper text itself. This is a deliberate deviation from the implicit convention that subfolders are created at v1.0; OPEN-ORG-009 documents the convention amendment.

## Current state

- **No paper text yet.** The active scaffold is now `session_logs/OPEN-SS-24_phase1_v0.3_working_draft.md` (Session 4 restructuring: graph-theoretic Lemma B$'$ via C7 + Steinitz; v0.2 supporting-hyperplane gap dissolved; refined-C1 facet (b) made load-bearing for FvdW realization at $N_\alpha \geq 7$; new C7 hypothesis registered as OPEN-SS-33 candidate). The earlier `session_logs/OPEN-SS-24_phase1_v0.2_working_draft.md` (Session 2 Steinitz pivot + Lemma A clean + Lemma B with two registered gaps + conditional Theorem statement + deltahedra-gap scope notes) is preserved as historical artifact recording the v0.2 framing that motivated Session 3's refined-C1 work and Session 4's Lemma-B restructuring. When SS-9 v0.1 is drafted, the paper .tex will land at `series_strong/papers/SS-9/SS-9_simplicial_alpha_polytope_connectivity.tex` (working title; final title TBD) and the working draft will move to `sketches/`.
- **Foundation work landed.** SS-7 v1.3 patched (multi-faceted-rigidity refinement of C1) at `series_strong/papers/SS-7/SS-7_alpha_cluster_edge_formula.tex`. This is the foundation v0.3's Lemma B$'$ rests on; refined-C1 facet (b) is load-bearing in Theorem clause (iv).
- **Registry entries pending ratification.** OPEN-SS-29 (programme-level closure of C5), OPEN-SS-30 (programme-level closure of C6), OPEN-SS-31 (deltahedra-gap structural realization), OPEN-SS-32 (cluster-level oblate-deformation slip-plane mode), **OPEN-SS-33 (programme-level closure of C7 contact-graph planarity, NEW Session 4)** all in `Research_Frontier.md`. Forward-looking predictions PRED-O-16/17/18 (slip-plane single-cluster extension, single-to-hierarchical transition, hierarchical additivity) in `predictions.md`.

## Layout

```
SS-9/
├── SS-9-README.md                                          ← this file
├── (paper .tex/.pdf — does not yet exist)
├── reviews/                                                ← reviewer correspondence (empty; pending external review)
├── letters/                                                ← Opus correspondence (empty; none yet)
├── sketches/                                               ← derivation notes, exploratory analyses
│   └── SS-9_table1_residual_fingerprint.md                ← SS-7 Table 1 residual decomposition into Regime A/B/icosahedron/Regime C; foundation for OPEN-SS-32 slip-plane mechanism
├── scripts/                                                ← Python verification scripts (empty; none yet)
├── founders_voice/                                         ← Thomas's recorded intuitions
│   └── 001_slip_plane_intuition.md                        ← Thomas's 26 April 2026 Session 3 articulation of the bulk-distortion / slip-plane / tectonic-plate reading; the load-bearing physical insight that motivated OPEN-SS-32 mechanism reading
└── documentation_suite/                                    ← four-tier documentation (reasoning + development + transcript + future doc-suite)
    ├── reasoning-SS-9.md                                   ← Tier 4: full Opus substantive reasoning verbatim, housekeeping excluded; canonical source
    ├── development-SS-9.md                                 ← Tier 3: curated vignettes summarizing substantive transactions
    ├── transcript-SS-9.md                                  ← Tier 2: pointer-map indexing all transactions
    └── (paper-level doc-suite files — mechanism/glossary/phenomena/philosophy/keywords/reviews/FAQ/lay-summary — to be produced at Trigger 2 paper completion)
```

Three of six standard subfolders are empty (`reviews/`, `letters/`, `scripts/`) and carry `.gitkeep` placeholders. They will be populated as artifacts arrive: `letters/` once Opus drafts review-request correspondence, `reviews/` once external reviewers (Copilot/Grok/Sonnet/ChatGPT) respond, `scripts/` if/when numerical verification work is needed for the Lemma B gap closure or OPEN-SS-32 derivation.

## Cross-references

- **OPEN-SS-24** target: `Research_Frontier.md` MEDIUM-HIGH priority. Closure delivers C4 from CPP primitives; promotes 54 conditional D-N predictions to unconditional.
- **OPEN-SS-32** registered: cluster-level oblate-deformation slip-plane mode (provisional, pending derivation). Methodologically parallel to SS-8's OPEN-SS-28.
- **PRED-O-16/17/18** registered: forward-looking predictions for higher-N_α alpha-chain nuclei; testable against AME 2020 once SS-7 Table 1 is extended.
- **SS-7 v1.3**: refined C1 with multi-faceted rigidity (facets a/b/c). Foundation for SS-9 closure attempt.
- **SS-8 v1.0** H3': structural analog of OPEN-SS-32 at the interstitial scale. Cross-paper consilience anchors the slip-plane mechanism reading in the K_3 scale-recurrence (Pattern 6).

## Session log sequence

The session-log-as-handover discipline (operating_system.md §4) means the running handover for OPEN-SS-24 / SS-9 is the chronological session log sequence:

1. `session_logs/OPEN-SS-24_handover.md` (Session 1, 26 April 2026) — preserved as historical bootstrap; pre-§4-discipline genre.
2. `session_logs/2026-04-26_session_log_2.md` (Session 2) — v0.2 conditional-C4 closure scaffold; Steinitz pivot; deltahedra-gap insight; Template-A theoretical-development with parallel Template-B for OS codification.
3. `session_logs/2026-04-26_session_log_3.md` (Session 3) — off-track investigation of alpha rigidity; multi-faceted-rigidity refinement of C1; OPEN-SS-32 registered; PRED-O-16/17/18 registered; SS-7 v1.3 patched; subfolder created (this README produced).
4. `session_logs/2026-05-02_session_log.md` (Session 4) — v0.3 working draft produced; Lemma B$'$ graph-theoretic restructuring via C7 + Steinitz; v0.2 supporting-hyperplane gap dissolved; refined-C1 facet (b) integrated as load-bearing in Theorem clause (iv); new C7 hypothesis registered with OPEN-SS-33 candidate.

The next OPUS picking up OPEN-SS-24 closure should read these four logs in order, then this README, then the four documentation_suite/ files, then continue the v0.3 → v0.1 paper-text transition (or attempt Phase 4 programme-level closure of any of OPEN-SS-29/30/31/32/33 if the v0.3 conditional-theorem structure feels solid enough to ship as outline).
