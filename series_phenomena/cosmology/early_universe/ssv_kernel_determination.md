# SSV kernel determination — and why the √n̄ threat is coupling-bounded (likely a phantom)

*Patch 0764, Session 154. Acts on the Stage-D physical input the Ewald spec needs: the actual CPP SSV
interaction kernel. Determines it from the corpus (the DP-Sea polarization model) and then works out what
a Coulomb kernel implies for the long-range residual — surfacing that the √n̄ "threat" that organized
patches 0756–0763 is **coupling-bounded** and almost certainly a phantom of extrapolating a weak-coupling
law into strong coupling. Script: `scripts/0764_gamma_reframing.py`. **This is a CPP-side analytic result
offered to the panel for scrutiny; not self-certified. NO THEO.**

## 1. The kernel (solid, from corpus)

SSV = **Space Stress Vector** = the net electromagnetic/gravitational field at each lattice point
(`master_glossary.md`). The CP–CP interaction is how that field from one CP acts on another. The corpus
fixes its form in `series_foundations/dp-sea-polarization/DP-Sea-Polarization-Model.tex`: the steady
repulsion between an unpaired CP and the same-charge moiety is **Coulomb-like**,

  F_rep(v,r) = (k_e q₀²/r²)·(1 + κ_q P(v,r))²·(ω/ω₀)·(d₀/d_min)²,

i.e. a **1/r² force (1/r potential)** modulated by the DP-Sea polarization P(v,r). For the tilt's static
occupation problem P ≈ 0 (slow/static CPs), so the bare kernel is **Coulomb, V(r) ∝ q²/r**. The DP-Sea
(bound dipoles) acts as a dielectric background — it renormalizes k_e (an effective ε) but **preserves the
1/r form** (bound dipoles give a dielectric constant, not Yukawa screening). Mobile ± CPs in the early
plasma self-screen (Debye) — but that self-screening *is* the Debye–Hückel mechanism the Ewald test
targets, not an external rescue. **Kernel = Coulomb 1/r. Confidence: solid.**

## 2. What a Coulomb kernel implies — the residual is governed by Γ, not √n̄

For a Coulomb plasma the Debye–Hückel excess chemical potential is, in dimensionless form,

  μ_excess/kT = −c·Γ^{3/2}   (c = O(1); OCP limiting law c = 1/√3),

where **Γ = q²/(a·kT)** is the plasma coupling at the inter-particle spacing a = n^{−1/3}. Writing
a = n^{−1/3} turns this into the "√n" form, μ_excess/kT = −c(q²/kT)^{3/2}√n, so the spec's coefficient is
B ≡ c(q²/kT)^{3/2} and therefore

  **B·√n̄ ≡ |μ_excess|/kT ≡ c·Γ^{3/2}.**

The "√n̄" and the coupling Γ are not independent — B·√n̄ *is* c·Γ^{3/2}.

## 3. The √n̄ threat is a phantom

Within the Debye–Hückel regime of validity (Γ ≲ 1), B·√n̄ = c·Γ^{3/2} ≲ 0.58. **It can never reach
ln n̄ ≈ 170.** The "B·√n̄ ~ 10³⁷" scare came from holding q²/kT at an O(1) value and multiplying B by
√(10⁷⁴) = 10³⁷ — but at n̄ = 10⁷⁴ with q²/kT ~ 1, the coupling is Γ = (q²/kT)·n̄^{1/3} ≈ 5×10²⁴, i.e.
**deep strong coupling, where the DH formula that defines B is invalid.** The threat was an extrapolation
of a weak-coupling law into the strong-coupling regime. Reduced to the honest dimensionless invariant Γ,
the Debye √n̄ residual is bounded by ~Γ^{3/2} and cannot threaten the tilt (script §"THE PHANTOM").

This also resolves the 0757 corner cleanly: 0757 noted the √n̄ survives to 10⁷⁴ only if kT/q² ≳ 10²⁴·⁷
(absurdly weak coupling). But in *that* regime Γ ≪ 1 even at 10⁷⁴, so μ_excess/kT ~ Γ^{3/2} ≪ 1 — the
residual is present but dimensionless-tiny. **There is no regime in which the √n̄ is both present and
large.**

## 4. The only genuine residual, and why CPP passes

The residual reaches ln n̄ ≈ 170 only at Γ ~ 44 (DH form, already outside DH validity) or Γ ~ 190
(strong-coupling Madelung). So the **only** genuine threat is a *strongly coupled* plasma (Γ ~ tens–
hundreds: a correlation energy of tens–hundreds of kT per CP). That is a different functional form
(n^{1/3} Madelung, not √n), and charge neutrality (0756) suppresses it further.

CPP's early CP plasma is the opposite of that. A hot, **relativistic** charged plasma has kT ~ ℏc/a, so

  Γ = q²/(a·kT) ~ (e²/4πε₀)/(ℏc) = α ≈ 1/137 ≈ 0.007  (**weak coupling**),

giving |μ_excess|/kT ~ c·α^{3/2} ~ 3.6×10⁻⁴ ≪ ln n̄ ≈ 170 — PASS with ~5 orders of margin. On top of
this: on-GP stacking is a **contact** interaction (A1: no sub-GP space → no √n at all, 0757), and charge
neutrality cancels the leading mean-field (0756).

## 5. Confidence and the one model-dependent input

- **Kernel = Coulomb 1/r:** solid (corpus, DP-Sea model).
- **B·√n̄ = c·Γ^{3/2}; the √n̄ is coupling-bounded; the phantom diagnosis:** solid (standard plasma
  physics; verified numerically in the script).
- **The only genuine threat is strong coupling (Γ ~ tens+):** solid.
- **CPP's early plasma is weakly coupled (Γ ~ α):** this is the one input that imports the standard
  relativistic-plasma expectation (kT ~ ℏc/a) rather than being read directly off the CPP corpus. It is
  physically natural for a hot early CP plasma, but the precise Γ depends on CPP's emergent EM coupling
  and the ZBW ("temperature") scale. **This is the part to confirm.** To FAIL, CPP's early plasma would
  have to be pathologically strongly coupled (Γ ≳ tens), opposite to the relativistic expectation.

## 6. Consequence for the Ewald spec (Stage D reframed)

Stage D should not "measure B and extrapolate B·√n̄ to 10⁷⁴" (the phantom-prone framing). It should
**report μ_excess/kT as a function of Γ** and confirm it stays ≪ ln n̄ — which the identity in §2
guarantees for any non-pathological Γ. Stage A (reproduce DH) and Stage B (the crossover n_* — which *is*
the Γ = 1 line) already probe exactly this. The decisive physical input from CPP is now reduced to a
single number: **the coupling Γ of the early CP plasma** (expected ~α). A short reframing note is added to
the spec (§9), marked as a CPP-side analytic result pending panel review.

## 7. Status

This very likely **closes the long-range corner on the PASS side**: the kernel is Coulomb, the √n̄
residual is coupling-bounded (a phantom), the only real threat is strong coupling, and CPP's early plasma
is weakly coupled (Γ ~ α) — so μ_excess/kT ≪ ln n̄ with large margin, reinforced by neutrality (0756) and
the contact-interaction on-GP result (0757). **Per programme discipline this is not self-certified:** the
reframing (and especially the Γ ~ α estimate) is handed to the panel for scrutiny, and the recommendation
is that Stage A + Stage B numerically confirm μ_excess/kT ~ Γ^{3/2} stays ≪ ln n̄ before the
axiom-dissolution + prediction (n_s = 0.9649) are registered. NO THEO yet.

## Pointers

- Script: `scripts/0764_gamma_reframing.py` (the identity + the phantom + the CPP estimate).
- Kernel source: `series_foundations/dp-sea-polarization/DP-Sea-Polarization-Model.tex`.
- Builds on 0757 (analytic crossover = the Γ=1 line), 0756 (neutrality), 0759 (the spec).
- Reasoning: `reasoning/0764_ssv_kernel.md`.
