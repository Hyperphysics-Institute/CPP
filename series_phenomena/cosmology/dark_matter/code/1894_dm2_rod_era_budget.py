"""
1894 -- DM-2 rod-era re-scoping: the budget arithmetic that sets the gate's stakes,
and the import-verdict on whether rho_Lambda is an SI target.

Registered inputs: the 0722-derived suppression rho_L = (1/8pi) rho_P (l_P/R_H)^2
(dynamical, within ~2x observed; unified with OPEN-SM-6 by the CC umbrella);
the SI-2 portrait (f_occ ~ 0.1 median; E_z prior-shaped, F7 corner 16 keV);
pitch a = 1.0-1.3 fm.
"""
import math
HBARC = 197.327e-15 * 1e6 * 1.602e-19  # J*m
LP, RH = 1.616e-35, 1.4e26             # m
RHO_P = 4.6e113                        # J/m^3
rho_L = RHO_P * (LP / RH) ** 2 / (8 * math.pi)
rho_L_obs = 5.3e-10                    # J/m^3 (Planck 2018)
print("(1) The 0722 formula: rho_L = (1/8pi) rho_P (l_P/R_H)^2 = %.2e J/m^3" % rho_L)
print("    vs observed 5.3e-10 -> ratio %.2f  [within ~2x as registered]" % (rho_L / rho_L_obs))
# Portrait Sea budget
for a, ez_mev, tag in ((1.15, 0.016, "F7 corner (E_z = 16 keV)"), (1.15, 1.0, "E_z = 1 MeV"), (1.15, 100.0, "E_z = 100 MeV")):
    n_fm3 = 0.10 / a ** 3
    rho_sea = n_fm3 * ez_mev * 1.602e-13 / 1e-45   # J/m^3
    print("(2) Portrait Sea budget [%s]: n = %.3f fm^-3 -> rho_Sea = %.2e J/m^3 = %.1e x rho_L" % (
        tag, n_fm3, rho_sea, rho_sea / rho_L_obs))
print("""
(3) THE STAKES: the quiescent-Sea budget exceeds rho_Lambda by 39-44 orders across
    the portrait's E_z range. Excess-sourcing must therefore zero the uniform Sea
    EXACTLY (a ground-state subtraction/symmetry), not approximately -- 'suppressed'
    is not enough. This was the June arc's Gate-1; the portrait makes its stakes
    numerical for the first time.
(4) IMPORT VERDICT: the registered 0722 coefficient (1/8pi)*rho_P*(l_P/R_H)^2 is
    PARAMETER-FREE in substrate quantities (it carries only l_P, R_H) => under the
    registered form, rho_Lambda is a CONSISTENCY STATEMENT for the portrait, NOT an
    importable SI hard target. The under-determination of the SI system stays at 2
    unless the unified mechanism's derivation is shown to carry occupancy/coherence
    dependence -- a well-posed question for the arc, answered either way.""")
