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

---

## Patch 1502 — SF-3 v0.1 -> v0.2 review incorporation (Session 161, 1500-band window)

**Scope.** Fold the v0.1 panel (ChatGPT/Grok/Copilot) into v0.2. Reviews archived verbatim under `review/`. Net panel state: Grok SHIP; ChatGPT + Copilot REVISE-then-ship; zero physics blockers; all three re-verified the numerics independently (ChatGPT recomputed theta_quark = 124.035 deg matching the paper). Every requested change was framing/wording — the physics and all numbers are untouched.

**Triage reasoning.** The three reviews converged tightly, which made triage clean. I treated the union of their requests as the change set rather than litigating verdict labels, because the requests were mutually compatible and each was individually correct:
- The "complete quark mass spectrum" -> "heavy-quark" fix (Copilot) is a genuine over-claim correction: the V^(7/3) cage formula in §3 covers s/c/b/t only; light u/d are explicitly out of scope. I had carried "complete" into the abstract from loose drafting. Fixed.
- The Prop 5.1 reframing (ChatGPT "bookkeeping lemma" + Copilot "SM-7 provenance pointer" + Grok "self-contained algebra") is the substantive one. All three are really one concern: as written, Prop 5.1 could read as a *new* result and asserts the m_c-independence rather than showing it. I (a) retitled it a bookkeeping separation, (b) added the SM-7 provenance sentence (alpha_s and the shift come from the adjacency spectrum, not a fit to PDG-extracted phase — which is the actual loophole Copilot identified: indirect m_c dependence via fitting), and (c) added the amplitude algebra (A_q is an overall Koide scale, cancels from the cos-theta ratio). This is the right fix: it keeps the proposition but makes it honest and self-contained.
- The m_c qualification (ChatGPT) is correct and cheap: "never depended on m_c" overstates; "in the retained isotropic-shift formula, the phase does not depend on m_c" is the bounded, defensible claim. The unbounded version invited exactly the SM-7-provenance objection Copilot raised.
- Softening "unification" -> "mode complementarity / shared geometric origin" (Copilot) is correct discipline: a shared spectral partition is not a dynamical unification, and the SF-line should reserve "unification" for SF-7's actual cross-sector consistency machinery.
- The mass-scheme caveat (ChatGPT/Copilot) and the inherited-structural-choices sentence (Copilot/Grok) both head off "hidden parameter" objections without conceding anything — the calibration really is single-m_e; the caveats just make the boundary explicit.
- The CKM/delta_CP bounding (ChatGPT/Grok) prevents the analogy from reading as an equivalence of status. Posture-parallel, not difficulty-parallel.

**One judgment call flagged.** ChatGPT asked to replace "astronomically small" in §13.1. That phrase is actually PD-001 §4.1B template boilerplate for the Swarm-Validation Contribution. I softened it to "very small" for this external-facing draft but flagged the divergence from the template to Thomas rather than silently overriding a programme convention — his call whether to keep the softening or restore the template wording.

**No registry touches.** All edits inside this window's own files (sf-3_quarks.tex, changelog, this file, review/). OPEN-FP-3-CKM + predictions.md swarm counter + bib migration still deferred to the ship-time flagged integration patch.

**Next.** Cycle has Copilot/Grok/ChatGPT done; the remaining gate before SHIP is a Sonnet hostile pass (prompted via Claude) if Thomas wants it, then v0.2 -> ship. At ship: the deferred integration patch (refresh against origin/main first).
