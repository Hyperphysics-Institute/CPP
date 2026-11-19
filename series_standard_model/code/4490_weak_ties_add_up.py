#!/usr/bin/env python3
"""Patch 4490 illustration script (the checks are identities and arithmetic, not a test of physics): does a tie too weak to matter alone stay irrelevant when many such ties act together?

The founder's answer to 4489 §7.2: a tie so weak it produces no change when measured "cannot affect its entangled photon;
that's all that happens," and the photon still interferes with itself. This script checks two standard facts behind it:

  D1-D3  Englert's duality (PRL 77, 2154, 1996; already used in 4445): a photon whose path is tied to a partner record with
         overlap g between the two record states shows single-photon fringe visibility V = |g|, and V^2 + D^2 = 1 for a pure
         record with distinguishability D = sqrt(1 - g^2). Strong tie (g = 0): no fringes on its own. Weak tie (g near 1):
         fringes essentially full. So "it still interferes with itself" holds for weak ties and fails for strong ones.
  C1-C3  Compounding: N independent weak ties, each with overlap g = 1 - delta, give V = g^N ~ exp(-N*delta). Each tie alone
         changes V by delta (below any threshold you like); N of them can remove the fringes. A rule that drops every
         sub-threshold tie one by one predicts V = 1 regardless of N; the full ledger predicts g^N.

The model takes the ties as independent (product environment states), so overlaps multiply; correlated environments can do
better or worse than g^N. Physical anchors in the corpus reading: Englert's relation (4445); multiple-photon decoherence
(Kokorowski et al., PRL 86, 2191, 2001); QM-4's Lindblad theorem.

Pure Python. Exit 0 if every check holds.
"""
import math

rows = []

# D1-D3: single tie, visibility vs distinguishability
for label, g in (("D1 strong tie (records orthogonal)", 0.0),
                 ("D2 middling tie", 0.6),
                 ("D3 weak tie", 1 - 1e-6)):
    V = abs(g)
    D = math.sqrt(1 - g * g)
    ok = abs(V * V + D * D - 1) < 1e-12
    rows.append((label, f"g={g:.6f}", f"V={V:.6f}  D={D:.6f}", ok))

# C1-C3: N weak ties, each delta = 1e-6 (each alone shifts V by one part in a million)
delta = 1e-6
for label, N in (("C1 one weak tie", 1), ("C2 a million weak ties", 10**6), ("C3 ten million weak ties", 10**7)):
    V_full = (1 - delta) ** N
    V_cut = 1.0  # per-tie cut: every tie is below threshold, so all are dropped
    approx = math.exp(-N * delta)
    ok = abs(V_full - approx) < 1e-3 * max(approx, 1e-12) + 1e-9
    rows.append((label, f"N={N:,}  delta={delta:g}", f"full ledger V={V_full:.6f}   per-tie cut V={V_cut:.1f}", ok))

compounding_shown = (1 - delta) ** 10**7 < 1e-3
rows.append(("C4 per-tie cut and full ledger part ways", "N=10^7", f"difference = {1.0 - (1 - delta) ** 10**7:.6f}", compounding_shown))

print("WEAK-TIES TABLE (Patch 4490)")
for label, scope, value, ok in rows:
    print(f"{label:42s} {scope:26s} {value:48s} {'PASS' if ok else 'FAIL'}")
n = sum(r[3] for r in rows)
print(f"{n}/{len(rows)} PASS")
raise SystemExit(0 if n == len(rows) else 1)
