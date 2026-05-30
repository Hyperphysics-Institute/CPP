# B-iii — The Capacity Engine: Reducing "Does the Substrate Chiral Vacuum Form?" to the Sign of One Coefficient. Scoping

**Path:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/sketches/chir_biii_capacity_landau_scoping.md`
**Opened:** 30 May 2026 (Session 151 Patch 0668)
**Author:** Opus (Claude)
**Status:** Scoping at sketch level. NOT closure work, NOT a derivation, NOT a verdict move. Opens **B-iii** — the *capacity engine* of the CHIR ↔ electroweak bridge (`chir_ew_bridge_scoping.md`, Patch 0662), the **sole verdict-moving lever** for the chirality status question (V3/W3 → V1/V2/W1/W2). BRIDGE-1 (Patch 0663/0665) identified the bridge's ℤ₂-*skeleton* (kinematic, conditional on premise P2) and **isolated** the dynamical residue as B-iii. This sketch sharpens that residue into its tightest reachable form: it casts the capacity question as the stability of a ℤ₂-even Landau effective potential `V(η)` in the det-coset order parameter, and shows **the capacity question reduces to the sign of the quadratic coefficient μ²**. The *structure* of `V(η)` (ℤ₂-even, the allowed terms, the reduction to sign(μ²)) is Layer-2.5-reachable now and is what this sketch establishes; the *sign of μ²* itself is fixed only by the DSL effective action behind the F.1 §14.17 viability ceiling, and is registered here as the deep core, not reached.
**Scope:** Decompose B-iii into its two dynamical sub-questions (capacity, EWSB-identification); set up the Landau potential `V(η)` for the det-coset ℤ₂ order parameter; prove (structurally) that capacity ⟺ sign(μ²); name what fixes sign(μ²) (DSL, §14.17); connect the EWSB-identification half to CONJ-CHIR-1; record routes and decision gates. Executes no dynamics; fixes no coefficient.

---

## §0 Working-session firewall + anti-priorities

### §0.1 What this sketch IS

This opens **B-iii**, the third sub-target of the CHIR ↔ electroweak bridge (Patch 0662 §3): *the capacity engine — does the substrate dynamically break to a chiral phase, and is that break electroweak symmetry breaking?* It is exactly the deep spatial engine **1d-β-ii** and exactly **OPEN-SM-4 sub-claims (a)/(b)**; it is the **only** lever that can move the chirality verdict from primitive (V3/W3) toward emergent (V1/V2, W1/W2). The move here is to **scope, not charge**:

- Decompose B-iii into its two dynamical sub-questions (§3): **B-iii-(i)** capacity (does the ℤ₂ break?) and **B-iii-(ii)** the EWSB-identification (is the break EWSB?).
- Set up the **Landau effective potential** `V(η)` for the det-coset ℤ₂ order parameter η — the continuous precursor of the discrete `sign(n̂)` = FI-C-9 (§4).
- Show **structurally** that capacity reduces to **sign(μ²)** (μ² < 0 ⇒ symmetric vacuum unstable ⇒ chiral double-well ⇒ ℤ₂ breaks ⇒ V3→V1) (§5).
- Identify **what fixes sign(μ²)**: the DSL effective action, behind F.1 §14.17 — the deep core, not reachable now (§6).
- Connect the **EWSB-identification** half to CONJ-CHIR-1's dynamical content (§7).
- Record routes + decision gates (§8).

Scoping at sketch level. This is the **B-iii analog of what STATUS-2 did for the breaking chain and what BRIDGE-1 did for the ℤ₂-match**: it makes a deep question structurally precise (reduces it to one coefficient's sign) without answering it.

### §0.2 Anti-priorities sustained at this Patch

Per the scope-sketch discipline (0637/0643/0646/0652/0662):

1. **NO derivation; NO dynamics; NO coefficient fixed.** sign(μ²) is **not** computed — fixing it is exactly the deep core deferred behind §14.17. The Landau form is a *reformulation* of the capacity question, not a solution of it.
2. **NO verdict move.** FI-C-9 stays **V3**, `sign(δ)` stays **W3**. This sketch maps the engine that *would* move them; it does not run it.
3. **NO new programme-level Open-Problem registration / NO header count change.** B-iii already exists, registered three ways: as 1d-β-ii (OPEN-CHIR-1d-β), as OPEN-SM-4 sub-claims (a)/(b), and as the B-iii bullet of OPEN-CHIR-3. This sketch *refines the structure* of an existing target; it adds no problem. No new conjecture (CONJ-CHIR-1 already carries the EWSB-identification content).
4. **NO modification of the closed theorems** (STATUS-1/2, TARROW-1, BRIDGE-1, MERGE-1/2, CHI-1, CAP-1, PCD-ORIENTATION-1) or of the OPEN-SM-4 / Capotauro / F.1 sources. They are *consumed*, not edited (a one-line pointer is added to OPEN-CHIR-3's B-iii bullet).
5. **NO erosion of BRIDGE-1's honest cap.** Everything downstream that cites the ℤ₂-match keeps the "**kinematic only**" tag and the "**OPEN-SM-4 ℤ₂-reading is an interpretation (premise P2), not a derivation**" tag prominent. This sketch *presumes the kinematic ℤ₂-skeleton* (BRIDGE-1, conditional on P2) and asks the next question — whether that ℤ₂ *breaks* — without claiming the skeleton is more than kinematic.
6. **NO claim that chirality is now emergent**, and **NO claim that the break is EWSB.** B-iii-(ii) (the EWSB-identification) stays a conjectural dynamical identification (CONJ-CHIR-1), not a result.
7. **NO reviewer engagement** (scope sketches do not require external review). A future B-iii *structural lemma* (DG-3) would.

### §0.3 What this sketch IS NOT

Not a derivation that the chiral vacuum forms; not a computation of μ² or its sign; not a proof that the break is EWSB; not an OPEN-SM-4 / 1d-β-ii closure; not a theorem registration. It is the structural map that reduces the capacity question to the sharpest reachable form — one coefficient's sign — and pins the residue to the DSL.

---

## §1 Purpose and structure

### §1.1 Why scope this now

BRIDGE-1 closed B-i and, in doing so, left B-iii as the **sole remaining content of CONJ-CHIR-1** and the **sole verdict-moving lever** for the whole chirality status programme. Its Corollary (Kinematic half discharged; dynamical half isolated) states the residue as a dynamical *pair*:

> (i) does this one ℤ₂ **break** (capacity), and (ii) is the breaking **EWSB**?

Both sit behind the F.1 §14.17 viability ceiling, so they cannot be *derived* now. But the *structure* of the capacity question — what form the answer must take, and what single quantity decides it — is Layer-2.5-reachable, in exactly the way STATUS-2's breaking-chain group theory and BRIDGE-1's ℤ₂-match were reachable while the dynamics behind them were not. Sharpening B-iii now (a) makes the deferred target precise enough that, when the DSL effective action becomes computable, the capacity question is already reduced to a single sign; and (b) keeps the programme from stalling on the ceiling by doing the reachable structural half today.

### §1.2 The two dynamical sub-questions of B-iii

| sub-question | the precise content | reduces to | reachable now? |
|---|---|---|---|
| **B-iii-(i)** capacity | does the det-coset ℤ₂ spontaneously break (a chiral vacuum form)? | **sign(μ²)** of `V(η)` (this sketch) | structure: **yes**; the sign: **no** (DSL, §14.17) |
| **B-iii-(ii)** EWSB-identification | if it breaks, *is* the break electroweak symmetry breaking? | is the substrate μ² the EW Higgs μ²? (CONJ-CHIR-1) | **no** (deep, cross-sector) |

This sketch delivers the structural reduction for **(i)** and frames **(ii)** as the dynamical content of CONJ-CHIR-1.

---

## §2 The inputs B-iii consumes

B-iii presumes (does not re-derive) the kinematic skeleton already established:

- **From STATUS-2 (F2, 3/3):** the chiral-vacuum breaking *chain* is **H₄ → H₄⁺** (achiral isometry group order 14400 → rotation subgroup order 7200, index 2), **quotient ℤ₂** (the det-coset); order parameter the pseudoscalar `sign(n̂)` = FI-C-9; two degenerate vacua exchanged by any reflection (det = −1). STATUS-2 fixes *what would break and what the order parameter is* — but is silent on *whether* it breaks.
- **From BRIDGE-1 (Patch 0663/0665, 3/3) — kinematic only, conditional on premise P2:** the STATUS-2 det-coset ℤ₂ and the OPEN-SM-4 activation ℤ₂ ([600-cell] × ℤ₂ → [600-cell]) are the **same** ℤ₂ object (the ℤ₂-match). *This is a group-theoretic identification, NOT a derivation that the breaking occurs or that it is EWSB.* P2 (reading OPEN-SM-4's ℤ₂ as the enantiomorph ℤ₂) is an interpretation, falsifier B1.
- **From MERGE-2 (F1) / CHI-1 (F4):** the order parameter's realized value is `sign(n̂)`, magnitude |FI-C-9| = φ⁻³; the unique primitive pseudoscalar is FI-C-9 itself.

The one thing none of these supplies — and the one thing B-iii-(i) needs — is **dynamics**: a statement that the symmetric configuration η = 0 is or is not the stable vacuum. That is what the Landau potential is built to localize.

---

## §3 The Landau construction

### §3.1 The order parameter and its ℤ₂ action

STATUS-2's order parameter is the **discrete** sign `sign(n̂)` ∈ {+1, −1}, the det-coset label. For a *capacity* question — does a chiral vacuum form? — the natural object is its **continuous precursor**: a real scalar field

> **η** ≡ the det-coset order parameter (a P-odd pseudoscalar, the continuous version of `sign(n̂)`; η > 0 and η < 0 are the two enantiomorphs, η = 0 the achiral/symmetric configuration).

The det-coset ℤ₂ acts on η by the reflection that exchanges enantiomorphs:

> **ℤ₂:  η ↦ −η.**

η is the *amplitude* of substrate handedness; `sign(n̂) = sign(η)` is recovered as its realized sign once a nonzero vacuum is selected. (This is the standard Landau move: replace a discrete order parameter by a continuous field whose vacuum expectation value carries the discrete label.)

### §3.2 The effective potential is ℤ₂-even

Let `V(η)` be the effective potential governing η (the η-dependent part of the substrate effective action, integrated over the fast modes). Because the substrate dynamics are invariant under the det-coset ℤ₂ (the two enantiomorphs are *physically equivalent* before selection — STATUS-2's two degenerate vacua), `V` must be invariant under η ↦ −η:

> **V(−η) = V(η)  — V is an even function of η.**

Hence the Taylor expansion about the symmetric point contains **only even powers**:

> **V(η) = V₀ + μ² η² + λ η⁴ + 𝒪(η⁶),**

with no odd terms (no η, no η³). (An odd term would require a P-odd, ℤ₂-odd coupling — i.e. an explicit pseudoscalar source — which by STATUS-2's partial-1d-β-iii result *does not exist at the axiom level*; the only primitive pseudoscalar is FI-C-9 = η itself, so no external source generates an η-linear term. The ℤ₂-even form is therefore forced, not assumed.)

This is the **L2.5-reachable structural content**: the order parameter, its ℤ₂ action, and the forced ℤ₂-even form of `V`.

---

## §4 The reduction: capacity ⟺ sign(μ²)

Assume the stabilizing quartic λ > 0 (bounded-below potential; if λ ≤ 0 the expansion must be carried to 𝒪(η⁶) and the same sign-of-leading-stable-coefficient logic applies — see §4.3). Then the vacuum structure of `V(η) = V₀ + μ²η² + λη⁴` is fixed entirely by the **sign of μ²**:

- **μ² > 0 (symmetric vacuum):** the unique minimum is at **η = 0**. The ℤ₂ is *unbroken*; no chiral vacuum forms; `sign(n̂)` is undefined/zero. The substrate is achiral. → **capacity = NO.**
- **μ² < 0 (chiral double-well):** η = 0 is a local *maximum*; the minima are the degenerate pair **η = ±√(−μ²/2λ)** ≠ 0. The ℤ₂ is *spontaneously broken*; a chiral vacuum forms; `sign(n̂)` = sign of the selected η. → **capacity = YES.**
- **μ² = 0 (critical point):** the bifurcation; marginal. The boundary between the two regimes.

So:

> **B-iii-(i) capacity  ⟺  μ² < 0.**

The entire "does the substrate dynamically break to a chiral phase?" question — the V3→V1 lever — is **reduced to the sign of a single coefficient.** This is the sharpest reachable form of the capacity question, and the deliverable of this sketch.

### §4.1 What this buys (and what it does not)

It buys *precision*: the open question is no longer the qualitative "is chirality a dynamical outcome or a primitive?" but the quantitative "**is μ² < 0?**". When μ² < 0, STATUS-2's degenerate-pair picture is *realized* (the two det-cosets are the two wells) and the verdict moves V3 → **V1** (emergent mechanism; the sign stays contingent per STATUS-2's partial 1d-β-iii — the double-well is symmetric, so *which* well is a free/spontaneous choice, exactly the V1 "contingent sign" cell).

It does **not** buy the answer: the *value and sign of μ²* are not determined by any of the consumed inputs. STATUS-2 gives the order parameter and the would-be vacua; it does not give the potential's curvature at η = 0. Determining sign(μ²) requires the substrate **dynamics** (§6).

### §4.2 Why μ² (not the discrete sign) is the right object

The discrete `sign(n̂)` presupposes a *nonzero* vacuum — it is only defined in the broken (μ² < 0) phase. Asking "is chirality emergent?" *as a capacity question* is therefore asking whether the system is in the broken phase at all, which is a statement about the curvature of `V` at the symmetric point, i.e. **sign(μ²)**. Casting the capacity question in η rather than `sign(n̂)` is what makes it a well-posed dynamical question rather than a presupposition.

### §4.3 Robustness (λ ≤ 0 caveat)

If the quartic is not stabilizing (λ ≤ 0), the reduction is unchanged in spirit: the capacity verdict is set by the sign of the lowest-order coefficient that, together with the first stabilizing higher even term, determines whether η = 0 is a minimum. The structural claim "**capacity ⟺ the symmetric point is unstable ⟺ sign of the relevant quadratic curvature is negative**" survives; only the closed-form well location √(−μ²/2λ) is specific to the λ > 0 quartic. The machine-check (`verify_biii_landau_reduction.py`) demonstrates both the λ > 0 quartic and the μ² = 0 bifurcation explicitly, and explicitly does **not** assign a value to μ².

---

## §5 What fixes sign(μ²): the DSL effective action (the deep core, §14.17)

The coefficient μ² is the curvature of the substrate effective potential at the achiral point. It is fixed by the **DSL (Dynamical Substrate Law) effective action** — the substrate dynamics whose viability is gated by **F.1 §14.17** (the viability ceiling). Concretely, μ² is the η-quadratic coefficient obtained by integrating out the substrate's fast modes around the achiral configuration; its sign is a property of the DSL coupling structure, not of the 600-cell geometry alone (the geometry, being static and ℤ₂-symmetric, supplies the *form* of `V` but not the *sign* of its curvature).

This is registered here as the **deep core of B-iii**, identical to 1d-β-ii and OPEN-SM-4 sub-claims (a)/(b):

- **OPEN-SM-4 sub-claim (b)** — the substrate chirality *mechanism* (Reading-C candidate `n̂`, **OPEN-FI-C-9-FP-MECHANISM**) — is the magnitude/mechanism content that, if derived, would supply `V(η)` and hence sign(μ²).
- **OPEN-SM-4 sub-claim (a)** — the Capotauro *nucleation/activation event* (the universe-wide sign-selection, downstream of (b)) — is the *selection* of one well once μ² < 0, i.e. the spontaneous choice in the V1 "contingent sign" cell.

**Not reachable now.** sign(μ²) inherits the §14.17 viability ceiling. This sketch deliberately stops at the reduction and does not attempt the DSL computation.

---

## §6 The EWSB-identification half (B-iii-(ii)): connection to CONJ-CHIR-1

Even granting capacity (μ² < 0, the ℤ₂ breaks, a chiral vacuum forms), B-iii's second sub-question remains: **is that break electroweak symmetry breaking?** In the Landau language this is the question of whether the substrate order parameter η is *the same field as* (or dynamically locked to) the electroweak order parameter — equivalently, whether **the substrate μ² is the electroweak Higgs μ²**:

> **B-iii-(ii) EWSB-identification  ⟺  the substrate det-coset μ² is the electroweak Higgs mass-squared parameter** (so that the chiral-vacuum transition and EWSB are one event).

This is exactly the dynamical content of **CONJ-CHIR-1** ("the substrate chiral-vacuum transition is the Capotauro activation event, which is EWSB"). BRIDGE-1 discharged CONJ-CHIR-1's *kinematic* half (the ℤ₂'s are one object, conditional on P2) and isolated this dynamical half; the Landau framing localizes it precisely as the identification of two μ²'s. Note the two sub-questions are **independent**: μ² < 0 could hold (capacity YES) while the break is *not* EWSB (B-iii-(ii) NO) — this is exactly **falsifier B2** of BRIDGE-1 ("the ℤ₂ breaking is shown not to be EWSB — falsifies CONJ-CHIR-1 but not BRIDGE-1; the kinematic match survives as 'same ℤ₂ object, not EWSB'"). The Landau reduction makes that independence explicit: capacity is about the *sign* of the substrate μ²; EWSB-identification is about the *identity* of the substrate μ² with the EW Higgs μ².

---

## §7 Routes and decision gates

**Route A (the reachable structural half — executed by this sketch):** cast capacity as sign(μ²) of the ℤ₂-even Landau potential; this is L2.5 and is done here as a scope sketch (machine-checked). It makes the deferred target precise without charging the dynamics.

**Route B (the deep dynamics — deferred):** compute `V(η)` and hence sign(μ²) from the DSL effective action; resolve B-iii-(ii) by testing the substrate-μ² = Higgs-μ² identification. Highest payoff (the V3→V1 / W3→W1 engine and the EWSB identification), heaviest lift, inherits the §14.17 viability ceiling. Deferred.

**Decision gates:**
- **DG-1 (recommendation: keep tracking under existing IDs):** do **not** reserve a new problem ID. B-iii is fully tracked as 1d-β-ii (OPEN-CHIR-1d-β), OPEN-SM-4 (a)/(b), and OPEN-CHIR-3's B-iii bullet; this sketch refines structure only. Header count unchanged.
- **DG-2 (pointer):** add a one-line "B-iii SCOPED (Patch 0668, this sketch)" note to OPEN-CHIR-3's B-iii bullet in `frontier_sectors/CHIR.md` (done this patch) so the reduction is discoverable from the dashboard.
- **DG-3 (optional future, NOT now):** whether to crystallize the §3–§4 structural reduction into a small Layer-2.5 *structural lemma* theorem (provisional name THEO-CHIR-CAPACITY-1: "the det-coset capacity question is equivalent to sign(μ²) of a ℤ₂-even effective potential") — the B-iii analog of STATUS-2 / BRIDGE-1. Recommend deferring: a lemma that reduces a question to an undetermined sign is borderline-bookkeeping until the DSL can at least *constrain* sign(μ²); revisit when §14.17 lifts or when a partial DSL constraint appears. (This is the same calibration ChatGPT applied to STATUS-1: a classification is informative only when it yields a falsifiable constraint, not a relabeling.)
- **DG-4 (co-ownership):** the B-iii engine remains jointly tracked CHIR ↔ SM (OPEN-CHIR-3 ↔ OPEN-SM-4) so neither sector double-counts; this sketch lives in the CHIR arc and points to OPEN-SM-4, it does not duplicate the SM-side entry.

---

## §8 Honest status

This sketch opens B-iii and reduces its capacity half to the sharpest reachable form — **the sign of one coefficient, μ², of a ℤ₂-even Landau potential** — and frames its EWSB-identification half as the identity of that μ² with the electroweak Higgs μ² (CONJ-CHIR-1's dynamical content). It **derives nothing dynamical**: sign(μ²) is not computed, the chiral vacuum is not shown to form, and the break is not shown to be EWSB. **Scoping the capacity question is not deriving it.** The chirality verdict therefore **stays V3 (spatial) / W3 (temporal)** and will move only when the DSL effective action (behind F.1 §14.17) fixes sign(μ²) negative (V3→V1) and the substrate-μ² = Higgs-μ² identification is established (the EWSB half). The ℤ₂-skeleton this sketch builds on is **kinematic only** (BRIDGE-1), and the OPEN-SM-4 ℤ₂-reading it presumes is an **interpretation (premise P2), not a derivation**; those tags stay prominent. The bridge is not built; B-iii names, precisely, the one coefficient whose sign would build its load-bearing rung.
