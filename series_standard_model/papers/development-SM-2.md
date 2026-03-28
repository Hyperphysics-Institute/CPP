# Development History: SM-2 — Mass Generation from Geometric Hierarchies in the 600-Cell Lattice

**Series:** 600-Cell Standard Model Emergence
**Authors:** Thomas Lee Abshier ND, Grok (xAI), Claude Sonnet (Anthropic)
**Document type:** Development narrative — laboratory notebook record
**Last updated:** 26 March 2026

---

## Purpose of This File

This document records the intellectual history of SM-2: why it was written, what it attempted, what was superseded by later papers, and why its honest documentation of superseded claims is itself a model for scientific practice. SM-2 is unique in the CPP series in having a prominent "consistency with later papers" section that explicitly lists four results that were incorrect or imprecise in the original version. Understanding why these corrections were needed, and how they were discovered, is as important as understanding the paper's positive results.

---

## The Original Goal: A Mass Formula for All SM Particles

SM-2 was written before SM-1, SM-3, SM-4, SM-5, and SS-1 were completed. Its goal was ambitious: to produce mass estimates for all Standard Model particles from a unified CPP framework, using one calibration constant ($k \approx 0.0185$, fixed to the electron mass) and geometric structural assignments for each particle.

The framework was semi-empirical from the start. The cage assignments (which cage geometry corresponds to which particle) were motivated by the 600-cell polyhedral structure but were not derived from it. The ZBW energy contributions, inter-cage bonding terms, and DP cloud corrections were parameterised by effective occupancy values $N_k$ that were chosen on geometric grounds and refined to match PDG data.

The result was a framework that produced calibrated consistency with PDG values across all SM particles — but "calibrated consistency" is different from "parameter-free prediction," and SM-2 was honest about this distinction from its early versions. The paper was always positioned as semi-empirical scaffolding that would eventually be replaced by rigorous derivations.

---

## The Four Superseded Claims: Development History

### Claim 1: $1/\phi^2 \approx 1/3$ for charge screening

**Original claim:** The fractional charge of quarks ($+2/3$ for up-type, $-1/3$ for down-type) was derived from orbital ZBW charge screening by a factor of approximately $1/\phi^2 \approx 0.382 \approx 1/3$. The golden ratio $\phi$ appears throughout the 600-cell geometry, and $1/\phi^2$ was identified as the natural screening factor.

**What was wrong:** The approximation $1/\phi^2 \approx 1/3$ has a 14.6% error. Charge quantisation is an exact result ($\delta = 1/3$ exactly), not an approximate one. The $\phi$-based derivation was motivated by pattern-matching rather than rigorous geometry.

**How it was corrected:** SM-1 Theorem 1 proves $\delta = 1/3$ exactly from C3 cage symmetry and the completeness condition (all colour charges at base vertices sum to 1, and C3 symmetry forces all three to be equal). This is a topological proof that requires no approximation. The $1/\phi^2$ argument is retained in SM-2 Appendix G/H for historical context, clearly labelled as superseded.

**Lesson:** When a CPP result is approximate and a more fundamental derivation is available, the approximate result should be replaced rather than defended. The 14.6% discrepancy was a signal that the mechanism was not correctly identified.

### Claim 2: C₆₀ (60 vertices) as the top quark fourth cage

**Original claim:** The top quark was assigned to a fullerene-like cage of approximately 60 vertices, by analogy with the C₆₀ buckminsterfullerene.

**What was wrong:** No 60-vertex distance shell exists in the 600-cell. The assignment was based on qualitative reasoning (top quark mass requires a cage about 60 times larger than the bottom quark's cage) without verification against the actual 600-cell geometry.

**How it was corrected:** PS-1 computed the exact 600-cell distance shells and found no 60-vertex shell. The 30-vertex shell at $d^2 = 2$ was identified as the leading candidate. SM-2 updates all references to C₆₀ accordingly and notes that the mass formula using the 30-vertex shell is an open problem.

**Lesson:** Cage assignments must be verified against the exact 600-cell geometry, not estimated from mass ratios.

### Claim 3: Koide ratio from $\phi$-scaling

**Original claim:** The Koide ratio $K = 2/3$ for charged leptons was argued to follow from $\phi$-based scaling of lepton masses. The golden ratio appears in the 600-cell geometry, and the Koide formula was related to $\phi$-ratios.

**What was wrong:** The $\phi$-scaling gives the right order of magnitude but not the correct mechanism. The Koide relation is an exact result (K = 2/3 to 11 ppm), and an approximate mechanism cannot explain an exact result. The correct mechanism is spectral: the K3 eigenvalue ratio 2:1 forces K = 2/3 exactly, as proved in SM-3.

**How it was corrected:** SM-3 proves K = 2/3 from the K3 spectral theorem without reference to $\phi$. The SM-2 $\phi$-scaling argument is retained for historical context but is clearly superseded.

**Lesson:** The golden ratio $\phi$ appears throughout the 600-cell but is not the direct cause of every CPP result that involves numbers close to $\phi$-ratios. The spectral theorem is the correct mechanism for the Koide relation.

### Claim 4: Muon g-2 framed as a prediction

**Original claim:** The fractional DP mixing in the muon's orbital ZBW ($\sim 68.5\%$ eDP, 13% qDP, 18.5% hDP) was calibrated to the then-anomalous Fermilab muon g-2 measurement, and the agreement was described as a prediction.

**What happened:** The 2025 lattice QCD update brought Standard Model theory into agreement with experiment, resolving the anomaly. The "discrepancy" that SM-2 had calibrated to was shown to be a theory calculation error, not a new physics signal. The CPP "prediction" was therefore a post-diction of a discrepancy that turned out not to exist.

**How it was corrected:** SM-2 Version 30 relabels the muon g-2 result as a post-diction consistent with the resolved Fermilab measurement $(3.75 \pm 6.43) \times 10^{-10}$ (0.58σ tension, consistent with zero). The mixing fractions that produced this result were calibrated to the prior anomaly value; with the anomaly resolved, the post-diction is consistent but no longer interesting as a claim.

**Lesson:** Claims labelled as predictions should be made before the relevant measurement, not calibrated to existing anomalies. The Fermilab resolution exposed the SM-2 framing as post-hoc.

---

## The Positive Contributions of SM-2

Despite the four corrections, SM-2 makes genuine contributions that have not been superseded:

**1. The ZBW energy spectrum:** The framework of ZBW energy contributions, with geometric suppression $\sigma = 120^{-d}$ for $d$ unbound lattice dimensions, is the physical picture underlying SM-2's mass hierarchy. The $\sigma = 120^{-3}$ suppression for neutrinos (giving $\Sigma m_\nu \sim 0.017$ eV, consistent with cosmological bounds) is a specific prediction of this framework that has not been falsified.

**2. The DP composition rules:** SM-2 develops the rules for DP composition (leptons use equal 25% mix; quarks use radial gradient from qDP-favoured near centre to equalised outward). These rules encode the physical difference between colour-neutral and colour-charged particles and are used throughout the SM series.

**3. The semi-empirical calibration as a research map:** The effective occupancy parameters $N_k$ for each particle are not derived from first principles, but they are identified as the primary targets for future derivation (OP-SS-1). SM-2 functions as a map: it shows where the CPP framework needs to go (derive $N_k$ from cage geometry) and provides calibrated values that any future derivation must reproduce.

**4. The capotauro mechanism (SM-2 context):** The Capotauro symmetry-breaking event — the chiral polarity bias that distinguishes up-type from down-type quarks — is introduced in SM-2 and elaborated in SM-5 (for neutrino mixing corrections). This is CPP's account of the CP violation that breaks the up/down quark symmetry, and it is a genuine theoretical contribution even if it is not yet derived.

---

## The Role of SM-2 in the Series Architecture

SM-2 occupies an unusual position in the series: it is more empirical than any other paper, explicitly semi-empirical in its approach, and has had four significant claims superseded by later work. Yet it remains in the series because it serves an irreplaceable function: it is the paper that shows the CPP framework can be applied to all Standard Model particles simultaneously, producing calibrated estimates across the full mass spectrum from the electron to the top quark.

No other paper in the series attempts this comprehensive scope. SM-1 treats the cage structure; SM-3 through SM-5 treat the lepton sector; SS-1 treats the strong sector. SM-2 is the synthesis paper — the place where all the pieces are assembled into a unified, if approximate, picture of SM particle masses.

The corrections record in SM-2 is therefore not a weakness but a strength. It shows that the CPP framework is self-correcting: when more rigorous derivations become available, they replace the approximate motivational arguments without discarding the framework as a whole. SM-2's semi-empirical scaffold is being progressively replaced by rigorous theorems — but the scaffold was necessary to identify where the rigorous theorems needed to be.

---

*Document prepared by Claude Sonnet (Anthropic) in collaboration with Thomas Lee Abshier ND, March 2026. To be updated as OP-SS-1 (effective occupancy derivation) and the EW series develop.*
