"""
1863 -- OPEN-SS-43 campaign opening: R_s(N) candidate-route scalings, the capture term's
velocity power (resolving the 1/v^2-vs-1/v^4 pin from the v1.1 panel), and the
(E_c, R_s) over-determination map.

Grounded in the 1858 pipeline (V(r) = (E_c*r_c/r) exp(-r/R_s); capture boundary
V(b_max) = KE_COM; sigma = pi*b_max^2 / m_rod), re-read in full before this was written.

Provenance (CONV-003): m_el = 1408 MeV [0886]; sigma_el/m_el = 0.11 cm^2/g geometric
convention [0859/0886]; E_ee = 0.9 MeV [1813]; (E_c ~ 0.3 MeV, R_s ~ 15-30 fm) TARGETS
from the 1858 scan; N <~ 18-21 floor ceiling [1860]; chi = phi^-3/6 ~ 0.0394 [Capotauro].
"""
import math

C = 299792.458
MeV_g = 1.783e-27
RC = 1.0                      # 1858's contact radius (fm)
M_EL = 1408.0
CHI = ((1 + 5**0.5) / 2) ** -3 / 6      # Capotauro phi^-3/6

def bmax(v, Ec, Rs, N):
    """1858 capture boundary: solve (Ec*RC/b) exp(-b/Rs) = 0.5*mu*v^2, stdlib bisection."""
    mu = N * M_EL / 2
    KE = 0.5 * mu * (v / C) ** 2
    V = lambda r: (Ec * RC / r) * math.exp(-r / Rs)
    if V(RC) < KE:
        return RC
    lo, hi = RC, 3000.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if V(mid) > KE: lo = mid
        else: hi = mid
    return 0.5 * (lo + hi)

def som(v, Ec, Rs, N):
    b = bmax(v, Ec, Rs, N)
    return math.pi * b * b * 1e-26 / (N * M_EL * MeV_g)

if __name__ == "__main__":
    print("=" * 76)
    print(" 1863 -- OPEN-SS-43 opening: routes, velocity power, over-determination")
    print("=" * 76)

    # (A) element-scale anchors ------------------------------------------------
    sig_el_fm2 = 0.11 * M_EL * MeV_g * 1e26
    r_int = math.sqrt(sig_el_fm2 / math.pi)
    d_sq  = math.sqrt(sig_el_fm2)
    d_bond = 2 * 197.327 / 264.0
    print(f"\n(A) ELEMENT-SCALE ANCHORS: sigma_el = {sig_el_fm2:.1f} fm^2 [0.11 conv.]")
    print(f"    interaction radius r_int = {r_int:.2f} fm; square face d_sq = {d_sq:.2f} fm;")
    print(f"    structural bond scale d_bond ~ 2*(hbar c/264 MeV) = {d_bond:.2f} fm")
    print("    (the 0.11 anchor is polarizability-enhanced -> interaction, not hard size;")
    print("     both anchors carried, per the honesty flag in the derivation file)")

    # (B) velocity power of the 1858 model (resolves the panel pin) ------------
    print("\n(B) EFFECTIVE VELOCITY POWER p(v) = d ln(sigma/m) / d ln v  [1858 model, N=15]")
    anchors = [30, 50, 100, 200, 500, 1000, 1500, 2500, 3500]
    for Rs in (15.0, 20.0, 30.0):
        row = []
        for i in range(len(anchors) - 1):
            v1, v2 = anchors[i], anchors[i + 1]
            s1, s2 = som(v1, 0.30, Rs, 15), som(v2, 0.30, Rs, 15)
            p = math.log(s2 / s1) / math.log(v2 / v1)
            row.append(f"{p:5.2f}")
        print(f"    Rs={Rs:>4.0f}: v-bins {anchors}:  p = [{', '.join(row)}]")
    print("    => the power is NOT a single exponent: ~ -4 (Rutherford/Coulomb window,")
    print("       Copilot's gloss) where b_max << R_s; flattening toward ~ -1..-2 effective")
    print("       in the screening tail (corpus 1/v^2 gloss is the dwarf<->cluster average).")
    print("       The falsifier shape is the full b_max(v) curve, not one power.")

    # (C) candidate R_s(N) routes ----------------------------------------------
    print("\n(C) ROUTE TABLES: which N lands R_s in the 15-30 fm target?  (ceiling: N <~ 20)")
    print("    Route A (Sea saturation, R_s = (8N)^(1/3) * r0):")
    for r0, lab in [(1.0, "r0=1.0 fm (color)"), (r_int, f"r0={r_int:.2f} fm (interaction)")]:
        Ns = [N for N in range(1, 41) if 15 <= (8 * N) ** (1 / 3) * r0 <= 30]
        print(f"      {lab:>28}: N in window = {Ns if Ns else 'NONE <= 40'}"
              + ("  [above ceiling]" if Ns and min(Ns) > 21 else ""))
    print("    Route B (channel-suppressed Debye, N-flat):")
    print(f"      R_s = 1 fm / sqrt(chi) = {1/math.sqrt(CHI):.1f} fm  [below window]")
    print(f"      R_s = 1 fm / chi       = {1/CHI:.1f} fm  [IN window; N-independent]")
    print("    Route C (source coherence, R_s = N * d_el):")
    for d, lab in [(d_bond, "structural"), (r_int, "r_int"), (d_sq, "face")]:
        Ns = [N for N in range(1, 41) if 15 <= N * d <= 30]
        print(f"      d_el={d:4.2f} fm ({lab:>10}): N in window = {Ns}")

    # (D) over-determination map + N-trend structure ---------------------------
    print("\n(D) OVER-DETERMINATION: dwarf(v=50) sigma/m across (E_c, R_s), N=15 [1858 model]")
    print("        R_s:      10      15      20      25      30   fm")
    for Ec in (0.1, 0.2, 0.3, 0.5):
        vals = "  ".join(f"{som(50, Ec, Rs, 15):6.2f}" for Rs in (10, 15, 20, 25, 30))
        print(f"    E_c={Ec:.1f}:  {vals}")
    print("    => dwarf magnitude ~ R_s^2-sensitive, ~log E_c-sensitive: R_s is THE lever.")
    print("       Kill-criterion: ONE mechanism must land BOTH (R_s, E_c) in the ~1-2 band.")
    print("\n    N-trend under the two E_c scalings (R_s per Route C, d_el=r_int, v=50):")
    print("      N   R_s(C)   sigma/m [E_c flat=0.3]   sigma/m [E_c = N*0.02, charge-additive]")
    for N in (3, 5, 8, 12, 20):
        Rs = N * r_int
        print(f"     {N:>2}  {Rs:5.1f}fm        {som(50,0.30,Rs,N):6.2f}"
              f"                  {som(50,0.02*N,Rs,N):6.2f}")
    print("    => the coring magnitude's N-dependence is route- and E_c-scaling-dependent:")
    print("       a measurable discriminator once the mechanism is chosen.")

    print("\n" + "=" * 76)
    print(" STATUS: routes formalized, powers resolved as regime-local, map drawn.")
    print(" The mechanism SELECTION (A/B/C or other) is the founder decision point.")
    print("=" * 76)
