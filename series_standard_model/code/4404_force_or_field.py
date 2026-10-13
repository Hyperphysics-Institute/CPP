"""Patch 4404 -- founder (on 4403): the mass keeps the speed it gains; the velocity is stored as DP-arcs and DP separation,
which maintain constant (inertial) velocity; the Moment-to-Moment Delta SSV_abs between inner and outer limbs is the
accelerating force, the F in F = m a.

Part 1  if Delta SSV_abs is a FORCE the same for every CP (or proportional to the number of CPs), then a = F/m depends on
        what the body is made of.  Electron vs proton; titanium vs platinum (MICROSCOPE: |eta| < ~1e-15).
Part 2  if Delta SSV_abs sets the ACCELERATION (F = m g, with m everything that carries inertia, DP-arcs included),
        every body falls alike.  The internal-clock picture of 4403 does this automatically.
"""
u_amu = 1.66053907e-27
me, mp, mn = 9.1093837e-31, 1.67262192e-27, 1.67492750e-27

print("Part 1: the one reading to rule out -- a fixed push per CP that the DP-arc inertia resists (a = N F / m),")
print("        counting unpaired CPs only (3 per nucleon + electrons; DP-cloud CPs not counted)")
print(f"  electron vs proton (one CP vs a three-quark cage): accelerations differ by m_p/(3 m_e) ~ {mp/(3*me):.0f}x")
# neutral atoms: force proportional to CP count N = 3A (quarks) + Z (electrons); m = atomic mass
atoms = {"Ti-48": (48, 22, 47.9479463), "Pt-195": (195, 78, 194.9647911)}
acc = {}
for k, (A, Z, m) in atoms.items():
    N = 3*A + Z
    acc[k] = N/(m*u_amu)
    print(f"  {k}: CPs {N}, mass {m} u, CPs per unit mass {N/m:.6f} per u")
eta = 2*(acc["Ti-48"] - acc["Pt-195"])/(acc["Ti-48"] + acc["Pt-195"])
print(f"  Eotvos parameter Ti vs Pt (pure isotopes as stand-ins for MICROSCOPE's TA6V and PtRh10 alloys): eta = {eta:.2e}   (MICROSCOPE 2022: (-1.5 +- 2.7) x 1e-15)")
print("  -> excluded by ~10^13: whatever the counting, the received change must go with mass-energy to ~1e-15")

print("\nPart 2: the founder's step as he described it (v_{i+1} = v_i + the limb change, the same for every CP)")
print("  a = c^2 x (census difference across one PSR) / l_P for every body; F = m a with m = all the body's inertia")
print("  (DP-arcs, DP separation, binding).  eta = 0: assumed by the rule (a per-CP acceleration), not derived.")
print("  4403's internal-clock picture: every internal process (ZBW, DP-arc motion, binding) slows by the same (1 - u),")
print("  so momentum builds as m g t for every part, in proportion to its energy: weak equivalence automatically.")
print("  Remaining test of the same kind: gravitational binding energy (strong equivalence; lunar laser ranging,")
print("  Nordtvedt parameter |eta_N| <~ 1e-4, Hofmann and Mueller 2018; TODO-4364-SELFGRAV).")
