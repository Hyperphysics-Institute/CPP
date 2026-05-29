# F.1 OPEN-FP-F1-2 — Layer 4 Axiomatic Derivation of Mechanism A from A1–A11 Scoping

**Path:** `series_umbrella/series_substrate_chirality_arc/dynamical_substrate_law/sketches/F1_open_fp_f1_2_mechanism_a_layer4_scoping.md`
**Opened:** 29 May 2026 (Session 149 Patch 0646)
**Author:** Opus (Claude)
**Status:** Scoping at sketch level. NOT closure work. Opens the OPEN-FP-F1-2 trajectory — the deepest programme commitment registered at F.1 v1.0 SHIP — as a multi-session arc. This document executes no derivation: it decomposes OPEN-FP-F1-2 into its sub-targets, carves out the `sign(δ)`-enantiomorph gate (L4-D) as the explicit first substantive sub-target (the shared gate for the chirality-merge sign MERGE-β and OPEN-CHIR-2a), articulates candidate routes with trade-offs, and registers the decision-gate items requiring Thomas input. **The F.2-paper-trajectory decision (Route β) is explicitly DEFERRED, not taken, at this Patch.**
**Scope:** Decompose "derive Mechanism A (MA.1 + MA.2) from CPP primitive axioms A1–A11 alone" into derivation sub-targets; identify which sub-target is the cross-sector gate (`sign(δ)` ↔ enantiomorph); state honestly what a Layer-4 closure does and does NOT buy at each sub-target; enumerate the F.2-coupling and Layer-4-magnitude dependencies; register the routes and the decision gates.

---

## §0 Working-session firewall + anti-priorities

### §0.1 What this sketch IS

This document opens the **OPEN-FP-F1-2 trajectory** — the long-term Layer-4 axiomatic derivation of the F.1 framework axioms MA.1 (propagation-rate asymmetry) + MA.2 (framework-local current construction) from the CPP primitive axioms A1–A11 alone. The scope is:

- Decompose OPEN-FP-F1-2 into derivation sub-targets (§3): L4-A (rate-law form), L4-B (vertex-uniformity), L4-C (current construction), L4-D (the `sign(δ)` ↔ enantiomorph gate), L4-E (the δ–ε magnitude relation);
- Carve out **L4-D as the explicit first substantive sub-target** — the shared gate for the chirality-merge sign (MERGE-β of THEO-CHIR-MERGE-1) and OPEN-CHIR-2a — and state precisely what L4-D can and cannot resolve on its own (§3.4);
- Articulate three candidate routes (standalone FP trajectory / F.2 dedicated paper / narrow-first L4-D) with their trade-offs (§4);
- Enumerate the cross-sector dependencies, especially the F.2 substrate-Wigner-Eckart coupling that gates the *physicalization* of any sign result (§3.4, §6);
- Register the decision-gate items requiring Thomas input (§7).

The scope is **scoping at sketch level**, NOT closure work. Each sub-target in §3 is its own gated sub-trajectory; this document enumerates them but executes none.

### §0.2 Anti-priorities sustained at this Patch

Per the o-delta-squared / Layer-3-promotion scoping discipline + the OPEN-FP-F1-2 scoping window, the following are NOT triggered by this Patch:

1. **NO Layer-4 derivation work in this Patch** — this is the scoping document. Each sub-target L4-A..E is a separate gated sub-trajectory.
2. **NO modification of the v1.0 SHIPPED F.1 paper sources** — `dynamical_substrate_law.tex` and `.pdf` are frozen at v1.0 SHIPPED (Patch 0570). MA.1 + MA.2 remain framework axioms in the paper; any Layer-4 derivation lives in this sketch (and subsequent OPEN-FP-F1-2 trajectory Patches) until a future v2.0 §11 Mechanism-A-derivation chapter or a dedicated F.2 paper integrates it.
3. **NO modification of the hardened-theorem artifacts** (Patches 0550 + 0551 + 0552 + 0571 + the OPEN-FP-F1-1 / 1-5 sequence). MA.1 + MA.2 appear in those as hypotheses (H1)/(H2); their conditionality is untouched here.
4. **NO modification of F.1's programme-level theorems** (THEO-DSL-1..12 in `theorem-registry.md`). No THEO-DSL is registered, demoted, or restated by this scope sketch.
5. **NO new Open-Problem registration at programme level** — the parent OPEN-FP-F1-2 is already registered (Patch 0570). The sub-targets L4-A..E surfaced here are **scoping-internal**: they remain sub-questions of OPEN-FP-F1-2 until one crystallizes into a separately-trackable closure sub-target at a future Patch. The FP-sector header problem count is UNCHANGED.
6. **NO Route-β (F.2 dedicated paper) commitment** — surfaced in §4.2 and registered as decision-gate DG-2, explicitly DEFERRED per the Session-149 opening instruction.
7. **NO reviewer engagement** on this scoping Patch — Layer-3/4 scoping Patches do not require external review per `operating_system.md` §17.
8. **NO assertion that L4-D (the sign gate) is closable from A1–A11 alone** — §3.4 registers that even a clean structural `sign(δ)`↔`sign(n̂)` tie yields M1 (one chirality sign) only once the F.2 Wigner-Eckart coupling makes σ physical; the F.2 coupling is itself unbuilt. No merge-for-elegance (the THEO-CHIR-MERGE-1 discipline).
9. **NO claim that FI-C-9 is eliminated** by any L4-D outcome — M1 routes the temporal sign TO FI-C-9 (consumes, not derives); M2 adds a second consumed sign. Only the deeper 1d-β (FI-C-9 symmetry-breaking dynamics) touches FI-C-9's input status.

### §0.3 What this sketch IS NOT

It is not a Layer-4 derivation, not a paper draft, not an F.2 opening, not a theorem registration, and not a closure of MERGE-β or OPEN-CHIR-2a. It is the trajectory-opening map that lets the substantive sub-target Patches start from a shared decomposition.

---

## §1 Purpose and structure

### §1.1 Why scope this trajectory now

The CHIR audit-downstream arc (Session 148, Patches 0632–0644) drove chirality down to **at most two sign primitives** — `sign(n̂)` = FI-C-9 (spatial) and `σ_cycle` (temporal) — and showed (THEO-CHIR-MERGE-1, Patch 0644) that the question "one sign or two?" (MERGE-β) and the PCD time-reversal-asymmetry question (OPEN-CHIR-2a) are **the same question**, and that both are gated on the same thing: the Layer-4 derivation of Mechanism A, i.e. **OPEN-FP-F1-2**, specifically the sub-question *does `sign(δ)` tie to the enantiomorph `sign(n̂)`?* Two upstream programme arcs (the chirality-merge capstone and the PCD-arrow physicalization) now wait on this FP-sector target. Opening it with a shared decomposition is the highest-leverage next move.

### §1.2 What "scoping at sketch level" means here

The same discipline as the OPEN-FP-F1-1 scoping doc: enumerate the sub-targets, state what each derivation must produce, identify the load-bearing primitive inputs (A1, A6′, A11) and the cross-sector dependencies (F.2 coupling, the δ–ε relation), articulate routes, and surface the decision gates. No sub-target is executed; no route is committed beyond the carve-out of L4-D as the first substantive sub-target.

### §1.3 Document structure ahead

§2 recaps where MA.1 + MA.2 enter the F.1 machinery and exactly what is taken on faith. §3 is the decomposition (L4-A..E) with the honest cap on each. §4 is the three routes. §5 is the (provisional) artifact-sequence sketch under the recommended route. §6 is the pre-existing material to lean on. §7 is the decision gates.

---

## §2 Recap: where MA.1 + MA.2 enter, and what is taken on faith

### §2.1 The two framework axioms (F.1 §4, verbatim form)

**MA.1 (propagation-rate asymmetry).** Under vertex-aligned Reading C with `n̂ = v_host` and unit-vertex normalisation, the DI-bit propagation rate along unit-direction `ê` from any vertex `v` is
> `r(ê; v) = r₀ (1 + δ ê·n̂)`,
with `r₀ > 0` the H₄-idealized rate, `δ ∈ ℝ`, `|δ| ≪ 1`, and the rate **independent of the originating vertex `v`** (vertex-uniformity).

**MA.2 (framework-local current construction at O(δ¹)).** Under MA.1, the net DI-bit current at vertex `v` is
> `j_net(v) = Σ_{ê ∈ E₁(v)} [ r(ê;v) − r(−ê;v) ] ê + O(δ²)`,
the antisymmetric edge-rate-difference sum over the 12 first-shell directions.

### §2.2 What MA.1 + MA.2 buy downstream (so we know what's at stake)

MA.2 + the first-shell geometry (Theorem 5.1: `û_i·n̂ = −1/(2φ)` uniform; G2 icosahedral sum `Σ û_i = −(6/φ) n̂`) assemble in the F.1 Theorem 7.1 proof to
> `j_net(v_host) = (6δ/φ²) n̂ + O(δ²)`  (VERIFIED, `code/verify_phase1.py`).
This is the substrate-locality umbrella — manifestation (iv), the thermodynamic causal arrow, at sketch-document Layer 3. The **direction** of the arrow is `sign(δ)·n̂`; the **magnitude** carries `δ` and the structural constant `6/φ²`.

### §2.3 What is taken on faith at Layer 3 (the four faith-points)

Per F.1 §4.3 (Layer-rigor + Layer-4 deferral) and §2.3 (Scenario-A motivation), MA.1 + MA.2 are *independent framework commitments* at Layer 3. Four things are taken on faith:

- **(faith-1) The rate-law FORM** — linear in `ê·n̂`, single scalar `δ`, no O(δ⁰) tangent correction. Motivated by structural analogy to the Reading-C edge-length perturbation `ℓ(ê) = ℓ₀(1 + ε ê·n̂)` but not derived.
- **(faith-2) Vertex-uniformity** — `r` independent of `v`. Asserted from "the perturbation is global to the substrate primitive n̂," not derived from A11.
- **(faith-3) The current construction** — the antisymmetric first-shell sum form of MA.2. Asserted as the natural DI-bit flux, not derived from the PCD Displace-phase broadcast dynamics.
- **(faith-4) The sign and magnitude of `δ`** — F.1 §2.3 "Sign convention" calls the global sign `σ` in `ω_PCD = σ·n̂` a *Layer-3 convention* (the two choices T-reversal-symmetric, physical only via the F.2 coupling); and §3.1 leaves the δ–ε relation explicitly open ("Whether δ and ε are independent parameters or are related at Layer-4 axiomatization is an open question").

OPEN-FP-F1-2 is the discharge of faith-1, faith-2, faith-3 to A1–A11; faith-4 is the cross-sector gate (the MERGE-β / 2a question) and is the carve-out of this scope.

---

## §3 Decomposition: the five sub-targets L4-A..E

OPEN-FP-F1-2 decomposes along the four faith-points, with faith-4 split into its sign half (L4-D, the gate) and its magnitude half (L4-E).

### §3.1 L4-A — Derive the rate-law FORM from A1 + A6′

**One-line:** Derive `r(ê) = r₀(1 + δ ê·n̂)` — linear in `ê·n̂`, single scalar `δ`, no zeroth-order tangent term — from A1 (CPs interconnected by DI-bits carrying direction `ê` and rate `r(ê)`) + A6′ (PCD cycle as elementary discrete-time process) + the substrate primitive `n̂`.
**What a solution produces:** a derivation that the *only* first-order-isotropy-breaking rate modification consistent with (i) A1's DI-bit carrying a single directional datum `ê`, (ii) a single substrate-direction primitive `n̂` (one 4D direction, not a tensor field), and (iii) the PCD cycle's rate-setting role, is the rank-1 contraction `ê·n̂` at first order. The "single scalar δ" follows from `n̂` being a single direction; the "no O(δ⁰) tangent term" follows from the H₄-idealized substrate being isotropic at `δ = 0`.
**Layer / tractability:** plausibly Layer 2.5 reachable by a representation-theoretic argument (the first-order modification transforms in the vector rep; the only invariant pairing of `ê` with a single fixed `n̂` is `ê·n̂`). Does NOT need F.2. Estimated 1–3 sessions for a structural argument; publication-grade hardening more.
**Honest cap:** a structural-uniqueness argument fixes the FORM but not the *value or sign* of `δ` (that is L4-D + L4-E). It also presupposes the substrate-primitive `n̂` itself, which is upstream (FI-C-RC-1; the Reading-C selection, Patch 0419 Finding C-W37) — L4-A takes `n̂` as given, as does the whole F.1 paper.

### §3.2 L4-B — Derive vertex-uniformity from A11

**One-line:** Derive that `r(ê; v)` is independent of the originating vertex `v` from A11 (the 600-cell substrate's discrete geometric structure).
**What a solution produces:** the 600-cell is vertex-transitive under H₄; at vertex-aligned Reading C the residual symmetry is `H₃ = I_h` at the host, but the *rate law itself* references only `ê·n̂`, and `n̂` is a global substrate primitive (not a per-vertex field). Vertex-uniformity should follow from `n̂` being global + the rate depending on `ê` only through `ê·n̂`. The derivation must confirm there is no per-vertex modulation hiding in the PCD-cycle local environment.
**Layer / tractability:** plausibly publication-grade Layer 3 reachable (vertex-transitivity is well-established 600-cell geometry). Does NOT need F.2. Estimated 1–2 sessions. Likely the easiest sub-target.
**Honest cap:** uniformity of the *rate law's form* is near-immediate; the subtle point is whether the *value* of `δ` could vary by vertex — that is excluded only if `δ` is sourced globally (tied to the single `n̂`/`ε`), which loops back to L4-E.

### §3.3 L4-C — Derive the current construction MA.2 from A1 + A6′

**One-line:** Derive the antisymmetric first-shell sum `j_net(v) = Σ [r(ê) − r(−ê)] ê` from A1 (DI-bit flux between CPs) + A6′ (PCD Perceive/Compute/Displace cycle).
**What a solution produces:** the net DI-bit current at `v` is the vector sum of directed DI-bit fluxes; the flux along `ê` is set by the Displace-phase broadcast rate `r(ê)`; the *net* current subtracts the reverse flux `r(−ê)`, giving the antisymmetric difference; first-shell confinement at O(δ¹) is already a *theorem* (Corollary 6.2 shell-locality, publication-grade Layer 3), so L4-C need only derive the *construction*, not the locality. The `Σ over E₁(v)` is the first-shell restriction that the perturbation-locality theorem already justifies.
**Layer / tractability:** Layer 2.5–3. Partly discharged already — the locality half is THEO-DSL-1 (publication-grade). The remaining piece is grounding the antisymmetric-difference *form* in the Displace-phase dynamics of A6′. Does NOT need F.2. Estimated 2–4 sessions.
**Honest cap:** the construction's form is reachable; the O(δ²) collection rule it references is OPEN-FP-F1-1 territory (already a separate trajectory) and is not in L4-C scope.

### §3.4 L4-D — **THE GATE**: does `sign(δ)` tie to the enantiomorph `sign(n̂)` = FI-C-9? (FIRST SUBSTANTIVE SUB-TARGET)

**One-line:** Determine whether the sign of the Mechanism-A asymmetry parameter `δ` is fixed by the same frozen enantiomorph that fixes `sign(n̂)` = FI-C-9, or is an independent input. This is the MERGE-β gate (THEO-CHIR-MERGE-1) and — via the CHIR.md clarification — OPEN-CHIR-2a, in one sub-target.

**Why this is the gate.** The arrow direction is `sign(δ)·sign(n̂)`. THEO-CHIR-MERGE-1 reported MERGE-β = M3 (undetermined) for two registered reasons: (i) DSL-3 holds `σ` in `ω_PCD = σ·n̂` to be a Layer-3 convention; (ii) `δ` is an independent framework input whose tie to the enantiomorph is unpinned at Layer 3. L4-D attacks reason (ii) directly.

**The structural sub-question (the reachable half).** F.1 §2.3 "Coupling to PCD cycle" gives the physical seed: under MA.1, DI-bits captured from the `+n̂` side arrive *faster* than from the `−n̂` side; "the asymmetric DI-bit arrival induces a definite preference for one cycle progression direction... the one in which the asymmetric DI-bit flow is consistent with energy minimization." The structural question is: **does this energy-minimization criterion fix `sign(δ)` relative to the enantiomorph choice that defines `sign(n̂)`, or does it leave it free?** If the same handedness convention that orients `n̂` (FI-C-9) also fixes which side "arrives faster" (the sign of `δ`), then `sign(δ)` and `sign(n̂)` are NOT independent → the structural tie holds → **candidate M1**. If the energy-minimization criterion is satisfiable for either sign of `δ` independently of the `n̂`-enantiomorph, then `sign(δ)` is free → **candidate M2**.

**What L4-D resolves and what it does NOT — the honest cap (no merge-for-elegance).** Even a *clean structural tie* (sign(δ) ↔ sign(n̂)) does NOT by itself give M1. Per THEO-CHIR-MERGE-1 reason (i) and CHIR.md OPEN-CHIR-2a, the orientation `σ` becomes a *physical* datum (a genuine T-asymmetry, not a convention) only through the **F.2 substrate-Wigner-Eckart coupling** (Capotauro v2.0 §20), which is itself unbuilt. So the honest output map for L4-D is:
- L4-D structural tie holds **AND** F.2 coupling fixes σ physical → **M1** (one chirality sign; falsifier F2 of THEO-CHIR-MERGE-1 discharged toward M1).
- L4-D shows `sign(δ)` independent → **M2** (two signs; falsifier F3) — and this is decidable at L4-D *without* F.2, because independence breaks the tie regardless of physicalization.
- L4-D structural tie holds but F.2 coupling not yet built → **M3-structural-resolved**: the merge is narrowed to "one sign *if* σ physicalizes as the tie predicts," still pending F.2. This is the realistic near-term L4-D deliverable.

**FI-C-9 not eliminated.** M1 routes `δ`'s sign TO FI-C-9 (consumes it); M2 adds a second consumed sign. Neither derives FI-C-9 (that is 1d-β).
**Layer / tractability:** the structural half (energy-minimization sign criterion) is plausibly Layer 2.5 reachable from the F.1 §2.3 PCD-coupling narrative + A6′ + the FI-C-9 enantiomorph definition. The physicalization half needs F.2 (cross-sector, unbuilt). Estimated 2–5 sessions for the structural half; the full M1/M2 verdict gated on F.2.
**Cross-sector dependency:** F.2 substrate-Wigner-Eckart coupling (DG-1). Upstream consumers: OPEN-CHIR-MERGE (MERGE-β), OPEN-CHIR-2a, OPEN-CHIR-4.

### §3.5 L4-E — The δ–ε magnitude relation

**One-line:** Determine whether the Mechanism-A rate-asymmetry parameter `δ` is related to the Reading-C edge-length perturbation parameter `ε` (= `χ` = `φ⁻³` ≈ 0.236), or is an independent magnitude.
**What a solution produces:** F.1 §2.3 + §3.1 flag both as independent framework inputs sharing the same first-order linear-in-(`ê·n̂`) structure. A Layer-4 derivation might tie them (e.g. if both the rate and the edge-length respond to the *same* substrate-primitive magnitude `|χ| = φ⁻³`), pinning `δ` numerically and elevating the `6δ/φ²` arrow magnitude to a zero-parameter prediction.
**Layer / tractability:** harder; couples to the substrate-primitive-magnitude question (`|χ| = φ⁻³`, E21 / THEO-CHIR-CHI-1 territory). Does NOT need F.2 but DOES touch the chirality-magnitude derivation. Estimated 3–6 sessions. **Lower priority than L4-D** — the sign gate unblocks two upstream arcs; the magnitude is a refinement.
**Honest cap:** L4-E is distinct from L4-D — `sign(δ)` (the enantiomorph tie) and `|δ|` (the magnitude tie to `ε`) are separable. L4-D does not need L4-E and vice versa.

### §3.6 Dependency summary

| Sub-target | Discharges | Needs F.2? | Needs upstream | Tractability | Priority |
|---|---|---|---|---|---|
| L4-A rate-law form | faith-1 | no | `n̂` (FI-C-RC-1) | L2.5, 1–3 sess | med |
| L4-B vertex-uniformity | faith-2 | no | A11 600-cell | L3, 1–2 sess | low (easiest) |
| L4-C current construction | faith-3 | no | THEO-DSL-1 (have) | L2.5–3, 2–4 sess | med |
| **L4-D sign(δ)↔enantiomorph** | **faith-4 (sign); MERGE-β; 2a** | **physical half yes** | FI-C-9, A6′ | **L2.5 structural; 2–5 sess** | **FIRST** |
| L4-E δ–ε magnitude | faith-4 (magnitude) | no | `χ`=φ⁻³ (E21) | harder, 3–6 sess | low |

---

## §4 Three candidate routes

### §4.1 Route α — Standalone FP-sector multi-Patch trajectory

Pursue L4-A..E as separate gated sub-target Patches under the FP sector / DSL arc, each producing a sketch (and, where it hardens, a `hardened_theorems/` artifact + a THEO-DSL-N registration), exactly mirroring the OPEN-FP-F1-1 / 1-5 hardening-sequence pattern (the longest single-trajectory sequence in programme history, 13 artifacts). **Lightest commitment; most reversible; keeps everything inside the existing DSL machinery.** Recommended default for the *near-term sub-targets* (L4-A, L4-B, L4-C, and the structural half of L4-D).

### §4.2 Route β — Dedicated F.2 Layer-4 paper

`future_projects.md §300` already reserves "**F.2 as dedicated Layer-4 axiomatic derivation of Mechanism A**" — fold OPEN-FP-F1-2 into a new F-line flagship deriving MA.1 + MA.2 from A1–A11, estimated 5–15 sessions. **Heaviest commitment (a new flagship paper)**; appropriate only once enough sub-targets have closed at sketch level to justify a paper, or if Thomas wants to start the F.2 paper now. **DEFERRED at this Patch (DG-2).**

### §4.3 Route γ — Narrow-first on L4-D (the gate) alone

Skip L4-A/B/C; go straight at L4-D's structural half (the `sign(δ)` energy-minimization criterion) to deliver the M1/M2/M3-structural verdict that unblocks MERGE-β + OPEN-CHIR-2a. **Highest leverage per unit effort** *if* the structural half is tractable from the §2.3 PCD-coupling narrative without first formalizing MA.1/MA.2's derivation. Risk: L4-D's energy-minimization argument may implicitly lean on the rate-law form (L4-A) and the PCD Displace dynamics (L4-C), so a clean L4-D may need a thin L4-A/L4-C scaffold first.

### §4.4 Initial recommendation (per the Session-149 instruction)

**Route γ-leaning-α, Route β deferred.** Carve **L4-D (the sign gate) as the explicit first substantive sub-target** (this scope sketch does that), and open it next — but be prepared to drop in a thin L4-A (rate-law form) + L4-C (current construction) scaffold if the L4-D energy-minimization argument requires them. Pursue L4-B and L4-E later as independent refinements. Do **not** commit Route β (the F.2 paper) until the L4-D verdict and at least the L4-A/C scaffold are in hand — the paper decision is DG-2, deferred. This keeps the move reversible and honest about the 10–20-session full-closure reality while front-loading the one sub-target two upstream arcs are waiting on.

---

## §5 Provisional artifact sequence (under Route γ-leaning-α)

Sketch only; not committed. Sequence and Patch granularity decided at each sub-target's opening Patch.

1. **L4-D structural half** — sketch `F1_l4d_sign_delta_enantiomorph_scoping.md` → if tractable, a Layer-2.5 finding resolving the energy-minimization sign criterion; reports M2 (decidable now) or M1/M3-structural (M1 pending F.2). *Possibly preceded by a thin L4-A + L4-C scaffold.*
2. **L4-A rate-law form** — representation-theoretic uniqueness argument; candidate `hardened_theorems/mechanism_a_rate_law_form.tex` + THEO-DSL-N if it hardens.
3. **L4-B vertex-uniformity** — likely the cleanest publication-grade Layer-3 artifact; candidate `hardened_theorems/mechanism_a_vertex_uniformity.tex`.
4. **L4-C current construction** — grounds MA.2's antisymmetric-difference form in A6′ Displace dynamics; leans on THEO-DSL-1 for the locality half.
5. **L4-E δ–ε magnitude** — couples to the `χ` = φ⁻³ derivation; deferred refinement.
6. **(DG-2 decision point)** — whether to fold 1–5 into an F.2 paper (Route β) or keep them as DSL-arc artifacts (Route α).

---

## §6 Pre-existing material to lean on

### §6.1 Within the F.1 paper folder
- **F.1 §2.3** (Scenario-A motivation) — the PCD-coupling narrative (the L4-D seed) + the sign-convention paragraph + the δ–ε open-question paragraph (the L4-E seed).
- **F.1 §3.1** (A1–A11 recap) — the load-bearing primitives A1 (CP + DI-bit), A6′ (PCD cycle / `ω_PCD`), A11 (600-cell); the δ–ε independence note.
- **F.1 §4** (MA.1 + MA.2 + Layer-4 deferral) — the exact axiom statements to be discharged.
- **F.1 §7.2 Theorem 7.1 proof** — shows precisely where MA.2 enters (Step 2) and what the arrow direction/magnitude depend on.
- **THEO-DSL-1** (perturbation-locality, publication-grade Layer 3) — already discharges the *locality* half of L4-C.

### §6.2 In the SSCA arc
- **THEO-CHIR-MERGE-1** (Patch 0644) + `chirality_derivations/sketches/theo_chir_merge_1_scope.md` — the MERGE-α/β decomposition, the M1/M2/M3 outcome map, and the falsifiers F1–F4 that L4-D feeds.
- **THEO-CHIR-CAP-1** (Patch 0640) — pinned the *spatial* capture handedness to `sign(n̂)` = FI-C-9 (the parallel L4-D seeks for the temporal sign).
- **Capotauro v2.0 §20** — the F.2 substrate-Wigner-Eckart datum construction (the physicalization gate, DG-1).
- **THEO-CHIR-CHI-1** (Patch 0638, E21) — `χ` = φ⁻³ locality selection (the L4-E magnitude anchor).
- **Capotauro v2.0 §2.3** — the Reading-C edge-length perturbation `ε` (the L4-E counterpart).

### §6.3 At programme level
- **`frontier_sectors/FP.md`** OPEN-FP-F1-2 entry (the parent registration; enriched with this decomposition at Patch 0646).
- **`frontier_sectors/CHIR.md`** OPEN-CHIR-MERGE / OPEN-CHIR-2a / OPEN-CHIR-4 (the upstream consumers).
- **`future_projects.md` §300** — the reserved F.2-paper Route-β framing.

---

## §7 Decision-gate items requiring Thomas input

### DG-1 — The F.2-coupling dependency for L4-D's physicalization
L4-D's structural half (sign criterion) is reachable without F.2, but the M1 verdict needs the F.2 substrate-Wigner-Eckart coupling to make σ physical, and F.2 is unbuilt. **Decision:** (a) pursue L4-D's structural half now and report M3-structural-resolved (tie-pending-F.2) [recommendation — delivers the decidable M2-vs-not verdict immediately]; or (b) open the F.2 coupling first so L4-D can deliver a full M1/M2 verdict in one arc; or (c) interleave.

### DG-2 — Route selection (α standalone vs β F.2 paper) — DEFERRED
Per the Session-149 instruction, the F.2-paper decision is deferred. **Registered as a future decision gate**, to be revisited once the L4-D verdict + an L4-A/C scaffold are in hand. No action this Patch.

### DG-3 — L4-D scaffold depth
Does the L4-D energy-minimization sign argument need a thin L4-A (rate-law form) + L4-C (current construction) scaffold first, or can it run on the §2.3 PCD-coupling narrative alone? **Decision deferred to the L4-D opening Patch** — discovered by attempting the structural argument; recommendation is to attempt L4-D directly and pull in scaffold only if the argument demands it.

### DG-4 — Is L4-E (δ–ε magnitude) in OPEN-FP-F1-2 scope, or a separate sub-question?
The δ–ε relation could be (a) part of the Mechanism-A derivation, or (b) a separate chirality-magnitude question owned by the `χ` = φ⁻³ / E21 trajectory. **Decision:** recommendation is to keep L4-E inside OPEN-FP-F1-2 as a low-priority sub-target but flag the E21 cross-link, revisited only after L4-D.

### DG-5 — Sub-target promotion to programme-level Open Problems
The sub-targets L4-A..E are scoping-internal at this Patch. **Decision:** promote a sub-target to a separately-trackable programme-level Open Problem (e.g. OPEN-FP-F1-2a) only when it crystallizes into a closure trajectory — recommendation is to promote L4-D first, at its opening Patch, given its two upstream consumers.

---

*Scope sketch opened at Patch 0646 (Session 149). No derivation performed; no route committed beyond the carve-out of L4-D as the first substantive sub-target; the F.2-paper decision (Route β) explicitly deferred (DG-2). The honest caps of THEO-CHIR-MERGE-1 are inherited verbatim: no merge-for-elegance, FI-C-9 not eliminated by any L4-D outcome, and even a clean sign-tie yields M1 only once the F.2 coupling makes σ physical.*
