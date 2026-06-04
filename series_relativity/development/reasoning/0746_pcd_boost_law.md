# Reasoning capture — Patch 0746: PCD boost-law derivation — the count-vs-stress fork

*Session 154. The decisive PCD-level derivation. Writeup: `.../development/pcd_boost_law_finding.md`.
Toy: `.../scripts/0746_pcd_derive_boost_law.py`. NO THEO.*

## How I worked it (and an honesty correction mid-derivation)

Grounded in the glossary: displacement is driven by SSV_net (vector, cancels under balance); SSV_abs is
the magnitude (sets PSR/gravity, does not cancel); the early cohort is net-neutral; and crucially the
boost acts on PSR_base, the SSV-INDEPENDENT baseline (PSR_eff = PSR_base/(1+alpha SSV_abs)).

First pass I leaned flatly NEGATIVE: CPP displacement is SSV-mediated, so the boost is mechanical
(SSV_abs~n -> n_s=-5; SSV_net~sqrt n even neutral -> n_s=-2), excluded. And I showed the charge-
neutrality hope (0745) FAILS: residual sqrt(n) fluctuations dwarf the entropic ln(n) by ~35 orders.

Then I caught the over-negativity: the boost acts on PSR_BASE, which is SSV-INDEPENDENT by construction.
So a reading where the baseline reach relaxes by the occupation COUNT n (configurational, decoupled from
the SSV field) is legitimate -- arguably more natural than tying a baseline-geometry change to the
instantaneous stress. That count-driven reading gives the entropic ln(n) -> 0.9649, and the residual-
fluctuation problem does NOT apply (count-driven, not field-driven). So it is a genuine FORK, not a flat
negative.

## The fork (the honest result)

(i) COUNT-driven / configurational: h ~ ln n -> n_s = 0.9649. Defensible (PSR_base is SSV-independent).
(ii) SSV-STRESS-driven: h ~ n or sqrt(n) -> n_s = -5 or -2, EXCLUDED; neutrality cannot save it.
Data REQUIRE (i). (i) is structurally defensible. (ii) is the everything-is-SSV default and is excluded.

## Decisive new content vs 0745
0745 hoped neutrality exposes the entropic log. 0746 shows: for the STRESS reading, neutrality fails
(sqrt(n) residual buries ln n by ~35 orders). The entropic log operates ONLY in the count-driven reading,
which is legitimate because PSR_base is SSV-independent. So the escape is real but specific.

## Honesty boundary
- Reported as a FORK, not a win and not a kill. Did not claim 0.965 is predicted (depends on the count-
  vs-stress coupling, undetermined). Did not flatly bury it either (the count-driven reading is
  defensible). Both correction directions logged.
- Scaling-level analysis of a separately-posited mechanism (H-engine), NOT a closed PCD solution. A
  sharpened fork, not a theorem. Stated explicitly.
- NO THEO; no prediction registered (conditional on the count-driven coupling).

## Pointer
- THE deciding computation: do the PCD rules grow PSR_base from occupation COUNT (-> ln n -> 0.965,
  zero-parameter since N_* CP-fixed) or from the SSV STRESS field (-> mechanical -> excluded)? Single
  coupling question; closes or breaks the spectrum thread. Clear of chirality. PCD = Perceive/Compute/Displace.
