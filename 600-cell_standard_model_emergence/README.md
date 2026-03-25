# Conscious Point Physics — Standard Model Emergence in the 600-Cell Lattice

**Authors:** Thomas Lee Abshier ND, Claude (Anthropic), Grok (xAI)  
**Last updated:** 25 March 2026  
**Status:** Four papers ready to submit. Strong sector paper submission-ready.

---

## What This Repository Is

This is the **source of truth** for the CPP Standard Model emergence programme.
The `papers/` directory contains the authoritative `.tex` files.
Everything else — derivation notebooks, working notes, development folders —
supports those papers but is not the theory itself.

If you want to know what CPP claims and what is proved, read the papers in order.
If you want to understand how a result was derived, read the corresponding `p*-`
directory. If you find a file that contradicts a paper, the paper takes precedence.

---

## The Theory in One Paragraph

Conscious Point Physics derives the Standard Model gauge structure, charge
quantisation, mass hierarchies, and neutrino mixing from the geometry of the
600-cell polytope (120 vertices, golden-ratio edge lengths) and a single
interaction rule: Conscious Points (CPs) exchange DI-bits via Space Stress
Vector (SSV) gradients at each Absolute Moment. No 19 free parameters.
One calibration constant (sea\_strength ≈ 0.178, fixed to the 600-cell Voronoi
geometry). All hierarchies follow from lattice invariants.

---

## The Four K3 Results (Papers 1, 3, 4, 5)

The **same equilateral triangle** — the K3 base of the 600-cell tetrahedral
cage — encodes four distinct Standard Model quantities:

| Result | Value | Mathematical structure of K3 | Paper |
|--------|-------|-------------------------------|-------|
| Charge quantisation | δ = 1/3 | Combinatorial: 3 equal vertices, completeness | 1 |
| Koide lepton mass ratio | K = 2/3 | Spectral: eigenvalue ratio λ₊/|λ₋| = 2:1 | 3 |
| Lepton mass constraint | 11 ppm | Vertex occupation ∝ |ψᵢ|² | 4 |
| Tribimaximal PMNS mixing | U_TBM exact | Eigenvector–vertex change of basis | 5 |

All four are derived from CPP axioms with no free parameters.

---

## The Nine Strong-Sector Theorems (Strong Sector Paper)

| # | Theorem | Key result |
|---|---------|------------|
| 1 | SU(3)_c from tetrahedral hopping | Gell-Mann matrices reproduced exactly |
| 2 | Gluon masslessness | From open-path topology (exact) |
| 3 | One-loop β-function | β₀ = 7 from Casimir algebra |
| 4 | α_geom from 600-cell Voronoi | Exact closed form: 3(11+5√5)√(5+√5)/320 |
| 5 | k_SM derived | From α_geom and coordination number z=12 |
| 6 | sea_strength derived | Factor 120/12 from 600-cell vertex-to-cage count |
| 7 | GMO mass formula | From SU(3) algebra, matches hadron data |
| 8 | Hadron decuplet equal spacing | From SU(3) representation theory |
| 9 | Quark mass ordering (strict) | m_u < m_d < m_s < m_c < m_b < m_t proved |

All nine theorems are proved or proved-with-honest-caveat.
Open problems are registered in `open_problems/`, not hidden.

---

## Authoritative Files — Read These

All authoritative `.tex` files live in `papers/`. These are the theory.

```
papers/
├── paper_1_binding-mechanisms_and_cage_stability.tex
├── paper_1b_reconstruction_1_of_original_CPP_mass_calculations.tex
├── paper_1c_reconstruction_2_bridge_original_to_600_cell.tex
├── paper_2_mass_generation_from_geometric_hierarchies_and_cage_complexity.tex
├── paper_3_k3_spectral_theorem_koide_formula.tex          ← K3 theorem, v5
├── paper_4_charged_lepton_masses_from_k3_spectral_theorem.tex
└── paper_5_tribimaximal_neutrino_mixing_zeroth_order_pmns_from_k3_cage_base.tex
```

The strong sector paper lives at the repo root of the series:

```
cpp_ss_unified_v2.tex    ← Strong sector: 9 theorems, submission-ready
```

---

## What Is Proved vs What Is Open

### Proved (no remaining caveats)
- SU(3)_c from 600-cell tetrahedral hopping (Theorem 1)
- Gluon masslessness from open-path topology (Theorem 2)
- β₀ = 7 (Theorem 3)
- α_geom exact closed form (Theorem 4)
- k_SM and sea_strength derived (Theorems 5–6)
- GMO relations and hadron spectrum (Theorems 7–8)
- δ = 1/3 charge quantisation (Theorem 1, Paper 1)
- K = 2/3 Koide ratio from K3 spectrum (Paper 3, all postulates derived)
- Tribimaximal PMNS at zeroth order (Paper 5)

### Proved conditional / consistency checks
- K = 2/3 satisfied by nature to 11 ppm (Paper 4, consistency check)
- TBM angles within ~10% of NuFIT (Paper 5, zeroth order)

### Open (registered in `open_problems/`)
| ID | Problem | Gate |
|----|---------|------|
| OP-SS-1 | Quark mass ladder: exact mechanism | Next research session |
| OP-SM-7d | Koide phase θ = 132.73° | Electroweak sector (proved: not from K3+SSV) |
| OP-SM-7e | Why exactly three lepton generations | Group theory of 600-cell cells |
| OP-SM-4 | Capotauro mechanism for θ₁₃ | TBM corrections, reactor angle |
| OP-SM-5 | TBM corrections (~10%) | Charged-lepton diagonalisation |
| OP-EW-1–6 | Electroweak sector open problems | EW series consolidation |
| OP-QM-1 | Born rule from CPP ZBW dynamics | Foundational QM series |

### Falsified (recorded so they are not tried again)
- φ^(3(l-1)) volume scaling for quark masses: 3–8× error (PS-1, March 2026)
- C₆₀ cage for top quark: no 60-vertex shell in 600-cell (PS-1)
- Aharonov-Bohm loop as origin of θ: C3 symmetry prevents it (Session F)
- 4D 600-cell embedding breaking C3: tested computationally, C3 preserved (Session G)

---

## Repo Structure

```
600-cell_standard_model_emergence/
│
├── papers/                          ← AUTHORITATIVE: final .tex files
│
├── cpp_ss_unified_v2.tex            ← AUTHORITATIVE: strong sector paper
├── cpp_strong_series.bib            ← bibliography
│
├── open_problems/                   ← registered open problems
│   ├── README.md
│   ├── OP-SM/   OP-SS/   OP-EW/
│   ├── OP-SR/   OP-QM/   OP-SD/
│   └── OP-GLOBAL/
│
├── potential_solutions.md           ← candidate mechanisms for open problems
│
├── p1-binding-mechanisms/           ← Paper 1 derivations
├── p2-*/                            ← Paper 2 derivations (mass generation, EW, etc.)
├── p3-lepton-koide-spectral/        ← Papers 3–5 derivations
│   └── derivations/
│       └── ps1_quark_mass_ladder.ipynb
│
├── cpp-zbw-mixing-fractions/        ← ZBW mixing fraction notebooks
│   └── notebooks/
│       ├── lepton_zbw_mixing.ipynb
│       └── quark_zbw_mixing.ipynb
│
├── suppression/                     ← cross-paper suppression mechanisms
│
└── archive/                         ← superseded/development work
    ├── README.md                    ← what is here and why
    └── grok-development/            ← early Grok explorations
```

---

## Development Logs

Session-by-session records of what was attempted, what was found, and what
changed between paper versions:

- `papers/development_p3-koide-spectral.md` — Sessions A–H (K3 theorem, Papers 3–5)
- `papers/development_strong_series.md` — strong sector sessions

---

## Key Numerical Constants (All Derived)

| Constant | Value | Source |
|----------|-------|--------|
| φ (golden ratio) | (1+√5)/2 = 1.6180… | 600-cell vertex coordinates |
| α_geom | 3(11+5√5)√(5+√5)/320 ≈ 0.5594 | 600-cell Voronoi integral, Theorem 4 |
| k_SM | α_geom/(12φ²) ≈ 0.01781 | Theorem 5 |
| sea\_strength | 10·k_SM ≈ 0.1780 | Theorem 6 |
| ħω₀ | sea·ħc/r_conf ≈ 87.8 MeV | ZBW hopping energy |
| E_eDP | sea·ħc/(φ²·r_conf) ≈ 83.9 MeV | Theorem 3 |
| δ | 1/3 (exact) | Theorem 1: C3 completeness |
| K (Koide) | 2/3 (exact) | K3 spectral theorem: λ₊/|λ₋| = 2 |

One calibration: `r_conf ≈ 0.4 fm` from the Cornell potential / hadron size.

---

## What Comes Next

**Ready to submit now (no further changes needed):**
1. `cpp_ss_unified_v2.tex` — strong sector
2. `paper_3_k3_spectral_theorem_koide_formula.tex`
3. `paper_4_charged_lepton_masses_from_k3_spectral_theorem.tex`
4. `paper_5_tribimaximal_neutrino_mixing_zeroth_order_pmns_from_k3_cage_base.tex`

**Next research sessions:**
1. PS-1 (quark mass ladder): Thomas's DP-cloud thermal picture — compute SSV
   radial potential eigenvalues with cage boundary conditions
2. EW series consolidation: close OP-EW-1 through OP-EW-6
3. Paper 6 (neutrino masses): σ = 120^{-d} suppression formula
4. OP-SM-4 (Capotauro → θ₁₃): complete the PMNS sector

---

## Authorship and Standards

Every numerical claim in the papers is backed by runnable code.
The standard: if a result cannot be verified by re-running a notebook or
script, it does not appear in a paper.

Papers are reviewed by Claude Opus (Anthropic) before submission.
Fabricated tables (Grok, March 2026, twice) are documented in the
archive and in the development logs. The verification standard they
violated is the standard every result must meet.

**Authors:**
- Thomas Lee Abshier ND — physical framework, direction, theoretical insight
- Claude Sonnet / Opus (Anthropic) — derivations, code, paper writing, review
- Grok (xAI) — conceptual contributions (credited per session in dev logs)

---

*License: Content CC-BY-4.0; Code MIT (see individual files).*  
*Feedback, rigorous critiques, and falsification attempts are welcome.*
