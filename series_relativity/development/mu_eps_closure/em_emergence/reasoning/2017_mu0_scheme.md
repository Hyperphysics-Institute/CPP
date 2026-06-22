# Reasoning capture — Patch 2017: deriving the μ₀-emergence scheme from c06 (the 2016 gate)

**STATUS: verbatim (captured at-patch).** Window: 2000-band. Opus worker; integrator = Thomas.

## The job and the trap
Thomas: derive the mu0-emergence scheme from c06 -- the gate that converts 2016's conditional-PASS to PASS.
The trap: 2016 ASSUMED mu0~alpha_B (symmetric, PASS). I must DERIVE which scheme c06 forces, not pick the
one that passes. The honest fork: mu0 ~ compliance (1/C, PASS) vs mu0 ~ kinetic inductance (m~C, FAIL).

## What I found, and the subtlety I did NOT paper over
Two independent c06-grounded arguments:
1. VSL-consistency: CPP commits to VSL (EU-1: c varies). With eps0~1/C, the kinetic scheme mu0~C gives
   mu0 eps0 = const => c FIXED => no VSL. So VSL EXCLUDES the kinetic FAIL scheme. BUT -- and the script
   made me see this -- VSL alone does NOT uniquely give PASS: a FLAT mu0 (S0) also gives VSL yet still
   FAILs R2 (Z0~sqrt(C)). So VSL-consistency is necessary but not sufficient; I said so rather than
   overclaiming "VSL <=> PASS."
2. c06 forces S1 over S0: (a) the photon is RECONSTRUCTED each Moment from the frozen displacement config
   (lines 103-104,110), NOT inertially transported -> mu0 is a compliance (~1/C), not a kinetic inductance
   (~m); (b) line 91 states explicitly "mu0,eps0 share one DP stiffness" -> mu0 depends on C the same way
   eps0 does (both ~1/C), excluding the flat S0. Together -> S1 -> PASS.

## The deepest honest statement
The kinetic FAIL scheme is excluded TWICE (by VSL and by reconstruction), and the surviving scheme is the
same mu0~1/C that powers VSL. So R2 is NOT an independent falsifier: it can only fail by also killing VSL.
Conditional on CPP's standing VSL commitment, R2 PASSES. That's a real reduction -- the impedance falsifier
and the horizon mechanism are welded by one scaling.

## Where I held back
This closes the gate at the level of c06's STATED mechanism + the VSL commitment. It does NOT derive mu0
from the DI-bit reconstruction DYNAMICS explicitly (line 91 is a corpus assertion I lean on). That full
derivation is the residual depth of OPEN-SR-9 -- a rigor upgrade, not a gate -- and the natural content of
SF-6. I flagged it as such and did not call it first-principles closure. Recommended round-3 panel review of
the lock before the corpus leans on it.

## Discipline
- Worker patch, owned path mu_eps_closure/em_emergence/ only. Proposed c06 cross-ref deferred to integrator
  (finding section 6). NO THEO (conditional + consistency; fixed-omega0/VSL are existing c02/EU-1). Files
  via bash; git status verified.
