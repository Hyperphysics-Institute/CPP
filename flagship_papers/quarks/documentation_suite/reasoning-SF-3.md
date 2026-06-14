# SF-3 — Tier-4 Reasoning Capture

**Location:** `/CPP/flagship_papers/quarks/documentation_suite/reasoning-SF-3.md`
**Convention:** Append-only verbatim reasoning across the SF-3 development arc (four-tier documentation discipline; reasoning-capture protocol bound to the patch contract). Newest entries appended at the bottom.

---

## Patch 1500 — SF-3 v1.0 `.tex` assembly (Session 161, 1500-band window)

**Scope.** First substantive SF-3 patch: assemble `sf-3_quarks.tex` v1.0 from the verified structural core (1308) + outline (1303), to the 16-section paper-formatting standard. Reframing of shipped SM-7/8/9/10 + SS-1/2 + SM-6; **no new derivation**.

**Band decision.** SF-3 was assigned the **1500–1599** band by Thomas at session open. This was the collision-safe choice: the SF-7 grand-unification window owns 1300–1399 (consumed through 1313 and still open as the integration seat), and the SF-1 charged-leptons window owns 1400–1499 (dispatched 14 Jun, 1400 consumed). 1500–1599 was unclaimed by any of the six live windows. Patch 1500 is the first in-band label.

**Calibration adjudication carried into the paper.** The load-bearing drafting decision is not new physics but adjudicating SM-8 (Route A, zero-param, predicts m_c) vs SM-7 (Route B, Koide + fitted m_c). The structural core (1308) sharpened the 1303 recommendation: because SM-8 *predicts* m_c at −1.6%, the SM-7 m_c calibration is redundant, so m_c is demoted from calibration to derived, restoring the single-m_e headline. I made Proposition 5.1 (phase–mass independence) the explicit vehicle for the 1308 sharpening: θ_quark is a function of {α_s, sin²θ_W, z} only, so the "re-ground the phase on derived m_c" step the 1303 outline proposed is provably unnecessary. This is the one place the paper states a small result (a proposition) rather than pure reframing, and it is what lets the single-m_e claim be made cleanly.

**Why Route A despite worse b/t residuals.** Route B gives ~0.3% better b/t. I kept Route A canonical anyway because the SF-7 unification spine needs *one* calibration across leptons (SF-1), neutrinos (SF-4), and quarks (SF-3); a second calibration for a sub-percent accuracy gain would break the "hierarchy without hierarchy" headline that SF-7 §9's master table commits to. The honest trade is stated openly in §7.

**CKM kept honestly open.** No CKM derivation exists anywhere in the corpus (SM-10 is the FEM scaling-mechanism paper, not a mixing paper). Registered OPEN-FP-3-CKM in-paper as an `openproblem` environment and framed it as the structural analog of SF-4's open δ_CP — the uniform "masses derived, mixing-sector open" posture across fermion flagships. Deliberately did NOT touch any shared registry: OPEN-FP-3-CKM registration in `frontier_sectors/` + the predictions.md swarm-counter bump are deferred to ship time via a flagged integration patch (collision discipline).

**Numerics.** Every number in the paper was reproduced from first inputs (m_e, z, φ, C_F) by `code/1500_verify_sf3_core.py` before drafting and again after: M0 = 3.79 MeV; masses 96.3 / 1249 / 4115 / 169,570 MeV at RMS 2.11%; α_s = 5/(8φ) = 0.3863; sin²θ_W + α_s = 1/φ exactly; ratio = F/E = 5/3; θ_quark = 124.04° (−0.04% vs PDG 124.09°). All checks PASS.

**Compile.** Two-pass pdflatex: 11 pages, 0 errors, 0 undefined references. Used inline `thebibliography` (allowed alternative) for standalone v1 compilation; migration to the master `cpp_references.bib` is a ship-time task. Renamed a paper macro `\deg`→`\dgr` to avoid clobbering LaTeX's predefined `\deg` operator.

**Format compliance.** 16-section standard followed: minimal source-header (no inline CHANGELOG block — points to `changelog-sf-3.md`); clean title block (no version-history paragraph); abstract + keywords + plain-language summary + raggedright + TOC; §Open Problems Addressed in the intro; §Physical Interpretation with the required §4.1A CP/GP Signature subsection (load-bearing axioms / visible-vs-smoothed discreteness / macroscopic shadow); §CPP-to-Conventional-Physics Mapping table; §Conclusion with the required §4.1B Swarm-Validation Contribution + Problem Status subsections.

**Forward (next phase, Thomas-driven).** v1.0 → review: produce the CONV-001 single-block panel package for ChatGPT/Grok/Copilot; incorporate review; at ship, register OPEN-FP-3-CKM + bump predictions.md swarm counter via a flagged integration patch (refresh against origin/main first). Estimated 5–7 sessions to ship per the outline.
