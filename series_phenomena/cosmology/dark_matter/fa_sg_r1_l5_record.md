# FA-SG-R1 LEG L5 RECORD — the optional J6 hop-Laplacian branch, run on the [ADJ] trigger: **J6-DIVERGE** — the alternative assembly provably CANNOT stagger (M-matrix positivity) and screens at ℓ ≈ 0.199 fm ≈ 2× the joint band, matching its own analytic dispersion (0.1955 fm); a representation-dependence finding in its own right, adverse to neither branch per the new-branch ruling

**Patch 2689, 21 July 2026. Executing charter §2 R1-L5 under its
pre-frozen classes. Trigger determination [ADJ, disclosed for the panel
vote]: legs L1–L4 left a live representation-dependence question —
J3-REVISE showed the scale normalization-sensitive within the 1/r
assembly, and the L2 committed consistency test failed — so whether the
staggered-exponential structure belongs to ANY screened z=12 lattice
operator or to the dense 1/r multiple-scattering assembly specifically
was live; the first branch of the frozen trigger ("if legs L1–L4 leave a
live representation-dependence question") was judged met under PD-006.
Verify: `code/2689_r1_l5_hop_laplacian.py`. 79.5% not in scope.**

## §1 — The alternative assembly (zero free parameters)

Nearest-neighbour hop (graph) Laplacian on the z=12 edge set, (Δf)_i =
Σ_{j~i}(f_j − f_i), whose continuum limit on any z=12 Barlow packing is
2a²∇²f (isotropy of the 12-shell). The screened equation discretizes to
A φ = s with **A = −Δ + 2(κa)² I = −Δ + 8I** at the frozen κa = 2; unit
point source at the central site. Analytic expectations stated pre-run
in the verify script: (i) A is an M-matrix ⇒ A⁻¹ ≥ 0 elementwise ⇒ the
response is strictly positive — **staggering is impossible in this
assembly, as a theorem**; (ii) the [001] lattice dispersion gives
4 + 8cosh(q/√2) = 20 ⇒ ℓ_hop = a/(√2·arccosh 2) = 0.1955 fm.

## §2 — Results

| Arena | positivity | ℓ_hop (3 windows) | R² |
|---|---|---|---|
| FCC R=9 | min response +1.8e−10; neg-frac 0.000 | 0.2003 ± 0.0025 fm | 0.990–0.997 |
| HCP R=9 | min response +2.0e−10; neg-frac 0.000 | 0.1988 ± 0.0024 fm | 0.993–0.999 |

Both confirm the M-matrix positivity numerically and land on the
analytic dispersion value; the assembly is arena-independent (FCC vs
HCP concordant) just as the 1/r assembly was at L1.

## §3 — Verdict and reading (frozen classes only)

**J6-DIVERGE**: materially different structure (no staggering — provably)
AND materially different scale (≈ 0.199 fm vs the joint band
[0.0836, 0.0956] fm; note 0.199 fm ≈ the 1/r assembly's own weak-coupling
Yukawa regime scale, L4 §3 first row). Per Grok's adopted ruling this is
**a representation-dependence finding in its own right, adverse to
neither branch by itself**: the sign-staggered evanescent response at
ℓ = 1/(2κ) is a property of the dense 1/r multiple-scattering assembly
specifically — arena-independent WITHIN that assembly (L1 CONCORD), but
not shared by every screened z=12 lattice operator. Which assembly the
Sea's derivation chain actually grounds (S1b derived the 1/r
discrete-site scattering form; the hop-Laplacian is a NEW branch, not a
defect of that derivation) is for the panel at the returns.

**Fence audit:** clean. Reasoning: `reasoning/2689.md`.
