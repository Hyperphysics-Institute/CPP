#!/usr/bin/env python3
"""
Patch 4139 — TODO-4138-A3G2MAG. The magnitude test A3G-2 now needs, and the
frame problem it exposes in the amendment itself.

4138 withdrew A3G-2's T-parity protection and left it UNRUN, with one candidate
rescue: if only the TRANSIENT bracelet channel reads b there is no long-range
spin-dependent potential and comagnetometer bounds do not apply. This patch
tests that rescue and then does the magnitude comparison.

EMPIRICAL INPUT (cited in the doc):
  He3-Xe129 free-precession comagnetometer, equatorial component of a
  background field coupling to the BOUND NEUTRON spin:
      b_perp^n  <  8.4e-34 GeV   (68% C.L.)
  This is an ENERGY: the bound is on a spin-direction-dependent energy
  splitting that modulates at the sidereal frequency as the lab rotates
  relative to a preferred frame.
"""
import numpy as np

out = []
def say(s=""):
    print(s); out.append(s)

BOUND = 8.4e-34          # GeV, comagnetometer limit on bound-neutron spin energy
V_CMB = 370.0            # km/s, solar-system motion w.r.t. the CMB
C_KMS = 299792.458
BETA = V_CMB / C_KMS
LAMBDA_QCD = 0.2         # GeV, the confining scale
G_F = 1.1663787e-5       # GeV^-2
M_PI = 0.13957           # GeV

say("H1  does the 4138 transient-bracelet rescue survive? NO -- two ways it fails")
say("    (a) A_i is BROADCAST, not local. The amendment puts A_i into LSP', the")
say("        GP-to-GP packet (A3'), and into the DI-bit payload (AP-4). That is")
say("        the SAME long-range channel that carries Phi and V_i. A channel in")
say("        the broadcast is long-range BY CONSTRUCTION; 4125 itself identified")
say("        A1.A2 as ordinary long-range magnetic dipole-dipole. So 'the")
say("        bracelet is transient' does not make the A channel short-range.")
say("    (b) The comagnetometer bound is not on a force between two masses at")
say("        all. It is on a spin-direction-dependent ENERGY of ONE neutron,")
say("        modulating as the lab rotates. No second body is needed, so an")
say("        argument about two-body potentials cannot reach it.")
say("    => The rescue I proposed at 4138 is WITHDRAWN. My own candidate, one")
say("       patch old, and it does not survive being written out.")
say()

say("H2  the frame problem -- and it revises Patch 4134")
say("    b = A.V with V = SSV_net, which the corpus defines in the ABSOLUTE")
say("    (Nexus) frame: A3' has LSP' propagating 'at c = l_P/t_P in the absolute")
say("    (Nexus) frame', and SSV_net is what a CP's displacement is computed")
say("    from. A nucleon at rest in the lab is NOT at rest in that frame: it")
say(f"    drifts at {V_CMB:.0f} km/s, beta = {BETA:.3e}.")
say()
say("    4134 computed W = sum_i s_i V_i in the NUCLEON REST FRAME and found")
say("    <n.W> = 0 by the L = 0 s-wave average. Add the common drift u to every")
say("    quark's V_i, as the absolute frame requires:")
s = np.array([+1.0, +1.0, -1.0])          # SU(6) proton u-up u-up d-down
say(f"        W -> W + (sum_i s_i) u ,  sum_i s_i = {s.sum():+.0f} for the SU(6) proton")
say("    The drift does NOT cancel: the spin projections sum to +1, not 0, so")
say(f"    B_tot picks up n.u with |u| = beta = {BETA:.3e}.")
say("    The s-wave average cannot remove it -- u is fixed in the lab while the")
say("    cage orientations average, so it survives exactly the averaging that")
say("    killed the internal term.")
say()
say(f"    Residual <b> from drift alone ~ {BETA:.1e}, against the ~1e-7 hadronic")
say(f"    PV bound: a factor {BETA/1e-7:.0e} too large IF anything reads b linearly.")
say("    **This revises 4134: the rest-frame calculation was incomplete.**")
say()

say("H3  the magnitude comparison, with the unknown coupling named")
say("    Write the spin-direction-dependent energy as  E = kappa * beta * cos(theta).")
kappa_max = BOUND / BETA
say(f"    Comagnetometer: kappa * beta <= {BOUND:.1e} GeV")
say(f"                 => kappa <= {kappa_max:.2e} GeV")
say()
say("    Candidate scales for kappa, from the least to the most suppressed:")
rows = [("strong / confining scale", LAMBDA_QCD),
        ("weak-suppressed hadronic  G_F m_pi^2 * Lambda", G_F * M_PI**2 * LAMBDA_QCD)]
for nm, k in rows:
    say(f"      {nm:<46} kappa ~ {k:.2e} GeV   -> exceeds bound by {k/kappa_max:.1e}")
say()
say(f"    Even the weak-suppressed estimate -- the MOST suppressed scale the")
say(f"    corpus offers, and the one 4137 argued for -- overshoots by ~1e23.")
say("    To respect the bound, kappa must be below ~7e-31 GeV, i.e. suppressed")
say(f"    relative to the confining scale by {kappa_max/LAMBDA_QCD:.0e}.")
say("    No scale in CPP is known to me that is that small -- but the corpus")
say("    DOES have a suppression claim, and it is the right place to look:")
say()
say("H3b the corpus's own preferred-frame suppression claim (SD-1)")
say("    SD-1 (Hossenfelder Claim 1), verbatim: 'The preferred frame is real")
say("    but its effects are suppressed by the ratio of laboratory scales to")
say("    cosmological scales, making it undetectable at current precision.'")
L_LAB, L_HUBBLE, L_PLANCK = 1.0, 1.3e26, 1.6e-35        # metres
for nm, r in (("lab / Hubble", L_LAB / L_HUBBLE),
              ("Planck / Hubble", L_PLANCK / L_HUBBLE)):
    say(f"      {nm:<18} = {r:.1e}  -> kappa ~ {r * LAMBDA_QCD:.1e} GeV, "
        f"{'PASSES' if r * LAMBDA_QCD < kappa_max else f'still {r*LAMBDA_QCD/kappa_max:.0e} over'}")
say(f"    Needed: kappa <= {kappa_max:.1e} GeV, i.e. suppression "
    f"{kappa_max/LAMBDA_QCD:.0e} below the confining scale.")
say("    So the lab/Hubble reading of SD-1's claim falls ~3 orders SHORT, and")
say("    the Planck/Hubble reading over-suppresses by 25 orders. The claim as")
say("    written does not settle this case either way -- it names a mechanism")
say("    without fixing the ratio, and the two natural readings straddle the")
say("    bound. That is where the work has to go, not into a coefficient.")
say()

say("H4  what this means -- stated carefully, because the claim is large")
say("    This does NOT show the amendment is false. It shows that IF anything")
say("    reads b linearly AND V is the absolute-frame SSV_net, then a bound")
say("    neutron carries a sidereal spin-energy modulation ~22 orders above")
say("    the measured limit. One of those two must give.")
say()
say("    THE LIVE ESCAPE, and it is not numerical: SR-1 derives special")
say("    relativity in CPP from the SSV_abs / SSV_net decomposition -- i.e.")
say("    observables do not depend on absolute velocity. If that coverage")
say("    extends to the A channel, the drift term is unobservable and the")
say("    bound does not bite. **But SR-1 predates the A3' amendment and does")
say("    not mention A_i.** The amendment added a broadcast component that")
say("    SR-1's derivation never covered.")
say()
say("    So the test reduces to ONE question, and it is sharp:")
say("      Is b = A.V Lorentz-covariant under CPP's own emergent SR -- i.e.")
say("      is V the ABSOLUTE SSV_net (then b is frame-dependent and A3G-2")
say("      FIRES), or the LOCAL RELATIVE SSV_net measured against the local")
say("      sea rest frame (then b is frame-independent and A3G-2 passes)?")
say()
say("VERDICT")
say("  A3G-2 is NOT passed and NOT unrun: it is CONDITIONALLY FIRING.")
say("  It fires unless the amendment's b is shown Lorentz-covariant, and the")
say("  gap if it is not is ~1e23 -- not a coefficient quibble.")
say("  4138's transient-bracelet rescue is withdrawn (H1).")
say("  4134's rest-frame calculation is revised as incomplete (H2).")
say("  Nothing here withdraws chi_4. The question named in H4 decides it.")

open("/tmp/4139_out.txt", "w").write("\n".join(out))
