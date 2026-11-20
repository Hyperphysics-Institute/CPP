#!/usr/bin/env python3
"""Patch 4492 illustration script: what the Nexus's one-quantum update must look like, and how faint the atom's trail in the
Sea must be.

The founder (4492): the atom's core CPs and its KE/DP-arc CPs are one entangled quantum; when the core is bumped, the Nexus
tensor updates every CP of the quantum at once, so the arcs in the other path respond too.

  U1  A uniform update (every part of the quantum gets the same change of phase) leaves the fringes untouched for any path
      separation d: contrast 1. It cannot blur anything.
  U2  The update a momentum kick q makes is position-dependent: each part's phase changes by q.x, so the two paths differ by
      q.d. Averaged over the photon's random directions (dipole emission, axis perpendicular to d), the contrast is the closed
      form C = j0(kd) - j2(kd)/2 (4491): 1 at d = 0, zero near 0.437 wavelengths, partial revival. Only this kind of update
      reproduces the observed loss and revival (Chapman et al. 1995).
  S1  The trail in the Sea. If every Moment of flight left a record of the path in the DP Sea with overlap g between the two
      paths' records, the contrast after N Moments would be g^N. Taking one Moment as one Planck time (QM-4's bath correlation
      time; the corpus value) and a 1 ms flight, N ~ 1.9e40; keeping half the contrast needs 1 - g < ln2 / N, i.e. a per-Moment
      distinguishability D = sqrt(1 - g^2) below about 1e-20.
  S2  QM-4's dephasing rate gamma = sea_strength^2 E_P / hbar (sea_strength = 0.185), applied to a free atom, would give a
      coherence time of order 1e-42 s: it cannot apply to free flight, only to couplings that leave records.

Pure Python. Illustrations of standard formulas under the stated assumptions, not tests of CPP. Exit 0 if every check holds.
"""
import math

rows = []


def C_dipole(x):
    if x == 0:
        return 1.0
    j0 = math.sin(x) / x
    j2 = (3 / x ** 2 - 1) * math.sin(x) / x - 3 * math.cos(x) / x ** 2
    return j0 - j2 / 2


k = 2 * math.pi  # wavelength = 1
# U1: uniform phase change phi applied to both paths: relative phase 0 -> contrast |<e^{i(phi - phi)}>| = 1
import cmath
phis = [2 * math.pi * j / 64 for j in range(64)]  # random-looking uniform phases, same on both paths
for d in (0.0, 0.437, 1.0):
    c = abs(sum(cmath.exp(1j * (phi - phi)) for phi in phis) / len(phis))  # an identity: relative phase is zero
    rows.append(("U1 uniform update", f"d = {d} lambda", c, abs(c - 1) < 1e-12))
# U2: position-dependent update, closed form
for d, expect in ((0.0, 1.0), (0.4367, 0.0), (0.6737, 0.3355)):
    c = abs(C_dipole(k * d))
    rows.append(("U2 position-dependent update", f"d = {d} lambda", c, abs(c - expect) < 2e-3))

# S1: Sea trail
t_P = 5.391e-44
t_flight = 1e-3
N = t_flight / t_P
eps_max = math.log(2) / N          # 1 - g allowed for C >= 0.5
D_max = math.sqrt(2 * eps_max)     # D ~ sqrt(2(1-g)) for g near 1
rows.append(("S1 Moments in a 1 ms flight", "one Moment = t_P", N, 1e40 < N < 1e41))
rows.append(("S1 allowed per-Moment D for C >= 0.5", "g^N >= 1/2", D_max, D_max < 1e-19))

# S2: QM-4 rate applied to free flight
sea = 0.185
gamma = sea ** 2 / t_P  # E_P / hbar = 1 / t_P
tau = 1 / (2 * gamma)
rows.append(("S2 QM-4 gamma = sea^2 E_P/hbar", "per second", gamma, gamma > 1e41))
rows.append(("S2 its coherence time 1/(2 gamma)", "seconds", tau, tau < 1e-41))

print("ONE-QUANTUM UPDATE AND SEA-TRAIL TABLE (Patch 4492)")
for name, scope, val, ok in rows:
    print(f"{name:40s} {scope:20s} {val:12.4g}  {'PASS' if ok else 'FAIL'}")
n = sum(r[3] for r in rows)
print(f"{n}/{len(rows)} PASS")
raise SystemExit(0 if n == len(rows) else 1)
