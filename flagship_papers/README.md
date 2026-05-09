# Flagship Papers

**Location:** `/CPP/flagship_papers/`
**Established:** 8 May 2026 (Session 37 opening, patch 0293)
**Architecture established:** 9 May 2026 (Session 38, patch 0295) — Option-3 four-family + unification SF-line
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

## The SF-line architecture (Option 3)

The Standard Model fermion-mass programme is structured as four family-paper flagships plus a unification synthesis. Each family paper presents the full first-principles derivation of one Standard Model family in apex-paper form; the unification paper synthesizes the four families into the headline answer to the hierarchy problem.

This architecture was established at Session 38 (9 May 2026) per Thomas's strategic posture of no-compromise rigor: every fermion mass parameter back to 600-cell + Conscious Point primitives, the "register-as-open" card used judiciously and one or two layers removed from the present problem where possible. The four-family structure honestly frames the work scope, gives each Standard Model family its apex venue, and produces a natural unification paper at the end. Sequential ship of SF-1 → SF-2 → SF-3 → SF-4 → SF-5 (with SF-1, SF-2, SF-3 likely concurrent or near-concurrent given they are primarily reframing of strong corpus, and SF-4 the heavy lift).

| ID | Paper | Folder | Status | Sessions to v1.0 | Inclusion-criterion fit |
|----|-------|--------|--------|---------------------|------------------------|
| **SF-1** | Charged Lepton Mass Spectrum from K3 + 600-Cell Geometry | [`charged_leptons/`](charged_leptons/) | Planned (lowest-risk; reframing) | 3–5 | (1), (4) |
| **SF-2** | Electroweak Sector Unification from 600-Cell Geometry | [`electroweak/`](electroweak/) | Planned (reframing + identified gaps) | 5–8 | (1), (3) |
| **SF-3** | Quark Sector Unification from 600-Cell Distance Shells | [`quarks/`](quarks/) | Planned (reframing) | 4–6 | (1), (4) |
| **SF-4** | Neutrino Sector Unification from 600-Cell Geometry | [`neutrinos/`](neutrinos/) | **Active — audit complete (Session 37); mechanism selection pending** | 10–14 | (1), (4) |
| **SF-5** | Standard Model Unification — Hierarchy Without Hierarchy | [`unification/`](unification/) | Planned (depends on SF-1..4 ship) | 5–8 | (1), (3), (4) |

The original Track-1 hierarchy paper outline (now in [`unification/hierarchy_paper_outline.md`](unification/hierarchy_paper_outline.md)) provides extensive source material for the eventual SF-5 synthesis; its structure shifted from single-paper-covering-12-masses to synthesis-of-four-family-papers when Option-3 was adopted at Session 38.

## Other flagship paper candidates (separate from the SF-line)

The SF-line covers the SM-fermion-mass programme. Two additional flagship-paper candidates from the original Session 37 four-track plan remain valid but are separate from the SF-line:

- **Anomaly-targeting paper #2** — cosmological constant, strong CP, muon g-2, $\Lambda_{QCD}$/proton mass, baryon asymmetry. Candidate selection deferred. Inclusion-criterion fit: (1) or (2).
- **Eight-experiment manifesto audit** — audit the November 2025 viXra-targeted eight-experiment falsification manifesto against current post-SS-9 / post-SM-3-through-8 formalism; republish via Zenodo if 5+/8 hold up. High strategic value at low effort. Inclusion-criterion fit: (2).

These are not yet scaffolded into folders; they are deferred-priority items that may be promoted in parallel with SF-line work as time and energy permit.

## Why this architecture

Three reasons over the alternatives (single-paper Track 1; two-paper SF-1-neutrino + SF-2-SM; SM-N-incremental-papers + SF-1):

1. **Honest decomposition of the work.** SF-1, SF-2, SF-3 are primarily reframing work over already-strong corpus (SM-3/4/6, SM-1/6, SM-7/8/9/10). SF-4 is the heavy lift (new derivation campaign). SF-5 is synthesis. Each piece is sized to its actual nature; nothing is overloaded.
2. **Sequencing produces compounding strategic momentum.** Ship SF-1 first (lowest-risk) while SF-4 derivation is in progress. By the time SF-4 ships, three flagship papers are already in the corpus; reviewers see CPP's track record before they engage with the hardest derivation.
3. **Audience separation by Standard Model family.** SF-1 for charged-lepton specialists, SF-2 for electroweak theorists, SF-3 for QCD/quark people, SF-4 for neutrino people, SF-5 for the broad physics audience reading across sectors. Each paper meets its audience where it is.

## Relation to series papers

Flagship papers do not replace series papers — they build on them. The SF-line cites the SM and SS series extensively; it does not duplicate their content. Series papers remain the derivation infrastructure; flagship papers present that infrastructure in solving-named-problem form, in forced-choice-prediction form, or in cross-domain-unification form.

When a flagship paper relies primarily on a single series, the series' `README-series_*.md` should add a "Flagship synthesis" line linking to the relevant flagship paper, so a reader entering through the series finds the synthesis pointer.

## Folder convention

Each flagship paper lives in its own subfolder under `flagship_papers/`, named for the family or the problem it addresses (e.g. `charged_leptons/`, `neutrinos/`, `unification/`). The subfolder houses the paper `.tex` and `.pdf` once produced, plus `documentation_suite/`, `letters/`, `founders_voice/`, and `sketches/` per the SS-9 four-tier discipline as the paper develops.

Filenames follow CPP convention: no version suffixes in filenames (version history lives in the internal CHANGELOG header).

The `sketches/` subfolder pattern is imported from SS-9's `series_strong/papers/SS-9/sketches/`: working documents that develop subsidiary derivations before integration into the main `.tex` source. They are open-source and effectively part of the paper for any reader who wants to see the development path.

## Operational discipline — family switches

The SF-line is developed serially with one Claude conversation window active at a time. Default primary work is the active heavy-lift paper (currently SF-4). Other family papers are advanced as derivation logic dictates rather than by fixed shipping priority — when a specific identified derivation gap in the active paper is most cleanly closed by first developing a specific result in another family, work switches to that family until the result ships, then returns.

Every such switch is recorded in [`SF-line_switch_log.md`](SF-line_switch_log.md) with trigger, target, planned return condition, and outcome (filled in on return). The protocol exists to prevent procrastination disguised as redirection, to make the SF-line's actual development path readable to future reviewers, and to keep family-switches grounded in derivation logic rather than paper-shipping pressure or vague stuckness.

---

*Architecture established at Session 38 opening (patch 0295) per Thomas's strategic adoption of Option-3 four-family + SF-5 unification. Original folder established Session 37 (patch 0293). See [`../research_priorities.md`](../research_priorities.md) for the strategic frame.*
