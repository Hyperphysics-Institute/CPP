# C2R-L1 PREREG (FROZEN) — leading-order derivation: from the every-Moment response rule to the homogenized screening closure, deriving the per-site response strength α rather than imposing it

**Patch 2769, 22 July 2026. Charter: `fa_c2_rederivation_charter.md`
§2 (C2R-L1). Frozen before execution. Reasoning: `reasoning/2769.md`.**

## Route (committed)

1. **Linear response of a Sea site.** From the 2767 ontology inputs
   (F3): each site responds every Moment to the total static
   potential ψ at its GP; time-averaged induced source strength
   q_i = −α ψ(r_i), α the per-site static response strength
   (dimension: length, in the arc's convention). Linearity at weak
   bias is the leading order by construction.
2. **Self-consistency and homogenization.** ψ(r) = ψ_ext(r) −
   Σ_j α ψ(r_j)/|r − r_j|. With the core OCCUPIED (2767 — no
   exclusion region anywhere), homogenize the sum to
   ∫ n α ψ(r′)/|r−r′| d³r′ and reduce to the screened equation
   (−∇² + κ²)ψ = 4πQδ³ with **κ² = 4π n α**.
3. **The closure inverted.** At fixed κ and n, α = κ²/(4πn) is the
   UNIQUE homogenized closure — the continuum matching is derived,
   not chosen. Evaluate at the frozen operating point (κ = 2/a,
   FCC n = √2/a³, a = 0.589/φ fm) and compare with the imposed
   α = a/(π√2).
4. **Discreteness accounting (sets up L2).** Compute S_cont = 1/α
   and S_disc = Σ_{j≠0} e^{−κr_j}/r_j by direct FCC lattice
   generation; decompose S_cont − S_disc into the r < a core-medium
   contribution 4πn[1−(1+κa)e^{−κa}]/κ² and the outer
   discrete-vs-continuum residual. Identify the L4 record's "59%
   self-exclusion" with the core-medium fraction 1 − 3e^{−2} and
   restate its status under the 2767 ruling.

## Decision quantities (frozen; feed charter §3)

- **D1 = |α_derived/α_imposed − 1|** at the operating point;
  charter threshold 5%. (Derivation-identity outcome D1 = 0 is
  anticipated and is a RESULT, not a triviality: it certifies the
  matching as the unique occupied-core closure.)
- **D2 = ℓ_LO** = the frozen operator's committed robustness
  envelope at the derived α (no re-run owed if D1 = 0: same α, same
  operator, same envelope 0.0904 ± 0.0028 fm).
- Honesty bound (committed): L1 does NOT derive κ·a = 2 itself nor
  the per-site stiffness behind it — that remainder is named
  KINETIC-1-adjacent and does NOT constitute C2R-OBSTRUCTED, because
  the chartered L1 objective is the α↔κ closure, which closes.

## Verify script (committed spec)

`code/2770_c2r_l1_closure.py`, deterministic, no seeds: evaluates
α = κ²/(4πn) symbolically-numerically, generates the FCC lattice to
convergence for S_disc, computes the decomposition, prints D1 and
every quoted quantity. All record numbers quote script output.
