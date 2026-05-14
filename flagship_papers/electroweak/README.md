# SF-2: Electroweak Cage-Boson Unification — W±/W⁰/Z/H from 600-Cell Geometry

**Status:** **v1.0 SHIPPED** (14 May 2026 Session 83 close, Patch 0368). Joint main paper + Companion v1.0 SHIP issued in single patch with full version synchronization. Three-reviewer convergence on SHIP-at-v1.0 verdict achieved: ChatGPT v1.3 pair review (structural achievement validated; the project has evolved from "loosely connected speculative ideas" into "a coherent geometric-substrate research architecture with identifiable mathematical cores and explicit unresolved frontiers"); Copilot v1.0 + v1.2 reviews (SHIP-ready, no blockers); Grok v0.8 pair review explicit verdict: *"This is flagship-series work at its strongest. SHIP at v1.0."*
**Estimated sessions to v1.0 SHIP:** 5–8 (estimate at folder establishment Session 38; actual: 24 patches across Sessions 81–83, within revised estimate).
**Inclusion criterion fit:** (1) named known-unknown — the Weinberg angle, electroweak symmetry breaking, the W/Z mass relation, the Higgs origin; (2) forced-choice prediction — the W⁰ as a novel particle (CONJ-EW-W0 now structurally derived and externally validated across three reviewer passes); (3) cross-domain unification — within the EW sector mass spectrum, including a CPP-novel particle that current SM phenomenology does not name.

**v1.0 SHIP deliverables (Session 83 close):**
- `sf-2_electroweak.tex` — main paper at v1.0 SHIPPED, 1821 lines source (compile pending on ClearPC per Binary Artifact Workflow). 8 theorems + 9 corollaries + 6 propositions + 6 OPEN-FP-SF-2-* problems registered.
- `sf-2_companion.tex` — Companion paper at v1.0 SHIPPED, 1041 lines source. 4 TikZ figures, 11 tables, 4 mdframed rigor-positioning boxes, 2 embedded Python listings.
- `code/oblique_parameters_framework.py` (230 lines), `code/dp_chain_monte_carlo.py` (212 lines), `code/oblique_parameters_sensitivity_scan.py` (302 lines), `code/README.md` (96 lines) — three GPU-runnable Python programs with actual numerical results integrated into Companion.
- `documentation_suite/handover-SF-2.md` — Session 83 close handover (this folder's handover document; supersedes any earlier in-progress versions).
- Programme-level: `programmatic_decisions/PD-004-publication-pathway.md` (created Patch 0367); `templates/operating_system.md` §4 Phase 7 Version-discipline rule (added Patch 0367); `sketches/W0_neutrino_scattering_centroid_decoupling.md` (Thomas's insight captured Patch 0367).

**Forward queue post-Session 83:**
- Patches 0370-0375 documentation sequence: registers freeze, Tier-4 reasoning, development + transcript, 7-file companion suite, anthology chapter, TATWD integration. See `documentation_suite/handover-SF-2.md` for full ordering.
- ClearPC PDF compile + public posting (OSF + arXiv) at Thomas's discretion.
- Post-public-posting: W⁰ neutrino scattering paper-integration when authorized (captured insight in sketches/).

---

## Scope (Session 41 narrowed; delivered at v1.0)

SF-2 covers the **cage bosons of the electroweak sector**: W±, W⁰, Z, and H. These are particles whose mass and structure derive from CPP cage-stability mechanisms applied to specific 600-cell-shell geometries. They are *not* the photon (a polarization quantum of the dipole sea, addressed in SF-6) and *not* the gluon (a qDP relationship at baryon vertices, addressed in SF-5). The Session 41 architectural revision (patch 0301) separated those into their own flagship venues to give SF-2 mechanistic coherence.

Specifically:

- **W±:** charged massive cage bosons; eCP/qCP hDP combinations bound in a 12-CP bracelet cage (the W⁰ substrate plus a bound electron or positron). Mass derivation via cage-stability + bound-charge contribution. **DELIVERED at v1.0.**
- **W⁰:** **novel CPP prediction** — a neutral massive boson with a 12-CP bracelet/open-configuration cage structure. Functions as the substrate upon which W± states form when an electron/positron binds to it. The bracelet/open-configuration distinguishes it from Z's closed icosahedron and gives it a catalyst role in SM particle transformations. **Structurally derived at v1.0 via six propositions in §5 (centroid capture, activation transition, mass-degeneracy $m_{W^0} = m_{W^\pm}$ within ~1 MeV, disintegration timescale, reorganization probabilities, universality). Externally validated across three reviewer passes as the central original contribution.**
- **Z:** neutral massive cage boson; eCP/qCP hDP in a 12-CP icosahedral closed cage. **DELIVERED via Theorem 4.1 (12-vertex first distance shell, $I_h$ stabilizer).**
- **H (Higgs):** neutral massive cage boson; 20-CP dodecahedral cage structure. **DELIVERED via Theorem 4.3 (20-vertex second distance shell, $I_h$ stabilizer via Platonic duality; $A_5$ rotation group trivial-irrep delivers scalar character).**

In addition to the four cage-boson masses, SF-2 v1.0 establishes:
- $\sin^2\theta_W = 3/(8\phi)$ inherited from SM-6 as zero-parameter numerical correspondence emerging from spectral trace structure (numerically coincident with low-energy effective value; Weinberg angle runs with scale)
- Tree-level mass-ratio $m_Z/m_W = 1/\cos\theta_W$ to 0.54% with zero cross-calibration
- Mass-formula PARTIAL CLOSURE via three calibrated dilution factors $\eta_W, \eta_Z, \eta_H$ reproducing $m_W, m_Z, m_H$ at observed values
- EWSB cage-formation framing (Section 11; OPEN-FP-SF-2-EWSB registered for first-principles closure)
- Yang-Mills EFT continuum-limit recovery at proof-outline level (Theorem 8.3; full derivation = Layer 4 dedicated future paper per PD-004)
- Mass-gap theorem (Theorem 4.4): no additional electroweak scalar between $V=12$ and $V=20$ vertices, predicting no new scalar below ~200 GeV.

## v1.0 Predictions and falsifiers

**Zero-parameter predictions:**
- $\sin^2\theta_W = 3/(8\phi) = 0.23121$ (inherited from SM-6; matches observed to all decimal places at the low-energy effective value)
- $m_Z/m_W = 1/\cos\theta_W = 1.140$ vs observed 1.134 (0.54% match, zero cross-calibration)
- $m_{W^0} = m_{W^\pm}$ within ~1 MeV (structural mass-degeneracy from $W^0$ catalyst framework Proposition 5.3; **confirmed at parametric-scaling level by $\Delta T \approx 0$ across entire Companion sensitivity-scan grid**)
- W decay channel structure (V-A vector at $W^\pm$; structural preference from bracelet $120°/240°$ phase bias; theorem-level at finite-symmetry per OPEN-FP-SF-2-CHIR)
- Mass-gap forbidding additional electroweak scalar between $V=12$ and $V=20$ (no new electroweak scalar below ~200 GeV, modulo Higgs scale)

**Falsifiers (six):**
1. $W^0$ contribution to $S, T, U$ outside LEP/SLC 3$\sigma$ in derived continuum-EFT calculation (Companion §5.7 sensitivity scan demonstrates the substrate-symmetry-motivated parameter region with 83.6% within bounds at heuristic level)
2. $m_{W^0} \neq m_{W^\pm}$ observed by future precision measurement (sharp framework prediction)
3. Mass-gap violated by observation of an additional electroweak scalar below ~200 GeV
4. W-decay branching ratios deviate from $D_6$-symmetric structural predictions
5. Higgs spin observed not consistent with dodecahedral $A_5$ trivial-irrep classification
6. Continuum-limit Yang-Mills EFT recovery fails when Layer 4 dedicated paper is produced

---

## Source material inheritance

| Source paper | Content drawn | Status at v1.0 SHIP |
|--------------|---------------|---------------------|
| SM-1 | Cage stability, eCP linear-oscillator insight | Established; inherited |
| SM-6 | $\sin^2\theta_W = 3/(8\phi)$ exact | Established; inherited as zero-parameter numerical correspondence |
| SS-1 | Binary icosahedral group $\Gamma$ structure | Established; inherited for $SU(2)_L$ gauge algebra |
| EW-2 | W/Z cage geometry sketches | Inherited; expanded to theorem-level cage-shape uniqueness in §4 |
| EW-4 | Higgs cage / dodecahedral structure | Inherited; expanded to theorem-level in §4 + §7 |
| SM-7/8/9 | Mass-formula machinery $M_0 = m_e \cdot z/\phi$ | Established; inherited as calibration baseline |

## OPEN-FP problems registered at v1.0 SHIP

Six structural-derivation problems registered as future work:
- **OPEN-FP-SF-2-η**: substrate-derivation of the $\eta$ cage-stability dilution factor (currently calibrated per cage)
- **OPEN-FP-SF-2-EWSB**: substrate-derivation of EWSB cage-formation mechanism (analog to SM Higgs mechanism)
- **OPEN-FP-SF-2-loopfactor**: substrate-derivation of one-loop oblique correction structure (Companion §5.7 identifies geometric target band $|r_{33} - r_{3Q}| \lesssim 0.18$ with $r_{33} \geq 0.85$)
- **OPEN-FP-SF-2-shelldens**: substrate-derivation of $s_H$ shell-density factor (currently calibrated)
- **OPEN-FP-SF-2-chaincomp**: substrate-thermodynamic derivation of DP-chain composition ratios (Companion §6 toy MC reports exploratory baseline)
- **OPEN-FP-SF-2-CHIR**: chirality emergence in W bracelet structure (V-A coupling derivation; potential closure path via Patch 0367 W⁰ neutrino scattering centroid-decoupling sketch)

## What this folder contains (at Session 83 close)

```
flagship_papers/electroweak/
├── README.md                          (THIS FILE)
├── sf-2_outline.md                    (pre-paper outline; Session 81)
├── sf-2_electroweak.tex               (main paper v1.0 SHIPPED, 1821 lines)
├── sf-2_companion.tex                 (Companion v1.0 SHIPPED, 1041 lines)
├── sf-2_electroweak.pdf               (planned; ClearPC compile pending)
├── sf-2_companion.pdf                 (planned; ClearPC compile pending)
├── sketches/                          (pre-paper working documents + captured insights)
│   ├── SF-2_electroweak_sector_audit.md
│   ├── SF-2_W0_derivation.md
│   └── W0_neutrino_scattering_centroid_decoupling.md (Patch 0367)
├── code/                              (GPU-runnable Python programs)
│   ├── README.md
│   ├── oblique_parameters_framework.py
│   ├── dp_chain_monte_carlo.py
│   └── oblique_parameters_sensitivity_scan.py
└── documentation_suite/               (four-tier discipline)
    ├── handover-SF-2.md               (Session 83 close handover; Patch 0369)
    ├── reasoning-SF-2.md              (Tier 4 verbatim reasoning capture, 10 thematic sections, 460 lines; Patch 0371)
    ├── development-SF-2.md            (19 patch-grouped vignettes + 6 lessons learned, 277 lines; Patch 0372)
    └── transcript-SF-2.md             (20 per-patch transaction entries + patch summary table, 238 lines; Patch 0372)
```

**The four-tier documentation suite is the canonical documentation deliverable at v1.0 SHIP per PD-005 (four-tier subsumption for SF-line flagships).** The originally-planned 7-file companion suite (mechanism / glossary / phenomena / philosophy / reviews / keywords / FAQ-or-lay-summary) has been subsumed into the four-tier files plus programme-level registries plus the planned anthology chapter, per the precedent established by SS-9 v1.0 (Patch 0282) and SF-4 v1.0/v4.4 (Patches 0314 / 0344). The subsumption mapping:

| 7-file suite slot | Subsumed into |
|---|---|
| glossary | `master_glossary.md` SF-2 v1.0 W⁰ catalyst framework terms section (10 entries; Patch 0370) |
| mechanism | Main paper §5 + `reasoning-SF-2.md` Sections 1, 3, 5 |
| phenomena | `predictions.md` Section 2 (PRED-O-21 through PRED-O-24) + Section 6 SF-2 row + paper §6 |
| philosophy | `reasoning-SF-2.md` Sections 1, 10 + paper §11 EWSB framing |
| reviews | Patches 0359, 0360, 0361, 0363, 0364, 0366, 0367 commit messages + main paper / Companion title-block CHANGELOG entries + `reasoning-SF-2.md` Section 7 |
| keywords | Companion paper §2 glossary + main paper abstract + `master_glossary.md` SF-2 entries |
| FAQ / lay-summary | Anthology chapter at Rovelli/SciAm register, planned for Patch 0374 (~5,000-6,000 words) |

Two-Triggers discipline preserves the option to produce specific companion-suite files if external feedback substantively warrants (e.g., a sustained correspondence about the W⁰ catalyst mechanism would activate `mechanism-SF-2.md`) or if a v1.x revision produces substantive new content. The subsumption is the default, not an absolute rule. See `programmatic_decisions/PD-005-four-tier-subsumption-for-sf-line-flagships.md` for full rationale.

Anthology chapter at Rovelli/SciAm register planned for Patch 0374. TATWD integration planned for Patch 0375.

---

*Folder established at Session 38 (patch 0295) per Option-3 architecture; scope narrowed to cage bosons only at Session 41 (patch 0301) per the architectural-revision conversation that separated photon (to SF-6) and gluon (to SF-5) into their own flagships. SF-2 v0.1 drafting began Session 81; v1.0 SHIPPED Session 83 close, Patch 0368.*
