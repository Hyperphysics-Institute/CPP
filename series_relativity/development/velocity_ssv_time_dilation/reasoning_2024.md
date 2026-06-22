# Reasoning capture — Patch 2024: photon != phonon; R2 FAIL reopened, VTD-1/2 resolved

**STATUS: verbatim (captured at-patch).** Window: 2000-band. Opus worker; integrator = Thomas.

Thomas asked me to do the velocity calculations and see if any machinery is missing. I went in willing to
confirm the 2021 FAIL. The numbers instead reopened it -- and I followed them, the same way I followed them
INTO the FAIL in 2021. This is the integrity working in the other direction.

What I found:
1. VTD-1: the quadrature (Pythagorean) budget split gives EXACTLY gamma (verified 1e-9). The linear form
   doesn't. SR-1 has the quadrature structure. PASS conditional on orthogonality.
2. VTD-2: velocity alpha is a Lorentz scalar, so given VTD-1 it's preserved automatically. NOT an
   independent gate. I corrected my prior-patch overstatement that "VTD-2 = R2" -- for velocity it's
   protected by scalar invariance; gravity has no such protection.
3. R2 (the big one): the 2021 FAIL used c ~ sqrt(C) = the DP-lattice PHONON (acoustic) speed sqrt(C/m)a.
   But c06 says the PHOTON advances PSR/Moment = the BUDGET speed, and 2011 established photon != phonon.
   So 2021 plugged the phonon speed into the photon's impedance -- a category error. The photon speed's
   C-dependence is undetermined (set by the unspecified DeltaSSV<->C relation), NOT sqrt(C). So "Z0~sqrt(C),
   leaning FAIL" is not secure; the honest statement is R2 OPEN.

The resolution this points to (grounded, not tasted): c06 (photon=budget) + SR-1 (matter=budget) imply
light and matter draw from the SAME budget, so they co-scale under SSV -> alpha invariant while c varies ->
VSL + R2-PASS together. That's the unified-budget principle.

Discipline against tasting: I did NOT claim this revives R2 to PASS. It shows the FAIL was insecure and names
the route. R2 is OPEN, with remaining work (the DeltaSSV<->C relation + eps0 co-scaling). I was careful to
state the arc honestly: PASS(circular) -> FAIL(phonon category error) -> OPEN(photon!=phonon). I'm reopening
my own retraction because the physics says the retraction's positive claim (c~sqrt(C)) used the wrong mode --
not because OPEN is a nicer answer than FAIL.

Action: wrote the finding; updating R2-STATUS (leaning-FAIL -> OPEN) + the velocity DISCUSSION note's gates
(VTD-1 conditional-PASS, VTD-2 resolved). Flagged for integrator: the OPEN-COSMO-DM-2 / CONJ wording (R2 is
OPEN not FAIL not resolved). NO THEO.

Discipline: owned paths (velocity_ssv_time_dilation/, mu_eps_closure R2-STATUS). Files via bash; verified.
