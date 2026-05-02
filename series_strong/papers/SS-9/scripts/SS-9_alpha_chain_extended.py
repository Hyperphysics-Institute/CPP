#!/usr/bin/env python3
"""
SS-9 alpha-chain extended residual analysis (Session 4 follow-up arc, 2 May 2026).

Reproducibly compute the SS-7 LO formula vs empirical binding-energy comparison
for the strict-N=Z alpha-chain at N_alpha = 3 through 20, plus the deltahedron-
core / satellite-regime two-regime fit. Companion to:

  series_strong/papers/SS-9/sketches/SS-9_alpha_chain_extended_residuals.md

Outputs:
  - Residual table (LO formula vs empirical) for N_alpha in [3, 20]
  - Linear fits to |E|_actual vs N_alpha for two ranges:
      [3, 14]: simplicial deltahedron regime (slope-3 expected)
      [14, 20]: satellite regime (slope-1 observed)
  - Calibrated two-regime formula residuals
  - PRED-O-19 forward-looking predictions for N_alpha in [21, 25]

Constants from SS-5 v6 / SS-7 v1.3:
  B_alpha = 28.296 MeV   (experimental 4He binding, AME inherited)
  B_pair  = 2.342 MeV    (M_0 / phi, SS-5-derived via C3)

Empirical binding energies are from the Table of Isotopes (Firestone & Shirley,
1998; PNPI compilation), which agrees with AME 2020 to ~50 keV across the
strict-N=Z chain at the precision relevant to SS-7's per-row 0.1-1% target.
For final paper deliverables, values should be re-verified against AME 2020.

Run:
  python3 SS-9_alpha_chain_extended.py
"""

import numpy as np

# ---------------------------------------------------------------------------
# CPP constants (from SS-5 v6 / SS-7 v1.3, no fitted parameters)
# ---------------------------------------------------------------------------
B_ALPHA = 28.296   # MeV — experimental 4He binding (AME inherited)
B_PAIR  = 2.342    # MeV — M_0 / phi (SS-5 derived via C3)

# Calibrated parameter (Regime II only, calibrated from 56Ni residual)
B_SLIP  = 4.0      # MeV — persistent slip-plane bonus on the deltahedron core


# ---------------------------------------------------------------------------
# Empirical data: strict-N=Z alpha-chain binding energies (TOI 98, MeV)
# ---------------------------------------------------------------------------
ALPHA_CHAIN = [
    # (N_alpha, isotope, B_exp_MeV)
    ( 3, '12C',   92.1631),
    ( 4, '16O',  127.6211),
    ( 5, '20Ne', 160.6452),
    ( 6, '24Mg', 198.2592),
    ( 7, '28Si', 236.5392),
    ( 8, '32S',  271.7842),
    ( 9, '36Ar', 306.7192),
    (10, '40Ca', 342.0563),
    (11, '44Ti', 375.4793),
    (12, '48Cr', 411.4703),
    (13, '52Fe', 447.7044),
    (14, '56Ni', 483.9954),
    # Session 4 follow-up extension begins here:
    (15, '60Zn', 515.0004),
    (16, '64Ge', 545.9664),
    (17, '68Se', 576.3375),
    (18, '72Kr', 606.9185),
    (19, '76Sr', 638.0995),
    (20, '80Zr', 668.3805),
]

# Forward-looking PRED-O-19 test bed (binding values to be filled from AME 2020)
PRED_O_19_NUCLEI = [
    (21, '84Mo'),
    (22, '88Ru'),
    (23, '92Pd'),
    (24, '96Cd'),
    (25, '100Sn'),
]


# ---------------------------------------------------------------------------
# Formulas
# ---------------------------------------------------------------------------
def B_LO(N):
    """SS-7 leading-order formula: simplicial deltahedron, |E| = 3N - 6."""
    return N * B_ALPHA + (3 * N - 6) * B_PAIR

def B_satellite(N, B_slip=B_SLIP):
    """Regime II formula: deltahedron-core (N=14) + satellite alphas, plus
    persistent slip-plane bonus B_slip on the core. Valid for N >= 14."""
    return N * B_ALPHA + (N + 22) * B_PAIR + B_slip

def E_actual(N, B_exp):
    """Effective contact-graph edge count, inverted from binding."""
    return (B_exp - N * B_ALPHA) / B_PAIR


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------
def analyse_LO_residuals():
    """Compare empirical binding to SS-7 LO across the alpha-chain."""
    print("=" * 88)
    print("SS-7 LO formula vs empirical binding (alpha-chain N_alpha = 3-20)")
    print("=" * 88)
    print(f"{'N_a':>3} {'Nuc':>5} {'B_exp':>9} {'B_LO':>9} {'Resid_MeV':>10} "
          f"{'Resid_Bp':>9} {'|E|_act':>8} {'|E|_LO':>7} {'Δ|E|':>6}")
    print("-" * 88)
    prev_E = None
    for N, nuc, B in ALPHA_CHAIN:
        b_lo = B_LO(N)
        resid = B - b_lo
        e_act = E_actual(N, B)
        e_lo = 3 * N - 6
        delta = (e_act - prev_E) if prev_E is not None else float('nan')
        marker = ""
        if N == 14: marker = "  <-- end of simplicial regime"
        if N == 15: marker = "  <-- regime transition"
        delta_str = f"{delta:+.2f}" if not np.isnan(delta) else "  --"
        print(f"{N:>3} {nuc:>5} {B:>9.3f} {b_lo:>9.3f} {resid:>+10.3f} "
              f"{resid/B_PAIR:>+9.3f} {e_act:>8.2f} {e_lo:>7d} {delta_str}{marker}")
        prev_E = e_act
    print()


def fit_two_regimes():
    """Linear fits to |E|_actual vs N_alpha in the two regimes."""
    print("=" * 88)
    print("Linear fits |E|_actual vs N_alpha (regime diagnosis)")
    print("=" * 88)
    for label, N_range in [
        ('Regime I (simplicial deltahedron)', range(3, 15)),
        ('Regime II (deltahedron core + satellites)', range(14, 21)),
    ]:
        N_arr = np.array([d[0] for d in ALPHA_CHAIN if d[0] in N_range])
        E_arr = np.array([E_actual(d[0], d[2]) for d in ALPHA_CHAIN if d[0] in N_range])
        slope, intercept = np.polyfit(N_arr, E_arr, 1)
        N_lo, N_hi = min(N_arr), max(N_arr)
        print(f"  {label}: N_alpha in [{N_lo}, {N_hi}]")
        print(f"    slope     = {slope:6.3f}")
        print(f"    intercept = {intercept:+7.3f}")
        print(f"    formula   |E|(N) = {slope:.2f} * N + ({intercept:+.2f})")
        print()


def analyse_satellite_regime():
    """Test the calibrated two-regime formula B_satellite (Regime II)."""
    print("=" * 88)
    print(f"Regime II formula: B = N*B_alpha + (N+22)*B_pair + B_slip "
          f"(B_slip = {B_SLIP} MeV calibrated from 56Ni)")
    print("=" * 88)
    print(f"{'N_a':>3} {'Nuc':>5} {'B_pred':>10} {'B_exp':>10} "
          f"{'Residual':>10} {'Resid_Bp':>9}")
    print("-" * 88)
    rms_sum = 0.0
    count = 0
    for N, nuc, B in ALPHA_CHAIN:
        if N < 14:  # Regime II only
            continue
        b_pred = B_satellite(N)
        resid = B - b_pred
        rms_sum += resid ** 2
        count += 1
        print(f"{N:>3} {nuc:>5} {b_pred:>10.3f} {B:>10.3f} "
              f"{resid:>+10.3f} {resid/B_PAIR:>+9.3f}")
    rms = np.sqrt(rms_sum / count)
    print("-" * 88)
    print(f"  RMS residual: {rms:.3f} MeV across {count} nuclei (N_alpha = 14-20)")
    print(f"  Relative accuracy: {rms / np.mean([d[2] for d in ALPHA_CHAIN if d[0] >= 14]) * 100:.3f}%")
    print()


def predict_O19():
    """PRED-O-19 forward-looking predictions for N_alpha in [21, 25]."""
    print("=" * 88)
    print("PRED-O-19 forward-looking predictions (deltahedron-core + satellite extension)")
    print("=" * 88)
    print(f"{'N_a':>3} {'Nuc':>5} {'B_pred (MeV)':>13} {'note':>40}")
    print("-" * 88)
    for N, nuc in PRED_O_19_NUCLEI:
        b_pred = B_satellite(N)
        note = ""
        if N == 25: note = "<-- 100Sn doubly-magic (Z=N=50); shell effects?"
        print(f"{N:>3} {nuc:>5} {b_pred:>13.2f}    {note}")
    print()
    print("Falsification routes:")
    print("  - Residuals systematically > 1 MeV at N_alpha in [21, 25]")
    print("    -> falsifies satellite-regime extension, identifies N_alpha^(2)crit")
    print("  - 100Sn-specific deviation -> shell-closure correction needed")
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print()
    print(f"SS-9 alpha-chain extended residual analysis")
    print(f"B_alpha = {B_ALPHA} MeV, B_pair = {B_PAIR} MeV, B_slip = {B_SLIP} MeV")
    print(f"Companion sketch: series_strong/papers/SS-9/sketches/SS-9_alpha_chain_extended_residuals.md")
    print()
    analyse_LO_residuals()
    fit_two_regimes()
    analyse_satellite_regime()
    predict_O19()
