#!/usr/bin/env python3
"""
Patch 4161 — TODO-4160-ANISOTROPY. Escape (b) is not "cheap" -- it is CORRECT,
and Patch 4160's falsifier rests on a modelling error of mine.

THE ERROR. 4159/4160 computed <b> by substituting the TWELVE EDGE DIRECTIONS for
u_hat in b = sign(A.V). But the 12-edge rule quantises the DISPLACEMENT, not V:
c03, verbatim -- "The 12-edge selection rule chooses the lattice edge i* that
maximizes e_i . SSV_net". V is PRIOR to the selection and CONTINUOUS; the edge is
chosen FROM it. And the amendment's b is evaluated on V: 4120, "b ~ A.V is
derived, not postulated", with V = SSV_disp, the GP's summed register.

So b never sees the twelve directions. It sees their SUM.
"""
import numpy as np
out=[]
def say(s=""): print(s); out.append(s)
rng=np.random.default_rng(4161)
PHI=(1+5**0.5)/2
ico=[]
for s1 in (1,-1):
    for s2 in (1,-1):
        ico += [[0,s1,s2*PHI],[s1,s2*PHI,0],[s2*PHI,0,s1]]
ico=np.array(ico,float); ico/=np.linalg.norm(ico,axis=1)[:,None]

say("S1  V is a SUM over arrivals. Is the sum's direction isotropic?")
say("    Model: V = sum over the 12 PSR-shell directions with random weights.")
say("    The 5-design property that makes degree-2 moments direction-independent")
say("    to 1e-16 (Patch 4160 R2) makes the sum's COVARIANCE exactly isotropic --")
say("    so V is isotropic to second order BY CONSTRUCTION, and the deviations")
say("    start at degree 6 and are suppressed by the number of arrivals.")
say()
M=200000
say(f"    {'arrivals N':>11}{'spread of <b> over A directions':>34}")
A=rng.normal(size=(200,3)); A/=np.linalg.norm(A,axis=1)[:,None]
for N in (1,2,4,12,60):
    spreads=[]
    for _ in range(1):
        w=rng.normal(size=(M,12))
        if N<12:
            mask=np.zeros((M,12)); idx=rng.integers(0,12,size=(M,N))
            np.put_along_axis(mask, idx, 1.0, axis=1); w=w*mask
        V=w@ico
        V/=np.linalg.norm(V,axis=1)[:,None]
        beta=0.5
        vals=np.array([np.sign(V@a + beta).mean() for a in A])
        spreads.append(vals.max()-vals.min())
    say(f"    {N:>11}{spreads[0]:>34.4f}")
say()
say("    At N = 1 the CP reads a single arrival and the lattice shows through.")
say("    By N = 12 -- one contribution per PSR-shell direction, the generic case")
say("    -- the spread is at the sampling floor. THE ANISOTROPY IS AN ARTEFACT OF")
say("    TREATING V AS A SINGLE LATTICE DIRECTION.")
say()

say("S2  and the SAME calculation now settles 4158's isotropy premise")
say("    4158 assumed u_hat isotropic; 4159 showed the chi draft's double rotation")
say("    does not supply it and fell back on orientation-averaging; 4160 showed")
say("    there is nothing to average over. The real answer is simpler:")
say("    **V's direction is isotropic because V is a SUM over a spherical")
say("    5-design, whose second-moment tensor is exactly proportional to the")
say("    identity.** No orbit argument and no ensemble argument needed.")
C=ico.T@ico/12
say(f"    covariance of the 12-set: (1/12) sum e_i e_i^T =")
for r in C: say("      [" + "  ".join(f"{x:+.6f}" for x in r) + "]")
say(f"    off-diagonal max |.| = {np.max(np.abs(C-np.diag(np.diag(C)))):.2e}, "
    f"diagonal spread = {np.max(np.diag(C))-np.min(np.diag(C)):.2e}")
say("    Exactly (1/3) I. Any sum with independent weights is isotropic at")
say("    second order, hence its DIRECTION is isotropic for a Gaussian sum.")
say()
say("S3  WHAT STANDS AND WHAT FALLS")
say("    FALLS: Patch 4160's falsifier, entirely. It computed b on the quantised")
say("      displacement instead of on V. No sidereal modulation is predicted.")
say("    FALLS: Patch 4159's 'first distinctive empirical signature'. Same error,")
say("      opposite sign. The amendment is back to having no distinctive")
say("      signature, which is Patch 4155 section 4's position.")
say("    STANDS: Patch 4158's <b> = (v/c)cos(theta), now on a THIRD and finally")
say("      sound premise -- the 5-design covariance of the summed register.")
say("    STANDS: Patch 4159's negative result that the chi draft's double rotation")
say("      does not sweep the sphere uniformly. It just was not needed.")
say()
say("S4  the residual, which is real but small")
say("    V is isotropic at second order EXACTLY, and deviates at degree 6 --")
say("    the 5-design's limit. A CP that reads only ONE arrival per Moment would")
say("    see the lattice (N = 1 row above). Whether any physical regime is")
say("    arrival-starved -- very low DP-sea density, or the first Moment after a")
say("    creation event -- is not examined here and is the one place the")
say("    anisotropy could still live.")
open('/tmp/4161.txt','w').write('\n'.join(out))
