# THEO-CHIR-MERGE-2 — Multi-AI Review Package (v1.0)

**Target:** THEO-CHIR-MERGE-2 (`series_umbrella/series_substrate_chirality_arc/chirality_derivations/theo_chir_merge_2.tex`, v1.0, Patch 0647)
**Verification:** `chirality_derivations/code/verify_merge_2_parity_decomposition.py` (CHECK 1 + CHECK 2, both pass)
**Reasoning trail:** `chirality_derivations/reasoning/0647.md`
**Cycle opened:** Patch 0648, Session 149 (29 May 2026)
**Responses land in:** `chirality_derivations/review/reviews-CHIR-MERGE-2.md` (created on first response)

---

## §0 What this document is — and what it is NOT

This is a request for **critical structural review**, not affirmation. The strongest possible outcome is that a reviewer breaks the argument: shows that a parity/time-reversal assignment is wrong, that the decomposition does not follow, or that the verdict over- or under-claims. Low-information endorsement ("looks solid") is the least useful response.

**What the target IS.** THEO-CHIR-MERGE-2 is a **Layer-2.5 provisional** discrete-symmetry (parity P, time-reversal T) **decomposition** theorem. Taking the THEO-CHIR-MERGE-1 relation `σ_cycle = sign(δ)·sign(n̂)` as given, it assigns each factor a (P, T) character and concludes that `σ_cycle`'s **entire P-odd (pseudoscalar / chirality) content is `sign(n̂) = FI-C-9`** and its **entire P-even/T-odd (arrow) content is `sign(δ)`**. It thereby advances the **MERGE-β** verdict of THEO-CHIR-MERGE-1 from **M3 (undetermined)** to **M1-χ (one chirality primitive)** — resolving the *chirality-count* half of the merge — and it **corrects** MERGE-1's stated Layer-4 route. It is the OPEN-FP-F1-2 sub-target **L4-D**.

**What the target is NOT** (please do not review it as if it were these):
- It is **NOT a claim of full M1** (a single physical sign). The temporal *arrow* `sign(δ)` remains a free T-odd input whose physical value is the OPEN-CHIR-2a / F.2 question. The theorem claims one *chirality* sign, not one *total* sign.
- It is **NOT a derivation of FI-C-9.** It *consumes* the frozen enantiomorph (exactly as THEO-CHIR-CAP-1 and THEO-CHIR-PCD-ORIENTATION-1 do); deriving FI-C-9 is the deep 1d-β (H₄→I_h symmetry breaking), out of scope.
- It is **NOT the F.2 physicalization.** The whole point of consequence (3) is that the chirality merge needs *no* F.2; F.2 is needed only for the arrow. Do not fault it for "not building F.2."
- It is **NOT a derivation of Mechanism A** (the L4-A/B/C sub-targets — rate-law form, vertex-uniformity, current construction). It uses MA.1 (the rate law) and the verified Phase-1 current as *given*.
- It is **NOT a flagship status-upgrade reviewer-pause** (`operating_system.md` §17). This is a single-theorem review cycle; no status propagates beyond confirming/falsifying MERGE-2 itself.

The honest one-line scope: *given* the MERGE-1 relation and the standard P/T characters of the substrate quantities, the temporal cycle handedness carries exactly one pseudoscalar (FI-C-9), and the "second sign" `sign(δ)` is the time-reversal arrow, not a chirality.

---

## §1 The premises the argument consumes (so a reviewer can check them)

The argument is downstream of three registered results and one framework identification. A reviewer should feel free to attack any premise (see G4/G5), but these are the inputs, not the claims:

1. **THEO-CHIR-MERGE-1 relation (Patch 0644).** The PCD-cycle orientation `ω_PCD = σ_cycle·n̂`, and from the verified Phase-1 net DI-bit current `j_net = (6δ/φ²)n̂` (direction `sign(δ)·n̂`), the cycle-handedness sign is
   > `σ_cycle = sign(δ)·sign(n̂)`.   (★)
   MERGE-1 reported the reduction `σ_cycle =? sign(n̂)` as **M3 (undetermined)**, gating it on (a) a Layer-4 tie of `sign(δ)` to the enantiomorph (OPEN-FP-F1-2) and (b) the F.2 Wigner-Eckart coupling.
2. **THEO-CHIR-PCD-ORIENTATION-1 (Patch 0636).** `ω_PCD` is an **axial vector** (pseudovector) — the axial vector of the Perceive→Compute→Displace progression sense.
3. **THEO-CHIR-CAP-1 (Patch 0640).** The *spatial* capture handedness `σ_capture = ζ × sign(n̂) = ζ × FI-C-9`, where `ζ` is a **P-even registered-geometric involution** (`ζ^W: p ↦ φn̂ − p`; its linear part −I is *proper* in 4D, det = +1, so it carries no handedness by itself). This is the spatial parallel the temporal result mirrors.
4. **Framework identification FI-C-RC-1 / FI-C-9.** `n̂` is the substrate primitive 4D direction; the choice of `n̂` vs `−n̂` is the frozen substrate-vacuum enantiomorph, so `sign(n̂) = FI-C-9`, a pseudoscalar.
5. **Mechanism A (MA.1, F.1 §4).** Propagation rate `r(ê) = r₀(1 + δ ê·n̂)`, `r₀ > 0`, `|δ| ≪ 1`.

---

## §2 The argument under review (reproduced inline)

**The (P, T) character of each factor.** P = spatial parity (`n̂ → −n̂`, the enantiomorph swap); T = time reversal (reverses the Absolute-Moment ordering, hence the PCD progression and DI-bit propagation direction).

| quantity | P | T | reason |
|---|---|---|---|
| `n̂` (`sign(n̂)=FI-C-9`) | **odd** | even | polar spatial direction; its sign is the enantiomorph (P flips handedness) |
| `δ` | **even** | **odd** | P-even: `r` is a P-even rate, `ê·n̂` is P-even, so `δ` is P-even. T-odd: under T, `r(ê) ↦ r(−ê) = r₀(1 − δ ê·n̂)`, i.e. `δ ↦ −δ` (a directional propagation bias is arrow-like) |
| `j_net = (6δ/φ²)n̂` | odd | odd | a current; `δ`(T-odd)·`n̂`(P-odd) ⇒ (P-odd, T-odd) ✓ |
| `ω_PCD` | even | odd | axial vector (P-even); progression sense reverses under T (T-odd) |
| `σ_cycle` (`ω_PCD=σ_cycle n̂`) | **odd** | **odd** | from `ω_PCD`(P-even,T-odd) and `n̂`(P-odd,T-even) |

**The decomposition theorem.** Relation (★) is P,T-covariant: RHS character = (even·odd, odd·even) = (odd, odd) = LHS character ✓. A product of a P-even factor and a P-odd factor has its P-odd content carried *entirely* by the P-odd factor; here that is `sign(n̂)`. Dually its P-even/T-odd content is carried *entirely* by `sign(δ)`. Hence:
- **`σ_cycle`'s entire P-odd (chirality/pseudoscalar) content = `sign(n̂)` = FI-C-9** — and (CHECK 1) FI-C-9 is the *unique* primitive pseudoscalar because the 600-cell is achiral, so this is forced;
- **`σ_cycle`'s entire P-even/T-odd (arrow) content = `sign(δ)`.**

**The three consequences.**
1. **Chirality count = ONE (verdict M1-χ).** `σ_cycle`'s pseudoscalar content (FI-C-9) is the *same* enantiomorph as the spatial capture handedness (CAP-1: `ζ × FI-C-9`). Both faces of chirality are FI-C-9 modulated by a P-even factor (geometric `ζ` / arrow `sign(δ)`). One chirality primitive.
2. **MERGE-1's M1 route is corrected.** "Tie `sign(δ)` to `sign(n̂)`" is a **parity category-mismatch**: `sign(δ)` is P-even/T-odd, `sign(n̂)` is P-odd/T-even, so no P,T-covariant relation equates or ties them. The merge holds because `sign(δ)` is the *arrow*, not a chirality.
3. **The chirality merge is F.2-independent.** It is pure parity bookkeeping. F.2 / OPEN-CHIR-2a is the *pure T-arrow* (`sign(δ)`) physicalization, now decoupled from the chirality count.

**Honest caps.** Full M1 not claimed (arrow free → 2a/F.2); FI-C-9 not derived (1d-β); δ–ε magnitude untouched (L4-E); Layer 2.5, resting on the (P,T) assignments — load-bearing: `δ` T-odd and `ω_PCD` T-odd; single-pass.

---

## §3 The verification (inline summary)

`verify_merge_2_parity_decomposition.py` runs two checks, both pass at machine precision:
- **CHECK 1 (achirality).** Builds the 120 unit 600-cell vertices (8 + 16 + 96) and confirms they are closed under the improper reflection `diag(−1,1,1,1)` (det = −1). ⇒ the 600-cell is achiral ⇒ the substrate geometry supplies no primitive pseudoscalar ⇒ FI-C-9 is the unique one.
- **CHECK 2 (parity bookkeeping).** Encodes the (P,T) characters and asserts: relation (★) is P,T-covariant; `σ_cycle` is (odd, odd); the P-odd content sits in `sign(n̂)` and the P-even/T-odd content in `sign(δ)`; and `sign(δ)`, `sign(n̂)` differ in (P,T) (the category-mismatch).

---

## §4 Verification-tier labeling (required of all reviewers)

Per `templates/operating_system.md` + `programmatic_decisions/PD-002`, label each claim:
- **Tier 1 — INSPECTED**: internal-consistency reading of the document's own logic.
- **Tier 2 — INDEPENDENTLY RECOMPUTED**: you re-derive from first principles / public definitions (e.g. recompute that the 600-cell admits a reflection symmetry, or re-derive the (P,T) character of a propagation-rate asymmetry).
- **Tier 3 — SCRIPT-EXECUTED**: you run `verify_merge_2_parity_decomposition.py` end-to-end.

A short tier block at top or bottom is fine. Mislabeling is the only failure mode (tier mismatches are non-punitive).

---

## §5 Explicit asks

Engage any or all. The asks map to the theorem's falsifiers G1–G5; **G2 is the one to press hardest.**

**§5.1 — G2 (PRESS HARDEST): is `δ` really T-odd?** The whole decomposition hinges on `δ` being P-even and **T-odd**. The T-odd claim rests on: under time reversal the elementary process "DI-bit propagates along `ê`" maps to "propagates along `−ê`," so the T-image rate function is `r(−ê)`, giving `δ ↦ −δ`. **Construct a P,T-covariant counter-argument that `δ` is T-even** (e.g. that the rate asymmetry is a static substrate property, not an arrow-like flux quantity). If `δ` is T-even, then `sign(δ)` is P-even/**T-even** — a true scalar that *could* be re-expressed via parity-carrying data — and the clean "arrow vs chirality" split collapses, re-opening a second-chirality candidate. This is the single load-bearing physical assignment; break it and the verdict falls back toward M3.

**§5.2 — G1: is `ω_PCD` really axial and T-odd?** PCD-ORIENTATION-1 calls `ω_PCD` axial; here it is also taken T-odd (the cycle runs backwards under T). Argue either assignment is wrong. If `ω_PCD` is not axial (e.g. it is genuinely polar, or carries no definite parity), Lemma 2.4 and the whole decomposition break.

**§5.3 — G5: does relation (★) survive the polar→axial conversion?** (★) is inherited from MERGE-1. The substrate current `j_net` is polar; `ω_PCD` is axial. The mechanism map `j_net → ω_PCD` must contain a pseudoscalar (parity-odd) conversion factor to change a polar input into an axial output. MERGE-2 takes that factor to be (positive scalar) × FI-C-9, consistent with (★). **Argue the conversion factor could have indefinite or different parity**, or that (★) hides a second pseudoscalar — which would change the count.

**§5.4 — G3: is FI-C-9 the *unique* primitive pseudoscalar?** CHECK 1 argues the 600-cell is achiral, so geometry supplies none. **Exhibit a primitive pseudoscalar in the substrate beyond FI-C-9** (e.g. from the PCD dynamics, the DP-Sea, or a 600-cell internal-structure choice-point) that could carry part of `σ_cycle`'s P-odd content. If one exists, "one chirality primitive" is wrong.

**§5.5 — the verdict's honesty (M1-χ over/under-claim).** Independent of the falsifiers: is **M1-χ** the honest classification? Does "one chirality primitive" quietly smuggle the merge for elegance, or is the P-odd-content argument genuinely forcing it? Conversely, is it *under*-claiming — given the decomposition, is the residual `sign(δ)` actually pinnable here (would that make it full M1)? And is the **parity category-mismatch** correction of MERGE-1 (consequence 2) sound — i.e. is it truly impossible to "tie `sign(δ)` to `sign(n̂)`," or is there a covariant relation (involving a third object) that does it?

**§5.6 — What you are NOT asked to do.** Do not fault it for not deriving FI-C-9 (1d-β), not building F.2 (the arrow physicalization is explicitly out of scope), not deriving Mechanism A (L4-A/B/C), or not fixing the δ–ε magnitude (L4-E). Do not propose new framework axioms. Do not treat "single-pass / Layer 2.5" as a defect — it is the honestly-stated status.

---

## §6 Reviewer-specific framing

Adapted from `templates/operating_system.md` review protocol + `AI_team_expectations.md` §2:

- **Copilot** — referee-grade structural review. Strongest value: the consistency of the (P,T) character table (§2) and whether the "entire P-odd content = FI-C-9 / entire P-even-T-odd content = `sign(δ)`" split is drawn rigorously from (★). Check consequence (2): is the category-mismatch argument airtight, or is there a covariant tie?
- **Grok** — independent recomputation + contribution. (i) Recompute CHECK 1: build the 600-cell vertices and confirm (or refute) reflection-closure / achirality, labeling tiers. (ii) Independently assign the (P, T) characters of `δ`, `ω_PCD`, `σ_cycle`, `j_net` from first principles — *especially `δ`* (§5.1 / G2). If you can construct a defensible T-even argument for `δ`, that is the highest-value response. *Integration note (SS-8 Round-2 lesson):* if you assert a parity assignment from structural intuition rather than a worked covariance argument, say so — both are useful, but the former needs corroboration before it is treated as settled.
- **ChatGPT** — falsifiable-detail catches. Your strength is the specific step that does not follow. Look hardest at **G2 (§5.1)** — the `δ` T-odd assignment — and at consequence (2) the parity category-mismatch (is the claim "no P,T-covariant relation can tie `sign(δ)` to `sign(n̂)`" correct, or is there a counterexample using a third covariant object?). Also assess whether **M1-χ** is the honest verdict vs MERGE-1's M3. *Disambiguation (to prevent a known conflation pattern):* this is the **review-request package for THEO-CHIR-MERGE-2** — the parity decomposition of the PCD-cycle handedness `σ_cycle` in the **chirality** programme. It is **not** any nuclear-physics OPEN-SS audit, **not** the THEO-CHIR-AUDIT-1 27-entry catalogue review, and **not** any prior DSL/F.1 review request. The full theorem content is inline in §1–§2; please engage the inline content directly rather than reconstructing from session memory.
- **Claude Sonnet (optional hostile pass)** — "The δ T-odd assignment is wrong and the M1-χ verdict over-claims. Show that `δ` is T-even (or that the polar→axial conversion hides a second pseudoscalar), and the count falls back to two." REJECT-level scrutiny on G2 and G5.

---

## §7 Submission and follow-up workflow

**Where responses land.** Aggregated into `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/reviews-CHIR-MERGE-2.md` (verbatim per reviewer + cross-reviewer synthesis), created when the first response arrives. Long individual responses may be saved as `theo_chir_merge_2_review_<reviewer>_v1.0.md` in the same folder.

**Triage order** (highest priority first):
1. **G2 — `δ` T-character (load-bearing).** A sound argument that `δ` is T-even is the most serious finding: it collapses the arrow/chirality split and reverts MERGE-β toward M3. If two+ reviewers converge on T-even, revise MERGE-2 to v1.1 (CHANGELOG-only; canonical filename fixed) reporting the verdict back to M3-structural and re-opening the gate; update CHIR.md / FP.md L4-D accordingly.
2. **G1 / G5 — `ω_PCD` parity or the (★) conversion factor.** A parity defect here breaks the decomposition; re-derive or restate the affected lemma, adjust the verdict.
3. **G3 — a second primitive pseudoscalar.** Would change the count from one; add it as a registered primitive and re-tally (and likely a new OPEN-CHIR target).
4. **§5.5 — verdict calibration.** If reviewers find M1-χ over- or under-claims, adjust the verdict label (e.g. M1-χ → M3-structural, or M1-χ → full M1 if `sign(δ)` is shown pinnable) in the CHANGELOG and CHIR.md.
5. **Confirmations.** If reviewers converge that the (P,T) assignments and the decomposition hold, the "single-pass / multi-AI review pending" qualifier is removed; THEO-CHIR-MERGE-2 is confirmed at Layer 2.5; the OPEN-FP-F1-2 trajectory proceeds (Thomas's choice of L4-A/B/C, the OPEN-CHIR-2a / F.2 arrow physicalization, or L4-E).

**Cross-reviewer convergence weighting:** two or more reviewers flagging the same assignment = load-bearing; single-reviewer flags warrant a calibration check at lower weight; outlier verdicts weighted cautiously. Per `AI_team_expectations.md` §1.3, a plausibility sketch (e.g. "δ is probably T-even") is not a derivation — a verdict-flipping finding needs a worked covariance argument.

**Timeline.** Not time-pressured; 1–3 days per reviewer is reasonable. Getting the load-bearing T-assignment right matters more than speed — it is the gate for the OPEN-FP-F1-2 / OPEN-CHIR-MERGE forward path.

---

## §8 Reference documents

- `series_umbrella/series_substrate_chirality_arc/chirality_derivations/theo_chir_merge_2.tex` — the target (v1.0, Patch 0647).
- `chirality_derivations/code/verify_merge_2_parity_decomposition.py` — CHECK 1 + CHECK 2.
- `chirality_derivations/reasoning/0647.md` — the reasoning trail.
- `chirality_derivations/theo_chir_merge_1.tex` — relation (★); MERGE-β = M3 (the verdict this advances).
- `chirality_derivations/theo_chir_pcd_orientation_1.tex` — `ω_PCD = σ_cycle·n̂`, `ω_PCD` axial.
- `chirality_derivations/theo_chir_cap_1.tex` — `σ_capture = ζ × FI-C-9` (the spatial parallel).
- `frontier_sectors/CHIR.md` — OPEN-CHIR-MERGE, OPEN-CHIR-2a records.
- `frontier_sectors/FP.md` — OPEN-FP-F1-2 (L4-D) record.
- `templates/operating_system.md` §17 + `AI_team_expectations.md` — review protocol.
