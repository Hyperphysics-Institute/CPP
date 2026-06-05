# Ewald/RPA simulation spec: the long-range √n̄ residual test (panel protocol)

*Patch 0759, Session 154. A rigorous protocol for the one open question left in the n_s arc: does a
charge-balanced **long-range** (inter-GP) CP plasma develop an excess chemical potential μ_excess ∝ −√n̄
(Debye) whose coefficient is large enough to dominate ln n̄ ≈ 170 at the cosmological pivot n̄ ~ 10⁷⁴? The
0758 toy could not answer this (it broke down). This spec fixes the three things the toy got wrong and
defines a trustworthy test. The two methodological fixes are **validated** in
`series_phenomena/cosmology/early_universe/scripts/0759_ewald_method_validation.py`; the Ewald simulation
itself is specified here for the panel (Grok offered to run it). NO THEO.*

## 1. The one question, and the analytic target

**Question.** For the actual CPP SSV interaction, is there a μ_excess ∝ −√n̄ that survives charge
neutrality, and is it large enough to compete with the logarithm at the cosmological pivot n̄ ~ 10⁷⁴? **The
comparison must be dimensionless** (ChatGPT's calibration): the quantity that enters the tilt chain is
μ/kT = ln n̄ + (μ_excess/kT), so write the residual as a **dimensionless** coefficient
B ≡ (√n̄ coefficient of μ_excess/kT). The threat condition is then B·√n̄ ≳ ln n̄ — both sides dimensionless —
i.e. B·10³⁷ vs 170 → threat if B ≳ 1.7×10⁻³⁵. Reporting μ_excess in raw energy units and comparing to "170"
risks a hidden kT factor; always reduce to μ_excess/kT before comparing to ln n̄.

**Analytic reference (so the sim has a known target).**
- **Debye–Hückel limiting law** (weak coupling, unscreened Coulomb): μ_excess/kT = −½·κ·(q²/kT) with the
  inverse Debye length κ² = 4π n q²/(kT) (Gaussian units), i.e. μ_excess/kT = −(1/√(4π))·Γ^{3/2}·(…) — the
  point being μ_excess ∝ −√n. The simulation **must reproduce this** in the dilute weak-coupling limit
  before any other stage is trusted.
- **Debye-regime crossover** (0757): DH (hence the √n law) holds only for n < n_* ~ (kT/q²)³; above n_* the
  plasma is strongly coupled and the √n law does not apply. Stage B confirms this numerically.
- **Screening**: for a screened (Yukawa) interaction the √n is replaced by an analytic virial series
  (∝ n, n², …) whose leading term charge-balance cancels; the √n is specific to the unscreened long-range
  tail. Stage C maps B(ξ).

## 2. Why the 0758 toy failed → three fixes

1. **Naive long-range cutoff** → use **Ewald** (exact long-range Coulomb on a periodic lattice; or PME/P3M
   for large N). Screened (Yukawa) needs only a real-space cutoff.
2. **High-density / strong-coupling + raw-Widom blow-up** → run in the **dilute (weak-coupling) regime**
   and estimate μ_excess by **Kirkwood charging thermodynamic integration**, not raw Widom. (Validated,
   §5 FIX 2: raw Widom scatter explodes as coupling grows; charging/cumulant stays accurate.)
3. **Ill-conditioned narrow-range fit** → scan n over **many decades** (log-spaced), report the
   **column-normalized** condition number (true collinearity), and **subtract the A1-guaranteed C·ln n**
   before fitting the residual to A·n + B·√n + D. (Validated, §5 FIX 1: narrow range cond ≈ 600 → B
   unrecoverable; wide range cond ≈ 16 → B recovered.)

## 3. Method

**Energy (unscreened Coulomb): Ewald summation** on a periodic, overall-neutral lattice — real-space sum
of erfc(αr)/r, reciprocal-space sum over k of exp(−k²/4α²)|ρ(k)|²/k², minus the self-energy term;
tinfoil (conducting) boundary so the surface term vanishes for the neutral system. Standard formulas;
validate the Ewald energy against a known Madelung/known-config reference before production.
**Screened (Yukawa) energy:** real-space sum of q_iq_j e^{−r/ξ}/r within a cutoff ≳ 6ξ (no Ewald needed).

**Excess chemical potential: Kirkwood charging TI.** Insert a tagged particle and scale its charge
q → λ_c·q; then μ_excess = ∫₀¹ ⟨∂U/∂λ_c⟩_{λ_c} dλ_c, with the integrand averaged in equilibrium at each
λ_c (a Gauss–Legendre grid of ~8 λ_c points). Robust at all densities — the §5 fix. (Raw Widom may be
used as a cross-check only in the dilute limit where it still works.)

**Sampling:** Metropolis MC or MD; report integrated autocorrelation time τ_int, ≥ 4 independent seeds,
and an equilibration-discard of ≳ 10 τ_int. Confirm the stationary occupation/structure is Gibbs.

**Analytic cross-checks:** RPA/Debye–Hückel (limiting law, §1) as the dilute reference; optionally HNC for
moderate coupling.

## 4. Protocol (staged — each stage gates the next)

- **Stage A — method validation (REQUIRED first).** Unscreened Coulomb, dilute (Γ ≪ 1). Reproduce the DH
  limiting law μ_excess ∝ −√n to within a few percent, with finite-size scaling L → ∞. If the method does
  not recover the known √n here, nothing downstream is trustworthy.
- **Stage B — the crossover.** Scan coupling Γ and density n; locate n_* where the DH √n law gives way to
  strong coupling; confirm 0757's n_* ~ (kT/q²)³. This establishes whether the cosmological point sits in
  the DH regime (√n present) or beyond it (√n absent).
- **Stage C — screening.** Scan Yukawa screening length ξ; show B(ξ) → 0 as ξ decreases (screening removes
  the √n, leaving the charge-balance-cancelled virial series). Map how much screening is needed to make B
  negligible.
- **Stage D — the real SSV kernel.** Plug in the actual CPP SSV interaction (its range/form — the required
  physical input). Measure B and evaluate B·√n̄ vs ln n̄ at n̄ ~ 10⁷⁴.

## 5. Validated methodological fixes (this patch)

Script `0759_ewald_method_validation.py` validates the two fixes the protocol depends on:
- **FIX 1 (conditioned fit):** recovering a known B = 0.05 — narrow toy range (4,8,16,32) gives
  column-normalized cond ≈ 611 and B_fit = 1.38 (2654% error, unrecoverable); wide log-spaced range
  (10¹–10⁸) gives cond ≈ 16 and B_fit = 0.033 (≈ 35%, recoverable). Wide range + residual subtraction is
  required.
- **FIX 2 (density-robust μ):** as the coupling/density scale s grows, raw Widom (−ln⟨e^{−ΔE}⟩) scatters
  and biases (at s = 4: −5.5 ± 0.5 vs true −6.0), while the charging/cumulant estimator stays accurate
  (−6.04). Kirkwood TI, not raw Widom.

## 6. Observables & pass/fail

**Primary:** B, the **dimensionless** √n̄ coefficient of **μ_excess/kT** — measured in Stage A/B for the
relevant kernel, finite-size- and dilute-extrapolated, and finally for the real SSV kernel (Stage D). All
pass/fail comparisons are made between B·√n̄ and ln n̄, both dimensionless (μ_excess reduced by kT before
comparison — ChatGPT's calibration; equivalently, compare to kT·ln n̄ if working in energy units).

- **PASS** (the √n̄ does not threaten the tilt): either B ≈ 0 (screened / kernel cut off), **or** the
  cosmological point lies above n_* (strong-coupling regime, √n law absent — 0757), **or** B is resolvable
  but B·√n̄_pivot ≪ ln n̄ ≈ 170 (i.e. B ≲ 1.7×10⁻³⁵, dimensionless). Any of these closes the corner.
- **FAIL** (real threat): the real SSV kernel is effectively unscreened long-range, the cosmological point
  is in the DH regime, **and** B·√n̄_pivot ≳ ln n̄ (dimensionless) — the √n̄ residual dominates and n_s is
  dragged off 0.9649 into the excluded branch.

**Secondary / required gates:** Stage-A reproduction of the DH limiting law (method validation);
column-normalized fit condition number (must be modest); S(k→0) compressibility; equilibration
diagnostics (τ_int, seed spread).

## 7. What the panel is asked to do

Implement Stages A–D (independent implementations welcome — convergence across designs is the strong
result). The decisive deliverable is **B for the real SSV kernel** and the pass/fail at the cosmological
pivot. Grok offered to run with the real SSV form; this spec gives the rigorous protocol so the result is
trustworthy rather than a broken-toy artifact. The one physical input still required from CPP is the
**actual SSV interaction range/form** (Stage D) — without it, Stages A–C still bound the answer (screened
→ pass; unscreened-in-DH-regime → measure B and check), but Stage D is where it is settled.

## 8. Status

- The two methodological fixes are validated; the Ewald simulation is specified, not run (panel task).
- This converts the 0758 broken toy into a rigorous, staged, falsifiable protocol with a known analytic
  target (DH limiting law) and a clear pass/fail at the cosmological pivot.
- Combined with 0757 (analytic crossover + on-GP point-stack on-site → no √n) and 0756 (neutrality cancels
  the leading mean-field), this protocol targets the single remaining corner: the long-range inter-GP √n̄
  for the real SSV kernel.

## Pointers

- Validation script: `.../scripts/0759_ewald_method_validation.py` (FIX 1 + FIX 2 validated).
- Builds on 0758 (broken toy → this fix), 0757 (analytic √n + crossover), 0756 (neutrality).
- Reasoning: `.../reasoning/0759_ewald_spec.md`. Add to the swarm request as the rigorous protocol.
