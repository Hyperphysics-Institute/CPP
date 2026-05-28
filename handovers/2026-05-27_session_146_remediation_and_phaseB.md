[ ] STEP 0 (BLOCKING): `git clone https://github.com/Hyperphysics-Institute/CPP.git` + `grep -n "THEO-DSL" theorem-registry.md` + `ls series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/hardened_theorems/`. Do NOT register an identifier, place a file, or compute a coefficient until done. Skipping this is what broke Session 146.

# F.1 / DSL Handover — Session 146 Close (Remediation + Phase-B grounding)

**Repository state:** origin/main through Patch 0612 (Session 146 remediation arc 0610–0612).
**Active paper:** F.1 Dynamical Substrate Law (DSL). v1.0 SHIPPED (Patch 0570). Active sub-trajectory: OPEN-FP-F1-5 Sequence-2A — edge-aligned coefficient closure → reserved THEO-DSL-7.

## One-paragraph state
Session 146's legitimate Sequence-1 work (THEO-DSL-6/-8 structural, Patches 0596–0598) was followed by a misgrounded attempt at the edge-aligned O(δ²) coefficient: five patches (0605–0607) built from chat framing without cloning, with THEO-DSL identifier collisions, duplication, and a wrong top-level directory. The remediation arc reverted all of it (Patch 0610, restoring the exact pre-session state) while keeping + fixing a new reasoning-capture protocol, then re-established the edge-α₂ trajectory the right way (Patch 0611): every imported input verified against the registered primitives before any value was trusted. The cross-shell constants are confirmed (S1→S2=φ/2, S1→S3=φ²/2 — the latter vindicating the reverted constant and withdrawing an over-cautious Phase-R flag); the primitive layer + edge α₁ are complete. The actual α₂ closure was deliberately NOT shipped: it is a 2D vector path-class assembly the vertex machinery does not give directly, and the reverted positive values are sign-suspicious against the negative vertex α₂=−9/φ². The genuine new physics — THEO-DSL-7's coefficients — is the single open item, now correctly set up.

## Forward queue
**Priority 1:** Compute edge-aligned α₂ (THEO-DSL-7 candidate). File `hardened_theorems/o_delta_two_edge_aligned_coefficient.tex`; sketch Layer 3 under (H5_E); cite THEO-DSL-6 + G1_E/G1_E.2/G2_E/G2_E.3 + edge α₁. **Cross-check: reproduce vertex α₂=−9/φ² with the same 2D machinery FIRST.** Do NOT trust the reverted 9/(2φ), 9φ−12.
**Priority 2:** Sequence-2B face-aligned coefficients → THEO-DSL-9 (after 2A).
**Anti-priorities:** Do NOT attempt the closure without the clone + registry grep. Do NOT reuse a THEO-DSL number without checking the reserved table.

## Where to find detail
- **Session log:** `session_logs/2026-05-27_session_146_log.md`
- **Tier 4 reasoning:** `.../dynamical_substrate_law/documentation_suite/reasoning-dynamical-substrate-law.md` §"Session 146 … Remediation"
- **Setup + verified inputs:** `.../dynamical_substrate_law/sketches/F1_reading_C_edge_aligned_coefficient_scoping.md` §14
- **Verify scripts:** `.../dynamical_substrate_law/code/verify_edge_alpha2_inputs.py`, `code/verify_edge_crossshell_constants.py`
- **Protocol:** `templates/reasoning_capture_protocol.md`; wired in `bootup.md` §1 (Step-1 read list) + §3 (patch-contract rider)
- **Frontier:** `frontier_sectors/FP.md` §OPEN-FP-F1-5 (Sequence-2A grounding status)

## Step A–H Completion Audit
- **Step A (Tier 1 session log):** ✓ — `session_logs/2026-05-27_session_146_log.md` created (Phases R/B/H).
- **Step B (Tier 2 transcript):** ✓ — Session 146 remediation block appended to `documentation_suite/transcript-dynamical-substrate-law.md` (Patches 0610–0612).
- **Step C (Tier 3 vignette):** ✓ — vignette appended to `documentation_suite/development-dynamical-substrate-law.md` (substantive DSL reasoning occurred).
- **Step D (Tier 4 reasoning):** ✓ — canonical entry appended to `documentation_suite/reasoning-dynamical-substrate-law.md`.
- **Step E (per-registry audit):**
  - research_frontier (`frontier_sectors/FP.md`): ✓ — Sequence-2A grounding status added to OPEN-FP-F1-5.
  - theorem-registry: N/A — no theorem edits; THEO-DSL-7 remains correctly reserved (verified live).
  - axiom-registry: N/A — no axioms/predictions changed.
  - predictions: N/A. master_glossary: N/A — no new terms. paper_catalog: N/A — status unchanged.
  - organizational_frontier: N/A — no new OPEN-ORG items.
  - problem_histories: N/A. methods_catalogue: N/A — the "verify-inputs-before-closure / clone-first" discipline is a workflow pattern (operating_system/protocol scope), not a physics-derivation method.
- **Step F (reviewer artifacts):** N/A — no review content this session.
- **Step G (protocol / OS updates):** ✓ — reasoning-capture protocol fixed (Patch 0610) + wired into `bootup.md` §1/§3 (Patch 0612); line-1 BLOCKING clone gate adopted for all handovers.
- **Step H (handover document):** ✓ — this file, at canonical `handovers/` location with line-1 clone gate.

## Quick start (next session)
Clone (line 1). `grep "THEO-DSL" theorem-registry.md`. Read this handover + scoping §14 + the Tier 4 entry. Then compute edge α₂, vertex-cross-check first, capture reasoning+script per protocol, register THEO-DSL-7 candidate.
