# Reasoning capture — Patch 1115 (spin-2 Step 4: run at the Einstein wall + emergent route)

**Protocol:** `templates/reasoning_capture_protocol.md`. Reasoning behind the run + the option-D reframe.

## The task (architect's challenge)
TLA: don't axiomatize the spin bit yet. First try to extract the Einstein GR equations from current
axioms via the Fourier-type superposition / second-order ('change on top of the change') of SSV
vectors. If that fails, reconsider the spin bit (possibly granularity-related). His instinct: spin bit
probably NOT needed; SM fermion spin already handled by ZBW.

## The run
Transverse SSV plane wave, helicity-2 = {h_xx-h_yy, h_xy}. (sympy)
(1) linear d_(i V_j): 0. (2) TLA 2nd-order V_iV_j: (a^2-b^2)cos^2 f, ab cos^2 f -> PRESENT but ~amp^2,
freq 2w. (3) grad-bilinear dV dV: 0 (T_zz only). => TLA's intuition has the right STRUCTURE (V_iV_j
carries helicity-2) but wrong SCALING (2nd order, double freq) -> not the linear observed GW. Wall
stands for any local polynomial in (phi,V).

## The principled opening (why TLA's instinct is still defensible)
A no-axiom helicity-2 can be EMERGENT/collective, not a local polynomial. Weinberg-Witten: a Lorentz-
covariant conserved T_munu forbids massless spin-2 composites -> no emergent graviton in a Lorentz-
invariant theory. BUT CPP has a preferred frame (lattice + Absolute Moment), Lorentz emergent (SR-1) ->
EVADES Weinberg-Witten. CPP is in the condensed-matter emergent-gravity class (Wen, Volovik). And it
matches CPP's pattern: fermion spin from ZBW, Lorentz from lattice -> spin-2 from collective dynamics.
Granularity intuition = the emergent long-wavelength mode.

## Honest caveat
Emergent gravitons are NON-GENERIC: standard lattice elasticity = scalar+vector phonons only, no spin-2.
Needs special structure; 600-cell H_g slot is a hint (1112) + shell-sum would propagate it (1113), but
unproven and hard. Default expectation = no emergent helicity-2 unless 600-cell is special. So option D
is a calculation to attempt, not a result.

## Reframed verdict
1114 said: closing (a) needs axiom A/B/C. 1115 adds option D (emergent, no axiom, WW-evaded, CPP-
consistent, non-generic). Decision sharpens: attempt the emergent-graviton calc (D) FIRST; axiomatize
(A/B/C) only if it fails. TLA's instinct = the option-D bet, principled.

## What I did NOT claim
- Did NOT claim CPP has an emergent graviton (it's an open, hard, non-generic calculation).
- Did NOT close op:einstein (a). NO VERDICT MOVED.
- Was honest that TLA's 2nd-order idea has right structure but wrong scaling (partial validation).

## Confidence
- Solid (computed): superposition/local-polynomial routes give no linear helicity-2; V_iV_j is 2nd-
  order/double-freq.
- Solid (theorem): WW + the preferred-frame evasion put CPP in the emergent-gravity-permitted class.
- Open/uncertain: whether the 600-cell collective dynamics actually realize an emergent TT mode.
