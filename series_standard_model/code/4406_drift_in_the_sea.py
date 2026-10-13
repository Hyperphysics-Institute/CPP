"""Patch 4406 -- founder (on 4405): the CPs of a body picking up speed are not swinging faster; the increased KE is
stored in the DPs of the DP sea, as increased DP separation and DP-arc separation (SF-6; R-CP-NO-REST-MASS; 4097).

Part 1  with the gain applied to the body's drift (stored in the sea) rather than to each CP's swing, every body's drift
        rises by the same amount each Moment: equal fall by construction, whatever its internal speeds.  4405's toy
        (relativistic momentum added to near-cap CPs) modelled a mechanism CPP does not have and is withdrawn.
Part 2  the stored energy is (1/2) kappa V^2 (SF-6 pin).  kappa = E0/c^2 exactly for a closed self-bound pattern (Laue;
        the physical electron and cages), (2/3) U_pol/c^2 for an open cloud (the bare CP, scalar toy).
Part 3  action and reaction: active/passive mass ratio the same for every material (Bartlett-van Buren: Moon's
        centre-of-mass/centre-of-figure offset); with passive = inertial, active/inertial.  If electrons were open clouds (kappa = 2/3 of energy/c^2) and nucleons closed patterns
        (kappa = energy/c^2), aluminium and iron would differ in active/inertial mass by ~3e-6; lunar laser ranging
        bounds that at ~4e-12 (Bartlett and van Buren 1986).  So the electron's kappa must equal its E0/c^2 to ~4e-7,
        and binding energy must carry kappa = E/c^2 to ~1e-8; the closed-pattern (Laue) route is the candidate.
"""
me_u = 0.000548580
print("Part 1 (statement): a uniform drift gain of the body's centre of energy, carried by the sea -> eta = 0.")
print("        Under the one-PSR cap the drift must be a boost (swings re-timed: longer forward leg), not an addition to")
print("        each CP's step; added CP by CP with capping, a CP at the cap gains ~half the drift (composition-dependent).")

print("\nPart 2 (statement): kappa, closed vs open (SF-6 pin; the Laue half deferred by CONV-001 pending debt (d))")
print("  closed self-bound pattern: kappa = E0/c^2 (Laue, coefficient 1 forced)")
print("  open cloud (bare CP, scalar toy): kappa = (2/3) U_pol/c^2")

print("\nPart 3: if electrons were open clouds and nucleons closed patterns")
for name, Z, A, m in (("Al-27", 13, 27, 26.9815385), ("Fe-56", 26, 56, 55.9349375)):
    f = Z*me_u/m
    print(f"  {name}: electron mass fraction {f:.4e}")
fAl = 13*me_u/26.9815385; fFe = 26*me_u/55.9349375
# active ~ energy; inertia: electrons count (2/3) of their energy -> active/inertial = 1/(1 - f/3)
r = lambda f: 1/(1 - f/3)
print(f"  active/inertial: Al {r(fAl):.8f}, Fe {r(fFe):.8f}, difference {r(fAl)-r(fFe):.1e}  (LLR bound ~4e-12)")
print("  -> excluded by ~1e6.  What LLR forces: kappa/active the same for electrons as nucleons,")
df = fAl - fFe
print(f"     |1 - k_e| <~ 4e-12 / {df:.1e} = {4e-12/df:.0e}  (k_e = electron kappa / (E0/c^2))")
bAl, bFe = 8.332, 8.790      # MeV per nucleon binding
fb = (bFe - bAl)/931.494
print(f"  nuclear binding share differs Al vs Fe by {fb:.1e} of the mass -> binding energy must carry kappa = E/c^2 to"
      f" ~{4e-12/fb:.0e}")
