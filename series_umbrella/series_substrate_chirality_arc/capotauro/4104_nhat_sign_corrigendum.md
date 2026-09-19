# Capotauro v2.0 Corrigendum — the sign of χ is not fixed by the sign of n̂

**Patch:** 4104. **Lane:** EW (CHIR/paper cross-lane). **Discharges:** TODO-4103-NHAT.
**Verify:** `capotauro/code/4104_nhat_sign_check.py`.
**Scope: the SIGN clause only. |χ| = φ⁻³, |M| = χ/6 and THEO-CAP-1 are untouched.**

---

## 1. The claim under test

Capotauro v2.0 (shipped) states, twice:

> "The sign of χ (which enantiomorph is selected) and the magnitude of χ are both fixed by the
> substrate's primitive 4D direction n̂ (FI-C-RC-1): the sign follows from the sign of n̂ …"
>
> "Under v2.0, both the sign and the magnitude of χ are derived from … n̂ …: the sign of χ is
> fixed by which enantiomorph n̂ selects (i.e., by the sign of n̂ itself)."

## 2. Two independent results, both against it

**T1 — the general one. Flipping n̂ selects nothing, for any n̂.** In ℝ⁴, det(−I₄) = +1, so
central inversion is a **proper** rotation, and −I₄ is a symmetry of the 600-cell (verified).
Therefore (600-cell, n̂) and (600-cell, −n̂) are related by a proper rotation: they are
**congruent**, not enantiomorphic. "The sign of n̂ itself" cannot select an enantiomorph
because the two signs name the same configuration. (This is Patch 4072's finding; here made
explicit against Capotauro's wording.)

**T2 — the specific one. The cited reading is achiral.** Capotauro cites the vertex-aligned
reading FI-C-RC-2, n̂ = v_host. Exhaustive search over the 600-cell's Householder symmetries
finds **30 improper symmetries that fix n̂**. An object admitting an improper self-symmetry is
achiral — so there are no two enantiomorphs for n̂ to select *between*. (Patch 4046's finding,
confirmed computationally here.)

## 3. Fairness check — what would escape

A **generic** (non-symmetry-element) n̂ *does* escape T2: improper symmetries fixing it drop to
zero, and the pair is chiral. That is consistent with Patch 4063, which built a chiral 4D
structure from the 600-cell together with a generic H4⁺ orbit.

| n̂ | improper syms fixing it | chiral? |
|---|---|---|
| vertex-aligned (FI-C-RC-2, cited) | 30 | achiral |
| edge-midpoint | 12 | achiral |
| generic #1, #2 | 0 | chiral |

**But no choice of n̂ escapes T1**, which is the mechanism-level objection: whatever n̂ is, its
*sign* is not what distinguishes the enantiomorphs, because −I₄ is proper.

## 4. What is corrected, and what is not

**Corrected** (marked footnote at Definition `def:chi_order_parameter`, plus the v2.0
restatement): the sign clause is withdrawn. The magnitude derivation from the
perturbative-distance-ratio constraint stands.

**Not touched:** |χ| = φ⁻³; |M^K3| = |M^W| = |M^qDP| = χ/6 ≈ 0.0394; THEO-CAP-1; the
Δp_LR ≈ 0.0394 prediction validated within 2%. Those are magnitude results and no part of this
bears on them.

## 5. Why this matters beyond the paper

The programme's verdict register already says **V3 = NOT YET DERIVED** (Patch 4066, correcting
4064). Capotauro v2.0's prose says the sign *is* derived. **The register was right and the
prose ran ahead of it** — this is a prose/verdict mismatch inside a shipped flagship, not a new
contradiction.

It also tightens Patch 4103's conclusion. F5 needs an O(1) phase. 4103 established the arc
produces magnitudes and *at most* a sign. This patch removes the "at most a sign" from the n̂
route specifically: on the cited construction the arc currently derives **no sign either**. The
sign remains open business for sub-claim (b) / H1, exactly where the register puts it.

## 6. Owed

**PDF recompile of Capotauro** (Thomas's mechanical action) — source edited, PDF stale.
Registered in `todolist.md` as TODO-4104-CAPRECOMPILE.
