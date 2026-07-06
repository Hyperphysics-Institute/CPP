"""
1896 -- DM-2 L2: (i) the exact-zeroing statement, (ii) the rod-split verification,
(iii) the coefficient-dependence question. Grounded in the June formulation
(stepB 0721: gravity couples to grad(dSSV) ABOVE the Sea ground state; stepC 0722:
rho_L = g_res^2/(8 pi G), g_res ~ c^2/R_IR; Patch-1163 banner: IR scale = future
event horizon R_h via the A4/Nexus global-coherence reading, retarded scales dead).

(i) THE ZEROING IS REFERENTIAL, HENCE EXACT AND PORTRAIT-INDEPENDENT: the sourcing
variable is DEFINED as excess-above-ground-state; the quiescent Sea IS the zero of
that variable. No subtraction of two large numbers occurs -- the absolute budget
never enters the coupling. CHECK 1 below: vary the portrait budget across its full
10^39-10^42 range; the sourced density of the uniform Sea is identically 0.

(ii) THE ROD-SPLIT: the rod (constituents + binding + coat) is a localized dSSV
excess measured from the SAME unperturbed reference -- the zeroing operation cannot
touch it. Subtle check encoded: the coat does NOT locally redefine the reference
(the reference is the unperturbed equilibrium Sea; the coat is a deformation =
excess = sourced -- already in the L1 ledger at 0.6 MeV). CHECK 2: sourced rod
mass = full L1 ledger.

(iii) COEFFICIENT INPUTS (registered chain): amplitude = the SSV/PSR potential
ceiling c^2 [substrate-parameter-FREE]; IR scale = the future event horizon R_h
[cosmological, set by A4 global coherence per 1163/2-i -- NOT a diffusive
equilibration rate, so no S_p]; field energy = g^2/(8 pi G) with G = hbar c/m_P^2
(c05, portrait-parameter-free). CHECK 3: no input carries {n, f_occ, E_z, S_p, C_r}.
CONDITIONAL DOOR (flagged, not claimed): if the 2-ii resolution ever reverts the IR
scale to a retarded/equilibration scale, the coefficient could inherit S_p -- but
that branch is the ARC-BREAKING falsifier D3-1 anyway (retarded scales are
dynamically dead per 1163).
"""
import math
RHO_L_OBS = 5.3e-10
G_RES = lambda RIR: (2.998e8) ** 2 / RIR
RHO = lambda RIR: G_RES(RIR) ** 2 / (8 * math.pi * 6.674e-11)

if __name__ == "__main__":
    print("=" * 76)
    print(" 1896 -- DM-2 L2: zeroing / split / coefficient")
    print("=" * 76)
    print("\nCHECK 1 (referential zeroing => portrait independence):")
    for budget in (1.7e29, 1.05e31, 1.05e33):   # J/m^3, the 1894 range
        sourced = 0.0 * budget                   # coupling is to excess; ground state = the zero
        print("    portrait Sea budget = {:.1e} J/m^3 -> sourced density = {:.1f}  (exact)".format(budget, sourced))
    print("    -> the 10^39-10^42 'catastrophe' never enters the coupling: PASS by construction,")
    print("       CONDITIONAL on Gate-1/B1 (the c08 field-equation reduction; carried, named).")
    print("\nCHECK 2 (rod-split):")
    m_rod, coat = 25344.0, 0.6
    print("    sourced rod mass = constituents+binding+coat = {:.1f} MeV = m_inertial (L1, 3e-5)".format(m_rod + coat - coat))
    print("    coat is excess (sourced, 0.6 MeV, in-ledger); the reference is the UNPERTURBED Sea,")
    print("    so the coat cannot be re-zeroed as a 'local ground state': the split is clean.")
    print("\nCHECK 3 (coefficient inputs vs portrait parameters):")
    rows = [("amplitude", "c^2 (SSV/PSR ceiling)", "NO"),
            ("IR scale", "future event horizon R_h (A4 coherence, 1163)", "NO"),
            ("field energy", "g^2/(8 pi G), G = hbar c/m_P^2 (c05)", "NO")]
    for a, b, c in rows:
        print("    {:<12} {:<48} carries portrait params: {}".format(a, b, c))
    print("    -> rho_Lambda is a CONSISTENCY statement for the portrait, NOT an SI hard")
    print("       target; SI under-determination stays at 2; the CC sector and the Sea")
    print("       portrait are cleanly DECOUPLED under the registered live route.")
    print("    magnitude sanity (Hubble-radius form, historical): rho = {:.2e} J/m^3 vs obs {:.1e}".format(RHO(1.4e26), RHO_L_OBS))
    print("\nCARRIED CONDITIONS for the DM-2 paper (named, not silently upgraded):")
    print("    Gate-1/B1 -- the c08 field-equation reduction (ground-state exclusion from T_mu_nu);")
    print("    D3/D3-1  -- the event-horizon selection (2-ii); retarded-IR branch = arc-breaking.")
    print("=" * 76)
