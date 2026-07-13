# OPEN-DM-FLOQUET-1 — method (a) result: the transverse charge-switched bending sign is CONDITIONAL and NARROW

**Patch 2440, 12 July 2026 (Opus, DM lane).** **Status of OPEN-DM-FLOQUET-1: still OPEN** — this settles the
*sign structure* of the K_switch contribution, not the make-or-break. Candidate (B) stays **UNRESOLVED**.
Verify script: `code/2440_floquet_method_a_sign.py` (reproduces every number below). Reasoning: `reasoning/2440.md`.

## 0. What method (a) was asked to do
Per the scoping doc §4, method (a) is the reduced Floquet–Mathieu analysis that fixes the **sign** of the transverse
charge-switched bending eigenvalue honestly, under G1–G7, before any magnitude work. It is explicitly *not* a
survival verdict; it is the gatekeeper that says whether the magnitude computation (method (b)) is even worth running
and on what condition.

## 1. Model (leading, sign-level)
The lowest transverse bending coordinate `x` of the eCP coat obeys `x'' + ω²(τ) x = 0` (τ = ω_sw·t), with the
instantaneous transverse stiffness **charge-switched** between a same-charge repulsive phase (+A, restoring) for
duty fraction δ and an opposite-charge attractive phase (−A, Earnshaw anti-restoring) for 1−δ. Taken as a square wave
this is the **Meissner equation**, whose monodromy is closed-form, so the Floquet sign is *rigorous, not
perturbative*. The one dimensionless magnitude is ε = A/(m ω_sw²) = (ω_A/ω_sw)², ω_A = √(A/m); small ε = fast
switching. The static (adiabatic) average coefficient is ε·(2δ−1), **negative for δ < ½**. Since δ = 3/7 (the
Patch-2435 uniform-sampling **upper** bound) is < ½, the mode is **statically inverted** — consistent with the 2437
refutation, and the reason a dynamical (parametric) rescue is the only survival route.

## 2. Results (all G1-consistent)

**G1 (limit checks) — PASS.** δ→0 (pure attraction) → UNSTABLE (Earnshaw, no stabilization); δ→1 (pure repulsion) →
stable with k_eff → +ε. The method reproduces the correct static sign in both no-modulation limits, so the setup is
sound.

**The naive Kapitza expectation FAILS.** In the fast-switching limit the inverted δ=3/7 mode is **UNSTABLE**:
tr(M)/2 = 1.003, 1.027, 1.131 for ε = 10⁻³, 10⁻², 10⁻¹ (all > 1). Order-counting: the negative static average is
O(ε)·(2δ−1) while the ponderomotive stiffening is O(ε²); at small ε the O(ε) negative term dominates. **Fast
charge-switching does *not* guarantee ponderomotive stiffening when δ < ½** — this corrects the earlier heuristic
that ZBW-fast switching would robustly stiffen the mode.

**Stabilization exists only in a narrow intermediate-ε window.** At δ=3/7 (symmetric magnitude) the stable band is
**ε ∈ [0.179, 0.428]**, i.e. ω_sw/ω_A ∈ ~[1.5, 2.4]. Outside it — both slower *and* faster — the mode is unstable.
This is a Meissner stability tongue, not a robust ponderomotive plateau. Recovered physical stiffness in-band:
k_eff/A ≈ **0.12 mid-band** (ε=0.30), rising to ≈ 0.57 only at the top edge (ε≈0.428), which is a period-doubling
marginal-stability boundary — physically fragile, not a place to sit. For reference the negative static average that
must be overcome is |2δ−1| = 1/7 ≈ 0.143 of A.

**Two levers, both deferred to R1/R6:**
- **Branch asymmetry (R6).** With ε_rep=0.30 fixed, varying ε_att: k_eff_coeff = 0.106 / 0.065 / 0.037 / 0.010 for
  ε_att/ε_rep = 0.5 / 0.8 / 1.0 / 1.2, then **UNSTABLE** at 1.5, 2.0. A *weaker* attractive phase (plausible if the
  driven equilibrium places the attractive interval at larger separation / shallower curvature) strengthens the
  rescue; a stronger attractive phase kills it.
- **Dynamical δ (R2).** At fixed ε=0.30, k_eff_coeff rises monotonically through δ = 0.40→0.60 (0.012→0.243). Because
  3/7 is an *upper* bound (G5), the dynamical δ is likely ≤ 3/7 < ½, which keeps the system on the hard side of the
  transition where the window is narrowest and the recovered stiffness smallest.

## 3. Sign verdict (G7 honored)
**NOT-YET-FALSIFIED; survival NOT demonstrated.** The K_switch sign is **conditionally positive but narrow**: it is
positive only if the substrate-derived ε lands in ~[0.18, 0.43] with a favorable (≤1) branch asymmetry, and even then
recovers only ~0.12·A. The fast-switching limit is unstable. This is reported straight — it is **not** re-parametrized
toward survival, and the registry is **not** promoted.

## 4. What this does and does not settle
Method (a) has done its job: it converts the make-or-break into a sharp, checkable condition and rules out the
generic "fast switching stiffens it" story. It does **not** settle the sign, because the sign now depends on three
derived quantities that are magnitude/derivation work:
- **R1/R2** — the geometry-#3 driven equilibrium → the actual ε = (ω_A/ω_sw)² and the dynamical δ (satisfies G3).
- **R6** — which E_bond branch fragments (E_qq core vs E_ee coat, factor α_s/α≈53) and the branch asymmetry ε_att/ε_rep.
- **R5/G4** — the recomputed **geometry-#3 ponderomotive tensor** (the 2430 analog had a −190 transverse eigenvalue on
  the *superseded* far-out-coat geometry). K_switch (~0.12·A in-window) must be **netted** against it; if the geom-#3
  transverse ponderomotive eigenvalue is still strongly negative, the net can be < 0 regardless of the parametric
  rescue.

## 5. Next sub-step (recommended order)
**R1 — the geometry-#3 driven equilibrium**, self-consistent under ZBW + charge-switching, to pin ε and the dynamical
δ and check whether they even fall in the stable window; then **R5** (recompute + net the ponderomotive tensor on
geom #3). Only if the netted transverse sign is positive does method (b) (MD/kMC magnitude) become worth running.
Decision rule (scoping §5) unchanged; Ω_DM stays parked.
