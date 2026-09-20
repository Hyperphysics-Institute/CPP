#!/usr/bin/env python3
"""
Patch 4165 — TODO-4154-WHICHA. Which A enters b = A . V_i?

THREE READINGS, and they are physically different objects:
  (i)   the CP's OWN axial attribute (A1' as amended, 4120: "CPs carry the
        attribute")
  (ii)  the GP's A_i REGISTER -- the summed axial field from DI-bit arrivals,
        which is what the GP broadcasts
  (iii) the A carried by an individual arriving DI-bit (AP-4 payload)

The corpus does not say. 4154 argued (i) is required, from what F3 needs. This
patch tries to DECIDE it rather than argue it.
"""
import numpy as np
out=[]
def say(s=""): print(s); out.append(s)
rng=np.random.default_rng(4165)

say("T1  the decisive structural fact, from the founder's own cycle description")
say("    4152 verbatim: 'The GPs populate their register by computing/summing")
say("    the DI-bits ARRIVING FROM GPs at a PSR distance.' The register is built")
say("    from ARRIVALS. A GP's resident CP does not send itself a DI-bit, so")
say("    **the resident CP's own A is NOT in its own GP's register.**")
say("    Under reading (ii), b would therefore be built from the axial field of")
say("    the NEIGHBOURHOOD, with the particle's own spin absent from it.")
say()

say("T2  what that costs, computed: a free particle in an unpolarised sea")
say("    Under (ii), A_register = sum of N arriving axial contributions from a")
say("    sea with no net polarisation. Its magnitude grows as sqrt(N) while its")
say("    DIRECTION is random, uncorrelated with the particle's own spin.")
say(f"    {'N arrivals':>11}{'|<A_reg>| / sqrt(N)':>22}{'corr with own spin':>21}")
own=np.array([0.,0.,1.])
for N in (12,60,600,6000):
    M=20000
    arr=rng.normal(size=(M,N,3))
    reg=arr.sum(axis=1); reg/=np.linalg.norm(reg,axis=1)[:,None]
    say(f"    {N:>11}{np.linalg.norm(arr.sum(axis=1),axis=1).mean()/np.sqrt(N):>22.4f}"
        f"{(reg@own).mean():>21.4f}")
say("    The correlation with the particle's own spin is ZERO at every N.")
say("    So under (ii), for a free particle in an unpolarised sea, b carries NO")
say("    information about that particle's helicity. <b> over the ensemble is 0.")
say("    **Reading (ii) does not merely weaken V-A. It abolishes it.**")
say()

say("T3  reading (iii) is (ii) with N = 1")
say("    An individual arriving DI-bit carries a neighbour's A, not the")
say("    resident CP's. Same defect, worse statistics -- and it is the N = 1 row")
say("    that Patch 4161 already showed is not the physical regime.")
say()

say("T4  and reading (i) is what every standing result already assumed")
say("    4134 (nucleon <b> = 0 by the L=0 s-wave average of the CAGE's own")
say("      spins), 4135 (the bracelet's 64 spin assignments), 4157 (THEO-CHIR-1:")
say("      'positions, charges AND spins' of the configuration), 4158 (<b> =")
say("      (v/c)cos(theta), where A is the decaying particle's own spin axis).")
say("    Every one of them reads A as the CP's own. If (ii) were right, all four")
say("    would have to be redone, and 4158's agreement with the measured")
say("    polarisation law would be a coincidence.")
say()

say("T5  VERDICT")
say("    **A in b = A . V_i is the CP's OWN axial attribute -- reading (i).**")
say("    Decided, not merely argued, by T1+T2: the register is built from")
say("    arrivals, the resident CP does not send itself a DI-bit, so under (ii)")
say("    the particle's own spin is absent from its own bit and V-A vanishes.")
say()
say("    THE ASYMMETRY THIS EXPOSES, and it is a real structural point rather")
say("    than a tidy-up: b = A . V_i contracts a CP-LOCAL attribute with a")
say("    GP-HELD register. It is NOT a contraction of two register components,")
say("    and it is NOT a contraction of two CP attributes. The two factors come")
say("    from different objects in the cycle -- which is exactly why both are")
say("    present at the CP at the Moment of displacement (the GP stamps V_i on")
say("    it; it carries its own A) and why the bit is locally constructible.")
say()
say("    WHAT THIS LEAVES OPEN: the GP's A_i register is then NOT what b reads.")
say("    It still exists -- A3' broadcasts it, AP-4 transports it -- so what")
say("    does it do? On the evidence of Patch 4155's coupling census it sources")
say("    the A1.A2 spin-spin term, i.e. ORDINARY MAGNETISM, and nothing else")
say("    identified. That is a thin job for a broadcast channel and it is worth")
say("    asking whether the channel earns its place.")
open('/tmp/4165.txt','w').write('\n'.join(out))
