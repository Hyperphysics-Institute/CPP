"""
SS-9 OPEN-SS-35 sub-question (b) B-alpha layer 3:
Magic-number production verification via Goeppert-Mayer / Jensen shell-model
calculation with CPP-derived inputs.

CPP-derived inputs (no free parameters):
  hbar*omega from sub-question (a) Sessions 6, 7 (Level-1 partial closure)
  V_SO = (v_F/c)^2 * hbar*omega from layer 1 Session 8 (Level-1 partial closure)

Standard imports:
  HO + L.S Hamiltonian (textbook quantum mechanics)
  L.S operator structure from standard angular-momentum coupling

Result: All 7 empirical magic numbers {2, 8, 20, 28, 50, 82, 126} appear as
cumulative shell-closure positions in the CPP-derived spectrum. Gap magnitudes
at HO-boundary positions (2, 8, 20) match empirical to 20%; gap magnitudes at
spin-orbit-driven positions (28, 50, 82, 126) are 23-60% of empirical (soft).

This is the first qualitative cross-paradigm consilience claim of the
OPEN-SS-35 closure programme — partial.

Companion sketch:
  series_strong/papers/SS-9/sketches/SS-9_OPEN-SS-35_subquestion_b_Balpha_layer3.md
"""

import math


# ---------------------------------------------------------------------------
# Constants and CPP-derived inputs
# ---------------------------------------------------------------------------
hbar_omega = 13.0   # MeV at A~56, extrapolation from sub-question (a) Sessions 6,7
v_F_over_c = 0.30   # CPP layer 1 Session 8 (consistent with all three approaches)
V_SO = v_F_over_c**2 * hbar_omega   # 1.17 MeV

# Empirical magic numbers
EMPIRICAL_MAGIC = {2, 8, 20, 28, 50, 82, 126}

# Empirical gap approximations (rough values from Bohr-Mottelson / textbook)
EMPIRICAL_GAPS = {2: 12.0, 8: 10.0, 20: 8.0, 28: 5.0, 50: 4.0, 82: 3.0, 126: 2.0}


# ---------------------------------------------------------------------------
# Shell-model spectrum
# ---------------------------------------------------------------------------
def shell_levels(N_max, hw, vso):
    """Return all (E, label, n, l, j, deg, N) tuples up to HO shell N_max,
    sorted by single-particle energy."""
    spd = 'spdfghijkl'
    levels = []
    for N in range(N_max + 1):
        for l in range(N % 2, N + 1, 2):
            n = (N - l) // 2 + 1
            E_HO = (N + 1.5) * hw
            # j = l + 1/2
            E_jp = E_HO - vso * l/2
            j_p = l + 0.5
            deg_p = int(2*j_p + 1)
            label_p = f"{n}{spd[l]}{int(2*j_p)}/2"
            levels.append((E_jp, label_p, n, l, j_p, deg_p, N))
            # j = l - 1/2 (only for l > 0)
            if l > 0:
                E_jm = E_HO + vso * (l+1)/2
                j_m = l - 0.5
                deg_m = int(2*j_m + 1)
                label_m = f"{n}{spd[l]}{int(2*j_m)}/2"
                levels.append((E_jm, label_m, n, l, j_m, deg_m, N))
    levels.sort(key=lambda x: x[0])
    return levels


def annotate_levels(levels):
    """Add cumulative count and gap-above to each level. Returns list of dicts."""
    out = []
    cum = 0
    for i, (E, label, n, l, j, deg, N) in enumerate(levels):
        cum += deg
        gap = levels[i+1][0] - E if i+1 < len(levels) else 0
        out.append({
            'rank': i+1,
            'label': label,
            'E': E,
            'deg': deg,
            'cum': cum,
            'gap_above': gap,
            'is_empirical_magic': cum in EMPIRICAL_MAGIC,
            'l': l,
            'j': j,
            'N': N,
        })
    return out


# ---------------------------------------------------------------------------
# Magic-number rank analysis
# ---------------------------------------------------------------------------
def magic_number_ranks(annotated):
    """Sort levels by gap_above (descending), find rank of each empirical
    magic number's gap. Returns dict mapping magic_number -> (rank, gap, label)."""
    sorted_by_gap = sorted(annotated, key=lambda x: -x['gap_above'])
    ranks = {}
    for rank, lvl in enumerate(sorted_by_gap, 1):
        if lvl['cum'] in EMPIRICAL_MAGIC:
            ranks[lvl['cum']] = (rank, lvl['gap_above'], lvl['label'])
    return ranks


# ---------------------------------------------------------------------------
# Sensitivity scan
# ---------------------------------------------------------------------------
def sensitivity_scan(hw=hbar_omega, ratios=None):
    """Scan V_SO/hbar*omega and report magic-number ranks at each value."""
    if ratios is None:
        ratios = [0.0, 0.05, 0.09, 0.12, 0.15, 0.20, 0.25, 0.40]
    print(f"Sensitivity: V_SO/hbar*omega scan (hbar*omega = {hw} MeV)")
    print(f"  {'V_SO/hw':>9} {'V_SO':>6} {'magic ranks (gap MeV)':>50}")
    for ratio in ratios:
        vso = ratio * hw
        levels = shell_levels(7, hw, vso)
        annotated = annotate_levels(levels)
        ranks = magic_number_ranks(annotated)
        rstr = ', '.join(
            f"{m}@#{ranks[m][0]}({ranks[m][1]:.2f})" if m in ranks else f"{m}@---"
            for m in sorted(EMPIRICAL_MAGIC))
        print(f"  {ratio:>9.2f} {vso:>6.2f}  {rstr}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 80)
    print("OPEN-SS-35 sub-question (b) B-alpha layer 3:")
    print("Magic-number production verification with CPP-derived inputs")
    print("=" * 80)
    print()
    print("CPP-derived inputs:")
    print(f"  hbar*omega = {hbar_omega} MeV (sub-question (a) Sessions 6,7)")
    print(f"  v_F/c = {v_F_over_c} (layer 1 Session 8)")
    print(f"  V_SO = (v_F/c)^2 * hbar*omega = {V_SO:.3f} MeV")
    print(f"  V_SO/hbar*omega = {V_SO/hbar_omega:.3f}")
    print()
    print("Standard imports: HO + L.S Hamiltonian, standard QM angular-momentum")
    print("coupling, Mayer-Jensen single-particle scheme.")
    print()

    # Single-particle spectrum
    levels = shell_levels(7, hbar_omega, V_SO)
    annotated = annotate_levels(levels)

    print("=" * 80)
    print(f"Single-particle spectrum (truncated to N <= 6):")
    print("=" * 80)
    print(f"  {'#':>3} {'label':>9} {'E (MeV)':>10} {'2j+1':>5} {'cum':>5} "
          f"{'gap up':>8} {'magic?':>8}")
    print("  " + "-"*55)
    for lvl in annotated:
        if lvl['rank'] > 25:
            break
        magic = "** YES **" if lvl['is_empirical_magic'] else ""
        print(f"  {lvl['rank']:>3d} {lvl['label']:>9} {lvl['E']:>10.3f} "
              f"{lvl['deg']:>5d} {lvl['cum']:>5d} {lvl['gap_above']:>8.3f} "
              f"{magic:>8}")
    print()

    # Magic-number gap comparison
    print("=" * 80)
    print(f"Comparison to empirical magic-number gaps")
    print("=" * 80)
    ranks = magic_number_ranks(annotated)
    print(f"  {'magic':>6} {'CPP gap':>9} {'emp gap':>9} {'ratio':>8} "
          f"{'level <-':>10}")
    print("  " + "-"*45)
    for m in sorted(EMPIRICAL_MAGIC):
        if m in ranks:
            rank, gap, label = ranks[m]
            emp = EMPIRICAL_GAPS[m]
            ratio = gap / emp
            print(f"  {m:>6d} {gap:>9.3f} {emp:>9.1f} {ratio:>8.3f} {label:>10}")

    print()
    print("=" * 80)
    print("Sensitivity analysis: how V_SO/hbar*omega affects magic-number ranks")
    print("=" * 80)
    sensitivity_scan()

    print()
    print("=" * 80)
    print("Verdict")
    print("=" * 80)
    print("ALL 7 empirical magic numbers {2, 8, 20, 28, 50, 82, 126} appear")
    print("as cumulative shell-closure positions in the CPP-derived spectrum.")
    print()
    print("HO-boundary magic gaps (2, 8, 20) match empirical to within 20%.")
    print("Spin-orbit-driven magic gaps (28, 50, 82, 126) are 23-60% of empirical")
    print("at CPP V_SO/hbar*omega = 0.09 (soft end of magic-number-producing range).")
    print()
    print("To restore empirical gap hierarchy where magic 50 dominates magic 40,")
    print("V_SO/hbar*omega needs to be ~0.20-0.25, about 2-3x CPP layer-1 value.")
    print()
    print("Result: B-alpha layer 3 partial closure. Shell SEQUENCE reproduced;")
    print("gap MAGNITUDES at soft end of empirical. First qualitative cross-")
    print("paradigm consilience claim of OPEN-SS-35 closure programme.")
    print("=" * 80)


if __name__ == "__main__":
    main()
