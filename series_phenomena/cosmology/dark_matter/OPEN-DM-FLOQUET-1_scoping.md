# OPEN-DM-FLOQUET-1 — the transverse charge-switched bending eigenvalue on geometry #3 (the make-or-break, scoped)

**Registered:** Patch 2438, 11 July 2026 (Opus, DM lane). **Status:** OPEN, blocking candidate (B)'s make-or-break.
**Supersedes as the operative computation:** every cheaper route tried in 2426–2435 (isotropic assumption, gradient
read, axial average, charge-switching truncation) — all either failed CONV-001 review or reproduced worker bias.
**This doc pins exactly what must be computed and the guardrails that would have caught each prior failure.** No
shortcut is authorized; a result that skips any Required Element below is not an answer to OPEN-DM-FLOQUET-1.

## 0. The single blocking question
On geometry #3 (uniform axial spacing d; 8-qCP cube core at radius r_q; 8-eCP shell at R_e > r_q; opposite polarity
plane-to-plane; eCP–qCP–qCP–eCP diagonals), with the qCP core dynamically stabilized (jello/Earnshaw + ZBW +
charge-switching), **is the rod's effective TRANSVERSE bending modulus κ_θ large enough that κ_θ/E_bond ≥ 0.43?**
- ≥ 0.43 → candidate (B) survives (as a ring family at whatever N_stab = c·κ_θ/E_bond gives; N=8 specifically out).
- < 0.43 → soft → light rings form → DD-excluded → falsified.
- non-convergent / unresolvable → honestly UNRESOLVED (no default to either side).

## 1. The object to compute (precise definition)
κ_θ ≡ the second variation of the TIME-AVERAGED (secular/Floquet) energy of the rod with respect to a transverse
BENDING deformation of the rod axis, evaluated at the DRIVEN dynamical equilibrium of the ZBW + charge-switching
lattice, expressed as the lowest bending eigenvalue:

    κ_θ = min-bending-eigenvalue of  δ²E_sec[ρ] / δκ²  |_(driven equilibrium)

where E_sec is the cycle-averaged Coulomb energy over the full ZBW + charge-switching dynamics (BOTH charge phases),
ρ is the driven stationary distribution over configurations, and κ is the imposed rod-axis curvature. E_bond is the
axial fragmentation-bond depth for the SAME failure coordinate whose curvature enters κ_θ.

## 2. Required Elements (each is mandatory; skipping any voids the result)
- **R1 — Driven equilibrium.** Solve the lattice-stabilized separations (r_q, R_e, d) and CP trajectories
  self-consistently under ZBW + charge-switching, i.e. find where the SECULAR force vanishes. (2430/2434 evaluated
  at a hand-set site where |E|≠0 — non-equilibrium; that is disqualified.)
- **R2 — Dynamical duty cycle δ.** The stationary distribution over charge configurations under the driven
  dynamics. The combinatorial 3/7 (Patch 2435) is a UNIFORM-sampling UPPER BOUND, not the value. δ must come from
  the transition rates / residence times (or a rigorous detailed-balance argument that uniform holds).
- **R3 — Both charge phases.** E_sec must average the same-charge (repulsive, +curvature) AND opposite-charge
  (attractive, −curvature) intervals. (2434 dropped the (1−δ) opposite-charge term; the honest static average is
  (2δ−1), NEGATIVE at δ=3/7 — that truncation is the exact error being fixed.)
- **R4 — Transverse mode, not axial.** The bending eigenvalue is TRANSVERSE. It must be computed as such and shown
  distinct from the axial stiffness. (2434 substituted axial curvature ×x² for the bending mode — disqualified by
  2430's Laplace lesson: axial and transverse curvatures differ in sign.)
- **R5 — Netted, not stacked.** κ_θ = the lowest eigenvalue of the FULL secular Hessian = K_switch + K_ponderomotive
  + K_structural for the SAME mode at the SAME equilibrium. The charge-switching term must be NETTED against the
  2430 ponderomotive tensor (eigenvalues [−190,+173,+292] on the old geometry), not added on top of an unaddressed
  negative contribution. Recompute the ponderomotive tensor on geometry #3.
- **R6 — E_bond branch derived.** Which axial bond fragments first (E_qq core ~66 MeV vs E_ee coat ~0.49–1.25 MeV,
  a factor α_s/α ≈ 53) must be DERIVED from the fragmentation coordinate, not selected. The registered 2424 value
  used E_ee; 2434 used E_qq without justification.
- **R7 — Deformation-correlation, if invoked.** If any "both phases restoring" argument is used (same-charge resists
  compression, opposite resists tension), the switching law must be DERIVED to be correlated with the deformation
  (a ratchet/Floquet mechanism with phase and cycle work). With a deformation-UNCORRELATED δ it does not hold.

## 3. Anti-bias guardrails (verification battery the computation MUST pass)
Each guardrail names a specific prior failure it prevents. A result must report ALL of these, pass or fail.
- **G1 (both-phases limit check):** the method must reproduce δ→0 ⇒ pure-attraction Earnshaw-NEGATIVE and δ→1 ⇒
  pure-repulsion POSITIVE. A method that gives positive stiffness at δ→0 has dropped the attractive phase. [catches
  the 2434 truncation]
- **G2 (transverse ≠ axial):** report BOTH the axial and the transverse eigenvalues; the ratio uses the transverse.
  If they're equal, prove it; don't assume it. [catches the 2434 axial substitution]
- **G3 (equilibrium check):** report |secular force| at the evaluation point; it must be ≈ 0. [catches the
  2430/2434 non-equilibrium site]
- **G4 (netting check):** report K_switch, K_ponderomotive, K_structural separately AND their sum; removing any one
  must change the reported κ_θ. [catches stacking a positive term on an unaddressed negative one]
- **G5 (δ upper-bound honesty):** report both the uniform 3/7 upper bound AND the dynamical δ; if they differ, the
  dynamical one governs. [catches quoting the upper bound as the value]
- **G6 (branch honesty):** report the ratio for BOTH E_bond branches AND the derivation of which governs. [catches
  the deep-branch cherry-pick]
- **G7 (pre-registered sign):** it is stated NOW, before the computation, that a negative or sub-0.43 transverse
  eigenvalue will be reported as FAIL/UNRESOLVED and NOT re-truncated, re-parametrized, or re-geometried into
  survival. Any post-hoc geometry change to rescue a failing result must go through CONV-001 as a new round.

## 4. Method (multi-session; not a single-patch job)
Candidate approaches, in increasing rigor: (a) reduced Floquet–Mathieu analysis of the dominant bending mode
(analytic, gives the sign and rough magnitude); (b) molecular-dynamics / kinetic-Monte-Carlo of the ZBW +
charge-switching lattice with the secular bending Hessian extracted numerically at the self-consistent equilibrium;
(c) a rigorous variational lower bound on the lowest transverse bending eigenvalue. Recommended order: (a) to fix
the sign honestly (with G1–G7), then (b) for the magnitude if (a) is favorable. This is explicitly scoped as
multi-session; no pressure to force a single-patch number — that pressure is what produced the 2434 shortcut.

## 5. Decision rule (pre-registered)
Let κ_θ* = the transverse bending eigenvalue from R1–R5, E_bond* = the branch from R6.
- κ_θ*/E_bond* ≥ 0.43 → SURVIVES; register the ring family at N_stab = c·(κ_θ*/E_bond*), rerun DD at that mass.
- κ_θ*/E_bond* < 0.43 → FALSIFIED (light rings, DD-excluded).
- R1–R5 non-convergent → UNRESOLVED; do not default.
Ω_DM is not built until this resolves and (if survives) DD is rerun at the resulting mass.

## 6. Provenance / why this doc exists
Candidate (B) is the last DM-core coring survivor. Its make-or-break κ_θ/E_bond has been attempted four times this
session and each attempt was either refuted by CONV-001 or found to reproduce worker bias toward the founder's
lean (2437 adjudication; 3/5 seats flagged motivated reasoning). The honest state is UNRESOLVED. This scoping doc
converts the flailing into a disciplined specification so the next attempt is bias-guarded. Related open items:
OPEN-SS-43 (parent), OPEN-DM-CAPTURE-1, OPEN-COSMO-DM-1..4.

## 7. Progress log
- **Method (a) — sign — COMPLETE (Patch 2440, 12 July 2026).** Meissner (square-wave Floquet) analysis of the
  transverse mode. **G1 PASS.** Result: **sign is CONDITIONAL and NARROW.** The statically-inverted δ=3/7 mode is
  stabilized only inside ε ∈ ~[0.18, 0.43] (ω_sw/ω_A ~ 1.5–2.4); the fast-switching limit is UNSTABLE (the naive
  ponderomotive expectation fails — negative static average O(ε) dominates the O(ε²) gain). In-band recovery is
  modest (~0.12·A mid-band). Levers: branch asymmetry ε_att/ε_rep<1 helps (R6); dynamical δ likely ≤ 3/7 keeps it
  narrow (R2). **NOT-YET-FALSIFIED; survival NOT demonstrated; registry not promoted.** The sign now hinges on
  R1/R2 (does substrate ε,δ fall in-window), R6 (branch), and decisively R5/G4 (net against the recomputed geom-#3
  ponderomotive tensor — 2430 analog had a −190 transverse eigenvalue). See `floquet_method_a_sign_result.md`,
  `reasoning/2440.md`, `code/2440_floquet_method_a_sign.py`. **Next: R1 (driven equilibrium) → R5 (net).**
- **R1 — driven equilibrium — SCOPED (Patch 2441, 12 July 2026).** Setup + order-level ε map in
  `R1_geom3_driven_equilibrium_scoping.md` (`code/2441_r1_eps_scale_estimate.py`, `reasoning/2441.md`). Using
  ω_sw = the "SU(3)-type ZBW hop" (Compton-scale) [reasoning/2435], the sign question is **branch-dependent**: only
  the **deep E_qq core + qDP-hop** corner lands ε ≈ 0.21 in the method-(a) window [0.18,0.43]; shallow-E_ee and
  eDP-hop corners are deep in the unstable (too-fast) region. Favorable corner is **plausible, not established**
  (±30% in E_qq spans unstable ↔ in-window). Two decisive R1 sub-questions, both to be **derived**: (1) R6/G6 which
  bond fragments (only deep-core is in-window); (2) the effective ω_sw (qDP-hop vs eDP-hop vs residence-suppressed).
  R5/G4 netting still gates the final sign. **Next: full self-consistent R1 solve (branch derived; ω_sw from
  residence times) → R5.**


## §7 — FORK-SWITCH-1 (registered Patch 2452, 13 July 2026; founder-gated adjudication)

**The switching-process reading fork, discovered by the R1 in-situ solve's own mean-force diagnostic.** The corpus holds two readings of the δ=3/7 charge-switching:

- **(ANCHORED)** Pattern-anchored excursions: each pair spends (1−δ)=4/7 in its PATTERN product state, 3/7 flipped. This is the reading every quantitative patch since 2437 uses — E_static = (1−2δ)·(pattern) is only correct here. The jello property (2435) supplies broad excursion statistics about the pattern (yielding the combinatorial 3/7) without erasing the pattern the lattice is made of. Under ANCHORED the R1 drive is a coherent duty-3/7 alternation; the resonance-resolved response stabilizes the candidate on the central E_qq branch under clock readings C1 (bridgeable ×0.87, K_switch tongue-IN) and C2 (×1.62 fully), and kills under C3 (two-hop).
- **(UNIFORM)** 2435-literal uniform sampling of neutral configs: ⟨cᵢcⱼ⟩ = −1/7 for all intra-element pairs (pattern-independent), 0 inter-element. Demonstrated (2452 simulation): this breaks the arc's registered E_static convention (mean-force ratio 5.76 vs required 1.0) AND its stochastic spectrum is adiabatic-dominated (net λ_q ≈ −7×10⁻³, kills). UNIFORM-literal is therefore internally inconsistent with the 2437–2451 quantitative arc — evidence for ANCHORED, but adjudication belongs to the founder/panel, not Opus.

**Sub-fork (clock counting, C1 vs C2):** one collective pattern↔flipped alternation per Compton period (ħω₁=264; founder's 90/180/270 deterministic-cycle language leans this way) vs independent-DP flips at rate 12/7 per period (ħω₁=226.3). C3 (two hops/period, ħω₁=452.6) kills everywhere and is least natural against the glossary's one-oscillation-per-period ZBW. All shown in `code/2452_r1_insitu_solve.py`; none selected.

**Consumers:** the OPEN-DM-FLOQUET-1 verdict (directly); the arc's E_static convention corpus-wide within this campaign (via the UNIFORM branch's inconsistency). **Adjudication route:** CONV-001 packet (2450+2451+2452) or founder ruling. **Status: OPEN, founder-gated.**


### §7.1 — RECAST (Patch 2453, 13 July 2026, on founder input — verbatim question in reasoning/2453.md)
The founder identified the reading the §7 binary missed: **COHERENT-CYCLE** — SU(3)-type position switching as the PRIMARY dynamics (the hTetra observation; jello core per 2433; deterministic cycle per 1811), stiffening from the same-charge-repulsive vs opposite-charge-attractive apposition tension (which is 2434's own κ_θ = δ·Σk_rep·x² mechanism — the arc's mechanism was always the founder's; the pattern-STATICS underneath it were the drift). Reading space now: {ANCHORED (arc convention), **COHERENT-CYCLE (founder-favored, computed 2453)**, UNIFORM-INCOHERENT (ruled out)}. Computed map (2453): intra-element statics = the exact −1/7 all-attractive web (cohesive, E0 ≈ −1.8 GeV); inter-element phase-lock DERIVED by energy minimization (conjugated); **ROBUST across lock/coat brackets: ring statically BELOW straight (−29 to −55 MeV), closure downhill, bend negative (formation easy)**; NOT robust: tilt sign (set by the lock: +69159 derived-lock vs −16560 independent); dynamic channel valid-and-positive only for FAST (~Compton-rate) cycles — slower supercycles are nonlinear-invalid (quiver > spacing), unresolved not negative. **The decisive object is the CONCRETE CYCLE** (period + inter-element coherence): founder specification or panel adjudication closes tilt and the dynamic channel together. E_qq pin still owed (sets the fast-cycle validity boundary ~150 MeV).


### §7.2 — RESOLUTION PATH (Patch 2454, 13 July 2026): the founder's concrete cycle
The founder specified the dynamics (verbatim in reasoning/2454.md): home-anchored ZBW rebound dance — each CP perpetually oscillates home→opposite-partner→home (superposition-rebound, 2433), next leg to a different partner, SSV-guided, with contention preemption. Implemented (v3) after two diagnostic-forced corrections (uniform-choice decorrelates — erases SSV guidance; exchange-per-leg contradicts "reverse direction"). Under it ONE object answers stability: the mode-resolved mean dance energy (BO-valid; the 2453 linear-response validity problem dissolves). **Results: ring−straight −33..−104 MeV across the full sensitivity grid (partners 5/7 × regularization floor/soft 0.05–0.30 fm) — third independent confirmation; closure downhill; the ring's own modes: ellipticity + uniform tilt STABLE, tilt waves m=1,2 MARGINAL (0 to −1080±688, ~100× below the straight rod's), breathing registry-pinned (standing scope). Straight-rod instabilities reframed as formation-path (2447).** Named inputs remaining: saturation scale a; partner count 5 vs 6–7; rebound confirmation; coat-diagonal geometry confirmation; speed∝SSV refinement; registry-stiffness channel (order-level +15k dominance argument, flagged). **Status: FORK-SWITCH-1 resolution proposed via the founder's dynamics; CONV-001 packet 2450–2454 recommended. Candidate (B) → ~70%, leaning-SURVIVES at this treatment level, UNPROMOTED.**
