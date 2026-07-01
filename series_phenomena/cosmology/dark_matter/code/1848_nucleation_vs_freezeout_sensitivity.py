import numpy as np
# ============================================================
# Why route B (nucleation-limited) is the proper gradient, not route A (colder-DM freeze-out).
# The choice is decided by SENSITIVITY: an over-shoot by orders is a regime error, and the
# correct regime (nucleation-limited) has a MILD (linear) size law, not the exponential one.
# ============================================================
E_qq=66.0
print("ROUTE A (keep equilibrium freeze-out; make DM ~100x colder): <N> ~ exp(E_bond/2kT_form)")
print("  EXPONENTIAL in kT_form -> the tuning knob (T_DM/T_rad) must be pinned to ~10-15%:")
for kT in (1.2,1.4,1.7,2.0):
    print(f"    kT_form={kT:.1f} MeV -> <N> ~ {np.exp(E_qq/(2*kT)):.2g}")
print("  A factor ~1.7 in kT_form spans ~3 orders in <N>. Hitting 400-1000 = tuning an exponentially")
print("  sensitive, currently-unpinned decoupling temperature. Fixes the NUMBER, keeps a wrong lens.\n")

print("ROUTE B (nucleation-limited: strong-binding regime, all monomers polymerize):")
print("  size set by seeds, N_form ~ n_monomer/n_seed = 1/eps_nuc  (eps_nuc = seed fraction)")
print("  LINEAR in eps_nuc -> 'approximately right' is good enough:")
for eps in (5e-4,1e-3,1.4e-3,2.5e-3):
    print(f"    eps_nuc={eps:.1e} -> N_form ~ {1/eps:.0f}")
print("  Band 400-1000 <=> eps_nuc in [1.0e-3, 2.5e-3]: a factor ~2.5 window in a MILD parameter.")
print("  No exponential tuning; a broad, order-1e-3 nucleation efficiency lands in-band.\n")

print("VERDICT -- the proper gradient is B:")
print("  1. The 2-3 order over-shoot is a REGIME ERROR (equilibrium formula applied at E/kT~50 where")
print("     nucleation-and-growth, not detachment-equilibrium, sets the size) -- a symptom that the")
print("     lens is wrong, not that a temperature is mistuned. B fixes the cause; A patches the symptom.")
print("  2. B is the STANDARD physics of strong-binding aggregation (dust/polymer/structure nucleation).")
print("  3. B is ROBUST (linear in eps_nuc) vs A FRAGILE (exponential in kT_form): even if A 'works' it")
print("     leaves the dwarf branch a fine-tuned prediction; B can make it a genuine one.")
print("  Caveat (honest): B is the right FRAMEWORK, not a guaranteed rescue -- the CPP nucleation")
print("  efficiency must itself come out ~1e-3; that is the reframed calc, but it is non-fine-tuned.")
