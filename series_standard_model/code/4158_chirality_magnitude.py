#!/usr/bin/env python3
"""
Patch 4158 — TODO-4157-CHIRMAG: the MAGNITUDE half. THEO-CHIR-1 said when a
parity-odd effect is allowed; this asks how big it is.

THE IDEA. b is a BIT -- sign(A.V), two-valued by construction (A1'). A CP's
SSV_disp at any Moment is its ZBW circulation (magnitude ~ c) PLUS its drift
(magnitude v). So b is not constant over a ZBW cycle: it flips whenever the
circulation carries A.V through zero, and the drift BIASES the fraction of the
cycle spent on each sign. The observable is that time-average <b>, and its size
is set by v/c with no free parameter.

WHAT IT MUST REPRODUCE. The textbook V-A result, measured since Frauenfelder
1957: the longitudinal polarisation of the emitted electron is P = -v/c, and for
a spin axis at angle theta to the momentum the asymmetry goes as (v/c) cos theta.
"""
import numpy as np
out=[]
def say(s=""): print(s); out.append(s)
rng=np.random.default_rng(4158)
N=4_000_000

say("P1  the construction, stated before any number is computed")
say("    V = c * u_hat(t)  +  v_drift ,  b = sign(A . V)")
say("    u_hat is the ZBW circulation direction at that Moment. Averaging b over")
say("    a cycle gives <b>, the measurable asymmetry. No parameter is free: the")
say("    only input is the MEASURE of u_hat on the sphere, i.e. the ZBW geometry.")
say()

def avg_b(beta, cos_theta, measure, n=N):
    A = np.array([np.sqrt(max(0,1-cos_theta**2)), 0.0, cos_theta])
    if measure == 'isotropic':
        u = rng.normal(size=(n,3)); u /= np.linalg.norm(u,axis=1)[:,None]
    elif measure == 'planar_perp':        # circulation in the plane normal to A
        phi = rng.uniform(0,2*np.pi,n)
        e1 = np.array([cos_theta,0,-np.sqrt(max(0,1-cos_theta**2))]); e2=np.array([0,1.,0])
        u = np.cos(phi)[:,None]*e1 + np.sin(phi)[:,None]*e2
    elif measure == 'planar_par':         # circulation in a plane CONTAINING A
        phi = rng.uniform(0,2*np.pi,n)
        u = np.cos(phi)[:,None]*A + np.sin(phi)[:,None]*np.array([0,1.,0])
    V = u + np.array([0,0,beta])          # units of c
    return np.sign(V @ A).mean()

say("P2  which ZBW measure reproduces P = v/c ?  cos(theta) = 1")
say(f"    {'beta = v/c':>11}{'isotropic':>12}{'planar_perp':>13}{'planar_par':>12}{'target v/c':>12}")
for beta in (0.05,0.2,0.5,0.8,0.95):
    row=[avg_b(beta,1.0,m) for m in ('isotropic','planar_perp','planar_par')]
    say(f"    {beta:>11.2f}{row[0]:>12.4f}{row[1]:>13.4f}{row[2]:>12.4f}{beta:>12.2f}")
say()
say("    ISOTROPIC reproduces <b> = beta = v/c EXACTLY, at every speed.")
say("    The reason is elementary once seen: for u_hat uniform on the sphere,")
say("    A.u_hat is UNIFORM on [-1, 1] (Archimedes' hat-box theorem), so")
say("        <b> = P(A.u > -beta) - P(A.u < -beta) = (1+beta)/2 - (1-beta)/2 = beta.")
say("    A circulation NORMAL to the spin axis gives sign(beta) -- maximal at all")
say("    speeds, contradicting measurement. One CONTAINING the spin axis gives")
say("    the arcsine law (2/pi) arcsin(beta), also wrong.")
say()

say("P3  the angular law: does (v/c) cos(theta) come out too?")
beta=0.5
say(f"    beta = {beta};  {'cos(theta)':>11}{'<b> isotropic':>15}{'beta*cos':>11}{'ratio':>8}")
for ct in (1.0,0.8,0.5,0.2,0.0,-0.5,-1.0):
    got=avg_b(beta,ct,'isotropic'); want=beta*ct
    r = got/want if abs(want)>1e-9 else float('nan')
    say(f"    {'':>11}{ct:>11.2f}{got:>15.4f}{want:>11.4f}{r:>8.3f}")
say("    <b> = (v/c) cos(theta), the measured V-A angular law, with NO free")
say("    parameter -- the only input was the isotropy of the ZBW measure.")
say()

say("P4  and the MAXIMALITY, which was the original question")
say("    Why is the coupling 100% V-A rather than partially chiral? Because b is")
say("    a BIT. B3 makes the response LINEAR in b, and b takes only +-1, so the")
say("    coupling has no way to be partial -- there is no intermediate value to")
say("    couple to. A continuous helicity variable would give partial chirality.")
say("    THE COUPLING IS MAXIMAL AND THE OBSERVATION IS DILUTED: the measured")
say("    asymmetry is (v/c) cos(theta) NOT because the coupling is weak at low")
say("    speed, but because a slow particle's ZBW spends nearly half the cycle on")
say("    each sign. At v -> c the drift dominates the circulation and <b> -> 1.")
say("    That is the same massive/massless split Patch 4143 found: helicity is")
say("    frame-dependent for a massive particle and invariant for a massless one.")
say(f"    check: <b> at beta = 0.999 is {avg_b(0.999,1.0,'isotropic'):.4f}, at beta = 1 it is 1.")
say()

say("P5  WHAT IS DERIVED, AND WHAT IS ASSUMED -- the honest split")
say("    DERIVED: the FORM (v/c) cos(theta), exactly, from two inputs already in")
say("      the corpus -- b is a sign (A1'), and the response is linear in b (B3)")
say("      -- plus one geometric input.")
say("    ASSUMED: that the ZBW measure is ISOTROPIC on the sphere. The corpus's")
say("      chi draft axiom says the ZBW is a DOUBLE rotation -- circulation in two")

say("      orthogonal planes -- and two orthogonal circulations at incommensurate")
say("      frequencies do sweep the sphere, but I have NOT shown they sweep it")
say("      UNIFORMLY. That is the gap, and it is a real one: the single-plane")
say("      alternatives are both excluded by the data above, so the measured law")
say("      is evidence FOR the double rotation and AGAINST a single circulation.")
say("    NOT DERIVED: the sign. Whether it is -v/c (left-handed) or +v/c is set")
say("      by the polarity-to-duality assignment in the chi draft, not by this.")
open('/tmp/4158.txt','w').write('\n'.join(out))
