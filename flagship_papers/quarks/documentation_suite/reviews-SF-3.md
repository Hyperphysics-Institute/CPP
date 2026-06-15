# Reviews — SF-3: The Quark Sector from 600-Cell Geometry

Four review rounds (v0.1 → v0.4), multi-AI panel (ChatGPT, Grok, Copilot). Verbatim
review files archived under `flagship_papers/quarks/review/`. This file is the
navigation summary: who cared about what, and how it was resolved.

## Round 1 (v0.1) — ChatGPT / Grok / Copilot — Mixed → REVISE

First substantive pass. Grok leaned SHIP; ChatGPT/Copilot returned REVISE with
overlapping items. Resolved into v0.2:
- Proposition 5.1 scoped explicitly as a *bookkeeping observation*, not a theorem.
- `m_c` qualified as derived-not-input throughout.
- "Complete quark sector" → "heavy-quark sector".
- "Unification" language softened to "mode-fraction correspondence".
- PDG mass-scheme caveat added (scheme affects comparison, not calibration).
- CKM↔δ_CP analogy bounded ("parallel of posture, not equivalence").

## Round 2 (v0.2) — ChatGPT / Grok / Copilot — REVISE → ship-leaning

Resolved into v0.3:
- Conclusion `m_c` qualifier; acknowledgements reworded.
- §4 bare-partition gloss; §10 `A³` meaning made explicit.
- 120×120 adjacency anchor stated.
- §7 boxed one-line calibration-adjudication summary added.

## Round 3 (v0.3) — ChatGPT / Grok / Copilot — ship-leaning

Resolved into v0.4:
- "forced" → "selected by the mechanism" (generation count).
- §4 "one spectral trace" bounded to the inherited SM-6/SM-7 framework.
- SM-10 reminder (mass values do not depend on it) added to the conclusion.

## Round 4 (v0.4) — Grok SHIP; adversarial line-by-line pass

**Grok:** SHIP (polished, no blockers; minor optional polishing only). Re-verified
RMS 2.1%, complementarity exact, phase 124.04° (0.05%). (`review/sf-3_v0.4_review_grok.md`)

**Adversarial pass:** ready after three small "blocking" framing fixes, all of
which were applied at v1.0. (`review/sf-3_v0.4_review_adversarial.md`)

## Critical Review: the v0.4 adversarial pass — Detailed Response

This pass produced the cycle's most valuable catch. Its three "blocking" items and
their resolutions:

1. **Generation count still over-strong.** "Selected by the mechanism" implies the
   mechanism does the selecting as fact; SM-8 gives a model-dependent selection,
   not a uniqueness proof. → **Resolved:** "selected *within* the SM-8
   antipodal-identification model" (abstract, §6, §9, §13.1).

2. **Proposition 5.1 nuance (the key catch).** The phase–`m_c` independence holds
   *only because* `α_s` is taken as the structural value `5/(8φ)`; a running-
   coupling fit at the charm scale would re-introduce `m_c` indirectly.
   → **Resolved:** stated explicitly in §5, closing the running-coupling loophole.
   This is the difference between a proposition that is true and one that is
   *defensibly* true.

3. **Spectral-trace mapping is a correspondence, not a dynamical unification.**
   SM-6/SM-7 treat the mode fractions as candidates, not RGE-derived gauge
   couplings. → **Resolved:** §4 now says "structural correspondences ... not
   gauge couplings obtained from renormalization-group running".

Non-blocking items also applied: the MeV-scale clarification in the §9 ledger
(scale enters only via the electron-cage identification, shared SF-1/3/4); "within
the CPP ontology" on the §10 macroscopic-shadow paragraph.

Reviewer-attribution note: in this round, the "first paste" relayed to the panel
came through as the v0.4 `.tex` source itself rather than a separate review, so the
v0.4 substantive panel of record is Grok's SHIP plus the adversarial line-by-line
pass. No reviewer verdict was fabricated to fill the gap.

## Summary

| Round | Grok | ChatGPT | Copilot | Net |
|-------|------|---------|---------|-----|
| v0.1  | SHIP-leaning | REVISE | REVISE | REVISE |
| v0.2  | SHIP-leaning | REVISE | ship-leaning | converging |
| v0.3  | SHIP | ship-leaning | ship-leaning | converging |
| v0.4  | SHIP | (relay = .tex) | adversarial: ready after 3 fixes | **SHIP at v1.0** |

Zero physics blockers at any round. Every reviewer independently re-verified the
numbers every round. Convergence basis identical to SF-2/SF-4. The one designed
gate not run: a formal Sonnet hostile pass (available pre-public-deposit).
