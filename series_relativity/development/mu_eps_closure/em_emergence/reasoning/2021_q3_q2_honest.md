# Reasoning capture — Patch 2021: Q3/Q2 honest result (retraction of the R2 PASS)

**STATUS: verbatim (captured at-patch).** Window: 2000-band. Opus worker; integrator = Thomas.

## What happened
Thomas asked me to engage Q3 then Q2. I started Q3 by dropping the mu0~alpha_B analogy and using only the
identity Z0 = 1/(eps0 c) with the solid eps0~1/C, giving Z0 = C/c. That reduces R2 to: is c~C exactly?
Reading the VSL files to get c(C), I hit dp_sea_mu_eps_symmetry.md line 97: the corpus's own value is
c~sqrt(C). Z0 = C/sqrt(C) = sqrt(C) -> carries C -> FAIL. The PASS needed c~C exactly, which only the
2016 impedance route gave -- and that route DERIVED c~C from mu0~alpha_B~1/C, the analogy under test.
Circular.

## The discipline I held (this is the important part)
This reverses 2016/2017/2018, which I built. The temptation is to find a reason c~C after all. I checked
honestly: c~C requires m~1/C mechanically, which NO CPP scheme gives (fixed-omega0 -> m~+C -> c=const ->
FAIL; fixed-m -> c~sqrt(C) -> FAIL). So c~C is mechanically unnatural; the grounded options all FAIL. I
followed the numbers to a retraction rather than protecting my prior result.

## Root errors found in our own chain
1. 2002 virial: <KE>=<PE> is equipartition = the identity mu0 eps0=1/c^2, NOT Z0-geometricity. The "C
   cancels in the ratio" claim conflated the product (automatic) with the ratio (the actual question).
2. 2002 internal inconsistency: it claims BOTH Z0-geometric AND c~sqrt(C); given eps0~1/C these are
   incompatible (they force eps0~1/sqrt(C)). The casualty is "Z0 geometric."
3. 2016: mu0~alpha_B predicts c~C, contradicting the grounded c~sqrt(C). The PASS lived in that contradiction.

## Verdict, stated plainly
R2 is NOT closed to PASS. It is OPEN, leaning FAIL (grounded c~sqrt(C) -> Z0~sqrt(C) -> k_alpha~0.5, ~6
orders over the clock-LPI bound). It revives to PASS only if c~C is independently and self-consistently
grounded, which it currently is not. The 2016/2017/2018 PASS conclusions are retracted (the exercises
stand; the conclusion does not).

## What I owe and did
- Wrote the retraction finding; downgraded the em_emergence-local status docs (MU0/R2-STATUS/scope).
- Flagged for the integrator: the 0740/2002 internal inconsistency + the OPEN-COSMO-DM-2 "R2 resolved"
  wording that now needs correcting. Did NOT edit those shared files (worker discipline).
- This is the rigor upgrade Thomas asked for doing exactly its job: it found that the PASS was circular.
  Better now, in a development note, than after the corpus leaned on it or it shipped in SF-6.

## Discipline
- Owned paths only. NO THEO. Honest negative; not tasted. Files via bash; git status verified.
