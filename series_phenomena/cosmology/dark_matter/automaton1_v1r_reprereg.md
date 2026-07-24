# AUTOMATON-1 V-1R RE-PREREGISTRATION (FROZEN) — the comparative field-law gate

**Patch 2798. Frozen 2026-07-24 before any gate run, per the 2796
defect clause and the 2797 FAIL-STOP disposition. Everything
downstream of the validation gates (production runs, observables,
bands, verdict classes of 2796 §4) is UNCHANGED and is not re-opened
here.**

**V-1b (gate-on-the-gate, EXECUTED at freeze):** the real-space
Ewald comparator (`code/2798_ewald_comparator.py`) reproduces free
space to worst deviation 0.856% over r ∈ [3, 6], three directions,
M = 48 — PASS (< 2% band). It further establishes that EXACT torus
Coulomb over the 2797 diagnostic window ([8, 16], M = 48) has
p = 2.291: the original V-1 band [1.8, 2.2] was unsatisfiable for
ANY Coulombic field on this geometry, and the 2797 FAIL is hereby
classified a GATE-DESIGN defect, not a DR-1 defect.

**Disclosure:** the automaton's R = 3 jellium axis profile is
already of record (2797 appendix; global p = 2.311 — prospectively
Δp = 0.020 from exact Coulomb, and point ratios flat within ±3.1%).
V-1R at R = 3 is therefore CONFIRMATORY-DISCLOSED; R = 2 and R = 4
are blind.

## V-1R (frozen, comparative)

Configuration: single + charge pinned at origin, uniform
neutralizing background injection (−1/M³ per GP per Moment), M = 48,
equilibration 4M Moments, averaging 2M Moments, axes ±x, ±y, ±z.
Per R ∈ {2, 3, 4}, window r ∈ [2R + 2, 16]:

- ρ(r) = |V_auto|(r) / |E_Ewald|(r), normalized by its window mean
  (the relay's amplitude unit is conventional).
- **PASS bands: every window point's normalized ρ ∈ [0.90, 1.10],
  AND |p_auto − p_Ewald| ≤ 0.15 on the window** — required at ≥ 2 of
  3 R values (single-R failure with two passes = noted, gate open).
- FAIL at ≥ 2 of 3 R → DR-1 inadequate; STOP and re-prereg (as
  before).

V-2 (conservation/boundedness) and V-3 (isotropy; PASS of record at
2797) retain their 2796 definitions; V-2 executes after V-1R.
