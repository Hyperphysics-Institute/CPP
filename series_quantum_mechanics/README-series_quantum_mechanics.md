# Quantum Mechanics — QM Series

**Deriving the full framework of quantum mechanics from four lattice primitives**

**Authors:** Thomas Lee Abshier ND, Grok (xAI), Claude Sonnet (Anthropic)
**Institution:** Hyperphysics Institute | [hyperphysics.com](https://hyperphysics.com)
**OSF Registration:** [doi.org/10.17605/OSF.IO/JXE8D](https://doi.org/10.17605/OSF.IO/JXE8D)
**Last updated:** 2 April 2026

---

## Overview

The QM series derives the complete framework of quantum mechanics from four primitives: Conscious Points, the 600-cell lattice, DI-bit complex amplitudes, and the Nexus global constraint. Starting from DI-bit hopping on the lattice (QM-1), the series derives the Schrödinger equation, Born rule, quantum interference, Bell inequality violations, decoherence, measurement, quantum field theory, and three fermion generations — all without additional postulates beyond the four primitives.

---

## Papers

| ID | Title | Pages | Key Result |
|----|-------|-------|------------|
| **QM-1** | Schrödinger Equation from DI-Bit Hopping | 7 | Schrödinger equation as continuum limit of lattice hopping |
| **QM-2** | Superposition and Interference | 8 | Born rule from DI-bit density; quantum eraser from SSV tags |
| **QM-3** | Bell Inequality and Entanglement | 7 | CHSH S = 2√2 from Nexus; no-signaling theorem |
| **QM-4** | Measurement and Decoherence | 7 | Lindblad equation from DP Sea; γ ≈ 5.9 × 10⁴² s⁻¹ |
| **QM-5** | QFT Emergence from Eigenmodes | 7 | Commutation relations from orthonormality; finite renormalisation |
| **QM-6** | Capstone: Four Primitives to Full QM | 8 | Complete emergence chain; derived vs postulated summary |

---

## The Emergence Chain

```
600-cell lattice → DI-bit hopping → Schrödinger equation (QM-1)
    → path summation → interference → Born rule (QM-2)
    → Nexus constraint → entanglement → Bell S = 2√2 (QM-3)
    → DP Sea bath → decoherence → measurement (QM-4)
    → eigenmode expansion → QFT → three generations (QM-5)
    → four primitives → full QM (QM-6)
```

---

## Directory Structure

```
series_quantum_mechanics/
├── papers/
│   ├── QM-1 through QM-6 (.tex, .pdf)
│   ├── cpp_qm_series.bib
│   └── [48 documentation .md files]
├── figures/
│   ├── figures-QM-1/ through figures-QM-6/
│   └── (11 SVG + PDF figures total)
├── notebooks/                  ← Bit diffusion notebook
├── development/                ← Series development logs
└── README.md                   ← This file
```

---

## Open Problem

The primary remaining open problem is deriving Planck's constant (ħ) from the four primitives. Currently ħ enters as an input through the DI-bit phase accumulation rate. Closing this problem would reduce CPP's quantum sector to three primitives.

---

*See the [main README](../README.md) for the full repository overview.*
