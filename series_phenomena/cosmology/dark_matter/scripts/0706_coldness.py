#!/usr/bin/env python3
"""
Patch 0706 -- DM arc Step 3: coldness (qDP/hTetra velocity dispersion).

Question: are the free qDP/hTetra cold enough? Warm/hot DM free-streams and
suppresses small-scale structure; thermal-relic DM lighter than ~3 keV is ruled
out (Lyman-alpha / satellite counts). Cold DM is far heavier.

Decisive variable: the DM particle mass vs the ~keV warm boundary, and the
velocity dispersion at matter-radiation equality (when structure starts growing).
Tags: [c04/est] CPP mass scale; [obs] cosmology.
"""
import math

c = 2.9979e8
m_qDP_GeV, m_hTetra_GeV = 0.30, 1.5     # [est] QCD/constituent scale (from Step 1)
m_WDM_keV = 3.0                          # [obs] thermal warm-DM lower bound (~3 keV)

# epochs (photon temperature, in energy units)
T_QCD   = 0.2e9      # eV   QCD era (~200 MeV)
T_BBN   = 1.0e6      # eV   BBN (~1 MeV)
T_eq    = 0.75       # eV   matter-radiation equality (z~3400)
T_rec   = 0.26       # eV   recombination (z~1100)

def v_over_c(T_eV, m_GeV):
    # non-relativistic rms thermal speed v = sqrt(3 T / m c^2)
    return math.sqrt(3.0 * T_eV / (m_GeV * 1e9))

print("="*64)
print("DM arc Step 3: coldness of free qDP/hTetra")
print("="*64)
for name, m in [("qDP   ", m_qDP_GeV), ("hTetra", m_hTetra_GeV)]:
    print(f"\n{name}: m = {m:.2f} GeV = {m*1e6:.3g} keV")
    print(f"   m / warm-DM bound (~3 keV)      : {m*1e6/m_WDM_keV:.2e}   (>>1 => cold)")
    print(f"   becomes non-relativistic at T~m : ~{m:.2f} GeV  (QCD era, ~microseconds)")
    for ep, T in [("QCD era ~200 MeV", T_QCD), ("BBN ~1 MeV", T_BBN),
                  ("matter-rad equality", T_eq), ("recombination", T_rec)]:
        v = v_over_c(T, m)
        tag = "non-relativistic" if v < 0.1 else "RELATIVISTIC"
        print(f"      v/c at {ep:22s}: {v:.2e}  ({tag})")

print()
print("Verdict: COLD, by a wide margin.")
print(f" - GeV-scale mass is ~1e5-1e6 x above the ~3 keV warm-DM bound.")
print(" - Non-relativistic since the QCD era; v/c at matter-radiation equality")
print("   is ~1e-4 (qDP) and smaller for hTetra -- free-streaming length far below")
print("   the ~keV-WDM suppression scale, so small-scale structure is unaffected.")
print()
print("Honest caveat (does NOT change the verdict):")
print(" - This assumes the free qDP/hTetra kinetic temperature redshifts like a")
print("   decoupled species rather than being pinned to an ongoing-hot Sea bath.")
print("   §6c supports the cooling picture (hTetra freeze-out is a phase transition;")
print("   thermal collisions now only *degrade* bonding, not dominate). A rigorous")
print("   late-time Sea temperature ties to OPEN-SR-5, but coldness does not depend")
print("   on it critically -- the GeV mass scale alone secures it under standard cooling.")
print(" - Chemical freeze-out (when hTetras stop forming) is distinct from kinetic")
print("   decoupling (what sets the velocity dispersion); coldness rides on the latter.")
