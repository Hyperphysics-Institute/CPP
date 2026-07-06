"""
1878 -- CONFRONT-3 OPENED (founder green-light, 5 July 2026): the DM-baryon sector.
The campaign USED the rod-nucleon coupling (CONFRONT-1 np channel, 1866) but never
confronted the phenomenology that coupling implies: direct detection, overburden
thermalization, CMB drag, and the strongly-interacting-DM probe ladder. Scoping layer.

COUPLING CHAIN (registered CONFRONT-1 structure; same J4 pairwise-additive assumption
that carried the np channel now carries this sector):
  per-qCP-pair strength  g^2 = E_c/(8N)^2      [rod-rod contact E_c at r_c]
  rod(8N qCPs) - nucleon(3 qCPs):  E_rN = 24N g^2 = 3 E_c/(8N),  range R_s = r_c/chi
Born scattering length  a0 = (2 mu/(hbar c)^2) E_rN r_c R_s^2 ;
light-mediator form factor  a(q) = a0 * m_s^2/(m_s^2+q^2),  m_s = chi hbar c/r_c.

CONSTRAINT LADDER (pinned 5 July 2026; provenance):
  - CMB DM-baryon drag + gas-rich dwarf heating: sigma_n <~ O(1e-25) cm^2 in the
    0.1-100 GeV range (arXiv:2112.00707 summary of robust bounds).
  - Underground detectors (LZ/XENON): SHIELDED for this class -- "dark matter that
    interacts strongly with baryons ... likely absorbed traversing the rocks,
    suppressed flux in deep underground labs" (arXiv:2209.04387). Verified below by
    the atmospheric-thermalization estimate; LZ contact limits (~1e-47) DO NOT map.
  - XQC rocket (minimal shielding, ~165 km): THE decisive probe at tens of GeV.
    Excluded band at 0.1-100 GeV has a coherent-scattering-driven LOWER boundary
    reaching down to O(1e-27) cm^2 territory (Erickcek et al. 2007, PRD 76 042007,
    Fig 9 -- EXACT boundary at 25 GeV to be digitized/recomputed; Mahdawi-Farrar
    2017/2018 updates; Li et al. 2209.04387 note non-trivial parameter dependence).
  - DAMIC/CRESST surface runs close the ~micro-barn window at ~GeV masses
    (Mahdawi-Farrar JCAP 12 (2017) 004; JCAP 10 (2018) 007) -- below our mass.
NOTE: all published exclusions assume CONTACT interactions or sigma = sigma0*v^n;
our candidate is a LIGHT-MEDIATOR (m_s = 7.76 MeV) COMPOSITE (L ~ 20 fm) -- the
mapping is modified by both form factors and must be recomputed for a kill verdict.
"""
import math
HBARC = 197.327; RC = 1.0
CHI = ((1 + 5 ** 0.5) / 2) ** -3 / 6
RS = RC / CHI; MS = HBARC / RS                    # 7.764 MeV
M_EL = 1408.0; MN = 938.9

def a0(N, Ec):
    mrod = N * M_EL; mu = MN * mrod / (MN + mrod)
    ErN = 3.0 * Ec / (8 * N)
    return (2 * mu / HBARC ** 2) * ErN * RC * RS ** 2   # fm

def sig_n(N, Ec, q):                                     # cm^2, per nucleon
    a = a0(N, Ec) * MS ** 2 / (MS ** 2 + q ** 2)
    return 4 * math.pi * (a * 1e-13) ** 2

if __name__ == "__main__":
    print("=" * 78)
    print(" 1878 -- CONFRONT-3 scoping: the rod-nucleon sector vs the SIMP ladder")
    print("=" * 78)
    print("\n(1) COUPLING at the chi point (m_s = %.3f MeV, R_s = %.2f fm):" % (MS, RS))
    for N in (15, 18, 20):
        for lbl, Ec in (("flat", 0.30), ("additive", 0.02 * N)):
            print("    N={:>2} {:>9}: E_rN = {:.2e} MeV,  a0 = {:.3f} fm,  sigma_n(q=0) = {:.2e} cm^2".format(
                N, lbl, 3 * Ec / (8 * N), a0(N, Ec), sig_n(N, Ec, 0)))
    N, Ec = 18, 0.30
    print("\n(2) MOMENTUM DEPENDENCE (light mediator; N=18 flat):")
    for q, ctx in ((0.0, "CMB drag (q->0)"), (2.3, "XQC threshold ~100 eV Si"),
                   (7.8, "q = m_s"), (11.4, "XQC top ~2.5 keV Si"),
                   (50.0, "LZ-type Xe recoil ~10 keV"), (100.0, "Xe recoil ~40 keV")):
        print("    q = {:>6.1f} MeV ({:>24}): sigma_n = {:.2e} cm^2".format(q, ctx, sig_n(N, Ec, q)))
    print("\n(3) ATMOSPHERIC/OVERBURDEN THERMALIZATION (does LZ apply?):")
    # coherent scattering on air nuclei at halo-velocity momentum transfer
    A_air = 14.5; mA = A_air * MN / 1000 * 1000  # MeV
    mrod = N * M_EL
    muA = mA * mrod / (mA + mrod)
    v = 230e5 / 2.998e10                          # halo speed in c
    q_slow = muA * v                              # MeV, typical transfer
    aA = a0(N, Ec) * (muA / (MN * mrod / (MN + mrod))) * A_air * MS ** 2 / (MS ** 2 + q_slow ** 2)
    sigA = 4 * math.pi * (aA * 1e-13) ** 2
    col = 1000.0 / (A_air * 1.66e-24)             # nuclei/cm^2 through atmosphere
    ncoll = col * sigA
    floss = 2 * mrod * mA / (mrod + mA) ** 2
    print("    q_slow ~ {:.1f} MeV; coherent sigma_A(air) ~ {:.1e} cm^2".format(q_slow, sigA))
    print("    collisions through 1000 g/cm^2 atmosphere ~ {:.0f}; energy loss/coll ~ {:.0%}".format(ncoll, floss))
    print("    => rods THERMALIZE high in the atmosphere: underground detectors are")
    print("       SHIELDED (consistent with 2209.04387); LZ contact limits DO NOT map.")
    print("\n(4) LADDER VERDICTS (N = 18 flat; contact-mapping caveat everywhere):")
    print("    CMB drag + dwarf-gas heating  (<~1e-25):  sigma_n(0) = {:.1e}  -> PASS (~x20)".format(sig_n(N, Ec, 0)))
    print("    LZ/XENON underground (1e-47 contact)   :  INAPPLICABLE (shielded)")
    print("    XQC band at 10-100 GeV (lower edge ~1e-27 territory, Erickcek Fig 9):")
    print("       XQC-effective sigma_n(q = 2-11 MeV) = {:.1e} - {:.1e} cm^2".format(
        sig_n(N, Ec, 11.4), sig_n(N, Ec, 2.3)))
    print("       -> LIVE TENSION: the candidate sits AT the reported reach of the XQC")
    print("          exclusion. NOT a verdict either way: the published boundary is a")
    print("          contact-interaction mapping; ours is a 7.76 MeV mediator + 20 fm")
    print("          composite. The proper confrontation is the arc's task 1.")
    print("\n(5) ARC TASK LIST: (1) digitize/recompute the XQC boundary at 20-30 GeV for")
    print("    the light-mediator composite (recoil spectrum + attenuation, Erickcek")
    print("    method); (2) rod form factor at q ~ 2-11 MeV (qL ~ 0.2-1.1); (3) Earth-")
    print("    thermalized population phenomenology (accumulation, Dewar-class bounds,")
    print("    2112.00707); (4) CMB drag with proper velocity weighting; (5) verdict +")
    print("    paper hook (DM-1 v1.3 or DM-3 discriminant).")
    print("=" * 78)
