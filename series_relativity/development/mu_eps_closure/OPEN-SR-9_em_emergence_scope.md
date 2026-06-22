# OPEN-SR-9 — DP-Sea EM-Emergence & Impedance-Geometricity (Z₀) — Work-Item Scope

**Registered (scope):** Patch 2012 (21 June 2026) · **Window:** 2000-band · **Sector:** SR · **Status:** OPEN
**Provenance:** surfaced by the OPEN-COSMO-DM-2 residual-R2 arc (Patches 2002–2011) as the genuine upstream
prerequisite for R2's full closure. This file is the scoping document; the thin SR.md registration (OPEN-SR-9)
points here.

---

## Statement (what must be derived)

Derive, from the c06 microscopic substrate, **how a gapless photon (the EM field) emerges from the DP Sea** —
not as the acoustic/phonon mode of the DP lattice — and from that emergence read off the vacuum impedance
`Z₀ = √(μ₀/ε₀)` and its behavior under a Space-Stress-Vector (SSV) perturbation. Concretely, settle the
three coupled sub-questions:

1. **Emergence:** what collective excitation of the DP Sea is the photon (gapless, transverse, helicity-1),
   and what is its effective action `L = ½C P² + ½K(∇×P)² + …` with **both coefficients derived from one
   microscopic action**, not posited?
2. **VSL channel identity:** which substrate parameter does the variable-c (VSL) mechanism actually vary —
   the DP stiffness C (as 2002's c∝√C assumed), the bare Coulomb coupling, or the kinematic Planck Stepping
   Rate (PSR, as 0738/0746 describe)? Show whether these are the same channel or distinct.
3. **ε₀/μ₀ symmetry:** does that VSL channel enter the on-site polarizability ε₀ and the propagation μ₀
   **symmetrically** (→ Z₀ geometric, A=0) or asymmetrically (→ Z₀ carries the channel, A≠0)?

## Why it matters (what it gates)

- **R2 / OPEN-COSMO-DM-2 (primary):** the μ↔ε / Δc-LPI falsifier (0739/0740) reduces to "is Z₀ geometric?"
  (Δα/α = Δln Z₀; A = −dZ/dc). A geometric Z₀ ⇒ density-dependent c_eff is pure gravity, α fixed, the VSL
  horizon mechanism SURVIVES the atomic-clock LPI bound |k_α|<10⁻⁶. A Z₀ that carries the SSV channel ⇒
  k_α~O(1) ⇒ the mechanism is dead by ~6 orders. R2's leading-order K∝C is panel-CONFIRMed (2008/2009), but
  the *full* PASS is UNCONFIRMED at the action level until this item closes (2011 showed a naive action
  reproduces neither the geometric-Z₀ heuristic nor VSL).
- **c06 emission envelope / linewidth (secondary, already cross-referenced):** the same μ₀,ε₀(C,c)
  derivation feeds c06's photon coherence-length / Δν∝ν³ prediction (c06 line 185). Not make-work.
- **EU-1 / VSL horizon (foundational):** the EU-1 primordial-spectrum mechanism rests on the high-early-c_eff
  VSL horizon; this item grounds the EM-sector half of that.

## What closes it (deliverables)

- A derived EM-emergence construction: the gapless transverse helicity-1 mode of the DP Sea, with the
  effective action's electric (C) and magnetic/curl (K) coefficients from one microscopic Lagrangian.
- A decision on the VSL channel identity (stiffness vs bare-coupling vs PSR), grounded in 0738/0746/c06.
- The impedance result: `Z₀` in lattice units shown C-independent (pure 600-cell geometry → PASS) or
  C-dependent (→ FAIL), with the ε₀/μ₀ symmetry of the VSL channel established either way.
- Then (downstream, previously "conditions #1/#2"): bound the scale-dependent screening correction <10⁻⁶,
  and a round-3 adversarial panel review.

## Dependencies

- **c06** (`series_relativity/SR_companion_papers/c06_DP_chaining_as_mass_and_EM_substrate/`): the
  field-strength math B=∇×P (line 91) and the owed μ₀,ε₀(C,c) computation (line 185) live here.
- **EW-5** (`series_electroweak/papers/EW-5_*`): the emergent field-strength tensor F = ∂A−∂A.
- **0738 / 0746** (`series_relativity/development/`): the VSL/PSR mechanism definition (the channel-identity input).
- **c02**: the fixed ZBW frequency ω_ZBW (geometric) used in the inertia relation μ_DP = C/ω_ZBW².
- **2002–2011** (`mu_eps_closure/`): the virial heuristic, the shared-Coulomb-origin K∝C result, the panel
  verdicts, and the 2011 negative result that localized the residual here.

## Falsification routes / decidability

- If the derived Z₀ in lattice units comes out **∝ C** (or carries the VSL channel asymmetrically), then
  k_α ~ O(1) and the density-dependent-c_eff VSL mechanism is **falsified by ~6 orders** vs atomic-clock LPI.
- If the EM-emergence cannot produce a gapless helicity-1 mode from the DP Sea at all, the EM-substrate
  identification itself is in tension (a deeper, more serious failure).
- A PASS requires the VSL channel to enter ε₀ and μ₀ symmetrically — a specific, checkable structural claim.

## Honest framing

This is a **substantial physics task**, not a documentation cleanup. It requires EM *emergence* (a photon
from the DP Sea), which is harder than EM *propagation through* a medium and is not specified in the current
corpus at the level needed (the corpus has the field-strength math but not the emergence dynamics). It must
be done with the c06 microphysics in hand and **not by tasting** — a self-built lattice action can cancel C
by construction (the 2011 caution). Until it closes, R2 stays REVISE / leading-order-CONFIRMed.

## Cross-refs

`mu_eps_closure/R2-STATUS.md` (the R2 ladder + why this item exists); `R2-LATTICE-ACTION-ATTEMPT.md` (2011,
the negative result that surfaced it); `dp_sea_mu_eps_symmetry.md` (0740, the Z₀-geometric reduction);
`delta_c_lpi_filter.md` (0739); c06 line 185 (the owed computation); EU-1 (the VSL horizon it grounds).

NO THEO (work-item scoping; no new axiom/term/counted prediction — registration of an OPEN problem only).

---

## Progress note — Patch 2016 (first forward result; PASS-pointing)

Sub-question 1 (emergence/mode) **substantially answered** by the founder's mechanism: DP centers pinned to
GPs, the field is the internal pole-displacement wave (E=radial, B=tangential), one Coulomb binding — not the
acoustic/phonon mode the 2011 negative mis-used. Sub-question 3 (ε₀/μ₀ symmetry) **sharply advanced**: the
single-DP computation (`em_emergence/Z0-PARTITION-RESULT.md`) gives **geometric Z₀ (PASS) + varying c (VSL)**,
forced by the fixed Absolute Moment ω₀ (counterfactual with ω₀ free FAILs → not by construction). **Residual
now = one sharply-posed gate:** the symmetric emergence scheme μ₀∝α_B (as ε₀∝α_E) — derive it from the c06
EM-emergence dynamics. Sub-question 2 (VSL channel identity) **clarified**: c varies through the stiffness C
(c∝C), with the impedance ratio protected by the fixed ω₀. Then round-3 panel review.
