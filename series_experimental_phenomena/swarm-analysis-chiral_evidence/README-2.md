# Swarm Analysis: Chiral Lattice Evidence Across Scales

**Series:** Experimental Phenomena  
**Status:** Active research — supports Capotauro mechanism and OP-SM-7d  
**Last updated:** 26 March 2026  
**Authors:** Thomas Lee Abshier ND, Grok (xAI)

---

## What This Is

The Swarm Analysis is a systematic search for signatures of CPP's
chiral lattice symmetry-breaking (the Capotauro mechanism) in
real experimental and observational results across four scale regimes:

| Scale | Examples |
|-------|---------|
| **Subquantum** | Spintronics, spin Hall effect, ZBW signatures |
| **Quantum** | Double-slit, entanglement, quantum heating, cavity QED |
| **Macroscopic/Astrophysical** | Black hole jets, gamma-ray bursts, star clusters |
| **Cosmological** | Baryogenesis, dark matter, cosmic web filaments |

Fifty-eight real experimental results (January 2026 series) were each
interpreted through the CPP lens and assigned a one-line CPP explanation.
The catalog is in `swarm-entries-catalog-1-58.ipynb`.

---

## Why This Was Done

The Capotauro event — the chiral symmetry-breaking that created the
up/down quark distinction and matter/antimatter asymmetry — is a core
CPP postulate (see `postulates_and_theorems.md`, P-Capotauro).
If CPP is correct, signatures of this chirality should appear at
every scale, because the 600-cell lattice underlies all of physics.

The challenge issued to the analysis team (Claude Sonnet 4.0, January
2026): *find chiral evidence in randomly selected phenomena at
subquantum, quantum, macroscopic, and astronomic scales.*

---

## Key Finding

**The chiral signal is strongest at quantum and subquantum scales.**

This is the expected result if the Capotauro chirality is a
fundamental lattice property: at scales approaching the Planck length,
the discrete 600-cell geometry dominates. At macroscopic and cosmic
scales, the continuum limit smooths out the lattice asymmetry, and
chiral signatures become weaker relative to classical dynamics.

This scale-dependence is itself a CPP prediction:

> *Chiral asymmetry in observable phenomena should decrease with
> increasing physical scale, following the suppression factor
> σ = 120^{−d} where d is the number of effectively unbound
> lattice dimensions at that scale.*

This is the same suppression that appears in the neutrino mass formula
(Paper SM-5) and the vacuum energy estimate (TN-SR-1).

---

## Strongest Individual Entries

These entries have the most direct connection to proved CPP results
and are candidates for quantitative follow-up:

| Entry | Phenomenon | CPP connection |
|-------|-----------|----------------|
| **5** | Negative heating in trapped-ion system | Non-local ZBW energy redistribution via lattice edges |
| **13** | Giant intrinsic spin Hall effect | SSV torque on electron spins — connects to g-2 analysis |
| **51** | Shadow points as dark matter | Unpaired low-coherence CPs — connects to DP Sea structure |
| **55** | T2K/NOvA CP violation hint | Lepton-sector CPV seeds baryogenesis via Capotauro bias |
| **56** | 20 GeV galactic halo gamma excess | Shadow-point annihilation — testable prediction |
| **57** | 15 Mpc rotating cosmic filament | Primordial chiral torque on cosmic web structure |

---

## What Is Needed Before These Become Publications

The current swarm entries are qualitative: each says "X is caused by
chiral lattice effect Y." They are not yet falsifiable in the strong
sense because they do not give a predicted magnitude.

To convert a swarm entry into a publishable CPP prediction, each
needs:

1. **A quantitative formula** — what does CPP predict for the
   magnitude of the chiral effect at this scale?
2. **A comparison to the observed value** — does CPP's prediction
   match, or is there a discrepancy?
3. **A falsification criterion** — what observation would rule out
   the CPP interpretation?

The six entries above are the natural starting points for this work.

---

## Planned Paper

**CC-2: Chiral Signatures Across Scales — CPP Predictions for
Experimental Results at Quantum and Subquantum Scales**

Target scope: The five or six quantum/subquantum-scale entries with
the strongest CPP signal, developed with quantitative predictions.

**Gate:** CC-1 (Ξcc⁺ analysis) must be on OSF first.
Both CC-1 and CC-2 require SS-1 on OSF as the backbone citation.

---

## Connection to Open Problems

| Open Problem | Connection |
|-------------|------------|
| OP-SM-7d (Koide phase θ) | The Capotauro mechanism is the leading candidate for why C3 symmetry is broken — swarm entries at quantum scale may provide empirical evidence for this |
| OP-SR-6 (Big Bang cosmology) | Entries 55–57 (baryogenesis, cosmic web) connect to the Capotauro timing and the early universe |
| OP-SS-1 (quark mass formula) | Entry 51 (shadow points as dark matter) connects to the DP Sea structure that also determines quark masses |

---

## File Structure

```
series_experimental_phenomena/
└── swarm_analysis/
    ├── README.md                          ← this file
    ├── swarm-entries-catalog-1-58.ipynb   ← full catalog of all 58 entries
    └── entries/                           ← individual entry analysis notebooks
        ├── entry_05_negative_heating.ipynb
        ├── entry_13_spin_hall.ipynb
        └── ... (to be developed)
```

---

## Note on Methodology

The swarm entries were generated by presenting real experimental
results to the analysis team and asking for CPP interpretations.
This methodology has an inherent risk: it is easy to find a
CPP-sounding explanation for any result post-hoc. The entries
should be treated as **hypothesis generation**, not validation.

Validation requires the additional step of making quantitative
predictions *before* looking at the data — which is what the
planned CC-2 paper will do for selected entries.

---

*See also: `postulates_and_theorems.md` (Capotauro mechanism),
`open_problems/OP-SM/OP-SM-7d_koide_phase_theta.md`,
`paper_catalog.md` (CC-1, CC-2 planned)*
