# Step (b′) — Shell-sum rigor: the absolute-|SSV| monopole is annihilated (Patch 1108)

**Arc:** `series_relativity/op_einstein_closure/` · **Charter:** `README.md` · **Verify:**
`code/1108_stepBprime_shell_moments.py`
**Result:** the shell-sum reduces **exactly** to `∇²(Δ|SSV|)` — the would-be absolute-|SSV| term is
annihilated by the 600-cell neighbor-shell symmetry. **(b′) conditionally closed at leading order.**
**op:einstein NOT closed** (the nonlinear GR-recovery (a) remains). **NO VERDICT MOVED.**

## The question Step (b) left open
Step (b) (Patch 1107) showed c08's *stated* field equation is inert-Sea-safe, but the excess form
rests on a proof *sketch*: "the LSP broadcast at each Grid Point, summed over shells, gives
`∇²(Δ|SSV|) = (4πG/c²)ρ_mass`." The open worry: does that shell-sum silently drop an
**absolute-|SSV| term** that would let the uniform Sea gravitate?

## Where an absolute term would live, and why it can't survive
Expand the broadcast field `f` arriving from a neighbor at displacement `a·v̂` (shell radius `a`):
`f(x + a v̂) = f(x) + a (v̂·∇)f + ½a²(v̂·∇)²f + …`. The Grid Point's **displacement** response is the
*directional* (vector) sum over the shell — c05's gradient-sourcing: an isotropically surrounded GP
feels no net push. So the response is `∝ Σ v̂ · f(x+av̂)`, and term by term:

- **degree-0/1 (the absolute term):** `f(x)·Σ v̂` — this is the absolute field value (including the
  uniform Sea ground state, however enormous) times the shell's **monopole moment** `Σ v̂`. If
  `Σ v̂ = 0`, the absolute value contributes **nothing** to the displacement.
- **degree-2 (the gradient/Laplacian term):** `Σ v̂ (a v̂·∇)f = a (Σ v̂⊗v̂)·∇f`. If `Σ v̂⊗v̂ ∝ I`, this
  is `∝ ∇f` isotropically, and its divergence (the field equation) is `∝ ∇²f`.

So the absolute-|SSV| term sits **at the monopole**, and the inert-Sea property is exactly the
statement that the neighbor shell has **vanishing monopole** and **isotropic quadrupole**.

## The 600-cell shell delivers both — exactly
The neighbor shell is the 600-cell's 12 nearest neighbors (c07/c08 **12-edge selection rule**) = a
regular **icosahedron**. Computed (`code/1108_stepBprime_shell_moments.py`):

| moment | value | meaning |
|---|---|---|
| degree-1 `Σ v̂` | `0` exactly (\|·\| = 3.9×10⁻¹⁶) | **absolute-\|SSV\| term annihilated** |
| degree-2 `Σ v̂⊗v̂` | `4·I` exactly (isotropic) | continuum operator = **Laplacian** |
| degree-2,4 angular moments | match the sphere exactly | no anisotropy through degree 5 |
| degree-6 | deviates (~3×10⁻²) | first lattice-anisotropy correction |

The icosahedron is a **spherical 5-design**: angular moments through degree 5 equal the continuum
sphere exactly, and odd moments vanish by central symmetry (`v̂ → −v̂`). The monopole (degree 1) and
the Laplacian coefficient (degree 2) are therefore **exact**, not approximate.

## Conclusion
The shell-sum reduces **exactly** to `∇²(Δ|SSV|) = (source)` with the absolute-|SSV| monopole
**annihilated by icosahedral symmetry** — not subtracted by hand, not assumed away. (b′) closes the
shell-sum worry, **conditional on two existing CPP premises** (no new physics):
1. the neighbor shell is the 600-cell 12-edge icosahedron (c07/c08 selection rule);
2. the displacement responds to the *directional* broadcast imbalance — the vector/first-moment
   response — which is c05's gradient-sourcing. (Were the GP instead to respond to the *scalar* total
   incoming flux, the monopole would survive; c05 already excludes this.)

## Honest residual
- **Sub-leading anisotropy (new, separate).** The degree-6 deviation is a real lattice signature: CPP
  predicts a tiny directional/anisotropic gravity correction at 6th order in the multipole expansion.
  Irrelevant to the inert-Sea question, but a genuine (testable, far-future) prediction — flag for the
  frontier, do not pursue here.
- **(a) nonlinear GR-recovery** — whether `F` (c08 eq:F_term) assembles into `R_μν − ½g_μν R` — remains
  **the summit**, untouched. Schwarzschild cannot decide it (c08 remark).
- **Cosmological mode** — still SR-5 Step A/C, separate.

## Cap status update
Before 1107–1108 the cap was {excess-vs-absolute + shell-sum rigor + nonlinear recovery}. After this
step it is **just the nonlinear GR-recovery (a)** (+ the cosmological mode in SR-5): the entire
excess-sourcing / inert-Sea question — the cheapest kill — is now **conditionally closed and grounded
in 600-cell symmetry**, not assumed. The CC reconciliation's honest grade is unchanged (conditional on
(a)), but the conditional is now a single, well-posed GR-recovery problem.
