# SS-8 Round 2 Review Request — D1 SSV-Minimization Sketch

**From:** Thomas Abshier ND (Hyperphysics Institute) and Claude Opus
**Date:** 22 April 2026
**Subject:** Round 2 review — `SS-8_D1_ssv_minimization_sketch.md`
**Protocol:** `relationship_protocol.md` applies — line-cited evidence, diagnostic framings, dignity-preserving critique. Accurate dissent is more valuable to the programme than polite concurrence.

---

## 1. Context

The SS-8 paper is in exploratory pre-v0.1 state. It targets a derivation of the interstitial-neutron binding scaling law $\Delta_1(N_\alpha) = (6 - 12/N_\alpha) \cdot B_{\text{pair}}$ observed empirically in Phase 1b across N_α = 4..14 alpha-cluster nuclei, with two cases (N_α = 6 octahedron and N_α = 10 gyroelongated square bipyramid) matching to better than 1.5%.

Round 1 of external review was conducted on the H2' derivation note. All three reviewers engaged, and Round 1 produced three convergent findings:

- The note's tiered structure — Layer 1 (pure combinatorics theorem), Layer 2a (B_pair sourcing from SS-5 via A2 + A5 + A8' + A11 without SS-8 calibration), Layer 2b (paper-level structural hypotheses D1/D2/D3) — is sound.
- The three Layer 2b hypotheses are at the correct paper-level tier: D1 (interstitial neutron localizes at alpha-vertex), D2 (K₃-face-participation counting rule, deg(v) × B_pair at vertex v), D3 (bulk-regime averaging to the 2E/V invariant).
- Three first-principles open problems were opened: OPEN-SS-26 (D1 from SSV minimization), OPEN-SS-27 (D2 via A6' extension to interstitial scale), OPEN-SS-28 (D3 + residual decomposition).

Following Round 1, a first-principles attack on OPEN-SS-26 was attempted. The outcome is the subject of this Round 2 request.

---

## 2. Round 2 target

Please review `SS-8_D1_ssv_minimization_sketch.md` (21 April 2026) and the three targeted updates it produced in `SS-8_H2prime_derivation_note.md` (§6.2, §6.3, §10).

The sketch attempts to derive D1 via two independent SSV-energy models:

- **Model A (K₃-face-participation counting):** uses D2's counting rule as a premise and evaluates at four site classes. Delivers vertex-preference with gap factors 2.0× (octahedron) and 2.5× (GESBP).
- **Model B (SR-nn-pair Yukawa):** uses short-range pair physics with λ_nn << L_αα, independent of D2. Delivers vertex-preference with gap factors 1.57× (octahedron) and 1.59× (GESBP).

Numerical evaluation is in `ss8_ssv_minimization_sketch.py` (runs clean; produces the tables cited in sketch §3).

The sketch proposes two structural claims:

1. **D1 promotes from structural hypothesis to conditional theorem** (sketch §4.1, Theorem 3): under either Premise A (D2 + simplicial combinatorics) or Premise B (SR-nn-pair), D1 follows. Gap factors ≥ 1.5× across both test polytopes and both models.
2. **D1 and D2 are coupled** (sketch §5): under Model A, D1 is an arithmetic corollary of D2 via polytope combinatorics. This would mean OPEN-SS-26 naturally subsumes into OPEN-SS-27, since deriving D2 delivers D1 automatically.

**Both claims are labeled "proposed but not adopted" pending this review.** If reviewers concur, the sketch promotes and the note's §10 open-problem cascade consolidates. If reviewers identify circularity, insufficiency, or a hidden assumption, the sketch remains at exploratory tier and D1 stays a structural hypothesis.

---

## 3. Specific questions for Round 2

Please address each question where you have substantive input; skip any that fall outside your expertise or interest in this paper.

### Q1. Is the D1-D2 coupling genuine or circular?

Under Model A, D1 is an "arithmetic corollary" of D2 because deg(v) ≥ 3 > 2 > 1 > 0 holds for any simplicial polytope with V ≥ 4. Does this constitute a genuine structural derivation of D1 (given D2), or does it amount to relabeling D2's content as D1's content?

Specifically: is there a meaningful sense in which D1 has independent content even granted D2, or does D2 already fully determine D1?

### Q2. Does Model B stand alone, or smuggle D2-adjacent content?

Model B (SR-nn-pair Yukawa with λ_nn << L_αα) does not invoke D2's counting rule. It derives vertex-preference from pair-localization alone. Is this argument independent of D2 on its own terms, or does it carry an implicit counting assumption (e.g., "one primary bond per site," which is itself a quiet counting rule)?

If Model B is genuinely independent, D1 has two distinct supporting arguments rather than two paths through a single argument. This matters for the conditional-theorem status.

### Q3. Is "conditional theorem under either sufficient premise" the right tier for D1?

The sketch classifies D1 as a conditional theorem. Alternatives the reviewer may prefer:

- D1 remains a structural hypothesis; the sketch does not deliver enough to justify promotion.
- D1 is a "strengthened hypothesis with two independent supporting arguments" — weaker than conditional theorem, stronger than pure hypothesis.
- D1 is unconditional; a reviewer identifies a derivation from programme-level primitives that the sketch missed.

Please name which tier is defensible and why.

### Q4. Is the OPEN-SS-26 → OPEN-SS-27 consolidation warranted?

If Q1 is affirmative (coupling is genuine), does OPEN-SS-26 naturally fold into OPEN-SS-27? Or is there independent content in OPEN-SS-26 — e.g., the question of local-minimum stability beyond the four privileged sites — that consolidation would lose?

### Q5. Numerical robustness

Gap factors reported: Model A 2.0× (octahedron) / 2.5× (GESBP); Model B 1.57× / 1.59× at λ_nn / edge = 0.35. The sketch tested λ_nn / edge ∈ {0.25, 0.35, 0.50, 0.60} with vertex preference preserved throughout.

- Any reason to expect the gap would narrow, collapse, or reverse under different polytope choices (e.g., N_α = 7 pentagonal bipyramid, where Phase 1b shows ~10% residual rather than <1.5%)?
- Any non-Yukawa SSV functional form that would qualitatively change the result (power-law, step, oscillatory)?
- Any reason the Model A ↔ Model B agreement is coincidental rather than structural?

### Q6. Pattern 6 status

The H2' note §5 currently treats Pattern 6 (B_pair = M_0/φ recurring at nucleon-pair, ⁴He-closure, alpha-alpha, and now interstitial-alpha scales) as an observation inherited from the axiom registry, with necessity-vs-allowance remaining open.

Two candidate positions for the SS-8 treatment:

- **Position A (weaker):** Pattern 6 is an observation. SS-8's four-scale extension is further data for the observation, not a resolution of its necessity.
- **Position B (stronger):** Pattern 6 is a signature of A2 + K₃ eigenvalue structure; at every scale where three-node contact forms, the same K₃ calculation replicates and delivers M_0/φ. This would elevate Pattern 6 to a theorem-tier consequence.

Which position is defensible at the current evidence level? If Position B, does this suggest Pattern 6 should be investigated at the axiom-registry level rather than at the SS-8 paper level?

### Q7. What's missing?

Any content the sketch or note should cover but doesn't? Any failure mode not yet addressed — e.g., adversarial geometry, finite-λ_nn corrections, coupling of interstitial neutrons to each other at N_ex > 1, stability analysis beyond the four privileged sites, non-simplicial polytopes?

---

## 4. What is not under re-review in Round 2

To keep Round 2 focused, the following are not being re-reviewed:

- The H2' note's Layer 1 (pure combinatorics theorem) or Layer 2a (B_pair sourcing from SS-5).
- The empirical Phase 1b substrate (the 12-nucleus prediction table in `SS-8_Phase1_extended_map_findings.md`).
- The programme-level axiom set (unchanged at 9 axioms since SS-7 v1.2).
- The relationship_protocol.md Case 2 archival (documentation only).

If a reviewer identifies material problems in any of these, please flag them separately from the Q1–Q7 answers so the main-line review stays focused.

---

## 5. Artifacts

All artifacts live in the `Hyperphysics-Institute/CPP` repository on GitHub:

- `series_strong/papers/SS-8/sketches/SS-8_H2prime_derivation_note.md` — the H2' derivation note, post-update (the Round 2 baseline)
- `series_strong/papers/SS-8/sketches/SS-8_D1_ssv_minimization_sketch.md` — the Round 2 target
- `series_strong/papers/SS-8/scripts/ss8_ssv_minimization_sketch.py` — numerical script (useful for Q5)
- `series_strong/papers/SS-8/sketches/SS-8_Phase1_extended_map_findings.md` — Phase 1b substrate (context, not under review)

The commit that landed the sketch + updates is on main as of 22 April 2026; reference it if you want to pin to a fixed state.

---

## 6. Response format

No strict template. A response of 3–5 pages addressing Q1–Q7 is ideal. Line citations to the sketch or the H2' note (e.g., "sketch §4.1" or "note §6.3") are preferred over verbal summaries; this lets downstream integration identify what's being engaged precisely.

If a reviewer identifies a fundamental problem that invalidates the sketch's main conclusion — e.g., circular D1-D2 coupling under Q1, or a hidden assumption in Model B under Q2 — please flag that as the first item of the response. Subsequent questions can then be re-interpreted in that light rather than answered in the sketch's original framing.

No strict deadline. Async review at your pace.

---

*End of SS-8 Round 2 review request.*
