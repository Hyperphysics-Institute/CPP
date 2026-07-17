#!/usr/bin/env python3
"""Patch 2527: T-2 geometric-saturation bound (T-1 parked per locked order; see the record).

Capture zone per shell qCP = the AMBIENT screened horizon (registered picture): the Sea screens
single-hadron color at ~1 fm (SF-5); r_c = 1 fm is the registered 1858 convention. The maximal
geometric coat = the zone's full CP content, converted at 4 CPs per hTetra-equivalent (2519).

Density from REGISTERED geometry: every GP is occupied by a CP (glossary); nearest-neighbor
spacing = 600-cell edge = l_unit/phi (AXIM-2, edge = 1/phi in circumradius units); coordination
z = 12 (registered). Packing constant c_pack for a z=12, spacing-d 3D lattice: FCC value sqrt(2);
bracketed conservatively with c_pack in [1, sqrt(2)] since the 4D->3D tessellation detail is the
one small inference (flagged, not silent).

NOTE (OBS-RELIC-1 fence protocol): phi enters via the REGISTERED edge length 1/phi (AXIM-2,
glossary) -- its provenance is the lattice geometry, documented here as independent of the
fenced observation. phi^3 = 2 + sqrt(5): the sqrt(5) below is derived, not summoned.
"""
import math

phi = (1 + math.sqrt(5)) / 2
l_unit = 0.589                       # fm, registered
r_c = 1.0                            # fm, registered 1858 convention (SF-5 ~1 fm)
d = l_unit / phi                     # nearest-neighbor spacing, registered edge length
zone = (4/3) * math.pi * r_c**3

results = {}
for c_pack, label in [(1.0, "c_pack=1 (loose)"), (math.sqrt(2), "c_pack=sqrt2 (FCC, z=12)")]:
    rho = c_pack / d**3
    cps = rho * zone
    C_per_k = cps / 4.0              # hTetra-equivalents (4 CPs each, 2519 convention)
    m_per_k = C_per_k / 32.0         # rings per shell qCP
    results[label] = (rho, cps, C_per_k, m_per_k)
    print(f"{label}: rho = {rho:.1f} CP/fm^3; zone CPs = {cps:.0f}; "
          f"C/k = {C_per_k:.1f} hTe; m/k = {m_per_k:.3f}")

lo, hi = results["c_pack=1 (loose)"][3], results["c_pack=sqrt2 (FCC, z=12)"][3]
T1v = 0.4468
print(f"\nT-2 MAXIMAL bound: m/k in [{lo:.3f}, {hi:.3f}]  vs target {T1v}")
print(f"  closed form: m/k = (pi/96) * c_pack * phi^3 * (r_c/l_unit)^3, with phi^3 = 2+sqrt(5) "
      f"= {phi**3:.4f} (sqrt5 provenance: registered edge = 1/phi)")

# Necessary-condition test (asymmetric, pre-stated): corrections to the maximal bound only SUBTRACT
# (species composition, structural yield). Route survives iff max >= target.
assert lo >= T1v, "maximal bound below target would KILL the route (nothing adds)"
print(f"  NECESSARY CONDITION PASSED: maximal bound >= target (headroom x{lo/T1v:.2f}-x{hi/T1v:.2f})")

f_needed = (T1v/hi, T1v/lo)
print(f"  required species/structural yield fraction: f = {f_needed[0]:.3f}-{f_needed[1]:.3f}")
print(f"  (i.e., roughly HALF the zone content must be hTetra-formable to land on target)")

print("\nREADING: STRUCTURAL-PARTIAL. Bands: D-strong NO (band above window); D-directional NOT")
print("claimable (band [0.68, 0.96] sits above [0.30, 0.67]); NOT K1 (this is an upper bound,")
print("not a forced value -- the route is ALIVE pending the named pin).")
print("NAMED PIN NB-T2-1: the Sea's species composition -> f (hTetra-formable fraction of zone")
print("content); derivable-in-principle from the registered 0672a locks/sinks as its OWN")
print("pre-registered derivation; needed value 0.47-0.66. ALL CHECKS PASS")
