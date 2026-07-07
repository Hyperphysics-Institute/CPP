#!/usr/bin/env python3
"""Patch 2318 -- G4 Stage 2, S2-2: the coat-mode vertex. Result: an ADLER ZERO, derived from
the campaign's own exact symmetry -- the vertex is derivative-coupled, not coat-strength.

Chain (registered items only):
  (i)  The uniform delta|SSV| component decouples from the shell-broadcast EXACTLY
       (1108; recomputed exact at 2313: Sum v_hat = 0, algebraic).
  (ii) Every coupling in the corpus routes through that broadcast: Sea-internal (c05) and
       field<->matter (C5-only, THEO-SR-EIN-4). The coat itself is broadcast-built
       polarization. [Named condition C-f: no non-broadcast coupling exists in the corpus.]
  (iii) Therefore E_coat[|SSV| + const] = E_coat[|SSV|] exactly -> dE_coat/d(uniform) = 0
       -> the vertex couples to GRADIENTS of the mode only (Goldstone/Adler structure).
  (iv) RADIATIVE route: emitted quanta at omega ~ v/b have k = omega/c_s = v/(c b) (c_s = c,
       2317/C-e). Derivative coupling adds amplitude factor (k * l_coat), l_coat <= R_s
       -> power factor (k R_s)^2 ON TOP of the multipole (v/c)^3. Computed vs needed: the
       radiative route dies by 13-19 ORDERS. R3 CLOSED-negative (no enhancement; suppression).
  (v)  NEAR-ZONE route: reactive gradients at the encounter scale have k_eff ~ 1/b, so the
       near-zone coupling carries (R_s/b) ~ 0.2-0.8 -- ORDER UNITY, not Adler-suppressed.
       But for a linear gapless field the reactive energy RETURNS unless (a) it detaches as
       radiation (dead, (iv)) or (b) the substrate possesses INTRINSIC dissipation at the
       PCD level. (b) is exactly the DM-4 Stage-0(ii) capture-aftermath ruling -> FOUNDER FORK.
  (vi) SUFFICIENCY: because the Stage-1 budget is favorable, a tiny intrinsic fraction
       rescues capture: f_needed ~ needed_eff / (R_s/b)^2 ~ 1e-4..1e-2. The fork is sharp.
"""
import itertools, numpy as np, sympy as sp

checks = []

# (i)+(iii) the Adler zero at k=0, exact: shell-sum of a uniform mode value is zero
phi = (1 + sp.sqrt(5))/2
vs = []
for s1, s2 in itertools.product([1,-1],[1,-1]):
    vs += [sp.Matrix([0,s1,s2*phi]), sp.Matrix([s1,s2*phi,0]), sp.Matrix([s2*phi,0,s1])]
n = sp.sqrt(1+phi**2)
S = sp.simplify(sum((v/n for v in vs), sp.zeros(3,1)))
checks.append(("Adler zero exact: uniform mode component -> shell-broadcast response 0 (Sum v = 0, algebraic) -> vertex(k=0) = 0",
               S == sp.zeros(3,1), "algebraic zero"))

C = 2.998e8
RS = 25.42e-15
ANCHORS = ((10, 145e-15, 2.0e4), (50, 79e-15, 8.2e2), (200, 31e-15, 51.0))  # v[km/s], b_max, E_coat/E_col (LOW coat 0.144 MeV -> conservative needed eff uses HIGH ratio? use low-coat = HARDEST needed)
# needed efficiency = 1/(E_coat/E_col); use the LOW-coat (0.144 MeV) ratios = hardest case? No:
# Stage-1 registered ratios spanned coat 0.144..0.6; the CHARITABLE (easiest survival) ask uses the
# HIGH ratio. We test the radiative route against the EASIEST ask and it still dies:
EASIEST_ASK = {10: 1/8.5e4, 50: 1/3.4e3, 200: 1/2.1e2}

print(" radiative route (Adler x multipole) vs the EASIEST ask:")
worst_gap = None
rows = []
for vkms, b, _ in ANCHORS:
    v = vkms*1e3
    k = v/(C*b)                      # radiated wavenumber, c_s = c
    adler = (k*RS)**2
    dip   = (v/C)**3
    eff   = adler*dip
    need  = EASIEST_ASK[vkms]
    gap   = need/eff
    rows.append((vkms, adler, eff, need, gap))
    worst_gap = gap if worst_gap is None else min(worst_gap, gap)
    print(f"  v={vkms:>3}: (kR_s)^2 = {adler:.1e}; eff_rad = {eff:.1e}; ask = {need:.1e}; GAP = x{gap:.1e}")
checks.append((f"radiative route DEAD at every anchor even vs the easiest ask (min gap x{worst_gap:.0e} >= 1e13)",
               worst_gap > 1e13, [f"{r[4]:.0e}" for r in rows]))

print(" near-zone coupling scale (NOT Adler-suppressed; k_eff ~ 1/b):")
nz = {vkms: RS/b for vkms, b, _ in ANCHORS}
for vk, x in nz.items(): print(f"  v={vk:>3}: R_s/b_max = {x:.2f}")
checks.append(("near-zone coupling order-unity at all anchors (0.17-0.82) -- the reactive channel is open in COUPLING; its FATE is the dissipation ruling",
               all(0.1 < x < 1.0 for x in nz.values()), nz))

print(" sufficiency of intrinsic dissipation (the fork's stakes):")
suff = {}
for vkms, b, _ in ANCHORS:
    need = EASIEST_ASK[vkms]
    f = need/(RS/b)**2
    suff[vkms] = f
    print(f"  v={vkms:>3}: f_intrinsic needed ~ {f:.1e}")
checks.append(("a PCD-level intrinsic dissipation fraction f ~ 4e-4 (dwarfs) .. 7e-3 (200 km/s) SUFFICES -- the fork is sharp and small",
               suff[10] < 1e-3 and suff[200] < 1e-1, suff))

npass = 0
for name, ok, val in checks:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    npass += ok
print(f"{npass}/{len(checks)} PASS")
assert npass == len(checks)
