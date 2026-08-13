# PREREGISTRATION — THE CONSOLIDATED EXTRACTION RUN (committed BEFORE execution; the run's analysis is frozen here)

**Patch 3104 (13 Aug 2026). Sequencing ruled by the founder:
"Choose the way with the most integrity." Adjudication: a bracketed
assembly followed by measurement would place every extraction
decision AFTER the confrontation is seen — the contamination the
3068 freeze exists to prevent. Therefore: extraction FIRST, band-
blind, with this preregistration committed before any run; then ONE
assembly. Verify at execution: `scripts/3105_extraction_run.py`
(Patch 3105). Anti-extraction: nothing below references the band;
every definition and verdict rule is frozen here.**

## §1 — Instrument

The 3088 arc-force lattice array (corrected signs; Boris; retarded
partner; dwell-relaunch; quantized steps; validation gate mandatory),
extended with: (i) **mixed species** — half the pairs at bond
stiffness G = 1 (eDP-class), half at G = k² = 52.94 (qDP-class; the
strong bond is partner-internal: the retarded partner attraction is
multiplied by G; inter-pair forces stay electric, the tight-bound
strong far-field being second-order); (ii) **per-Moment pair-
separation retention** for the statistics below. **Declared
instrument regularization (flagged, not physics):** CP velocities
saturated at the substrate signal speed |V| ≤ 1 GP/Moment — required
because unit-Moment integration cannot resolve G ≈ 53 bonds (the
3103 lessons); this is a saturation at the information speed, NOT
the ruled-out fixed 1-GP step (R-STEP-SSV rejected the minimum-step
cap; a c-saturation under extreme force is a distinct statement).
**Whether the automaton itself caps CP response at c is posed to the
founder as FQ-9.1 in the results patch**; the s read-out carries
this flag until ruled.

## §2 — Cells (all arc ON, σ_n = 0.30 at recurrence onset, T = 3000)

- E1, E2: d_s = 8, γ ∈ {0.80, 0.90}, mixed species, seeds {5, 11}
- E3: d_s = 12, γ = 0.85, mixed species, seed 5
- B1–B3: d_s ∈ {5, 6, 7}, γ = 0.85, pure-e, seed 5 — the 3101 3D
  boundary confirmation cells
- Gate: check_twobody() must PASS first; a failed gate voids all.

## §3 — Frozen read-out definitions (stationary window = final third)

1. **r (gas/transient fraction):** mean fraction of pairs with
   separation d_p > d_s/2, over stationary Moments, e-class pairs.
2. **x_q (species split of the gas):** q-class share of all
   (pair, Moment) gas states. Symmetry check: expected ≈ the q seed
   fraction if species-blind; large asymmetry is itself a finding.
3. **η_z^gas:** mean(d_p²·1[d_p > d_s/2])/mean(1[d_p > d_s/2])/d_s²,
   e-class pairs (the gas-state excursion statistic).
4. **s_meas:** ⟨d_p²⟩_q-bound / ⟨d_p²⟩_e-bound over bound Moments
   (d_p ≤ d_s/2). Branch label (secondary; the measured value is the
   assembly input): ≤ 3/G² → "continuum-I-like"; else "floored-II-
   like." Carried with the §1 regularization flag either way.
5. **Arrangement factor:** a_C4 = S₄(pair centres, measured,
   periodic sum)/S₄(FCC at matched density), e-class stationary
   snapshots (5 snapshots averaged). Resolves the A-1 bracket
   [0.78, 1.35].
6. **Boundary confirmation:** phase per B-cell (3088 classifier
   unchanged); verdict = the d_s below which FAITHFUL is
   unattainable, compared against 6.9 ± 0.1 (E-register 1D value;
   the 3D array is e-class so the reference is the 3101 A-scan).

## §4 — Use commitments

The read-outs feed the single final assembly (next patch after
results) with NO post-hoc redefinition: if a read-out is
pathological (e.g. no gas states observed), the assembly carries the
3103 declared bracket for that input instead, stated as such. The
assembly then multiplies ONCE; in band or F-CLI-1 fires in those
words. Small-array caveat declared now: 27 pairs per cell is
statistics-poor; standard errors are reported and ride into the
assembly brackets. Kila6 Route C and the DM ledger untouched.
