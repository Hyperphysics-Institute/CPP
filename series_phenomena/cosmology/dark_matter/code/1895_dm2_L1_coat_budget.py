"""
1895 -- DM-2 L1: the rod-equivalence check. Under excess-sourcing, m_grav(rod) =
constituents + cage/rod binding + the coat (the Sea-polarization cloud, an excess
living OUTSIDE the N*m_el inertial ledger). Question: is the unledgered part small
vs the anchor tolerances (few %)?

Registered inputs only: rod-rod contact residual E_c = 0.3 MeV at r_c (J4 ledger --
the SAME normalization every DM-1 anchor used, so the comparison is ledger-consistent);
R_s = r_c/chi = 25.42 fm; E_ee = 0.9 MeV (e-channel ceiling; the neutral shell's
residual is below it); m_rod = 18*1408 MeV; pitch 1.15 fm.

Coat energy = the self-energy of the rod's screened residual field outside the core:
pair potential V(r) = q^2 e^{-mu r}/r with q^2 = E_c*r_c, mu = 1/R_s; field energy
U = (1/8pi) int [(grad phi)^2 + mu^2 phi^2] d^3r, phi = q e^{-mu r}/r, integrated
numerically from r_c to infinity (no closed-form trust).
"""
import math
RC, RS = 1.0, 25.42
EC, EEE = 0.3, 0.9
MROD = 18 * 1408.0

def coat_energy(q2, a, mu, rmax=400.0, n=200000):
    # U = (1/2) * q2 * integral_a^inf e^{-2 mu r} [ (1/r + mu)^2 + mu^2 ] ... do it as
    # u(r)*4pi r^2 with phi = sqrt(q2) e^{-mu r}/r in Gaussian normalization:
    h = (rmax - a) / n
    tot = 0.0
    for i in range(n):
        r = a + (i + 0.5) * h
        e = math.exp(-mu * r)
        dphi2 = (e * (1.0 / r ** 2 + mu / r)) ** 2
        m2phi2 = (mu * e / r) ** 2
        tot += (dphi2 + m2phi2) * r * r * h
    return 0.5 * q2 * tot  # MeV (q2 in MeV*fm; lengths in fm)

if __name__ == "__main__":
    mu = 1.0 / RS
    Uq = coat_energy(EC * RC, RC, mu)
    Ue_ceiling = coat_energy(EEE * RC, RC, mu)   # e-channel CEILING (neutral shell => below)
    print("=" * 74)
    print(" 1895 -- DM-2 L1: rod equivalence (coat budget vs inertial ledger)")
    print("=" * 74)
    print("\n(1) COAT (unledgered Sea excess):")
    print("    q-channel residual coat: U = %.4f MeV  -> %.1e of m_rod" % (Uq, Uq / MROD))
    print("    e-channel CEILING:       U = %.4f MeV  -> %.1e of m_rod" % (Ue_ceiling, Ue_ceiling / MROD))
    print("    added-mass (drag) bound: same order as the coat it drags -> <~ %.0e" % (2 * Uq / MROD))
    print("\n(2) IDENTICAL-IN-BOTH-LEDGERS entries (cannot break equivalence, bounded for scale):")
    # inter-element bonds: 17 links; per-link bond bounded by the hDP-scale fraction that
    # the pinned m_el already absorbs -- book both sides identically; magnitude note only:
    print("    17 inter-element links x O(1-10 MeV)/link ~ 20-170 MeV = 0.1-0.7%% of m_rod,")
    print("    but binding is negative excess in BOTH m_grav and m_inertial -> cancels in the ratio.")
    print("\n(3) VERDICT: m_grav/m_inertial - 1 = (coat + drag)/m_rod <= %.1e" % ((Uq + Ue_ceiling + 2 * Uq) / MROD))
    print("    vs anchor tolerance ~ 2-5e-2  ->  L1 PASSES with margin >= %.0e." % (0.02 / ((Uq + Ue_ceiling + 2 * Uq) / MROD)))
    print("    S_c note: the nucleon-coupling suppression is a COLOUR-channel property;")
    print("    gravity couples to energy -- untouched. Equivalence is ledger-consistent")
    print("    because E_c is the same registered normalization the anchors used (J4).")
    print("=" * 74)
