import numpy as np
# ============================================================
# Formation-size calculation: does PCD equilibrium aggregation produce N ~ 400-1000?
# ============================================================
# Reversible linear (equilibrium) polymerization:
#   attach ~ nu*phi (monomer activity phi), detach ~ nu*exp(-E_bond/kT)
#   <N> ~ sqrt(phi)*exp(E_bond/2kT)                                    ... (i)
# Freeze-out when the detach rate drops below the Hubble rate:
#   nu*exp(-E_bond/kT_form) = H_form  ->  E_bond/kT_form = ln(nu/H_form)
#   => <N> ~ sqrt(phi) * sqrt(nu/H_form)                              ... (ii)
E_qq = 66.0   # MeV, color core bond (alpha_s * hbar c / d)
print("The clean result:  <N> ~ sqrt(phi) * exp(E_bond/2 kT_form)  =  sqrt(phi * nu_PCD/H_form)")
print("Target N_form ~ 400-1000 (dwarf normalization, 1845) -> E_bond/kT_form = 2 ln(N/sqrt(phi)):\n")
for phi in (1.0, 1e-2):
    print(f" monomer activity phi={phi:g}:")
    for N in (400, 700, 1000):
        ratio = 2*np.log(N/np.sqrt(phi))       # E_bond/kT_form
        print(f"   N_form={N:5d}: E_bond/kT_form = {ratio:.1f}  ->  kT_form = E_bond/{ratio:.1f}")
    print()

print("kT_form for the element-element detachment bond (E_bond = n_bond * E_qq):")
print(f"{'E_bond(MeV)':>12}{'(n_qq)':>7}{'kT_form for N=700 (MeV)':>26}")
for nb in (1,2,4):
    Eb = nb*E_qq; kT = Eb/(2*np.log(700))
    print(f"{Eb:>12.0f}{nb:>7d}{kT:>26.2f}")

print("\nExponential sensitivity (the honest concern) -- N vs kT_form at E_bond = E_qq = 66 MeV:")
print(f"{'kT_form(MeV)':>13}{'<N> (phi=1)':>14}")
for kT in (3,4,5,6,8,10):
    print(f"{kT:>13.1f}{np.exp(E_qq/(2*kT)):>14.2g}")
print("  -> <N> swings from ~1e5 (kT=3) to ~27 (kT=10): a factor ~3 in kT_form spans 4 orders in <N>.")
print("     The dwarf normalization needs kT_form pinned to ~10-15% of ~4.7 MeV (for E_bond=66 MeV).")

print("\nVERDICT:")
print("  The formation size reduces to ONE substrate quantity: kT_form, the relic-epoch freeze-out")
print("  temperature (equivalently nu_PCD/H_form). N_form~400-1000 requires kT_form ~ E_bond/13.")
print("  For the element-element E_qq bond (66-264 MeV): kT_form ~ 4.7-19 MeV.")
print("  This is a SHARP, FALSIFIABLE condition -- but exponentially sensitive, so it is a genuine")
print("  prediction ONLY IF the substrate thermal history NATURALLY sets kT_form there; otherwise it")
print("  is a fine-tuning. Deciding which is the OPEN-COSMO-DM-4 (kT_form) calc. Not computable from")
print("  DM-lane geometry -- needs nu_PCD (substrate attempt frequency) and H_form (relic epoch).")
