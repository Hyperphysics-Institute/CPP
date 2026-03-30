# Development History: SM-4 — Charged Lepton Masses from the K3 Spectral Theorem

**Series:** 600-Cell Standard Model Emergence
**Authors:** Thomas Lee Abshier ND, Grok (xAI), Claude Sonnet (Anthropic)
**Document type:** Development narrative — laboratory notebook record
**Last updated:** 30 March 2026


## Origins: Applying the K3 Theorem to Real Masses

SM-4 was conceived immediately after the K3 Spectral Theorem (SM-3) was
established. SM-3 proved K = 2/3 from the K3 spectrum — but this is one
constraint on three masses. The natural next question was: can CPP determine
the individual lepton masses, not just their Koide ratio? SM-4 is the honest
answer to that question.


## Phase 1: The Parameter Counting Discovery

The first critical development was the parameter counting exercise. The
Koide parametrisation has three parameters (A, ρ, θ). SM-3 derived ρ = √2.
Two parameters remain. With three masses and one derived constraint, there
are exactly two degrees of freedom — A and θ. This was recognised as a
key precision: SM-3 gives one derived constraint; SM-4 gives a consistency
check using two calibrated parameters; the full determination of lepton masses
requires the EW sector to provide θ.

The parameter count audit — three initial, one derived, two calibrated, goal
of one calibrated plus one derived — became the organisational spine of SM-4
and was made explicit in the §2 Remark on free parameters.


## Phase 2: The θ Derivation Attempts (Sessions B–L)

The most intensive phase of SM-4's development was the search for a
derivation of θ = 132.73°. Eleven mechanisms were attempted across multiple
sessions:

Session B: Aharonov-Bohm flux through the K3 cage triangle — the C3 symmetry
prevents the flux from breaking the antibonding degeneracy.

Session C: Spin-orbit coupling within the cage — the symmetry of the coupling
preserves the degeneracy.

Session E: Löwdin downfolding from K₄ to K₃ via the apex vertex V₄ — the
apex is dark to the antibonding modes (⟨φ₋|v⟩ = 0), so the downfolding
leaves the antibonding eigenvalues unchanged. This was a key insight that
led directly to Theorem 2.

Session F: Aharonov-Bohm effects in the 4D 600-cell embedding — the 4D
structure preserves C3 exactly.

Session G: Full 600-cell computation of all 600 tetrahedral cells to check
whether the 4D embedding breaks C3 — computed exactly, C3 preserved in all
cells.

Session K: Self-consistent ZBW mass feedback — fixed-point iteration converges
to θ = 180° (trivial solution), not 132.73°.

Sessions H, I, J, L: Various perturbative corrections to the SSV potential
at the cage scale — all shown to be C3-symmetric and therefore incapable of
breaking the antibonding degeneracy.

All eleven mechanisms failed. The pattern of failure was uniform: every
mechanism that could act on the K3+SSV system either respects C3 symmetry
(and therefore cannot break the antibonding degeneracy) or requires physics
outside the K3+SSV framework (EW sector, Capotauro mechanism).


## Phase 3: The Structural Impossibility Theorem

The Löwdin downfolding result from Session E was the pivotal insight. The
calculation showed that the apex vertex V₄ couples only to the bonding mode
of K₃ and not to the antibonding modes — a mathematical consequence of C3
symmetry, not a numerical coincidence. This generalised to a structural
theorem: because C3 symmetry makes the antibonding subspace degenerate, and
because the degeneracy is protected by C3 against any C3-symmetric perturbation,
no mechanism within the K3+SSV framework can select θ.

The structural theorem converted eleven failures from a track record into a
consequence. The failures were not failures of imagination — they were
instances of a general proof. Theorem 2 was written, formalised, and included
in SM-4 v5.

This conversion of failure into theorem is the most important methodological
development in SM-4's history. It illustrates the CPP methodology: when
multiple attempts fail, the correct response is to look for the structural
reason, not to continue searching for a mechanism that does not exist.


## Phase 4: The Critical Angle Observation

During the parameter extraction session, it was noticed that θ = 132.73°
is close to θ_c = 135°. The critical angle θ_c = 3π/4 is the value at which
the electron mass vanishes exactly — a consequence of ρ = √2 applied to the
Koide parametrisation. The deviation θ_c − θ = 2.27° is consistent with a
second-order SSV correction: (5/4) × sea_strength² ≈ 2.3°. The coefficient
5/4 was identified empirically; its theoretical derivation is an open problem
within OPEN-P-SM-7d.

The critical angle observation was added to SM-4 as a Remark: the electron's
non-zero mass is a second-order correction on top of a nearly-massless
configuration, suggesting the EW sector contributes a small perturbative
shift to θ away from θ_c.


## Phase 5: Harmonisation to v5 (26 March 2026)

Eight harmonisation changes were applied (H1 through H8):

H1: Series ID SM-4 added to title; series name corrected.
H2: Author line updated to include Claude Sonnet (Anthropic).
H3: Institution block added.
H4: Date updated to Version 5, 26 March 2026.
H5: siunitx and graphicx packages added.
H6: Bibliography added (PDG 2024, Koide 1982, SS-1, SM-1, SM-3).
H7: Acknowledgements added.
H8: "Paper 3" → "SM-3" and "Paper 4" → "SM-4" throughout.

The language changes from Phase 1 (prediction → consistency check) were
incorporated throughout during this harmonisation.


## Current Status (30 March 2026)

SM-4 is submission-ready at v5. The six documentation files (mechanism,
glossary, reviews, philosophy, development, phenomena) were written on
30 March 2026. The existing development-SM-4.md (26 March 2026) and
philosophy-SM-4.md (26 March 2026) have been replaced with files
conforming to the six-file standard.


## Key Decisions Log

| Date | Decision | Rationale |
|------|----------|-----------|
| After SM-3 | SM-4 scoped as parameter-counting and θ paper | K3 theorem leaves two free parameters; SM-4 must address both |
| Sessions B–L | 11 θ mechanisms attempted systematically | Each failure constraints the solution space |
| Session E | Apex darkness identified as key lemma | ⟨φ₋|v⟩ = 0 follows from C3 + definition of antibonding modes |
| After Session L | Structural impossibility theorem formulated | 11 failures share one cause: C3 protects antibonding degeneracy |
| Post-SM-3 | Critical angle θ_c = 3π/4 noted and investigated | θ_c − θ ≈ (5/4) sea_strength² is empirically consistent |
| 26 Mar 2026 | Harmonisation to v5 | Series consistency: title, authors, bibliography, notation |
| 30 Mar 2026 | Language: prediction → consistency check throughout | Scientific honesty requires distinguishing derived constraints from calibrated fits |
