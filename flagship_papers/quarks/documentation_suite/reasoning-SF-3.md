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

---

## Patch 1503 — SF-3 v0.2 -> v0.3 polish (all reviewers SHIP) (Session 161, 1500-band window)

**Scope.** Fold the v0.2 panel into v0.3. All three reviewers returned SHIP (Grok unconditional; ChatGPT SHIP-after-2-wording-fixes; Copilot ship-ready-after-3-micro-edits), and all three explicitly re-checked the numerics and the inheritance chain and found no physics or structural issues. So v0.3 is pure polish — no physics, no number changes.

**Triage.** Light-touch; I applied the union again. Two items were genuine remaining instances rather than new asks:
- ChatGPT caught that the §13 conclusion still carried the *unqualified* "never depended on m_c" — I had only bounded the §5 and §7 instances in v0.2. Fixed the conclusion to match. This is the kind of thing that's easy to miss when you bound a phrase in two places but not the third; worth noting for future passes (grep the whole file for the phrase, not just the section you're editing).
- ChatGPT's acknowledgements reword is right: "performed the phase-mass independence argument" reads like a new derivation, which is exactly what we spent v0.2 establishing it is NOT. "Identified and documented the phase-mass bookkeeping separation" matches the Prop 5.1 reframing.

Copilot's three were clean clarifications (bare-partition gloss, A^3 physical meaning, 120x120 adjacency anchor) — all cheap, all improve a non-expert reader's footing, none change a claim. Copilot's micro-edit #1 ("remove unification in §4") was already done in v0.2 (the v0.2 §4 sentence reads "mode complementarity ... not a dynamical unification"); Copilot's fetch was stale there. I still completed the consistency tidy by softening the residual keyword and the §7 "complementarity layer," so no bare "unification" remains except the SF-7 grand-unification proper name.

Grok's only suggestion was a boxed §7 adjudication summary for panel visibility — added as a one-box mdframed. Good call: the calibration adjudication is the paper's headline move and now it's visually unmissable.

**State.** v0.3 is at three-reviewer SHIP. The remaining cycle gate is Sonnet (hostile/adversarial, prompted via Claude); after that, or if Thomas elects to ship on the three-reviewer convergence, v0.3 -> v1.0 SHIP carries the deferred integration patch (OPEN-FP-3-CKM registration in frontier_sectors/, predictions.md swarm-counter bump, inline-bib -> master cpp_references.bib migration), applied after a refresh against origin/main. I did NOT bump to v1.0 here — that's the ship decision, Thomas's to make.

---

## Patch 1504 — SF-3 v0.3 -> v0.4 over-claim tightening (Session 161, 1500-band window)

**Scope.** Fold the v0.3 panel into v0.4. Third consecutive unanimous SHIP (ChatGPT, Grok, Copilot). The reviewers explicitly classed the remaining items as stylistic, but two are genuine epistemic-honesty fixes worth making, and I made them:

1. **"forced" -> "selected by the antipodal-identification mechanism."** Copilot's catch is correct and matters for the programme's swarm-validation posture: SM-8 supplies a geometric *mechanism* (antipodal identification) for three generations, but does not prove uniqueness/necessity. Calling the count "forced" claims a proof we don't have. "Selected by the mechanism" is the honest verb. Changed all four instances (abstract, §6, §9, §13.1). This is exactly the kind of word that, left unfixed, hands a hostile referee a free "they overstate their results" point — cheap to fix, real to leave.
2. **"One spectral trace gives both couplings" -> bounded mode-fraction correspondence.** Two reviewers flagged it. SM-7 frames the shared adjacency origin as a mode-fraction correspondence, not a physical unification; the bold declarative overstated relative to the source. Reframed to "within the inherited SM-6/SM-7 framework ... a mode-fraction correspondence, not a dynamical unification." Keeps the content, drops the overreach.
3. SM-10-not-used reminder restated in the conclusion (cheap, requested).

**One item deliberately HELD, not silently applied.** ChatGPT asked to further soften the §13.1 "probability of reproducing them jointly by accident" sentence. That sentence is *required* content under PD-001 §4.1B (every paper must carry the implausibility-of-accident statement with the (band/space)^N scaling). I already softened "astronomically small" -> "very small" in v0.2 and flagged the template divergence to Thomas. Softening it further toward ChatGPT's "apparent joint explanatory burden" phrasing would erode a mandated element. So I held it and folded it into the standing §13.1 wording decision for Thomas rather than unilaterally neutering template content on an adversary's say-so. This is the right boundary: incorporate reviewer fixes that improve honesty; do not let an adversarial reviewer talk me out of a required programme element without the maintainer's call.

**Convergence note.** Three review rounds, unanimous SHIP each round, nits now exhausted. Continuing to spin v0.5, v0.6 ... on progressively smaller stylistic nits would be diminishing returns and risks over-fitting to reviewer taste. My recommendation to Thomas is to converge: either run the Sonnet hostile pass (the one remaining designed gate) or ship v0.4 -> v1.0 with the deferred integration patch. I did NOT bump to v1.0; the ship decision is Thomas's.

---

## Patch 1505 — SF-3 v0.4 -> v1.0 SHIP (Session 161, 1500-band window)

**Decision.** Thomas delegated the ship call ("send to v1.0 if you think we are ready") and authorised the registry integration ("update all delayed files; no other windows active"). My honest assessment: ready. Four review rounds, Grok SHIP all four, ChatGPT/Copilot converged REVISE->SHIP, no physics blocker at any round, numbers independently re-verified every round. The v0.4 adversarial pass still surfaced three small framing items, but all were honesty/scoping refinements (not physics), and I folded them in before shipping rather than shipping over them.

**The one item I want on record as the cycle's most valuable catch:** the v0.4 reviewer noted that Proposition 5.1's m_c-independence is *conditional on alpha_s being the structural value 5/(8 phi)* — if alpha_s were instead a running-coupling fit at the charm scale, m_c would re-enter indirectly. This is correct and it is exactly the kind of hidden conditional a hostile referee lives for. SF-3 does adopt the structural alpha_s, so the proposition holds, but the unstated version invited the objection. Now stated explicitly in §5. This is the difference between a proposition that is true and a proposition that is *defensibly* true, and it is the single best thing the review cycle produced.

**On "selected within the SM-8 antipodal-identification model."** This is the fourth progressive weakening of the generation-count verb across the cycle: "forced" (v0.1) -> "selected by the mechanism" (v0.4) -> "selected within the SM-8 model" (v1.0). Each step traded a sliver of rhetorical force for a sliver of honesty, and each was right: SM-8 supplies a model-dependent selection, not a theorem of uniqueness. The final phrasing is the one I'd defend to a skeptic.

**On NOT shipping over the items / NOT over-iterating.** I held the line in both directions this cycle: I refused to further soften the §13.1 implausibility statement (required PD-001 template content) on an adversary's say-so without Thomas's call, and I refused to keep spinning versions on shrinking stylistic nits. v1.0 is the right stopping point: the substantive feedback is exhausted, and the remaining reviewer suggestions (abstract call-out box, SM-7 appendix) are taste, not correctness.

**Proposition 5.1 is NOT a programme theorem.** It is a bookkeeping separation of inherited SM-7 structure. It does not enter theorem-registry.md. The integration patch registers only OPEN-FP-3-CKM (a genuine open problem) and the SF-3 predictions.

**Sonnet gate.** The designed cycle ends Opus -> Copilot -> Grok -> Sonnet -> Opus. A formal Sonnet hostile pass was not run; I flagged this to Thomas. For the repo-internal v1.0 SHIP state, four-round multi-reviewer convergence is the same bar SF-2/SF-4 shipped on. A Sonnet pass remains available before public OSF/arXiv deposit.

## Patch 1506 — SF-3 v1.0 ship-time registry integration (Session 161, 1500-band window)

Executed with no other windows active (Thomas confirmed), so the shared-registry edits apply immediately without serialization risk. Registered OPEN-FP-3-CKM (frontier), SF-3 predictions + swarm-counter bump, paper_catalog/README/INDEX entries, and the SF-3 master-bib entry. This is the "flagged integration patch" promised throughout the cycle; collision exposure was the reason it was deferred, and it is now safe precisely because Thomas serialized to this one window.
