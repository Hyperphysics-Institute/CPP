# Do the Capotauro Papers Need Rewriting? — Measured Answer

**Patch:** 4118. **Lane:** CHIR/EW. **Question (founder, 18 Sep 2026):** *"Do we need to rewrite
the Capotauro papers?"*

## Answer: No. It is a v2.0 → v2.1 revision — about 5% of one paper, plus scattered one-line edits.

I audited all 111 sections of `capotauro.tex` and every sibling paper in the arc rather than
estimating.

---

## 1. Capotauro.tex — where the damage actually is

**Sections that ARE the affected content (rewrite or retire): 119 lines of 2263 = 5.3%**

| lines | hits | section |
|---|---|---|
| 20 | 26 | Sub-claim (a) Capotauro nucleation event derivation |
| 24 | 14 | The primitive chirality magnitude \|χ\| = φ⁻³ *(the 4117 renaming)* |
| 19 | 10 | Q7 cosmological-nucleation scoping |
| 24 | 8 | Notable absences from the falsifier set |
| 15 | 5 | OPEN-SD-CHIR-PRIMITIVE umbrella manifestations (iv)/(v) |
| 13 | 4 | Future-window predictions: manifestations (iv)/(v) |
| 4 | 5 | Open Theorem-Level Work |

**Plus 41 scattered one-line mentions** across 20 further sections — those sections are 684
lines long in total but need only the 41 lines touched.

**Untouched: the flagship theorem.** `sec:composite_we`, which proves |M| = χ/6 ≈ 0.0394,
contains **zero** affected hits. The result, THEO-CAP-1, and PRED-O-25/26/27/31 stand without
a word changed.

## 2. Sibling papers — 14 one-line edits total, no structural work

| file | mentions |
|---|---|
| theo_chir_audit_1, chirality_continuum, theo_chir_chi_1, theo_chir_vw_1 | 2 each |
| theo_chir_cap_1 (1 + 1 sign-of-χ), theo_chir_merge_1, merge_2, tarrow_1, vw_2, dynamical_substrate_law | 1 each |

None of these *argue* from the event; they cite it in passing. A pointer update each.

## 3. The revision plan

**Already authorized (settled at 4104/4117, no further ruling needed):**
- **E1.** The 4104 sign-from-n̂ corrigendum — **already applied to source**, awaiting recompile.
- **E2.** Rename |χ| from "substrate primitive chirality magnitude" to an **anisotropy /
  perturbation amplitude** (TODO-4117-CHIRENAME). 24-line section, plus the ~12 places the
  phrase recurs. Follows directly from 4104 removing the sign; not contingent on the retirement.

**Awaiting the founder's TODO-4116-CAPRETIRE ruling:**
- **E3.** Retire §"Sub-claim (a) … nucleation event derivation" (20 lines) — rewrite as a
  **superseded** note with the reason (χ₄ supplies handedness structurally; its own mechanism
  withdrawn at 4104), not a deletion.
- **E4.** §"Q7 cosmological-nucleation scoping" (19 lines) — same treatment.
- **E5.** §"Notable absences from the falsifier set", §"Open Theorem-Level Work", the two
  manifestations sections — update to reflect that (a) is retired and F5 has no candidate
  mechanism.
- **E6.** 41 scattered one-liners + 14 sibling-paper pointers — mechanical sweep once E3–E5 fix
  the wording.
- **E7.** Sub-claim architecture table and abstract — restate as: (a) **superseded**,
  (b) open, (c) shipped.

**Version:** v2.0 → **v2.1**. A revision with a changelog entry, not a new paper. The
scholarly record keeps (a) visible as superseded, which is the right treatment for a claim that
was published and is now withdrawn.

## 4. Why this is small, in one sentence

The event was always a **separate sub-claim** that never closed, and the shipped result never
cited it — so retiring it is deleting an open promissory note, not dismantling an argument.

## 5. Sequencing

E1 is in source already. **E2 can go now.** E3–E7 wait on the ruling. All of it should land on
**one recompile** (TODO-4104-CAPRECOMPILE) rather than three — the PDF is stale either way.

**Recommendation: give the ruling on TODO-4116-CAPRETIRE first, then execute E2–E7 as a single
v2.1 patch and recompile once.**

No verdict moved. Nothing edited in this patch beyond filing the plan.
