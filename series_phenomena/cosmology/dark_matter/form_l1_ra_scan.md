# OPEN-DM-FORM-L-1 — R-A executed under the 2553 pre-registration: NO formation-side lower cutoff (closure pays even at L = 8); a union-stable payoff MAXIMUM at L = 20 (not 16); an equilibrium collapse at L = 24 banked behind the campaign's own upper-cutoff fence; adverse-direction for the derive-16 prize, candidate untouched

**Patch 2554, 18 July 2026. Status: OPEN-DM-FORM-L-1 CLOSED with banked structure;
adverse-direction FOR THE DERIVE-16 PRIZE recorded (per the frozen §4 readings); the
candidate is NOT adversely moved** (formation-side selection was never a registered
support of the 79.5 %). Verify: `code/2554_form_l1_scan.py` (42 dance runs, 234 s; all
assertions pass; the table and structure readings froze before the comparison sentence).

## 1. The frozen table (primary ⟨Ep⟩, MeV; ±2 floor rider on every entry)

| L | inner-edge pitch (fm) | dt=1/100 | 1/50 | 1/25 |
|---|---|---|---|---|
| 8 | 0.698 | +67.6 | +63.5 | +60.8 |
| 10 | 0.789 | +90.8 | +96.0 | +90.6 |
| 12 | 0.849 | +95.9 | +97.6 | +96.6 |
| 14 | 0.892 | +135.5 | +139.5 | +134.0 |
| 16 | 0.924 | +134.1 | +137.5 | +128.9 |
| 20 | 0.969 | +176.1 | +159.9 | +158.4 |
| 24 | 0.999 | +0.5 | −6.2 | +1.4 |

(FREF(L) = 10.47 for L ≥ 10, 10.58 at L = 8 — disclosed; ⟨Etot⟩ accounting same-shaped,
disclosed in the artifact. The L = 16 row reproduces the ENDBOND-3 pin exactly, as it
must — same runs.)

## 2. Frozen readings (per prereg §4, in order)

- **Lower cutoff: NONE.** Closure pays beyond floor at every L down to 8 — the stated
  pre-run hypothesis (inner-edge compression makes short rings unfavorable) is **WRONG
  and recorded as such**; tight curvature does not kill closure at dance strength.
- **Sign change: NOT union-stable** (one beyond-floor negative cell at (24, dt=1/50);
  the other two L = 24 cells zero-consistent) → no cutoff claim via this reading.
- **Interior argmax: UNION-STABLE at L = 20** (all three dt cells) → the §4
  interior-maximum reading fires: the licensed selection-flavored statement is that
  **the closure payoff peaks at L = 20 on this grid**.
- **The L = 24 collapse** (~160 MeV drop from L = 20, present far beyond floor in all
  three cells, landing zero-consistent): **BANKED as structure only.** The frozen §4 line
  "upper-cutoff claims of any kind → Branch I, NB-S3a-1 named" was drafted against
  kinetic cutoffs but reads broader, and the frozen letter governs: no upper-cutoff claim
  is made in-campaign. A successor may charter the equilibrium upper question, with the
  §4 audit item below as its mandatory first act.

## 3. The comparison sentence (prereg §5) — with a disclosed code defect

The artifact's sentence-generator implemented only the sign-change branch and printed
"no union-stable structure survived" — **a defect, disclosed**: the argmax reading DID
survive the union, and the prereg (not the incomplete generator) governs. The sentence is
deterministically derivable from the frozen table, so it is stated here without any
re-run: **L = 16 is not the payoff maximum; the union-stable maximum on this grid is
L = 20, one even rung above the registered candidate, with 16 inside the broad
closure-pays region.**

## 4. Named audit item (registered)

The reach classifier's "in-plane" test uses global Δz < 0.5·D; on rings, plane pairs near
the top (φ ≈ 90°) have small Δz between distinct planes, so the reach topology changes
discretely with L and orientation. This is verbatim registered-functional behavior (it was
present in every 2461/2510/2551 ring run), but it is a candidate mechanism for non-smooth
L-dependence — including the L = 24 collapse — and is registered as **AUDIT-DANCE-REACH-1**:
an implementation-fidelity item of exactly the class CONV-001 panels stress-test, mandatory
first act of any successor that wants to promote the L = 24 structure.

## 5. Honest placement

Formation-side structure exists at dance strength and it does not point at 16. Three
things keep this from being a candidate hit: (i) E_close magnitude is a payoff, not a
rate — formation *selection* is plausibly kinetic (NB-S3a-1) and this equilibrium
instrument was pre-declared unable to see it; (ii) the selection burden was always
registered on the stability side (OPEN-SS-43: N = 8 elements sole survivor at the
candidate mass), which this campaign explicitly did not re-litigate; (iii) the L = 20
peak and L = 24 collapse are unaudited against AUDIT-DANCE-REACH-1. What IS adverse: the
hoped-for clean formation-side route to deriving 16 did not materialize here, and the
dated adverse-direction-for-the-prize line goes to the standing disclosure package
alongside the S1 charge-ADM line.

## 6. Bookkeeping

79.5 % untouched. Dated line to the disclosure package. NB-S3a-1 remains the named
blocked project and is now the *only* live route to a formation-side derivation of 16.
Queue: plane-resident-fraction limb → δ_E → MW-MODES TC-extension; AUDIT-DANCE-REACH-1
available as a registrable audit. Next patch: 2555.

---
## 7. CORRECTION RIDER (Patch 2557): under reach-S (2556), the corrected table (see `reregistration_reach_s.md` §2) makes the **(20, 24) sign change UNION-STABLE** (L=24 closure-unfavorable beyond floor in all cells); argmax stays at L=20. The §2 upper-cutoff fence still governs in-campaign; the structure is promotion-READY for FORM-L-2 (held per 2556 §4).
