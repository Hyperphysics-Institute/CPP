# SF-2: Electroweak Sector Audit — Cage Bosons Against Current Corpus

**Status:** DRAFT — solo first-pass (Session 82, Mode B per Thomas's selection)
**Track:** SF-2 (Electroweak Cage-Boson Unification flagship paper) — Phase 1 pre-survey
**Author:** Claude Opus 4.7 (audit), Thomas Lee Abshier ND (strategic frame; corrections pending)
**Established:** 11 May 2026 (Session 82)
**Reading-pass basis:** EW-1 through EW-5 .tex files (5 papers, 1586 source lines); mechanism-EW-1 through mechanism-EW-5 (~310 lines); development-EW-1 through development-EW-5 (~270 lines); FAQ-EW-1, FAQ-EW-2, phenomena-EW-1 (selective); README-EW.md; FINAL-STATUS-1-April-2026.md
**Integration target:** Foundation document for SF-2 paper drafting; informs the eight-phase SF-2 campaign per `SESSION_81_HANDOVER_FOR_NEXT_CONTEXT.md`. Inputs to: SF-2 outline (Phase 2), W⁰ sub-derivation (Phase 3), cage-shape derivations (Phase 4), v0.1 drafting (Phase 5). Cross-references SF-4 audit precedent at `flagship_papers/neutrinos/sketches/SF-4_neutrino_sector_audit.md`.
**Posture:** This document does not select mechanisms. It inventories what each EW paper establishes, what is fitted, what is derived, what propagates into SF-2, what transfers to SF-6, and what is missing for SF-2 v1.0 SHIP — flagging items requiring Thomas's physical-intuition input on the corrections pass.

---

## §1. Strategic frame

SF-2 is the second SF-line flagship after SF-4. Its inclusion-criterion fit per `flagship_papers/electroweak/README.md` is:

1. **Named known-unknown** — the Weinberg angle, electroweak symmetry breaking, the W/Z mass relation, the Higgs origin
2. **Forced-choice prediction** — the W⁰ as a CPP-novel particle (CONJ-EW-W0)
3. **Cross-domain unification** — the four cage bosons (W±, W⁰, Z, H) as a single geometric family

The Session 41 architectural revision (patch 0301) narrowed SF-2's scope to **cage bosons only**: photon dynamics transfer to SF-6 (electromagnetism flagship), gluon dynamics transfer to SF-5 (strong-sector unification flagship). The EW corpus (EW-1 through EW-5, dated 2 April 2026) was written *before* this separation. Most of EW-1 through EW-5 is on-scope for SF-2; portions of EW-1 and EW-5 covering the photon channel and the abelian U(1)_Y emergence belong to SF-6.

The strategic posture inherits from SF-4: **conditional-closure framework from day one, FI accounting at every boundary, "RESOLVED" terminology read in conditional sense by default, multi-reviewer convergence at SHIP, Binary Artifact Workflow** (`templates/operating_system.md` §13). SF-4 had to crystallize these methodology conventions mid-campaign at v4.2; SF-2 inherits them codified.

The cardinal rule from the SESSION_81 handover: **W⁰ characterization at forced-choice-prediction level is the gate to v0.1 drafting.** Without bracelet geometry + W⁰ mass + W⁰-to-W± binding mechanism + experimental signature derived to theorem-equivalent level, SF-2 cannot reach v0.1. This audit's load-bearing output is §7 (the W⁰ runway).

---

## §2. SF-2 scope: the four cage bosons

| Particle | Cage geometry | Vertices | Coupling | Mass (PDG 2026) | Status in EW corpus |
|----------|---------------|----------|----------|-----------------|---------------------|
| **W±** | Bracelet (6 hDPs, open interior) | 12 CPs | V−A (75% LH) | 80.377 ± 0.012 GeV | EW-2 |
| **W⁰** | Bracelet — **CPP-novel** | 12 CPs | TBD | TBD (sub-W± scale?) | EW-2 §1, §2 |
| **Z** | Icosahedral closed loop | 12 vertices | Axial-vector | 91.1876 ± 0.0021 GeV | EW-3 |
| **H** | Dodecahedral closed shell | 20 vertices | Scalar (J=0) | 125.10 ± 0.20 GeV | EW-4 |

The unifying architectural insight (mechanism-EW-1 Part 1) is the **eigenvalue–topology correspondence**: the 600-cell adjacency matrix has six distinct eigenvalues
$$
\lambda \in \{12,\ 1+\varphi,\ \varphi-1,\ 1-\varphi,\ -\varphi,\ -(1+\varphi)\}
$$
each selecting a stable closed subgraph. The three EW boson topologies correspond to three of these six:

- $\lambda = 12$ (ground state, all-ones eigenvector, max symmetry) → **Z icosahedral 12-vertex loop**
- $\lambda \in \{1+\varphi,\ \varphi-1\}$ (intermediate positive pair) → **W bracelet 12-CP 6-hDP ring**
- $\lambda = -(1+\varphi)$ (most frustrated, max anti-correlation) → **H dodecahedral 20-vertex shell**
- $\lambda \in \{1-\varphi,\ -\varphi\}$ (excited modes of dodecahedral geometry) → **NO additional boson** (eigenvalue gap = mass gap prediction)

This is the seed of theorem-level cage-shape derivation that SF-2's Phase 4 must lift to rigorous status. The current EW-1 framing asserts the correspondence; whether it rises to theorem level under SF-line standards depends on whether each eigenvalue–topology pairing is *forced* (unique stable closed subgraph) or *selected* (one of several candidates). **[FLAG-1 for Thomas: is the bracelet ↔ {1+φ, φ−1} mapping uniquely forced by lattice spectrum, or one of multiple candidates that the EW corpus selected by argument? The mechanism file claims unique; the .tex paper EW-1 §2.1 says only "selects the 12-vertex configuration that closes into a hexagonal bracelet."]**

---

## §3. Derivation grade per EW paper

Adopting the SF-4 Claim Status Ledger conventions: **THEOREM** (proved at theorem level, no calibration), **STRUCTURAL ARGUMENT** (mechanism identified, quantitative result reproduced via calibration), **WORKING HYPOTHESIS** (registered but not closed), **SKETCH** (narrative-level only).

### §3.1 EW-1 (Electroweak Introduction): the framework paper

| Result | Grade | Notes |
|--------|-------|-------|
| Six 600-cell eigenvalues → boson topology selection | STRUCTURAL ARGUMENT | Asserted as theorems THEO-EW-1/-2/-3 in mechanism files; .tex paper presents as identification, not derivation of uniqueness |
| φ⁻³ ≈ 0.236 geometric dilution from shell-radius scaling | THEOREM-equivalent | Genuinely derived from 1:φ:φ² 600-cell shell structure; zero parameters |
| Holographic dilution η ~ 10⁻¹⁷ (Planck → weak scale residual) | WORKING HYPOTHESIS | OPEN-P-EW-1; argued from N ~ 10⁶¹ cosmic-horizon GPs but not derived |
| sin²θ_W = 0.2312 via four-layer p_k = (1−k/5)² | **SUPERSEDED** | SM-6 supersedes with $\sin^2\theta_W = 3/(8\varphi)$ at zero parameters; EW-1's MC framework had g' reverse-engineered to target (honesty note in phenomena-EW-V1, 31 March 2026 audit) |
| W⁰/W± distinction (CPP-specific) | WORKING HYPOTHESIS | Asserted but not derived; CONJ-EW-W0 registered in Research_Frontier as result of Session 41 |
| No boson between m_Z and m_H (eigenvalue gap prediction) | STRUCTURAL ARGUMENT | Falsifier-grade prediction consistent with LHC data through 2026 |

**EW-1 inheritance into SF-2**: the eigenvalue–topology framework is load-bearing. The Weinberg-angle derivation is REPLACED by SM-6. The φ⁻³ factor stays. The η problem propagates to SF-2 as OPEN-FP-SF-2-* (see §6).

### §3.2 EW-2 (W boson): the W± and W⁰ paper

| Result | Grade | Notes |
|--------|-------|-------|
| W bracelet topology from λ = {1+φ, φ−1} | STRUCTURAL ARGUMENT | mechanism-EW-2 Step 1 asserts "unique stable closed subgraph"; .tex EW-2 §2.1 less strong |
| Bracelet CP placement: 3×(±eCP), 3×(±qCP), Q=0 net | THEOREM-equivalent | Forced by Nexus alternating-polarity rule and net-zero constraint |
| Bracelet open-interior → reactive (vs Z/H closed → inert) | STRUCTURAL ARGUMENT | Topological distinction; physical claim is that open interior allows external CPs to enter |
| W⁰ spontaneous DP-Sea assembly at STP | WORKING HYPOTHESIS | Asserted; no formation-rate or stability calculation in EW-2 |
| W⁰ → W± charge acquisition via collision | SKETCH | Phenomenological Nexus charge-bookkeeping narrative; no binding-energy calculation |
| Left-handed 75% from 120°/240° bias: $P_L^{\rm eff} = 1 - \sin^2(60°) = 0.25$ | STRUCTURAL ARGUMENT | Specific numerical result; full continuum-limit 75%→100% claimed (FAQ-EW-2 Q3) but not proved |
| W mass m_W = 80.377 GeV | REPRODUCED (calibrated) | Uses sea_strength=0.185 (calibrated from neutron neutrality), hybrid_weak_factor=1.5 (3-weak-layers/2-EM-polarities heuristic), η~10⁻¹⁷ (op:dilution OPEN); r_max−r_min=3.5 l_P; f_geom = 1.5 × 1 × φ⁻⁴ = 0.219 |
| **Self-honesty correction (v3 → v3.1, mechanism-EW-2 Step 10)** | — | v3 reported error sensitivities ±0.010, ±0.008, ±0.004 GeV that were **back-calculated to match PDG uncertainty, not derived from the mass formula**. v3.1 corrected: formula sensitivities are ±4-6 GeV per ±5% parameter variation. MC averaging over 10⁶ events reduces SEM but does not reduce formula sensitivity. *Honest implication: m_W is reproduced by calibration of η, not derived.* |
| W decay channels (W→ℓν, W→qq̄') and Γ_W = 2.085 GeV | REPRODUCED | Branching ratios match SM phenomenology; mechanism is bracelet bit-dissociation |
| CDF W-mass anomaly partial resolution | SKETCH / Tier 4 | Listed as candidate mechanism (hybrid eCP/qCP contributions), not proved result |

**EW-2 inheritance into SF-2**: bracelet topology stays. CP placement stays. Reactive-vs-inert distinction stays. **W⁰ formation, W⁰ mass, W⁰ → W± binding mechanism, W⁰ experimental signature** are the four W⁰ sub-derivation gates (CONJ-EW-W0) that Phase 3 of SF-2 must close — see §7. The v3.1 honesty correction sets a precedent for SF-2: error sensitivities from formula, not back-calculated from PDG.

### §3.3 EW-3 (Z boson): the icosahedral closed loop

| Result | Grade | Notes |
|--------|-------|-------|
| Z icosahedral 12-vertex loop topology from λ = 12 | STRUCTURAL ARGUMENT | Same caveat as W-bracelet: uniqueness claim in mechanism file stronger than in .tex |
| Closure → no reactive openings → neutral currents only | STRUCTURAL ARGUMENT | Topological derivation of "Z does not change fermion identity" — strongest single mechanism in EW-3 |
| Loop density factor ℓ_Z (ideal 1.437, effective 1.2) | WORKING HYPOTHESIS | op:loopfactor OPEN: 1.437 from $1 + 1/n_v^{1/3}$ ideal; reduction to 1.2 attributed to 4D→3D stereographic projection losses, not derived. OPEN-P-EW-3 |
| Axial-vector coupling from 4-layer symmetric phase interference | STRUCTURAL ARGUMENT | Sketch-level mechanism using "three interlocked tetrahedra"; specific 0°/120°/240°/360° phase enumeration |
| Z mass m_Z = 91.1876 GeV | REPRODUCED (calibrated) | f_geom^Z = 1.5 × 1 × φ⁻⁴ × 1.2 = 0.263; same r_max−r_min=3.5 l_P; η calibrated independently to m_Z |
| m_Z/m_W predicted ratio 1.20 vs observed 1.134 (5% off) | WORKING HYPOTHESIS | op:mzw_ratio OPEN-P-EW-4; loop density alone insufficient |
| Tree-level self-consistency $m_Z/m_W = 1/\cos\theta_W = 1.140$ vs observed 1.134 | STRUCTURAL ARGUMENT | **0.5% agreement; strongest internal cross-check in EW series** (per development-EW-3, phenomena-EW-V2). Independent of mass-formula calibration |

**EW-3 inheritance into SF-2**: icosahedral cage shape stays. Loop density factor is a known gap. The 5% m_Z/m_W discrepancy is a SF-2 closure target. The tree-level self-consistency cross-check is the precedent for SF-2's internal-coherence demonstration.

### §3.4 EW-4 (Higgs): the dodecahedral shell

| Result | Grade | Notes |
|--------|-------|-------|
| H dodecahedral 20-vertex shell from λ = −(1+φ) | STRUCTURAL ARGUMENT | Most frustrated eigenvalue → maximum confinement energy → max mass; framing strongest of EW corpus |
| Icosahedron–dodecahedron duality (12-vertex Z dual to 20-face dodecahedron / 20-vertex H) | THEOREM-equivalent | Standard polyhedral duality |
| Scalar J=0 from A₅ symmetry | THEOREM-equivalent | **A₅ has no non-trivial reps for odd angular momentum** — strongest theorem-grade result in EW-4 for SF-2 inheritance. mechanism-EW-4 Step 3 |
| Shell density factor s_H (ideal 1.29 or 1.014, effective 1.4) | WORKING HYPOTHESIS | op:shelldens OPEN; ideal from $\sqrt{20/12} \cdot \varphi^{-1/2}$, "Monte Carlo effective" 1.4 |
| H mass m_H = 125.10 GeV | REPRODUCED (calibrated) | f_geom^H = 0.0635; **uses r_max=4.5 l_P (different from W/Z 3.5 l_P)** — this is op:mass OPEN; η calibrated independently |
| **op:e0 inconsistency**: $m_H = E_0/\varphi^2 \approx 94$ GeV from EW-5 unified-scale formula vs $m_H = 125$ GeV from direct EW-4 calc | OPEN PROBLEM | Internal contradiction in EW corpus; honestly registered as op:e0 in both EW-4 and EW-5; SF-2 must resolve |
| No symmetry breaking, no Higgs field, no VEV | STRONG PHILOSOPHICAL CLAIM | EW-4 §3 explicitly: "There is no sense in which SU(2)_L × U(1)_Y is a symmetry that gets broken". Three bosons "have always had those masses" |
| Decay channels (H → bb̄, WW*, τ⁺τ⁻, ZZ*, γγ) + Γ_H = 4.07 MeV | REPRODUCED | Branching ratios match SM |
| Prediction: no second scalar below ~200 GeV | STRUCTURAL ARGUMENT | Eigenvalue-gap argument; consistent with LHC data |

**EW-4 inheritance into SF-2**: dodecahedral cage shape stays. A₅-forces-scalar derivation is a clean theorem candidate. **op:e0 inconsistency is a load-bearing SF-2 gate**: the 30% mismatch between the two H mass derivations (94 GeV vs 125 GeV) must be resolved or it becomes a paper-internal contradiction at v0.1. The no-SSB philosophical claim should be revisited under SF-2 framing: under cage-stability primitives, what is "electroweak symmetry breaking" in CPP?

### §3.5 EW-5 (Unification): the capstone paper with proved theorems

The strongest paper in the EW corpus by theorem density.

| Theorem | Statement | Grade | Inheritance into SF-2 |
|---------|-----------|-------|-----------------------|
| **THEO-EW-6** (Thm 4.1) | SU(2)_L algebra $[I^a, I^b] = i\epsilon^{abc}I^c$ from 600-cell 120°/240° biases via binary icosahedral group Γ (order 120) acting on 120 vertices | THEOREM | Direct inheritance; SU(2)_L is the gauge symmetry SF-2 needs |
| **THEO-EW-7** (Thm 5.2) | Nexus gauge invariance: local phase transformations $\psi \to e^{i\alpha(x)}\psi$ preserve all observables via Σ Δb_i = 0 (discrete Ward identity) | THEOREM | Direct inheritance; gauge invariance is foundational for the continuum-limit theorem |
| **THEO-EW-8** (Thm 5.3) | Yang-Mills EFT limit: discrete bit-exchange dynamics → $\mathcal{L}_{\rm eff} = -\tfrac{1}{4}F^{a\mu\nu}F_{a\mu\nu} + (D_\mu\Phi)^\dagger(D^\mu\Phi) - V(\Phi)$ at coarse-graining $l_P/L \to 0$ | THEOREM | Direct inheritance; this is the bridge from CPP discrete dynamics to the SM EFT |
| **THEO-EW-9** (Thm 6.1) | Weinberg angle $\sin^2\theta_W = 0.2312$ from $p_k = (1-k/5)^2$ four-layer interference | **SUPERSEDED** | Replaced by SM-6 $\sin^2\theta_W = 3/(8\varphi)$ at zero parameters; EW-5's framework retained as descriptive context but SF-2 cites SM-6 as primary |

Plus the four open problems (op:dilution, op:coupling, op:e0, op:mass) consolidated honestly.

**EW-5 inheritance into SF-2**: three of four theorems (SU(2)_L, gauge invariance, Yang-Mills EFT) propagate directly. The Weinberg-angle theorem is replaced by SM-6. The four open problems all propagate.

### §3.6 Summary of grades (corpus-wide)

| Grade | Count | Examples |
|-------|-------|----------|
| THEOREM | ~5 | THEO-EW-6/-7/-8 (SU(2), gauge invariance, Yang-Mills); φ⁻³ geometric dilution; A₅ → J=0 for H |
| STRUCTURAL ARGUMENT | ~10 | Eigenvalue–topology mappings (3 bosons + no-middle-boson gap); φ⁻⁴ vertex-count factor; closure → inertness; 75% V−A; m_Z/m_W self-consistency |
| WORKING HYPOTHESIS | ~6 | ℓ_Z, s_H, η holographic dilution, vertex_count_correction, g/g' calibrations |
| SKETCH | ~3 | W⁰ formation rate; W⁰ → W± charge acquisition binding-energy; W⁰ experimental signature |
| REPRODUCED (calibrated) | 4 boson masses + 2 widths + branching ratios | m_W, m_Z, m_H all reproduce PDG with η calibrated independently per boson |
| SUPERSEDED | 1 | EW-5 Thm 6.1 Weinberg angle (replaced by SM-6) |

---

## §4. Source-material map (EW-N → SF-2 sections)

Anticipated SF-2 section structure modeled on SF-4 v4.4:

| SF-2 section | Content | Source material |
|--------------|---------|-----------------|
| §1 Introduction + §1.4 closure status | Cage-boson family motivation; partial-closure flagship framing; conditional-closure framework declaration | EW-1 §1; SF-4 §1.4 template; `templates/conditional_closure_framework.md` |
| §1.6 Claim Status Ledger | 12-row+ table per claim with closure status | SF-4 §1.6 template; this audit §3 |
| §2 SM-corpus inheritance | sin²θ_W = 3/(8φ) from SM-6; four-cage taxonomy from SM-1; binary icosahedral group from SS-1; eigenvalue–topology framework from QM Paper 6 / EW-1 | SM-6 (Weinberg angle); SM-1 (cage stability); SS-1 (Γ group structure); QM Paper 6 (six eigenvalues) |
| §3 Cage geometries from 600-cell eigenvalues | Six eigenvalues, three boson topologies, no-middle-boson gap, derivation of bracelet/icosahedron/dodecahedron uniqueness | EW-1 §2; mechanism-EW-1 Part 1; **NEW WORK**: rigorous derivation of cage-shape uniqueness (Phase 4 of SF-2 campaign) |
| §4 W± and W⁰ from bracelet topology | Bracelet geometry, CP placement, open-interior reactivity, V−A coupling, **W⁰ as CPP-novel particle (CONJ-EW-W0)** | EW-2 §1-§4; mechanism-EW-2; **NEW WORK**: §7 W⁰ runway (this audit) |
| §5 Z boson from icosahedral cage | Icosahedral closure, axial-vector coupling, m_Z derivation | EW-3 §2-§4; mechanism-EW-3 |
| §6 Higgs from dodecahedral cage | Dodecahedral shell, A₅ → J=0 scalar derivation, m_H derivation, op:e0 resolution | EW-4 §2-§3; mechanism-EW-4; **NEW WORK**: op:e0 reconciliation |
| §7 SU(2)_L emergence and gauge invariance | SU(2) algebra from Γ acting on 120 vertices; Nexus gauge invariance; Yang-Mills EFT limit | EW-5 §3-§4 (THEO-EW-6/-7/-8 directly inherited) |
| §8 Weinberg angle from SM-6 | sin²θ_W = 3/(8φ) at zero parameters; tree-level m_Z/m_W = 1/cos θ_W cross-check at 0.5% | SM-6 (primary); EW-1 / EW-5 (descriptive context for replacement) |
| §9 Boson mass spectrum: cage-stability framework | Unified mass formula attempt; resolves op:mass + op:e0 + op:loopfactor + op:shelldens jointly via cage-stability primitives; **THIS IS THE LARGEST OPEN WORK** | EW-2 §4, EW-3 §3, EW-4 §3 (existing fitted-parameter framework); **NEW WORK**: unified zero/few-parameter mass derivation |
| §10 Electroweak symmetry breaking in CPP | Cage-formation-as-EWSB framing; reconciliation with EW-4 "no SSB" stance under cage-stability primitives | EW-4 §3; **NEW WORK**: SF-2 framing decision |
| §11 Cross-sector closure attempt: SF-2 ↔ SM-5 OP-SM-4 Capotauro | Joint closure of EW substrate dynamics + Capotauro for δ_CP, sin²θ_{13}, baryon asymmetry | OPEN-SM-4 entry in Research_Frontier; SF-4 first-cross-sector-closure precedent (Composite K3-Cage-Shell Theorem) |
| §12 Predictions + falsifiers | W⁰ experimental signature; m_Z/m_W cleaning; no-second-scalar-below-200 GeV; possibly δ_CP if Capotauro closure succeeds | EW-1/2/3/4/5 prediction tables; **NEW WORK**: §7 W⁰ signature |
| §13 Discussion (closure architecture, cross-sector posture) | First closure of forced-choice-prediction inclusion criterion; second cross-sector closure attempt | SF-4 §11 template |

---

## §5. SF-2 vs SF-6 boundary

Per the Session 41 architectural revision (patch 0301), the EW corpus is partitioned between SF-2 (cage bosons) and SF-6 (electromagnetism). The audit-time partition:

### §5.1 Stays in SF-2 (cage-boson scope)

- EW-1 §2 (three EW boson topologies)
- EW-1 §3 (Weinberg angle — but with SM-6 supersession)
- EW-1 §4 (mass reproduction + op:dilution as it applies to W/Z/H)
- EW-2 entire content (W± and W⁰)
- EW-3 entire content (Z)
- EW-4 entire content (H)
- EW-5 §3.1 (SU(2)_L from binary icosahedral group — THEO-EW-6)
- EW-5 §4 (Nexus gauge invariance and Yang-Mills EFT — THEO-EW-7, THEO-EW-8)
- EW-5 §5 (Weinberg angle — superseded; descriptive context only)

### §5.2 Transfers to SF-6 (electromagnetism scope)

- EW-1 plain-language summary "edge modes (linear, abelian) carry electromagnetism while face modes (circulatory, non-abelian) carry the weak force" — the **photon-as-edge-mode** content is SF-6 territory
- EW-1 §3 "Tr(A²) + Tr(A³)/3 = 1440 + 2400 = 3840 channels; 1440 edge modes for U(1)_Y / 1440 photon channels" (from FINAL-STATUS-1-April-2026) — the edge-mode topological-invariant content sits in SF-6 as part of the photon derivation
- EW-5 §3.2 (U(1)_Y from radial DP polarization gradient; g'/g ≈ (40/64)φ⁻¹ ≈ 0.387 ratio) — the U(1)_Y derivation is SF-6 source material for the photon U(1)_EM ancestry
- FAQ-EW-1 B1 "photon massless because open-path eDP propagating mode — same reason gluons are massless" — SF-6 (and SF-5 for the gluon analog)

### §5.3 Shared (referenced by both, primary in SM-6)

- sin²θ_W = 3/(8φ) — primary derivation in SM-6; referenced by SF-2 for the W/Z mass-ratio cross-check; referenced by SF-6 for the U(1)_Y / SU(2)_L mixing structure
- φ⁻³ ≈ 0.236 geometric dilution — primary in EW-1; inherited by both SF-2 (cage-boson masses) and SF-6 (photon propagation scale, if SF-6 needs it)

### §5.4 Decision items for Thomas (corrections pass)

**[FLAG-2 for Thomas: §5.2 partition.]** The mode-counting argument that gives the 3/8 fraction (1440/3840) is structurally located in EW-1 (Section 3) and in the FINAL-STATUS-1-April-2026 derivation. SM-6 took the cleaner spectral-trace path and produced 3/(8φ). The question for SF-2 is whether the mode-counting argument should be:

- (i) cited in SF-2 as background, with SM-6 cited as the primary path; mode-counting transfers to SF-6 as the photon-channel derivation
- (ii) reproduced in SF-2 because it's load-bearing for the cage-boson + photon partition story; SF-6 cites it as the SF-2 origin
- (iii) extracted entirely into SF-6 along with the photon content; SF-2 cites SM-6 only

I lean (i): cleanest split, minimal duplication, respects the Session 41 architectural intent. Defer to your call.

---

## §6. Open-problem inheritance

### §6.1 Existing OPEN-P-EW-* entries propagating into SF-2

| Original ID | Statement | Disposition in SF-2 |
|-------------|-----------|---------------------|
| OPEN-P-EW-1 | Holographic dilution η ~ 10⁻¹⁷ from first principles | **PROPAGATE** as OPEN-FP-SF-2-1 (η first-principles). Highest-priority residual; load-bearing for *all* mass predictions becoming zero-parameter |
| OPEN-P-EW-2 | Self-consistent mass formula with single integration range r_max | **PROPAGATE** as OPEN-FP-SF-2-2 (unified cage-stability mass formula). Bound to OPEN-P-EW-4 + op:e0 |
| OPEN-P-EW-3 | g, g' from vertex counting without calibration factor | **PROPAGATE** as OPEN-FP-SF-2-3. Note: under SM-6 supersession this becomes "derive the g, g' values consistent with sin²θ_W = 3/(8φ) from cage-stability + 600-cell vertex spectrum" |
| OPEN-P-EW-4 | Mass ratios m_H/m_Z and m_Z/m_W from eigenvalue ratios | **PROPAGATE** as OPEN-FP-SF-2-4. The m_Z/m_W 5% loop-density discrepancy is the immediate target; m_H/m_Z is bound to op:e0 |
| op:e0 (EW-4 §3, EW-5 §6) | $m_H = E_0/\varphi^2 = 94$ GeV vs direct calc 125 GeV inconsistency | **MUST RESOLVE** at v0.1. Either fold into OPEN-FP-SF-2-2 (unified mass formula) or register separately as OPEN-FP-SF-2-5 |
| op:loopfactor (EW-3 §2.2) | Loop density ℓ_Z reduction 1.437 → 1.2 from 4D→3D projection | **PROPAGATE** as OPEN-FP-SF-2-6 OR fold into OPEN-FP-SF-2-4 |
| op:shelldens (EW-4 §2.2) | Shell density s_H ideal 1.29 → effective 1.4 | **PROPAGATE** OR fold into OPEN-FP-SF-2-2 |
| OPEN-P-EW-5 (mentioned FAQ-EW-2 Q2) | W⁰ contribution to existing electroweak precision observables | **PROPAGATE** as OPEN-FP-SF-2-W0-PREC. Tied to the W⁰ experimental-signature derivation in §7 |

### §6.2 New OPEN-FP-SF-2-* slots opening at SF-2 launch

| Anticipated ID | Statement | Source |
|----------------|-----------|--------|
| OPEN-FP-SF-2-W0-1 | W⁰ bracelet uniqueness: prove the 12-CP bracelet is the unique stable closed subgraph at λ ∈ {1+φ, φ−1} (vs the icosahedron at λ=12); rule out alternative 12-CP open configurations | §7 below |
| OPEN-FP-SF-2-W0-2 | W⁰ mass derivation from bracelet cage-stability primitives; predict whether $m_{W^0} = m_{W^\pm}$ exactly, or differs at $O(\alpha)$ from bound-charge contribution | §7 |
| OPEN-FP-SF-2-W0-3 | W⁰ → W± bound-charge binding mechanism: how does an electron/positron bind to the bracelet to produce the W± state? What is the binding-energy contribution to m_W±? | §7 |
| OPEN-FP-SF-2-W0-4 | W⁰ experimental signature: where would W⁰ appear in collider data? what kinematic/topological distinction from SM W±? why has it not been seen? | §7 |
| OPEN-FP-SF-2-CHIR | Left-handed 75% → 100% continuum-limit derivation (massless helicity selection): prove the 75%/25% phase-space preference becomes 100%/0% V−A coupling at $m/E \to 0$ | EW-2 §4.1; FAQ-EW-2 Q3 |
| OPEN-FP-SF-2-EWSB | "Electroweak symmetry breaking" in CPP: reconcile EW-4 "no SSB" stance with cage-stability primitives; is cage formation the CPP analog of SSB, or is the EW gauge symmetry never broken? | EW-4 §3, conclusion |

### §6.3 Cross-sector open problem available for joint closure

| ID | Statement | Joint-closure target |
|----|-----------|----------------------|
| OPEN-SM-4 (Capotauro) | Lattice chirality-activation event [600-cell] × ℤ₂ → [600-cell] deriving χ = φ⁻¹; produces δ_CP ≈ 195°, sin²θ_{13} ≈ 0.022, baryon asymmetry | If SF-2's EW substrate dynamics close jointly with SM-corpus inheritance, this is the **second cross-sector closure in CPP** and brings SF-4 to 8/8 predictions. See §8 |

---

## §7. W⁰ runway — the four-deliverable campaign for CONJ-EW-W0

This is the cardinal-rule section. Per the SESSION_81 handover, **W⁰ characterization is the gate to v0.1 drafting**. The CONJ-EW-W0 entry in Research_Frontier registers four deliverables. Their state at SF-2 launch:

### §7.1 Deliverable (a): bracelet/open-configuration cage geometry, derived as stable, distinct from icosahedron at the same 12-vertex count

**Current EW corpus state**: EW-2 §2.1 *selects* the 12-vertex configuration that closes into a hexagonal bracelet; mechanism-EW-2 Step 1 *asserts* uniqueness from λ ∈ {1+φ, φ−1}. No proof that the bracelet is the only stable 12-CP closed subgraph at this eigenvalue pair — alternative open or partially-closed configurations are not enumerated and ruled out.

**Gap for SF-2**: theorem-level derivation that the 6-hDP bracelet is the unique stable closed 12-CP subgraph compatible with λ ∈ {1+φ, φ−1}. This parallels SS-9's Lemma B' (contact graph = 1-skeleton of convex 3-polytope via Steinitz + FvdW + C8) but for a CPP eCP/qCP hDP graph rather than a nuclear alpha cluster.

**Tractability assessment**: medium. The eigenvalue–topology correspondence is supported by QM-6 derivation of the six eigenvalues; the question is whether each eigenvalue (or eigenvalue pair) admits a unique stable closed subgraph or multiple candidates. **[FLAG-3 for Thomas: how confident are we that the bracelet is forced as opposed to selected? If forced, by what argument? If selected, what alternatives need to be enumerated and ruled out?]**

**Estimated effort**: 1-2 sessions, contingent on Thomas's input on uniqueness argument.

### §7.2 Deliverable (b): W⁰ mass from bracelet cage-stability

**Current EW corpus state**: EW-2 §4.3 derives $m_W = 80.377$ GeV from $f_{\rm geom}^W \cdot {\rm sea\_strength} \cdot (\hbar c/l_P^3) \cdot 4\pi \cdot 3.5 l_P \cdot \eta_W$ with $f_{\rm geom}^W = 0.219$ for the bracelet. This is the mass of the charged W±, not the neutral W⁰. EW-2 implicitly treats them as the same mass (since the bracelet topology is the same), but this is not justified — the charged W± has an additional bound-charge contribution.

**Gap for SF-2**: derive whether $m_{W^0} = m_{W^\pm}$ exactly (bracelet cage-stability dominates; bound-charge contribution negligible) or whether they differ at $O(\alpha)$ or $O(m_e/m_W)$ or some other small parameter. The W± / W⁰ mass split (if any) is a sharp prediction.

**Tractability assessment**: low-medium. The cage-stability mass formula in EW-2 is reproduced via η calibration, not derived from first principles, so the W⁰ vs W± split inherits the same calibration ambiguity. A cleaner path: derive the *ratio* $m_{W^0}/m_{W^\pm}$ from substrate primitives, which is dimensionless and independent of η.

**Estimated effort**: 2-3 sessions including substrate-primitive derivation of the bound-charge contribution to $m_{W^\pm}$.

### §7.3 Deliverable (c): W⁰ → W± bound-charge mechanism

**Current EW corpus state**: EW-2 §3 sketches a Nexus charge-bookkeeping narrative — a quark deposits charge to the bracelet during a collision, becoming the W±; charge is returned to decay products. No binding-energy calculation; no mechanism for *where* on the bracelet the bound charge sits, what holds it there, or what energetic cost the binding incurs.

**Gap for SF-2**: derive the W⁰ + e⁻ → W⁻ (or W⁰ + e⁺ → W⁺) bound-charge mechanism from CPP substrate primitives. Specifically:

- Where does the eCP (electron) sit on/in the bracelet? Inside the open interior? On a vertex? Bound by what SSV interaction?
- What is the binding energy? Does it match the observed $m_{W^\pm}$ as a sum of $m_{W^0}$ + $m_e$ + binding?
- What is the lifetime of the W⁰ + e⁻ bound state before decay? Is it consistent with the observed W± lifetime?

**Tractability assessment**: medium. This is the most novel CPP-mechanical work in the SF-2 campaign. Closest precedent: SM-1's cage-stability + bound-charge framework for the charged leptons (where the eCP binds to a tetrahedral cage with δ = 1/3 quantization). The W⁰ + eCP system may be a similar bound state at a different scale.

**Estimated effort**: 3-4 sessions, contingent on §7.2 deliverable progress.

### §7.4 Deliverable (d): W⁰ experimental signature

**Current EW corpus state**:
- EW-2 §5.3 mentions: "DP Sea precision tests could detect signature" (vague)
- EW-2 §5.3 mentions: "Exotic decay modes at BR ~10⁻¹³" (no mechanism)
- EW-2 §5.3 mentions: "CDF W mass anomaly partial resolution via hybrid eCP/qCP contributions" (Tier 4 candidate)
- FAQ-EW-2 Q2: "circulates as virtual particle in loops; contributes to vacuum polarization at same order as W± but with different sign for some terms"
- OPEN-P-EW-5 (informal): "Whether existing EW precision data can already constrain W⁰ contribution"

**Gap for SF-2**: derive a *sharp* W⁰ experimental signature. Candidate signatures:

1. **Virtual W⁰ in vacuum polarization**: contributes to $\Pi_{WW}$ at same order as W± with sign differences. Specific signature: $S$, $T$, $U$ oblique-parameter shifts. Is the W⁰ contribution already constrained by LEP/SLC precision data?
2. **Resonance**: could W⁰ appear as a narrow neutral resonance at $m_{W^0} \approx m_{W^\pm}$ in some channel? If so, what channel ($Z\gamma$? $\gamma\gamma$? $\nu\bar\nu$?)? Why has LEP, LHC not seen it?
3. **CDF W-mass anomaly**: if hybrid eCP/qCP contributions to bracelet confinement energy shift $m_{W^\pm}$ at higher collision energies, the W⁰/W± framework predicts a specific energy-dependent W-mass shift — testable.
4. **Lepton-flavor-violating loop effects**: if W⁰ propagates as virtual catalyst in flavor-changing processes, are there specific BR predictions for $\mu \to e\gamma$ or similar?
5. **Anomalous triple-gauge couplings**: W⁰ enters $WWZ$, $WW\gamma$ vertices as a virtual line; specific aTGC predictions?

**Gap**: SF-2 must pick one (or several) of these candidates and develop them to *predictive* level — a number with an experimental program that could falsify it within 5-10 years.

**Tractability assessment**: high uncertainty. Candidate (1) (oblique parameters) is the most immediately testable since precision EW data are extensive. Candidate (3) (CDF W-mass anomaly) is already on the table but the mechanism is Tier 4. Candidate (5) (aTGC) is testable at HL-LHC. Candidates (2) and (4) are speculative.

**Estimated effort**: 2-4 sessions, parallel-able with §7.1-§7.3. The signature derivation cannot start before §7.1 (bracelet geometry) is closed, but can run in parallel with §7.2 and §7.3.

### §7.5 Summary: W⁰ campaign total

| Deliverable | Sessions | Critical-path | Tractability |
|-------------|----------|---------------|--------------|
| (a) bracelet uniqueness | 1-2 | YES — gates everything | Medium |
| (b) W⁰ mass | 2-3 | NO — parallel with (c) | Low-medium |
| (c) bound-charge mechanism | 3-4 | NO — parallel with (b) | Medium |
| (d) experimental signature | 2-4 | NO — can start after (a) | High uncertainty |
| **TOTAL W⁰ campaign** | **6-10 sessions** | — | — |

This is Phase 3 of the 8-phase SF-2 campaign per the SESSION_81 handover. The handover estimated 2-3 sessions for Phase 3; this audit's reading of the gaps suggests 6-10 sessions is more realistic. **[FLAG-4 for Thomas: timeline divergence between handover estimate (2-3 sessions for Phase 3) and audit reading (6-10 sessions). Resolution: either the handover estimate assumed a more lightweight W⁰ characterization, or the audit is overestimating the depth needed for forced-choice-prediction status.]**

---

## §8. Cross-sector closure candidate: SF-2 ↔ SM-5 OP-SM-4 Capotauro

Per OPEN-SM-4 entry in `research_frontier.md` and the SESSION_81 handover, the Capotauro mechanism is registered as the candidate for the **second cross-sector closure in CPP** (after SF-4 v4.0's K3-Cage-Shell composite theorem).

### §8.1 What OPEN-SM-4 currently registers

- **One-line statement**: derive the lattice chirality-activation event that establishes $\chi \approx \varphi^{-1}$ and produces CP violation
- **What a solution looks like**: symmetry breaking $[600\text{-cell}] \times \mathbb{Z}_2 \to [600\text{-cell}]$; derive $\chi = \varphi^{-1}$; reproduce $\delta_{CP} \approx 195°$, $\sin^2\theta_{13} \approx 0.022$, baryon asymmetry
- **Sectors**: SM + SR; Priority HIGH
- **Dependencies**: "requires EW development" — this is the structural reason it pairs with SF-2
- **Current best lead**: $\delta_{CP} \approx 195°$ matches NuFIT; mechanism physically motivated but not formalised

### §8.2 Why SF-2 is the right venue

The Capotauro mechanism is a *chirality-activation event* — a left-handed bias in lattice dynamics. SF-2's substrate-level work on the W bracelet's 75% left-handed preference (deliverable §7 + OPEN-FP-SF-2-CHIR) is exactly the kind of chirality-mechanism derivation that Capotauro requires. If SF-2 derives the chirality bias at theorem level from CPP substrate dynamics, the Capotauro closure may follow as a corollary.

### §8.3 What joint closure would deliver

If successful:

- **For SF-4**: 7/8 → 8/8 zero-parameter neutrino-sector predictions (the 8th being $\delta_{CP}$)
- **For SM-5**: closure of $\sin^2\theta_{13}$ TBM correction; closure of the OP-SM-4 entry that has stood since 23 March 2026
- **For CPP**: second cross-sector closure, validating Finding β-10 as a generic pattern in mature theoretical frameworks
- **For cosmology**: baryon asymmetry mechanism becomes a CPP derivation rather than a separate open problem
- **For SF-2 itself**: SF-2 ships at the same theorem level that SF-4 ships at, with both flagships achieving cross-sector closure

### §8.4 Sequencing within SF-2

Per the SESSION_81 handover Phase 7 (Cross-sector closure attempt with SM-5 OP-SM-4, 2-4 sessions, OPTIONAL), this is attempted *after* SF-2 v1.0 SHIP — not as part of v0.1 drafting. The rationale: stable SF-2 substrate-level theorems (Phase 6 multi-cycle review convergence) become the foundational inputs for Capotauro closure. Same architectural pattern as SF-4 v4.0 (Composite Theorem closure attempted after SF-4 v1.0 SHIP).

### §8.5 Falsification posture

If Capotauro closure fails (the SF-2 substrate dynamics are insufficient to determine OP-SM-4 closure), it does NOT undermine SF-2 v1.0. SF-2 ships at 7/7 cage-boson coverage (W±, W⁰, Z, H, sin²θ_W via SM-6, W/Z mass ratio cross-check, EWSB framing); the Capotauro closure is registered as a future cross-sector closure attempt, like SS-corpus ↔ SF-5 strong-unification.

---

## §9. Findings and flagged-uncertainty list

Numbered for Thomas's corrections pass.

### §9.1 Structural findings

**Finding γ-1** (eigenvalue bridge is load-bearing). The eigenvalue–topology correspondence (6 eigenvalues → 3 boson topologies) is the structural backbone of the EW corpus. SF-2 cannot avoid making this rise to theorem level: each eigenvalue–topology pairing must be either *forced* (uniquely determined) or *selected* (rule out alternatives). This is Phase 4 of the SF-2 campaign (sub-shell shape derivations).

**Finding γ-2** (Weinberg-angle supersession is clean). SM-6's $\sin^2\theta_W = 3/(8\varphi)$ replaces EW-1/EW-5's MC-with-fitted-g' derivation cleanly. SF-2 inherits SM-6 directly and demotes EW-1/EW-5's $p_k = (1-k/5)^2$ to descriptive context. No SF-2-internal contradiction; clean inheritance.

**Finding γ-3** (mass derivations are the dominant work). The four boson masses (m_W, m_W⁰, m_Z, m_H) are currently reproduced with **6-8 fitted parameters** across the EW corpus (sea_strength, hybrid_weak_factor, ℓ_Z, s_H, η_W, η_Z, η_H, vertex_count_correction). This is the largest gap for SF-2 to close. Strategy options: (i) unified mass formula closing op:mass + op:e0 + op:loopfactor + op:shelldens; (ii) zero-parameter mass *ratios* via dimensionless cage-stability primitives (η-independent path); (iii) ship v1.0 with calibrated η but with the cage-shape geometric framework derived (calibrated absolute scale + derived ratios = conditional partial closure). Strategy (iii) parallels SF-4's PARTIAL CLOSURE framing for $\sigma_\nu$.

**Finding γ-4** (op:e0 must resolve at v0.1). The internal contradiction between EW-4's $m_H = 125$ GeV direct calc and EW-5's $m_H = E_0/\varphi^2 \approx 94$ GeV unified-scale formula is a *paper-internal contradiction* if both derivations appear unmodified in SF-2 v0.1. Resolution options: (i) one path is correct, the other is wrong — pick the correct one; (ii) both paths are reproductive with different parameter sets — the unified formula needs revision; (iii) the "unified scale" $E_0$ concept is replaced by cage-stability primitives entirely.

**Finding γ-5** (m_Z/m_W tree-level self-consistency is the strongest cross-check). The 0.5% agreement between independent Weinberg-angle derivation (SM-6 cos θ_W = 0.8773) and independent boson-mass derivations (91.188/80.377 = 1.134) is the load-bearing internal-coherence demonstration for SF-2. Tighten or retain at v0.1.

**Finding γ-6** (75% V−A → 100% V−A is sketch-level). The continuum-limit derivation of exact V−A coupling from the 75% phase-space preference is asserted in FAQ-EW-2 Q3 but not proved. Either lift to theorem level (OPEN-FP-SF-2-CHIR) or register as known limitation in §1.6 claim status ledger.

**Finding γ-7** (no-SSB philosophical claim needs SF-2 framing). EW-4 §3 explicitly: "There is no sense in which SU(2)_L × U(1)_Y is a symmetry that gets broken." SF-2 inherits or revises this. Either way, §10 of SF-2 must state the framing explicitly.

**Finding γ-8** (W⁰ experimental signature is the highest-uncertainty deliverable). Of the four CONJ-EW-W0 deliverables, (d) experimental signature has the highest scope-uncertainty and the most options. Resolution: pick 1-2 candidate signatures at the start of Phase 3 and develop those; register others as deferred.

**Finding γ-9** (v3.1 EW-2 mass-sensitivity correction is the precedent). The honest correction of back-calculated error sensitivities in EW-2 v3 → v3.1 sets the discipline for SF-2: error sensitivities derived from formula, not back-calculated from PDG. Apply pre-flight check at Phase 5 v0.1 drafting.

**Finding γ-10** (Capotauro cross-sector closure is high-value, low-priority for v0.1). OPEN-SM-4 joint closure delivers SF-4 8/8 + δ_CP + baryon asymmetry. Attempted post-v1.0 SHIP per Phase 7. Do not let the cross-sector ambition gate v1.0.

### §9.2 Flagged uncertainties (require Thomas input)

| Flag | Item | Resolution path |
|------|------|------------------|
| **FLAG-1** | Bracelet uniqueness from λ = {1+φ, φ−1}: forced or selected? | Thomas's physical-intuition input on cage-stability argument |
| **FLAG-2** | SF-2 vs SF-6 partition of mode-counting argument (1440/3840 = 3/8) | Strategic decision: (i) primary in SM-6 + cited in SF-2 + reproduced in SF-6, (ii) reproduced in SF-2, (iii) entirely in SF-6 |
| **FLAG-3** | Eigenvalue-pair → topology uniqueness argument: where does the proof live? | Existing in QM-6? Or new work in SF-2 Phase 4? |
| **FLAG-4** | W⁰ campaign sessions estimate: handover 2-3 vs audit 6-10 | Reconcile: either lighter W⁰ characterization than audit assumes, or longer Phase 3 than handover assumes |
| **FLAG-5** | "Hybrid_weak_factor = 1.5" heuristic (3 weak layers / 2 EM polarities) — derived or fitted? | Trace origin; if heuristic, register as OPEN-FP-SF-2-* candidate |
| **FLAG-6** | "Sea_strength = 0.185" from neutron charge neutrality — what's the source paper? | Confirm derivation chain; if from QM-* or SM-*, cite explicitly |
| **FLAG-7** | "Vertex_count_correction = 1.18" for g — pure calibration, or has a geometric origin? | Same |
| **FLAG-8** | op:e0 resolution strategy — pick a direction before v0.1 | Strategic decision; affects §6 and §9 of SF-2 |
| **FLAG-9** | W⁰ experimental signature: which of the 5 candidate signatures (oblique params, narrow resonance, CDF anomaly, LFV loops, aTGC) to develop? | Pick 1-2 at Phase 3 start |
| **FLAG-10** | EWSB-in-CPP framing: maintain "no SSB" stance from EW-4, or revise to "cage formation as EWSB analog"? | §10 of SF-2 framing decision |

---

## §10. Mechanism-selection decisions for Thomas (corrections pass)

Per the SF-4 audit precedent (§"This audit does not select a mechanism. The mechanism-selection decision is Thomas's call"), this audit identifies but does not resolve the strategic decisions.

### §10.1 Strategy decisions for the SF-2 outline (Phase 2)

1. **Closure-level framing at v0.1**: PARTIAL CLOSURE (mass formula calibrated; cage-shape geometric framework derived) — SF-4 v1.0 precedent. Reasonable default; confirm.
2. **op:e0 resolution direction**: (a) unified mass formula closes op:e0 as corollary; (b) op:e0 is independent and resolved separately; (c) the "$E_0$" concept is replaced. Default: (a) — keeps closures coherent.
3. **SF-2 vs SF-6 partition**: per §5.4 default option (i). Confirm.
4. **W⁰ signature candidates to develop**: per §7.4, default candidates (1) oblique parameters + (3) CDF W-mass anomaly. Confirm or revise.
5. **Capotauro cross-sector attempt**: yes (Phase 7 optional) or no (defer entirely)? Default: yes-attempt-with-falsification-posture per §8.5.

### §10.2 Architectural decisions

6. **Eigenvalue-topology theorem residence**: Phase 4 work in SF-2, or back-reference to QM-6? Confirm where the rigorous derivation of cage-shape uniqueness lives.
7. **EWSB framing**: "no SSB" inherited from EW-4 vs "cage formation as EWSB analog". Affects whether §10 of SF-2 is a substantive section or a brief framing remark.
8. **The "Higgs-like resonance" vs "Higgs boson" terminology**: EW-4 uses both. SF-2 standardize on which?

### §10.3 Methodology decisions

9. **Reviewer rotation**: ChatGPT + Grok + Copilot (SF-4 precedent). Confirm.
10. **Cycle target**: 4-cycle ChatGPT trajectory per SF-4 + 1 Grok + 1 Copilot at SHIP. Confirm.
11. **Anthology chapter title**: pending v1.0 SHIP. Candidate "The Bracelet, the Loop, and the Shell" or similar concrete-evocative. Defer to post-v1.0.

---

## §11. Forward roadmap (SF-2 Phases 2-8)

Per the SESSION_81 handover 8-phase structure:

- **Phase 1 (THIS audit, Session 82)**: Pre-survey and audit. **STATUS: DRAFT COMPLETE, awaiting Thomas's corrections pass.**
- **Phase 2**: SF-2 outline (1 session). Inputs: this audit + Thomas's FLAG-1 through FLAG-10 resolutions + §10 strategy decisions. Output: `flagship_papers/electroweak/sf-2_outline.md`.
- **Phase 3**: W⁰ sub-derivation campaign (audit estimate 6-10 sessions, handover estimate 2-3 sessions; reconcile per FLAG-4). Output: `flagship_papers/electroweak/sketches/SF-2_W0_derivation.md` + supporting sketches per deliverable (a)/(b)/(c)/(d).
- **Phase 4**: Sub-shell shape derivations (1-2 sessions). Output: `flagship_papers/electroweak/sketches/SF-2_cage_shape_derivations.md`. Lift eigenvalue-topology correspondence to theorem level.
- **Phase 5**: v0.1 .tex drafting (2-3 sessions). Output: `flagship_papers/electroweak/sf-2_electroweak.tex` at v0.1. Apply v3.1 EW-2 honesty discipline on error sensitivities.
- **Phase 6**: Multi-cycle review trajectory toward v1.0 SHIP (3-5 sessions). Standard reviewer rotation + four-cycle ChatGPT trajectory.
- **Phase 7**: Cross-sector closure attempt with OP-SM-4 Capotauro (2-4 sessions; OPTIONAL). Per §8.
- **Phase 8**: Dossier-completeness closeout (3-5 patches; SF-4 Sessions 78-81 pattern).

**Total estimated effort at audit completion**: 12-15 sessions to v1.0 SHIP + dossier-completeness; +2-4 if Phase 7 cross-sector closure attempted. Matches handover estimate.

---

## §12. Closing observation

The EW corpus (EW-1 through EW-5, 2 April 2026) is **structurally rich and methodologically pre-SF-line**. It establishes the four-boson eigenvalue–topology framework, proves SU(2)_L emergence and Yang-Mills EFT at theorem level, and identifies the W⁰ as a CPP-novel particle — but it does so before the conditional-closure framework, FI accounting, Binary Artifact Workflow, and multi-reviewer convergence pattern were codified. The Weinberg-angle derivation has already been superseded by SM-6's cleaner spectral-trace path. The mass derivations carry 6-8 fitted parameters across the corpus.

SF-2's task is **not to re-derive the EW corpus from scratch** but to:

1. Inherit the eigenvalue–topology framework + the three EW-5 theorems (SU(2)_L, Nexus invariance, Yang-Mills EFT) + the φ⁻³ geometric dilution + the m_Z/m_W tree-level cross-check at 0.5%
2. Lift the bracelet/icosahedron/dodecahedron cage-shape selection from STRUCTURAL ARGUMENT to THEOREM (Phase 4)
3. Close the W⁰ four-deliverable campaign (Phase 3) to forced-choice-prediction status
4. Either close the mass-derivation gaps (op:mass + op:e0 + op:loopfactor + op:shelldens) via unified cage-stability formula, or ship at PARTIAL CLOSURE level with calibrated η (SF-4 v1.0 precedent)
5. Inherit SM-6's $\sin^2\theta_W = 3/(8\varphi)$ directly; supersede EW-1/EW-5's MC-based derivation
6. Apply the v3.1 EW-2 honesty discipline (formula-derived error sensitivities, not back-calculated from PDG) corpus-wide
7. Optionally close cross-sector with OP-SM-4 Capotauro (Phase 7) for δ_CP and SF-4 8/8 closure

The W⁰ is the most distinctive prediction: a forced-choice claim that the Standard Model is missing a neutral massive boson at the bracelet topology. If the W⁰ characterization closes from CPP cage-stability primitives at theorem level (deliverables a-d in §7), SF-2 becomes a flagship-class prediction paper independent of the cage-boson reframing strength.

The methodology runway is paved. The conditional-closure framework, the FI accounting discipline, the Binary Artifact Workflow, the multi-reviewer convergence pattern, the four-cycle ChatGPT trajectory, the four-tier documentation suite, the anthology chapter at SciAm register, the dossier-completeness closeout sequence — all in force from Session 82 onward. The compound interest from SF-4's methodological investment starts paying out at SF-2.

**Next session output**: Thomas's corrections pass on this audit (FLAG-1 through FLAG-10 + §10 strategy decisions), then Phase 2 SF-2 outline.

---

**Status of this document**: DRAFT — solo first-pass per Mode B selection. Pending Thomas's corrections pass on:
- The 10 flagged uncertainties (FLAG-1 through FLAG-10)
- The 11 strategy decisions in §10
- Any structural errors in audit gradings (§3)
- Any source-material map errors (§4)
- Any open-problem inheritance disposition errors (§6)

The flagged items mark the boundary between what solo reading of the EW corpus can settle and what requires physical-intuition input. Corrections-pass output is the input to Phase 2 SF-2 outline drafting.

**Audit completed**: 11 May 2026 (Session 82). Phase 1 of 8-phase SF-2 campaign per SESSION_81 handover.
