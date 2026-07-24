# AUTOMATON-1 EXECUTION RECORD (appended per leg; frozen 2796 prereg)

## LEG 1 — VALIDATION GATES: V-3 PASS, V-1 FAIL-STOP (Patch 2797)

**Executed 2026-07-24. Engine: `code/2797_automaton1_engine.py` (the
frozen Moment rule + DR-1..DR-3; FFT shell-convolution relay; DR-3
self-parcel exclusion verified structural — the shell band excludes
distance 0, so no GP ever receives its own transmission).
Reasoning: `reasoning/2797.md`.**

**V-3 (shell isotropy): PASS** — dipole-moment axis anisotropy 0.00%
at R ∈ {2, 3, 4} (|S| = 62/98/210; exact by cubic symmetry).

**V-1 (static field law): FAIL as frozen — production BLOCKED per
the prereg's own clause ("DR-1 is inadequate; STOP and
re-prereg").** Frozen procedure (pinned ± dipole, M = 32, R = 3,
window r ∈ [2R, M/3]): p = 2.683 vs band [1.8, 2.2].

**V-2: not reached** (V-1 blocks in execution order).

**Diagnostic appendix (same-font; measurements only, no re-freeze
tonight):**
1. Excluding the window's lower-edge point (r = 6 = 2R exactly):
   p = 1.988 over [7, 10] — the frozen window included its own
   near-field boundary point (the X4 window-edge lesson, recurring
   at design time).
2. The frozen configuration pins a DIPOLE and demands monopole
   scaling — the − partner's cancellation steepens large-r decay by
   construction (M = 48 wide-window: p = 2.219).
3. Single-charge jellium redesign (principled monopole): p = 2.31 —
   2.47, with LOCAL slope RISING toward the cell midplane (2.14 →
   2.35 → 2.64) — the signature of the torus itself (the field must
   vanish at M/2 by symmetry), afflicting ANY field including exact
   Coulomb.
4. Comparative-gate concept (automaton vs exact lattice Coulomb on
   identical torus/window): the quick Fourier comparator produced
   implausible exact-Coulomb slopes (local p = 0.72 near free-space
   conditions) and is itself SUSPECT — a verified real-space
   Ewald-sum comparator is required before any comparative band can
   be frozen.

**Disposition:** V-1's frozen design conflated three separable
effects (near-field edge point; dipole vs monopole scaling; torus
midplane steepening). Whether DR-1's relay field is
Coulomb-consistent is NOT YET DETERMINED — the honest current
answer is "the frozen test could not have decided it for any
field." Re-prereg (fresh patch) will freeze a comparative V-1:
automaton monopole-jellium field vs a VERIFIED exact-Coulomb
comparator on identical geometry, axes, and window, with the band
on the DIFFERENCE — after the comparator is validated against the
free-space law at small r/M. No production Moment has been run; the
79.5% is untouched; PR4 remains open pending the re-gated run.
