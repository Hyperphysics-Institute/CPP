# SF-4 — Changelog (version history)

**Paper:** `flagship_papers/neutrinos/sf-4_neutrinos.tex` — SF-4: Neutrino Sector Unification from 600-Cell Geometry.
**Purpose:** canonical version-history / development archaeology for SF-4, per `templates/paper-formatting.md` §3.1 (no inline CHANGELOG block in the `.tex`; codified Patch 0408/0409).
**Migrated here:** Patch 0572g (Session 149) — the full inline `% Version ...` comment block (v1.1 + v4.x development narrative, 1,177 lines) was moved verbatim out of the `.tex` source into this file; the `.tex` now carries only a minimal header + pointer line. Content below is the migrated block, de-commented, unchanged.

---

============================================================
SF-4: Neutrino Sector Unification from 600-Cell Geometry
       Eight Parameters from One Calibration
Flagship Paper Series (SF-line)

Version 1.1 -- 30 May 2026 (Session 149 -- post-v1.0-SHIP correction.
  Corrects the inner/outer ZBW orbital relationship from the recorded
  ``2:1 frequency'' wording to the recovered result: the Mode-2 standing-
  wave RADIUS ratio is r_out/r_in = 2 (exact), and under 1/r^2 force
  balance the orbital ANGULAR-FREQUENCY ratio is omega_in/omega_out =
  (r_out/r_in)^(3/2) = 2*sqrt(2) (exact), NOT 2. The earlier ``2x
  frequency'' conflated the radius ratio with the frequency ratio.
  Recovered from pre-rigid-documentation development (chat ee212abb,
  19 Mar 2026); see series_strong/papers/recovery-SS-1-spin-zbw-
  frequency.md + CONJ-P-SS-1. IMPACT: the d_eff = 5 Picture A closure
  (the SHIPPED closure) merges spin + orbital orientation into one
  channel via the inner/outer PHASE LOCK, not via the numeric ratio, so
  sigma_nu = z^-10 and all numerical predictions are UNCHANGED. Only the
  wording is corrected. Picture B (NOT selected) was the value-dependent
  ``two-half-cycles-per-moment'' picture; the 2*sqrt(2) correction makes
  its literal counting inexact, which further favors Picture A. Internal
  development history below (v1.0 SHIP Session 54; v4.x archival polish)
  is retained unchanged.)

Version 4.4 -- 11 May 2026 (Session 81 — three-reviewer convergence
  archival polish pass. v4.3 received verdict (a) v1.0 SHIP-ready
  from ChatGPT and concurrent independent verdicts from Grok
  ('outstanding, zero show-stoppers, ready for v1.0 archival') and
  Copilot ('fully SHIP-ready, no remaining corrections required').
  v4.4 incorporates the only non-blocking items Grok suggested for
  true archival quality: (1) JUNO 2025 first-physics empirical
  sourcing made explicit in Table 1 caption (the comparison values
  for sin^2(theta_12) and Delta-m^2_21 in v4.3 were already updated
  to JUNO 2025 values inline but the caption still attributed all
  empirical values to NuFIT 6.0 -- v4.4 corrects this);
  (2) NEW footnote on mass-extraction logic added immediately after
  Table 1 explaining how absolute mass values are obtained in the
  lightest-massless approximation (m_1 -> 0, m_2 -> sqrt(Delta-m^2_21),
  m_3 -> sqrt(|Delta-m^2_31|)) and how the comparison-level residuals
  are computed -- previously the logic was clear in §6 prose context
  but external readers not tracking the development sequence would
  benefit from one explicit summary statement at the table;
  (3) NEW footnote on 2026 cosmology Sigma-m_nu bounds tightening
  added to the Sigma-m_nu row of Table 1 noting that bounds vary
  from 72 meV (DESI 2024 + Planck PR3 + Planck PR4 lensing) to
  ~100-120 meV (DESI + Planck PR4 + Pantheon+ / DES-SN5YR) depending
  on dataset combination, with the trend toward tightening
  continuing through 2026; the SF-4 prediction Sigma-m_nu = 64.9 meV
  is below the tightest bound currently published and provides a
  falsifier against future cosmology that tightens further;
  (4) minor m_nu_3 row label correction in Table 1: 'from
  Delta-m^2_32' -> 'from |Delta-m^2_31|' (the comparison value
  50.9 meV is computed in the lightest-massless approximation as
  sqrt(|Delta-m^2_31|) where |Delta-m^2_31| = Delta-m^2_21 +
  |Delta-m^2_32| approx 2.588e-3 eV^2; the v4.3 label was
  technically slightly incorrect). All four are wording/sourcing
  precision; no theorem changes, no new sections, no structural
  modifications. Mathematical content unchanged. v4.4 is the
  archival-deposit-quality version, suitable for direct upload to
  Zenodo + arXiv. Patch 0342, .tex-only per established workflow.)

Version 4.3 -- 11 May 2026 (Session 77 ChatGPT v4.2 re-review
  final three textual consistency fixes. ChatGPT v4.2 re-review
  verdict was (b) 'v1.0 SHIP-ready after the following 3 specific
  fixes' with confirmation that all four v4.2 calibration fixes
  landed cleanly at theorem level (correlator suppression leading-
  order calibrated, Theorem 5.2 uniqueness properly scoped,
  conditional closure explicitly framed, overdetermination
  language corrected). The three remaining issues are residual
  stale-text spots in section 1 that survived the v4.0 -> v4.1 ->
  v4.2 cleanup waves -- exactly the 'global consistency sweep'
  class of issue noted in the v4.1 commit message. v4.3
  incorporates the three textual consistency fixes:
  (1) Section 1.3 'Inherits as open' bullet rewritten to reflect
  v4.0 conditional resolution: SM-5's K3-eigenmode-identification
  ansatz no longer 'inherits as open' but is conditionally
  resolved cross-sector via the v4.0 Composite Theorem. OP-SM-7d
  still legitimately inherits-as-open (it is a separate open
  problem in the EW sector with no current closure). The bullet
  is split accordingly. (2) Section 1.4 'What this paper delivers'
  bullet for the K3-Cage-Shell Consistency Theorem updated from
  'at the SM-5-inheritance level' / 'SM-5-ansatzed TBM-direction
  selection (Route C structural closure)' to 'closed at conditional
  theorem-closure level via the Composite K3-Cage-Shell Coupling
  Theorem (v4.0)'. The mass-basis-reads-flavor-basis observation
  and TBM-direction coincidence content is preserved; the
  inheritance posture is updated to reflect v4.0 closure. (3)
  Section 1.5 'What this paper does not deliver' bullets for
  OPEN-FP-SF-4-1 and OPEN-FP-SF-4-2 'full RESOLUTION' wording
  replaced with 'conditional theorem-level resolution' /
  'resolution at the current CPP theorem-stack inheritance level'
  to match the global rem:conditional_closure framing from v4.2.
  All three fixes are pure wording precision; mathematical content
  unchanged. ChatGPT v4.3 re-review expected to clear (a) verdict
  for v1.0 SHIP-readiness. After v4.3, SF-4 advances to public
  posting readiness pending Thomas's discretion on Zenodo + arXiv
  submission timing. Patch 0338, .tex-only per established
  workflow (PDF recompilation deferred to local machine).)

Version 4.2 -- 11 May 2026 (Session 76 ChatGPT v4.1 re-review
  incorporation. ChatGPT v4.1 re-review returned verdict (b)
  "v1.0 SHIP-ready after the following 4 specific fixes" --
  substantial improvement from v4.0's (c) "not yet v1.0 SHIP-ready"
  verdict. The four remaining issues are wording precision and
  proof-strength calibration, not structural contradictions; v4.2
  incorporates all four. (1) Lemma 3.1 (No-Anchor Correlator
  Vanishing) statement and proof reworded to avoid overclaiming
  exact vanishing: the lemma's content is correctly stated as
  "correlator contributes no coherent V^(1/3)-order enhancement"
  rather than "correlator vanishes" -- the O(1/V^2) bound is the
  actual result; the framing now matches that bound rather than
  claiming exact zero. Sub-claim (c) text in the alpha-exponent
  derivation updated to match the revised lemma statement.
  Lemma title softened from "No-Anchor Correlator Vanishing" to
  "No-Anchor Correlator Suppression". (2) Theorem 5.2 clause
  (iii) "uniquely" / "Forced by" language softened to
  "structurally selected within the symmetry-preserving perturbative
  class" / "Determined by" -- the cage-shell-to-K3-eigenmode
  assignment is uniquely selected within the symmetry class allowed
  by S_2(V_1)-invariance, not uniquely forced in an unqualified
  sense (nearby symmetry-equivalent embeddings under relabelings
  are not excluded by the perturbation alone). Mathematical content
  unchanged; phrasing now matches the actual proof strength.
  (3) NEW Remark on closure level added immediately after the
  Composite K3-Cage-Shell Coupling Theorem statement (Section 5.7)
  making the conditional-theorem-closure framing explicit: the
  Composite Theorem closes OPEN-FP-SF-4-2 and SM-5 op:nu_id at the
  conditional theorem closure level within the current CPP theorem
  stack (six FIs + four CPP axioms load-bearing), not at the full
  derivational closure level from CPP primitives alone. References
  to OPEN-FP-SF-4-2 and op:nu_id as "RESOLVED" throughout the
  paper should be read in this conditional sense. This makes
  visible the same FI-accounting structure that v3.0 had for
  OPEN-FP-SF-4-1 closure. (4) Terminology sweep: selective
  "RESOLVED" instances in conclusion-adjacent sections and
  forward-roadmap qualified with "conditionally resolved at the
  current CPP theorem stack inheritance level" or equivalent
  phrasing where the conflation between conditional closure and
  full derivational closure could occur. Most "RESOLVED"
  statements are preserved as-is (the conditional sense is set by
  the new Remark in Section 5.7); only locations where the closure
  sense was ambiguous receive the qualifier. Programme state
  UNCHANGED: v4.2 is wording precision and calibration work, not
  new theorem content. Theorem count UNCHANGED at 5. Bibliography
  UNCHANGED at 25 entries. PDF compilation: two pdflatex passes
  clean. ChatGPT v4.2 re-review expected to verify the four
  calibration fixes and clear v1.0-SHIP-readiness verdict (a) for
  public posting. Patch 0337.)

Version 4.1 -- 11 May 2026 (Session 75 ChatGPT v4.0 review
  incorporation. ChatGPT v4.0 review identified six specific
  structural and consistency issues blocking v4.0 to v1.0-SHIP-
  ready advancement; v4.1 incorporates all six fixes plus stale-
  text cleanup. (1) Section 5.6 Argument 3 subsection rewritten
  from "V=4 vs V=30 split inherits SM-5's open problem" framing
  (which directly contradicted Theorem 5.2 / Section 5.7) to
  "v1.0-v3.0 historical posture, superseded at v4.0 by the
  Composite K3-Cage-Shell Coupling Theorem" framing. Route C
  closure summary (Section 5.6.X) updated to remove stale
  inheritance language. (2) Section 11 cross-sector implications
  subsubsection (sec:cross_sector, SM-5 K3 antibonding-doublet
  subsection) rewritten from stale "closure would simultaneously
  close OPEN-FP-SF-4-2" framing to "both problems resolved
  jointly at v4.0" framing per Theorem 5.2 closure. (3) NEW
  Lemma 3.1 (No-Anchor Correlator Vanishing) added to Section 3.3
  to make the implicit step from A4 substrate-isotropy to the
  vanishing of the leading two-point SSV correlator explicit;
  addresses ChatGPT concern that A4 vertex-isotropy alone does
  not automatically imply vanishing two-point correlator without
  the no-anchor / no-shared-reference-direction structure being
  stated. Lemma proves the leading SSV correlator vanishes
  between distinct cage-shell vertices in the unanchored
  configuration via factorization of the joint distribution; sub-
  leading O(1/V^2) corrections accounted for. Sub-claim (c) proof
  now invokes Lemma 3.1 explicitly. (4) Pair-count normalization
  language at sub-claim (d) reframed: rather than "the factor
  1/2 is absorbed into M_0 normalization" (which implied
  freely renormalizing M_0 inside SF-4), the v4.1 text
  acknowledges that M_0 is calibrated against m_e in SM-7 with
  a specific convention for per-link counting; the combinatorial
  pair-sum binom(V,2) at leading order yields V^2/2 * M_0 in
  absolute units, equivalently V^2 * M_0 in the per-ordered-pair
  SM-7 convention. The boxed result uses the SM-7 convention
  throughout. (5) The "overdetermined: two independent arguments"
  language for the cage-shell coupling claim (Table 1.1 caption,
  Theorem 5.2 clause (iii), Section 5.8 closure status) softened
  to "two consistent reformulations of the same V_1-support /
  mu-tau-parity structure" framing. ChatGPT correctly identified
  that the wavefunction-spread argument (reading amplitude
  magnitudes) and the symmetry-character argument (reading parity
  under V_2 to V_3 exchange) are two views of the same eigenstate
  structure rather than two independent derivations. The agreement
  between formulations is now framed as confirming internal
  consistency rather than as overdetermination from independent
  arguments. (6) Theorem 5.2 clause (i) generalized from the
  specific rank-one perturbation Delta H = epsilon_L|V_k><V_k|
  to the general statement that ANY S_2(V_k)-invariant leading-
  order perturbation lifts the antibonding-doublet degeneracy
  and is diagonal in the basis specified by clause (ii). The
  specific rank-one form (with epsilon_L > 0 from A1+A7+A9
  physical contributions) is presented as the leading instance
  that the physical situation produces. This makes the basis
  selection in clause (ii) manifestly robust against the specific
  form of the perturbation, requiring only S_2(V_k)-invariance.
  Stale-text cleanup: three sentences at lines 1077, 1099, 1215
  (Section 6 inheritance table, Section 6 dependencies, Section 5
  remark rem:sm5_op) all carrying pre-v4.0 "tied to SM-5's open
  problem" framing rewritten to v4.0 RESOLVED status.
  Programme state UNCHANGED: no theorem-level mathematical content
  added or removed; v4.1 strengthens proofs (new Lemma 3.1
  makes implicit step explicit) and corrects internal inconsistencies
  in v4.0 between updated sections (5.7, 5.8, 11) and stale
  sections (5.6, 6, 11 subsection). Theorem count UNCHANGED at 5
  (Lemma 3.1 counted as supporting lemma to Theorem 3.1, not as
  independent theorem). Bibliography UNCHANGED at 25 entries.
  PDF compilation: two pdflatex passes clean. ChatGPT v4.1 re-
  review pending; if clean, v4.1 SHIP-ready for public posting.
  Patch 0336.)

Version 4.0 -- 10 May 2026 (Sessions 68-73 OPEN-FP-SF-4-2 +
  SM-5 op:nu_id cross-sector closure campaign. The K3 anti-
  bonding-doublet degeneracy lifting (the foundational open
  problem of CPP neutrino sector, registered as SM-5 op:nu_id
  and inherited into SF-4 as OPEN-FP-SF-4-2 sub-target) advances
  from PARTIAL CLOSURE at v3.0 to RESOLVED at theorem level at
  v4.0. The Sessions 68-71 derivation chain closes both open
  problems simultaneously -- the FIRST CROSS-SECTOR CLOSURE IN
  CPP. All three sub-claims of the OPEN-FP-SF-4-2 closure close
  from CPP axioms A1, A4, A7, A9 plus six foundational inputs
  (FI-K-1 K3 spectrum SM-3-inheritance; FI-K-2 neutrino
  identification SM-5; FI-K-3 K3 base structure SM-1; FI-K-4
  600-cell distance-shell structure; FI-K-5 SF-4 v3.0 cage-shell
  mass formula Theorem 3.1; FI-K-6 charged-lepton K3-vertex
  identification SM-4): (a) K3 antibonding-doublet degeneracy
  lifting via charged-lepton K3-vertex occupation breaking S_3
  down to S_2(V_k) stabilizer; the perturbation Delta H =
  epsilon_L|V_k><V_k| with epsilon_L > 0 is diagonal in the
  TBM-aligned basis (off-diagonal element vanishes because
  |phi_-^(2)> has zero amplitude on V_1) -- Sessions 68-69; (b)
  TBM-basis selection via standard S_3 representation-theory
  branching rule 2|_{S_2} = 1_+ + 1_- which uniquely yields
  |phi_-^(1)> = (2,-1,-1)/sqrt(6) (mu-tau-symmetric, 1_+ irrep)
  and |phi_-^(2)> = (0,-1,1)/sqrt(2) (mu-tau-antisymmetric, 1_-
  irrep) -- Session 70 closes SM-5's op:nu_id at theorem level;
  (c) cage-shell coupling via wavefunction-spread + symmetry-
  character matching (OVERDETERMINED: two independent arguments
  give the same V assignment), forcing |phi_-^(1)> -> V=4
  tetrahedral cage and |phi_-^(2)> -> V=30 icosidodecahedral
  shell with mu-tau-antisymmetric character matching antipodal-
  pair structure (1_- multiplicity 14 under S_2(V_1) subset
  I_h) -- Session 70. Six verification flags Vbeta-1 through
  Vbeta-6 discharged Session 71. Composite K3-Cage-Shell
  Coupling Theorem formalized as three-clause theorem covering
  (i) degeneracy lifting, (ii) TBM-basis selection, (iii)
  cage-shell coupling. SIMULTANEOUSLY RESOLVES BOTH OPEN-FP-
  SF-4-2 AND SM-5 op:nu_id at theorem level -- cross-sector
  mutual closure methodologically templated for future CPP
  work. v4.0 paper integration this session (Session 72,
  patch 0333): Theorem 5.1 clause (iii) upgraded from SM-5-
  inheritance level to theorem level; new Theorem 5.X composite
  K3-Cage-Shell Coupling added; sec:k3_openwork fully rewritten
  from "Open theorem-level work" to "OPEN-FP-SF-4-2 closure
  status (RESOLVED at v4.0)"; Remark rem:inheritance_not_
  weakening updated to "jointly resolved"; bibliography
  sf4_open_fp_sf_4_2_closure bibitem added; sec:open_fp_sf42
  subsection in section 11 rewritten to RESOLVED status with
  SM-5 op:nu_id RESOLVED cross-reference; section 1.4 ship-
  status text updated to reflect joint OPEN-FP-SF-4-1 + OPEN-
  FP-SF-4-2 RESOLVED at v4.0; Table 1.1 K3-Cage-Shell
  Consistency row promoted from PARTIAL CLOSURE to CLOSED at
  theorem level. Cross-sector implication: SM-5 paper companion
  update note required at programme-registry level (Session
  73 SHIP mechanics). FIRST CROSS-SECTOR CLOSURE IN CPP.)

Version 3.0 -- 10 May 2026 (Sessions 62-67 OPEN-FP-SF-4-1
  alpha-exponent residual closure campaign. The alpha-exponent
  residual sub-task of OPEN-FP-SF-4-1 (sub-goal 4 of v1.0:
  theorem-level derivation of V^(7/3) -> V^2 reduction at the
  bound/unbound boundary) advances from OPEN at v2.0 to
  CLOSED at theorem level at v3.0. With the Picture A axiomatic
  closure already RESOLVED at v2.0 (sub-goals 1-3), the alpha-
  exponent closure completes OPEN-FP-SF-4-1 at all four sub-goals.
  OPEN-FP-SF-4-1 advances from ADVANCED (v2.0) to RESOLVED (v3.0).
  All four sub-claims of the alpha-exponent closure close from
  CPP axioms A1, A2, A4, A6', A7, A9 plus four foundational
  inputs (FI-α-1 SM-9-inheritance for bound-mode V^(7/3); FI-α-2
  cage-cooperative SSV reinforcement; FI-α-3 neutrino as unbound
  3D orbital ZBW (same as Picture A FI-3); FI-α-4 rigid-cage
  operational definition with central-anchor condition):
  (a) cage cooperation requires rigid cage via SSV-coherence-
  from-geometry argument (Session 62); (b) unbound 3D orbital
  ZBW has no rigid cage at FI-level (Session 62); (c) no
  cooperation -> bare per-link energy via central-CP-anchor
  argument with O(1/V^2) sub-leading from K3 eigenmode discrete-
  symmetry residual (Session 63); (d) bare per-link energy -> V^2
  scaling via combinatorial pair-count theorem (Session 64).
  Composite theorem boxed: m_unbound = M_0 · V^2 · sigma_nu at
  leading order in V; bound-mode V^(7/3) = V^2 · V^(1/3) reduces
  to V^2 alone with V^(1/3) -> 1 in the unbound regime --
  rigorous form of the v1.0/v2.0 structural argument. Six
  verification flags discharged (Session 65); foundational vs
  derived accounting consolidated (Session 65). Sub-leading
  refinement: antibonding-mode bound relaxes from O(1/V^2) to
  O(1/V) for ν_1 (V=4) and ν_3 (V=30); bonding-mode bound at
  V=12 unchanged at 0.69%. Empirical residual decomposition into
  three sources: (A) alpha-exponent residual; (B) K3-eigenstructure
  partial-binding (OPEN-FP-SF-4-2 territory); (C) O(alpha_EM)
  cross-channel correlations. ν_2 (V=12) 1.7% empirical within
  refined ≤2.7% bound; ν_3 (V=30) 8.3% empirical exceeds (A)+(C)
  bound by factor ~2 -- dominated by (B) K3-eigenstructure
  partial-binding -- structurally identifies OPEN-FP-SF-4-2
  closure as next quantitative-residual-reduction priority.
  v3.0 mechanics: §3.3 (sec:alpha_derivation) full rewrite from
  structural argument to theorem-level proof; §1.5 claim-status
  ledger row CLOSED at theorem level; §4.5 (sec:suppression_open
  work) OPEN-FP-SF-4-1 RESOLVED with full closure narrative; §3.1
  mass formula introduction updated; §1.4 closure status updated;
  §11 Discussion OPEN-FP-SF-4-1 closing subsection rewritten;
  bibliography sf4_alpha_exponent_closure bibitem added. Working
  sketch document at flagship_papers/neutrinos/sketches/SF-4_alpha
  _exponent_closure.md captures all reasoning verbatim per Tier 4
  discipline (1184 lines, 13 sections + 9 findings + close, growing
  monotonically across Sessions 62-65). Documentation suite
  programme-level registration is Session 67 work.)

Version 2.0 -- 10 May 2026 (Sessions 55-60 OPEN-FP-SF-4-1 Picture A
  axiomatic closure campaign. Picture A advances from PARTIAL-CLOSURE
  "leading candidate for theorem-level closure" status (v1.0) to
  AXIOMATIC CLOSURE ACHIEVED at theorem level. All four sub-claims
  of Picture A close from CPP axioms A1-A11 plus foundational inputs
  (3D embedding, neutrino identification, spin-orbital 2:1 frequency
  convention): (a) substrate independence via timescale-separation
  κ_1 ≤ 2m/m_P + A6' edge-sector decomposition (Sessions 56-57);
  (b) AND-of-factors via A6' decomposition into independent gauge
  sectors (Session 57); (c) equilibrium uniform via transitive-action
  uniformity lemma applied to A2+A4+A6' (Session 58); d_eff = 5 via
  icosahedral irrep decomposition 3_vector + 1 + 3_axial-locked
  (Session 59). The leading-order prediction sigma_nu = (1/z^2)^5 =
  1/z^10 is now rigorously derived. Sub-leading 2% empirical residual
  is identified as downstream effects (V^2-vs-V^7/3 cage-shell
  approximation, K3 partial-binding, O(alpha_EM) cross-correlations),
  not Picture A corrections. v2.0 mechanics: §4.3.1 (Picture A) full
  rewrite from sketch closure; §4.3.4 cross-comparison table
  updated; §4.5 (OPEN-FP-SF-4-1) status advances with Picture A
  sub-task RESOLVED, α-exponent sub-task remaining OPEN. Working
  sketch document at flagship_papers/neutrinos/sketches/SF-4_picture
  _A_axiomatic_closure.md captures all reasoning verbatim per Tier 4
  discipline. Documentation suite update is Session 61 work.)

Version 1.0 -- 9 May 2026 (Session 54 v1.0 SHIP. Five independent
  AI review passes converged on v1.0-promotion-ready: ChatGPT × 3
  (passes 1-3 across v0.5 → v0.9) + Grok × 1 + Copilot × 1
  (independent passes on v0.7). Reviewer's pass-3 forward-looking
  statement: "After those fixes, I would be comfortable promoting
  SF-4 to v1.0 SHIP as a partial-closure flagship prediction
  paper." v1.0 SHIP mechanics: title block updated, CHANGELOG
  entry added, theorem-registry entries (THEO-SF-4-1/PROP-SF-4-2/
  THEO-SF-4-3) registered, paper_catalog SF-line section added
  with SF-4 v1.0 SHIPPED row, four-tier documentation suite
  created (handover/development/transcript/reasoning), SF-line
  transcript §17 Sessions 42-54 added, repo metadata transitioned
  to v1.0 SHIPPED status. Substantive content frozen at v1.0;
  future work flows through OPEN-FP-SF-4-1 + OPEN-FP-SF-4-2 +
  SF-2 closure for delta_CP.)

Version 0.9 -- 9 May 2026 (Session 53 v0.9 incorporates ChatGPT
  review pass 3 feedback on v0.8. ChatGPT pass 3 verdict: "promote
  to v0.9, not v1.0 yet" with three blocking polish/numerical
  issues: (1) JUNO uncertainty formatting bug; (2) mass-ratio
  arithmetic inconsistency; (3) stale JUNO bibitem. Plus minor
  CHANGELOG bookkeeping. v0.9 lands all four. Reviewer:
  "After those three fixes, I would be comfortable promoting
  SF-4 to v1.0 SHIP as a partial-closure flagship prediction
  paper.")

Version 0.8 -- 9 May 2026 (Session 52 v0.8 incorporates Grok and
  Copilot independent review pass feedback. Both reviewers
  independently assessed v0.7 as "close to v1.0 SHIP quality" with
  mostly polish items. v0.8 lands the consolidated polish: JUNO
  2025 update, prominent mass-basis remark, operator picture,
  geometric-origin reminder, Sigma m_nu sanity check, partial-
  failure scenarios, expanded out-of-scope, refined category
  labels.)

Version 0.7 -- 9 May 2026 (Session 51 v0.7 incorporates ChatGPT
  review pass 2 feedback. ChatGPT pass 2 returned 7.5/8 v0.6
  corrections landed cleanly with three remaining issues: (1)
  mass-ratio language not fully propagated through §3.4 lead-in
  and §6.1 table category label; (2) direct-mass falsifier
  numerical-logic bug — predicted m_β ≈ 8.7 meV but text said
  "m_β > 5 meV would falsify", which is backwards; (3) §8.2
  "splitting ratio residuals" mislabel where the residuals are
  mass-ratio. v0.7 lands all three fixes plus paper-wide sweep.)

Version 0.6 -- 9 May 2026 (Session 50 v0.6 incorporates ChatGPT
  review pass 1 feedback. 8 substantive corrections plus
  bibliography updates. Paper now at ~1340 lines source; PDF
  recompiled. Ready for AI review pass 2.)

Version 0.5 -- 9 May 2026 (Session 49 v0.5 integration polish:
  stale v0.x version-number references in body text removed
  throughout (abstract, §1.4, §4.3 framing, §4.3 Table 4.1,
  §4.5, §5.8); cross-section consistency verified between §3.4,
  §4.4, §6.1 predictions tables; equation-reference and theorem-
  reference resolution checked (all \\ref and \\eqref targets
  resolve to existing labels); paper now reads as v1.0-target
  document rather than mid-iteration draft; v1.0 SHIP after AI
  review passes per SS-9 methodology)

Version 0.4 -- 9 May 2026 (Session 48 v0.4 fills §6-§11 closing
  sections to full draft quality; all 12 sections (§0-§11) now
  at full paper quality; v0.5 next is integration polish before
  AI review passes toward v1.0 SHIP)

Version 0.3 -- 9 May 2026 (Session 47 v0.3 fills §5 K3-Cage-Shell
  Consistency Theorem to full draft quality from sketches/
  SF-4_k3_cage_shell_consistency.md; foundation §0-§3 and §4
  unchanged from v0.2; §6-§11 unchanged from v0.1)

Version 0.2 -- 9 May 2026 (Session 46 v0.2 fills §4 Suppression
  Mechanism to full draft quality from sketches/SF-4_suppression_
  derivation.md §2-§3 (walk-dimension framework, channel
  enumeration), §7 (three convergent pictures with cross-comparison
  table), §8 (combined result and predictions); foundation §0-§3
  and §5-§11 unchanged from v0.1; v0.3 fills §5 K3-Cage-Shell
  Consistency from sketches/SF-4_k3_cage_shell_consistency.md)

Version 0.1 -- 9 May 2026 (Session 45 initial .tex shipped from
  sf-4_outline.md established at Session 44 patch 0304; covers
  §0 abstract, §1 introduction, §2 SM-5 K3-eigenmode foundation,
  §3 Candidate C cage-shell mass formula at full draft quality;
  §4 suppression mechanism, §5 K3-Cage-Shell Consistency Theorem,
  §6-§11 closing sections shipped as substantive stubs with key
  results stated and full development scheduled for v0.2-v0.5
  per the §11 drafting plan in sf-4_outline.md)

CHANGELOG:
  v2.0 (10 May 2026 Sessions 55-60) -- OPEN-FP-SF-4-1 Picture A
    axiomatic closure achieved.

    The v2.0 promotion lands after a six-session axiomatic closure
    campaign (Sessions 55-60) targeting the v1.0 OPEN-FP-SF-4-1
    "Picture A theorem-level closure from CPP axioms A1-A11" goal.
    Picture A advances from "leading candidate" status (v1.0) to
    AXIOMATIC CLOSURE ACHIEVED (v2.0) with all four sub-claims at
    theorem level:

    - Sub-claim (a) substrate independence (Sessions 56-57, patches
      0317-0318): closes via timescale-separation κ_1 ≤ 2m/m_P
      (orbital ZBW frequency to Planck frequency ratio) + A6' edge-
      sector substrate-substrate independence + standard total-
      probability + causality. For all sub-Planck modes (every SM
      particle), correction to σ_channel = 1/z² is at most
      (m/m_P)²/z³ — utterly negligible. (V1) sanity check confirmed
      via SM-7/SM-8/SM-9 bound-mode mass formulas: bound modes have
      cage-cooperative SSV reinforcement giving amplified per-link
      energies, but unbound modes lack confinement volume and have
      per-chain frequency at the ZBW ground-state mc²/ℏ — exactly
      as the §8.3 timescale argument assumed. (V2) and (V3) flags
      also resolved favorably.

    - Sub-claim (b) AND-of-factors (Session 57, patch 0318): closes
      at theorem level via A6' edge-sector decomposition of substrate
      state components (ρ, φ, O-vector) into independent gauge
      sectors, with sub-leading O(α_EM) cross-correlations.

    - Sub-claim (c) equilibrium uniform marginal (Session 58, patch
      0319): closes at theorem level via the transitive-action
      uniformity lemma — any G-invariant probability measure on a
      finite set with transitive G-action is uniform — applied to
      the icosahedral group I_h acting transitively on the 12 DP-
      orientation options at each vertex, under A2 + A4 + A6' edge
      dynamics. Robust across (R2)-S vs (R2)-L readings of "DP
      orientation."

    - d_eff = 5 first-principles channel enumeration (Session 59,
      patch 0320): closes at theorem level via icosahedral irrep
      decomposition. The 5 channels are the irrep direct sum
      3_vector ⊕ 1 ⊕ 3_axial|_{spin-orbital-locked} = 3 spatial +
      1 ZBW phase + 1 orientation. Channel count is complete: no
      color (singlet), no weak isospin (not per-channel for free
      eigenstate propagation), no flavor (mixing arises only over
      macroscopic distances), no chirality (locked), no separate
      helicity (derived from spatial + orientation).

    Leading-order prediction now rigorous:
      σ_ν = σ_channel^{d_eff} = (1/z²)^5 = 1/z^{10} ≈ 1.62 × 10^{-11}
    for z = 12.

    The 2% empirical residual is downstream effects, NOT Picture A
    corrections (per Sessions 56 Finding 4): V²-vs-V^{7/3} cage-shell
    approximation, K3 partial-binding, O(α_EM) cross-correlations.
    These are not invalidated by the closure but are sub-leading.

    Sub-goals 1-3 of the v1.0 §4.5 OPEN-FP-SF-4-1 list (Picture A
    formalization, independence verification, channel-count rigor)
    are RESOLVED. Sub-goal 4 (α-exponent V^{7/3} → V² reduction in
    the unbound regime) is NOT addressed by Picture A closure and
    remains OPEN.

    v2.0 mechanics: §4.3.1 (Picture A) full rewrite from working
    sketch document; §4.3.4 cross-comparison table updated to show
    Picture A status as CLOSED at theorem level; §4.5 OPEN-FP-SF-4-1
    status updated with Picture A sub-task RESOLVED, α-exponent
    sub-task remaining OPEN. Title block updated. CHANGELOG entry
    added. Documentation suite update (reasoning-SF-4.md /
    development-SF-4.md / transcript-SF-4.md) is Session 61 work.

    Working sketch document at
      flagship_papers/neutrinos/sketches/SF-4_picture_A_axiomatic_closure.md
    captures all reasoning verbatim per Tier 4 discipline (1106
    lines across 13 sections, growing monotonically across Sessions
    55-59).

  v1.0 (9 May 2026 Session 54) -- SHIPPED.

    The v1.0 SHIP promotion lands after a six-session derivation
    campaign (Sessions 38-43 mechanism + sub-derivations),
    four-session paper drafting campaign (Sessions 44-48
    v0.1-v0.4), one-session integration polish (Session 49 v0.5),
    three-session ChatGPT review iteration (Sessions 50-51 + 53
    v0.6/v0.7/v0.9), one-session Grok+Copilot independent reviews
    (Session 52 v0.8), and the present Session 54 SHIP-mechanics
    pass.

    Five independent AI review passes converged on v1.0-promotion-
    ready:
      - ChatGPT pass 1 (v0.5 → v0.6, Session 50): "NOT v1.0-
        shippable yet" → 8 substantive corrections + bibliography
        updates + "derives" overclaiming audit
      - ChatGPT pass 2 (v0.6 → v0.7, Session 51): "Close to v1.0
        SHIP quality" → 3 fixes (mass-ratio language propagation;
        direct-mass falsifier numerical-logic bug; cross-ref
        integrity)
      - Grok pass 1 (v0.7 → v0.8, Session 52): "very close to v1.0
        SHIP quality" → 6 polish suggestions
      - Copilot pass 1 (v0.7 → v0.8, Session 52): "close to v1.0
        SHIP quality" → 11 polish suggestions
      - ChatGPT pass 3 (v0.8 → v0.9, Session 53): "promote to v0.9,
        not v1.0 yet" → 3 v1.0-blocking fixes (JUNO uncertainty
        formatting; mass-ratio arithmetic consistency; JUNO
        bibliography arXiv:2511.14593) + bookkeeping
      - ChatGPT pass-3 forward-looking: "After those fixes, I
        would be comfortable promoting SF-4 to v1.0 SHIP as a
        partial-closure flagship prediction paper."

    Substantive content (§0-§11) is frozen at v1.0. The .tex
    source file is not edited further unless and until external
    post-public-posting feedback prompts a v1.x revision. The
    four-tier documentation suite (documentation_suite/handover-
    SF-4.md, development-SF-4.md, transcript-SF-4.md, reasoning-
    SF-4.md) is ACTIVE — additional documentation artifacts
    (anthology chapter, TATWD integration, supplemental docs)
    can ship post-v1.0 without re-opening the .tex.

    v1.0 SHIP DELIVERABLES:
      1. Title block updated to "Version 1.0 SHIPPED"
      2. theorem-registry.md: SF-line section added with
         THEO-SF-4-1 (K3-Cage-Shell Consistency, structural-
         numerical level; conditional on K3-eigenmode-
         identification ansatz from SM-5), PROP-SF-4-2
         (mu-tau-exchange symmetry of mass operator in flavor
         basis), THEO-SF-4-3 (exact recovery of TBM angles).
         Summary-Statistics SF row added: 2 theorems + 1
         proposition. Total theorem count updated.
      3. paper_catalog.md: SF-line catalog section added with
         SF-4 v1.0 SHIPPED row.
      4. Four-tier documentation suite created at
         flagship_papers/neutrinos/documentation_suite/
         (handover-SF-4.md, development-SF-4.md, transcript-
         SF-4.md, reasoning-SF-4.md).
      5. flagship_papers/SF-line_development_transcript.md §17
         added covering Sessions 42-54 SF-4 v1.0 ship arc.
      6. INDEX.md and flagship_papers/neutrinos/README.md
         transitioned to v1.0 SHIPPED status.
      7. research_frontier.md programme-state-changes captured.

    PROGRAMME STATE CHANGES from v1.0 SHIP:
      - Theorem registrations: THEO-SF-4-1, PROP-SF-4-2,
        THEO-SF-4-3 added to theorem-registry. Theorem count
        52 → 54 (+ 1 proposition).
      - No new conjectures registered (CONJ-EW-W0 and
        CONJ-SS-Gluon-4Vertex were already registered at
        Session 41 patch 0301).
      - Predictions registered (qualitative): seven of eight
        neutrino-sector parameters at zero free parameters via
        the cage-shell mass formula + K3-Cage-Shell Consistency
        Theorem. Quantitative prediction registry update is
        scope-deferred to a future Research_Frontier sweep.
      - Programme negative-result count UNCHANGED.
      - Open-problem registry: OPEN-FP-SF-4-1 PARTIAL CLOSURE
        preserved; OPEN-FP-SF-4-2 PARTIAL CLOSURE preserved;
        both flagged as primary v1.0+ targets in the SF-4
        post-ship work plan.

    POST-v1.0 WORK QUEUE (in priority order):
      (A) OPEN-FP-SF-4-1 Picture A formalization from CPP axioms
        A1-A11 — single-paper continuation work; estimated 5-10
        sessions of focused derivation. Closure converts the
        suppression mechanism from PARTIAL CLOSURE to theorem
        level.
      (B) Cross-sector cooperation with SM-5 antibonding-doublet
        open problem closure — closure benefits both SM-5 and
        SF-4's OPEN-FP-SF-4-2 simultaneously. Cross-sector
        mutual-closure opportunity.
      (C) SF-2 EW-flagship drafting — produces delta_CP via
        OP-SM-7d Capotauro mechanism (route ii deferral). On
        SF-2 closure, SF-4 v2.0 update extends prediction count
        from 7/8 to 8/8 zero-parameter.
      (D) Anthology chapter at Rovelli/SciAm register (parallel
        to SS-9 "The Polyhedron's Conditions"). Title TBD; ~5000
        words at popular-science register. ~Session 55-56.
      (E) TATWD integration to CPP_the_theory.md (popular-science
        book outline). Parallel to SS-9 integration in Session
        35. ~Session 56-57.
      (F) JUNO 2025 follow-up at peer-review publication: when
        the JUNO arXiv:2511.14593 paper progresses to peer-
        reviewed publication, replace the bibitem with the
        peer-reviewed reference. Minor bibliography sweep only.

  v0.9 (9 May 2026 Session 53) -- ChatGPT review pass 3 feedback
    on v0.8 incorporated. Three v1.0-blocking issues plus minor
    CHANGELOG bookkeeping. Reviewer verdict: "promote to v0.9,
    not v1.0 yet" with explicit "after those three fixes, I would
    be comfortable promoting SF-4 to v1.0 SHIP" assessment.

    1. JUNO UNCERTAINTY FORMATTING BUG (ChatGPT #1):
       v0.8 §3.4 wrote: "Δm²_21 = 7.50 × 10⁻⁵ eV² ± 0.12"
       which reads dimensionally wrong (the ±0.12 should be on
       the 7.50 factor not the 10⁻⁵ eV² unit). Fixed:
       "Δm²_21 = (7.50 ± 0.12) × 10⁻⁵ eV²"
       Bibliography always had this correctly.

    2. EMPIRICAL MASS-RATIO ARITHMETIC CONSISTENCY (ChatGPT #2):
       v0.8 §3.4 quoted empirical m_2/m_1 = 8.66, m_3/m_1 = 50.9,
       and m_1 ≈ 0.96 meV together. These three numbers cannot
       all be true simultaneously under any single normalization
       convention:
       - 8.66 meV = √Δm²_21 (m_1 → 0 massless limit, treating
         as absolute mass value)
       - 50.9 meV = √|Δm²_31| (same convention)
       - "ratio 8.66" only equals "absolute m_2 = 8.66 meV" if
         m_1 = 1 meV exactly (not 0.96)
       - 0.96 meV = √(Δm²_21/(9² - 1)) = the back-solved value
         assuming m_2/m_1 = 9 (SF-4 prediction) self-consistently
       v0.9 §3.4 rewrite: dropped the inconsistent "0.96 meV
       self-consistent fit" language; explicitly adopts m_1 → 0
       massless approximation as the comparison convention with
       new eq:empirical_masses showing m_2 → √Δm²_21 ≈ 8.66 meV
       and m_3 → √|Δm²_31| ≈ 50.9 meV; presents two equivalent
       comparison conventions: (a) absolute-mass comparison
       gives 2%/8% match to SF-4 (8.81/55.1 meV) — the convention
       used in Table 4.2 and §6 master predictions table; (b)
       ratio-level comparison under implicit m_1 = 1 meV reference
       gives 4%/11% match — the convention used in summary
       statements (abstract, §6.2 residual-pattern, §8 intro,
       §11.2). Both views show the same underlying residual
       pattern; both are valid. The 2-11% range conservatively
       bounds the leading-order V² structural residual; OP-SM-7d
       is the natural lifting mechanism. Net: §3.4 rewritten
       with explicit convention statements; no other paper
       sections needed updating since they already use one
       convention or the other consistently within their context.

    3. JUNO BIBLIOGRAPHY UPDATE (ChatGPT #3):
       v0.8 had \bibitem{juno2025_first_results} marked "in
       preparation (2025); reference to be updated when peer-
       reviewed publication available". ChatGPT pass 3 confirmed
       the JUNO 2025 first physics result is now on arXiv as
       arXiv:2511.14593. v0.9 replaces the provisional bibitem
       with the arXiv reference; values sin²θ12 = 0.3092±0.0087
       and Δm²_21 = (7.50±0.12)×10⁻⁵ eV² preserved.

    4. CHANGELOG BOOKKEEPING:
       v0.8 CHANGELOG opened with "Ten distinct edits" but the
       v0.8 body said "Eight specific edits". Fixed:
       "Eight specific edits" → "Ten distinct edits" for internal
       consistency.

    CROSS-REFERENCE INTEGRITY: All `\ref` and `\eqref` targets
    resolve to existing `\label` definitions (verified by comm
    of grep extractions; new eq:empirical_masses label added).
    PDF recompiled successfully.

    Net: ~25 lines net change concentrated in §3.4 mass-ratio
    arithmetic rewrite. Paper at ~1780 lines source.
    Reviewer's v0.9 forward-looking assessment: "After those
    fixes, I would be comfortable promoting SF-4 to v1.0 SHIP
    as a partial-closure flagship prediction paper."

  v0.8 (9 May 2026 Session 52) -- Grok and Copilot independent
    review pass 1 feedback incorporated. Both reviewers
    independently assessed v0.7 as "close to v1.0 SHIP quality" /
    "very close to v1.0 SHIP quality" with mostly polish items.
    v0.8 lands the consolidated set of polish items from both
    review streams. Ten distinct edits:

    1. JUNO 2025 FIRST PHYSICS RESULTS INTEGRATION (Grok #1):
       - §3.4 lead-in updated: Δm²_21 from NuFIT 6.0 (7.49e-5)
         → JUNO 2025 first physics (7.50e-5 ± 0.12) with NuFIT
         6.0 cited as consistent corroboration
       - §6.1 master predictions table sin²θ12 row: 0.307±0.013
         (NuFIT 6.0) → 0.3092±0.0087 (JUNO 2025; NuFIT 6.0 cited
         as consistent)
       - Bibliography: new \\bibitem{juno2025_first_results}
         entry for the JUNO 2025 first-physics public values,
         marked "in preparation" with note to update reference
         when peer-reviewed publication available

    2. STRUCTURAL-VS-STATISTICAL RESIDUAL NOTE (Grok #3):
       §3.4 added clarifying sentence noting that the 4% and 11%
       residuals are STRUCTURAL (the same V² scaling assumption
       produces them across both ratios simultaneously) rather
       than STATISTICAL (independent measurement uncertainties),
       and that OP-SM-7d Capotauro mechanism is the natural
       lifting mechanism.

    3. RATIOS-VS-ABSOLUTE-SCALE CONCEPTUAL SEPARATION (Copilot
       suggestion #3): §3.4 added "Two distinct structural claims"
       paragraph at end of section explicitly distinguishing
       (a) mass-ratio prediction (zero-parameter, robust to σ_ν
       closure level) from (b) absolute-scale claim (separate
       structural claim via σ_ν, carries OPEN-FP-SF-4-1
       PARTIAL CLOSURE status). Pointers to master table and
       claim-status ledger included.

    4. OPERATOR-LEVEL PICTURE FOR α=2 (Copilot suggestion #1):
       §3.3 added new paragraph "Operator-level picture" giving
       explicit CPP-operator interpretation of the V^{7/3} → V²
       reduction at the bound/unbound boundary. The neutrino
       mass operator is proportional to substrate pair-
       interaction count summed over cage-shell vertices; for
       bound modes this is multiplied by linear-cage-dimension
       factor capturing rigid-cage spatial extent; for unbound
       modes the geometric-extent term has no CPP-operational
       definition (no rigid cage exists for unbound 3D ZBW
       configuration), so the leading non-zero contribution is
       the V² pair-count alone. This addresses "what is mass?"
       directly at operator level.

    5. GEOMETRIC-ORIGIN PARAGRAPH FOR V ∈ {4,12,30} (Grok #4):
       §3.2 added new paragraph "Geometric origin of the three V
       values" explaining each: (i) V=12 is the icosahedral first
       shell (z=12 coordination); (ii) V=4 is the tetrahedral
       inscribed sub-cage of shell 1 via compound-of-five-
       tetrahedra, distinguished by SM-1 four-cage taxonomy;
       (iii) V=30 is the icosidodecahedral d²=2 shell (15
       antipodal pairs). Pointers to §5.5.1 Table 5.1 verified
       shell sequence and \cite{abshier_sm1} for taxonomy.

    6. PROMINENT MASS-BASIS-VS-FLAVOR-BASIS BOXED REMARK (Copilot
       suggestion #11): §3.2 inserted blue-shaded mdframed
       clarification box at first appearance of \eqref{eq:vassignment}
       (the cage-shell assignment). Explicitly states that the
       assignment is in mass basis (K3-eigenmode basis from
       SM-5), not flavor basis (K3 vertex basis); flavor-basis
       reading would force PMNS=identity contradicting
       observation. Pointer to §5 and §5.2 for full discussion.
       Promotes the load-bearing observation to first appearance.

    7. Σm_ν COSMOLOGICAL-BOUND SANITY CHECK (Copilot suggestion
       #2): §4.5 (Combined cage-shell + suppression result) added
       new paragraph "Cosmological-bound sanity check" with
       explicit derivation eq:sumcheck:
         Σm_ν = M_0 · σ_ν · (V_1² + V_2² + V_3²) = M_0 · σ_ν · 1060
              ≈ 64.9 meV
       Note that no empirical input was used; absolute-scale
       prediction is purely structural via σ_ν. Comparison to
       DESI/Planck 72 meV bound and Planck PR4 supernova 86 meV
       alternative bound. Pointer to §9.1.3 cosmological falsifier.

    8. PARTIAL-FAILURE SCENARIOS / MODULAR FALSIFICATION (Copilot
       suggestion #9): §9.2 added new subsection
       "Partial-failure scenarios and modular falsification" with
       three explicit scenarios:
       - TBM falsified, mass ratios survive → cage-shell mass
         mechanism remains viable; K3-eigenmode-identification
         ansatz needs revision
       - Mass ratios falsified, hierarchy survives → cage-shell
         vertex assignment {4,12,30} needs revision; mass-
         mechanism principle (m ∝ V^α) potentially viable
       - Hierarchy falsified (JUNO inverted) → cleanest single-
         claim falsification of cage-shell assignment
       Closes with: strict-C inheritance discipline ensures
       inherited content carries inherited risk structurally
       separable from new SF-4 content.

    9. §10.3 EXPANDED OUT-OF-SCOPE (Copilot suggestion #7-8):
       Two additional explicit out-of-scope items added:
       - Radiative corrections and renormalization-group running
         (mass formula at zeroth-order tree level; substrate
         provides regulator; v1.0+ work bundled with SF-2 OP-SM-7d)
       - Leptogenesis and baryon-asymmetry origin (requires δ_CP
         deferred to SF-2 plus cosmological evolution; SF-4
         makes no claim about leptogenesis viability or BAU
         magnitude)

    10. §6.1 MASTER PREDICTIONS TABLE CATEGORY LABEL REFINEMENT
       (Copilot suggestion #3): "Mass eigenvalues (zero parameters)"
       → "Mass eigenvalues (absolute scale: PARTIAL CLOSURE via
       σ_ν)"; "Mass ratios (zero parameters, V² scaling)" → "Mass
       ratios (zero-parameter, V² scaling alone --- robust to
       σ_ν closure)". Makes the structural-claim distinction
       visible at a glance in the master table.

    M_0 NOTATION: Copilot's suggestion #5 (z/φ vs "z/4") was an
    OCR misread; verified M_0 = m_e · z/φ_g consistent throughout
    v0.7 source via grep. No notational fix needed.

    Net: ~120 lines new content across 10 distinct edits. Paper
    advanced from 1591 lines (v0.7) to ~1700 lines (v0.8).
    PDF recompiled.

  v0.7 (9 May 2026 Session 51) -- ChatGPT review pass 2 feedback
    incorporated. Pass 2 verdict: 7.5/8 v0.6 corrections landed
    cleanly; v0.6 strong improvement over v0.5 but not yet
    v1.0-shippable. Three remaining issues fixed in v0.7:

    1. MASS-RATIO LANGUAGE FULLY PROPAGATED. v0.6 fixed the
       abstract but left several body-text mislabels:

       a. §3.4 SUBSECTION TITLE: "Splitting predictions at zero
          free parameters" → "Mass-ratio predictions at zero
          free parameters"
       b. §3.4 LEAD-IN: "the mass-squared ratios are m_2/m_1=
          9.00, m_3/m_1=56.25" → "the mass ratios are m_2/m_1=
          9.00, m_3/m_1=56.25" (these ARE mass ratios, not mass-
          squared ratios)
       c. §6.1 MASTER TABLE CATEGORY LABEL: "Mass-squared
          splitting ratios (zero parameters, V² scaling)" →
          "Mass ratios (zero parameters, V² scaling)" — the rows
          in this category show m_2/m_1=9.00 and m_3/m_1=56.25
       d. §8 INTRO: "structural residuals on the splitting
          ratios" → "structural residuals on the mass ratios"
       e. §8.2: "structural residuals 4% and 11% in the splitting
          ratio predictions of eq:massratios" → "structural
          residuals 4% and 11% in the mass-ratio predictions of
          eq:massratios"
       f. §11.2: "V² structural residuals (4% and 11% in the
          splitting ratios)" → "V² structural residuals (4% and
          11% in the mass ratios)"

       Six total relabels. The remaining "mass-squared splitting"
       / "mass-squared ratios" usages in the paper (lines 441,
       696, 698, 1163) are all legitimate references to actual
       Δm² quantities and have been preserved.

    2. DIRECT-MASS FALSIFIER NUMERICAL-LOGIC BUG CORRECTED.
       v0.6 §9.1.2 said: "A direct-mass measurement of m_β >
       5 meV at the level of the predicted scale would force at
       least one mass eigenvalue to exceed the cage-shell
       prediction by a factor of ~5, falsifying the σ_ν = z^{-10}
       structural prediction."

       BUG: the same paragraph stated "predicted m_β ≈ 8.7 meV"
       (from the PMNS-weighted sum). 5 meV is BELOW 8.7 meV, so
       a measurement of m_β > 5 meV would CONFIRM not falsify.

       v0.7 reframes the falsifier around inconsistency with the
       predicted scale: a measurement returning either (a) a
       robust upper bound substantially below ~8.7 meV (e.g.,
       m_β < 3-5 meV at high confidence — SF-4 absolute scale too
       large) or (b) a measurement substantially above ~8.7 meV
       (e.g., m_β ≳ 30-50 meV — SF-4 absolute scale too small)
       would falsify. Two-sided framing now correct relative to
       the predicted central value.

       Abstract correspondingly updated: "the principled direct-
       mass-measurement falsifier at m_ν1 > 5 meV" → "the
       principled direct-mass falsifier --- a beta-decay
       measurement of m_β robustly inconsistent with the predicted
       m_β ≈ 8.7 meV". Maintains the principled-not-near-term
       framing while removing the numerical-logic error.

    3. CROSS-REFERENCE INTEGRITY VERIFIED. All `\\ref` and
       `\\eqref` targets resolve to existing `\\label` definitions
       (zero orphan references). Compiled PDF page count and
       binary updated.

    Net: ~10 lines net change across 7 specific edits + 2-line
    section-title rename. Paper now at 1517 lines source. PDF
    recompiled.

  v0.6 (9 May 2026 Session 50) -- ChatGPT review pass 1 feedback
    incorporated. 8 specific corrections plus bibliography
    updates and "derives" audit:

    1. ABSTRACT (§0): full rewrite incorporating multiple fixes:
       - "derives seven of eight parameters" → "proposes a
         structurally constrained leading-order derivation of
         seven parameters" (softening overclaiming until
         OPEN-FP-SF-4-1 is closed)
       - "mass-squared splitting predictions m_2/m_1=9.00 and
         m_3/m_1=56.25" → "mass ratio predictions" (these are
         mass ratios, not mass-squared splittings); added explicit
         mass-squared ratio values (81 and 3164) for clarity
       - JUNO falsifier: "JUNO 2026+ resolution" → "JUNO mass-
         ordering measurement (multi-year program; ~3sigma in ~6
         years)"
       - Cosmological bound: noted "one stringent combination"
         framing with $\sim 86$ meV alternative analyses
       - Direct-mass falsifier: explicit "principled... but
         exceeds near-term experimental sensitivity" framing
       - "SF-4 introduces no new ansatz beyond SM-5's" →
         "SF-4 introduces no new fitted parameter beyond inherited
         single calibration M_0, but the cage-shell coupling
         assignment to specific K3 eigenmodes is a new structural-
         coupling claim whose theorem-level proof remains
         OPEN-FP-SF-4-2"

    2. §1.5 FOUNDER'S VOICE: softened "This paper derives seven of
       those eight numbers" to "proposes a structurally constrained
       leading-order derivation of seven of those eight numbers";
       "JUNO experiment will deliver in 2026+" softened to
       multi-year program; mass-ordering identification fixed
       ("electron neutrino" → "muon neutrino" for the m_2 closest-
       in-mass case)

    3. NEW §1.6 CLAIM STATUS LEDGER: 12-row table (Table
       tab:claim_ledger) with explicit closure status for each
       substantive claim. Categories: THEOREM (inherited or
       computed); INHERITED TAXONOMY (not independent SF-4
       theorem); STRUCTURAL ARGUMENT (open theorem closure);
       PARTIAL CLOSURE (numerical exact, theorem v1.0+);
       INHERITED CONDITIONAL THEOREM; INHERITED ANSATZ
       (open problem); FORCED CONSEQUENCE; REGISTER-AS-OPEN;
       NOT PREDICTED; NOT SPECIFIED. Caption explicitly states
       the framework's epistemic posture: "no new fitted
       parameter; one new structural-coupling claim at PARTIAL
       CLOSURE level".

    4. §1.3 + §3.1: "exponent alpha=2 derived from the bound/
       unbound boundary" softened to "argued from the bound/
       unbound boundary (structural argument; theorem-level
       closure registered as part of OPEN-FP-SF-4-1)"

    5. §2.5 INHERITANCE TABLE caption: "no new ansatz" replaced
       with "no new fitted parameter beyond M_0; new structural-
       coupling claim is OPEN-FP-SF-4-2"

    6. §3.4 SPLITTINGS: NuFIT 5.3 numbers (Δm²_21=7.39e-5,
       |Δm²_32|=2.52e-3) updated to NuFIT 6.0 (7.49e-5, 2.513e-3);
       added explicit clarification paragraph distinguishing mass-
       ratio comparison (4%/11% match) from mass-squared splitting
       ratio (Δm²_31/Δm²_21 = 39.5 predicted vs 34.1 empirical,
       13% match)

    7. §4 INTRO: "This section derives σ_ν=z^{-10}" → "proposes
       a structurally constrained leading-order derivation of
       σ_ν=z^{-10}... Theorem-level rigor from CPP axioms A1-A11
       is registered as OPEN-FP-SF-4-1 and is post-v1.0 work"

    8. §4.2: "§4.3 derives the per-channel suppression" softened
       to "§4.3 proposes the per-channel suppression strength via
       three convergent physical pictures"

    9. §4.4 TABLE 4.2: removed "(= m_νe in NH)" identification
       (m_νe usually means m_β in beta-decay, not m_1);
       analogous "(= m_νμ)" and "(= m_ντ)" removed

    10. §5 INTRO + §5.7 + §5.8: three instances of "no new ansatz
        beyond SM-5's" replaced with "no new fitted parameter
        beyond inherited single calibration M_0; new structural-
        coupling claim is OPEN-FP-SF-4-2"

    11. §6.1 MASTER PREDICTIONS TABLE:
        - "(JUNO 2026+)" → "(JUNO multi-year program)"
        - NuFIT 5.3 → NuFIT 6.0; updated angle values:
          sin²θ12 = 0.307±0.013; sin²θ23 = 0.572 (NO, octant
          ambiguity); sin²θ13 = 0.02203±0.00056
        - Caption: added "one stringent combination" framing for
          DESI/Planck bound; added "Planck PR4 + supernovae" $\sim
          86$ meV alternative reference

    12. §6.2 + §8.2: sin²θ13=0.0224 → 0.02203 (NuFIT 6.0)

    13. §6.3 A_4 COMPARISON: "additionally derives the absolute
        mass scale" softened to "additionally proposes a
        structurally constrained derivation of the absolute mass
        scale"

    14. §9.1.1 JUNO FALSIFIER: full rewrite. Title: "Inverted
        hierarchy (JUNO 2026+)" → "Inverted hierarchy (JUNO
        multi-year program)". Body: removed crisp 2026-2028
        resolution claim; added multi-year program / ~6 years
        to ~3sigma framing; added current global-fit position
        note (NuFIT 6.0 NO/IO equipoise without SK-atm); added
        DUNE/Hyper-K reinforcement note

    15. §9.1.2 DIRECT-MASS FALSIFIER: full rewrite. Title:
        "Direct mass measurement above ~5 meV" → "Principled
        direct-mass falsifier (longer-timescale)". Body:
        distinguishes m_β (beta-decay observable) from m_ν1
        (lightest mass eigenstate); predicted m_β ≈ 8.7 meV with
        NH+SF-4 values; explicit "5 meV principled threshold is
        well below the sensitivity floor of currently-funded
        direct-measurement programmes" with KATRIN ~0.5 eV /
        Project 8 ~40 meV current sensitivity stated; framed as
        "conceptually clean but not near-term experimentally
        accessible"

    16. §9.1.3 COSMOLOGICAL BOUND: full rewrite. Added "Dataset-
        dependence of the cosmological bound" subsection
        qualifying the 72 meV bound as "one stringent combination"
        and noting Planck PR4 + supernovae alternative analyses
        relax to ~86 meV. SF-4 prediction Σm_ν=64.9 meV stated as
        consistent with all current cosmological bounds across
        dataset-combination range. Falsifier strength reframed
        as scaling with dataset-independence of any future
        tightening

    17. BIBLIOGRAPHY: \bibitem{nufit53} replaced with
        \bibitem{nufit60} (Esteban et al. arXiv:2410.05380, Oct
        2024 - NuFit-6.0); added \bibitem{naredo_tuero_2024} for
        Planck-PR4 supernova-relaxation analysis (arXiv:2407.07595
        + arXiv:2406.14554)

    Net: ~70 lines new content (claim ledger ~50 + falsifier
    rewrites ~30 - 10 net of softenings); paper now at 1340 lines
    source. PDF recompilation succeeds.

  v0.5 (9 May 2026 Session 49) -- integration polish pass.
    Substantive content of all 12 sections unchanged from v0.4;
    this pass cleans stale-version-number references and verifies
    internal consistency. Edits:
    - Abstract (§0): "PARTIAL CLOSURE in v0.1" + "v0.2-v0.3
      drafting iterations" → "ship at PARTIAL CLOSURE" (forward-
      looking framing, no draft-iteration history)
    - §1.4 What this paper does not deliver: 3 instances of
      "in v0.1" → cleaned (removed unnecessary version qualifier,
      cleaner forward-reference to "post-v1.0 work")
    - §4.3 three-pictures framing: "single-pick at v0.x" →
      "single-pick at the v1.0 level"
    - §4.3 Table 4.1: column header "v0.2 status" → "v1.0 status"
    - §4.5 OPEN-FP-SF-4-1: "v1.0+ work. The v0.1-v0.5 SF-4 paper
      ships at" → "post-v1.0 work. The SF-4 paper ships at"
    - §5.8 OPEN-FP-SF-4-2: same v0.1-v0.5 reference cleaned
    Verification:
    - All \\ref and \\eqref targets resolve to existing \\label
      definitions (verified by comm of grep extractions)
    - Numerical predictions consistent across §3.4 (splitting
      ratios 9.00/56.25), §4.4 (mass values 0.98/8.81/55.1/64.9
      meV), §6.1 (master predictions table)
    - Theorem 5.1 / Proposition 5.2 / Theorem 5.3 numbering
      verified consistent throughout
    - 22 bibliography entries (12 internal + 10 external)
      formatted consistently
    Net: 7 stale-version-reference fixes; ~10 lines net change;
    paper now at 1270-line v1.0-target draft.

  v0.4 (9 May 2026 Session 48) -- §6-§11 closing sections filled to
    full draft quality. All six closing sections expanded from
    stubs to full paper-quality content:
    §6 Predictions Summary: master predictions table restructured
      with grouped categories (mass eigenvalues / splitting ratios
      / PMNS angles / mass ordering / CP phase) and explicit
      NuFIT/DESI/Planck citations; §6.2 structural-residual
      pattern (tight 2-4% vs looser 8-14% matches with explanation
      via OP-SM-7d Capotauro corrections concentration); §6.3
      comparison to A_4 discrete-symmetry models (Harrison/Ma/
      Altarelli-Feruglio) noting CPP-specific physical
      identification of K3 as colour-cage base.
    §7 delta_CP Posture (Route ii): full justification of route ii
      selection at Session 39 with three reasons (scope discipline,
      inheritance integrity, SF-2 readiness); §7.2 four candidate
      handles for eventual route i derivation enumerated for
      SF-2 forward reference (cage-orientation angle, Capotauro
      bias, K3-eigenstate phase structure, substrate chirality).
    §8 Higher-Order Corrections (OP-SM-7d Inheritance):
      inheritance posture explicit; §8.2 expected effects of
      OP-SM-7d closure on TBM angles + mass eigenvalue corrections
      + delta_CP derivation as three classes of residuals closing
      simultaneously; §8.3 what this means for v1.0 ship.
    §9 Cumulative Falsifier: 5 falsifiers fully developed.
      §9.1 Direct SF-4 falsifiers: §9.1.1 inverted hierarchy
      (JUNO 2026+) clean named near-term; §9.1.2 direct mass
      measurement >5 meV (KATRIN++/Project 8); §9.1.3 cosmological
      tightening to <50 meV (DESI/CMB-S4/LSST). §9.2 Framework-
      level falsifiers: §9.2.1 PMNS deviation from TBM (DUNE/
      Hyper-K); §9.2.2 substrate-mechanism deviation from sigma=
      z^(-10). §9.3 What is not predicted (Majorana-vs-Dirac,
      0nu beta beta, sterile neutrinos).
    §10 Open Theorem-Level Work: §10.1 OPEN-FP-SF-4-1 (Picture A
      formalization) with 4 sub-goals; OPEN-FP-SF-4-2 (vertex-
      by-vertex K3-coupling) with 3 sub-goals; §10.2 alpha=2
      structural-derivation handle; §10.3 items not addressed in
      v1.0; §10.4 forward roadmap with 4 priority categories.
    §11 Discussion: §11.1 programme-level pattern (structural
      agreement at integer counts as load-bearing signal) with
      SS-7 / SM-9 / SF-4 cross-comparison and methodological
      stance statement; §11.2 cross-sector implications fully
      developed (SF-2 OP-SM-7d closure, SM-5 antibonding-doublet
      open problem, walk-dimension framework cross-sector
      applications including free-particle propagators / light
      propagation / other gauge bosons, SF-7 grand unification);
      §11.3 outlook with experimental programme timeline (2026-
      2032+) and theoretical research directions.
    Bibliography: 9 new external references added (NuFIT 5.3,
    DESI 2024, Planck 2018, JUNO design report, KATRIN 2022,
    Project 8, DUNE TDR 2020, Harrison-Perkins-Scott 2002,
    Ma-Rajasekaran 2001, Altarelli-Feruglio 2010).
    Net: §6-§11 expanded from ~120 lines stubs to ~480 lines
    full paper-quality content. Foundation §0-§3 and §4-§5
    (Sessions 45-47) unchanged. Paper now at all-sections-full-
    quality status; v0.5 integration polish next.

  v0.3 (9 May 2026 Session 47) -- §5 K3-Cage-Shell Consistency
    Theorem filled to full draft quality. The §5 stub from v0.1
    (~30 lines) replaced with full paper-quality content (~280
    lines) including:
    - Theorem 5.1 (K3-Cage-Shell Consistency, structural-numerical
      level) with three clauses (i,ii,iii) stated formally
    - §5.2 mass-basis-vs-flavor-basis clarification with explicit
      proof-by-contradiction argument why flavor-basis fails
    - §5.3 numerical zeroth-order consistency: Eq:V2flavor with
      exact rational matrix elements; Proposition 5.2 (exact mu-tau
      exchange symmetry of V^2_flavor) with proof; Theorem 5.3
      (exact recovery of TBM angles from V^2_flavor) with proof
    - §5.4 structural-physical question identification with three
      framing observations
    - §5.5 Route C structural closure: §5.5.1 600-cell distance-
      shell structure (Table 5.1 with verified vertex counts),
      §5.5.2 V=4 as tetrahedral subset of shell 1 via compound-of-
      5-tetrahedra, §5.5.3 V=20 exclusion by SM-1 particle-type
      taxonomy
    - §5.6 K3-eigenmode-to-shell coupling pattern with three
      arguments: nu_2 -> V=12 forced by S_3 subset H_3 (Argument 1);
      antibonding modes split between V=4 and V=30 forced by
      broken-symmetry sign structure (Argument 2); V=4 vs V=30
      split inherits SM-5 open problem with wavefunction-spread/
      mu-tau-symmetry-character argument (Argument 3)
    - §5.7 Route C closure summary; Remark 5.4 (inheritance, not
      weakening) on SF-4's relationship to SM-5's open problem
    - §5.8 OPEN-FP-SF-4-2 status with three enumerated sub-goals
      for theorem-level closure (vertex-by-vertex K3-coupling
      theorem; antibonding-doublet split rigorous derivation tied
      to SM-5 closure; Routes A and B as alternative closures)
    Net: §5 expanded from ~30 lines stub to ~280 lines full
    paper-quality content. Foundation §0-§3 and §4 (Session 46
    v0.2) unchanged. §6-§11 closing sections still substantive
    stubs (queued for v0.4).

  v0.2 (9 May 2026 Session 46) -- §4 filled to full draft quality.
    §4.1 walk-dimension framework: Definition (walk channel),
    Definition (walk dimension), bound-vs-unbound boundary
    statement with explicit recovery of bound-mode formula
    m = M_0 V^(7/3) at sigma=1.
    §4.2 channel enumeration: 3 spatial + 1 ZBW phase + 1
    orbital orientation = d_eff = 5 with detailed text per
    channel; Remark on coarse-grained vs stochastic phase
    advance (subtlety from sketches §3.2).
    §4.3 three convergent pictures: §4.3.1 Picture A
    (two-sided DI-bit exchange) at full quality, §4.3.2
    Picture B (two ZBW half-cycles) at full quality, §4.3.3
    Picture C (edge-straddling) at full quality, §4.3.4
    cross-comparison table (Table 4.1).
    §4.4 combined result: sigma_nu = z^(-10) ≈ 1.62×10^(-11),
    predictions table (Table 4.2) with 2% sigma match / 2% nu_2
    mass / 8% nu_3 mass; note on z=12 recurrence across mass
    quantum, cage-shell vertex count, and suppression formula.
    §4.5 OPEN-FP-SF-4-1 status: Picture A formalization
    priority; sub-goals enumerated for v1.0+ work.
    Net: §4 expanded from ~65 lines stub to ~290 lines full
    paper-quality content.

  v0.1 (9 May 2026 Session 45) -- initial .tex from outline.
    Foundation sections (§0-§3) drafted at full quality with
    citations to SM-1, SM-3, SM-5, SM-7, SM-8, SM-9. Remaining
    sections shipped as substantive stubs to establish paper
    structure; v0.2 fills §4 suppression-mechanism derivation
    in full from sketches/SF-4_suppression_derivation.md;
    v0.3 fills §5 K3-Cage-Shell Consistency from sketches/
    SF-4_k3_cage_shell_consistency.md; v0.4-v0.5 fill closing
    sections; v1.0 SHIPs after Thomas review and AI review
    passes per SS-9 methodology.
============================================================
