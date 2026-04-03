# Electroweak Sector — EW Series

**Deriving the W, Z, and Higgs bosons from 600-cell lattice geometry**

**Authors:** Thomas Lee Abshier ND, Grok (xAI), Claude Sonnet (Anthropic)
**Institution:** Hyperphysics Institute | [hyperphysics.com](https://hyperphysics.com)
**OSF Registration:** [doi.org/10.17605/OSF.IO/JXE8D](https://doi.org/10.17605/OSF.IO/JXE8D)
**Last updated:** 2 April 2026

---

## Overview

The EW series derives the electroweak sector of the Standard Model from the geometry of the 600-cell lattice. Photons and weak bosons emerge as different organisational modes of the same Dipole Sea vacuum — edge modes (abelian, U(1)_Y) carry electromagnetism while face-circulation modes (non-abelian, SU(2)_L) carry the weak force. The Weinberg angle is derived from the edge-to-face mode ratio, and the SU(2) gauge algebra from the binary icosahedral group.

**Key result (superseded by SM-6):** The Weinberg angle sin²θ_W was originally derived in this series via Monte Carlo methods. SM-6 provides the cleaner analytical derivation: sin²θ_W = 3/(8φ) ≈ 0.2318 from spectral traces. The EW series retains its value for the boson structure models (W bracelet, Z ring, Higgs shell) and the Yang-Mills emergence theorem.

---

## Papers

| ID | Title | Pages | Key Result |
|----|-------|-------|------------|
| **EW-1** | Electroweak Introduction | 6 | Gauge emergence from 600-cell modes; SU(2) from binary icosahedral group |
| **EW-2** | The W Boson from CPP | 6 | W as open hDP bracelet; W⁰ prediction; V−A coupling at 75% |
| **EW-3** | The Z Boson from CPP | 5 | Z as closed icosahedral ring; Z/W mass ratio from loop density |
| **EW-4** | The Higgs Boson from CPP | 5 | Higgs as dodecahedral shell; J=0 from A₅ symmetry |
| **EW-5** | Electroweak Unification | 6 | Yang-Mills EFT as continuum limit; 6 open problems identified |

---

## Directory Structure

```
series_electroweak/
├── EW-1_electroweak_introduction.tex/.pdf
├── EW-2_w_boson_from_cpp.tex/.pdf
├── EW-3_z_boson_from_cpp.tex/.pdf
├── EW-4_higgs_boson_from_cpp.tex/.pdf
├── EW-5_electroweak_unification.tex/.pdf
├── cpp_ew_series.bib
├── figures/                          ← MC distribution plots (PNG)
├── notebooks/                        ← Weinberg angle Monte Carlo code
├── development/                      ← Session logs including SM-6 derivation session
├── [development/glossary/mechanism/phenomena/philosophy/reviews/FAQ/keywords]-EW-N.md
└── README.md                         ← This file
```

---

## Documentation

Each paper has 8 companion files: development, glossary, mechanism, phenomena, philosophy, reviews, FAQ, and keywords.

---

## Open Problems

The EW series identifies 6 open problems (OPEN-P-EW-1 through OPEN-P-EW-6) that must be closed before the full electroweak derivation is complete. The most significant is OPEN-P-EW-1: the η ∼ 10⁻¹⁷ factor that sets the overall boson mass scale is not yet derived from lattice geometry — it is currently the mass scale itself, not a geometric structure.

---

## Relationship to SM-6

SM-6 (April 2026) supersedes the EW series Weinberg angle derivation. The original EW approach used Monte Carlo mode sampling; SM-6 provides the exact analytical formula sin²θ_W = 3/(8φ) from spectral traces. The EW series remains valuable for:
- Boson structure models (W bracelet, Z icosahedral ring, Higgs dodecahedral shell)
- SU(2)_L derivation from binary icosahedral group (THEO-EW-3)
- Yang-Mills emergence as continuum limit (THEO-EW-8)
- The W⁰ prediction (novel, testable, not in SM)

---

*See the [main README](../README.md) for the full repository overview.*
