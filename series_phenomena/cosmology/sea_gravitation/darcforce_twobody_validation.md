# D-ARC-FORCE TWO-BODY VALIDATION — the 3085 instability DIAGNOSED (naive v×B kick) and FIXED (Boris rotation, parameter-free); close-range floor flagged for the array port

> **PROVENANCE BANNER (Patch 3088, 12 Aug 2026):** the 3086 code's
> MAGNETIC sign is inverted relative to its own docstring (repulsion
> for parallel currents where the analytic derivation — the ruled,
> textbook SF-6 limit — has attraction). Finding 2 of this record
> (Boris fixes the pump) VALIDATED THE PUSHER, which is sign-agnostic;
> the orbit also stayed bounded partly because the sign/launch
> mismatch kept it away from close range. With textbook signs,
> resolved orbits (a = 4/6/10) are bounded with drift 1.6e-5 / 8.8e-6
> / 8.0e-7; the a = 2 orbit decays into sub-unit passages — the §3
> close-range flag reproduced, and structurally absent on the lattice.
> See `darcforce_array_record.md` §1–§2.

**Patch 3086 (12 Aug 2026). Verify: `scripts/3086_arc_twobody.py`.
One +/− pair, free space, instantaneous forces (retardation off so
the analytic limit exists). Analytic orbit condition with the
parallel-current magnetic binding: v² = 1/(4a − 1). No band quantity
anywhere.**

## Findings

1. **The 3085 instability, reproduced in minimum setting and
   diagnosed:** with the naive `v += v×B` kick, the γ = 1
   conservative orbit PUMPS energy (+2.86 over 20,000 Moments;
   radius 2.4 → 31,816) — the known non-conservative discretisation
   of a force that does no work. In the 54-CP array this compounds
   to the observed overflow. The instability was never physics.
2. **The fix, validated:** the Boris pusher (half electric kick,
   EXACT ROTATION for the magnetic part — |v| preserved by
   construction — half kick; brake as a separate factor) holds the
   same orbit bounded with energy drift −0.003 over 20,000 Moments:
   three orders of magnitude improvement, parameter-free.
3. **Close-range flag (for the array port):** braked and lattice
   variants show floor-softened passage — after orbital decay the
   pair falls in, the r ≥ 1 force floor weakens capture through the
   passage, and the pair drifts back out. The floor is my modelling
   convenience; the automaton's true co-location behaviour
   (superposition, zero-force release, R-DWELL-1 relaunch) is what
   the array port must implement at close range instead.

## Next session, first CC item (updated)

Port Boris + the ruled close-range rules into the lattice array
(3083 script), then run the SAME pre-stated criterion (recurrent
superposition + η ≪ 2.25 + small f_sw + flat v²). The 3084
disposition stands: untested, not failed; a STABLE arc run that
fails earns the falsification conversation in full.
