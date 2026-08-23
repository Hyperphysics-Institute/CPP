# **THE JITTER ARC, PRICED HONESTLY — and a limitation that caps its reach: THE DM ENGINE CONTAINS NO STOCHASTIC TERM AT ALL** (`2902_mobile_sea_engine.py` has no `normal`, no `random`, no noise channel), so **every tail finding from 3183–3195 applies to the DE-lane v2 instrument ONLY and does NOT transfer to the DM lane** — there is no drive there to mis-specify; the founder's question "is it just the principle?" is answered: **partly yes, and the part that is more than principle is smaller than the arc's volume suggests**

**Patch 3196 (22 Aug 2026). Assessment, plus the one measurement that
would give the arc DM reach. Nothing claimed beyond what was
measured.**

## §1 — What the arc actually bought (ledger, not narrative)

| result | status | worth |
|---|---|---|
| Phase A: arrival spectrum computable, monopole-dominated, f_b-controlled | measured | a Sea-structure computation; **no prediction touched** |
| Phase B premise (jitter unlocks d_s^emp) | **REFUTED** (3181) | negative result, honestly the arc's largest single correction |
| Sea is intrinsically intermittent, 20–110× Gaussian burst rate | measured, power-gated | **a real substrate property** |
| Gaussian surrogate suppresses that intermittency ~100× at operating amplitude | measured, dose-response | **a real instrument defect, corpus-wide for tail statistics** |
| Variance is not a sufficient drive specification; heavy tails specifically | measured (3193) | **a real corpus-wide fact about every DE-lane instrument** |
| Calibration carries a 0.043 drive-shape systematic | measured (3195) | **an annotation on d_s^emp — 0.9%** |

**What the arc did NOT do:** it moved no prediction that meets the
sky. F-W-1 (w_now = −1.023) is untouched. The DM ledger is untouched.
Candidate (B) at 79.5% is untouched. No new number faces observation
because of any of it.

## §2 — The limitation that caps its reach

`2902_mobile_sea_engine.py` — the DM lane's engine — has **no
stochastic term**: no `normal`, no `random`, no injected drive. The
DM campaigns' Seas are jittered in POSITION at construction
(`build_sea_jittered`) and then evolve deterministically.

**Consequences, stated plainly:**
1. **The tail findings do not transfer to DM.** There is no drive
   whose shape could be mis-specified. Any statement that the DM
   response campaigns are exposed to D-TAIL-1's finding would be
   false, and the record should not imply it.
2. **The founder's 3177 §2.3 diagnosis needs re-reading in this
   light.** "Intermittent versus smooth driving give materially
   different response statistics at matched variance" is now
   MEASURED TRUE for the DE instrument — and for the DM engine it
   can only refer to intermittency INTRINSIC to the deterministic
   dynamics, not to any drive. Whether that intrinsic intermittency
   exists there is **unmeasured**.
3. **So the arc's DM relevance is currently ZERO, pending §3.**

## §3 — THE BRIDGE MEASUREMENT (chartered, for VideoCPU)

**D-SALT-2: is the DM engine's own force series intermittent?** Run
the D-SALT-1 instrument — power gate first, γ₂ and BURST on per-CP
experienced-force time series, Gaussian null for comparison — on the
DM engine's deterministic evolution at the campaign geometry.
- **INTERMITTENT** ⇒ the founder's mechanism has a home in the DM
  lane after all, as an intrinsic property, and response-vs-tail
  questions there become askable. **This is the only route by which
  the arc acquires DM reach.**
- **NEAR-GAUSSIAN** ⇒ the DM engine's dynamics are smooth, the
  mechanism does not apply there, and the founder's 3177 §2.3
  diagnosis loses its proposed cause in the DM lane specifically —
  **a real narrowing, and worth knowing before more DM campaigns are
  designed around it.**
Frozen before running: the power gate must separate synthetic
saltatory from synthetic Gaussian at ≥ 5 SE or every statistic is
BLIND and the test is VOID (3182 precedent, unchanged).

## §4 — The founder's question, answered directly

*"Is it just the principle of it that we proved?"* — **For the DM
lane: as of now, yes, and not even that, since the principle does not
apply to an engine with no drive.** For the DE lane: **more than
principle, but modestly so** — one measured 0.9% systematic on the
calibrated spacing, one corpus-wide instrument defect for tail
statistics, and one substrate property (intrinsic intermittency)
established on a power-gated test. **The arc's honest value is that
it made three unexamined assumptions examinable, and two of them
turned out false.** That is worth the compute it consumed; it is not
worth more than that, and the record should not inflate it.
