#!/usr/bin/env python3
"""
PATCH 2444 -- OPEN-DM-FLOQUET-1 / actual E_qq core-bond depth + peel-stall test.
Pins the least-trustworthy number from 2443 (the core depth, floated to 4.7 MeV) using
CPP-anchored ingredients, then tests the founder's "core out-resists the spring" peel
argument -> derives the effective E_bond denominator (single-rung vs junction) instead
of choosing it.

ANCHORS (repo): m_qCP=132 MeV (qDP=264=2 m_qCP, 1816/0886), reduced mass mu=66 MeV;
alpha_s=5/(8 phi)=0.386; hbar*c=197.3 MeV*fm; delta=3/7; d=1.15 fm STRONG-SSV-set (2433:
"the strong force (qCP, steep SSV) sets d" -- NOT a Coulomb/ZBW balance).

The 2443 depth (4.7 MeV) was an ARTIFACT: it forced K_ZBW from d*=1.15 with the charge-
switched (1/7) coefficient. That is wrong because the spacing is set by the STRONG SSV,
not by the charge-switched Coulomb. This pins the depth from the confinement instead.
"""
import numpy as np
AHC=197.3; PHI=(1+np.sqrt(5))/2; ALPHA_S=5/(8*PHI); DELTA=3/7
m_qCP=132.0; mu=m_qCP/2; d=1.15
U_hinge=1.057   # MeV per hinge, from 2443 finite-angle U(theta)
print("="*72); print("E_qq CORE-BOND DEPTH -- CPP-anchored"); print("="*72)
print(f"m_qCP={m_qCP} MeV  mu(reduced)={mu} MeV  alpha_s={ALPHA_S:.4f}  d={d} fm  delta=3/7")
print()
# (1) Is the qCP relativistically confined at d? zero-point KE at Dx~d
KE_nr=AHC**2/(2*mu*d**2)          # non-relativistic ZP kinetic
KE_rel=AHC/d                       # relativistic E~pc
print("(1) qCP zero-point energy confined to Dx ~ d=1.15 fm:")
print(f"    non-rel (hbar c)^2/(2 mu d^2) = {KE_nr:.0f} MeV   rel  hbar c/d = {KE_rel:.0f} MeV")
print(f"    both >> mu c^2={mu} MeV -> RELATIVISTIC confinement.")
print(f"    => the well holding the qCP at 1.15 fm must be ~{KE_rel:.0f}-{KE_nr:.0f} MeV DEEP")
print(f"       (a soft Coulomb/ZBW bond of a few MeV CANNOT confine it -> confirms 2433:")
print(f"        spacing is STRONG-SSV-set, deep; the 2443 4.7 MeV was a forced-K artifact).")
print()
# (2) E_qq depth estimates (the energy to remove one qCP from d to infinity)
E_raw   = ALPHA_S*AHC/d                    # raw Coulomb binding at d (static opp-charge)
E_switch= (1-2*DELTA)*ALPHA_S*AHC/d        # charge-switched net (fast-switch time avg) at d
E_conf_lo, E_conf_hi = KE_rel, KE_nr       # confinement-scale (must hold vs ZP escape)
print("(2) E_qq depth estimates (energy to separate one qCP to infinity):")
print(f"    raw Coulomb at d              alpha_s hc/d      = {E_raw:6.1f} MeV  (upper, static opp-charge)")
print(f"    charge-switched net at d      (1-2d)alpha_s hc/d= {E_switch:6.1f} MeV  (fast-switch time avg)")
print(f"    strong-confinement scale      ~ ZP escape       = {E_conf_lo:6.0f}-{E_conf_hi:.0f} MeV  (holds qCP at 1.15fm)")
print(f"    => robust LOWER bound on core depth ~ {E_switch:.0f} MeV (even the switched net);")
print(f"       physical value ~ {E_raw:.0f}-{E_conf_lo:.0f} MeV (Coulomb component to confinement scale).")
print()
# (3) Peel-stall test: does 1 MeV of released bend energy break the next core bond?
print("="*72); print("PEEL-STALL TEST (does the loop unzip through the core?)"); print("="*72)
print(f"    released bend energy per hinge (2443 U): {U_hinge:.2f} MeV")
print(f"    Coulomb attraction has NO barrier -> rupture requires the FULL binding.")
print(f"    (monotonic -A/r: separating to infinity costs the whole depth; no inflection.)")
for lab,E in [("charge-switched net",E_switch),("raw Coulomb",E_raw),("confinement",E_conf_lo)]:
    margin=E/U_hinge
    verdict="STALLS (core holds)" if E>U_hinge else "propagates (unzips)"
    print(f"    core depth={E:6.1f} MeV vs {U_hinge:.2f} MeV/hinge -> margin x{margin:5.1f} -> {verdict}   [{lab}]")
print()
print("    coat bonds ~0.49 MeV < 1 MeV/hinge -> a peel WOULD rip the coat, but")
print("    the coat sits at LARGER radius (outer); the peel front reaches the core and")
print("    STALLS there (margin >=9x on the most pessimistic core estimate).")
print()
# (4) Consequence for the E_bond denominator + the ratio (depth cancels)
print("="*72); print("CONSEQUENCE -- the fork resolves toward JUNCTION cohesion"); print("="*72)
r_q=d/np.sqrt(2)
ratio_geom=2*(r_q/d)**2
print(f"    peel stalls at the deep core => opening the loop requires breaking the WHOLE")
print(f"    plane-plane junction (core-inclusive), NOT a single 490 keV rung.")
print(f"    => effective E_bond = junction cohesion (deep), the founder's picture.")
print(f"    flexure ratio is GEOMETRIC: kappa/E_bond = 2(r_q/d)^2 = {ratio_geom:.3f} (core-only),")
print(f"       ~0.66 with coat (2443) -> IN-WINDOW [0.43,0.81].  The DEPTH CANCELS in the")
print(f"       ratio, so this holds regardless of whether the core is 10 or 200 MeV.")
print()
print("="*72); print("HONEST CAVEATS (G7)"); print("="*72)
print("  - The confinement DEPTH (~170-220 MeV) is a zero-point-escape estimate, NOT a")
print("    strong-sector-derived number. Robust claim is only: core depth >> 1 MeV/hinge.")
print("  - Deep binding is CONDITIONAL on Floquet stability (method (a) eps-window, the")
print("    plausible-but-unestablished corner 2441); if the bond isn't Floquet-stable it")
print("    doesn't hold at all.")
print("  - This DERIVES the peel-stall (physical argument) but the reframing of the")
print("    registered E_bond (490 keV single-rung -> junction cohesion) STILL must clear")
print("    CONV-001. This is the INPUT to that packet, not a bypass.")
print("  - Also implies FLEXURE (strong-SSV-dominated axial stiffness) is the ring-closure")
print("    mode, distinct from the method-(a) transverse-rigid charge-switched mode. That")
print("    mode-identification is itself a CONV-001 question.")
print("  - Candidate (B): still UNRESOLVED. Registry NOT promoted. Omega_DM parked.")
