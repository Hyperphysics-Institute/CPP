#!/usr/bin/env python3
"""
SM-6 Verification Notebook
===========================
Paper: SM-6 — The Charged Lepton Mass Spectrum from 600-Cell Lattice Geometry
Authors: Thomas Lee Abshier ND, Grok (xAI), Claude Opus (Anthropic), Copilot (Microsoft)
Date: 2 April 2026

Purpose: Independently verify every numerical claim in SM-6.
         Run this script from a clean environment with only numpy/scipy.
         All 10 verification steps should print PASS.
"""

import numpy as np
from itertools import permutations

# ============================================================
# CONSTANTS
# ============================================================
phi = (1 + np.sqrt(5)) / 2  # golden ratio
PHI_INV = 1 / phi

# PDG 2024 lepton masses (MeV)
M_E = 0.51099895
M_MU = 105.6583755
M_TAU = 1776.86

print("=" * 70)
print("  SM-6 VERIFICATION NOTEBOOK")
print("  All 10 verification steps must print PASS")
print("=" * 70)
print(f"\n  Golden ratio φ = {phi:.10f}")
print(f"  1/φ = {PHI_INV:.10f}")
print()

# ============================================================
# STEP 1: Build the 600-cell (120 vertices, 720 edges)
# ============================================================
print("STEP 1: Build the 600-cell")
print("-" * 50)

vertices = []

# 8 vertices: permutations of (±1, 0, 0, 0)
for i in range(4):
    for s in [1, -1]:
        v = [0, 0, 0, 0]
        v[i] = s
        vertices.append(tuple(v))

# 16 vertices: (±1/2, ±1/2, ±1/2, ±1/2)
for s0 in [0.5, -0.5]:
    for s1 in [0.5, -0.5]:
        for s2 in [0.5, -0.5]:
            for s3 in [0.5, -0.5]:
                vertices.append((s0, s1, s2, s3))

# 96 vertices: even permutations of (φ/2, 1/2, 1/(2φ), 0)
half_coords = [phi / 2, 0.5, 1 / (2 * phi), 0.0]
even_perms = [
    p for p in permutations(range(4))
    if sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j]) % 2 == 0
]
for perm in even_perms:
    base = [half_coords[perm[i]] for i in range(4)]
    nonzero_idx = [i for i in range(4) if base[i] != 0.0]
    for mask in range(2 ** len(nonzero_idx)):
        v = list(base)
        for k, idx in enumerate(nonzero_idx):
            if mask & (1 << k):
                v[idx] = -v[idx]
        vertices.append(tuple(v))

# Deduplicate
unique = []
for v in vertices:
    if not any(all(abs(v[i] - u[i]) < 1e-10 for i in range(4)) for u in unique):
        unique.append(v)

V = np.array(unique)
N = len(V)

# Build adjacency matrix
dists = np.zeros((N, N))
for i in range(N):
    for j in range(i + 1, N):
        d = np.linalg.norm(V[i] - V[j])
        dists[i, j] = d
        dists[j, i] = d

edge_length = np.min(dists[dists > 1e-10])
A = (np.abs(dists - edge_length) < 1e-6).astype(float)
np.fill_diagonal(A, 0)

num_edges = int(np.sum(A) / 2)
degree = int(np.sum(A[0, :]))

# Count faces
face_count = 0
for i in range(N):
    for j in range(i + 1, N):
        if A[i, j] > 0.5:
            for k in range(j + 1, N):
                if A[j, k] > 0.5 and A[i, k] > 0.5:
                    face_count += 1

print(f"  Vertices: {N}  (expected: 120)  {'PASS' if N == 120 else 'FAIL'}")
print(f"  Edges:    {num_edges}  (expected: 720)  {'PASS' if num_edges == 720 else 'FAIL'}")
print(f"  Faces:    {face_count}  (expected: 1200)  {'PASS' if face_count == 1200 else 'FAIL'}")
print(f"  Degree:   {degree}  (expected: 12)  {'PASS' if degree == 12 else 'FAIL'}")
print(f"  Edge length: {edge_length:.6f}  (expected 1/φ = {PHI_INV:.6f})  "
      f"{'PASS' if abs(edge_length - PHI_INV) < 1e-6 else 'FAIL'}")

step1 = (N == 120 and num_edges == 720 and face_count == 1200
         and degree == 12 and abs(edge_length - PHI_INV) < 1e-6)
print(f"\n  STEP 1: {'PASS ✓' if step1 else 'FAIL ✗'}\n")

# ============================================================
# STEP 2: Verify 9 eigenvalues with correct multiplicities
# ============================================================
print("STEP 2: Eigenvalue spectrum (9 distinct eigenvalues)")
print("-" * 50)

eigenvalues_raw = np.linalg.eigvalsh(A)
eigenvalues_raw = np.sort(eigenvalues_raw)[::-1]

# Expected eigenvalues and multiplicities
expected = [
    (12, 1), (6 * phi, 4), (4 * phi, 9), (3, 16), (0, 25),
    (-2, 36), (-4 / phi, 9), (-3, 16), (-6 / phi, 4)
]

print(f"  {'Expected λ':>12} {'Mult':>5} {'Found':>12} {'Found mult':>10} {'Match':>6}")
print(f"  {'─' * 12} {'─' * 5} {'─' * 12} {'─' * 10} {'─' * 6}")

all_match = True
for exp_val, exp_mult in expected:
    count = np.sum(np.abs(eigenvalues_raw - exp_val) < 0.01)
    match = (count == exp_mult)
    if not match:
        all_match = False
    # Find closest actual eigenvalue
    closest = eigenvalues_raw[np.argmin(np.abs(eigenvalues_raw - exp_val))]
    print(f"  {exp_val:12.4f} {exp_mult:5d} {closest:12.4f} {count:10d} "
          f"{'✓' if match else '✗'}")

print(f"\n  STEP 2: {'PASS ✓' if all_match else 'FAIL ✗'}\n")
step2 = all_match

# ============================================================
# STEP 3: Spectral traces Tr(A²) = 1440, Tr(A³) = 7200
# ============================================================
print("STEP 3: Spectral trace identities")
print("-" * 50)

A2 = A @ A
A3 = A2 @ A
trA2 = np.trace(A2)
trA3 = np.trace(A3)

print(f"  Tr(A²) = {trA2:.1f}  (expected: 1440 = 2E)  "
      f"{'PASS' if abs(trA2 - 1440) < 0.5 else 'FAIL'}")
print(f"  Tr(A³) = {trA3:.1f}  (expected: 7200 = 6F)  "
      f"{'PASS' if abs(trA3 - 7200) < 0.5 else 'FAIL'}")

step3 = abs(trA2 - 1440) < 0.5 and abs(trA3 - 7200) < 0.5
print(f"\n  STEP 3: {'PASS ✓' if step3 else 'FAIL ✗'}\n")

# ============================================================
# STEP 4: Bare Weinberg ratio 3/8
# ============================================================
print("STEP 4: Bare Weinberg ratio = 3/8")
print("-" * 50)

N_E = trA2        # = 1440
N_F = trA3 / 3    # = 2400
bare_ratio = N_E / (N_E + N_F)

print(f"  N_E = Tr(A²) = {N_E:.0f}")
print(f"  N_F = Tr(A³)/3 = {N_F:.0f}")
print(f"  N_E/(N_E + N_F) = {bare_ratio:.8f}")
print(f"  3/8 = {3 / 8:.8f}")
print(f"  Match: {'PASS' if abs(bare_ratio - 3 / 8) < 1e-10 else 'FAIL'}")

step4 = abs(bare_ratio - 3 / 8) < 1e-10
print(f"\n  STEP 4: {'PASS ✓' if step4 else 'FAIL ✗'}\n")

# ============================================================
# STEP 5: Corrected Weinberg angle 3/(8φ)
# ============================================================
print("STEP 5: Weinberg angle sin²θ_W = 3/(8φ)")
print("-" * 50)

eta = PHI_INV  # propagation efficiency
sin2_W = eta * N_E / (N_E + N_F)
sin2_W_formula = 3 / (8 * phi)
sin2_W_pdg = 0.23121

print(f"  η = l_edge/R_circ = 1/φ = {eta:.8f}")
print(f"  sin²θ_W = η × N_E/(N_E+N_F) = {sin2_W:.8f}")
print(f"  3/(8φ) = {sin2_W_formula:.8f}")
print(f"  PDG: {sin2_W_pdg}")
print(f"  Formula match: {'PASS' if abs(sin2_W - sin2_W_formula) < 1e-12 else 'FAIL'}")
print(f"  PDG agreement: {100 * abs(sin2_W - sin2_W_pdg) / sin2_W_pdg:.4f}%")

step5 = abs(sin2_W - sin2_W_formula) < 1e-12
print(f"\n  STEP 5: {'PASS ✓' if step5 else 'FAIL ✗'}\n")

# ============================================================
# STEP 6: Self-energy isotropy on K₃ faces
# ============================================================
print("STEP 6: Self-energy isotropy on K₃ faces")
print("-" * 50)

# Find a face
face = None
for i in range(N):
    for j in range(i + 1, N):
        if A[i, j] > 0.5:
            for k in range(j + 1, N):
                if A[j, k] > 0.5 and A[i, k] > 0.5:
                    face = (i, j, k)
                    break
            if face:
                break
    if face:
        break

face_idx = list(face)
rest_idx = [i for i in range(N) if i not in face_idx]

A_fr = A[np.ix_(face_idx, rest_idx)]
A_rr = A[np.ix_(rest_idx, rest_idx)]
A_rf = A[np.ix_(rest_idx, face_idx)]

# K₃ antibonding basis
ab1 = np.array([2, -1, -1]) / np.sqrt(6)
ab2 = np.array([0, 1, -1]) / np.sqrt(2)

# Evaluate self-energy at ω = 2 (bonding eigenvalue)
omega = 2.0
G_rr = np.linalg.inv(omega * np.eye(len(rest_idx)) - A_rr)
Sigma = A_fr @ G_rr @ A_rf

# Project onto antibonding subspace
Sigma_a1a2 = ab1 @ Sigma @ ab2
Sigma_a1a1 = ab1 @ Sigma @ ab1
Sigma_a2a2 = ab2 @ Sigma @ ab2

print(f"  Face: {face}")
print(f"  Σ(ω=2) antibonding off-diagonal: {Sigma_a1a2:.2e}")
print(f"  Σ(ω=2) antibonding diagonal 1:   {Sigma_a1a1:.8f}")
print(f"  Σ(ω=2) antibonding diagonal 2:   {Sigma_a2a2:.8f}")
print(f"  Isotropy (diag1 ≈ diag2): {abs(Sigma_a1a1 - Sigma_a2a2):.2e}")
print(f"  Off-diagonal < 1e-12: {'PASS' if abs(Sigma_a1a2) < 1e-12 else 'FAIL'}")

step6 = abs(Sigma_a1a2) < 1e-12 and abs(Sigma_a1a1 - Sigma_a2a2) < 1e-10
print(f"\n  STEP 6: {'PASS ✓' if step6 else 'FAIL ✗'}\n")

# ============================================================
# STEP 7: Bond counting — ε = 2sin²θ_W/(z+1)
# ============================================================
print("STEP 7: Bond counting — ε = 2sin²θ_W/(z+1)")
print("-" * 50)

z = 12
z_plus_1 = z + 1

# Verify bond structure at K₃ vertex
internal_bonds = sum(1 for v in face_idx[1:] if A[face_idx[0], v] > 0.5)
external_bonds = int(np.sum(A[face_idx[0], :])) - internal_bonds

epsilon = 2 * sin2_W / z_plus_1
epsilon_formula = 3 / (52 * phi)

print(f"  Internal bonds per K₃ vertex: {internal_bonds}  (expected: 2)  "
      f"{'PASS' if internal_bonds == 2 else 'FAIL'}")
print(f"  External bonds per K₃ vertex: {external_bonds}  (expected: 10)  "
      f"{'PASS' if external_bonds == 10 else 'FAIL'}")
print(f"  z+1 = {z_plus_1}  (closed neighbourhood)")
print(f"  ε = 2sin²θ_W/(z+1) = {epsilon:.10f}")
print(f"  3/(52φ) = {epsilon_formula:.10f}")
print(f"  Match: {'PASS' if abs(epsilon - epsilon_formula) < 1e-14 else 'FAIL'}")

step7 = (internal_bonds == 2 and external_bonds == 10
         and abs(epsilon - epsilon_formula) < 1e-14)
print(f"\n  STEP 7: {'PASS ✓' if step7 else 'FAIL ✗'}\n")

# ============================================================
# STEP 8: Koide phase cos(θ) = -(2+ε)/3
# ============================================================
print("STEP 8: Koide phase from isotropic shift")
print("-" * 50)

cos_theta_pred = -(2 + epsilon) / 3
cos_theta_formula = -(2 / 3) * (1 + sin2_W / z_plus_1)
cos_theta_formula2 = -(2 / 3) * (1 + 3 / (104 * phi))
theta_pred = np.degrees(np.arccos(cos_theta_pred))

# PDG Koide phase
sm = np.array([np.sqrt(M_E), np.sqrt(M_MU), np.sqrt(M_TAU)])
S = np.sum(sm)
A_koide = S / 3
cos_theta_pdg = (sm[0] / A_koide - 1) / np.sqrt(2)
theta_pdg = np.degrees(np.arccos(cos_theta_pdg))

print(f"  cos(θ) = -(2+ε)/3 = {cos_theta_pred:.10f}")
print(f"  cos(θ) = -(2/3)(1+sin²θ_W/(z+1)) = {cos_theta_formula:.10f}")
print(f"  cos(θ) = -(2/3)(1+3/(104φ)) = {cos_theta_formula2:.10f}")
print(f"  All three forms equal: "
      f"{'PASS' if abs(cos_theta_pred - cos_theta_formula) < 1e-14 and abs(cos_theta_pred - cos_theta_formula2) < 1e-14 else 'FAIL'}")
print(f"  θ_pred = {theta_pred:.6f}°")
print(f"  θ_PDG  = {theta_pdg:.6f}°")
print(f"  cos(θ) PDG = {cos_theta_pdg:.10f}")
print(f"  Agreement: {100 * abs(cos_theta_pred - cos_theta_pdg) / abs(cos_theta_pdg):.4f}%")

step8 = (abs(cos_theta_pred - cos_theta_formula) < 1e-14
         and abs(cos_theta_pred - cos_theta_formula2) < 1e-14
         and 100 * abs(cos_theta_pred - cos_theta_pdg) / abs(cos_theta_pdg) < 0.01)
print(f"\n  STEP 8: {'PASS ✓' if step8 else 'FAIL ✗'}\n")

# ============================================================
# STEP 9: Predicted lepton masses
# ============================================================
print("STEP 9: Predicted lepton masses")
print("-" * 50)

theta_rad = np.radians(theta_pred)
sm_pred = np.array([
    A_koide * (1 + np.sqrt(2) * np.cos(theta_rad + 2 * np.pi * i / 3))
    for i in range(3)
])
m_pred = sm_pred ** 2
scale = M_E / m_pred[0]
m_pred *= scale

K_check = np.sum(m_pred) / np.sum(np.sqrt(m_pred)) ** 2

pdg_masses = [M_E, M_MU, M_TAU]
names = ["electron", "muon", "tau"]

print(f"  {'Lepton':>10} {'Predicted':>12} {'PDG':>12} {'Agreement':>10}")
print(f"  {'─' * 10} {'─' * 12} {'─' * 12} {'─' * 10}")
for name, mp, ma in zip(names, m_pred, pdg_masses):
    pct = 100 * abs(mp - ma) / ma
    print(f"  {name:>10} {mp:12.6f} {ma:12.6f} {pct:9.4f}%")

print(f"\n  K = {K_check:.12f}  (exact 2/3 = {2 / 3:.12f})")
print(f"  Muon agreement < 0.2%: {'PASS' if 100 * abs(m_pred[1] - M_MU) / M_MU < 0.2 else 'FAIL'}")
print(f"  Tau agreement < 0.2%:  {'PASS' if 100 * abs(m_pred[2] - M_TAU) / M_TAU < 0.2 else 'FAIL'}")

step9 = (100 * abs(m_pred[1] - M_MU) / M_MU < 0.2
         and 100 * abs(m_pred[2] - M_TAU) / M_TAU < 0.2)
print(f"\n  STEP 9: {'PASS ✓' if step9 else 'FAIL ✗'}\n")

# ============================================================
# STEP 10: Mutual reinforcement
# ============================================================
print("STEP 10: Mutual reinforcement check")
print("-" * 50)

K = 2 / 3
sin2_from_koide = z_plus_1 * (cos_theta_pdg / (-K) - 1)

print(f"  sin²θ_W from Koide phase: {sin2_from_koide:.8f}")
print(f"  sin²θ_W from spectral traces: {sin2_W:.8f}")
print(f"  sin²θ_W from PDG: {sin2_W_pdg:.8f}")
print(f"  Koide vs spectral agreement: "
      f"{100 * abs(sin2_from_koide - sin2_W) / sin2_W:.4f}%")
print(f"  Agreement < 0.2%: "
      f"{'PASS' if 100 * abs(sin2_from_koide - sin2_W) / sin2_W < 0.2 else 'FAIL'}")

# Check that CONJ-EW-1 gives BETTER masses than PDG sin²θ_W
eps_conj = 2 * sin2_W / z_plus_1
eps_pdg_w = 2 * sin2_W_pdg / z_plus_1
cos_conj = -(2 + eps_conj) / 3
cos_pdg_w = -(2 + eps_pdg_w) / 3

theta_conj_rad = np.arccos(cos_conj)
theta_pdg_w_rad = np.arccos(cos_pdg_w)

sm_conj = np.array([A_koide * (1 + np.sqrt(2) * np.cos(theta_conj_rad + 2 * np.pi * i / 3)) for i in range(3)])
sm_pdg_w = np.array([A_koide * (1 + np.sqrt(2) * np.cos(theta_pdg_w_rad + 2 * np.pi * i / 3)) for i in range(3)])

m_conj = sm_conj ** 2 * (M_E / sm_conj[0] ** 2)
m_pdg_w = sm_pdg_w ** 2 * (M_E / sm_pdg_w[0] ** 2)

mu_err_conj = 100 * abs(m_conj[1] - M_MU) / M_MU
mu_err_pdg = 100 * abs(m_pdg_w[1] - M_MU) / M_MU

print(f"\n  Muon error with 3/(8φ): {mu_err_conj:.4f}%")
print(f"  Muon error with PDG sin²θ_W: {mu_err_pdg:.4f}%")
print(f"  CONJ-EW-1 gives better masses: "
      f"{'PASS' if mu_err_conj < mu_err_pdg else 'FAIL'}")

step10 = (100 * abs(sin2_from_koide - sin2_W) / sin2_W < 0.2
          and mu_err_conj < mu_err_pdg)
print(f"\n  STEP 10: {'PASS ✓' if step10 else 'FAIL ✗'}\n")

# ============================================================
# FINAL SUMMARY
# ============================================================
all_steps = [step1, step2, step3, step4, step5, step6, step7, step8, step9, step10]

print("=" * 70)
print("  FINAL SUMMARY")
print("=" * 70)
for i, (passed, label) in enumerate(zip(all_steps, [
    "600-cell construction",
    "9 eigenvalues with multiplicities",
    "Spectral traces Tr(A²)=1440, Tr(A³)=7200",
    "Bare Weinberg ratio 3/8",
    "Corrected Weinberg angle 3/(8φ)",
    "Self-energy isotropy on K₃",
    "Bond counting ε = 3/(52φ)",
    "Koide phase cos(θ) = -(2+ε)/3",
    "Predicted lepton masses",
    "Mutual reinforcement",
]), start=1):
    print(f"  Step {i:2d}: {'PASS ✓' if passed else 'FAIL ✗'}  {label}")

n_pass = sum(all_steps)
print(f"\n  {n_pass}/10 steps passed.")
if n_pass == 10:
    print("  ALL NUMERICAL CLAIMS IN SM-6 ARE VERIFIED.")
else:
    print(f"  WARNING: {10 - n_pass} step(s) failed — investigate.")

print("=" * 70)
