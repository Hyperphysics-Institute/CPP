# OPEN-SR-9 / R2 — Does the Asymmetric (Centroid-Shifting) DP Response Rescue the PASS? No.

**Patch:** 2022 (22 June 2026) · **Window:** 2000-band · **Work item:** OPEN-SR-9 / R2 (tests the 2021 retraction)
**Status of result:** **The 2021 retraction STANDS.** The founder correctly noted the DP response is
**asymmetric**: the inverse-square field is stronger on the near pole, so the poles displace unequally and
the DP centroid shifts (it is not a symmetric stretch about a fixed center). This is real and the picture is
improved. But it is a **higher-multipole / gradient** effect that does **not** change the leading C-scaling of
ε₀. R2 reduces (Patch 2021) to Z₀ = 1/(ε₀c) = C/c, and the rescue would require ε₀ ∝ 1/√C; the computation
shows ε₀ ∝ 1/C is robust to the asymmetry, so Z₀ = C/c is unchanged and R2 still leans FAIL on the grounded
c∝√C. **Verify:** `scripts/2022_asymmetry_check.py`.

---

## The only lever the correction has

The retraction rests on three facts; the asymmetry can touch only one of them:
- Z₀ = 1/(ε₀c) — an unconditional EM identity (μ₀ε₀=1/c²); independent of DP internals. **Untouchable.**
- c(C) — the lattice propagation speed; set by the wave mechanics, not the polarization response shape. The
  asymmetry is a quasi-static polarization effect, so it does not change c(C). **Untouched.**
- ε₀ ∝ 1/C — the polarizability. **This is the only thing the asymmetry could change**, and the rescue is
  specifically ε₀ ∝ 1/√C (which with c∝√C would give Z₀=const, PASS).

## The computation (lets the exponent come out however it comes out)

Two poles, harmonic restoring stiffness C about ±d0/2, driven by the FULL inverse-square field of a charge at
R (asymmetry = near pole sees more field). Self-consistent solve; α_E, centroid shift, field asymmetry; sweep C.

| regime | field asymmetry | centroid shift | d ln α_E / d ln C |
|---|---|---|---|
| linear / LPI-relevant (R≫d0) | ~0.17 | nonzero (~1e-3…1e-5) | **−1.000** |
| strong (R~3 d0) | up to ~1.08 | nonzero (~0.18) | **−1.07** |

The centroid shift and field asymmetry are **nonzero** (the founder is right about the physics), but the
leading C-exponent of ε₀ stays at −1 (it drifts to −1.07 under huge asymmetry — *toward* 1/C, away from the
−0.5 that would rescue PASS). Reason: to leading order each pole displaces by (local force)/C, so the dipole
polarizability is set by the curvature C → α_E ∝ 1/C; the asymmetry adds multipole/gradient structure (the
centroid shift) on top, but does not rescale the leading dipole term.

## Verdict

ε₀ ∝ 1/C is robust to the asymmetric/centroid-shifting response ⇒ Z₀ = C/c unchanged ⇒ with grounded c∝√C,
**Z₀ ∝ √C, R2 still leans FAIL.** The 2021 retraction stands. The correction genuinely improves the physical
picture (and would matter for forces/gravity, where the field-gradient net force is real), but it is not a
lever on the impedance scaling. NO THEO. Honest negative; the exponent was free to land at −0.5 and did not.
