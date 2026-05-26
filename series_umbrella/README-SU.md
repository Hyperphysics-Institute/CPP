# Series Umbrella (SU)

**Location:** `/CPP/series_umbrella/`
**Purpose:** Top-level container for *problem-arc-organized* paper groupings and for heterogeneous papers awaiting a stable grouping pattern. SU is structurally distinct from the existing phenomenology-sector series at the `/CPP/` root level; it organizes papers by *which open problem they jointly attack*, not by *which sector of physics they describe*.
**Established:** 26 May 2026 (Session 144 Patch 0571d — first sub-umbrella `series_substrate_chirality_arc/` (SSCA) established with three migrated flagship papers; OS §15.13 codification follow-on at Patch 0571f).
**Audience:** Future Opus sessions adding papers that don't fit cleanly into a phenomenology-sector series, and the future programme-state in which a third or fourth problem-arc emerges.

---

## The two-axis taxonomy

The CPP corpus has been growing under a single organizing axis since its inception: papers are grouped by which sector of observed physics they describe. The `/CPP/` root contains directories for the strong sector (`series_strong/`), the standard model in the large (`series_standard_model/`), the electroweak sector (`series_electroweak/`), the quantum-mechanics sector (`series_quantum_mechanics/`), special relativity (`series_relativity/`), substrate dynamics (`series_foundations/dp-sea-polarization/` and related), and the sector-flagship phenomenology container (`flagship_papers/`). This axis — let us call it the *phenomenology axis* — is the way physics-as-discipline has organized itself for roughly a century. It is the axis along which graduate-level physics curricula are partitioned, the axis along which physics journals route submissions, and the axis along which experimentalists divide labor.

It is also not the only axis that organizes work. As the CPP programme has matured, a second axis has become operationally important: the *problem-arc axis*. A problem arc is a sequence of papers that share an organizing open problem rather than a phenomenology sector. The papers in an arc attack different phenomenology sectors but converge on closing the same umbrella problem. The Substrate-Chirality Arc — the first arc the programme has named — is the worked example: three papers (Capotauro, Chirality Continuum, F.1) sit in three different phenomenology territories (mass-mixing chirality in SM territory, electroweak V−A coupling in EW territory, substrate-locality in SD territory) but are bound together by the OPEN-SD-CHIR-PRIMITIVE umbrella problem and its five-manifestation enumeration.

The phenomenology axis cannot accommodate a problem arc. Capotauro could be placed in `series_standard_model/` because its primary observable lives in SM territory, but doing so would hide its membership in the chirality arc, would separate it from the other two arc papers that close different manifestations, and would make the OPEN-SD-CHIR-PRIMITIVE umbrella structurally invisible at the filesystem level. The information loss is real and compounds as additional arcs emerge.

SU exists to make the second axis explicit. The `/CPP/` root now has eight phenomenology-organized peers (the existing six sector series + the sector-flagship container + the new SU container) plus the SU container, which is itself problem-arc-organized internally. A reader visiting `/CPP/` sees the two axes side by side: phenomenology folders at root, problem arcs inside SU. The taxonomic information lives in the file path.

The SU container is not a peer of the existing sector series even though it sits at the same root level. It is a *different kind* of container. Sector series are organized along one axis; SU is the container for everything organized along the second axis. The peer relationship is between SU and the union of the sector series, not between SU and any individual sector series.

## What lives inside SU

Two kinds of contents:

**(1) Sub-umbrellas** — folders named `series_<arc-name>/` that group papers sharing a stable problem-arc identity. Each sub-umbrella has its own README and its own internal organizing principle (an umbrella problem, a methodology, a cross-sector closure pattern, or whatever parameter is most prominent for the arc). The first sub-umbrella is `series_substrate_chirality_arc/` (SSCA), established at Patch 0571d alongside SU itself. Future sub-umbrellas might cover cross-sector closure methodology, cosmological phenomenology, conditional-theorem framework development, or any other organizing principle that consolidates two or more papers into a coherent arc.

**(2) Ungrouped papers** — papers that don't fit any existing sub-umbrella and have no identified arc-membership yet. These live directly under `series_umbrella/<paper-name>/` and accumulate until a grouping pattern becomes obvious. The accumulation is friction-free: a new paper that doesn't fit a phenomenology sector goes into SU without requiring an arc-membership decision. When two or more accumulated papers share a stable organizing principle, a sub-umbrella folder is created and the papers migrate in via `git mv` at a regrouping Patch.

The accumulate-then-group workflow is deliberate. The alternative — requiring every new SU paper to identify its arc-membership at creation time — would slow paper creation and would force premature grouping commitments. The cost of the accumulate-then-group approach is occasional regrouping overhead (a `git mv` Patch every few months when a new sub-umbrella emerges); the benefit is that the programme can write papers without first solving their taxonomic placement, and groupings emerge organically from the work rather than being imposed in advance.

## Existing sub-umbrellas

### `series_substrate_chirality_arc/` — SSCA

Established 26 May 2026 (Patch 0571d). Three papers: Capotauro (v1.0 + v2.0), Chirality Continuum, and F.1 Dynamical Substrate Law. All three sit under the OPEN-SD-CHIR-PRIMITIVE umbrella problem, which scopes the substrate's primitive chirality as a cross-sector unification target across five named observable manifestations:

- (i) K3-doublet mass-mixing chirality — CLOSED by Capotauro v1.0/v2.0 (THEO-CAP-1).
- (ii) Electroweak V−A coupling — CLOSED at substrate level by Capotauro v2.0 (THEO-SD-CHIR-1); Layer 4 EFT closure by Chirality Continuum (THEO-CHIR-CONT-2).
- (iii) Electromagnetic-handedness — **OPEN**, no current closure-trajectory machinery.
- (iv) Thermodynamic causal-arrow direction — CLOSED at sketch-document Layer 3 by F.1 (THEO-DSL-3).
- (v) Cosmological-vacuum asymmetry — **OPEN**, registered as OPEN-FP-F1-4.

Three of five manifestations are closed at varying rigor levels; two remain open. SSCA's canonical manifestation tracker lives at `series_substrate_chirality_arc/manifestation_inventory.md`. The detailed arc-level README at `series_substrate_chirality_arc/README-SSCA.md` covers the arc's history, its methodology cross-references, and its future-trajectory candidates.

## Adding a new paper to SU

When a new paper doesn't fit cleanly into an existing phenomenology sector (the standard test: does the paper's primary closure-target sit in SS / SM / SEW / SQM / SR / SD territory exclusively, or does it span sectors / address a programme-level umbrella problem / introduce methodology that isn't sector-bound?), it goes into SU. Two cases:

**(a) The paper belongs to an existing sub-umbrella.** Place it under that sub-umbrella's folder directly. Update the sub-umbrella's README and its manifestation/inventory tracker. Standard paper-creation discipline (sketches, documentation_suite, reviews directories) applies inside the sub-umbrella.

**(b) The paper does not belong to any existing sub-umbrella.** Place it under `series_umbrella/<paper-name>/` directly. No sub-umbrella assignment required. The paper accumulates here until a grouping pattern emerges.

## Regrouping discipline (the OS-level check)

Per the OS §15.13 codification (Patch 0571f), every paper-completion Patch that touches an SU paper triggers a brief **SU regrouping audit**:

- *Count*: how many ungrouped papers currently sit under `series_umbrella/` (i.e., not inside any sub-umbrella folder)?
- *Threshold*: if the count is ≥ 3, examine the ungrouped papers' open problems, methodologies, and closure-targets for shared organizing principles.
- *Decision*: if two or more ungrouped papers share a stable organizing principle (an umbrella problem registered in `research_frontier.md`; a cross-sector closure methodology; a programme-level theorem chain; or any other arc-identifying signature), create a sub-umbrella folder and propose the migration in a regrouping Patch. The migration is `git mv` (preserving paper history) + new `README-<arc>.md` (the arc's introduction) + new tracker file (the arc's organizing principle made explicit) + path-reference sweep across the corpus.
- *N/A escape valve*: if no shared organizing principle is identified, the count stays as-is; the audit is recorded as "N/A — no grouping pattern" in the paper-completion Patch's audit table and re-fires at the next paper-completion Patch touching SU.

The threshold of 3 is empirical: 2 papers can share a principle by coincidence; 3 papers sharing a principle is usually a real arc. The threshold may be tightened or loosened by future codification based on observed cadence.

## Naming conventions inside SU

- **Sub-umbrella folder names**: `series_<topic>/` with topic as a short underscore-separated phrase (e.g., `series_substrate_chirality_arc`). The acronym is constructed by taking the first letter of each significant word (SSCA for Substrate Chirality Arc; the leading "S" in the folder name stands for "series", not for the topic — the acronym takes only the topic letters).
- **Sub-umbrella README**: `README-<acronym>.md` (e.g., `README-SSCA.md`) — matches the actual-practice form used in `series_foundations/README-series_foundations.md`, `series_quantum_mechanics/README-series_quantum_mechanics.md`, `series_electroweak/README-EW.md`. The OS §11 spec is `{scope}-README.md`; actual practice has settled on `README-{scope}.md`; the latter form is used here. (The OS §11 spec / actual-practice divergence is a candidate housekeeping item for a future Patch.)
- **Tracker files inside a sub-umbrella**: named for the arc's organizing principle (e.g., `manifestation_inventory.md` for SSCA's five-manifestation enumeration). No README/INDEX prefix.
- **Ungrouped paper folders**: `series_umbrella/<paper-name>/` directly — same as if the paper were inside a sub-umbrella, just one folder level shallower.

## Relationship to existing taxonomy

The pre-SU taxonomy at `/CPP/` root recognized two kinds of paper containers: phenomenology-sector series (`series_<sector>/`) and the sector-flagship container (`flagship_papers/`). The post-SU taxonomy adds a third kind: the problem-arc container (`series_umbrella/`). The three kinds correspond to three operational categories:

1. **Sector series** — papers that close a phenomenology sector via a sequence of related results within that sector. Identifier: `S<short-sector-code>` (SS, SM, SEW, SQM, SR, SD). Examples: SS-7, SS-8, SS-9 in `series_strong/`; SM-3, SM-4 in `series_standard_model/`.
2. **Sector flagship** — single-paper flagship that closes a sector phenomenology at flagship-level generality. Identifier: `SF-N` (SF-2, SF-4). Examples: SF-2 in `flagship_papers/electroweak/`; SF-4 in `flagship_papers/neutrinos/`. The `flagship_papers/` container's contents are sector-flagship papers after the SSCA migration; the three migrated papers were not sector-flagship in this sense.
3. **Problem-arc paper** — paper that closes a manifestation of an umbrella problem or otherwise contributes to a cross-sector closure programme. Identifier varies (F-N for F-line flagships closing OPEN-SD-CHIR-PRIMITIVE manifestations; paper-name-only for F-line precursors like Capotauro and Chirality Continuum that predate the F-line numbering). Examples: F.1 in SSCA; Capotauro v1.0/v2.0 in SSCA; Chirality Continuum in SSCA.

The three categories are not mutually exclusive at the paper-content level — a phenomenology-sector paper can contribute to a problem arc (SF-2's chirality work feeds OPEN-FP-SF-2-CHIR which feeds into Chirality Continuum), and a problem-arc paper can have phenomenology-sector content (F.1's substrate-locality derivation references quantum-mechanical primitives). But the categories are mutually exclusive at the *paper-container-membership* level: each paper lives in exactly one folder, and the folder reflects the paper's *primary* taxonomic identity.

When a paper's primary identity is ambiguous, the SU container is the default. Papers move out of SU into a sector folder if they turn out to be primarily sector-bounded; papers move into a sub-umbrella when an arc-membership becomes obvious. Both kinds of migrations are mechanical (`git mv` + path-reference sweep + sub-umbrella tracker update).

## Future evolution

The SU mechanism is designed to be extended without restructuring. Anticipated patterns:

- **Sub-umbrella creation** when accumulated ungrouped papers reach the regrouping threshold and share an organizing principle. Pattern: `git mv` ungrouped papers into a new `series_<arc-name>/` folder; create `README-<acronym>.md` + tracker file; path-reference sweep.
- **Sub-umbrella retirement** when all of an arc's manifestations or sub-claims close. Pattern: the arc's papers remain in their folder (as historical record); the README is updated to reflect the closed-arc status; the arc no longer attracts new papers. (The arc folder is not deleted — the closure is itself programme-state-significant.)
- **Paper migration between sub-umbrellas** if a paper's arc-membership is reassessed. Rare. Pattern: same as sub-umbrella creation but with single-paper scope.
- **Cross-sub-umbrella papers** if a paper closes manifestations of two different umbrellas simultaneously. Provisionally placed under the primary umbrella with the secondary umbrella's tracker file noting the cross-membership. No physical duplication.

The accumulate-then-group workflow is the load-bearing discipline. The SU mechanism makes paper creation cheap by removing the taxonomic gate at paper-creation time. Regrouping audits at paper-completion time keep the corpus from drifting into permanently-ungrouped accumulation. The combination is intended to scale to a programme an order of magnitude larger than the current corpus.

— Established at Patch 0571d (26 May 2026); discipline reference `templates/operating_system.md` §15.13 (Patch 0571f).
