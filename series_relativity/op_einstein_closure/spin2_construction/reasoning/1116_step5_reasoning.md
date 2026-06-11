# Reasoning capture — Patch 1116 (spin-2 Step 5: the emergent-graviton verdict)

**Protocol:** `templates/reasoning_capture_protocol.md`. Reasoning behind the decisive option-D verdict.

## The task
Architect asked: attempt option D (emergent graviton) before axiomatizing. Build the long-wavelength
effective theory of the scalar+vector field on the 600-cell lattice; does a propagating helicity-2 mode
emerge? Outcome determines whether the spin-bit axiom is necessary.

## The chain
1. Per-site d.o.f. = scalar(1)+vector(3)=4 -> D(k) is 4x4 -> exactly 4 propagating branches.
2. Little-group (SO(2) about k) helicity classification: scalar->0; V_par->0; V_perp(2)->+/-1. Max |h|=1.
   Helicity-2 needs an e^{+/-2i theta} basis vector -- absent from span{phi,Vx,Vy,Vz}.
3. Explicit D(k) (sympy) with general icosahedral nearest-neighbor couplings (c_s,lambda,mu,g),
   k along the 5-fold axis: phi mixes only to V_z (helicity 0); transverse (Vx,Vy) block off-diagonal
   = 0 -> pure helicity-1 doublet, no Vx-Vy quadrupole channel. Branches = {0,0,+1,-1}.
4. Couplings set dispersions, NOT helicity content (fixed by representation). => no emergent helicity-2,
   for ANY couplings.
5. Composite/bilinear already excluded (1115: 2nd order, double freq). All no-axiom routes closed.

## Verdict
Option D FAILS. Closing op:einstein (a) / matching observed tensor GW polarizations REQUIRES a
fundamental rank-2 d.o.f. (spin-bit axiom, A/B/C). The architect's instinct (no spin bit) is refuted;
his FALLBACK intuition (granularity insufficient) is exactly right -- the per-GP info (scalar magnitude
+ vector direction) is representationally too poor to host spin-2.

## Framing (honest + fair)
NOT a defect of CPP: every successful gravity theory has a FUNDAMENTAL spin-2 (the metric); emergent
gravitons are the rare exotic case needing large local Hilbert spaces. CPP needing a fundamental rank-2
d.o.f. places it WITH mainstream gravity. Weinberg-Witten evasion (1115) made D permitted but not
realized -- permission necessary, not sufficient.

## What I did NOT claim
- Did NOT refute CPP; determined ONE axiom is needed (normal in physics).
- Did NOT move any verdict/THEO/PRED/count. (b)/(b') CC local half unaffected.
- The axiom CHOICE (A/B/C) + its form + source coupling remain the architect's deliberate step.

## Confidence
- Solid (representation theory + explicit D(k)): scalar+vector lattice has modes {0,0,+/-1}, no spin-2,
  for any couplings. This is robust.
- The conclusion (spin-bit axiom necessary) follows rigorously, conditional only on the established fact
  that the per-GP d.o.f. is scalar+vector (architect-confirmed, corpus-confirmed 1114).
