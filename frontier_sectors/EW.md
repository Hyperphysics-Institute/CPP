<!--
  Extracted from Research_Frontier.md lines 1020-1100
  Source range: Electroweak Sector
  Extraction date: 2026-05-25
  Master dashboard: Research_Frontier.md
-->

## Electroweak Sector (EW) — 9 problems

### OPEN-EW-1: Derive η ~ 10⁻¹⁷ (Planck-to-Weak Scale Ratio)
**Status:** OPEN
**Sector(s):** EW
**Priority:** HIGHEST
**One-line statement:** Derive the hierarchy ratio η = l_P/r_EW from CPP, solving the hierarchy problem.
**What a solution looks like:** First-principles expression for η from 600-cell geometry.
**Dependencies:** None blocking (hardest single problem)
**Cross-sector connections:** OPEN-G-2
**Current best lead:** None strong. "Requires new scaling argument."
**Paper(s):** EW-2
**Note added Patch 0946 (chirality lane):** D₆ of order 12 is the stabiliser of the *bare* Petrie hexagon. Decorating it with the ruled 3 qDP + 3 eDP drops the stabiliser to order 6 (alternating), 2 (blocked) or 1 (the chiral pair) — verify `series_umbrella/series_substrate_chirality_arc/chirality_derivations/code/0946_w0_chirality_source.py` T7. The lane's D₆ statement is correct as written; any downstream argument applying D₆ to the *decorated* W⁰ needs the surviving subgroup, which depends on an arrangement the founder has not yet fixed.

> **NOTICE (Patch 4064, 16 Sep 2026).** Founder ruling: U's decoration points are additional GPs and are admissible. Cost: 61× sites, spacing 0.11–0.19 vs 0.618, coordination 2. **U is not promoted** — the corpus's reviewed route (n̂ + sign(δ), chiral dynamics on an achiral lattice) needs none of it and 4048 says geometry cannot reach V−A anyway. The chiral-lattice question is closed the way CAPACITY-1 implied. Read `series_standard_model/reasoning/4064.md`.
>
> **NOTICE (Patch 4088, 17 Sep 2026).** **SF-6 fourth-axis check: clean.** No shipped SF-6 result depends on the fourth-axis component of the DP displacement (zero references to a fourth coordinate in its derivations; the single "4D" mention is inside its own OPEN-SD-CHIR-PRIMITIVE problem statement). So χ₄'s F2 condition — EM reads 3-space only — is **free to adopt at zero cost to the corpus**, though it remains a specification, not a consequence (4086). **F5 → CKM dependency registered:** the axiom's CP-violation filter cannot close inside the chirality arc; it needs an O(1) substrate phase near 68.5° *and* the CKM mixing angles, the latter being SF-2's generation-transition problem (4087). **`manifestation_inventory.md` corrected at this patch:** (iii) EM handedness struck, (iv) causal arrow re-filed as T-odd — the umbrella has **three** genuine manifestations, not five.
>
> **NOTICE (Patch 4068, 16 Sep 2026).** **Mechanism A cannot be the chirality source.** Θ is an exact improper symmetry of its dynamics at every δ (rates depend on geometry only through e·n̂; Θ fixes both), so no functional of its NESS can split the Θ-odd bracelet helicity — the splitting is **identically zero**, verified on SF-2's 1200-ring orbit with live controls. **δ breaks T, not P.** The mechanism question is open with no candidate; the live question is *what in CPP is P-odd at all* (`TODO-4068-EW`). Erratum to 4050's |h| claim recorded there. See `series_standard_model/reasoning/4068.md`.
>
> **NOTICE (Patch 4066, 16 Sep 2026) — ERRATUM.** The chirality **mechanism** question is **OPEN** and is an EW question. n̂ alone is achiral (4046: Θ fixes it); FI-C-9 is V3 = *not yet derived*. 4064 closed only the lattice branch. **The live step is 4050's uncomputed splitting:** the W bracelet's two P-odd helicity states are exactly degenerate; whether a Mechanism-A environment (δ = φ⁻³) splits them, with what sign and magnitude, is unexecuted and needs no new GPs. See `TODO-4066-EW` and `series_standard_model/reasoning/4066.md`.
>
> **NOTICE (Patch 4063, 16 Sep 2026).** The chiral-lattice arc (4009–4054) ended with "no chiral 4D structure has been built; the gap is dimensional." **That gap is closed at cluster scale:** U = 600-cell ∪ generic H4⁺-orbit is chiral (symmetry group exactly H4⁺, exhaustive), with z = 12 on every core vertex. The earlier failures were forced by Steinberg's theorem (mirror-point orbits are achiral). The **tiling** obstruction (4019) stands and is the real foundation question; the **V−A maximality** question (4048) is now measurable on a dense 4D graph (TODO-4063-EW (1)). Read `series_standard_model/reasoning/4063.md`.
>
**Last updated:** 14 Sep 2026 (Patch 4001 — the 0945 registration renumbered `OPEN-EW-5` → `OPEN-EW-7`: it collided with the 23 March `OPEN-EW-5` in this same file. EW lane opened, block 4000–4099, G-EW-BLOCK-4000.) Earlier 13 Sep 2026 (Patch 0945 — the W mass-breakdown problem registered, from the founder's W⁰ ring ruling and the Patch 0944 bracelet harmonisation.) Earlier 23 March 2026

---

### OPEN-EW-7: W Mass-Breakdown Species Dependence
**Status:** **RESOLVED 14 Sep 2026, Patch 4002 (EW lane)** — **neither of the two pre-registered outcomes.** The breakdown is neither species-dependent nor count-dependent: every row of SM-2's table is a fixed-fraction partition of its *calibrated PDG total*, with the residual closing the sum, so nothing about the constituents enters the arithmetic. But the relabel still moves two cells, through a switch the question did not anticipate. Across all 12 rows `E_inter` is exactly 0.10 of the total or exactly 0, and the switch is set **12/12** by whether the object has a **closed polyhedral cage** — 0 for the electron, the up, the down and the former linear-chain W; 0.10 for every tetra/icosa/dodeca object. The 0945 relabel puts the W on the Petrie hexagon of the **first-shell icosahedron** (SF-2 v1.0 Thm 4.2) — the Z's own cage — so the W crosses that switch. `E_inter` 0 → 8038, residual 22774 → 14736, **total 80380 MeV unchanged**, and the W row becomes term-for-term identical to Z and Higgs. Applied to SM-2 at this patch; verify `series_standard_model/code/4002_ew7_w_breakdown.py` (all checks pass). **Soft point, stated:** the switch rule is read off the table's own 12/12 consistency, not stated in prose anywhere in SM-2. If it is rejected, two cells revert and no total moves. Earlier status: OPEN — **registered 13 Sep 2026, Patch 0945** (chirality lane, cross-lane; SM held no active ID block). **RENUMBERED FROM `OPEN-EW-5` AT PATCH 4001 (EW lane):** 0945 minted an ID that had been in continuous use in this same file since 23 March 2026 (`OPEN-EW-5: W⁰ Virtual Particle — Quantitative Properties`, below). The March entry has precedence and keeps the number; this one moves to the next free EW id. **Cite `OPEN-EW-7` from here on; `OPEN-EW-5` between 13 and 14 Sep 2026 means this problem in records written in that window.**
**Sector(s):** EW, SM
**Priority:** MEDIUM — blocks one edit of a shipped-paper corrigendum, nothing else
**One-line statement:** Does SM-2's W mass breakdown depend on the *species* of the 12 CPs in the W, or only on their count?
**Why it is open now.** The founder ruled (13 Sep 2026) that the W⁰ is a neutral 12-member ring of three qDPs and three eDPs, with W^± a W⁰ carrying a ±eCP; harmonised at Patch 0944 against this lane's W-bracelet (SF-2 v1.0 Thm 4.2 — Petrie hexagon of the first-shell icosahedron, six vertices, D₆ of order 12). SM-2's Mass Contribution Breakdown row currently reads `W & Linear 6-hDP chain & 40190 & 13397 & 0.0 & 4019 & 0.0 & 22774 & 80380`. **The member count is unchanged** — a 6-hDP chain and the W⁰ ring are both 12 CPs — so the question is whether the terms are count-driven or species-sensitive.
**What a resolution looks like:** either (i) the breakdown is species-blind and count-driven, in which case the row survives as a pure relabel and corrigendum edit (g) applies unchanged; or (ii) the hDP species enters the ZBW / inter-layer bonding / DP-cloud terms, in which case the W mass fit needs recomputation against 3 qDP + 3 eDP and the 80380 MeV total must be re-derived.
**Dependencies:** none blocking.
**Cross-sector connections:** `OPEN-EW-2` (unified boson mass formula) and `OPEN-EW-3` (the bracelet's 4D→3D projection factor, currently calibrated rather than derived) both take the bracelet as their geometric object, so a species sensitivity here would touch f_geom. The topology correction (linear chain → ring) moves SM-2 *toward* this lane's object, not away.
**Consumer:** `series_standard_model/corrigenda/SM-2_composition_corrigendum.md` edit (g), which is held pending this answer; edits (a)–(f) are independent and can be applied now.
**Paper(s):** SM-2, EW-2
**Last updated:** 13 Sep 2026

---

### OPEN-EW-2: Unified Boson Mass Formula
**Status:** OPEN
**Sector(s):** EW
**Priority:** HIGH
**One-line statement:** Single formula M_X = (sea_strength · ℏc/l_P) · f_geom(X) for all four EW bosons from subgraph geometry.
**What a solution looks like:** f_geom derivable from vertex counts and loop structure; W, Z, H at <1%; γ, g = 0.
**Dependencies:** OPEN-EW-3 (loop density), OPEN-EW-4 (mass ratios)
**Cross-sector connections:** OPEN-SS-6 (glueball shares same formula)
**Current best lead:** W, Z, H masses already reproduced at <1%.
**Paper(s):** EW-1–5
**Last updated:** 23 March 2026

---

### OPEN-EW-3: Loop Density 4D Projection Factor
**Status:** OPEN
**Sector(s):** EW
**Priority:** MEDIUM
**One-line statement:** Derive the numerical value of the 4D→3D projection factor in f_geom for the W bracelet.
**Dependencies:** None blocking
**Cross-sector connections:** OPEN-EW-2, CONJ-EW-1
**Current best lead:** Currently calibrated rather than derived.
**Paper(s):** EW-2
**Last updated:** 23 March 2026

---

### OPEN-EW-4: EW Boson Mass Ratios from Eigenvalue Ratios
**Status:** OPEN
**Sector(s):** EW
**Priority:** HIGH
**One-line statement:** Prove M_W : M_Z : M_H equals the relevant 600-cell eigenvalue combination.
**Dependencies:** None blocking
**Cross-sector connections:** sin²θ_W derivation
**Current best lead:** φ/(φ+1) = φ⁻¹ ≈ 0.618 does not match M_W/M_Z ≈ 0.882. Precise combination needed.
**Paper(s):** EW-3
**Last updated:** 23 March 2026

---

### OPEN-EW-5: W⁰ Virtual Particle — Quantitative Properties
**Status:** OPEN — **this is the original OPEN-EW-5, in this file since 23 March 2026.** Patch 0945 (13 Sep) duplicated the number on a different problem; that one was renumbered `OPEN-EW-7` at Patch 4001 and this entry is unchanged.
**Sector(s):** EW
**Priority:** MEDIUM
**One-line statement:** Derive mass, width, and coupling of CPP W⁰ before Weinberg mixing.
**Dependencies:** CONJ-EW-1
**Cross-sector connections:** sin²θ_W derivation
**Paper(s):** EW-4
**Last updated:** 23 March 2026

---

### OPEN-EW-6: Chirality from Eigenvalue-Weighted Phase Bias
**Status:** OPEN
**Sector(s):** EW
**Priority:** MEDIUM
**One-line statement:** Prove weak interaction chirality arises from phase bias in icosahedral eigenvalue-weighted loop traversal.
**Dependencies:** None blocking
**Cross-sector connections:** Parity violation, OPEN-G-2
**Current best lead:** Only one helicity couples to W loop geometry; mechanism proposed but not proved.
**Paper(s):** EW-5
**Last updated:** 23 March 2026

---

**[Patch 0743 — physical cartoon recorded (not yet absorbed): B field as rotating DPs.** A moving charge radially polarizes the DPs (radial pole displacement = E) and swings each DP's like-pole around an axis (rotation = B) — so there is no separate B field, only rotating DPs; E and B are two motions of one DP response (hence μ₀,ε₀ share one stiffness, reinforcing the Patch 0740 Z₀-geometric result). The mathematical form exists in the corpus (EW-5 SSV-curl field strength; c06 B=curl-of-pattern); the **mechanical cartoon does NOT** — captured in `series_electroweak/development/b_field_as_rotating_dp_physical_cartoon.md` (Thomas's interpretation, w/ Grok). Small EM-sector task to fold it formally into EW-1 (Maxwell derivation) / c06 as the physical paragraph under the math.]**

**[Patch 2926 — arc queue item CLOSED: c = 1/5 DERIVED ANALYTICALLY.** The 2884/2900 round-trip drive admits an exact closed form — the outgoing-leg discriminant is a perfect square, d_out = r(1+2βμ+β²)/(1−β²), radial/angular dependence factorizes exactly (deriving the measured m- and r-range invariance), and D(β) = 2πR_m Σ 8β^{2n+1}/[(2n−1)(2n+1)(2n+3)] — the second difference of the even sphere moments. **c = 1/5 EXACT; c₄ = 1/35 exact (7/240 candidate REFUTED — fit-truncation artifact, explained to 3×10⁻⁵); c_{2n} = 3/[(2n−1)(2n+1)(2n+3)].** Confronted with the banked direct bound c = +0.91 ± 2.40 (Patch 2924): consistent. Sharper targets inherited by the entrainment cancellation programme and OPEN-HYB-SHAPE-1. Record: `flagship_papers/electromagnetism/sketches/c_one_fifth_analytic_derivation.md`; script `code/2926_c_one_fifth_derivation.py`. Sketch-tier per arc precedent; no items opened/closed; ledger untouched.]**

**[Patch 2927 — entrainment cancellation NON-UNIVERSAL; entrained drive closed-form through O(ε²).** The 2900 cancellation point ε* = 0.0589 was measured at one configuration; across the six robustness configs it spans 0.00735–0.44620 (×61). Exact theory: D(β;ε) = 2π[R_mΦ + εR_{m+3}Ψ + ε²R_{m+6}X] + O(ε³) with ψ₃(m) = −8(4m+1)/3, χ₃(m) = −4(m+1)(113m+22)/15; ε* = smallest positive root of R_mφ₃ + εR_{m+3}ψ₃ + ε²R_{m+6}χ₃ = 0 — a structure-tuned condition coupling the kinematic rationals to where the Sea's response lives (effective expansion parameter ~ε/r³ₘᵢₙ). Direction (A)'s burden is now a fixed-point statement against exact targets at all β-orders. Record: `flagship_papers/electromagnetism/sketches/entrainment_nonuniversality_record.md`; script `code/2927_entrainment_nonuniversality.py`. Sketch-tier; no items opened/closed; ledger untouched.]**

**[Patch 2928 — the 2900 registered prediction c₄ → 0 under full self-consistency REFUTED for the displacement-field fixed-point closure, both return conventions.** SC closure δ = ε·amp(y+δ)·û(y+δ) iterated to fixed point: ε*_SC = 0.0422 (V1) / 0.0207 (V2) with c₄(ε*_SC) = −0.923 / −0.612 — self-consistency makes the β⁴ pathology 2.5× WORSE than one-shot (−0.373), not zero; c = 0 and c₄ = 0 do not coincide in either variant. The map has a finite basin (ε_conv ≈ 0.0658, variant-independent); the one-shot ε* = 0.0589 sits barely inside it. Both cheap routes to Newton I (universal dial, 2927; dressed dial, 2928) are now closed by measurement; direction (A) survives only as a travelling steady state with Sea-side (DP–DP) coupling — connecting to OPEN-EW-ANTISCREEN-1 as the one measured piece of collective Sea physics. Record: `flagship_papers/electromagnetism/sketches/sc_entrainment_c4_refutation.md`; script `code/2928_sc_entrainment_c4_confrontation.py`. Sketch-tier; no items opened/closed; ledger untouched.]**

### OPEN-EW-ANTISCREEN-1: Collective Anti-Screening of the Bonded ZBW Sea
**Status:** OPEN
**Sector(s):** EW, SD
**Priority:** HIGH
**One-line statement:** The bonded ZBW Sea's persistent static response to a +1 source is polarization-REVERSED (+ member leans toward the source) while an isolated pair polarizes normally — derive the many-body inversion mechanism.
**Dependencies:** None blocking (measured; convention audited clean at Patch 2918)
**Cross-sector connections:** Statics rebuild (suspended 2892); ε₀/screening story of SF-6; the β⁰ core of the co-moving pattern (Patch 2917–2922 anatomy)
**Current best lead:** Founder-physics question candidate — what in the pair–pair ZBW bonding inverts the collective polarization? Data: `flagship_papers/electromagnetism/data/2918_control_fields.json`.
**Paper(s):** SF-6 successor / SF-8
**Registered:** Patch 2918; frontier entry Patch 2925.
**Last updated:** 1 August 2026

---

### OPEN-HYB-SHAPE-1: Hybrid Pipeline High-β Shape Failure — Mechanism Unidentified
**Status:** OPEN
**Sector(s):** EW, WORKFLOW
**Priority:** MEDIUM (deprioritized: the direct instrument answers the arc's question)
**One-line statement:** The hybrid Stage-2 drive turns over at β ≈ 0.15 while the direct measurement shows sustained growing drive through β = 0.30 (12σ sign-level refutation at Patch 2924) — identify the hybrid's high-β failure mechanism.
**Dependencies:** None blocking
**Cross-sector connections:** OPEN-K1-MEMORY-1 adjacency (pattern-window convergence); the parity-defect class (Patch 2920)
**Current best lead:** Prime suspect (window-support truncation growing with β) tested and KILLED at Patch 2924 §2. Remaining candidates: co-moving pattern non-convergence at short T; β³ basis leakage; kernel-weighted truncation.
**Paper(s):** none yet
**Registered:** Patch 2924; frontier entry Patch 2925.
**Last updated:** 1 August 2026

---

### CLOSED-EW-NOTE-001: δ_CP ≈ 65.5° is not a 600-cell vertex-vertex angle (filed Patch 4097, 18 Sep 2026)

**Status:** CLOSED — negative result filed per Thomas's instruction, session 233.

The genuine 120-vertex 600-cell has vertex-vertex angles only at multiples of 36°: {36°, 60°, 72°, 90°, 108°, 120°, 144°, 180°}. The CKM phase δ_CP = 65.5° ± 3.3° does not match any of them (closest: 60° at −1.67σ, 72° at +1.97σ). An earlier apparent 66.1° hit was from a 216-vertex non-standard build — not a genuine 600-cell angle.

**Consequence:** the simplest route to δ_CP from 600-cell geometry is closed. Derivation belongs to OPEN-SM-11. *(This line originally read "SF-2's generation-transition structure"; no such structure exists — corrected at Patch 4102, which found SF-2 is explicitly generation-BLIND and routes δ_CP^(CKM) through the Capotauro phase factor instead.)* Two bracketing angles (60°, 72°) suggest the CP phase may come from a combination of inter-shell transition angles in SF-2's framework.

**Filed in:** axiom_maturation.md §2aa, reasoning/4096.md, OPEN-SM-11, todolist.md TODO-4097-R2.

---

### DP-CAL-1: sea-DP internal configuration — a NAMED CALIBRATION, not a derivation (registered Patch 4107)

**Status:** ADOPTED as a calibration on founder instruction (18 Sep 2026). **Sector(s):** EW, QM, CHIR.
**One-line statement:** A ground-state sea DP has its two CPs' ZBW spins **strongly biased antiparallel** (not exactly antiparallel) and their DP arc cohorts **opposed**.

**RESTATED at Patch 4122 on founder correction:** *"The helical bit's orientation will be most strongly biased antiparallel by its pair, but it will not be exact because of the influence of the Di-bits from the DP Sea"*, and *"vacuum-state magnetism should not be exactly zero on a finite scale because of charge motion."* DP-CAL-1 is therefore a **bias with a residual**, not an identity. F2's cancellation is **bounded, not exact**: the residual is δ/π per DP for sea-induced misalignment δ, giving δ < ~3e−10 rad in the coherent channel and effectively no constraint if sea contributions are incoherent (TODO-4122-COHERENCE).

**Provenance, split by rigor:**
- **Arc cohorts opposed — DERIVED.** SF-6 derives EM from eDP-Sea Polarization; polarizing a dipole displaces its +CP and −CP in opposite directions by definition; Patch 4097 makes the arc cohort the product of that displacement. Not a free choice.
- **Spins antiparallel — CALIBRATED.** The founder states plainly that no spin has ever been assigned to any CP (`founders_voice/4107_ruling_dp_spin_calibration_turn.md`). He assumes antiparallel and directed that the F2-supportive value be carried forward as a first point of evidence, then tested against the corpus.

**What it buys:** F2 (EM stays P-even under χ₄) holds exactly and pointwise, R = q(b₊−b₋) = 0. The Patch 4106 falsifier is not triggered.

**Supporting empirics (Patch 4107 sweep):** bosonic DP sea (spin 0); **no ferromagnetic vacuum** (parallel spins would magnetise the vacuum — the sharpest of the four); R-F3 wants the same underlying principle. No contradiction found anywhere in the sweep.

**What would overturn it:** any corpus result requiring parallel sea-DP spins. A demonstration that a ground-state sea DP has no arc cohort at all would *also* save F2, by a third route.

**Why it is registered here:** a calibration carried forward silently becomes a premise nobody audits — the failure mode this lane hit at Patch 4102. DP-CAL-1 is named so a future worker can find it and test it rather than inherit it as fact.

**Registered:** Patch 4107, 18 Sep 2026.

---