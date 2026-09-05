# OPEN-GR-SHELL-DATUM-1, first rung: Israel's second junction condition written out for the static ℓ = 2 tide. The first junction never fixed K(R) — 3624's K(R) = 0 was the assumption ξ_in = ξ. The shell's shear and isotropic pressure are set by the tide (not by the closure); the whole datum is ONE number, δσ, and k₂ runs over both signs with it (−0.080 at K(R) = 0; −0.049 for a rigid surface; +0.012 for fixed count density). The register's own closure is not a stress law but the CENSUS (uniform count inside the moved level set): its Newtonian limit is Kelvin's k₂ = 3/2. The relativistic census at C = 0.375 is the next act; GR-2 V2.2's sign statement is HELD pending it

**Patch 3631, Session 162, 5 Sep 2026.** Verify `code/3631_shell_datum_junction_verify.py` (24/24; every field equation and both junction conditions derived symbolically — Hinderer's convention `g_tt = −f(1+HY)`, `g_rr = (1−HY)/f`, `g_ang = r²(1−KY)`). Reasoning `reasoning/3631.md`. No paper touched.

## §1 The configuration, and the machinery checked on it
Exterior Schwarzschild (mass M) for r > R; interior flat with lapse ½ uniform (the register at cap, 3375); surface at areal R = 8M/3, the level set of the register (3396). Israel on the background: σ = (1 − √f)/(4πR) = 1/(8πR), P = σ/4, 4πR²σ = 4M/3 — 3624's bookkeeping recovered from the extrinsic-curvature jump.

The exterior static ℓ = 2 sector re-derived from the linearised Ricci (no recall): (r,θ) gives K′ = H′ + 2MH/(r(r−2M)); (θ,θ) with K′ eliminated gives 3624's algebraic K; (tt) with K eliminated *is* the master ODE. Growing solution H_G = r(r−2M), K_G = r² − 2M². Decaying solution in **closed form** by reduction of order (W = 1/H_G): `H_D = −5(r−2M)[6r³ − 18r² + 8r + 4 − 3r²(r−2M)² ln(r/(r−2M))]/(16 r (r−2M)²)`, normalised r³H_D → 1, no growing admixture — no numerical integration, no cancellation (3629's lesson).

## §2 The first junction, done properly — K(R) was never fixed
Surface r = R + ξY outside, ρ = R + ξ_in Y inside. Continuity of the induced metric:
- `g_tt`: `ξ f′(R) + f(R) H(R) = 0` — the lapse pin. This is the level set (3624 §2). It fixes ξ.
- `g_θθ`: `ξ_in = ξ − R K(R)/2` — it **defines** the interior displacement (= the areal-radius modulation of the surface 2-sphere, δr_areal). It does **not** constrain K(R).

So 3624's `K(R) = 0` was the additional assumption `ξ_in = ξ` — equal *coordinate* displacements on the two sides — which is not a junction condition and not a corpus rule. That is exactly the hidden datum CONV-041 named (Q2, YES 4–1), now located: it is the second junction condition, and the first junction leaves the exterior's decaying amplitude λ free.

## §3 The second junction — the shell's response, affine in the one free coefficient
`S^a_b = −([K^a_b] − δ^a_b [K])/8π` to first order, decomposed as `δS^t_t = −δσ Y`, `δS^A_B = δP Y δ^A_B + Π (Y^{:A}_{:B} − ½δ^A_B ∇²Y)/R²`. With the lapse pin imposed and the exterior field equations used at R, per unit tide (H_G normalised to r(r−2M)) at R = 8M/3:

| | value |
|---|---|
| δσ | 0.01547 − 0.00476 λ |
| δP | 0.05858 − 0.000027 λ |
| Π | 0.2083 − 0.000097 λ |
| K(R) | 5.111 + 0.2364 λ |
| δr_areal | −8.395 − 0.6329 λ |

Three things follow.
1. **Shell conservation with the lapse pinned:** `δP = 2Π/R²` — an identity in λ that holds *only* once the exterior field equations are imposed (Bianchi, not tautology). The level set is what makes the lapse uniform on the surface, so no pressure gradient is needed against a lapse gradient: the isotropic pressure perturbation is carried entirely by the shear.
2. **The surface must carry shear.** Π = 0 forces δP = 0 at the same λ but leaves δσ ≠ 0 (−10.2): a barotropic fluid shell cannot sit statically in the tide. (Its Love number would be ~8; excluded.)
3. **Π and δP are set by the tide, not by the closure** — their λ-slopes are < 10⁻³ of their black-hole values. **The entire second-junction datum is one number: δσ, how the count per proper area responds to the tide**, and `λ = 3.25 − 210 δσ`.

## §4 The family — and the sign is not robust
| closure | λ | y | k₂ | Λ |
|---|---|---|---|---|
| black hole | 0 | 5 | 0 | 0 |
| `K(R) = 0` (3624: ξ_in = ξ) | −21.62 | −31/3 | **−0.080** | −7.2 |
| `δr_areal = 0` (surface intrinsically rigid) | −13.27 | −125/9 | **−0.049** | −4.4 |
| `δσ = 0` (count per proper area fixed at cap) | +3.25 | +1/3 | **+0.012** | +1.1 |
| `Π = 0` (no shear; excluded by §3.2) | 2142 | −6.8 | 7.9 | 714 |

The magnitude |k₂| ~ 0.01–0.1 is robust (3629), **the sign is not**: 3624/3626's negative sign was the K(R) = 0 closure's, and the fixed-count-density closure is positive. GR-2 V2.2's sign statement is therefore **HELD pending §5** — no corrigendum yet, because the register's own closure is none of these three.

## §5 The register's own closure is the census, not a stress law
The corpus does not describe the surface as matter with a constitutive law; it describes M as the count at cap (GR-1c's dictionary; 3629 Q5), the register v as the 1/r census of the count (v = M/r_iso outside; R-PSR-LAW-LOG, 3390), the surface as the level set v = 2/3, and the interior as uniformly at cap. In those variables the second junction condition is answered without any stress law: **the induced exterior field is the census of a uniform-count region bounded by the moved level set.** GR's S_ab is then bookkeeping, as σ was.

Newtonian limit, solved self-consistently (uniform density, tide E r²P₂, boundary the level set of self + tide): `δ = −15ER/(8πGρ)`, `Q = (4π/5)ρR⁴δ`, **`k₂ = 3/2`** — Kelvin's homogeneous-body Love number (h₂ = 5/2). Positive, O(1), ~20× the K(R) = 0 magnitude. At C = 0.375 the number will be different (the incompressible relativistic body's k₂ falls steeply with compactness) and may not even keep the sign; what is settled here is *which computation* the register prescribes.

## §6 Standing and next
- OPEN-GR-SHELL-DATUM-1: **ADVANCED, not closed.** The datum is located (the second junction), reduced (one number, δσ), and its register-native closure identified (the census). Owed: **the relativistic census** — the corpus's v = M/r_iso law applied to the perturbed count region at C = 0.375, with the level set v = 2/3 and the interior uniform at cap; this yields δσ (equivalently λ) and hence the theory's own k₂, sign included. One patch.
- GR-2 V2.2: no change now. If the relativistic census returns k₂ > 0, V2.3 (sign) and PRED-O-40's falsifier (currently "a positive k₂ falsifies") must be re-cut.
- Founder question (physical picture, one): under a static tide, is the count inside the R-core still uniform at cap out to the moved level set — the census picture of §5 — or does the count pile up on the bulge (δσ ≠ 0 on the surface in GR's bookkeeping)? The derivation assumes the former, which is what 3375 says.
