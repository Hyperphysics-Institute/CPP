#!/usr/bin/env python3
"""C7 PMNS normalization-closure route map — numerical checks (CPP Patch 1209).

Verifies (1) the Lagrange divisibility diagnostic for the stated overlap-fraction
denominators against |H4| = 14400, and (2) the JUNO falsification trajectory of the
candidate value sin^2 theta_12 = 12/40 = 0.300. Pure-stdlib; no deps.
"""

H4 = 14400  # |H4|, the 600-cell symmetry group order

# --- Lagrange diagnostic: a genuine subgroup order must divide |H4| ---
print("Lagrange check (subgroup order must divide |H4|=14400):")
admissible = {}
for d in (12, 40, 21):
    ok = (H4 % d == 0)
    admissible[d] = ok
    print(f"  {d:>3}: 14400/{d} = {H4/d:.4f}  -> {'divides' if ok else 'DOES NOT DIVIDE (not a subgroup order)'}")
assert admissible[12] and admissible[40] and not admissible[21], admissible
print("  => 12/21 cannot be a clean subgroup-overlap fraction (21 inadmissible).")

# --- candidate rational values ---
s12 = 12 / 40
s23 = 12 / 21
print(f"\nsin^2 th12 = 12/40 = {s12:.4f}")
print(f"sin^2 th23 = 12/21 = {s23:.4f}")
assert abs(s12 - 0.300) < 1e-6
assert abs(s23 - 0.5714) < 1e-3

# --- JUNO falsification trajectory for sin^2 th12 ---
juno_central = 0.3092      # JUNO 2025 first physics result
print(f"\nsin^2 th12 = 0.300 vs JUNO 2025 central {juno_central} (+/- 0.0087):")
for sigma in (0.0087, 0.0030, 0.0015):
    tension = abs(juno_central - s12) / sigma
    tag = {0.0087: "JUNO 2025", 0.0030: "JUNO ultimate", 0.0015: "full-run optimistic"}[sigma]
    print(f"  sigma={sigma:.4f} ({tag:<19}): tension = {tension:.2f} sigma")

assert abs(abs(juno_central - s12)/0.0087 - 1.06) < 0.05   # ~1.06 sigma now
assert abs(abs(juno_central - s12)/0.0030 - 3.07) < 0.05   # ~3.07 sigma at ultimate

# --- th23 octant note (informational) ---
nufit_no_3sig_upper = 0.513   # NuFIT 6.0 NO 3-sigma upper bound (SK-incl)
print(f"\nsin^2 th23 = {s23:.4f} vs NuFIT6.0 NO 3sigma upper bound {nufit_no_3sig_upper}: "
      f"{'ABOVE (tension, octant-dependent)' if s23 > nufit_no_3sig_upper else 'inside'}")
print("  (th23 is a DUNE/T2HK target, not a JUNO observable.)")

print("\nVERDICT: 0.300 on ~3-sigma JUNO falsification trajectory; 21 fails Lagrange; "
      "normalization fitted. C7 = HIGH-RISK, not high-payoff. ALL CHECKS PASS")
