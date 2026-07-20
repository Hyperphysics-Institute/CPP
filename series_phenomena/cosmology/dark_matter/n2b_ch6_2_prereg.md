# N2-B-CH6-2 pre-registration (corrected): the channel scan re-entered with both aim conventions EXPLICIT — the control is the verbatim absolute-aim reproduction of the registered stall (demonstrated at 2612), the scan is centroid-relative by declaration, committed before the read

**Patch 2613, 20 July 2026. Status: N2-B-CH6-2 OPENED at pre-registration.** Supersedes
the 2610 prereg's defective C-A (which conflated aim conventions; RC4 at 2611; defect
confirmed at 2612). Governed by this document only. Verify: none at prereg.

## 1. The two conventions, named (the 2611 lesson codified)

**ABSOLUTE-AIM** (the registered chain protocol, 2604 verbatim): incident launched at
the fixed laboratory column [b·D, 0, ztop + 4D] — faithful to ambient flux arriving in
the lab frame. **CENTROID-RELATIVE** (the face probe): incident launched at
cluster-center + axis·(ext + 4D) + offset — faithful to the face-geometry question.
They are DIFFERENT experiments; this campaign runs both, reads each against its own
question, and never trades verdicts between them.

## 2. Cells (all deterministic; dt-union {1/100, 1/200} unconditional; TC = 120; η = 0.5)

- **Controls (absolute-aim, verbatim stage_capture):** C-A′ soft stage 7 must read
  MISS/UNBOUND (the registered stall; reproduced at 2612); C-B′ steep stage 7 must
  read CAP (the registered completion). Both at both dt. Failure → RC4′, STOP.
- **The scan (centroid-relative):** the identical 22 declared soft cells of 2610 §2
  (six axes × b ∈ {0, 0.5, 1.0}D; three azimuths at the original face; the charge
  flip), re-run under THIS prereg. The 2611 artifact's outputs are citable as prior
  raw data; the READ happens on tonight's runs only.

## 3. Readings (frozen)

- **RC1′ — NO SHELL:** controls pass AND all 22 centroid-relative cells read
  dt-stable CAP → registers: **the soft 6-cluster captures on every declared channel
  when aimed; the registered stall is (per 2612) an aim-drift artifact; the shell
  hypothesis closes NEGATIVE.** A soft-chain continuation cell (drift-following aim,
  or absolute-aim with declared flux geometry) may be DECLARED, not run.
- **RC2′ — FACE STRUCTURE:** controls pass AND ≥ 1 centroid-relative cell reads
  dt-stable non-CAP → the face map registers with its structure (which channels stick;
  honest scope: charge as tested, v = 0.1c).
- **RC3′ — UNSTABLE:** dt-unstable cells are excluded from the map; > 3 unstable →
  DEFECT-HUNT, nothing registers.
- **RC4′ — CONTROL FAILURE:** STOP, nothing read.
- Fences: no chain continuation runs tonight under any reading; win-candidate packet
  frozen (and carries the 2612 correction before dispatch — founder-flagged); B4
  untouched; relic fence; 79.5% untouched.

## 4. Bookkeeping

Next patch: execution. Verify script `code/2614_n2b_ch6_rescan.py`.
