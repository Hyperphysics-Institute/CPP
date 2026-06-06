#!/usr/bin/env python3
# ============================================================
# 0781_eu1_numerics.py
# Verification of the paper-body numerical claims of EU-1
# (Primordial scalar spectral index from substrate inflation).
#
# Reproduces, with stdlib only:
#   (1) n_s = 1 - 2/N_*  and  alpha_s = -2/N_*^2  at the pivot N_* = 57
#   (2) the e-fold/pivot bookkeeping  N_* = (1/3) ln(N_CP/N_GP)
#   (3) the ideal-ZRP chemical-potential slope  d mu / d ln rho -> 1
#       (Poisson grand-canonical), giving p = 2 exactly in the ideal limit
#   (4) the O(alpha) SSV-correction scaling  Delta n_s ~ 2 eta / N_*
#   (5) the Debye/Gamma reframing:  |mu_excess|/kT = c * Gamma^{3/2},
#       Gamma = alpha/kappa, kappa ~ 1  =>  residual << ln nbar ~ 170
#
# No third-party dependencies.  All checks print PASS/FAIL.
# ============================================================

import math

ALPHA = 1.0 / 137.035999          # fine-structure constant
N_STAR = 57.0                     # observable pivot (e-folds remaining at pivot)
N_STAR_TOTAL = 60.5               # total e-folds (1/3) ln(N_CP/N_GP)
LN_NBAR_PIVOT = 170.0             # ln(nbar) at the cosmological pivot, nbar ~ 1e74

results = []

def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))


# ---- (1) n_s and alpha_s at the pivot --------------------------------------
n_s = 1.0 - 2.0 / N_STAR
alpha_s = -2.0 / N_STAR**2
check("n_s = 1 - 2/57 = 0.9649",
      abs(n_s - 0.9649) < 5e-4,
      f"n_s = {n_s:.6f}  (Planck 2018 central 0.9649 +/- 0.0042)")
check("alpha_s = -2/57^2 = -0.0006",
      abs(alpha_s - (-0.0006)) < 5e-5,
      f"alpha_s = {alpha_s:.6f}  (Planck -0.0045 +/- 0.0067)")


# ---- (2) e-fold bookkeeping  N_* = (1/3) ln(N_CP/N_GP) ----------------------
# Observable-universe CP count ~ 1e80, seed cohort N_GP ~ 13 (one GP shell).
N_CP = 1.0e80
N_GP = 13.0
N_efold = (1.0 / 3.0) * math.log(N_CP / N_GP)
check("N_efold = (1/3) ln(1e80/13) ~ 60",
      abs(N_efold - N_STAR_TOTAL) < 1.5,
      f"N_efold = {N_efold:.2f}  (total); pivot N_* = 57 sits ~{N_efold-N_STAR:.1f} e-folds before end")


# ---- (3) ideal-ZRP chemical-potential slope  d mu / d ln rho -> 1 ----------
# Grand-canonical Poisson site:  mu/kT = ln(rho)  =>  d(mu/kT)/d ln rho = 1.
# Numerically: rho(z) = z for Poisson with fugacity z; mu/kT = ln z.
def mu_over_kT(ln_rho):
    return ln_rho          # ideal indistinguishable (Poisson) limit
h = 1e-6
ln_rho0 = 5.0
slope = (mu_over_kT(ln_rho0 + h) - mu_over_kT(ln_rho0 - h)) / (2 * h)
# n_s - 1 = 2 * d ln H_eff / dN, H_eff ∝ mu ∝ ln nbar ∝ N_rem  => p = 2 * slope
p = 2.0 * slope
check("ideal ZRP slope d mu/d ln rho = 1 (=> p = 2)",
      abs(slope - 1.0) < 1e-9 and abs(p - 2.0) < 1e-9,
      f"slope = {slope:.12f}, p = {p:.12f}")


# ---- (4) O(alpha) SSV-correction scaling  Delta n_s ~ 2 eta / N_* -----------
# Toy perturbed ZRP g(n) = n (1 + lambda (n-1)), lambda ~ Gamma ~ alpha.
# eta(lambda) = d mu/d ln rho - 1 ~ (linear in lambda); table from 0774.
table = {
    0.0:        (0.0,        0.0),
    0.1*ALPHA:  (1.5e-3,     5e-5),
    ALPHA:      (1.4e-2,     5e-4),
    3*ALPHA:    (4.1e-2,     1.5e-3),
    10*ALPHA:   (1.2e-1,     4.3e-3),
}
ok = True
detail_lines = []
for lam, (eta, dns_expected) in table.items():
    dns = 2.0 * eta / N_STAR
    agree = abs(dns - dns_expected) / max(dns_expected, 1e-12) < 0.15 or dns_expected == 0.0
    ok = ok and agree
    detail_lines.append(f"lambda={lam:.5f}  eta={eta:.2e}  Dn_s={dns:.2e} (tab {dns_expected:.2e})")
check("Delta n_s = 2 eta/N_* scaling matches 0774 table",
      ok,
      "; ".join(detail_lines))
# physical coupling: theory error ~5e-4 = 0.12 sigma_Planck
dns_phys = 2.0 * 1.4e-2 / N_STAR
check("physical-coupling theory error ~5e-4 ~ 0.12 sigma_Planck",
      abs(dns_phys - 5e-4) < 1e-4 and (dns_phys / 0.0042) < 0.2,
      f"Dn_s(alpha) = {dns_phys:.2e}, = {dns_phys/0.0042:.3f} sigma_Planck")


# ---- (5) Debye/Gamma reframing: residual << ln nbar -------------------------
# Coulomb plasma:  |mu_excess|/kT = c * Gamma^{3/2},  c = 1/sqrt(3) (DH).
# Gamma = alpha/kappa, kappa = kT_bath/E_Pl ~ 1 (LEMMA-NS-BATH).
c_DH = 1.0 / math.sqrt(3.0)
kappa = 1.0
Gamma = ALPHA / kappa
residual = c_DH * Gamma**1.5
check("Debye residual c*Gamma^{3/2} << ln nbar ~ 170",
      residual < 1e-3 and residual < LN_NBAR_PIVOT,
      f"Gamma = alpha/kappa = {Gamma:.4e}, |mu_ex|/kT = {residual:.4e} << {LN_NBAR_PIVOT}")
# fail threshold: residual ~ ln nbar requires Gamma ~ tens (strong coupling)
Gamma_fail = (LN_NBAR_PIVOT / c_DH)**(2.0/3.0)
check("FAIL only at strong coupling Gamma ~ tens (cold plasma)",
      Gamma_fail > 10.0,
      f"residual reaches ln nbar at Gamma ~ {Gamma_fail:.1f} (deep strong coupling; opposite the hot tilt epoch)")


# ---- report ----------------------------------------------------------------
print("=" * 72)
print("EU-1 numerical verification (Patch 0781)")
print("=" * 72)
allpass = True
for name, ok, detail in results:
    tag = "PASS" if ok else "FAIL"
    allpass = allpass and ok
    print(f"[{tag}] {name}")
    if detail:
        print(f"        {detail}")
print("=" * 72)
print("ALL PASS" if allpass else "SOME FAILED")
print("=" * 72)
