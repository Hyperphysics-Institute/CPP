[ ] STEP 0 (BLOCKING): git clone the repo + `grep -n "THEO-DSL" theorem-registry.md`. Do NOT proceed to any physics/registration/Phase-B work until done. This handover exists because skipping the clone is exactly what broke Session 146.

# REMEDIATION PLAN — Session 146 DSL misgrounding cleanup

WRITTEN: 2026-05-27, Session 146, after clone-based diagnosis.
PURPOSE: overflow-survival recovery state. If the context window breaks
mid-remediation, a fresh instance reads THIS FILE + /home/claude/REMEDIATION/
snapshots/ and continues with zero reconstruction.

================================================================================
## STEP 0 — BLOCKING PRECONDITION (the root-cause fix)
================================================================================
Before ANY work: clone the repo.
    cd /home/claude && rm -rf CPP && git clone --depth 1 \
      https://github.com/Hyperphysics-Institute/CPP.git
The entire Session-146 failure happened because this was skipped and work
proceeded from chat-prompt framing + conversation_search instead of ground
truth. NEVER claim a THEO-DSL identifier or a file location without grepping
the live theorem-registry.md and listing the live DSL folder first.

================================================================================
## DSL = "Dynamical Substrate Law"  (definitive; answers the open slot)
================================================================================
THEO-DSL-N = Theorem, Dynamical Substrate Law, N. The F.1 arc.
Canonical home: series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/

================================================================================
## GROUND TRUTH — the real THEO-DSL registry structure
================================================================================
Three Reading-C orientation variants, each with STRUCTURAL + COEFFICIENT slots:

  vertex-aligned   I_h   1D    structural THEO-DSL-4 (P0585)
                               coeff      THEO-DSL-3 (alpha_1 = 6/phi^2)
                                          THEO-DSL-5 (alpha_2 = -9/phi^2, P0591/0592)
  edge-aligned     D_5   2D    structural THEO-DSL-6 (P0596)
                               coeff      THEO-DSL-7  <-- RESERVED, Sequence-2A, OPEN
  face-aligned     C_s   3D    structural THEO-DSL-8 (P0597)
                               coeff      THEO-DSL-9  <-- RESERVED, Sequence-2B, OPEN

Real DSL artifacts live in:
  series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/hardened_theorems/
Geometric primitives for edge-aligned Sequence-2A already landed there:
  G1_E   (P0601) first_shell_d5_orbit_projections.tex
  G1_E.2 (P0602) first_shell_first_shell_edge_d5_orbits.tex
  G2_E   (P0603) second_shell_projection_d5_orbits.tex   [check exact name]
  G2_E.3 (P0604) cross_shell_edge_d5_orbits.tex
Edge-aligned O(delta^1) coeff ALREADY done:
  o_delta_one_edge_aligned_coefficient.tex
    -> alpha_1^(rho)  = 4/phi^2     ~ 1.528   (NOT 3/phi^3 — I mis-cited that)
    -> alpha_1^(edge) = 2(2+phi)    ~ 7.236
Edge-aligned O(delta^2) coeff: NOT yet present -> this is the genuine new work.

================================================================================
## WHAT WENT WRONG (the five Session-146 patches, all misgrounded)
================================================================================
All five landed in a NEW top-level hardened_theorems/ that did not exist before
(wrong directory — real work is in the DSL subfolder).

  P0605  edge_aligned_second_order_alpha2.tex
         = edge-aligned alpha_2. CORRECTLY CONCEIVED (this is the THEO-DSL-7 /
         Sequence-2A target). BUT derivation suspect: my inline lemma used
         cross-shell additive constant +phi^2/2; the registered G2_E.3 primitive
         (P0604) uses +phi/2 for S1->S2 onto n_edge. My "extra factor of phi"
         justification contradicts the primitive. Values claimed:
            alpha_2^rho  = 9/(2 phi) ~ +2.7812
            alpha_2^edge = 9 phi - 12 ~ +2.5623
         STATUS: UNVERIFIED. Must re-derive against G2_E.3 in Phase B.
  P0605a edge_aligned_o_delta_squared_closure.tex  ("THEO-DSL-7 umbrella")
         identifier semantically ~right (edge coeff) but miscited structural as
         "P0600" (really THEO-DSL-6 / P0596). Redundant with P0605.
  P0606  vertex_aligned_invariant_subspace_structural.tex
         DUPLICATE of THEO-DSL-4 (vertex 1D structural) + THEO-DSL-3 (6/phi^2).
         Vertex first-order was NEVER missing. Pure redundancy. DISCARD.
  P0606a vertex_aligned_o_delta_squared_closure.tex  ("THEO-DSL-8")
         COLLIDES with registered THEO-DSL-8 (face-aligned structural). Content
         redundant (vertex closure = DSL-3/4/5). DISCARD.
  P0607  o_delta_squared_orientation_phase_diagram.tex  ("THEO-DSL-9")
         COLLIDES with reserved THEO-DSL-9 (face coeff). "Complete phase diagram"
         OMITTED the face-aligned 3D variant entirely. DISCARD (or rebuild later
         as a genuine 3-variant phase-diagram doc under a FREE number, post-DSL-9).

Protocol patches (KEEP, in templates/, correctly located):
  P0608  reasoning_capture_protocol.md + build_reasoning.sh   -> FIX, don't revert
  P0609  hardened_theorems/reasoning/*.md + scripts/*.py        -> revert WITH the
         top-level dir (they document reverted work); snapshots in /tmp preserve them.

================================================================================
## PHASE R (cleanup, low-risk) — do FIRST, leaves repo clean even if B overflows
================================================================================
1. Delete entire top-level hardened_theorems/ (5 .tex + reasoning/ + scripts/).
   It did not exist pre-session; this restores hardened_theorems to DSL-subfolder-only.
2. Fix templates/reasoning_capture_protocol.md:
   - §7: fill DSL = Dynamical Substrate Law.
   - §6: correct bucketing — DSL reasoning lives in the DSL subfolder
     (series_umbrella/.../dynamical_substrate_law/hardened_theorems/reasoning/),
     NOT top-level hardened_theorems/reasoning/.
   - add a STEP-0 clone-precondition note + handover-gate rule.
3. Fix templates/build_reasoning.sh example path to the DSL subfolder.
4. theorem-registry.md: I NEVER edited it this session -> nothing to revert there.
   DSL-7/8/9 remain as the registry intends (7 reserved, 8 face-structural,
   9 reserved). Good.
5. Ship Phase R as ONE patch. Repo is then clean + correct.

================================================================================
## PHASE B (re-derivation, real physics, separate turn) — survives window break
================================================================================
Rebuild ONLY edge-aligned alpha_2 as the genuine THEO-DSL-7 coefficient:
  - LOCATION: series_umbrella/.../dynamical_substrate_law/hardened_theorems/
              o_delta_two_edge_aligned_coefficient.tex   (parallels o_delta_one_)
  - VERIFY FIRST: re-derive the cross-shell projection constant against G2_E.3
    (cross_shell_edge_d5_orbits.tex). Establish whether the S1->S3 constant is
    +phi/2, +phi^2/2, or other, from the registered primitive — do NOT trust the
    P0605 value.
  - CITE: THEO-DSL-6 (structural, the 2D subspace) + G1_E/G1_E.2/G2_E/G2_E.3
    primitives + edge alpha_1 (4/phi^2, 2(2+phi)).
  - REGISTER: as THEO-DSL-7 (candidate) coefficient entry, sketch Layer 3 under
    (H5_E), per the registry's stated plan.
  - Capture reasoning fragment + verify script IN THE DSL SUBFOLDER per the
    (now-corrected) reasoning-capture protocol.
  - Vertex + face work: NONE NEEDED (vertex = DSL-3/4/5 done; face structural =
    DSL-8 done; face coeff = DSL-9 future Sequence-2B, out of scope).

================================================================================
## HANDOVER GATE (root-cause fix for the skipped-clone problem)
================================================================================
Every handover doc this programme generates MUST open with, as line 1, an
unchecked BLOCKING gate:
  [ ] STEP 0 (BLOCKING): git clone the repo; do not proceed until done.
Rationale: instances follow the in-context handover over the general bootup.md,
so the precondition must live IN the handover, not only the bootup.
