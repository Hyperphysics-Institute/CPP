#!/usr/bin/env python3
"""Patch 2538 verify -- the sec6g stoichiometric convergence (structure only, no derivation).

Checks that the founder's sec6g formation story reproduces the registered Candidate-B structure:
  1. Plane unit = 2 x (eDP-qDP) = 2 eDP + 2 qDP = 4 eCP + 4 qCP = 8 CPs (matches the registered
     element-plane: 4 qCPs at square corners + 4 eCPs on diagonals).
  2. Element = 2 planes = 4 eDP + 4 qDP = 16 CPs, priced 4*88 + 4*264 = 1408 MeV (2452 mass lock).
  3. Ring = 8 elements = 16 planes (N_planes = 16; founder's "stack 16 high"); 8 x 1.408 = 11.264 GeV.
  4. hDP-route identity: hDP-A + hDP-B = (+e,-q) + (-e,+q) = 2 eCP + 2 qCP = same CP content as
     one eDP-qDP unit -- both pairings feed the identical plane unit (the Q4 restructuring premise).
"""
ok = True
def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and cond

# CP contents
eDP = {"eCP": 2, "qCP": 0}
qDP = {"eCP": 0, "qCP": 2}
unit = {k: eDP[k] + qDP[k] for k in eDP}                     # one eDP-qDP unit
plane = {k: 2 * unit[k] for k in unit}                       # 2 units
check("plane = 4 eCP + 4 qCP = 8 CPs", plane == {"eCP": 4, "qCP": 4})

element = {k: 2 * plane[k] for k in plane}                   # 2 planes
check("element = 8 eCP + 8 qCP = 16 CPs = 4 eDP + 4 qDP", element == {"eCP": 8, "qCP": 8})
check("element mass 4*88 + 4*264 = 1408 MeV", 4 * 88 + 4 * 264 == 1408)

check("ring: 8 elements = 16 planes; mass 8 * 1.408 = 11.264 GeV",
      8 * 2 == 16 and abs(8 * 1.408 - 11.264) < 1e-9)

hDP_A = {"eCP": 1, "qCP": 1}   # +eCP / -qCP (canonical labels; content count only)
hDP_B = {"eCP": 1, "qCP": 1}   # -eCP / +qCP
hpair = {k: hDP_A[k] + hDP_B[k] for k in hDP_A}
check("hDP-A + hDP-B has identical CP content to one eDP-qDP unit", hpair == unit)

print()
print("ALL CHECKS PASS" if ok else "FAILURES PRESENT")
raise SystemExit(0 if ok else 1)
