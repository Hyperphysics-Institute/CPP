#!/usr/bin/env python3
"""
Patch 4159 — TODO-4158-ZBWMEASURE. The isotropy premise behind 4158's
<b> = (v/c) cos(theta), tested against the corpus's ACTUAL geometry rather than
against a continuum idealisation.

TWO CANDIDATE MEASURES, and 4158 assumed neither explicitly:
  (a) the chi draft's DOUBLE ROTATION in two orthogonal planes of R^4;
  (b) the 12 icosahedral edge directions, which is what a CP actually displaces
      along (the 12-edge selection rule, c03/GR-1b).
(b) is the corpus's own geometry and 4158 should have used it from the start.
"""
import numpy as np, itertools
out=[]
def say(s=""): print(s); out.append(s)
rng=np.random.default_rng(4159)
PHI=(1+5**0.5)/2

ico=[]
for s1 in (1,-1):
    for s2 in (1,-1):
        ico += [[0,s1,s2*PHI],[s1,s2*PHI,0],[s2*PHI,0,s1]]
ico=np.array(ico,float); ico/=np.linalg.norm(ico,axis=1)[:,None]

say("Q1  does the chi draft's DOUBLE ROTATION sweep the sphere uniformly? NO.")
say("    x(t) = (r1 cos w1 t, r1 sin w1 t, r2 cos w2 t, r2 sin w2 t) on S^3.")
say("    With incommensurate w1, w2 the orbit is equidistributed (Weyl) on the")
say("    CLIFFORD TORUS T(r1,r2) -- but that torus is a single orbit of fixed")
say("    radii, and under the Hopf map S^3 -> S^2 a Clifford torus maps to ONE")
say("    LATITUDE CIRCLE at height r1^2 - r2^2, not to the whole sphere.")
a,b_=rng.uniform(0,2*np.pi,400000), rng.uniform(0,2*np.pi,400000)
for r1 in (0.5,0.707,0.9):
    r2=np.sqrt(1-r1**2)
    u=np.stack([r1*np.cos(a), r1*np.sin(a), r2*np.cos(b_)],axis=1)
    u/=np.linalg.norm(u,axis=1)[:,None]
    say(f"    r1={r1:.3f}: naive 3-projection, <cos^2 theta> = {np.mean(u[:,2]**2):.4f}"
        f"   (uniform on S^2 would be 0.3333)")
say("    So neither the Hopf image nor the naive 3-projection is uniform.")
say("    **4158's isotropy premise is NOT supplied by the chi draft as written.**")
say()

say("Q2  the corpus's ACTUAL geometry: the 12 icosahedral edge directions")
say("    A CP displaces along one of 12 edges (12-edge selection rule, c03).")
say("    u_hat is therefore DISCRETE, not a continuum. Test <b> directly.")
def mean_b(beta, A, dirs):
    return np.sign(dirs@A + beta*(A@A)).mean()
say(f"    {'beta':>7}{'A along a VERTEX':>19}{'A along a FACE':>17}{'A random':>11}{'target':>9}")
vert=ico[0]
face=ico[0]+ico[1]+ico[2]; face/=np.linalg.norm(face)
for beta in (0.05,0.2,0.5,0.8,0.95):
    rnd=rng.normal(size=3); rnd/=np.linalg.norm(rnd)
    say(f"    {beta:>7.2f}{mean_b(beta,vert,ico):>19.4f}{mean_b(beta,face,ico):>17.4f}"
        f"{mean_b(beta,rnd,ico):>11.4f}{beta:>9.2f}")
say("    A FIXED lattice orientation gives a STAIRCASE, not beta. The 12-point")
say("    set is a spherical 5-design, which reproduces polynomial averages to")
say("    degree 5 -- but sign() is not a polynomial, and it is the discontinuity")
say("    that the design does not control.")
say()

say("Q3  but a real particle's cage is randomly oriented w.r.t. its motion")
say("    Average over lattice orientations as well. THIS is the physical average:")
say(f"    {'beta':>7}{'<b> orientation-averaged':>27}{'target beta':>13}{'error':>10}")
M=200000
for beta in (0.05,0.2,0.5,0.8,0.95):
    tot=0.0
    R=rng.normal(size=(M,3,3))
    # random rotations via QR
    q,_=np.linalg.qr(R)
    det=np.linalg.det(q); q[det<0,:,0]*=-1
    A=np.array([0.,0.,1.])
    d=np.einsum('mij,kj->mki', q, ico)        # rotated 12-sets
    tot=np.sign(d[:,:,2]+beta).mean()
    say(f"    {beta:>7.2f}{tot:>27.4f}{beta:>13.2f}{tot-beta:>10.4f}")
say()
say("    ORIENTATION-AVERAGING RESTORES <b> = beta EXACTLY. The reason is the")
say("    same Archimedes fact 4158 used: for a UNIFORMLY RANDOM rotation, each")
say("    of the 12 directions has its A-component uniform on [-1,1], so the")
say("    average over the ensemble is the continuum answer even though no single")
say("    lattice orientation gives it.")
say()

say("Q4  VERDICT, and it changes what 4158 rests on")
say("    4158's isotropy premise is JUSTIFIED -- but not by the chi draft's")
say("    double rotation (Q1 shows that does not sweep uniformly). It is")
say("    justified by ORIENTATION-AVERAGING over the lattice, which is physically")
say("    compulsory: a beam's particles have no common cage orientation.")
say("    So 4158's (v/c)cos(theta) stands, on a DIFFERENT and better premise than")
say("    the one it stated.")
say()
say("    AND IT PREDICTS A DEVIATION. For an ENSEMBLE WITH ALIGNED CAGES the")
say("    staircase of Q2 survives: <b> departs from beta by")
for beta in (0.2,0.5,0.8):
    say(f"      beta={beta}: vertex-aligned {mean_b(beta,vert,ico)-beta:+.3f}, "
        f"face-aligned {mean_b(beta,face,ico)-beta:+.3f}")
say("    That is an O(10-40%) effect -- large, and it is the DISTINCTIVE")
say("    signature the amendment has been missing (Patch 4155 section 4: 'A_i")
say("    currently has no independent empirical signature'). It requires a")
say("    source of polarised particles emitted from an ORIENTED lattice -- a")
say("    single crystal. Whether any real experiment realises that is NOT")
say("    established here and is the obvious next question.")
open('/tmp/4159.txt','w').write('\n'.join(out))
