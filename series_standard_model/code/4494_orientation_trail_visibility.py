#!/usr/bin/env python3
"""Patch 4494 illustration script: does an energy-free orientation trail spoil the fringes?

The founder (4494): after the core passes, the DPs it went by are left with their plus/minus orientation transposed -- a trail,
but no energy lost or given. Model each Sea DP's orientation as a two-state system (spin-1/2 style). The fringe visibility
left after the two arms recombine is the overlap of the Sea's final states for "core went down arm A" and "core went down
arm B" (Englert's relation, 4445, 4490):

  V = |Tr( rho_Sea  U_A^dagger U_B )|

  T1  The trail lies only in the arm the core took; one DP fully flipped (theta = pi): V = 0 for a start across the turning axis
      and for a random start; V = 1 only for a start along the turning axis (the turn then adds only a phase). So the record holds
      averaged over orientations, not for every one.
  T2  A million DPs each turned by a small angle (1e-3 rad), only in the core's arm: V = cos(theta/2)^N ~ exp(-N theta^2 / 8).
  T3  The same with the Sea's orientations random to begin with (maximally mixed): V is unchanged -- an unknown starting
      orientation does not hide the trail.
  T4  Both arms trailed alike (the arm without the core flipped the same way): V = 1.
  T5  The trail undone before the arms meet: V = 1.

numpy only; illustrations of the standard overlap formula, not tests of CPP. Exit 0 if every check holds.
"""
import numpy as np


def R(theta):
    """Rotation of a two-state orientation by angle theta about x."""
    c, s = np.cos(theta / 2), np.sin(theta / 2)
    return np.array([[c, -1j * s], [-1j * s, c]])


I2 = np.eye(2)
up = np.array([[1, 0], [0, 0]], complex)
mixed = I2 / 2


def V_single(rho, UA, UB):
    return abs(np.trace(rho @ UA.conj().T @ UB))


rows = []
# T1: core's arm only: arm A path leaves the DP flipped, arm B leaves it alone
v = V_single(up, R(np.pi), I2)
rows.append(("T1 one DP flipped, core's arm only", "theta = pi, z start", v, abs(v) < 1e-12))
v = V_single(mixed, R(np.pi), I2)
rows.append(("T1 same, random starting orientation", "theta = pi, mixed", v, abs(v) < 1e-12))
xplus = 0.5 * np.array([[1, 1], [1, 1]], complex)
v = V_single(xplus, R(np.pi), I2)
rows.append(("T1 same, start along the turning axis", "theta = pi, x start", v, abs(v - 1) < 1e-12))
# T2: N DPs, small angle, product of single overlaps
N, th = 10**6, 1e-3
v1 = V_single(up, R(th), I2)
v = v1 ** N
rows.append(("T2 1e6 DPs turned 1e-3 rad, core's arm", "pure start", v, abs(v - np.exp(-N * th**2 / 8)) < 1e-4))
v1m = V_single(mixed, R(th), I2)
vm = v1m ** N
rows.append(("T3 same, random starting orientations", "mixed start", vm, abs(vm - v) < 1e-9))
# T4: both arms trailed alike: whichever arm the core took, both DP sets end flipped the same way
v = V_single(up, R(np.pi), R(np.pi))
rows.append(("T4 both arms trailed alike", "theta = pi", v, abs(v - 1) < 1e-12))
# T5: trail undone before the arms meet
v = V_single(up, R(-np.pi) @ R(np.pi), I2)
rows.append(("T5 trail undone before recombination", "flip then unflip", v, abs(v - 1) < 1e-12))

print("ORIENTATION-TRAIL TABLE (Patch 4494)  V = |Tr(rho U_A^+ U_B)|")
for name, scope, val, ok in rows:
    print(f"{name:42s} {scope:20s} V = {val:.4f}  {'PASS' if ok else 'FAIL'}")
n = sum(r[3] for r in rows)
print(f"{n}/{len(rows)} PASS")
raise SystemExit(0 if n == len(rows) else 1)
