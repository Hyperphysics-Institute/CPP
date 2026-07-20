# N2-B-CH6 executed: **VERDICT RC4 — CONTROL FAILURE; THE SCAN STOPS UNREAD.** C-A did not reproduce the registered miss (every cell including the original channel read dt-stable CAP in the scan's centroid-relative frame); the defect is an AIM-CONVENTION discrepancy between the scan and the registered chain protocol, and it is the next patch's subject

**Patch 2611, 20 July 2026. Governed by `n2b_ch6_prereg.md` (2610) ONLY. Artifact:
`code/2611_n2b_ch6_scan.py`. Verdict read from the prereg's frozen readings.**

## 1. What happened

C-R passed (soft and steep stages 5–6 regenerate BOUND, the registered path). Then
**C-A failed**: the original soft channel — the cell that MUST reproduce the registered
stage-7 MISS — read **CAP (Sea ≈ 338 MeV, dt-stable)**. Per the frozen RC4: **STOP;
nothing is read as physics; no RC1/RC2 claim exists.** The 22 soft cells and the steep
control all read dt-stable CAP (46/46 runs, 0 dt-unstable); those outputs are DISCLOSED
here as raw instrument data only — under RC4 they carry no registered interpretation.

## 2. The defect, located by inspection (hypothesis, named for the diagnostic)

The registered `stage_capture` (2604, verbatim) launches the incident at **absolute**
coordinates `[b·D, 0, ztop + 4D]` — a fixed laboratory column. The scan's cells aim
**centroid-relative** (start = cluster center + axis·(ext + 4D) + offset). A grown
cluster is not at the origin: every capture imparts momentum; the object recoils and
translates. **H-drift (named, not promoted):** by stage 7 the soft 6-cluster has
drifted far enough from the fixed launch column that the registered incident passed at
large effective impact parameter — the registered "miss" would then be a property of
the PROTOCOL's aim convention, not of the cluster's face. The prereg's C-A, as I wrote
it, silently conflated the two conventions; the control did its job by failing loudly.

## 3. What follows (frozen by RC4)

The defect is the next patch's subject: a diagnostic that (i) reproduces the registered
stage-7 launch VERBATIM (absolute aim) and must recover the registered MISS, (ii) logs
the cluster centroid position/velocity at launch and the launch line's closest-approach
distance to it, and (iii) reads H-drift against those numbers. If H-drift confirms, the
2604 "shell/plateau structure" classification requires a disclosed correction, and the
face-map question — now well-posed — re-enters through a CORRECTED prereg with both aim
conventions explicit. Nothing registers tonight from this scan.

## 4. Standing

Fences held throughout: no chain continuation, win-candidate packet frozen, B4
untouched, relic fence, 79.5% untouched. The scan's 46 deterministic runs remain in the
artifact for citation by the corrected campaign; they are data, not verdicts.
