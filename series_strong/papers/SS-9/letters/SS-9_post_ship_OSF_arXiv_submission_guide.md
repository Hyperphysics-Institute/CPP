# SS-9 v1.0 Post-Ship Public Posting Guide — OSF Deposit + arXiv Submission

**Purpose**: This document provides the operational protocol for publicly posting SS-9 v1.0 via OSF deposit (DOI 10.17605/OSF.IO/JXE8D registered earlier) and arXiv submission, as the venue for **sub-task (e)** in its rescoped form ("open invitation post-v1.0 ship via public posting").

**Created**: 7 May 2026 Session 33 (paper completion sequence Track 4).

**Status at creation**: SS-9 v1.0 SHIPPED to GitHub origin/main at commit `84ee07f` Session 32 push (7 May 2026). Conditional theorem closure paper, 32 pages compiled, three pdflatex passes zero errors. Polish track FINAL with sub-tasks (a)–(d.7) DONE and (e) RESCOPED. Cumulative seven-pass review tally with all converged on v1.0-ready (d.1 ChatGPT v0.4, d.2 CoPilot v0.5, d.3 ChatGPT v0.6, d.4 ChatGPT v0.7 post-cache-bust, d.5 Grok v0.7, d.6 CoPilot v0.7, d.7 ChatGPT v0.8 with figure fixes at v0.9).

**Audience**: Thomas (decision authority on submission timing) and Isak (primary OSF executor per existing programme practice).

---

## 1. Pre-submission checklist

Before initiating any public posting, verify the following items on the local repository at `~/Documents/GitHub/CPP` (must be at origin HEAD `84ee07f` or later):

- **Paper compiles cleanly**: three pdflatex passes from a fresh build directory produce 32 pages with zero errors after pass 3. Pre-flight bare-c_i pattern check shows zero hits in the paper body. Title page renders "Version 1.0 — 7 May 2026 (conditional theorem closure paper; v1.0 promotion from v0.9 on the explicit basis of seven independent AI review passes; sub-task (e) external/human review rescoped to open invitation post-v1.0 ship via public posting — see Note on v1.0 designation in §9)" with the §9 cross-reference correctly resolved.

- **Figure 1 invariants verified**: all 8 panels of the FvdW deltahedra figure pass the programmatic invariant audit per Lesson 6 (see `series_strong/papers/SS-9/documentation_suite/transcript-SS-9.md` transactions 681–685 for the audit script, or `reasoning-SS-9.md` Session 32 §II for the full mechanism description).

- **Bibliography is correct**: all `\bibitem` entries are cited in the body; no orphan entries (the `ss10_forthcoming` entry was removed at v0.8 per Grok d.5 housekeeping). All in-body citations resolve to bibliography entries with no `??` placeholders.

- **All cross-references resolve**: section references, theorem references, equation references, figure references all show the correct numbers in the compiled PDF. No `Reference ... undefined` warnings in the build log.

- **PDF is the v1.0 PDF**: the OSF deposit and arXiv upload must reflect the v1.0 source on GitHub origin/main. If the local working tree has uncommitted changes (`git status --short` shows any output other than possibly the `SS-9_OPEN-SS-32_Ushape_anharmonic_phase4.py` Session 11 leftover), do not submit; either commit-and-push or reset to origin first.

- **License decision documented**: the public posting requires an explicit license declaration. Programme practice for the CPP papers is **CC BY 4.0** (Creative Commons Attribution 4.0 International) for both OSF and arXiv. This permits any reader to redistribute and adapt the work with attribution, which serves the programme's goal of broad scrutiny while preserving authorship attribution. The license should be declared on the OSF project page and selected in the arXiv submission form.

- **GitHub origin/main reflects v1.0**: confirm `git log origin/main --oneline -1` shows commit `84ee07f` (Session 32 v1.0 SHIP push) or later. The OSF deposit and arXiv source should be content-equivalent to this state.

If any pre-submission item fails, defer the public posting until the discrepancy is resolved. The post-v1.0 cadence does not have an external deadline — the v1.0 paper has been on GitHub since 7 May 2026 and remains accessible there for any reader who finds it via the repository link.

---

## 2. OSF deposit procedure

The OSF DOI **10.17605/OSF.IO/JXE8D** was registered earlier in the programme (per existing OSF practice for the SS series). The deposit step uploads the v1.0 artifacts to the registered project.

### 2.1 Artifacts to deposit

- **Primary**: `SS-9_simplicial_alpha_polytope_connectivity.tex` (LaTeX source, v1.0)
- **Primary**: `SS-9_simplicial_alpha_polytope_connectivity.pdf` (compiled PDF, 32 pages, 538,873 bytes per Session 32 build)
- **Bibliography**: `cpp_references.bib` (the central CPP bibliography file, single source of truth per OPEN-WORKFLOW-1)
- **Optional supporting material**: a copy of the `series_strong/papers/SS-9/sketches/` folder for transparency about the development trajectory; the `documentation_suite/` four-tier files for Tier 4 verbatim reasoning visibility. These are not required for submission but support the open-science framing.

### 2.2 OSF metadata fields

Fill in the OSF project page metadata as follows:

- **Title**: "SS-9: Conditional Derivation of Simplicial Alpha-Polytope Connectivity from CPP Lattice Geometry"
- **Authors**: Thomas Lee Abshier, ND (corresponding); Claude Opus (Anthropic)
- **Affiliation**: Hyperphysics Institute, Kalispell, Montana
- **Contact email**: drthomas007@protonmail.com
- **DOI**: 10.17605/OSF.IO/JXE8D (already registered)
- **Description (abstract)**: Use the abstract from the paper's compiled PDF (visible on the title page below the author block).
- **Tags / keywords**: nuclear physics, alpha-cluster theory, simplicial polytope, Steinitz's theorem, Freudenthal–van der Waerden classification, conditional theorem, Conscious Point Physics, CPP, 600-cell lattice, mathematical physics
- **License**: CC BY 4.0
- **Date**: 7 May 2026

### 2.3 Project description text (suggested)

The OSF project page benefits from a short description that orients new readers. Suggested text:

> SS-9 is a conditional theorem closure paper deriving simplicial alpha-polytope connectivity from the CPP lattice geometry under a registered hypothesis stack (C1' + C2 + C3 + C5 + C6 + C7 + C8 + rigid packing + 3D-non-degeneracy). The five-clause Theorem 6.1 establishes that the alpha-cluster contact graph is the 1-skeleton of the unique Freudenthal–van der Waerden convex deltahedron at FvdW values $N_\alpha \in \{4, 5, 6, 7, 8, 9, 10, 12\}$, with edge count $|E| = 3N_\alpha - 6$ exactly — the simplicial-polytope assumption used as a paper-level structural hypothesis (C4) in SS-7 and inherited by SS-8 is now derived as a theorem clause. The conditions C5/C6/C7/C8 first-principles closure are registered as programme-level open problems OPEN-SS-29/30/33/37 with multiple candidate closure routes including a distance-geometry / Euclidean-distance-matrix / rigidity-theory / realization-spaces approach (Route (d)). The paper was advanced to v1.0 on the explicit basis of seven independent AI review passes; sub-task (e) external/human review was rescoped from "blocking gate" to "open invitation post-v1.0 ship via public posting" because no human domain-expert reviewer was available in the author's research network. Domain-expert feedback from nuclear physics, alpha-cluster theory, computational geometry, and discrete mathematics is actively invited.

### 2.4 Cross-references

- The OSF project page should link to the GitHub repository: https://github.com/Hyperphysics-Institute/CPP
- The README on GitHub (or `paper_catalog.md`) should include a back-link to the OSF DOI once the deposit is live.
- The arXiv submission (next section) should include the OSF DOI in the comments field.

### 2.5 Expected timing

OSF deposits are immediate (no review queue). The DOI resolves to the project page within minutes of upload completion.

---

## 3. arXiv submission procedure

arXiv is the standard preprint server in physics and mathematics. SS-9's content fits two arXiv categories.

### 3.1 Categories

- **Primary**: `nucl-th` (Nuclear Theory) — the alpha-cluster physics content
- **Secondary**: `math-ph` (Mathematical Physics) — the conditional theorem framework, Steinitz's theorem application, FvdW classification use, and Route (d) connections to EDM theory / rigidity theory / realization spaces

The combination signals appropriately to both the nuclear-physics audience (where empirical relevance lives) and the mathematical-physics audience (where the conditional theorem framework and Route (d) connections to recognized mathematical programmes are most useful for closure work).

### 3.2 Endorsement

arXiv requires an endorser for first-time submitters in a category. If Thomas does not yet have an `nucl-th` or `math-ph` endorsement, contact options include:
- A colleague or contact who has prior arXiv submissions in `nucl-th` or `math-ph` (most physics or applied-math academic researchers will have this)
- The arXiv endorsement-request form, which can be sent to potential endorsers along with the SS-9 PDF as evidence of submission-readiness

The endorsement requirement only applies once per category; subsequent submissions in the same category do not require new endorsement.

### 3.3 Upload format

arXiv strongly prefers **LaTeX source** over PDF-only submissions. The submission should be a tarball containing:

- `SS-9_simplicial_alpha_polytope_connectivity.tex`
- `cpp_references.bib`
- Any auxiliary files needed for compilation (none expected at v1.0; verify by trying a clean build from a fresh directory containing only those two files)

arXiv compiles the LaTeX source on its own infrastructure (a recent TeX Live distribution). The compile must succeed there. If the local Windows + MiKTeX build differs from arXiv's Linux + TeX Live, source-level adjustments may be needed (extremely unlikely for a paper that compiles with vanilla `pdflatex` and uses only the standard packages already in the v1.0 source: `amsmath`, `amssymb`, `amsthm`, `mdframed`, `tikz`, `tikzlibrary{positioning,calc}`, `hyperref`, `geometry`).

### 3.4 arXiv metadata fields

- **Title**: "SS-9: Conditional Derivation of Simplicial Alpha-Polytope Connectivity from CPP Lattice Geometry"
- **Authors**: "Thomas Lee Abshier, Claude Opus"
- **Abstract**: paste from paper title page (the standard abstract block; ~250 words)
- **Comments**: "32 pages, 1 figure (8 panels). Conditional theorem closure paper. Companion paper to arXiv:[SS-7 arXiv ID once posted] and arXiv:[SS-8 arXiv ID once posted]. OSF deposit: https://doi.org/10.17605/OSF.IO/JXE8D. GitHub source: https://github.com/Hyperphysics-Institute/CPP. v1.0 promoted from v0.9 on the explicit basis of seven independent AI review passes; sub-task (e) external/human review rescoped to open invitation post-v1.0 ship via public posting (see §9 'Note on the v1.0 designation' in the paper for the full rationale). Domain-expert feedback from nuclear physics, alpha-cluster theory, computational geometry, and discrete mathematics actively invited."
- **License**: CC BY 4.0
- **Primary subject class**: `nucl-th`
- **Cross-list**: `math-ph`
- **MSC classification (math-ph cross-list)**: 52B10 (3-dimensional polytopes), 52C25 (rigidity and flexibility of structures), 81V35 (Nuclear physics), 82D10 (Plasmas)
- **PACS classification (nucl-th)**: 21.60.Gx (Cluster models), 21.10.Dr (Binding energies and masses), 02.40.Pc (General topology), 02.10.Ox (Combinatorics; graph theory)

### 3.5 Expected timing

arXiv submissions go through a moderation queue:
- **Standard moderation**: 1–2 business days for typical submissions
- **Holds for review**: occasionally extends to 1 week if moderators request clarification (typical reasons: unclear category fit, formatting issues, content concerns). The conditional-theorem framing and explicit AI-review-only rescope documentation in the comments may invite moderator scrutiny; the response should be straightforward (the paper says exactly what its validation status is and what it claims to deliver).

### 3.6 Submission timing relative to OSF

OSF deposit can precede arXiv submission (immediate vs. moderated), allowing the arXiv comments to reference the live OSF DOI. Suggested order: OSF deposit first, then arXiv submission with OSF DOI in comments.

---

## 4. Post-submission tracking

### 4.1 Filing incoming external feedback

Sub-task (e) in its rescoped form is "open invitation post-v1.0 ship via public posting." Any incoming external feedback — from arXiv readers, OSF visitors, or direct email correspondence following the public posting — should be filed under:

```
series_strong/papers/SS-9/reviews/external/
```

with one Markdown file per reviewer per round, named `<reviewer-name>_<date>_<round>.md` (parallel to the existing AI-review filing convention in `reviews/` for the d.1–d.7 review materials, except those live at the AI-review level not external).

Each filed external review should be referenced in the next session log entry and in `Research_Frontier.md` (last-updated header note about external review activity).

### 4.2 v1.x revision triggers

External feedback that surfaces substantive issues triggers a v1.x revision on the same polish-track cadence as v0.1 → v1.0:

- **v1.1** for the first round of external-feedback incorporation (modeled on v0.5 sub-task d.1)
- **v1.2** for the second round (modeled on v0.6 sub-task d.2)
- ... and so on

The polish-track methodology applies: per-symmetric-honesty verification of each external point against the v1.0 source independently before incorporation; pure-accept disposition only on points confirmed real and well-grounded; push-back (with rationale) on points that misread the conditional-theorem framing or attempt to import standards inappropriate to a CPP-internal derivation.

### 4.3 Programme-level tracking

The Research_Frontier.md and future_projects.md files should be updated with each external-review event:

- Last-updated header for the session that received the feedback
- (A.2) entry status updated from "(A.2) COMPLETE" to "(A.2) v1.x revision in progress" when an external feedback round is being incorporated
- Returns to "(A.2) COMPLETE" after each v1.x ship

If external feedback is sustained over multiple rounds, the cumulative-review tally extends from seven AI passes (d.1–d.7) to "seven AI passes plus N external-reviewer rounds," matching the symmetric-honesty discipline applied throughout the polish track.

### 4.4 No-feedback case

If the public posting does not generate substantive external feedback within a reasonable window (programme suggestion: 6 months, but no fixed deadline), the v1.0 designation persists unchanged. The "AI-validated conditional theorem closure paper, ready for external feedback via public posting" status remains accurate; what would change is only the cumulative tally of external rounds (which would remain zero). Sub-task (e) in its rescoped form is satisfied by the act of public posting, not by the receipt of feedback.

---

## 5. Symmetric-honesty notes for the public-posting framing

Two specific framings should be preserved in any public-posting context:

### 5.1 The conditional-theorem framing

The paper does not claim to derive the FvdW realization unconditionally. It derives the FvdW realization under the registered hypothesis stack, with C5/C6/C7/C8 first-principles closure registered as programme-level open problems. A reader who interprets the paper as "Abshier and Claude have derived the alpha-cluster geometry from CPP" without attaching "conditionally on C5+C6+C7+C8" is misreading. The §9 Roadmap to v1.0 subsection's six-item enumeration plus the new "Note on the v1.0 designation" three-paragraph block plus the title block plus the CHANGELOG v1.0 entry all establish the conditional framing explicitly. The OSF abstract and arXiv comments should reinforce, not soften, this framing.

### 5.2 The AI-review-only basis

The v1.0 designation rests on seven AI review passes by three independent reviewers (ChatGPT, CoPilot, Grok). It does not rest on human domain-expert review, which was rescoped at v1.0 to "open invitation post-v1.0 ship via public posting" because no human domain-expert reviewer was available in the author's research network. A reader who interprets the v1.0 designation as "human-domain-expert-validated" is misreading; the paper itself states this explicitly in the §9 "Note on the v1.0 designation" paragraph. The OSF description and arXiv comments should preserve this transparency rather than soften it for marketing purposes. A paper that claimed v1.0 status without disclosing the AI-review-only basis would mislead readers about the validation type, and the symmetric-honesty discipline applied throughout the polish track would be broken.

---

## 6. Coordination with other paper completion sequence tracks

The SS-9 v1.0 ship is one component of the larger paper completion sequence (Session 33+). Other parallel tracks:

- **Anthology chapter at Rovelli/Scientific American register** (Session 34 planned): a dedicated narrative-style chapter that captures the SS-9 dramatic arc (the puzzle from SS-7's $3N_\alpha - 6$ formula; the clue that $3N_\alpha - 6$ is suspiciously Euler's formula; the journey through three lemmas and Steinitz's theorem; the conditional-theorem result; the four OPEN-SS-* registries that the proof itself reveals as not-yet-closed). Lives at `anthology/` (folder to be created at Session 34) parallel to SS-7 and SS-8 chapters.

- **TATWD integration as C4 closure on refined-C1 foundation** (Session 35 planned): SS-9 slots into the Standard Model emergence narrative in `CPP_the_theory.md` as the C4-derivation step that closes the simplicial-polytope structural assumption used by SS-7 and SS-8. Combined SS-7 + SS-9 reads: "from CPP primitives + refined-C1 + C2 + C3, get the binding formula plus the simplicial-polytope structure conditionally on C5/C6/C7/C8, with twelve zero-parameter nuclear binding predictions to within 1.5%."

- **Registers freeze** (this session, Session 33): paper_catalog.md SS-9 row updated from "Pre-paper / active development" to "OSF pending" with v1.0 SHIPPED state; theorem-registry.md adds THEO-SS-16 (SS-9 main theorem); master_glossary.md appends "Terms Added — SS-9 v1.0" with 6 new entries (Conditional theorem closure paper, FvdW classification, Note on v1.0 designation programme practice, Programmatic invariant audit, Schlegel diagram, Steinitz's theorem). Companion to this guide.

The four tracks together complete the SS-9 lifecycle from v1.0 ship through public posting, narrative integration into the anthology, and integration into the TATWD book.

---

## 7. Decision authority and execution

- **Decision authority on submission timing**: Thomas (the principal author and corresponding author).
- **Decision authority on submission categories and metadata**: Thomas, with input from this guide.
- **OSF execution**: Isak Gutierrez handles OSF submissions per existing programme practice (see `paper_catalog.md` "Publication Plan" section: "Isak Gutierrez handles OSF submissions"). The artifacts in §2.1 above plus the metadata in §2.2 should suffice.
- **arXiv execution**: Thomas or Isak, with the endorsement step in §3.2 handled per local practice.

If Thomas chooses to defer the public posting (e.g., to wait for the anthology chapter and TATWD integration to land first, presenting a more complete programme picture at posting time), that is a legitimate option. The paper has been on GitHub origin/main since 7 May 2026 and remains accessible there to any reader who finds it via the repository link.

---

*This guide will be referenced from Research_Frontier.md last-updated header for Session 33 and from the (A.2) entry in future_projects.md. Updates after each public-posting event (OSF deposit live, arXiv submission accepted, first external feedback received) should be appended to Section 4 of this document with date and patch number.*
