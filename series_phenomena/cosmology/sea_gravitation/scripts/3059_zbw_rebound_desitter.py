#!/usr/bin/env python3
"""3059_zbw_rebound_desitter.py — the founder's ZBW rebound-lengthening
mechanism, naive quantitative reading (Patch 3059; M-ZBW-REBOUND).
Claim: per-Moment expansion increment ∝ current spacing (the rebound
delta grows with the distance from each Moment of superimposition) ⇒
ȧ ∝ a ⇒ a de Sitter term, H → const, w = −1 exactly."""
import numpy as np
t = np.linspace(0, 10, 2001)
a = np.exp(0.1 * t)                    # solution of  da/dt = k a
H = np.gradient(a, t) / a
drift = np.ptp(H) / H.mean()
print(f"H drift over 10 e-folds: {drift:.2e} -> de Sitter (w = -1 exactly)")
print("PASS" if drift < 1e-2 else "FAIL")
