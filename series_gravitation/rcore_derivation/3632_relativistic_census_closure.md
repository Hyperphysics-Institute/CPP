# OPEN-GR-SHELL-DATUM-1, rung 2: the census closure made relativistic — and where it stops. Convention corrected (Kelvin's homogeneous body is k₂ = 3/4 in the corpus's Hinderer convention, not 3/2); the closure is one line, λ = −(6/5) M R̄ δ̄; everything now turns on δ̄, the level set's displacement in the LATTICE FRAME. Two bracketing identifications give k₂ = +0.033 and −0.22: the sign of the theory's Love number is a question about the static residual of the harmonic-pattern frame at the wall (F-16), not about the shell

**Patch 3632, Session 162, 5 Sep 2026.** Verify `code/3632_relativistic_census_closure_verify.py` (8/8). Reasoning `reasoning/3632.md`. Founder working postulate **P-COUNT-UNIFORM-TO-LEVEL-SET** (`founders_voice/founder_working_postulate_count_uniform_to_level_set_2026-09-05.md`). No paper touched.

## §1 A convention error in 3631 §5, corrected
The corpus's k₂ is Hinderer's. Two checks: Hinderer's closed formula equals `λ/(2R⁵)` exactly for the decaying amplitude λ of 3631 (four values, 10⁻⁹) — the far-field induced coefficient *is* the Love number; and its Newtonian limit is `k₂ = (2 − y)/(2(y + 3))`, which for the incompressible body (`y = −1`) gives **3/4**. 3631 §5's "k₂ = 3/2" was Love's convention (h₂ = 1 + 2k₂ = 5/2, same physics). **In the corpus's convention Kelvin's homogeneous body is k₂ = 3/4.** Still positive, still an order of magnitude above the family of 3631 §4.

## §2 The closure, in one line
Far field: `−(1 + g_tt)/2 = fHY/2 → v_pert = −(r²/2)Y − (λ/2)Y/r³` (the register `v = −(1+g_tt)/2` to leading order). Census of a uniform-count region (`ρ_c = 3M/(4πR̄³)`, lattice radius `R̄ = 3M/2`) whose boundary moves by `δ̄Y` in lattice coordinates: `v_ind = (3/5) M R̄ δ̄ Y/r̄³`. Equating the induced coefficients:

**`λ = −(6/5) M R̄ δ̄`**, hence `k₂ = λ/(2R⁵)`.

Check: with the *Newtonian* level set (self + layer + tide) this returns 3/4. With the R-core's level set — the lapse pin of the Einstein exterior at C = 0.375 — it returns the theory's number **once δ̄ is known in lattice coordinates.**

## §3 Where it stops: δ̄ is a lattice-frame quantity
`δ̄ = (dr̄/dr)·ξ_RW − ζ^r(R)`, with `dr̄/dr = 9/8` at the surface and `ζ` the static gauge vector from RW gauge to the lattice frame — which 3611 established is the **harmonic-pattern frame**, whose residual at the wall is the open founder question F-16 ("GPs do not move" `ζ = 0`, or the retarded pattern). This is the same residual that changed the wave-sector register content by O(1). Two brackets:

| identification | δ̄ | λ | k₂ | Λ |
|---|---|---|---|---|
| (A) `ζ^r(R) = 0` (3611's stated residual) | `(9/8)ξ_RW` | +8.97 | **+0.033** | +3.0 |
| (B) areal radius of the level-set sphere, background-mapped | `(9/8)δr_areal` | −60.4 | **−0.224** | −20 |

`k₂(ζ^r) = 0.0333 + 0.0210 ζ^r` per unit tide, with its zero at `ζ^r = ξ_RW|_{λ=0} = −1.58` — where the lattice-frame level set does not move at all and the R-core is tidally a black hole. **The residual decides the sign.**

## §4 What has been achieved and what is owed
- The shell datum of CONV-041 is no longer "the shell's constitutive law": it is **the lattice-frame displacement of the register's level set**, one number, entering a one-line closure whose Newtonian limit is Kelvin's. The stress S_ab is bookkeeping.
- Premise labelled: P-COUNT-UNIFORM-TO-LEVEL-SET (founder: working postulate, no opinion). If a surface excess exists, 3631's δσ reopens.
- **Owed — the next rung, and it is OPEN-GR-LATTICE-FRAME-1's static face:** the static ℓ = 2 vacuum perturbation of Schwarzschild in the lattice frame (harmonic-pattern gauge on the isotropic background; Φ-channel `h̄₀₀ ↔ count` per A3′ C5, τ = 0, the traceless remainder the `Q_ij` content), with the residual fixed by F-16 — and a test the census itself supplies: is `δv` *harmonic in lattice coordinates* (p = 0, 3389) compatible with the Einstein exterior at O(M·tide)? If yes, δ̄ follows and k₂ is the theory's; if not, the census and the exterior disagree at second order and that is a finding.
- GR-2 V2.2: HELD as before. PRED-O-40's falsifier ("a positive k₂") is on notice.
