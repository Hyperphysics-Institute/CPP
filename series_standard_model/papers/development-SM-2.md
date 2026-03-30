# Development History: SM-2 — Mass Generation from Geometric Hierarchies in the 600-Cell Lattice

**Series:** 600-Cell Standard Model Emergence
**Authors:** Thomas Lee Abshier ND, Grok (xAI), Claude Sonnet (Anthropic)
**Document type:** Development narrative — laboratory notebook record
**Last updated:** 30 March 2026

---

## Origins: The Mass Hierarchy Question

SM-2 originated from the most basic empirical challenge to CPP: can
the framework reproduce the actual numbers? SM-1 established that
cage structures exist and are stable, but it left the quantitative
mass question open. The E ≈ N/2 × SSV₀ formula gives qualitative
ordering but the muon is not simply 3× heavier than the electron —
the actual ratio is 207×. Something beyond the bare cage binding
energy must contribute significantly.

The development of SM-2 was driven by the question: what additional
contributions bring the cage binding energies into quantitative
agreement with the PDG mass table?

---

## Phase 1: Identifying the Four Contributions

Early sessions identified four distinct contributions to particle
masses beyond the bare cage binding:

1. ZBW kinetic energy (E_ZBW): the orbital Dipole Pair's kinetic energy
2. Inter-layer bonding (E_inter): SSV interaction between nested cage shells
3. DP cloud energy (E_cloud): energy of the polarised Sea cloud
4. Residual: remaining calibrated correction

The ZBW contribution was the most physically motivated — the orbital
ZBW DP is present in all fermions and contributes the same type of
SSV energy as the cage binding. The suppression factor σ = 120^{-d}
for different particle types emerged as the key to bridging from the
electron (d=0, σ=1) to neutrinos (d=3, σ ≈ 5.8 × 10⁻⁷).

---

## Phase 2: The VEV Formula and k

The vacuum expectation value formula ⟨φ⟩ = k × E_P / N_lattice⁴ × φ_k
emerged from dimensional analysis: how should the Planck energy
be suppressed to reach the MeV scale?

The factor N_lattice⁴ = 120⁴ ≈ 2.07 × 10⁸ was identified from the
600-cell's 4D geometry — one factor of 120 per spatial+temporal
dimension. The golden-ratio generation factor φ_k handles the
between-generation scaling. The calibration constant k ≈ 0.0185
was then fixed by the electron mass.

The geometric motivation for k (k ~ 1/(N × φ²) ≈ 0.00318, refined
to 0.0185 by generational averaging) established that k was not
arbitrary — it was of the right order from the lattice geometry alone.
The exact derivation of k was registered as OP-SM-1 and was
subsequently solved to 3.8% via α_geom = 0.5594 (k_SM =
α_geom/(12φ²) ≈ 0.01781). The remaining 4% is the stereographic
projection correction.

---

## Phase 3: Cage Assignments and N_k Calibration

The effective cage occupancy values N_k were developed through
iterative comparison with PDG masses. For leptons, the correspondence
is clean: N_k = 1, 4, 12 for electron, muon, tau maps onto the
cage vertex counts (minimal, tetrahedral, icosahedral) with good
quantitative agreement when all four contributions are included.

For quarks, the N_k values required calibration to PDG because the
light quark masses are non-perturbative and the formula cannot yet
be derived from first principles. The heavy quark values (charm,
bottom, top) are more constrained — the K3 thermal picture (discovered
later, in the PS-1 sessions) confirmed K(c,b,t) = 2/3 to 0.42%,
consistent with the cage framework.

For the gauge bosons (W, Z, Higgs), cage structures were assigned
based on their known properties: W as linear hDP chain (polarity-
inverting, EW series), Z as icosahedral cage (symmetric coupling,
parity-conserving), Higgs as dodecahedral cage (heaviest, scalar).

---

## Phase 4: The Muon g-2 Episode

During SM-2 development, the Fermilab muon g-2 measurement showed
a 4.2σ anomaly from the Standard Model prediction. SM-2 included
an analysis of the DP mixing fraction in the muon's orbital ZBW:
with 68.5% eDP, 13% qDP, and 18.5% hDP, the CPP correction was
δ_μ ≈ 2.9 × 10⁻¹⁰, consistent with the anomaly.

In June 2025, the lattice QCD calculation was updated and the
anomaly was resolved: Δa_μ = (3.75 ± 6.43) × 10⁻¹⁰, consistent
with zero. The CPP calculation was consistent with the anomaly when
it was an anomaly and consistent with zero when it was resolved —
because the mixing fractions were calibrated to the anomaly value.
This converted the g-2 result from a prediction to a post-diction.

The lesson: calibrating any quantity to a disputed experimental value
creates vulnerability when that value is revised. SM-2 v30 explicitly
labels the muon g-2 as a post-diction.

---

## Phase 5: The C₆₀ Falsification (March 2026)

The most significant development event in SM-2's history was the
falsification of the C₆₀ cage assignment. Earlier versions used
60 vertices as the top quark's fourth cage, motivated by the rough
mass ratio top/bottom ≈ 40 — suggesting ~4× more cage vertices than
the bottom's 20-vertex dodecahedral cage.

The PS-1 computation (March 2026) computed all 600-cell distance
shells exactly. The shells have vertex counts 12, 20, 12, 30, 12, 20...
(palindromic). No 60-vertex shell exists. The C₆₀ assignment was
a hypothesis that failed.

The 30-vertex shell at d²=2 was identified as the correct fourth
cage candidate: all 30 vertices equidistant from the reference
vertex, degree-4, vertex-transitive. N_k for the top quark was
recalibrated to ~30000 accordingly. The mass formula using this
geometry is open (OP-SS-1).

This falsification affected SM-1, SM-2, and the open problems
register simultaneously. It is documented here as a record of
CPP's error-correction process.

---

## Phase 6: Consistency Harmonisation (v30, March 2026)

Version 30 incorporated four consistency corrections:

1. C₆₀ → 30-vertex shell (from PS-1)
2. 1/φ² → δ = 1/3 exact (from SM-1 Theorem 1)
3. Koide from φ-scaling → K3 spectral theorem (from SM-3)
4. Muon g-2 prediction → post-diction (from Fermilab 2025 resolution)

These corrections were identified by Claude Opus in the pre-submission
review. Each correction makes the paper more honest and more
consistent with the rest of the series. The consistency table at
the top of SM-2 v30 documents all four superseded claims explicitly.

---

## Current Status (30 March 2026)

SM-2 is submission-ready at v30. It is a semi-empirical framework
demonstrating calibrated consistency of the cage hierarchy with
the full SM mass table, with honest labelling of what is derived
vs calibrated. The principal open problem (OP-SS-1) would convert
it from semi-empirical to predictive.

The six SM-2 documentation files were written on 30 March 2026:
mechanism-SM-2.md, glossary-SM-2.md, reviews-SM-2.md,
philosophy-SM-2.md, development-SM-2.md (this file), and
phenomena-SM-2.md.

---

## Key Decisions Log

| Date | Decision | Rationale |
|------|----------|-----------|
| Early 2026 | Four-contribution formula | Bare cage binding insufficient; ZBW, inter-layer, cloud needed |
| Early 2026 | σ = 120^{-d} for suppression | Geometric dilution across d unbound lattice dimensions |
| Early 2026 | k ≈ 0.0185 calibrated to electron | Single calibration anchor for entire mass table |
| Mar 2026 | C₆₀ → 30-vertex shell | PS-1 falsified C₆₀; 30-vertex shell is correct geometry |
| Mar 2026 | 1/φ² → δ = 1/3 exact | SM-1 Theorem 1 supersedes the approximation |
| Mar 2026 | Koide mechanism relabelled | SM-3 K3 spectral theorem is the correct derivation |
| Mar 2026 | Muon g-2 relabelled post-diction | Fermilab 2025 resolution removed the anomaly |
| Mar 2026 | "Calibrated consistency" language | Scientific honesty requires distinguishing calibration from prediction |
