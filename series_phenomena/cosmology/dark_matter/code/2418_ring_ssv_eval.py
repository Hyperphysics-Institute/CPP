import math

# ---- Registered substrate constants (candidate-INDEPENDENT: Sea / mode properties) ----
E_gap   = 0.9e6      # eV   e-channel activation gap (2311 inventory) -- Sea property
E_ee    = 0.9e6      # eV   e-channel contact bond (hopping barrier scale) -- Sea property
T_cap   = 3.2e-3     # eV   OPEN-DM-TAMB-1 present-epoch ambient cap (2330 check 11) -- Sea property
# knee window that ANY coring-capable capture must reach (2330 sec4, PRW-D invariant form)
knee_lo, knee_hi = 1.60e3, 11.27e3   # eV
# band-edge cadence ceiling: nu_max = c/a with a = l_P  ->  hbar*nu_max = E_Planck
E_Planck = 1.22e28   # eV   (hbar*c/l_P) -- the largest conceivable knee prefactor

# ---- Candidate-SPECIFIC inputs (the ring's only levers) ----
R_s_ring = 25.42     # fm   ring coat screening radius (2399)
# ring masses N*1.408 GeV, N=4-8; dominant N=6 ~ 8.45 GeV (2383). Coring demand is a
# dwarf-velocity sigma/m ~ O(1-10) cm^2/g -> a required knee of ORDER the dwarf window.
# The exact ring coring demand doesn't matter below; we show why.

print("="*72)
print("RING-FAMILY |SSV| DISSIPATIVE-CAPTURE EVALUATION (re-run in ring config)")
print("="*72)

# 1) Harmonic-null: coherent route = 0 exactly (candidate-blind). Survival = threshold events.
#    The operative surviving channel is L (creation), k-INDEPENDENT:
#        knee = hbar * kappa_c * nu * exp(-E_gap / T_amb)
#    Evaluate the MOST GENEROUS possible knee at the capped T_amb:
#    take nu at the band edge (hbar*nu = E_Planck) and kappa_c = 3 (top of prior).
kappa_c_max = 3.0
suppression = math.exp(-E_gap / T_cap)                 # exp(-0.9MeV / 3.2meV)
log10_supp  = (-E_gap / T_cap) / math.log(10)
knee_max_at_cap = kappa_c_max * E_Planck * suppression  # eV, absolute ceiling

print(f"\nActivation factor at the cap: exp(-E_gap/T_cap) = exp(-{E_gap/T_cap:.3e})")
print(f"   log10(suppression) = {log10_supp:.3e}   (i.e. ~10^{log10_supp:.2e})")
print(f"\nMOST GENEROUS knee reachable at T_amb = T_cap = 3.2 meV:")
print(f"   knee_max = kappa_c(=3) * E_Planck * suppression")
print(f"   log10(knee_max / eV) = {math.log10(kappa_c_max*E_Planck) + log10_supp:.3e}")
print(f"   required window: [{knee_lo:.2e}, {knee_hi:.2e}] eV  (log10 ~ {math.log10(knee_lo):.2f}-{math.log10(knee_hi):.2f})")

log10_shortfall = (math.log10(knee_lo)) - (math.log10(kappa_c_max*E_Planck) + log10_supp)
print(f"\n   KNEE SHORTFALL vs the EASIEST edge of the window: ~10^{log10_shortfall:.3e}")
print(f"   (the '×10^29' in 2330 is the T_amb ratio 82keV/3.2meV; the KNEE ratio is far worse)")

# 2) Which inputs are candidate-specific?  The only R_s-dependent term is D_hop*k^2 (transport).
#    Transport is already CLOSED (knee_hop <= 324 keV < required, 2330 sec5) AND the surviving
#    channel L is k-independent -> R_s_ring = 25.42 fm never enters the operative knee.
print("\n" + "-"*72)
print("CANDIDATE-DEPENDENCE AUDIT")
print("-"*72)
print(" harmonic-null theorem  : mode property (omega=ck, no-carried-velocity) -> ring-blind")
print(" E_gap = 0.9 MeV        : Sea's lowest creation channel               -> ring-blind")
print(" T_amb cap = 3.2 meV    : mode's own gravitating radiation (one-ledger) -> ring-blind")
print(f" k = 1/R_s (ring 25.42fm): enters ONLY D_hop*k^2 = transport, already CLOSED; ")
print("                          surviving channel L is k-INDEPENDENT -> R_s irrelevant")
print(" ring coring demand     : the ONLY ring lever; sets required knee ~keV;")
print(f"                          cannot bridge a 10^{log10_shortfall:.1e} knee gap.")

# 3) Could the encounter transiently heat the Sea above the cap and self-activate?
#    Encounter frequency content ~ v/b ~ 45 eV (gate file) << E_gap = 0.9 MeV.
omega_enc = 45.0  # eV, gate file
print("\n" + "-"*72)
print(f" transient self-activation? encounter content ~{omega_enc} eV vs gap {E_gap:.1e} eV")
print(f"   -> {E_gap/omega_enc:.1e}x below the gap; encounter cannot fire threshold events.")
print("="*72)
print("RESULT: |SSV| dissipative capture is DEAD for the ring family, and dead")
print("        CANDIDATE-BLIND -- every killing term is a Sea/mode property the ring")
print("        cannot move. The only escapes are the two OPEN-DM-TAMB-1 evasions")
print("        (mode non-thermalization / one-ledger self-excitation exemption),")
print("        which are also Sea-level -- re-aiming at the ring does not reopen them.")
print("="*72)
