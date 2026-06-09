# Path A spec-review results + refined L-CAP-A — Axis 1 confirmed, Axis 2 has a valid gap

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/0917_pathA_specreview_refined_LCAPA.md`
**Patch:** 0917 · **Reviews adjudicated (of the Path A spec, 0916):** Review-1 (CONFIRM), ChatGPT (RESTATE), Copilot (PENDING).
**Disposition:** **Axis 1 confirmed; Axis 2 RESTATE — ChatGPT's falsifier is valid (the Gershgorin "m=12 worst-case" step does not follow).** The Q3 fix worked (linking 0824 resolved ChatGPT's earlier Q3 falsifier). Refined L-CAP-A below. **No re-fire**; CAPACITY-1 reserved; V3/W3 stand; conditional on Mechanism A.

---

## 1. Confirmed — Axis 1 (eigenmode completeness)

Both reviewers confirm the Axis-1 logic: a real-symmetric M_eff has a complete eigenbasis, so the single inequality |K_lift|·a_max(M_eff) < 1 clears **every** mode at once for a *fixed* observable — legitimately exhausting the "which mode" axis and replacing the per-mode scan. Both correctly note this is a **lemma target**, not yet a result: it requires the actual full-operator (all-shells, incl. d=2) diagonalization to return a_max < 1/|K_lift| ≈ 18.9. Both also ask for the normalization to be stated explicitly (done in §3).

## 2. Valid falsifier — Axis 2 (worst-case observable): my Gershgorin step was flawed

ChatGPT (RESTATE): *"m=12 engages the most neighbours → maximizes the row sum → it is the worst-case observable"* does **not** follow from Gershgorin. Gershgorin gives only an **upper** bound, ρ(M) ≤ max row sum; it does not say the largest-support observable has the largest *spectral radius*, nor that sign/phase coherence in a smaller-support observable can't produce a larger eigenvalue with fewer engaged neighbours.

**This is correct.** Direct check: the row-sum bound gives a_max(M(m')) ≤ 12·max|entry|, but the **actual** a_max(M(12)) = |K_lift|/K_c ≈ **0.64** (measured |entry| ≈ 0.053) — far below the loose bound of 12. So "m=12 maximizes the row-sum bound (12)" ≠ "m=12 maximizes the actual spectral radius (0.64)." A more-local observable with a larger effective coupling |K_lift(m')| > 0.053 could exceed 0.64 while still satisfying ≤ 12. The {4,6,8,12} scan (→ [0.50, 0.64]) supports m=12 worst-case but is a **sample** — i.e. Axis 2 is back to the original Q1 problem, now on the *observable* axis. (Review-1's Axis-2 CONFIRM made the same conflation — it wrote "≤ 12 = row-sum(M(12)) ≈ a_max(M(12))," but a_max(M(12)) = 0.64 ≠ 12 — so it does not rescue the step. ChatGPT's is the more rigorous review; one CONFIRM that repeats the flaw does not discharge it.)

## 3. Refined L-CAP-A

- **Normalization (both reviewers).** All η-observables are normalized to unit variance on the Mechanism-A measure, so by Cauchy–Schwarz the per-edge entries satisfy |M_ij| ≤ 1. (This makes the Axis-1 Gershgorin step clean; it does **not** by itself close Axis 2 — that is exactly the point.)
- **L-CAP-A(i) — Axis 1 (unchanged).** Diagonalize the full M_eff(12) (all shells); confirm |K_lift|·a_max(M_eff(12)) < 1 as a complete-spectrum eigenvalue (incl. the d=2 shell — compute, don't assume).
- **L-CAP-A(ii)′ — Axis 2 (REPLACES the flawed Gershgorin worst-case claim).** Prove the **observable-monotonicity theorem**: for every CHI-1-confined η-observable m', the normalized coupling matrix M(m') is a compression and/or non-negative sub-weighting of M(12) that introduces **no coherence-enhancing sign reweighting**; hence ρ(M(m')) ≤ ρ(M(12)). Equivalently and checkably: the effective coupling |K_lift(m')| ≤ |K_lift(12)| for all admissible m'. The {4,6,8} scan is then a sanity check, **not** the proof.

## 4. The deeper read: Axis 2 *is* the η-identity, surfacing a third time

Establishing L-CAP-A(ii)′ requires **characterizing the admissible-observable class** — which η-definitions are dynamically allowed, and their sign structure. That is the **η-identity** question: the node flagged all season as the one place that might require the PCD layer. It has now surfaced three times — as C1, as the DG-3 Q1 falsifier, and now as Axis 2 of the Path-A closure — and each attempt to bound around it (the scan, the Gershgorin row-sum) has been correctly flagged as not closing it. So the next attempt is decisive in a useful way:

- **If the F.1 window proves L-CAP-A(ii)′** (the admissible observables are genuinely sub-weightings of m=12 with no sign-coherence enhancement), Path A closes and CAPACITY-1 can re-fire as a true universal claim.
- **If proving it reduces to pinning the dynamical observable** (the PCD-layer question), we will have **localized the irreducible residual precisely**: chirality-as-a-primitive is provable *except* at the η-identity. That is itself a real result — the season's central question ("does this need the PCD layer?") answered "yes, here, at this exact sub-lemma," not vaguely.
- **Fallback (Path B):** narrow CAPACITY-1 to "V1 excluded within the admissible local-η class at the physical bias" — airtight now, weaker headline.

## 5. Disposition + next steps

- **No verdict moved.** CAPACITY-1 reserved; V3/W3 stand; OPEN-CHIR-1d-β OPEN; count unchanged.
- **Hand refined L-CAP-A to the F.1 window** — the load is now L-CAP-A(ii)′ (the monotonicity theorem) plus the L-CAP-A(i) diagonalization and the normalization statement.
- **Collect Copilot's spec review** (pending — only a placeholder came through).
- **Carry forward for the re-fire** (independent of the above): Q3 fix validated (keep the 0824/0825 links + 0823 annotation); Q4 (both-modes wording) and Q2 (physical-bias scope limit) still queued.
- **Decision gate:** L-CAP-A(ii)′ closes → re-fire universal CAPACITY-1; bottoms out at the η-identity → Thomas's PCD layer or Path B.

## Scope held

Spec-review record + refined closure sub-lemma. **No verdict moved, no THEO, no ID, no CHIR.md edit, no re-fire.** Conditional on Mechanism A (OPEN-FP-F1-2).
