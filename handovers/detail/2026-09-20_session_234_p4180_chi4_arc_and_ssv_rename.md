# Session 234 — Handover

**Patches 4132–4180.** Date 2026-09-20. Lanes: EW, GR, WORKFLOW.
**Filename carries the `pNNNN` token enacted at Patch 4132** — sort `handovers/` by filename and read
the last entry; the token makes that true again for multi-handover sessions.

---

## 0. Read with

- `series_standard_model/axiom_maturation/chirality_axiom_maturation.md` — every patch of this arc is
  logged there in order, newest first.
- `todolist.md` — all owed items, each with its result inline.
- `bootup.md` §0.5 — now **ten** D-rules; D-10 and D-11 were enacted this session.

## 1. What the founder owes (mechanical actions)

- **22 PDF recompiles**, from the `SSV_net → V_i` rename (4164) and the edge-index re-lettering
  (4163, held deliberately so each file compiles once):
  **SF-2, SF-6, SF-8 · GR-1, GR-1b, GR-1c, GR-1e, GR-1f, GR-1g, GR-1h, GR-1i, GR-1j, GR-2 ·
  QM-1, QM-4, QM-5, QM-6 · SR-2, c01, c03, c04, c06**
- **One decision, an axiom change (PD-006(a)): what becomes of A3′'s A_i channel.** See §3.

## 2. What was done

**Governance.** 4132 fixed a handover-sort defect that would have booted this session 35 patches
stale. 4144 fixed the commit-message format (4,000-character subjects were leaving the founder's
terminal in the pager). 4169 enacted **D-10** (grep for a prior correction before asserting the
corpus lacks a premise) and **D-11** (a document's prose must reproduce its script's table), and
added a second cost record to **D-4**.

**Nomenclature.** `SSV_net` **retired**; the corpus uses **`V_i`**. This finished a rename A3′ began
at Patch 1129 and never propagated — SR-2 states the identity outright. 642 sites across 193 live
files; frozen provenance (handovers, session logs, archive, verify scripts, `founders_voice/`,
per-patch `NNNN_*.md`) untouched. Edge index re-lettered to `k` to avoid `e_i · V_i`.

**Physics — the F3/chirality arc.** F3CALC closed; R-F3 retired in favour of **R-F3-ISO**, which
carries both sectors. **THEO-CHIR-1** proposed (a configuration is parity-odd-detectable iff
positions + charges + spins admit no improper symmetry) — **not yet registered in
`theorem-registry.md`**. And **⟨b⟩ = (v/c)·cos θ derived** — the measured V−A polarisation law, no
fitted parameter, from b being a sign (A1′) + linearity (B3) + the isotropy of a sum over a spherical
5-design.

**Falsifiers.** **A3G-2's recorded pass was wrong** — its own verify script printed the refutation
and the prose inverted it (4138). Re-run and **it passes on sound grounds** (4143: b needs
*covariance*, not invariance). Suite: **five of nine**.

## 3. The state of χ₄ — read this before touching the amendment

**A1′ is load-bearing and cheap.** Its carried attribute is the ZBW circulation's **sense** — a
*sign*, not a field. b = A·V_i contracts it with the V_i register, and everything derived this
session (V−A, F3, THEO-CHIR-1, the polarisation law) rests on A1′ **alone**.

**A3′'s A_i channel has had every support tested, and none held:**

| support | result |
|---|---|
| empirical | near-empty — magnetism the corpus already had (SM-2 derives spin *and* moment from ZBW charge circulation), plus a mixing term bounded at ε ≤ 5×10⁻⁴⁷ |
| observability | κ_A = 16πG/c⁴ on the zero-parameter branch puts it 10¹⁸ below the LIGO vector-mode bound |
| structural ("spin is a source with no channel") | fails on CPP's own r_ZBW = 0.631 fm — spin here is **resolved circulation**, hence orbital, hence already in V_i |
| independence | fails — ∇ × V_i supplies 2 of 3 components at every k; the third is longitudinal and needs the pseudoscalar source 4172 excluded |

**That is a recommendation to restate or retire A3′'s amendment. It is not "χ₄ is wrong."** The
founder ruled at 4178 to keep it on realism; 4179 reports that the condition that ruling names is in
doubt. **The decision is his and is open.**

## 4. What is next, in order

1. **F5** — still the blocker, no mechanism on file. It has been the blocker all session and nothing
   here touched it.
2. **A3G-4 / A3G-5 / A3G-6** — unrun.
3. **TODO-4126-CAGEMOMENT** — deferred since before this session; the real cage evaluation of the
   nucleon moment. **The lane could use a result that adds rather than corrects.**
4. **THEO-CHIR-1 registration** — after a review pass.

## 5. Honest note for the next window

This session produced a great deal of correction: 4138 (A3G-2's inverted table), 4141 (my own 4140
overreach), 4148 and 4149 (two census errors), 4161 (my own 4159/4160 modelling error), 4168 (an
error a prior Opus had already made at 0732 and the founder had already corrected), 4174 (my own
4173, one patch old), 4178 (my own 4172, six patches old). **Three of those were failures of search,
not of reasoning — the corpus held the answer.** D-10 exists because of them. **Read §0.5 before
working, not after.**
