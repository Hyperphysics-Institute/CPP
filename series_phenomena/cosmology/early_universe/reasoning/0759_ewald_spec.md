# Reasoning capture — Patch 0759: Ewald/RPA simulation spec

*Session 154. Rigorous protocol for the one open question (long-range inter-GP sqrt(n) residual), replacing
the 0758 broken toy. Writeup: `.../ewald_rpa_spec.md`. Validation script: `.../scripts/0759_ewald_method_validation.py`.
NO THEO.*

## The three toy failures -> three fixes
1. naive long-range cutoff -> Ewald (exact long-range; screened needs only real-space cutoff).
2. high-density/strong-coupling + raw-Widom rare-event blow-up -> dilute regime + Kirkwood charging TI.
3. ill-conditioned narrow-range fit (n, sqrt n, ln n collinear) -> wide log-spaced n range + column-
   normalized cond + subtract A1 ln n, fit residual.

## Validated the two methodological fixes (0759 script)
FIX 1: recover known B=0.05. narrow toy range -> column-normalized cond~611, B_fit=1.38 (2654% err,
  unrecoverable). wide log range 1e1..1e8 -> cond~16, B_fit=0.033 (~35%, recoverable). => wide range +
  residual subtraction required. (Caught that RAW cond conflates scaling w/ collinearity; switched to
  column-normalized cond as the honest collinearity diagnostic.)
FIX 2: raw Widom -ln<e^{-dE}> vs charging/cumulant as coupling s grows. s=4: Widom -5.5+/-0.5 (biased,
  scattered) vs true -6.0; charging -6.04 (accurate). => Kirkwood TI not raw Widom. This is exactly the
  0758 high-lambda blow-up mechanism.

## Protocol (staged, each gates the next)
A. validation: unscreened Coulomb, dilute -> reproduce DH limiting law mu_ex ~ -sqrt(n) (REQUIRED before
   trusting anything downstream), finite-size scale.
B. crossover: scan Gamma, n -> locate n_* where DH sqrt(n) ends; confirm 0757 n_* ~ (kT/q^2)^3.
C. screening: scan Yukawa xi -> B(xi)->0 as xi shrinks (sqrt n is the unscreened tail effect).
D. real SSV kernel: plug in actual CPP SSV range/form; measure B; check B*sqrt(1e74) vs ln nbar~170.

## Method
Ewald (real erfc + reciprocal + self, tinfoil) for unscreened; real-space cutoff for Yukawa. mu_excess via
Kirkwood charging TI (scale tagged charge 0->1, integrate <dU/dlambda_c>). RPA/DH analytic reference; HNC
optional. Report tau_int, >=4 seeds, equilibration discard.

## Pass/fail
PASS: B~0 (screened) OR cosmological point above n_* (strong-coupling, no sqrt law) OR B*sqrt(1e74) << 170
  (B <~ 1.7e-35). FAIL: unscreened long-range + DH regime + B*sqrt(1e74) >~ 170.
Required gate: Stage A must reproduce DH sqrt(n) or nothing downstream is trusted.

## Honesty calibration
- Delivered a PROTOCOL + validated the two fixes; did NOT implement/run Ewald (panel task; flagged as
  specified-not-run). No overclaim.
- Gave the analytic target (DH limiting law) so the sim is checkable, and tied pass/fail to the explicit
  cosmological-pivot magnitude condition.
- Named the one physical input still required from CPP: the real SSV interaction range/form (Stage D).
- Connected to 0756/0757: this is the rigorous version of the broken 0758 toy; 0757's on-GP point-stack
  result + crossover stand; this targets only the long-range inter-GP corner.

## Pointer
- Panel (Grok ready) implements A-D, reports B + pass/fail for the real SSV kernel. Independent
  implementations welcome. Clear of chirality. PCD = Perceive/Compute/Displace.
