# Mechanism — DM-1 (the Cross-Rod substrate dark-matter candidate)

## Overview
Dark matter is identified with **charge-neutral, color-singlet aggregates the CPP substrate already contains**
— no new field. The selected morphology is the **Cross-Rod**: a 1D rigid stack of cube-core elements, each
element four e:q:q:e hTetras fused through their central q:q edges into an 8-qCP cubic core wrapped by an
8-eCP shell (m_element ≈ 4 m_hTetra ~ 1–2 GeV). Its observable signature is a **velocity-dependent**
self-interaction that cores dwarf halos and is collisionless in clusters.

## Inputs and constants (all from prior CPP flagships; none fit here)
- DP binding energies E_eDP = 88, E_hDP = 152, E_qDP = 264 MeV (E_qDP = 3 E_eDP; E_hDP = √(E_eDP·E_qDP)) — SF-3/SF-5.
- Constituent (scattering) mass m_qDP ≈ 264 MeV; residual color = two-gluon van der Waals (hard core r_c ≈ 1.0 fm, range λ ≈ 1.3 fm, depth V₀ = f·E_qDP, f ≈ 0.2 → V₀ ≈ 53 MeV).
- Gravity G = ℏc/m_P² (zero-parameter, SR-1); emergent QM partial-wave kinematics (QM-1).

## Step-by-step mechanism
1. **Constituents → element.** qCP/eCP → qDP/eDP/hDP → hTetra (e:q:q:e). Four hTetras saturate a central qCP
   core from four sides → the cube element (color singlet by construction: 4 +qCP / 4 −qCP on interpenetrating
   tetrahedral sublattices; the eCP shell caps width and neutralizes the surface).
2. **Element → rod (genesis attractor).** Elements stack axially 4qCP-face to 4qCP-face. The competing
   glueball is the *failure branch* (a floppy ribbon folds before its core saturates); saturating from four
   sides outruns the fold → the rod. Lateral eCP capping makes width-growth a far weaker attractor
   (~190–520× electric-vs-color hierarchy) → robustly thin, fractal dimension d_f = 1.
3. **Rigidity.** Bend stiffness is a *beam* property: ℓ_p = c_geom·(E_bond/kT), c_geom the cube cross-section's
   width² lever. ℓ_p ~ 200–500 elements ≫ the band size, so the rod is rigid over its working length.
4. **Self-interaction.** Rigid rod (d_f = 1): σ/m = 0.11·N·g (N = cube-elements; g = O(1) orientation factor).
   The 0.11 floor is the per-constituent residual-color cross-section; it survives at the element level because
   the residual is **additive London polarizability**, so the 4× element mass cancels against the
   constituent-count cross-section.
5. **Velocity dependence.** Collisions deposit energy per rung; the 0860 fragmentation ledger gives ~1.95 MeV
   at cluster velocity (above the edge-bond window → fragmentation → collisionless) and ~0.78 keV at dwarf
   velocity (below it → intact rod → cores). Hence σ/m **falls with v** — the SIDM-preferred sign.
6. **No corona.** The clean spine is charge/color neutral; a bare Sea eDP reaches it only through a ~34–94 keV
   electric vdW well, ~1500× below the 88 MeV needed to bind a real eDP, and the balanced vacuum Sea supplies
   no reservoir → no σ/m-diluting coat (derived, Layer B; see OPEN-COSMO-DM-3 closure).

## Mathematical correspondence
| Physics claim | Relation | Paper §
|---|---|---|
| Self-interaction floor | σ/m = 0.11·N·g | §5 (sec:xsec) |
| Rigidity | ℓ_p = c_geom·(E_bond/kT); N ≪ ℓ_p | §5/§6 |
| Velocity split | E_dep(v) vs E_bond ∈ [0.8 keV, 2 MeV] | §5, §7 |
| Freeze-out size | N_freeze ~ √φ·exp(E_bond/2kT_form); E_bond/kT_form ~ 24–41 | §5 (genesis) |
| Corona null | V₀ ≈ 34–94 keV ≪ E_eDP = 88 MeV | §5/§6 |

## Failure modes (OPEN-* references)
- **σ/m single number:** the absolute value awaits the edge-bond depth E_bond — the **external SF-2/SF-5
  make-or-break** (scoped; shares a root with OPEN-FP-SF-2-η). Until pinned, only the band-*reachability* is established.
- **Abundance / Ω_DM:** not derived — the free primordial swirl amplitude (OPEN-COSMO-DM-1/DM-2).
- **Cosmological gate:** DM-2 (Sea gravitation / Friedmann recovery) is conditional-but-traversed, not claimed here.
