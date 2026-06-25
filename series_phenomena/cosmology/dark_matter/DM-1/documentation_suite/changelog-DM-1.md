# Changelog — DM-1 (Substrate Dark-Matter Candidate)

Canonical .tex: `DM-1/DM-1_substrate_dark_matter_candidate.tex`
(Filename fixed; version history tracked here, not in the filename.)

**Versioning convention:** assembled drafts ship at **v0.1 (DRAFT)** and increment
through the panel review cycle (v0.2, v0.3, … as reviewer feedback is folded in),
promoting to **v1.0** only once the multi-AI panel is satisfied at final ship.
DM-1 is pre-review.

## v0.1 (DRAFT) — Positive-Discriminant Candidate — Patch 0856 (assembled) / 0857 (version label) (24 June 2026)
- **Promotion to .tex.** Publication-form conversion of the working markdown draft
  `series_phenomena/cosmology/dark_matter/DM-1_draft_manuscript.md` (assembled
  Patches 0700–0855) into the EU-1 house style (article class, natbib/plainnat,
  CPP macros, per-paper subfolder).
- Three figures included via `\graphicspath{{../figures/}}`: residual V(r) +
  saturation (Fig. 1, Patch 0849), density confrontation (Fig. 2, Patch 0850),
  core-radius-vs-σ/m panel (Fig. 3, Patch 0851).
- Embedded bibliography: CPP flagships (SF-3, SF-5, SR-1, QM-1) + verified
  external refs (Mateo+ 1991; Goerdt+ 2006; Jardel & Gebhardt 2012; de Blok+ 2008;
  Oh+ 2008; Kaplinghat, Tulin & Yu 2016; Li 2004; McCrea & Milne 1934). All
  external citation details web-verified at promotion.
- Honesty carried verbatim from the draft: the IC 2574 high-velocity tension
  (abstract, §6, §7, grade), the calibrated mass scale + abundance (§8), and the
  Sea-gravitation gate now down to one condition after the c08 discharge (§9,
  Patch 1161). Grade: positive discriminant, not full identification.
- Compiles clean (pdflatex, two-pass: 0 undefined citations/refs; 9 pp).

### Content provenance (markdown draft → .tex)
Draft sections §1–§11 → paper §§1–10 + appendix; internal dev scaffolding
([FILLED]/[TIGHTEN]/[DONE] markers, the §11 checklist, the provenance block)
dropped in the publication form. The markdown draft remains the working source
of truth; the .tex is the shippable artifact.

### Open at ship (none gating; all flagged in §8–§10 + Open Directions)
- f pin-down (companion mass-scale / colour-polarizability) → collapses the
  magnitude band and decides the IC 2574 tension.
- Sea-gravitation: one remaining condition (event-horizon IR-scale selection).
- Abundance route-B (asymmetric DM) derivation of ~5:1.
- OSF deposit manifest (Thomas-action manual step).
