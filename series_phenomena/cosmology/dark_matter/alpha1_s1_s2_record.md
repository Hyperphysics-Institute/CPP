# OPEN-DM-ALPHA-1 S1+S2 RECORD — the polarizability bridge derived from the founder's statistical mechanism: **D1 = CHI-STRUCTURED** (local continuous kernel at k→0 with genuine O(Γ) ≈ 20–25% pair-correlation structure at d_DP scale; Γ = 1/(√2π) = 0.225); **D2 = the continuum matching α = κ²/4πn is DERIVED as the long-wavelength coefficient**, and α′ is identified as a discretization conflation (the r<a exclusion over-excludes even on its own terms: proper self-cell = 30.3%, not 59.4%); the θ scale component is **CHI-INCOMPLETE** pending the founder's answer on the agitation width

**Patch 2701 (this record + verify script), 21 July 2026. Executed
under the frozen 2698 charter, stages S1→S2, from the ten founder
commitments (2697 §3 + 2700 §2) and registered inputs only. Verify:
`code/2701_alpha1_s1_s2_derivation.py` (all closed-form; output quoted
below verbatim). No grade, cap, rider, or class motion from inside the
arc; the D2 branch recommendation routes to the CONV-001 packet (2703).
79.5% not in scope.**

## §1 — S1: the kernel, from the mechanism

The Sea is a two-species (±) CP field on GPs; each CP's Moment update
follows the TOTAL SSV_net (commitment 2); pairing is transient
(commitment 1); the bias response is a time-averaged occupation shift
(commitments 4–5); self-exclusion is at GP/superposition scale,
point-like (commitment 3). Linearizing the time-averaged occupation
against a static potential φ with agitation width θ:
δn_± = ∓(n_± q/θ)φ_tot, giving induced charge ρ_ind = −(n_CP q²/θ)φ_tot
and the self-consistent field equation

  φ_tot(r) = φ_ext(r) − (κ_D²/4π) ∫ φ_tot(r′)/|r−r′| d³r′,
  κ_D² = 4π n_CP q²/θ.

**The kernel is LOCAL and CONTINUOUS at leading order** — a Debye-type
density response — with validity governed by the coupling
Γ = q²κ_D/θ: pair-correlation (structured) corrections at the
inter-particle scale d_DP enter at O(Γ). With the S2 reconciliation
value Γ = 1/(√2π) = 0.2251 (§2), those corrections are ≈ 20–25% —
small enough that the local kernel leads, large enough that d_DP-scale
structure is genuine. **D1 = CHI-STRUCTURED** under the frozen classes:
locally continuous k→0 limit, real structure at the DP spacing.

## §2 — S2: the α bridge, the reconciliation, and the θ gap

**Discretizing the integral equation** on sites of density n_DP
(∫ → Σ_j /n_DP) yields φ_i = φ_ext,i − (κ_D²/(4π n_DP)) Σ_j φ_j/r_ij —
i.e. the registered operator M = I + αG with

  **α = κ_D²/(4π n_DP)** — the continuum matching, now DERIVED as the
  k→0 coefficient of the statistically continuous medium
  (= 0.08193374 fm at κ_D = κ). This is the derivation the R1 panel's
  Q3 ruling demanded (GPT: "long-wavelength matching … requires a
  derivation showing that the relevant uniform mode samples the
  continuum susceptibility"): under the founder's mechanism the medium
  IS continuous in the time average, so the uniform mode samples it by
  construction.

**The α′ audit.** The site sum with G_ii = 0 drops the self-cell's
share of the continuous response. Verified closed-form: the screened
Wigner–Seitz self-cell (R_ws = 0.5527a) carries 30.29% of S_cont; the
L4 construction excluded r < a = 59.40% — over-exclusion even as a
discretization argument. Under commitment 3 (exclusion is GP-scale,
point-like) the physical medium responds inside the cell, so α′ = 1/S_disc
= 0.1320 fm conflates (i) exclusion of response the medium possesses
with (ii) lattice-discreteness error. **D2: the derivation selects the
continuum branch; α′ is reclassified (recommendation, panel property)
from "alternative normalization" to "discretization diagnostic."** The
α^(−1/2) law remains struck.

**Reconciliation with S1c (frozen requirement).** Imposing κ_D = κ =
2/d_DP DEFINES the agitation scale rather than testing it:
θ_implied = 4π n_CP q²/κ² = **2√2π q²/a = 24.410 q²/fm** — order the
CP–CP Coulomb energy at DP spacing (8.886 × q²/a). Whether this is the
mechanism's own scale is a physics question now WITH the founder
(posed 21 July); until answered, the numerical closure is
**CHI-INCOMPLETE on the θ component** — the kernel FORM and the
matching STRUCTURE stand independently of it, exactly as the charter
anticipated. If the founder supplies an independent scale, the
reconciliation converts from definition to test; agreement would be a
lock (reported, not elevated — non-elevation clause extended here by
charter §3).

## §3 — Verify output (committed verbatim)

Script output, 21 July 2026 run: a = 0.3640220 fm; κ = 5.4941731 /fm;
n_DP = 29.3178443 /fm³; n_CP = 58.6356886 /fm³; α_cont = 0.08193374 fm;
θ_implied = 24.4099681 q²/fm (= 2√2π q²/a identity); Γ = 0.2250791;
R_ws = 0.2011839 fm (0.5527a); self-cell fraction 0.3029251 vs r<a
fraction 0.5939942; S_cont = 12.204984 /fm vs committed S_disc =
7.576067 /fm; S_cont(1−f_cell) = 8.507788 /fm; κ·d_DP = 2.0000.
Reasoning: `reasoning/2701.md`.
