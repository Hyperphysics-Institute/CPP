# Flagship Papers

**Location:** `/CPP/flagship_papers/`
**Established:** 8 May 2026 (Session 37 opening, patch 0293)
**Strategic source:** [`/CPP/research_priorities.md`](../research_priorities.md)

---

## What this folder is for

These are the **apex papers** of the Conscious Point Physics programme: cross-cutting papers that solve named unsolved problems in physics, plus the eventual cross-domain unification paper. They are the papers a new reader should read first.

A flagship paper is distinguished from a series paper by its argumentative role, not by its source material. Series papers (SM, SS, EW, QM, SR, SD) are *derivation* papers — each takes the framework and derives the next thing. A flagship paper takes a body of completed derivations and presents them as a solution to a named problem in mainstream physics, or as a cross-domain synthesis. The audience entry point, the reviewer expectation, and the rhetorical shape all differ.

## Inclusion criterion

To live in `flagship_papers/`, a paper must do at least one of:

1. **Solve a named known-unknown** in mainstream physics — the hierarchy problem, the cosmological constant, strong CP, muon g-2, baryon asymmetry, and the like.
2. **Make a forced-choice prospective prediction** that an upcoming experiment will confirm or falsify, before measurement.
3. **Provide a cross-domain unification** — one framework deriving phenomena from multiple sectors, presented for an audience reading across sectors.
4. **Bridge to recognized mathematics** in a way that anchors the framework against the "numerology" pattern-match (Steinitz, Coxeter, Freudenthal–van der Waerden classification, polytope theory, distance geometry, rigidity theory, etc.).

The strategic rationale is in [`../research_priorities.md`](../research_priorities.md): paradigm shifts in physics are not driven by derivation accuracy alone; they require forced-choice predictions, solving known unsolved problems, cross-domain unification, and bridges to recognized mathematics. Flagship papers are the artifacts that carry those four ingredients to the physics community.

## Current contents

### Track 1 — Hierarchy problem reframing paper [ACTIVE]

[`hierarchy_problem/hierarchy_paper_outline.md`](hierarchy_problem/hierarchy_paper_outline.md) — outline with source-material map, comparison table draft, reviewer-anticipation analysis, and four open questions to resolve with Thomas before drafting begins.

**Working title:** *Hierarchy Without Hierarchy: Standard Model Mass Spectrum from 600-Cell Distance Shells.*

**Headline claim (draft):** CPP derives the entire Standard Model fermion mass spectrum — 12 masses spanning 12 orders of magnitude — from a single mass scale $M_0 = m_e \cdot z/\phi \approx 3.79$ MeV via 600-cell distance-shell multipliers and the K3 spectral structure. The Koide formula for charged leptons emerges as a spectral theorem rather than a numerical coincidence. The hierarchy "problem" — the 12-orders-of-magnitude span — becomes a deduction from the geometry of the 600-cell, not an empirical input.

**Status:** drafting begins Session 37+; estimated 5-8 sessions to v1.0 SHIP. Inclusion-criterion fit: (1) solves a named known-unknown ✓, (4) bridges to recognized mathematics ✓ (polytope theory, K3 spectral structure).

### Track 2 — Anomaly-targeting paper #2 [PLANNED]

Candidate selection deferred to post-Track-1 evaluation. Candidates ranked rough leverage × tractability: strong CP, cosmological constant (Grok pre-600-cell sketch needs rigorous redo in current formalism), muon g-2, Λ_QCD/proton mass, baryon asymmetry. Inclusion-criterion fit anticipated under (1) or (2) depending on candidate.

### Track 3 — Eight-experiment manifesto audit [PLANNED]

Audit the November 2025 viXra-targeted eight-experiment falsification manifesto against current post-SS-9 / post-SM-3-through-8 formalism. Outcome is either republish via Zenodo with proper DOI as v1.0 if 5+/8 hold up, or v1.1 manifesto with corrections then publish. High strategic value at low effort (1-2 sessions). Inclusion-criterion fit: (2) forced-choice prospective predictions.

### Track 4 — Cross-cutting unification paper [PLANNED]

The "one paper a senior physicist reads in an evening" — axiom set, seven sectors, distinctive predictions, falsifier. Source material: `CPP_the_theory.md` and the anthology chapters as draft material. Long-term high-leverage; 8-12 sessions when reached. Inclusion-criterion fit: (3) cross-domain unification.

## Why a separate folder

Three reasons:

1. **Discoverability.** A senior physicist or potential arXiv endorser opening the repo sees `series_*` folders and has to infer which papers to read first. Flagship papers carry the framework to the physics community; they should be the most visible artifacts in the repo, not the most buried.

2. **Argumentative role.** Series papers and flagship papers differ in rhetorical and strategic role even when they share source material. The hierarchy paper draws entirely from SM-2 through SM-10 source content, but its role is presenting that content *as a solution to a named problem* — not as the next derivation in the SM series. Filing it next to SM-10 makes it read as "another SM paper" when its strategic role is something different.

3. **Cross-disciplinarity.** Tracks 2-4 are inherently cross-cutting in source material. The cosmological constant paper draws from SM, SR, and SD; the unification paper draws from all six sectors. Forcing these into a series taxonomy distorts what they are. The flagship folder is their natural home.

## Relation to series papers

Flagship papers do not replace series papers — they build on them. The hierarchy paper cites SM-2 through SM-10 extensively; it does not duplicate their content. Series papers remain the derivation infrastructure; flagship papers present that infrastructure to external audiences in solving-named-problem form, in forced-choice-prediction form, or in cross-domain-unification form.

When a flagship paper relies primarily on a single series, that series' `README-series_*.md` should add a "Flagship synthesis" line linking to the relevant flagship paper, so a reader entering through the series finds the synthesis pointer.

## Folder convention

Each flagship paper lives in its own subfolder under `flagship_papers/`, named for the problem it addresses (e.g. `hierarchy_problem/`, `cosmological_constant/`, `unification/`). The subfolder houses the paper `.tex` and `.pdf` once produced, plus `documentation_suite/`, `letters/`, `scripts/`, `sketches/`, and `founders_voice/` per the SS-9 four-tier discipline as the paper develops. Outline-stage papers may live in their subfolder as a single `*_outline.md` until v0.1 drafting begins.

Filenames follow CPP convention: no version suffixes in filenames (version history lives in the internal CHANGELOG header).

---

*Folder established at Session 37 opening (patch 0293) per Session 36 close+ strategic conversation. See [`../research_priorities.md`](../research_priorities.md) for the strategic frame and [`../SESSION_36_HANDOVER_FOR_NEXT_CONTEXT.md`](../SESSION_36_HANDOVER_FOR_NEXT_CONTEXT.md) for the conversation that established the four-track priority order.*
