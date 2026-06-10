# Deriving the three Era-2 inputs from the CPP corpus — two firmed, one scoped, one corpus inconsistency flagged

**Patch:** 0833 (Session 156, 10 June 2026) · **Type:** grounding / derivation pass (no verdict, no THEO/ID). · **Lane:** DM-2 / `dark_matter/`.
**Resolves first-pass:** the three inputs the 0830–0832 arc kept pointing back to — m_qDP, the residual fraction f, the qDP statistics. **Verify:** `code/0833_required_inputs_derivation.py`.

---

## Input 1 — qDP constituent mass: ratio derived, scale firmed, an appendix inconsistency surfaced

The mass-generation **mechanism** is c04 (`c04_ZBW_hbar_mass_units`): rest mass is the energy of one complete Compton standing-wave (ZBW) resonance cycle, `mc² = ℏν_C`, derived from boundary conditions rather than assumed. c04 supplies the *form*; the *scale* comes from the DP-Sea binding energies. The DP-Sea appendix gives `E_eDP = αℏc/(φl_p) ≈ 88 MeV` and `E_qDP = 3·E_eDP ≈ 264 MeV`, the factor 3 being the color factor.

**The clean, load-bearing part is the ratio:** `E_qDP/E_eDP = 3` (color factor), giving **m_qDP ≈ 264 MeV** — consistent with Step-1's 0.30 GeV estimate, and a derived *ratio* rather than a guess.

**The inconsistency I must flag:** the appendix states `r_min = φ·l_p ≈ 2.61×10⁻³⁵ m` (the golden-ratio-scaled *Planck* length), but `αℏc/(2.61×10⁻³⁵ m) ≈ 5.5×10¹⁹ MeV`, not 88 MeV — off by ~6×10¹⁷. The quoted 88 MeV instead requires `r_min ≈ 0.016 fm = 1.6×10⁻¹⁷ m`, eighteen orders of magnitude larger than the Planck length. So the *absolute* eDP/qDP scale does **not** follow from the Planck length as written; it traces to an `r_min ≈ 0.016 fm` scale that the appendix mislabels. **m_qDP ≈ 264 MeV stands as a scale-calibrated value (matched to the constituent/QCD scale via E_eDP=88), not a clean Planck-derived one.** This appendix line should be reconciled (separately, in the DP-Sea paper).

Impact: using the derived **264 MeV** (vs the 0.30 GeV estimate) raises σ/m by ~14% (σ/m ∝ 1/m): realistic-f 0.17 → 0.19, worst-case-f 0.50 → 0.57 cm²/g — both still safely below the SIDM bound. The collisionless conclusion (0831) is unchanged.

## Input 3 — qDP statistics: bosonic, but too quantum to self-bind → diffuse, on firmer ground

c04 and the DP-Sea spin table attribute a **fermion ZBW (spin-½)** to the bare Conscious Point. A qDP is a bound +qCP/−qCP pair — two spin-½ fermions — hence an **integer-spin boson**. So the cold DM medium is a system of identical **bosonic** hard-core particles (a He-4-like quantum fluid), *not* the free Fermi gas that was the most-bindable bracket in 0832.

This initially looks like it *reopens* the nugget question — a Bose system has lower kinetic and is more bindable. But the right diagnostic is the **de Boer quantum parameter** `Λ = ℏc/(r_c√(m·ε))`, ε = well depth = f·E_qDP. Liquid He-4 self-binds at Λ ≈ 0.18; only Λ ≲ 0.5 self-binds at all. For the qDP:

| f | ε [MeV] | Λ | |
|---|---|---|---|
| 0.05 | 13 | 3.34 | diffuse |
| 0.10 | 26 | 2.36 | diffuse |
| 0.50 | 132 | 1.06 | diffuse |
| 1.00 | 264 | 0.75 | diffuse |

Across the entire physical depth range, **Λ ≈ 0.75–2.4 — far above the He-4 self-binding regime.** The light qDP medium is too quantum (zero-point dominates the attraction) to condense into a self-bound liquid; it stays a **diffuse gas**. This *restores* 0832's diffuse conclusion, now on the correct (bosonic) statistics rather than the Fermi bracket. A self-bound nugget phase would require Λ ≲ 0.2 — a much heavier and/or deeper system (hTetra-scale at ~1.5 GeV with deep attraction), **not** the qDP — which is a clean, concrete falsifier/boundary rather than a hand-wave.

## Input 2 — residual fraction f: bounded and estimated, not yet CPP-derived (scoped)

f is bounded above structurally: f < 1 (the residual color attraction is the van-der-Waals **residue** of the qDP's own color binding E_qDP, weaker than its source — the same hierarchy that excludes the 0831 resonance and keeps the medium below the Fermi self-binding threshold). The realistic value f ~ 0.05–0.2 is by **analogy** (the nuclear force is ~5–20% of the constituent binding; molecular van der Waals is ≲1% of the chemical bond) — not yet a CPP derivation.

Deriving f from CPP requires the **qDP color polarizability**: from the qCP separation (`r_min`) and the color coupling, compute the induced color-dipole moment and the leading van-der-Waals/London `−C₆/r⁶` coefficient between two neutral qDPs, evaluated at contact. The corpus fixes the inputs (qDP size ~λ_qDP, the color factor, the Cornell inter-quark potential with σ ≈ 0.9 GeV/fm) but does not yet assemble the neutral-neutral residual. This is the one genuinely open derivation, and it is scoped — a real calculation, not a free parameter. The arc's conclusions are robust to it: collisionless holds for all f ≤ 1 (0831), and diffuse holds across all f by the de Boer parameter (Input 3).

## Net

Two of three inputs firmed: **m_qDP ≈ 264 MeV** (color-factor-3 ratio; consistent with the estimate; absolute scale flagged) and the **statistics** (bosonic, but de Boer Λ ≈ 0.75–2.4 ⇒ robustly diffuse). The third, **f**, is bounded (< 1) and estimated (~0.05–0.2), with its CPP derivation scoped to the qDP color polarizability. The Era-2 conclusions — glueball-avoidance, σ/m-safe, diffuse CDM — now rest on three corpus-grounded facts: the color factor 3 (mass), the residual-force hierarchy f < 1 (collisionless), and the de Boer quantum parameter (diffuse despite bosonic statistics). Remaining open work: the f color-polarizability derivation, and reconciling the DP-Sea appendix mass-scale line.

## Scope

Grounding / derivation pass against the corpus. **No closure, no THEO/ID, no verdict.** Flags a numerical inconsistency in the DP-Sea appendix (for separate reconciliation in that paper). de Boer estimate uses representative `r_c = 1.0 fm`; identical-particle statistics and the precise hard-core scale remain refinements. Conditional on the qDP/hTetra-DM conjecture and the Mechanism-A measure.
