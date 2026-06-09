# L-CAP-A computation assessment — Axis 1 established; Axis 2 still open (the monotonicity theorem)

**Location:** `series_umbrella/series_substrate_chirality_arc/chirality_derivations/review/0918_LCAPA_computation_assessment.md`
**Patch:** 0918 · **Assesses:** the F.1/DSL-window L-CAP-A computation (their Patch 1200) + the two CONFIRM spec-reviews of 0916.
**Disposition:** **Axis 1 ESTABLISHED** (the diagonalization). **Axis 2 NOT established** — the F.1 computation re-ran the original 0916 Gershgorin row-sum argument (it had not seen the 0917 refinement); that argument was refuted by ChatGPT and replaced in 0917 by the observable-monotonicity theorem **L-CAP-A(ii)′**, which remains to be proven. **Path A NOT closed; no re-fire.** CAPACITY-1 reserved; V3/W3 stand; conditional on Mechanism A.

---

## 1. Axis 1 — ESTABLISHED ✓

The F.1 diagonalization: M_eff row sum ≈ **0.644** (NN: 12×0.053 = 0.636; d=2: 20×0.0004 = 0.008; higher ≈ 0), so `|K_lift|·a_max(M_eff) ≈ 0.644 < 1`; the 2nd-shell lift is ~1.25%, nowhere near the falsifier (a_max ≥ 18.9). Crucially, the m=12 operator is **vertex-transitive**, so the uniform eigenvector saturates the row-sum bound — Gershgorin is **tight** for this single fixed operator, and a_max ≈ 0.644 is the genuine complete-spectrum largest eigenvalue (all shells, 2nd shell computed not assumed). **Axis 1 closes.** (Still mean-field; true K_c (0823) only widens.)

This is exactly why the Gershgorin tool is *fine for Axis 1* (bounding one vertex-transitive operator, where the bound is saturated) but *not for Axis 2* (ordering different operators by their row sums — see §2).

## 2. Axis 2 — NOT established (the refuted argument was re-run)

The F.1 Axis-2 text is the **original 0916 Gershgorin argument**: "a_max(M(m′)) ≤ (engaged neighbours)×(max|C|); m=12 engages all 12 at full weight → maximal row sum → strictly smaller a_max for m′<12; confirmed by the {4,6,8,12} scan." The F.1 window cited 0916/0821/0824/0823 but **not 0917** — it computed before the refinement reached it. This is the precise argument ChatGPT refuted (0917 §2) and that 0917 replaced. The gap is unchanged:

- The step "m=12 has the largest row sum ⇒ m=12 has the largest spectral radius" does **not** follow. Gershgorin is an *upper* bound; for m=12 it is saturated (vertex-transitive), giving a_max=0.644, but for a more-local m′ the bound (its own row sum) need not be saturated, and m′'s **actual** spectral radius is not ordered by m=12's row sum.
- The argument tacitly assumes (a) per-link |C(m′)| ≤ 0.053 for **all** observables and (b) every m′ operator is uniform (so a_max = n·|C|). For m=12 both hold (icosahedral symmetry, vertex-transitive). For a more-local m′ neither is guaranteed: a subset observable can break I_h → non-uniform / sign-coherent couplings with a_max > n·|C̄|; and a more-local η could be *more* strongly correlated per link (|C(m′)| > 0.053). Assumptions (a)+(b) **are** the monotonicity theorem — assuming them is assuming the conclusion.
- The {4,6,8,12} scan confirms m=12 worst among those four — but that is the **sample**, i.e. the original Q1 gap, now on the observable axis.

So Axis 2 is not closed. (The two CONFIRM spec-reviews of 0916 endorse the Gershgorin step, but each repeats the same conflation — one wrote "≤12 = row-sum(M(12)) ≈ a_max(M(12))," and a_max(M(12)) ≈ 0.644 ≠ 12 — so they do not discharge ChatGPT's falsifier.)

## 3. Sharpened rigorous route for Axis 2 (replaces Gershgorin; for the F.1 window)

The monotonicity reduces to a single concrete, checkable condition via **Perron–Frobenius** (not Gershgorin row-sums):

> For real-symmetric M, `ρ(M) ≤ ρ(|M|)` (entrywise absolute value). For non-negative matrices, entrywise domination implies spectral-radius domination. Hence **if `|M(m′)_ij| ≤ |M(12)_ij|` entrywise for every admissible CHI-1-confined observable m′**, then
> `ρ(M(m′)) ≤ ρ(|M(m′)|) ≤ ρ(|M(12)|) ≈ 0.644 < 1`
> (where `ρ(|M(12)|)` = the row sum 0.644, saturated by the uniform mode on the vertex-transitive graph). So **Axis 2 closes iff every admissible more-local η-observable has per-link correlator magnitude ≤ that of the full vertex figure (|C(m′)| ≤ 0.053).**

This is rigorous (Perron–Frobenius does the ordering Gershgorin could not) and reduces the whole observable axis to **one structural fact**: no admissible more-local η is more strongly per-link correlated than m=12. That fact is the **η-identity** — it asks what the admissible observable class is and how strongly its members couple. The {4,6,8} scan supports it (|C| not exceeding the m=12 value) but does not prove it for all admissible m′.

## 4. The decision gate (unchanged, now precise)

- **If the F.1 window proves the entrywise domination** `|C(m′)| ≤ 0.053` ∀ admissible m′ (a structural property of the η-observables), then ρ(M(m′)) ≤ 0.644 < 1 by Perron, Axis 2 closes, **Path A closes**, re-fire universal CAPACITY-1.
- **If the domination cannot be proven structurally** — i.e. it reduces to pinning the dynamical observable — then the **η-identity is the located irreducible residual**: chirality-as-primitive is provable except at this one structural fact, which is where Thomas's PCD-layer insight (or a deeper derivation) is genuinely required. Else **Path B**: narrow CAPACITY-1 to "V1 excluded over the admissible local-η class with |C| ≤ 0.053, at the physical bias."

## 5. Disposition + next steps

- **No verdict moved. Path A NOT closed** (Axis 1 done, Axis 2 open). No re-fire.
- **Re-hand to the F.1 window WITH 0917 + 0918** (it executed 0916 and missed both): the task is L-CAP-A(ii)′ via the **Perron route** — prove `|C(m′)| ≤ 0.053` entrywise for all admissible CHI-1 observables. The Gershgorin row-sum argument is *not* sufficient (it bounds each operator by its own row sum without ordering them; ChatGPT 0917).
- **Axis 1 banked as established**; carry into the eventual re-fire.
- Q2/Q3/Q4 fixes still queued for the re-fire; Q3 fix (0824/0825 links) validated.

## Scope held

Computation assessment + sharpened sub-lemma route. **No verdict moved, no THEO, no ID, no CHIR.md edit, no re-fire.** Conditional on Mechanism A (OPEN-FP-F1-2).
