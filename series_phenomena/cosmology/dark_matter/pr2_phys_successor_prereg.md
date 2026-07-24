# PR2-PHYS SUCCESSOR GATE — PREREGISTRATION DRAFT FOR PANEL RATIFICATION (Patch 2795)

**Status: DRAFT-FOR-RATIFICATION. Authority: the P2 two-level ruling
(2794, adopted 4–1): PR2-FROZEN FAIL stands as-letter; the original
operationalization is retired as an invalid proxy; a successor gate
must be freshly chartered by the panel on the registered binding
spec before candidate promotion can proceed on this line. This
document instantiates that spec. IT DOES NOT EXECUTE until ratified
by CONV-001 majority; ratification returns may AMEND any constant
below.**

## §0 — Pre-observation disclosure (read first)

The successor runs on the EXISTING committed 15-chain archive
(`data/rv2714/`, `data/x3x4/`) — the ladder already satisfies PR2's
multiplicity matrix, and new chains would add cost without new
discriminating power. Consequence, disclosed plainly: the battery
(Patch 2793) already published the per-rung joint shared-pole values
(0.9643 ± 0.0094 / 0.9665 ± 0.0102 / 0.9787 ± 0.0104 /
0.9600 ± 0.0118), which are components of this gate's estimator.
**The only quantities still blind are the (a_s, 1/L) surface
extrapolation κ_phys,eff, its goodness of fit, and its total
uncertainty** — the pass/fail-deciding numbers. The panel ratifies
(or rejects) this gate KNOWING the per-rung inputs; the verdict-
deciding extrapolation has not been computed and will not be until
ratification. (Worker attestation: no surface fit of the joint-pole
values has been run; the first such fit will be the gated one.)

## §1 — Frozen estimator (per the registered spec)

Per rung a_s ∈ {0.04, 0.02, 0.01, 0.005}:

1. **Real-space component:** rung-pooled profile on the FIXED
   PHYSICAL window (0.08, 0.546) fm (no a_s-dependent edge). Form
   selection: two-mode Yukawa sum if ΔAIC(two − one) ≥ 10 on the
   rung (per the committed battery procedure, verbatim), else single
   mode; κ_asym ≡ the smaller decay constant.
2. **k-space component:** κ_k² from the four smallest committed
   shells via k²(1/S_zz − 1), per-sample PA-1 blocks where they
   exist (all 0.02/0.01/0.005 new chains); for the archived 0.04
   rung, the MAIN-A/B between-chain spread ⊕ 1.5% floor model
   (DEV-1-ratified scope) supplies the k-side weight.
3. **Joint shared pole:** κ_phys(rung) = inverse-variance
   combination of κ_asym and κ_k under one shared pole (the
   committed battery req-4 machinery, verbatim, DEV-B1-fixed).
4. **Covariance model:** 24-block × 2000-resample bootstrap for
   every rung-level quantity (per-sample where PA-1 exists;
   profile-side blocks for archived chains, limitation stated).

**Surface and verdict (the blind stage):**
κ_phys(a_s, L) = κ_eff + c₁·a_s^p + c₂/L, p ∈ {1, 2} both reported,
AIC-selected. **GOF gate: the selected surface must achieve
χ²/dof ≤ 2.0; otherwise the gate returns UNRESOLVED (no
pass/fail).** The predefined a_s = 0.01 form-ambiguity treatment:
the rung enters the surface via its joint κ_phys regardless of its
form class (the k-side stabilizes the pole); its form class is
reported but does not gate.

**PR2-PHYS PASS:** κ_eff/κ_D ∈ [0.97, 1.03] AND total uncertainty
(bootstrap ⊕ |κ_eff(p=1) − κ_eff(p=2)|/2) ≤ 0.03 AND GOF gate met
AND the RV-4 staggering census remains zero on all consumed chains
(carried of record from leg 5). **FAIL:** κ_eff outside the band by
more than the total uncertainty with GOF met. **UNRESOLVED:**
anything else. Same-font in every branch; enactment into the PR
ledger occurs only via panel adjudication of the executed record.

## §2 — Ratification questions (per seat)

**R1.** Ratify this successor gate as PR2-PHYS (UPHOLD / AMEND with
wording / OVERTURN — including, if desired, amending the window,
shell count, GOF threshold, band, or requiring fresh chains)?
**R2.** Confirm the §0 disclosure is acceptable (per-rung inputs
known; extrapolation blind) — or require new-seed chains instead?

Execution follows a ≥3-seat majority; any seat's AMEND with majority
support binds before execution.
