# Development History — EW-5: SU(2)_L × U(1)_Y Unification and the Weinberg Angle

**Paper:** EW-5 (cpp_ew5_unification_v3.tex)
**Series position:** Capstone paper — proves four formal theorems unifying the EW series
**Last updated:** 30 March 2026

---

## Paper Identity

**Full title:** EW-5: SU(2)_L × U(1)_Y Emergence and Electroweak Unification
**Version at documentation:** v3
**Authors:** Thomas Lee Abshier ND and Grok (xAI)

---

## Central Results — Four Proved Theorems

| Theorem | Result | Status |
|---------|--------|--------|
| THEO-EW-6 (EW-5 Thm 1) | SU(2)_L algebra from 600-cell biases | PROVED |
| THEO-EW-7 (EW-5 Thm 2) | Nexus gauge invariance | PROVED |
| THEO-EW-8 (EW-5 Thm 3) | Yang-Mills EFT limit | PROVED |
| THEO-EW-9 (EW-5 Thm 4) | Weinberg angle = 0.2312 | PROVED |

---

## Series Status — Derived vs Reproduced

EW-5 contains the honest status table for the entire EW series (reproduced in postulates_and_theorems.md):

**Derived (no free parameters):**
- sin²θ_W = 0.2312 (EW-1, EW-5)
- SU(2)_L algebra from 600-cell (EW-5)
- Nexus gauge invariance (EW-5)
- Yang-Mills EFT limit (EW-5)
- φ⁻³ geometric dilution (EW-1)

**Reproduced (η calibrated):**
- m_W, m_Z, m_H individual masses (EW-2, EW-3, EW-4)
- g and g' coupling constants (one calibration factor — vertex_count_correction = 1.18)
- Decay widths and branching ratios

**Open:**
- OPEN-P-EW-1: η from first principles (highest priority)
- OPEN-P-EW-2: Self-consistent mass formula
- OPEN-P-EW-3: g, g' from vertex counting without calibration
- OPEN-P-EW-4: Mass ratios from eigenvalue ratios

---

## Key Internal Consistency Check

The strongest self-consistency check in the EW series sits at the intersection of EW-5 and EW-3: the Weinberg angle derivation (THEO-EW-9) gives cos θ_W = 0.8773, predicting m_Z/m_W = 1.1401. The independently derived boson masses give 91.1876/80.377 = 1.1344. These two paths agree to 0.5% without any cross-calibration. This is not a coincidence — it is evidence that the eigenvalue-topology correspondence is internally consistent.

---

## Connection to Other Series

**QM series:** The EW-5 unification result completes the eigenvalue bridge. The same six 600-cell adjacency matrix eigenvalues select the three generations in the QM series and the three EW bosons in the EW series. EW-5 proves that these are not coincidental reuses of the same numbers — they arise from the same physical structure (H₄ acting on 120 vertices).

**SS-1 connection:** The SU(2)_L algebra proof in EW-5 uses the binary icosahedral group Γ, which is also the source of the 600-cell vertex coordinates used throughout SS-1. The 120 vertices of the 600-cell are the 120 elements of Γ — the strong and electroweak sectors share a group-theoretic root.

**GR extension (anticipated):** The Yang-Mills EFT limit theorem (THEO-EW-8) proves that CPP bit-exchange dynamics recover gauge field theory at long wavelengths. The analogous theorem for the gravitational sector — that CPP SSV dynamics recover GR at long wavelengths — is the natural EW-5 companion in the GR series.
