# Blast-radius adjudication — SR-1 k / PSR inheritors

**Date:** 15 July 2026 · **Patch:** 2480 · **Handover queue item:** 3
**Rule applied (SR.md, Patch 2474):** (k, ΔSSV) is a matched normalisation pair; only the
product k·ΔSSV is physical; mixing conventions rescales γ−1 by exactly α (44% at α = 0.5594).

## Method

Corpus-wide grep for the PSR formula, k's value, k·ΔSSV products, and α_geom, classified
per artifact into: **A** (bills k's numerical value as derived), **B** (dimensional-necessity
argument), **C** (α_geom as physical constant), **D** (product-only use), **F** (fabricated-MC
citation). Shipped-tier artifacts (companion .tex + doc-suite .md) adjudicated individually;
reasoning fragments and transcripts are verbatim-by-design records and are out of correction
scope (their statements are historical, not live billing).

## Disposition table

| Artifact | Classes | Verdict | Action |
|---|---|---|---|
| c01 absolute moment | A, D | value-billing only; own physics unaffected | **CORRECTED 2480** — convention note at eq. (PSR); matched-pair rule stated |
| c02 dipole stiffness | A, B, C, D, E, +internal inconsistency | **deepest inheritor**: withdrawn dimensional-necessity billing; "fully geometric γ, no free parameter" (withdrawn); fabricated-MC citation; "56% packing efficiency" interpretation of a unit-dependent number; AND the inline k = 1/(C·l_P³/E_P) was dimensionally inconsistent with its own §1 value — a live matched-pair mixing inside one paper | **CORRECTED 2480** (3 correction notes; original claims quoted-in-withdrawal). **Residual physics question registered: OPEN-SR-C02-NORM** — whether the Coulomb-constant chain, which uses C directly rather than the product, is convention-invariant. Verify-script spec in the registry entry. |
| c03 born rule | D | product-only (1 use) | verified convention-safe; no action |
| c05 newtonian gravity | D | product-only (1 use); E-billings are its own results | verified convention-safe; no action |
| c07 weak-field GR | A, D | one value-billing in the glossary item; all 5 uses inside the product | **CORRECTED 2480** — convention note; explicitly records that no result depends on the convention |
| c08 strong-field GR | D | product-only (22 uses) | verified convention-safe; no action |
| c09 GW echoes | — | no k dependence (E-hits are its own results) | out of blast radius |
| c11 Kerr | — | same | out of blast radius |
| c12 Kerr–Newman | — | same | out of blast radius |
| c13 superradiance | — | same | out of blast radius |
| c14 quark confinement | D | product-only (2 uses) | verified convention-safe; no action |
| SR-2 quadrupole | (SR-1 cite) | zero-parameter billing is the λ = 16πG/c⁴ chain — independent of k, NOT an inheritance. One genuine inheritance: the Weinberg–Witten evasion cited SR-1 for "emergent Lorentz invariance" | **CORRECTED 2480** — the evasion survives (it needs only the preferred-frame structure, which stands); the dependency status made honest (equivalence by construction; derivation open as OPEN-SR-EPSILON). The F4 flag on SR-2_figures.py was a detector bug (AugAssign not counted as fill — fixed); the figures were genuinely regenerated (ledger 0.999998, Patch 1137). |
| SR-1 phenomena doc | C, D, E, F | Section 2 = the withdrawn five-prediction set live; Section 3 = four consilience entries: V1 muon (void twice), V2 the fabricated MC as a registered consilience datum, V3 α_geom two-sector consilience (SR leg withdrawn), V4 GPS (withdrawn deviation formula) | **CORRECTED 2480** — banner + per-entry statuses: P1/P2/P3/P5 WITHDRAWN, P4 CONDITIONAL (Casimir, per 2474), V1 WITHDRAWN, V2 STRUCK (tombstoned), V3 DOWNGRADED to shared-geometry observation (re-evaluable if ΔSSV acquires independent normalisation), V4 REFRAMED (zero deviation by construction, no discriminating power) |
| SR-1 reviews doc | F ×2 | reviewer-praise paragraph endorses three now-withdrawn items (predictions, MC, H.1); v17 CHANGELOG row bills the fabricated MC as "Independent verification" | **CORRECTED 2480** — annotated, not rewritten (review records preserved verbatim; correction notes appended). The annotation states the lesson explicitly: multi-cycle read-time review caught none of it. |
| early-universe reasoning (0732/0733) | (mentions) | verbatim reasoning records; 0733 already carries its own correction (super-c withdrawal) | out of correction scope by design |
| SM-1 glossary/mechanism | — | no solo k-value, no product use (coarse-regex false hit) | out of blast radius |

## Summary

Of the handover's 14 named inheritors plus the doc-suite extension found by the sweep:
**5 corrected** (c01, c02, c07, SR-2, + the SR-1 phenomena/reviews pair), **5 verified
convention-safe** (c03, c05, c08, c14, SM-1 docs), **5 out of scope** (c09/c11/c12/c13 no
k-dependence; reasoning fragments verbatim-by-design). **One live physics question remains:
OPEN-SR-C02-NORM** — the only place in the corpus where the α convention could touch a
physical output, with a pre-specified two-convention verify test and a G7 kill-discipline
clause.

The 44% hazard was found REALIZED in exactly one place: inside c02 itself (the
k = 1/(C·l_P³/E_P) vs k = l_P³/E_P inconsistency), not in any downstream propagation —
every downstream consumer either used the invariant product or quoted the value inertly.
