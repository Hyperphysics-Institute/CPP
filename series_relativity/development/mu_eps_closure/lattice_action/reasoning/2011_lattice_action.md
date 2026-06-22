# Reasoning capture — Patch 2011: R2 lattice-EM action attempt (an honest negative)

**STATUS: verbatim (captured at-patch).** Window: 2000-band. Opus worker; integrator = Thomas.

## The instruction and the pressure
Thomas: take R2 the rest of the way (c06 action -> screening bound -> round-3), NOT by tasting. After an
arc of increasingly confident heuristics (2002 virial, 2008 shared-Coulomb, panel CONFIRM at leading
order), the pull was to produce a lattice action that "closes" it. That is exactly the tasting trap.

## What I did and the moment I caught myself
I built a corpus-grounded lattice action and integrated it out. My FIRST draft of the script's verdict text
asserted "explicit C cancels in Z0 (geometric)" -- the result I expected. Then I read the actual numbers:
Z0 = 2.08, 4.17, 8.34, 16.68 across an 8x Q sweep. Z0 ~ Q. It does NOT cancel. I had written the expected
conclusion, not the computed one. I caught it, rewrote the verdict to match the numbers, and reran. This is
the single most important thing in this patch: the numbers refuted my expectation and I followed the
numbers.

## The honest result
The naive construction (photon = transverse acoustic mode) reproduces NEITHER the 2002/2008 geometric-Z0
(it gives Z0~Q) NOR the VSL c-variation (c comes out geometric). The PSR channel moves c but gives A=-1.
Diagnosis: a DP-lattice acoustic mode is a phonon, not a photon -- the construction mis-identifies the EM
emergence. So the pair-potential/virial cancellation does NOT survive into this action, exactly ChatGPT's
warning.

## What this means, stated without flinching
This DEEPENS the residual rather than closing it. The 2002/2008 geometric-Z0 is revealed as a HEURISTIC the
correct action must reproduce -- and a naive action does not, so it is currently UNCONFIRMED at the action
level. R2's full PASS is blocked on the c06 EM-EMERGENCE mechanism (how a gapless photon emerges, which
parameter the VSL varies, whether it enters eps0 and mu0 symmetrically) -- deeper than the stiffness ratio
or the screening. Steps 2 and 3 of Thomas's plan are not reachable until step 1 (the action) is, and step 1
is blocked on the emergence construction.

## Why I report a negative instead of a closure
The whole arc's credibility rests on not faking the one genuinely open thing. I could have shipped the
first-draft "Z0 cancels" text and called R2 closed. The numbers said otherwise. Reporting the negative --
and that it slightly deepens the residual -- is the only honest move. R2 stays REVISE; the leading-order
K∝C (panel-confirmed) stands; the action-level geometric-Z0 is now explicitly unconfirmed; the real
prerequisite is the c06 EM-emergence derivation, which I did not have and did not fabricate.

## Discipline
- Worker patch, owned path mu_eps_closure/lattice_action/ only. NO edit to c06/CONJ/0740/EW-5/R2-STATUS
  (the status update is described here; the canonical R2-STATUS edit is left for a consolidation patch /
  integrator). NO THEO. Files via bash; git status verified.
