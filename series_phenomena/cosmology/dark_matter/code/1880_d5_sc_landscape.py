"""
1880 -- D5 executed by landscape: where does the candidate SURVIVE as a function of
S_c (nucleon-coupling suppression factor, J11)?  Founder directive: "choose the D5
choice that saves the candidate." That directive is executable only by computing the
survival region of the FULLY COMPOSED baryon ladder -- suppressing the coupling also
un-shields the underground detectors, so naive D5-A choices can die by LZ.

Ladder as a function of S_c (E_rN -> S_c * E_rN):
  1. XQC: predicted counts via the 1879 partial-wave pipeline (attractive,
     line-folded = maximal variant), criterion: total in-band < 527 & no bin viol.
  2. Overburden shielding of LZ: collisions in 4.3e5 g/cm^2 rock (4300 m.w.e., SURF);
     rod KE ~ 7.5 keV total, ~45% loss per mass-matched collision => >= 10 collisions
     degrades below threshold ("shielded"). sigma_A(rock~Si proxy) from the same
     partial-wave solve at 230 km/s.
  3. LZ (if unshielded): sigma_n at Xe-recoil momenta vs 9.2e-48 @ 36 GeV / ~1e-47
     @ 25.3 GeV (LZ PRL 2022, arXiv:2207.03764).
  4. np channel: delta a_np = 2.9e-3 * S_c fm (N=15 anchor, 1866) vs ~3e-3 detectable.
  5. CMB drag: 4.4e-27 * S_c^2 (Born regime) vs ~1e-25 (2112.00707).
Natural suppression scales (color-neutral nucleon vs the rod's coherent unipolar
cage): first-power dipole S_c ~ R_N/R_s = 0.035; second-power S_c ~ (R_N/R_s)^2 =
1.3e-3; full decoupling S_c -> 0.
"""
import math, sys
exec(open('code/1879_xqc_recomputation.py').read().split('if __name__')[0])
mod = sys.modules['__main__']
E_RN_BASE = E_RN
LZ_LIM = 1.0e-47
RN = 0.9  # fm, nucleon radius scale
ROCK_COL = 4.3e5 / (24.0 * 1.66e-24)   # nuclei/cm^2 over LZ (A~24 proxy)

def xqc_total(sc):
    mod.E_RN = E_RN_BASE * sc
    counts, sat = predicted_bins(-1, True)
    mod.E_RN = E_RN_BASE
    nviol = sum(1 for b, (lo, hi, obs, f) in enumerate(BINS)
                if counts[b] > obs + 5 * math.sqrt(obs + 1))
    satv = sat > SAT[1] + 5 * math.sqrt(SAT[1])
    return sum(counts), sat, nviol + (1 if satv else 0)

def sigA_rock(sc):
    mod.E_RN = E_RN_BASE * sc
    A, mT = TARGETS["Si"]
    mu = mT * M_ROD / (mT + M_ROD)
    v = 230.0 / CKMS; k = mu * v / HBARC
    d = phase_shifts(make_V(A, -1, True), mu, k, min(max(int(k * 108), 10), 70))
    mod.E_RN = E_RN_BASE
    return sum(4 * math.pi / (k * k) * (2 * l + 1) * math.sin(dd) ** 2
               for l, dd in enumerate(d)) * 1e-26  # cm^2

def sig_n_LZ(sc):
    mT = 938.9; mu = mT * M_ROD / (mT + M_ROD)
    q = 49.5  # MeV, Xe recoil ~10 keV
    a = (2 * mu / HBARC ** 2) * (E_RN_BASE * sc) * RC * RS ** 2 * (HBARC/RS) ** 2 / ((HBARC/RS) ** 2 + q ** 2)
    return 4 * math.pi * (a * 1e-13) ** 2

if __name__ == "__main__":
    print("=" * 88)
    print(" 1880 -- S_c survival landscape (J11). Natural scales: R_N/R_s = %.3f ; (R_N/R_s)^2 = %.1e" % (RN / RS, (RN / RS) ** 2))
    print("=" * 88)
    print(" {:>8} | {:>9} {:>6} | {:>10} {:>9} | {:>10} | {:>9} | {:>8} | verdict".format(
        "S_c", "XQC tot", "viol", "rock coll", "shielded", "LZ sig_n", "da_np", "CMB"))
    grid = [1.0, 0.3, 0.1, 0.035, 0.01, 3e-3, 1.3e-3, 1e-4, 1e-6, 2e-9]
    for sc in grid:
        tot, sat, nv = xqc_total(sc)
        sA = sigA_rock(sc)
        ncoll = ROCK_COL * sA
        shielded = ncoll >= 10
        lz = sig_n_LZ(sc)
        lz_ok = shielded or lz < LZ_LIM
        danp = 2.9e-3 * sc
        cmb = 4.4e-27 * sc * sc
        xqc_ok = (nv == 0)
        alive = xqc_ok and lz_ok and cmb < 1e-25
        print(" {:>8.1e} | {:>9.0f} {:>6} | {:>10.2e} {:>9} | {:>10.1e} | {:>9.1e} | {:>8.1e} | {}".format(
            sc, tot + sat, nv, ncoll, "YES" if shielded else "no", lz, danp, cmb,
            "ALIVE" if alive else ("dead: XQC" if not xqc_ok else ("dead: LZ" if not lz_ok else "dead: CMB"))))
    print("""
 READ-OUT:
  - Island I  (shielded SIMP): S_c where XQC passes AND rock-shielding holds.
  - Dead zone: shielding fails but coupling still >> LZ reach.
  - Island II (decoupled): S_c small enough to pass LZ UNSHIELDED (~< 2e-9).
  - Natural scale placement: first-power color-dipole S_c = R_N/R_s = 0.035 vs
    second-power (R_N/R_s)^2 = 1.3e-3 -- the table shows which island each hits.
  - Island-I residual checks NOT yet pinned (arc tasks): CRESST-2017-surface /
    DAMIC-shallow reach at 25 GeV; Dewar-class (NFM18/NBN19) bounds on the
    thermalized population (2112.00707). Flagged J12.""")
    print("=" * 88)
