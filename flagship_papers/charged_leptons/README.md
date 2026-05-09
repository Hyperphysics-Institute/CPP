# SF-1: Charged Lepton Mass Spectrum from K3 + 600-Cell Geometry

**Status:** Planned. Primarily reframing of existing strong corpus; lowest-risk SF-line paper to ship first.
**Estimated sessions to v1.0 SHIP:** 3–5.
**Inclusion criterion fit:** (1) named known-unknown — the charged lepton mass hierarchy and the Koide formula; (4) bridge to recognized mathematics — K3 graph spectral structure.

---

## Scope

The charged lepton mass spectrum ($m_e, m_\mu, m_\tau$), the Koide formula $K = 2/3$, the Weinberg angle, and the Koide phase $\theta$, all from a single calibration ($m_e$) plus 600-cell geometry. The paper presents the existing K3 spectral derivation in apex-paper form: focused on the named problems (Why $m_\mu/m_e \approx 207$? Why $m_\tau/m_\mu \approx 17$? Why does Koide hold to 11 ppm?), audience-targeted at the broader physics community, with reviewer-anticipation rigor.

## Source material (from current corpus, primarily reframing)

| Source paper | Content drawn |
|--------------|---------------|
| SM-1 | C3 cage symmetry, $\delta = 1/3$ exact charge quantisation, ZBW Hamiltonian foundations |
| SM-3 | K3 Spectral Theorem; Koide $K = 2/3$ from $A_{K_3}$ adjacency spectrum, conditional on P1–P3 (Layer A/B/C decomposition) |
| SM-4 | Charged lepton mass formulae from Koide + amplitude $A$ + phase $\theta$; structural impossibility of $\theta$ from K3+SSV |
| SM-6 | $\sin^2\theta_W = 3/(8\phi)$, Koide phase derived, $m_\mu = 105.47$ MeV (0.18%), $m_\tau = 1774.1$ MeV (0.15%); zero shape parameters |

## Inheritance status of source material

The source material is in good shape but has Layer-B inheritances (P3 thermal equilibration in SM-3; the Koide phase derivation in SM-6). SF-1 inherits these honestly per the SS-9 conditional-theorem closure pattern. No new derivation work is anticipated; if a Layer-B condition surfaces during reframing, it is registered as `OPEN-FP-1-*` and inherited rather than closed.

## Strategic role within Option-3 architecture

SF-1 ships first because: (a) primarily reframing means lowest derivation risk; (b) early ship establishes flagship-paper momentum for the SF-line before SF-4 (the heavy lift) ships; (c) charged leptons are the most-precisely-measured fermion sector, so the apex-paper rhetorical framing has the strongest empirical anchor.

## What this folder will contain (as drafting begins)

- `sf-1_outline.md` — paper outline analogous to the original Track-1 hierarchy outline
- `sf-1_charged_leptons.tex/.pdf` once drafting starts
- `sketches/` — staging documents for any sub-derivations
- `documentation_suite/` — companion documentation per SS-9 four-tier discipline
- `letters/` — e.g. cover letter for OSF, arXiv submission guide
- `founders_voice/` — Thomas's framing and motivation pieces

---

*Folder established at Session 38 (patch 0295) per Option-3 four-flagship + SF-5 architecture. See [`../README.md`](../README.md) for the full architecture rationale.*
