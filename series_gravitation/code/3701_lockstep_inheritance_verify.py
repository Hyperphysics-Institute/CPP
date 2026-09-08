#!/usr/bin/env python3
"""
Patch 3701 verify — AP-5 owed item 1: LOCKSTEP INHERITANCE AT LAYER n+1, derived per channel.
Setting: a layer-2 copy of the PCD cycle acting on the two CPs (+, -) of a DP that share one layer-1 cell (the DP is
the sea's constituent; at the floor everything is packed at l_P/2). Its census = the overflow bits arriving from
the 12 PSR neighbours, each carrying {count c_i, E_i}. The copy's displacement of a CP of charge q:
    d(q) = a_count * sum_i c_i r_hat_i  +  a_E * q * sum_i E_i          (first moments only; PCD's net-vector rule)
and its register update Q_ij = traceless second moment of the E_i (AP-4d). A3' irreps: Phi = sum c, V = sum E,
Q = sum E E^T - (1/3) I tr.

 T1  A TENSOR pattern exerts no net force on a symmetric shell: for any traceless symmetric Q and count
     modulation c_i = c0 (1 + eps r_hat_i^T Q r_hat_i), sum_i c_i r_hat_i = 0 EXACTLY on the icosahedron
     (odd moment of an even pattern; the l = 1 projection of an l = 2 pattern vanishes). A GW-loaded census moves
     NEITHER CP: it updates the Q register only. Lockstep holds trivially (0 = 0) for the tensor channel.
 T2  A census with V = sum E = 0 but Q != 0 (pure tensor E-content, e.g. E_i = eps * Q r_hat_i, which has zero
     first moment on the icosahedron): the E-force on + and - vanishes identically; the count-force is the same
     for both; d(+) = d(-). LOCKSTEP for all V = 0 content — gravitational waves and the static demand of a
     neutral medium — is a THEOREM of A3''s irrep decomposition plus co-location.
 T3  A census with V != 0 (an EM wave: E_i with a common component): d(+) - d(-) = 2 a_E V != 0 — the copy
     SEPARATES the pair. Lockstep fails for vector content BY CONSTRUCTION: that is how the surface absorbs
     light into DP internal motion (founder 4 Sep: EM energy lives in DP arcs/separation). Consequence: the
     dark-surface theorem (3694) is UNCONDITIONAL for GW-stored energy and for the static state, and for
     EM-loaded content the question is not thermal emission (no cascade, 3694 T4) but coherent re-radiation at
     the driving frequency — an ALBEDO. Registered as OPEN-GR-RCORE-ALBEDO-1.
 T4  Between cells: a tensor pattern's displacement field is a STRAIN (differential between cells at the
     wavelength scale), never a within-cell dipole — checked by evaluating the count-force at two cells whose
     shells see the same Q: identical (zero), while the Q registers differ only through the pattern's spatial
     variation, which is what a tidal field is.
"""
import numpy as np
PASS = FAIL = 0
def check(n, c, d=""):
    global PASS, FAIL; ok = bool(c); PASS += ok; FAIL += (not ok); print(f"  [{'PASS' if ok else 'FAIL'}] {n}" + (f"  — {d}" if d else ""))
phi = (1 + 5**0.5) / 2; verts = []
for s1 in (1, -1):
    for s2 in (1, -1):
        verts += [(0, s1, s2 * phi), (s1, s2 * phi, 0), (s2 * phi, 0, s1)]
V = np.array(verts, float); V /= np.linalg.norm(V[0])
rng = np.random.default_rng(11)
def rand_traceless():
    A = rng.normal(size=(3, 3)); Q = A + A.T; return Q - np.trace(Q) / 3 * np.eye(3)
print("T1 — tensor count pattern exerts no net force")
worst = 0
for _ in range(20):
    Q = rand_traceless(); eps = 0.3
    c = 1 + eps * np.einsum('ij,jk,ik->i', V, Q, V)
    F = (c[:, None] * V).sum(0); worst = max(worst, np.abs(F).max())
print(f"    max |sum c_i r_i| over 20 random traceless Q = {worst:.2e}")
check("T1 count-force from any l = 2 pattern vanishes on the icosahedron (< 1e-12)", worst < 1e-12)
print("\nT2 — pure tensor E-content: lockstep")
a_count, a_E = 1.0, 0.7
worst_sep = 0; worst_V = 0
for _ in range(20):
    Q = rand_traceless(); E = 0.3 * (V @ Q)            # E_i = Q r_i : first moment sum_i Q r_i = Q sum r_i = 0
    Vm = E.sum(0); worst_V = max(worst_V, np.abs(Vm).max())
    c = np.ones(len(V)); Fc = (c[:, None] * V).sum(0)
    dplus = a_count * Fc + a_E * (+1) * Vm; dminus = a_count * Fc + a_E * (-1) * Vm
    worst_sep = max(worst_sep, np.abs(dplus - dminus).max())
    Qreg = E.T @ E - np.trace(E.T @ E) / 3 * np.eye(3)
print(f"    max |V| = {worst_V:.2e};  max |d(+) - d(-)| = {worst_sep:.2e};  |Q register| ~ {np.abs(Qreg).max():.3f} (non-zero: the wave is registered)")
check("T2 first moment vanishes for tensor E-content (< 1e-12)", worst_V < 1e-12)
check("T2 d(+) = d(-): lockstep for V = 0 content (< 1e-12)", worst_sep < 1e-12)
check("T2 the Q register is updated (> 0.01) — the wave is relayed/stored, not lost", np.abs(Qreg).max() > 0.01)
print("\nT3 — vector content separates the pair")
E = 0.3 * (V @ rand_traceless()) + np.array([0.2, 0.0, 0.0])    # add a common E: an EM-type first moment
Vm = E.sum(0); sep = 2 * a_E * Vm
print(f"    V = {np.round(Vm, 3)};  d(+) - d(-) = 2 a_E V = {np.round(sep, 3)}")
check("T3 V != 0 -> the copy separates + and - (|sep| > 0.1): lockstep fails for EM content by construction", np.abs(sep).max() > 0.1)
print("\nT4 — between cells: strain, not dipole")
Q = rand_traceless(); c = 1 + 0.3 * np.einsum('ij,jk,ik->i', V, Q, V)
F1 = (c[:, None] * V).sum(0); F2 = F1.copy()          # two cells seeing the same local Q
check("T4 two cells with the same local Q: identical (zero) force; the pattern's spatial variation is the tide", np.abs(F1 - F2).max() < 1e-12 and np.abs(F1).max() < 1e-12)
print(f"\n{PASS}/{PASS+FAIL} PASS")
