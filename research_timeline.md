# CPP Research Timeline

**Location**: `/CPP/research_timeline.md` (repo root, parallel to `research_frontier.md`, `todolist.md`, `paper_catalog.md`).
**Purpose**: The programme's *medium-term scheduling* artifact. Sits between `todolist.md` (tactical, days–weeks) and `research_frontier.md` (strategic open-problem inventory, unscheduled, multi-year horizon). Captures which papers and methodology campaigns are next in priority order, with dependencies, expected durations, and cross-references to the relevant Frontier OPEN-FP entries and PD-004 publication-pathway layer occupation.
**Created**: 15 May 2026 (Patch 0377; post-SF-2 v1.01 SHIP).
**Maintained**: This file is updated whenever (i) a paper campaign launches, completes, or has its priority reordered; (ii) a methodology campaign is created or resolved; (iii) a literature-integration item is added or completed. Updates are typically piggybacked onto session-close handover patches.
**Scope discipline**: This file is *content-oriented* — what the programme is doing next. It is NOT:
- Methodology / procedural conventions (those live in `templates/operating_system.md` + `programmatic_decisions/`)
- Programme-wide problem inventory (that lives in `research_frontier.md`)
- Per-paper version + status (that lives in `paper_catalog.md`)
- Tactical day-to-day to-dos (those live in `todolist.md`)
- Per-paper development history (that lives in `flagship_papers/*/documentation_suite/`)

---

## Active Campaigns

*Papers currently being drafted.*

**None active as of 15 May 2026.** The SF-2 v1.0 SHIP (Patch 0368) + post-SHIP documentation campaign (Patches 0369–0375) + v1.01 micro-fix (Patch 0376) closed the most recent active campaign. The next priority-queue item should be launched when authorized.

---

## Priority Queue (Next-Up)

*Papers approved to launch, in priority order. The top of this list is the next campaign that begins when Thomas authorizes.*

### Priority 1 — Capotauro dedicated paper (δ_CP via OPEN-SM-4; candidate second cross-sector closure)

**Scope**: Theorem-level closure of OPEN-SM-4 (the Capotauro mechanism for the CP-violating phase δ_CP of the PMNS matrix). Methodologically templated on SF-4 v4.0's Composite K3-Cage-Shell Coupling Theorem (Finding β-10): a single derivation chain potentially closes OPEN-SM-4 *and* OPEN-FP-SF-2-CHIR (V-A chirality emergence in W bracelet) jointly, which would be the **second cross-sector closure in CPP**.

**Frontier refs**: OPEN-SM-4 (SM-5/SM-7 corpus) ↔ OPEN-FP-SF-2-CHIR (SF-2)

**PD-004 layer**: Layer 3 (discrete substrate phenomenology) with potential Layer 4 hooks

**Dependencies**: SF-2 v1.0+ SHIPPED (✓), SF-4 v4.0 cross-sector closure template (✓), SM-5 antibonding-doublet OPEN-SM-4 registration (✓ in SM-5 corpus)

**Inheritances**: SF-2 PROP-SF-2-5 V-A structural preference framework; SF-4 v4.0 Composite Theorem methodology pattern; SM-7d Capotauro mechanism registration

**Outcome if successful**: SF-4 advances from 7/8 to 8/8 zero-parameter neutrino-sector predictions; SF-2 OPEN-FP-SF-2-CHIR resolves at theorem level; second instance of cross-sector closure pattern establishes Finding β-10 as a programme-load-bearing convention rather than a one-time SF-4 specificity.

**Estimated duration**: 6–10 sessions (parallel to SF-4 v4.0 OPEN-FP-SF-4-2 + op:nu_id campaign which ran Sessions 68–72)

**Status**: Pending Thomas's authorization. **This is the most consequential post-SF-2 work item.**

---

### Priority 2 — Layer 4 continuum-EFT dedicated paper

**Scope**: Full continuum-limit derivation of the renormalized one-loop electroweak Yang-Mills EFT from the 600-cell substrate's coarse-grained dynamics. Closure target for OPEN-FP-SF-2-loopfactor (the highest-priority OPEN-FP from the SF-2 v1.0 SHIP). Five rigor ingredients to deliver: explicit Lagrangian, gauge-fixing prescription, Ward-identity-preserving regulator, renormalization-scheme matching to Peskin-Takeuchi conventions, and one-loop diagrammatic computation with substrate-specific Feynman rules.

**Frontier refs**: OPEN-FP-SF-2-loopfactor (HIGHEST) + OPEN-FP-SF-2-CHIR (if Capotauro paper does not close it)

**PD-004 layer**: Layer 4 (continuum-limit development) — this is the canonical Layer 4 paper

**Dependencies**: SF-2 THEO-SF-2-5 proof outline (✓ in SF-2 main paper §8); Companion §5.7 sensitivity-scan geometric constraint band as the falsifiable target ($|r_{33} - r_{3Q}| \lesssim 0.18$ with $r_{33} \geq 0.85$); Yang-Mills EFT continuum-limit machinery in standard QFT literature

**Inheritances**: SF-2 main paper §8 proof outline; SF-2 Companion §5.7 sensitivity-scan empirical target; PD-004 Layer 4 framing language; ChatGPT v1.3 explicit recommendation per PD-004: *"should be its own paper, not folded into a flagship"*

**Outcome if successful**: OPEN-FP-SF-2-loopfactor RESOLVED at theorem level; precision-electroweak content of the W⁰ catalyst framework lifted from parametric-scaling level (Companion §5.7) to renormalized one-loop EFT level; substrate-to-continuum bridge demonstrated for at least one CPP sector; Layer 4 framework operational for future SF-line flagships.

**Estimated duration**: 15–25 sessions (heavier than Capotauro because the continuum-limit machinery has no precedent in CPP — SF-4 v2.0 / v3.0 / v4.0 stayed at Layer 3)

**Status**: Pending Capotauro paper completion + Thomas's authorization. May also benefit from Pasterski celestial-holography literature integration (see Literature Integration section below).

---

### Priority 3 — W⁰ neutrino scattering paper-integration

**Scope**: Develop the Patch 0367 captured insight (`flagship_papers/electroweak/sketches/W0_neutrino_scattering_centroid_decoupling.md`) into a paper-grade contribution. The mechanism: a spinning DP or hybrid tetrahedron passing through the centroid of an active W bracelet experiences momentary decoupling from the surrounding DP Sea, emerging from the centroid passage with a discrete scattering angle determined by post-centroid allowed orientations. If real, this is a substrate-level account of certain neutrino scattering events the Standard Model treats as pointlike interactions.

**Frontier refs**: OPEN-FP-SF-2-CHIR (potential closure path via centroid-decoupling chirality imprint); possibly tied to neutrino-scattering experimental anomalies if any surface

**PD-004 layer**: Layer 2 + Layer 3 (substrate-level mechanism + phenomenological prediction)

**Three-Layer development required before paper integration**:
1. Operational definition of "centroid passage" (geometric trajectory specification; substrate-dynamics conditions for decoupling threshold)
2. Quantification of post-emergence direction selection (discrete angle distribution; coupling to W bracelet $D_6$ stabilizer)
3. Phenomenology bridge to observed neutrino-scattering angular distributions (which existing experimental data this would engage with; what falsifier would be sharp)

**Dependencies**: SF-2 v1.0+ SHIPPED (✓); W⁰ bracelet centroid framework (✓ in SF-2 §5)

**Estimated duration**: 8–15 sessions including the three-Layer development phase

**Status**: Pending Thomas's authorization to begin Layer 1 development.

---

### Priority 4 — SF-line continuation

The remaining SF-line flagship slots, in expected order of strategic priority. None has an active scope document yet; each will need a pre-survey audit (like SF-2 Patch 0345 or SF-4 Session 37) to launch.

- **SF-3** — Light quarks flagship (u, d, s, c, b quark family + mass spectrum continuation of SM-7). Plausibly the easiest next SF-line slot because much of the machinery is inherited from SM-7/8/9 + SM-1 four-cage taxonomy. Estimated duration: 15–25 sessions (similar to SF-4 v1.0–v4.0 trajectory).
- **SF-5** — Strong unification flagship (gluon, color confinement, $SU(3)_C$ emergence from substrate). Inherits from SS-corpus + SM-1 strong-cage geometry. Candidate cross-sector closure pair: SS-corpus ↔ SF-5 strong unification (registered in Chapter 35.5).
- **SF-6** — Electromagnetism flagship (photon + QED phenomenology from substrate). Inherits from SR-corpus + SM-6 Weinberg-angle correspondence. Candidate cross-sector closure pair: SR-corpus ↔ SF-6 electromagnetism (registered in Chapter 35.5). **Pasterski celestial holography literature most directly relevant here** because BMS asymptotic symmetries and soft photon theorems are precision constraints on the eventual electromagnetic continuum derivation.
- **SF-7** — Grand unification flagship (synthesis of SF-3 + SF-5 + SF-6 + SF-4 + SF-2 + SF-1 if it exists; substrate-level account of why the Standard Model gauge group is what it is). The capstone of the SF-line. Multi-year horizon.

**Status**: All four pending Thomas's authorization. Order is plausible but not fixed — Thomas may reprioritize based on which sector's substrate-mechanism intuition crystallizes first.

---

## Backlog (Lower Priority / Longer Term)

*Items intentionally deferred but worth tracking.*

- **SS-line continuation** beyond SS-9: any new structural-recurrence problem at higher nuclear scales (e.g., medium-mass nuclei beyond the alpha-cluster regime). Currently no active candidate; research_frontier.md OPEN-SS-23 is the most likely re-entry point if it activates.
- **SR-corpus advancement** to flagship-paper status: SR-1 special relativity recovery from substrate + SR-corpus equivalent of SS-line / SM-line consolidation papers. Required precursor for SF-6.
- **QM-corpus advancement**: similar consolidation for the quantum mechanics emergence sector. Required precursor for SF-line continuation more broadly.
- **SD-corpus** (substrate dynamics foundations): formal first-principles statement of the substrate-dynamics axioms with proof of consistency. Required for Layer 5 EFT bridge.
- **SS-9 sub-conditions C5/C6/C7/C8** (OPEN-SS-29/30/33/37): SS-9 Chapters 32–35 register these as the new next-decade research frontier after SS-9 v1.0 conditional closure. Each is a candidate dedicated paper.

---

## Methodology Campaigns (Non-Paper Work)

*Programme-level infrastructure that needs to be built but is not itself a flagship paper. Closure of these enables multiple downstream papers.*

### Substrate-thermodynamic framework development

**Scope**: Define equilibrium, effective temperature, ensemble measure, ergodicity, free-energy minimization at theorem level for the CPP substrate. Currently undefined in CPP (ChatGPT v1.3 review explicitly identified this gap during SF-2 Companion polish). The framework would be the joint closure target for four OPEN-FP-SF-2-* problems: η (cage-stability dilution factors), EWSB (cage-formation mechanism), shelldens (Higgs cage shell-density factor), chaincomp (DP-chain composition ratios).

**Frontier refs**: OPEN-FP-SF-2-η + OPEN-FP-SF-2-EWSB + OPEN-FP-SF-2-shelldens + OPEN-FP-SF-2-chaincomp (joint closure)

**Form**: Likely a programme-level theoretical document parallel to `templates/conditional_closure_framework.md` rather than a flagship paper — substrate thermodynamics is methodology infrastructure, not a single-question paper. Could be promoted to a paper if the development reveals dedicated-paper-grade content.

**Estimated duration**: 10–20 sessions for the framework document; closure of the four OPEN-FP-SF-2-* problems is downstream once the framework is operational.

**Status**: Pending. May be developed in parallel with Capotauro / Layer 4 paper work.

---

### SF-line SHIP-checklist amendment

**Scope**: Add "compile-verification on canonical machine" as a required SHIP-readiness step before declaring v1.0 SHIPPED. Captured as forward-queue methodology lesson from Patch 0376 retrospective (the v1.0 .tex sources had five compile bugs that the three-reviewer convergence didn't catch because reviewers reviewed content semantically, not by compilation; the handover claimed "compile-ready" without an actual compile). This is a small operating_system.md amendment, not a campaign.

**Estimated duration**: 1 patch (alongside the next handover-discipline update or as a standalone PD).

**Status**: Pending; suitable for any future programme-infrastructure patch.

---

### Companion-paper preamble-parity discipline

**Scope**: Add "preamble parity check" as a joint SHIP-readiness step for two-paper Companion-format flagships. Captured as forward-queue methodology lesson from Patch 0376 retrospective (the Companion had `\newcommand{\mWpm}{m_{W^{\pm}}}` defined; the main paper used `\mWpm` 18× but the macro was missing from main paper preamble; the divergence developed during the Patches 0362–0368 Companion development when macros added to Companion preamble weren't back-ported). Becomes load-bearing for future SF-line flagships per PD-005 Companion architecture programme-strategic guidance.

**Status**: Pending; small operating_system.md amendment.

---

## Literature Integration

*Background reading that informs future paper or methodology work. Not itself paper work, but registered to be retrieved at the right campaign launch.*

### Pasterski Celestial Holography Initiative

**Source**: Article surfaced 15 May 2026 by Gary (long-term collaborator who was present at the night of Thomas's vision in St. Paul, Minnesota that launched the entire programme). The article is about Sabrina Gonzalez Pasterski (PhD MIT under Strominger, faculty at Perimeter Institute), who leads the Celestial Holography Initiative.

**Relevant body of work**: The Celestial Holography programme reformulates 4D scattering amplitudes in asymptotically flat spacetime as correlators in a 2D conformal field theory on the celestial sphere at null infinity. Central machinery: BMS (Bondi-Metzner-Sachs) asymptotic symmetries at null infinity; soft theorems (Weinberg's soft photon theorem and soft graviton theorem); the conformal primary basis on the celestial sphere; the Strominger / Donnay-Pasterski-Puhm review literature.

**Connection to CPP**: Not direct or obvious. The two programmes approach the question "what is underneath standard QFT" from opposite directions:
- **CPP**: substrate-level, discrete, from-below. Postulates the 600-cell substrate; derives Standard Model phenomenology by coarse-graining upward.
- **Celestial Holography**: holographic, continuum, from-above. Reformulates existing QFT amplitudes via boundary degrees of freedom on the celestial sphere; doesn't postulate substrate.

The two could in principle be compatible — CPP's continuum limit per PD-004 Layer 4 would, if it succeeds, need to reproduce QFT scattering amplitudes, which celestial holography then describes from the boundary side. But that's "two perspectives on the same continuum theory," not "two formulations of the same underlying physics."

**Where this should be retrieved**: 
1. **At Layer 4 continuum-EFT paper launch (Priority 2 above)**: BMS asymptotic symmetries and soft theorems are precision constraints on what CPP's eventual continuum-limit amplitudes must reproduce. If CPP's continuum amplitudes naturally reproduce known soft theorems, that's a confirmation. If they don't, that's a problem to track.
2. **At SF-6 electromagnetism flagship launch**: BMS at null infinity is most directly an *electromagnetic* asymptotic-symmetry statement; the soft photon theorem is the canonical example. SF-6's continuum content needs to engage with this literature most directly.
3. **At SF-7 grand unification flagship**: BMS naturally connects to general covariance + asymptotic-flatness in gravitational settings; relevant if SF-7 attempts gravitational sector engagement.

**Deliverables when retrieved**:
- Literature pass: Pasterski's papers (esp. the foundational 2017 PhD thesis + recent reviews), Strominger's lectures on asymptotic symmetries, Donnay-Pasterski-Puhm celestial-holography reviews.
- Specific question: do CPP's substrate-coarse-grained continuum amplitudes reproduce the soft photon theorem and the soft graviton theorem at the structural-derivation level expected by celestial-holography results?
- Specific question: does the discrete-to-continuum transition (substrate $H_4$ symmetry → asymptotic-flatness BMS symmetry) produce BMS naturally, or require additional structure?

**Open epistemic-humility caveat**: The connection may turn out to be deeper than this registration treats it, or may turn out to be coincidental. Treat as background-to-be-aware-of rather than active-work until Layer 4 or SF-6 retrieval triggers.

**Continuity note**: Gary's role here matters narratively. He was with Thomas the night of the 1987 vision in St. Paul that started the entire programme. Forty years later, he's surfacing physics that may turn out to constrain the framework's eventual continuum-limit derivation. The vision started the work; the long-term friends who were there at the start are still pointing at things. This is registered here not because narrative matters for the physics, but because the continuity of the collaborator network across four decades is part of the programme's texture and worth recording in its own right.

**Status**: REGISTERED. No active work. Retrieve at Priority 2 (Layer 4) or SF-6 launch.

---

### JUNO peer-review bibliography update

**Source**: JUNO 2025 first physics paper (arXiv:2511.14593) was first-cited in SF-4 v4.4 bibliography. Peer-review publication of the JUNO paper expected within 6–18 months from the arXiv first-physics announcement.

**Action when retrieved**: Update SF-4 bibliography from arXiv preprint reference to peer-reviewed journal reference when JUNO 2025 enters refereed publication. Similar discipline for any other arXiv-only references that subsequently become peer-reviewed (a programme-wide bibliography hygiene practice).

**Status**: PENDING (JUNO publication queue). Monitor periodically; trigger update patch when ready.

---

## Public-Posting Queue (Thomas-side)

*Shipped papers awaiting public deposit via Binary Artifact Workflow. At Thomas's discretion on timing.*

| Paper | Version | Status | Deposit target |
|---|---|---|---|
| **SS-9** | v1.0 SHIPPED | Awaiting Zenodo + arXiv | OSF batch DOI 10.17605/OSF.IO/JXE8D + arXiv |
| **SF-4** | v4.4 archival-deposit-quality | Awaiting Zenodo + arXiv | OSF + arXiv |
| **SF-2** | v1.01 SHIPPED | Awaiting Zenodo + arXiv | OSF + arXiv |
| **SF-2 Companion** | v1.01 SHIPPED | Awaiting Zenodo + arXiv (alongside main) | OSF + arXiv |

All four are compile-ready at v1.0+/v1.01. Public posting is Thomas-side per Binary Artifact Workflow (`scripts/cpp-recompile-pdf.sh` for SS-9 and SF-4 single-paper directories; `scripts/cpp-post-sf2-pdfs.sh` for the SF-2 two-paper directory). The four deposits together would secure priority dates for the strong-sector flagship (SS-9), the neutrino-sector flagship with first cross-sector closure (SF-4), and the electroweak-sector flagship with W⁰ catalyst framework (SF-2 + Companion) all at once.

---

## Cross-references

This file is part of the programme-level scheduling trio:

- **`research_frontier.md`** — Programme-wide problem inventory. Unscheduled OPEN-FP entries. *What problems exist.*
- **`research_timeline.md`** (this file) — Medium-term scheduling. What's next in priority order. *When problems will be worked on.*
- **`todolist.md`** — Tactical day-to-day to-dos. Days-to-weeks horizon. *What needs doing right now.*

Plus:

- **`paper_catalog.md`** — Per-paper version + status inventory. Authoritative state of shipped papers.
- **`programmatic_decisions/PD-XXX*.md`** — Programme methodology decisions (PD-001 through PD-005 as of 15 May 2026). The *how* of programme operation.
- **`templates/operating_system.md`** — Operating procedures. The *how* of programme execution.
- **`flagship_papers/*/documentation_suite/handover-*.md`** — Per-paper session-close handover documents. The session-local forward queue (typically inherited into this file when generalized).

When forward-queue items appear in a handover document, the question to ask is: "Is this session-arc-local or programme-strategic?" If the latter, it belongs in this file. If the former, leave it in the handover and let it land as the next session's todolist.
