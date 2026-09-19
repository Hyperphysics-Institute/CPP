#!/usr/bin/env python3
"""
Patch 4136 — TODO-4134-SPINORIENT. Does the A_i channel itself induce the
spin-orientation correlation that R-F3-ISO forbids?

THE QUESTION
------------
4134 derived B_tot = n.W (n the spin axis, W = sum_i s_i V_i a polar vector in
the cage frame) and found F3 holds because an L = 0 ground state's internal
frame is isotropically distributed relative to n, so <n.W> = 0.  R-F3-ISO names
the requirement: no frame-spin correlation above ~1e-7.  4135 then showed
R-F3-ISO carries BOTH sectors.  So if the amendment's own A_i channel generates
that correlation, it is not a correction to F3 -- it is F3's failure mode, and
it takes the weak sector's mechanism down with it.

WHAT A CORRELATION REQUIRES
---------------------------
<n.W> != 0 is POLAR order: the distribution over cage orientations must
distinguish +n from -n.  That needs an energy term ODD under n -> -n, i.e. of
the form (axial) . (polar).  Two candidates from the A3G-2 broadcast table:

   A . r-hat   monopole-dipole   P = -1, T = -1   -> chi_4 CANNOT source (F6+B3)
   A . V       = b itself        P = -1, T = +1   -> chi_4 CAN source

and one that is NOT odd under n -> -n:

   (A . V)^2   quadratic in b    P = +1, T = +1   -> the TODO-4124 loophole

Checks:
  E1  a LINEAR term g*(n.W-hat) does induce polar order; size it, and invert
      the ~1e-7 hadronic PV bound to a bound on g
  E2  a QUADRATIC term c*(n.W-hat)^2 induces ALIGNMENT but NOT polar order --
      <n.W> stays exactly 0.  So TODO-4124-QUADRATIC does NOT open this one.
  E3  T-parity census of the routes, and which are actually closed
"""
import numpy as np

np.set_printoptions(precision=6, suppress=True)
out = []
def say(s=""):
    print(s); out.append(s)

rng = np.random.default_rng(4136)
N = 2_000_000
# isotropic cage orientations; by symmetry only the angle to n matters
u = rng.uniform(-1, 1, N)                 # cos(theta) between n and W-hat

say(f"    Monte Carlo noise floor at N = {N:,} samples: "
    f"{1 / (3 ** 0.5 * N ** 0.5):.1e} -- values below it are noise, so the")
say("    small-coupling rows are given ANALYTICALLY (Langevin) and cross-checked.")
say()
say("E1  LINEAR coupling  E = -g * (n . W-hat):  does it make polar order?")
say("    g         <cos theta> exact    Monte Carlo")
for g in (1e-1, 1e-3, 1e-5, 1e-7, 1e-9):
    exact = (1 / np.tanh(g) - 1 / g) if g > 1e-6 else g / 3  # Langevin L(g)
    w = np.exp(g * u)                     # Boltzmann weight, g in units of kT
    eps = (u * w).sum() / w.sum()
    say(f"    {g:.0e}    {exact:+.6e}        {eps:+.3e}")
say("    epsilon = L(g) -> g/3 for small g: a linear axial.polar term makes")
say("    polar order in exact proportion to its strength. NOT protected.")
say()
W_MAG = 1.1654                            # |W| for the SU(6) proton, Patch 4134
PV_BOUND = 1e-7
say(f"    B_tot = epsilon * |W| = epsilon * {W_MAG:.4f}, and the hadronic PV bound")
say(f"    is ~{PV_BOUND:.0e}, so epsilon <= {PV_BOUND / W_MAG:.2e} and therefore")
say(f"    g <= {3 * PV_BOUND / W_MAG:.2e} in units of the confining energy scale.")
say("    A linear A.(polar) coupling of ordinary strength is EXCLUDED by 7 orders.")
say()

say("E2  QUADRATIC coupling  E = -c * (n . W-hat)^2:  the TODO-4124 loophole")
say("    c         <cos theta> MC      <cos^2 theta>   (1/3 = isotropic)")
for c in (10.0, 1.0, 1e-2, 1e-4):
    w = np.exp(c * u ** 2)
    eps = (u * w).sum() / w.sum()
    ali = (u ** 2 * w).sum() / w.sum()
    say(f"    {c:.0e}    {eps:+.3e}        {ali:.6f}")
say("    <cos theta> is EXACTLY zero for every c, analytically: exp(c u^2) is")
say("    even in u, so the odd moment integrates to zero. The MC column shows")
say("    only the sampling floor above.")
say("    The quadratic term DOES produce alignment -- <cos^2> departs from 1/3,")
say("    strongly at c = 10 -- but <cos theta> stays ZERO to sampling precision")
say("    at every strength, because exp(c u^2) is EVEN in u. Nematic order, not")
say("    polar order. A pseudoscalar needs polar order.")
say()
say("    => TODO-4124-QUADRATIC's loophole, which DOES reopen A3G-2 and A3G-3,")
say("       does NOT reopen R-F3-ISO. This protection is strictly better than")
say("       theirs in exactly the respect the 4125 caveat names.")
say()

say("E3  route census -- what is actually closed, and what is F3 restated")
rows = [
    ("A . r-hat  (monopole-dipole)", "-1", "-1", "CLOSED by F6 (b is T-even) + B3 (linear)"),
    ("A . v      (spin-velocity)",   "-1", "-1", "CLOSED, same fact"),
    ("(A . V)^2  (quadratic in b)",  "+1", "+1", "CLOSED here by E2 -- even in n, no polar order"),
    ("A . V      (= b itself)",      "-1", "+1", "NOT CLOSED -- see below"),
]
say(f"    {'route':<30} {'P':>3} {'T':>3}  status")
for r, p, t, st in rows:
    say(f"    {r:<30} {p:>3} {t:>3}  {st}")
say()
say("    The A.V route is NOT closed and CANNOT be closed by T-parity: b is")
say("    T-EVEN by F6, which is exactly why it is available as a carrier. An")
say("    A.V term in the nucleon's internal energy is a P-odd term in the strong")
say("    Hamiltonian -- which IS hadronic parity violation, the thing bounded at")
say("    ~1e-7. Excluding it by assumption would be circular. So for this route")
say("    R-F3-ISO is not an independent protection; it is F3 restated.")
say()
say("VERDICT")
say("  SPINORIENT SPLITS. Three of the four routes by which the A_i channel")
say("  could generate the forbidden correlation are closed: two by the F6+B3")
say("  T-parity fact, and the quadratic one by E2, independently of F6 and B3.")
say("  The fourth -- an A.V term in the internal energy -- is not closed and is")
say("  not closeable this way; it is the same question F3 asks, so F3 is")
say("  self-consistent here rather than newly threatened.")
say()
say("  THE COST, and it is the honest headline: the two closed T-parity routes")
say("  close by the SAME F6+B3 premise that already carries A3G-2 and A3G-3.")
say("  The premise concentration the 4125 caveat flagged and the 4128 audit")
say("  narrowed now carries a THIRD result. If F6 fails, A3G-2, A3G-3 and two")
say("  of R-F3-ISO's four routes reopen together.")

open("/tmp/4136_out.txt", "w").write("\n".join(out))
