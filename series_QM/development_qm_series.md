# CPP QM Series — Development Log
**GitHub path:** `CPP/series_QM/development_qm_series.md`
**Session date:** 22–23 March 2026
**Participants:** Thomas Lee Abshier (theory), Claude Sonnet 4.5 (drafting, correction, figures), Grok (independent parallel rewrites)

---

## Overview

This document records the complete development history of the CPP Quantum Mechanics series (Papers CPP-2040a through CPP-2040f), from initial diagnosis of the v1 papers through the final v3.1 merge. It covers every major decision, every error found and corrected, and the rationale for each structural choice.

---

## Stage 1 — Diagnosis of the v1 QM Papers

The session began with six pre-existing v1 papers (CPP-2040a through 2040f) submitted on Pastebin. All six were read and diagnosed before any rewriting began.

### CPP-2040a (Schrödinger) — CRITICAL ERROR FOUND

**Error:** The v1 paper derived the Schrödinger equation via the route:
```
DI-bit master equation → Fokker-Planck → Schrödinger
```
This is **mathematically invalid**. The Fokker-Planck equation is:
```
∂ρ/∂t = D∇²ρ   (real-valued, classical diffusion)
```
The Schrödinger equation is:
```
iℏ∂ψ/∂t = Hψ   (complex-valued, quantum evolution)
```
No continuum limit of a real diffusion equation produces the imaginary unit `i`. The paper had skipped the essential physical ingredient: **phase accumulation per hop**.

**Correct derivation worked out analytically and numerically:**
DI bits carry both density ρ AND geometric phase φ. The complex amplitude ψ = √ρ·e^{iφ} evolves under complex hopping on the 600-cell lattice. The hopping amplitude is:
```
T = ℏ²/(4mΔs²)
```
The key factor-of-4 (not 2) was derived: the 600-cell has z=12 neighbours in d=3 dimensions. The graph Laplacian gives:
```
Σ_{j~i}(ψ_j - ψ_i) = 2Δs²∇²ψ
```
The factor z/(2d) = 12/6 = 2 is absorbed into the denominator of T. Using T = ℏ²/(2mΔs²) — as Grok's paper later did — gives −ℏ²∇²ψ/m instead of −ℏ²∇²ψ/(2m), wrong by a factor of 2. This correction propagated through all six papers.

**Physical insight:** The imaginary unit arises from phase accumulation, not from any ad hoc prescription. Classical diffusion transports density without phase; quantum hopping transports complex amplitude with phase. This single distinction produces Schrödinger, not Fokker-Planck.

### CPP-2040c (Bell/Entanglement) — CRITICAL ERROR FOUND

**Error:** The v1 paper described the singlet as "two particles sharing a fixed pool of DI-bit phases set at emission." This is a **local hidden-variable (LHV) model**. Bell's theorem applies and gives |CHSH| ≤ 2. The paper was claiming to derive |CHSH| = 2√2 while using an argument that only allows ≤ 2.

**Correct derivation:** Two ingredients are needed together:
1. Non-separability: the singlet |Ψ⁻⟩ cannot factor into |φ_A⟩⊗|φ_B⟩ (proved algebraically — 4-coefficient contradiction).
2. Born rule: P = |projection|² gives E = −cosθ. Classical probability rules give E = 1−2θ/π, which only reaches |S| = 2 at optimal settings.

The Nexus maintains the non-separable joint state globally, which is why it is not an LHV: it enforces a global non-factorising constraint, not a local variable carried by the particles.

### CPP-2040d (Measurement) — ERRORS FOUND

**Errors:**
- Lindblad equation asserted without derivation. Fixed by explicit Born-Markov elimination of the DP Sea bath.
- Pointer basis claimed to be "apparatus-dependent" (standard). In CPP it is stronger: the pointer basis is the SSV eigenstates, fixed by the lattice geometry, independent of apparatus. This is a genuine CPP-specific prediction distinguishable from standard einselection.

### CPP-2040e (QFT) — FOUR ERRORS FOUND

1. **Field operators derived from real density ρ_i** (wrong — must use complex amplitude ψ_i = √ρ_i·e^{iφ_i}).
2. **Commutation relations asserted from "120°/240° phase geometry"** — non-derivation. Fixed: two-line proof from eigenmode orthonormality.
3. **Fermion/boson distinction not derived.** Fixed: CP exclusion principle (one per Grid Point, infinite SSV repulsion for same-sign CPs) → fermionic anticommutators; neutral DI bits → bosonic commutators.
4. **Renormalization claimed as "solved."** Corrected: the Planck cutoff makes loops FINITE but LARGE (~E_P²). The hierarchy problem is converted from infinite to finite fine-tuning — a logical improvement, not a solution.

Also removed: the SM particle mass formula (three free parameters, curve-fitting not derivation). The six-eigenvalue / three-generation mapping was retained as an explicitly flagged open problem.

### CPP-2040b (Superposition) — MISSING PAPER

CPP-2040b did not exist as a separate paper in the v1 series. It was written from scratch, covering:
- Born rule non-circularity (A_0 geometrically defined, not from probability)
- SSV as which-path tag (CPP-specific: SSV gradient at slits encodes which-path information without a separate detector)
- Quantum eraser as SSV cancellation
- Connection between path-sum form and Schrödinger equation (both are equivalent descriptions of DI-bit hopping)

### CPP-2040f (Capstone) — REBUILT

The v1 capstone was rebuilt to accurately summarise the corrected v2 results, with an explicit "what CPP has derived vs. postulated" comparison table and five formally listed open problems.

---

## Stage 2 — The T Factor Correction (All Papers)

The hopping amplitude correction — T = ℏ²/(4mΔs²) not ℏ²/(2mΔs²) — was the single most important mathematical correction. It arose from properly working out the graph Laplacian of the 600-cell:

| Quantity | Value | Source |
|---|---|---|
| Coordination number z | 12 | 600-cell geometry |
| Spatial dimension d | 3 | 3D space |
| z/(2d) factor | 12/6 = 2 | Graph Laplacian |
| Correct T | ℏ²/(4mΔs²) | Absorbs factor 2 |
| Incorrect T (Grok) | ℏ²/(2mΔs²) | Off by factor 2 |

This was verified numerically: with T = ℏ²/(4mΔs²) and the graph Laplacian giving 2∇²ψ, the kinetic term −T·(Aψ)/Δs² = −[ℏ²/(4mΔs²)]·2Δs²∇²ψ = −ℏ²∇²ψ/(2m) ✓

---

## Stage 3 — Grok's Independent Rewrites

Grok (independent AI) wrote parallel versions of all six papers, submitted on Pastebin 22 March 2026. These were read and compared:

**URLs:**
- 2040a: https://pastebin.com/nMxhnfXS
- 2040b: https://pastebin.com/YBjpPPbF
- 2040c: https://pastebin.com/QdvzX3ci
- 2040d: https://pastebin.com/jhf2LMnG
- 2040e: https://pastebin.com/XiXX9209
- 2040f: https://pastebin.com/6J8FprvK

**What Grok did better:**
- Concise abstract structure (result in first sentence)
- "Only two processes exist" framing for introductions
- Clean 2-4 line proofs
- Excellent quantum pressure physical interpretation sentence in 2040a
- QFT commutator proof identical to ours (confirming correctness)

**What Grok got wrong:**
- T = ℏ²/(2mΔs²) in every paper (wrong by factor 2, as diagnosed above)
- Grok's justification: "factor 2 arises from 4+4 forward/backward neighbours" — this double-counts since the factor is already in the graph Laplacian

**Decision:** v3.1 takes Grok's lean structure as the skeleton and adds our content where needed.

---

## Stage 4 — v3.1 Merge (Claude Rewrite)

**Files produced:**
| Paper | File | Key content |
|---|---|---|
| CPP-2040a | cpp2040a_v31.tex | Schrödinger from hopping, T=ℏ²/(4mΔs²) remark, Appendix on graph Laplacian |
| CPP-2040b | cpp2040b_super_v31.tex | Superposition, SSV which-path, quantum eraser |
| CPP-2040c | cpp2040c_v31.tex | Bell, non-separability proof, CHSH=2√2, no-signaling |
| CPP-2040d | cpp2040d_v31.tex | Lindblad from DP Sea, pointer=SSV eigenstates |
| CPP-2040e | cpp2040e_v31.tex | QFT from eigenmodes, finite renorm, hierarchy problem |
| CPP-2040f | cpp2040f_v31.tex | Capstone, comparison table, 5 open problems |
| cpp_qm_series.bib | — | 40-entry bibliography |

**Preamble (all papers):**
```latex
\usepackage{svg}
\svgsetup{inkscapelatex=false,inkscapeformat=pdf,inkscapepath=svgdir}
\usepackage[numbers,sort&compress]{natbib}
\usepackage{graphicx}
\usepackage{caption}
\usepackage{float}
```

---

## Stage 5 — Compile Errors Fixed

### 2040b (Superposition) — \EP undefined
**Error:** `\EP` used on line 250 in the predictions section but not defined in preamble. Overleaf compiled with XeLaTeX (line 1 of error log: "XeTeX, Version 3.141592653") which halts immediately on undefined macros.
**Fix:** Added `\newcommand{\EP}{E_P}` to preamble. The other five papers all defined `\EP` because they use it more extensively; this one was trimmed too aggressively.

### 2040d (Measurement) — \bra undefined
**Error:** Line 246 used `\bra{\Psi_{\rm tot}}` but preamble only defined `\ket`, not `\bra`.
**Fix:** Added `\newcommand{\bra}[1]{\langle#1|}` immediately below the `\ket` definition.

---

## Stage 6 — SVG Figures

Eleven figures generated for the QM series, then revised through multiple rounds:

| Figure file | Paper | Content | Revisions |
|---|---|---|---|
| qm2040a_fig1_gaussian_packet.svg | 2040a | DI-bit Gaussian wave packet on lattice | 1 |
| qm2040a_fig2_discrete_continuum.svg | 2040a | Discrete→continuum transition | 1 |
| qm2040b_fig1_multipath_geodesics.svg | 2040b | Double-slit path families | 4 |
| qm2040b_fig2_amplitude_summation.svg | 2040b | Phasor diagram + interference pattern | 5 |
| qm2040b_fig3_quantum_eraser.svg | 2040b | Three-panel eraser sequence | 1 |
| qm2040c_fig1_nexus_singlet.svg | 2040c | EPR pair with Nexus | 1 |
| qm2040c_fig2_chsh_correlations.svg | 2040c | Classical vs quantum correlation curves | 2 |
| qm2040d_fig1_decoherence.svg | 2040d | Density matrix evolution + decay curve | 2 |
| qm2040d_fig2_pointer_basis.svg | 2040d | Bloch sphere → pointer states | 1 |
| qm2040e_fig1_600cell_modes.svg | 2040e | 600-cell + eigenvalue table | 3 |
| qm2040f_fig1_emergence_hierarchy.svg | 2040f | Full emergence chain from primitives | 1 |

**Figure revision history (issues fixed):**

**2040b Fig 1 (multipath geodesics):**
- v1: Slit 1/2 labels overlapped path lines
- v2: Labels moved right of barrier, but Slit 2 label still overlapped outgoing lines
- v3: Labels moved left of barrier ("Slit 1 ←"), but Slit 2 gap was missing from barrier (bottom wall started at y=202 instead of y=230)
- v4 (final): Three-section barrier (top y=30–140, middle y=168–202, bottom y=230–340) with both gaps open; labels on left clear of all paths

**2040b Fig 2 (phasor diagram):**
- v1: Resultant label "ψ = Σ Aₖe^(iφₖ)" overlapped A₂ vector
- v2: Split into two lines, placed right of arrowhead — still overlapped A₂
- v3: A₃ label moved to left, but too far left (x=110)
- v4: A₃ label moved right to x=126 (halfway), but still touched resultant
- v5 (final): A₃ label at x=126, text-anchor="end", clear of all vectors

**2040c Fig 2 (CHSH correlations):**
- v1: 45° and 135° angle labels dropped below x-axis into legend area
- v2 (final): Extended viewBox height to 400, x-axis labels at y=340, angle labels at y=355, legend at y=380

**2040d Fig 1 (decoherence):**
- v1: γ = sea_str² E_P/ℏ text baseline at y=307, box bottom edge at y=306 — 1px overflow
- v2 (final): Box height 48→60, text moved up 2px, 10px clear padding below

**2040e Fig 1 (600-cell modes):**
- v1: Six eigenmode circles (r=11) barely contained their labels
- v2: Moved to dedicated left panel with hexagonal arrangement, but circles still touching labels
- v3 (final): Circles enlarged to r=16 with comfortable text padding; right panel has separate legend dots (r=7)

**Final figure set:** `CPP/series_QM/*/figures/qm2040X_figY_name.svg` (canonical names, no version suffixes)

---

## Stage 7 — Synthesis Paper for Submission

A compressed synthesis paper was written targeting *Foundations of Physics*:
- File: `cpp_qm_synthesis_submission.tex`
- Content: Five theorems, each with proof, plus open problems, predictions table, and Appendix on the 600-cell graph Laplacian
- Self-contained with its own bibliography (18 entries)
- Does not assume familiarity with the full series

---

## Key Decisions Log

| Decision | Rationale |
|---|---|
| T = ℏ²/(4mΔs²) not ℏ²/(2mΔs²) | z/(2d) = 2 factor from 12-neighbour 3D graph Laplacian |
| No Fokker-Planck route | Real diffusion cannot produce imaginary unit; fundamentally wrong route |
| LHV error in Bell paper corrected | Previous argument (shared bit pool at emission) was an LHV model; Bell's theorem rules it out |
| SM mass formula removed from QFT paper | Three free parameters, curve-fitting; not a derivation |
| Hierarchy problem labelled "finite, not solved" | Planck cutoff makes loop finite but large; still requires fine-tuning |
| Born rule borrowed from companion C3 | Not derivable from the four primitives alone; honestly disclosed |
| Pointer basis = SSV eigenstates (lattice-fixed) | Stronger than standard einselection; CPP-specific prediction |
| Six eigenvalues / three generations = open problem | Structural coincidence; no mass ratio derivation yet |
| Bibliography: inline thebibliography | Easier for Overleaf single-file editing; switch to \bibliography{cpp_qm_series} for multi-paper management |
| \usepackage{svg} + \svgsetup | Required for Overleaf XeLaTeX SVG rendering with inkscape backend |

---

## File Locations

**Overleaf:** Each paper in its own project, figures in `figures/` subfolder.

**GitHub:**
```
CPP/series_QM/
├── cpp_qm_series.bib
├── development_qm_series.md   (this file)
├── cpp2040a_schrodinger/
│   ├── cpp2040a_v31.tex
│   └── figures/
│       ├── qm2040a_fig1_gaussian_packet.svg
│       └── qm2040a_fig2_discrete_continuum.svg
├── cpp2040b_superposition/
│   ├── cpp2040b_super_v31.tex
│   └── figures/
│       ├── qm2040b_fig1_multipath_geodesics.svg
│       ├── qm2040b_fig2_amplitude_summation.svg
│       └── qm2040b_fig3_quantum_eraser.svg
├── cpp2040c_bell_entanglement/
│   ├── cpp2040c_v31.tex
│   └── figures/
│       ├── qm2040c_fig1_nexus_singlet.svg
│       └── qm2040c_fig2_chsh_correlations.svg
├── cpp2040d_measurement/
│   ├── cpp2040d_v31.tex
│   └── figures/
│       ├── qm2040d_fig1_decoherence.svg
│       └── qm2040d_fig2_pointer_basis.svg
├── cpp2040e_qft/
│   ├── cpp2040e_v31.tex
│   └── figures/
│       └── qm2040e_fig1_600cell_modes.svg
└── cpp2040f_capstone/
    ├── cpp2040f_v31.tex
    └── figures/
        └── qm2040f_fig1_emergence_hierarchy.svg

CPP/synthesis/
└── cpp_qm_synthesis_submission.tex
```

---

## Session Timestamps (UTC)

- Session start: 2026-03-22 ~22:00 UTC
- v1 diagnosis complete: ~23:00
- v2 papers written: ~02:00 2026-03-23
- Grok papers received and compared: ~03:00
- v3.1 merge complete: ~04:30
- Bibliography written: ~04:45
- Figures generated (round 1): ~05:30
- Figure corrections (rounds 2–5): ~06:30–09:00
- Compile errors fixed: ~09:15
- Synthesis paper written: ~10:00
- Development log written: ~10:30

---

*End of development log.*
