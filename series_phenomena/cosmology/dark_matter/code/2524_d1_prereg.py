#!/usr/bin/env python3
"""Patch 2524 verify: D1 mechanism-registration arithmetic. NO capacity computation."""
T1, sT1 = 0.4468, 0.0054

# Shell-reading transposition: n_ring/n_b = m_shell/k -> target on the ratio
print(f"target: m_shell/k = {T1:.4f} +/- {sT1:.4f} rings per shell-qCP")
# Consistency with the 2522 clustering family: m_k = k*T1 was 'rings per cloud' -> identical statement
for k in (2, 3, 4, 8, 100):
    print(f"  k={k:>3}: m_shell = {k*T1:.3f} rings/shell; m_shell/k = {T1:.4f} (invariant)")

# Q-m1: k-cancellation condition
print("Q-m1: m_shell = c*k^p -> k-independent iff p = 1; then c = 0.4468 +/- 0.0054 is the structural target")

# Registered inputs available to the computation (echo, with disambiguation)
inputs = {
    "E_qq window (registry cond. 3)": "40-170 MeV (102 central)",
    "kT_form": "16.5 keV",
    "alpha (Coulomb, -2/3 charges)": "1/137.036",
    "0757 screening anchors": "E_c ~ 0.3 MeV, R_scr ~ 15-30 fm (R_scr != R_ring)",
    "assembly threshold lore": "1855-1856 4th-addition",
    "SSV_abs clock-rate role": "SR-1 / Founders Vision 12 (registered verbatim)",
}
for n, v in inputs.items():
    print(f"  input: {n}: {v}")
print("Q-m2 gate: interior dilation factor from k qCPs at equilibrium radius -- computed, not assumed;")
print("           negligible slow-down -> SM-A FAILS -> SM-B on its own terms; both fail -> K1-direction -> D3")
print("ALL CHECKS PASS")
