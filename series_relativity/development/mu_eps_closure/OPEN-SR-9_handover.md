# HANDOVER — OPEN-SR-9: DP-Sea EM-Emergence & the From-Substrate Impedance Verdict

**Purpose:** start a fresh window on OPEN-SR-9, the EM-emergence mechanism that grounds the R2
vacuum-impedance falsifier *unconditionally* (from the substrate), rather than at the field-content level
where R2 currently rests. Written 22 June 2026, building on origin HEAD 2043. Worker derives; TLA = founder's
eye on the c06 EM-emergence mechanism. **Read the scope doc first:**
`series_relativity/development/mu_eps_closure/OPEN-SR-9_em_emergence_scope.md`.

---

## 0. Orientation — where R2 left this

R2 (the μ↔ε / Δc-LPI falsifier: does Z₀=√(μ₀/ε₀) stay geometric so α doesn't drift) is now **PASS
conditional, both conditions met WITHIN the audited LSP field content** (frontier_sectors/SR.md OPEN-SR-9,
Patch 2041 update; `mu_eps_closure/R2-STATUS.md`): VTD-1 cleared at SR-1 strength (2037/2038, panel P1-SOUND
×4), and the f(C,Σ) anisotropy attack closed at the field-content level (scalar SSV_abs sets c_photon, 2028;
~11-order locality residual, 2029; no-rank-2 static completeness, 2030/2031; A3′ rank-2 Q_ij static-null by
OB-3). **OPEN-SR-9 is the UNCONDITIONAL route**: derive the same verdict directly from the DP-Sea EM-emergence,
so R2's PASS no longer leans on the field-content audit being the whole story.

## 1. The mission (what must be derived) — three coupled sub-questions

From the scope doc:
1. **Emergence.** What collective excitation of the DP Sea *is* the photon — gapless, transverse, helicity-1
   (NOT the acoustic/phonon mode; Patch 2011 + 2024 established photon≠phonon) — and what is its effective
   action `L = ½ C P² + ½ K (∇×P)² + …` with **both** the electric (C) and magnetic-curl (K) coefficients
   derived from **one** microscopic c06 Lagrangian, not posited.
2. **VSL channel identity.** Which substrate parameter does variable-c actually vary — the DP stiffness C (as
   the old 2002 c∝√C assumed), the bare Coulomb coupling, or the kinematic PSR (0738/0746)? Show whether
   these are one channel or distinct.
3. **ε₀/μ₀ symmetry.** Does that channel enter the on-site polarizability ε₀ and the propagation μ₀
   **symmetrically** (⇒ Z₀ geometric, A=0, R2 PASS) or asymmetrically (⇒ Z₀ carries the channel, A≠0, FAIL by
   ~6 orders)?

## 2. THE decisive computation (do this first — it is panel-unanimous, 2040)

Two strains at **identical local scalar C** — one **anisotropic** (velocity-like), one **isotropic**
(gravity-like) — compute the **photon-mode speed** from the *emerged* EM action (not from the field-content
argument):
- **Equal ⇒ universality grounded from substrate ⇒ R2 → UNCONDITIONAL PASS.**
- **Differ ⇒ R2 reopens** (the field-content argument was necessary but not sufficient; birefringence is real
  in the substrate after all).

This is the from-substrate test of exactly the scalar-channel claim that 2028–2031 + founders_vision (22 Jun)
established at the field-content level. The handover's whole point is to settle it by *derivation*, not audit.

### §2-RESULT (Patch 2050) — crux sharpened, founder-adjudicated, computation run

**Sharpened crux (founder §10, 2050).** The decisive computation reduces from "compute two strains" to a single
mechanism question: *does the magnetic curl-coupling K enter the photon's advance, so c_b inherits K_ij under
anisotropic strain — or is the advance set by the scalar PSR alone?* This is the two-strain verdict stated at
the level of the PCD machinery (kinematic budget speed c=PSR/t_P vs constitutive wave speed c=1/√(με)).

**TLA adjudication (2050, captured verbatim in `em_emergence/reasoning/2050_*.md` §1).** Purely scalar-PSR. The
B-channel is non-fundamental — an artifact of charge motion through the DP Sea; the DP rotational motion is
SSV-neutral, so B contributes zero SSV, hence zero to PSR. There is **one** independent stiffness: the E/SSV
scalar channel. ⇒ K does NOT enter the advance.

**Computation (`em_emergence/verify/sr9_dispersion_two_strain.py`).** EM-form action
L = ½ε₀Ṗ² − ½(1/μ₀)(∇×P)², C entering as the polarizability ε₀∝1/C in the kinetic term (gapless photon; the
on-site-mass reading is the gapped phonon-side object). Both branches computed:
- B independent → c_∥≠c_⊥ → birefringence → **DIFFER → reopen** (the live kill branch, shown explicitly);
- B non-fundamental (TLA) → one photon ⇒ lock **1/μ₀ = ε₀c_b²** ⇒ μ₀ slaved to scalar c_b ⇒ c_∥=c_⊥=c_b ⇒
  **EQUAL → PASS**, with Z₀ = 1/(ε₀c_b) → (ε₀=k_e/C, c_b∝C) → **C cancels → Z₀ geometric**.

**Status: the two-strain test returns EQUAL ⇒ R2 → unconditional-PASS, CONTINGENT on "B carries no SSV."** This
is a status move and is **DEFERRED to TLA pending CONV-001 panel.** Two honest residuals carry forward: (1) the
panel must stress-test whether B is *exactly* SSV-neutral or only to leading order (a 2nd-order rotational SSV
re-admits a small K_ij / sub-leading birefringence to bound against the 2029 LPI limit); (2) the full
across-C-range claim still imports c_b∝C from the 2025 Lorentz argument — the lock reduces the remaining
substrate obligation to deriving c_b(C) (the ΔSSV↔C relation), the recommended next work item.

### §2-VERDICT (Patch 2051) — CONV-001 returned UNANIMOUS HOLED; close NOT adopted

Panel (ChatGPT, Grok, Gemini, Copilot), adversarial/full-inline/history-disclosed: **HOLED, unanimous.** The
2050 EQUAL→PASS is **NOT adopted**; **R2 remains at conditional-PASS** (audited field-content level). One hole,
two faces: (Face 1) the scalar-PSR-only advance — "B carries zero SSV" — is *adjudicated, not derived*; a
2nd-order rotational SSV re-admits K_ij → birefringence → DIFFER → reopen; (Face 2) the lock 1/μ₀=ε₀c_b² is
*imposed after* the action, not derived from it (Grok: circular — isotropy assumed to define μ₀, then "proved"
via that μ₀). Same hole: Face 2's lock is legitimate only if Face 1 holds exactly. Survived panel: algebra
clean (4/4); mode identification (gapless photon vs gapped phonon, C→ε₀) NOT the hole; conditional structure
intact (IF exact neutrality THEN EQUAL). Net: 2050 *reduces* the close to one decidable question, does not
achieve it. **Next work item OPEN-SR-9-B** (charter: `em_emergence/OPEN-SR-9-B_velocity_emergence_charter.md`,
opened Patch 2052): establish **velocity as holographically emergent** from a fixed SSV-only GP update rule
(swarm + theorem, exactly as B-emergence was) — NOT a velocity-insensitivity *axiom* (founder-corrected at 2052:
that multiplies axioms; the positive claim is the load-bearing one, and velocity-insensitivity descends as a
corollary). Spine = **Obligation A** (exact γ + the Michelson–Morley undetectability conspiracy, from the
`velocity_ssv_time_dilation/` arc) — selected as the phenomenon most likely to *break* emergence (CPP has a real
preferred frame [c01] that must be made exactly undetectable against a ~10⁻¹⁸ null). First brick: derive the
relativity of simultaneity (exact γvx/c²) from the fixed rule + a no-hidden-velocity audit; then close
contraction + dilation + resync to exact Lorentz on one rule. Once it lands, **B-neutrality becomes a theorem**
(not adjudication), both CONV-001 hole-faces close, and R2's geometric Z₀ descends as a corollary; the same
brick also retro-grounds SR-1 + VTD-1. NB the 2051 §4 "compute 2nd-order rotational SSV" framing is SUPERSEDED
(mis-posed — presumes a velocity-channel the emergence claim dissolves); see the 2051 CORRECTION note. R2 stays
conditional-PASS until the charter closes. Needs a TLA consult on the GP update rule's explicit form (the
simultaneity-resync mechanism).

## 3. THE central integrity risk — read twice

**A self-built lattice action can cancel C by construction.** The registration says this in as many words, and
it is the dominant failure mode: it is trivially easy to write an effective action that returns geometric Z₀
because you built it to. The discipline that ran the R2 arc applies at maximum strength here:
- The action's C and K coefficients must come from the **c06 microscopic Lagrangian** by honest derivation —
  show the work from the DP-chaining dynamics, not a posited L with the answer baked in.
- Run the two-strain computation **before** deciding what you hope it shows; report equal/differ as it falls.
- If you find yourself choosing an action *because* it gives geometric Z₀, stop — that is the tasting failure.
- Adversarial CONV-001 panel review (full inline, neutral, history disclosed) on the emergence construction
  AND the two-strain verdict, before any status move on R2.

## 4. Deliverables (scope doc)

- The EM-emergence construction: gapless transverse helicity-1 mode of the DP Sea, effective action with C and
  K from one microscopic Lagrangian.
- A grounded decision on the VSL channel identity (stiffness vs bare-coupling vs PSR), from 0738/0746/c06.
- The impedance result: Z₀ in lattice units shown C-independent (pure 600-cell geometry ⇒ PASS) or C-dependent
  (⇒ FAIL), with the ε₀/μ₀ symmetry of the VSL channel established either way — plus the two-strain verdict.
- Downstream: bound the scale-dependent screening correction <10⁻⁶; round-3 adversarial panel.

## 5. Starting plan

1. **Read** the scope doc; `R2-STATUS.md` (full ladder, esp. 2024–2031 + the 2037–2043 tail); the
   field-content resolution files in `em_emergence/` (R2-RESOLUTION-VIA-LORENTZ, UNIVERSALITY-GROUNDED-SCALAR-
   SSV, C07-STATIC-COMPLETENESS-RESOLVED) so the from-substrate computation can be checked against the
   field-content argument it must reproduce or overturn.
2. **Read c06** (`series_relativity/SR_companion_papers/c06_DP_chaining_as_mass_and_EM_substrate/`): B=∇×P
   field-strength math (line 91) and the owed μ₀,ε₀(C,c) computation (line 185) — this is where the emergence
   action must come from. Also EW-5 (emergent F=∂A−∂A) and c02 (fixed ω_ZBW, for μ_DP=C/ω_ZBW²).
3. **Construct** the gapless transverse mode + effective action, C and K from the one Lagrangian. Founder
   consult (TLA) on the c06 mechanism where the construction needs adjudication.
4. **Run the two-strain computation** (§2). Report as it falls.
5. **CONV-001 panel** on construction + verdict. Then move R2 status only if earned.

## 6. Dependencies, environment, definition of done

- **Dependencies:** c06, EW-5, 0738/0746 (VSL/PSR channel input), c02; Patches 2002–2011 (R2 arc), 2024–2043
  (R2 field-content closure + VTD-1).
- **Environment/protocols:** unchanged — see `velocity_ssv_time_dilation/VTD-1_handover.md` §5 (repo, container
  clone, owned greenfield paths, defer shared-registry edits — incl. SR.md OPEN-SR-9 registration, R2-STATUS,
  CONJ.md — to TLA, precautionary apply-and-push macro, verify clean apply before presenting). **Patch band:
  the 2000-band is in active multi-window use (HEAD 2043); confirm a free band/number with TLA before
  committing — do NOT assume 2044 is yours.** Reasoning-capture protocol incl. **§10 founder-contribution
  capture** (verbatim TLA blocks; run `templates/sweep_founder_contributions.sh` at close).
- **Done when:** the EM-emergence construction is derived (C,K from one c06 Lagrangian, not posited); the
  two-strain verdict is computed and panel-reviewed; the VSL channel identity is decided; and R2's status is
  updated to unconditional-PASS (equal) or reopened (differ) — with the anti-tasting guard documented and the
  construction NOT reverse-engineered to the desired Z₀.

NO THEO at the worker level (conditional results; defer all axiom/registry moves to TLA). The prize: R2 stops
being conditional-on-field-content and becomes a from-substrate verdict — the last kill-or-confirm of the VSL
early-universe horizon mechanism that EU-1 rests on.
