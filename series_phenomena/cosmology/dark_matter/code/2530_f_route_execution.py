#!/usr/bin/env python3
"""Patch 2530 verify — NB-T2-1 route execution checks.

Documents the adjudication numerics and verifies the frozen-reading application:
  1. The draft-tier 25/25/50 statement maps to x = 1/2, f_hTe = 1/2 — inside the pass window
     (i.e., WHY the 2529 null-baseline trap was decision-relevant).
  2. R-B directional note: Boltzmann factor for a 1 MeV differential at kT_form = 16.5 keV
     (equilibrium-there would saturate the skew; premise unregistered, note only).
  3. Frozen-reading application: no derived f exists -> Branch I per 2529 §6 (encoded as the
     absence of a derivation product, not a computed value).
  4. Reopening contract: the frozen mapping x -> f_hTe -> m/k band -> charter branch is a total
     function — tested at sample dial values so a future registration drops in with zero decisions.
"""
import math

ok = True
def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and cond

# Frozen constants (2527/2529)
phi = (1 + math.sqrt(5)) / 2
B_lo = (math.pi / 96) * 1.0 * phi**3 * (1.0 / 0.589) ** 3
B_hi = B_lo * math.sqrt(2)
T1, dT1 = 0.4468, 0.0054
PASS_LO, PASS_HI = T1 / B_hi, 0.5          # reachable window per 2529 (conditional ceiling)
DS_LO, DS_HI = 0.436, 0.458                 # D-strong (charter v1.1)
DD_LO, DD_HI = 0.30, 0.67                   # D-directional

# --- 1. The .tex null baseline ---
pair_fracs = {"eDP": 0.25, "qDP": 0.25, "hDP_AB": 0.50}
check("draft-tier fractions sum to 1", abs(sum(pair_fracs.values()) - 1.0) < 1e-12)
x_tex = 2 * pair_fracs["qDP"]               # n(qDP)/N with pairs = 2N total
f_tex = 1 - x_tex
check(f"25/25/50 -> x = {x_tex:.2f}, f_hTe = {f_tex:.2f} (the null baseline)", abs(f_tex - 0.5) < 1e-12)
check("null baseline lies inside the pass window (the trap was decision-relevant)",
      PASS_LO <= f_tex <= PASS_HI + 1e-12)

# --- 2. R-B directional note ---
kT_form_MeV = 0.0165
boltz = math.exp(-1.0 / kT_form_MeV)        # 1 MeV differential
check(f"Boltzmann note: exp(-1 MeV / 16.5 keV) = e^-{1.0/kT_form_MeV:.1f} ~ {boltz:.1e} "
      "(equilibrium-at-kT_form would saturate the skew; premise unregistered)", boltz < 1e-20)

# --- 3. Frozen-reading application ---
derived_f = None                            # NO derivation product exists: R-A miss, R-B/R-C Branch I
check("no derived f exists -> 2529 §6 bullet 4 -> Branch I / NB-F-1 -> D3", derived_f is None)

# --- 4. Reopening contract: total function on the dial ---
def frozen_reading(x):
    """A future declarative-strength registration of x resolves the campaign with zero new decisions."""
    f = 1 - x
    if f > 0.5 + 1e-12:
        return "HALT-DIAGNOSE (conditional-floor breach; see 2530 §4 rider)"
    mk_lo, mk_hi = f * B_lo, f * B_hi
    if f < PASS_LO:
        return f"K1-direction -> D3 (m/k in [{mk_lo:.3f}, {mk_hi:.3f}])"
    d_strong = (mk_lo <= DS_HI) and (mk_hi >= DS_LO)
    d_dir = (mk_hi >= DD_LO) and (mk_lo <= DD_HI)
    tag = "D-strong-overlap" if d_strong else ("D-directional" if d_dir else "outside-bands")
    return f"{tag} (m/k in [{mk_lo:.3f}, {mk_hi:.3f}]) -> panel adjudication"
for x_sample in (0.50, 0.52, 0.534, 0.60, 0.80, 0.45):
    print(f"       reopening test x = {x_sample:.3f}: {frozen_reading(x_sample)}")
check("reopening mapping is total on sampled dials (no undefined branch)",
      all(isinstance(frozen_reading(v), str) for v in (0.45, 0.5, 0.534, 0.9)))

print("\nALL CHECKS PASS" if ok else "\nCHECK FAILURES PRESENT")
raise SystemExit(0 if ok else 1)
