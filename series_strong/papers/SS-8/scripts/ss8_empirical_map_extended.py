#!/usr/bin/env python3
# ============================================================
# SS-8 Phase 1 Step 2: Extended empirical map
# Purpose: tabulate SS-7 residuals across the full
#          (N_alpha, N_excess) grid to characterize the
#          neutron-excess signature.
#
# Key move: walk Z at fixed alpha-core (Z = 2 N_alpha), add
# pairs of neutrons to get N_ex = 0, 2, 4, 6, 8. SS-7 formula
# is evaluated at the same N_alpha = Z/2 regardless of N_ex.
# The residual Delta(N_alpha, N_ex) = B_exp - B_SS7(N_alpha)
# is what SS-8 must derive.
#
# Author: Claude Opus, 21 April 2026 (SS-8 Phase 1, extension
#         of ss8_empirical_map.py driven by authentic AME 2020)
# ============================================================

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from ame2020_loader import load_ame2020, B  # noqa: E402

# --- SS-7 v1.2 formula (unchanged) ---
B_alpha  = 28.296   # MeV, ^4He binding (SS-5, via A8')
B_pair   = 2.342    # MeV, M_0/phi (SS-5, via A11)

def ss7_pred(N_alpha: int) -> float:
    return N_alpha * B_alpha + (3 * N_alpha - 6) * B_pair

# --- load AME 2020 once ---
AME = load_ame2020()

def Bx(Z: int, A: int):
    """Wrapper returning (B_MeV, estimated_flag) or (None, None) if missing."""
    entry = AME.get((Z, A))
    if entry is None:
        return None, None
    return entry["BE_total"], entry["estimated"]


# --- Grid: even-even isotopes at Z = 2 N_alpha, N_ex in {0, 2, 4, 6, 8} ---
Na_range = list(range(3, 15))       # 3..14
Nex_range = [0, 2, 4, 6, 8]

# Element labels at Z = 2*N_alpha
ELEM = {6: "C", 8: "O", 10: "Ne", 12: "Mg", 14: "Si", 16: "S",
        18: "Ar", 20: "Ca", 22: "Ti", 24: "Cr", 26: "Fe", 28: "Ni"}

print("=" * 96)
print("EXTENDED EMPIRICAL MAP:  Delta(N_alpha, N_ex) = B_exp - B_SS7(N_alpha)   [MeV]")
print("  rows: N_alpha   |   cols: N_ex = N - Z (extra neutrons on alpha-core)")
print("  '*' = extrapolated AME value (#-flagged); '-' = nuclide not in AME")
print("=" * 96)

header = f"{'N_a':>4} {'Z=2Na':>6} {'Elem':>4} "
for nex in Nex_range:
    header += f"{'N_ex='+str(nex):>10} "
header += "  notes"
print(header)
print("-" * 96)

# Store the Delta values for downstream characterization
grid_delta = {}       # (Na, Nex) -> Delta in MeV
grid_estimated = {}   # (Na, Nex) -> was AME value estimated

for Na in Na_range:
    Z = 2 * Na
    pred = ss7_pred(Na)
    row = f"{Na:>4} {Z:>6} {ELEM[Z]:>4} "
    for nex in Nex_range:
        A = 4 * Na + nex
        Bexp, est = Bx(Z, A)
        if Bexp is None:
            row += f"{'-':>10} "
            grid_delta[(Na, nex)] = None
            grid_estimated[(Na, nex)] = None
        else:
            delta = Bexp - pred
            grid_delta[(Na, nex)] = delta
            grid_estimated[(Na, nex)] = est
            mark = "*" if est else " "
            row += f"{delta:>+9.3f}{mark} "
    print(row)

print()

# -------- Characterize the pattern -------------------------------------------

print("=" * 96)
print("CHARACTERIZATION 1:  Is Delta linear in N_ex at fixed N_alpha?")
print("  For each N_alpha row, report Delta per extra neutron pair (Delta / (N_ex/2))")
print("  and Delta per extra neutron (Delta / N_ex).")
print("=" * 96)

print(f"{'N_a':>4}  {'N_ex':>5}  {'Delta (MeV)':>12}  {'Delta/N_ex':>12}  {'Delta/pair':>12}")
print("-" * 60)
for Na in Na_range:
    for nex in [2, 4, 6, 8]:
        d = grid_delta[(Na, nex)]
        if d is None: continue
        est = grid_estimated[(Na, nex)]
        mark = "*" if est else " "
        per_n = d / nex
        per_pair = d / (nex // 2)
        print(f"{Na:>4}  {nex:>5}  {d:>+11.3f}{mark} {per_n:>+11.3f}   {per_pair:>+11.3f}")
    print()  # blank between alpha-chain rows

# -------- Per-neutron contribution trend vs N_alpha at fixed N_ex ------------

print("=" * 96)
print("CHARACTERIZATION 2:  Per-neutron contribution Delta/N_ex vs N_alpha")
print("  Columns = N_ex values; rows = N_alpha. Reveals whether the extra-binding")
print("  per neutron depends on alpha-core size (decoration-mechanism diagnostic).")
print("=" * 96)

header = f"{'N_a':>4}  "
for nex in [2, 4, 6, 8]:
    header += f"{'N_ex='+str(nex):>13} "
print(header)
print("-" * 64)
for Na in Na_range:
    row = f"{Na:>4}  "
    for nex in [2, 4, 6, 8]:
        d = grid_delta[(Na, nex)]
        if d is None:
            row += f"{'-':>13} "
        else:
            est = grid_estimated[(Na, nex)]
            mark = "*" if est else " "
            row += f"{(d/nex):>+11.3f}{mark} "
    print(row)
print()

# -------- Isobar chains at N_ex=+2,+4 for mass-number diagnostic -------------

print("=" * 96)
print("CHARACTERIZATION 3:  Does Delta/N_ex saturate, drift, or oscillate as N_a grows?")
print("  Summary across N_ex = +2 and +4 (the best-measured columns).")
print("=" * 96)

for nex in [2, 4]:
    vals = [(Na, grid_delta[(Na, nex)], grid_estimated[(Na, nex)])
            for Na in Na_range if grid_delta[(Na, nex)] is not None]
    measured = [(Na, d/nex) for Na, d, est in vals if not est]
    if measured:
        mean = sum(v for _, v in measured) / len(measured)
        # sample std
        var = sum((v - mean) ** 2 for _, v in measured) / max(1, len(measured) - 1)
        std = var ** 0.5
        lo = min(v for _, v in measured); hi = max(v for _, v in measured)
        print(f"N_ex = {nex}:  N measured = {len(measured)}  "
              f"mean Delta/N_ex = {mean:+.3f} MeV   std = {std:.3f}   "
              f"range = [{lo:+.3f}, {hi:+.3f}]")
print()

# -------- Stress test: 48Ca -------------------------------------------------

print("=" * 96)
print("STRESS TEST: 48Ca (N_alpha = 10, N_ex = +8, doubly magic)")
print("=" * 96)
B48Ca, est = Bx(20, 48)
pred10 = ss7_pred(10)
delta48 = B48Ca - pred10
print(f"  B_exp (48Ca)       = {B48Ca:.3f} MeV   (AME 2020, {'estimated' if est else 'measured'})")
print(f"  SS-7 pred(N_a=10)  = {pred10:.3f} MeV")
print(f"  Delta              = {delta48:+.3f} MeV over 8 extra neutrons")
print(f"  Per extra neutron  = {delta48/8:+.3f} MeV")
print(f"  Per extra pair     = {delta48/4:+.3f} MeV")

# -------- ODD-A SCAN (discriminator for valence-pair vs interstitial) ---------
print()
print("=" * 96)
print("ODD-A SCAN: Z = 2 N_alpha even, N_ex = 1 (single extra neutron on alpha-core)")
print("  Discriminator: pure valence-pair predicts Delta(N_ex=1) ~ 0 (no partner).")
print("  Interstitial predicts Delta(N_ex=1) ~ k * B_pair (single-neutron coordination).")
print("  Interstitial-with-pairing predicts Delta(N_ex=1) ~ Delta(N_ex=2)/2 - pairing_bonus.")
print("=" * 96)

print(f"{'N_a':>4} {'Z':>4} {'Nucl':>6} {'B_exp (MeV)':>13} {'Delta (MeV)':>13}  "
      f"{'Delta(N_ex=2)/2':>17}  {'pairing gap':>13}")
print("-" * 84)
odd_A_rows = []
for Na in Na_range:
    Z = 2 * Na
    A_odd = 4 * Na + 1
    Bexp, est = Bx(Z, A_odd)
    if Bexp is None:
        continue
    pred = ss7_pred(Na)
    delta_odd = Bexp - pred
    delta_even = grid_delta[(Na, 2)]
    if delta_even is None:
        continue
    half_even = delta_even / 2.0
    pairing = half_even - delta_odd   # if positive: odd N_ex has LESS binding per neutron
    mark = "*" if est else " "
    elem = ELEM[Z]
    label = f"{A_odd}{elem}"
    print(f"{Na:>4} {Z:>4} {label:>6} {Bexp:>13.3f} {delta_odd:>+12.3f}{mark} "
          f"{half_even:>+17.3f}  {pairing:>+12.3f}")
    odd_A_rows.append((Na, delta_odd, half_even, pairing, est))

if odd_A_rows:
    measured = [(Na, do, he, p) for Na, do, he, p, est in odd_A_rows if not est]
    if measured:
        avg_pairing = sum(p for _, _, _, p in measured) / len(measured)
        print()
        print(f"  Average pairing gap (Delta_even/2 - Delta_odd) = {avg_pairing:+.3f} MeV")
        print(f"  Interpretation: if positive, odd-A loses ~this much binding by missing")
        print(f"  the opposite-polarity pairing bonus (consistent with ~B_pair/2 to ~B_pair).")

# -------- CALCIUM ISOTOPE CHAIN FULL SCAN -----------------------------------
print()
print("=" * 96)
print("CALCIUM ISOTOPE CHAIN: Z=20, full scan N = 20..28 (N_ex = 0..8)")
print("  Reveals odd-even staggering and smoothness of Delta(N_ex) at fixed N_alpha=10.")
print("=" * 96)

print(f"{'Nucl':>6} {'N':>3} {'N_ex':>5} {'B_exp (MeV)':>13} {'Delta (MeV)':>13} "
      f"{'Delta/N_ex':>12} {'Delta-Delta_prev':>16}")
print("-" * 84)
pred_Ca = ss7_pred(10)
prev_delta = 0.0
ca_data = []
for N in range(20, 29):
    A = 20 + N
    Bexp, est = Bx(20, A)
    if Bexp is None:
        continue
    delta = Bexp - pred_Ca
    nex = N - 20
    mark = "*" if est else " "
    label = f"{A}Ca"
    increment = delta - prev_delta
    per_n = delta / nex if nex > 0 else 0.0
    print(f"{label:>6} {N:>3} {nex:>5} {Bexp:>13.3f} {delta:>+12.3f}{mark} "
          f"{per_n:>+11.3f}  {increment:>+16.3f}")
    ca_data.append((nex, delta, est))
    prev_delta = delta

# Odd-even staggering in the increments: second-difference diagnostic
print()
if len(ca_data) >= 3:
    print("  Odd-even staggering in Ca chain (second differences of Delta vs N_ex):")
    print(f"  {'triplet':>20} {'D2 Delta':>12}")
    for i in range(1, len(ca_data) - 1):
        nex_mid = ca_data[i][0]
        D2 = ca_data[i - 1][1] - 2 * ca_data[i][1] + ca_data[i + 1][1]
        tag = "odd-center" if nex_mid % 2 == 1 else "even-center"
        print(f"  N_ex = {ca_data[i-1][0]}, {nex_mid}, {ca_data[i+1][0]}  "
              f"({tag:>11}):  {D2:>+9.3f}")

# -------- PARTIAL-ALPHA CHECK: 6Li alpha-deuteron binding -------------------
print()
print("=" * 96)
print("PARTIAL-ALPHA: 6Li as alpha + deuteron (briefing's K3-incomplete hypothesis)")
print("=" * 96)

B_6Li, _ = Bx(3, 6)     # Z=3, A=6
B_4He, _ = Bx(2, 4)
B_2H,  _ = Bx(1, 2)     # deuteron
alpha_d_binding = B_6Li - B_4He - B_2H

print(f"  B(6Li)                      = {B_6Li:.3f} MeV")
print(f"  B(4He) + B(2H)              = {B_4He + B_2H:.3f} MeV")
print(f"  alpha-d binding             = {alpha_d_binding:.3f} MeV")
print(f"  Briefing's (2/3) * B_pair   = {2.0*B_pair/3.0:.3f} MeV")
print(f"  Ratio (observed/prediction) = {alpha_d_binding / (2.0*B_pair/3.0):.3f}")
print(f"  Hypothesis: deuteron engages 2 of 3 edges of an alpha K3 face;")
print(f"  predicted binding = (2/3) * B_pair. Compare to full K3 contact = B_pair.")
