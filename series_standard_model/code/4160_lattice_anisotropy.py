#!/usr/bin/env python3
"""
Patch 4160 — TODO-4159-CRYSTAL link 2, and it turns into a possible falsifier.

LINK 2 ASKED: is the substrate lattice's orientation tied to a material
crystal's? Answer: NO, and for a reason that makes things worse rather than
better. The 600-cell has spacing l_P ~ 1.6e-35 m; a material crystal ~1e-10 m,
25 orders larger. A material crystal cannot orient the substrate. But the
substrate does not need orienting: IT ALREADY HAS A GLOBAL ORIENTATION. Every GP
has the same twelve neighbours pointing the same twelve ways, everywhere.

So Patch 4159's orientation-averaging -- which is what rescued
<b> = (v/c)cos(theta) -- IS NOT AVAILABLE. There is nothing to average over.
"""
import numpy as np
out=[]
def say(s=""): print(s); out.append(s)
rng=np.random.default_rng(4160)
PHI=(1+5**0.5)/2
ico=[]
for s1 in (1,-1):
    for s2 in (1,-1):
        ico += [[0,s1,s2*PHI],[s1,s2*PHI,0],[s2*PHI,0,s1]]
ico=np.array(ico,float); ico/=np.linalg.norm(ico,axis=1)[:,None]

say("R1  the corpus's own no-preferred-direction argument, and what it proves")
say("    founders_vision: 'The 600-cell is the same in every direction at every")
say("    vertex -- each GP has the same twelve neighbours arranged the same way.")
say("    So when a CP displaces, it has no built-in bias toward any neighbour.'")
say("    That establishes VERTEX-TRANSITIVITY. It does NOT establish DIRECTIONAL")
say("    isotropy: the twelve neighbours point in twelve SPECIFIC directions, and")
say("    those directions are the same at every vertex -- which is precisely a")
say("    GLOBAL ORIENTATION, not the absence of one.")
say()

say("R2  why nobody has noticed: the 12-set is a spherical 5-DESIGN")
A=rng.normal(size=(50000,3)); A/=np.linalg.norm(A,axis=1)[:,None]
say(f"    {'observable':<34}{'spread over directions':>24}")
for deg in (2,4,6):
    v=np.mean((A@ico.T)**deg,axis=1)
    say(f"    {'polynomial moment, degree '+str(deg):<34}{v.max()-v.min():>24.2e}")
say("    Degrees 2 and 4 are direction-independent to 1e-16 -- EXACTLY isotropic.")
say("    Degree 6 breaks it (4.7e-2), as a 5-design must.")
say("    **Every observable CPP has tested is polynomial and low-degree.** That")
say("    is why SR-1's emergent Lorentz invariance has held: the lattice IS")
say("    isotropic to everything anyone has asked it.")
say()

say("R3  but b is SIGN-VALUED, and sign() is not a polynomial")
say(f"    {'beta':>6}{'mean over dirs':>16}{'min':>9}{'max':>9}{'SPREAD':>9}")
A=rng.normal(size=(200000,3)); A/=np.linalg.norm(A,axis=1)[:,None]
for beta in (0.1,0.2,0.3,0.5,0.7,0.9):
    v=np.sign(A@ico.T + beta).mean(axis=1)
    say(f"    {beta:>6.1f}{v.mean():>16.4f}{v.min():>9.4f}{v.max():>9.4f}{v.max()-v.min():>9.4f}")
say("    The MEAN over directions is beta -- 4158's law. But the SPREAD is")
say("    0.17 to 0.50, i.e. 17-50% of full polarisation, DEPENDING ON DIRECTION.")
say("    **b is the first observable in CPP that can see the lattice's")
say("    anisotropy**, because it is the first that is not a low-degree")
say("    polynomial. The amendment introduced it.")
say()

say("R4  what this predicts, and it is not a small prediction")
say("    The lattice orientation is a GLOBAL CONSTANT. A laboratory direction")
say("    sweeps relative to it as the Earth rotates. So the measured longitudinal")
say("    polarisation of beta-decay electrons should show a SIDEREAL MODULATION")
say("    with ICOSAHEDRAL structure, of amplitude tens of percent at beta ~ 0.2-0.7.")
say("    Nothing in the Standard Model produces that. Nothing in the data shows it.")
say()
say("    THIS IS A FALSIFIER-CLASS PROBLEM, NOT A PREDICTION TO CELEBRATE. Beta")
say("    polarimetry has been done since 1957 and Lorentz-violation searches bound")
say("    spin-direction sidereal effects at the 1e-33 GeV level (the He3-Xe129")
say("    comagnetometer bound used at Patch 4139). A tens-of-percent modulation")
say("    would have been seen a lifetime ago.")
say()

say("R5  the escapes, and what each would cost")
say("    (a) b is NOT read per-Moment per-edge, but only after averaging over many")
say("        Moments in which the CP's own orientation relative to the lattice")
say("        changes. Requires a mechanism that decorrelates cage orientation from")
say("        the lattice -- but the cage OCCUPIES lattice vertices, so its")
say("        orientation is lattice-locked by construction. Hard.")
say("    (b) The displacement direction is NOT restricted to the 12 edges at the")
say("        Moment b is evaluated -- i.e. the 12-edge selection rule and the")
say("        b-evaluation happen at different stages. Cheap if true, but it")
say("        contradicts c03/GR-1b as written.")
say("    (c) b enters observables only through quantities that ARE low-degree")
say("        polynomial in b -- but B3 says the response is LINEAR in b, and")
say("        linear-in-sign is exactly the non-polynomial case. Contradicts B3.")
say("    (d) The substrate lattice has DOMAINS smaller than a laboratory, so a")
say("        real measurement averages over orientations after all. Nothing in the")
say("        corpus proposes domains, and they would have their own signatures.")
say()
say("    I do not know which, if any, is right. (b) is the cheapest and (d) the")
say("    most speculative. What I am confident of: as the corpus stands, the")
say("    combination {12-edge selection + b = sign(A.V) + B3 linearity + a")
say("    globally oriented lattice} predicts an effect that is not observed.")
open('/tmp/4160.txt','w').write('\n'.join(out))
