#!/usr/bin/env python3
"""Patch 4489 verify script: the entanglement budget (monogamy) and the size of the ledger.

The founder's answer to 4488 §6 asks (i) whether there is a maximum amount of entanglement effect, and
(ii) how the universe could keep the accounting, e.g. a table of "percentage of entanglement" of every CP
with every other CP. This script checks three standard facts the reading leans on:

  Monogamy rows (Coffman-Kundu-Wootters, PRA 61, 052306, 2000): for three two-level units A, B, C in a pure state,
         tau(A:B) + tau(A:C) <= tau(A:BC) <= 1. A two-level unit has a budget of one (a d-level unit: log2 d, in squashed entanglement); what it shares with B it cannot
         also share with C. Checked on the singlet-plus-spectator, W and GHZ states, and 2000 random states.
  T1     A pairwise table misses the tie: the GHZ state has ZERO pairwise entanglement for every pair,
         yet A is fully tied to BC (tau(A:BC) = 1). So "percentage of entanglement of every CP with every
         other CP" cannot be the ledger.
  S1     Ledger size: the joint state of N two-level units needs 2^N complex numbers; a pairwise table
         needs N(N-1)/2. Printed for small N and for N = 300 (where 2^N exceeds 10^90).

numpy only. Exit 0 if every check holds.
"""
import numpy as np

rng = np.random.default_rng(4489)
SY = np.array([[0, -1j], [1j, 0]])
YY = np.kron(SY, SY)


def rho_of(psi):
    psi = psi / np.linalg.norm(psi)
    return np.outer(psi, psi.conj())


def partial_trace(rho, keep, n=3):
    """Keep the listed qubits (sorted), trace the others. Qubit 0 is the most significant."""
    rho = rho.reshape([2] * (2 * n))
    trace_out = [q for q in range(n) if q not in keep]
    for k, q in enumerate(sorted(trace_out, reverse=True)):
        m = n - k
        rho = np.trace(rho, axis1=q, axis2=q + m)
    d = 2 ** len(keep)
    return rho.reshape(d, d)


def concurrence(r2):
    """Wootters concurrence of a two-qubit density matrix."""
    rt = YY @ r2.conj() @ YY
    ev = np.sqrt(np.abs(np.sort(np.linalg.eigvals(r2 @ rt).real)[::-1]))
    return max(0.0, ev[0] - ev[1] - ev[2] - ev[3])


def tangles(psi):
    r = rho_of(psi)
    rA = partial_trace(r, [0])
    t_A_BC = 4 * np.linalg.det(rA).real          # pure state: tau(A:BC) = 4 det(rho_A)
    t_AB = concurrence(partial_trace(r, [0, 1])) ** 2
    t_AC = concurrence(partial_trace(r, [0, 2])) ** 2
    return t_AB, t_AC, t_A_BC


def ket(bits):
    v = np.zeros(8, complex)
    v[int(bits, 2)] = 1
    return v


states = {
    "singlet(AB) + spectator C": (ket("010") - ket("100")),
    "W state": (ket("100") + ket("010") + ket("001")),
    "GHZ state": (ket("000") + ket("111")),
}

rows = []
ok_all = True
for name, psi in states.items():
    tab, tac, tabc = tangles(psi)
    ok = tab + tac <= tabc + 1e-9 and tabc <= 1 + 1e-9
    ok_all &= ok
    rows.append((name, tab, tac, tabc, ok))

worst = -1.0
for _ in range(2000):
    psi = rng.normal(size=8) + 1j * rng.normal(size=8)
    tab, tac, tabc = tangles(psi)
    worst = max(worst, tab + tac - tabc)
rand_ok = worst <= 1e-9
ok_all &= rand_ok

print("MONOGAMY TABLE (Patch 4489): tau = tangle = concurrence^2; budget per unit = 1")
print(f"{'state':28s} {'tau(A:B)':>9s} {'tau(A:C)':>9s} {'sum':>7s} {'tau(A:BC)':>10s}  verdict")
for name, tab, tac, tabc, ok in rows:
    print(f"{name:28s} {tab:9.4f} {tac:9.4f} {tab + tac:7.4f} {tabc:10.4f}  {'PASS' if ok else 'FAIL'}")
print(f"{'2000 random pure states':28s} max[tau(A:B)+tau(A:C)-tau(A:BC)] = {worst:+.2e}  {'PASS' if rand_ok else 'FAIL'}")

g = [r for r in rows if r[0] == "GHZ state"][0]
t1 = g[1] < 1e-9 and g[2] < 1e-9 and abs(g[3] - 1) < 1e-9
ok_all &= t1
print(f"T1  GHZ: every pairwise tangle 0, tau(A:BC) = {g[3]:.4f} -> a pairwise table misses the tie  {'PASS' if t1 else 'FAIL'}")

print("S1  ledger size: joint state (2^N amplitudes) vs pairwise table (N(N-1)/2 entries)")
for N in (3, 10, 50, 300):
    joint = 2 ** N
    pair = N * (N - 1) // 2
    print(f"    N = {N:4d}: joint = {float(joint):.3e}   pairwise = {pair}")
s1 = 2 ** 300 > 10 ** 90
ok_all &= s1
print(f"S1  2^300 > 10^90  {'PASS' if s1 else 'FAIL'}")
n_checks = len(rows) + 3
print(f"{'ALL PASS' if ok_all else 'SOME FAIL'} ({n_checks} checks)")
raise SystemExit(0 if ok_all else 1)
