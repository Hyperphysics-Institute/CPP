# Suppression Mechanisms in Conscious Point Physics (CPP)

All mass scales, coupling strengths, and anomaly contributions in CPP emerge from a small set of geometric constraints imposed by the 600-cell lattice. This directory documents every suppression factor used in the theory.

## Core Geometric Origins
- Fixed vertex count: N_lattice = 120 per 600-cell
- Golden ratio: φ = (1 + √5)/2 ≈ 1.618 (edge lengths, dihedral angles, projection deficits)
- Dimensional binding: d = 0 (bound orbital), 1 (linear extras), 3 (unbound neutrinos)
- Holographic bound: information/entropy scales with 120^{-d} or 120^{-dimensional volume terms}

## Summary Table

| Suppression              | Expression                  | Geometric Origin                              | Phenomena Affected                     | Typical Magnitude     |
|--------------------------|-----------------------------|-----------------------------------------------|----------------------------------------|-----------------------|
| Holographic entropy      | σ = 120^{-d}                | Vertex count bounds unbound modes             | Neutrino masses, quark linear extras   | 1 → 5.8×10^{-7}      |
| VEV volume dilution      | 1 / N_lattice⁴              | 4D volumetric entropy per cell                | Overall mass scale from Planck         | ~1 / (120)^4 ≈ 3×10^{-9} |
| Golden ratio layering    | ϕ^k (k=1,2,3,...)           | Icosahedral/tetrahedral growth sequences      | Generational hierarchies               | φ ≈1.618 per layer   |
| EM fine-structure        | α ≈ 1 / (360/φ² - 2/φ³)     | Golden angle frustration in 4D→3D projection  | QED couplings, g-2 loops               | ≈1/137.036           |
| Radiative loop (g-2)     | S = α / (2π)                | ZBW cycle (2 phases) × projection inefficiency| Muon/electron g-2 corrections          | ≈1.16×10^{-3}        |

## Usage Notes
- Every suppression is derived from lattice invariants—no free parameters beyond the single electron mass calibration (which sets k ≈ 0.0185).
- Cross-references: see Paper 2 Sections 2, 5, Appendices A–F; Paper 1 Section 10.
- All code that applies these factors lives in ../cpp-zbw-mixing-fractions/ and ../mass_calculations/.

Contributions, questions, and rigorous critiques welcome.
