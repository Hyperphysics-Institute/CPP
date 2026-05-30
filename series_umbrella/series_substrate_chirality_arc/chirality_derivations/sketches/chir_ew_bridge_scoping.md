# OPEN-CHIR-3 ∪ 1d-β-v — The CHIR ↔ Electroweak (SM) Bridge: Is Substrate Chirality the Source of Electroweak Chiral Structure? Scoping

**Path:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/sketches/chir_ew_bridge_scoping.md`
**Opened:** 30 May 2026 (Session 150 Patch 0662)
**Author:** Opus (Claude)
**Status:** Scoping at sketch level. NOT closure work. Opens the **CHIR ↔ electroweak bridge** — the cross-sector trajectory that, if built, would carry chirality from *primitive* (V3/W3) toward *emergent* (V1/V2 and W1/W2). After the chirality primitive/emergent-status capstone closed review-hardened on both halves (spatial FI-C-9 = V3→V1, STATUS-1+STATUS-2; temporal `sign(δ)` = W3→W1, TARROW-1), the **only lever that can actually move either verdict lives outside the CHIR sector**, in the electroweak/SM sector. This document executes no derivation: it decomposes the bridge into sub-targets, states the P-face/T-face correspondence precisely, records the empirical anchors already in the corpus, registers the grand-unification conjecture, and sets the decision gates.
**Scope:** Decompose "connect substrate chirality (FI-C-9, `sign(δ)`) to electroweak chiral structure (parity violation, δ_CP)" into sub-targets; separate the Layer-2.5-reachable structural correspondence from the deep cross-sector dynamics; map the F.1 §14.17 viability ceiling and the OPEN-SM-4 co-ownership; register the routes and decision gates.

---

## §0 Working-session firewall + anti-priorities

### §0.1 What this sketch IS

This opens the **CHIR ↔ electroweak bridge trajectory**, unifying two already-registered targets that turn out to be the same problem:
- **OPEN-CHIR-1d-β-v** (the SM-chirality cross-link, named scope-only in the Patch-0652 1d-β decomposition: "is FI-C-9 = the source of electroweak parity violation?"), and
- **OPEN-CHIR-3** ("Alignment with observed Standard-Model chirality": construct the derivation chain from the substrate handedness to weak-interaction parity violation and the PMNS/CKM CP-phases; deps E4, E26).

These are the **same bridge** viewed from the chirality side (1d-β-v) and the SM side (OPEN-CHIR-3). The bridge is co-owned with **OPEN-SM-4** (Formalise the Capotauro Mechanism). The scope is:

- Decompose the bridge into four sub-targets (§3): **B-i** (the correspondence dictionary / CPT-unified structural map — L2.5-reachable now), **B-ii** (the magnitude anchors δ_CP, Δp_LR — partial now), **B-iii** (the capacity engine: is the substrate chiral-vacuum transition EWSB? — deep, 1d-β-ii, behind §14.17), **B-iv** (the grand-unification conjecture);
- State the **P-face / T-face correspondence** precisely (§4) and lift the TARROW-1 CPT unification onto the SM bridge;
- Record the **empirical anchors** already in the corpus (§5);
- Register the **grand-unification conjecture** CONJ-CHIR-1 (§6);
- Map routes + decision gates (§7).

Scoping at sketch level, NOT closure work. Each sub-target is its own gated sub-trajectory; this document executes none.

### §0.2 Anti-priorities sustained at this Patch

Per the scope-sketch discipline (0637/0643/0646/0652):

1. **NO derivation in this Patch.** No bridge is built; no SM observable is derived; no chirality verdict moves (FI-C-9 stays V3, `sign(δ)` stays W3). Each sub-target B-i..iv is a separate gated sub-trajectory.
2. **NO new programme-level Open-Problem registration / NO header count change.** OPEN-CHIR-3 and OPEN-SM-4 are already registered; 1d-β-v is already a named (scoping-internal) sub-target. This sketch *unifies* 1d-β-v into OPEN-CHIR-3 and decomposes the bridge; it does not add a problem. The **one new registered object is a conjecture** (CONJ-CHIR-1, §6) — conjectures are the appropriate registration form for a proposed-but-unproved cross-sector identification.
3. **NO modification of the closed chirality theorems** (STATUS-1, STATUS-2, TARROW-1, MERGE-1/2, CHI-1, CAP-1, PCD-ORIENTATION-1). They are *consumed* here as the bridge's substrate-side inputs; that consumption is untouched.
4. **NO modification of OPEN-SM-4 / Capotauro / F.1 sources.** The §14.17 viability ceiling, OPEN-SM-4, and the Capotauro paper are referenced, not edited (a cross-ref note is added to OPEN-SM-4; no content change).
5. **NO claim that the bridge holds.** The P-face/T-face correspondence and the EWSB identification are registered as a **conjecture and a decomposition**, not as established results. No merge-for-elegance: the ℤ₂-match anchor (§4.3) is presented as a *structural coincidence worth testing*, not a proof.
6. **NO reviewer engagement** (scope sketches do not require external review).
7. **NO claim that chirality is now emergent.** At current rigor it remains emergent-down-to-two-primitives (FI-C-9 V3 + `sign(δ)` W3); this sketch maps the deep path that *would* eliminate them, it does not walk it.

### §0.3 What this sketch IS NOT

Not a derivation of EW parity violation, not a δ_CP calculation, not an OPEN-SM-4 closure, not a theorem registration, not a proof that the substrate chiral vacuum is EWSB. It is the trajectory-opening map for the deepest and most consequential chirality bridge.

---

## §1 Purpose and structure

### §1.1 Why scope this now

The status programme is *complete and review-hardened* as a classification: chirality reduces to exactly two irreducible sign-objects, and for each we know the verdict, the pinned upgrade, and the single thing that would move it.

| object | character | verdict | upgrade pin | the sole reopener of full derivation |
|---|---|---|---|---|
| `sign(n̂)` = FI-C-9 | P-odd, T-even | V3 | V1 (1d-β-ii) | cross-sector P-odd pseudoscalar (1d-β-v) |
| `sign(δ)` (the T-arrow) | P-even, T-odd | W3 | W1 (F.2 + DSL) | cross-sector T-odd quantity |

TARROW-1's signature result: by CPT those two reopeners are the **same** cross-sector object — the SM CP/T-violating phase (OPEN-SM-4). So every Layer-2.5 structural piece *inside* CHIR is done; the only lever left that can move chirality from primitive toward emergent is the cross-sector bridge to the electroweak sector. Scoping it now is the natural next theoretical bridge-building step.

### §1.2 The headline question this bridge addresses

*Is substrate chirality the source of the Standard Model's chiral structure — or independent of it?* If sourced (the bridge holds), chirality is **emergent via the SM**, FI-C-9 and `sign(δ)` are the substrate faces of EW parity violation and CP-violation, and the magnitude χ = φ⁻³ should thread the observables. If independent, the two are distinct primitives and the SM chirality has its own origin. The bridge sub-targets are designed to decide between these.

---

## §2 The registered substrate-side facts the bridge consumes

The bridge's substrate side is fully registered and review-hardened — it consumes, it does not re-derive:

- **F1 (MERGE-2, 3/3):** all substrate chirality reduces to `σ_cycle = sign(n̂)·sign(δ)`; P-odd content = FI-C-9, T-odd content = the arrow `sign(δ)`.
- **F2 (STATUS-2, 3/3):** the substrate chiral-vacuum **breaking chain is H₄ → H₄⁺** (achiral isometry group order 14400 → rotation subgroup order 7200, index 2, **quotient ℤ₂**); order parameter = the det-pseudoscalar `sign(n̂)` = FI-C-9; two degenerate vacua related by a reflection.
- **F3 (TARROW-1, 3/3):** the arrow `sign(δ)` is W3; the spatial V2-reopener and the temporal W2-reopener are, under assumed CPT, the same SM CP/T-violating object.
- **F4 (CHI-1, registered):** the magnitude χ = φ⁻³ = FI-C-9's value, the symmetric bias of the host vertex's two nearest 600-cell distance shells.
- **F5 (CAP-1 / OPEN-SM-4 sub-claim (c), SHIPPED):** the Capotauro Wigner–Eckart result Δp_LR = χ/6 = φ⁻³/6 ≈ 0.0394 (validated within 2% of observed ~0.04).

These five are the bridge's load-bearing substrate inputs.

---

## §3 The bridge decomposition (four sub-targets)

**B-i — the correspondence dictionary (L2.5-reachable NOW; the recommended next theorem).**
Formalize the structural map {substrate-chirality sign-objects} ↔ {SM chiral observables}, with the CPT unification (F3) lifted onto the SM bridge:
- `sign(n̂)` = FI-C-9 (P-odd) ↔ **electroweak parity violation** (the V−A, left-handed-only weak coupling; audit E26). Parity violation *is* spatial chirality in the SM, so this is the natural P-face identification.
- `sign(δ)` (T-odd) ↔ **SM CP-violation** (the δ_CP phase; via CPT, T-violation).
- the CPT statement (F3): these are the **two faces of one EW chiral structure**, not two independent links.
This is reachable now because it is structural bookkeeping over already-registered theorems (F1–F5) — no new dynamics. It would be a "bridge correspondence" structural theorem (provisional name THEO-CHIR-BRIDGE-1), with its own honest cap: a *correspondence map*, not a derivation that the substrate objects *produce* the SM observables.

**B-ii — the magnitude anchors (PARTIAL now; scope + what-it-takes).**
Two empirical signposts already carry χ = φ⁻³ (= FI-C-9) into SM observables (§5). State precisely what makes each load-bearing: the δ_CP anchor → OPEN-SM-4 via Capotauro (sub-claims (a)/(b)); the Δp_LR anchor → already partially load-bearing (F5, sub-claim (c) shipped). B-ii is the magnitude bridge; B-i is the sign/structure bridge.

**B-iii — the capacity engine (DEEP; = 1d-β-ii; behind F.1 §14.17; NOT L2.5 now).**
Does the substrate dynamically break to a chiral phase, and **is that break electroweak symmetry breaking?** This is exactly OPEN-SM-4 sub-claims (a) (the nucleation/activation event) + (b) (the chirality mechanism — Reading-C `n̂`, OPEN-FI-C-9-FP-MECHANISM), and exactly the spatial capacity engine 1d-β-ii. It is the sole engine for V3→V1 (and the analog F.2+DSL engine for W3→W1). Deferred behind the DSL viability ceiling.

**B-iv — the grand-unification conjecture (REGISTERED as CONJ-CHIR-1; §6).**
The proposed answer that ties B-i/B-ii/B-iii together: the substrate chiral-vacuum transition *is* EWSB.

---

## §4 The P-face / T-face correspondence (the bridge map)

### §4.1 P-face (spatial): FI-C-9 ↔ electroweak parity violation
The weak interaction couples only to left-handed fermions (V−A); parity violation is the SM's spatial chiral asymmetry. The substrate's spatial chiral asymmetry is `sign(n̂)` = FI-C-9. **Conjectured identification:** FI-C-9 is the substrate origin of EW parity violation (audit E26; 1d-β-v; OPEN-CHIR-3's "derivation chain to weak-interaction parity violation"). This is the spatial V2-reopener of STATUS-2.

### §4.2 T-face (temporal): sign(δ) ↔ SM CP-violation (δ_CP)
SM CP-violation (the CKM/PMNS δ_CP phase) is, under CPT, T-violation. The substrate's temporal chiral asymmetry is the arrow `sign(δ)`. **Conjectured identification:** `sign(δ)` is the substrate origin of SM CP/T-violation (OPEN-SM-4). This is the temporal W2-reopener of TARROW-1.

### §4.3 CPT unification + the ℤ₂-match anchor
By F3 (TARROW-1, under assumed CPT) the P-face and T-face reopeners are the **same** SM CP/T object — so the bridge is *one* structure with two faces, not two bridges. A second, independent structural anchor sharpens this:
> **The ℤ₂-match.** STATUS-2 (F2) gives the substrate chiral-vacuum breaking as H₄ → H₄⁺, an **index-2 ℤ₂ quotient**. OPEN-SM-4's chirality-activation event is registered as the symmetry breaking **[600-cell] × ℤ₂ → [600-cell]**. These two ℤ₂'s are candidates to be *the same* ℤ₂ — the substrate-vacuum reflection that selects the enantiomorph. If they coincide, the substrate chiral-vacuum transition (F2) and the Capotauro activation event (OPEN-SM-4) are the same event, which is the content of CONJ-CHIR-1.

This ℤ₂-match is a **structural coincidence worth testing**, not a proof; it is the single most concrete near-term lead (a B-i sub-check).

---

## §5 The empirical anchors (already in the corpus; to be made load-bearing)

Both signposts carry the substrate-chirality magnitude χ = φ⁻³ (= FI-C-9) into SM observables:

- **δ_CP ≈ 193.3°** (CHI-1 signpost) vs **NuFIT 195° ± 40°** / OPEN-SM-4's δ_CP ≈ 195°. The CP-phase anchor (T-face). Made load-bearing by OPEN-SM-4 sub-claims (a)/(b).
- **Δp_LR = χ/6 = φ⁻³/6 ≈ 0.0394** vs observed **~0.04** (CAP-1, F5; sub-claim (c) SHIPPED). A left–right parity asymmetry — the P-face magnitude, already partially load-bearing.

Both were explicitly logged as "support φ⁻³ but **not used in the proof**" (CHI-1). Making them load-bearing — deriving δ_CP and Δp_LR *from* χ = φ⁻³ = FI-C-9 — is the B-ii payoff and simultaneously the magnitude side of the V2/W2 reopener.

---

## §6 The grand-unification conjecture (CONJ-CHIR-1)

**CONJ-CHIR-1 (registered this Patch in CONJ.md):** *The substrate chiral-vacuum transition (STATUS-2's H₄ → H₄⁺, order parameter FI-C-9) is the Capotauro chirality-activation event of OPEN-SM-4, and this event is electroweak symmetry breaking. Equivalently: FI-C-9 is the substrate face of EW parity violation, `sign(δ)` is the substrate face of SM CP/T-violation (one structure by CPT), and the magnitude χ = φ⁻³ sets δ_CP and Δp_LR.*

**If true:** chirality is **fully emergent (V2 / W2) via the SM** — the deepest possible answer to the headline question — with the two substrate primitives reabsorbed as the substrate description of EW chiral structure. **If false** (the ℤ₂'s are distinct, or the substrate chirality is independent of EWSB): chirality and SM chirality are separate primitives, and the verdict stays V3/W3 with the bridge severed. **Falsification routes:** (a) the STATUS-2 ℤ₂ and the OPEN-SM-4 ℤ₂ are shown structurally distinct (§4.3 fails); (b) χ = φ⁻³ is shown *not* to set δ_CP / Δp_LR once OPEN-SM-4 (a)/(b) are derived; (c) CPT-invariance of the substrate fails (severs the P-face/T-face unification, TARROW-1 falsifier T5).

---

## §7 Routes and decision gates

**Route A (recommended — structure first):** deliver **B-i** (the correspondence dictionary + the ℤ₂-match sub-check) as the next theorem (THEO-CHIR-BRIDGE-1, L2.5). It is reachable now, it is the natural complement to STATUS-2/TARROW-1, and it tests the most concrete lead (§4.3) without committing to the deep dynamics. Then **B-ii** (the magnitude anchors, partial). **B-iii** (the capacity engine = 1d-β-ii / OPEN-SM-4 (a)/(b)) stays deferred behind §14.17.

**Route B (capacity first):** attack 1d-β-ii / OPEN-SM-4 sub-claims (a)/(b) directly — the deep dynamics. Highest payoff (it is the V3→V1 / W3→W1 engine), heaviest lift, inherits the DSL viability ceiling. Deferred.

**Decision gates:**
- **DG-B1 (recommended EXECUTE next):** crystallize **B-i** into THEO-CHIR-BRIDGE-1 (ID to reserve when drafted). The ℤ₂-match (§4.3) is its centerpiece.
- **DG-B2:** whether to reserve a standalone bridge ID or keep tracking under OPEN-CHIR-3 ∪ 1d-β-v (recommend: track under OPEN-CHIR-3, which already exists, until B-i crystallizes).
- **DG-B3:** co-ownership protocol with OPEN-SM-4 (the SM/SR sector) — confirm the bridge is jointly tracked CHIR ↔ SM so neither sector double-counts.

---

## §8 Honest status

This sketch opens the bridge and decomposes it; it derives nothing. Chirality remains emergent-down-to-two-primitives (FI-C-9 V3 + `sign(δ)` W3) at current rigor. The bridge, if built, is the path to V2/W2 (full emergence via the SM); CONJ-CHIR-1 is the proposed shape of that path; B-i is the first reachable step and the test of the ℤ₂-match lead. The deep engine (B-iii / 1d-β-ii / OPEN-SM-4 (a)/(b)) stays behind F.1 §14.17.
