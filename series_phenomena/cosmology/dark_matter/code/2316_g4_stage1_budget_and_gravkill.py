#!/usr/bin/env python3
"""Patch 2316 -- G4 Stage 1: coupling inventory quantification (OPEN-DM-CAPTURE-1).

(1) BRANCH (a) KILL-CHECK: if the rod pair couples to the gapless |SSV| mode ONLY at
    gravitational strength, the encounter loss is quadrupole-bremsstrahlung class:
    DeltaE_grav ~ G mu^2 v^5 / (c^5 b) (order-unity prefactor irrelevant at this verdict scale).
    Computed at the REGISTERED 2311 kinematics triples -> DeltaE/E_col ~ 1e-53. The kill
    condition's premise ("only gravitational-strength -> capture dies") is now QUANTIFIED:
    dead by ~53 orders, at every anchor velocity.
(2) ENERGY BUDGET: E_coat / E_col ~ 1e3-1e5 -- capture does NOT need an efficient channel;
    it needs a coat-scale channel at efficiency ~1e-5..1e-3. The favorable direction.
(3) THE SUPPRESSION STRUCTURE (Stage-2 frame): subsonic Landau protection. For a gapless
    linear mode with speed c_s, steady subsonic motion cannot radiate (Cherenkov threshold);
    encounter transients radiate with multipole powers of (v/c_s). Reference band computed
    at c_s = c (broadcast speed; c_s itself UNPINNED -- 1169 gives gaplessness, not speed,
    its own next-item). Dipole reference (v/c)^3 ~ 1e-14..1e-11: the visible Stage-2 tension.
Registered inputs: 2311 kinematics (v, b_max, E_col); coat scale 0.144-0.6 MeV (1895/1868);
mu = m_rod/2, m_rod = 25.344 GeV.
"""
import math
G, C = 6.674e-11, 2.998e8
MEV_J = 1.602e-13
M_ROD_MEV = 25344.0
MU_KG = (M_ROD_MEV/2) * MEV_J / C**2
COAT_MEV = (0.144, 0.6)                      # q-channel residual .. full coat scale (1895)
TRIPLES = ((10, 145, 7.04e-6), (50, 79, 1.76e-4), (200, 31, 2.82e-3))  # v[km/s], b_max[fm], E_col[MeV] (2311)

checks = []
rows = []
for vkms, bfm, Ecol_MeV in TRIPLES:
    v, b = vkms*1e3, bfm*1e-15
    dE_grav = G * MU_KG**2 * v**5 / (C**5 * b) / MEV_J          # MeV
    r_grav  = dE_grav / Ecol_MeV
    budget  = tuple(cm / Ecol_MeV for cm in COAT_MEV)
    beta    = v / C
    rows.append((vkms, r_grav, budget, beta, beta**3))
    print(f" v={vkms:>3} km/s b_max={bfm:>3} fm : DeltaE_grav/E_col = {r_grav:.1e} ; "
          f"E_coat/E_col = {budget[0]:.1e}..{budget[1]:.1e} ; v/c = {beta:.1e} ; (v/c)^3 = {beta**3:.1e}")

checks.append(("branch (a) dead by >= 45 orders at every registered anchor",
               all(r[1] < 1e-45 for r in rows), [f"{r[1]:.0e}" for r in rows]))
checks.append(("energy budget favorable: E_coat/E_col >= 2e2 at every anchor (needed efficiency <= ~5e-3)",
               all(r[2][1] > 2e2 for r in rows), [f"{r[2][1]:.0e}" for r in rows]))
checks.append(("subsonic depth: v/c_s <= 7e-4 at all anchors (c_s = c reference; Landau/Cherenkov regime)",
               all(r[3] < 7e-4 for r in rows), [f"{r[3]:.0e}" for r in rows]))
# The Stage-2 tension band, stated as arithmetic (NOT a verdict): needed efficiency vs the
# dipole-reference suppression at c_s = c. If the coat-mode vertex is coat-strength and the
# leading transient is dipole, efficiency ~ (v/c_s)^3 <= 1e-11 < needed 1e-5..1e-3 -> the
# survive routes are (i) c_s << c, (ii) sub-dipole/contact transfer (near-zone drag), or
# (iii) vertex enhancement -- each computable from registered objects (1868 coat; c05 dispersion).
need_lo = min(1/r[2][1] for r in rows); dip_hi = max(r[4] for r in rows)
checks.append((f"Stage-2 tension REGISTERED: needed eff >= {need_lo:.0e} vs dipole-ref (v/c)^3 <= {dip_hi:.0e} "
               f"(gap ~{need_lo/dip_hi:.0e}) -- survive routes named, none pre-judged",
               need_lo/dip_hi > 1e3, "tension real"))

npass = 0
for name, ok, val in checks:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  ({val})")
    npass += ok
print(f"{npass}/{len(checks)} PASS")
assert npass == len(checks)
