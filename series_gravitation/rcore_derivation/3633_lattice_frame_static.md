# OPEN-GR-SHELL-DATUM-1 rung 3 = OPEN-GR-LATTICE-FRAME-1's static face: the static ℓ = 2 exterior in the corpus's two candidate lattice frames. The harmonic-pattern frame (3611) computed with F-16 option 1; the census frame constructed and shown residual-free. Three readings, one sign: k₂ = +0.033 (harmonic, lapse), +0.088 (harmonic, C5's h̄₀₀), +0.042 (census). Under P-COUNT-UNIFORM-TO-LEVEL-SET the R-core's Love number is POSITIVE. Two corpus statements found to be weak-field only: C5's "statics: τ = 0", and the p = 0 census's agreement with the harmonic-pattern frame. PRED-O-40's falsifier ("a positive k₂") must be re-cut → a win-check round is the review-economy trigger

**Patch 3633, Session 162, 5 Sep 2026.** Verify `code/3633_lattice_frame_static_verify.py` (15/15; the harmonic condition derived symbolically on Schwarzschild, nothing recalled). Reasoning `reasoning/3633.md`. No paper touched.

## §1 The harmonic-pattern frame, statically
Gauge vector `ζ_μ = (0, bY, cY_{,θ}, 0)` from RW gauge to `∇^ν h̄_μν = 0`. The t and φ components vanish identically; the r and θ components give two coupled radial ODEs (θ-free). Facts:
- **The RW tide is not harmonic**: `∇^ν h̄_{rν} = 4(1 − M/r)Y` — O(M/r) relative to the tide. RW = harmonic at first order only.
- Homogeneous exponents `b ~ r^p`: **p = 3, 1 (growing), −2, −4 (decaying)** — the gradient modes `∇(r²Y)`, `∇(Y/r³)` and their partners.
- The particular series for the tide carries **the harmonic-coordinate logarithm**: `b = −(4/15) M r ln r + (41/45) r + …`. The frame at infinity is log-ambiguous (as harmonic coordinates on Schwarzschild are); the p = 1 coefficient is a convention (set to 0 = `ln(r/M)`). It does not touch the wall under option 1.
- **F-16 option 1** (ζ = 0 at the wall): the two decaying-mode coefficients solved; `b(R) = c(R) = 0` to 10⁻⁸; `b′(R) = 6.2`, `c′(R) = −7.9` per unit tide.

## §2 What the frame says at the wall
| quantity at R (per unit tide, λ = 8.97) | value |
|---|---|
| `h₀₀` (unchanged: b(R) = 0) | −1.246 |
| `h̄₀₀` (C5's register channel) | −2.665 |
| spatial trace of `h̄`, τ | **0.695** |

- **C5's static clause "τ = 0" does not hold at the wall** in the harmonic-pattern frame. It is the weak-field statement: the c07 dictionary linearised gives the lock `g^{ij}h_ij = −3(1 − v/2)·g^{tt}h_tt`, which is C5's `−3` only at v = 0; at the wall it is `−2`. The corpus's static dictionary (c07, nonlinear) and its linear one (C5) disagree at O(v).
- Linearised c07 map: `dh̄₀₀/dv = 4` at v = 0, **27/32** at the wall.
- **The census test:** δv read from the lapse in the harmonic frame is *not* harmonic in lattice coordinates near the wall (normalised residual −1.2 at r = 2.7M) and tends to harmonic at large r (0.05 at 30M, decaying like (M/r) ln r). **The p = 0 census (3389) and the harmonic-pattern frame (3611) are the same frame at first order and different frames at O(M·tide).** The test I proposed in 3632 was, as posed, a statement about *which* frame — not a consistency test of the exterior, because a gauge vector can make any one scalar harmonic.

## §3 The census frame
The gauge in which δv **is** harmonic in lattice coordinates (its two far-field coefficients the exterior's) and the c07 trace lock holds. `b(r)` is algebraic — `b = [2NN′δv_target − fH]/f′`, finite at the wall (0.43) — and `c(r)` algebraic from the lock. **It always exists and has no residual.** In it the level set is the Newtonian one in lattice radius and the closure closes by itself: **λ = (3/2)R̄⁵, k₂ = (3/4)(R̄/R)⁵ = +0.0422**, Λ ≈ +3.8. Consistency: `(9/8)(ξ_RW − b_cf(R))` equals the Newtonian level set to 10⁻⁶.

## §4 The three readings
| frame / reading | λ | k₂ | Λ |
|---|---|---|---|
| harmonic-pattern, register = lapse (R-CLOCK-RATE-IS-DISPLACEMENT), F-16 opt. 1 | 8.97 | **+0.033** | +3.0 |
| harmonic-pattern, register = h̄₀₀ (C5, linearised c07 at the wall) | 23.7 | **+0.088** | +7.9 |
| census frame (δv harmonic, c07 lock) | 11.4 | **+0.042** | +3.8 |

**Every corpus-native reading is positive**, 0.03–0.09. 3632's negative bracket (B) — the level-set sphere's own areal radius — is no frame of the corpus. Under P-COUNT-UNIFORM-TO-LEVEL-SET, **the sign of the R-core's tidal Love number is positive**; the magnitude is frame-dependent by ×3 and awaits one decision the corpus has not made: whether the static register is the lapse or h̄₀₀ at strong field, and whether the lattice frame is harmonic-pattern or census. The exterior GR-2 sentence that survives all three: `k₂ ≈ +0.03…+0.09, Λ ≈ +3…+8` at a = 0.

## §5 Consequences and next
- **PRED-O-40's falsifier is inverted.** V2.1/2.2 say "a positive k₂ falsifies"; the theory's own frames give positive. GR-2 owes V2.3 (sign; magnitude as a range over the frame question; PRED-O-40 re-cut: "Λ consistent with 0 at ±3, or a *negative* k₂, falsifies"). ET/CE reach unchanged.
- **Review economy: WIN-CHECK trigger met** (a sign flip of a minted prediction is a corpus claim conversion). A round — Q1 the harmonic-frame derivation; Q2 F-16 option 1 as the static residual; Q3 the c07/C5 discrepancy at O(v); Q4 the census frame's legitimacy (is "δv harmonic" a frame or a physics statement?); Q5 the closure λ = −(6/5)MR̄δ̄; Q6 P-COUNT-UNIFORM-TO-LEVEL-SET's standing; Q7 whether V2.3 as sketched is warranted — is recommended and, under PD-006, will be dispatched as **CONV-042 at Patch 3634** unless the founder redirects.
- OPEN-GR-SHELL-DATUM-1: the shell stress is bookkeeping (3631), the datum is the lattice-frame level set (3632), the frames all give one sign (3633). **ADVANCED to sign-determined; magnitude frame-dependent.** OPEN-GR-LATTICE-FRAME-1 now carries the static question too: lapse vs h̄₀₀; harmonic vs census.
- Superseded: 3624/3626/3627's "the sign is negative / the theory's" (it was K(R) = 0's, 3631); 3632's bracket (B) as a candidate.
