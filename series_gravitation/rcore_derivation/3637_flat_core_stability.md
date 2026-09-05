# OPEN-GR-SATURATED-CORE-1 rung 3: stability of the flat-core branch, by what statics can decide. The combined SLy sequence (TOV → threshold → flat core growing) has M(N_b) monotone with no cusp up to the branch maximum; the flat-core stars are bound and their binding grows. But at fixed baryon mass, M is NOT stationary at the register radius — it rises with core radius (dM/dr_c > 0 for every member): the flat-core star is a CONSTRAINED equilibrium held by the register cap, ~0.05 M☉ above the GR configuration of the same baryon number at 2.08 M☉. Stability is therefore exactly the rigidity of the cap. R-FLOOR-REGISTER makes the cap a saturation limit (rigid): then the branch inherits the TOV branch's stability up to ~2.9 M☉ and CPP passes J0740 with a flat-core star — with a signature: radii RISE with mass above the 1.78 M☉ knee

**Patch 3637, Session 162, 5 Sep 2026.** Verify `code/3637_flat_core_stability_verify.py` (6/6; SLy, recalled coefficients as 3636). Reasoning `reasoning/3637.md`. No paper touched. CONV-042 held.

## §1 The combined sequence (SLy)
| p_c/p_thr | r_c (km) | M (M☉) | N_b (M☉) | R (km) | N_b − M |
|---|---|---|---|---|---|
| 0.72 | 0 | 1.645 | 1.860 | 11.39 | 0.215 |
| 1.00 (threshold) | 0 | 1.779 | 2.040 | 11.22 | 0.260 |
| 0.88 | 3.9 | 1.860 | 2.146 | 11.13 | 0.286 |
| 0.64 | 6.5 | **2.080** | 2.400 | **11.23** | 0.320 |
| 0.47 | 8.1 | 2.307 | 2.634 | 11.58 | 0.327 |
| 0.31 | 9.8 | 2.614 | 2.925 | 12.27 | 0.311 |
| 0.25 | 10.5 | 2.768 | 3.064 | 12.67 | 0.297 |

M and N_b increase monotonically through the threshold and along the branch: **no turning point, no cusp** in the M–N plane up to the branch maximum. The stars are bound; the binding peaks near 2.3 M☉ and then declines slowly. **The radius has a minimum (11.1 km near 1.9 M☉) and then rises with mass** — the opposite of GR's TOV branch, where R falls toward the maximum.

## §2 The variational test — the cap bears a load
For flat-core members at 1.86, 2.08, 2.38 M☉: at fixed baryon mass, vary the core radius (envelope kept hydrostatic). M is **not stationary** at the register radius; `(dM/dr_c)/(M/r_c) = +0.010, +0.082, +0.170`, monotone across it. The star would lower its GR energy by shrinking the core — through configurations with central lapse < ½, which the register forbids. Against the GR (TOV) star of the same baryon number (the register-forbidden one): the flat-core star is heavier by 0.004 → 0.050 M☉ from 1.86 → 2.08 M☉. **The flat-core star is a constrained equilibrium: the cap holds it, ~0.05 M☉c² above the unconstrained GR minimum at J0740's mass.**

## §3 What stability now is
The Harrison–Thorne–Wakano–Wheeler turning-point theorem needs the sequence to be extrema of M at fixed N — it is not, in the unconstrained GR sense (§2). On the **constraint manifold** (register at cap inside the level set, level set at lapse ½, envelope hydrostatic, core structureless) the flat-core equilibria *are* the constrained extrema, the constrained sequence has no cusp (§1), and stability is inherited from the sub-threshold TOV branch up to the branch's own mass maximum. So:

- **Cap rigid** (R-FLOOR-REGISTER: "the PSR floor is a register-saturation limit on SSV_abs" — a hard limit, as ruled 1 Sep): **the flat-core branch is stable to ~2.9 M☉.** CPP passes J0740 with a flat-core star of R ≈ 11.2 km, predicts the 1.78 M☉ knee and rising radii above it, and puts GW190814's secondary on the branch.
- **Cap soft** (demand in excess can push the register past the floor): nothing above 1.78 M☉ is stable; CPP is contradicted by J0740 at 4σ.

**The corpus's own ruling makes the cap rigid.** The one line to confirm by picture: does demand in excess of the cap ever move the register (a floor that yields under load), or is a saturated register saturated (the floor holds)? R-FLOOR-REGISTER says the latter; this patch is read under it.

## §4 The signature, and what is owed
- **M–R knee at 1.78 M☉**: below it, GR; above it, radius rising with mass (11.1 km at 1.9 → 11.2 at 2.08 → 12.7 at 2.8). Testable now against NICER's J0740 (12.4 ± 1) and J0030 (1.4 M☉, ~12–13 km): both consistent at 1σ; a future 2.5 M☉ radius at ~12 km would discriminate from every GR EOS that reaches 2.5 (all of which have R falling).
- The stored constraint energy (~0.05 M☉c² at 2.08) is released only if the cap yields — a merger-dynamics question, not touched.
- Owed: a dynamical (radial-mode) confirmation of the constrained argument; published EOS tables; APR4 and a stiff EOS for the knee's EOS-independence (3636: 1.78 vs 1.79). OPEN-GR-SATURATED-CORE-1 stands at **stability decided conditionally on cap rigidity**.
