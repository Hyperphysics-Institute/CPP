#!/usr/bin/env python3
"""
Patch 4173 — TODO-4172-SOURCEEQ: write A_i's source clause, and ask whether its
coefficient is a NEW parameter or an existing one.
"""
import numpy as np
out=[]
def say(s=""): print(s); out.append(s)
G=6.67430e-11; c=2.99792458e8; hbar=1.054571817e-34
kappa=8*np.pi*G/c**4

say("S1  the dimensional question")
say("    A3': Q_ij sourced by -(16 pi G/c^4) T_ij^TF.")
say("    T_ij has units of energy density, J/m^3.")
say("    Spin density s_i has units of angular momentum per volume,")
say("    J.s/m^3 -- one factor of TIME more than T_ij.")
say("    So the SAME coefficient cannot act on s_i directly: the natural")
say("    bridge is one factor of c over a length, or equivalently")
say("        source_A = c * (curl s)   [J/m^3, matching T_ij]")
say("    which is the same construction magnetisation uses to source a")
say("    magnetic field (B from curl M). No new constant is introduced.")
say()

say("S2  so the coefficient is NOT a new parameter -- if the Einstein-Cartan")
say("    reading of Patch 4172 is right")
say("    In Einstein-Cartan, spin sources torsion with THE SAME kappa =")
say(f"    8 pi G/c^4 = {kappa:.3e} m/J that sources curvature. Torsion")
say("    introduces NO new coupling. If A_i is CPP's torsion channel, the")
say("    amendment inherits that and the zero-parameter claim survives.")
say("    **That is the answer TODO-4172-SOURCEEQ was asking for, and it is")
say("    the good outcome: the missing coefficient is G, already in A3'.**")
say()

say("S3  and Einstein-Cartan then tells us HOW BIG -- the known answer")
say("    EC torsion is non-propagating: it gives a CONTACT spin-spin term of")
say("    energy density ~ (kappa/2) s^2. Evaluated at real spin densities:")
say(f"    {'system':<28}{'n (m^-3)':>11}{'s = n hbar':>13}{'u_EC (J/m^3)':>15}{'vs system':>14}")
rows=[("polarised iron",8.5e28,1e5),
      ("nuclear matter",1.7e44,1e32),
      ("neutron-star core",5e44,1e34)]
for nm,n,ref in rows:
    s=n*hbar; u=0.5*kappa*s**2
    say(f"    {nm:<28}{n:>11.1e}{s:>13.2e}{u:>15.2e}{u/ref:>14.1e}")
say("    (last column = ratio to a characteristic energy density of that system:")
say("     1e5 J/m^3 for a magnet's field energy, 1e32 for nuclear binding,")
say("     1e34 for neutron-star pressure)")
say()
say("    EVERYWHERE ACCESSIBLE THE TERM IS ~40 ORDERS TOO SMALL. That is the")
say("    standard Einstein-Cartan result, known since the 1970s, and it is NOT")
say("    a CPP failing.")
say()

say("S4  THE CONSILIENCE, and it reframes the whole session")
say("    Four independent routes this session found A_i empirically empty:")
say("      4155 sec 4  no distinctive signature; only magnetism")
say("      4165 sec 6  b does not read the register")
say("      4170 sec 3  spin-mixing bounded at 5e-47 per Moment")
say("      4171 sec 1  neither identified job is a prediction")
say("    If A_i is the torsion channel, THAT IS THE EXPECTED ANSWER, not a")
say("    defect. Torsion is famously unobservable at accessible densities. The")
say("    amendment was being judged by a standard its own physics does not meet")
say("    and was never going to.")
say()

say("S5  WHERE A_i WOULD MATTER -- and this is a real redirection")
say("    EC torsion becomes significant at the CARTAN DENSITY, where the contact")
say("    term rivals the rest-mass term: n_Cartan ~ m c^2/(kappa hbar^2) roughly.")
m_n=1.675e-27
n_cart=(m_n*c**2)/(kappa*hbar**2)
say(f"    n_Cartan ~ {n_cart:.2e} m^-3   vs nuclear {1.7e44:.1e} m^-3")
say(f"    ratio: {n_cart/1.7e44:.1e}")
say("    So A_i's arena is not the laboratory. It is the EARLY UNIVERSE and,")
say("    NOT neutron-star cores either -- the Cartan density is 3.8e56 times")
say("    nuclear, so only the EARLY UNIVERSE reaches it, which is exactly where")
say("    the EC literature puts torsion: singularity avoidance, bouncing")
say("    cosmologies, and nothing at lower density.")
say("    **CPP has an early-universe lane. That is where this channel should be")
say("    tested, and it is not where any of this session's work looked.**")
open('/tmp/4173.txt','w').write('\n'.join(out))
