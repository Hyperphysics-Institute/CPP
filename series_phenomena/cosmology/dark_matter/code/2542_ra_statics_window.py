#!/usr/bin/env python3
"""Patch 2542 -- OPEN-DM-RODCLOSE-1 R-A: the statics window, under the 2541 prereg ONLY.

Blindness order enforced in code: Parts 1-3 are fully symbolic in L (no literal 16 appears);
Part 4 freezes the window objects; ONLY Part 5 performs the pre-registered comparison.

Part 1 -- normalization walk (2450 lineage, re-verified this session by rerunning the artifact):
  S(N) = d2E/dkappa^2 [MeV*fm^2], full-rod, small-kappa: S(8)=+138, S(16)=+291, chord +263.
  Per-length modulus B = S / L_rod, L_rod = N*D, D = 1.15 fm.
Part 2 -- symbolic bend energy at harmonic order (2541 sec1 frozen form):
  E_bend(L) = (1/2) * B * L_rod * kappa_ring^2, kappa_ring = 2*pi/L_rod  ->  2*pi^2*B/(L*D).
Part 3 -- comparators (2541 sec3 union rule): f=1 (per-collision energy ~ kT) and f=3/2
  (mean translational KE (3/2)kT). Accessibility: f*kT >= E_bend(L).
Part 4 -- FROZEN window objects: closure relation kT*L = 2*pi^2*B/(f*D); accessibility bound
  L_min(T); survival floor kT < E_endbond in [40,170] MeV; upper (long-rod) cutoff = Branch I.
Part 5 -- pre-registered comparisons (only here may 16 appear).
"""
import sympy as sp

D = 1.15
S = {"arc_N16": 291.0, "chord_N16": 263.0, "arc_N8": 138.0}
L_rod = {"arc_N16": 16 * D, "chord_N16": 16 * D, "arc_N8": 8 * D}   # normalization walk only
B = {k: S[k] / L_rod[k] for k in S}
B_lo, B_hi = min(B.values()), max(B.values())
print("Part 1 -- per-length modulus B [MeV*fm]:",
      {k: round(v, 3) for k, v in B.items()}, f"-> band [{B_lo:.2f}, {B_hi:.2f}]")
assert B_lo == B["chord_N16"] and B_hi == B["arc_N16"]
assert abs(B["arc_N8"] - B["arc_N16"]) / B["arc_N16"] < 0.06   # ~L scaling coherence

L, Bs, f, kT = sp.symbols('L B f kT', positive=True)
E_bend = sp.simplify(L * D * Bs / 2 * (2 * sp.pi / (L * D))**2)
assert sp.simplify(E_bend - 2 * sp.pi**2 * Bs / (L * D)) == 0
print("Part 2 -- E_bend(L) = 2*pi^2*B/(L*D)  [symbolic, verified]")

# Part 3/4: frozen window objects
rel = sp.Eq(kT * L, 2 * sp.pi**2 * Bs / (f * D))     # closure relation (threshold equality)
C = {(fk, Bk): float(2 * sp.pi**2 * Bv / (fv * D))
     for fk, fv in (("f=1", 1), ("f=3/2", sp.Rational(3, 2))) for Bk, Bv in
     (("B_lo", B_lo), ("B_hi", B_hi))}
union_lo, union_hi = min(C.values()), max(C.values())
print(f"Part 4 -- closure relation kT*L = C [MeV], per comparator/convention: "
      f"{ {k: round(v,1) for k,v in C.items()} }")
print(f"          FROZEN union band: kT*L in [{union_lo:.1f}, {union_hi:.1f}] MeV")
E_endbond = (40.0, 170.0)
print(f"          survival floor: kT < E_endbond in [{E_endbond[0]:.0f}, {E_endbond[1]:.0f}] MeV")
print("          upper (long-rod) cutoff: BRANCH I (kinetic; NB-S3a-1 named)")

print()
print("Part 5 -- PRE-REGISTERED COMPARISONS (window frozen above)")
L16 = 16
kT16_lo, kT16_hi = union_lo / L16, union_hi / L16
print(f"  (a) kT_form | L=16 (union): [{kT16_lo:.1f}, {kT16_hi:.1f}] MeV")
Eb16_lo, Eb16_hi = 2 * 3.14159265358979**2 * B_lo / (L16 * D), 2 * 3.14159265358979**2 * B_hi / (L16 * D)
print(f"      E_bend(16) = [{Eb16_lo:.1f}, {Eb16_hi:.1f}] MeV")
dE_lo, dE_hi = Eb16_lo - E_endbond[1], Eb16_hi - E_endbond[0]
print(f"  (b) DeltaE_close(16) = E_bend - E_endbond = [{dE_lo:.1f}, {dE_hi:.1f}] MeV  (< 0 throughout)")
assert dE_hi < 0
print(f"  (c) survival at derived T: kT_hi = {kT16_hi:.1f} < {E_endbond[0]:.0f} MeV  ->  "
      f"{'CONSISTENT' if kT16_hi < E_endbond[0] else 'INCONSISTENT'}")
kT_old = 0.0165
Lmin_old = union_lo / kT_old, union_hi / kT_old
print(f"  (d) carried kT_form = 16.5 keV -> L_min in [{Lmin_old[0]:.0f}, {Lmin_old[1]:.0f}] planes"
      f"  -> INCONSISTENT with L=16 by ~3 orders (RECORDED, not repaired)")
echo = -68.8
inside = dE_lo < echo < dE_hi
back_Eendbond = (Eb16_lo + Eb16_hi) / 2 - echo
print(f"  (e) cross-lineage echo (NOT an input): dance ring-straight {echo} MeV sits "
      f"{'INSIDE' if inside else 'OUTSIDE'} the DeltaE_close(16) band; "
      f"back-implied E_endbond ~= {back_Eendbond:.0f} MeV (cf. 102 MeV contact lock; echo only)")
print()
print("FENCE: no new sqrt(5) introduced in this derivation; alpha_s = 5/(8*phi) enters "
      "UPSTREAM inside the registered 2450 functional (pre-existing lineage) -- noted per procedure.")
print("ALL ASSERTIONS PASS")
