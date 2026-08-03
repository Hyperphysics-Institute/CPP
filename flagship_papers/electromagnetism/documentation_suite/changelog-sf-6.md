# Changelog — SF-6 (sf-6_electromagnetism.tex)

Canonical filename `sf-6_electromagnetism.tex` (no version suffix). Version lives in the title block; history here (per the OS version-archaeology rule — no CHANGELOG block in the `.tex`).

## v1.0.1 — 2 August 2026 (Patch 2954) — terminology only, no physics moved
- Founder ruling (registered Patch 2953 §1–§2): the "ZDC / Zero-point Dipole Chain" acronym is retired; it is NOT entered in the master glossary. Synonymy determination: ZDC named a CHAIN of ZBW-oscillating dipoles, not the ZBW oscillation itself, so the rewrite uses ZBW-rooted "ZBW chain" language rather than a blind ZDC→ZBW substitution.
- `.tex`: macro `\ZDC` renamed `\ZBWC` (renders "ZBW-chain"; 39 sites); Definition retitled "ZBW chain"; §2 heading, abstract, and keywords rephrased; internal labels eq:massZDC/eq:photonZDC renamed (no rendered change). Physics content, equations, tier labels, and open-problem registrations untouched.
- documentation_suite/glossary-SF-6.md: four entries reworded to ZBW-chain vocabulary with the retirement noted.
- Recompile pending founder-side (mechanical); expected 15 pp, 0 undefined refs as at v1.0.

## v1.0 SHIPPED — 21 June 2026 (Patch 1607)
- SHIP on unanimous-advance panel: Grok SHIP, Gemini SHIP, Copilot advance-no-restate, ChatGPT accept-v0.3-to-v1.0 (cycle-2 confirm pass, SCRIPT-EXECUTED, no verdict-flipping objections remaining).
- Two final wording edits (editorial; no physics moved):
  1. Plain Language Summary: "the unification of mass and light is solid" → "…is the companion-grade CPP core identification" (ChatGPT: "solid" too strong).
  2. §9: "candidate escape" → "an unproven research direction explicitly not a resolution sketch" (ChatGPT).
- Version 0.3 → 1.0 SHIPPED. Compiles clean: 15 pp, 0 undefined refs. 1600/1602 verifiers all-pass (unchanged).

## v0.3 — 21 June 2026 (Patch 1606) — review cycle 1 restate
- 4-reviewer panel (ChatGPT, Grok, Gemini, Copilot); 2/4 SCRIPT-EXECUTED (Grok, ChatGPT), all Tier-1 identities pass. Tally: 3 SHIP / 1 restate.
- Convergent finding (T2): the E=ℏν_C unification is a definitional/ontological IDENTIFICATION, not a derivation; the v0.2 "derived / most rigorous result" language overclaimed. Restated throughout (abstract, §1 box, §3) as a companion-grade substrate-level identification / ontological reduction; §3 gains explicit honesty points (the ν_C assignments match standard Compton/Planck–Einstein relations; the dispersion is imported from SR-1; "no new postulates" = "beyond the companion framework").
- T3: Michelson–Morley named as a flagship-level open falsifier; SSV-independent-Z₀ marked a research direction, not a resolution.
- Calibrations: §1 boxed warning ("SF-6 does not derive μ0,ε0,c,γ(v), or the MM null from first principles"); §4 Tier-2 value reminder; data-availability "algebraic consistency identities, not first-principles derivations"; §3 c06 nucleation-center cross-ref.

## v0.2 — 21 June 2026 (Patch 1602)
- OPEN-FP-6-EMHAND re-scoped: substrate manifestation (iii) is already closed (THEO-SD-CHIR-2 / THEO-CHIR-CONT-3); SF-6 owes only the EM-phenomenology expression, constrained by the parity obstruction (P-even EM expresses, cannot source, P-odd handedness).
- TP-1 consistency thread added (§6 + §12): the traveling-ZDC photon = TP-1's cuttable DP-Sea disturbance; QM-5 second quantization; intrinsic band top ω_max=2√3/t_P (λ_max=z=12). Bundled `code/1602_verify_bandtop.py`.

## v0.1 (pre-review draft) — 21 June 2026 (Patch 1600)
- First .tex assembly to the 16-section apex standard, mirroring SF-3. 13 sections + appendix; synthesis/reframing, NO new derivation.
- Spine: c06 (E=ℏν_C; standing/traveling ZDC; Z₀; emission/absorption; lensing) + DP-Sea-Polarization-Model (Tier-2 μ0,ε0,c,γ(v)) + SR-1 + QM-1..6 + EW-1.
- Two-tier rigor stated plainly; two inherited-opens (OPEN-FP-6-CONSTANTS, OPEN-FP-6-EMHAND); Michelson–Morley tension carried. Bundled `code/1600_verify_sf6_core.py` + `reasoning/1600.md`.

## Pre-assembly staging
- README source-map correction: Patch 1601 (EW-3/EW-5 → c06 + DP-Sea spine).
- Structural core: `sketches/SF-6_structural_core.md` (Patch 1310).
- Outline: `sf-6_outline.md` (Patch 1305).

## Patch register
| Patch | Version | Scope |
|-------|---------|-------|
| 1600 | v0.1 | .tex assembly + verifier + reasoning |
| 1601 | — | README source-map correction |
| 1602 | v0.2 | EMHAND re-scope + TP-1 consistency |
| 1603 | — | review package (cycle open) |
| 1605 | — | review cycle 1 aggregation |
| 1606 | v0.3 | restate (T2 relabel + T3 falsifier) |
| 1607 | v1.0 | SHIP (2 wording edits) |
| 1608 | v1.0 | Phase 7 doc suite + .tex CHANGELOG-block removal |
