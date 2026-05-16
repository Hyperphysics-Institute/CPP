# CPP Paper Formatting Standard

**Location:** `/CPP/templates/paper-formatting.md`
**Purpose:** Master template for generating and finalising all CPP series papers.
**Last updated:** 24 April 2026 (added §15 cross-reference to operating_system.md §11 for filename convention after SS-8 v0.1 rename correction; added §§4.1A and 4.1B CP/GP Signature and Swarm-Validation Contribution required subsections per PD-001; previously 2 April 2026)
**Maintainer:** Thomas Lee Abshier ND, with AI team

---

## How to Use This Document

When generating a new `.tex` file or finalising an existing one, the AI assistant should read this file first and apply all standards below. This document is the single source of truth for CPP paper formatting.

The human author may provide a shorthand prompt referencing this file:
> "Generate the final .tex file for [paper]. Follow `/CPP/templates/paper-formatting.md`."

The AI should then apply every section of this standard without needing individual reminders.

---

## 1. Document Class and Packages

### 1.1 Required Preamble

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{amsmath,amssymb,amsfonts,amsthm}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{hyperref}
\usepackage{booktabs}
\usepackage{array}
\usepackage{enumitem}
\usepackage{float}
\usepackage[font=small, labelfont=bf]{caption}
\usepackage{parskip}
\usepackage{mdframed}

% SVG figure support
\usepackage{svg}
\svgsetup{
    inkscapelatex=false,
    inkscapeformat=pdf,
    inkscapepath=svgdir}

% Bibliography
\usepackage[authoryear,round]{natbib}
\bibliographystyle{plainnat}

% Hyperlinks
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    citecolor=blue,
    urlcolor=blue
}
```

### 1.2 Theorem Environments

```latex
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}
```

### 1.3 Standard CPP Macros

```latex
\newcommand{\lP}{l_P}
\newcommand{\tP}{t_P}
\newcommand{\EP}{E_P}
\newcommand{\SSV}{\mathrm{SSV}}
\newcommand{\phig}{\varphi}          % golden ratio
\newcommand{\Tr}{\operatorname{Tr}}
```

Add paper-specific macros after these standard ones, with a comment block:

```latex
% --- Paper-specific macros ---
\newcommand{\Kthree}{\mathrm{K}_3}
```

---

## 2. Title Block

### 2.1 Format

```latex
\title{\textbf{[SERIES]-[NUMBER]: [Full Title]}\\[6pt]
{\large [Series identifier line, e.g. "Conscious Point Physics Flagship Paper Series"]}\\[4pt]
{\Large \textbf{Version [X.Y] --- [Date]}}}

\author{Thomas Lee Abshier, ND \and [AI authors]}

\date{\normalsize Hyperphysics Institute, Kalispell, Montana\\
\url{https://hyperphysics.com}\\
\href{mailto:drthomas007@protonmail.com}{drthomas007@protonmail.com}\\[4pt]
\small OSF DOI: [DOI if registered]}
```

**Clean title-page convention (adopted Patch 0408, Session 115; codified Patch 0409, Session 116).** The title block renders ONLY: title, sub-title or series identifier (if any), Version line + date, author, institution address block. The title block MUST NOT contain a visible version-history paragraph (e.g., `{\normalsize v0.X incorporates ... v0.(X-1) shipped ...}`). Such paragraphs were standard before 16 May 2026 but are retired because they ambush first-time readers with programme archaeology before the abstract. Programme-internal version archaeology lives in `documentation_suite/changelog-<paper>.md` (see `operating_system.md` ``Version-archaeology architecture rule'').

### 2.2 Version Numbering

- v1: first complete draft
- v2, v3...: revisions incorporating review feedback
- v2.1, v2.2...: minor cosmetic/formatting changes within a revision

Always update the version number in the title when changes are made.

### 2.3 Timestamps and Timezones

- **Development documents, session logs, timelines:** Mountain Time, always labelled explicitly. Use MDT (UTC-6) March–November, MST (UTC-7) November–March. Example: `1 Apr 2026, 3:15 PM MDT`.
- **Paper headers, version blocks, `.tex` title dates:** Date only, no clock time. Example: `2 April 2026`.
- **Git commits and OSF metadata:** UTC (automatic — do not override).

### 2.3 Author Block

AI co-authors appear on the author line with their platform in parentheses:
- `Grok (xAI)`
- `Claude Opus (Anthropic)` or `Claude Sonnet (Anthropic)` — use the specific model
- `Copilot (Microsoft)`

Include only those AIs that made substantive contributions to the paper's content. The Acknowledgements section provides detailed attribution.

---

## 3. Comment Blocks

### 3.1 Source-file header block

Place at the very top of the `.tex` file, before `\documentclass`:

```latex
% ============================================================
% [SERIES]-[NUMBER]: [Short Title]
% [Optional one-line descriptor — e.g. "A Conditional Theorem Closure Paper for OPEN-XX-N"]
% Conscious Point Physics Flagship Paper Series (or appropriate series identifier)
% Version history: flagship_papers/<paper>/documentation_suite/changelog-<paper>.md
% ============================================================
```

**No CHANGELOG comment block in source (adopted Patch 0408, Session 115; codified Patch 0409, Session 116).** The historical pattern of prepending `% Version 0.X -- ...` comment blocks at the top of `.tex` source files (sometimes growing to 300+ lines of session-by-session development narrative before the first non-comment line) is retired. These blocks bloated source files and discouraged researcher entry into the paper source. Source-file headers now carry only the minimal identification block above plus a pointer to the canonical changelog file.

Contributor attribution that previously lived inside CHANGELOG blocks now lives in the paper's Acknowledgements section (when the 7-file documentation suite is produced post-v1.0) or in the `documentation_suite/changelog-<paper>.md` file's per-version entries (during v0.x drafting).

### 3.2 Section Markers

Use `%` comment dividers to mark major sections for navigation:

```latex
% ============================================================
% SECTION 3: Part I — The Weinberg Angle
% ============================================================
\section{Part~I: The Weinberg Angle}
```

### 3.3 Figure Insertion Comments

When figures are inserted, add a comment block explaining placement:

```latex
% ============================================================
% FIGURE 2 — K₃ face with closed neighbourhood
% INSERT after the isotropy theorem, before the Koide phase proof.
% Source: /CPP/series_standard_model/figures/figures_SM-6/fig2_k3_neighbourhood.svg
% ============================================================
\begin{figure}[H]
```

---

## 4. Document Structure

### 4.1 Order of Sections (after `\begin{document}`)

```
\maketitle
\begin{abstract} ... \end{abstract}
\textbf{Keywords:} ...

\textbf{Plain Language Summary:} ...

\raggedright
\tableofcontents
\newpage

\section{Introduction}
\subsection{Open Problems Addressed}   % ← list which Research_Frontier.md entries this paper confronts
\section{...}  (body sections — definitions, lemmas, theorems, proofs)
\section{Physical Interpretation}       % ← CPP mechanism: what physical objects are involved and what are they doing?
\subsection{CP/GP Signature at This Scale}    % ← REQUIRED (PD-001, 24 Apr 2026); see §4.1A below
\section{CPP-to-Conventional-Physics Mapping}  % ← structural correspondence table
\section{Conclusion}
\subsection{Swarm-Validation Contribution}    % ← REQUIRED (PD-001, 24 Apr 2026); see §4.1B below
\subsection{Problem Status After This Paper}  % ← state new status of each problem addressed
\section*{Acknowledgements}
\bibliography{...}
\appendix  (if needed)
```

**Open Problems Addressed** (in Introduction): List each `Research_Frontier.md` entry the paper confronts, by ID and short title. Example:
```latex
\subsection{Open Problems Addressed}
This paper addresses OPEN-SS-11 (SU(3) operator uniqueness) and
advances CONJ-SM9-1 (pair counting decomposition) to partially proved status.
```

**Physical Interpretation** (after the mathematical derivation): Explain the CPP mechanism in terms of CPs, DPs, chains, cages, SSV fields, and DI-bit propagation. What physical objects are involved? What are they doing? Where is the energy? This section should be intelligible to a physicist who accepts the CPP ontology but hasn't read the mathematical proof. Example: SS-3 §5 identifies the 8 gluon degrees of freedom as 4 linear DP-chain bond oscillations + 4 coupled harmonic junction oscillations on the polarity-structured tetrahedron.

**CPP-to-Conventional-Physics Mapping** (after Physical Interpretation): Provide a table or structured comparison showing how each element of the CPP mechanistic account corresponds to the conventional physics description. The mapping is *structural*, not literal — CPP operates at a finer granularity than perturbative QFT. The correspondence is at the level of symmetry, degrees of freedom, and observable predictions.

#### 4.1A CP/GP Signature at This Scale (REQUIRED — per PD-001, 24 April 2026)

Every CPP paper includes this subsection, typically as the final subsection of Physical Interpretation. Rationale and full context: `programmatic_decisions/PD-001-signature-thread-and-swarm-convention.md`.

The subsection must do three things, each in its own paragraph or labelled block:

1. **Load-bearing axiom identification.** Name which axiom(s) do load-bearing work in this paper's derivation. Example (SS-8): A2 (600-cell topology, supplying $z=12$), A5 (propagation efficiency, supplying $1/\varphi$), A8$'$ (cage-volume scaling, supplying $M_0 = m_e z/\varphi$), A11 (lattice-scale grounding, fixing MeV units via $\Lambda_{\text{QCD}}$).

2. **Visible-vs-smoothed discreteness.** Identify where the discrete lattice structure is still visible in the paper's result — the $\varphi$ factors, the $z=12$ coordination, the $K_3$ recurrence, the simplicial-polytope combinatorics — versus where the discreteness has been averaged-out by summing over many lattice sites, cage volumes, or DP-sea contributions. This is where Thomas's orders-of-magnitude-dilution concern is explicitly addressed.

3. **Macroscopic shadow correspondence.** Note which empirical regularity in conventional (non-CPP) physics is the macroscopic shadow of the sub-quantum discreteness articulated by this paper. Example (SS-8): the $2E/V$ scaling law is the macroscopic shadow of nucleon-nucleon $K_3$ collective modes happening at many simultaneous contact faces at each alpha-vertex; what conventional nuclear physics calls "mean-field pairing" is, in CPP, the averaged-out manifestation of discrete face-participation counting.

Purpose: without this subsection, readers (reviewers, critics, later curriculum readers) have no anchor connecting the paper's macroscopic-scale predictions to the programme's sub-quantum foundations. Including it makes the CP/GP-to-conventional-physics thread explicit within each paper, without requiring the heavy metaphorical/illustrative work that belongs in the curriculum-development phase. Length: typically half to one page; longer only when the signature is especially intricate.

#### 4.1B Swarm-Validation Contribution (REQUIRED — per PD-001, 24 April 2026)

Every CPP paper includes this subsection as the standard closing subsection of Conclusion, immediately before Problem Status. Rationale and full context: `programmatic_decisions/PD-001-signature-thread-and-swarm-convention.md`.

The subsection is short (one paragraph typical, formulaic) and states:

1. **Predictions added.** How many zero-parameter (or explicitly-parameter-counted) empirical correspondences this paper contributes. Example (SS-8): 12 primary ($N_{\text{ex}} = 2$) + 30 secondary ($N_{\text{ex}} \in \{3,\ldots,8\}$) = 42 predictions.

2. **Running swarm total.** The cumulative count of zero-parameter empirical correspondences across the entire CPP programme as of this paper, derived from the same unchanged axiom stack. Source: `predictions.md` cumulative-counter header (to be added).

3. **Implausibility-of-accident statement.** A brief statement that the probability of such correspondence from accident or hidden tuning scales as $(\text{residual band} / \text{typical parameter space})^N$ and is astronomically small at the swarm's present size.

Purpose: the programme's epistemic weight lives in the cumulative swarm, not in any individual paper's result. Without this closing subsection, each paper reads as an isolated correspondence that could plausibly be coincidence. With it, every paper participates in and reinforces the cumulative argument — the single most important thing each paper does for the programme as a whole.

**Retroactive adoption.** Existing papers (SS-5, SS-7, SM-3, SM-8, SM-11, etc.) will add both §4.1A and §4.1B at their next major-revision cycle; the mathematical content is already present and only the explicit articulation is being added. SS-8 v0.2 will establish the realized template.

**Problem Status After This Paper** (in Conclusion, after Swarm-Validation Contribution): State the updated status of each problem. Example:
```latex
\subsection{Problem Status After This Paper}
\begin{itemize}
\item OPEN-SS-11: OPEN → THEO (proved in Theorem 2)
\item CONJ-SM9-1: CONJ → PROP (partially supported; full proof pending SM-10 FEM)
\item NEW: OPEN-SS-15 (registered; emerged from Theorem 2 corollary)
\end{itemize}
```

### 4.2 Abstract Formatting

The abstract should be indented and justified (LaTeX default for the `abstract` environment). After the abstract, switch to `\raggedright` for the body text.

### 4.3 Keywords

Place immediately after the abstract, before the Plain Language Summary:

```latex
\medskip\noindent
\textbf{Keywords:} keyword1, keyword2, keyword3, ...
```

Include 8–15 keywords covering: the specific physics topic, the mathematical methods, the CPP framework terms, and any standard classification terms (e.g., "Koide formula," "spectral graph theory").

### 4.4 Plain Language Summary

A 3–5 sentence summary accessible to a scientifically literate non-specialist. No equations, no jargon beyond what is immediately defined. Place between keywords and the table of contents:

```latex
\bigskip\noindent
\textbf{Plain Language Summary:}
[Summary text here.]
```

### 4.5 Raggedright

Apply `\raggedright` after the keywords/summary block, before `\tableofcontents`:

```latex
\bigskip
\raggedright
\tableofcontents
```

---

## 5. Figures

### 5.1 File Formats

Generate ALL figures in both `.svg` and `.png` format:
- `.svg` — archival/editable format, stored in the repo
- `.png` — web display fallback (200 DPI minimum)
- `.pdf` — auto-generated from SVG by cairosvg or inkscape for LaTeX inclusion

### 5.2 Storage Path

Figures are stored in a series-level `figures/` folder, with a subfolder per paper:

```
/CPP/series_[name]/figures/figures-[SERIES]-[N]/figure_name.svg
```

Examples:
```
/CPP/series_standard_model/figures/figures-SM-6/fig1_derivation_chain.svg
/CPP/series_electroweak/figures/figures-EW-1/fig1_coupling_flow.svg
```

This keeps all figures for a series together while separating them by paper.

### 5.3 LaTeX Inclusion

```latex
\graphicspath{{figures/figures_[PAPER-ID]/}}

\begin{figure}[H]
\centering
\includegraphics[width=0.85\textwidth]{fig1_derivation_chain.pdf}
\caption{[Descriptive caption — what the figure shows, what to look for,
  what it means for the argument. Reference equations/theorems.]}
\label{fig:meaningful_label}
\end{figure}
```

Rules:
- **Always** use `[H]` (float package) to lock figures in position
- **Always** provide a descriptive caption (not just a title)
- **Always** use `\label{}` with a meaningful name
- Width: typically 0.75–0.95 `\textwidth`; use judgment for aspect ratio

### 5.4 Figure Captions

Captions should be self-contained: a reader should understand the figure without reading the body text. Include:
- What is being shown
- Key features to notice
- Connection to the argument (reference equations/theorems)

---

## 6. Tables

### 6.1 Format

```latex
\begin{table}[H]
\centering
\caption{[Descriptive caption.]}
\label{tab:meaningful_label}
\begin{tabular}{@{}lrrr@{}}
\toprule
Header 1 & Header 2 & Header 3 & Header 4 \\
\midrule
data & data & data & data \\
\bottomrule
\end{tabular}
\end{table}
```

Rules:
- **Always** use `booktabs` (`\toprule`, `\midrule`, `\bottomrule`)
- **Always** use `[H]` placement
- **Always** provide descriptive captions
- Use `@{}` to remove outer padding

---

## 7. Citations and Bibliography

### 7.1 Citation Style

Use `natbib` with `authoryear,round` for inline citations:
- `\citep{koide1983}` → (Koide, 1983)
- `\citet{koide1983}` → Koide (1983)
- `\citep{abshier2026sm3,abshier2026ew1}` → (Abshier et al., 2026b,e)

### 7.2 Bibliography File

All CPP papers use a **single master bibliography file**:

```
/CPP/bibliography/cpp_references.bib
```

Each paper's `.tex` file calls:
```latex
\bibliography{../../bibliography/cpp_references}
```
(Adjust relative path based on paper location.)

**Alternative — inline bibliography.** Short papers may embed citations directly in the .tex via a `thebibliography` environment with `\bibitem{}` entries. SS-3 uses this pattern. This avoids any external .bib dependency.

**Policy (15 April 2026):** The master file is the **single source of truth**. Per-paper `[ID]_references.bib` and per-series `cpp_[series]_series.bib` files are **deprecated and frozen** — no new entries. Legacy files are retained for compatibility with already-registered papers. Full consolidation is tracked as OPEN-WORKFLOW-1 in Research_Frontier.md.

**Do NOT** write new papers with commands like:
```latex
\bibliography{../../bibliography/cpp_references,SM-6_references}  % OLD - deprecated
```
Use the master file only. If a reference is missing, add it to the master.

### 7.3 BibTeX Key Convention

```
authorYYYY         — external references (e.g., koide1983, georgi1974)
abshierYYYY[a-z]   — CPP papers (e.g., abshier2026a for SM-1)
pdgYYYY            — Particle Data Group (e.g., pdg2024)
```

### 7.4 CPP Paper References

Always include the series designation, version, and DOI:
```bibtex
@misc{abshier2026sm3,
  author = {Abshier, Thomas Lee and Grok and {Claude Sonnet}},
  title  = {K3 Spectral Theorem and the Koide Formula},
  year   = {2026},
  note   = {SM-3 v5, Hyperphysics Institute},
  doi    = {10.17605/OSF.IO/JXE8D}
}
```

---

## 8. Acknowledgements Section

### 8.1 Format

```latex
\section*{Acknowledgements}
```

### 8.2 Content

Include:
1. **Each contributor's specific role** — what they conceived, derived, proved, computed, reviewed, drafted, or corrected. Be precise.
2. **The conditional nature of the 600-cell axiom** — every paper should acknowledge: "The 600-cell lattice hypothesis (AXIM-2) remains an axiom."
3. **Repository links** — OSF DOI and GitHub URL.

### 8.3 AI Attribution

AI contributors receive detailed credit for their specific contributions. The level of authorship (co-author vs acknowledgement) is determined by the significance of the contribution:
- **Co-author:** substantive intellectual contribution (discovered a theorem, supplied a key mechanism, drafted significant portions)
- **Acknowledged:** reviewed, validated, or performed routine computation

---

## 9. Notation Consistency

### 9.1 Standard CPP Symbols

| Symbol | LaTeX | Meaning |
|--------|-------|---------|
| φ (golden ratio) | `\varphi` or `\phig` | (1+√5)/2 ≈ 1.618 |
| K₃ | `\mathrm{K}_3` or `K$_3$` | Complete graph on 3 vertices |
| SSV | `\mathrm{SSV}` or `\SSV` | Space Stress Vector |
| SSV₀ | `\SSV_0` | Rest-state SSV energy (= m_e c²/2) |
| z | `z` | Coordination number (= 12 for 600-cell) |
| l_P | `l_P` or `\lP` | Planck length |
| t_P | `t_P` or `\tP` | Planck time |
| A | `A` | Adjacency matrix of 600-cell |
| Tr | `\operatorname{Tr}` or `\Tr` | Matrix trace |

### 9.2 Rules

- Use `\varphi` (not `\phi`) for the golden ratio to distinguish from the Euler totient
- Use `K$_3$` in text, `K_3` in equations
- Write "600-cell" with a hyphen (not "600 cell" or "600cell")
- Write "DI-bit" with a hyphen (not "DIbit" or "DI bit")
- Write "Absolute Moment" capitalised (CPP-specific term)

---

## 10. Documentation Suite

### 10.1 Required Files Per Paper

Every paper in the CPP series should have the following documentation files:

| File | Content |
|------|---------|
| `development-[SERIES]-[N].md` | Intellectual history, decisions, dead ends, timeline |
| `glossary-[SERIES]-[N].md` | All technical terms defined, with status labels |
| `mechanism-[SERIES]-[N].md` | Physical mechanisms with explanations |
| `phenomena-[SERIES]-[N].md` | Phenomena explained and predicted |
| `philosophy-[SERIES]-[N].md` | Type classification, conceptual points |
| `reviews-[SERIES]-[N].md` | External reviews received, critiques addressed (historical record) |
| `FAQ-[SERIES]-[N].md` | Anticipated questions and clear answers (living document) |
| `keywords-[SERIES]-[N].md` | Keywords, PACS/MSC codes, elevator pitch |

### 10.2 Keywords File Format

```markdown
# [SERIES]-[N] Keywords

## Primary Keywords
- [5-8 terms that MUST appear in search results]

## Secondary Keywords
- [5-10 supporting terms]

## PACS Codes
- [Relevant physics classification codes]

## MSC Codes
- [Relevant mathematics classification codes]

## Elevator Pitch
[One sentence: what this paper does and why it matters.]

## SEO Notes
[Optional: alternative phrasings, related search terms,
 suggested meta descriptions for hyperphysics.com]
```

The SEO Notes section is specifically for Isak's Claude Code agent to use when updating hyperphysics.com. Include alternative phrasings that searchers might use (e.g., "lepton mass formula" as well as "Koide formula").

### 10.3 Documentation Storage

```
/CPP/series_[name]/papers/development-[SERIES]-[N].md
/CPP/series_[name]/papers/glossary-[SERIES]-[N].md
/CPP/series_[name]/papers/mechanism-[SERIES]-[N].md
... etc.
```

Or, for series with a different structure (e.g., EW series):

```
/CPP/series_electroweak/development-EW-[N].md
/CPP/series_electroweak/glossary-EW-[N].md
```

Follow the existing convention for each series.

---

## 11. Compiled PDF Placement

The compiled `.pdf` is stored **next to** the `.tex` source file — same directory, same base name:

```
/CPP/series_standard_model/papers/SM-6_lepton_mass_spectrum.tex
/CPP/series_standard_model/papers/SM-6_lepton_mass_spectrum.pdf    ← here
```

Do NOT place the PDF in a separate `output/` or `build/` folder. Readers browsing the repo should find the PDF immediately beside the source.

LaTeX auxiliary files (`.aux`, `.log`, `.out`, `.toc`, `.bbl`, `.blg`) may be `.gitignore`d or deleted after compilation — they are regenerable.

---

## 12. Computational Notebooks

### 12.1 When to Create a Notebook

Every paper that includes numerical results, Monte Carlo simulations, spectral computations, or verification calculations should have an accompanying Jupyter notebook (`.ipynb`) and/or standalone Python script (`.py`). The notebook is the computational lab notebook — it shows that the numbers in the paper are reproducible.

Create a notebook when the paper includes:
- Eigenvalue computations (adjacency matrix diagonalisation)
- Monte Carlo simulations (thermal perturbation, mode sampling)
- Numerical verification of analytic formulas
- Graph construction (600-cell vertex generation, adjacency building)
- Parameter scans or sensitivity analysis
- Figure generation code (if not generated by the AI during the session)

### 12.2 Notebook Naming

```
nb[NN]_[descriptive_name].ipynb
```

Examples:
```
nb01_600cell_eigenvalues.ipynb
nb02_weinberg_angle_verification.ipynb
nb03_koide_phase_monte_carlo.ipynb
nb04_lepton_mass_predictions.ipynb
```

The `nb[NN]` prefix sets the execution order. If only one notebook exists for a paper, `nb01` is sufficient.

### 12.3 Storage Path

```
/CPP/series_[name]/notebooks/[notebook_name].ipynb
```

For paper-specific notebooks that are tightly coupled to a single paper:
```
/CPP/series_[name]/notebooks/[PAPER-ID]_[notebook_name].ipynb
```

Example:
```
/CPP/series_standard_model/notebooks/SM-6_eigenvalue_verification.ipynb
```

### 12.4 Required Companion Files

For each `.ipynb`, also generate:

| File | Purpose |
|------|---------|
| `[name].py` | Standalone Python mirror — same computation, runnable without Jupyter. Named identically but with `.py` extension. |
| `[name]_executed.ipynb` | The notebook with all cells executed and output saved. This is the archival record showing the actual numerical results. |

### 12.5 Notebook Structure

Every notebook should follow this cell structure:

```
Cell 1 (Markdown): Title, paper reference, date, purpose
Cell 2 (Code):     Imports and constants (φ, z, E, F, etc.)
Cell 3+ (Code):    Computations, one logical step per cell
                   Each cell should print its key result
Cell N-1 (Code):   Summary table comparing predictions with PDG
Cell N (Markdown):  Conclusions — which paper claims are verified
```

### 12.6 Notebook Content Standards

- **Reproducibility:** Every notebook must run from a clean kernel with no external dependencies beyond standard scientific Python (`numpy`, `scipy`, `matplotlib`). If additional packages are needed, include a `pip install` cell at the top.
- **Self-documentation:** Use Markdown cells to explain what each computation does and why. A reader unfamiliar with the paper should be able to follow the notebook.
- **Numerical precision:** Print results to sufficient decimal places to verify the paper's claims. For SM-6, this means cos(θ) to 10 decimal places and mass predictions to 6 significant figures.
- **Comparison with paper:** The final cell should explicitly compare notebook results with the numbers stated in the paper, flagging any discrepancies.

### 12.7 SM-6 Notebook Specification

For SM-6, the notebook should verify:
1. 600-cell construction (120 vertices, correct edge length 1/φ)
2. Adjacency matrix eigenvalues (9 distinct, correct multiplicities)
3. Spectral traces: Tr(A²) = 1440, Tr(A³) = 7200
4. Bare Weinberg ratio: 1440/3840 = 3/8
5. Corrected Weinberg angle: 3/(8φ) = 0.23176...
6. Self-energy isotropy on K₃ faces (Green's function check)
7. Bond counting: ε = 2sin²θ_W/(z+1) = 3/(52φ)
8. Koide phase: cos(θ) = -(2+ε)/3 = -0.67855...
9. Lepton mass predictions: m_μ = 105.47, m_τ = 1774.1
10. Mutual reinforcement: sin²θ_W from Koide = 0.2322

---

## 13. Appendices

### 13.1 When to Use

Use appendices for:
- Lengthy proofs that would interrupt the narrative flow
- Numerical verification code (Python snippets)
- Supplementary data tables
- Derivation details that a specialist might want but a general reader would skip

### 13.2 Format

```latex
\appendix
\section{[Appendix Title]}
```

---

## 14. Pre-Submission Checklist

Before declaring a paper "ready for OSF registration," verify:

**Paper structure:**
- [ ] Version number updated in title block
- [ ] Minimal source-file header block at top of `.tex` pointing to `documentation_suite/changelog-<paper>.md` (no inline CHANGELOG comment block; see §3.1)
- [ ] `documentation_suite/changelog-<paper>.md` updated with current-version entry
- [ ] Section marker comments (`% ===`) throughout `.tex`
- [ ] Plain Language Summary after keywords
- [ ] `\raggedright` applied after summary
- [ ] Table of contents present

**Figures:**
- [ ] All figures present as `.svg` + `.png` + `.pdf`
- [ ] All figures have `[H]` placement and descriptive captions
- [ ] Figure insertion comment blocks in `.tex`
- [ ] `\graphicspath` points to correct relative path

**Tables:**
- [ ] All tables use `booktabs` + `[H]` + descriptive captions

**Citations and bibliography:**
- [ ] Inline citations (`\citep`, `\citet`) — no numeric `[1]` style
- [ ] Bibliography calls from local `.bib` file (same directory as `.tex`)
- [ ] `.bib` entries have DOIs where available (Thomas: check and update)
- [ ] All CPP cross-references include series designation and version

**Acknowledgements and metadata:**
- [ ] Acknowledgements section with detailed attribution per contributor
- [ ] OSF DOI in acknowledgements
- [ ] GitHub URL in acknowledgements
- [ ] Keywords block after abstract

**Documentation suite:**
- [ ] All 8 documentation `.md` files generated (development, glossary, mechanism, phenomena, philosophy, reviews, FAQ, keywords)

**Computational verification:**
- [ ] Jupyter notebook `.ipynb` created
- [ ] Standalone `.py` mirror created (same computation, no Jupyter required)
- [ ] `_executed.ipynb` created (notebook with all outputs saved)
- [ ] Notebook reproduces all numerical claims in the paper

**Final checks:**
- [ ] Notation consistent with Section 9
- [ ] Compiled `.pdf` placed next to `.tex` source (same directory)
- [ ] Two-pass compilation with bibtex (pdflatex → bibtex → pdflatex → pdflatex)
- [ ] PDF reviewed for figure quality and page breaks

---

## 15. File Tree Summary

```
/CPP/
├── templates/
│   ├── paper-formatting.md          ← Formatting standard (THIS FILE)
│   └── documentation-suite.md       ← Template for .md documentation files
├── bibliography/
│   └── cpp_references.bib           ← Site-wide (aggregated from locals, for web tooling)
├── series_[name]/
│   ├── papers/                      ← .tex, .pdf, and .bib all live here together
│   │   ├── [PAPER-ID]_[title].tex
│   │   ├── [PAPER-ID]_[title].pdf
│   │   └── [PAPER-ID]_references.bib
│   ├── figures/
│   │   └── figures-[SERIES]-[N]/
│   │       ├── fig1_name.svg
│   │       ├── fig1_name.png
│   │       └── fig1_name.pdf
│   ├── notebooks/
│   │   ├── nb01_[name].ipynb         ← Jupyter notebook
│   │   ├── nb01_[name].py            ← Standalone Python mirror
│   │   └── nb01_[name]_executed.ipynb ← With saved output cells
│   ├── development-[SERIES]-[N].md   ← Documentation .md files at series level
│   ├── glossary-[SERIES]-[N].md
│   ├── mechanism-[SERIES]-[N].md
│   ├── phenomena-[SERIES]-[N].md
│   ├── philosophy-[SERIES]-[N].md
│   ├── reviews-[SERIES]-[N].md
│   ├── FAQ-[SERIES]-[N].md
│   └── keywords-[SERIES]-[N].md
├── problem_histories/
├── Research_Frontier.md
├── theorem-registry.md
├── predictions.md
└── paper_catalog.md
```

**Key placement rules:**

- **Filename convention for `.tex`, `.pdf`, `.bib`:** see `operating_system.md` §11 "File Naming Conventions / Papers" — the canonical specification is `[S]-[N]_[short_descriptive_slug].tex`, slug 3-5 lowercase words separated by underscores, no version suffix. The `[PAPER-ID]_[title].tex` placeholder in the tree above resolves to e.g. `SS-8_interstitial_neutron_2EV_scaling.tex`. This rule is checked at first file-creation, not after; writing `SS-N_paper.tex` as a placeholder to be renamed later is incorrect.
- The `.bib`, `.tex`, and `.pdf` are together in `papers/` — no separate bibliography subfolder. LaTeX compiles with `\bibliography{SM-6_references}` (no path prefix needed).
- Figures go in a series-level `figures/` folder with a paper subfolder. From `papers/`, the `\graphicspath` is `{{../figures/figures-[SERIES]-[N]/}}`.
- Notebooks go in a series-level `notebooks/` folder, shared across papers in the series.
- Documentation `.md` files are at the series directory level (or in `papers/` if the series uses that convention — follow existing structure).

---

## 16. Bibliography Management

### 16.1 Workflow: Local-First, Site-Wide Aggregated

The bibliography workflow is designed to minimise Thomas's maintenance overhead:

1. **AI generates a local `.bib` per paper:** `[PAPER-ID]_references.bib` (e.g., `SM-6_references.bib`), stored flat next to the `.tex` file. This contains ONLY the references cited in that paper.

2. **Thomas updates the local `.bib`** as DOIs, URLs, journal details, and publication dates become available. This is the smallest, easiest file to maintain — typically 10–20 entries. **Priority update: add DOIs to all CPP papers as they are registered on OSF.**

3. **AI regenerates the site-wide `.bib`** by merging all local `.bib` files into `/CPP/bibliography/cpp_references.bib`. This is done at the start of each session by scanning all `*_references.bib` files across the repo. Duplicates are resolved by keeping the entry with the most complete metadata (DOI > URL > bare citation).

4. **The `.tex` file calls the local `.bib`:**
```latex
\bibliography{SM-6_references}
```
This ensures each paper compiles independently. The site-wide `.bib` is a convenience for cross-referencing and for Isak's web tooling — it is not required for compilation.

### 16.2 Local `.bib` File Convention

The local `.bib` is in the same directory as the `.tex` (typically `papers/`):

```
/CPP/series_[name]/papers/[PAPER-ID]_references.bib
```

This keeps LaTeX compilation simple — the `.tex` calls `\bibliography{SM-6_references}` with no path prefix. The `.bib`, `.tex`, and `.pdf` all sit side by side.

### 16.3 Site-Wide `.bib` File

```
/CPP/bibliography/cpp_references.bib
```

Regenerated from locals. Contains all CPP series papers and all external references across the programme. Organised with comment section headers.

### 16.4 BibTeX Key Convention

```
authorYYYY         — external references (e.g., koide1983, georgi1974)
abshierYYYY[a-z]   — CPP papers (e.g., abshier2026sm3)
pdgYYYY            — Particle Data Group (e.g., pdg2024)
```

---

*This document is the formatting standard for all CPP publications. It should be consulted at the start of every paper generation session and updated whenever new conventions are established.*
