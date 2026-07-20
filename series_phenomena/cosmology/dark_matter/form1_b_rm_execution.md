# FORM-1 Agenda B — reduced-model execution record: VERDICT FB-ORD FAIL ∧ FB-LOC FAIL at the single-pair reduction — the boundary's carrier is NOT a one-mode object; the mechanism account gains a named competitor; Tier 2 registers UNMET

**Patch 2656, 20 July 2026. Execution under `form1_b_sink_derivation.md` (2655)
§3 as amended RM-A1 (below). Verify: `code/2656_form1_b_rm.py` (spec-to-code
trace table + three guard triggers in the script header per METH-L2-018; all
guards PASS). One pass per cell; no iteration; no parameter moved.**

## 0. RM-A1 — pre-execution amendment (disclosed before the run, sequencing exact)

The frozen §3 spec item 1 (two free qCPs, m = 132 each) gives reduced mass
μ = 66 and shifts every model frequency √2 above the registered 2628 map
ω(w) = (w/D)√(2E_qq/m), which was registered AT m = 132 — the anchored-target
convention. Discovered on spec-internal consistency review BEFORE any run;
amended to the anchored-target convention (incident m = 132 against a fixed
target), sourced to the 2628 registration itself, per the RELIC-1 v1.1 /
charter-v1.1 pre-execution-amendment precedent. No outcome existed when the
amendment was made. Freeze discipline unviolated.

## 1. Raw outputs (verbatim)

```
[G-A] eta=1.0 split kills oscillation: PASS
[G-B] eta=0, w=2, dtf=1/400: Sea=8.5e-14, Edrift=1.92 MeV: PASS
[G-C] statics: omega_eff (combined well) vs registered Morse-only omega:
  w=2: 2.039 vs 1.743 (+17.0%)   w=2.5: 2.487 vs 2.178 (+14.2%)
  w=3: 2.932 vs 2.614 (+12.2%)   w=4: 3.818 vs 3.485 (+9.5%)
  (the engine electric kernel's curvature at the minimum; reported, not hidden)
[CALIBRATION FACE] v=0.10, eta=0.5, W-A single-pass, final-inc(1/200->1/400):
  w=2: S_WA = 24.214, 24.379, 24.461   final-inc = 0.34%
  w=3: S_WA = 12.638, 12.656, 12.663   final-inc = 0.06%
  w=4: S_WA = 11.588, 11.607, 11.614   final-inc = 0.06%
[HOLDOUT FACE] (w=2.5 QUARANTINED diagnostic)
  H1 w=2.5: 15.005, 15.047, 15.066     final-inc = 0.13%
  H2 w=4 @ {1/400,1/800}: 11.614, 11.618   final-inc = 0.03%
  H3 w=2 @ {1/400,1/800}: 24.461, 24.502   final-inc = 0.17%
```

## 2. Reading (frozen at 2655 §3, applied verbatim)

- **FB-ORD: FAIL.** Model final-inc is NOT monotone increasing in w — it is
  largest at the SOFT width and flat-small at w = 3, 4. The instrument's
  registered ordering (0.41% → 7.2% → 11.6%) is not reproduced in kind.
- **FB-LOC: FAIL.** Every width sits deep in the convergent class (≤ 0.34%);
  no boundary exists anywhere on the model's face.
- **Tier 2: UNMET** at this reduction. Per charter v1.1, FD-FULL and
  FD-PARTIAL are unreachable for Agenda B through this arm; the Agenda-B
  composite is bounded above by **FD-BOUNDARY** (FB-T1 stands as theorem —
  the entry condition; the quantitative boundary prediction did not land).
  The composite waits for the session close per charter §5; nothing renames.
- **FB-RC check:** guards all pass; the model is faithful to its (amended)
  spec; this is a physics negative for the REDUCTION, not an instrument
  defect. No defect-ledger entry.

## 3. The diagnosis (mechanical, observation-grade, no claim promoted)

The single-pair reduction removes, simultaneously, BOTH structures that could
carry schedule dt-sensitivity:

1. **Multi-mode phase structure.** After capture the model has one degree of
   freedom; its sheds sample one phase, and the W-A sum's whole-period
   cancellation (2655 §2) protects it at every width — which is exactly what
   the flat sub-0.4% face shows. The instrument's schedule, by contrast,
   samples the 4-square's internal mode sector (m1/m2/ℓ — the registered
   2513/2635 decomposition), several stiff anharmonic phases at once.
2. **Chaotic trajectory divergence.** A 1-dof autonomous system cannot be
   chaotic. The registered corpus already holds a precedent for stiffness-
   gated non-convergence of exactly this shape: **Branch U's chaotic floor
   (2513/2514, OPEN-DM-MW-MODES-1)** — dt-differences amplified at trajectory
   level rather than sampled-phase level.

The 2655 mechanism account therefore gains a named competitor, and the record
registers both, neither promoted:

- **FB-MECH-A (phase-sample decoherence, 2655 §2):** the schedule fails where
  sampled phase decoheres; predicts the steep width RE-CONVERGES as dt falls
  (Ξ ∝ dt) — H2 at {1/400, 1/800} should fall materially out of the
  saturated class.
- **FB-MECH-B (multi-mode chaotic divergence, Branch-U class):** the schedule
  fails where the target's coupled anharmonic modes go chaotic; predicts the
  steep width does NOT re-converge on any affordable ladder — H2 stays in
  the saturated class, erratic.

**H2 is the discriminator between A and B — a genuinely two-sided holdout
whose either outcome is informative.** H3 (soft width at finer dt) tests the
cancellation-order account on the convergent side under both. H1 (w = 2.5)
retains its boundary-location value only under A; under B it reads as a
chaos-onset probe, no sharp prediction.

## 4. Tier-3 predictions (frozen NOW, before any registered-instrument run)

The registered-instrument holdout arc (next patches, its own prereg) will read
against these, written before any instrument cell runs:

- **P-H2:** under FB-MECH-A, w = 4 final-inc at {1/400, 1/800} ≤ 5% (leaves
  the saturated class); under FB-MECH-B, ≥ 5% (stays). Whichever fires
  classifies the mechanism; NEITHER outcome licenses any schedule consumer.
- **P-H3:** w = 2 final-inc at {1/400, 1/800} remains convergent-class
  (≤ 2.5%) under both accounts; the A-account's cancellation structure
  additionally expects it at or below the registered 0.41% class.
- **P-H1:** w = 2.5 (QUARANTINED) — under A: convergent-to-marginal (< 5%);
  under B: unconstrained (chaos onset may be sharp on either side).
- **Pin control (mandatory):** the instrument holdout run must first
  reproduce the 2629 P1 printed row (S_WA at w ∈ {2,3,4} × dt ∈
  {1/100,1/200,1/400}) to the printed digit before any holdout cell counts.

## 5. Standing

Fences verbatim (charter §6): no schedule consumer moves under any reading;
w = 2.5 and w = 3 quarantined; DISC amendment scope untouched; 2513/2635/C7
unedited; **79.5% untouched.** Reasoning: `reasoning/2656.md`.
