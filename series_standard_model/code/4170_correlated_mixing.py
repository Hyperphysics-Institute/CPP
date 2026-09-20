#!/usr/bin/env python3
"""
Patch 4170 — TODO-4166-MIXING: the TIGHT bound on the founder's spin-mixing
rule, for a CORRELATED environment.

4166 bounded A_next = normalise((1-eps) A + eps A_env) at eps <~ 1e-24 per
Moment, assuming A_env is RANDOM and uncorrelated Moment to Moment. That is the
DIFFUSIVE case: angular error accumulates as sqrt(eps^2 n).

In a POLARISED medium A_env has a persistent mean direction. The pull is then
BALLISTIC -- it accumulates as eps*P*n, not sqrt -- and the bound tightens by a
factor sqrt(n), which for Planck-rate Moments is enormous.
"""
import numpy as np
out=[]
def say(s=""): print(s); out.append(s)
t_P=5.391247e-44

say("Q1  diffusive vs ballistic, the scaling")
say("    unpolarised environment:  <theta^2> ~ eps^2 n        -> eps <= sqrt(tol/n)")
say("    polarised environment:    theta     ~ eps P n        -> eps <= tol/(P n)")
say("    ratio of the two bounds = sqrt(n)/P  -- and n is t/t_P.")
say()
say(f"    {'system':<34}{'t (s)':>9}{'n = t/t_P':>12}{'sqrt(n)':>11}")
for nm,t in (("neutron crossing a foil",1e-9),("muSR in a magnetised sample",1e-5),
             ("nuclear spin in a ferromagnet",1e0)):
    n=t/t_P
    say(f"    {nm:<34}{t:>9.0e}{n:>12.2e}{np.sqrt(n):>11.2e}")
say("    So the ballistic bound is 17 to 21 orders tighter than the diffusive one.")
say()

say("Q2  the numbers")
say(f"    {'system':<32}{'t (s)':>8}{'P':>6}{'tol (rad)':>11}{'eps <=':>11}")
rows=[("neutron, polarised foil",1e-9,0.1,1e-3),
      ("muSR, magnetised sample",1e-5,0.1,1e-4),
      ("nuclear spin, ferromagnet",1e0,0.5,1e-2),
      ("muon g-2 storage ring",1e-5,0.01,1e-10)]
best=1e99
for nm,t,P,tol in rows:
    n=t/t_P; eps=tol/(P*n); best=min(best,eps)
    say(f"    {nm:<32}{t:>8.0e}{P:>6.2f}{tol:>11.0e}{eps:>11.1e}")
say()
say(f"    TIGHTEST: eps <= {best:.1e} per Moment.")
say(f"    Against 4166's diffusive bound of ~1e-24, that is "
    f"{1e-24/best:.0e} times tighter.")
say()

say("Q3  what the tight bound does to the proposal")
say("    The founder's rule survives -- nothing here forbids it -- but at")
say(f"    eps <~ {best:.0e} the environmental term changes a spin by less than one")
say("    part in 1e46 per Moment. Over the ~1e34 Moments a neutron spends")
say("    crossing a foil that is a total rotation below 1e-3 rad BY CONSTRUCTION,")
say("    i.e. the bound is saturated exactly where it was set and the term is")
say("    unobservable everywhere else.")
say()
say("    THE CONSEQUENCE FOR TODO-4165-CHANNELJOB, and it is not encouraging.")
say("    4166 offered the spin-evolution rule as the A_i register's SECOND JOB,")
say("    beyond sourcing ordinary magnetism. That job is real but its magnitude")
say("    is now bounded to irrelevance: the register can rotate a spin, but only")
say("    by an amount no experiment could ever see. A channel whose two jobs are")
say("    (a) reproduce magnetism the corpus already had and (b) an effect bounded")
say("    below 1e-37 per Moment is still a channel looking for work.")
say()

say("Q4  WHERE A REAL TEST WOULD HAVE TO COME FROM -- and it is not this")
say("    The bounds above are set by ALREADY-EXPLAINED relaxation: every system")
say("    listed has its measured rate accounted for by known magnetic")
say("    interactions, so eps is bounded by the RESIDUAL, not by the rate. To")
say("    turn this into a prediction rather than a bound one needs a system where")
say("    (i) the known mechanisms are computable to high precision, and (ii) the")
say("    environmental polarisation P can be VARIED while everything else is held")
say("    fixed -- because eps enters as eps*P*n, so the CPP term is the part of")
say("    the relaxation rate LINEAR IN THE MEDIUM'S POLARISATION.")
say("    That is a genuine experimental signature and it is the first one this")
say("    session has found that is not already excluded. It is also far beyond")
say("    what the numbers above could reach: a 1e-37 effect is not measurable by")
say("    varying P over any accessible range.")
say("    Stated plainly: THE SIGNATURE EXISTS IN PRINCIPLE AND IS UNREACHABLE IN")
say("    PRACTICE by the systems considered here.")
open('/tmp/4170.txt','w').write('\n'.join(out))
