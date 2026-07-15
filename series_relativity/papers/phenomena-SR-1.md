# Phenomena — SR-1: Mechanistic Derivation of Relativistic Effects via SSV in the Dipole Sea

**Paper:** SR-1_special_relativity_emergence.tex
**Last updated:** 15 July 2026 (Patch 2480 status correction; content baseline v17, 26 March 2026)

> **CORRECTION BANNER (Patches 2471–2475, SR-1 triage — read before any entry below).**
> The 2471–2475 triage established: k is a normalisation convention, not a derived constant
> (α cancels identically in k·ΔSSV; the dimensional-necessity argument is withdrawn); γ enters
> as an INPUT via the ΔSSV normalisation (App. A.8.1), so γ_CPP = γ_SR is an identity by
> construction and admits no deviation; the five acceleration-scaled predictions and the muon
> bound are WITHDRAWN (the claimed deviation k·ΔSSV IS γ−1, double-counted; every ΔSSV
> definition is velocity-dependent and no derivation bridges to acceleration); the Monte-Carlo
> "machine-precision confirmation" citations are WITHDRAWN (the cited scripts were stubs);
> and the Geometric Insufficiency Theorem (App. H.1) is DEMOTED to a three-model Proposition.
> Entry-level statuses below are corrected accordingly; original claims are preserved struck
> or quoted so the correction is legible.

SR-1 is a different kind of paper from SS-1 or the SM series. Those papers derive new algebraic structures or mass ratios from CPP geometry. SR-1 gives a mechanical account of special relativity — and, post-triage, its honest billing is: the lattice framework reproduces SR **exactly by construction** (the γ content is supplied through the ΔSSV normalisation), with the geometry contributing the displacement-budget structure and functional form. It is a mechanism-and-consistency paper, not a prediction paper; it currently has zero falsifiable predictions (OPEN-SR-EPSILON carries the physical debt; OPEN-SR-H1-CLASS carries the reopened route).


## Section 1: Explained Phenomena (PHEN-E)

### PHEN-SR1-E1. Time Dilation — Clocks Run Slow in Moving Frames

**Observation:** Moving clocks run slow by the factor γ = 1/√(1−v²/c²). This is confirmed by muon lifetime measurements, atomic clock comparisons on aircraft and satellites (Hafele-Keating, GPS), and particle accelerator decay rates. It is one of the most precisely tested predictions in all of physics.

**CPP account:** Any physical clock requires a cyclic process that accumulates a fixed total displacement D to complete one tick — one oscillation of an atom, one heartbeat, one electronic cascade. Each Absolute Moment contributes PSR_eff = l_P/(1+k·ΔSSV) to this accumulation. When ΔSSV > 0 (particle is moving), PSR_eff < l_P, and each Moment contributes less to the accumulation. More Absolute Moments are therefore needed per clock tick: N = D/PSR_eff = N₀ × γ. Every physical process slows by exactly the same factor γ because all use the same displacement budget. The absolute Moment rate is universal — only the per-Moment displacement magnitude varies.

**SR-1 element:** Appendix B (Time Dilation Mechanism), §A.6


### PHEN-SR1-E2. Length Contraction — Moving Objects Are Shortened

**Observation:** Moving objects are contracted along the direction of motion by the factor 1/γ. This is observed in relativistic heavy-ion collisions (Lorentz-contracted nuclei) and required for the consistency of electromagnetism (force transformation laws).

**CPP account:** Bulk velocity v consumes fraction f = v/c of the displacement budget. The remaining spatial extent of the CP aggregate along the direction of motion is reduced by the same factor as the PSR: L' = L₀/γ_CPP = L₀/(1+k·ΔSSV). Length contraction is the spatial consequence of the same Voronoi budget constraint that produces time dilation — not a separate postulate, but the same mechanism applied to spatial rather than temporal extent.

**SR-1 element:** §3 (Main Results)


### PHEN-SR1-E3. The Twin Paradox — The Travelling Twin Is Younger

**Observation:** A traveller who leaves Earth at high velocity, turns around, and returns is younger than the twin who stayed behind. This is confirmed by the Hafele-Keating experiment (1971), GPS clock corrections, and muon storage ring experiments. The result is asymmetric despite the apparent symmetry of relative motion.

**CPP account:** The stay twin accumulates ΔSSV ≈ 0 throughout — inertial motion, PSR_eff ≈ l_P, clocks tick at the normal rate. The travel twin accumulates nonzero ΔSSV during acceleration phases (outbound, turnaround, return). ΔSSV accumulation is a frame-independent physical fact — it marks the worldline of whichever twin undergoes acceleration. The age difference at reunion:

    Δt_age = ∫₀ᵀ (γ_SR(τ) − 1) dτ

is nonzero for any non-inertial path and exactly zero for any inertial path. The asymmetry requires no appeal to relativity of simultaneity; it is the direct physical consequence of asymmetric ΔSSV accumulation along the two worldlines.

**SR-1 element:** §A.6 (Twin Paradox), Fig. 4


### PHEN-SR1-E4. The Speed of Light as an Absolute Limit

**Observation:** No massive particle has ever been observed travelling at or above c. Accelerator experiments confirm that additional energy input produces increasing momentum and kinetic energy but the velocity asymptotically approaches c without reaching it. Light (photons, massless particles) travels at exactly c.

**CPP account:** Theorem A.8.2: c = l_P/t_P is the maximum CP propagation speed, proved from the Voronoi insphere geometry. In the unstressed lattice (ΔSSV = 0), a CP executing a pure spatial step achieves |Δx| = l_P in time t_P, so v = l_P/t_P =: c. Under stress (ΔSSV > 0), PSR_eff < l_P and v_max < c. As v → c, ΔSSV → ∞ and PSR_eff → 0: the lattice brings any CP to rest relative to internal resonances before it reaches c. Massless particles (photons, gluons — open-path DP modes) propagate at exactly c because they are not localised CP aggregates and do not accumulate the cage binding energy that would produce ΔSSV.

**SR-1 element:** Theorem A.8.2 (Speed Limit)


### PHEN-SR1-E5. Lorentz Covariance — Physics Is the Same in All Inertial Frames

**Observation:** All the laws of physics are the same in every inertial reference frame. No preferred direction or preferred frame has been detected in any experiment (Michelson-Morley and successors). The laws of electromagnetism, the weak force, and the strong force are all Lorentz-covariant.

**CPP account:** Lorentz covariance is derived from H₄ symmetry (Appendix C.2), not postulated. The 600-cell Coxeter group H₄ acts transitively on all 120 vertices; by Schur's lemma the second-moment tensor of all vertex vectors equals (1/4)δμν — the unique H₄-invariant rank-2 tensor is the identity, identical to the SO(4)-invariant tensor. Every macroscopic observable averaged over one 600-cell motif is isotropic. Analytic continuation of the timelike Absolute Moment direction then converts SO(4) isotropy to SO(3,1) Lorentz symmetry. No preferred direction is detectable at any scale L >> l_P; discreteness corrections enter only at order (l_P/L)² and are unobservable in all current experiments.

**SR-1 element:** Appendix C.2 (Lorentz Covariance from H₄ Symmetry)


## Section 2: Novel Predictions (PHEN-P)

### PHEN-SR1-P1. Time-Dilation Deviation at ~10²⁰g

**Prediction:** At sustained accelerations of order a ≈ 10²⁰g, a fractional deviation from the standard SR time-dilation prediction of order δ ~ 10⁻²⁰ is expected. This arises from the saturation of the Voronoi displacement budget at Planck-scale stress levels.

**Observable:** An atomic clock subjected to 10²⁰g for 1 ms in a laser-driven plasma accelerator or extreme centrifugal field would show a > 5σ discrepancy from standard SR while remaining fully consistent with CPP.

**Falsifiability:** A null result at 10²⁰g sensitivity would require k to differ from l_P³/E_P by a factor of 10²⁰ — well outside the current experimental constraint of k < 10¹⁶ × (l_P³/E_P) from muon storage ring data.

**Status:** **WITHDRAWN (Patch 2474).** Acceleration-scaled; no derivation bridges the velocity-dependent ΔSSV to acceleration, and the claimed deviation is γ−1 double-counted. δ ~ 10⁻²⁰ corresponds to v ≈ 4 cm/s, unrelated to 10²⁰g.


### PHEN-SR1-P2. Clock Offset in Ultra-High-Speed Centrifuges

**Prediction:** Precision optical clocks in next-generation centrifuges reaching 10¹⁸–10¹⁹g for seconds should show a measurable offset from the SR prediction at the 10⁻¹⁸–10⁻¹⁹ level.

**Status:** **WITHDRAWN (Patch 2474).** Same defect as P1 (acceleration-scaled, deviation double-counted).


### PHEN-SR1-P3. Gravitational-Wave Dispersion at Extreme Curvature

**Prediction:** In regions of extreme spacetime curvature near neutron-star mergers, small deviations in gravitational-wave propagation speed or phase are expected at the 10⁻²⁰ level, arising from the same PSR_eff compression mechanism applied to the GW carrier modes.

**Status:** **WITHDRAWN (Patch 2474).** Same defect as P1.


### PHEN-SR1-P4. Casimir Pressure Modification from 4D Voronoi UV Cutoff

**Prediction:** The discrete 600-cell lattice imposes a UV cutoff on vacuum fluctuation modes at the Planck scale. Because the 4D Voronoi volume scales as V ∝ r⁴, the correction to the Casimir pressure between parallel plates is:

    δP_Casimir/P_Casimir ~ (l_P/d)⁴

where d is the plate separation. The fourth power (not second power) arises from the 4D mode-density scaling: the 4D mode volume integral contributes two extra powers of l_P/d compared to a 3D UV cutoff. At d = 100 nm this correction is ~10⁻⁴⁰; at d = 10 nm it rises to ~10⁻³⁰. These are far below current experimental sensitivity but represent a falsifiable signature of the 4D lattice structure distinct from any 3D-cutoff model.

**Status:** **CONDITIONAL (Patch 2474)** — retained, not withdrawn: the (l_P/d)⁴ form needs an independent 4D spectral-measure derivation before it can be billed as a prediction. Currently undetectable; possibly accessible with next-generation MEMS at d ≈ 10 nm.


### PHEN-SR1-P5. Unruh Temperature Modification

**Prediction:** An accelerated observer in CPP perceives a modified Unruh temperature:

    T_CPP = T_U × γ_CPP = T_U × (1 + k·ΔSSV)

where T_U = ħa/(2πk_Bc) is the standard Unruh temperature. The fractional shift δT/T ≈ 10⁻²⁰ at a ≈ 10²⁰g — identical in magnitude to the clock-dilation deviation but from a completely different observable (thermal radiation spectrum or excitation rate). This prediction is orthogonal to the clock tests and can be probed through analogue systems (superconducting-qubit circuits, superradiant amplification).

**Status:** **WITHDRAWN (Patch 2474).** Same defect as P1 — the modification factor (1 + k·ΔSSV) is γ_CPP, an identity with γ_SR; the "deviation" is the double-count.


## Section 3: Validated Phenomena — Consilience (PHEN-V)

### PHEN-SR1-V1. Muon Storage Ring Time Dilation (Bailey 1977) — CPP Deviation 10⁻²² Below Bound

**The data:** Relativistic muons (γ ≈ 29.33) in a CERN storage ring experienced sustained centripetal accelerations of order 10¹⁸g while their lifetimes were precisely measured. The observed time-dilation factor agreed with the standard SR prediction to fractional accuracy 2 × 10⁻³ (95% CL).

**Status: WITHDRAWN as consilience (Patch 2474 — the muon bound is void twice).** The entry bounded (i) a normalisation convention (k carries no physical content by itself) and (ii) a deviation that the framework forbids (γ_CPP = γ_SR is an identity; the predicted deviation was γ−1 double-counted). CPP's actual statement about Bailey 1977 is exact agreement by construction — a consistency property shared with SR itself, carrying no discriminating power. The original billing is preserved above for the record; it is not a consilience datum.


### PHEN-SR1-V2. ~~k = l_P³/E_P Confirmed by Monte Carlo to Machine Precision~~ — STRUCK (Patch 2471)

**Struck in full.** The committed script was a stub (empty vertex list, pass-body loop, "For brevity" marker) — one of four MC citations withdrawn at Patch 2471. *History (founder statement, 15 July 2026, Patch 2481):* the run itself occurred in-session during the pre-protocol Sonnet era; what failed was the recording — the real script was never committed and a placeholder took its place. The citation is therefore **unrecorded verification** (reconstructible), not fabrication. Independently of the recording failure, the claim was doubly void — and this is why the STRUCK status survives even a successful reconstruction: k = l_P³/E_P with prefactor 1 rests on the withdrawn dimensional-necessity argument, and k's numerical value is a normalisation convention that no simulation could "confirm" (α cancels identically in k·ΔSSV — verified in the replacement stdlib battery `code/2471_k_convention_and_alpha_geom_verification.py`, 31/31). Entry retained as a tombstone so the correction is legible. Reconstruction target: the Voronoi second-moment/stiffness integral itself (a legitimate computation) — NOT a "confirmation of k," which no run can supply.


### PHEN-SR1-V3. α_geom Appears Independently in Both SR-1 and SS-1

**The number:** α_geom = 3(11+5√5)√(5+√5)/320 ≈ 0.5594 appears in two independent derivations: in SR-1 as the 600-cell Voronoi stiffness integral that establishes the functional form of the PSR saturation curve, and in SS-1 (THEO-SS-4) as the exact geometric coupling constant from which sea_strength is derived. Both derivations use the same 600-cell Voronoi face-area second-moment integral in 4D.

**Status: DOWNGRADED from consilience to shared-geometry observation (Patch 2474).** The SS-1 leg stands (THEO-SS-4). The SR-1 leg is withdrawn as a physical constant: within SR-1, α_geom is a normalisation-dependent stiffness measure (0.5594 per circumradius, 0.2444 per l_P) whose value cancels from the physical product k·ΔSSV. That both sectors evaluate the same 600-cell Voronoi face-area second-moment integral remains true and is worth recording — but with only one leg carrying physical content, it is no longer a two-sector consilience result. If ΔSSV acquires an independent operational normalisation (OPEN-SR-EPSILON; the DM/SF-6 coupling route), α becomes physical and this entry can be re-evaluated.


### PHEN-SR1-V4. GPS Clock Corrections Are Consistent with CPP

**The data:** GPS satellite clocks require daily corrections for both special-relativistic time dilation (satellites moving at ~3.9 km/s, γ-1 ≈ 8.4 × 10⁻¹¹) and general-relativistic gravitational blueshifting (combined correction ≈ 38 μs/day). These corrections are verified daily to ~1 ns precision.

**Status: REFRAMED (Patch 2474).** The original entry quoted a deviation of order 10⁻³⁸ from the withdrawn acceleration-scaled formula. The corrected statement is stronger and emptier at once: γ_CPP = γ_SR identically, so CPP's deviation from SR at GPS precision is exactly zero by construction. Compatibility with GPS is therefore automatic — a consistency property, not a validated prediction, and it carries no discriminating power against SR.


*Document prepared by Thomas Lee Abshier ND and Claude Sonnet (Anthropic), 30 March 2026.*
