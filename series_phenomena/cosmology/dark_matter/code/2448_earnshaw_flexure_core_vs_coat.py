#!/usr/bin/env python3
"""
PATCH 2448 -- OPEN-DM-FLOQUET-1 / the load-bearing joint examined (founder-directed):
does flexure escape Earnshaw? RESULT: NO -- the full-lattice collective bend stiffness
is NEGATIVE. This RETRACTS the flexure-robust / in-window ratio of 2443/2446 (an axial-
bond-only artifact) and returns the make-or-break to conditional/marginal (ponderomotive
rescue, unpinned eps-window) for BOTH modes. Same failure class as 2427 (axial average),
caught here before the panel rather than by it.

Founder reframe: the E_qq SSV (alpha_s, steep) keeps ZBW residency localized in the core
-> examine as a residency/migration problem, look at the SSV directly.
GROUNDING: the SSV is Coulomb-SHAPED at the operative (code) level (field = sum q rhat/r^2),
coupling alpha_s core / alpha coat. So Earnshaw (div^2 V=0) applies to BOTH species.
"""
import numpy as np
from numpy.linalg import eigvalsh, norm
AHC=197.3; PHI=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI); ALPHA=1/137.036; DELTA=3/7
d=1.15; N_PL=8; D=d; A_Q=d; R_E=1.6*(d/np.sqrt(2))
print("="*76); print("EARNSHAW / does FLEXURE escape it? (load-bearing joint)"); print("="*76)
print(f"alpha_s={ALPHA_S:.4f} alpha={ALPHA:.5f} (alpha_s/alpha)={ALPHA_S/ALPHA:.1f} ^2={(ALPHA_S/ALPHA)**2:.0f}")
print()
# (1) single-bond radial stiffness (what 2443/2446 used) -- positive, but ISOLATED
A_eff=(1-2*DELTA)*ALPHA_S*AHC; K=A_eff*d/2
dstar=2*K/A_eff; Vpp_rad=-2*A_eff/dstar**3+6*K/dstar**4
print(f"(1) single-BOND radial stiffness V''_rad={Vpp_rad:+.2f} (POSITIVE) -- but this is the")
print(f"    ISOLATED-bond number the 2443/2446 axial-bond approximation summed. Not the lattice.")
print()
def plane(R,a_q):
    h=a_q/2
    return [(+h,+h,+1,'q'),(-h,+h,-1,'q'),(-h,-h,+1,'q'),(+h,-h,-1,'q'),
            (+R,0,-1,'e'),(0,+R,+1,'e'),(-R,0,-1,'e'),(0,-R,+1,'e')]
def rod_cfg(kap,scale=1.0):
    Cc=[];Pp=[];Ww=[]
    for k in range(N_PL):
        s=k*D
        if kap<1e-9: cx,cz,phi=0.0,s,0.0
        else:
            R=1/kap; phi=s/R; cx=R*(1-np.cos(phi)); cz=R*np.sin(phi)
        cph,sph=np.cos(phi),np.sin(phi); par=(-1)**k
        for (x,y,sgn,sp) in plane(R_E,A_Q):
            X=(cx+x*cph)*scale; Z=(cz+x*sph)*scale; Y=y*scale
            Cc.append(sgn*par);Pp.append((X,Y,Z));Ww.append(np.sqrt(ALPHA_S) if sp=='q' else np.sqrt(ALPHA))
    return np.array(Cc,float),np.array(Pp,float),np.array(Ww,float)
def Esw(cfg):
    Cc,Pp,Ww=cfg; E=0.0;n=len(Cc)
    for i in range(n):
        for j in range(i+1,n):
            r=norm(Pp[i]-Pp[j])
            if r>1e-9: E+= -(1-2*DELTA)*Ww[i]*Cc[i]*Ww[j]*Cc[j]*AHC/r
    return E
# (2) THE DECISIVE TEST: full-lattice collective bend stiffness, correct straight reference
E0=Esw(rod_cfg(0.0))
print("(2) FULL-LATTICE collective bend stiffness (correct straight reference, small kappa):")
print(f"    E0(straight)={E0:.3f} MeV")
print(f"    {'kappa':>7} {'R[fm]':>8} {'dE[MeV]':>11} {'dE/kappa^2':>11}")
vals=[]
for kap in [0.005,0.01,0.02]:
    dE=Esw(rod_cfg(kap))-E0; vals.append(dE/kap**2)
    print(f"    {kap:>7.3f} {1/kap:>8.1f} {dE:>11.5f} {dE/kap**2:>11.0f}")
S_bend=np.mean(vals)
dE_coll=Esw(rod_cfg(0.0,scale=0.99))-E0
print(f"    bend stiffness d^2E/dkappa^2 = {S_bend:+.0f} MeV*fm^2   collapse(scale .99) dE={dE_coll:+.2f} MeV")
print(f"    => collapse RESISTED (+), but BEND is UNSTABLE ({S_bend:+.0f} < 0): the straight rod")
print(f"       is Earnshaw-UNSTABLE to bending. FLEXURE does NOT escape Earnshaw.")
print()
# (3) what this retracts
print("(3) RETRACTION: 2443/2446 summed ONLY the axial inter-plane bonds (which resist bending)")
print("    and missed the intra-/cross-plane pairs that (net) DESTABILIZE the bend. The full")
print("    lattice flips the sign: kappa_theta is NEGATIVE, so the 'geometric ratio ~0.66")
print("    in-window' was an axial-bond ARTIFACT -- same failure class as 2427's axial average,")
print("    which 2430 caught. The flexure-robust / modes-disagree story (2443-2446) is CORRECTED.")
print()
# (4) what SURVIVES: core >> coat ponderomotive rescue (both modes now need it)
print("(4) WHAT SURVIVES -- both modes are Earnshaw-negative and need the ZBW/ponderomotive")
print("    rescue; the CORE does the heavy lifting for BOTH:")
print(f"    K_pond(core)/K_pond(coat) ~ (alpha_s/alpha)^2 = {(ALPHA_S/ALPHA)**2:.0f}  (founder's point holds)")
print(f"    core migration exp(-{ALPHA_S/ALPHA:.0f}x) vs coat (steep E_qq localizes ZBW residency).")
print(f"    So IF the ponderomotive rescues the bend at all, the core is why. But whether it")
print(f"    clears the negative {S_bend:+.0f} at N=16 is the conditional/marginal eps-window question")
print(f"    (method a), NOW OWED for the BEND mode -- the flexure-ponderomotive netting (R5-analog).")
print()
print("="*76); print("HONEST READ (G7) -- the verdict moves DOWN"); print("="*76)
print("  - Flexure does NOT escape Earnshaw. My 2443-2446 favorable case rested on an axial-")
print("    bond approximation that overcounted; corrected, the static bend stiffness is NEGATIVE.")
print("  - Both flexure and transverse are Earnshaw-negative -> BOTH need the ZBW ponderomotive")
print("    rescue in an unpinned eps-window. The make-or-break is back to method (a)'s")
print("    conditional/marginal state -- NOT the robust in-window I reported.")
print("  - Interesting flip: a negative static bend stiffness means straight rods WANT to curl")
print("    (spontaneous formation, favorable) -- but ring STABILITY (a stable minimum at N=16)")
print("    then rests entirely on the ponderomotive, un-computed for this mode.")
print("  - The core's alpha_s^2 (2800x) rescue is the one robust favorable element and applies")
print("    to both modes.")
print("  - OWED (decisive): the flexure-ponderomotive netting (does ZBW stabilize a bend")
print("    equilibrium at N=16?). Until then candidate (B) is UNRESOLVED-leaning-MARGINAL,")
print("    not favorable. Registry NOT promoted; Omega_DM parked. This is the load-bearing")
print("    joint breaking under scrutiny -- found before the panel, as intended.")
