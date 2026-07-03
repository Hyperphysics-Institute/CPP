"""
1859 -- Collision-energy reconciliation: does a typical cluster fragment the Cross-Rod?

The gating question from the 2026-07-03 handover (task 1). Paper DM-1 v1.0 sec:xsec says
cluster collisions (~1.95 MeV) exceed the bond window => fragmentation => collisionless.
Thread 1855-1858 computed ~0.04-0.5 MeV at the Cross-Rod's own pins => below E_ee => intact.

This script settles it by (A) reproducing the paper's numbers and identifying their
provenance, (B) recomputing at the Cross-Rod's own pinned parameters, (C) quantifying the
Maxwellian high-v tail, and (D) bracketing the energy-localization criterion.

Pinned inputs: m_element = 1408 MeV (0886), E_ee = 0.9 MeV side-bond (1813),
N_dwarf = 5-60 (DM-1 v1.0 sec:xsec), axial end-bond = E_qq-class, deep (1855).
"""
import numpy as np
from math import erf, sqrt, pi, exp

C_KMS = 299792.458

def ke_com_MeV(N, m_MeV, v_kms):
    """Total COM kinetic energy of a rod-rod collision, mu = N*m/2 (equal rods).
    This is the 0860/paper criterion: whole-collision KE vs ONE bond energy."""
    mu = 0.5 * N * m_MeV
    return 0.5 * mu * (v_kms / C_KMS) ** 2

def v_thr_kms(N, m_MeV, E_bond_MeV):
    """Velocity at which total COM KE = E_bond (the paper's own criterion, inverted)."""
    return C_KMS * sqrt(2.0 * E_bond_MeV / (0.5 * N * m_MeV))

def maxwell_tail(v_thr, sigma_1d):
    """P(v_rel > v_thr) for Maxwellian velocities: v_rel is Maxwell-distributed with
    per-component dispersion sqrt(2)*sigma_1d. Number-weighted (per-encounter)."""
    a = sqrt(2.0) * sigma_1d
    x = v_thr / a
    cdf = erf(x / sqrt(2.0)) - sqrt(2.0 / pi) * x * exp(-x * x / 2.0)
    return 1.0 - cdf

if __name__ == "__main__":
    print("=" * 74)
    print(" 1859 -- collision-energy reconciliation (fragmentation vs capture fork)")
    print("=" * 74)

    # (A) provenance: reproduce the paper's 1.95 MeV / 0.78 keV exactly ---------
    N_hoop, m_rung = 1183, 264.0          # 0860 hoop ledger parameters
    ke_cl_hoop = ke_com_MeV(N_hoop, m_rung, 1500.0)
    ke_dw_hoop = ke_com_MeV(N_hoop, m_rung, 30.0)
    print("\n(A) PROVENANCE of the paper's sec:xsec figures")
    print(f"    0860 hoop ledger (N={N_hoop}, m_rung={m_rung:.0f} MeV, rod mass "
          f"{N_hoop*m_rung/1e3:.0f} GeV):")
    print(f"      cluster (1500 km/s): {ke_cl_hoop:.3f} MeV   <- the paper's '~1.95 MeV'")
    print(f"      dwarf   (  30 km/s): {ke_dw_hoop*1e3:.3f} keV  <- the paper's '~0.78 keV'")
    print("    => sec:xsec imported the HOOP-picture numbers (N=1183, 264 MeV rungs)")
    print("       into the Cross-Rod paragraph without rescaling to (N=5-60, 1408 MeV).")

    # (B) the honest numbers at the Cross-Rod's own pins ------------------------
    m_el, E_ee = 1408.0, 0.9              # 0886 element mass; 1813 side-bond
    print("\n(B) HONEST recomputation at the Cross-Rod's own pinned parameters")
    print(f"    m_element = {m_el:.0f} MeV, E_ee (weakest link, side-bond) = {E_ee} MeV")
    print(f"    {'N':>4} {'rod mass':>10} {'KE@1500':>10} {'KE@2260':>10} "
          f"{'v_thr(E_ee)':>12} {'ratio 0860/honest':>18}")
    for N in [5, 15, 30, 60]:
        ke15 = ke_com_MeV(N, m_el, 1500.0)
        ke22 = ke_com_MeV(N, m_el, 2260.0)   # <v_rel> = 2.26*sigma_1d, sigma=1000
        vth = v_thr_kms(N, m_el, E_ee)
        print(f"    {N:>4} {N*m_el/1e3:>8.1f}GeV {ke15:>9.3f}M {ke22:>9.3f}M "
              f"{vth:>9.0f}kms {ke_cl_hoop/ke15:>17.1f}x")
    print("    => typical-cluster KE is BELOW E_ee for the entire N=5-60 band at 1500")
    print("       km/s; the 4-44x 'discrepancy' is exactly the rod-mass ratio")
    print("       (312 GeV hoop vs 7-85 GeV Cross-Rod). Same formula, stale (N, m).")

    # (C) the Maxwellian tail: what fraction of collisions DO fragment? ---------
    print("\n(C) HIGH-VELOCITY TAIL under the paper's own (generous) total-KE criterion")
    print(f"    {'N':>4} {'v_thr':>7}", end="")
    sigmas = [700.0, 1000.0, 1250.0]
    for s in sigmas:
        print(f"  P(frag)@sig={s:.0f}", end="")
    print()
    for N in [5, 15, 30, 60]:
        vth = v_thr_kms(N, m_el, E_ee)
        print(f"    {N:>4} {vth:>6.0f}k", end="")
        for s in sigmas:
            print(f"  {maxwell_tail(vth, s)*100:>13.2f}%", end="")
        print()
    print("    => short end (N<~15): <~5% of encounters in a rich cluster exceed the")
    print("       bond energy even on the generous criterion; long end (N~60): tens of")
    print("       percent. Fragmentation is PARTIAL and N-dependent, not the clean")
    print("       above-window switch sec:xsec describes.")

    # (D) the criterion ladder: how generous is total-KE-vs-one-bond? -----------
    print("\n(D) ENERGY-LOCALIZATION bracket (which mu participates?)")
    ke_contact = ke_com_MeV(1, m_el, 1500.0)   # element-element contact, mu = m/2
    v_contact = v_thr_kms(1, m_el, E_ee)
    print(f"    per-contact (mu = m_el/2):  KE@1500 = {ke_contact*1e3:.1f} keV; "
          f"v needed for E_ee = {v_contact:.0f} km/s (~{v_contact/C_KMS:.3f}c)")
    print("    total-COM  (mu = N*m/2):    the (B)/(C) numbers -- an UPPER bound:")
    print("      a fully inelastic merger thermalizes KE over ~2N bonds, so even")
    print("      captured pairs need KE comfortably ABOVE E_ee to break any one bond.")
    print("    bond ladder: E_ee = 0.9 MeV is the WEAKEST link (side/coat). The axial")
    print("      end-bond is E_qq-class and deep (1855: 'irreversible'); if rod-cutting")
    print("      must break the axial bond, fragmentation is excluded outright.")
    print("    => every rung of the ladder moves the verdict the SAME direction.")

    # verdict --------------------------------------------------------------------
    print("\n" + "=" * 74)
    print(" VERDICT: outcome 2 (fragmentation FAILS for typical clusters at the")
    print(" paper's own N=5-60), with a partial-3 rider: the Maxwellian tail")
    print(" fragments only the long end (N>~40) at tens-of-percent rates. The")
    print(" sec:xsec mechanism sentence rests on unrescaled 0860 hoop numbers.")
    print(" Cluster safety must come from the capture falloff (1857/1858), with")
    print(" tail fragmentation of the long end as at most an assist.")
    print("=" * 74)
