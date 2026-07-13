"""
OPEN-DM-FLOQUET-1  method (a): reduced Floquet-Mathieu SIGN analysis of the
transverse charge-switched bending mode on geometry #3.   Patch 2440 (Opus).

Reproduces every number quoted in floquet_method_a_sign_result.md and reasoning/2440.md.

Model (leading, sign-level; magnitude deferred to R1/R2/R5/R6):
    x'' + w2(tau) x = 0        (dimensionless, tau = w_sw * t)
x  = lowest TRANSVERSE bending coordinate of the eCP coat.
Instantaneous transverse stiffness is charge-switched (square wave / Meissner limit):
    same-charge (repulsive) phase : +A   (restoring, +curvature)   fraction delta
    opposite-charge (attractive)  : -A   (Earnshaw anti-restoring)  fraction 1-delta
Meissner limit => monodromy is closed-form => the Floquet SIGN is rigorous,
not perturbative.

Dimensionless coefficient magnitude per phase:  eps = A/(m w_sw^2) = (w_A/w_sw)^2,
w_A = sqrt(A/m).  eps small  = fast switching (naive ponderomotive/Kapitza regime).
Static (adiabatic) average coefficient:  eps*(2*delta - 1)  ->  NEGATIVE for delta<1/2.
delta = 3/7 (uniform-sampling UPPER bound, Patch 2435) is < 1/2  ->  statically inverted.

GUARDRAILS exercised here: G1 (delta->0,1 limits), G2 (transverse mode; axial is a
separate statically-bound mode, not stabilized by this mechanism), G5 (3/7 is the
upper bound; dynamical delta governs and is swept), G7 (sign reported straight:
UNSTABLE / conditional / narrow -- not re-parametrized into survival).
"""
import numpy as np

TWO_PI = 2 * np.pi


def T_osc(alpha, t):
    """x'' + alpha x = 0, alpha>0 (oscillatory), transfer matrix over time t."""
    w = np.sqrt(alpha)
    c, s = np.cos(w * t), np.sin(w * t)
    return np.array([[c, s / w], [-w * s, c]])


def T_hyp(alpha, t):
    """x'' - alpha x = 0, alpha>0 (hyperbolic / anti-restoring), transfer matrix."""
    w = np.sqrt(alpha)
    c, s = np.cosh(w * t), np.sinh(w * t)
    return np.array([[c, s / w], [w * s, c]])


def monodromy(eps, delta, eps_att=None):
    """One switching period. Phase 1 repulsive (+eps, oscillatory) duration 2pi*delta;
    phase 2 attractive (-eps_att, hyperbolic) duration 2pi*(1-delta). eps_att defaults
    to eps (equal Coulomb magnitude)."""
    ea = eps if eps_att is None else eps_att
    t1, t2 = TWO_PI * delta, TWO_PI * (1 - delta)
    M1 = T_osc(eps, t1) if eps > 0 else np.array([[1.0, t1], [0.0, 1.0]])
    M2 = T_hyp(ea, t2) if ea > 0 else np.array([[1.0, t2], [0.0, 1.0]])
    return M2 @ M1


def floquet(eps, delta, eps_att=None):
    """Return (stable?, k_eff_coeff). k_eff_coeff = (w_eff/w_sw)^2, directly comparable
    to the static average eps*(2delta-1). Stable iff |tr M| < 2 (multipliers on unit
    circle)."""
    M = monodromy(eps, delta, eps_att)
    tr = np.trace(M)
    if abs(tr) < 2.0:
        mu = np.arccos(tr / 2.0)           # Floquet phase per period in (0,pi)
        return True, (mu / TWO_PI) ** 2
    return False, np.nan


def stable_bands(delta, eps_att_ratio=1.0, eps_max=1.2, n=12000):
    grid = np.linspace(1e-3, eps_max, n)
    stab = np.array([floquet(e, delta, None if eps_att_ratio == 1.0
                              else e * eps_att_ratio)[0] for e in grid])
    bands, s = [], None
    for i in range(len(grid)):
        if stab[i] and s is None:
            s = grid[i]
        if (not stab[i]) and s is not None:
            bands.append((s, grid[i - 1]))
            s = None
    if s is not None:
        bands.append((s, grid[-1]))
    return grid, stab, bands


def main():
    d = 3.0 / 7.0
    print("=" * 72)
    print("G1 -- limit checks (no modulation must give the static sign)")
    print("=" * 72)
    for delta in [0.0, 1e-4, 1.0, 1.0 - 1e-4]:
        st, ke = floquet(0.2, delta)
        print(f"  delta={delta:8.4f}: stable={st!s:5} static={0.2*(2*delta-1):+.4f} "
              f"k_eff={ke if st else float('nan'):+.5f}")
    print("  expect: delta->0 UNSTABLE (Earnshaw); delta->1 stable, k_eff->+eps=0.2")

    print("\n" + "=" * 72)
    print("Small-eps (fast switching) at delta=3/7: NAIVE Kapitza expectation FAILS")
    print("=" * 72)
    for eps in [1e-3, 1e-2, 1e-1]:
        half = np.trace(monodromy(eps, d)) / 2.0
        print(f"  eps={eps:.0e}: tr/2={half:+.6f}  "
              f"{'UNSTABLE (|tr/2|>1)' if abs(half) > 1 else 'stable'}   "
              f"static={eps*(2*d-1):+.5f}")
    print("  reason: negative static avg is O(eps); ponderomotive gain is O(eps^2);")
    print("  at small eps the O(eps) negative term dominates -> no stabilization.")

    print("\n" + "=" * 72)
    print("Stable eps-window at delta=3/7 (symmetric magnitude) + recovered stiffness")
    print("=" * 72)
    grid, stab, bands = stable_bands(d)
    print(f"  stable eps band(s): {[(round(a,4), round(b,4)) for a, b in bands]}")
    best = (-1.0, None, None)
    for e in grid[stab]:
        _, ke = floquet(e, d)
        phys = ke / e                       # k_eff / A  = fraction of bare stiffness
        if phys > best[0]:
            best = (phys, e, ke)
    _, ke_mid = floquet(0.3, d)
    print(f"  mid-band eps=0.30: k_eff/A = {ke_mid/0.3:.4f}  (coeff {ke_mid:.5f})")
    print(f"  peak k_eff/A = {best[0]:.4f} at eps={best[1]:.4f} (top edge, marginal)")
    print(f"  must beat |static avg|/A = |2delta-1| = {abs(2*d-1):.4f}")

    print("\n" + "=" * 72)
    print("R6 lever -- branch asymmetry eps_att/eps_rep at eps_rep=0.3, delta=3/7")
    print("=" * 72)
    for r in [0.5, 0.8, 1.0, 1.2, 1.5, 2.0]:
        st, ke = floquet(0.3, d, eps_att=0.3 * r)
        print(f"  eps_att/eps_rep={r:.1f}: stable={st!s:5} "
              f"k_eff_coeff={ke if st else float('nan'):+.5f}")
    print("  attractive weaker (ratio<1) -> stronger stabilization; stronger -> unstable")

    print("\n" + "=" * 72)
    print("R2 lever -- dynamical duty cycle at fixed eps=0.3")
    print("=" * 72)
    for dd in [0.40, 3/7, 0.45, 0.48, 0.50, 0.55, 0.60]:
        st, ke = floquet(0.3, dd)
        print(f"  delta={dd:.4f}: stable={st!s:5} k_eff_coeff={ke if st else float('nan'):+.5f}"
              f"  static={0.3*(2*dd-1):+.5f}")

    print("\nSIGN VERDICT (method a): NOT-YET-FALSIFIED, survival NOT demonstrated.")
    print("K_switch sign is CONDITIONAL and NARROW: positive only for")
    print("eps in ~[0.18,0.43] (w_sw/w_A ~ 1.5-2.4) at delta=3/7, modest magnitude")
    print("(~0.12*A mid-band). Fast-switching limit is UNSTABLE. Netting against the")
    print("geometry-#3 ponderomotive tensor (R5/G4) is pending and can flip the sign.")


if __name__ == "__main__":
    main()
