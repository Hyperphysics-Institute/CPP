# BAND PROVENANCE AUDIT — `SUST_REF` INVALIDATED, COEFFICIENT CLAIM SUSPENDED

**Patch 3176, 22 August 2026.** Free audit, no campaign, no engine legs.
Commissioned by the founder before any dispatch of the Patch 3175
coefficient finding. **Outcome: the finding is SUSPENDED, and the band
that produced it is invalidated across Route B, Route C and the
β-ladder.**

---

## §1 — WHAT `0.026·β` ACTUALLY MEASURES

Traced to origin: `flagship_papers/electromagnetism/sketches/beta_zero_control_record.md`
§3. In context, 0.026·β is the amplitude of the motion-proportional (a1)
component of **`p_x`**, where `p = plus - minus` in
`2914_response_field.py` line 41 — the **dipole moment (separation
vector) of a Sea pair**, binned in co-moving bins, inner ring ρ ∈ [1,3].

It is a **DISPLACEMENT of Sea-pair members**, in length units.

## §2 — WHAT `sust_B` MEASURES

`sust_B = D[LATE] − D[PRE]`, D = F_step − F_ctrl, F = `src_net[0]` —
the axial component of Σ_e q_src·q_e·û /(4π(R²+SOFT2)) evaluated **at
the source**. A **FORCE on the source**, in field units.

Different object (Sea pairs vs the source), different dimension
(displacement vs force).

## §3 — WHERE THE TRANSPLANT HAPPENED

`series_phenomena/cosmology/dark_matter/code/3028_kmem3_analysis.py`
line 24: `SUST_REF = 2.6e-3  # 2918 sustained scale`, used at line 143
as a factor-2 acceptance band on a **force** statistic. Inherited by
`3054_kmemC_analysis.py` (`SUST_REF0`, scaled by β/0.10), by the Route C
disposition (CONV-024), and by the β-ladder's coefficient reading. The
transplant carries the polarization amplitude into the force band **as
though the conversion factor were 1**.

## §4 — THE FOUNDER'S RULING AND THE COMPUTED FACTOR

Founder (21 Aug 2026): a coupling exists — every CP's position converts
to source force — but it is 1/r³-suppressed and configuration-dependent,
with dipole cancellation applying or not depending on separation versus
distance. So the factor is computable and is **not** unity.

`code/3176_polarization_to_force_conversion.py` computes it on the exact
2914 geometry (`build_sea_sym`, classes A/B, seeds 4/5/6 — the 2918
grid) with the engine's exact force law, both members, no dipole
approximation. Parity of the imposed profile is the dominant unknown, so
**both parities are computed and BOTH are reported; neither is
selected**:

| profile | F_CONV | corrected band at β=0.10 | transplanted / corrected |
|---|---|---|---|
| inner ring, UNIFORM | −0.0010 ± 0.0039 | 2.70e-06 | ≈ 963× |
| all rings, UNIFORM | −0.0077 ± 0.0037 | 2.00e-05 | ≈ 130× |
| inner ring, ODD | −0.0000 ± 0.0000 | ≈ 0 | undefined |
| all rings, ODD | +0.0000 ± 0.0000 | 0 | undefined |

**The ODD result is exact, and it is the structurally important one.**
An odd-in-ξ polarization profile against an even-in-ξ force kernel sums
to exactly zero net axial force at the source. The 2918 record states
the persistent map **is** ODD-dominated (0.0138 vs 0.0053). If a1 shares
that parity, a Sea polarization of this shape produces **no sustained
axial force on the source at all** — the premise of the band is
geometrically void, not merely mis-scaled.

Under every profile tested the transplanted band is too large by **at
least two orders of magnitude**.

## §5 — CONSEQUENCE FOR THE PATCH 3175 FINDING

**COEFFICIENT-OVERPREDICTED is SUSPENDED, not retracted-as-false.** Its
claim was that measurement (k ≈ 0.0074) falls ≈3.5× BELOW the prediction
(0.026). Against any corrected band the measured 9.14e-04 at β = 0.10 is
**45×–340× ABOVE** it. **The finding fails in magnitude AND inverts in
direction.** No claim of a CPP overprediction survives; equally, no claim
of underprediction is minted here — an invalidated comparator supports
no verdict in either direction.

**What is NOT touched:** the scaling arc. BETA-UNRESOLVED, the ratio
test and the through-origin fit never reference 0.026. The Patch 3175
gate pass, the four rung measurements, and the underpower diagnosis all
stand. The Kila6 β = 0.05 closure remains valid and launchable.

**Upstream exposure, flagged not adjudicated:** Route C's DISP-I3
signature ("all five arms FAIL S3-C, universally and one-directionally,
every arm undershooting its band's lower edge") was computed against
this band. If the band is too large by ≥100×, universal undershoot is
what a mis-sited band would manufacture regardless of the physics.
**DISP-I3's evidentiary basis is now IN QUESTION.** This record does not
move it — re-adjudication requires its own round, with the panel seeing
this audit.

## §6 — SEPARATE PROVENANCE FINDING: F-W-1 IS NOT THE CALIBRATION TARGET

The founder recalled calibrating on "1.023". `calibration_record.md` §1–3
shows otherwise: the calibration anchor is **Λ**, yielding
d_s^emp = 4.636 (the single O(1) empirical anchor). **w_now = −1.023 is a
downstream output of the 3098 displacement theorem**, not the calibrated
quantity — so F-W-1 stands as a live prediction, correctly labelled.

Honest caveat recorded: w is downstream of a Λ-calibrated anchor, so it
is not a wholly independent prediction of dark-sector physics — it
predicts the *equation of state and its evolution* given a spacing
calibrated to Λ's present value. That is a legitimate prediction and
should be stated in exactly those terms in any dispatch.

## §7 — DISCLOSED LIMITATIONS OF THIS AUDIT

1. Static and non-retarded; the campaigns are dynamic with retardation,
   which breaks exact symmetry and could make the ODD case nonzero.
2. Source at origin; in the campaigns the source is off-centre and
   moving.
3. The a1 profile's true parity is not archived in readable form; §4
   uses the record's statement about the **persistent** map, which is a
   different component.

None of these rescues a factor of 130–963. A full-fidelity conversion —
computing the force directly from the archived a1 map under retardation
— is the clean successor and is cheap. **Registered as OPEN-BAND-CONV-1.**
