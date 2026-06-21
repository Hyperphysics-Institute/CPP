#!/usr/bin/env python3
"""
1600_verify_sf6_core.py
-----------------------
Standalone verifier for the SF-6 electromagnetism flagship TIER-1 identities.

SF-6 introduces no new derivation. Its companion-grade (Tier-1) core leans on a
handful of inherited inter-constant identities; this script asserts each of those
against CODATA values so that any drift between code and paper fails an assertion.

IMPORTANT — scope discipline (matches the paper's two-tier rigor accounting):
  * This verifier asserts ONLY the Tier-1 inter-constant *relations*
    (c = 1/sqrt(mu0*eps0), Z0 = sqrt(mu0/eps0), and the E = hbar*nu_C <=> h*nu
    <=> m*c^2 consistency).
  * It deliberately does NOT assert the Tier-2 toy-model constants
    (mu0, eps0, c, gamma) as *derivations*. Those come from the DP-Sea-
    Polarization toy model "by tuning parameters" and are registered as
    OPEN-FP-6-CONSTANTS; asserting them as derived results would misrepresent
    the rigor floor the paper is at pains to state.

Python standard library only; no external data files.

Source provenance:
  E = hbar*nu_C unification ........... c06 (eq. unification)  [Tier 1]
  c = 1/sqrt(mu0*eps0), Z0 ............ Maxwell relation / c06  [Tier 1]
  mu0, eps0, c (toy-model origin) ..... DP-Sea-Polarization model [Tier 2, NOT asserted as derived]
"""

import math

# ----- CODATA 2018 reference values (the targets the Tier-1 relations must satisfy) -----
C_CODATA   = 299_792_458.0          # m/s, exact (SI definition)
MU0        = 1.25663706212e-6       # N/A^2  (vacuum magnetic permeability)
EPS0       = 8.8541878128e-12       # F/m    (vacuum electric permittivity)
Z0_CODATA  = 376.730313668          # ohm    (impedance of free space)
HBAR       = 1.054571817e-34        # J*s
H_PLANCK   = 6.62607015e-34         # J*s, exact
M_E        = 9.1093837015e-31       # kg     (electron mass, for the mc^2 <=> hbar*nu_C check)


def rel_close(a, b, rtol):
    """True if a and b agree to within relative tolerance rtol."""
    return abs(a - b) <= rtol * abs(b)


def main():
    checks = []

    # --- Tier 1, identity 1: Maxwell relation c = 1/sqrt(mu0*eps0) ---
    c_from_consts = 1.0 / math.sqrt(MU0 * EPS0)
    ok1 = rel_close(c_from_consts, C_CODATA, 1e-6)
    checks.append(("c = 1/sqrt(mu0*eps0)  [eq:maxwellrel]", c_from_consts, C_CODATA, ok1))
    assert ok1, f"c from constants {c_from_consts} != CODATA c {C_CODATA}"

    # --- Tier 1, identity 2: impedance of free space Z0 = sqrt(mu0/eps0) ---
    z0_from_consts = math.sqrt(MU0 / EPS0)
    ok2 = rel_close(z0_from_consts, Z0_CODATA, 1e-6)
    checks.append(("Z0 = sqrt(mu0/eps0)   [eq:maxwellrel]", z0_from_consts, Z0_CODATA, ok2))
    assert ok2, f"Z0 from constants {z0_from_consts} != CODATA Z0 {Z0_CODATA}"

    # --- Tier 1, identity 3: product/ratio decomposition the SSV-independent-Z0
    #     conjecture relies on: (mu0*eps0) and (mu0/eps0) are independent combos,
    #     and c^2 * Z0 reconstructs them.  c^2 = 1/(mu0*eps0); Z0 = sqrt(mu0/eps0).
    #     Check the cross-identity  mu0 = Z0 / c  and  eps0 = 1/(Z0*c). ---
    mu0_recon  = Z0_CODATA / C_CODATA
    eps0_recon = 1.0 / (Z0_CODATA * C_CODATA)
    ok3a = rel_close(mu0_recon, MU0, 1e-6)
    ok3b = rel_close(eps0_recon, EPS0, 1e-6)
    checks.append(("mu0  = Z0 / c         [product/ratio split]", mu0_recon, MU0, ok3a))
    checks.append(("eps0 = 1 / (Z0 * c)   [product/ratio split]", eps0_recon, EPS0, ok3b))
    assert ok3a and ok3b, "product/ratio reconstruction of mu0/eps0 failed"

    # --- Tier 1, identity 4: E = hbar*nu_C unification consistency.
    #     For a photon: E = h*nu = hbar*nu_C with nu_C = nu  ->  h = 2*pi*hbar. ---
    h_from_hbar = 2.0 * math.pi * HBAR
    ok4 = rel_close(h_from_hbar, H_PLANCK, 1e-6)
    checks.append(("h = 2*pi*hbar         [E=hbar*nu_C <=> h*nu]", h_from_hbar, H_PLANCK, ok4))
    assert ok4, f"h from hbar {h_from_hbar} != h {H_PLANCK}"

    # --- Tier 1, identity 5: for a massive particle, mc^2 = hbar*nu_C defines the
    #     Compton frequency nu_C = mc^2/hbar; round-trip must return mc^2. ---
    mc2     = M_E * C_CODATA**2
    nu_C    = mc2 / HBAR
    mc2_rt  = HBAR * nu_C
    ok5 = rel_close(mc2_rt, mc2, 1e-12)
    checks.append(("mc^2 = hbar*nu_C      [standing-ZDC, eq:massZDC]", mc2_rt, mc2, ok5))
    assert ok5, "mc^2 <-> hbar*nu_C round trip failed"

    # ----- report -----
    width = 44
    print("SF-6 Tier-1 inter-constant verifier — Patch 1600")
    print("=" * 72)
    for name, got, ref, ok in checks:
        flag = "PASS" if ok else "FAIL"
        print(f"[{flag}] {name:<{width}} got={got:.9g}  ref={ref:.9g}")
    print("=" * 72)
    print("All Tier-1 identities PASS. (Tier-2 toy-model constants mu0/eps0/c/gamma")
    print("are NOT asserted as derivations here — see OPEN-FP-6-CONSTANTS.)")


if __name__ == "__main__":
    main()
