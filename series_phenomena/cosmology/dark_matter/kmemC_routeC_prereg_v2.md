# PREREGISTRATION v2 — K-MEM ROUTE C, CORRECTED DESIGN VARIABLE (Δ = SOURCE TRAVEL − T_BALL); ISOLATION ARMS + A DEDICATED MARGIN ARM

**Patch 3055 (10 Aug 2026). SUPERSEDES `kmemC_routeC_prereg.md` (v1,
Patch 3053), which is retained in-repo unedited as the anti-erasure
record. Amended BEFORE any evidentiary leg: only the pre-launch
calibration ran, it is evidence-excluded by v1 §3, and it FAILED ITS
OWN OK-CHECK — the failure is the reason for this amendment and is
recorded at `kmemC_calibration_failure_record.md`. No data has been
looked at; nothing evidentiary exists.**

---

## §1 — What v1 got wrong (the correction, stated first)

v1 froze the design variable as ΔT = T_exit − T_close, where T_exit
was the Moment the source leaves the domain. Reconstruction from the
committed Route B configuration shows:

| Route B domain | source travel L | exits? | T_BALL = 1.5·x_half | **Δ = L − T_BALL** | S1 tail |
|---|---|---|---|---|---|
| d24 | 36.0 | **NO** (ends at +18) | 36.0 | **0.0** | SIGNIFICANT |
| d28 | 36.0 | NO | 42.0 | −6.0 | c.w.z. |
| d32 | 36.0 | NO | 48.0 | −12.0 | c.w.z. |

Three v1 defects: (1) **the source never exits** at β = 0.10 — T_exit
does not exist in the regime the artifact was observed in; the Patch
3047 §4 diagnosis was about the source TRAVEL DISTANCE matching
T_BALL, not an exit; (2) T_exit is β-dependent, so v1's drive ladder
would have MOVED THE GEOMETRY while sizing the drive — geometry and
drive were coupled; (3) the calibration bisection searched the wrong
direction and the v1 ΔT targets were unreachable inside the
admissible x_src0 range. All three were caught by the calibration's
own OK-check with zero evidentiary legs run.

**Corrected design variable:** **Δ ≡ L − T_BALL**, where
L = β·(T_END − t_step) is the post-step source travel distance and
T_BALL = 1.5·x_half. Δ is closed-form in (β, T_END, x_half) — no
bisection, no engine calibration run, and it reproduces the Route B
pattern exactly (artifact at Δ = 0, absent at Δ < 0).

## §2 — Arms (FROZEN; x_src0 = −L/2 centred; wall margin = x_half − L/2 ≥ 4 enforced; t_step = 24 throughout; annulus RHO = (1,8); spacing 2.5; 2907 jitter; shared-seed pair matching; master seed 30550810)

| Arm | Class | x_half | T_END | β | L | x_src0 | margin | **Δ** | N_pairs | Role |
|---|---|---|---|---|---|---|---|---|---|---|
| **A0** | isolation | 24 | 384 | 0.10 | 36 | −18 | 6 | **0** | 128 | Route B d24 VERBATIM — the artifact must APPEAR |
| **A0′** | isolation | 16 | 264 | 0.10 | 24 | −12 | 4 | **0** | 128 | matched Δ, DISTINCT geometry — the artifact must ALSO appear |
| **A1** | isolation | 32 | 384 | 0.10 | 36 | −18 | 14 | **−12** | 128 | Route B d32 replicate at 2× pairs — must be ABSENT |
| **A2** | isolation | 28 | 504 | 0.10 | 48 | −24 | 4 | **+6** | 128 | the POSITIVE side, never explored — must be ABSENT |
| **AK** | margin | 28 | 104 | 0.60 | 48 | −24 | 4 | +6 | 512 | κ_sys ONLY (window 32 pts ≥ 8); NON-tail-inferential |

Design-class compliance (the frozen minority requirements, now in the
correct variable): both signs of Δ present (A1 −12, A2 +6) ✓; two
geometrically distinct configurations at matched Δ = 0 (A0 x=24/T=384
and A0′ x=16/T=264) ✓ — **strictly stronger than v1**, since the
diagnosis must now reproduce the artifact in a box it has never been
seen in; the artifact configuration reproduced (A0) ✓.

**Why a separate margin arm.** The 3052 lesson requires the
systematic response ≥ 10σ, which needs a strong drive; but at
β = 0.10 the isolation arms cannot reach it, and raising β on an
isolation arm would change Δ and destroy comparability. AK therefore
carries the drive (β = 0.60, 6× amplitude) in a SHORT run that keeps
L and hence Δ fixed at a clean value, with N = 512 for the σ. AK's
window is too short for tail inference and it is declared
non-tail-inferential; the isolation arms carry the tail question.

## §3 — Pre-launch checks (evidence-excluded)

1. **Calibration = arithmetic** (no engine runs): the driver prints
   the §2 table computed from the frozen constants and asserts every
   Δ target and every margin ≥ 4; any mismatch → STOP.
2. **AK resolvability pilot** (4 pairs, EXCLUDED from evidence):
   projects SNR(N = 512). Frozen escalation ladder — **N only, never
   β** (β escalation would move Δ): 512 → 1024. Below 10 at 1024 →
   STOP AND REPORT (panel; no further escalation admissible).
3. Isolation arms are NOT pilot-gated (their statistic is S1, whose
   Route B sensitivity at 64 pairs already detected the artifact;
   these arms carry 128).

## §4 — Frozen statistics (computed only on a complete manifest)

- **S3-C control** (all arms): Route B recipe with the band scaled by
  β/0.10. A failing INFERENTIAL arm is PROSPECTIVELY
  NON-INTERPRETABLE and drops from inference (minority clause).
- **S1-C tail** (isolation arms only): Route B S1 recipe verbatim.
- **κ_sys** (AK primary; isolation arms reported non-gating): the
  Patch 3051 estimator, per-arm t_post = t_step + 1.5·x_half + 6,
  late window = final 48 Moments; BRANCH-FIT expected at AK.
- **P-ISO:** S1-C SIGNIFICANT at BOTH Δ = 0 arms (A0 and A0′) AND
  c.w.z. at every valid Δ ≠ 0 arm.
- **P-κ:** AK resolves on BRANCH-FIT with κ_sys^{U99} < 1.

## §5 — FROZEN DISPOSITION TREE (total; evaluated in order; standing NONE until the single panel round)

1. Fewer than TWO isolation arms pass S3-C, or AK fails S3-C →
   **DISP-I3** (instrument; panel).
2. S1-C SIGNIFICANT in ANY valid Δ ≠ 0 arm → **DISP-T: THE FALSIFIER
   FIRES** — domain-robust control-valid tail; indictment SUSTAINED;
   item 1B FAILS; Candidate (B) fails requirement 7.
3. P-ISO ∧ P-κ → **DISP-R: RETIREMENT FINALIZED + MARGIN CERTIFIED**
   → item 1B DISCHARGES → **SEVEN OF SEVEN** (panel confirms).
4. P-ISO ∧ ¬P-κ → **DISP-P: PARTIAL** (tail retires; margin leg
   open).
5. ¬P-ISO because the artifact fails to reproduce at A0 → **DISP-X**
   (the geometric diagnosis fails; Q1 standing reopens).
6. ¬P-ISO because A0 shows it but A0′ does not → **DISP-G:
   GEOMETRY-SPECIFIC** — the artifact is real but not the Δ = 0
   mechanism; panel re-diagnoses (this branch exists because A0′ is
   the genuinely new test).
7. else → **DISP-M3 IMPASSE.**

No interim looks; the analysis refuses incomplete manifests; no
retune after launch; one panel round on completion.

## §6 — Effort

≈ 3720 CPU-h ≈ 7 days wall at Route-B parallelism (A0 666, A0′ 305,
A1 887, A2 1019, AK 841). **Frozen pre-launch reduction** (declared
now, usable only before launch, at the founder's election): isolation
N 128 → 96 and AK 512 → 384, giving ≈ 2800 CPU-h ≈ 5.3 days — AK's
SNR projection must still clear 10 at the reduced N or the reduction
is void.
