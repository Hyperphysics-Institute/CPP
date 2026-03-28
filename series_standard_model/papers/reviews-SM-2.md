# Reviews: SM-2 — Mass Generation from Geometric Hierarchies in the 600-Cell Lattice

**Series:** 600-Cell Standard Model Emergence
**Document type:** Living review record — objections, responses, revisions
**Last updated:** 26 March 2026

---

## Purpose of This File

This document records all substantive reviews of SM-2. SM-2 is the most heavily corrected paper in the series and the one most likely to draw critical attention from external reviewers, because it claims mass estimates for all Standard Model particles while openly acknowledging that several of those claims have been superseded or corrected. The reviews file records the history of those corrections and provides prepared responses to the objections that SM-2's scope and honesty will inevitably provoke.

---

## Review 1: Claude Opus Pre-Submission Review (March 2026)

**Reviewer:** Claude Opus (Anthropic) — rigorous pre-submission review
**Date:** March 2026
**Verdict:** Corrections incorporated; submission-ready with caveats prominently noted
**Overall assessment:** The Opus review flagged four significant issues in earlier versions: the C₆₀ assignment, the $1/\phi^2$ charge approximation, the Koide $\phi$-scaling, and the muon g-2 framing. All four were corrected in Version 30.

---

### Objection 1.1: C₆₀ Assignment Falsified

**The objection:** The top quark cage assignment to C₆₀ (60 vertices) is inconsistent with the exact 600-cell distance shell geometry (PS-1, 2026).

**Assessment: VALID — major correction requiring explicit documentation**

**Response/revision:** All C₆₀ references replaced with 30-vertex shell throughout paper and glossary. Prominent correction notice in abstract and Version 30 note. Consistency table added noting this correction. The mass formula using the 30-vertex shell is registered as open.

**Status: RESOLVED**

---

### Objection 1.2: $\delta = 1/3$ Is Exact; $1/\phi^2$ Approximation Is Wrong

**The objection:** Charge quantisation $\delta = 1/3$ is proved exactly in SM-1 (Theorem 1) from C3 symmetry. The $1/\phi^2 \approx 0.382 \approx 1/3$ approximation used in SM-2 Appendices G/H has a 14.6% error and should not be cited as the derivation.

**Assessment: VALID — critical for series integrity**

**Response/revision:** SM-2 Version 30 adds a dedicated section "Charge Quantisation: Relationship to SM-1" that explains the supersession clearly. Appendices G/H are retained for historical context but explicitly labelled "Approximate; Superseded by SM-1." Every reference to the quark charge derivation in the paper now cites SM-1 Theorem 1 as the correct result.

**Status: RESOLVED**

---

### Objection 1.3: Koide Ratio from $\phi$-Scaling Is Wrong Mechanism

**The objection:** SM-3 proves $K = 2/3$ from the K3 spectral theorem (eigenvalue ratio 2:1). The $\phi$-scaling approach in SM-2 gives the right order of magnitude but not the correct physical mechanism.

**Assessment: VALID — important distinction**

**Response/revision:** SM-2's consistency table notes: "Koide ratio from $\phi$-scaling — Superseded by SM-3 K3 spectral theorem — $K = 2/3$ exact from spectral ratio $\lambda_+/|\lambda_-| = 2$." The $\phi$-scaling approach is retained for historical context only.

**Status: RESOLVED**

---

### Objection 1.4: Muon g-2 Was a Post-Diction, Not a Prediction

**The objection:** The mixing fractions in SM-2 were calibrated to the prior Fermilab anomaly. The 2025 lattice QCD resolution of the anomaly means this was a post-diction of a discrepancy that turned out not to exist.

**Assessment: VALID — requires honest reframing**

**Response/revision:** SM-2 Version 30 explicitly labels the muon g-2 result as "a post-diction, not an independent prediction." The relevant passage now reads: "The mixing fractions were calibrated to the prior anomaly value. With the 2025 lattice QCD update bringing theory into agreement with experiment, this is now a post-diction rather than a prediction."

**Status: RESOLVED**

---

### Objection 1.5: Series Name and Paper IDs Inconsistent

**The objection:** Title said "Standard Model Emergence in the 600-Cell Lattice Series" and referred to "Paper 1," "Paper 3," etc.

**Assessment: VALID — series consistency**

**Response/revision:** Title updated to "SM-2" with correct series name. All "Paper N" references updated to SM-N throughout body text and consistency table.

**Status: RESOLVED**

---

## Summary Table of Objections

| # | Objection | Assessment | Status |
|---|-----------|-----------|--------|
| 1.1 | C₆₀ cage does not exist | Valid — major correction | Resolved |
| 1.2 | δ = 1/3 exact; φ² approximation wrong | Valid — critical | Resolved |
| 1.3 | Koide φ-scaling is wrong mechanism | Valid | Resolved |
| 1.4 | Muon g-2 is post-diction | Valid | Resolved |
| 1.5 | Series name and paper IDs wrong | Valid | Resolved |

---

## Anticipated Future Objections

**F1: "SM-2 has four corrected claims. This means the framework is unreliable."**

Response: The four corrections demonstrate that the CPP framework is self-correcting, not that it is unreliable. Each correction was made when a more rigorous derivation became available (SM-1 for charge quantisation, SM-3 for the Koide mechanism, PS-1 for the cage geometry, the Fermilab/lattice QCD resolution for the g-2 framing). A framework that identifies its errors and corrects them is more trustworthy than one that never flags corrections. The corrections are documented prominently in the paper itself, not hidden in errata.

**F2: "The effective occupancy parameters $N_k$ are just fitting parameters, not geometric results."**

Response: Correct — $N_k$ values are structural assignments motivated by cage geometry but calibrated to PDG data. This is explicitly stated throughout the paper. The $N_k$ values are the primary target of OP-SS-1 (derivation of cage-specific binding energies from first principles). SM-2 is a semi-empirical framework; it claims calibrated consistency, not parameter-free prediction. The distinction is maintained throughout the paper.

**F3: "Neutrino mass estimates are not predictions — $\sigma = 120^{-3}$ is another free parameter."**

Response: The suppression $\sigma = 120^{-d}$ for $d$ unbound lattice dimensions is not a free parameter in the usual sense: the exponent $d = 3$ for neutrinos follows from CPP's treatment of unbound ZBW modes ($d = 0$ for bound orbital, $d = 1$ for linear ZBW extras, $d = 3$ for fully unbound). The base 120 is the number of 600-cell vertices — a fixed geometric property. The suppression formula is therefore a geometric prediction, not a fitted parameter. The neutrino mass estimates ($\Sigma m_\nu \sim 0.017$ eV) are consistent with the cosmological bound ($< 0.072$ eV, Planck+DESI 2025), and the framework predicts normal mass ordering, which is consistent with current data. These are genuine, falsifiable predictions.

**F4: "The Capotauro mechanism is named after something unexplained and has no derivation."**

Response: The Capotauro mechanism is a hypothesis — a proposed physical event (chiral symmetry breaking in the early universe that distinguishes up-type from down-type quarks) that CPP invokes to explain certain asymmetries in the quark and neutrino sectors. It is not derived in SM-2. It is registered as an open problem and named for identification purposes. The name does not imply the mechanism is established; it is a label for a research target, following standard practice in theoretical physics (e.g., "the Higgs mechanism" was named and used before the Higgs boson was confirmed).

**F5: "This paper has too many caveats and corrections to be publishable."**

Response: The level of caveat and correction in SM-2 reflects the paper's actual epistemic status, not a deficiency in the science. The alternative — publishing without the caveats — would be dishonest. SM-2's honest accounting of what is derived vs. calibrated, what is correct vs. superseded, is a model for how theoretical physics papers should be written when they are part of a developing programme. Reviewers who demand fewer caveats are asking for less honesty, not more rigor.

---

*Document prepared by Claude Sonnet (Anthropic) in collaboration with Thomas Lee Abshier ND, March 2026. Append new reviews below this line with date and reviewer.*
