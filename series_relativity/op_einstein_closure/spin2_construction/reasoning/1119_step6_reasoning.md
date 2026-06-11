# Reasoning capture — Patch 1119 (Step 6, the third assault: non-radiality connection re-run)

**Protocol:** `templates/reasoning_capture_protocol.md`. Verbatim reasoning from the Opus
session, Session 156 lane (band 11xx), 11 June 2026. Companion to
`1119_step6_nonradial_connection_rerun.md` + `code/1119_step6_connection_covariant_modes.py`.

---

## The architect's prompt (the mechanism, in Thomas's words)

> "The four-dimensional nature of the 600-cell, and the fact that every GP has 12 GPs as
> nearest neighbors, which requires an incremental turn to choose each one, meaning that
> regardless of how far out the PSR (Planck Sphere Radius) l_P, there will be an element of
> rotation involved in it because the GPs in the 600-cell are not inherently radial. This is a
> twist that we did not consider in our run-up against the Einstein GR wall. Can we rerun that
> using the concept of the GP's non-radiality? ... showing that there is an angular element,
> however small, in the radial extension of the GP-GP message at full PSR ... an element of
> tangential/spin displacement associated with each PSR increment in the traversal of the GW
> across many light-years, which could be the source of the detected GW signal."

## Step 0 — was this actually untested? (the audit that justified the run)

Re-read `code/1116_step5_emergent_graviton_modes.py` before anything else. The 1116 dynamical
matrix couples neighbors via `λ δ_ab + μ n_a n_b` — scalar coefficients only. There is **no
per-edge rotation operator anywhere in 1116**. The path geometry enters only through the phase
factors `e^{ik·n_j}` (which neighbor, at what offset), never as a transport acting on the
carried components. So the architect's mechanism — the hop *turning the data* — was genuinely
outside the verdict's coverage. The third assault was well-posed, not a re-litigation.

## Step 1 — formalization choice

The twist mechanism is exactly a **discrete connection**: per-edge transport `R_j` applied to
the carried data on each hop. Key choices and why:

- **Antipodal consistency `R_{−j} = R_jᵀ`** (hopping back undoes the turn): required for the
  dynamical matrix to be Hermitian, and physically necessary (a round trip along one edge must
  be the identity, else the "spring" energy is ill-defined).
- **Equivariant family:** for the lattice to remain homogeneous/isotropic under the icosahedral
  point group, the per-edge axis must be constructed from the edge data itself; the only vector
  available per edge is `n_j`, so the equivariant connections are `R_j(θ)` = rotation about
  `n_j` by θ — a one-parameter family. The geometric value, if data were transported
  quaternionically along a 600-cell edge (36° subtended on S³), is θ = π/5.
- **Generality backstop:** also test arbitrary per-edge SO(3) rotations (200 random
  antipodal-consistent draws) and note the O(4) generalization analytically, so the conclusion
  does not hinge on the equivariance assumption.

## Step 2 — the prior, stated before running (the structural argument)

Expected the verdict to survive, for one reason: **rotations preserve rank.** The carried
space `(φ, V)` is 4-dimensional with J_z spectrum {0,0,±1}; the helicity-±2 projector on it is
identically zero; transports are rotations, hence irrep-preserving — they redistribute a
vector's components but cannot manufacture a 5-component symmetric-traceless object from 4
components of data. Secondary physical argument: the twist is *static* (a property of the
channel); the GW strain oscillates at the source frequency; a fixed channel twist can rotate /
birefringe what was sent but cannot add first-order oscillating rank-2 content never radiated.
Stated to the architect in advance; the run was committed regardless of the prior (three
payoffs identified: strongest justification plank if it survives; quantified byproduct either
way; pivot if wrong).

## Step 3 — the analytic spine (derived before coding, confirmed numerically)

1. **Gap at k=0.** `Σ_j R_j(θ)`: each `R_j = cosθ·I + (1−cosθ)·n_jn_jᵀ + sinθ·[n_j]_×`.
   Sum over the shell: `Σ n_jn_jᵀ = 4I` (12 unit vectors, isotropic), `Σ [n_j]_× = 0`
   (antipodal pairs). So `Σ R_j = (12cosθ + 4(1−cosθ))·I = (8cosθ+4)·I`, giving
   `D(0) = (12 − 8cosθ − 4)·I = 8(1−cosθ)·I = 16 sin²(θ/2)·I`. **A nonzero twist gaps the
   vector modes at M = 4|sin(θ/2)| Planck masses.** (Numerically confirmed to 6 digits at five
   θ values.)
2. **O(k) chiral term.** Expanding `Σ R_j(1 − e^{ik·n_j})` to O(k): the cosθ·I piece gives
   `Σ(k·n_j) = 0` (odd); the `(1−cosθ)n n^T` piece is odd → 0; the `sinθ[n_j]_×` piece is
   odd×odd = even → survives: `−i sinθ [Σ n_j(n_j·k)]_× = −4i sinθ [k]_×`. Eigenvalues on the
   transverse doublet: `±4 sinθ·k` → `ω²_± = M² ± 4 sinθ·k + c²k²` — circular birefringence.
   Crucially `[k]_×` *is* the J_z generator: the chiral term is m-diagonal, splitting ±1 but
   moving nothing toward ±2. (Numerical splitting/k = 2.3642 vs formula 8 sinθ = 2.3642 at
   θ=0.3.)
3. **The bound.** χ(α) = 2+2cosα; ∮χ(α)e^{−2iα}dα/2π = 0 exactly (numerically 1.4×10⁻¹⁶).

## Step 4 — what the numbers said

- m=±2 weight across all branches, all θ in the equivariant family: ≤ 9×10⁻¹⁶ (machine zero).
- 200 random antipodal-consistent SO(3) connections, helicity measured about random k̂:
  max m=±2 weight 2×10⁻¹⁵ (machine zero).
- Empirical θ bounds from the gap: photon (m_γ < 10⁻¹⁸ eV) → θ < 4×10⁻⁴⁷; graviton
  (m_g < 1.2×10⁻²² eV) → θ < 5×10⁻⁵¹. Geometric θ = π/5 → M = 1.236 Planck masses.

## Step 5 — the interpretive turn (the result that wasn't in the prior)

The run produced something better than a mere survival of the verdict: **the absolute (Nexus)
frame is revealed as load-bearing.** The dichotomy is sharp: either (i) the broadcast data is
carried in the universal lattice frame (R_j = I; CPP-native, since the Nexus frame is
axiomatic) — in which case 1116's calculation was already exactly right; or (ii) the data is
parallel-transported through local edge frames — in which case the vector sector is
Planck-massive (at the geometric θ=π/5, M ≈ 1.24 M_Planck) and long-range gravity/EM dies. The
observed masslessness *forces* (i) to one part in 10⁴⁶. So the architect's twist intuition,
run to ground, converts the absolute-frame axiom from background ontology into an empirically
necessary structural feature. The non-radiality is real — but it lives in the path (which
neighbor, already in 1116's phases), not in the payload.

Also noted, fenced as DIRECTION not claim: the chiral O(k) term is a natural substrate-
chirality order parameter with a now-known empirical ceiling (10⁻⁴⁶–10⁻⁵¹) — a potential
future hook for the chirality lane. No cross-lane file touched.

## Discipline notes

- One bug in-session: numpy 2.x renamed `trapz` → `trapezoid`; fixed, no physics content.
- NO VERDICT MOVED: no THEO/PRED/ID registered, no count change. Private-lane paths only
  (spin2_construction/ + parent INDEX/README, owned subtree). No contested file touched.
- Falsifier honored: had any connection produced a nonzero m=±2 weight or a fifth branch, the
  step document would have reported a pivot to the emergent route, not a survival.
