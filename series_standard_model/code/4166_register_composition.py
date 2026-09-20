#!/usr/bin/env python3
"""
Patch 4166 — the founder corrects Patch 4165's premise, and the verdict has to
be re-derived on a sound one.

FOUNDER, 20 Sep: "The CP must communicate its presence to the GP for computation
of the DI-bit imprint. The CP on the GP would also need to communicate its axial
vector to the GP so that it can sum its influence with the DI-bits received each
Moment."

HE IS RIGHT AND 4165 SECTION 2 IS WRONG. If the GP did not know its resident
CP's attributes it could not imprint them on outgoing DI-bits, and then a charge
could not radiate its presence at all -- EM would not work. So the register IS
(own CP) + (arrivals), and 4165's "the CP's own A is not in its own GP's
register" is withdrawn.

DOES THE VERDICT SURVIVE? Re-derived below on the corrected composition, and it
does -- for a DIFFERENT and better reason: DILUTION.
"""
import numpy as np
out=[]
def say(s=""): print(s); out.append(s)
rng=np.random.default_rng(4166)
own=np.array([0.,0.,1.])

say("U1  the register's composition, corrected")
say("    A_register = w_own * A_CP  +  sum over N arrivals of neighbour axials.")
say("    In an UNPOLARISED sea the arrivals sum to a random vector of magnitude")
say("    ~ sqrt(N) while A_CP is a single unit contribution. So the register's")
say("    correlation with the CP's own spin is DILUTED by the neighbour count.")
say()
say(f"    {'N arrivals':>11}{'corr(register, own spin)':>27}{'-> V-A would be':>18}")
M=200000
for N in (4,12,60,600):
    arr=rng.normal(size=(M,N,3)).sum(axis=1)
    reg=own+arr
    reg=reg/np.linalg.norm(reg,axis=1)[:,None]
    c=(reg@own).mean()
    say(f"    {N:>11}{c:>27.4f}{c*100:>17.1f}%")
say()
say("    THE REPAIRED ARGUMENT. If b read the REGISTER's axial content, the")
say("    helicity signal would be diluted by exactly this factor: at the generic")
say("    N = 12 the register is only ~15% correlated with the particle's own")
say("    spin, so V-A would be ~15% of maximal, not 100%.")
say("    **The measured coupling is maximal. So b reads the CP's OWN A.**")
say("    4165's verdict stands; 4165's reason does not.")
say()

say("U2  the founder's MIXING proposal, and the bound it must respect")
say("    'the two add, the environmental axial vector and the CP axial vector")
say("     mix in some proportion, and that is the axial vector carried by the CP")
say("     to its next location after the V_i displacement.'")
say("    This is a SPIN-EVOLUTION rule: A_next = normalise((1-eps) A + eps A_env),")
say("    with A_env random in an unpolarised sea. It is exactly what would")
say("    produce spin relaxation -- and spin relaxation is measured.")
say()
say("    Random-walk estimate: angular diffusion per Moment ~ eps^2, so the")
say("    accumulated variance after n Moments is ~ eps^2 n and coherence is lost")
say("    when eps^2 n ~ 1.")
t_P=5.391e-44
cases=[("muon g-2 storage ring", 1e-5, 1e-10),
       ("neutron polarimetry flight", 1e-1, 1e-3),
       ("electron spin in a Penning trap", 1e3, 1e-6)]
say(f"    {'experiment':<32}{'t (s)':>9}{'tolerance':>11}{'n Moments':>12}{'eps <=':>11}")
for nm,t,tol in cases:
    n=t/t_P
    eps=np.sqrt(tol/n)
    say(f"    {nm:<32}{t:>9.0e}{tol:>11.0e}{n:>12.2e}{eps:>11.1e}")
say()
say("    **The environmental mixing fraction is bounded below ~1e-24 per Moment.**")
say("    So the founder's mixing is allowed -- but only at a level where the CP's")
say("    own A is conserved to 24 decimal places per Moment. The environment")
say("    cannot meaningfully rotate a spin on the Moment timescale.")
say()

say("U3  what that buys, and it is not nothing")
say("    (a) It REPAIRS 4165 without changing its answer, on a premise the")
say("        founder supplied rather than one I mis-assumed.")
say("    (b) It gives the A_i register a SECOND job beyond magnetism, which is")
say("        what TODO-4165-CHANNELJOB was asking for: the register is the")
say("        environmental term in the spin-evolution rule. Thin, but real.")
say("    (c) It makes spin relaxation a CPP observable with a number attached.")
say("        Any measured spin-relaxation rate that is NOT accounted for by")
say("        known mechanisms would bound eps from BELOW -- i.e. the rule is")
say("        falsifiable, not merely permitted.")
say()
say("U4  WHAT I HAVE NOT DONE")
say("    The eps bound is a random-walk ESTIMATE, not a derivation from the")
say("    corpus's own DI-bit statistics: I assumed A_env is random and")
say("    uncorrelated Moment to Moment. If environmental axials are CORRELATED")
say("    over many Moments -- which a nearby polarised medium would make them --")
say("    the walk becomes ballistic and the bound tightens by a further factor")
say("    of sqrt(n). That is the case worth computing next, and it is where a")
say("    real prediction would live.")
open('/tmp/4166.txt','w').write('\n'.join(out))
