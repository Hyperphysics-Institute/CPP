# SF-3 Changelog — Quark Sector Flagship

**Location:** `/CPP/flagship_papers/quarks/documentation_suite/changelog-sf-3.md`
**Paper:** `flagship_papers/quarks/sf-3_quarks.tex`
**Convention:** Canonical version-archaeology record (per `operating_system.md` version-archaeology architecture rule). The `.tex` title block shows only the current version; per-version history lives here.

---

## v1.0 SHIPPED — 14 June 2026 (Session 161, Patch 1505; 1500-band SF-3 window)

**SHIP.** Four review rounds (v0.1–v0.4); Grok SHIP all four; ChatGPT/Copilot REVISE→SHIP convergence; no physics blockers at any round; numbers independently re-verified by every reviewer every round. Thomas delegated the ship call and authorised the registry integration. Final v0.4-panel items folded in before ship:
- **Generation count** "selected by the antipodal-identification mechanism" -> "selected within the SM-8 antipodal-identification model" (abstract, §6, §9, §13.1) — SM-8 gives a model-dependent selection, not a uniqueness proof.
- **Proposition 5.1 nuance (the cycle's most valuable catch):** the phase–m_c independence holds *because* $\alphas$ is taken as the structural value $5/(8\phig)$; were $\alphas$ a running-coupling fit at the charm scale, $m_c$ would re-enter indirectly. Stated explicitly in §5, closing the running-coupling loophole.
- **§4** added: within SM-6/SM-7 these are *structural correspondences*, not RGE-derived gauge couplings.
- **§9** added the MeV-scale clarification (the scale enters only via the electron-cage identification, the same calibration shared across SF-1/3/4).
- **§10** macroscopic-shadow paragraph bounded with "within the CPP ontology" ("fact" -> "claim").

Title block -> **Version 1.0 SHIPPED**. Recompile: 13 pages, 0 errors. All four v0.1–v0.4 review sets archived verbatim under `review/`.

**Ship-time integration (Patch 1506, applied with no other windows active):** OPEN-FP-3-CKM registered in `frontier_sectors/SM.md`; `predictions.md` SF-3 entries + swarm counter; `paper_catalog.md`, `README.md`, `INDEX.md` entries; SF-3 BibTeX added to master `cpp_references.bib`. Proposition 5.1 is a bookkeeping separation, NOT registered as a programme theorem.

**Not done at v1.0 (post-SHIP Phase 7A/7B/7C, deferred):** the 7-file companion documentation suite; programme_orientation/theory-overview/founders_vision/axiom-registry/master_glossary deep updates; anthology chapter; OSF deposit; optional Sonnet hostile pass before public deposit. The inline `thebibliography` is retained in the `.tex` for standalone compilation (master bib now also carries SF-3 for cross-referencing).

---

## Phase 7A documentation suite — 14 June 2026 (Session 161, Patch 1507; 1500-band SF-3 window)

Paper-level Phase 7A delivered: the 7-file companion documentation suite under `documentation_suite/` — `development-SF-3.md` (Tier 3), `glossary-SF-3.md`, `mechanism-SF-3.md`, `phenomena-SF-3.md`, `philosophy-SF-3.md`, `reviews-SF-3.md`, `keywords-SF-3.md` — plus the Tier-2 `transcript-SF-3.md` pointer-map. Tier-4 `reasoning-SF-3.md` + `changelog-sf-3.md` were already in place. **Deferred:** Section B verification *notebook* (.ipynb) — the `.py` verifier `code/1500_verify_sf3_core.py` already passes ALL CHECKS and stands as the verification artifact; the executed-notebook form is a thin remaining 7A item. **Remaining for Phase 7B/7C:** deep theory-doc passes (programme_orientation, theory-overview, axiom-registry, master_glossary, founders_vision, future_projects, problem_histories), the anthology chapter (C13), OSF deposit, the §13.1 wording decision, the optional Sonnet hostile pass, and the H6 final mechanical audit.

---

## Phase 7B sweep + 7C final audit — 14 June 2026 (Session 161, Patch 1509; 1500-band SF-3 window)

**Phase 7B theory-doc sweep** (the program-level orientation docs beyond the 1506 registry integration):
- `programme_orientation.md` — NEW **Chapter 22k** (SF-3 quark-sector synthesis) in Part VI, with the calibration-route adjudication + Prop 5.1 + OPEN-FP-3-CKM body integration; Part VI scope note + last-updated note; scorecard headline UNCHANGED at 108. (Clears the C10 audit FAIL.)
- `theory-overview.md` — SF-3 row added to the flagship results table; SF-line status row → 4 SHIPPED (fixed the prior 4-listed/4-future mismatch).
- `master_glossary.md` — Koide-phase entry extended with the SF-3 phase–mass independence (Prop 5.1); NEW **OPEN-FP-3-CKM** glossary entry.
- `axiom-registry.md` — count-ledger note: axiom set UNCHANGED at 9, no new theorem (Prop 5.1 is bookkeeping), swarm UNCHANGED at 108 (synthesis; inherited predictions).
- `future_projects.md` — SF-3 SHIPPED programme-level note; OPEN-FP-3-CKM flagged as the load-bearing quark-sector forward item.
- `problem_histories/PH-OPEN-FP-3-CKM.md` — NEW problem-history file (per the doc-suite template).

**Phase 7C final audit:** `bash scripts/publication_audit.sh SF-3` → **PUBLICATION AUDIT: PASS** (0 advisory warnings). H2 placeholder scan clean, verification script exits 0, pdflatex compiles, H7 bibliography central-only. **Tooling fix (registered openly per the symmetric-honesty discipline):** the audit's paper-locator used case-sensitive `find -name "${ID}_*.tex"`, which could not match the lowercase flagship filename convention (`sf-3_quarks.tex`) — a latent bug that would mis-fire on every lowercase-named paper (SF-2/SF-4 predate the audit script and were never run through it). Changed to `-iname` for both the `.tex` and fallback-dir locators; this is a general fix, and the SF-3 paper + its 10-file documentation suite were independently confirmed present before and after.

**Protocol status:** Phase 7A complete (1507) + anthology chapter C13 (1508) + Phase 7B theory-doc sweep + Phase 7C audit PASS (1509). **Remaining (Thomas's discretion, non-blocking):** the §13.1 "very small" wording decision; the optional Sonnet hostile pass; the OSF deposit; the thin Section-B verification *notebook* (.ipynb) — the .py verifier already passes.

---

## v0.4 — 14 June 2026 (Session 161, Patch 1504; 1500-band SF-3 window)

**Third review-incorporation pass — over-claim tightening.** Folds the v0.3 panel (verbatim in `review/`, `*_v0.3_*`). **All three returned SHIP again** (ChatGPT SHIP; Grok SHIP; Copilot ready-for-incorporation) — remaining items explicitly stylistic, not scientific. Applied the two genuine over-claim corrections plus one restatement:
- **"forced" -> "selected by the antipodal-identification mechanism"** for the three-generation count (abstract §(iv), §6, §9 ledger, §13.1) (Copilot: SM-8 gives a geometric *mechanism*, not a uniqueness/necessity proof — "forced" overstated it).
- **§4 "One spectral trace gives both the electroweak and the strong coupling"** reframed to "Within the inherited SM-6/SM-7 framework, a single spectral trace supplies both couplings as complementary edge- and face-mode fractions --- a mode-fraction correspondence, not a dynamical unification" (ChatGPT nit A + Copilot over-claim a — bounds the claim to the inherited framework and to a correspondence, not a physical unification).
- **§13 conclusion:** restated that the mass values do not depend on SM-10's still-calibrated chain-network mechanism (its first-principles closure is a mechanism-depth question, not a mass-prediction caveat) (Copilot/ChatGPT).

Recompile: 13 pages, 0 errors. Numbers unchanged. Shared-registry edits still DEFERRED to ship.

**HELD (pending Thomas):** ChatGPT's nit B asks to further soften the §13.1 implausibility-of-accident sentence ("the probability of reproducing them jointly by accident...") — but that is *required* PD-001 §4.1B template content (the implausibility statement). Not auto-applied; folded into the open §13.1 wording decision (which also covers the earlier "astronomically small" -> "very small" softening). **Editorial-only, not applied:** ChatGPT nit C ("hierarchy without hierarchy" appears 2x — deliberate motif); Grok's optional abstract call-out box.

**Status:** three full review rounds, unanimous SHIP each round; nits now exhausted/stylistic. Ready for the ship decision.

---

## v0.3 — 14 June 2026 (Session 161, Patch 1503; 1500-band SF-3 window)

**Second review-incorporation pass — polish to ship-ready.** Folds the v0.2 panel (ChatGPT, Grok, Copilot — verbatim in `review/`, `*_v0.2_*`). **All three returned SHIP** (Grok SHIP; ChatGPT SHIP after 2 wording fixes; Copilot ship-ready after 3 micro-edits). No physics or structural issues found by any reviewer; all numbers re-confirmed. Polish applied:
- **§13 conclusion:** remaining unqualified "the quark Koide phase never depended on $m_c$" -> "in the retained SM-7 isotropic-shift formula, the quark Koide phase does not depend on $m_c$" (ChatGPT — last unbounded instance; the §5/§7 instances were already bounded in v0.2).
- **Acknowledgements:** "performed ... the phase--mass independence argument" -> "identified and documented the phase--mass bookkeeping separation" (ChatGPT — aligns the credit with the Prop 5.1 reframing).
- **§4 bare-partition** sentence clarified ("...unweighted adjacency contributions before propagation-efficiency scaling") (Copilot micro #2).
- **§10** added the physical meaning of $A^3$ ("oriented face-adjacency walks ... colour-flux relays across cage faces") (Copilot micro #3).
- **§4** anchored the adjacency operator dimension ($120\times120$) (Copilot optional).
- **Consistency tidy:** the residual "unification" in the keyword list and the §7 "complementarity layer" softened (Copilot micro #1 was already substantively done in v0.2 §4; this completes it). SF-7 grand-unification proper-name instances retained.
- **§7 boxed adjudication summary** added for panel visibility (Grok suggestion).

Recompile: 13 pages, 0 errors. Numbers unchanged -> verify script still validates. Shared-registry edits still DEFERRED to ship.

**Status:** all three external reviewers at SHIP. Remaining gates before v1.0: optional Sonnet hostile pass; then the ship-time flagged integration patch (OPEN-FP-3-CKM, predictions.md swarm counter, bib migration).

---

## v0.2 — 14 June 2026 (Session 161, Patch 1502; 1500-band SF-3 window)

**Review-incorporation pass.** Folds the v0.1 multi-AI panel (ChatGPT, Grok, Copilot — verbatim in `review/`). Panel verdict: 1 SHIP (Grok), 2 REVISE-then-ship (ChatGPT, Copilot); **no physics blockers** — all three independently re-verified the numerics; every requested change was framing/wording. Changes applied:
- **Over-claim fix:** abstract "complete quark mass spectrum" -> "heavy-quark mass spectrum (strange, charm, bottom, top)" (the cage formula covers the four heavy quarks; light u/d excluded).
- **Proposition 5.1** retitled "Phase–mass separation --- a bookkeeping observation" and explicitly scoped as a bookkeeping separation of inherited SM-7 structure, not a new derivation; §5 now carries the SM-7 provenance pointer (alpha_s and the phase shift come from the adjacency spectrum, not PDG masses) and the amplitude drop-out algebra (A_q cancels from cos theta).
- **m_c qualification:** unqualified "the phase never depended on m_c" -> "in the retained isotropic-shift formula, the phase does not depend on m_c" (§5, §7).
- **Soften "unification":** §4 "electroweak–strong unification" -> "mode complementarity from a single spectral trace --- a shared geometric origin, not a dynamical unification."
- **Mass-scheme caveat** added in §3 (PDG pole/MS-bar scheme affects the comparison, not the calibration).
- **CKM/delta_CP analogy** bounded in abstract + §8 ("limited sense ... a parallel of posture, not an equivalence of difficulty or status").
- **Inherited-structural-choices** sentence added in §7 (7/3, M_0, z*C_F inherited from SM-9/SS-2, not re-tuned); plus explicit "Route A canonical; Route B superseded."
- **Promotional language:** §13.1 "astronomically small" -> "very small." (NB: PD-001 §4.1B template boilerplate uses "astronomically small"; this softening diverges slightly from that template per ChatGPT's adversarial note — flagged for Thomas.)
- **Versioning consistency** (Copilot #4): title now v0.2, changelog header v0.2; the v1.0/v0.1 mentions remaining below are clearly historical.

Recompile: two-pass pdflatex, 12 pages, 0 errors (two benign hyperref PDF-bookmark warnings from `$\S10$` in a heading). Numbers unchanged -> `1500_verify_sf3_core.py` still validates (no new computation; no new verify script needed). Shared-registry edits still DEFERRED to ship.

---

## v0.1 — 14 June 2026 (Session 161, Patches 1500/1501; 1500-band SF-3 window)

First complete pre-review draft. Assembled from the SF-3 structural core (Patch 1308) and outline (Patch 1303) to the 16-section paper-formatting standard. Synthesis/reframing of shipped results — **no new derivation**. (Drafted at Patch 1500 with an over-claiming "v1.0" title-block label; relabelled to v0.1 at Patch 1501 to match the SF-2 drafting precedent, where v1.0 is reserved for the post-review SHIP. No content change.)

**Content established:**
- §3 Zero-parameter heavy-quark mass spectrum, Route A (SM-8/SM-9): $M_q = m_e(z/\phi)V^{7/3}$, top relay $\times z C_F$; RMS 2.1% (s/c/b/t); $m_c$ demoted to derived.
- §4 Strong coupling $\alpha_s = 5/(8\phi)$ as face-mode fraction; exact complementarity $\sin^2\theta_W + \alpha_s = 1/\phi$; ratio $F/E = 5/3$ (SM-7/SM-6).
- §5 Quark Koide phase $\theta_{\rm quark} = 124.04^\circ$ (0.05%); **Proposition 5.1 (phase–mass independence)** — the one in-paper result: phase depends on $\{\alpha_s, \sin^2\theta_W, z\}$ only, so no re-grounding on derived $m_c$ is needed (sharpens the 1303 wording).
- §6 Three generations forced; no fourth quark (SM-8).
- §7 Calibration ledger: Route-A adjudication (single $m_e$; $m_c$ derived).
- §8 OPEN-FP-3-CKM registered in-paper (mixing/quark $CP$ phase undelivered); SF-4-$\delta_{CP}$ parallel.
- §10 §4.1A CP/GP Signature; §11 mapping table; §13 §4.1B Swarm-Validation Contribution + Problem Status.

**Verification:** `code/1500_verify_sf3_core.py` reproduces all numerics from first inputs — ALL CHECKS PASS. Two-pass pdflatex: 11 pages, 0 errors, 0 undefined references.

**Deferred to ship (flagged integration patch, after refresh against origin/main):** OPEN-FP-3-CKM registration in `frontier_sectors/`; `predictions.md` swarm-counter update; bibliography migration from inline `thebibliography` to master `cpp_references.bib`.

**Not yet done:** multi-AI review cycle (CONV-001 panel package); documentation suite companion files; figures (none in v1.0).
