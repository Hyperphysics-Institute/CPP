# Flagship Papers

**Location:** `/CPP/flagship_papers/`
**Established:** 8 May 2026 (Session 37 opening, patch 0293)
**Architecture established:** 9 May 2026 (Session 38, patch 0295) — Option-3 four-family + unification SF-line
**Architecture revised:** 9 May 2026 (Session 41, patch 0301) — 7-paper SF-line; SF-2 scope-narrowed to cage bosons only; SF-5 strong-sector and SF-6 electromagnetism added; SF-5-original (unification synthesis) renumbered to SF-7
**Strategic source:** [`/CPP/research_priorities.md`](../research_priorities.md)

---

## What this folder is for

These are the **apex papers** of the Conscious Point Physics programme: cross-cutting papers that solve named unsolved problems in physics, plus the cross-domain unification synthesis. They are the papers a new reader should read first.

A flagship paper is distinguished from a series paper by its argumentative role, not by its source material. Series papers (SM, SS, EW, QM, SR, SD) are *derivation* papers — each takes the framework and derives the next thing. A flagship paper takes a body of completed derivations and presents them as a solution to a named problem in mainstream physics, or as a cross-domain synthesis. The audience entry point, the reviewer expectation, and the rhetorical shape all differ.

## Inclusion criterion

To live in `flagship_papers/`, a paper must do at least one of:

1. **Solve a named known-unknown** in mainstream physics — the hierarchy problem, the cosmological constant, strong CP, muon g-2, baryon asymmetry, and the like.
2. **Make a forced-choice prospective prediction** that an upcoming experiment will confirm or falsify, before measurement.
3. **Provide a cross-domain unification** — one framework deriving phenomena from multiple sectors, presented for an audience reading across sectors.
4. **Bridge to recognized mathematics** in a way that anchors the framework against the "numerology" pattern-match (Steinitz, Coxeter, Freudenthal–van der Waerden classification, polytope theory, distance geometry, rigidity theory, etc.).

## The SF-line architecture (7-paper)

The SF-line is structured as **six family/sector flagship papers plus a grand unification synthesis**. Each family/sector paper presents the full first-principles derivation of one Standard Model family or particle class in apex-paper form; the grand-unification paper synthesizes the six predecessors into the headline answer to the hierarchy problem and the cross-sector unification claim.

This 7-paper architecture revises the 5-paper Option-3 architecture established at Session 38. The revision came at Session 41 from a structural-symmetry observation: the original SF-2 ("electroweak") bundled four physically distinct boson categories — cage bosons (W±, Z, H), the W⁰ catalyst-substrate, the photon (eDP polarization quantum, not cage-bound), and the gluon (qDP relationship at baryon's tetrahedral vertices, not cage-bound). The first two are mass-derivation targets via cage-stability mechanisms. The latter two operate by entirely different CPP mechanisms and have entirely different audiences (strong-sector specialists for the gluon; classical/relativistic/quantum physics audiences for the photon). Folding all four into one paper would have produced an incoherent flagship; separating gives each its proper venue.

Sequential ship of SF-1 → SF-2 → SF-3 → SF-4 → SF-5 → SF-6 → SF-7. SF-1, SF-2, SF-3 likely concurrent or near-concurrent given they are primarily reframing of strong corpus. SF-4 is the heavy-lift derivation campaign currently active. SF-5 and SF-6 are corpus-rich syntheses where the substantive physics already exists in series-paper form (SS-1 through SS-9+ for SF-5; EW-1 through EW-5 + SR-1 + QM-1 through QM-6 for SF-6) and the work is primarily synthesis-and-presentation. SF-7 depends on all six predecessors.

| ID | Paper | Folder | Status | Sessions to v1.0 | Inclusion-criterion fit |
|----|-------|--------|--------|---------------------|------------------------|
| **SF-1** | Charged Lepton Mass Spectrum from K3 + 600-Cell Geometry | [`charged_leptons/`](charged_leptons/) | Planned (lowest-risk; reframing) | 3–5 | (1), (4) |
| **SF-2** | Electroweak Cage-Boson Unification — W±/W⁰/Z/H from 600-Cell Geometry | [`electroweak/`](electroweak/) | Planned (reframing + W⁰ novel registration; sub-shell-shape derivations) | 5–8 | (1), (2), (3) |
| **SF-3** | Quark Sector Unification from 600-Cell Distance Shells | [`quarks/`](quarks/) | Planned (reframing) | 4–6 | (1), (4) |
| **SF-4** | Neutrino Sector Unification from 600-Cell Geometry | [`neutrinos/`](neutrinos/) | **Active — audit complete (S37); mechanism selected (S39); OPEN-FP-SF-4-1 PARTIAL CLOSURE physical picture in hand (S41); OPEN-FP-SF-4-2 K3-Cage-Shell Consistency pending** | 10–14 | (1), (4) |
| **SF-5** | Strong-Sector Unification — Gluon Re-counting, Glueballs, Confinement from Tetrahedral Vertex Bonding | [`strong/`](strong/) | Planned (synthesis of SS-1 through SS-9+ + OPEN-SS-6 glueball + OPEN-SS-37 routes) | 5–8 | (1), (2), (3), (4) |
| **SF-6** | Electromagnetism Unified — Classical, Relativistic, Quantum from eDP Sea Polarization | [`electromagnetism/`](electromagnetism/) | Planned (synthesis of EW-1 through EW-5 + SR-1 + QM-1 through QM-6) | 5–8 | (3), (4) |
| **SF-7** | Standard Model Grand Unification — Hierarchy Without Hierarchy | [`unification/`](unification/) | Planned (depends on SF-1 through SF-6 ship) | 5–8 | (1), (3), (4) |

The original Track-1 hierarchy paper outline (now in [`unification/hierarchy_paper_outline.md`](unification/hierarchy_paper_outline.md)) provides extensive source material for the eventual SF-7 synthesis; its structure shifted from single-paper-covering-12-masses (original Track 1) to synthesis-of-four-family-papers (Session 38 Option-3) to **synthesis-of-six-family-and-sector-papers** (Session 41 7-paper architecture).

## Particle coverage of the SF-line

SF-line papers collectively address all 17 SM particles plus several novel CPP predictions and the cross-sector mixing parameters. The accounting:

| Particle class | Particles | Count | Massive? | Flagship venue |
|---|---|---|---|---|
| Charged leptons | e, μ, τ | 3 | Yes | SF-1 |
| Cage bosons (electroweak) | W±, Z, H | 3 (W± degenerate) | Yes | SF-2 |
| Neutral W boson (CPP novel) | W⁰ | 1 | Yes (predicted) | SF-2 |
| Photon | γ | 1 | No | SF-6 |
| Gluon | g | 1 (CPP) / 8 (SM) | No | SF-5 |
| Quarks | u, d, c, s, t, b | 6 | Yes | SF-3 |
| Neutrinos | ν_e, ν_μ, ν_τ | 3 | Yes | SF-4 |
| **Total** | | **18 particles addressed (17 SM + 1 CPP novel)** | | |

Quantitative-prediction count across the SF-line: 16 masses (12 fermion + 3 cage-boson + 1 W⁰), 9 masslessness predictions (1 photon + ~8 SM-equivalent gluon types from CPP gluon-counting), and the cross-sector mixing parameters (PMNS in SF-4, CKM in SF-3, EW phases in SF-2). The "12 fermion masses from one calibration" headline frames the SF-1/SF-3/SF-4 fermion-mass subset specifically; the full SF-line addresses ~33 quantitative predictions.

**On the gluon counting:** the CPP claim is that there are not 8 distinct gluon types but rather different bonding relationships between the 4 tetrahedral vertices upon which a baryon forms; the SM SU(3) octet is a phenomenological dressing of this 4-vertex structure. This is registered as CONJ-SS-Gluon-4Vertex in `research_frontier.md` and is a substantive falsifiable claim addressed in SF-5.

**On the W⁰:** a novel CPP prediction. The W⁰ is a neutral massive boson with a bracelet-shaped/open-configuration cage structure, distinct from the icosahedral Z. It functions as a catalyst substrate for SM particle transformations: an electron or positron binds to the W⁰ to create the W± charged states. This is registered as CONJ-EW-W0 in `research_frontier.md`. Experimental signature is a derivation target in SF-2.

## Other flagship paper candidates (separate from the SF-line)

The SF-line covers the SM-particle programme. Two additional flagship-paper candidates from the original Session 37 four-track plan remain valid but are separate from the SF-line:

- **Anomaly-targeting paper #2** — cosmological constant, strong CP, muon g-2, $\Lambda_{QCD}$/proton mass, baryon asymmetry. Candidate selection deferred. Inclusion-criterion fit: (1) or (2).
- **Eight-experiment manifesto audit** — audit the November 2025 viXra-targeted eight-experiment falsification manifesto against current post-SS-9 / post-SM-3-through-8 formalism; republish via Zenodo if 5+/8 hold up. High strategic value at low effort. Inclusion-criterion fit: (2).

These are not yet scaffolded into folders; they are deferred-priority items that may be promoted in parallel with SF-line work as time and energy permit.

## Why this 7-paper architecture

Three reasons over the 5-paper architecture it replaces:

1. **Mechanistic coherence within each paper.** Each flagship has a single underlying CPP mechanism or single coherent particle class. SF-2 bundling cage bosons + photon + gluon would have required three different mechanism narratives in one paper (cage-stability for W/Z/H, polarization-quantum for photon, qDP-bonding for gluon), undermining the paper's argumentative unity. Separating gives each paper a coherent mechanism narrative.
2. **Audience-fit by particle class.** Strong-sector specialists, classical-EM/optics readers, and electroweak theorists are different audiences with different entry-question expectations. SF-5 reaches strong-physics audiences; SF-6 reaches an extraordinarily broad audience (classical EM is taught in every undergraduate physics curriculum); SF-2 reaches electroweak theorists. Bundling them prevents each paper from meeting its proper audience.
3. **Source-corpus richness justifies the count.** SF-5 has SS-1 through SS-9+ plus OPEN-SS-6 glueball plus OPEN-SS-37 routes — substantial corpus that warrants its own apex venue. SF-6 has EW-1 through EW-5 plus SR-1 plus QM-1 through QM-6 — also substantial. The 7-paper architecture is honest about the corpus already in hand; the 5-paper architecture under-scoped what the SF-line actually needs to present.

## Relation to series papers

Flagship papers do not replace series papers — they build on them. The SF-line cites the SM, SS, EW, SR, and QM series extensively; it does not duplicate their content. Series papers remain the derivation infrastructure; flagship papers present that infrastructure in solving-named-problem form, in forced-choice-prediction form, or in cross-domain-unification form.

When a flagship paper relies primarily on a single series, the series' `README-series_*.md` should add a "Flagship synthesis" line linking to the relevant flagship paper, so a reader entering through the series finds the synthesis pointer.

## Folder convention

Each flagship paper lives in its own subfolder under `flagship_papers/`, named for the family or the problem it addresses (e.g. `charged_leptons/`, `neutrinos/`, `strong/`, `electromagnetism/`, `unification/`). The subfolder houses the paper `.tex` and `.pdf` once produced, plus `documentation_suite/`, `letters/`, `founders_voice/`, and `sketches/` per the SS-9 four-tier discipline as the paper develops.

Filenames follow CPP convention: no version suffixes in filenames (version history lives in the internal CHANGELOG header).

The `sketches/` subfolder pattern is imported from SS-9's `series_strong/papers/SS-9/sketches/`: working documents that develop subsidiary derivations before integration into the main `.tex` source. They are open-source and effectively part of the paper for any reader who wants to see the development path.

## Flagship papers outside the SF-N numerical convention

As of 20 May 2026 the flagship corpus includes two papers outside the SF-N family/sector numbering. They live in `flagship_papers/` at parallel rigor and ship discipline; they are flagship-class artifacts under the inclusion criterion (solving named known-unknowns, providing cross-domain unification) but address structural-mechanism questions rather than family/sector reframings, so they do not occupy SF-N slots:

| Folder | Paper | Status | Outside-SF-N reason |
|---|---|---|---|
| [`capotauro/`](capotauro/) | **Capotauro [v1.0 SHIPPED Session 122 Patch 0415, 16 May 2026 + v2.0 v1.0 SHIPPED Session 135 Patch 0479, 19 May 2026]** — Substrate-Vacuum Chirality on the K3-Doublet (v1.0); Three-Way Cross-Sector Substrate-Level Unification across K3-doublet + W-bracelet + qDP/eDP (v2.0); 12 foundational inputs; 3 programme-level theorems THEO-CAP-1 + THEO-SD-CHIR-1 + THEO-SD-CHIR-2; 11-route falsifier set | Substrate-mechanism question (substrate-vacuum chirality magnitude $\|\chi\| = \phi^{-3}$ derivation + cross-sector unification); does not reframe a SM family or sector; OPEN-SM-4 sub-claims (b)+(c) closure with sub-claim (a) Capotauro nucleation event remaining open. First flagship paper outside SF-N convention; first flagship to undergo substantive v2.0 extension. |
| [`chirality_continuum/`](chirality_continuum/) | **Chirality Continuum [v1.0 SHIPPED Session 137 Patch 0509, 20 May 2026]** — Joint Layer 4 EFT Cross-Sector Closure of OPEN-FP-SF-2-CHIR (Electroweak V–A Coupling) and SM-2 v2.0+ (Quark Chiral-Polarity-Bias) from substrate handle $\|M\| = \chi/6$; 3 programme-level theorems THEO-CHIR-CONT-1+2+3; 4 programme-level methods METH-CHIR-CONT-1+2+3+4; 15 foundational inputs FI-CHIR-CONT-1 through -15; cross-sector convergence at observable scale §6.5 as structural prediction of joint-paper format | Joint-paper-format cross-sector EFT closure question (Layer 4 bridge from substrate handle $\chi/6$ to observable scales via topological-projection argument). Adopts joint-paper format under OPEN-SD-CHIR-PRIMITIVE umbrella; THEO-CHIR-CONT-N theorem-naming convention parallels SF-Line's THEO-CAP-N + SD's THEO-SD-CHIR-N (sector-agnostic bridge theorems for cross-sector unification). Second flagship outside SF-N; first with ex ante joint-paper format adoption at viability decision gate. First flagship in CPP programme history to achieve three-reviewer convergence at first reviewer round each. |

**Pattern observation.** Both papers were not anticipated in the Session 41 7-paper SF-line architecture (Patch 0301). Capotauro emerged from OPEN-SM-4 substrate-vacuum chirality work via Reading C closure trajectory at Sessions 87–135; Chirality Continuum emerged as the natural Layer 4 EFT extension of Capotauro v2.0's substrate-level cross-sector unification (next-window seed from Patch 0481c → flagship paper at Patches 0482–0509 single extended session). The pattern suggests substrate-mechanism flagships and cross-sector Layer 4 flagships are durable emergent categories of the CPP flagship corpus alongside the SF-N family/sector flagships. Future flagship candidates in these categories: OPEN-SD-CHIR-PRIMITIVE manifestations (iv) thermodynamic causal arrow + (v) cosmological-vacuum asymmetry Layer 4 closures (per `future_projects.md` F.2 + F.3 priorities; estimated 4–10 sessions each).

## Operational discipline — family switches

The SF-line is developed serially with one Claude conversation window active at a time. Default primary work is the active heavy-lift paper (currently SF-4). Other family/sector papers are advanced as derivation logic dictates rather than by fixed shipping priority — when a specific identified derivation gap in the active paper is most cleanly closed by first developing a specific result in another family, work switches to that family until the result ships, then returns.

Every such switch is recorded in [`SF-line_switch_log.md`](SF-line_switch_log.md) with trigger, target, planned return condition, and outcome (filled in on return). The protocol exists to prevent procrastination disguised as redirection, to make the SF-line's actual development path readable to future reviewers, and to keep family-switches grounded in derivation logic rather than paper-shipping pressure or vague stuckness.

## Architecture history

| Session | Date | Architecture | Notes |
|---------|------|--------------|-------|
| S36 close+ | 7 May 2026 | Single-paper Track 1 (hierarchy paper) | Original framing; dissolved at S37 |
| S37 | 8 May 2026 | `flagship_papers/` folder created (patch 0293), Track-1 outline migrated | Hierarchy paper as flagship-class artifact |
| S38 | 9 May 2026 | 5-paper Option-3: SF-1 through SF-4 family papers + SF-5 unification (patch 0295) | Replaced single-paper Track 1 |
| S41 | 9 May 2026 | **7-paper architecture: SF-1 through SF-6 family/sector papers + SF-7 grand unification** (patch 0301) | SF-2 scope-narrowed to cage bosons only; SF-5 strong and SF-6 electromagnetism added; SF-5-original renumbered to SF-7 |
| S122 | 16 May 2026 | **Flagship corpus extended outside SF-N convention with Capotauro v1.0 SHIP** (patch 0415) | First flagship outside SF-N; substrate-mechanism flagship for OPEN-SM-4 sub-claim (c) substrate-vacuum chirality |
| S135 | 19 May 2026 | **Capotauro v2.0 v1.0 SHIPPED** (patch 0479) — first flagship to undergo substantive v2.0 extension | Three-way cross-sector substrate-level unification under OPEN-SD-CHIR-PRIMITIVE umbrella; 12 FIs; 3 theorems; 11-route falsifier set |
| S137 | 20 May 2026 | **Flagship corpus extended outside SF-N convention with Chirality Continuum v1.0 SHIP** (patch 0509) | Second flagship outside SF-N; joint-paper-format flagship for Layer 4 EFT cross-sector closure; THEO-CHIR-CONT-N theorem-naming convention; first three-reviewer convergence at first reviewer round each in CPP programme history |

---

*Architecture established at Session 38 opening (patch 0295) per Thomas's strategic adoption of Option-3 four-family + SF-5 unification; revised at Session 41 (patch 0301) to 7-paper architecture per Thomas's structural-symmetry observation that gluon and photon are not cage-bound bosons and warrant their own flagships. Original folder established Session 37 (patch 0293). See [`../research_priorities.md`](../research_priorities.md) for the strategic frame.*
